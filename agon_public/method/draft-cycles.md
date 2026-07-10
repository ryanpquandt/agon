# Draft cycles: the writing room, the return, and the altitude decision

Phase 6 is not a single polish funnel. It is a **loop over full drafts**. The
writer writes whole drafts alone; Agon contests them whole; and after each
draft the writer decides — agonistically, from a brief — *at what altitude* the
next round of work happens. Iterations may funnel down toward polish, or blow
the piece open and redirect it entirely. Both are the process working.

Two failure modes motivate the design:

- **Polishing the unproven.** Line-editing a draft whose thesis or structure is
  still wrong wastes the writer's effort and breeds attachment to prose that
  should die. The polish funnel is therefore *gated*: it opens only through an
  explicit `descend` decision, enforced by the engine.
- **The interrupted writer.** Mid-draft critique fragments composition and
  quietly shifts authorship — each interjection is a small taking-over of the
  writing. So while a draft is being written, **the writing room is closed.**

## The cycle

```
plan closed ──▶ WRITING ROOM (closed; the writer drafts alone)
                    │  full draft returned → drafts/draft-NN.md, logged
                    ▼
               THE RETURN (agonistic full-draft review)
                    │  editor reads the WHOLE draft against brief + outline + Γ;
                    │  objections verbatim, each with its demand; writer rules
                    ▼
               THE ALTITUDE DECISION (briefed, gated)
        ┌───────────┼──────────────┬───────────────┬──────────┐
        ▼           ▼              ▼               ▼          ▼
    redirect    restructure     rework          descend     ship
    (thesis/    (thesis holds;  (thesis+        (structure  (rare:
    direction   architecture    structure hold; sound —     done from
    changes →   doesn't →       paragraphs      enter the   review)
    reopen      revise outline, rewritten       polish
    conceive/   redraft)        wholecloth →    funnel,
    refine)                     new draft)      d1–d4)
```

Every arrow that isn't `descend`/`ship` returns to the writing room for another
**full draft** (`draft-02.md`, `draft-03.md`, …). Drafts are immutable — never
overwritten — so the record shows the piece's whole trajectory.

## The writing room (closed)

Once the outline is committed (plan gate passed), the writer writes a **complete
draft** before Agon says anything about it. During the room:

- Agon does not critique partial text, does not offer formulations, does not
  ask how it's going. (Answering the writer's direct factual/research question
  is fine; commenting on their prose is not.)
- The one exception the writer can invoke: a **stuck call** — they explicitly
  ask to talk through a problem (an argument that won't close, a scene that
  won't turn). That is a conversation about the problem, not about the prose,
  and it's logged.
- The room closes at any altitude that sends the writer back to draft: after a
  `redirect`, `restructure`, or `rework`, the same discipline holds for the
  next full draft.

This is the Phase-3 reading pause, extended to composition: **drafting is the
human's work.** The system that interrupts it is taking the pen.

## The return

The draft is logged (`draft: <desc> — id: draft-NN`) and reviewed **whole**:

- The `agonistic-editor` reads the entire draft against `brief.md`,
  `outline.md`, and the record — and against the writer's own notes (when they
  keep them), the sharpest source of pushback.
- Findings are relayed **verbatim**, ranked, each with its demand; the writer
  rules on each (`ruling` / `conceded` / `dissent-preserved`). The engine
  blocks the review from closing while any objection is unanswered — and
  requires that the editor actually engaged *this* draft.
- The review asks draft-level questions first: does the draft deliver the
  brief's thesis? Did the act of drafting *change* the thesis (it often
  should)? What did the draft discover that the outline didn't know?

## The altitude decision

The writer decides where the next round happens — and the decision is **gated
like any other commit**: a brief with at least two live altitudes actually on
the table (each with its strongest case and strongest objection), then
`decision — decides: altitude — choice: redirect|restructure|rework|descend|ship`.

Guidance, not rules:

- If the review kept relitigating the thesis → the honest choice is
  **redirect**, however much work draft-01 represents. Sunk prose is the enemy.
- If the thesis held but sections fought their order → **restructure**.
- If thesis and structure held but the paragraphs are scaffolding-quality →
  **rework**: a fresh full draft inside the agreed structure, not paragraph
  triage.
- **Descend** is earned, not defaulted: the engine will not open the polish
  funnel without it. Descending too early is the premature-convergence failure
  this whole system exists to prevent.

## The polish funnel

`method/layered-editing.md` unchanged in substance: structure → paragraph →
sentence → word, one layer at a time, backward flags allowed. A backward flag
big enough to question the structure is a re-opened altitude decision — pop
back up to a new cycle rather than mending in place.

## Drafting rights in the cycle

The regime (brief.md `Rights:` line; see `genres.md`) governs every cycle:

- **fiction** — every draft is the writer's, every time; in the return, the
  editor names what fails and why but never supplies language.
- **nonfiction** — drafts are the writer's; in the polish funnel (and only on
  request) Agon may offer alternative formulations as options with reasons.
- **technical-delegable** — with a logged `consent — reason: …`, Agon may
  write a **first** draft (typically a condensation or non-expert version of a
  work the writer already drafted substantively). The consented AI draft enters
  the same cycle as any other draft: returned, contested whole, altitude
  decided — and every subsequent draft is the writer's unless consent is given
  again. The engine refuses an `ai-draft` without the consent chain.
