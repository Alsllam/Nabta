---
name: make-doc
description: Create or update one of the project's deliverable documents (vision, pedagogy, srs, study-notes, architecture, database, api, ai-safety, privacy, user-guide, test-plan, pilot-report) as Markdown, render it to .docx with the docs pipeline, and commit it as a doc(...) commit. Use when the user invokes /make-doc <key> or asks for one of these documents.
---

# make-doc

Produce a professional, bilingual-aware Word deliverable from a Markdown source.

## Inputs

`/make-doc <key> [section or change request]`. Keys and the phase each grows in are in
`docs/PLAN.md` §10. Source: `docs/deliverables/<key>.md`. Output: `docs/deliverables/out/<Key>.docx`.
Template and build script: `docs/deliverables/_template/` (created in roadmap step 0.2; if it
does not exist yet, tell the user to run that step first). The pipeline is a documents tool,
not a stack choice.

## Procedure

1. **Read what exists**: the current `<key>.md` (if any), `docs/PLAN.md`, `ROADMAP.md`, and
   whatever the document describes — `docs/curriculum/skills.*.json` for `pedagogy`, the lab
   READMEs and ADRs for `study-notes` and `architecture`, code once it exists for `database`
   and `api`. Documents describe the **actual** repo state — never invent tables, endpoints or
   results; mark planned items *Planned*. Before Phase 5's ADRs exist, no document names a
   product; it names capabilities and candidates.
2. **Structure** — every document has:
   - YAML front matter: `title`, `subtitle` (Arabic title), `author`, `version`, `date`, `status`
     (Draft / Review / Approved).
   - A revision history table (append a row per change; patch for wording, minor for new
     sections, major for scope change).
   - Numbered headings; stable IDs (`FR-TUT-003`, `NFR-SAF-001`, `R-L-SOUND-م`, `ADR-004`);
     diagrams as fenced Mermaid blocks **plus** a rendered PNG/SVG in
     `docs/deliverables/assets/` (Pandoc does not render Mermaid — use the template's diagram
     script; if it cannot run, say so and keep an ASCII fallback).
   - A bilingual glossary (Arabic ↔ English) in `srs`, `pedagogy`, `privacy`, `user-guide`.

   Per-key outlines:
   - `vision`: problem, users, product principles (PLAN §9), scope & non-goals, the reference
     child's story and the goals derived from it, success metrics for study / pilot / product,
     operating model (solo), risks, roadmap summary.
   - `pedagogy`: three domains; skill graph (codes, names ar/en, stage, group, prerequisites,
     mastery criterion, content scope) as prose *and* as `docs/curriculum/skills.v<version>.json`
     — the two change together; session shape; scheduler rules; adaptation levers; assessment
     rules; activity catalogue (tier 1 templates with parameters, tier 2 generated kinds and
     their briefs); the child-facing progress view; the learner-model algorithm once Phase 4
     chooses it.
   - `srs` (IEEE 830): introduction, overall description, actors, use cases UC-01…UC-10 with
     pre/post conditions, functional requirements per capability (`FR-CUR`, `FR-LRN`, `FR-TUT`,
     `FR-CNT`, `FR-SPC`, `FR-RPT`, `FR-AI`), non-functional (child safety, privacy, offline,
     latency and cost budgets, i18n/RTL, accessibility, device floor), external interfaces,
     traceability matrix.
   - `study-notes`: one section per module A–E; per step: the question, the experiment, the
     results table, what changed in the design, the ADR if any. Grows with every study step.
   - `architecture`: capability view (PLAN §6) with module rules and event map, key flows
     (daily session, story generation, read-aloud scoring); after Phase 5, the software
     architecture with products named and the decisions log from `docs/decisions/`.
   - `database`: after the Phase 5 ADR — ERD, dictionary, indexes, migrations log, retention
     and encryption notes for recordings and packs.
   - `api`: auth, conventions, endpoints per capability, idempotent submit, error model, examples.
   - `ai-safety`: the pipeline constraints → validators → safety layer → cache → review;
     prompts (versioned); providers and routing; data that may leave the device; usage caps;
     eval suites and results; failure modes and fallbacks.
   - `privacy`: privacy policy and terms for parents, ar and en sections, children's-data
     provisions (consent scopes, retention, export/delete).
   - `user-guide`: parent guide, task-based, screenshots when the app exists.
   - `test-plan`: strategy, levels, eval suites in CI, environments, deployment, rollback, runbook.
   - `pilot-report`: design (families, duration, pre/post test), telemetry, results, iterations,
     the stop criterion and whether it was hit.
3. **Write/update the Markdown.** Clear, specific, testable wording. Arabic text in RTL-marked
   paragraphs (the template's custom style: `::: {custom-style="RTL"}`). Child-facing text
   samples are fully diacritised.
4. **Render** with the build script (`docs/deliverables/_template/build.ps1 <key>`). Open
   nothing; verify the file exists and is non-trivial in size. Report any warnings.
5. **Present, then commit on the developer's go**: show the diff summary and stop; when they
   agree (or said "commit directly"), commit `doc(<key>): <what changed>` — stage the `.md`,
   assets, the `.docx`, and for `pedagogy` the matching `skills.*.json`.
6. **Hand back**: path of the `.md` and `.docx`, version number, and what is still marked
   *Planned* so the next phase knows what to fill in.

## Quality bar

- No lorem-ipsum, no placeholder sections without a *Planned* marker.
- Requirements use "shall"; each has an ID, a priority (M/S/C), and a source (use case,
  goal, or roadmap step).
- Results quoted in `study-notes` match the lab README they come from, sample size included.
- Diagrams match the module rule (no shared storage between modules).
