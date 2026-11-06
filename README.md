# Mosquito Alert website: the 2025 Hugo scaffold

This branch holds the Hugo scaffold that the project team started in October 2025, frozen as it was when the Phase 1 specification for quotation was published in November 2026. It is an **optional** starting point for the contractor: see Appendix C of the specification, in `bid-phase1/` on the `main` branch. There is no obligation to use it and no advantage in the evaluation either way.

It contains:

- A Hugo configuration with the three languages (Spanish at the root, `/ca/`, `/en/`), the permalink scheme for posts and events, and the Spanish main menu copied from WordPress.
- Layouts for the home page (sections driven by data files), blog list and single post, taxonomy pages, a header with menu toggle and language menu, and a footer driven by data files.
- A first WordPress-export converter (`scripts/wxr_to_hugo.py`) that writes front matter and the HTML body verbatim, used to import 30 test posts, and a script that profiles the export.
- A placeholder Decap CMS configuration and a GitHub Actions workflow (manual trigger only).

Known gaps are listed in Appendix C of the specification. Build with [Hugo extended](https://gohugo.io/installation/) 0.125 or later:

```sh
hugo server
```

Images are missing because the media files of the current site are not in this repository.

Licence: [GPL-3.0](LICENSE).
