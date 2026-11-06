# Mosquito Alert website

The future home of [www.mosquitoalert.com](https://www.mosquitoalert.com) as a static site generated with [Hugo](https://gohugo.io) and hosted on GitHub Pages, replacing the current WordPress site.

**Status (November 2026):** the migration is being contracted. The specification for quotation is in [`bid-phase1/`](bid-phase1/): quotations for work packages 1 and 2 (migration pipeline; theme and site build) are due Friday 13 November 2026, 12:00 CET, and packages 3 and 4 (page conversion; launch) will be requested in December. This repository holds a scaffold that the project team started in 2025; bidders may use it as a starting point or ignore it (see Appendix C of the specification).

## The project in two phases

| Phase | What | Status |
|---|---|---|
| 1. Migration | Move the current site to Hugo as it is: same content, URLs, navigation and languages, essentially the same look | Specification published; quotations for WP1–2 due 13 Nov 2026 |
| 2. Redesign | Restructure the site and apply the new Mosquito Alert visual identity | 2027, separate contract |

## Repository layout

| Path | Contents |
|---|---|
| `bid-phase1/` | Phase 1 specification (Markdown and PDF) and `url_inventory.csv`, the public URLs of the current site |
| `config/_default/config.toml` | Hugo configuration: three languages (Spanish at the root, `/ca/`, `/en/`), permalinks, Spanish main menu |
| `content/` | Content per language (`content/es`, `content/ca`, `content/en`). Only 30 test posts so far |
| `layouts/`, `assets/`, `i18n/`, `data/` | The scaffold theme: home page sections, blog list and post, taxonomy pages, header, footer |
| `scripts/` | A first WordPress-export converter (`wxr_to_hugo.py`) and helper scripts |
| `decap/` | Placeholder Decap CMS configuration (not in use) |
| `tools/spec-build/` | Builds the specification PDF from its Markdown source |
| `.github/workflows/deploy.yml` | GitHub Pages deployment, switched off (manual trigger only) until the migration is done |

The media files of the current site (1.46 GB) and the WordPress export are **not** in this repository; they are handed to the contractor at kick-off. Images are therefore missing when the scaffold is built.

## Building locally

Install [Hugo extended](https://gohugo.io/installation/) (0.125 or later) and run:

```sh
hugo server
```

## Licence

Code and templates: [GPL-3.0](LICENSE). The specification documents in `bid-phase1/` are CC BY 4.0. Site content and images belong to Mosquito Alert and its authors and are not covered by these licences.
