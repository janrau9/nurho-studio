# Nurho Studio - Obsidian Vault

YouTube shorts automation studio for 2 people:
- **Jan** (dev) - AI video generation with ComfyUI
- **Jarjan** (creative) - Clipping/repurposing with DaVinci Resolve

## Vault Structure

```
00-Inbox/          - Quick capture (ideas, links, random thoughts)
01-Projects/       - Video projects organized by channel
  _Templates/      - Project templates (ai-video, clip-video)
  jan-shorts/      - Jan's AI-generated shorts
  jarjan-shorts/   - Jarjan's clipping channel
  Video Pipeline.md - Kanban board for tracking all videos
02-Knowledge/      - SOPs, tool configs, learnings
03-Assets/         - Reusable assets registry (links, not files)
Daily Notes/       - Daily standups
Templates/         - Obsidian templates
```

## Key Files

- `01-Projects/Video Pipeline.md` - Main Kanban board (requires Kanban plugin)
- `01-Projects/_Templates/ai-video-template.md` - Template for Jan's AI shorts
- `01-Projects/_Templates/clip-video-template.md` - Template for Jarjan's clips
- `02-Knowledge/Workflows/ai-shorts-workflow.md` - Full AI video production SOP
- `Templates/Daily Note.md` - Daily standup template

## Workflow

1. Capture ideas in `00-Inbox/`
2. Create video project folder using template in appropriate channel folder
3. Track progress on `Video Pipeline.md` Kanban board
4. Document learnings in `02-Knowledge/Learnings/`

## Git Sync

Both Jan and Jarjan sync via git. Large media files are NOT committed - only links/references in markdown.

## Obsidian Plugins Needed

- Kanban (for Video Pipeline board)
- Templater (for auto-generating project folders)
- Calendar (for daily notes)
