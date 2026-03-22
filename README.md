# ONNX Landscape

The [ONNX Landscape](https://landscape.onnx.ai) maps the ecosystem of frameworks, runtimes, compilers, tools, and organizations that support ONNX. Built with [landscape2](https://github.com/cncf/landscape2).

## Repository structure

```
landscape.yml      # All landscape items, organized by category
settings.yml       # Appearance and site configuration
guide.yml          # Guide content shown on the landscape site
CNAME              # Custom domain (landscape.onnx.ai)
hosted_logos/      # SVG logo files (one per item)
fetch-logos.sh     # Script to download logos into hosted_logos/
.github/workflows/
  landscape.yml    # Build and deploy to GitHub Pages on push to main
```

## Adding or updating an entry

1. Edit `landscape.yml` — add an item under the appropriate category with `name`, `homepage_url`, `logo`, and `description`.
2. Add the corresponding SVG logo to `hosted_logos/` named to match the `logo:` field.
3. Open a pull request.

## Logo sources

- [Simple Icons](https://simpleicons.org/) — SVGs for most well-known brands
- `fetch-logos.sh` — downloads the standard set; run it once after cloning

## Building locally

Install [landscape2](https://github.com/cncf/landscape2#installation), then:

```sh
landscape2 build \
  --data-file landscape.yml \
  --settings-file settings.yml \
  --guide-file guide.yml \
  --logos-path hosted_logos \
  --output-dir /tmp/onnx-landscape

landscape2 serve --landscape-dir /tmp/onnx-landscape
```

## Deployment

Pushes to `main` that touch any landscape file trigger the GitHub Actions workflow, which builds the site and deploys it to GitHub Pages at [landscape.onnx.ai](https://landscape.onnx.ai).

**DNS record required:**
```
landscape.onnx.ai  CNAME  onnx.github.io
```

## Optional secrets

| Secret | Purpose |
|--------|---------|
| `LANDSCAPE_GITHUB_TOKENS` | Comma-separated GitHub PATs — increases API rate limits during build for repo metadata enrichment |
