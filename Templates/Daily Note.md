---
date: <% tp.file.title %>
tags: [daily-note]
---
# <% tp.date.now("dddd, MMMM DD, YYYY", 0, tp.file.title, "YYYY-MM-DD") %>

[[Daily Notes/<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>|← Yesterday]] · [[Daily Notes/<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>|Tomorrow →]]

> [!note]  What were you grateful for yesterday
> 1.

---

> [!tip] High Priority
> ```tasks
> not done
> tags include #priority/high
> due before <% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>
> hide tags
> hide backlink
> hide edit button
> hide postpone button
> ```

> [!todo] Low Priority
> ```tasks
> not done
> tags include #priority/medium
> due before <% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>
> hide tags
> hide backlink
> hide edit button
> hide postpone button
> ```

> [!success] Completed
> ```tasks
> done on <% tp.file.title %>
> hide tags
> hide backlink
> hide edit button
> hide postpone button
> ```

> [!quote] Journal & ideas
> -

---

> [!todo] Plan tomorrow (<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>)
> - [ ]  

---

> [!success] What went well?
> -

> [!warning] What could improve?
> -
