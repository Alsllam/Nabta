---
title: "Nabta — Software Requirements Specification"
subtitle: "نبتة — مواصفة متطلّبات البرمجيات"
author: "Abdulsalam"
version: "0.1"
date: "2026-09-21"
status: "Draft"
---

## Revision history {.unnumbered}

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 0.1 | 2026-09-21 | Abdulsalam | First version: actors, UC-01…UC-11, functional requirements per capability, non-functional requirements with planning values, external interfaces as ports, traceability to goals G1–G15 and scheduler rules R1–R14, glossary |

# Introduction

## Purpose

This document states what Nabta shall do, precisely enough that each statement can be shown to
hold or fail. It is written before any technology is chosen: it names capabilities, ports and
limits, never products. The study phases (1–5) measure candidates against the limits stated
here; the build phases (6–9) implement the requirements in the stack the study's decision
records choose.

## Scope

Nabta v1: an adaptive tutor for children aged 4–8 learning to read, write and count in Arabic,
with a parent surface and an operator surface. Out of scope for v1 — by decision, not omission
(see the charter's non-goals): open-ended conversation with the child, child accounts, retained
recordings, social features, ads or purchases, generated illustrations or video, dialect speech,
an English track, teacher mode.

## Conventions

- Requirements use **shall**. Each has a stable ID, a priority — **M** must, **S** should,
  **C** could — and a **source**: a goal from the charter (`G1`–`G15`), a scheduler rule from the
  pedagogy (`R1`–`R14`), a principle (`P1`–`P8`, `P-1`–`P-7`), a use case (`UC-nn`) or a roadmap step.
- Values marked *(planning)* are targets set before measurement; the experiment named beside
  them replaces them with measured numbers. A planning value is a requirement on the study, not
  a promise of the product.
- *Planned* marks a requirement whose mechanism is decided later; the requirement itself stands.

## References

Charter: `docs/deliverables/vision.md` · Pedagogy: `docs/deliverables/pedagogy.md` · Skill graph:
`docs/curriculum/skills.v0.1.json` · Master plan: `docs/PLAN.md` §6 (capabilities), §7 (data), §9
(principles).

::: {custom-style="RTL"}
**الملخص.** تحدّد هذه الوثيقة ما يجب أن يفعله نظام نبتة بصياغة يمكن اختبارها: كل متطلّب له معرّف
ثابت وأولوية ومصدر (هدف من قصة ماسة، أو قاعدة من قواعد المجدول، أو مبدأ). كُتبت قبل اختيار أيّ تقنية:
تسمّي القدرات والمنافذ والحدود، لا المنتجات. القيم المعلَّمة *(planning)* أهداف تُقاس عليها المرشّحون في
مراحل الدراسة ثم تُستبدل بأرقام مقاسة.
:::

# Overall description

## Product perspective

Four deliverables, one system:

| Deliverable | Provisional folder | Holds | Built in |
| --- | --- | --- | --- |
| **Tutor core** (backend) | `core/` | curriculum store, learner model, scheduler, session engine, content service, speech service, AI gateway, platform (parent identity, storage, background jobs, nightly pack build), observability | Phases 6, 8 |
| **Child app** | `child-app/` | garden, session, template activities, cached audio, stroke capture, offline pack, idempotent sync, parent lock with quick settings | Phase 7 |
| **Parent web** | `web/` | onboarding and consents, dashboard, "why this session", weekly report, parent assistant, privacy, export/delete | Phase 9 |
| **Operator web** | `web/` | curriculum and template editors, content review queue, evals dashboard, usage and caps | Phase 9 |

**Surface split — proposed decision D-2026-09-21-8.** The child app holds only what a parent
needs while the device is in the child's hands: the lock, session minutes, the microphone
switch. Everything a parent *reads or asks* — the dashboard, reasons, the weekly report, the
assistant, privacy and export — lives on the parent web, reachable from the parent's own phone
at any time. Rationale: it keeps the child app small and fully offline, and puts the assistant
where its retrieval runs. *Status: proposed; confirmed or reversed in this document's next revision.*

## Product functions (summary)

Daily session from a pre-built pack → evidence → mastery statuses → next plan with reasons →
weekly report and assistant for the parent → operator review, evals and caps.

## User classes

See § Actors. The child cannot read, cannot consent and cannot complain; the parent is the
account; the operator is one person.

## Operating environment (technology-neutral)

- Child devices: Android and iOS phones and tablets at the device floor in NFR-DEV; a full
  session without a network connection.
- Parent and operator: a modern browser; network required.
- Backend: one deployable unit (P-1) with background jobs; AI providers behind ports.

## Design constraints

The charter's principles P1–P8 and decisions P-1…P-7; the pedagogy's scheduler rules R1–R14; the
goals G1–G15. Technology constraints arrive only through ADRs.

## Assumptions and dependencies

- A speech engine can hear a child read Arabic at a usable word error rate (tested in B2; if
  not, read-aloud evidence is dropped and FR-SPC-004…007 become *Could*).
- Constrained story generation is feasible above a small letter set (A3); below it, template
  stories serve (FR-CNT-007).
- A device at the floor can play cached audio, capture strokes and render vector animation
  within NFR-PERF (measured in the platform spike before E5).

# Actors

| Actor | Description | Surfaces |
| --- | --- | --- |
| **Child** | Learner 4–8; touch and voice only; never reads an instruction | Child app |
| **Parent** | Account owner; consents, configures, reads, asks | Parent web; lock and quick settings in the child app |
| **Operator** | The developer as curriculum author, reviewer and administrator | Operator web |
| **Scheduler** *(system)* | Builds the session plan and the pack | Tutor core |
| **AI providers** *(external)* | Language model, synthesis, recognition, moderation, retrieval — behind ports | Tutor core |

# Use cases

Each use case names its surface, preconditions, the main flow, postconditions and the
alternatives that matter. Requirements cite use cases as sources.

## UC-01 Parent onboarding

**Actor** Parent · **Surface** Parent web · **Phase** 9
**Pre** No account, or an account with no child.
**Flow** Create account → read the short privacy summary → give consent per scope (voice
processing; external content generation), each separately → create the child: nickname, age band,
language, numerals, avatar, interests (choose from a list), story cast (first names and
relation), session minutes, daily cap → set the child-app PIN.
**Post** A child profile exists with two consent records; a first pack is queued.
**Alternatives** Consent for voice refused → the child app hides the microphone; sessions run
touch-only. Consent for external generation refused → stories are template stories only.
Median completion ≤ 5 minutes (G7).

## UC-02 Daily session

**Actor** Child · **Surface** Child app · **Phase** 6, 7
**Pre** A pack for today (or the last available pack) is on the device; the child is selected
by PIN.
**Flow** Garden and greeting (seed if a skill was mastered last time) → warm-up reviews →
new skill, skin chosen by picture → story (listen; read aloud if allowed) → goodbye on a success.
**Post** Attempts are stored locally with client-generated ids; the garden reflects new
statuses; results sync when a network is available.
**Alternatives** No network throughout → identical experience; sync later (G12). No pack for
today → last pack, template-only session, flagged for the parent. Parent limit reached → the
plan ends on the last mastered activity (R7).

## UC-03 Reading track

**Actor** Child · **Surface** Child app · **Phase** 6–8
Letter shapes → sounds → confusable pairs → harakat syllables → long vowels, sukoon, shadda,
tanween → positional forms and joining → words (taa marbuta, hamza, the article) → sight words →
sentences → passages with comprehension, as the `R-*` stages of the skill graph.
**Pre/Post** Per skill: prerequisites mastered / status updated by counted evidence.

## UC-04 Writing track

**Actor** Child · **Surface** Child app · **Phase** 6–8
Pre-writing strokes → trace with stroke order → write from sound → harakat on letters → joined
letters → copy a word → dictation of a word, then a sentence, as the `W-*` stages.
**Constraint** Tracing needs the canvas size in NFR-DEV-002.

## UC-05 Arithmetic track

**Actor** Child · **Surface** Child app · **Phase** 6–8
One-to-one counting → numerals 0–10 in the child's numeral system → compare and order → bonds →
add and subtract within 10 → to 20, tens and ones → to 100, skip counting → personalised word
problems read aloud, as the `A-*` stages.

## UC-06 Read-aloud assessment

**Actor** Child · **Surface** Child app (capture) + Tutor core (scoring) · **Phase** 8
**Pre** Voice consent granted; the item is a word, sentence or story within the child's letter set.
**Flow** Child reads → audio captured → recognised and aligned to the target per word → each
word gets a match and a confidence → words above the floor become evidence; the rest become
"no evidence" → the recording is purged at its time-to-live.
**Post** Evidence rows without audio; the mastery estimate never decreased by a below-floor
attempt (G10).
**Alternatives** N below-floor attempts in a row → Nabta offers touch (G6). No consent →
this use case is unavailable and never prompted for.

## UC-07 Personalised story

**Actor** Scheduler · **Surface** Tutor core (nightly) → Child app · **Phase** 8
**Pre** The child's statuses and cast; generation consent; a letter set above the template
threshold (else UC-07a).
**Flow** The scheduler writes the brief (kind, target letter, allowed letters and harakat, cast,
interests, value, length) → the model returns a structured story → validators in fixed order →
safety layer → one repair round on failure → cache with status Validated → synthesise audio →
into the pack. Read aloud in session with word highlighting.
**Post** A Validated story and its audio in the pack; a log row with prompt version, cost and
validator report.
**UC-07a Template story** Below the threshold or on any final failure: a hand-written story
with slots for the hero and a cast member, tagged with its letter set.

## UC-08 Parent dashboard and weekly report

**Actor** Parent · **Surface** Parent web · **Phase** 9
**Flow** Dashboard: mastery map per letter with harakat progress, sessions this week, minutes,
the current knot, link to "why this session today". Weekly: three sentences and one screen-free
activity ≤ 5 minutes that names the knot; the parent marks it tried or later.
**Post** Report delivered once a week; no notifications in between.

## UC-09 Operator administration

**Actor** Operator · **Surface** Operator web · **Phase** 9
Edit the skill graph and templates with validation on save; review Flagged content and sample
Validated content; run eval suites and read their results; watch usage, cost and caps; see
validator rejection rates.

## UC-10 Export or delete a child

**Actor** Parent · **Surface** Parent web · **Phase** 10
**Flow** Export: a machine-readable file and a readable summary of everything stored about the
child. Delete: profile, consents, statuses, attempts, packs, cached content and any recording,
irreversibly; confirmation shown.
**Post** Export delivered; or no row references the child and the deletion is logged (without
the data).

## UC-11 Parent assistant

**Actor** Parent · **Surface** Parent web · **Phase** 9
**Pre** Signed-in parent; a child selected.
**Flow** The parent asks in Arabic or English («كيف أساعد ماسة في ن وت؟») → the system
retrieves passages from the pedagogy, the parent guide, the activity library and the child's
statuses → answers with sources shown → logs the query and answer.
**Post** An answer with citations; a `ParentQuery` row; the daily cap decremented.
**Alternatives** Question outside the child's learning (medical, diagnostic, unrelated) → the
assistant says what it can help with and offers the nearest useful thing; it never guesses.
Retrieval finds nothing → it says so and points to the guide. The child app never shows this
use case.

# Functional requirements

## FR-CUR — Curriculum

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| FR-CUR-001 | The system shall store the skill graph as versioned data in the format of `docs/curriculum/skills.v<n>.json`, with codes that are ASCII, unique and never renamed; retired skills shall be marked deprecated. | M | 0.4a |
| FR-CUR-002 | The system shall validate a graph on load — prerequisites exist, no cycles, stages and activities known, scopes valid — and shall refuse to load an invalid graph. | M | 0.4a |
| FR-CUR-003 | The system shall expand per-letter skill kinds into concrete nodes and shall resolve the three prerequisite forms (exact code, `@same`, `any_of_kind` with `min`). | M | 0.4a |
| FR-CUR-004 | The system shall compute a child's frontier — skills not mastered whose prerequisites are satisfied, thresholds counted — from the child's statuses. | M | R4, pedagogy § skill model |
| FR-CUR-005 | The system shall store content items — letters with positional forms, syllables, words with full harakat, sight words, numerals, template stories — each with a level, a derived letter set and media keys. | M | UC-03…07 |
| FR-CUR-006 | The system shall derive a text's letter set and harakat with one decomposition function shared by content authoring and story validation. | M | G2 |
| FR-CUR-007 | The system shall keep a registry of activity templates with parameter schemas and available skins. | S | pedagogy § catalogue |
| FR-CUR-008 | Operator edits to the graph, content and templates shall be validated on save and shall record provenance (source, reviewer, date). | S | UC-09 |
| FR-CUR-009 | Proposals from an authoring agent shall land in a staging area with provenance and shall never modify canonical data without an operator's acceptance. | C | A7 |
| FR-CUR-010 | Scheduler parameters shall be read from the graph file's `policy` block, never hard-coded. | M | 0.4b |

## FR-LRN — Learners

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| FR-LRN-001 | A child profile shall hold exactly: nickname, age band, language, numeral system, avatar, interests (from a list), story cast (first names and relation), session minutes, daily cap. Fields for surname, photo, date of birth and location shall not exist. | M | G7, P2, P5 |
| FR-LRN-002 | A child shall be data owned by a parent account and selected in the child app by a PIN; a child shall have no credentials. | M | P-5, vision non-goals |
| FR-LRN-003 | Consent shall be recorded per scope — voice processing, external content generation — with timestamps, and shall be revocable; features shall be gated by the scope they need. | M | G7, P2 |
| FR-LRN-004 | The system shall keep, per (child, skill): status (`not-started`, `learning`, `mastered`), a mastery estimate, a retention state and the next review date. | M | pedagogy § mastery |
| FR-LRN-005 | Every attempt shall record: child, session, activity, skill(s), correctness or score, confidence, response time, hints used, modality, the distractor chosen if any, and whether it counts as evidence. | M | R8, R9 |
| FR-LRN-006 | An attempt below the confidence floor shall be stored as no-evidence and shall never lower a mastery estimate or advance a review. | M | G10 |
| FR-LRN-007 | Mastery statuses shall be updated from counted evidence by the graph's named mastery rules; the update algorithm shall sit behind one interface so Phase 4 can replace it without changing statuses or codes. | M | pedagogy § mastery, *Planned* |
| FR-LRN-008 | A parent shall be able to export everything stored about a child in a machine-readable form plus a readable summary, and to delete a child irreversibly, including recordings, packs and cached content. | M | UC-10 |
| FR-LRN-009 | A parent account shall support several children, each with its own PIN, statuses and packs. | S | UC-01 |

## FR-TUT — Tutor

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| FR-TUT-001 | The scheduler shall produce a session plan that satisfies scheduler rules R1–R14 of the pedagogy. | M | R1–R14 |
| FR-TUT-002 | Given the same graph, statuses, evidence, settings and date, the scheduler shall produce the same plan; any randomness shall be seeded from the session id. | M | R13 |
| FR-TUT-003 | Every planned activity shall carry a reason object — kind, rule, cause, text in Arabic and English — produced by the rule that chose it. | M | G8, R12 |
| FR-TUT-004 | A plan shall fit the parent's session limit at the 95th percentile of activity durations and shall end with an activity the child has mastered. | M | G4, R7 |
| FR-TUT-005 | The plan, its content and its audio shall be assembled into a pack before the session so that a complete session runs with no network call. | M | G12, R14 |
| FR-TUT-006 | Result submission shall be idempotent on client-generated ids; a resubmitted result shall change nothing. | M | G12 |
| FR-TUT-007 | Activities shall implement the hint ladder (replay → highlight → reveal) with scaffold after `policy.scaffold_after_misses` and switch after `policy.switch_after_misses`; no activity shall have a terminal failure state. | M | G3, R6 |
| FR-TUT-008 | The child shall choose between two skins of the new-skill activity by picture; evidence shall be recorded on the skill, never on the skin. | M | R11 |
| FR-TUT-009 | The system shall enforce the parent's session minutes and daily cap. | M | P2 |
| FR-TUT-010 | The system shall detect confusion between two letters per `policy.confusion_trigger` and shall schedule the pair's discrimination skill and spacing. | S | G11, R9 |
| FR-TUT-011 | The child's progress view shall be rendered from statuses as a garden that only grows: per-letter growth stages, no empty slots, a seed for a skill mastered in the last session. | M | P7, pedagogy § garden |
| FR-TUT-012 | Sessions shall interleave domains per R5. | S | R5 |

## FR-CNT — Content

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| FR-CNT-001 | The story brief — kind, target letter and minimum count, allowed letters and harakat, cast, interests, value from `policy.story_values`, length — shall be produced by the scheduler; the model shall never choose or relax its own constraints; no parent free text shall enter a brief. | M | R10, P-3 |
| FR-CNT-002 | Generation shall go through the AI gateway with a versioned prompt and a structured output schema. | M | FR-AI |
| FR-CNT-003 | Generated text shall pass validators in this fixed order — letters ⊆ allowed; harakat complete and allowed on every letter; target count; length; hero present; blocked words — then the safety layer; each failure shall be logged with the prompt version. | M | G2, P5 |
| FR-CNT-004 | On failure the system shall attempt at most one repair round with the failure named, then fall back to a template story or a read-aloud of known words. | M | R10 |
| FR-CNT-005 | Generated content shall carry a status — Generated, Validated, Flagged, Approved, Rejected — and only Validated or Approved content shall be placed in a pack. | M | P5 |
| FR-CNT-006 | In generated word problems, every number shall be re-parsed from the text and checked against the brief before use. | M | UC-05 |
| FR-CNT-007 | Template stories with slots for the hero and a cast member shall be tagged with the letter set they require and shall serve the story phase while the child's mastered letters are fewer than `policy.template_story_until_letters`. | M | UC-07a |
| FR-CNT-008 | Flagged content shall enter an operator review queue; a sample of Validated content shall be reviewed weekly. | S | UC-09 |
| FR-CNT-009 | The system shall generate no illustration or video for the child in v1. | M | vision non-goals |
| FR-CNT-010 | Packs shall be built in a nightly batch per child; audio and content shall be cached by content hash and reused wherever the same text recurs. | M | G12, G15 |

## FR-SPC — Speech

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| FR-SPC-001 | Every text sent to synthesis shall be fully diacritised; the synthesis port shall reject text with a missing haraka on a letter that needs one. | M | P-2, Checkpoint B |
| FR-SPC-002 | Synthesised audio shall be cached per (text hash, voice) and pre-synthesised into the pack; no synthesis call shall occur during a session. | M | G12, NFR-PERF-004 |
| FR-SPC-003 | Nabta shall speak with one consistent Modern Standard Arabic voice, in short imperative sentences; the voice is chosen by ADR after B1. | M | D-2026-09-21-1 |
| FR-SPC-004 | Read-aloud shall capture audio, recognise it, align it to the target text per word, and produce a match and a confidence per word. | M | UC-06 |
| FR-SPC-005 | A configured confidence floor shall separate evidence from no-evidence; its value is the number measured in B3, per engine. | M | G10, *Planned* |
| FR-SPC-006 | Recordings shall be encrypted at rest, purged at their time-to-live (24 hours, planning), and shall never leave the device without the voice-processing consent; evidence rows shall keep per-word results only. | M | G13, P6 |
| FR-SPC-007 | After N consecutive below-floor attempts (N from policy, planning 2) the session shall offer to continue by touch. | S | G6 |
| FR-SPC-008 | Live per-word feedback during reading may be offered if B4 shows it earns its cost; otherwise scoring is after the utterance. | C | B4, *Planned* |
| FR-SPC-009 | Handwriting shall be scored on the device from stroke data — order, direction, approximate shape — with generous tolerance; stroke images shall not be stored beyond the session. | M | pedagogy § assessment, C1 |

## FR-RPT — Reports and the parent surface

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| FR-RPT-001 | The dashboard shall show the mastery map per letter with harakat progress, sessions this week, minutes, and the current knot, from the same statuses the garden uses. | M | UC-08, G11 |
| FR-RPT-002 | "Why this session today" shall render every activity's reason in plan order and the count of attempts that were not counted as evidence. | M | G8, R8 |
| FR-RPT-003 | The weekly report shall contain at most three sentences and at least one screen-free activity of at most five minutes that names the current knot; the parent shall be able to mark it tried or later. | M | G9 |
| FR-RPT-004 | The parent assistant shall answer a parent's question from retrieved passages of the pedagogy, the parent guide, the activity library and the child's statuses, with sources shown; it shall be available only on the parent surface. | M | UC-11 |
| FR-RPT-005 | The assistant shall decline questions outside the child's learning — including medical or diagnostic ones — by saying what it can help with; it shall never present an answer without a source. | M | UC-11, P1 |
| FR-RPT-006 | Parent settings shall include session minutes, daily cap, numeral system, consents and PIN. | S | UC-01 |
| FR-RPT-007 | No notification shall be addressed to the child; parent notifications shall be limited to the weekly report and consent or safety events. | M | P7 |
| FR-RPT-008 | The operator surface shall provide the review queue, eval results, usage and caps, validator rejection rates, and curriculum and template editors. | M | UC-09 |

## FR-AI — AI gateway

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| FR-AI-001 | Every language-model, synthesis, recognition, moderation and retrieval call shall go through a port owned by the platform; providers shall be configuration. | M | PLAN §6 rule "AI behind interfaces" |
| FR-AI-002 | Every call shall be logged with caller (child, parent or system), provider, model, purpose, prompt version, tokens or characters, latency and cost. | M | E4 |
| FR-AI-003 | Calls shall be capped per child per day and globally; when a cap is reached the system shall fall back to templates, never to a broken session. | M | G15, P8 |
| FR-AI-004 | Only these fields may leave the device or server to an external provider: nickname, age band, interests, cast first names and relations, and non-personal constraints; recordings and parent free text shall never be sent. The port shall enforce this as an allow-list. | M | P5, E2 |
| FR-AI-005 | Provider errors — rate limits, timeouts, connection failures — shall be handled with bounded retries and the fallback in FR-CNT-004; partial output shall never reach a child. | M | E4 |
| FR-AI-006 | Prompts shall be versioned; eval suites shall run in CI against prompt versions and shall gate releases. | M | A6, E4 |
| FR-AI-007 | Logged usage shall be reconciled against the provider's usage reports where available. | S | E4 |
| FR-AI-008 | No free-form input from a child shall ever be sent to a model. | M | P-3 |

# Non-functional requirements

## Child safety (NFR-SAF)

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-SAF-001 | No generated text shall be shown or spoken to a child unless its status is Validated or Approved. | M | G2, P5 |
| NFR-SAF-002 | A red-team suite shall run in CI; zero leakage on the suite shall gate every release. | M | E1 |
| NFR-SAF-003 | The child experience shall contain no open-ended conversation. | M | P-3 |
| NFR-SAF-004 | The child experience shall contain no ads, purchases, locked content, streak loss or child-addressed notifications. | M | P7 |
| NFR-SAF-005 | Every child-facing text shall be fully diacritised. | M | P-2 |

## Privacy (NFR-PRV)

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-PRV-001 | Data about a child shall be limited to the fields in FR-LRN-001 plus statuses, attempts, packs and query logs; nothing else shall be collected. | M | P5 |
| NFR-PRV-002 | A data-flow map of a session and of a parent-assistant question shall be maintained and every field classified; the external allow-list in FR-AI-004 shall be derived from it. | M | E2 |
| NFR-PRV-003 | Consent grants and revocations shall be auditable. | M | P2, Phase 10 |
| NFR-PRV-004 | The developer's own children (Stage 0) shall be subject to every rule above without exception. | M | vision § Success |

## Offline (NFR-OFF)

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-OFF-001 | A full session, including audio and story, shall run with no network; results shall be kept on the device until acknowledged by the server. | M | G12 |
| NFR-OFF-002 | A pack for one child-week shall not exceed 60 MB *(planning; measured in B4)*. | M | G12, B4 |
| NFR-OFF-003 | If no pack exists for today, the last pack shall be used with a template-only session and the parent informed. | M | UC-02 |

## Performance (NFR-PERF)

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-PERF-001 | Touch-to-visible-response shall be ≤ 100 ms at the 95th percentile on the device floor. | M | vision § tech requirements; platform spike |
| NFR-PERF-002 | Cached audio shall start playing ≤ 300 ms after the triggering event. | M | B4 |
| NFR-PERF-003 | Stroke capture shall record every pointer event at the display's refresh rate with no dropped points. | M | C1 |
| NFR-PERF-004 | No AI call shall be made synchronously during a session. | M | G12 |
| NFR-PERF-005 | A parent-assistant answer shall arrive within 8 s at the 95th percentile *(planning)*. | S | UC-11 |
| NFR-PERF-006 | The nightly batch shall build packs for 1,000 children within 6 hours *(planning; E3)*. | S | E3 |

## Cost (NFR-COST)

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-COST-001 | Cost per child-day, all providers included, shall not exceed the ceiling set by E3; planning value USD 0.02 per child-day at list prices; measured weekly. | M | G15, E3 |
| NFR-COST-002 | Identical text shall be synthesised once and shared; identical briefs shall not be generated twice. | M | P8 |
| NFR-COST-003 | A provider free to the developer shall be costed at list price in every estimate. | M | CLAUDE.md lab rules |

## Internationalisation (NFR-I18N)

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-I18N-001 | Every surface shall be right-to-left; parent and operator surfaces shall offer Arabic and English from the first screen; the child app shall be Arabic with audio and pictures, no text a child must read. | M | P3, G1 |
| NFR-I18N-002 | Numerals shall follow the child's setting (Eastern or Western) in every child-facing view. | M | P-2 |
| NFR-I18N-003 | Fonts used for child-facing text shall render harakat correctly on every letter form; a rendering test set shall exist. | M | 0.2, P-2 |

## Accessibility (NFR-ACC)

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-ACC-001 | Child-app touch targets shall be ≥ 64 px; no interaction shall be time-limited; colour shall never be the only signal; reduced-motion settings shall be respected. | M | G1, G3 |
| NFR-ACC-002 | A non-reading child shall be able to complete a session without adult help. | M | G1 |

## Device floor (NFR-DEV)

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-DEV-001 | The child app shall meet NFR-PERF on an Android or iOS device of roughly 2019 mid-range class with 2 GB RAM *(planning; platform spike)*. | M | vision R4, E5 |
| NFR-DEV-002 | Tracing activities shall require a canvas of at least 12 cm on its shorter side; on smaller screens the app shall use landscape or mark the writing track unavailable, never a cramped canvas. | M | vision R4 |

## Reliability, observability, explainability, testing

| ID | Requirement | Pri | Source |
| --- | --- | --- | --- |
| NFR-REL-001 | Result delivery shall be at-least-once with idempotent handling; no attempt shall be counted twice. | M | G12 |
| NFR-REL-002 | The backend shall be one deployable unit with daily backups and a tested restore. | S | P-1 |
| NFR-OBS-001 | The operator shall be able to see weekly: usage and cost per child-day, cap hits, validator rejection rates, eval scores, and the share of attempts below the confidence floor. | M | E4 |
| NFR-EXP-001 | Every planned activity shall have a reason renderable in one Arabic sentence to a parent. | M | G8 |
| NFR-TST-001 | Automated tests shall exist for: mastery-rule arithmetic, scheduler determinism (R13) and rule compliance (R1–R14), every content validator, alignment scoring, graph validation, and one end-to-end happy path per capability. | M | CLAUDE.md |

# External interfaces

All AI capabilities are **ports**: the system defines the interface; a provider is configuration
chosen by ADR. Each port logs per FR-AI-002 and enforces FR-AI-004.

| Port | Input | Output | Decided in |
| --- | --- | --- | --- |
| Generate | brief, prompt version, output schema | structured story or word problem; usage | A2, A3, E3 |
| Repair | previous output, named failure | corrected structured output | A3 |
| Synthesise | fully diacritised text, voice id | audio, duration | B1, B4 |
| Recognise & align | audio, target text | per-word match and confidence | B2, B3 |
| Moderate | text | verdict, categories | E1 |
| Retrieve | question, scope (documents, child id) | passages with sources | A4 |
| Illustrate *(deferred)* | brief | image | C3 |

Device interfaces: microphone (only with consent), touch and stylus events, encrypted local
storage for packs and pending results. Parent channels: the parent web; email for the weekly
report *(Could)*. Export: a machine-readable file plus a readable summary.

# Traceability

## Goals to requirements

| Goal | Requirements |
| --- | --- |
| G1 no reading needed | NFR-I18N-001, NFR-ACC-001, NFR-ACC-002 |
| G2 nothing above ability | FR-CUR-006, FR-CNT-003, FR-CNT-005, NFR-SAF-001 |
| G3 no failure state | FR-TUT-007, NFR-ACC-001 |
| G4 on time, on success | FR-TUT-004, FR-TUT-009 |
| G5 personal content | FR-CNT-001 (cast), FR-CNT-007 |
| G6 modality switch | FR-SPC-007 |
| G7 minimal setup | FR-LRN-001, FR-LRN-003, UC-01 |
| G8 why today | FR-TUT-003, FR-RPT-002, NFR-EXP-001 |
| G9 weekly report | FR-RPT-003 |
| G10 no evidence, never wrong | FR-LRN-006, FR-SPC-005 |
| G11 confusion is a diagnosis | FR-TUT-010, FR-RPT-001 |
| G12 offline, idempotent | FR-TUT-005, FR-TUT-006, NFR-OFF-001…003, NFR-REL-001 |
| G13 ephemeral recordings | FR-SPC-006, FR-LRN-008 |
| G14 gain on unseen text | pilot design (Phase 11); NFR-OBS-001 |
| G15 cheap to run | FR-AI-003, FR-CNT-010, NFR-COST-001…003 |

## Use cases to requirements

| UC | Requirements |
| --- | --- |
| UC-01 | FR-LRN-001…003, FR-LRN-009, FR-RPT-006 |
| UC-02 | FR-TUT-001…009, FR-TUT-011, NFR-OFF-*, NFR-PERF-001…004 |
| UC-03…05 | FR-CUR-001…005, FR-LRN-004…007 |
| UC-06 | FR-SPC-004…007, FR-LRN-006 |
| UC-07 / 07a | FR-CNT-001…007, FR-CNT-010, FR-SPC-001, FR-SPC-002 |
| UC-08 | FR-RPT-001…003, FR-RPT-007 |
| UC-09 | FR-CUR-008, FR-CNT-008, FR-RPT-008, NFR-OBS-001 |
| UC-10 | FR-LRN-008, NFR-PRV-003 |
| UC-11 | FR-RPT-004, FR-RPT-005, FR-AI-001…004, NFR-PERF-005 |

# Glossary

| Arabic | English | Meaning here |
| --- | --- | --- |
| حزمة الجلسة | pack | the plan, content and audio assembled before a session so it runs offline |
| المزامنة | sync | sending stored results to the server when a network exists |
| مكرَّر بأمان | idempotent | resubmitting the same result changes nothing |
| نطاق الموافقة | consent scope | one thing a parent allows separately: voice processing; external generation |
| الدليل | evidence | an attempt that counts toward mastery; below the confidence floor it does not |
| عتبة الثقة | confidence floor | the recognition confidence below which nothing is recorded |
| السبب | reason | the structured explanation attached to every planned activity |
| الجبهة | frontier | skills whose prerequisites are mastered and which are not yet mastered |
| طلب القصة | brief | the scheduler's constraints for a generated story or word problem |
| قصة قالبية | template story | a hand-written story with slots, used while the letter set is small |
| المنفذ | port | an interface the platform owns; the provider behind it is configuration |
| قيمة تخطيط | planning value | a target set before measurement; an experiment replaces it |
| المشغّل | operator | the developer as curriculum author, reviewer and administrator |
| الجهاز الأدنى | device floor | the least capable device the child app must perform on |
| العقدة الحالية | current knot | the skill the child is currently struggling with, named to the parent |

Pedagogical terms (skill, stage, harakat, quick skill, garden…) are defined in the pedagogy
document's glossary and are not repeated here.
