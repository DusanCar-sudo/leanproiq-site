#!/usr/bin/env python3
"""Adds the two promo cards to the Aura Code site.

Run from the site folder (the one that holds index.html), after copying this kit's
assets/ and energy-node/ folders into it:

    python3 apply_ads.py            # edits index.html, keeps index.html.bak
    python3 apply_ads.py --check    # only reports what it would do

It inserts promo.css at the end of the page's <style> block and promo.html right after
the hero section. Running it twice does nothing the second time.
"""
import pathlib, shutil, sys
here = pathlib.Path(__file__).resolve().parent
page = pathlib.Path("index.html")
if not page.exists():
    sys.exit("index.html not found here. Run this from the site folder.")
src = page.read_text(encoding="utf-8")
if 'id="more"' in src and "promo-card" in src:
    sys.exit("The promo cards are already in index.html. Nothing to do.")
css = (here / "promo.css").read_text(encoding="utf-8")
block = (here / "promo.html").read_text(encoding="utf-8")
anchor = "<!-- MISSION -->"
if anchor not in src or "</style>" not in src:
    sys.exit("index.html does not look like the Aura Code page (no MISSION marker or <style>). Nothing changed.")
out = src.replace("</style>", css + "</style>", 1).replace("  " + anchor, block.strip("\n") + "\n\n  " + anchor, 1)
if out.count("promo-card") < 2:
    sys.exit("Insertion failed. Nothing changed.")
missing = [p for p in ("assets/energy-node.jpg", "assets/lean-robotics.jpg", "energy-node/index.html") if not pathlib.Path(p).exists()]
if "--check" in sys.argv:
    print("OK to apply." + (" Missing files to copy first: " + ", ".join(missing) if missing else ""))
    sys.exit(0)
shutil.copyfile(page, "index.html.bak")
page.write_text(out, encoding="utf-8")
print("Promo cards added. Backup saved as index.html.bak.")
if missing:
    print("Copy these from the kit before deploying: " + ", ".join(missing))
