---
title: "Nabta — Curriculum & Learning-Model Design"
subtitle: "نبتة — تصميم المنهج ونموذج التعلّم"
author: "Abdulsalam"
version: "0.1"
date: "2026-09-21"
status: "Draft"
---

## Revision history {.unnumbered}

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 0.1 | 2026-09-21 | Abdulsalam | First version: skill model, letter sequence, session shape, scheduler rules, assessment, activity catalogue, generated content, the garden, glossary. Matches `docs/curriculum/skills.v0.1.json` |

# Purpose and scope

This document is the pedagogy of Nabta: what is taught, in what order, how a session is shaped,
how evidence becomes mastery, and how the next session is chosen. It is written so that a
scheduler can execute it and a parent can be told why. It has a twin: the skill graph in
[`docs/curriculum/skills.v0.1.json`](../curriculum/skills.v0.1.json) — the data this prose
explains. **The two change together**; a rule stated here without a field there, or a node there
without a sentence here, is a defect. Scheduler parameters that the rules below cite by name
(review intervals, the confusion trigger, the value list, session limits) live in the file's
`policy` block for the same reason.

What this version does not decide: the learner-model algorithm (how evidence becomes a mastery
estimate) and the review-scheduling algorithm. Both are studied and chosen in Phase 4; every
place that depends on them is marked *Planned* and carries the v0.1 placeholder rule instead.

::: {custom-style="RTL"}
**الملخص.** هذه الوثيقة هي «تربية» نبتة: ماذا يُعلَّم، بأيّ ترتيب، كيف تُشكَّل الجلسة، كيف تتحوّل
الإجابات إلى إتقان، وكيف تُختار الجلسة التالية. كُتبت بحيث ينفّذها مجدول ويُشرح للوالد ما فعلته.
توأمها ملف المهارات `skills.v0.1.json`؛ لا يتغيّر أحدهما دون الآخر. ما لم يُحسم بعد — خوارزمية
نموذج المتعلّم وجدولة المراجعة — يُدرَس في المرحلة الرابعة، ومواضعه هنا معلَّمة بـ *Planned*.
:::

# Principles of the pedagogy

1. **Mastery learning.** A child moves to a skill only when its prerequisites are mastered, and
   "mastered" is a stated criterion, not a feeling (§ Mastery criteria).
2. **The edge of ability.** Every session teaches one new skill from the *frontier* — skills
   whose prerequisites are all mastered but which are not yet mastered themselves. In the
   learning-science literature this is the *zone of proximal development*: what a child can do
   with help today and alone tomorrow. The frontier is computed from the graph; it is never a
   position in a list.
3. **Explainable by construction.** Every activity in a session plan carries a structured
   reason produced *by* the decision that chose it (§ Scheduler rules, R12). The sentence the
   parent reads is the reason, rendered.
4. **Evidence, not judgement.** Touch answers are exact evidence; read-aloud is evidence only
   above a confidence floor; handwriting is motor practice scored generously. Nothing lowers a
   mastery estimate because a microphone heard mumbling (vision G10).
5. **No failure state.** Every activity is solvable through a hint ladder; a wrong tap changes
   nothing on screen except Nabta's next sentence; sessions end on time and on a success (G3, G4).
6. **Diagnose, don't repeat.** Repeated confusion between two letters is a *skill* with its own
   node (`R-DISC-*`), answered with a different activity and spacing, never the same drill louder
   (G11).
7. **The child chooses the skin, the tutor chooses the skill.** Template activities come in a
   few visual themes; agency without loss of control.

# Domains and stages

Three domains, nineteen stages. A **stage** is a named group of skills used for progress views
and for the parent's sentence "she is in the harakat stage"; it never orders instruction —
prerequisites do (§ The skill model).

## Reading (R)

| Stage | Name | What mastering it means | Typical band |
| --- | --- | --- | --- |
| `r-letters` | الحروف | Recognises each letter's isolated shape and links it to its sound; tells confusable pairs apart | KG |
| `r-harakat` | الحركات | Reads a letter with fatha, kasra, damma as a syllable (مَ مِ مُ) | KG |
| `r-long-vowels` | المدود والسكون | Reads long vowels (مَا مِي مُو), sukoon, shadda, tanween | KG → G1 |
| `r-forms` | أشكال الحرف واتصاله | Recognises letters in initial, medial and final position inside words | G1 |
| `r-words` | الكلمات | Blends syllables into words; taa marbuta, alef maqsura, hamza, the definite article; sight words | G1 |
| `r-sentences` | الجمل | Reads two-, three- and five-word sentences | G1 |
| `r-passages` | النصوص القصيرة والفهم | Reads a three-sentence passage; answers literal and inferential questions | G2 |

## Writing (W)

| Stage | Name | What mastering it means | Typical band |
| --- | --- | --- | --- |
| `w-pre` | ما قبل الكتابة | Controls straight, curved, looped and zigzag strokes | KG |
| `w-letters` | كتابة الحروف | Traces a letter with correct stroke order; writes it from its sound; writes harakat on it | KG → G1 |
| `w-words` | كتابة الكلمات | Writes letters joined; copies a word | G1 |
| `w-dictation` | الإملاء | Writes a word, then a short sentence, from dictation | G1 → G2 |

## Arithmetic (A)

| Stage | Name | What mastering it means | Typical band |
| --- | --- | --- | --- |
| `a-count` | العدّ | One-to-one counting to 5, then to 10 | KG |
| `a-numerals` | الأرقام | Recognises, traces and writes 0–9 (Eastern or Western per the child's setting) | KG |
| `a-compare` | المقارنة والترتيب | More/fewer with objects, then numerals; orders 0–10 | KG |
| `a-bonds` | تركيب الأعداد | Number bonds of 5 and 10 | G1 |
| `a-add-sub-10` | الجمع والطرح ضمن ١٠ | Adds and subtracts within 5, then 10 | G1 |
| `a-to-20` | الأعداد حتى ٢٠ | Counts and reads 11–20, tens and ones, adds and subtracts within 20 | G1 |
| `a-to-100` | الأعداد حتى ١٠٠ | Numbers to 100; skip counting by 2, 5, 10 | G2 |
| `a-problems` | المسائل اللفظية | Personalised word problems, read aloud by Nabta, add then subtract | G1 → G2 |

Bands (`KG` 4–5, `G1` 6–7, `G2` 7–8) say where a skill *typically* appears. They are not gates:
a five-year-old who reaches `r-words` reads words.

# The skill model

## Anatomy of a skill

Every node has: a **code** (stable, ASCII), a **domain**, a **stage**, a **band**, a **name** in
Arabic and English, **prerequisites**, a **mastery rule** (by name), the **activities** that can
teach or test it, and a **content scope** — which letters, harakat, forms, word lists or number
ranges it may use. Example, as it appears after expansion:

```json
{ "code": "R-H-FATHA-MEEM", "domain": "R", "stage": "r-harakat", "band": "KG",
  "name": { "ar": "الميم بالفتحة", "en": "م with fatha" },
  "prerequisites": ["R-L-SOUND-MEEM", "R-H-FATHA-CONCEPT"],
  "mastery": "quick", "quick": true,
  "activities": ["syllable-blend", "sound-match"],
  "scope": { "letters": ["م"], "harakat": ["fatha"] } }
```

The scope is what a template activity is parameterised from: `syllable-blend` with this node
shows مَ, plays its sound, and asks the child to pick it among مِ and مُ once those exist.

## Per-letter kinds and how a letter grows

Nine skill *kinds* exist once per letter; the file lists each kind once and the checker expands it
across the 28 letters (9 × 28 = 252 nodes). Read top to bottom, they are the growth of one
letter — and the growth the child sees in her garden (§ The progress view):

| Kind | The child can… | Garden |
| --- | --- | --- |
| `R-L-SHAPE-<L>` | recognise the isolated shape among neighbours in the sequence | a sprout with a small tag |
| `R-L-SOUND-<L>` | tap the letter when its sound is played | a bud with the letter |
| `R-H-FATHA-<L>` · `R-H-KASRA-<L>` · `R-H-DAMMA-<L>` | read the syllable مَ / مِ / مُ | two petals open per haraka |
| `R-F-JOIN-<L>` | find the letter in initial, medial and final position in a word | the flower's centre fills |
| `W-TRACE-<L>` | trace the letter with correct stroke order | — (writing track, shown as a leaf) |
| `W-WRITE-SOUND-<L>` | write the letter from its sound, no guide | — |
| `W-JOIN-<L>` | write the letter joined in a word | — |

Kinds marked `quick` in the file use the lighter mastery rule and may be scheduled several to a
session once their concept is known (§ Scheduler rules, R4).

## Concepts and threshold prerequisites

Some things are taught once, on whatever letters the child happens to know: the fatha, the
kasra, the damma, each long vowel, sukoon, shadda, tanween, and the fact that letters join.
These are **concept nodes** whose prerequisite is a *threshold*:

```json
"prerequisites": [ { "any_of_kind": "R-L-SOUND", "min": 3 } ]
```

"At least three letter sounds, any letters." After the concept is mastered, every letter's quick
sub-skill for it unlocks as that letter's own sound is mastered. This is what makes "harakat are
sub-skills of the letter" affordable: one concept, then 28 quick nodes, instead of 28 slow ones.

## Discrimination pairs

Fifteen pairs differ by dots or by a single feature and are confused for months: ب/ت، ت/ث،
ب/ن، ت/ن، ن/ي، د/ر، ج/ح، ح/خ، د/ذ، ر/ز، س/ش، ص/ض، ط/ظ، ع/غ، ف/ق. Each is a node
(`R-DISC-BEH-TEH` …) whose prerequisites are the two sounds, taught with `letter-tap` restricted
to the pair and with `dot-count`. A pair node also gets scheduled early when the evidence log
shows the child choosing one member for the other (§ Scheduler rules, R9).

## Prerequisite forms

| Form | Meaning |
| --- | --- |
| `"CODE"` | that exact node |
| `"KIND@same"` | this letter's node of that kind (per-letter kinds only) |
| `{"any_of_kind": KIND, "min": n}` | at least *n* nodes of that kind mastered, any letters |

## Codes and versions

Codes are ASCII, upper case, dash-separated, with letters named by their Unicode names
(`MEEM`, `BEH`) — never by the glyph, so they survive file names, URLs and consoles. Codes are
**stable forever**: thousands of `SkillMastery` rows will point at them; a skill that is no longer
right is marked `deprecated`, never renamed. The file version changes when codes or semantics
change, not when nodes are added.

## Mastery criteria (v0.1 placeholder)

| Rule | Criterion | Used by |
| --- | --- | --- |
| `standard` | 4 correct of the last 5 attempts, across ≥ 2 sessions | shapes, sounds, pairs, words, sentences, arithmetic |
| `quick` | 3 of the last 4, across ≥ 1 session | per-letter harakat, joining, tracing, writing |
| `concept` | 3 of the last 4, across ≥ 1 session | concept nodes |

Only attempts that count as evidence enter the window (§ Assessment rules). Each (child, skill)
pair has a **status** — `not-started`, `learning`, `mastered` — and it is the status, not the
rule, that the garden, the parent's grid and the scheduler read. *Planned (Phase 4):* the rule is
replaced by a probabilistic estimate (Bayesian Knowledge Tracing is the working candidate) and a
retention state for reviews; the statuses and the codes do not change.

## Size and validation

v0.1 is 85 authored entries (9 per-letter kinds + 76 single nodes) that expand to **328 nodes**
(reading 210, writing 92, arithmetic 26) with 892 prerequisite edges, no cycles, and a longest
chain of 13 steps from a letter's shape to inferential comprehension. The checker
`lab/0.4-skill-graph/check_graph.py` proves this on every change and prints the frontier; a
graph that fails it does not ship.

# The letter sequence

The graph decides eligibility, not order: a new child is eligible for all 28 letter shapes at
once. Order is the scheduler's, and it starts from the default sequence in the file:

| # | Letters | Why here |
| --- | --- | --- |
| 1–5 | ا م س ب ل | Simple shapes, frequent, visually distinct from each other; enough for the first syllables and the first template stories |
| 6–11 | د ن ر ت و ي | Completes a kernel of eleven letters; ت is kept away from ب and ن, د from ر |
| 12–16 | ك ف ح ع ج | Frequent letters with new shapes; ج is separated from ح by ع |
| 17–22 | ص ق ش خ ط ه | Second members of pairs arrive after their partners have settled |
| 23–28 | ز ذ ث ض غ ظ | Rarest letters and the last members of confusable pairs |

Two rules modify it per child: **the child's name letters come first** (R2) — it is the one
word every child wants to read, and it makes the garden personal from day one — and **no
confusable pair is introduced back to back** (R3). Neither changes the file; both are scheduler
behaviour, which is why the sequence is data and the rules are prose.

# Session shape

Default 10 minutes; the parent sets 5–15. The five phases are fixed; their lengths and modality
mix follow the age band. Nabta speaks Modern Standard Arabic in short imperative sentences; no
phase requires the child to read an instruction.

| Phase | KG (4–5) | G1 (6–7) | G2 (7–8) | What happens |
| --- | --- | --- | --- | --- |
| Greeting | 0.5 min | 0.5 | 0.5 | The garden, one seed if a skill was mastered last time, «نَلْعَب؟» |
| Warm-up review | 2 | 3 | 3 | Due reviews first (R1); touch-heavy; ends on a correct answer |
| New skill | 4 | 4 | 4 | One frontier skill (R4); the child picks the skin (R11); hint ladder on misses |
| Story | 2 (template) | 2.5 | 3 | Letter-focus or review story; listen, then read aloud if the band and consent allow |
| Goodbye | 0.5 | 0.5 | 0.5 | The success event (R7): a plant grows, «إِلَى الْغَد» |

Per band: KG sessions are touch-first and may skip read-aloud entirely; G1 adds read-aloud and
tracing every session; G2 adds dictation and comprehension. The daily cap is one session unless
the parent allows two.

# Scheduler rules

The rules any scheduler must honour, numbered so tests and reasons can cite them. Inputs: the
graph, the child's statuses and evidence log, the review state, the parent's settings, today's
date. Output: an ordered session plan whose every activity carries a reason (R12).

| # | Rule |
| --- | --- |
| R1 | **Reviews before new material.** Every skill whose review is due today is scheduled in warm-up, most overdue first, up to the warm-up budget. *Planned:* the review interval comes from the Phase 4 spaced-repetition algorithm; v0.1 uses the fixed intervals in `policy.review_intervals_days` — 1, 3, 7, 14, 30 days after mastery. |
| R2 | **Name letters first.** Among frontier letter skills, letters in the child's nickname precede the default sequence. |
| R3 | **Confusable pairs never adjacent.** The second member of a pair is not introduced in the session after the first; at least two other letters intervene. |
| R4 | **One new standard skill per session**, from the frontier, in the phase "New skill". Up to `policy.quick_per_session_max` (three) `quick` nodes may be added in the same session once their concept is mastered, and they count as follow-ups, not as the new skill. |
| R5 | **Interleave domains.** Every session has reading; every second session adds writing or arithmetic; no session has three domains in the new-skill phase. |
| R6 | **Scaffold, then switch.** Two consecutive misses on an activity → next hint-ladder level; three → switch to another activity for the same skill, or offer a break; never a fourth attempt of the same item. |
| R7 | **End on time and on a success.** The plan fits the parent's limit at the 95th percentile of activity durations; the last activity is one the child has mastered; if time runs out, the new skill is dropped before the goodbye is. |
| R8 | **Low confidence is no evidence.** Read-aloud attempts below the confidence floor are not scheduled around, not counted in mastery windows, and not shown as errors (R6 does not count them as misses). |
| R9 | **Confusion is a diagnosis.** When the evidence log shows a child choosing letter *y* for letter *x* in ≥ 3 of the last 6 attempts on either (`policy.confusion_trigger`), the pair node `R-DISC-x-y` is pulled to the front of the frontier and the two letters are spaced apart in reviews. |
| R10 | **Story last, inside the letter set.** The story brief uses only mastered letters and harakat (plus the session's new letter if it was mastered in-session for a letter-focus story); if no validated story fits, a template story or a read-aloud of known words takes its place — never a story above ability. |
| R11 | **The child chooses the skin.** For the new-skill activity, two skins of the same template are offered by picture; evidence is recorded on the skill, never on the skin. |
| R12 | **Every activity carries a reason** (§ Explainability). |
| R13 | **Deterministic.** Same inputs → same plan. Randomness (skin order, item order) is seeded from the session id. |
| R14 | **Offline.** The plan and its content are built into a pack before the session; a session never waits for a network call. |

# Explainability — the reason contract

A reason is produced *by* the rule that chose the activity and rendered to the parent later. It
is data:

```json
{ "kind": "review-due" | "frontier-new" | "quick-followup" | "remediation-confusion" | "story",
  "rule": "R1",
  "cause": { "skill": "R-L-SOUND-SEEN", "mastered_at": "2026-09-15", "interval_days": 7 },
  "text": { "ar": "تعلّمت صوت السين قبل ستة أيام، واليوم موعد مراجعته قبل أن يبدأ النسيان.",
            "en": "She learned the sound of س six days ago; today is its review before forgetting sets in." } }
```

| Kind | Cause carries | Rendered sentence (ar) |
| --- | --- | --- |
| `review-due` | the skill, when it was mastered, the interval | «تعلّمت صوت السين قبل ستة أيام، واليوم موعد مراجعته.» |
| `frontier-new` | the prerequisites that unlocked it | «أتقنت شكل الميم، فاليوم نتعلّم صوتها.» / «أتقنت صوت ثلاثة حروف، فاليوم نبدأ الفتحة.» |
| `quick-followup` | the concept and the letter | «تعرف الفتحة وصوت الباء، فاليوم «بَ».» |
| `remediation-confusion` | the pair and the counts | «خلطت بين ن و ت في ٦ من ٩ محاولات؛ اليوم نشاط يميّز النقاط.» |
| `story` | the letter set size and the kind | «قصة بحروفها الإحدى عشرة، لتقرأ شيئًا كاملًا بنفسها.» |

The parent's screen "Why this session today?" is these objects rendered in order, plus the count
of attempts that were *not* counted (R8) — «٣ محاولات صوتية لم تُحسب معها ولا ضدّها».

# Adaptation levers

| Lever | What changes | Driven by |
| --- | --- | --- |
| Difficulty | which skill (frontier vs review), distractor closeness | statuses, evidence log |
| Pace | repetitions per item, quick nodes per session (0–3) | recent accuracy, response times |
| Modality | touch-only vs voice vs stroke | age band, consent, R8 events (switch to touch) |
| Interest | skin, story cast and theme | profile interests, the child's skin choices |
| Scaffolding | hint ladder: replay → highlight → reveal | R6 |
| Affect | Nabta's sentence, break offer, session length | misses in a row, time of day, R7 |

# Assessment rules

- **Touch answers are exact.** Correct or not; the tapped distractor is recorded (it feeds R9).
- **Read-aloud yields per-word evidence** with a confidence score. Below the **confidence
  floor** nothing is recorded — not right, not wrong. *Planned:* the floor is the number
  experiment B3 finds, per engine. Above it, a matched word is evidence for every skill the word
  exercises (its letters' sounds, its harakat, its word-stage skill).
- **Handwriting is scored on stroke order, direction and approximate shape** with generous
  tolerance; it is motor practice, not grading. A trace that starts at the right point and moves
  in the right direction passes even if wobbly. *Planned:* tolerance values from C1.
- **Evidence weight.** In v0.1 every counted attempt weighs the same in the k-of-n window.
  *Planned (Phase 4):* per-modality slip and guess parameters.
- **Recordings are scored, then purged** within their time-to-live; the evidence row keeps the
  per-word result, never the audio.

# Activity catalogue — tier 1 templates

Templates are parameterised from the skill's scope and the learner's state; they are instant,
safe and offline, and make up most of a session. Each exists in a few **skins** (themes) that
change pictures and sounds, never the mechanic.

| Code | The child… | Parameters | Evidence | Modality |
| --- | --- | --- | --- | --- |
| `letter-tap` | taps the target letter among distractors — by shape, by sound, or inside a word | target, distractors, mode | correct + which distractor | touch |
| `sound-match` | hears a sound and picks the letter (or hears a letter and picks its syllable) | letter, options | correct | audio + touch |
| `dot-count` | counts the dots on a letter and picks the match (pair discrimination) | pair | correct | touch |
| `syllable-blend` | drags a haraka onto a letter and hears the syllable; then picks the syllable heard | letter, haraka | correct | audio + touch |
| `word-build` | assembles a word from letter tiles in order | word, letters | correct, order errors | touch |
| `sight-word-tap` | taps the sight word among look-alikes | word, distractors | correct | touch |
| `read-aloud` | reads a word, sentence or story into the microphone | text | per-word match + confidence | voice |
| `letter-trace` | follows numbered dots to trace a letter (or a pre-writing stroke) | letter, form, guide | stroke order, direction, shape | stroke |
| `letter-write` | writes the letter from its sound with no guide | letter | as above, stricter | stroke |
| `word-copy` | copies a word shown above the canvas | word | per-letter join | stroke |
| `dictation` | writes what Nabta says | text | per-letter, harakat | audio + stroke |
| `count-tap` | taps objects one by one while Nabta counts, or taps the numeral for a count | n, objects | correct | touch |
| `number-trace` / `number-write` | traces, then writes, a numeral | numeral | stroke score | stroke |
| `compare` | picks the group with more / fewer, or the larger numeral | a, b, mode | correct | touch |
| `order-tap` | taps numbers in ascending order | numbers | correct, first error | touch |
| `add-objects` / `sub-objects` | combines or removes objects and picks the total | a, b | correct | touch |

# Generated content — tier 2

## Two story kinds

| Kind | Purpose | Extra constraint | When |
| --- | --- | --- | --- |
| **Letter-focus** | fix the sound of a newly mastered letter | the target letter appears ≥ 4 times | the session after a letter's sound is mastered |
| **Review / value** | fluency, joy, and one value from a fixed list | the value is chosen from the closed list `policy.story_values` (يشارك، يصدق، يساعد، يعتذر، يصبر) — never free text | when there is no new letter, or alternating |

## The brief

The scheduler writes the brief; the model never chooses its own constraints and the parent
never types free text into it.

```json
{ "purpose": "letter_focus", "target": "س", "min_target_count": 4,
  "allowed_letters": ["ا","ب","ت","م","ن","س","ل","د","ر","و","ي"],
  "allowed_harakat": ["fatha","kasra","damma","sukoon"],
  "cast": { "hero": "ماسة", "others": ["سامي","توت"] }, "interests": ["قطط"],
  "value": null, "length": { "sentences": 3, "max_words": 12 } }
```

Validators run after generation, in order: letters ⊆ allowed · harakat ⊆ allowed and complete
on every letter · target count · length · the hero is present · no word on the blocked list · the
safety layer. Any failure → one repair round with the failure named, then fallback (R10). A
story is cached with its status only after every validator passes.

::: {custom-style="ChildText"}
مَاسَة تُنَادِي تُوت.

تُوت لَا يَرُدّ.

تُوت نَامَ!
:::

Eleven letters, three sentences, the hero and her cat: the first story ماسة read in the charter.

## Template stories

Under about six mastered letters, generation is nearly impossible (experiment A3 measures where
the line is). Until then, **template stories** — hand-written, with slots for the hero and a cast
member, each tagged with the letter set it needs — take the story phase. They are content items,
authored under review like everything else.

## Word problems

A brief with numbers instead of letters: operation, range, the cast, the objects. Numbers in the
generated text are **re-parsed and checked against the brief** before the problem is used; the
child hears the problem read aloud and answers by touch, so no reading skill is required.

# The progress view — the garden

The child never sees a table. Her home screen is a garden, and it is a *view* over the same
(child, skill) statuses the parent sees as a grid:

| Status of a letter's nodes | Garden |
| --- | --- |
| nothing started | nothing — no empty slot, no grey outline |
| `R-L-SHAPE` mastered | a sprout with the letter on a small tag |
| `R-L-SOUND` mastered | a bud showing the letter |
| each of fatha / kasra / damma mastered | two petals open (six for all three) |
| `R-F-JOIN` mastered | the centre fills |
| a skill mastered in the last session | a seed to plant at the next greeting |

The garden **only grows** (P7): nothing withers on a missed day, and there is no streak to lose.
Writing progress appears as leaves on the stem; arithmetic as a small vegetable patch beside the
flowers. However many nodes the graph has, the garden shows at most 28 flowers.

# Content items and word lists *(Planned)*

The activities and briefs above draw on **content items**: letters with their forms, syllables,
words with full harakat, sight words, numbers, and template stories. Each word item stores its
harakat and its **derived** letter set (`decompose("مَاسَة") → م ا س ة`) — the same function that
validates generated stories. Graded word lists for ages 4–8 do not exist ready-made; the first
fifty words are authored by hand in the next steps, and the curriculum authoring agent
(experiment A7) extends them under review. Format and counts: *Planned*.

# Learner model *(Planned — Phase 4)*

Per (child, skill): a mastery estimate updated from counted evidence, and a retention state that
schedules reviews. Candidates studied in Phase 4: Bayesian Knowledge Tracing, Item Response
Theory / Elo, Deep Knowledge Tracing (read only), SM-2 / FSRS. The contract this document fixes
now: statuses `not-started` / `learning` / `mastered`; a mastery estimate that never decreases
from a below-floor attempt; a review interval per mastered skill; and the H1 hypothesis — the
graph, the learner model and a deterministic scheduler decide *what*, the language model only
*writes*.

# Open questions for Phase 4 and Stage 0

1. Is three letter sounds the right threshold for the fatha concept, or should the concept wait
   for the child's name letters? (Stage 0.)
2. Do KG children need read-aloud at all, or is touch evidence enough until G1? (B2, Stage 0.)
3. How many quick nodes per session before fatigue shows? (D6, Stage 0.)
4. Where is the confidence floor per engine? (B3.)
5. What review load does the v0.1 interval table produce at 60 and 120 days? (D5.)
6. Does the name-letters entry point help motivation enough to justify a non-standard first
   syllable set? (Stage 0.)

# Glossary

| Arabic | English | Meaning here |
| --- | --- | --- |
| مهارة | skill | a node in the graph: something a child can do, with a code and a mastery criterion |
| متطلّب | prerequisite | a skill that must be mastered first |
| الجبهة | frontier | skills whose prerequisites are all mastered and which are not yet mastered |
| مرحلة | stage | a named group of skills used for progress views; never an ordering mechanism |
| مجموعة الحرف | letter group | all nodes about one letter; what a flower in the garden represents |
| مهارة سريعة | quick skill | a per-letter sub-skill with the lighter mastery rule |
| مفهوم | concept node | a skill taught once, unlocked by a threshold of other skills |
| زوج التباس | confusable pair | two letters told apart by a dedicated skill (`R-DISC-*`) |
| الحركات | harakat | short-vowel marks: فتحة، كسرة، ضمة؛ plus سكون، شدّة، تنوين |
| المدّ | long vowel | ا ي و lengthening a vowel: مَا مِي مُو |
| معيار الإتقان | mastery criterion | the stated rule that turns evidence into `mastered` |
| الدليل | evidence | a counted attempt; read-aloud below the confidence floor is not evidence |
| عتبة الثقة | confidence floor | the recognition confidence below which nothing is recorded |
| سُلّم المساعدة | hint ladder | replay → highlight → reveal |
| القِشرة | skin | a visual theme of a template activity; the child chooses it |
| طلب القصة | story brief | the scheduler's constraints for a generated story |
| قصة قالبية | template story | a hand-written story with slots, used while the letter set is small |
| الحديقة | garden | the child's progress view; a rendering of skill statuses that only grows |
| السبب | reason | the structured explanation attached to every planned activity |
| منطقة النموّ القريب | zone of proximal development | what a child can do with help today and alone tomorrow — the frontier |
