# Wellness Origin Spa: SEO preview

Private website redesign, separate from the original preview and official business website. 29 published sitemap URL paths preserved, plus a preview note, author utility archive, legacy fallbacks, and custom 404 page. Original logo and images from the user-supplied website snapshot. No AI-generated images.

## Build and verify

Python 3 (standard library only) and Node.js are sufficient:

    python3 build.py
    python3 check.py
    node --check dist/app.js

Static output is `dist/`. No package installation or client framework required. `content.json` contains the retained source summaries and policy wording; `build.py` contains the rewritten page copy. CSS and JavaScript are kept directly in `dist/` and preserved by the generator. Optimized image assets are checked in. `asset-sources.json` records original image filenames.

## Privacy and behavior

The hosted preview is private. Page-level `noindex,follow` is intentional. Its sitemap is intentionally empty to avoid listing non-indexable URLs. Access is enforced by the hosting platform, not robots.txt. No forms submit data, no booking transaction runs, no analytics/tracking pixels load, and no financing application is embedded. Booking continues to the existing official website. The treatment-interest selector stays local to the browser and does not reserve an appointment.

Fine-pointer users get an optional cursor halo, subtle magnetic buttons and hero-image motion. Touch interfaces keep standard controls. All animation respects `prefers-reduced-motion`. Native view transitions are progressive enhancement. Content and navigation remain in source HTML without waiting for JavaScript.

## Verified in this build

- 29 source sitemap paths generated and retained.
- 31 non-redirect HTML pages: exactly one title, description, canonical, H1 and parseable JSON-LD each; unique titles and descriptions.
- Local internal link and asset-file checks pass, including metadata image references.
- Correct DaySpa, WebSite, WebPage, Service and BreadcrumbList relationships; no staging-hostname names or invented reviews/credentials.
- Browser review at desktop width and narrow iframe viewports corresponding to 320, 390 and 768 px containers. Effective content widths were 305, 375 and 753 px because of scrollbars; no horizontal overflow after styles loaded.
- Mobile menu, catalog filter, booking interest selector and FAQ open/close tested.
- No application JavaScript errors observed; browser-extension errors were present and unrelated.
- JavaScript is about 4 KB, CSS about 16 KB, all optimized images together about 1.3 MB. This is an asset-budget check, not a Lighthouse or field performance result.

## Still outside the preview

The live WordPress and Elementor installation, its missing CSS files, its schema settings, rewards automation, Google Business Profile, Search Console, GA4, server redirects, customer bookings and financing have not been changed. No SEO ranking, indexing, lab score or real-user Core Web Vitals improvement is claimed. Re-run Lighthouse and field checks after production deployment.

Confirm pricing, device names, staff credentials, clinical oversight, suitability, membership inclusions, cancellation rules and image rights with the business before launching. Published menu prices are labeled snapshot facts. Time-limited sales and review-linked incentives are not promoted. Legal policy wording is reproduced for reference, with the preview scope disclosed; it is not legal certification.

## Production launch gate

Do not deploy this preview over the live website without an authorized launch, backup and rollback plan. Review the page inventory first. The seven permanent redirects in `redirect-map.json` and `dist/_redirects` must be installed and verified on the target host. Compatibility HTML fallback pages use meta refresh, which is not a verified HTTP 301. No fallback redirects for missing waxing or lashes pages were invented.

`production-sitemap.xml` is prepared for the existing official domain and preserves 29 paths. When launch is approved, set `SITE_ORIGIN` to the confirmed public origin and `INDEXABLE=1` when building, then review robots, canonicals, sitemap, metadata and schema again. Keep author utility and preview notes noindex. Do not submit the preview sitemap to search engines. Inspect all HTTP status/redirect chains, 404 behavior, booking/account/payment journeys and conversion measurement on production.

## Source repository

The user-selected WellnessoriginV2 GitHub repository is public. Its source visibility is independent of the private hosted preview. No GitHub Pages publishing workflow is included.
