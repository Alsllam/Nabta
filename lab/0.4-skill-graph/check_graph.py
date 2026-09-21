"""check_graph.py — expand and validate the skill graph in docs/curriculum/skills.v<version>.json.

The graph is authored as *templates + instances*: entries under "per_letter" are skill kinds that
exist once per letter (R-L-SHAPE x 28 letters = 28 nodes); entries under "skills" are single
nodes. This script expands the templates, resolves the three prerequisite forms, and checks
that the result is a well-formed DAG. It also prints the "frontier" — the skills a child could
be taught next — for two example learner states, which is the whole point of a prerequisite
graph: the order is computed, never typed.

Usage:  python check_graph.py [path-to-skills.json]
Exit code 0 = well-formed (so it can run as a test). Written in Python because it is on this
machine; it is ~150 lines and moves to whatever ADR-001 chooses in minutes — not a decision.
"""
import json
import re
import sys
from collections import defaultdict, deque
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to cp1252; Arabic names would crash print()

CODE_RE = re.compile(r"^[RWA]-[A-Z0-9]+(-[A-Z0-9]+)*$")
DEFAULT = Path(__file__).resolve().parents[2] / "docs" / "curriculum" / "skills.v0.1.json"


def expand(data):
    """Turn per-letter kinds into concrete nodes; return (nodes by code, codes by kind)."""
    letters = sorted(data["letters"], key=lambda l: l["order"])
    nodes, kinds = {}, defaultdict(list)
    for kind in data["per_letter"]:
        for L in letters:
            code = f"{kind['kind']}-{L['name']}"
            node = {k: v for k, v in kind.items() if k not in ("kind", "name", "prerequisites")}
            node.update(code=code, kind=kind["kind"], letter=L,
                        name={"ar": kind["name"]["ar"].format(**L), "en": kind["name"]["en"].format(**L)},
                        prereq_spec=kind["prerequisites"])
            nodes[code] = node
            kinds[kind["kind"]].append(code)
    for s in data["skills"]:
        if s["code"] in nodes:
            raise SystemExit(f"duplicate code: {s['code']}")
        node = dict(s)
        node.update(kind=s["code"], letter=None, prereq_spec=s.get("prerequisites", []))
        nodes[s["code"]] = node
        kinds[s["code"]].append(s["code"])
    return nodes, kinds


def resolve(nodes, kinds):
    """Translate prerequisite specs into ('all', code) or ('any', [codes], min); collect errors."""
    errors = []
    for code, n in nodes.items():
        n["prereqs"] = []
        for p in n["prereq_spec"]:
            if isinstance(p, str) and p.endswith("@same"):
                if n["letter"] is None:
                    errors.append(f"{code}: '@same' only makes sense on a per-letter kind"); continue
                target = f"{p[:-5]}-{n['letter']['name']}"
                if target not in nodes: errors.append(f"{code}: prerequisite {target} does not exist"); continue
                n["prereqs"].append(("all", target))
            elif isinstance(p, str):
                if p not in nodes: errors.append(f"{code}: prerequisite {p} does not exist"); continue
                n["prereqs"].append(("all", p))
            elif isinstance(p, dict) and "any_of_kind" in p:
                group = kinds.get(p["any_of_kind"], [])
                if not group: errors.append(f"{code}: any_of_kind {p['any_of_kind']} has no nodes"); continue
                if p["min"] > len(group): errors.append(f"{code}: min {p['min']} > {len(group)} nodes of {p['any_of_kind']}"); continue
                n["prereqs"].append(("any", group, p["min"]))
            else:
                errors.append(f"{code}: unknown prerequisite form {p!r}")
    return errors


def edges_of(nodes):
    """Every prerequisite becomes an edge prerequisite -> skill (threshold groups contribute all their members)."""
    out, indeg = defaultdict(list), {c: 0 for c in nodes}
    for code, n in nodes.items():
        for pr in n["prereqs"]:
            sources = [pr[1]] if pr[0] == "all" else pr[1]
            for s in sources:
                out[s].append(code); indeg[code] += 1
    return out, indeg


def check_dag(nodes):
    """Kahn's algorithm: repeatedly remove nodes with no remaining prerequisites. Leftovers = a cycle."""
    out, indeg = edges_of(nodes)
    depth, queue, order = {c: 0 for c in nodes}, deque(c for c, d in indeg.items() if d == 0), []
    while queue:
        c = queue.popleft(); order.append(c)
        for nxt in out[c]:
            depth[nxt] = max(depth[nxt], depth[c] + 1)
            indeg[nxt] -= 1
            if indeg[nxt] == 0: queue.append(nxt)
    cyclic = [c for c, d in indeg.items() if d > 0]
    return cyclic, depth, sum(len(v) for v in out.values())


def frontier(nodes, mastered):
    """Skills not yet mastered whose prerequisites are all satisfied — what the scheduler chooses from."""
    def ok(pr):
        return (pr[1] in mastered) if pr[0] == "all" else (len(set(pr[1]) & mastered) >= pr[2])
    return sorted(c for c, n in nodes.items() if c not in mastered and all(ok(pr) for pr in n["prereqs"]))


def validate_fields(data, nodes):
    errors = []
    domains = {d["code"] for d in data["domains"]}
    stages = {s["code"]: s["domain"] for s in data["stages"]}
    bands = {b["code"] for b in data["bands"]}
    activities = {a["code"] for a in data["activities"]}
    rules = set(data["mastery_rules"])
    glyphs = {l["glyph"] for l in data["letters"]}
    for code, n in nodes.items():
        if not CODE_RE.match(code): errors.append(f"{code}: code is not ASCII upper-case dash-separated")
        if n["domain"] not in domains: errors.append(f"{code}: unknown domain {n['domain']}")
        if n["stage"] not in stages: errors.append(f"{code}: unknown stage {n['stage']}")
        elif stages[n["stage"]] != n["domain"]: errors.append(f"{code}: stage {n['stage']} belongs to domain {stages[n['stage']]}")
        if n["band"] not in bands: errors.append(f"{code}: unknown band {n['band']}")
        if n["mastery"] not in rules: errors.append(f"{code}: unknown mastery rule {n['mastery']}")
        for a in n["activities"]:
            if a not in activities: errors.append(f"{code}: unknown activity {a}")
        scope_letters = (n.get("scope") or {}).get("letters")
        if isinstance(scope_letters, list):
            for g in scope_letters:
                if g != "@same" and g not in glyphs: errors.append(f"{code}: scope letter {g} is not in 'letters'")
    return errors


def main(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    nodes, kinds = expand(data)
    errors = resolve(nodes, kinds) + validate_fields(data, nodes)
    cyclic, depth, n_edges = check_dag(nodes)
    if cyclic: errors.append("cycle among: " + ", ".join(sorted(cyclic)[:10]))

    letters = sorted(data["letters"], key=lambda l: l["order"])
    by_domain = defaultdict(int)
    for n in nodes.values(): by_domain[n["domain"]] += 1
    quick = sum(1 for n in nodes.values() if n.get("quick"))
    roots = [c for c, n in nodes.items() if not n["prereqs"]]

    print(f"skills.v{data['version']} — {len(data['per_letter'])} per-letter kinds × {len(letters)} letters + {len(data['skills'])} single nodes")
    print()
    print("| Check | Result |")
    print("| --- | --- |")
    print(f"| Authored entries | {len(data['per_letter']) + len(data['skills'])} |")
    print(f"| Concrete nodes after expansion | {len(nodes)} (R {by_domain['R']}, W {by_domain['W']}, A {by_domain['A']}) |")
    print(f"| Prerequisite edges | {n_edges} |")
    print(f"| Acyclic | {'yes' if not cyclic else 'NO'} |")
    print(f"| Unknown prerequisites / fields | {len(errors)} |")
    print(f"| Longest prerequisite chain | {max(depth.values())} steps ({max(depth, key=depth.get)}) |")
    print(f"| Roots (no prerequisites) | {len(roots)} |")
    print(f"| Quick nodes (lighter mastery rule) | {quick} |")
    print()

    first3 = [L["name"] for L in letters[:3]]
    state_a = set()
    state_b = {f"R-L-SHAPE-{n}" for n in first3} | {f"R-L-SOUND-{n}" for n in first3}
    fa, fb = frontier(nodes, state_a), frontier(nodes, state_b)
    print(f"Frontier for a new child: {len(fa)} skills — e.g. {', '.join(fa[:4])} …")
    print(f"Frontier after mastering shape+sound of {', '.join(L['glyph'] for L in letters[:3])}: {len(fb)} skills — "
          f"R-H-FATHA-CONCEPT {'unlocked' if 'R-H-FATHA-CONCEPT' in fb else 'still locked'}, "
          f"R-H-FATHA-{first3[0]} {'unlocked' if f'R-H-FATHA-{first3[0]}' in fb else 'locked (needs the concept first)'}")
    print()
    for e in errors: print("ERROR", e)
    print("RESULT:", "well-formed" if not errors else f"{len(errors)} problem(s)")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else DEFAULT))
