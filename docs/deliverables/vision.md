---
title: "Nabta — Vision & Project Charter"
subtitle: "نبتة — الرؤية وميثاق المشروع"
author: "Abdulsalam"
version: "0.1"
date: "2026-09-21"
status: "Draft"
---

## Revision history {.unnumbered}

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 0.1 | 2026-09-21 | Abdulsalam | First charter: problem, users, the reference child and her goals, principles, scope and non-goals, success horizons, risks, roadmap summary |

# Executive summary

Nabta (نبتة, "seedling") is an adaptive tutor that teaches children aged 4–8 to read, write and
count in Arabic, at the quality of a devoted private tutor. A parent sets up the child in five
minutes; the child meets Nabta every day in a ten-minute session that reviews what is fading,
teaches one new skill at the edge of what the child can do, and ends with a story written only
from the letters the child has mastered — starring the child. Every answer updates a per-skill
mastery model; the next session is planned from it; a parent can always be told, in one sentence,
why a skill was chosen today.

Nabta is a tutor, not a chatbot. Nothing generated reaches a child unvalidated, the child never
chats with an unconstrained model, children are not accounts, recordings are deleted after they
are scored, and a full session runs without a network connection.

The project has two goals of equal weight: **to teach the developer's own children first, then
publish the product if it works**; and **to learn AI from first principles, one measured
experiment at a time**. Technology is deliberately undecided: every component enters the stack
through an experiment and a decision record ([PLAN.md](../PLAN.md) §4, §8).

::: {custom-style="RTL"}
**الملخص.** نبتة معلّم ذكي متكيّف يعلّم الأطفال من ٤ إلى ٨ سنوات القراءة والكتابة والحساب بالعربية.
يهيّئ الوالد ملف الطفل في خمس دقائق، ثم يلتقي الطفل بنبتة يوميًا في جلسة من عشر دقائق: مراجعة لما
بدأ يُنسى، مهارة جديدة واحدة على حافة قدرته، وقصة مكتوبة فقط بالحروف التي أتقنها وهو بطلها. كل
إجابة تحدّث نموذج إتقان لكل مهارة، ومنه تُخطَّط الجلسة التالية، ويمكن دائمًا إخبار الوالد بجملة
واحدة لماذا اختيرت هذه المهارة اليوم.

نبتة معلّم لا روبوت محادثة: لا يصل الطفل شيء مولَّد قبل التحقّق منه، ولا يحادث الطفل نموذجًا حرًّا،
والطفل ليس حسابًا، والتسجيلات تُحذف بعد تقييمها، والجلسة الكاملة تعمل بلا إنترنت.

للمشروع هدفان بوزن واحد: **تعليم أولاد المطوّر أولًا ثم النشر إن نجح**، و**تعلّم الذكاء الاصطناعي من
المبادئ الأولى بتجربة مقاسة في كل خطوة**. التقنيات غير محسومة عمدًا.
:::

# The problem

Learning to read Arabic is harder than it looks from the outside:

- **28 letters with up to four positional forms each** — a child must recognise ب as ب، بـ، ـبـ، ـب.
- **Short vowels are diacritics (harakat)** that carry the pronunciation and then vanish from adult
  text. A beginner needs them on every letter; most children's apps drop them or place them wrong.
- **Diglossia.** The child speaks a dialect at home and meets Modern Standard Arabic in books.
  The words a five-year-old knows by ear are not the words on the page.
- **Confusable pairs** — ب ت ث ن ي, ج ح خ, د ذ, ر ز, س ش, ص ض, ط ظ, ع غ, ف ق — differ by dots
  alone, and the confusion persists for months unless it is taught as a skill of its own.

One-on-one tutoring is the only method that reliably closes gaps, and it is expensive, scarce and
unevenly distributed. Screen products for this age are English-first, generic, and "adaptive"
only in name: every child sees the same sequence, progress is a streak counter, and the child
wanders a map of games with no plan behind it.

# Users

| Actor | Who | Primary need |
| --- | --- | --- |
| **Child** | Learner aged 4–8; cannot read instructions; touch and voice only | A patient tutor that is never boring and never shaming |
| **Parent** | Account owner; consents, sets up the child, sets time limits, reads the weekly report, asks how to help | Know the child is learning and safe; do one useful thing a week |
| **Curriculum author / operator** | The developer | Maintain the skill graph, content and templates; review flagged content; watch evals, cost and caps |
| **Teacher** *(future)* | Classroom user | See a class at a glance; assign focus skills |

The age band 4–8 is wide on purpose — it spans KG to grade 2 — and the product adapts by age
band: shorter, touch-heavy sessions for the youngest; more reading and writing for the oldest.
The curriculum is one graph; the entry point and the session shape differ per child.

# The reference child: ماسة

Every requirement in this project can be traced to a moment in one story. ماسة is five years and
nine months old; her little brother is سامي; her cat is توت. She knows the *shape* of her name from
her school bag and does not yet know it is made of letters.

::: {custom-style="RTL"}
**المساء الأول.** أمّها فتحت نبتة بعد العشاء وأعطتها ست دقائق: الاسم الذي تحبّ أن تُنادى به، عمرها،
أنها تحبّ القطط والألوان، أن لها أخًا صغيرًا اسمه سامي وقطة اسمها توت، وأن الجلسة عشر دقائق، وأن
الميكروفون مسموح. ثم سلّمتها الجهاز.

**الجلسة الأولى.** لا توجد قصة؛ ماسة لا تعرف حرفًا واحدًا بعد، ونبتة لا تكذب عليها بقصة لا تستطيع
قراءتها. ظهرت نبتة — نبتة صغيرة خضراء بصوت هادئ — وعرضت ثلاثة حروف: م، ا، س. لمست ماسة الحرف
الخطأ مرتين. لم يحدث شيء أحمر، ولم يقل أحد «خطأ». أعادت نبتة الصوت ببطء وأضاءت الحرف الصحيح قليلًا.
انتهت الجلسة بعد تسع دقائق على نجاح.

**اليوم الثاني عشر.** ماسة تعرف أحد عشر حرفًا. لأول مرة ظهر نصّ:
:::

::: {custom-style="ChildText"}
مَاسَة تُنَادِي تُوت.

تُوت لَا يَرُدّ.

تُوت نَامَ!
:::

::: {custom-style="RTL"}
كل حرف في هذه الأسطر حرفٌ أتقنته هي، والقطة قطتها. ما لا تعرفه أمّها أن المدقّق رفض النسخة الأولى
من القصة لأنها استعملت حرفًا لم تتعلّمه ماسة بعد.

**اليوم التاسع عشر، في السيارة.** لا إنترنت. الجلسة تعمل كاملة، والنتائج تنتظر حتى الليل.

**اليوم الثالث والعشرون.** ماسة نعسانة وتُتمتم. الميكروفون يلتقط صوتًا غير واضح. نبتة لا تحسبها
خطأ ولا تُنقص شيئًا من تقدير الإتقان؛ تسأل: «نُجرّب باللمس؟» وتكمل الجلسة باللمس. التسجيل يُحذف.

**الأسبوع السادس.** ماسة تخلط بين ن وت — ستّ مرات. نبتة لم تكرّر التمرين بصوت أعلى: أدخلت نشاطًا
يميّز النقاط وباعدت بين الحرفين. تقرير الأسبوع وصل لأمّها في ثلاث جمل ونشاط بورقة وقلم، وسطر يشرح
لماذا اختارت نبتة هذا الحرف اليوم. وحين سألت أمّها «كيف أساعدها في ن وت؟» جاء الجواب من دليل
الوالدين ومن حالة ماسة نفسها، مع مصدره.

**اليوم التسعون.** ماسة تقرأ جملة لم ترها من قبل. أمّها لم تشترِ شيئًا داخل التطبيق، ولم ترَ إعلانًا،
ولم تُعاقَب ماسة على يوم انقطعت فيه.
:::

## Goals derived from the story

Each goal names the moment it comes from and the measurement that would show it is not met.
Goals are the source of the requirements in the SRS and of the acceptance criteria in the pilot.

| ID | Goal | How we know | From |
| --- | --- | --- | --- |
| G1 | A child completes a full session without reading a word on screen | A non-reading four-year-old finishes a session with no adult help; every instruction is audible, every control is pictorial | First session |
| G2 | No text reaches the child that they cannot read today | 100 % of displayed text decomposes into letters and words this child has mastered; zero exceptions | No story on day one |
| G3 | No failure state in the interface | Every activity is solvable through a hint ladder (replay → highlight → reveal); no red, no "wrong" | Two misses, nothing red |
| G4 | The session ends on time and on a success | p95 session length ≤ the parent's limit; 100 % of sessions end on a success event — including bad ones | Nine minutes of ten |
| G5 | Generated content belongs to this child | Story includes the child or a cast member in ≥ 90 % of cases while staying inside the letter set | توت is her cat |
| G6 | Fatigue or unclear audio changes the modality, not the estimate | After N low-confidence attempts the activity switches to touch and offers to continue | Day 23 |
| G7 | Setup takes ≤ 5 minutes with the least possible data | Median setup ≤ 5 min; no surname, photo or location; voice consent separate from generation consent and revocable | The first evening |
| G8 | A parent is told why this skill today, in one sentence | Every planned activity carries a human-readable reason generated from the scheduler's decision | The weekly report's last line |
| G9 | The weekly report is three sentences and one paper activity | ≤ 3 sentences, ≥ 1 screen-free activity ≤ 5 min, names the current knot («ن مقابل ت») | Week six |
| G10 | Low confidence is no evidence, never wrong | Mastery never decreases from an attempt below the confidence floor; the floor is measured (B3), not guessed | Day 23 |
| G11 | Repeated confusion is a diagnosis, not a reason to repeat | Confusion pairs are detected and answered with a different activity and spacing, never the same drill | Six ن/ت mistakes |
| G12 | A full session without a network, and a sync that never double-counts | Session including audio runs from a pre-synced pack; submission is idempotent on client-generated ids | The car |
| G13 | Recordings are scored, then gone | No recording older than its time-to-live exists anywhere; encrypted while it exists; never leaves the device without consent | Day 23 |
| G14 | Gain is measured on text the child has never seen | Pre/post letter-sound and decoding test on materials outside the app; in-app accuracy is calibration, not success | Day 90 |
| G15 | Cheap enough for one operator | Cost per child-day under the ceiling set in E3, watched weekly with per-child caps | — |

Three of these cost something real, and the charter accepts the cost: **G2** makes the first week
the hardest to design (no text to read yet, so a week of delight without text); **G10** discards a
share of the child's effort to avoid ever being unfair to a sleepy child; **G12** forces all
generation into a nightly pack, which means tomorrow's story is written on a *predicted* letter
set — the tension between G12 and G2 is an architecture decision owed before Phase 8.

# Product principles

The eight principles of [PLAN.md](../PLAN.md) §9 are non-negotiable; they are restated here as the
charter's terms.

| # | Principle | In practice |
| --- | --- | --- |
| P1 | Child-safe by construction | No free chat; every child-facing text passes constraints, validators and a safety layer; template fallback on any rejection |
| P2 | Parent in control | Consent per scope (voice processing, external content generation); session length and daily cap; export and delete |
| P3 | Arabic first, bilingual always | Modern Standard Arabic with full harakat; right-to-left everywhere; ar + en from the first screen |
| P4 | Explainable pedagogy | A parent can be told *why* a skill was chosen |
| P5 | Nothing unvalidated reaches a child | Generated content is cached only after validation; flagged items go to review |
| P6 | Recordings are ephemeral | Scored, then purged on a time-to-live; stored encrypted; never sent externally without consent |
| P7 | No dark patterns | No ads, no purchases in the child experience, no streak punishment; the child's progress view (a garden) only ever grows |
| P8 | Free to run, one operator | Caching, per-child daily caps, a cost model kept current |

# Scope and non-goals

## In scope for v1

- **Three domains** — reading, writing, arithmetic — for ages 4–8, as one skill graph with per-child
  entry points and age-band session shapes.
- **Nabta's voice is Modern Standard Arabic**, in short imperative sentences a four-year-old
  follows by ear; all child-facing text is fully diacritised.
- **The daily session** — child picker, greeting, warm-up review, one new skill, story, wrap-up —
  runs entirely from a pre-synced pack; results sync later.
- **Template activities** (letter-tap, letter-trace, syllable-blend, word-build, count-tap,
  number-trace, compare, add-objects, read-aloud) skinned in a few visual themes the child chooses
  between — the scheduler picks the skill, the child picks the skin.
- **Generated stories** of two kinds — letter-focus and review/value — written under constraints
  from a brief the scheduler produces, validated, safety-checked, cached; template stories while the
  child's letter set is still tiny.
- **Read-aloud assessment** with a confidence floor; **handwriting** scored on stroke order and
  direction with generous tolerance.
- **The child's progress view** is a garden: one plant per letter that grows as its sub-skills are
  mastered; nothing withers.
- **Parent surface**: onboarding with two separate consents, dashboard with the mastery map,
  "why this session today", the weekly report with a paper activity, and the **parent assistant**
  — questions about the child's learning answered from the pedagogy, the parent guide, the
  activity library and the child's state, with sources shown.
- **Operator surface**: curriculum and template editing, content review queue, evals, usage and caps.
- **Export or delete a child's data** on request.

## Non-goals — the safety scope of v1

Each of these is a decision, not an omission. They define what the product refuses to be.

| Non-goal | Why |
| --- | --- |
| No open-ended conversation with the child | Every child-facing text is constrained and validated (P1, P-3). The parent assistant is adult-facing only |
| No child accounts, no surname, no photo, no location | Children are data owned by a parent account, selected by a PIN (P2, P5) |
| No retained recordings, no voice data for training | Scored then purged (P6) |
| No leaderboards, no comparison between children, no social features | Motivation comes from the child's own garden, not from others |
| No ads, no purchases, no locked content visible to the child, no notifications addressed to the child | P7 |
| No streak that can be lost | Days missed are never punished; the garden only grows |
| No dialect voice in v1 | One consistent MSA voice; dialect-aware speech is a Phase 12 question |
| No generated illustrations or video in v1 | Studied in C3; decided after the experiment |
| No English track, no teacher mode, no sibling play | Phase 12 |
| No parent free text sent to any model about the child | Only nickname, age band, interests and cast names ever leave the device, and only with consent |

## Deferred — studied, then decided

Story illustrations (C3), live read-aloud feedback versus batch scoring (B4), fine-tuning versus
prompting (A5), on-device versus hosted inference per component (E3). Each has an experiment and
enters v1 only through an ADR.

# Success — four horizons

| Horizon | Who | Target | Stop criterion |
| --- | --- | --- | --- |
| **Study** (Phases 1–5) | The developer | Every open component in PLAN §8.1 has an ADR backed by a measured experiment; the developer can explain each choice from first principles; Checkpoints A–E passed from memory | An experiment that cannot be run on a solo budget is reported as *not run*, never faked |
| **Stage 0 — family test** (from Phase 7) | The developer's own children | The child completes sessions without help (G1) for two weeks; the parent can answer "why this skill today" from the app (G8); no goal in the table above is visibly violated | A child refuses sessions for a week, or any child-facing text outside the letter set reaches the screen |
| **Pilot** (Phase 11) | 10 families | ≥ 4 sessions/week for 8 weeks; measurable gain on a letter-sound and decoding pre/post test on unseen material (G14); median session completion ≥ 80 % | No measurable gain over the control expectation, or any safety incident |
| **Product** | Public | 1,000 active children within 6 months of publish; median session completion ≥ 80 %; cost per child-day under the E3 ceiling | Cost per child-day exceeds the ceiling for a month |

Stage 0 is new relative to the master plan: the first users are the developer's own children.
Every rule about children's data applies to them exactly as to anyone else's — their recordings are
purged, their profiles hold no surname, and nothing about them enters the lab.

# Operating model

- **One developer**, who is also the curriculum author, the native-speaker rater of Arabic quality,
  and the first parent.
- **Study first.** Phases 0–5 produce documents, experiments and decision records; no product code
  is written until every component in PLAN §8.1 has an ADR.
- **One roadmap step = one commit = one learning note.** Every commit is reviewed by the developer
  before it lands — the diff is part of the lesson.
- **Cheap to run.** One deployable; caching, per-child caps and a cost model kept current; a
  provider that is free to the developer is still measured beside an alternative and priced at
  list price.
- **Documents are part of the product.** This charter, the pedagogy, the requirements and the
  study log grow with every phase and render to Word from Markdown.

# Decisions taken so far (product, not technology)

| ID | Decision | Where recorded |
| --- | --- | --- |
| P-1 … P-7 | One operator, Arabic-first with harakat, no open chat with the child, explainable pedagogy, data minimisation, the way of working, local git until the pilot | PLAN §8.2 |
| D-2026-09-21-1 | Nabta's spoken voice is MSA, not dialect | This charter, §Scope |
| D-2026-09-21-2 | Age range stays 4–8; the session shape adapts by age band | This charter, §Users |
| D-2026-09-21-3 | The child's progress view is a garden that only grows; letters grow in stages as sub-skills are mastered | This charter, §Principles P7; pedagogy v0.1 |
| D-2026-09-21-4 | Two story kinds (letter-focus, review/value from a fixed list); template stories while the letter set is small | Pedagogy v0.1 |
| D-2026-09-21-5 | The parent assistant (UC-11) is in v1 scope, adult-facing, grounded, with sources | PLAN §2, this charter |
| D-2026-09-21-6 | Generated illustrations and video are out of v1; decided after C3 | PLAN §3.4, this charter |
| D-2026-09-21-7 | Stage 0 of the pilot is the developer's own children | This charter, §Success |

# Risks

| # | Risk | Likelihood | Impact | Mitigation | Tested in |
| --- | --- | --- | --- | --- | --- |
| R1 | No speech engine hears a five-year-old read Arabic well enough | High | Read-aloud evidence collapses; the learner model runs on touch and tracing only | G10 already tolerates it; an early spike before Phase 1 with the developer's own voice and consented adult recordings; design the evidence model so read-aloud is additive | B2, B3 |
| R2 | Constrained story generation fails on small letter sets | High | The first weeks have no generated story | Template stories with slots until ~6 letters; validator-driven repair loop | A3 |
| R3 | Nightly pack versus today's frontier (G12 vs G2) | Certain | A pre-generated story can fall outside the child's letter set after a bad warm-up | Decide before Phase 8 between spare stories, freezing the letter set before warm-up, or stories below ability never above | E5, Phase 8 |
| R4 | A phone is too small for a child's tracing hand | High | Writing track needs a tablet or landscape phone | Recorded as a device requirement in the SRS; measured in the stroke-capture spike | C1, E5 |
| R5 | Cost per child-day exceeds what one operator can carry | Medium | Product is not free to run | Caching, batch generation, per-child caps, list-price cost model from the first experiment | E3, E4 |
| R6 | Graded Arabic word lists for ages 4–8 do not exist ready-made | Certain | Curriculum data must be built by hand | First 20 nodes and 50 words by hand in 0.4; the authoring agent (A7) extends them under review | 0.4, A7 |
| R7 | MSA instructions are not understood by the youngest children | Medium | G1 fails for four-year-olds | Short imperative sentences, audio-first, tested on the developer's own children in Stage 0 | Stage 0 |
| R8 | Children's-data law (KSA PDPL, COPPA-style rules) constrains what leaves the device | Medium | Rework of the data flow | Data-flow map and minimisation in E2; consent per scope from onboarding | E2, Phase 10 |
| R9 | A hosted provider changes price or terms | Medium | Cost model breaks | Providers are configuration behind one port; every ADR names its revisit trigger | E3, E5 |
| R10 | One developer's time — the study is ~32 steps before product code | High | Motivation and momentum | One step per sitting; checkpoints as milestones; the design prototype keeps the destination visible | Every step |

# Roadmap summary

| Phase | Outcome |
| --- | --- |
| 0 | Repo, plan, this charter, pedagogy v0.1 with the skill-graph seed, SRS v0.1, capability architecture |
| 1 | Study — AI foundations: tokens, models, constrained generation, retrieval and the parent assistant, fine-tuning, evals, the authoring agent |
| 2 | Study — Speech: synthesis with harakat, recognition of child speech, reading assessment and the confidence floor, latency |
| 3 | Study — Vision and handwriting: strokes versus pixels, vision models as judges, story illustrations (decision) |
| 4 | Study — Adaptive learning: knowledge tracing, spaced repetition, the deterministic scheduler, H1 versus H2 |
| 5 | Study — Safety, data, deployment, cost → one ADR per component → the stack decision |
| 6–9 | Build — tutor core, child experience, content and speech, parent and operator surfaces |
| 10 | Hardening and child safety |
| 11 | Pilot with 10 families, then publish |
| 12 | Toward the Primer: long-term memory, comprehension dialogues, English, dialects, classrooms |

Full detail: [ROADMAP.md](../../ROADMAP.md).

# Appendix — the interaction prototype {.unnumbered}

A clickable design prototype of the child and parent screens (thirteen screens: picker, garden,
letter-tap with its hint ladder, tracing, story with read-aloud, the "no evidence" moment,
wrap-up; onboarding, dashboard with the mastery map, "why this session", weekly report, data and
privacy) was built on 2026-09-21 and lives outside the repo as a private design canvas. It is
interaction design, not a platform choice; the platform is decided in Phase 5.
