# Curriculum data

The skill graph is data, not code: `skills.v<version>.json`. The pedagogy document
(`docs/deliverables/pedagogy.md`) explains it in prose; the two change together.
`lab/0.4-skill-graph/check_graph.py` expands and validates a file and prints its frontier.

## Shape of the file

| Key | What |
| --- | --- |
| `domains` | `R` reading, `W` writing, `A` arithmetic |
| `bands` | `KG` (4–5), `G1` (6–7), `G2` (7–8) — where a skill typically appears; not a gate |
| `stages` | Named groups of skills per domain (`r-letters`, `r-harakat`, …) with an `order`. **A label for parents and progress views, never an ordering mechanism** — prerequisites are |
| `letters` | The 28 letters with a Unicode name (`MEEM`), the Arabic name, whether it joins, and `order` — the default introduction sequence (simple and frequent first, confusable pairs never adjacent). The scheduler pulls the child's name letters forward |
| `mastery_rules` | Named rules a skill points at: `standard` 4-of-5 over ≥ 2 sessions, `quick` and `concept` 3-of-4 over ≥ 1. Placeholders until Phase 4 chooses the learner model; the status labels views read (not-started / learning / mastered) survive that change |
| `activities` | The tier-1 template catalogue (codes, modality, parameter names) and the two tier-2 generated kinds |
| `per_letter` | **Skill templates instantiated once per letter.** Nine kinds × 28 letters = 252 nodes from nine entries. Names use `{ar}` / `{glyph}` placeholders |
| `skills` | Single concrete nodes: concepts, discrimination pairs, words, sentences, pre-writing, arithmetic |

## Codes

- ASCII, upper case, dash-separated: `R-L-SOUND-MEEM`, `R-DISC-BEH-TEH`, `A-ADD-10`.
  Letters are named by their Unicode names, never by the glyph, so codes survive file names,
  URLs, consoles and regular expressions.
- **Stable forever.** Thousands of `SkillMastery` rows will point at them. A skill that is no
  longer right gets `"status": "deprecated"`; it is never renamed or deleted.
- Per-letter codes are `<KIND>-<LETTER>`; the kind is what `any_of_kind` refers to.

## Prerequisites — three forms

| Form | Meaning | Example |
| --- | --- | --- |
| `"CODE"` | that exact node | `"R-SK-CONCEPT"` |
| `"KIND@same"` | this letter's node of that kind (per-letter kinds only) | `"R-L-SHAPE@same"` in `R-L-SOUND` |
| `{"any_of_kind": KIND, "min": n}` | at least *n* nodes of that kind mastered, any letters | the fatha concept unlocks after 3 letter sounds |

The third form is what keeps the graph honest about how children learn: a concept is taught
once, on whichever letters the child happens to know, and then every letter gets a quick
sub-skill for it.

## Adding a skill

1. Add the node (or per-letter kind) with code, domain, stage, band, name ar/en, prerequisites,
   mastery rule, activities, scope.
2. Run `python lab/0.4-skill-graph/check_graph.py` — it must print `RESULT: well-formed`.
3. Add content items whose letter set the new scope needs (from step 0.4b onward).
4. Bump the file version only when codes or semantics change, not when nodes are added.

No code is written per letter or per skill; templates are parameterised by scope, so a new
node is picked up automatically.
