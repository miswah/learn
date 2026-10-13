# Agent Guidelines: Workspace Skills & Subagents

This file defines the project instructions and multi-agent roles for Gemini and Antigravity agents in this workspace.

---

## Workspace Structure

- **`.pi/skills/teach/`**: Pedagogical skill defining the "Unconditional Truths First" and "Motivated Discovery" teaching method.
- **`.pi/skills/visualize/`**: Visualization skill for diagramming concepts minimally and accurately.
- **`.pi/skills/ask-user-question/`**: Clarifying and preference questioning protocol.
- **`.pi/skills/quiz/`**: Diagnostic graded knowledge testing with immediate feedback.
- **`.pi/skills/md-log/`**: Session mirroring to `learn_log.md` with Obsidian callouts.
- **`.pi/skills/visual-tools/`**: Toolchain for authoring, editing, and rendering Mermaid & SVG diagrams.
- **`.pi/agents/`**: Role definitions for subagents (`researcher.md`, `mermaid-maker.md`, `svg-maker.md`).
- **`learn_log.md`**: Running study log where dependency diagrams, lessons, and node explanations are recorded.

---

## Subagents Directory (`.pi/agents/`)

- **`researcher`**: Web researcher for gathering authoritative sources and verifying technical facts.
- **`mermaid-maker`**: Authors and validates Mermaid diagrams with minimal clutter (<= 7 nodes).
- **`svg-maker`**: Authors clean SVG diagrams for geometric/spatial representations.

---

## Skills Directory (`.pi/skills/`)

- **`teach`** ([`teach/SKILL.md`](.pi/skills/teach/SKILL.md))
- **`visualize`** ([`visualize/SKILL.md`](.pi/skills/visualize/SKILL.md))
- **`ask-user-question`** ([`ask-user-question/SKILL.md`](.pi/skills/ask-user-question/SKILL.md))
- **`quiz`** ([`quiz/SKILL.md`](.pi/skills/quiz/SKILL.md))
- **`md-log`** ([`md-log/SKILL.md`](.pi/skills/md-log/SKILL.md))
- **`visual-tools`** ([`visual-tools/SKILL.md`](.pi/skills/visual-tools/SKILL.md))
