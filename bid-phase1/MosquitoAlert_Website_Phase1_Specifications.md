# Mosquito Alert Website — Phase 1 Specifications for Quotation

**Version:** 1.0 · **Date:** 6 November 2026
**Client:** Mosquito Alert, Universitat Pompeu Fabra (UPF)
**Contact:** John Palmer, john.palmer@upf.edu
**Reference site:** [www.mosquitoalert.com](https://www.mosquitoalert.com) (the current WordPress site, which this project replaces)
**Attachments:** `url_inventory.csv`, the list of the 2,204 public URLs of the current site; the public repository `Mosquito-Alert/website`, whose `scaffold-2025` branch is an optional starting point (Appendix C)

---

## 1. Summary

We want to move the public website of Mosquito Alert, [www.mosquitoalert.com](https://www.mosquitoalert.com), from **WordPress** to a **static site generated with Hugo and hosted on GitHub Pages**, so that the project team can maintain it by editing files in a Git repository, without WordPress, plugins or a hosting provider.

**Phase 1, this request, migrates the current site**: the same content, URLs, navigation and languages, presented with a plain, functional theme. It is a migration, not a redesign, and it does **not** reproduce the look of the current site. The migrated site lives on a preview address; a later **Phase 2**, contracted separately, will restructure and restyle it under a new visual identity, and only then will it replace `www.mosquitoalert.com`. Phase 1 must therefore separate content, structure and styling cleanly, so that Phase 2 is a redesign of the theme and not a second migration.

The site is used by people around the world: schools, journalists, public-health staff, researchers and the users of the Mosquito Alert app, and it is linked from scientific papers and from the app. **Links must keep working** (section 6.1).

The work is divided into four work packages (section 4). **This request asks for binding quotations for work packages 1 and 2** (the content migration pipeline, and the theme and site build), to be delivered on a preview site by **11 December 2026** and accepted and invoiced by **18 December 2026**. Work package 3 (conversion of the page-builder pages) will be requested separately in December for January–February 2027, and work package 4 (launch) after Phase 2. Both are described here so that you can see the whole; no prices are requested for them. Quotations are due by **Friday 13 November 2026, 12:00 CET** (section 12).

| At a glance | |
|---|---|
| What | Migration of an existing multilingual WordPress site (about 600 blog posts, 200 pages, 85 FAQ items, 160 past events, 1 GB of media) to Hugo on GitHub Pages, keeping its URLs |
| Design | A plain, functional theme with the current logo and colours (TECH-12). The look of the current site is not reproduced; Phase 2 redesigns the site before it goes live |
| Visitors enter data? | Only a newsletter sign-up, handled by Mailchimp. No contact forms, comments or accounts |
| Server / backend | **None.** A static site on GitHub Pages, built by GitHub Actions |
| Languages | Spanish (default, at the root), Catalan (`/ca/`), English (`/en/`) |
| Licence | GPL-3.0, in a public repository of the Mosquito-Alert GitHub organisation |
| Starting point | Optional: a Hugo scaffold started by the project team, on the `scaffold-2025` branch of the public repository (Appendix C) |
| Work period | WP1 and WP2: Mon 23 Nov – Fri 11 Dec 2026, accepted and invoiced by Fri 18 Dec. WP3: January–February 2027, separate request. WP4 (launch): after Phase 2 |
| Price | A fixed price for WP1 and a fixed price for WP2, **excluding VAT**, with VAT shown separately, plus a price for each option. No prices for WP3, WP4 or Phase 2 |

Each requirement has one priority: **MUST** (required) or **SHOULD** (expected; tell us if dropping it would lower the price). Optional items marked **OPT** are priced separately. Requirement IDs (e.g. `URL-03`) are there so you can refer to them in your quotation. The **WP** column says which work package a requirement belongs to.

---

## 2. Background

[Mosquito Alert](https://www.mosquitoalert.com) is a citizen-science project that tracks disease-carrying mosquitoes with the help of volunteers, who report mosquitoes, bites and breeding sites with a mobile app. It is coordinated by research centres in Catalonia (CEAB-CSIC, UPF, CREAF and ICREA) and works with public-health authorities, schools and research groups across Europe and beyond.

The website was built on WordPress in 2014, with the Avada theme and its page builder (Fusion Builder), WPML for the three languages, and a dozen plugins, and it has been extended and updated since, through 2026. It is maintained by an external provider, and the team has limited control over it. The site has grown to about 600 blog posts, 200 pages, an FAQ section and an events calendar that stopped in 2018, with about 1.4 GB of uploaded media. The team prefers to work with static sites and Git, as it already does for its other web properties, and wants a site that it can update, back up and restyle itself.

Phase 1 moves the content as it is, onto a plain theme. Phase 2 (2027, separate contract) will reorganise the content and apply a new visual identity that has already been drafted, and the new site will replace `www.mosquitoalert.com` only when Phase 2 is done. Section 4.3 explains what Phase 1 must do to prepare for it.

---

## 3. Timeline

| Date | Step |
|---|---|
| Until Wed 11 Nov 2026, 12:00 CET | Questions by email to john.palmer@upf.edu. Answers are shared with all bidders. |
| **Fri 13 Nov 2026, 12:00 CET** | **Quotation deadline for WP1 and WP2** |
| Wed 18 Nov | Decision communicated |
| Mon 23 Nov | Kick-off call (1 hour). The project team hands over the WordPress export, the media files, the URL inventory and access to the repository (section 9). |
| **Fri 11 Dec** | **Milestone 1: WP1 and WP2 delivered.** The migration pipeline runs end to end. A preview site shows all blog posts, FAQ items and events with the home, blog and page templates in the three languages. Pages are migrated but not yet converted (that is WP3). |
| Wed 16 Dec | The project team sends one consolidated round of feedback on WP1 and WP2 |
| **Fri 18 Dec** | **Acceptance of WP1 and WP2 confirmed by the project team, and invoices submitted** |
| Mid-December | Request for quotations for WP3 (this document, updated), with about two weeks to reply |
| January–February 2027 (indicative) | WP3: conversion of the pages (about four weeks); **Milestone 2** (the complete site on the preview address, with the URL check report); one review round; acceptance; one month of bug fixes |
| Until Thu 18 Feb 2027 | Bug fixes on WP1 and WP2 at no extra cost |
| 2027, after Phase 2 | Phase 2 (restructuring and redesign, separate contract) works on the preview site. Then WP4: content freeze and final pipeline run, **launch** at `www.mosquitoalert.com`, and the old site kept at a fallback address for three months |

Each work package is invoiced when it is accepted. **WP1 and WP2 must be accepted and invoiced in 2026**, by 18 December. Payment follows UPF's standard procedures after the invoice is accepted; UPF will tell the selected contractor what invoicing requirements apply. Please confirm in your quotation that you can meet these dates. The current WordPress site stays in production, and keeps receiving new posts, until the launch.

---

## 4. Scope

### 4.1 Work packages

| WP | Work package | Contents | Due |
|---|---|---|---|
| **WP1** | **Content migration pipeline** | A documented, re-runnable pipeline that turns the WordPress export and media folder into Hugo content: posts, pages, FAQ items, events, taxonomies, translation links, media at their original paths, and the redirect map (sections 6.1, 6.2) | 11 Dec 2026 |
| **WP2** | **Theme and site build** | The Hugo theme: layouts, shortcodes, navigation, header and footer, blog and taxonomy templates, search, newsletter sign-up, analytics with consent, metadata, build and deployment (sections 6.4–6.9, 7) | 11 Dec 2026 |
| **WP3** | **Conversion of the page-builder pages** | The 192 pages built with Fusion Builder, converted to the shortcodes of WP2 (section 6.3) | Jan–Feb 2027, separate request |
| **WP4** | **Launch and handover** | Content freeze run, URL check report against production, switchover of `www.mosquitoalert.com`, old-site fallback, documentation and handover (section 10) | After Phase 2 (2027), separate request |

WP2, WP3 and WP4 depend on the content model that WP1 produces, and WP3 uses the shortcodes that WP2 implements (TECH-11). Appendix A fixes that model so that packages can be awarded separately. **This request is for WP1 and WP2.** If you quote for only one of them, say which. Their bidders will be invited to quote for WP3 in December, without any guaranteed right to it.

### 4.2 In scope

- **WP1 and WP2 (this request):** sections 6.1, 6.2, 6.4–6.9 and 7, and section 8 as it applies to the templates, deployed to a preview site, with documentation. The pipeline runs on the kick-off export.
- **WP3 (later request):** section 6.3, on the preview site.
- **WP4 (after Phase 2):** the content-freeze run of the pipeline, the switchover to `www.mosquitoalert.com` and the old-site fallback (section 10).
- The three languages, with the language switcher taking visitors to the translated page where one exists.

### 4.3 Looking ahead: Phase 2

Phase 2 will restructure the site and apply a new identity (new logo, colour palette, typography and iconography, already drafted), and the site will replace `www.mosquitoalert.com` only when Phase 2 is done. Phase 1 therefore does not need to look like the current site, and no time should be spent matching it (TECH-12). What Phase 1 must do is make Phase 2 easy: keep content free of presentation (no inline styles, no theme-specific HTML in content files), express colours, fonts and spacing as design tokens in one place, build pages from a small set of named components (TECH-04, PAGE-03), and keep the theme separable from the content and the pipeline, so that a designer can restyle or replace it without touching either. Phase 2 is **not part of this request**, and no prices or proposals for it are requested.

### 4.4 Out of scope

- A new design (that is Phase 2), new content, translations, or rewriting existing texts. Content is migrated as it is, including its errors.
- Contact forms (the three pages that embed one get email links instead, COMM-02), comments (the 19 existing comments are not migrated), user accounts, and the events calendar as a live feature (events become a static archive, MIG-06).
- The WordPress site itself: the contractor does not need, and will not get, access to the WordPress administration. All input comes from export files (section 9).
- Other Mosquito Alert web properties linked from the site: the public map (`map.mosquitoalert.com`), the education site (`edumosquitoalert.com`), the data portal, the app stores. Links to them are kept as they are.
- Paid services. The base scope must run on GitHub's free tier.

---

## 5. The current site

The live site is the content reference for Phase 1 (its design is not reproduced, section 4.3). Browse it; the numbers below are from its sitemaps (5 November 2026) and from the WordPress export of 30 October 2025. Appendix B has the full inventory.

| Content | Count | Notes |
|---|---|---|
| Blog posts | 607 URLs (es 219, ca 214, en 174) | 2014–2026; 20–50 new posts a year. Standard HTML with image captions, galleries and embedded YouTube videos, tweets and issuu documents |
| Pages | 206 URLs (es 62, ca 61, en 83) | 192 of 211 published pages are built with Fusion Builder, using about 20 element types (Appendix B). Up to three levels deep (e.g. `/proyectos-cientificos/aim-cost/`) |
| FAQ items | 87 URLs, in 5 categories | Shown as accordions on one FAQ page per language |
| Events | 162 URLs | A calendar that ended in 2018, with venues and organisers |
| Blog category and tag archives | 51 + 1,068 URLs | Linked from every post |
| Author pages | 8 | |
| Menus | 3 main menus of 35–38 items, two levels deep; 7 smaller top-bar and footer menus per language | |
| Media | 2,790 original files, 1.46 GB, at `/wp-content/uploads/YYYY/MM/` | 971 files (610 MB) are referenced by published content; 251 PDFs (474 MB); no file over 25 MB. The copy supplied contains originals only; the content also references 839 scaled variants (e.g. `-1024x768.jpg`) that WordPress generated (MIG-04) |
| Dynamic features | Site search; newsletter sign-up (Mailchimp for WordPress); 3 pages with a Contact Form 7 form; Google Analytics 4 | Fonts: Roboto and Open Sans (Google Fonts); Font Awesome icons |
| Platform | WordPress 6.0, Avada 7.2 with a custom child theme, WPML 4.5, Yoast SEO, W3 Total Cache, The Events Calendar, Avada FAQ | |

URL scheme: Spanish at the root (`/`), Catalan under `/ca/`, English under `/en/`. Posts are `/<slug>/` directly under the language root; pages are nested by section; the blog index is `/blog/`; categories and tags are `/blog/category/<slug>/` and `/blog/tag/<slug>/`; FAQ items are `/faq-items/<slug>/`; events are `/agenda/<slug>/` in all three languages; feeds are `/feed/`. Media URLs have no language prefix.

---

## 6. Functional requirements

### 6.1 URLs and redirects (URL)

The attached `url_inventory.csv` lists every public URL of the current site with its type and language. Each type is treated as follows:

| Tier | URL types | Treatment |
|---|---|---|
| **1. Keep identical** | Home pages, blog posts, pages, FAQ items, blog indexes, media files referenced by content, all documents (PDF and similar) | Same path, same content |
| **2. Generate** | Blog category and tag archives, events and the events index, scaled image variants | Same path, generated by Hugo; archives marked `noindex, follow` |
| **3. Redirect** | Anything in tiers 1–2 that cannot keep its path, plus pages the project team decides to drop (listed at kick-off, e.g. `/en/sample-page/`) | HTML redirect page to the closest equivalent, listed in the redirect map |
| **4. Let go** | Author pages, FAQ-category and element-category archives, WordPress query URLs (`/?p=`, `/?page_id=`), paginated archive pages (`/page/N/`), `/wp-json/`, `/xmlrpc.php` and other WordPress endpoints | The custom 404 page |

| ID | WP | Priority | Requirement |
|---|---|---|---|
| URL-01 | WP1 | MUST | Every tier-1 URL in the inventory resolves (HTTP 200) at exactly the same path on the new site, with the same content. Trailing slashes behave as they do today. |
| URL-02 | WP1 | MUST | Media keep their original paths, `/wp-content/uploads/YYYY/MM/<file>`, for every file referenced by migrated content and for every document (PDF, DOC, XLS, PPT, ZIP other than app installers) in the media folder, whether referenced or not. Images may be recompressed, but keep their file names. |
| URL-03 | WP1 | MUST | Tier-2 URLs exist at their current paths: category and tag archives (`/blog/category/<slug>/`, `/blog/tag/<slug>/`, with the `/ca/` and `/en/` prefixes), events (`/agenda/<slug>/`) and the events index. Archive pages carry `<meta name="robots" content="noindex, follow">`. |
| URL-04 | WP1 | MUST | A **redirect map** (one file, Appendix A) lists every changed or dropped URL with its target. The build turns each entry into an HTML redirect page (`<meta http-equiv="refresh">` plus a canonical link, as Hugo aliases do), since GitHub Pages cannot send HTTP redirects. The project team can add entries by editing the file. |
| URL-05 | WP1 | MUST | WordPress-specific link forms in content are rewritten: scheme and host variants (`http://`, missing `www`) to relative links; links to URLs in the redirect map to their targets; links to scaled image variants to the file that will exist (MIG-04). |
| URL-06 | WP2 | SHOULD | The feed URLs `/feed/`, `/ca/feed/` and `/en/feed/` keep returning a valid RSS feed of the blog. If GitHub Pages makes that impossible, each language has a feed at a stable path (e.g. `/feed.xml`) and the old URL redirects to it. |
| URL-07 | WP1 | MUST | A **URL check script** in the repository requests every URL in the inventory against a given host and reports status, final target and tier. Its report against the preview site is delivered with WP1, and against the production site with WP4 (section 10). |
| URL-08 | WP2 | MUST | A custom **404 page** (GitHub Pages serves one `404.html`) that detects the language from the path, offers site search and links to the home page, blog and FAQ in that language. |
| URL-09 | WP2 | SHOULD | The 404 page and the home page handle WordPress query links in the browser: `/?p=<id>` and `/?page_id=<id>` redirect to the post or page with that WordPress ID (a lookup table generated by WP1), and `/?s=<term>` opens the site search with that term. |

### 6.2 Content migration (MIG)

| ID | WP | Priority | Requirement |
|---|---|---|---|
| MIG-01 | WP1 | MUST | A documented, **re-runnable pipeline** (Python or Node, in the repository) converts a WordPress export file (WXR) and a copy of the uploads folder into Hugo content following Appendix A: published posts, pages, FAQ items and events, with title, publication and modification dates, slug, author name, categories, tags, featured image, excerpt, Yoast SEO title and description, WordPress ID and language. Drafts, private and trashed items are not migrated. |
| MIG-02 | WP1 | MUST | **Translation links.** The export does not say which posts and pages are translations of each other. The pipeline obtains this from the live site (the `hreflang` links that WPML and Yoast print on every page, crawled from the URL inventory, and again for new items at content freeze) and records it as Hugo translation keys, so that the language switcher goes to the translated page where one exists and to the language home page otherwise. |
| MIG-03 | WP1 | MUST | **Post bodies** are converted to Markdown, keeping HTML where Markdown would lose structure (tables, complex figures). WordPress markup becomes Hugo shortcodes: `[caption]` to a figure with caption, galleries to a gallery, YouTube, Vimeo, Twitter/X, SoundCloud and issuu embeds and `[embed]`/`[video]` to embed shortcodes, Fusion gallery markup in posts likewise. No WordPress-, Avada- or plugin-specific classes, inline styles or scripts remain. |
| MIG-04 | WP1 | MUST | **Media processing.** Referenced files are copied to `static/wp-content/uploads/YYYY/MM/` unchanged in name. Raster images are recompressed (same format and dimensions, metadata stripped, visually lossless). References to scaled variants that do not exist in the supplied originals are either regenerated at the same path or rewritten to the original (URL-05); say which you propose. Unreferenced images and the app installer ZIPs are left out, following a keep/drop list from the project team, and the dropped files are handed over as one archive. The published site stays below 900 MB (TECH-01). |
| MIG-05 | WP1 | MUST | **FAQ items** become content with their category, order and anchors, and the FAQ page of each language shows them as accordions grouped by category, as today. |
| MIG-06 | WP1 | MUST | **Events** (2016–2018) become a static archive: one page per event with date, venue and organiser, and an index per language sorted by date. They are not shown in the main navigation unless they are today. |
| MIG-07 | WP1 | MUST | The pipeline is **idempotent and reports changes**: run again with a newer export, it adds, updates and removes content to match, and prints a summary (new, changed, removed items). Items whose WordPress modification date has not changed since the previous run are left untouched, so that pages converted or fixed by hand (WP3) survive a re-run; items changed in WordPress since are listed for re-conversion. It runs at kick-off and at content freeze, and the team can run it later. |
| MIG-08 | WP1 | MUST | Internal links point to the new paths (URL-05); links to other domains, including images hosted on other domains, are left as they are. Attachment pages (`/<slug>/<attachment-slug>/`) are not migrated; links to them point to the file. |
| MIG-09 | WP1 | SHOULD | Embeds of third-party media (YouTube, Twitter/X, issuu, SoundCloud) load only when the visitor clicks a placeholder that shows the thumbnail or title, so pages make no third-party requests on load. |
| MIG-10 | WP1 | MUST | Content checks: the pipeline fails with a clear message if an item lacks a title, slug or language, or if a referenced media file is missing, and lists the items concerned. |

### 6.3 Pages built with Fusion Builder (PAGE)

Of the 211 published pages, 192 are stored as Fusion Builder shortcodes (Appendix B lists the elements and how often they occur). Their content and structure are carried over with a small set of Hugo shortcodes, without Avada; their look is not reproduced (section 4.3).

| ID | WP | Priority | Requirement |
|---|---|---|---|
| PAGE-01 | WP3 | MUST | Each page keeps its content: the same sections in the same order, with the same texts, headings, images, links, buttons, tabs, accordions and embedded media as today. Multi-column arrangements are kept where they carry meaning (e.g. person cards, side-by-side comparisons) and otherwise flattened to one column. Spacing, typography, colours and decoration follow the Phase 1 theme, not the current page. |
| PAGE-02 | WP3 | MUST | A **converter** (part of the pipeline, or a separate script) translates the structural and frequent elements automatically: containers, rows and columns, text, image frames, separators, titles, buttons, list items and checklists, tabs, content boxes, person cards, FAQ, YouTube/Vimeo, and global elements. Rare elements (sliders, testimonials, counters, code blocks, blog element) may be converted by hand or simplified to a static equivalent agreed with the project team. |
| PAGE-03 | WP3 | MUST | Page files contain **editable Markdown or HTML with Hugo shortcodes** (Appendix A). Pasting rendered theme HTML is not acceptable. No Avada or Fusion CSS, JavaScript or class names remain. |
| PAGE-04 | WP3 | MUST | The 18 **global elements** that pages reuse (calls to action, logo strips and similar) are defined once, as shortcodes or partials, and included by name. |
| PAGE-05 | WP3 | SHOULD | The WordPress page template (full width, 111 pages; default, 81; blank, 19) is recorded in front matter (`layout`), and the blank-template pages are shown without header and footer where they are today. Otherwise all pages use the theme's page layout. |
| PAGE-06 | WP3 | MUST | A **conversion report** with one line per page (converted automatically, hand-fixed, simplified, dropped, and the elements that could not be converted). No visual side-by-side review is required; an automated check that every paragraph, image and link of the live page is present in the converted page is a SHOULD. |
| PAGE-07 | WP2 | MUST | The **home pages** (3) are rebuilt as data-driven sections (hero, highlights, app download, latest posts, calls to action, newsletter, partner logos) with the current texts, links and images, which live in data files, as the scaffold already sketches. The layout of the sections follows the Phase 1 theme, not the current home page. |

### 6.4 Blog and taxonomies (BLOG)

| ID | WP | Priority | Requirement |
|---|---|---|---|
| BLOG-01 | WP2 | MUST | Blog index per language at `/blog/` (and `/ca/blog/`, `/en/blog/`) with pagination, showing featured image, date, title and excerpt. |
| BLOG-02 | WP2 | MUST | Post layout: title, date, author name, featured image, body, categories and tags, share links that are plain links (no third-party scripts), and previous/next post. |
| BLOG-03 | WP2 | MUST | Category and tag archive pages at their current paths (URL-03), with the same list layout. |
| BLOG-04 | WP2 | SHOULD | Related posts (same category) at the end of each post. |
| BLOG-05 | WP2 | MUST | An **author** can be set per post as plain text (name), with no author pages. |

### 6.5 Navigation, header and footer (NAV)

| ID | WP | Priority | Requirement |
|---|---|---|---|
| NAV-01 | WP2 | MUST | Main menu per language with the same items, labels, order, two levels and targets as the current WordPress menus (which are in the export), defined in configuration or data files that the team can edit. Items pointing to dropped URLs are removed or retargeted at kick-off. |
| NAV-02 | WP2 | MUST | Header: logo, main menu, language switcher (Spanish, Catalan, English, to the translated page, MIG-02), search link, and the social links and quick links of today's top bar. Its layout follows the Phase 1 theme. |
| NAV-03 | WP2 | MUST | Footer per language with the contents of the current footer: the smaller menus, partner and funder logos, social links, app store badges, newsletter sign-up (COMM-01) and legal links, laid out by the theme. |
| NAV-04 | WP2 | MUST | Mobile navigation (hamburger menu) covering the full menu, usable by keyboard and screen reader. |

### 6.6 Search (SRCH)

| ID | WP | Priority | Requirement |
|---|---|---|---|
| SRCH-01 | WP2 | MUST | Site search per language with a **static index** built at deploy time (e.g. Pagefind), covering posts, pages, FAQ items and events, with results showing title, excerpt and date. No external search service. |
| SRCH-02 | WP2 | SHOULD | The current search URL form `/?s=<term>` keeps working (URL-09). |

### 6.7 Newsletter, contact and social (COMM)

| ID | WP | Priority | Requirement |
|---|---|---|---|
| COMM-01 | WP2 | MUST | Newsletter sign-up with **Mailchimp's embedded form**, posting directly to Mailchimp (the team supplies the form code), with a honeypot field and the current consent text. No server component. |
| COMM-02 | WP3 | MUST | The three pages that embed a Contact Form 7 form get an email link or email address supplied by the team instead. No contact forms anywhere on the site. |
| COMM-03 | WP2 | MUST | Social links (Twitter/X, Facebook, YouTube, RSS, app stores) as plain links with icons served from the site. No social widgets or scripts. |

### 6.8 Analytics and cookies (ANA)

The site currently uses Google Analytics 4 without a consent banner. The team may switch to a cookieless analytics service before kick-off (OPT-03). Quote ANA-02 as a separate line so we can see the saving if it is dropped.

| ID | WP | Priority | Requirement |
|---|---|---|---|
| ANA-01 | WP2 | MUST | The analytics snippet is set from the site configuration (measurement ID supplied by the team) and can be turned off with one setting. Nothing from the analytics provider loads before consent. |
| ANA-02 | WP2 | MUST | A lightweight **cookie-consent banner** in the three languages (accept, reject, link to the cookies policy page), remembered in the browser, that gates analytics. Texts supplied by the team. No consent-management service. |
| ANA-03 | WP2 | MUST | Apart from analytics after consent, the Mailchimp form submission, and third-party media the visitor activates (MIG-09), pages make **no third-party requests**: fonts, scripts, styles and icons are served from the site. Google Fonts are replaced by self-hosted files of the same families. |

### 6.9 Metadata and SEO (SEO)

| ID | WP | Priority | Requirement |
|---|---|---|---|
| SEO-01 | WP2 | MUST | Per page and language: title and description (from the Yoast fields where present, otherwise generated), canonical URL, `hreflang` links between translations and `x-default`, Open Graph and Twitter card tags with the featured image, a default social image, `sitemap.xml` (per language, with an index), `robots.txt` and favicons. |
| SEO-02 | WP2 | MUST | The **preview site** carries `noindex` and a visible "preview" banner until the launch (WP4), so that visitors and search engines are not confused by two sites. |
| SEO-03 | WP2 | SHOULD | Structured data (`Article`) for blog posts, and `BreadcrumbList` for nested pages. |

---

## 7. Technical requirements (TECH)

| ID | WP | Priority | Requirement |
|---|---|---|---|
| TECH-01 | WP2 | MUST | **Hugo (extended), current stable release**, pinned in the build. Static output only: no server-side code, database or accounts. The build fails if the published site exceeds 900 MB or if Hugo reports errors, and completes within the GitHub Pages limits (1 GB site, 10-minute deployment). |
| TECH-02 | WP2 | MUST | Source, content and media live in a **public repository of the Mosquito-Alert GitHub organisation** under **GPL-3.0**, as plain files (**no Git LFS**). Third-party components have GPL-3.0-compatible licences; fonts and icons are licensed for self-hosting. |
| TECH-03 | WP2 | MUST | **GitHub Actions** builds the main branch and deploys it to **GitHub Pages** at a preview address (the `github.io` address or a subdomain the team provides), and is ready to deploy to `www.mosquitoalert.com` (custom domain, HTTPS enforced) with a configuration change at launch (WP4). Previews of pull requests are a SHOULD. |
| TECH-04 | WP2 | MUST | **Separation of content, structure and style.** Content files hold Markdown or HTML with shortcodes and front matter only; layouts and partials hold structure; one stylesheet system holds presentation, with colours, type scale, spacing and breakpoints as CSS custom properties in one tokens file. No inline styles in content, and no content in templates. |
| TECH-05 | WP1 | MUST | The pipeline needs **no access to WordPress**: its inputs are the export file, the uploads folder, the crawled translation links (MIG-02) and the inventory, all provided as files. |
| TECH-06 | WP1 | MUST | The pipeline, converter, crawler and URL check script are in the repository with a README that lets a developer run them from scratch in under an hour. |
| TECH-07 | WP2 | MUST | **Editing without a developer.** A team member can add or edit a post or page and upload an image through the GitHub web interface, following a short editor guide (in English; Spanish is a SHOULD). Changes deploy automatically. |
| TECH-08 | WP2 | SHOULD | Featured and page images are served as responsive, lazy-loaded images processed by Hugo, while the original file keeps its URL (URL-02). |
| TECH-09 | WP2 | SHOULD | A link checker runs in the build (e.g. htmltest or lychee) and fails on broken internal links. |
| TECH-10 | WP2 | MUST | `hugo server` runs the site locally without the migration tooling, and the README says how. |
| TECH-11 | WP2 | MUST | The **shortcodes of Appendix A.3** are implemented in the theme, styled, documented, and shown together on a demo page that is not published in production, so that WP3 can convert pages against them. |
| TECH-12 | WP2 | MUST | **Plain theme.** The Phase 1 theme is simple and functional: the current logo, the current main colours (Appendix B.5), one or two self-hosted open-licence typefaces, and a documented set of components (header, footer, home sections, post, list, page, FAQ, event, search, 404 and the shortcodes of Appendix A.3). It does not reproduce the look of the current site, and no time should be spent matching it. Phase 2 restyles or replaces the theme without touching content, data files or the pipeline. |

---

## 8. Quality requirements (QUAL)

| ID | WP | Priority | Requirement |
|---|---|---|---|
| QUAL-01 | WP2 | MUST | **Responsive** from 360 px phones to large desktop screens. No horizontal page scrolling, except inside tables. |
| QUAL-02 | WP2 | MUST | **Browsers:** the latest two versions of Chrome, Edge, Firefox and Safari (macOS); Safari on iOS 16 or later; Chrome on Android. |
| QUAL-03 | WP2 | MUST | **Accessibility** of templates, navigation, search, banner and shortcodes: WCAG 2.2 level AA, full keyboard operation, visible focus, correct headings and landmarks, sufficient contrast, 200% zoom. Migrated content keeps its existing alt texts. UPF is a public body, so Spanish web accessibility rules apply (RD 1112/2018). |
| QUAL-04 | WP2 | MUST | **Performance:** the home page and a typical blog post score at least 90 in Lighthouse Performance (mobile), with third-party embeds not activated. |
| QUAL-05 | WP2 | MUST | **Languages:** all interface strings live in translation files, and dates are formatted per language. Adding a language means adding files, not changing code. |
| QUAL-06 | WP4 | MUST | **Content fidelity:** the number of published posts, pages, FAQ items and events per language matches the final export, and a sample review (section 10.2) finds no missing text, images, links or embeds. |

---

## 9. What the project team provides

By the kick-off on **Monday 23 November 2026**, unless noted:

1. **The WordPress export (WXR)** of the whole site, and a fresh export at content freeze (WP4, after Phase 2). The export contains unpublished items and author details; it is confidential and only published content is migrated.
2. **A copy of the uploads folder** (2,790 files, 1.46 GB, originals only), the list of files referenced by published content, the keep/drop list for unreferenced files, and the new files at content freeze.
3. **The URL inventory** (attached now), the list of URLs to drop, and decisions on any tier questions within one working day.
4. **Access**: the public repository in the Mosquito-Alert GitHub organisation (Appendix C) and GitHub Pages for the preview site; at launch (WP4), the DNS change (done by the team's DNS administrator, following the contractor's instructions, with the old site kept at a fallback address).
5. **Accounts and texts**: the Mailchimp form code, the Google Analytics measurement ID (or the chosen alternative), the cookie banner and consent texts in three languages, logos in vector form, and email addresses to replace the three forms.
6. **Translations** of any new interface strings within two working days of receiving the string file.
7. **One contact person** (John Palmer), who replies to questions within one working day, and a communications team that does the review rounds (16 December for WP1 and WP2; February for WP3; at launch for WP4) and reports issues in the repository.

---

## 10. Deliverables and acceptance

### 10.1 Deliverables

**WP1 and WP2 (this request), by 11 December 2026:**

1. In the repository: the migration pipeline, the translation-link crawler and the URL check script, with a README that lets a developer run them from scratch (TECH-06), and the content they produce from the kick-off export: posts, pages (migrated, not yet converted), FAQ items, events, the media at their original paths and the redirect map.
2. The theme: layouts, navigation, header and footer, blog and taxonomy templates, search, newsletter sign-up, analytics and consent banner, metadata, the shortcodes of Appendix A.3 with their demo page (TECH-11), and the editor guide (TECH-07), with a README covering local setup, editing content, adding redirects and deployment.
3. The preview site deployed by GitHub Actions (TECH-03, SEO-02), and the URL check report against it (URL-07).
4. A 30-minute handover call, and bug fixes at no extra cost until Thursday 18 February 2027.

**WP3 (later request):** the converted pages and the conversion report (PAGE-06), the complete site on the preview address (Milestone 2), and bug fixes at no extra cost for one month after acceptance.

**WP4 (after Phase 2):** the content-freeze run; the production site at `www.mosquitoalert.com`; the URL check report against production; the archive of dropped media files (MIG-04); a 1-hour handover call; and bug fixes at no extra cost for one month after launch.

### 10.2 Acceptance criteria

A work package is accepted when its MUST requirements are met and the checks below pass. For WP1 and WP2, the checks run on the preview site between 11 and 18 December, leaving aside the pages that WP3 converts; for WP3, they run on the preview site at Milestone 2; for WP4, on the production site at launch.

1. **URLs:** the URL check report shows every tier-1 URL returning 200 with the equivalent content (for WP1 and WP2, pages may still show unconverted content), every tier-2 URL returning 200, every tier-3 URL returning a redirect page to the mapped target, and every tier-4 URL returning the 404 page. The internal link checker reports no broken links.
2. **Content:** counts per type and language match the final export (QUAL-06). The team compares a random sample of 30 posts and 20 pages with the old site and finds no missing text, images, links or embeds.
3. **Languages:** the switcher takes the visitor to the translation on a sample of 20 posts and pages that have one, and to the language home page where there is none.
4. **Independence:** browsing every template type with the network inspector open shows no request to WordPress, Avada, Google Fonts or any third party other than those allowed in ANA-03.
5. **Devices and accessibility:** layouts work at 360 px, 768 px and 1440 px; an automated scan (e.g. axe) of each template type shows no critical or serious issues; the menu, search, banner, tabs and accordions work with the keyboard alone.
6. **Performance:** QUAL-04 is met.
7. **Editing:** a team member, following the editor guide, publishes a test post with an image and edits a page through the GitHub web interface, and the changes appear on the site automatically.
8. **Pipeline:** running the pipeline again on the same export changes nothing (WP1). The content-freeze run (MIG-07) reproduces the site from the fresh export, with the posts added since kick-off present and nothing else changed unexpectedly, as shown by its change report (WP4).

---

## 11. Optional items (price separately)

These may or may not be ordered.

| ID | Option |
|---|---|
| OPT-01 | **Editing interface.** A Git-based CMS for editors (e.g. Sveltia CMS or Decap CMS) with GitHub login, the three languages, image uploads and an editorial (draft/review) workflow, including whatever small authentication helper it needs on a free tier, and its documentation. |
| OPT-02 | **Contact forms** for the three pages that have one today, through a form service with spam protection and a GDPR-compliant privacy text, with no server of our own. Name the service and any cost. |
| OPT-03 | **Cookieless analytics** instead of Google Analytics: set-up and configuration of a privacy-friendly service chosen with the team (e.g. Plausible, Umami or GoatCounter), so that no consent banner is needed. Name the service and any cost. |
| OPT-04 | **Cloudflare in front of GitHub Pages** (free plan), set up for the preview site and reusable at launch: DNS, HTTPS, and server-side redirects generated from the redirect map (Bulk Redirects), so that redirected URLs return HTTP 301 instead of an HTML redirect page. |
| OPT-05 | **Comments archive:** the 19 existing comments shown as static text under their posts. |

---

## 12. How to submit a quotation

Send your quotation by email to **john.palmer@upf.edu** by **Friday 13 November 2026, 12:00 CET**. Please include:

1. **A fixed price excluding VAT for WP1 and for WP2**, with the applicable VAT shown separately (if you are established outside Spain, say whether the reverse charge applies instead), and ANA-02 as a separate line. UPF may award the two packages together or separately, and may award them to different bidders. If you quote for only one, say which. Tell us which SHOULD items you would drop to reduce the price, and by how much.
2. **A price excluding VAT for each optional item** OPT-01 to OPT-05.
3. **Confirmation that you can deliver WP1 and WP2 by 11 December and invoice by 18 December 2026**, and who will do the work between 23 November and 18 December.
4. **Your approach**: Hugo version and theme approach; how the pipeline obtains translation links (MIG-02); how you handle scaled image variants (MIG-04); how the shortcodes of Appendix A.3 (TECH-11) will support the later conversion of the Fusion Builder pages; whether you would start from the scaffold (Appendix C) or from scratch, and why.
5. **2–3 examples** of relevant work, such as WordPress-to-static migrations, Hugo or other static sites, and multilingual or accessible websites, with links.
6. **Assumptions and exclusions.**

We will choose based on: the quality and realism of the approach to keeping URLs working and to the content model, relevant experience, price (compared excluding VAT), and ability to meet the dates.

---

## Appendix A. Content model

This is the interface between the work packages. The contractor for WP1 may propose adjustments at kick-off; once agreed, all packages follow it. Names are suggestions.

### A.1 Repository layout

| Path | Contents |
|---|---|
| `content/es/`, `content/ca/`, `content/en/` | Content per language. Spanish is the default language and is served at the root |
| `content/<lang>/blog/<slug>/index.md` | Blog posts. Permalink `/<slug>/` under the language root, as in WordPress. `content/<lang>/blog/_index.md` is the blog index at `/blog/` |
| `content/<lang>/<section>/.../<slug>/index.md` | Pages, nested as in their URL (`_index.md` for a page that has child pages), e.g. `content/es/proyectos-cientificos/aim-cost/index.md` for `/proyectos-cientificos/aim-cost/` |
| `content/<lang>/faq-items/<slug>.md` | FAQ items, at `/faq-items/<slug>/`, grouped on the FAQ page by the `faq_categories` taxonomy |
| `content/<lang>/agenda/<slug>.md` | Events, at `/agenda/<slug>/`, with an index at `/agenda/` |
| `static/wp-content/uploads/YYYY/MM/` | Media at their original paths |
| `data/redirects.csv` | Redirect map: `from,to,note`. The build turns each line into an HTML redirect page |
| `data/wordpress_ids.json` | WordPress ID to path lookup for URL-09 |
| `data/navigation.yaml`, `data/footer.yaml`, `data/home/<lang>.yaml` | Menus, footer and home page sections per language |
| `i18n/<lang>.yaml` | Interface strings |
| `layouts/`, `assets/css/`, `assets/js/` | Theme. One tokens file (`assets/css/tokens.css`) holds colours, type and spacing |
| `tools/` | Pipeline, converter, crawler and URL check script, with their README |

Taxonomy URLs are set with Hugo's taxonomy permalinks so that categories are `/blog/category/<slug>/` and tags `/blog/tag/<slug>/`.

### A.2 Front matter (YAML)

| Field | Used by | Notes |
|---|---|---|
| `title`, `date`, `lastmod`, `slug`, `draft` | all | `date` is the WordPress publication date; `slug` reproduces the WordPress slug exactly |
| `translationKey` | all | Same value for the translations of one item (MIG-02) |
| `description`, `seo_title` | all | From the Yoast fields; `description` falls back to the excerpt |
| `image` | posts, pages | Featured image path under `/wp-content/uploads/` |
| `author` | posts | Display name as text |
| `categories`, `tags` | posts | Slugs as in WordPress, so archive URLs match |
| `wordpress_id`, `wordpress_url` | all | For traceability and URL-09 |
| `aliases` | any | Additional old paths that should lead here (Hugo generates the redirect pages) |
| `layout` | pages | `full-width`, `default` or `blank` (PAGE-05) |
| `faq_categories`, `weight` | FAQ items | Category slugs and display order |
| `event_start`, `event_end`, `venue`, `organizer`, `event_url` | events | From The Events Calendar fields |

### A.3 Shortcodes

| Shortcode | Replaces | Notes |
|---|---|---|
| `figure` | `[caption]`, image frames | `src`, `alt`, `caption`, `link`, optional size |
| `gallery` | `[gallery]`, Fusion gallery | List of images with optional captions |
| `youtube`, `vimeo`, `tweet`, `soundcloud`, `embed` | Embeds and `[embed]`, `[video]` | Click-to-load placeholder (MIG-09) |
| `row` / `col` | Fusion container, row, column | `col` takes a width fraction (e.g. `1/2`, `1/3`) |
| `box` | Content box, counter box, testimonial | Title, icon or image, text, link |
| `tabs` / `tab` | Fusion tabs | |
| `accordion` / `item` | Fusion FAQ, toggles | Also used by the FAQ page |
| `button` | Fusion button | Label, link, style (primary, secondary), target |
| `person` | Fusion person | Name, role, image, links |
| `checklist` | Fusion checklist, list items | |
| `separator`, `heading` | Fusion separator, title | |
| `include` | Fusion global elements | Includes a named partial (PAGE-04) |
| `document` | Links to PDFs | Title, path, size |

---

## Appendix B. Inventory of the current site

Counts from the live sitemaps (5 November 2026) and the WordPress export of 30 October 2025. The export also contains 103 draft, 11 private and 36 trashed items, which are not migrated.

### B.1 Public URLs, by type and language

| Type | Spanish | Catalan | English | Total | Tier |
|---|---|---|---|---|---|
| Blog posts | 219 | 214 | 174 | 607 | 1 |
| Pages (incl. home) | 62 | 61 | 83 | 206 | 1 |
| FAQ items | 29 | 29 | 29 | 87 | 1 |
| Events | 76 | 43 | 43 | 162 | 2 |
| Blog categories | 17 | 17 | 17 | 51 | 2 |
| Blog tags | 352 | 366 | 350 | 1,068 | 2 |
| FAQ categories | 5 | 5 | 5 | 15 | 4 |
| Author pages | 8 | – | – | 8 | 4 |
| **Total** | | | | **2,204** | |

Blog posts by year of last modification: 2014–2016, 24; 2017, 161; 2018, 93; 2019, 27; 2020, 87; 2021, 40; 2022, 56; 2023, 41; 2024, 22; 2025, 52; 2026 (to November), 4.

### B.2 Content in the export

| Item | Count | Notes |
|---|---|---|
| Published posts | 603 (es 218, ca 213, en 172) | 601 have a featured image; 8 authors |
| Markup in posts | `[caption]` 827; galleries 14; YouTube 52; Twitter/X 19; issuu 8; `[video]` 11; Fusion gallery 6 | Images hosted on other domains: 37 (edumosquitoalert.com, twimg.com, springernature.com and others) |
| Published pages | 211 (es 64, ca 62, en 85) | 192 use Fusion Builder; templates: full width 111, default 81, blank 19 |
| Fusion global elements | 18 | Used 46 times |
| FAQ items | 84 (28 per language) | 5 categories |
| Events | 160 (es 74, ca 43, en 43) | 2016: 27; 2017: 79; 2018: 54; with 60 venues and 17 organisers |
| Menus | 231 items in 24 menus | 3 main menus (es 38, en 36, ca 35 items), plus top-bar, footer and link menus per language |
| Contact Form 7 forms | 10 defined, 3 embedded in published pages | `/ca/ambits-dactuacio/educacio/`, `/en/area-of-activity/education/`, `/webquest-madrid-murcia-girona/` |
| Mailchimp form | 1 | In the footer of every page |
| Comments | 19 | Not migrated (OPT-05) |

### B.3 Fusion Builder elements in published pages

| Element | Occurrences | Suggested treatment (Appendix A.3) |
|---|---|---|
| `fusion_builder_column` | 2,406 | `row` / `col` |
| `fusion_text` | 1,359 | Markdown or HTML |
| `fusion_imageframe` | 1,201 | `figure` |
| `fusion_separator` | 783 | `separator` or dropped |
| `fusion_builder_container` / `fusion_builder_row` | 452 each | `row` |
| `fusion_li_item` | 340 | List items in `checklist` |
| `fusion_button` | 259 | `button` |
| `fusion_tab` / `fusion_tabs` | 158 / 25 | `tabs` / `tab` |
| `fusion_content_box` / `fusion_content_boxes` | 97 / 25 | `box` |
| `fusion_title` | 96 | `heading` |
| `fusion_person` | 69 | `person` |
| `fusion_checklist` | 57 | `checklist` |
| `fusion_global` | 46 | `include` |
| `fusion_blog` | 43 | Latest-posts partial |
| `fusion_social_links` | 43 | Social links partial |
| `fusion_slide` / `fusion_slider` | 27 / 9 | Static `gallery` or first slide (simplification) |
| `[caption]` | 24 | `figure` |
| `fusion_code` | 20 | Raw HTML, reviewed by hand |
| `fusion_faq` | 15 | `accordion` |
| `fusion_youtube` / `fusion_vimeo` | 14 / 1 | `youtube` / `vimeo` |
| `fusion_counter_box` / `fusion_counters_box` | 12 / 3 | `box` (static number) |
| `fusion_builder_column_inner` / `fusion_builder_row_inner` | 12 / 6 | Nested `row` / `col` |
| `fusion_testimonial` / `fusion_testimonials` | 6 / 6 | `box` |
| `[video]`, `[embed]` | 5, 3 | `embed` |

### B.4 Media

| Item | Files | Size |
|---|---|---|
| All files in the uploads folder (originals) | 2,790 | 1,462 MB |
| Referenced by published content | 971 | 610 MB |
| Not referenced | 1,819 | 852 MB |
| Of which PDFs (kept, URL-02) | 185 | 249 MB |
| Of which app installer ZIPs (dropped, redirected to the app stores) | 6 | 154 MB |
| All PDFs | 251 | 474 MB |
| Scaled image variants referenced by content but not in the folder | 839 distinct paths | – |

Estimated published size after processing: 650–750 MB, including recompressed images.

### B.5 Current platform and third-party requests

WordPress 6.0.18; Avada 7.2 with the child theme `mosquitoalert`; Fusion Builder 3.2; WPML 4.5.10; Yoast SEO; W3 Total Cache; Contact Form 7; Mailchimp for WordPress; The Events Calendar; Avada FAQ; GitHub Embed. Third-party requests on page load today: Google Analytics 4 (`G-3YLRH1LLLW`) and Google Fonts (Open Sans; Roboto is also used); YouTube, Twitter/X and issuu on pages that embed them. Main colours in the current stylesheet: yellow `#ffdd18`, dark grey `#333333`, red `#c91d31`, greens `#54770f`, `#65bc7b`, `#a0ce4e`.

---

## Appendix C. The optional Hugo scaffold

In 2025 the project team started a Hugo version of the site. It is kept, frozen, on the **`scaffold-2025` branch** of the public repository **`github.com/Mosquito-Alert/website`** (GPL-3.0); the `main` branch holds this specification and is where the contractor's work will go. You may start from the scaffold, take parts of it, or ignore it; there is no obligation and no advantage in the evaluation either way. It contains:

- A Hugo configuration with the three languages (Spanish at the root), the permalink scheme for posts and events, and the Spanish main menu copied from WordPress.
- Layouts for the home page (hero, highlights, app, latest posts, calls to action, newsletter, partners, driven by data files), blog list and single post, taxonomy pages, a header with menu toggle and language menu, and a footer driven by data files.
- A first WordPress-export converter (`scripts/wxr_to_hugo.py`) that writes front matter and the HTML body verbatim, used to import 30 test posts, and a script that profiles the export.
- A placeholder Decap CMS configuration and a GitHub Actions workflow (deployment switched off in the public copy).

Known gaps, which this specification resolves: the converter does not handle translation links, shortcodes or media; its test copy of the uploads folder was flattened, so media URLs did not match the original paths; media were stored with Git LFS, which the deployment cannot afford; the permalink setting for pages does not support nested pages; and the Decap configuration depends on a service that is being retired. The branch builds with `hugo server`; images are missing because the media are not in the public repository (they are supplied to the contractor, section 9).

---

*Mosquito Alert is coordinated by CEAB-CSIC, UPF, CREAF and ICREA. This specification is published under CC BY 4.0; the website code is GPL-3.0.*
