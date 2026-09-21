---
name: learn
description: Give a focused, first-principles explanation of one topic from the Nabta study plan (language models, tokens, prompting, embeddings, fine-tuning, evals, agents, speech synthesis and recognition, alignment, handwriting recognition, knowledge tracing, spaced repetition, guardrails, children's data, inference cost) anchored to this repo's notes and experiments. Use when the user invokes /learn <topic> or asks "explain X" while studying or building.
---

# learn

Teach one topic, from first principles, anchored to this repo, without writing product code.

## Procedure

1. **Scope the topic** to one idea. If the request is broad, pick the piece relevant to the
   current or next roadmap step and say so.
2. **Anchor it**: find where the topic already appears (or will appear) in this repo — a lab
   README, a learning note, an ADR, `docs/PLAN.md` §4, or code once it exists — and cite files
   and lines. If nothing exists yet, say which step will create it.
3. **Explain in this order**, briefly:
   - *What you already know that this maps to* — a general-programming idea (a hash map, a
     state machine, a probability you'd compute by hand, a cache), never a framework from an
     earlier project. Assume no AI background: define every term the first time it appears.
   - *The core idea* in ≤ 10 lines.
   - *A minimal example* in Nabta's terms (10–25 lines: a tiny calculation, a prompt and its
     constraint, a five-line simulation), runnable in the lab runtime where one exists.
   - *The trap* — the one mistake people make with it, and how this repo's guardrails or
     experiments avoid it.
   - *Check yourself* — one question, answer hidden behind `<details>`.
4. **Offer, don't do**: end with the roadmap step and the experiment where this will be
   measured. Do not modify product code or commit. If the user wants the explanation kept,
   save it as `docs/learning/topics/<slug>.md` and commit `learn(<slug>): <topic>`.

## Tone

Peer explaining at a whiteboard. No fluff, no history lessons, concrete over abstract,
numbers over adjectives.
