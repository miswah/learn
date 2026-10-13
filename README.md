# learn

[![video](assets/thumbnail.png)](https://www.youtube.com/watch?v=kzcI5F4tGiU)

My AI learning system from this video: [How I Use AI to Learn Things](https://www.youtube.com/watch?v=kzcI5F4tGiU).

This is a personal system I built for myself, shared as-is. Built as a pi configuration: the teaching philosophy encoded in a skill, a few small extensions, and agent definitions.

## What's in it

- `skills/teach/` — the philosophy and the process
- `skills/visualize/` — adds a correct, minimal diagram to a lesson when an idea is clearer as a picture
- `extensions/ask-user-question/` — the agent asks you questions through a UI popup
- `extensions/quiz/` — graded questions with instant feedback (✓/✗, correct answer, explanation)
- `extensions/md-log/` — link a markdown file to the session
- `extensions/visual-tools/` — tools for visualization subagents
- `agents/` — `researcher`, `svg-maker`, `mermaid-maker`: the subagents the system delegates to
- `setup.sh` — automated setup script to integrate the environment with Antigravity & Gemini CLI

## Install & Setup

This repo **is** a `.pi` directory. From your learning project's root:

```bash
git clone https://github.com/amosblomqvist/learn .pi
```

Then run the setup script to configure the workspace:

```bash
./.pi/setup.sh
```

### What `setup.sh` does

1. **Symlinks Root Instructions**: Links `AGENTS.md` and `GEMINI.md` from `.pi/` into the project root so AI agents load guidelines automatically.
2. **Configures `.agents` for Antigravity / Gemini CLI**:
   - Symlinks `.agents/skills` to `../.pi/skills`.
   - Symlinks `.agents/rules/agents.md` if available.
   - Generates `.agents/skills.json` to register the skills path.
3. **Initializes Study Log**: Creates `learn_log.md` with default headers if it doesn't already exist.
4. **Keeps Git Clean**: Adds `.pi`, `.agents`, `AGENTS.md`, `GEMINI.md`, `learn_log.md`, and `viz/` to `.git/info/exclude` (if a git repository exists), preventing learning artifacts from cluttering `git status` without altering `.gitignore`.

Then open pi (or your agent environment) in that directory. (Or copy the pieces you want into your existing project config.)

## Requirements

- [pi](https://github.com/earendil-works/pi)
- A subagent implementation, so the system can spawn the researcher and the visual makers. Recommended: [pi-interactive-subagents](https://github.com/amosblomqvist/pi-interactive-subagents) (tmux only). With it, everything works out of the box. Any other implementation works too, but expect to adapt the agent definitions, e.g. `agents/researcher.md` lists `safe_bash` in its tools, which is specific to that extension.
- `ask-user-question` — use the copy bundled here. If your setup already has an `ask-user-question` extension, use **this** one in its place. Popups from different extensions serialize through a shared UI lock, which only works when it's the same implementation.

## Notes

You can run the system without subagents. The main session does the teaching. You just lose the researcher (truth verification) and the generated visuals.

The teaching skill is written for one learner (me). Edit the skill to fit how you learn best.
