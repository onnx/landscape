# ONNX Landscape

The [ONNX Landscape](https://onnx.ai/landscape/) maps the ecosystem of frameworks, runtimes, compilers, tools, and organizations that support ONNX. Built with [landscape2](https://github.com/cncf/landscape2). Inclusion is not an endorsement or a statement of current project membership.

## Repository structure

```
landscape.yml      # All landscape items, organized by category
settings.yml       # Appearance and site configuration
guide.yml          # Guide content shown on the landscape site
CNAME              # Intended custom domain (requires DNS and Pages setup)
hosted_logos/      # SVG logos and clearly labeled text placeholders
scripts/           # Input and generated-site checks
fetch-logos.sh     # Legacy helper for fetching a subset of logos
.github/workflows/
  landscape.yml    # Build and deploy to GitHub Pages on push to main
```

## Adding or updating an entry

1. Edit `landscape.yml` — add an item under the appropriate category with `name`, `homepage_url`, `logo`, and `description`.
2. Add the corresponding SVG logo to `hosted_logos/` and set `logo:` to its filename (for example, `example.svg`, without a directory prefix). Use a logo that you have permission to distribute, and record its source in the pull request.
3. Run `python scripts/check-landscape.py` (requires PyYAML), build the site, and check the generated output as shown below. The second check catches errors that landscape2 may log without failing the build.
4. Open a pull request. CI validates the configuration and generated site without deploying it.

## Logo sources

- [Simple Icons](https://simpleicons.org/) — SVGs for most well-known brands
- Some entries have neutral text placeholders because a suitable logo has not yet been sourced. These are not official logos; contributions replacing them with properly sourced SVGs are welcome.
- `fetch-logos.sh` is an older helper that overwrites files and fetches only a subset of the logos. Review its URLs and the downloaded files before using them.

## Building locally

Install [landscape2](https://github.com/cncf/landscape2#installation), then:

```sh
landscape2 build \
  --data-file landscape.yml \
  --settings-file settings.yml \
  --guide-file guide.yml \
  --logos-path hosted_logos \
  --output-dir /tmp/onnx-landscape-preview/landscape

python scripts/check-landscape.py --built-dir /tmp/onnx-landscape-preview/landscape
python -m http.server 8000 --directory /tmp/onnx-landscape-preview
```

Open `http://localhost:8000/landscape/`. The parent directory mirrors the configured Pages subpath.

## Deployment

Pushes to `main` trigger the GitHub Actions workflow, which builds and deploys the site to [onnx.ai/landscape/](https://onnx.ai/landscape/). Pull requests run the same build checks without deploying.

The intended `landscape.onnx.ai` domain requires both DNS and GitHub Pages configuration. A file named `CNAME` alone does not configure the domain for a Pages Actions deployment. An administrator must configure the custom domain in the repository's Pages settings, set the DNS record, and wait for HTTPS provisioning. After verifying the domain, update `url` in `settings.yml`, remove its `/landscape` `base_path`, and update the links in this README.

**DNS record:**
```
landscape.onnx.ai  CNAME  onnx.github.io
```

## Optional secrets

| Secret | Purpose |
|--------|---------|
| `LANDSCAPE_GITHUB_TOKENS` | Comma-separated GitHub PATs — increases API rate limits during build for repo metadata enrichment |
