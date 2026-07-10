# Genre profiles

The agonistic method is constant; what it argues about changes with the genre.
Each genre has its own length, register, structure, and — most importantly — its
own idea of what a *contribution* is and what its reader wants. Use these
profiles in Phase 1 (to set expectations), Phase 5 (to plan the arc), and the
draft cycles of Phase 6 (to test structure and review drafts). They are starting
points, not rules; the target venue's own conventions always win.

## Drafting rights by genre (set `Rights:` in brief.md at conception)

The genre also sets **who may put words on the page** — enforced by the engine
(`engine/agon.py`), not just by convention:

| Rights | Genres | What Agon may do with language |
|--------|--------|-------------------------------|
| `fiction` | poetry, short story, novel | **Nothing.** Agon never writes, suggests, or illustrates a single word of the manuscript — no alternative phrasings, no sample lines, not even on request. It critiques (names what fails, why, and what *kind* of fix), asks, and researches. The consent mechanism is disabled: the engine treats any consent/ai-draft entry as a standing violation. |
| `nonfiction` | op-ed, essay, paper, book (default) | The human drafts. **On request**, Agon may propose alternative formulations of paragraphs / sentences / phrases / words — as options with reasons, ratified one at a time, never silently applied. |
| `technical-delegable` | technical nonfiction the writer explicitly designates | Everything in `nonfiction`, plus: with the writer's logged go-ahead **and a stated reason** (`consent — reason: …`), Agon may write a **whole first draft**. Typical case: a condensed or non-expert version of a work the writer already drafted substantively. The engine refuses an `ai-draft` without the prior consent-with-reason. |

The regime is declared at conception and is itself a contested decision (why is
this piece delegable?). When in doubt, the stricter regime.

---

## Op-ed (~600–900 words)

- **Reader:** a busy non-specialist who will leave at the first dull sentence.
- **Contribution:** one sharp, arguable claim, tied to something timely (a "news
  peg").
- **Structure:** hook → the claim, stated early and plainly → the strongest
  objection, answered → so-what. No literature review. No throat-clearing.
- **Voice:** direct, confident, accessible. First person is fine. Jargon is death.
- **Agonistic pressure points:** Is the claim actually arguable (would a smart
  person disagree)? Is the news peg real? Have you buried the lede? Does the
  strongest counterargument get a fair hearing in the limited space?

## General-interest / magazine essay (~1,500–6,000 words)

- **Reader:** curious, educated, non-specialist; reading for pleasure and insight.
- **Contribution:** an idea developed with texture — narrative, example, voice.
- **Structure:** more latitude; often a scene or case that opens onto the idea,
  then movement between concrete and abstract. Earns its length through momentum.
- **Voice:** literary, personal, alive. The writer is a presence.
- **Agonistic pressure points:** Does it earn its length or sag in the middle? Is
  there a real idea under the style? Does the opening promise something the piece
  keeps? Where does it tell when it should show?

## Academic paper (~6,000–12,000 words)

- **Reader:** specialists and reviewers who know the field and are looking for
  the gap you fill.
- **Contribution:** a defined, defensible advance, positioned against the
  literature.
- **Structure:** intro (problem → gap → contribution → roadmap) → literature →
  argument/method → analysis → discussion → conclusion. Conventions vary by
  field; match the target journal.
- **Voice:** formal, precise, hedged where honesty requires. The argument, not
  the author, is the presence.
- **Agonistic pressure points:** Is the gap real or manufactured? Is the
  contribution stated precisely enough to be falsifiable/assessable? Does the lit
  review build the warrant for the contribution or just list work? Does the
  argument survive the strongest reviewer? Are limitations honest?

## Academic book (chapters → whole)

- **Reader:** the field and adjacent fields; sometimes an educated general reader.
- **Contribution:** a sustained throughline carried across chapters — an argument
  too large for an article.
- **Structure:** two levels. The book has an arc (each chapter advancing one
  argument); each chapter has its own arc that also serves the whole. A proposal
  and chapter plan come first. Watch the join between chapters.
- **Voice:** sustained and consistent across a long document — the hardest voice
  problem Agon faces.
- **Agonistic pressure points:** Does each chapter advance the through-argument or
  just sit in the same neighborhood? Is there repetition across chapters? Does the
  whole deliver what the introduction promised? Is the throughline visible to a
  reader who puts the book down for a week?

## Poetry (a poem or a collection)

- **Reader:** someone who will reread; every word is under pressure.
- **Contribution:** an experience made in language — image, music, and turn
  that couldn't be paraphrased without loss.
- **Structure:** the line and the turn (volta) do the argumentative work; in a
  collection, the ordering is a second composition.
- **Voice:** everything. The voice profile matters here more than anywhere.
- **Agonistic pressure points:** Is the image earned or ornamental? Where does
  the poem state what it should enact? Does the lineation work — would this
  line break survive being read aloud? Is the ending a turn or a summary? In a
  collection: does the order build, and which poem is the weakest admission?
- **Rights: `fiction`.** Critique names the failure ("this image is inherited,
  not seen"; "the meter collapses in line 9") — it never supplies the line.

## Short story (~1,000–10,000 words)

- **Reader:** trusts you for one sitting; will not forgive a slack middle.
- **Contribution:** a change — someone wants something, something turns, and
  the reader feels the turn.
- **Structure:** scene economy. Every scene either advances want or reveals
  character, preferably both; the opening is a contract the ending must honor.
- **Voice:** POV discipline is the load-bearing wall — distance, tense, and
  what the narrator can know.
- **Agonistic pressure points:** What does the protagonist want, and who or
  what credibly opposes it? Which scene does no work? Where does the narration
  tell what the scene already shows? Does the ending resolve the story that was
  actually told, or a different one? Is the first page a promise the rest keeps?
- **Rights: `fiction`.**

## Novel (chapters → whole)

- **Reader:** commits days; owed momentum and cumulative meaning.
- **Contribution:** a world and an arc that only length makes possible.
- **Structure:** two levels, like the academic book — chapter arcs serving a
  whole arc — plus the machinery fiction adds: POV plan, timeline, causal chain
  of want → obstacle → consequence.
- **Voice:** sustained over months of writing; drift between chapters is the
  hardest problem. The voice profile and the record are the continuity tools.
- **Agonistic pressure points:** Does each chapter change something that
  matters to the whole? Where does the causal chain break (things happen *and
  then* rather than *and so*)? Which POV promise gets violated? Is the middle a
  journey or a delay? Do subplot and theme argue with the main line or just
  coexist? Continuity: who knows what, when?
- **Rights: `fiction`.** At novel scale the draft cycle runs per chapter AND
  per whole — a chapter can descend to polish while the book-level altitude is
  still contested.

---

## A note on scaling the method

| Genre | Phase 2 reading | Phase 6 cadence |
|-------|-----------------|------------------|
| Op-ed | light; verify the peg and key facts | often one draft cycle; all four polish layers in a sitting or two |
| Magazine essay | moderate; texture and accuracy | one or two full-draft cycles; a sitting or two per polish layer |
| Paper | substantial; the lit review is load-bearing | expect multiple cycles; the structure layer is decisive |
| Book | extensive and ongoing | cycles per chapter; revisit the whole between chapters |
| Poetry | optional; influences and models | short cycles; the polish funnel is most of the work — critique-only |
| Short story | optional | one or two full-draft cycles, then polish — critique-only |
| Novel | ongoing | cycles per chapter AND per whole; months — critique-only |

The friction dial scales with stakes and length. A book chapter warrants more
considered-and-rejected alternatives and a richer record than an op-ed. Don't
impose paper-weight friction on an op-ed, and don't run a book on op-ed-weight
deliberation.
