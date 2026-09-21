# Nabta (نبتة)

An adaptive, Arabic-first AI tutor that teaches children aged 4–8 to read, write and count — a
patient private tutor that plans every session from what the child actually knows. Inspired by
the Primer in *The Diamond Age*. Built and operated by one person.

**The technology is chosen by study, not by habit.** Phases 1–5 are an AI study curriculum —
language models, speech, vision and handwriting, adaptive-learning science, safety and deployment
economics — with a measured experiment and a decision record for every component. The product is
built in Phases 6–9 on those decisions.

| Folder | What | Status |
| --- | --- | --- |
| `docs/` | Plan, deliverables (Vision, Pedagogy, SRS, Architecture written; Study Notes from Phase 1), curriculum seed `docs/curriculum/skills.v0.1.json`, learning notes, ADRs | Phase 0 done |
| `lab/` | One folder per experiment: hypothesis, method, results, what it means for Nabta. First: the skill-graph checker (0.4a) | Phase 1 next |
| `core/` · `child-app/` · `web/` | Placeholders with READMEs; names provisional, technology decided by the Phase 5 ADRs | Phases 6–9 |

Start here: [docs/PLAN.md](docs/PLAN.md) → [ROADMAP.md](ROADMAP.md) → `docs/deliverables/out/*.docx`.

## Working on it

- One roadmap step = one commit = one note in `docs/learning/`. Study steps also ship an
  experiment in `lab/`. Rules in [CLAUDE.md](CLAUDE.md).
- Documents: edit `docs/deliverables/<key>.md`, render with `docs/deliverables/_template/build.ps1 <key>`.
- The skill graph is data: `docs/curriculum/skills.v<version>.json`; `python lab/0.4-skill-graph/check_graph.py` validates it.
- Lab keys: copy `.env.example` to `.env` (ignored); read only inside `lab/`. Audio, lab outputs and secrets never enter git (`.gitignore`).

## Safety promise (short form)

The child never chats with an unconstrained model. Every story is generated under constraints,
validated and safety-checked before it is cached. Why a skill was chosen can always be explained
to a parent. Children are not user accounts; voice recordings are scored and then deleted.
Full text: `docs/deliverables/privacy.md` (Phase 10).
