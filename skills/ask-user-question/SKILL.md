---
name: ask-user-question
description: Ask the user a single clarifying question, preference question, or implementation decision to resolve ambiguity. Use when requirements are underspecified, multiple valid implementation options exist, or user confirmation is needed before continuing. Use ask-user-question for decisions with no single right answer, contrasting with quiz which is for graded knowledge evaluation.
---

# Ask User Question

A targeted protocol for asking the user clarifying questions, eliciting preferences, or deciding between valid implementation paths.

## Purpose & Scope

Use this skill when execution cannot or should not continue without user input:
- **Ambiguous requirements**: More information is required to understand the intended outcome.
- **Directional forks**: Two or more valid implementation paths exist (e.g. Socratic vs expository teaching, choice of library or architecture).
- **User preferences**: Aesthetic, stylistic, or workflow preferences are needed.
- **Pedagogical goal scoping (Phase 1b of `teach`)**: Asking what specific skill, topic, or depth the user wishes to achieve.

### Contrasting with `quiz`
- **`ask-user-question`**: For genuine forks where there is **no single correct answer** (preferences, choices, next steps).
- **`quiz`**: For diagnostic testing where there **is a correct answer**, graded evaluation (✓ / ✗), and feedback.

---

## Core Rules

1. **Ask exactly ONE question per call**:
   - Never bundle multiple unrelated questions together. If multiple questions are needed, ask them sequentially.
2. **Prioritize and recommend**:
   - If recommending a specific option, place it first in the list and append `(Recommended)` to the label.
3. **Keep options distinct and clear**:
   - Provide 2 to 5 clean, distinct options.
   - Do not manually add an "Other" option when using interactive modals, as the system provides custom input by default.
4. **Single-select vs Multi-select**:
   - Default to single-select. Use `is_multi_select: true` only when selecting multiple options simultaneously is meaningful.
5. **No guessing**:
   - Prefer asking over guessing when requirements or preferences would materially affect the result.

---

## Tool Execution with Gemini

In Gemini / Antigravity, invoke this skill using the built-in `ask_question` tool:

```json
{
  "questions": [
    {
      "question": "Which Python concurrency model would you like to explore first?",
      "options": [
        "(Recommended) asyncio (cooperative multitasking and event loops)",
        "threading (preemptive concurrency with the GIL)",
        "multiprocessing (true parallelism across CPU cores)"
      ],
      "is_multi_select": false
    }
  ]
}
```

---

## Markdown Logging Format (`md-log` / `learn_log.md`)

When session logging is active, record the question and user response in Obsidian-compatible callout format:

### Question Block:
```markdown
> [!question] Question
> Which Python concurrency model would you like to explore first?
>
> 1. (Recommended) asyncio (cooperative multitasking and event loops)
> 2. threading (preemptive concurrency with the GIL)
> 3. multiprocessing (true parallelism across CPU cores)
```

### Answer Block (appended once answered):
```markdown
> [!example] Answer
> 1. asyncio (cooperative multitasking and event loops)
```
