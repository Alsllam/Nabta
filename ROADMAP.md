# Roadmap

Source of truth for progress. One step = one commit = one learning doc.
Legend: `[ ]` todo · `[x]` done · each step lists the **topics it teaches**.
Phases beyond the active one stay coarse; the first step of each phase (`N.0`) expands it.
Study steps (Phases 1–5) also ship an experiment under `lab/` and, when a choice emerges, an ADR.

---

## Phase 0 — Bootstrap & docs foundation  `active`

Plan, roadmap and CLAUDE.md were drafted on 2026-09-10. This phase turns the draft into a working
repo and writes the foundation documents **without naming any technology**: the product, the
curriculum, the requirements and the capabilities. Technology arrives in Phases 1–5.

- [x] **0.1 Repo bootstrap** — `git init`; copy the four workflow skills (`next-step`,
      `checkpoint`, `make-doc`, `learn`) and `docs/learning/TEMPLATE.md` from Wathiq and adapt them
      (document keys, study-step handling, no reference-stack assumptions); add a
      `lab/TEMPLATE/` (README with hypothesis · method · results table · "what this means for
      Nabta"); `docs/decisions/README.md`; first commit. *Topics: reusing a way of working
      without reusing its technology; experiment template.*
- [x] **0.2 Docs pipeline** — copy `docs/deliverables/_template/` (reference `.docx`, build and
      diagram scripts) and `deliverables/README.md` from Wathiq; render a smoke doc with Arabic
      RTL text. *Topics: the Markdown → Word pipeline (a documents tool, not a stack choice).*
- [ ] **0.3 Vision & Charter doc** — `docs/deliverables/vision.md` → `.docx`: problem, users,
      product principles (PLAN §9), scope & non-goals, success metrics for study / pilot / product,
      operating model, risks, roadmap summary. *Topics: charter for a child-facing product;
      non-goals as safety scope.*
- [ ] **0.4 Pedagogy v0.1** — `docs/deliverables/pedagogy.md` → `.docx`: three domains, ~120
      skills with stable codes (`R-…`, `W-…`, `A-…`), prerequisites, content scope, mastery
      criteria; session shape; scheduler rules; adaptation levers; assessment rules; the tier-1
      activity catalogue with parameters. Plus `docs/curriculum/skills.v0.1.json` and a small
      script that checks the JSON is a DAG (the first `lab/` artefact). *Topics: curriculum
      design, modelling a DAG as data, mastery criteria you can test.*
- [ ] **0.5 SRS v0.1** — actors, UC-01…UC-10 with pre/post conditions, FR per capability
      (`FR-CUR`, `FR-LRN`, `FR-TUT`, `FR-CNT`, `FR-SPC`, `FR-RPT`, `FR-AI`), NFR (child safety,
      privacy, offline, latency budgets, i18n/RTL, accessibility, cost per session), glossary ar/en.
      *Topics: testable requirement wording; latency and cost as requirements the study must meet.*
- [ ] **0.6 Capability architecture v0.1** — `architecture.md` with PLAN §6 as the container
      view (capabilities, no products), the module rules, the event map, and three key flows
      (daily session, story generation, read-aloud scoring). Marked *products decided in Phase 5*.
      *Topics: designing to capabilities and contracts before choosing tools.*
- [ ] **0.7 Repo layout & tooling** — `lab/`, `docs/curriculum/`, and placeholder READMEs for
      the future `core/`, `child-app/`, `web/` folders (names are provisional until Phase 5);
      `.editorconfig`, `.gitattributes`, `.gitignore` (secrets, audio, recordings, lab outputs),
      `.env.example` for API keys used only inside `lab/`. *Topics: a repo that can hold a study
      and, later, a product.*
- [ ] **0.CP Checkpoint** — "Name the capabilities in PLAN §6 and explain why a child is not a
      user account."

## Phase 1 — Study: AI foundations (Module A)  *(expand at start)*

A1 tokens and cost of Arabic · A2 model landscape (local small / server open-weights / hosted) ·
A3 prompting, structured output, the validator-driven repair loop, prompt caching and reasoning
models with the constrained-story experiment · A4 embeddings, retrieval and RAG — themed
vocabulary and the parent assistant (UC-11) · A5 adapting models (prompting vs fine-tuning vs
LoRA) · A6 evaluation and the first eval suite, model-as-judge · A7 agents vs state machines: the
curriculum authoring agent with function calling, hand loop vs agents SDK. Step 1.1 also sets up
the lab runtime (ADR-001: the language and environment experiments are written in — chosen for how
fast we learn, nothing else). *Topics: how language models work, prompting, structured output,
conversation state, caching, embeddings, RAG, fine-tuning, evals, tool use.*

- [ ] 1.0 Expand phase into steps
- [ ] 1.CP Checkpoint A — "Why does Arabic cost more tokens than English, and what did that change in the design?"

## Phase 2 — Study: Speech (Module B)  *(expand at start)*

B1 speech synthesis and Arabic diacritisation, engine comparison with blind rating · B2 speech
recognition and child speech, word-error-rate comparison · B3 reading assessment: forced
alignment, per-word scoring, the confidence floor · B4 latency, streaming, caching, and live
read-aloud feedback through a real-time speech API versus batch.
*Topics: TTS and ASR internals, alignment, confidence, latency budgets, real-time speech.*

- [ ] 2.0 Expand phase into steps
- [ ] 2.CP Checkpoint B — "Why must text sent to speech synthesis be fully diacritised, and where in the pipeline does that happen?"

## Phase 3 — Study: Vision & handwriting (Module C)  *(expand at start)*

C1 stroke vs image recognition, DTW template scoring prototype · C2 vision-language models as
judges, agreement with geometry · C3 image generation for story illustrations — style
consistency, safety, cost (deferred from v1; decided here). *Topics: online handwriting
recognition, template matching, vision models, image generation.*

- [ ] 3.0 Expand phase into steps
- [ ] 3.CP Checkpoint C — "Stroke data or an image — which does a tracing activity need, and why?"

## Phase 4 — Study: Adaptive learning (Module D)  *(expand at start)*

D1 knowledge components and the skill graph · D2 Bayesian Knowledge Tracing · D3 IRT / Elo ·
D4 Deep Knowledge Tracing (read, size against the pilot) · D5 spaced repetition · D6 deterministic
session planning · D7 the H1 vs H2 simulation with 1,000 synthetic learners.
*Topics: learner modelling, spaced repetition, simulation as a design tool.*

- [ ] 4.0 Expand phase into steps
- [ ] 4.CP Checkpoint D — "A child answers three right then one wrong — what happens to P(mastery), and why does slip matter?"

## Phase 5 — Study: Safety, deployment, cost → stack decision (Module E)  *(expand at start)*

E1 guardrail layers (allow-list validators, hosted moderation, review sampling) and the red-team
set · E2 data-flow map and minimisation · E3 where inference runs and the cost model, batch vs
on-demand pack generation · E4 observability, usage ledger from the provider's usage API, caps,
and the fault drill that must end in a template fallback · E5 one ADR per component in PLAN §8.1,
then Architecture & DB v0.1 written from the ADRs.
*Topics: guardrails, moderation, children's data, inference economics, batch processing,
observability, error handling, decision records.*

- [ ] 5.0 Expand phase into steps
- [ ] 5.CP Checkpoint E — "If the hosted model's price doubled tomorrow, which component would you move first, and what would the child notice?"

## Phase 6 — Build: tutor core  *(expand after Phase 5)*

Curriculum store + seeder with DAG validation, learner model, scheduler, session engine with
idempotent submit and offline sync, AI gateway with usage ledger and caps — in the stack chosen
at E5. *Topics: depend on the ADRs.*

- [ ] 6.0 Expand phase into steps

## Phase 7 — Build: child experience v1  *(expand after Phase 5)*

Child picker with PIN, session flow, `letter-tap`, `letter-trace` (stroke capture), `count-tap`,
cached audio, offline activity pack, rewards. One new platform concept per step.

- [ ] 7.0 Expand phase into steps

## Phase 8 — Build: content & speech  *(expand after Phase 5)*

Constrained story and word-problem generation with validators and the safety layer, review
queue, synthesis cache, read-aloud scoring with the confidence floor, handwriting scoring,
recording lifecycle, eval suites in CI.

- [ ] 8.0 Expand phase into steps

## Phase 9 — Build: parent & admin  *(expand after Phase 5)*

Onboarding + consent, child profiles and story cast, dashboard with mastery map, weekly report,
the parent assistant (UC-11: grounded answers with sources), settings; curriculum and template
editors, content review queue, evals dashboard, usage; observability and backups.

- [ ] 9.0 Expand phase into steps

## Phase 10 — Hardening & child safety  *(expand at start)*

Consent audit trail, data-minimisation review, export/delete a child, rate limits, encryption at
rest for recordings and packs, red-team evals as regression tests, security review, `privacy` doc.

- [ ] 10.0 Expand phase into steps

## Phase 11 — Pilot & publish  *(expand at start)*

10-family pilot with a pre/post letter-sound and decoding test, telemetry, two iteration rounds,
`pilot-report`; landing page, Privacy/Terms, listing, deployment, open-source core.

- [ ] 11.0 Expand phase into steps

## Phase 12 — Toward the Primer  *(not scheduled)*

Long-term memory of the child across years, guided comprehension dialogues, English track,
dialect-aware speech, teacher classroom mode, sibling play. Opened only after Phase 11.
