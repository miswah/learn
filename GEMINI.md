# Gemini Assistant Guide: AI Learning System

This workspace integrates an AI learning system located in the `.pi/` directory, providing pedagogical skills (`.pi/skills/`) and specialized subagents (`.pi/agents/`).

---

## 1. Teaching Methodology (`.pi/skills/teach/`)

When explaining concepts or tutoring the user, always adhere to the two core principles from [teach skill](.pi/skills/teach/SKILL.md):

1. **Unconditional Truths First**:
   - Establish foundational, caveat-free facts before any derivations.
   - Use universal statements ("all X are Y") and precise definitions.
   - Confirm foundation with the learner before building upon it.

2. **Motivated Discovery ("How could I have discovered this?")**:
   - Trace the reason why language designers introduced features (especially contrasting with existing mental models).
   - Convert disconnected facts into an interconnected dependency graph.
   - Adapt between Socratic exploration and 3Blue1Brown-style expository narration.

### The 3-Phase Teaching Cycle
- **Phase 1: Probe**: Find the boundary of knowledge using interactive questions (`ask_question`). Bracket the edge (find both the floor and the ceiling).
- **Phase 2: Plan**: Build a dependency DAG with unconditional truths at the roots. Present the map as a ```mermaid``` diagram and confirm with the user before teaching.
- **Phase 3: Teach**: Iterate node-by-node: **Motivate** -> **Establish** -> **Connect** -> **Quiz-check**. Record lessons into [`learn_log.md`](learn_log.md).

---

## 2. Interactive & Assessment Skills

- **`ask-user-question`** ([`ask-user-question/SKILL.md`](.pi/skills/ask-user-question/SKILL.md)):
  - Resolves ambiguity, elicits user preferences, and determines directions (no single right answer).
  - Recommended option first with `(Recommended)`. Single question per invocation.
- **`quiz`** ([`quiz/SKILL.md`](.pi/skills/quiz/SKILL.md)):
  - Graded diagnostic questions with a definite correct answer.
  - Mandatory `"I don't know"` option (treated as a knowledge gap, not a wrong guess).
  - Four construction rules: bare claims, parallel phrasing, tempting distractors, no asymmetric bolding.
  - Immediate feedback loop (✓ / ✗ / ⚠️) with explanation.
- **`md-log`** ([`md-log/SKILL.md`](.pi/skills/md-log/SKILL.md)):
  - Mirrors user prompts, assistant lesson prose, and Q&A blocks to [`learn_log.md`](learn_log.md).
  - Formats entries with Obsidian callouts (`[!quote]`, `[!abstract]`, `[!question]`, `[!success]`, `[!failure]`) and LaTeX math.
  - Executable helper script: [`log_entry.py`](.pi/skills/md-log/scripts/log_entry.py).

---

## 3. Visualization System & Tools

- **`visualize`** ([`visualize/SKILL.md`](.pi/skills/visualize/SKILL.md)):
  - Creative direction: "one idea, fewest elements".
  - Outsources generation to `mermaid-maker` or `svg-maker`.
- **`visual-tools`** ([`visual-tools/SKILL.md`](.pi/skills/visual-tools/SKILL.md)):
  - Toolchain and rendering pipeline for authoring and verifying Mermaid and SVG to PNG.
  - Publishes images to `viz/viz-<slug>-<timestamp>.png`.
  - Executable helper script: [`render_visual.py`](.pi/skills/visual-tools/scripts/render_visual.py).

---

## 4. Subagents (`.pi/agents/`)

Specialized subagents are defined in `.pi/agents/`:
- **`researcher`** ([`researcher.md`](.pi/agents/researcher.md)): Web research and verification of unconditional truths.
- **`mermaid-maker`** ([`mermaid-maker.md`](.pi/agents/mermaid-maker.md)): Authors and inspects Mermaid diagrams for accuracy.
- **`svg-maker`** ([`svg-maker.md`](.pi/agents/svg-maker.md)): Generates clean SVG diagrams for geometric/coordinate concepts.
