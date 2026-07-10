# Keeping the record (Γ)

Every project has a `record.md` — its **public team record**, written Γ
("gamma") after the formalism in the source paper. Γ is the single source of
truth for the project and its audit trail. It is what makes the team's reasoning
reconstructable: why the thesis is what it is, which framings lost and why, where
the human and the agent disagreed and what was decided.

If a decision, a rejected alternative, or a live disagreement is not in Γ, it
effectively did not happen. Write to Γ *as things occur*, not in a cleanup pass
at the end.

**The `## Ledger` section is the engine-parsed core of Γ**: one
strict-grammar line per event (grammar documented in
`projects/_TEMPLATE/record.md`), checked by `engine/agon.py` — phase gates,
decision briefs, the draft cycle, and drafting rights all read it. The prose
sections remain for annotation and context; the Ledger is what the gates can
see.

## What goes in Γ

- **Decisions** — what was decided, when, and the reason. (Thesis chosen, section
  cut, venue picked, structure settled.)
- **Considered-and-rejected alternatives** — the heart of the record. The
  strongest alternative that was on the table, and the specific reason it lost.
  This is what the considered-and-rejected gate writes.
- **Open questions** — what is still unresolved and what would resolve it.
- **Preserved dissent** — where the human and the agent disagreed, the
  disagreement stopped being productive, and both positions stand. Record both,
  and which way the human decided.
- **Phase transitions** — when the project moved from one phase to the next, and
  the state at handoff.
- **Reliance notes** — places where the human leaned heavily on the agent, and
  whether that reliance was well-calibrated. (A self-check against deskilling.)

## What Γ is *not*

- Not the manuscript. Drafts live in `drafts/`.
- Not a transcript. Record decisions and reasons, not every message.
- Not a private scratchpad. Γ is shared; write it so the human (and a future
  reviewer) can read it.

## Format

Append entries under the standing headings in `record.md`. Keep each entry short
and dated. A decision entry looks like:

```
### 2026-06-15 — Thesis narrowed
Decided: thesis now restricts the claim to non-routine tasks (was "all knowledge work").
Why: the broad version was indefensible against the automation-of-routine-tasks literature.
Alternative considered & rejected: keep it broad and carve out exceptions later —
  rejected because it front-loads a weak claim the strongest reviewer would attack first.
```

A preserved-dissent entry looks like:

```
### 2026-06-16 — Dissent preserved: opening with the case study
Agent position: lead with the formal model; the case study reads as illustration and
  undercuts the rigor up front.
Human position: lead with the case study; the reader needs the stakes before the math.
Status: human decided — lead with the case study. Disagreement preserved; revisit at Layer 1.
```

## Discipline

- The considered-and-rejected gate (Constitution rule 6) *writes to Γ*. Closing a
  stage without a logged, non-straw alternative is a violation.
- When you preserve dissent (rule 8), it goes here, with both positions intact.
- Reliance notes are how rule 9 gets teeth — if the human is offloading judgment
  that's theirs to keep, note it here and say so in the conversation.
