# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a Hugo-based Persian blog built with the PaperMod theme. The site is deployed to GitHub Pages and configured for Persian (Farsi) content with RTL support.

## Key Configuration

- **Hugo Config**: `hugo.toml` - Main configuration file
- **Site URL**: https://01sadra.github.io/
- **Language**: Persian (fa-IR) with RTL layout
- **Theme**: PaperMod theme (located in themes directory, empty - likely copied into repo)
- **Content Directory**: `content/` - Contains blog posts organized by year/month
- **Static Assets**: `static/` - Contains CSS and fonts
- **Custom CSS**: `/css/rtl.css` for Persian RTL support

## Development Commands

### Building the Site
```bash
# Generate the site (output to public/ directory)
hugo
```

### Local Development
```bash
# Start local development server
hugo serve
# Or with drafts enabled
hugo serve -D
```

### Content Management
```bash
# Create new blog post
hugo new blog/YYYY/MM/YYYY-MM-DD-title/index.md
```

## Architecture

### Content Structure
- Blog posts are organized in `/content/blog/YYYY/MM/` directories
- Each post has its own folder with `index.md` and optional `images/` subdirectory
- Persian permalinks configured as `/:slug/`

### Theme & Styling
- PaperMod theme with extensive customization
- Custom RTL CSS at `/static/css/rtl.css` and `/css/rtl.css`
- Persian Vazir font included
- Light theme only (theme toggle disabled)

### Hugo Configuration Highlights
- RSS, sitemap, and taxonomy generation disabled
- Raw HTML enabled in markdown
- Pagination set to 5 posts per page
- Reading time, share buttons, and post navigation disabled
- Persian menu items for categories and tags

### Content Processing
- `fix_hugo.py` script wraps markdown content in `{{< rawhtml >}}` shortcodes
- This allows HTML content to be processed properly in Hugo

## GitHub Pages Deployment

### GitHub Actions Workflow
The site uses GitHub Actions for automated deployment to GitHub Pages. The workflow is defined in `.github/workflows/hugo.yaml` and automatically builds and deploys the site on every push to the main branch.

### Deployment Process
1. **Create Feature Branch**: Work on changes in feature branches
2. **Create Pull Request**: Push branch and create PR to main
3. **Merge to Main**: Once approved, merge PR to main branch
4. **Automatic Deployment**: GitHub Actions workflow automatically builds and deploys

### GitHub Pages Configuration
- Navigate to repository Settings → Pages
- Set source to "GitHub Actions" (not "Deploy from branch")
- Site deploys to: https://01sadra.github.io/

### Deployment Commands
```bash
# Push current branch to GitHub
git push origin [branch-name]

# Create and switch to new feature branch
git checkout -b feature/new-feature-name

# After PR approval and merge, pull latest main
git checkout main
git pull origin main

# Delete merged feature branch locally
git branch -d feature/branch-name
```

## Special Files
- `fix_hugo.py`: Python script for content processing (wraps content in rawhtml shortcodes)
- Persian content throughout with categories and tags in Persian