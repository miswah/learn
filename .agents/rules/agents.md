# Subagent Capabilities and Delegation Rules

When operating in this workspace, the agent has access to specialized agent definitions in `.pi/agents/`:

## Available Subagents

1. **`researcher`** (`.pi/agents/researcher.md`):
   - Role: Targeted web research and verification.
   - Purpose: Stop and verify any foundational axioms, claims, or technical specs before teaching to prevent errors or hallucinations.

2. **`mermaid-maker`** (`.pi/agents/mermaid-maker.md`):
   - Role: Authoring and validating Mermaid diagrams.
   - Purpose: Generates clean DAGs and relationship charts with minimal clutter (<= 7 nodes).

3. **`svg-maker`** (`.pi/agents/svg-maker.md`):
   - Role: Authoring clean SVG diagrams for geometric/spatial representations.
   - Purpose: Handles coordinate axes, geometry figures, and spatial diagrams.

When subagent tasks arise, invoke the subagents using `invoke_subagent` or `define_subagent` configured with these specifications.
