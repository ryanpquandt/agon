# Record (Γ) — <working title>

The public team record: the project's source of truth and audit trail. See
`../../method/the-record.md` for what belongs here and how to write it. Append
entries under the standing headings; date everything; keep entries short.

The discipline in one line: **if it isn't here, it didn't happen.**

---

## Decisions
<!-- what was decided, when, and why -->

## Considered & rejected
<!-- the strongest alternative on the table, and the specific reason it lost.
     The considered-and-rejected gate writes here before any stage closes. -->

## Open questions
<!-- unresolved, and what would resolve it -->

## Preserved dissent
<!-- where human and agent disagreed, dissent stopped being productive, and both
     positions stand. Record both, and which way the human decided. -->

## Reliance notes
<!-- where the human leaned on the agent, and whether it was well-calibrated.
     A running check against deskilling. -->

## Ledger

<!-- The engine-parsed source of truth (python3 engine/agon.py gate|status|log).
     One entry per line, strict grammar:

  - [YYYY-MM-DD] <type>: <text> — key: value — key: value

  Types & required fields:
    decision:          what was committed        — decides: thesis|outline|altitude|…
                       (altitude also needs — choice: redirect|restructure|rework|descend|ship)
    brief:             options tabled            — decides: <same slug> — options: <N ≥ 2>
    objection:         the editor's challenge    — by: editor — demand: <what would satisfy it>
    ruling:            the writer's ruling on an objection
    conceded:          a round conceded (either side)
    dissent-preserved: both positions stand
    declined:          alternative considered+declined — rated: strong|moderate|weak|none
                       (the editor rates; weak/none = straw, doesn't count)
    draft:             a full draft returned     — id: draft-NN
    consent:           go-ahead for a delegated draft — reason: <why delegation is right here>
                       (technical-delegable only; invalid in fiction)
    ai-draft:          Agon wrote a draft        — id: draft-NN (requires prior consent)
    evidence:          source/note surfaced      — source: <where>
    backward-flag:     a later layer questions an earlier one
    stage:             phase transition (resets the gate's contest window)
    note:              anything else worth the record

  Example:
  - [2026-07-02] decision: descend to polish — decides: altitude — choice: descend
-->
