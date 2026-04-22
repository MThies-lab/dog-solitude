# Mona Lisa Overdrive Website - User Guide

## Welcome to Your Website Management System

This guide will walk you through everything you need to know to update and maintain the Mona Lisa Overdrive website. No deep technical knowledge required - just follow the steps!

**Website:** https://monalisaoverdrive.net

---

## Table of Contents

- [Quick Start](#quick-start)
- [Common Tasks](#common-tasks)
  - [Adding a New Show](#adding-a-new-show)
  - [Updating Social Media Links](#updating-social-media-links)
  - [Changing Band Member Info](#changing-band-member-info)
  - [Updating Photos](#updating-photos)
  - [Editing Homepage Text](#editing-homepage-text)
- [Publishing Your Changes](#publishing-your-changes)
- [Tips and Best Practices](#tips-and-best-practices)
- [Getting Help](#getting-help)

---

## Quick Start

### What You Need

1. **A text editor** - Any of these work:
   - VS Code (recommended, free): https://code.visualstudio.com
   - Sublime Text
   - Atom
   - Even TextEdit (Mac) or Notepad (Windows) in a pinch

2. **Terminal/Command Prompt** - To build the website
   - Mac: Use "Terminal" app
   - Windows: Use "Command Prompt" or "PowerShell"

3. **Python and MkDocs installed** - Should already be set up, but if not:
   ```bash
   pip install mkdocs mkdocs-material
   ```

### Your Website Files

Everything lives in this folder structure:

```
mlo-website/
├── docs/                    ← Your content lives here!
│   ├── index.md            ← Homepage
│   ├── show-dates.md       ← Show dates page
│   ├── about.md            ← About/band members page
│   ├── images/             ← All photos
│   └── stylesheets/        ← Design/colors (advanced)
└── mkdocs.yml              ← Site settings
```

**Important Rule:** Only edit files in the `docs/` folder and `mkdocs.yml`. Never touch the `site/` folder - it's auto-generated.

---

## Common Tasks

### Adding a New Show

**Time Required:** 5-10 minutes

**Files You'll Edit:** `docs/show-dates.md`

#### Step-by-Step Instructions

1. **Open the file** `docs/show-dates.md` in your text editor

2. **Find this section** (around line 7):
   ```html
   <div id="upcoming-shows" markdown="0">
   ```

3. **Copy this entire template** (one complete show):
   ```html
   <div class="event-card" data-date="2026-04-18">
   <div class="event-date">April 18th, 2026</div>
   <div class="event-venue">The Eagle's Dare</div>
   <div class="support-acts">with Bridge to Breakdown</div>
   <div class="ticket-price">$8 presale, $12 day-of admission</div>
   <div class="ticket-link"><a href="https://...">Presale Tickets Available Now</a></div>
   <div class="age">21+</div>
   <div class="show-time">Doors at 7pm Show at 9pm</div>
   <div class="event-details">
       Your show description here...<br>
       <img src="/images/your-poster.png" alt="Show poster">
   </div>
   <iframe src="[GOOGLE MAPS EMBED - See below]" width="100%" height="300" style="border:0; border-radius: 8px; margin: 20px 0; box-shadow: 0 0 15px var(--glow-purple);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
   <div class="show-cta">
       <a href="https://eventbrite.com/..." class="cta-button">Get Tickets</a>
       <a href="https://facebook.com/..." class="cta-button" target="_blank">Facebook Event</a>
       <a href="https://maps.google.com/?q=..." class="cta-button" target="_blank">Get Directions</a>
   </div>
   </div>
   ```

4. **Paste it** right after the opening `<div id="upcoming-shows">` line (before any existing shows)

5. **Update these fields:**

   | Field | What to Change | Example |
   |-------|---------------|---------|
   | `data-date` | Show date in YYYY-MM-DD format | `2026-05-15` |
   | `event-date` | Human-readable date | `May 15th, 2026` |
   | `event-venue` | Venue name | `Satellite Bar & Lounge` |
   | `support-acts` | Opening bands (or delete this line) | `with The Neon Kings` |
   | `ticket-price` | Price info | `$10 advance, $15 door` |
   | `ticket-link` | URL to buy tickets | Full Eventbrite link |
   | `age` | Age requirement | `18+` or `All Ages` |
   | `show-time` | Door time and show time | `Doors 8pm / Show 9pm` |
   | `event-details` | Full description | Your show announcement |
   | Three `cta-button` links | Ticket, Facebook, Directions URLs | Update all three |

6. **Add Google Maps embed** (this makes the map show up):
   - Go to https://maps.google.com
   - Search for your venue (e.g., "Eagles Dare Wilmington NC")
   - Click the **Share** button
   - Click the **Embed a map** tab
   - Click **Copy HTML**
   - Find the `src="..."` part in the copied code
   - Replace the `src="[GOOGLE MAPS EMBED]"` in your show card with what you copied

   **Example:**
   ```html
   <!-- Before -->
   <iframe src="[GOOGLE MAPS EMBED]" ...>

   <!-- After -->
   <iframe src="https://www.google.com/maps/embed?pb=!1m18!..." ...>
   ```

7. **Add a show poster** (optional):
   - Save your poster image to `docs/images/`
   - Name it something like `show-may-15-2026.png`
   - Update the image line:
     ```html
     <img src="/images/show-may-15-2026.png" alt="May 15th show poster">
     ```

8. **Save the file**

9. **[Build and publish](#publishing-your-changes)** your changes

#### Important Notes

- **The `data-date` must be in YYYY-MM-DD format** - This is how the website knows when to automatically move the show to "Past Shows"
- **Put newest shows first** - Add new shows at the top of the list
- **Check your links** - Make sure ticket URLs work before publishing

---

### Updating Social Media Links

**Time Required:** 2 minutes

**Files You'll Edit:**
- `mkdocs.yml` (footer links)
- `docs/index.md` (homepage cards)

#### Footer Social Icons

1. **Open** `mkdocs.yml` in your text editor

2. **Find this section** (around line 52):
   ```yaml
   extra:
     social:
       - icon: fontawesome/brands/instagram
         link: https://instagram.com/monalisaoverdrive
         name: Follow us on Instagram
   ```

3. **Update the `link:` value** with your new URL

4. **To add a new platform**, copy one block and change it:
   ```yaml
       - icon: fontawesome/brands/youtube
         link: https://youtube.com/@yourchannelname
         name: Watch on YouTube
   ```

   **Popular icons:**
   - Instagram: `fontawesome/brands/instagram`
   - Facebook: `fontawesome/brands/facebook`
   - Twitter/X: `fontawesome/brands/x-twitter`
   - YouTube: `fontawesome/brands/youtube`
   - TikTok: `fontawesome/brands/tiktok`
   - Spotify: `fontawesome/brands/spotify`
   - Bandcamp: `fontawesome/brands/bandcamp`
   - SoundCloud: `fontawesome/brands/soundcloud`

#### Homepage Social Cards

1. **Open** `docs/index.md`

2. **Find the section** (around line 34):
   ```html
   <div class="grid-2col">
   <div class="card">
   <h3>Instagram</h3>
   <p>Behind-the-scenes content, show updates, and visual overdrive.</p>
   <a href="https://www.instagram.com/..." class="cta-button">Follow on Instagram</a>
   </div>
   ```

3. **Update the link** inside `<a href="...">` tags

4. **To add a new card**, copy an entire `<div class="card">...</div>` block and update:
   - `<h3>` - Platform name
   - `<p>` - Short description
   - `href` - Your profile URL
   - Button text

---

### Changing Band Member Info

**Time Required:** 5 minutes per member

**File You'll Edit:** `docs/about.md`

#### Updating Member Info

1. **Open** `docs/about.md`

2. **Find the member's card** (search for their name):
   ```html
   <div class="member-card">
   <img src="/images/aboutphotos/scott 1.jpg" alt="Scott Ewell" class="member-image-placeholder">
   <h3> Scott Ewell </h3>
   <span class="member-role">Twin Turbo Guitar</span>
   <div class="member-bio">
   "The sound fell from the sky..."
   Meet one of MLO's Twin Turbo Guitars, Scott Ewell!
   </div>
   ```

3. **Update what you need:**
   - **Photo**: Replace the image file in `docs/images/aboutphotos/` (keep same name, or update the `src` path)
   - **Name**: Change the text between `<h3>` tags
   - **Role**: Update `<span class="member-role">` text
   - **Bio**: Edit everything inside `<div class="member-bio">`
   - **Associated Acts**: Add/remove links in the `member-acts-list` section

#### Adding Associated Acts

Find the member's `member-acts-list` section:

```html
<div class="member-acts-list">
<div class="Associated Act"><a href="https://spotify.com/...">Band Name</a></div><br>
<div class="Associated Act"><a href="https://...">Another Band</a></div><br>
</div>
```

To add more, just copy a line and update the link and name.

#### Adding a New Band Member

1. **Copy an entire member card** (from `<div class="member-card">` to its closing `</div>`)

2. **Paste it** inside the `<div class="grid-2col">` section

3. **Update all the details** (photo, name, role, bio, acts)

4. **Add their photo** to `docs/images/aboutphotos/`

**Photo Requirements:**
- Square format (400px × 400px or larger)
- JPG or PNG format
- Good lighting, clear face
- File size under 500KB (use https://tinypng.com to compress)

---

### Updating Photos

**Time Required:** 5 minutes

#### Adding New Photos

1. **Prepare your image:**
   - Resize large photos (max 1200px wide for hero images, 800px for others)
   - Compress using https://tinypng.com or https://squoosh.app
   - Name it something clear: `band-photo-2026.jpg` not `IMG_8472.jpg`

2. **Upload to the right folder:**
   - Band photos: `docs/images/`
   - Member photos: `docs/images/aboutphotos/`
   - Show posters: `docs/images/`

3. **Reference it in your markdown file:**
   ```html
   <img src="/images/band-photo-2026.jpg" alt="Mona Lisa Overdrive live at Satellite">
   ```

#### Replacing the Hero Image (Homepage Banner)

1. **Add your new photo** to `docs/images/`
   - Recommended size: 1200px wide × 800px tall
   - Landscape orientation works best

2. **Open** `docs/index.md`

3. **Find this line** (around line 7):
   ```html
   <img src="images/1 band photo.jpg" alt="Mona Lisa Overdrive" class="hero-logo">
   ```

4. **Update the filename**:
   ```html
   <img src="images/your-new-photo.jpg" alt="Mona Lisa Overdrive" class="hero-logo">
   ```

#### Replacing the Logo/Favicon

1. **Add your new logo** to the main `mlo-website/` folder (not inside `docs/`)
   - Best format: Square PNG or JPG
   - Size: 512px × 512px minimum

2. **Open** `mkdocs.yml`

3. **Find these lines** (around 25-26):
   ```yaml
   favicon: MLO new logo white.JPG
   logo: MLO new logo white.JPG
   ```

4. **Update the filename**:
   ```yaml
   favicon: your-new-logo.png
   logo: your-new-logo.png
   ```

---

### Editing Homepage Text

**Time Required:** 5 minutes

**File You'll Edit:** `docs/index.md`

#### Changing the Scrolling Ticker Text

1. **Open** `docs/index.md`

2. **Find the ticker lines** (around 4 and 10):
   ```html
   <span class="ticker-text">Are you just breathing or are you really alive? /// Are you just breathing or are you really alive? /// Are you just breathing or are you really alive? /// </span>
   ```

3. **Update the message** - Important: Repeat it 3 times with ` /// ` between each:
   ```html
   <span class="ticker-text">New message here /// New message here /// New message here /// </span>
   ```

   The repetition makes the scrolling animation loop smoothly.

#### Changing the Band Description

1. **Find the description section** (around line 18):
   ```markdown
   ## We're Mona Lisa Overdrive:

   A neon heartbeat cracking the room open at the seams...
   ```

2. **Edit the text** - Use `<br>` for line breaks:
   ```markdown
   This is line one.<br>
   <br>
   This is line two with a space above it.<br>
   ```

---

## Publishing Your Changes

### Every time you make changes, follow these steps:

#### Step 1: Preview Locally (Optional but Recommended)

```bash
cd dog-solitude/mlo-website
mkdocs serve
```

- Open your browser to http://127.0.0.1:8000
- Check that everything looks right
- Press `Ctrl+C` to stop the preview server

#### Step 2: Build the Site

```bash
cd dog-solitude/mlo-website
mkdocs build
```

**What this does:** Converts your Markdown files into a complete website in the `site/` folder.

**Watch for errors:** If you see red error messages, there's a problem. Check:
- Did you close all your HTML tags? (`<div>` needs a `</div>`)
- Did you save all your files?
- Are image file paths correct?

#### Step 3: Deploy to Your Web Server

**Method 1: Manual Upload (via FTP/SFTP)**

1. Connect to your web hosting via FTP client (FileZilla, Cyberduck, etc.)
2. Upload the entire `site/` folder contents to your web server
3. Make sure files go to the correct public directory (often called `public_html` or `www`)

**Method 2: If Using GitHub Pages**

```bash
git add .
git commit -m "Updated show dates"
git push
```

The site will auto-deploy in 1-2 minutes.

**Method 3: If Using Netlify/Vercel**

Just push to GitHub - the site auto-deploys when you push to the main branch.

---

## Tips and Best Practices

### Before You Edit

1. **Make a backup** - Copy the entire `mlo-website/` folder somewhere safe
2. **Test locally first** - Use `mkdocs serve` to preview before deploying
3. **Check your work** - Proofread text, test all links

### While Editing

1. **Use a good text editor** - VS Code shows syntax errors and has nice formatting
2. **Be careful with HTML tags** - Every `<div>` needs a closing `</div>`
3. **Save frequently** - Don't lose your work!
4. **Check indentation** - In YAML files (`mkdocs.yml`), indentation matters

### Common Mistakes to Avoid

| Mistake | Problem | Solution |
|---------|---------|----------|
| Editing `site/` folder directly | Changes get overwritten | Only edit `docs/` folder |
| Wrong date format in shows | `data-date="April 18th"` | Must be `data-date="2026-04-18"` |
| Forgetting to build | Changes don't appear online | Always run `mkdocs build` |
| Image paths with `docs/` | Images don't show | Use `/images/photo.jpg` not `/docs/images/photo.jpg` |
| Mixing tabs and spaces | YAML errors | Use 2 spaces for indentation in `mkdocs.yml` |

### File Naming Conventions

**Good:**
- `show-poster-may-2026.png`
- `band-photo-satellite-lounge.jpg`
- `scott-profile-2026.jpg`

**Bad:**
- `IMG_8472.jpg` (not descriptive)
- `my photo.png` (spaces in filename)
- `SHOW POSTER!!.jpg` (special characters)

**Rules:**
- Use lowercase
- Use hyphens instead of spaces
- No special characters (except `-` and `_`)
- Be descriptive

---

## File Quick Reference

### Files You'll Edit Often

| File | Purpose | When to Edit |
|------|---------|--------------|
| `docs/index.md` | Homepage content | Updating hero text, social links |
| `docs/show-dates.md` | Shows page | Adding new shows |
| `docs/about.md` | Band member profiles | Updating bios, photos, projects |
| `mkdocs.yml` | Site settings | Changing footer links, enabling pages |

### Files You Might Edit Occasionally

| File | Purpose | When to Edit |
|------|---------|--------------|
| `docs/stylesheets/extra.css` | Colors and design | Changing brand colors (advanced) |
| `docs/music.md` | Music/releases | When you enable the music page |
| `docs/photos.md` | Photo gallery | When you enable the photos page |

### Files You Should Never Edit

| File/Folder | Why |
|-------------|-----|
| `site/` | Auto-generated, gets deleted on rebuild |
| `docs/javascripts/show-dates.js` | Advanced code, breaks show automation if wrong |

---

## Getting Help

### I Made a Mistake!

**Don't panic.** Here's what to do:

1. **Restore from backup** (you made one, right?)
2. **Or revert your changes** - just undo what you changed
3. **Run `mkdocs build --clean`** to rebuild fresh
4. **Check the error message** - it often tells you exactly what's wrong

### Error Messages

**"ERROR - Config file 'mkdocs.yml' does not exist."**
- You're in the wrong folder
- Solution: `cd dog-solitude/mlo-website`

**"ERROR - The 'docs_dir' should not contain the 'site_dir'."**
- Don't put `site/` inside `docs/`
- Solution: Delete `docs/site/` if it exists

**"ERROR - Doc file 'xyz.md' contains an error."**
- There's a syntax error in that file
- Solution: Check for unclosed HTML tags, missing quotes

### Common Questions

**Q: How do I know if my changes worked?**
- Run `mkdocs serve` and check http://127.0.0.1:8000 before deploying

**Q: Why don't I see my changes on the live site?**
- Did you run `mkdocs build`?
- Did you upload the new `site/` folder?
- Try clearing your browser cache (Cmd+Shift+R or Ctrl+Shift+R)

**Q: Can I have someone else edit the site?**
- Yes! Give them this guide and the `mlo-website/` folder

**Q: Where are the site backups?**
- You should make them manually
- Copy the entire `mlo-website/` folder to a safe location regularly

**Q: How do I add a new page to the navigation?**
- Uncomment it in `mkdocs.yml` under the `nav:` section
- Or add a new line: `- New Page: new-page.md`
- Create `docs/new-page.md` with your content
- Run `mkdocs build`

---

## Need More Technical Details?

See the **CONFIGURATION_GUIDE.md** for in-depth technical documentation, including:
- Complete CSS breakdown
- JavaScript functionality
- Advanced customization
- Troubleshooting

---

## Cheat Sheet

### Quick Build & Deploy

```bash
# 1. Preview your changes
cd dog-solitude/mlo-website
mkdocs serve
# Check http://127.0.0.1:8000

# 2. Build the site
mkdocs build

# 3. Deploy (upload site/ folder to web host)
```

### Quick Show Date Template

```html
<div class="event-card" data-date="YYYY-MM-DD">
<div class="event-date">Month Day, Year</div>
<div class="event-venue">Venue Name</div>
<div class="support-acts">with Opening Acts</div>
<div class="ticket-price">$X presale, $Y day-of</div>
<div class="ticket-link"><a href="URL">Get Tickets</a></div>
<div class="age">21+</div>
<div class="show-time">Doors 7pm Show 9pm</div>
<div class="event-details">
Description here...
<img src="/images/poster.png" alt="Poster">
</div>
<iframe src="GOOGLE_MAPS_EMBED" width="100%" height="300" style="border:0; border-radius: 8px; margin: 20px 0; box-shadow: 0 0 15px var(--glow-purple);" allowfullscreen="" loading="lazy"></iframe>
<div class="show-cta">
<a href="TICKET_URL" class="cta-button">Get Tickets</a>
<a href="FB_EVENT_URL" class="cta-button">Facebook Event</a>
<a href="MAPS_URL" class="cta-button">Get Directions</a>
</div>
</div>
```

---

**You've got this!** The site is designed to be easy to update. Just follow the steps, test before deploying, and you'll be managing the website like a pro in no time.

**Questions?** Check the CONFIGURATION_GUIDE.md or review this README.

---

**Last Updated:** April 6, 2026
**Website:** https://monalisaoverdrive.net
