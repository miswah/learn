---
name: md-log
description: Mirror and append teaching sessions, dialogues, lessons, and Q&A blocks to a designated markdown log file (e.g., learn_log.md) for clean reading and persistence in Obsidian or markdown viewers. Formats entries using Obsidian/GitHub callouts and LaTeX math notation.
---

# Markdown Log (md-log)

Mirrors reading-relevant lesson content, user queries, dialogues, and Q&A blocks into a designated markdown file (`learn_log.md` by default) for reading rendered notes in Obsidian or any markdown viewer.

## Purpose & Scope

Terminal sessions are transient and difficult to read for extended study. A rendered `.md` file provides:
- Live rendering of math via native LaTeX (`$inline$` and `$$display$$`).
- Syntax-highlighted code blocks.
- Native rendering of Mermaid diagrams.
- Clean visual hierarchy with collapsible GitHub/Obsidian callout blocks.
- Inline visual image embeds (`![[viz-slug-timestamp.png|500]]` or markdown links).

### What Gets Logged:
1. **User prompts**: Questions, requests, and goals.
2. **Assistant lessons**: Explanations, derivations, motivated discovery prose, summaries.
3. **Q&A blocks**: Interactive questions, quizzes, selections, and graded feedback.
4. **Visual diagrams**: Mermaid charts and published images from `viz/`.

### What Is Omitted:
- Internal tool calls, command executions (bash, search, file read/edit traces). Keep the study log free of implementation noise.

---

## Callout Standards

All blocks are formatted using Obsidian and GitHub Flavored Markdown callout syntax:

### 1. User Prompts
```markdown
> [!quote] YOU
>
> What is the difference between Python's asyncio and Java threads?
```

### 2. Assistant Lesson Prose
```markdown
> [!abstract] PI
>
> In Java, threading is preemptive and OS-managed. In Python, `asyncio` is cooperative and runs on a single-threaded event loop...
```

### 3. Directional Questions & Answers (`ask-user-question`)
```markdown
> [!question] Question
> What would you like to cover next?
>
> 1. Try practice exercises with asyncio
> 2. Deep-dive into event loop mechanics

> [!example] Answer
> 1. Try practice exercises with asyncio
```

### 4. Quiz Questions & Graded Results (`quiz`)

#### Question Block:
```markdown
> [!question] Quiz
> What does `int | str` mean in Python 3.10+?
>
> 1. Runtime validates that the value is an int or str
> 2. A static type hint indicating the value can be either int or str
> 3. I don't know
```

#### Result Block: Correct
```markdown
> [!success] Quiz — correct ✓
> Your answer: 2. A static type hint indicating the value can be either int or str
> Correct answer: 2
>
> `X | Y` is purely a type hint (PEP 604) for static checkers. Runtime values remain unchanged and unchecked.
```

#### Result Block: Incorrect
```markdown
> [!failure] Quiz — incorrect ✗
> Your answer: 1. Runtime validates that the value is an int or str
> Correct answer: 2. A static type hint indicating the value can be either int or str
>
> Type annotations do not perform runtime validation in Python. Runtime logic requires explicit `isinstance()` checks.
```

#### Result Block: "I don't know"
```markdown
> [!question] Quiz — I don't know
> Your answer: I don't know
> Correct answer: 2. A static type hint indicating the value can be either int or str
>
> `X | Y` is evaluated only by static type checkers. Runtime values remain plain objects.
```

---

## Logging Helper Script

To ensure atomic writes and perfect callout formatting, run the companion script:
`scripts/log_entry.py` (relative to this skill directory).

### Usage Examples:

```bash
# Log a user message
python3 .pi/skills/md-log/scripts/log_entry.py --file learn_log.md user "How does GIL affect threading?"

# Log an assistant explanation
python3 .pi/skills/md-log/scripts/log_entry.py --file learn_log.md assistant "The Global Interpreter Lock ensures only one thread executes Python bytecode at a time."

# Log a directional question
python3 .pi/skills/md-log/scripts/log_entry.py --file learn_log.md question "Which topic next?" \
  -o "Asyncio event loops" -o "Multiprocessing"

# Log an answer
python3 .pi/skills/md-log/scripts/log_entry.py --file learn_log.md answer "Asyncio event loops"

# Log a quiz question
python3 .pi/skills/md-log/scripts/log_entry.py --file learn_log.md quiz-question "What does str | None mean?" \
  -o "Intersection of str and None" -o "Equivalent to Optional[str]" -o "I don't know"

# Log a quiz result
python3 .pi/skills/md-log/scripts/log_entry.py --file learn_log.md quiz-result \
  --status correct \
  --user-answer "2. Equivalent to Optional[str]" \
  --correct-answer "2" \
  --explanation "In Python 3.10+, X | None is the idiomatic syntax for Optional[X]."
```
