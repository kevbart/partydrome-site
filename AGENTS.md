# Partydrome site - instructions for every agent

These rules apply to this repository. `CLAUDE.md` and `GEMINI.md` contain just `@AGENTS.md`.

Playbook packs: gui

## What this repo is

The public web pages for the Partydrome app, served by GitHub Pages at <https://kevbart.github.io/partydrome-site/>.
Google Play links to `privacy.html` as the app's privacy policy. The app itself lives in the private `party-games` repo.

## Rules

1. **Public.** Everything here is visible to anyone: no app code, keys, test data or personal email addresses. The only
   address on the pages is the app's own feedback address.
2. **The privacy policy follows the app.** The source text is `docs/store/privacy-policy.md` in `party-games`; change both
   in the same piece of work and update "Last updated". Google Play reads the page at its fixed address, so never rename
   `privacy.html`.
3. Plain HTML and one stylesheet, no build step and no scripts, so the page always loads and has nothing to track.
4. Commits use `kevbart@users.noreply.github.com` (set in this clone's git config), so no personal address goes public.

## How to test

`python tests/check_site.py` checks every page links its stylesheet, every local link exists, the policy has its contact
address and no personal address appears anywhere.
