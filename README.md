# Mosquito Alert website

The future home of [www.mosquitoalert.com](https://www.mosquitoalert.com) as a static site generated with [Hugo](https://gohugo.io) and hosted on GitHub Pages, replacing the current WordPress site.

**Status (November 2026):** the migration is being contracted. The specification for quotation is in [`bid-phase1/`](bid-phase1/): quotations for work packages 1 and 2 (migration pipeline; theme and site build) are due Friday 13 November 2026, 12:00 CET. Package 3 (page conversion) will be requested in December, and package 4 (launch) after the Phase 2 redesign: the current site stays live until then. The `main` branch holds the specification and will receive the contractor's work. A Hugo scaffold that the project team started in 2025 is kept, frozen, on the [`scaffold-2025`](https://github.com/Mosquito-Alert/website/tree/scaffold-2025) branch; bidders may use it as a starting point or ignore it (see Appendix C of the specification).

## The project in two phases

| Phase | What | Status |
|---|---|---|
| 1. Migration | Move the current site to Hugo: same content, URLs, navigation and languages, on a plain theme (the current look is not reproduced) | Specification published; quotations for WP1–2 due 13 Nov 2026 |
| 2. Redesign | Restructure the site, apply the new Mosquito Alert visual identity, then launch | 2027, separate contract |

## Repository layout

| Path | Contents |
|---|---|
| `bid-phase1/` | Phase 1 specification (Markdown and PDF) and `url_inventory.csv`, the public URLs of the current site |
| `tools/spec-build/` | Builds the specification PDF from its Markdown source |
| branch `scaffold-2025` | The 2025 Hugo scaffold: configuration for the three languages, home, blog and taxonomy layouts, a first export converter and 30 test posts. Frozen; optional starting point, with its own README |

The media files of the current site (1.46 GB) and the WordPress export are **not** in this repository; they are handed to the contractor at kick-off.

## Licence

Code and templates: [GPL-3.0](LICENSE). The specification documents in `bid-phase1/` are CC BY 4.0. Site content and images belong to Mosquito Alert and its authors and are not covered by these licences.
