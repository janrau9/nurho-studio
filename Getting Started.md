# Getting Started

Quick setup guide to start producing AI shorts.

---

## Step 1: Install Claude Code

Both Jan and Jarjan need Claude Code installed:

```bash
# Install Claude Code (requires Pro or Max subscription)
npm install -g @anthropic-ai/claude-code

# Or with Homebrew
brew install claude-code
```

Then run `claude` in terminal to authenticate.

---

## Step 2: Install Obsidian Plugins

Open Obsidian → Settings → Community Plugins → Browse

Install these two:
- **Shell commands** - Runs automation scripts
- **Buttons** - Clickable buttons in notes

After installing both, **restart Obsidian**.

---

## Step 3: Python Setup (For Image Generation Only)

Only needed when you want to batch-generate images from ComfyUI.

```bash
cd /mnt/c/Users/janra/Documents/nurho-studio
pip install -r scripts/requirements.txt
```

Create `.env` for ComfyUI URL:

```bash
cp .env.example .env
```

Edit `.env`:
```
COMFYUI_URL=http://localhost:8000
```

---

## Step 4: Verify ComfyUI

Make sure ComfyUI Desktop is running on `http://localhost:8000`

(Skip until you need image generation)

---

## You're Ready!

### Your Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  1. CREATE PROJECT                                          │
│     Dashboard.md → Click "New Project" → Enter title        │
│     → Folder created, README opens                          │
│     → Fill in the Concept section                           │
├─────────────────────────────────────────────────────────────┤
│  2. GENERATE SCRIPT                                         │
│     Open terminal in project folder:                        │
│     $ claude                                                │
│     $ /generate-script                                      │
│     → Review script.md → Approve or edit                    │
├─────────────────────────────────────────────────────────────┤
│  3. GENERATE STORYBOARD                                     │
│     $ /generate-storyboard                                  │
│     → Review storyboard.md → Tweak prompts if needed        │
├─────────────────────────────────────────────────────────────┤
│  4. GENERATE IMAGES                                         │
│     Click "Generate Images" button in Obsidian              │
│     → Review images in image-gallery.md                     │
├─────────────────────────────────────────────────────────────┤
│  5. MANUAL STEPS                                            │
│     → Audio: ElevenLabs (paste script, download VO)         │
│     → Edit: DaVinci Resolve (assemble everything)           │
│     → Publish: YouTube upload                               │
└─────────────────────────────────────────────────────────────┘
```

### Custom Commands

| Command | What it does |
|---------|--------------|
| `/generate-script` | Reads concept from README, creates script.md |
| `/generate-storyboard` | Reads script.md, creates storyboard.md with image prompts |

---

## Quick Links

- [[01-Projects/Dashboard|Dashboard]] - Start here
- [[01-Projects/Video Pipeline|Video Pipeline]] - Kanban board
- [[02-Knowledge/Workflows/ai-shorts-workflow|AI Shorts Workflow]] - Full production SOP

---

## Troubleshooting

### Claude Code not found
```bash
npm install -g @anthropic-ai/claude-code
```
Make sure you have Node.js 18+ installed.

### "Not authenticated"
Run `claude` and follow the login prompts. Requires Pro or Max subscription.

### Images not generating
- Is ComfyUI running?
- Check `COMFYUI_URL` in `.env` matches your setup

### Buttons don't work in Obsidian
- Did you install Shell commands plugin?
- Did you restart Obsidian after installing?
