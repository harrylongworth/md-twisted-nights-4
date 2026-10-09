# Project: Twisted Nights, Night Four: Old Friends (md-twisted-nights-4)

Tom's book, published under the pen name **T.L. Shadowmarsh**, continuing straight on from
`harrylongworth/md-twisted-nights-3` (Book 3, *Night of Embers*). See `harrylongworth/md-claude`
(now `Amhazing-Pty-Ltd/md-claude`) for the master CLAUDE.md — branch/deploy workflow,
devlog/changelog format, skills, and the eBook operations summary all apply here. This file only
covers what's specific to this project.

## What this is

Book 4 of a planned five (author: "maybe"). Book 3 closed with **"Prelude to Night Four"**:
at 3:33 AM a tree deep in the woods outside Bellemarsh glitches blue and **Withered Bonnie**
steps out of it — one arm missing, no face, two small points of light in the hollow. That is
Book 4's opening hook. Everything else about the plot is the author's call; source of truth is
`docs/story-bible.md`.

## IMPORTANT — not for commercial distribution

Same restriction as Books 1-3: FNAF's characters and setting (including Withered Bonnie) are
Scott Cawthon/Steel Wool Studios IP, not freely licensed like SCP (CC-BY-SA). Personal /
free-reading only. Do not add ISBN/KDP metadata, do not suggest a KDP upload. The T.L.
Shadowmarsh pen name stays firewalled from the commercial pen names.

## Continuity dependency on Books 1-3

This book assumes Books 1-3 (`md-twisted-nights`, `md-twisted-nights-2`, `md-twisted-nights-3`)
as read. Attach all three repos to any drafting session. Do not contradict any of their story
bibles without flagging it as a deliberate retcon and noting the retcon in every affected
book's story bible. Notably:
- **The Bellemarsh Record** (Book 3's end matter) is unreliable in-world. Its seeds — Phantom
  Freddy, the Puppet in the well maze, the two golden bears — are **reserved for Books 4-5 and
  are not explained on the page until the author directs**. Its dates do not override the
  manuscripts.
- Leo Fontenot is the series' recurring inciting-incident character; the pack has noticed.
- Grim Foxy is dormant again at his site; Twisted Foxy visits him. Miller's private file on
  Violet Hellstorm is open and unfiled; Reyes is confirmed to full command over a recorded
  Drell-loyalist dissent. These are the carried-over threads (see the story bible).
- House style: ages 10-15, spooky-but-funny ensemble, multi-POV, dread over gore, restraint
  endings (disarm, don't kill). ~14,000 words, ~22 short chapters, 4 acts, interludes.
- Each book ends with a short **"Prelude to Night N+1"** after the final chapter, before END
  MATTER.
- **No raw HTML in `book.md`** — Book 2 and 3 both shipped an unmatched `</center>`. Use pandoc
  fenced divs.

## Build

Same pandoc pipeline as Books 1-3 (once `book.md` exists; `apt-get install -y pandoc` first in
a cloud container):

```bash
pandoc book.md -o dist/book.epub --toc --toc-depth=2 --epub-cover-image=cover.jpg --css=epub.css --metadata-file=metadata.yaml
```

Validate with `epubcheck` rather than trusting pandoc's exit code. Never `--number-sections`.

## Key files

- `docs/story-bible.md` — source of truth for this book (per the `fiction-workshop` skill);
  update it first when plot/character facts change
- `docs/devlog.md` + `docs/devlog/` fragments, `docs/changelog.md` — standard format, see
  master CLAUDE.md
- `.claude/skills/` — `book-writer`, `fiction-workshop`, `humanize` (copied from Book 3)
- `tools/cover.py` — the shared series cover generator; **keep all four repos' copies
  identical**. Book 4 has no entry yet (title now chosen; see devlog backlog).
- `metadata.yaml`, `epub.css` — build metadata and stylesheet, matching Books 1-3

## Workflow

Writing repo — commit straight to `main`, no ff gate (see master CLAUDE.md branch/deploy section).
