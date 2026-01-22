<%*
// Prompt for project title
const title = await tp.system.prompt("Project Title", "my-awesome-video");
if (!title) return;

// Clean title for folder name
const cleanTitle = title.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');

// Create folder path for Jan's channel
const date = tp.date.now("YYYY-MM-DD");
const folderName = `${date}-${cleanTitle}`;
const folderPath = `01-Projects/jan-shorts/${folderName}`;

// Create the folder
await app.vault.createFolder(folderPath);

// Create README.md with AI video project template
const projectContent = `# ${title}

> Created: ${tp.date.now("YYYY-MM-DD HH:mm")}
> Creator: **Jan**
> Type: AI Generated

## Actions

### Step 1: Generate Script
Open terminal in this folder:
\`\`\`bash
cd "${folderPath}"
claude
\`\`\`
Run: \`/generate-script\` → Review script.md → Approve or edit

### Step 2: Generate Storyboard
Run: \`/generate-storyboard\` → Review storyboard.md → Approve or edit prompts

### Step 3: Generate Images

\`\`\`button
name 🖼️ Generate Images
type command
action Shell commands: Execute: Generate Images
color green
\`\`\`

\`\`\`button
name 🎲 Regenerate (New Seed)
type command
action Shell commands: Execute: Generate Images (New Seed)
color blue
\`\`\`

---

## Status
- [x] Idea/Concept
- [ ] Script (Claude Code)
- [ ] Storyboard (Claude Code)
- [ ] Images (ComfyUI)
- [ ] Audio (ElevenLabs)
- [ ] Edit (DaVinci Resolve)
- [ ] Review
- [ ] Published

## Info
| Field | Value |
|-------|-------|
| Creator | Jan |
| Channel | jan-shorts |
| Type | AI Generated |
| Target length | 60s |
| Publish date | |

## Concept

> **Write your idea here. Claude will use this to generate the script.**

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
- **Seed:**
- **ComfyUI workflow:**

---

## Performance (post-publish)
| Metric | Value |
|--------|-------|
| Views (24h) | |
| Views (7d) | |
| CTR | |
| Retention | |
| Learnings | |
`;

// Create the file
const filePath = `${folderPath}/README.md`;
const file = await app.vault.create(filePath, projectContent);

// Open it
await app.workspace.getLeaf().openFile(file);

new Notice(`✅ Created: ${folderName}`);
tR = "";
-%>
