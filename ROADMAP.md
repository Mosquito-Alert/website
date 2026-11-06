# Mosquito Alert Website Migration Roadmap

## Goals
- Preserve existing URLs, multilingual content, and visual identity while moving off WordPress.
- Enable communications staff to publish posts and update landing pages without developer involvement.
- Establish a reproducible, version-controlled workflow using Hugo for generation and Decap CMS for editing.
- Prepare for future enhancements (design refresh, new content types) without interrupting the current site.

## High-Level Approach
1. **Audit & Inventory**: Map current WordPress structure (permalinks, languages, custom post types, taxonomies, media usage).
2. **Export Content & Assets**: Extract WordPress data into structured formats suitable for Hugo.
3. **Build Static Clone**: Recreate the existing site visuals and navigation in Hugo using the exported content.
4. **Layer Editorial UI**: Configure Decap CMS for multilingual posts and landing-page editing.
5. **Automate Delivery**: Set up CI/CD, automated link checks, previews, and deployment workflows.
6. **Transition Plan**: Validate the static clone, coordinate content freeze, switch DNS, and schedule follow-up improvements.

## Suggested Timeline (Iterate as Needed)
- **Week 0-1**: Access WordPress backend, content audit, select tooling.
- **Week 1-2**: Export proof-of-concept (subset of posts + landing page), prototype Hugo build.
- **Week 2-3**: Implement multilingual templates, replicate navigation, configure Decap CMS collections.
- **Week 3-4**: Automate exports, wire up media handling, create editorial training materials.
- **Week 4-5**: QA, link checking, SEO verification, performance testing, deployment rehearsal.
- **Week 5**: Content freeze, final sync, launch, and post-launch monitoring.

## WordPress Export Strategy
- **Primary Recommendation**: Use WP-CLI `wp export` or the built-in WordPress XML export to pull posts, pages, custom post types, media metadata, taxonomies, and menus. Combine with `wp media export` to collect attachments.
- **Structured Data Option**: Install WPGraphQL and use a scripted fetch (Node/Python) to export content as Markdown (for rich text) plus YAML/JSON front matter. This ensures consistent multilingual fields and custom fields.
- **Static Snapshot**: Run `wget`/`httrack` or plugins like Simply Static to capture ISO copies for reference and diffing; treat as validation artifacts rather than primary content sources.
- **Hugo-Focused Tools**: Evaluate WordPress-to-Hugo exporter plugins (e.g., wp2static-hugo, Hugo WP Exporter). They can auto-convert posts to Markdown with front matter but still review output for taxonomy, language tags, and shortcodes.
- **Media Handling**: Export the `/wp-content/uploads` directory directly (SFTP, rsync, or plugin) to maintain original paths and filenames; plan to place it under `static/uploads`.
- **Redirect Inventory**: Extract the WordPress permalink settings and any custom redirects (`.htaccess`, Redirection plugin) to replicate or translate into Hugo's `aliases` and hosting-level rules.

## Hugo Implementation Outline
- **Config**: Use `config/_default/config.toml` (or YAML) with multilingual setup (`defaultContentLanguage`, `languages`, `permalinks`) mirroring WordPress slugs.
- **Content Structure**: Organize Markdown by language, e.g., `content/en/blog`, `content/es/blog`. Include front matter fields for SEO metadata, author info, featured images, and translation mapping (`translationKey`).
- **Layouts**: Convert WordPress theme templates into Hugo layouts and partials. Keep shared elements (`header`, `footer`, nav) in `layouts/partials`. Reuse existing CSS/JS under `assets/` and `static/` directories.
- **Multilingual**: Use Hugo's built-in `i18n/` directory for UI strings and `relref` for cross-language navigation. Validate that language switcher URLs match WordPress conventions.
- **Shortcodes**: Create Hugo shortcodes for any WordPress blocks/shortcodes that appear in content (maps, galleries, embeds) to maintain rendering fidelity.
- **Testing**: Establish `scripts/` for automation (e.g., exporting, diffing HTML snapshots, running link checkers like `html-proofer`).

## Decap CMS Configuration Plan
- **Admin Interface**: Place configuration in `decap/admin/config.yml`, hosted at `/admin` via Netlify or similar. Protect with authentication (Netlify Identity, Git Gateway, or custom OAuth).
- **Collections**:
  - Blog posts per language (or a single collection with language field). Configure custom widgets for translation pairs, tags, authors.
  - Landing pages as structured content with repeatable sections. Consider using nested/nested-lists widgets to allow editors to manage hero content, CTAs, screenshots.
  - Global settings (navigation, footer links, contact info) via singleton collections stored in `data/` files.
- **Media Library**: Point Decap to `static/uploads/`. Enable image previews and consider adding an image processing pipeline (Hugo image processing with `resources.Get`).
- **Editorial Workflow**: Enable editorial workflow (draft/review/publish) so communications staff can preview and request approval. Provide training docs/videos.

## Automation & Deployment
- **Repository Structure**: Keep the Hugo project versioned on GitHub. Store scripts, Decap config, and import tooling alongside the content; use branches + pull requests for every migration milestone.
- **CI/CD**: Configure a GitHub Actions workflow that checks out with `lfs: true`, installs Hugo Extended, runs `hugo --minify`, and deploys via `actions/upload-pages-artifact` + `actions/deploy-pages` to GitHub Pages.
- **Preview Links**: Enable branch deploy previews using GitHub Pages’ “Preview” environments or third-party tooling (e.g., Cloudflare Pages, Netlify) for editorial review before merges.
- **Redirects & Headers**: If you need custom headers/redirects later, commit `_headers` / `_redirects` in `static/` and serve through a CDN (Cloudflare/Netlify proxy) or add rules at your DNS/CDN layer.
- **Monitoring**: After launch, set up GitHub Pages status notifications, integrate with Google Search Console, and schedule Lighthouse/link-check runs in CI.

## GitHub Pages Hosting Notes
- GitHub Pages serves the static files produced by the Actions workflow; keep `static/uploads/` tracked with Git LFS so `actions/checkout` retrieves originals for each build and Hugo outputs them under `public/uploads/`.
- GitHub’s Pages bandwidth is generous for public projects, but LFS bandwidth/storage (1 GB each on free accounts) may require paid upgrades or an external asset bucket if the media library grows.
- Configure Decap’s `media_folder` to `static/uploads` so new uploads automatically get tracked by LFS (ensure collaborators have Git LFS installed locally).
- Document the publish path: Decap commit → pull request → Actions build (with link checks) → Pages deployment. Provide guidance for emergency manual deploys by running `hugo` locally and pushing the `gh-pages` branch if Actions is unavailable.

## Immediate Next Steps
- Obtain WordPress backend access; export a pilot dataset (one blog post per language and a landing page) via WP-CLI or WPGraphQL.
- Confirm permalink structure and language handling (directories vs subdomains) to encode in Hugo config.
- Set up repository, run `hugo new site` (or use this scaffold) to initialize the project, and commit baseline structure.
- Draft the initial `config/_default/config.toml` with site metadata and language definitions.
- Prototype Decap `config.yml` for the blog collection, including translation fields and media settings.
- Schedule an editorial workshop to validate the Decap UI and gather feedback before migrating all content.
