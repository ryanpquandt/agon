# The four-layer polish funnel

This is the **polish funnel** — the downstream half of Phase 6, reachable only
through an explicit `descend` altitude decision after a full-draft review (see
`draft-cycles.md`; the engine enforces the gate). It refines a draft whose
thesis and structure have already survived contest, in four passes from the
largest structures to the smallest. The order is not a suggestion. **You do not
fix a sentence in a section that may get cut; you do not choose the perfect word
in a sentence that may get rewritten.** Polishing prose that hasn't earned its
place is the most common way to waste a writer's effort and to fall in love with
material that should go.

Drafting rights hold in the funnel (`genres.md`): in **fiction**, layers 3 and 4
name the failure and the kind of fix but never supply language — no options, no
illustrative spans. In **nonfiction**, options-with-reasons are welcome at the
sentence and word layers, on request, ratified one at a time.

Across all four layers the constitution holds: the human is the first mover, the
prose is theirs, and the editor is agonistic — it pushes back with reasons and
concedes when wrong. What changes layer to layer is *what the friction is about*.

---

## Layer 1 — Structure

**The question:** Does the overall architecture serve the thesis?

Work at the level of the whole piece and its major parts. Nothing below the
section/move level is in scope yet — resist every urge to fix wording.

Agonistic moves:
- Does each section earn its place? Name any that could be cut without loss.
- Is the order the *argumentative* order, or just the order ideas arrived in?
- Where is the thesis actually established — and is it too late?
- What does the strongest opposing reader say, and does the structure answer them?
- Is anything load-bearing missing? Is anything redundant?
- For the genre: does the arc match what this venue and reader expect? (See
  `genres.md`.)

Exit when: the human can state in one sentence what each section does and why it
sits where it does, and at least one structural alternative (a different order, a
cut section, a different entry point) is in Γ as considered and rejected.

**Artifact:** `drafts/d1-structure.md` (or a revised `outline.md`).

---

## Layer 2 — Paragraph

**The question:** Does each paragraph do one job, and do they connect?

The structure is now fixed. Work paragraph by paragraph within it.

Agonistic moves:
- What is this paragraph's single job? If you can't name it, it's two paragraphs
  or none.
- Does the topic sentence promise what the paragraph delivers?
- Is the evidence in the right paragraph, and is it enough?
- Do the transitions carry the argument, or just sit between blocks?
- Is the paragraph order within the section right?
- Are there paragraphs that are really just throat-clearing?

Exit when: every paragraph has a nameable job and a defensible position, and a
real alternative arrangement was weighed and logged.

**Artifact:** `drafts/d2-paragraph.md`.

---

## Layer 3 — Sentence

**The question:** Is each sentence clear, and does it move?

Now the prose. Here you may propose specific edits — always as options with
reasons, ratified one at a time by the human, never silently applied.

Agonistic moves:
- Find the sentence whose meaning you had to reconstruct, and say why.
- Flag hedging that drains a claim the writer actually wants to make.
- Watch rhythm: are all the sentences the same length? Where does monotony dull a
  point that should land?
- Where does passive voice hide an agent who should be named?
- Are the logical connectives (*therefore, but, because, although*) honest about
  the relation, or decorative?

Exit when: the human has ruled on each flagged sentence and the prose reads
cleanly aloud.

**Artifact:** `drafts/d3-sentence.md`.

---

## Layer 4 — Word

**The question:** Is every word the right word, and does it sound like the human?

The finest pass. Diction, precision, and voice.

Agonistic moves:
- Flag imprecise words where a sharper one exists — propose it with a reason.
- Hunt jargon that excludes the intended reader; hunt clichés that dull a fresh point.
- Check voice against `voice/voice-profile.md`: amplify the characteristic moves,
  and excise the documented tics and crutches. **Surpass the infelicities — do
  not reproduce them.**
- Watch for words doing more rhetorical work than the evidence licenses.

Exit when: the human has ratified the diction and the piece reads as the best
version of their voice.

**Artifact:** `drafts/d4-word.md` → the final manuscript.

---

## Notes that apply to all layers

- **One layer at a time.** If you spot a word-choice problem during the structure
  pass, note it in Γ for later and move on. Don't let a small fix pull you out of
  the level you're working at.
- **Backward flags are allowed.** If the sentence pass reveals that a paragraph's
  job was never real, raise it as a backward flag — but the decision to reopen an
  earlier layer is the human's, and it goes in Γ.
- **Genre sets the dial.** A 700-word op-ed may run all four layers in one
  sitting; a book chapter may spend a week per layer. Scale accordingly.
- **The deep critique is optional.** For any layer, you may dispatch the
  `agonistic-editor` subagent to produce a thorough independent pass, then bring
  it back for the human to respond to first. The subagent critiques; it never
  rewrites.
