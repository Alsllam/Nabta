# Nabta — Master Plan

> **نبتة** — "seedling". An adaptive AI tutor that teaches young children (4–8) to **read, write and
> count in Arabic** at the quality of a devoted private tutor. Inspired by *A Young Lady's
> Illustrated Primer* (Neal Stephenson, *The Diamond Age*) and the "Primer" request by Andrew Miklas.
>
> **Technology is deliberately undecided.** The first phases study AI from first principles; every
> component enters the stack through an experiment and a decision record. What is borrowed from
> [Wathiq](D:/Training/Wathiq) is the *way of working* — one step = one commit, learning notes,
> checkpoints, documents as deliverables — not its technologies.

::: {custom-style="RTL"}
**الملخص.** نبتة معلّم ذكي متكيّف للأطفال من ٤ إلى ٨ سنوات يعلّمهم القراءة والكتابة والحساب
بالعربية. يهيّئ الوالد ملف الطفل (اسمه، عمره، اهتماماته، أفراد أسرته) ثم يلتقي الطفل بنبتة يوميًا في
جلسة قصيرة: مراجعة لما بدأ يُنسى، مهارة جديدة واحدة على حافة قدرته، وقصة مولَّدة له هو بطلها
ومكتوبة فقط بالحروف والكلمات التي يستطيع قراءتها اليوم. كل إجابة وكل قراءة بصوت عالٍ وكل حرف يرسمه
يحدّث نموذج إتقان لكل مهارة، ومنه تُخطَّط الجلسة التالية. الوالد يتلقى تقريرًا أسبوعيًا مع نشاط واحد
يقوم به مع طفله. نبتة تكمّل المعلّم ولا تستبدله.

**التقنيات غير محسومة عمدًا.** المراحل الأولى دراسة لتقنيات الذكاء الاصطناعي من الصفر: النماذج
اللغوية، الصوت (تحويل النص إلى كلام والتعرف على الكلام)، الرؤية والكتابة اليدوية، خوارزميات التعلم
المتكيّف، السلامة والخصوصية والتكلفة. كل مكوّن يدخل المشروع عبر تجربة مقاسة وقرار موثّق (ADR)،
لا لأنه استُخدم من قبل.
:::

## 1. Vision

**Problem.** Learning to read Arabic is hard: 28 letters with up to four positional forms, short
vowels carried by diacritics (harakat) that vanish from adult text, and a gap between the dialect a
child speaks and the Modern Standard Arabic of books. One-on-one tutoring is the only method that
reliably closes gaps, and it is expensive, scarce and unevenly distributed. Screen products for this
age group are English-first, generic, and "adaptive" only in name: every child sees the same
sequence.

**Product.** Nabta is a tutor, not a chatbot. A parent creates a child profile (nickname, age band,
language, interests, family and pets for stories). The child then meets Nabta every day for a
10–15 minute session: a warm-up that reviews what is fading, one new skill at the edge of what the
child can do, and a story generated for that child — starring them, written only with the letters
and words they can read today — followed by a small celebration. Every answer, read-aloud attempt
and traced letter updates a per-skill mastery model; the next session is planned from it. Parents
get a weekly report in plain Arabic with one five-minute offline activity.

**Operator.** One developer. Technology choices are open: Phases 1–5 study AI from first
principles and choose each component by experiment. The product must be cheap to run and must
complete a full session without a network connection.

**Success.**

| Horizon | Target |
| --- | --- |
| Study (Phases 1–5) | Every component in §8 has an ADR backed by a measured experiment; the developer can explain each choice from first principles |
| Pilot | 10 families, ≥ 4 sessions/week for 8 weeks; measurable gain on a letter-sound + decoding pre/post test |
| Product | 1,000 active children within 6 months of publish; median session completion ≥ 80 % |

## 2. Users and core use cases

| Actor | Who | Primary need |
| --- | --- | --- |
| Child | Learner aged 4–8; cannot read instructions; touch + voice only | A patient tutor that is never boring and never shaming |
| Parent | Account owner; gives consent, sets up the child, sets time limits, reads reports | Know the child is learning and safe; do one useful thing a week |
| Curriculum author / Admin | The operator | Maintain the skill graph and templates, review flagged content, watch evals, cost and caps |
| Teacher *(future)* | Classroom user | See a class at a glance; assign focus skills |

| UC | Use case | Built in phase |
| --- | --- | --- |
| UC-01 | Parent onboarding: account, consent, child profile (nickname, age band, language, numerals, interests, story cast, avatar), session length and daily cap | 9 |
| UC-02 | Daily session: child picker → greeting → warm-up review → new skill → story → wrap-up sticker; works offline from a pre-synced activity pack, results sync later | 6, 7 |
| UC-03 | Reading track: letter shapes/names → letter sounds → harakat syllables → long vowels, sukoon, shadda → positional forms and connection → blending words → sight words → sentences → short passages with comprehension | 6–8 |
| UC-04 | Writing track: pre-writing strokes → trace letters with stroke order → write a letter from its sound → connect letters → copy words → write from dictation | 6–8 |
| UC-05 | Arithmetic track: counting and one-to-one → numerals 0–10 (Eastern/Western) → compare and order → number bonds → +/− within 10 → numbers to 20 and 100, place value → +/− within 20 → personalised word problems → skip counting | 6–8 |
| UC-06 | Read-aloud assessment: child reads a word/sentence/story → speech recognition → word-level alignment → evidence for the learner model; low confidence is "no evidence", never "wrong" | 8 |
| UC-07 | Personalised story: generated under constraints (allowed letters and vocabulary, length, interests, story cast), validated, safety-checked, cached, read aloud with word highlighting | 8 |
| UC-08 | Parent dashboard and weekly report: mastery map, time, streak, struggling skills, one offline activity; settings | 9 |
| UC-09 | Admin: edit skill graph and templates, review flagged content, run evals, watch usage and caps | 9 |
| UC-10 | Export or delete a child's data | 10 |

## 3. The tutor's brain — pedagogy (domain, not technology)

What separates Nabta from "a chatbot for kids" is a pedagogy that is **explainable**: a parent can
be told in one sentence why a skill was chosen. How that is implemented is an open question with a
working hypothesis, tested in Phase 4:

- **H1 (engineered tutor):** a skill graph + a learner model + a deterministic scheduler decide
  *what* to teach; a language model only *writes* content under constraints.
- **H2 (model-as-tutor):** a language model with the learner's state in its context decides what
  comes next, with the skill graph as guidance.

Phase 4 simulates both and measures time-to-mastery, retention, explainability and cost. The rest of
this section describes the domain either hypothesis must serve.

### 3.1 Skill graph

A directed acyclic graph of skills across three domains (Reading, Writing, Arithmetic). Each skill:
code, ar/en name, level band, prerequisites, mastery criterion, allowed activity types, and a
**content scope** (which letters, harakat, words or number ranges it may use). Maintained as data in
`docs/curriculum/skills.v<version>.json`. v0.1 targets roughly 120 skills drawn from KSA KG and
Grade 1–2 Arabic and mathematics standards and from Science-of-Reading phonics adapted to Arabic.

### 3.2 Learner model

Per (child, skill): an estimate of mastery updated from evidence (touch answers, read-aloud scores,
handwriting scores), plus a retention state for review scheduling. Candidate algorithms — Bayesian
Knowledge Tracing, Item Response Theory / Elo, Deep Knowledge Tracing, SM-2 / FSRS — are studied
and compared in Phase 4.

### 3.3 Session shape and scheduler rules

Default 12-minute session: hello 0.5 → warm-up 3 → learn 5 → story 3 → goodbye 0.5.
Rules any scheduler must honour: due reviews before new material; one new skill per session at the
edge of ability; interleave domains; two consecutive misses → scaffold, three → switch activity or
offer a break; respect the parent's time limit; always end with a success.

### 3.4 Activities — two tiers

| Tier | What | Examples |
| --- | --- | --- |
| 1 — templates | Parameterised from the skill's content scope and the learner model; instant, safe, offline; the bulk of a session | `letter-tap`, `letter-trace`, `syllable-blend`, `word-build`, `count-tap`, `number-trace`, `compare`, `add-objects`, `read-aloud` |
| 2 — generated | Written by a model under constraints (letter set, vocabulary, length, interests, story cast), then validated and safety-checked before a child sees it | `story`, `word-problem`, `dialogue` |

### 3.5 Assessment and adaptation

Touch answers are exact. Read-aloud yields per-word evidence with a confidence floor below which
nothing is recorded. Handwriting is scored on stroke order, direction and shape with generous
tolerance — motor practice, not grading. Adaptation levers: which skill (difficulty), repetitions
(pace), audio- vs text-heavy (modality), themes and cast (interest), hint ladder model → prompt →
fade (scaffolding), tone and breaks (affect).

### 3.6 Tutor persona

"نبتة" is a sprout character with one consistent voice: kind, patient, celebrates effort, never
shames, never claims to be human, and in v1 never opens an unconstrained conversation.

## 4. The AI study curriculum (Phases 1–5)

Each study step produces four things: a **concept note** in the developer's own words
(`docs/learning/`), a **runnable experiment** with a results table (`lab/<step-id>-<slug>/`), a
"**what this means for Nabta**" paragraph, and — when a choice emerges — an **ADR**
(`docs/decisions/`). Experiments are small and measured; a native-speaker rating (the developer)
counts as a measurement for Arabic quality as long as the sample and rubric are written down.

### Module A — Foundations of modern AI (Phase 1)

| Step | Concept | Experiment | Nabta question |
| --- | --- | --- | --- |
| A1 | What a language model is: tokens, next-token prediction, context window, sampling, why it hallucinates | Tokenise the same Arabic and English passage with three tokenisers; tokens per word | How much more does Arabic cost, and what does that change? |
| A2 | The model landscape: open-weights vs hosted APIs, sizes, quantisation, what runs on a laptop / phone / server; Arabic benchmarks | Same prompt on one small local model and two hosted models; latency, cost, Arabic quality | Which class of model can write a child's story? |
| A3 | Prompting as programming: roles, few-shot, constraints, structured output (schemas), refusals | Constrained Arabic story with an allowed letter set; compliance rate by model and temperature | Can a prompt alone keep a story inside a letter set? |
| A4 | Embeddings and retrieval: similarity, when retrieval helps and when it does not | Embed a graded word list; nearest neighbours for "words a level-3 child can read" | Does retrieval help pick vocabulary? |
| A5 | Adapting models: prompting vs fine-tuning vs LoRA vs distillation; data needs and costs | Fine-tune a small model on ~200 synthetic constrained stories; compliance vs prompting | Is fine-tuning worth it for constraint compliance? |
| A6 | Evaluation: eval sets as the unit tests of AI, model-as-judge and its limits, regression | An eval harness for A3 rerun across models | What is our first eval suite? |
| A7 | Agents and tool use: function calling, loops, when *not* to use an agent | A tiny tool-calling loop; compare with a hand-written state machine for a session | Is a session an agent or a state machine? |

**Checkpoint A:** "Why does Arabic cost more tokens than English, and what did that change in the design?"

### Module B — Speech (Phase 2)

| Step | Concept | Experiment | Nabta question |
| --- | --- | --- | --- |
| B1 | How text-to-speech works: text → phonemes → acoustic model → vocoder; neural TTS; voice cloning. Arabic: diacritisation decides pronunciation | 20 sentences with and without harakat on three or four engines (open and hosted); blind native-speaker rating | Which voice can a child listen to for ten minutes, and what text must it receive? |
| B2 | How speech recognition works: features, encoder/decoder, CTC vs attention, word timestamps; why child speech is harder | Recordings of read words and sentences on three engines; word error rate per engine | Can any engine hear a six-year-old read Arabic? |
| B3 | Reading assessment: forced alignment, phoneme scoring, pronunciation-assessment services, confidence | Align a known target text to audio; per-word match; find the confidence floor | Where does "no evidence" beat "wrong"? |
| B4 | Streaming and latency: real-time vs batch, on-device speech, audio caching | End-to-end latency prompt → speech → playback; cache hit rate on a session's text | What must be pre-generated before a session starts? |

**Checkpoint B:** "Why must text sent to speech synthesis be fully diacritised, and where in the pipeline does that happen?"

### Module C — Vision and handwriting (Phase 3)

| Step | Concept | Experiment | Nabta question |
| --- | --- | --- | --- |
| C1 | Online (stroke) vs offline (image) handwriting recognition; template matching (DTW), stroke order; small on-device models | Capture strokes for five letters; DTW score vs template; then an image classifier on the rendered strokes | Strokes or pixels for a tracing activity? |
| C2 | Vision-language models: what they can judge, cost and latency | A vision model rates "is this a well-traced ب?"; agreement with the DTW score | Does a model add anything over geometry here? |

**Checkpoint C:** "Stroke data or an image — which does a tracing activity need, and why?"

### Module D — Adaptive learning science (Phase 4)

| Step | Concept | Experiment | Nabta question |
| --- | --- | --- | --- |
| D1 | Knowledge components, skill graphs, mastery learning, the zone of proximal development | Encode 20 reading skills as a graph; check it is acyclic and every skill is reachable | Is the v0.1 graph well-formed? |
| D2 | Bayesian Knowledge Tracing | Implement BKT; unit tests on hand-computed cases | How does P(mastery) move on three rights and one wrong? |
| D3 | Item Response Theory and Elo-style ratings | Implement a 1-parameter model; compare with BKT on simulated learners | Does item difficulty buy us anything at this age? |
| D4 | Deep Knowledge Tracing and why we may not need it | Read and summarise; estimate data needs against our pilot size | When would a learned model beat BKT? |
| D5 | Spaced repetition: SM-2, FSRS | Implement one; simulate retention over 60 days | What is the review load per session? |
| D6 | Session planning: interleaving, scaffolding, fatigue | A deterministic scheduler over the graph and learner model; property tests | Same inputs, same plan? |
| D7 | Hypothesis test H1 vs H2 | Simulate 1,000 synthetic learners under the engineered scheduler and under model-as-tutor; time-to-mastery, retention, cost, explainability | Which hypothesis does Nabta build on? |

**Checkpoint D:** "A child answers three right then one wrong — what happens to P(mastery), and why does slip matter?"

### Module E — Safety, privacy, deployment and cost (Phase 5)

| Step | Concept | Experiment | Nabta question |
| --- | --- | --- | --- |
| E1 | Guardrails: input/output classifiers, allow-lists, constrained decoding; why a prompt is not a safety boundary | 50 red-team prompts through the story pipeline; leakage rate per layer | Which layer catches what? |
| E2 | Children's data: minimisation, consent, retention, what may leave the device or server | A data-flow map of one session; classify every field | What must never leave the device? |
| E3 | Where inference runs: on-device, self-hosted server, hosted APIs; latency, cost, privacy | Cost model for 1,000 children × one session/day under each option | What does a session cost, and where? |
| E4 | Observability for AI: logging, tracing, caps, evals in CI | A usage ledger and a cap on the A3 harness | What do we watch weekly? |
| E5 | **Stack decision** | One ADR per component in §8, each citing the experiment that decided it; Architecture & DB v0.1 written from the ADRs | — |

**Checkpoint E:** "If the hosted model's price doubled tomorrow, which component would you move first, and what would the child notice?"

## 5. Phases and checkpoint questions

| # | Phase | Outcome | Checkpoint question |
| --- | --- | --- | --- |
| 0 | Bootstrap & docs foundation | Repo, plan, Vision, **Pedagogy v0.1** (skill graph on paper + JSON seed), SRS v0.1, capability architecture v0.1 (no products named) | Name the capabilities in §6 and explain why a child is not a user account. |
| 1 | Study — AI foundations (Module A) | Concept notes A1–A7, lab experiments, first eval suite, ADRs on model class and prompting approach | Checkpoint A |
| 2 | Study — Speech (Module B) | Notes B1–B4, engine comparisons, ADRs on synthesis, recognition and assessment | Checkpoint B |
| 3 | Study — Vision & handwriting (Module C) | Notes C1–C2, tracing prototype, ADR on handwriting scoring | Checkpoint C |
| 4 | Study — Adaptive learning (Module D) | Notes D1–D7, simulator, ADR on the learner model and H1/H2 | Checkpoint D |
| 5 | Study — Safety, deployment, cost → **stack decision** (Module E) | Notes E1–E4, data-flow map, cost model, one ADR per component, Architecture & DB v0.1 | Checkpoint E |
| 6 | Build — tutor core | Curriculum store + seeder, learner model, scheduler, session engine, offline-capable API | How does the scheduler choose between a due review and a frontier skill? |
| 7 | Build — child experience v1 | Child picker, session flow, three template activities, cached audio, offline pack, rewards | Where does the tracing canvas state live, and what syncs when the network returns? |
| 8 | Build — content & speech | Constrained story generation with validators and safety filter, synthesis cache, read-aloud scoring, handwriting scoring, evals | A generated story contains a word outside the allowed letter set — where is it caught and what does the child see? |
| 9 | Build — parent & admin | Onboarding + consent, dashboard, weekly report, curriculum and template editors, review queue, evals dashboard, observability | What three signals would tell you story quality dropped this week? |
| 10 | Hardening & child safety | Consent audit, minimisation review, export/delete, rate limits, encryption of recordings, red-team evals as regression tests, `privacy` doc | Where does a child's voice recording live, for how long, and who can read it? |
| 11 | Pilot & publish | 10-family pilot with pre/post test, iterate, landing page, listing, open-source core | What did the pre/post test measure, and what result would have made you stop? |
| 12 | Toward the Primer | Long-term memory across years, guided comprehension dialogues, English track, dialect-aware speech, teacher mode, sibling play | — |

Phases 1–5 are sequential by design: each module's ADRs are inputs to the next. Build phases 7 and
9 may interleave with 8.

## 6. Capability architecture (technology-neutral)

```
 Child experience ──┐                 ┌─ Language model(s)      — content generation only
 Parent surface     ├──► Tutor core ──┤─ Speech synthesis      — cached per text + voice
 Admin surface      ┘       │         ├─ Speech recognition    — read-aloud evidence
                            │         └─ Handwriting scoring   — stroke-based
                            ├─ Curriculum store   skill graph, templates, content items, word lists
                            ├─ Learner model      mastery + retention per (child, skill), evidence log
                            ├─ Scheduler          due reviews → frontier → rules → session plan
                            ├─ Content service    generate → validate → safety → cache → review
                            ├─ Speech service     synthesis, recognition, alignment, recording lifecycle
                            └─ Platform           parent identity, storage, background jobs, AI gateway
                                                  (routing, caps, usage ledger), observability
```

Rules that hold whatever the stack turns out to be:

- **Explicit boundaries.** Curriculum, Learners, Tutor, Content, Speech, Reports and the AI
  gateway are separate modules with contracts; no module reads another's storage directly.
- **AI behind interfaces.** Every model, synthesis and recognition call goes through a port owned by
  the platform; providers are configuration; every call is logged and capped.
- **Nothing unvalidated reaches a child.** Generated content is cached only after validation and
  a safety check; any rejection falls back to a template activity.
- **Children are not accounts.** A child is data owned by a parent account, selected by a PIN.
- **Offline is a feature.** The child experience completes a session from a pre-synced pack;
  result submission is idempotent on client-generated ids.

## 7. Conceptual data model v0.1 (grows in the Database doc after Phase 5)

- **Curriculum:** `Domain` (code, name ar/en) · `Skill` (code, domain, name ar/en, level band,
  mastery criterion, content scope) · `SkillPrerequisite` · `ActivityTemplate` (code, type, tier,
  parameter schema, modality) · `ContentItem` (letter / syllable / word / sight word / number /
  shape, text with harakat, letter set, level, media keys) · `WordList` (level, words)
- **Learners:** `Child` (parent, nickname, age band, language, numerals, avatar, interests, story
  cast, session minutes, daily cap) · `Consent` (scopes, granted/revoked) · `SkillMastery` (child,
  skill, mastery estimate, retention state, next review, status) · `Attempt` (child, session,
  activity, skill, correct, score, confidence, response time, hints, modality, evidence)
- **Tutor:** `Session` (child, planned minutes, plan, summary, status, synced at) ·
  `SessionActivity` (order, phase, template, skill, content refs, parameters, result)
- **Content:** `GeneratedContent` (kind, child?, skill, prompt version, constraints, text, status
  Generated / Validated / Flagged / Approved / Rejected, validation report, model, cost) ·
  `ReviewItem` · `AudioAsset` (text hash, voice, provider, blob, duration) · `ActivityPack`
- **Speech:** `Recording` (child, attempt, blob, retain-until, transcript, alignment, status)
- **Reports:** `WeeklyReport` (child, week, content, sent at)
- **AI gateway:** `Usage` (who, provider, model, purpose, tokens, latency) · `Prompt` (name,
  version, body, hash) · `EvalRun` (suite, prompt version, model, scores)

## 8. Decisions

### 8.1 Open — decided by study, one ADR each

| Component | Candidates to study (not a shortlist — the study may add or drop) | Decided in |
| --- | --- | --- |
| Language model for content | Small open-weights run locally · larger open-weights on a server · hosted APIs; with or without fine-tuning | A2, A3, A5, E3 |
| Prompting and output control | Plain prompting · schema-constrained output · constrained decoding · post-validation | A3, A6, E1 |
| Speech synthesis | Open neural TTS · hosted neural voices · on-device engines; Arabic diacritised input | B1, B4 |
| Speech recognition and reading assessment | Open ASR models · hosted ASR · pronunciation-assessment services · forced alignment | B2, B3 |
| Handwriting scoring | Stroke template matching · small on-device classifier · vision model | C1, C2 |
| Learner model and scheduler | BKT · IRT/Elo · DKT · SM-2/FSRS; engineered scheduler vs model-as-tutor | D2–D7 |
| Safety layer | Output classifiers · allow-list validators · constrained decoding · human review sampling | E1 |
| Where inference runs | On-device · self-hosted server · hosted APIs, per component | E3 |
| Child experience platform | Native mobile · cross-platform toolkit · web app; must do audio, strokes, offline | E5 |
| Backend, storage, jobs, identity | Chosen at E5 from the requirements the study produced | E5 |
| Parent and admin surfaces | Chosen at E5 | E5 |

### 8.2 Already taken — product and process, not technology

| ID | Decision | Why |
| --- | --- | --- |
| P-1 | One operator; cheap to run; one deployable | Same constraint as Wathiq; keeps scope honest |
| P-2 | Arabic first: MSA with full harakat for early reading; Eastern or Western numerals per child | Matches school; harakat are the vowels a beginner needs |
| P-3 | No open-ended chat with the child in v1 | Safety and scope; every child-facing text is constrained and validated |
| P-4 | Pedagogy must be explainable to a parent (H1 is the working hypothesis, tested in D7) | Trust; testability |
| P-5 | Child data minimisation; recordings have a time-to-live | Children's-privacy law and parental trust |
| P-6 | Way of working from Wathiq: one step = one commit = one learning note; checkpoints gate phases; deliverables as Markdown rendered to `.docx` | Proven with this developer; documents travel with the code |
| P-7 | Local git until the pilot phase | Learning cadence first; publish after safety hardening |

## 9. Child-safety and privacy principles (non-negotiable)

| # | Principle | In practice |
| --- | --- | --- |
| P1 | Child-safe by construction | No free chat; every child-facing text passes constraints, validators and a safety filter; template fallback on any rejection |
| P2 | Parent in control | Consent per scope (voice processing, external content generation); session length and daily cap; export/delete |
| P3 | Arabic first, bilingual always | MSA with harakat, right-to-left everywhere, ar + en from the first screen |
| P4 | Explainable pedagogy | A parent can be told *why* a skill was chosen |
| P5 | Nothing unvalidated reaches a child | Generated content is cached only after validation; flagged items go to review |
| P6 | Recordings are ephemeral | Scored, then purged on a time-to-live; stored encrypted; never sent to an external service without consent |
| P7 | No dark patterns | No ads, no purchases in the child experience, no streak punishment, sessions end on time with a success |
| P8 | Free to run, one operator | Caching, per-child daily caps, a cost model kept current from E3 |

## 10. Deliverable documents

| Key | File | Grows in phase |
| --- | --- | --- |
| `vision` | Vision & Project Charter | 0 |
| `pedagogy` | Curriculum & Learning-Model Design (skill graph, session shape, scheduler rules, assessment rules, activity catalogue; algorithm chosen in Phase 4) | 0 → 4, 6, 8 |
| `srs` | Software Requirements Specification (IEEE 830 style, ar+en glossary) | 0 → every phase |
| `study-notes` | AI Study Log: one section per module with experiments, results and what changed | 1 → 5 |
| `architecture` | Capability architecture (0) → Software Architecture with products named (5 →) | 0, 5, 6, 8, 9 |
| `database` | Database Design (ERD, dictionary, migrations log) — after the stack decision | 5 → |
| `api` | API Specification | 6 → |
| `ai-safety` | AI Content, Speech & Child-Safety Design | 5, 8, 10 |
| `privacy` | Privacy Policy (for parents) & Terms, ar+en | 10, 11 |
| `user-guide` | Parent Guide | 9 |
| `test-plan` | Test Plan & Deployment Guide | 9, 10, 11 |
| `pilot-report` | Pilot Design & Results | 11 |

## 11. Reading list (mapped to modules)

- **A** — Vaswani et al., *Attention Is All You Need* (read for the ideas, not the math);
  Karpathy, *Intro to Large Language Models* and *Let's build the GPT Tokenizer*; a tokenizer
  playground for Arabic; provider prompt-engineering guides; Anthropic, *Building Effective
  Agents*; a survey of Arabic LLM benchmarks
- **B** — Radford et al., *Robust Speech Recognition via Large-Scale Weak Supervision* (Whisper);
  an overview of neural TTS (Tacotron → VITS → current); Montreal Forced Aligner docs; papers on
  Arabic diacritisation and on children's ASR
- **C** — Online handwriting recognition surveys; dynamic time warping tutorials; a vision-language
  model overview
- **D** — Corbett & Anderson, *Knowledge Tracing* (1995); Piech et al., *Deep Knowledge Tracing*
  (2015); FSRS algorithm write-up; SM-2; Koedinger's Knowledge-Learning-Instruction framework;
  Science-of-Reading primers; research on harakat and diglossia in Arabic early literacy; KSA
  Ministry of Education KG and Grade 1–2 standards
- **E** — OWASP LLM Top 10; COPPA, GDPR-K and KSA PDPL provisions on children's data; model
  pricing pages and quantisation guides for the cost model
