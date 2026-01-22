# AI Shorts Generation Workflow

## Pipeline Overview
1. **Concept** (5 min) - Hook + core idea
2. **Script** (15 min) - Write or AI-generate, refine hook
3. **Storyboard** (15 min) - Break into 5-sec scenes, write prompts
4. **Image Generation** (30 min) - ComfyUI batch generation
5. **Video Generation** (30 min) - Animate images or generate clips
6. **Audio** (15 min) - VO, background music, SFX
7. **Edit** (30 min) - Assemble in DaVinci/CapCut
8. **Review** (10 min) - Self-review or brother review
9. **Publish** (5 min) - Upload, metadata, schedule

## Step Details

### 1. Concept
- Start with a hook that grabs in first 1-2 seconds
- Core idea should be explainable in one sentence
- Check if similar content exists, find differentiator

### 2. Script
- Use Claude for initial draft if stuck
- Structure: Hook → Build-up → Payoff
- Keep under 150 words for 60s video
- Read aloud to check pacing

### 3. Storyboard
- Break into ~5 second scenes (12 scenes for 60s)
- Write image generation prompt for each scene
- Note camera movement / animation style
- Include text overlay notes

### 4. Image Generation
- Use consistent style seed across scenes
- Batch generate in ComfyUI
- Generate 2-3 variants per scene, pick best
- Upscale selected images

### 5. Video Generation
- Animate with ComfyUI or external tool
- Keep motion subtle to avoid artifacts
- Target 24fps minimum
- Check for consistency between scenes

### 6. Audio
- VO: ElevenLabs or record yourself
- Music: Royalty-free, match energy to content
- SFX: Subtle accents, don't overdo
- Mix levels: VO loudest, music bed under

### 7. Edit
- Assemble in DaVinci Resolve
- Add captions (burned in or auto)
- Color grade for consistency
- Export: 1080x1920, 30fps, high bitrate

### 8. Review
- Watch on phone (actual viewing experience)
- Check: hook strength, pacing, audio levels
- Get brother review if time permits

### 9. Publish
- Title: Hook-driven, curiosity gap
- Description: Keywords + CTA
- Tags: Relevant, not spammy
- Schedule for optimal time

## Automation Opportunities
- [ ] Script generation with Claude
- [ ] Batch prompt generation from storyboard
- [ ] ComfyUI workflow for consistent style
- [ ] Auto-upload script (future)

## Tools
| Purpose | Tool |
|---------|------|
| Script | Claude / manual |
| Images | ComfyUI |
| Video | ComfyUI / Runway |
| Audio | ElevenLabs / stock |
| Edit | DaVinci Resolve |
| Publish | Manual → automate later |

## Quality Checklist
- [ ] Hook grabs attention in first 2 seconds
- [ ] No awkward pauses or dead air
- [ ] Audio levels consistent throughout
- [ ] Text is readable on mobile
- [ ] No AI artifacts visible
- [ ] Ending has clear payoff or CTA
