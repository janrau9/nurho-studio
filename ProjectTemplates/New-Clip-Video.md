<%*
// Prompt for project title
const title = await tp.system.prompt("Project Title", "my-clip-video");
if (!title) return;

// Clean title for folder name
const cleanTitle = title.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');

// Create folder path for Jarjan's channel
const date = tp.date.now("YYYY-MM-DD");
const folderName = `${date}-${cleanTitle}`;
const folderPath = `01-Projects/jarjan-shorts/${folderName}`;

// Create the folder
await app.vault.createFolder(folderPath);

// Create README.md with clip video project template
const projectContent = `# ${title}

> Created: ${tp.date.now("YYYY-MM-DD HH:mm")}
> Creator: **Jarjan**
> Type: Clip/Repurpose

## Status
- [x] Idea/Concept
- [ ] Source Selection
- [ ] Clip Extraction
- [ ] Edit
- [ ] Captions/Text
- [ ] Review
- [ ] Published

## Info
| Field | Value |
|-------|-------|
| Creator | Jarjan |
| Channel | jarjan-shorts |
| Type | Clip/Repurpose |
| Target length | 60s |
| Publish date | |

## Source Material

**Original video/stream:**


**Timestamp range:**
- Start:
- End:

**Why this clip works:**


---

## Edit Notes

### DaVinci Resolve Settings
- Resolution: 1080x1920 (9:16)
- Frame rate: 30fps
- Export: MP4 H.264, 15-20 Mbps

### Captions
- Style:
- Font:
- Position:

### Music/SFX
- Background track:
- Sound effects:

---

## Links
- Source video:
- Final video:
- YouTube link:

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
