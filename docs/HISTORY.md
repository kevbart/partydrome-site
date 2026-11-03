# Partydrome site - complete history

Every change in full, append-only, under the same headings as `docs/DEVLOG.md`. Search it; do not read it whole.

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
