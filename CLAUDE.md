# Nabta (نبتة) — Adaptive Arabic Tutor for Young Children

Nabta is an adaptive AI tutor that teaches children aged 4–8 to read, write and count in Arabic,
at the quality of a devoted private tutor. A parent sets up the child; the child meets Nabta daily
in a short session; every answer updates a per-skill mastery model that plans the next session.
Inspired by *The Diamond Age*'s Primer.

**Technology is undecided on purpose.** The developer (Abdulsalam) is studying AI from first
principles through this project. Phases 1–5 are a study curriculum (language models, speech,
vision and handwriting, adaptive-learning science, safety and deployment economics); every
component enters the stack through a measured experiment and an ADR. Nothing is chosen because it
was used in an earlier project.

Master plan: [docs/PLAN.md](docs/PLAN.md). Progress: [ROADMAP.md](ROADMAP.md).
Deliverables live in `docs/deliverables/` as Markdown and render to `.docx` with `/make-doc`.
Curriculum data (the skill graph seed) lives in `docs/curriculum/`. Experiments live in `lab/`.
Decisions live in `docs/decisions/` as ADRs.

## What is borrowed from Wathiq, and what is not

| Borrowed (way of working) | Not borrowed (technology) |
| --- | --- |
| One step = one commit = one learning note | Backend framework, web framework, mobile toolkit |
| Phases expanded just-in-time; checkpoints gate phases | Model runtime, model choice, speech engines |
| Deliverable documents as Markdown → `.docx` | Database, job scheduler, hosting |
| The four skills: `/next-step`, `/checkpoint`, `/make-doc`, `/learn` | Any library "because it worked before" |

`D:\Training\Wathiq` may be read for the workflow, docs pipeline and skill files only. **Do not
propose, scaffold or reference a technology because Wathiq or any other earlier project used it.**
If a technology is worth considering, it appears as a *candidate* in a study step, is measured
against the alternatives, and is recorded in an ADR — or it does not enter the repo.

## The workflow — non-negotiable rules

1. **One roadmap step = one commit.** Never bundle two steps; never commit a half-done step.
   **The commit waits for the developer's review of the diff** — present the changes and stop;
   commit only on their go, unless they said "commit directly". Every diff is a lesson to read.
2. **Every step ships a learning doc** at `docs/learning/<step-id>-<slug>.md` following
   `docs/learning/TEMPLATE.md`, written *with* the work, in the developer's own words.
3. **Study steps (Phases 1–5) ship four things:** the concept note, a runnable experiment in
   `lab/<step-id>-<slug>/` (README with hypothesis · method · results table · "what this means
   for Nabta"), the Nabta paragraph, and an ADR when a choice emerges. An experiment that was not
   run is not a result — say so.
4. **Commit message convention:** first line `step(<id>): <what>`; body starts with `Learned:`.
   Checkpoints: `checkpoint(<phase>): passed`. Documents: `doc(<name>): <what>`.
   Decisions: `adr(<nnn>): <title>`.
5. **Teach while building.** Concepts first, from first principles, then the experiment. Assume
   a strong general-programming background and **no** AI background; define every term the first
   time it appears. Later, when building, explain the *why* at the line where a new idea appears.
6. **ROADMAP.md is the source of truth.** Tick the box in the same commit. Phases are expanded
   into commit-sized steps just-in-time (step `N.0`). Build phases 6–9 are expanded only after
   Phase 5's ADRs exist.
7. **Checkpoints gate phases** via `/checkpoint`: the user answers from memory before seeing the answer.
8. **Documents are part of the product.** Each phase updates its deliverables; the `pedagogy`
   doc and `skills.*.json` change together; `study-notes` grows with every study step.

## Experiment rules (lab/)

- **Measure, don't assume.** Every comparison has a table: candidates × metrics, with sample size.
  Arabic quality is rated blind by a native speaker (the developer) with a written rubric.
- **Small is fine, hidden is not.** Twenty sentences or two hundred stories are enough if the
  sample and its limits are stated in the README.
- **Record cost and latency** for every candidate that has them, in the units the cost model (E3)
  uses: per session, per child-day.
- **Keys and endpoints via environment variables** read only inside `lab/`; never in the repo.
- **No child data in the lab.** Synthetic text, the developer's own voice, or consented adult
  recordings only.
- **The lab runtime** (language, environment) is itself decided in step 1.1 by ADR-001, on one
  criterion: how fast we can learn with it.

## Product guardrails (hold whatever the stack becomes)

- **Child-safe by construction.** No open-ended chat with the child. Every child-facing generated
  text goes constraints → validators → safety layer → cache; any rejection falls back to a
  template activity. Nothing reaches the child from generated content unless its status is
  `Validated` or `Approved`.
- **Explainable pedagogy.** A parent can be told why a skill was chosen. H1 (engineered tutor) is
  the working hypothesis; Phase 4 step D7 tests it against H2 (model-as-tutor) before anything
  is built on either.
- **AI behind interfaces.** Every model, synthesis and recognition call goes through a port owned
  by the platform; providers are configuration; every call is logged and capped per child per day.
- **Validate AI output.** Stories are decomposed against the allowed letter set and word list;
  numbers in word problems are re-parsed; failures are logged with the prompt version.
- **Children are not accounts.** Store nickname, age band, language, numerals, interests, story
  cast — no surname, photo or location. External services, if any, receive nickname + interests
  at most; never recordings, never parent free-text.
- **Recordings are ephemeral.** Scored, then purged on a time-to-live; stored encrypted; a low
  confidence score never lowers mastery.
- **Explicit module boundaries.** Curriculum, Learners, Tutor, Content, Speech, Reports, AI gateway:
  contracts and events between them, never shared storage.
- **Offline is a feature.** A full session runs from a pre-synced activity pack; result submission
  is idempotent on client-generated ids.
- **Arabic-first, right-to-left everywhere**; ar + en text from the first screen.
- **No secrets in git.**
- **Tests where they pay:** learner-model math, scheduler determinism, content validators,
  alignment scoring, DAG checks, and one happy path per service.

## Skills in this repo (copied from Wathiq in step 0.1 and adapted)

- `/next-step` — implement the next unchecked ROADMAP step (study or build), write its learning
  doc and, for study steps, its lab experiment; commit.
- `/checkpoint` — run the active phase's quiz; on pass, close the phase and commit.
- `/make-doc <key>` — build/update a deliverable (`vision`, `pedagogy`, `srs`, `study-notes`,
  `architecture`, `database`, `api`, `ai-safety`, `privacy`, `user-guide`, `test-plan`,
  `pilot-report`).
- `/learn <topic>` — a focused, first-principles explanation of a topic from the plan, anchored to
  this repo's notes and experiments.

## Environment notes

- Windows 11, PowerShell primary. Tools installed on this machine are **not decisions**; the lab
  runtime is chosen in step 1.1, and product technologies in Phase 5.
- Git: local only, branch `main`, commit directly. No remote until Phase 11.
