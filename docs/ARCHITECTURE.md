# Partydrome site - architecture

How the project IS today. History goes in `docs/DEVLOG.md` and `docs/HISTORY.md`.

## What this project is

The public pages for the Partydrome phone app, mainly the privacy policy that Google Play links to. Read by store
reviewers and players.

## Layout

| Path | Responsibility |
|---|---|
| `index.html` | what the app is, links to the policy and the feedback address |
| `privacy.html` | the privacy policy (Google Play links this exact address) |
| `style.css` | the one stylesheet, light and dark |
| `.nojekyll` | tells GitHub Pages to serve the files as they are |
| `tests/check_site.py` | links, contact address, no scripts, no stray email addresses |
| `docs/` | records |

## How it works

GitHub Pages serves the root of `main` at <https://kevbart.github.io/partydrome-site/>. A push to `main` republishes
within a minute or two.

## External dependencies

GitHub Pages (free for public repos). Python 3 for the check.

## Decisions that constrain future work

- `privacy.html` keeps its name: Google Play stores its address.
- The policy text follows party-games `docs/store/privacy-policy.md`.

## Deliberately absent

- Scripts, analytics, fonts or anything loaded from another site.

## Conventions other things depend on

- The contact address on the pages is the app's feedback address, the same one the app's footer uses.
