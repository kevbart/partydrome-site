"""Checks the public Partydrome pages before they go live: every page links the stylesheet, every local link points at a
file that exists, the privacy policy names its contact address, and no personal address or script slips in (the repo is
public and the pages promise no tracking). Prints its check count; exits 1 on any failure."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONTACT = "DoeStep24601@gmail.com"
checks = failures = 0


def check(ok, what):
    global checks, failures
    checks += 1
    if not ok:
        failures += 1
        print("FAIL:", what)


pages = sorted(ROOT.glob("*.html"))
check(len(pages) >= 2, "index.html and privacy.html exist")
for page in pages:
    text = page.read_text(encoding="utf-8")
    check('href="style.css"' in text, page.name + " links style.css")
    check("<script" not in text.lower(), page.name + " has no scripts")
    check('name="viewport"' in text, page.name + " fits phone screens")
    for link in re.findall(r'href="([^"#:]+)"', text):
        check((ROOT / link).exists(), page.name + " links an existing file: " + link)

privacy = (ROOT / "privacy.html").read_text(encoding="utf-8")
check(CONTACT in privacy, "privacy policy names the contact address")
check(re.search(r"Last updated: \d{4}-\d\d-\d\d", privacy) is not None, "privacy policy has its date")

for path in ROOT.rglob("*"):
    if path.is_file() and ".git" not in path.parts and path.suffix in (".html", ".css", ".md", ".py"):
        text = path.read_text(encoding="utf-8")
        addresses = set(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", text)) - {CONTACT, "kevbart@users.noreply.github.com"}
        check(not addresses, "no other email address in " + str(path.relative_to(ROOT)) + ": " + ", ".join(sorted(addresses)))

print("site: %d checks, %d failures" % (checks, failures))
sys.exit(1 if failures else 0)
