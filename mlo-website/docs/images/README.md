# Image Organization Guide

## Folder Structure

```
images/
├── photos/
│   ├── live/        → Live performance photos
│   ├── promo/       → Promotional shots
│   ├── bts/         → Behind the scenes
│   └── fan/         → Fan submitted photos
├── press/           → Press kit images (hi-res downloads)
├── epk/             → EPK specific images
└── general/         → Logos, band photos, misc

videos/
├── music-videos/      → Official music videos
├── live-performances/ → Live show recordings
├── studio-sessions/   → Studio/BTS videos
└── visualizers/       → Audio visualizers
```

## File Naming Rules

### DO:
- Use lowercase letters only
- Use hyphens (-) to separate words
- Keep ALL original words - do not shorten or abbreviate
- Be descriptive

### DON'T:
- Use spaces
- Use underscores (_)
- Use capital letters
- Shorten words

### Examples:
✓ `eagles-dare-debut-show-april-2026.jpg`
✓ `mona-lisa-overdrive-band-photo-promotional.jpg`
✓ `behind-the-scenes-sound-check-setup.jpg`
✓ `front-street-brewery-collaboration-beer.jpg`

✗ `Eagles Dare Show.jpg` (capitals, spaces)
✗ `eagles_dare_show.jpg` (underscores)
✗ `edshow.jpg` (shortened/abbreviated)
✗ `show1.jpg` (not descriptive)

## Image Quality

- **Keep hi-def/full resolution** - DO NOT compress or optimize
- Upload original quality photos
- Git handles large files fine
- Only exclude files if they exceed GitHub's 100MB single file limit

## Using Images in Markdown Files

### From photos.md:
```markdown
<img src="images/photos/live/your-photo-name.jpg" alt="Description">
```

### From epk.md:
```markdown
<img src="images/epk/your-photo-name.jpg" alt="Description">
```

### From any .md file in docs/:
All paths are relative to the docs/ folder, so just use `images/folder/filename.jpg`

## Adding Photos to Gallery Pages

### In photos.md:
1. Upload photo to appropriate folder (live/promo/bts/fan)
2. Find the relevant section in photos.md
3. Copy the template card structure (in HTML comments)
4. Update the src path and alt text
5. Add caption with event/date info

### Template:
```html
<div class="card">
<img src="images/photos/live/your-photo-name.jpg" alt="Description" style="width: 100%; border-radius: 8px; margin-bottom: 10px;">
<p style="text-align: center; color: var(--neon-cyan);"><strong>Event Name</strong><br>Date - Venue</p>
</div>
```

## Large Files

If you have files larger than 100MB:
1. Consider if they're necessary for web display
2. If needed for archive, store separately
3. Uncomment the exclusion rules in .gitignore
4. Use web-optimized versions for the site (keep originals elsewhere)

Most photos under 10-20MB are fine to commit directly.

## Videos

### Hosting Recommendation

**DO NOT commit large video files to the repo.** Instead:

1. **Upload to YouTube or Vimeo** (recommended)
   - Professional hosting
   - Bandwidth handling
   - Better playback experience
   - Easy embedding

2. **Use embed codes in .md files**
   - YouTube: Get embed code from Share → Embed
   - Vimeo: Get embed code from Share → Embed

### Video File Naming (if using local files)

Same rules as photos:
- Lowercase only
- Hyphens instead of spaces
- Keep all words - no abbreviations
- Examples:
  ✓ `eagles-dare-debut-full-set-april-2026.mp4`
  ✓ `song-title-official-music-video.mp4`
  ✗ `video1.mp4`

### Local Video Files

Only use for:
- Small preview clips (under 25MB)
- Thumbnails/posters
- Short loops/backgrounds

For full videos, always use YouTube/Vimeo embedding.

### Adding Videos to videos.md

See the HTML comment templates in videos.md for:
- YouTube embed structure (responsive)
- Vimeo embed structure (responsive)
- Local video with controls

Path from videos.md: `videos/category/filename.mp4`
