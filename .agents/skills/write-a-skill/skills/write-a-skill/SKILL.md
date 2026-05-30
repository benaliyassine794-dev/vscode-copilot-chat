---
name: write-a-skill
description: Create new agent skills with proper structure, progressive disclosure, and bundled resources. Use when user wants to create, write, build, or author a new skill — including skills for music production, multilingual content, video editing and montage, social media, analytics, AI workflows, or any other domain.
license: MIT
metadata:
  derived_from: "https://github.com/mattpocock/skills/tree/main/skills/productivity/write-a-skill"
  original_author: "Matt Pocock (@mattpocock)"
  original_license: MIT
  version: 1.1.0
---

# Write a Skill

Create new Claude agent skills that follow progressive disclosure, stay under 100
lines in SKILL.md, and bundle references + scripts for deterministic operations.

## Phase 1 — Gather

1. Ask the user: **What is the skill's purpose?** (one sentence)
2. Ask: **What triggers this skill?** ("Use when..." — be specific)
3. Ask: **What domain?**
   - Content & Media: social media, copywriting, music, video editing, montage
   - Languages & Localization: multilingual, translation, RTL/LTR content
   - Engineering: code review, refactoring, testing, APIs, SDKs
   - Data & Analytics: reporting, dashboards, metrics analysis
   - AI & Automation: prompt engineering, workflows, agent design
   - Business: strategy, finance, project management
   - Creative: design, storytelling, music production, brand identity
4. Ask: **What should references cover?** (deep detail that doesn't fit in 100 lines)
5. Ask: **What should scripts do?** (deterministic operations: validate, generate, check)

## Phase 2 — Draft

### SKILL.md (must be ≤ 100 lines)
```yaml
---
name: <kebab-case-name>
description: <Third-person. Action verb first. "Use when..." trigger. ≤ 1024 chars.>
version: 1.0.0
---
```

**Structure rules:**
- Phases or steps, not prose paragraphs
- Every heavy detail → `references/<filename>.md`
- Every repeatable operation → `scripts/<name>.py`
- No time-sensitive info (dates, version numbers in body text)
- Consistent terminology throughout

### References (one level deep — NO subdirectories)
```
references/
  <topic_1>.md    ← deep guides, tables, examples
  <topic_2>.md
```

### Scripts (stdlib Python only — no LLM calls, no network)
```
scripts/
  <validator>.py  ← validate, score, check, format, generate
```

## Phase 3 — Review (Matt Pocock's 6-item checklist)

Run: `python scripts/skill_review_checklist_runner.py <path/to/SKILL.md>`

1. **Description triggers correctly** — does "Use when" match real user intent?
2. **≤ 100 lines** — SKILL.md stays lean
3. **No time-sensitive info** — no "as of 2024", specific version numbers
4. **Consistent terminology** — same names used throughout all files
5. **Concrete examples** — at least one worked example per framework/pattern
6. **References one level deep** — flat structure, no nested subdirectories

Fix any failures, then push the skill to `.agents/skills/<skill-name>/`.
