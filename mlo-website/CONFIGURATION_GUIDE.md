# Mona Lisa Overdrive Website Configuration Guide

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [MkDocs Configuration (mkdocs.yml)](#mkdocs-configuration)
5. [Custom CSS Stylesheet](#custom-css-stylesheet)
6. [JavaScript Functionality](#javascript-functionality)
7. [Page-by-Page Configuration](#page-by-page-configuration)
8. [Building and Deploying](#building-and-deploying)
9. [Maintenance and Updates](#maintenance-and-updates)
10. [Troubleshooting](#troubleshooting)

---

## Project Overview

This website was built for **Mona Lisa Overdrive**, a synthwave/vaporwave band from Wilmington, NC. The site features a distinctive cyberpunk/vaporwave aesthetic with neon colors, animated gradients, and retro scanline effects.

**Website URL:** https://monalisaoverdrive.net

**Development Framework:** MkDocs with Material for MkDocs theme

**Design Philosophy:** Transform a documentation-style site into an immersive band experience with custom CSS overrides and vaporwave aesthetics.

---

## Technology Stack

### Core Technologies
- **MkDocs 1.x** - Static site generator
- **Material for MkDocs 9.7.3** - Base theme
- **Python 3.x** - Required for MkDocs
- **Markdown** - Content format
- **HTML/CSS/JavaScript** - Custom components

### Key Dependencies
```bash
mkdocs==1.6.1
mkdocs-material==9.7.3
```

### Installation
```bash
# Install Python dependencies
pip install mkdocs mkdocs-material

# OR use a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Mac/Linux
# venv\Scripts\activate   # On Windows
pip install mkdocs mkdocs-material
```

---

## Project Structure

```
dog-solitude/mlo-website/
├── mkdocs.yml                      # Main configuration file
├── docs/                           # Source content directory
│   ├── index.md                   # Homepage
│   ├── about.md                   # Band member profiles
│   ├── show-dates.md              # Upcoming/past shows
│   ├── music.md                   # Music page (currently disabled)
│   ├── photos.md                  # Photo gallery (currently disabled)
│   ├── videos.md                  # Video content (currently disabled)
│   ├── press.md                   # Press kit (currently disabled)
│   ├── epk.md                     # Electronic press kit (currently disabled)
│   ├── stylesheets/
│   │   └── extra.css              # Custom vaporwave styling
│   ├── javascripts/
│   │   └── show-dates.js          # Auto-move shows when dates pass
│   └── images/                    # Image assets
│       ├── 1 band photo.jpg       # Hero image
│       ├── eaglesdareapril18th.png
│       └── aboutphotos/           # Band member photos
│           ├── scott 1.jpg
│           ├── van7 2.jpg
│           ├── jared 10.jpg
│           ├── phil 5.jpg
│           └── matt 20.jpg
├── site/                          # Generated static site (git ignored)
│   └── [build output]
└── MLO new logo white.JPG         # Favicon and logo
```

---

## MkDocs Configuration

### File Location
`dog-solitude/mlo-website/mkdocs.yml`

### Complete Configuration Breakdown

```yaml
# Site Metadata
site_name: Mona Lisa Overdrive
site_url: https://monalisaoverdrive.net
site_description: 'Synthwave, Vaporwave, Electronic Music - Are you just breathing or you really alive?'
site_author: 'Mona Lisa Overdrive'
```

**Purpose:** Defines the site's basic identity and SEO metadata.

**When to Update:**
- Change `site_name` if band name changes (unlikely)
- Update `site_description` for different taglines or SEO optimization
- Update `site_url` if domain changes

---

```yaml
# Theme Configuration
theme:
  name: material
  palette:
    - scheme: slate              # Dark mode base
      primary: deep purple       # Primary color accent
      accent: pink              # Interactive elements
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

**Purpose:** Establishes the base Material theme with dark mode enabled.

**Note:** The light mode toggle is actually **hidden** via CSS (`extra.css` line 111-114), as the vaporwave aesthetic requires dark mode only.

---

```yaml
  font:
    text: Share Tech Mono        # Main body text font
    code: Courier New            # Code/monospace font
```

**Purpose:** Sets monospace fonts for the retro/tech aesthetic.

**Font Source:** Google Fonts (loaded in `extra.css` line 5)

**To Change Fonts:**
1. Update these values in `mkdocs.yml`
2. Update the `@import` statement in `extra.css` line 5
3. Update CSS font-family declarations throughout `extra.css`

---

```yaml
  features:
    - navigation.instant         # Fast page transitions
    - navigation.tracking        # Update URL on scroll
    - navigation.sections        # Group nav items in sections
    - navigation.top             # "Back to top" button
    - search.suggest             # Search autocomplete
    - search.highlight           # Highlight search terms
```

**Purpose:** Enables Material theme features for better UX.

**Note:** Search functionality is **hidden** via CSS but remains functional if you want to re-enable it.

---

```yaml
  favicon: MLO new logo white.JPG
  logo: MLO new logo white.JPG
```

**Purpose:** Sets the browser tab icon and site logo.

**To Update:**
1. Replace `MLO new logo white.JPG` in the root directory
2. Keep the same filename, OR update these lines with the new filename

---

```yaml
# Custom Assets
extra_css:
  - stylesheets/extra.css

extra_javascript:
  - javascripts/show-dates.js
```

**Purpose:** Links custom styling and functionality.

**Critical:** These files contain all the vaporwave styling and show date automation.

---

```yaml
# Markdown Extensions
markdown_extensions:
  - attr_list                    # Add HTML attributes to markdown
  - md_in_html                   # Use markdown inside HTML
  - admonition                   # Callout boxes
  - pymdownx.details             # Collapsible sections
  - pymdownx.superfences         # Advanced code blocks
```

**Purpose:** Enables advanced Markdown features needed for custom HTML components.

**Required For:**
- `attr_list` & `md_in_html`: Allow the custom hero section and card layouts
- Other extensions: Currently used minimally, but available for future features

---

```yaml
# Site Navigation
nav:
 - Home: index.md
 - Show Dates: show-dates.md
 # - Music: music.md           # Commented out = not in nav
 # - Photos: photos.md         # Commented out = not in nav
 # - Videos: videos.md         # Commented out = not in nav
 # - Press: press.md           # Commented out = not in nav
 # - EPK: epk.md              # Commented out = not in nav
 - About: about.md
```

**Purpose:** Defines the left sidebar navigation menu.

**To Add a Page:**
1. Uncomment the line (remove `# `)
2. Ensure the corresponding `.md` file exists in `docs/`
3. Run `mkdocs build` to regenerate the site

**Navigation Order:** Pages appear in the order listed here.

---

```yaml
# Social Media Links (Footer)
extra:
  social:
    - icon: fontawesome/brands/instagram
      link: https://instagram.com/monalisaoverdrive
      name: Follow us on Instagram
    - icon: fontawesome/brands/facebook
      link: https://facebook.com/monalisaoverdrive
      name: Like us on Facebook
    - icon: fontawesome/brands/spotify
      link: https://spotify.com
      name: Listen on Spotify
```

**Purpose:** Creates social media icons in the footer.

**To Update:**
- Change `link` values to actual band social media URLs
- Add more platforms by copying the format
- Available icons: https://fontawesome.com/icons (use `fontawesome/brands/[name]` format)

---

## Custom CSS Stylesheet

### File Location
`dog-solitude/mlo-website/docs/stylesheets/extra.css`

### CSS Architecture Overview

The stylesheet is organized into major sections:

1. **CSS Variables (Lines 7-19)** - Color palette
2. **Global Overrides (Lines 25-103)** - Body background and animations
3. **Header Styling (Lines 104-160)** - Top navigation bar
4. **Sidebar Styling (Lines 173-204)** - Left navigation
5. **Hero Section (Lines 216-337)** - Homepage banner
6. **Headings (Lines 342-371)** - Typography
7. **Links & Buttons (Lines 377-413)** - Interactive elements
8. **Show Date Cards (Lines 419-502)** - Event styling
9. **Grid Layouts (Lines 508-527)** - Responsive cards
10. **Band Member Cards (Lines 533-642)** - About page profiles
11. **Scanline Effects (Lines 648-669)** - Retro CRT effect
12. **Footer (Lines 675-683)** - Bottom section
13. **Mobile Navigation Fix (Lines 685-753)** - Hamburger menu
14. **Responsive Adjustments (Lines 759-776)** - Mobile typography

---

### Section 1: CSS Variables (Color Palette)

```css
:root {
    --neon-pink: #ff0080;
    --neon-purple: #b400ff;
    --neon-cyan: #00ffff;
    --neon-green: #00ff80;
    --deep-purple: #0f0528;
    --dark-purple: #1a0a3e;
    --mid-purple: #280050;
    --glow-pink: rgba(255, 0, 128, 0.6);
    --glow-purple: rgba(180, 0, 255, 0.6);
    --glow-cyan: rgba(0, 255, 255, 0.4);
}
```

**Purpose:** Centralized color system for the vaporwave aesthetic.

**To Rebrand Colors:**
1. Update these hex values
2. The entire site will update automatically
3. Consider adjusting glow opacity values (0.4-0.6 range) for subtlety

**Color Usage:**
- **Neon Pink** - Primary headings, hover states, active elements
- **Neon Purple** - Borders, secondary headings, glows
- **Neon Cyan** - Body text, links, default interactive states
- **Deep/Dark/Mid Purple** - Backgrounds (dark to light gradient)

---

### Section 2: Global Background Animation

```css
body {
    font-family: 'Share Tech Mono', 'Courier New', monospace !important;
    background: linear-gradient(180deg, ...);
    background-size: 100% 200%;
    animation: metallic-shift 20s ease-in-out infinite;
}
```

**Purpose:** Creates the animated metallic purple gradient background.

**Animation:** `metallic-shift` (lines 88-95) creates a slow 20-second vertical gradient movement.

**Pseudo-elements:**
- `body::before` (lines 47-69) - Adds a vertical light-to-dark overlay
- `body::after` (lines 71-86) - Adds radial gradient spotlights

**Performance Note:** These animations are lightweight and use CSS transforms for smooth performance.

---

### Section 3: Header Hiding Elements

```css
/* Hide dark mode toggle and search bar */
.md-header__option,
.md-search {
    display: none !important;
}
```

**Purpose:** Removes Material theme elements that don't fit the band aesthetic.

**To Re-enable Search:**
1. Remove or comment out line 112 (`.md-search { display: none !important; }`)
2. Keep line 111 to hide the palette toggle

**Also Hidden:**
- Line 127-129: Header logo (redundant with title)
- Line 183-185: Sidebar site title (redundant)

---

### Section 4: Hero Section (Homepage Banner)

#### Ticker Animation
```css
.ticker-wrapper { ... }
.ticker-content { animation: ticker-scroll 25.5s linear infinite; }
```

**Purpose:** Creates the scrolling text effect at top/bottom of hero.

**Location:** `index.md` lines 2-13

**To Update Ticker Text:**
- Edit `index.md` lines 4 and 10
- Repeat the text 3 times with ` /// ` separators for seamless loop

**Animation Speed:** Adjust `25.5s` (line 248) to make it faster/slower

---

#### Hero Logo

```css
.hero-logo {
    max-width: 600px;
    mask-image: radial-gradient(...);
}
```

**Purpose:** Displays the band photo with a fade-out edge effect.

**To Update Image:**
- Replace `docs/images/1 band photo.jpg`
- Update line 7 in `index.md` if filename changes

---

#### Hero Title

```css
.hero-subtitle {
    font-family: 'Orbitron', sans-serif;
    background: linear-gradient(90deg, ...);
    animation: gradient-shift 25.5s linear infinite;
}
```

**Purpose:** The animated rainbow gradient text for "Mona Lisa Overdrive"

**Font:** Orbitron (Google Font, imported line 5 of CSS)

**Animation:** Colors shift horizontally every 25.5 seconds

**To Update:**
- Text: Edit `index.md` line 13
- Colors: Modify gradient stops in CSS lines 309-316
- Speed: Change `25.5s` in line 321

---

### Section 5: Show Date Cards

```css
.event-card {
    background: linear-gradient(135deg, ...);
    border: 2px solid var(--neon-purple);
    transition: all 0.3s ease;
}

.event-card:hover {
    transform: translateX(5px);
    border-color: var(--neon-pink);
    box-shadow: 0 0 30px var(--glow-pink);
}
```

**Purpose:** Styles event cards with hover animations.

**Sub-elements:**
- `.event-date` - Large cyan date text
- `.event-venue` - Pink venue name
- `.event-details` - Body text
- `.support-acts`, `.ticket-price`, `.age`, `.show-time` - Metadata

**Hover Effect:** Cards slide right 5px and change border color.

---

### Section 6: Grid Layouts

```css
.grid-2col {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}
```

**Purpose:** Creates responsive card layouts that stack on mobile.

**Usage:**
- Homepage: Social media cards (`index.md` lines 34-62)
- About page: Band member profiles (`about.md` line 16)

**Responsive Behavior:** Cards automatically stack when viewport < 300px per card.

---

### Section 7: Band Member Cards

```css
.member-card {
    background: linear-gradient(135deg, ...);
    transition: all 0.3s ease;
}

.member-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 35px var(--glow-cyan);
}
```

**Purpose:** Styles the "About" page band member profiles.

**Sub-elements:**
- `.member-image-placeholder` - Circular profile photo with border glow
- `.member-role` - Cyan job title (e.g., "Bass Boss")
- `.member-bio` - Biography text
- `.member-acts` - Associated musical projects

**Hover Effect:** Cards lift up 5px with cyan glow.

**Image Styling:** 200px × 200px circles with 3px neon cyan border.

---

### Section 8: Mobile Navigation Fix

**Added:** April 6, 2026 (this conversation)

```css
@media screen and (max-width: 76.1875em) {
    .md-sidebar--primary {
        position: fixed;
        left: -242px;
        transition: transform 0.3s ease;
    }

    [data-md-toggle="drawer"]:checked ~ .md-container .md-sidebar--primary {
        transform: translateX(242px);
    }
}
```

**Purpose:** Fixes the hamburger menu navigation on mobile devices.

**Breakpoint:** 76.1875em (approximately 1230px) - Material theme's tablet/mobile breakpoint.

**Behavior:**
1. Sidebar hidden off-screen by default (`left: -242px`)
2. When hamburger clicked, checkbox `#__drawer` is checked
3. Sidebar slides in (`translateX(242px)`)
4. Overlay appears behind sidebar (`z-index: 5`)
5. Clicking overlay or link closes menu

**Z-index Layers:**
- Overlay: `z-index: 5`
- Sidebar: `z-index: 6`
- Hamburger icon: `z-index: 7`

---

### Section 9: Scanline Effect

```css
.md-content::before {
    background: repeating-linear-gradient(
        0deg,
        rgba(0, 0, 0, 0.1) 0px,
        transparent 1px,
        transparent 2px,
        rgba(0, 0, 0, 0.1) 3px
    );
    pointer-events: none;
}
```

**Purpose:** Creates a retro CRT monitor scanline effect over content.

**Appearance:** Subtle horizontal lines every 3 pixels.

**To Adjust:**
- **Intensity:** Change `rgba(0, 0, 0, 0.1)` opacity (0.0-0.2 recommended)
- **Spacing:** Adjust the pixel values (currently 3px repeat)
- **To Disable:** Comment out lines 648-664

---

## JavaScript Functionality

### File Location
`dog-solitude/mlo-website/docs/javascripts/show-dates.js`

### Purpose
Automatically moves show date cards from "Upcoming Shows" to "Past Shows" when the date passes.

### How It Works

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const today = new Date();
    const upcomingContainer = document.getElementById('upcoming-shows');
    const pastContainer = document.getElementById('past-shows');
```

**Step 1:** Runs when page loads, grabs current date and both containers.

---

```javascript
upcomingShows.forEach(show => {
    const showDate = new Date(show.getAttribute('data-date'));
    if (showDate < today) {
        pastContainer.insertBefore(show, pastContainer.firstChild);
    }
});
```

**Step 2:** Checks each show's `data-date` attribute. If past, moves to past shows container.

---

```javascript
setTimeout(function() {
    checkAndMoveShows();
    setInterval(checkAndMoveShows, 24 * 60 * 60 * 1000);
}, timeUntilMidnight);
```

**Step 3:** Schedules automatic re-check at midnight every day.

---

### Requirements

**HTML Structure in `show-dates.md`:**

```html
<div id="upcoming-shows">
    <div class="event-card" data-date="2026-04-18">
        <!-- Show content -->
    </div>
</div>

<div id="past-shows">
    <!-- Past shows appear here automatically -->
</div>
```

**Critical:**
- Container IDs must be `upcoming-shows` and `past-shows`
- Each event card must have `data-date` attribute in `YYYY-MM-DD` format
- Both containers must exist (even if empty)

---

### Limitations

- Only works on page load or midnight refresh
- Requires users to refresh page for update
- If user's clock is wrong, may misplace shows

**Future Enhancement:** Could add server-side pre-processing during `mkdocs build`.

---

## Page-by-Page Configuration

### Homepage (`index.md`)

#### Hero Section (Lines 1-14)

```html
<div class="hero-section">
    <div class="ticker-wrapper">
        <div class="ticker-content">
            <span class="ticker-text">Your scrolling text here /// Repeat 3x /// </span>
        </div>
    </div>
    <img src="images/1 band photo.jpg" alt="Mona Lisa Overdrive" class="hero-logo">
    <div class="ticker-wrapper">
        <div class="ticker-content">
            <span class="ticker-text">Another ticker /// Repeat 3x /// </span>
        </div>
    </div>
    <h1 class="hero-subtitle"> Mona Lisa Overdrive</h1>
</div>
```

**To Customize:**
- **Top Ticker:** Line 4 - Update message, repeat 3 times with ` /// ` separators
- **Bottom Ticker:** Line 10 - Same format
- **Hero Image:** Line 7 - Change `src` path
- **Title:** Line 13 - Update band name (will break gradient width if drastically different length)

---

#### Band Description (Lines 18-30)

Standard Markdown with `<br>` tags for line breaks.

**Formatting Note:** Using `<br><br>` creates double line breaks for dramatic pauses in the description.

---

#### Social Media Cards (Lines 33-62)

```html
<div class="grid-2col">
<div class="card">
<h3>Platform Name</h3>
<p>Description text here.</p>
<a href="https://..." class="cta-button">Button Text</a>
</div>
<!-- More cards -->
</div>
```

**To Add a Platform:**
1. Copy lines 35-43 (one complete card)
2. Paste inside `<div class="grid-2col">` (after line 34)
3. Update `<h3>`, `<p>`, `href`, and button text
4. Grid auto-adjusts to fit cards

**To Remove a Platform:**
- Delete the entire `<div class="card">...</div>` block

---

### Show Dates Page (`show-dates.md`)

#### Upcoming Shows Section (Lines 7-43)

```html
<div id="upcoming-shows" markdown="0">
<div class="event-card" data-date="2026-04-18">
<div class="event-date">April 18th, 2026</div>
<div class="event-venue">The Eagle's Dare</div>
<div class="support-acts">with Bridge to Breakdown</div>
<div class="ticket-price">$8 presale, $12 day-of admission</div>
<div class="ticket-link"><a href="...">Presale Tickets Available Now</a></div>
<div class="age">21+</div>
<div class="show-time">Doors at 7pm Show at 9pm</div>
<div class="event-details">
    Description text here...<br>
    <img src="/images/poster.png" alt="Show poster">
</div>
<iframe src="[Google Maps embed]" ...></iframe>
<div class="show-cta">
    <a href="..." class="cta-button">Get Tickets</a>
    <a href="..." class="cta-button">Facebook Event</a>
    <a href="..." class="cta-button">Get Directions</a>
</div>
</div>
</div>
```

---

**To Add a New Show:**

1. **Copy the entire `.event-card` block** (lines 8-42)

2. **Update the `data-date` attribute:**
   ```html
   <div class="event-card" data-date="2026-05-15">
   ```
   Format: `YYYY-MM-DD` (critical for auto-move feature)

3. **Update show details:**
   - `.event-date` - Human-readable date
   - `.event-venue` - Venue name
   - `.support-acts` - Opening bands (or remove this line)
   - `.ticket-price` - Pricing info
   - `.ticket-link` - Ticket URL
   - `.age` - Age requirement
   - `.show-time` - Door/show times
   - `.event-details` - Full description

4. **Add Google Maps embed:**
   - Go to Google Maps, search venue
   - Click "Share" → "Embed a map"
   - Copy iframe code
   - Replace entire `<iframe>` tag (line 36)

5. **Update CTA buttons:**
   - Get Tickets - Eventbrite/ticket link
   - Facebook Event - FB event URL
   - Get Directions - Google Maps link

6. **Paste the new card** inside `<div id="upcoming-shows">` (after line 7, before the closing `</div>` on line 43)

---

**To Remove a Show Manually:**
- Delete the entire `<div class="event-card">...</div>` block
- OR let the JavaScript auto-move it when date passes

---

#### Past Shows Section (Lines 46-51)

```html
<div id="past-shows">
<!-- Shows automatically appear here via JavaScript -->
</div>
```

**Currently:** Commented out, so past shows are hidden.

**To Enable Past Shows:**
1. Uncomment lines 47-51
2. Past shows will automatically populate here when dates pass
3. Shows appear in reverse chronological order (newest first)

---

### About Page (`about.md`)

#### Band Description (Lines 2-13)

Standard Markdown introduction text.

---

#### Band Member Grid (Lines 16-147)

```html
<div class="grid-2col">
<div class="member-card">
<img src="/images/aboutphotos/name.jpg" alt="Name" class="member-image-placeholder">
<h3>Member Name</h3>
<span class="member-role">Role Title</span>
<div class="member-bio">
Bio text here...
</div>
<div class="member-acts">
<span class="member-acts-label">Associated Acts</span>
<div class="member-acts-list">
<div class="Associated Act"><a href="...">Band Name</a></div><br>
</div>
</div>
</div>
<!-- More members -->
</div>
```

---

**To Update a Member:**

1. **Photo:** Replace file in `docs/images/aboutphotos/` or update `src` path (line 19)
2. **Name:** Update `<h3>` tag (line 21)
3. **Role:** Update `.member-role` span (line 23)
4. **Bio:** Edit `.member-bio` div content (lines 25-32)
5. **Associated Acts:**
   - Update links in `.member-acts-list` (lines 36-40)
   - Add more acts by copying the format: `<div class="Associated Act"><a href="URL">Name</a></div><br>`

---

**To Add a Member:**

1. Copy lines 17-43 (complete member card)
2. Paste inside `<div class="grid-2col">` section
3. Update all details as above
4. Add photo to `docs/images/aboutphotos/`

---

**To Remove a Member:**
- Delete the entire `<div class="member-card">...</div>` block

---

**Special Layout Note:**

Matt Tease's card (lines 120-147) is centered using:
```html
<div style="display: flex; justify-content: center; margin: 30px 0;">
<div class="member-card" style="max-width: 400px;">
```

This centers a single card. Remove this wrapper for standard grid alignment.

---

### Other Pages (Currently Disabled)

The following pages exist but are commented out in navigation:

- `music.md` - Music/discography page
- `photos.md` - Photo gallery
- `videos.md` - Video content
- `press.md` - Press releases
- `epk.md` - Electronic press kit

**To Enable:**
1. Uncomment the line in `mkdocs.yml` nav section (lines 44-48)
2. Update content in the corresponding `.md` file
3. Run `mkdocs build`

---

## Building and Deploying

### Development Workflow

#### 1. Local Development Server

```bash
cd dog-solitude/mlo-website
mkdocs serve
```

**Opens:** http://127.0.0.1:8000

**Features:**
- Live reload on file changes
- Preview before building
- Shows build warnings/errors

**To Stop:** Press `Ctrl+C`

---

#### 2. Build Static Site

```bash
cd dog-solitude/mlo-website
mkdocs build
```

**Output:** `site/` directory contains full static website.

**What Gets Built:**
- All `.md` files converted to HTML
- CSS/JS copied to `site/assets/`
- Images copied to `site/images/`
- Navigation structure generated

**Build Warnings:** Review any warnings about excluded files or broken links.

---

#### 3. Clean Build

```bash
cd dog-solitude/mlo-website
mkdocs build --clean
```

**Purpose:** Deletes `site/` directory first, then rebuilds fresh.

**Use When:**
- Files aren't updating
- Old pages still appearing
- Major structural changes

---

### Deployment Options

#### Option 1: Manual Upload (Current Method)

1. Run `mkdocs build`
2. Upload entire `site/` directory to web host via FTP/SFTP
3. Point domain to uploaded directory

**Pros:** Simple, works with any host
**Cons:** Manual process, easy to forget files

---

#### Option 2: GitHub Pages

1. Create GitHub repository
2. Push source to repo
3. Enable GitHub Pages in settings
4. GitHub Actions can auto-build on push

**Setup:**
```bash
# In project root
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/username/mlo-website.git
git push -u origin main
```

**GitHub Actions Workflow** (`.github/workflows/deploy.yml`):
```yaml
name: Deploy MkDocs
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: 3.x
      - run: pip install mkdocs mkdocs-material
      - run: mkdocs gh-deploy --force
```

---

#### Option 3: Netlify/Vercel

1. Connect GitHub repo to Netlify/Vercel
2. Set build command: `mkdocs build`
3. Set publish directory: `site`
4. Auto-deploys on git push

**Pros:** Free, auto-deploy, CDN, HTTPS
**Cons:** Requires GitHub account

---

### Domain Configuration

**Current Domain:** monalisaoverdrive.net

**DNS Setup:**
- Point A record to hosting server IP
- OR point CNAME to hosting provider

**HTTPS:** Ensure SSL certificate is active for secure connection.

---

## Maintenance and Updates

### Regular Maintenance Tasks

#### 1. Adding New Shows

**Frequency:** As shows are booked

**Steps:**
1. Open `docs/show-dates.md`
2. Copy existing event card template
3. Update all show details (date, venue, etc.)
4. Add Google Maps embed
5. Run `mkdocs build`
6. Deploy updated `site/` directory

**Reminder:** Use `YYYY-MM-DD` format for `data-date` attribute.

---

#### 2. Updating Social Media Links

**Frequency:** When URLs change or new platforms added

**Files to Update:**
- `mkdocs.yml` lines 52-61 (footer icons)
- `docs/index.md` lines 34-62 (homepage cards)

**Steps:**
1. Update URLs in both locations
2. Run `mkdocs build`
3. Deploy

---

#### 3. Updating Band Member Info

**Frequency:** Member changes, new projects, bio updates

**File:** `docs/about.md`

**Steps:**
1. Update text in relevant member card
2. Replace photo if needed (keep same filename or update path)
3. Run `mkdocs build`
4. Deploy

---

#### 4. Refreshing Images

**Frequency:** New promo photos, album art, etc.

**Process:**
1. Optimize images (use WebP or compressed JPEG)
2. Upload to `docs/images/` or subdirectory
3. Update `src` paths in `.md` files
4. Old images can be deleted (check no pages reference them first)
5. Run `mkdocs build`
6. Deploy

**Image Optimization Tools:**
- TinyPNG (https://tinypng.com)
- Squoosh (https://squoosh.app)
- ImageOptim (Mac app)

**Recommended Sizes:**
- Hero image: 1200px wide max
- Band photos: 800px wide max
- Profile photos: 400px × 400px
- Posters: 1000px wide max

---

### Seasonal Updates

#### Before a Show

1. Add show to `show-dates.md`
2. Post announcement (outside website scope)
3. Test ticket links

#### After a Show

1. Show auto-moves to past (if enabled)
2. Consider adding photos to gallery (future feature)
3. Update press page with reviews (if applicable)

#### Annual Checks

1. Review all external links (social media, Spotify, etc.)
2. Update copyright year in footer if customized
3. Check for MkDocs/Material theme updates
4. Review Google Analytics (if installed)

---

### Content Guidelines

#### Writing Style

- **Voice:** Energetic, cyberpunk, slightly mysterious
- **Tone:** Immersive, enthusiastic, poetic
- **References:** Vaporwave culture, retrofuturism, neon aesthetics

#### Consistency Checklist

- [ ] Band name: "Mona Lisa Overdrive" (not "MLO" in formal text)
- [ ] Location: "Wilmington, NC"
- [ ] Tagline: "Are you just breathing or are you really alive?"
- [ ] Color scheme: Neon pink/purple/cyan (don't add reds, yellows, greens)
- [ ] Font usage: Orbitron for headings, Share Tech Mono for body

---

## Troubleshooting

### Common Issues

#### Issue: Mobile Navigation Not Working

**Symptoms:** Hamburger menu doesn't open sidebar on mobile

**Solution:**
1. Verify `extra.css` includes mobile navigation fix (lines 685-753)
2. Check that `mkdocs build` was run after adding fix
3. Clear browser cache
4. Test on actual device (not just browser resize)

**Debug Steps:**
```bash
# Rebuild clean
mkdocs build --clean

# Check for CSS errors in terminal output
```

---

#### Issue: Images Not Showing

**Symptoms:** Broken image icons or blank spaces

**Common Causes:**
1. **Wrong path:** Images must be in `docs/images/` and referenced without `docs/`
2. **Case sensitivity:** `Image.jpg` ≠ `image.jpg` on Linux servers
3. **Not deployed:** Image added locally but not uploaded to server

**Solutions:**
```html
<!-- CORRECT (in .md files) -->
<img src="images/photo.jpg">
<img src="/images/photo.jpg">

<!-- WRONG -->
<img src="docs/images/photo.jpg">
<img src="../images/photo.jpg">
```

---

#### Issue: CSS Changes Not Applying

**Symptoms:** Edited `extra.css` but site looks the same

**Solutions:**
1. **Hard refresh:** Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
2. **Rebuild:** Run `mkdocs build --clean`
3. **Clear cache:** Browser dev tools → Network tab → Disable cache
4. **Check syntax:** CSS error can break entire file (look for missing `}` or `;`)

**Validation:**
```bash
# Check CSS syntax
# Open extra.css in VS Code - it will highlight errors
```

---

#### Issue: Show Dates Not Auto-Moving

**Symptoms:** Past show still in "Upcoming" section

**Checklist:**
1. `data-date` attribute is present: `<div class="event-card" data-date="2026-04-18">`
2. Date format is `YYYY-MM-DD`
3. Container ID is `upcoming-shows`
4. Container ID is `past-shows` (if past shows section enabled)
5. JavaScript file is loaded (check browser console for errors)

**Manual Check:**
```javascript
// Open browser console on show-dates page
document.getElementById('upcoming-shows')  // Should not be null
document.getElementById('past-shows')      // Should not be null
```

---

#### Issue: Navigation Link Not Appearing

**Symptoms:** Uncommented page in `mkdocs.yml` but not in nav

**Solution:**
1. Check indentation in `mkdocs.yml` (must use spaces, not tabs)
2. Verify file exists at specified path
3. Run `mkdocs build` and check for warnings
4. Hard refresh browser

**Correct Format:**
```yaml
nav:
 - Home: index.md
 - New Page: new-page.md  # Two spaces before dash
```

---

#### Issue: Build Warnings

**Common Warnings:**

1. **"Excluding 'README.md' from the site"**
   - Normal, can ignore
   - OR delete `docs/README.md`

2. **"Pages exist but not in nav"**
   - Lists pages not linked in navigation
   - Intentional for disabled pages (music.md, etc.)
   - OR add them to nav in `mkdocs.yml`

3. **"MkDocs 2.0 is incompatible with Material for MkDocs"**
   - Warning about future MkDocs version
   - Safe to ignore for now
   - Site still builds correctly

---

#### Issue: Gradient/Animation Looks Wrong

**Symptoms:** Colors glitching, animations jerky, or no glow effects

**Browser Compatibility:**
- Site requires modern browser (Chrome 90+, Firefox 88+, Safari 14+)
- Some effects may not work on older mobile browsers

**Check:**
1. Update browser to latest version
2. Enable hardware acceleration in browser settings
3. Some effects may not work in "Reader Mode" or print preview

---

### Getting Help

#### Check Browser Console

```
1. Right-click page → Inspect
2. Click "Console" tab
3. Look for red error messages
```

**Common Error Messages:**
- "Failed to load resource" - Missing file (check path)
- "Unexpected token" - JavaScript syntax error
- "Uncaught ReferenceError" - Variable not defined

---

#### MkDocs Documentation

- Official Docs: https://www.mkdocs.org
- Material Theme: https://squidfunk.github.io/mkdocs-material/

---

#### Check File Permissions

If deploying to Linux server:

```bash
# Make sure files are readable
chmod 644 site/*.html
chmod 644 site/**/*.css
chmod 644 site/**/*.js
chmod 755 site/images/
```

---

## Quick Reference

### Key File Paths

```
mkdocs.yml                           # Main config
docs/stylesheets/extra.css          # All styling
docs/javascripts/show-dates.js      # Show automation
docs/index.md                       # Homepage
docs/show-dates.md                  # Shows page
docs/about.md                       # About page
docs/images/                        # Image assets
```

### Key Commands

```bash
mkdocs serve        # Preview locally
mkdocs build        # Build site
mkdocs build --clean # Clean rebuild
mkdocs --version    # Check version
```

### Color Variables

```css
--neon-pink: #ff0080
--neon-purple: #b400ff
--neon-cyan: #00ffff
--deep-purple: #0f0528
```

### CSS Class Reference

```css
.hero-section         /* Homepage banner */
.ticker-wrapper       /* Scrolling text */
.hero-logo           /* Band photo */
.hero-subtitle       /* Gradient title */
.grid-2col           /* Card layout */
.card                /* Standard card */
.cta-button          /* Call-to-action button */
.event-card          /* Show date card */
.member-card         /* Band member profile */
```

---

## Conclusion

This configuration guide documents the complete structure of the Mona Lisa Overdrive website. The site is built on MkDocs with heavy CSS customization to create a unique vaporwave aesthetic while maintaining the ease of Markdown-based content management.

**Core Philosophy:**
- Content in Markdown (easy to update)
- Design in CSS (no touching HTML/theme files)
- Automation in JavaScript (minimal, targeted)

**Remember:**
1. Always run `mkdocs build` after changes
2. Test locally with `mkdocs serve` before deploying
3. Keep backups of custom CSS (it's the heart of the design)
4. Document any new features added in the future

---

**Document Version:** 1.0
**Last Updated:** April 6, 2026
**Author:** Configuration by Claude (Anthropic)
**Website:** https://monalisaoverdrive.net

---

**End of Configuration Guide**
