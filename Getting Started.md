# Getting Started

Complete guide for Nurho Studio - YouTube shorts automation for Jan and Jarjan.

---

## Quick Setup Checklist

- [ ] Install Claude Code (`npm install -g @anthropic-ai/claude-code`)
- [ ] Install Obsidian plugins: **Shell commands** + **Buttons**
- [ ] Restart Obsidian
- [ ] Run `pip install -r scripts/requirements.txt`
- [ ] Copy `.env.example` to `.env`
- [ ] Verify ComfyUI runs on `localhost:8000`

---

## Vault Structure

```
nurho-studio/
├── Dashboard.md              ← Start here - create new projects
├── Video Pipeline.md         ← Kanban board - track all videos
├── Getting Started.md        ← This guide
│
├── 00-Inbox/                 ← Quick capture (random ideas, links)
│
├── 01-Projects/              ← All video projects
│   ├── jan-shorts/           ← Jan's AI-generated videos
│   │   └── 2026-01-22-cat-rescue/
│   │       ├── README.md     ← Project hub (concept, status, buttons)
│   │       ├── script.md     ← Generated script
│   │       ├── storyboard.md ← Scene prompts for ComfyUI
│   │       ├── image-gallery.md ← Review generated images
│   │       └── images/       ← Generated images
│   └── jarjan-shorts/        ← Jarjan's clip videos
│
├── 02-Knowledge/             ← SOPs, tool configs, learnings
│   ├── Workflows/            ← How-to guides
│   └── Tools/                ← Tool setup docs
│
├── 03-Assets/                ← Reusable assets (links, not files)
│
├── ProjectTemplates/         ← Templates for new projects
│   ├── New-AI-Video.md       ← Jan's template
│   └── New-Clip-Video.md     ← Jarjan's template
│
├── scripts/                  ← Python automation
│   └── generate_images.py    ← ComfyUI batch generation
│
└── .claude/skills/           ← Custom Claude commands
    ├── generate-script/      ← /generate-script
    └── generate-storyboard/  ← /generate-storyboard
```

---

## Full Workflow: Idea → Published Video

### Step 1: Create Project
**Where:** Obsidian → [[Dashboard]]
**Action:** Click "New Video Project" → Select template → Enter title
**Result:** Folder created in `01-Projects/jan-shorts/YYYY-MM-DD-title/`

### Step 2: Write Concept
**Where:** Project README.md (opens automatically)
**Action:** Fill in the Concept section:
- **Hook** - What grabs attention in first 2 seconds
- **Core idea** - One sentence summary
- **Why it will work** - Target audience, emotion, trend

### Step 3: Generate Script
**Where:** Terminal in project folder
```bash
cd "01-Projects/jan-shorts/your-project"
claude
/generate-script
```
**Result:** `script.md` with timed scenes and voiceover (~150 words)
**Review:** Read → Edit if needed → Approve

### Step 4: Generate Storyboard
**Where:** Same Claude session
```bash
/generate-storyboard
```
**Result:** `storyboard.md` with 12 scenes and ComfyUI prompts
**Review:** Check prompts → Tweak for your style → Approve

### Step 5: Generate Images
**Where:** Obsidian → Project README.md
**Action:** Click "🖼️ Generate Images" button
**Requires:** ComfyUI running on localhost:8000
**Result:** `images/` folder + `image-gallery.md`
**Review:** Check images → Click "Regenerate (New Seed)" for bad ones

### Step 6: Generate Audio (Manual)
**Where:** ElevenLabs website
**Action:**
1. Copy "Full Script" section from `script.md`
2. Paste into ElevenLabs
3. Select voice → Generate → Download
4. Also: Pick background music from YouTube Audio Library

### Step 7: Edit Video (Manual)
**Where:** DaVinci Resolve
**Settings:** 1080x1920 (9:16), 30fps
**Steps:**
1. Import: images, voiceover, music
2. Lay voiceover on timeline first
3. Sync images to VO timing
4. Add Ken Burns (zoom/pan) to images
5. Add captions - large font, readable on mobile
6. Add music bed at -18dB under VO
7. Color grade for consistency
8. Export: MP4 H.264, 15-20 Mbps

### Step 8: Review
**Where:** Your phone
**Action:** Transfer video → Watch like a viewer would
**Checklist:**
- [ ] Hook grabs in first 2 seconds?
- [ ] Text readable on small screen?
- [ ] Audio clear, no clipping?
- [ ] Pacing feels right?
- [ ] Ending satisfying?

### Step 9: Publish (Manual)
**Where:** YouTube Studio
**Action:**
1. Upload video
2. Title: Hook-driven with curiosity gap
3. Description: Brief + hashtags + "Made with AI"
4. Thumbnail: First frame or custom
5. Schedule or publish immediately
**Then:** Update README with YouTube link, move Kanban card to "Published"

### Step 10: Track Performance
**When:** 24h and 7d after publish
**Action:** Update Performance table in README:
- Views (24h / 7d)
- CTR (click-through rate)
- Retention (avg % watched)
- Learnings: What worked, what didn't

---

## Custom Commands

| Command | What it does |
|---------|--------------|
| `/generate-script` | Reads concept from README → Creates `script.md` |
| `/generate-storyboard` | Reads script → Creates `storyboard.md` with image prompts |

---

## Tools Used

| Tool | Purpose |
|------|---------|
| **Obsidian** | Project management, notes, buttons |
| **Claude Code** | Generate script & storyboard |
| **ComfyUI** | Generate images from prompts |
| **ElevenLabs** | Text-to-speech voiceover |
| **DaVinci Resolve** | Video editing |
| **YouTube Studio** | Publishing |

---

## Quick Links

- [[Dashboard]] - Start here
- [[Video Pipeline]] - Kanban board
- [[02-Knowledge/Workflows/ai-shorts-workflow|AI Shorts Workflow]] - Detailed SOP

---

## Troubleshooting

### Claude Code not found
```bash
npm install -g @anthropic-ai/claude-code
```
Requires Node.js 18+

### "Not authenticated"
Run `claude` and follow login prompts. Requires Pro or Max subscription.

### Buttons don't work
1. Install Shell commands plugin
2. Install Buttons plugin
3. Restart Obsidian

### Images not generating
1. Is ComfyUI running?
2. Check `.env` has correct `COMFYUI_URL`
3. Check ComfyUI has the required model

### Command not found: /generate-script
Make sure you're running `claude` from the vault root, not a subfolder.
