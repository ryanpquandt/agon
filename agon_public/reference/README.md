# reference/

Your research library lives here. Both folders are optional, gitignored, and
yours to populate:

- **`articles/`** — your PDF library (papers, chapters, clippings). Drop files
  in directly, or symlink an existing library:
  `ln -s ~/path/to/your/articles reference/articles`. The `research-scout`
  agent searches it before going to the web.
- **`notes/`** — a markdown copy of your permanent notes (notes on the books
  and articles you've read), exported from whatever system you keep them in —
  Obsidian, Zettlr, Roam, plain files. One file per note or page works best.
  The agents mine it for suggestions during research and for pushback during
  drafting: the sharpest challenge to a draft is often your own recorded note
  that complicates the claim. Keeping it current is up to you.

If either folder is empty or missing, Agon simply works without it.
