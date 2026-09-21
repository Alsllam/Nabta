---
name: next-step
description: Execute the next unchecked step in ROADMAP.md — a study step (concept note + lab experiment + "what this means for Nabta" + ADR when a choice emerges) or a build step — in teaching mode, write its learning doc, update the deliverable docs it touches, and commit it as one step commit. Use when the user says "next step", "continue", "لنبدأ", "الخطوة التالية", or invokes /next-step.
---

# next-step

Execute exactly **one** roadmap step end-to-end. Never two, unless the user explicitly asks.

## Procedure

1. **Locate the step.** Read `ROADMAP.md`; the target is the first unchecked `[ ]` step of the
   phase marked `active`.
   - Phase-expansion step (`N.0`): break the phase into commit-sized steps in ROADMAP.md, using
     `docs/PLAN.md` §4 (study modules A–E) or §5 (build phases) as the source. Every step gets a
     *Topics* line. Study steps also get an *Experiment* line (what is measured, the candidates,
     the sample) and a *Docs* line (`study-notes` at least). Build steps get a *Docs* line where
     relevant. Build phases 6–9 are expanded only after Phase 5's ADRs exist.
   - Checkpoint (`N.CP`): stop and tell the user to run `/checkpoint`.
2. **Announce the lesson first.** In 3–6 lines: what will be studied or built, which topics it
   teaches (the step's *Topics* line), and what the developer already knows that it maps to — a
   strong general-programming background and **no** AI background, so every AI term is defined
   the first time it appears. Never map a concept to a framework from an earlier project.
3. **Study steps (Phases 1–5) ship four things.**
   - The **concept note**: the first half of the learning doc, from first principles, in the
     developer's own words.
   - A **runnable experiment** in `lab/<step-id>-<slug>/`, started from `lab/TEMPLATE/`:
     hypothesis · method (candidates, sample size, metrics, rating rubric) · how to run ·
     results table · limits · what this means for Nabta. Run it and paste the real numbers.
     An experiment that was not run is not a result — write *not run* and why.
   - The **"what this means for Nabta"** paragraph.
   - An **ADR** in `docs/decisions/` when a choice emerges, from `docs/decisions/TEMPLATE.md`,
     citing the experiment. No ADR → no technology enters the repo.

   Lab rules (CLAUDE.md): measure, don't assume · keys via environment variables read only
   inside `lab/` · no child data · record cost and latency per session and per child-day ·
   a candidate that is free to the developer (e.g. an employer's cloud access) is measured
   beside at least one alternative, and its cost is recorded at list price.
4. **Build steps (Phases 6–11) implement in teaching mode**, in the stack the ADRs chose.
   - Small, readable diffs; the *why* commented at the exact line where a new idea appears.
   - Every guardrail in CLAUDE.md: child-safe by construction, AI behind interfaces, module
     boundaries, children are not accounts, offline, RTL, no secrets.
   - Tests where they pay: learner-model math, scheduler determinism, content validators,
     alignment scoring, DAG checks, one happy path per service.
   - Verify with the narrowest relevant command and show the result. Never claim green
     without running it.
5. **Update deliverable docs** named on the step's *Docs* line, following the `/make-doc`
   procedure. `study-notes` grows with every study step; `pedagogy` and
   `docs/curriculum/skills.*.json` change together; no document names a product before its
   ADR exists.
6. **Write the learning doc** at `docs/learning/<step-id>-<slug>.md` following
   `docs/learning/TEMPLATE.md`. "The mental shift" must be specific to this step; "Gotchas hit"
   must be real ones from this session; for study steps, "What this means for Nabta" is
   mandatory and the experiment's headline number appears in it.
7. **Tick the checkbox** in ROADMAP.md.
8. **Commit** everything from this step as one commit:

   ```
   step(<id>): <imperative subject>

   Learned: <comma-separated topic list>
   ```

   Stage only files belonging to this step — never `.env`, recordings, or large or personal
   lab outputs. Do not push (local-only repo until Phase 11).
9. **Hand back.** Name the step, the commit hash, the learning doc path, the experiment's
   headline number if any, and what the *next* step will be — then stop. Do not start it.

## Quality bar

- The learning doc's table references real files and lines from this commit.
- A study step with an empty results table is not done.
- If the step turns out bigger than one sitting, split it: tick nothing, propose sub-steps
  (`<id>a`, `<id>b`) in ROADMAP.md, commit the roadmap change, and do the first sub-step.
- Nothing is proposed, scaffolded or referenced because an earlier project used it.
