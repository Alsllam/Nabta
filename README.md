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
| `docs/` | Plan, deliverables (Vision, Pedagogy, SRS, Study Notes, Architecture…), curriculum seed, learning notes, ADRs | Phase 0 |
| `lab/` | One folder per study experiment: hypothesis, method, results, what it means for Nabta | Phase 1 |
| *(product folders)* | Named and created after the Phase 5 stack decision | Phase 6 |

Start here: [docs/PLAN.md](docs/PLAN.md) → [ROADMAP.md](ROADMAP.md) → `docs/deliverables/out/*.docx`.

## Working on it

- One roadmap step = one commit = one note in `docs/learning/`. Study steps also ship an
  experiment in `lab/`. Rules in [CLAUDE.md](CLAUDE.md).
- Documents: edit `docs/deliverables/<key>.md`, render with `docs/deliverables/_template/build.ps1 <key>`.
- The skill graph is data: `docs/curriculum/skills.v<version>.json`.

## Safety promise (short form)

The child never chats with an unconstrained model. Every story is generated under constraints,
validated and safety-checked before it is cached. Why a skill was chosen can always be explained
to a parent. Children are not user accounts; voice recordings are scored and then deleted.
Full text: `docs/deliverables/privacy.md` (Phase 10).
