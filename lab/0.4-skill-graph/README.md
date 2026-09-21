# 0.4a — Skill graph: expand, validate, compute the frontier

> **Step:** 0.4a · **Module:** pre-study (Phase 0; feeds D1) · **Date:** 2026-09-21 · **Status:** run

## Question for Nabta

Is the v0.1 skill graph well-formed — every prerequisite exists, no cycles, codes stable and
ASCII — and does a prerequisite graph actually *compute* what to teach next, or does it only
constrain it?

## Hypothesis

Authoring the graph as templates (per-letter kinds) plus single nodes keeps the source under
100 entries while expanding to 300+ nodes with no cycle. The threshold prerequisite form
(`any_of_kind … min`) behaves as designed: the fatha concept unlocks after **three** letter
sounds, and no per-letter fatha node unlocks before the concept. The number that would change
my mind: a cycle, a dangling prerequisite, or the concept unlocking with fewer than 3 sounds.

## Method

- **Candidates:** none — this is a validation, not a comparison. (The template's comparison
  sections are kept so the next experiment starts from the same shape.)
- **Sample:** `docs/curriculum/skills.v0.1.json` — 9 per-letter kinds × 28 letters + 76 single
  nodes. No child data; the two "learner states" are synthetic sets of mastered codes.
- **Metrics:** node and edge counts; acyclicity (Kahn's algorithm); unknown prerequisites /
  fields; longest prerequisite chain; number of roots; frontier size for a new child and for a
  child who has mastered shape + sound of the first three letters.
- **Cost & latency:** not applicable (runs locally in well under a second).

## How to run

```
python lab/0.4-skill-graph/check_graph.py            # default: docs/curriculum/skills.v0.1.json
python lab/0.4-skill-graph/check_graph.py path.json   # any version
```

Exit code 0 means well-formed, so the same command is the test.

## Results

| Check | Result |
| --- | --- |
| Authored entries | 85 |
| Concrete nodes after expansion | 328 (R 210, W 92, A 26) |
| Prerequisite edges | 892 |
| Acyclic | yes |
| Unknown prerequisites / fields | 0 |
| Longest prerequisite chain | 13 steps (`R-C-INFER`) |
| Roots (no prerequisites) | 30 |
| Quick nodes (lighter mastery rule) | 170 |
| Frontier, new child | 30 skills — all 28 `R-L-SHAPE-*`, `W-PRE-LINE`, `A-CNT-1TO1-5` |
| Frontier after shape + sound of ا م س | 28 skills — `R-H-FATHA-CONCEPT` **unlocked**; `R-H-FATHA-ALEF` **locked** until the concept is mastered |

Raw output: run the command above; it prints this table.

## Limits

- The checker validates **form**, not pedagogy. Whether ب should precede ت, whether three
  sounds are the right threshold for the fatha concept, or whether 4-of-5 is a sensible mastery
  rule are questions for 0.4b, D1–D2 and the Stage 0 family test.
- 892 edges are mostly threshold expansions (each `any_of_kind … min` becomes up to 28 edges).
  The count says little about difficulty; the longest chain (13) says more.
- The two learner states are hand-picked, not sampled.

## What this means for Nabta

The graph decides **eligibility**, never **order**: a brand-new child is eligible for 30 skills
at once, including every letter's shape. Sequencing — the default letter order in `letters`,
pulling the child's name letters forward, keeping confusable pairs apart, one new skill per
session — is the scheduler's job (D6), and the `frontier()` function in `check_graph.py` is
the seed of that scheduler. The threshold prerequisite makes the harakat model honest: the
concept is taught once on whatever letters the child knows, and the 170 quick per-letter nodes
that follow are what a session can batch several of. For G8, the reason a parent reads
("تعلّمت صوت ثلاثة حروف، فاليوم نبدأ الفتحة") is exactly the prerequisite that unlocked the
skill — the graph carries the explanation for free.

## Decision

None. No technology was chosen: the graph is JSON, and the checker is a 150-line script that
moves to whatever ADR-001 picks. The **data model** decisions (ASCII codes, templates ×
letters, three prerequisite forms, named mastery rules, stage as a label) are recorded in
`docs/curriculum/README.md` and in the learning note for 0.4a.
