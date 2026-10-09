# Devlog fragments (house standard, all repos)

Parallel sessions kept conflicting on the shared `docs/devlog.md` (three
rebase conflicts and two mangled entries in md-claude on 2026-08-13 alone),
so every repo uses a **fragment + consolidation** pattern:

- **Worker sessions**: write your devlog entry as a NEW file in this
  directory — `YYYYMMDD-HHMM-<slug>.md` (Sydney time, slug a few words,
  e.g. `20260813-1750-website-migration-plan.md`). Body = the normal entry
  text (`- YYYYMMDD @HHMM — **What happened.** Details…`). Do NOT edit
  `docs/devlog.md`'s `## Done` section — file creation can't conflict;
  shared-file edits do.
- **Consolidation is single-writer**, at the repo's natural moment:
  - **md-claude**: the chief-of-staff sweep rolls fragments into
    `docs/devlog.md` `## Done` (newest first) and deletes the absorbed
    fragment files (git history preserves them).
  - **Project repos**: the session doing the next release/cut consolidates
    the devlog in the same step as the changelog consolidation — or any
    session Harry asks to tidy.
- **Readers** (sweeps included): current state = `docs/devlog.md` plus any
  not-yet-consolidated fragments here (filename sort = time order).
- `## Ideas / backlog` in `docs/devlog.md` remains directly editable
  (low-traffic, additive edits only).

Rollout: existing repos adopt this the next time a session touches them —
copy this README into `docs/devlog/` and note the convention in the project
CLAUDE.md. New repos get it from the new-project checklist.
