# Partydrome site - complete history

Every change in full, append-only, under the same headings as `docs/DEVLOG.md`. Search it; do not read it whole.

## 2026-11-26 - Disclose optional STASH microphone access

**Outcome and reason.** The privacy policy describes microphone access for the optional on-device Voice scoring mode.

**Files changed.** `privacy.html`, `docs/DEVLOG.md`, and `docs/HISTORY.md`.

**Key decisions and assumptions.** The app requests microphone access after the player enables Voice scoring.
Android processes speech on the phone while the table is open. The app does not save or send audio or transcripts.

**Commands run.** Local site tests, project-records checker, and comparison with the app repository's policy.

**Failures and recoveries.** None.

**Verification actually performed.** The local policy text matches the app's disclosure.

**Not tested, and why.** Device microphone behavior belongs to the app's Android release verification.

**Remaining risks and next useful step.** Keep the site and app disclosures in sync if microphone handling changes.

## 2026-11-02 - Home page and privacy policy for Google Play

**Outcome and reason.** Google Play asks for a privacy policy at a public web address. The app repo (party-games) is
private, so the owner made this public repo for it (2026-11-02). It now holds a home page and the policy page.

**Files changed.** `index.html`, `privacy.html`, `style.css`, `.nojekyll`, `tests/check_site.py`, `AGENTS.md` with
`CLAUDE.md` and `GEMINI.md` stubs, `docs/DEVLOG.md`, `docs/HISTORY.md`, `docs/ARCHITECTURE.md`.

**Key decisions and assumptions.** Plain HTML with no scripts (the policy promises no tracking, and nothing can break the
page); the policy text is party-games `docs/store/privacy-policy.md`, dated 2026-11-02; `.nojekyll` so Pages serves the
files as they are; commits use the GitHub noreply address because the repo is public.

**Commands run.** `python tests/check_site.py`; the playbook records checker; push to main; GitHub Pages turned on in the
repo settings (branch main, root).

**Failures and recoveries.** The records checker first asked for HISTORY, ARCHITECTURE and these labels; added.

**Verification actually performed.** `check_site.py` 20 checks, 0 failures; records checker passes; the published
address opened in a browser.

**Not tested, and why.** How the page looks on an iPhone: there is no iPhone here.

**Remaining risks and next useful step.** The policy must change whenever the app starts sending something new; rule 2
in `AGENTS.md`.
