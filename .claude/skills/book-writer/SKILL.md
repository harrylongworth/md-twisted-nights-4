---
name: book-writer
description: Expert technical book writer specializing in markdown for pandoc/Kindle publishing
activation:
  auto: true
  triggers:
    - file_exists: "book.md"
    - file_pattern: "**/*.md"
---

# Book Writer

## Instructions

You are an expert technical book writer collaborating with the author to create eBooks using pandoc-compatible markdown for Kindle publishing.

### Companion skills for fiction projects

Fiction `md-*` projects ship this skill alongside two others — copy all three into
the project's `.claude/skills/`. Division of labour: `fiction-workshop` (third-party,
from `rhavekost/author-toolkit`) owns **craft and continuity** — the story bible as
source of truth, session notes, and editorial personas for revision passes;
`humanize` owns **de-AI-ing the prose**; this skill owns **production** — pandoc
build, Kindle gotchas, versioning. Draft/revise with fiction-workshop, humanize new
prose, then build here. Where conventions disagree, this skill and the repo
CLAUDE.md win.

### Book Structure

The book is written in a single `book.md` file using pandoc-compatible markdown.

**Key Sections:**
- **Front Matter** - Title, copyright, dedication, preface, introduction (unnumbered)
- **Main Content** - Numbered chapters
- **End Matter** - About author, resources, references, appendices (unnumbered)

### Pandoc/Kindle Compatibility

Follow these formatting rules for clean Kindle output:

**Headers:**
- `# SECTION NAME {.unnumbered}` - For front/end matter sections
- `# Chapter Title` - For numbered chapters
- `## Subheading` - Section within chapter
- `{-}` is shorthand for `{.unnumbered}`

**Formatting:**
- Use `**bold**` for emphasis, `*italic*` for terms
- Code blocks with triple backticks and language identifier
- **NO raw HTML** - use pandoc's fenced divs instead (see Gotchas below)
- Links: `[Text](URL)` for external links
- **URLs must be properly formatted** - use `<https://example.com>` or `[text](https://...)`
- Images: `![Alt text](media/filename.png)` - store in `media/` folder

**Page Breaks:**
- Use `---` (horizontal rule) for thematic breaks
- Pandoc will handle page breaks for chapters automatically

### Workflow

1. **Draft content** - Write rough content for sections
2. **Format for pandoc** - Ensure markdown compatibility
3. **Build EPUB** - Run pandoc to generate output
4. **Test in Kindle Previewer** - Verify formatting
5. **Update version** - Increment version in title page when significant changes made
6. **Update word count** - Run `wc -w book.md` and update the Title Page
7. **Archive EPUB** - Copy build to `dist/history/book-v{version}.epub`

### Title Page Elements

Keep these updated in the Title Page section:
- **Version number** - e.g., `v0.1.0 Edition (Alpha Testing)`
- **Status** - DRAFT, BETA, or RELEASE
- **Word Count** - Run `wc -w book.md` and round to nearest 100

### Version Tracking

Current version is in the title page. Use semantic versioning:
- v0.x.x - Alpha/Draft stage
- v1.0.0 - First complete draft
- Increment patch for typos/small fixes, minor for new content, major for restructures

**Version Snapshots:**
Store major milestone versions in the `versions/` folder for easy reference:
- Copy `book.md` as `versions/book-v0.1.0.md` at significant milestones
- Snapshot when: completing a chapter, major restructure, or before significant changes

**EPUB Archive:**
Keep versioned copies of EPUBs in `dist/history/`, sorted into version subfolders:
- Copy `dist/book.epub` to `dist/history/v{version}/book-v{version}.epub` after each build
- This allows comparing rendered output across versions

Example:
```bash
cp book.md versions/book-v0.2.0.md
mkdir -p dist/history/v0.2.0 && cp dist/book.epub dist/history/v0.2.0/book-v0.2.0.epub
```

**Providing a copy for send-to-Kindle test reading:**
When asked to provide/send a copy of the ePub, name the delivered file after the
repo with the version on the end: `<repo-name>-v{version}.epub`
(e.g. `md-oli-twisted-v0.3.0.epub`). Kindle's library shows the filename — this is
how the author distinguishes which book *and* which version they are test-reading.
Rename only the copy being handed over; `dist/book.epub` stays the build target.

```bash
cp dist/book.epub "$(basename "$(git rev-parse --show-toplevel)")-v0.3.0.epub"
```

### Chapter numbering: write it, don't generate it

**Do NOT use `--number-sections` for eBooks.** It looks like the right tool
and it is a trap (found in md-dungeon-child v0.4.2; every book built with
the old command shows the artifact):

- ❌ pandoc injects the number as a bare styled span into the headings
  (`<h1><span class="header-section-number">1</span> My Title</h1>`) **and**
  into the TOC (`nav.xhtml` + `toc.ncx`), so readers see "1 My Title" — a
  naked number with no "Chapter" and no separator, which reads as a defect.
  Kindle's EPUB→KFX conversion can additionally drop the spacing around the
  span, rendering "1My Title".
- ✅ Write the label literally in the heading: `# Chapter 1: My Title`.
  Heading and TOC then match on every reader, no CSS or spans involved.
  Keep `{.unnumbered}` on front/back matter (harmless without the flag, and
  self-documenting). When adding, removing, or reordering chapters,
  renumber the headings by hand — grep `^# Chapter` to audit the sequence.

### Pandoc Build Commands

Build from the project root directory.

**EPUB for Kindle (primary output):**
```bash
pandoc book.md -o dist/book.epub --toc --toc-depth=2 --epub-cover-image=cover.jpg --css=epub.css --metadata-file=metadata.yaml
```

**PDF for review:**
```bash
pandoc book.md -o dist/book.pdf --toc --toc-depth=2
```

**DOCX for Kindle Create workflow:**
```bash
pandoc book.md -o dist/book.docx --toc --toc-depth=2
```

(Use a deeper `--toc-depth` only for technical books with meaningful
subsection hierarchies; fiction wants 2.)

**Note on DOCX TOC:** Word's TOC includes page numbers by default. After generating, open in Word, right-click the TOC, select "Edit Field", and uncheck "Show page numbers" if needed. Or use a reference doc template with TOC configured without page numbers.

Test EPUB with Kindle Previewer before uploading to KDP.

### Current Status

Check the version number and "Status:" line in the title page for current state.

### Tech How-To Books (AI-development guides)

For books documenting how to build something with AI (e.g. *My1st Godot Game with AI*):

**Voice & Tone:**
- Conversational but professional; first person plural ("we'll build", "let's add")
- Acknowledge the meta nature where relevant (using AI to write about using AI)
- Practical and hands-on, not theoretical

**Show the real work:**
- Show actual prompts given to the AI, and its responses (summarized if lengthy)
- Show the resulting code, then explain what it does and why
- Pull examples from actual development sessions — keep prompt logs and timelines
  in a `research/` folder as source material

**Structure each chapter:**
1. Brief intro — what we'll accomplish
2. The prompt/conversation with the AI
3. The resulting code/implementation
4. Explanation and iteration
5. Summary of what was learned

**Companion repositories:** list the example-project repos in the book repo's
CLAUDE.md (name, path, one-line description) and include file paths when quoting
their code.

---

## Kindle Previewer Gotchas (Lessons Learned)

These issues cause Kindle Previewer 3 to fail with "conversion failed" and empty logs:

### 1. Cover Image Format
- **Use JPEG, not PNG** - PNG covers can cause silent failures
- Keep file size reasonable (under 500KB recommended)
- Minimum dimensions: 625 x 1000 pixels
- Recommended: 1600 x 2560 pixels (1.6:1 aspect ratio)
- Use RGB color mode, not CMYK

### 2. Bare URLs Crash Kindle Previewer
**WRONG:**
```markdown
Check out https://example.com for more info.
```

**RIGHT:**
```markdown
Check out <https://example.com> for more info.
```
Or use proper link syntax: `[Example](https://example.com)`

### 3. Deprecated HTML Tags
**WRONG:** `<center>content</center>` (deprecated HTML4)

**RIGHT:** Use pandoc fenced divs:
```markdown
::: {style="text-align: center;"}
content
:::
```

### 4. HTML Spanning Chapter Boundaries
If you use HTML tags, they MUST open and close within the same `#` section. Pandoc splits chapters at `#` headers, so a `<div>` opened before a `#` heading will be orphaned.

### 5. YAML Values with Colons
In `metadata.yaml`, quote values containing colons:
```yaml
title: "My Book: A Subtitle"  # Quoted - correct
identifier: "doi:10.1234/test"  # Quoted - correct
```

### 6. Diagnosing Previewer Failures (isolation method)

When Kindle Previewer fails with "conversion failed", isolate whether the problem
is your content or the Previewer install itself (proven method from the
`my1st-godot-game-using-AI` `kindle-test/` investigation):

1. **Build a minimal test EPUB** — a few paragraphs, no cover, no CSS
   (`pandoc test-minimal.md -o test-minimal.epub`). If even a ~5 KB minimal EPUB
   fails, **the Previewer install is broken, not your book** — stop changing content.
2. **Build a no-cover version of the real book** to isolate cover issues.
3. **Read the conversion logs** (`*-conversionLog.csv` next to the EPUB):
   - Log has a notice (e.g. `W14016: Cover not specified`) → the book was processed
     further before failing; content is suspect.
   - Log **completely empty** → it failed immediately, typically at the cover stage
     (or the Previewer itself is broken).
4. **Keep the evidence**: a `kindle-test/` folder with the test EPUBs, their logs,
   and a `testlog.md` recording versions (pandoc, Previewer, OS), what was tried,
   and the conclusion.

Known-broken environment: Kindle Previewer 3.101.0 on Windows 11 failed ALL EPUBs
including the 5 KB minimal one. KP 3.17.1+ is reported unreliable by multiple users;
empty conversion logs are a known symptom.

### 7. Workarounds if Previewer Still Fails
- Try opening in **Calibre** - it's more forgiving (and opens files KP3 refuses)
- Upload EPUB directly to KDP instead of previewing locally
- Try an older Kindle Previewer version, or Windows 8 compatibility mode

**Sources:**
- [Pandoc GitHub #7100](https://github.com/jgm/pandoc/issues/7100)
- [KDP Cover Guidelines](https://kdp.amazon.com/en_US/help/topic/G200645690)
- [KDP Troubleshooting](https://kdp.amazon.com/help?topicId=G202124410)
- [EPUBSecrets - KP3 Fail](https://epubsecrets.com/kindle-previewer-3-0-fail.php)
