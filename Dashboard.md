# Video Production Dashboard

```button
name ➕ New Video Project
type command
action Templater: Open Insert Template modal
color purple
```

> **Keyboard:** `Ctrl+P` → type "New AI Video" or "New Clip Video"

```button
name 📋 Open Pipeline Board
type link
action [[Video Pipeline]]
color default
```

---

## Quick Stats

### In Progress
```dataview
LIST
FROM "01-Projects/jan-shorts"
WHERE contains(file.name, "README") AND !completed
LIMIT 5
```

### Recently Published
```dataview
TABLE publish-date as "Published"
FROM "01-Projects/jan-shorts"
WHERE completed
SORT publish-date DESC
LIMIT 5
```

---

## Quick Links

- [[Getting Started]] - First time setup
- [[Video Pipeline]] - Kanban board
- [[02-Knowledge/Workflows/ai-shorts-workflow|AI Shorts Workflow]] - Full SOP
- [[02-Knowledge/Tools/automation-setup|Automation Setup]] - Script setup guide
- [[02-Knowledge/Tools/comfyui-setup|ComfyUI Setup]] - Generation settings
