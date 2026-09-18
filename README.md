# Structural System Matrix

A weighted decision matrix for choosing the structure of a mid-rise building over a
reinforced-concrete podium and one level of parking basement. It compares five systems
for the storeys above the podium:

| System | Above the podium |
|---|---|
| Wood Frame | Light wood-frame bearing walls, I-joist or open-web floors |
| Concrete | RC flat-plate slabs with RC columns |
| Mass Timber | Glulam post-and-beam with CLT floors |
| Hybrid 1 | Steel columns with point-supported CLT floor panels — no beams |
| Hybrid 2 | Load-bearing steel-stud walls with CLT floor panels |

**Live:** https://kenttp.github.io/structural-system-matrix/

## What it does

- Rates each system **1 (worst) to 5 (best)** on ten criteria: foundations, basement
  tanking (buoyancy), speed of construction, MEP flexibility, acoustics, aesthetics,
  encapsulation (fire), government grants (GWP), biophilic design, and a renamable
  "Other" row. Every rating carries an editable rationale note.
- Each criterion can be **switched on or off** and given a **weight (1–5)**. The weighted
  score is Σ(weight × rating) ÷ Σ weight, shown live as a ranked bar chart.
- A **cost rating** ($ to $$$$$) sits under each system and can be folded into the score
  (cheaper counts higher).
- The **storeys above grade** control applies the BC Building Code height tiers: wood frame
  is excluded above 6 storeys, and the mass timber and hybrid options move through the
  encapsulated mass timber (EMTC) tiers — 0-minute encapsulation to 8 storeys (Group C) or
  9 (Group D), 50-minute to 12, 70-minute to 18 — with the Encapsulation row re-rated
  automatically. A reference table lists the tiers with article numbers and sources.
- Custom criteria can be added; state persists in the browser and can be shared as a link
  (`Copy share link` encodes the whole matrix in the URL); `Copy table` pastes into Excel.

The default ratings and notes are Sense Engineering's structural view for a Metro
Vancouver site. Cost ratings are relative placeholders — confirm them with a quantity
surveyor before quoting.

## Code basis

BC Building Code 2024, Revision 1 (in force 10 April 2024), adopted in the Vancouver
Building By-law 2025 (in force 15 September 2025):

- Light wood frame: 6 storeys and 18 m to the top floor — Articles 3.2.2.50 (Group C) and
  3.2.2.58 (Group D), sprinklered.
- EMTC: Table 3.2.2.93 and Articles 3.1.6.4–3.1.6.9 (encapsulation ratings, exposed timber
  allowances, cladding). 12-storey provisions in Articles 3.2.2.48 / 3.2.2.57.
- High-building provisions (Subsection 3.2.6) are flagged per Article 3.2.6.1: Group C once
  the top floor is above 18 m; Group D above 36 m, or above 18 m only where the exit-width
  test fails. The app maps these to about 7 and 11 storeys respectively.
- Embodied carbon: VBBL 2025 (Section 10.4) requires a 20 % reduction for new Part 3
  buildings of up to 6 storeys that can be built in wood and 10 % for all others — a target
  set by building class, not by the material chosen, so a low-rise concrete scheme carries
  the 20 % target too.
- Sources are linked at the bottom of the page. Confirm the applicable edition, occupancy
  mix and any alternative solutions with the authority having jurisdiction.

## Repository layout

```
src/template.html   the page — all HTML, CSS and JavaScript, with two logo placeholders
brand/              Sense logo artwork (PNG, light and dark variants)
build.py            fills the placeholders and writes index.html (and dist/artifact.html)
index.html          built output served by GitHub Pages — do not edit by hand
```

The logos are embedded as bytes and painted onto `<canvas>` elements rather than loaded as
images, so the page also renders inside sandboxed viewers that block image URLs.

## Build

```bash
python build.py
```

Python 3 standard library only; no dependencies. Open `index.html` directly or serve the
folder with any static server. To change the default ratings, notes or systems, edit
`DEFAULT_CRITERIA`, `DEFAULT_COST` and `SYSTEMS` in `src/template.html` and rebuild. If
you change defaults, bump the `KEY` constant (`ssm-state-v3`) so browsers that saved the
old defaults pick up the new ones.

## Deploy

GitHub Pages serves `index.html` from the root of `main`. Any static host works the same
way — the whole tool is one file.
