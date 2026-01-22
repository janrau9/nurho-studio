# Automation Setup Guide

## Quick Start

### 1. Install Obsidian Plugins

Open Obsidian Settings → Community Plugins → Browse, then install:

1. **Shell commands** - Runs the Python scripts
2. **Buttons** - Creates clickable buttons in notes

After installing, **restart Obsidian** to load the pre-configured commands.

The commands are already configured:
- `Generate Script` - Creates script from your concept
- `Generate Storyboard` - Creates prompts from script
- `Generate Images` - Runs ComfyUI to generate images

### 2. Install Python Dependencies

```bash
cd /mnt/c/Users/janra/Documents/nurho-studio
pip install -r scripts/requirements.txt
```

### 2. Configure API Keys

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your keys
```

Required keys:
- `ANTHROPIC_API_KEY` - Get from https://console.anthropic.com/

Optional (for future automation):
- `ELEVENLABS_API_KEY`
- YouTube API credentials

### 3. Verify ComfyUI is Running

Make sure ComfyUI Desktop is running on `http://localhost:8000`

---

## Workflow Commands

Run these from the vault root directory.

### Generate Script (Idea → Script)

```bash
python scripts/generate_script.py "01-Projects/jan-shorts/YOUR-PROJECT-FOLDER"
```

**Input:** Project folder with `README.md` containing your concept
**Output:** `script.md` in the same folder

### Generate Storyboard (Script → Prompts)

```bash
python scripts/generate_storyboard.py "01-Projects/jan-shorts/YOUR-PROJECT-FOLDER"
```

**Input:** `script.md` from previous step
**Output:** `storyboard.md` with scene-by-scene prompts

### Generate Images (Prompts → Images)

```bash
python scripts/generate_images.py "01-Projects/jan-shorts/YOUR-PROJECT-FOLDER"
```

**Optional flags:**
- `--seed 12345` - Use specific seed for reproducibility

**Input:** `storyboard.md` with prompts
**Output:**
- `images/` folder with generated PNGs
- `image-gallery.md` for reviewing in Obsidian

---

## Project Folder Structure

After running all commands, your project folder will look like:

```
01-Projects/jan-shorts/2026-01-21-my-video/
├── README.md           # Project overview + concept
├── script.md           # Generated script
├── storyboard.md       # Scene prompts
├── image-gallery.md    # Review generated images
└── images/
    ├── scene-01.png
    ├── scene-02.png
    └── ...
```

---

## Troubleshooting

### "ANTHROPIC_API_KEY not set"
Make sure you created `.env` from `.env.example` and added your key.

### "Cannot connect to ComfyUI"
1. Open ComfyUI Desktop
2. Check it's running on port 8000 (or update `COMFYUI_URL` in `.env`)

### "No concept found"
Make sure your project's README.md has a `## Concept` section with your idea.

### Images look wrong / inconsistent
- Use the same `--seed` value across regenerations
- Check your ComfyUI has the model specified in the workflow
- Adjust the workflow in `generate_images.py` for your setup

---

## Customizing the Workflow

### Change ComfyUI Workflow

Edit `scripts/generate_images.py` and modify the `BASIC_WORKFLOW` dict to match your preferred ComfyUI setup.

### Change Claude Model

Edit the `CLAUDE_MODEL` variable in `generate_script.py` and `generate_storyboard.py`.

### Adjust Prompts

Edit the `SCRIPT_PROMPT` and `STORYBOARD_PROMPT` strings to change how Claude generates content.
