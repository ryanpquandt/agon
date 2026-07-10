# Agon

*An agonistic partner and scaffold for a human–AI writing team.*

Agon (Greek *ἀγών*, "contest" — the root of *agonism*, *protagonist*,
*antagonist*) is a writing system built on one bet, drawn from the **Agonism
Hypothesis**: in hard, consequential work, a human–AI team that builds in
*structured, well-placed friction* beats both automation and rubber-stamp review.
Writing is hard, consequential work. So Agon doesn't write *for* you — it writes
*with* you, and it earns its place by disagreeing well.

Two commitments are wired into everything:

- **You are the first mover, always.** Every phase begins with your idea, your
  framing, your words. Agon responds.
- **Agon never takes over the writing.** It questions, structures, researches, and
  edits. The prose is yours. If you ask it to "just write it," it will hand the
  pen back.

It supports the full range: op-eds, magazine and general-interest essays,
academic papers and books, and — under the strictest regime — poetry and fiction.

**This is a v1**, published for public use and comment. Questions, reactions,
and reports from your own writing practice are genuinely wanted: open a GitHub
issue or write to **ryan.p.quandt@gmail.com**.

---

## Contents

- [Quick start: running Agon in a terminal](#quick-start-running-agon-in-a-terminal)
- [The idea: what "agonistic" means here](#the-idea-what-agonistic-means-here)
- [How Agon exemplifies agonism — and where it only aspires to](#how-agon-exemplifies-agonism--and-where-it-only-aspires-to)
- [The six phases](#the-six-phases)
- [The engine: gates the model can't talk past](#the-engine-gates-the-model-cant-talk-past)
- [How it's organized](#how-its-organized)
- [Optional inputs: your voice and your notes](#optional-inputs-your-voice-and-your-notes)
- [Failure modes](#failure-modes)
- [Status: v1](#status-v1)
- [License & citation](#license--citation)

---

## Quick start: running Agon in a terminal

Agon runs inside [Claude Code](https://claude.com/claude-code), Anthropic's
terminal-based AI agent. You need three things: a terminal, Claude Code (which
requires a Claude account), and Python 3 (for the engine — no packages to
install).

### On a Mac

1. **Open Terminal** — press `⌘`-space, type `Terminal`, hit return.
2. **Install Claude Code**:
   ```
   curl -fsSL https://claude.ai/install.sh | bash
   ```
   (Full install options: <https://docs.claude.com/en/docs/claude-code/setup>.)
3. **Get Agon** — either clone it:
   ```
   git clone https://github.com/ryanpquandt/agon.git
   ```
   or click **Code → Download ZIP** on the GitHub page and unzip it.
4. **Move into the folder and start Claude Code** (starting from *inside* the
   folder matters — that's how the constitution and skills load):
   ```
   cd agon
   claude
   ```
   Log in when prompted.
5. **Write.** Type `/agon` and tell it what you want to write, or just start
   talking about the piece. `/agon-new` scaffolds a fresh project folder.

Python 3 ships with macOS; you can confirm the engine works with
`python3 engine/agon.py selftest`.

### On a PC (Windows)

1. **Open PowerShell** — press the Windows key, type `PowerShell`, hit enter.
2. **Install Claude Code**:
   ```
   irm https://claude.ai/install.ps1 | iex
   ```
3. **Install Python 3** if you don't have it (from
   [python.org](https://www.python.org/downloads/) or the Microsoft Store —
   check with `python --version`).
4. **Get Agon** — `git clone https://github.com/ryanpquandt/agon.git`, or
   download and unzip the ZIP from GitHub.
5. **Move into the folder and start**:
   ```
   cd agon
   claude
   ```
6. Type `/agon` and go. One note: where the docs say `python3`, on Windows type
   `python` (e.g. `python engine/agon.py selftest`).

---

## The idea: what "agonistic" means here

The **Agonism Hypothesis** (Gonzalez & Quandt, in preparation): in non-routine,
consequential work, a human–AI team that embeds *structured, task-focused
friction* at points of real uncertainty outperforms both full automation and
approval-only oversight — provided the friction is substantive, bounded, and
procedurally integrated.

Friction here is not conflict for its own sake. It is the disciplined exchange
of reasons: surfacing contrary evidence, keeping live alternatives on the table,
calibrating how much a suggestion should be trusted, and leaving a record that
can be reconstructed later. Seamless assistance — the industry's default goal —
is precisely the wrong goal for serious writing: frictionless help invites
premature convergence (the first framing wins), hides uncertainty (the prose
sounds sure before the thinking is), and atrophies the writer's own skill. The
bet is that *the right disagreement, in the right place, makes the writing
better.* The full argument is in `method/principles.md`.

## How Agon exemplifies agonism — and where it only aspires to

Each clause of the hypothesis is built into a mechanism:

- **The human is the first mover** (every phase, every decision). This is what
  makes the friction *productive*: agonism needs a real judgment to push
  against, the human's tacit knowledge anchors the project, and the writer
  stays a writer only by doing the generative work. An AI that moves first
  reduces the human to reacting to a machine's frame.
- **Dissent must be authentic, not performative.** Agon argues the position it
  actually holds after reading your work, grounds every objection in the text
  in front of it, and concedes when it's wrong. The research this rests on
  (Nemeth's work on authentic vs. devil's-advocate dissent) is sharp: a real
  dissenter stimulates better thinking than a role-played one, even saying the
  same words.
- **The considered-and-rejected gate.** No stage closes on easy agreement — a
  genuine alternative must be weighed and beaten on the merits first, and the
  editor rates declined alternatives so a straw man doesn't count. This is the
  anti-groupthink mechanism: easy consensus is a warning sign, not a finish
  line.
- **The record (Γ).** Every project keeps `record.md`: decisions with reasons,
  alternatives rejected and why, and disagreements *preserved* rather than
  smoothed over. When contest stops being productive, both positions stand on
  the record and the human decides. The team's reasoning is reconstructable.
- **Friction is a dial, not a default.** The hypothesis predicts an interior
  optimum: too little friction and the first draft of everything wins; too much
  and you get fatigue, deadlock, and a writer who stops listening. Pushback
  concentrates where premature convergence is expensive (thesis, structure,
  altitude) and gets out of the way for routine mechanics and deadlines.
- **Drafting rights keep the team a team.** The point is synergy — a pair that
  knows more than either member — not substitution. So who may put words on the
  page is an explicit, genre-indexed regime: in fiction Agon supplies *no*
  manuscript language ever; in nonfiction, options-with-reasons on request; a
  delegated first draft only with logged, reasoned consent. Refusing to
  ghostwrite is the product, not a limitation of it.
- **The engine makes the discipline procedural.** The hypothesis requires
  friction that is "procedurally integrated" — not left to good intentions.
  `engine/agon.py` is that clause made literal: deterministic gates over the
  project record that refuse to close a phase without a real contest on the
  books.

**And where it only aspires:** the design *encodes* the hypothesis; whether any
given session *exhibits* it is an empirical question. Large language models are
trained toward agreeableness and fluent confidence — the exact failure modes
this system exists to resist — and no gate can verify that an objection was
sincere, only that one was raised, answered, and logged. The engine checks the
form of the contest; the constitution demands its substance; the gap between
them is real and it is where this system will succeed or fail. That gap is a
standing reason for this release: reports of where the friction was real and
where it was theater are the most valuable feedback this project can get.

## The six phases

1. **Conceive** (`/agon-conceive`) — theme, question, thesis, genre, venue,
   voice, and the **drafting rights** (fiction: Agon writes no words;
   nonfiction: options on request; technical-delegable: consented first draft).
2. **Map research** (`/agon-research`) — find the literature; split *must-read-
   before-drafting* from *citable-but-not-essential*.
3. **Read** (`/agon-reading`) — a deliberate pause. You read; Agon holds the plan
   and captures notes. It will not draft during this phase.
4. **Refine** (`/agon-refine`) — revise the question, angle, and thesis after
   reading.
5. **Plan** (`/agon-plan`) — build and stress-test the structure. Closing it
   closes the **writing room**.
6. **Draft cycles** (`/agon-draft`) — you write a **full draft alone**; then a
   whole-draft agonistic review; then the **altitude decision** (redirect |
   restructure | rework | descend | ship). Iterate — or descend into the polish
   funnel: **structure → paragraph → sentence → word.**

Phases are a default path, not a cage — you can move backward, skip, or loop.
Two disciplines are hard, though: the writing room stays closed while you draft
(no critique of partial text, no formulations), and the polish funnel opens only
through an explicit `descend` decision. Not sure where you are? Run `/agon` —
it reads the project and proposes the next step.

## The engine: gates the model can't talk past

`engine/agon.py` (Python 3, standard library, one file) parses each project's
`## Ledger` — a strict one-line-per-event grammar documented in
`projects/_TEMPLATE/record.md` — and enforces what must hold no matter which
model is driving:

- **Phase-close gates** — the editor must actually have fired; every objection
  needs a ruling, a concession, or preserved dissent; rejected alternatives
  count only when rated `strong|moderate` (straw doesn't count).
- **Brief-before-commit** — thesis, outline, and altitude decisions are refused
  without a prior brief carrying at least two live options.
- **The draft cycle** — a review requires a logged full draft and editor
  engagement with *that* draft; polish is reachable only through `descend`.
- **Drafting rights** — an `ai-draft` without prior logged consent (or any
  consent at all in a fiction project) is a standing violation.

`status` orients, `gate` checks, `log` appends, `selftest` verifies the engine
itself. If it isn't in the Ledger, it didn't happen.

## How it's organized

```
agon/
  CLAUDE.md          the constitution — the rules Agon operates under
  README.md          this file
  engine/            agon.py — deterministic gates over the markdown ledger
  method/            the deep reference (principles, draft cycles, layered editing,
                     genres + drafting rights, the record)
  voice/             your past publications + the generated voice-profile.md
  reference/         articles/ (your PDF library) + notes/ (your permanent notes)
  projects/          one folder per piece (each with brief, reading-plan, record,
                     outline, drafts) — _TEMPLATE is the seed
  .claude/
    skills/          the phase skills (agon-*)
    agents/          research-scout, agonistic-editor, voice-analyst
```

Your writing stays yours in every sense: `.gitignore` keeps `projects/`,
`voice/`, and `reference/` out of version control by default, so a fork of this
repo never accidentally publishes your drafts, notes, or manuscripts.

## Optional inputs: your voice and your notes

**Voice.** Drop past publications into `voice/` and run `/agon-voice`. The
analyst builds `voice/voice-profile.md`: the characteristic moves worth
amplifying *and* the recurring tics worth leaving behind — used in the word
layer to keep the piece the best version of your voice rather than generic
competent prose.

**Notes.** If you keep permanent notes on what you read (Obsidian, Zettlr,
Roam, plain files), export a markdown copy into `reference/notes/`. The agents
mine it for **suggestions** during conception and research, and for
**pushback** during review — the sharpest challenge to a draft is often your
own recorded note that complicates the claim, or the idea you had two years ago
and forgot. Your notes are quoted to you, never published, and gitignored.

Both are optional; everything works without them.

## Failure modes

Anticipated and, in some cases, already observed. The engine and constitution
are counterweights, not cures — watch for these in your own use, and report
what you see.

- **Performative dissent.** The model manufactures objections to seem
  rigorous — friction as theater. The constitution forbids it (authentic
  positions only, concede when wrong), but no gate can verify sincerity. If
  every draft gets exactly three objections of similar weight, be suspicious.
- **Straw gates.** The considered-and-rejected gate is satisfied in letter by
  an alternative nobody would actually hold. The editor's strength ratings
  (only `strong|moderate` count) exist for this, but the ratings are
  themselves the model's — the human should occasionally audit a "rejected"
  alternative and ask whether it ever really lived.
- **Ledger theater.** Entries logged to pass gates rather than to record a
  real contest. The engine checks form, not substance: it can verify an
  objection was answered, not that it was worth raising or honestly ruled on.
- **Ghostwriting by increments.** "Options with reasons" become de facto
  drafting when every suggestion is ratified unchanged. The rights regime and
  one-at-a-time ratification slow this; the honest check is the writer's own
  ratification rate. (This is why fiction disables options entirely.)
- **Sycophancy relapse.** The model concedes too fast, softens findings in
  relay, or wraps objections in praise until they stop landing. Verbatim
  relay of the editor's findings is the rule precisely because summaries
  drift agreeable.
- **Misplaced friction.** Pushback on routine mechanics, or a gate blocking
  under a real deadline — the interior optimum missed from the other side.
  The dial guidance in `method/principles.md` addresses when to turn friction
  *down*; use it.
- **Reliance creep.** The writer offloads judgment piece by piece — research
  first, then structure, then rulings — while nominally staying first mover.
  Γ's reliance notes exist to catch this, but only if they're honestly kept.
- **A rubber-stamping human.** Agonism takes two. If the human rules on
  objections pro forma to get to "done," the system becomes approval-only
  oversight with extra paperwork — the exact thing it was built against. No
  mechanism here can fix this; only noticing it can.
- **Voice flattening.** Line edits that converge on generic competence. The
  voice profile is the counterweight: amplify what's characteristic, retire
  what isn't working — never sand everything smooth.

## Status: v1

This is version 1 of a working system. It runs daily on real writing projects —
op-eds, essays, and academic work — but it is one writer's instrument, and the
open question is how it holds up in other hands, other genres, and other
writing practices.

Feedback of any kind is welcome, especially: where the friction paid off, where
it was noise, where the gates blocked something they shouldn't have (or waved
through something they should have caught), and where the model slipped toward
ghostwriting despite everything.

- **GitHub issues** — for anything, from bug to philosophy.
- **Email** — <ryan.p.quandt@gmail.com> for comments and questions.
- **PRs** — welcome, especially to the method docs and genre profiles. For
  changes to the Constitution (`CLAUDE.md`) or the engine's gates, open an
  issue first — those encode the core bet, and loosening them is usually the
  wrong fix. Run `python3 engine/agon.py selftest` before submitting engine
  changes.

## License & citation

MIT — see `LICENSE`.

The source paper: Gonzalez & Quandt, *The Agonism Hypothesis for Human-AI
Teaming* (in preparation).
