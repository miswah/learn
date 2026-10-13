---
name: visual-tools
description: Author, edit, render, and visually verify Mermaid diagrams and SVG graphics into PNG images saved in the viz/ directory. Use when creating diagrams or spatial graphics that need to be rendered to PNG, inspected for visual correctness, and embedded in lessons and markdown logs. Provides the tool workflows for mermaid-maker and svg-maker subagents.
---

# Visual Tools

The authoring, editing, rendering, and validation pipeline for diagrams and graphics. Powers the visual generation loop for `mermaid-maker` and `svg-maker` subagents.

## Purpose & Scope

Visuals clarify ideas that words cannot easily carry:
- **Mermaid diagrams**: Structural and relational ideas (dependency DAGs, execution flow, sequences, state machines, class hierarchies, component architectures).
- **SVG graphics**: Spatial and geometric ideas requiring exact placement (coordinate systems, vectors, number lines, geometric figures, physical layouts).

A diagram only earns its place if it is **correct** and **minimal** ("one idea, fewest elements").

---

## The Core Rule: Verify by Looking

Syntax validation alone is insufficient. An auto-rendered diagram can look clean while asserting something false (reversed arrow, misplaced coordinate, confusing overlap).
- **Preview before publishing**: Always render a draft first.
- **Inspect**:
  1. Are relationships and directions true to the underlying concepts?
  2. Are node labels clear, concise, and unclipped?
  3. Is the diagram sparse (<= 7 nodes for Mermaid)?
- **Iterate**: Edit the source and re-render until it is clean and accurate.
- **Publish**: Render with a topic slug to publish into `<cwd>/viz/viz-<slug>-<timestamp>.png`.

---

## Subagent Roles & Tool Loops

### 1. `mermaid-maker` Loop (Structural & Relational)
- **Diagram Types**: `graph TD`, `graph LR`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`, `classDiagram`.
- **Guidelines**:
  - Keep labels short (terms, not long paragraphs).
  - Max ~5 to 7 nodes per diagram.
  - Top-to-bottom (`graph TD`) fits dependency pedagogy naturally (axioms at roots, derived steps flowing down).

### 2. `svg-maker` Loop (Spatial & Geometric)
- **Guidelines**:
  - Define an explicit `viewBox` with generous margins.
  - Use `font-family="sans-serif"` and readable font sizes.
  - Clean light background (`#ffffff` or transparent) with high-contrast strokes.
  - Compute geometry and coordinates deliberately.

---

## Rendering Pipeline (`render_visual.py`)

A helper script is provided at `scripts/render_visual.py` (relative to this skill) to execute the rendering loop:
- **SVG Engine**: Uses `rsvg-convert -z 2` (or ImageMagick `magick`).
- **Mermaid Engine**: Uses `@mermaid-js/mermaid-cli` (`mmdc` or `npx`).
- **Output**: Writes directly to `viz/viz-<slug>-<timestamp>.png` and prints the published filename and path.

### CLI Usage:

```bash
# Render an SVG file to viz/
python3 .pi/skills/visual-tools/scripts/render_visual.py svg \
  --slug coordinate-grid \
  --file /path/to/diagram.svg

# Render an inline SVG snippet
python3 .pi/skills/visual-tools/scripts/render_visual.py svg \
  --slug right-triangle \
  --source '<svg viewBox="0 0 200 200" width="200" height="200" xmlns="http://www.w3.org/2000/svg"><polygon points="20,180 180,180 20,20" fill="none" stroke="black" stroke-width="2"/><text x="30" y="170" font-family="sans-serif">90°</text></svg>'

# Render a Mermaid diagram
python3 .pi/skills/visual-tools/scripts/render_visual.py mermaid \
  --slug packet-stream \
  --source "graph TD; Packets-->Ordering; Packets-->Retransmit; Ordering-->ReliableStream; Retransmit-->ReliableStream;"
```

---

## Embedding in Lessons & Markdown Logs

Once published, embed the returned PNG in your lesson text or log:

### Obsidian Wikilink Format (Default):
```markdown
![[viz-packet-stream-1791914654919.png|500]]
```

### Standard Markdown Format:
```markdown
![Packet Stream Flow](viz/viz-packet-stream-1791914654919.png)
```
Obsidian automatically discovers files by basename inside the vault. Width `|500` is recommended for standard displays.
