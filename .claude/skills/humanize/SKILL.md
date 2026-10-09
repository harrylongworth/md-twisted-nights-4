---
name: humanize
description: >
  Strip AI-generated "tells" from draft prose while PRESERVING the project's
  deliberate voice. Invoke manually on a passage, chapter, or pasted text —
  e.g. "/humanize the opening of Chapter 4". Not an AI-detector-evasion tool;
  it exists to make new/AI-assisted drafting sound like the rest of the work.
activation:
  auto: false
---

# Humanize

## What this is

A prose-editing pass that removes the mechanical patterns typical of AI-generated
text **without** flattening the intentional voice of the work. Use it when a
passage was drafted quickly, generated, or just reads "off" against the
surrounding text.

The pattern taxonomy below is synthesized from several open-source Claude
humanizer skills — chiefly `blader/humanizer` (33 patterns, built on Wikipedia's
*Signs of AI writing*), `Aboudjem/humanizer-skill` (43 patterns +
burstiness/perplexity scoring), and `jpeggdev/humanize-writing` (8-pass method).
What's added here is the **voice guardrail**: some "AI tells" may be the target
style of a given project and must be left alone.

**This is NOT for defeating AI detectors, academic dishonesty, or passing off
generated text as original human authorship elsewhere.** It is an in-house style
tool for the author's own manuscripts.

## The prime directive: know the voice before you cut

**Before flagging anything, read the project's CLAUDE.md / style rules and 1–2
neighboring paragraphs.** Establish:

- Which "tells" are actually the house style here (e.g. a Dickens pastiche
  deliberately uses long periodic sentences, semicolons, antithesis, tricolon,
  an ironic omniscient narrator — a generic humanizer would destroy it).
- The spelling standard (US/UK/AU English) — normalize consistently, don't leave
  a mix.
- Character facts that are hard errors to change: established pronouns, names,
  diction, register (e.g. a period novel bans modern idiom like "okay",
  "basically", "a lot going on" unless a character's diction warrants it).
- Audience restraint rules (e.g. YA: dark themes handled honestly but without
  gratuitous detail — don't sanitize, don't sensationalize).

Match the **local** voice, not a generic "natural" voice. Your job is to catch
the *machine* patterns hiding among the *craft* ones.

## Modes

State which mode you're in at the top of your reply.

- **detect** — Scan only. Report each flagged span with its pattern name, a
  one-line reason, and a suggested fix. Change nothing.
- **rewrite** — Produce a revised version of the passage that removes genuine
  tells and matches the work's voice. Show the rewrite; on request, a short
  before/after diff of notable changes.
- **edit** — Apply minimal in-place edits to the target file via the Edit tool,
  changing only flagged spans. Always confirm the file/range first.

Default to **detect** if the author hasn't said. Never edit the manuscript
without an explicit target range or confirmation, and keep any story bible in
sync if a change alters character/plot facts.

## The pattern taxonomy (what to hunt)

Flag these **only when they read as machine output**, not when they're doing
deliberate work. Require a *cluster* of tells, not a lone instance.

### A. Content & substance
1. **Significance inflation** — "marks a pivotal moment", "stands as a testament
   to", "cannot be overstated". Cut or ground in concrete stakes.
2. **Promotional / travel-brochure adjectives** — "vibrant", "nestled",
   "breathtaking", "bustling". (Atmosphere is fine; empty boosterism is not.)
3. **Vague attribution** — "many believe", "it is said", "experts argue" used to
   fake authority. In fiction, dramatize the source or cut.
4. **Superficial "-ing" analysis** — trailing participial clauses that add motion
   but no meaning ("highlighting the tension, showcasing the divide").
5. **Speculative gap-filling stated as fact** — invented detail asserted with
   false confidence. Keep only what the work earns.

### B. Diction
6. **AI vocabulary tics** — "delve", "leverage", "tapestry", "landscape",
   "realm", "interplay", "crucial", "myriad", "testament", "underscore",
   "navigate (abstractly)".
7. **Copula avoidance** — "serves as / functions as / acts as" where "is" is truer.
8. **Elegant variation / synonym cycling** — renaming the same thing every
   mention ("the boy" → "the youngster" → "the lad" → "the child" in one
   breath). One or two deliberate variants: fine. A thesaurus parade: cut.
9. **False ranges** — "from X to Y" across non-comparable things.
10. **Register-breaking idiom** — filler that punctures the established voice
    (project-specific; see Prime Directive).

### C. Rhythm & structure (the subtle ones)
11. **Metronomic cadence / uniform sentence length** — the biggest tell. AI prose
    has low *burstiness*: sentences of similar length in a row. Human prose
    varies hard — a forty-word sentence, then a four-word one. **Fix by varying,
    not by shortening everything.** (The failure mode is uniformity, not length.)

    **11a. Em-dash density (budget, don't ban).** Em-dashes can be voice, but AI
    prose over-produces them. Scan per page/scene; where several land close
    together, keep the strongest and recast the rest (comma, full stop, or
    parenthetical). Target the *cluster*, never the lone effective dash.

    **11b. Epigram-ending tic.** Chapters/sections that all close on a polished
    one-liner read as generated. Keep the best per chapter; let others end
    plainer.
12. **Manufactured staccato drama** — "It was gone. All of it. Just like that."
    Fake punch via fragments. Allowed sparingly; suspicious in clusters.
13. **Negative parallelism as a verbal tic** — "It wasn't just X. It was Y."
    Occasional use is rhetorical; every third sentence is machinery.
14. **Rule-of-three on autopilot** — tricolons that pad rather than build.
15. **Aphorism formulas** — "X is the language of Y", "in a world where…". Cut
    unless the narrator earns it.
16. **Signposting / connective tissue** — "Moreover", "Furthermore",
    "Additionally", "Importantly", "It's worth noting". Rare in good narrative
    prose; usually deletable.

### D. Artifacts & typography
17. **Chatbot residue** — "I hope this helps", "let me know", "Certainly!",
    "Here's a revised version" leaking into the manuscript.
18. **Meta / knowledge-cutoff disclaimers**, placeholder text ("[insert name]"),
    stray markdown bleeding into prose, UTM junk, emoji.
19. **Curly-vs-straight quote inconsistency**, mechanical boldface, title-case in
    headings where the work uses sentence style. (Cross-check the project's
    formatting gotchas: no raw HTML, wrap bare URLs, quote YAML colons.)

### E. Filler & hedging
20. **Redundant phrasing** — "in order to" → "to", "the fact that", "at this
    point in time".
21. **Excessive hedging** — "somewhat", "rather", "arguably", "perhaps" stacked.
    (A narrator's *ironic* qualification is different — that's voice.)
22. **Generic upbeat conclusions** — tidy uplift the work hasn't earned. Match
    the ending's temperature to the book.

### F. Motif & consistency (fiction)
23. **Motif budget** — recurring images must *do something new* on each
    appearance. Cut reminder-only repeats that re-invoke a symbol without
    advancing it.
24. **Over-explanation** — let images land unglossed; trim the sentence that
    explains the image you just wrote.
25. **Lexicon discipline** — characters swear/speak by consistent things (check
    the story bible). Flag an oath or idiom in the wrong character's mouth.
26. **Pronoun audit** — every character holds their established pronouns. Any
    slip is a hard error, not a style call.

## Workflow

1. **Read around the passage.** Sample 1–2 neighboring paragraphs plus the
   project style rules to lock the local voice, narrator stance, and rhythm.
2. **Scan against the taxonomy.** Mark real tells; consciously *spare* the
   deliberate voice features (Prime Directive). Note clusters, not isolated hits.
3. **Draft the fix** preserving all meaning, plot, and character. Vary sentence
   length for burstiness rather than uniformly shortening. Replace machine
   diction with voice-appropriate diction.
4. **Self-audit.** Ask: "If I dropped this into the surrounding chapter, would a
   reader feel a seam?" and "What here still reads as generated?" Revise those.
5. **Report** in the chosen mode. List notable changes so the author can accept
   or reject. Flag any change that touches a bible-tracked fact.

## False-positive guards (do NOT flag)

- Whatever the project's style rules declare as house style (long periodic
  sentences, semicolons, archaic vocabulary, a narrator addressing the reader…).
- A *single* well-placed em-dash — only *clusters* are the tell (§11a).
- A single short emphatic sentence for real effect.
- Deliberate antithesis, tricolon, or extended metaphor doing rhetorical work.
- Specific, hard-to-fabricate concrete detail (usually a sign of *good* writing).
- Any character's established pronouns and diction.

When unsure whether something is craft or machinery, **leave it and ask the
author.** The cost of stripping voice is higher than the cost of one surviving
tell.

## Credit

Synthesized from open-source Claude humanizer skills: `blader/humanizer`,
`Aboudjem/humanizer-skill`, and `jpeggdev/humanize-writing`. First adapted for
*Oli Twisted*; generalized here for reuse.
