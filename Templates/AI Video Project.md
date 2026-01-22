# <% tp.file.title %>

> Created: <% tp.date.now("YYYY-MM-DD HH:mm") %>

## Actions

### Step 1-2: Use Claude Code
Open terminal in this folder and run `claude`:
```
claude
```
Then ask:
- "Generate a 60s video script based on my concept below"
- "Generate storyboard with image prompts from the script"

### Step 3: Generate Images
```button
name 🖼️ Generate Images from Storyboard
type command
action Shell commands: Execute: Generate Images
color green
```

```button
name 🎲 Regenerate with New Seed
type command
action Shell commands: Execute: Generate Images (New Seed)
color blue
```

---

## Status
- [x] Idea/Concept
- [ ] Script (Claude Code)
- [ ] Storyboard (Claude Code)
- [ ] Images (Button above)
- [ ] Audio (manual: ElevenLabs)
- [ ] Edit (manual: DaVinci Resolve)
- [ ] Review
- [ ] Published

## Info
| Field | Value |
|-------|-------|
| Channel | jan-shorts |
| Target length | 60s |
| Style | AI-generated |
| Publish date | |

## Concept

> **Write your idea here. Claude Code will use this to generate script.**

**Hook (first 2 seconds):**


**Core idea (one sentence):**


**Why it will work:**


---

## Generated Files
- [[script]] - Review and edit
- [[storyboard]] - Review prompts
- [[image-gallery]] - Select best images

## Links
- Final video:
- YouTube link:

## Generation Notes
- **Style reference:**
- **Seed:** (use same seed for consistency)
- **ComfyUI workflow:**

## Revision Log
| Date | What Changed | Why |
|------|--------------|-----|
| <% tp.date.now("YYYY-MM-DD") %> | Created project | Initial |

## Performance (post-publish)
| Metric | Value |
|--------|-------|
| Views (24h) | |
| Views (7d) | |
| CTR | |
| Retention | |
| Learnings | |
