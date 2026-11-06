# Specification build

Turns the Markdown specification into a designed web page and a PDF.

| Source (edit this) | PDF (generated) | Web page (generated) |
|---|---|---|
| `bid-phase1/MosquitoAlert_Website_Phase1_Specifications.md` | `bid-phase1/MosquitoAlert_Website_Phase1_Specifications.pdf` | `tools/spec-build/out/mosquitoalert-phase1-spec.html` |

Run `./tools/spec-build/build.sh`. It needs pandoc, python3 and node. The first run installs `playwright-core`. If Chromium is missing, run `npx playwright-core install chromium` in this folder.

**Header facts are not read from the Markdown.** The title, dates, work period and "at a glance" boxes at the top of the page are set in `CFG` in `build_web.py`. If you change those facts in the Markdown, update them there too. The requirement counts and the PDF footer version are read from the Markdown automatically.

The tooling was first written for the H-MIP project (github.com/h-mip) and is reused here unchanged apart from the configuration.
