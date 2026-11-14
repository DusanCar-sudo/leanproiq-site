# Promo cards for the Aura Code site (leanproiq.com)

Adds an "Also from Lean Progress IQ" band right after the hero, with two cards:

- **Aura Energy Node** links to `energy-node/` on the same site.
- **Lean Robotics IQ** links to https://leanroboiq.online.

## Apply

From the Aura Code site folder (the one with `index.html` that is deployed to Vercel):

1. Copy `assets/energy-node.jpg` and `assets/lean-robotics.jpg` into the site's `assets/`.
2. Copy this branch's root `index.html` to `energy-node/index.html` in the site folder.
3. Run `python3 apply_ads.py` (it keeps `index.html.bak`; `--check` only reports).
4. Deploy as usual: `vercel --prod`.

`promo.css` and `promo.html` are the inserted pieces if you would rather paste them by hand.
