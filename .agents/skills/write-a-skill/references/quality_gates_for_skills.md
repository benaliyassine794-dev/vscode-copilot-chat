# Quality Gates for Skill Libraries

This reference answers exactly one decision: **what checks must pass before a new skill enters the library, and why?**

Pair with `scripts/skill_review_checklist_runner.py` for the automated gate.

## The Six Mandatory Gates (per Matt Pocock's checklist)

| # | Check | Why it matters |
|---|---|---|
| 1 | Description includes triggers ("Use when ...") | Without trigger, agent guesses when to activate — high false-positive rate |
| 2 | SKILL.md under 100 lines | Over-conditioning; agent reads tangential detail and misroutes |
| 3 | No time-sensitive info | Dates/versions/year refs rot; agent receives stale guidance |
| 4 | Consistent terminology | Synonym drift confuses the agent + downstream users |
| 5 | Concrete examples included | Without an example, agent constructs from scratch and hallucinates |
| 6 | References one level deep | Deep nesting = agent gives up resolving the reference chain |

## Why Programmatic, Not Manual

Manual review of these 6 items:
- Drifts across reviewers (different humans interpret "concrete example" differently)
- Slows PR cadence (every reviewer re-reads every skill against every check)
- Misses regressions (a skill once compliant can drift across updates)

Programmatic gate (the `skill_review_checklist_runner.py` tool):
- Same verdict regardless of reviewer
- Runs in CI in seconds
- Catches regressions automatically
- Documents the explicit criteria — no implicit reviewer judgment

## Quality Gate Sequencing

Apply gates in this order during PR:

```
1. Description validator      (fast; catches most issues early)
2. Structure validator        (fast; folder layout + line counts)
3. Review checklist runner    (combined; all 6 of Matt's items)
4. Karpathy complexity check  (code quality; only if scripts/ exists)
5. Link integrity scan        (cross-skill references)
6. Citation density check     (references/ bibliography)
```

## Common Failure Modes (and Fixes)

| Failure | Common cause | Fix |
|---|---|---|
| Description >1024 chars | Trying to describe every feature | Cut to verbs + objects + triggers; move details to SKILL.md |
| SKILL.md >100 lines | Inline workflows that belong in references | Move workflows to `references/<workflow>.md`; replace with 1-line pointers |
| Missing "Use when" | Description written as marketing copy | Rewrite second sentence to start with "Use when ..." |
| Time-sensitive info | "As of October 2024 ..." | Remove date; describe pattern that doesn't depend on date |
| No examples | Abstract guidance only | Add at least 1 code block showing minimum invocation |
| Deep references | Subfolder structure under references/ | Flatten to one level |

---

**Source authorities (non-exhaustive):**

- **Matt Pocock — write-a-skill** (https://github.com/mattpocock/skills/, MIT) — the 6-item review checklist
- **Karpathy, A. — public commentary on LLM coding pitfalls** (X.com, 2024-2025) — discipline framework
- **Anthropic — Building agents with skills** (https://docs.claude.com/en/docs/agents/skills) — official skill quality guidance
- **Continuous Integration / Continuous Deployment patterns** — Humble & Farley (Continuous Delivery, 2010) — gate sequencing principles
- **The Phoenix Project** (Kim et al., 2013) + Three Ways of DevOps — quality gates as constraint management
- **Hyrum's Law** as applied to skill libraries — once a skill's behavior is observed, downstream depends on it
- **Software craftsmanship + the Boy Scout Rule** — leave each skill cleaner than you found it; gates enforce the floor
