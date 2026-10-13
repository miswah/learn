---
name: quiz
description: Administer a graded diagnostic quiz question to assess understanding, bracket knowledge boundaries, or confirm that a concept has locked in. Use during the probe phase (1a) to map knowledge edges and during the teach phase (3) after establishing a node. Always includes an 'I don't know' option, evaluates answers, and reveals immediate feedback with an explanation.
---

# Quiz

A graded diagnostic assessment protocol designed to test understanding, locate knowledge boundaries, and confirm that learned concepts have locked in.

## Purpose & Scope

Use this skill whenever posing a question that **has a definite correct answer**:
- **Phase 1a (Probe)**: Map the learner's knowledge frontier along every thread the planned lesson depends on. Binary search difficulty to bracket the edge (find both the floor and the ceiling).
- **Phase 3 (Teach - Quiz-check)**: Confirm that a newly taught node (foundational unconditional truth or derived step) has actually landed before building anything on top of it.
- **Socratic discovery**: When prompting the learner to deduce a step themselves, if the deduction has a definite right answer, pose it as a `quiz`.

---

## 4 Construction Rules for Quiz Options

To make multiple-choice questions truly diagnostic and eliminate subconscious bias:

1. **Every option is a bare claim — no justification**:
   - The #1 giveaway is the correct option carrying its own explanation ("..., because it preserves X") while distractors are bare.
   - Put **zero** "why" in any option. All reasoning belongs in the post-answer `explanation`.
2. **Write the correct claim first, then mutate into distractors**:
   - Take the correct claim, then identify specific, common misconceptions.
   - State what someone holding each misconception would claim, using the *exact same* grammatical skeleton, length, and register as the correct claim.
3. **Tempting, not tricky**:
   - Each distractor must reflect a real error or confusion a learner might hold, yet be unambiguously wrong upon understanding.
4. **No asymmetric bolding or length cues**:
   - Never highlight or bold keywords in only the correct answer. Keep all options parallel.

---

## Non-Negotiable Protocols

### 1. Always Include "I don't know"
Every quiz must include `"I don't know"` as an explicit option:
- An honest `"I don't know"` is a genuine knowledge frontier, never a wrong guess.
- It prevents lucky guesses from inflating the learner's perceived knowledge level.
- When chosen, **never** flag with an error `✗` or mark as failure. Acknowledge the knowledge frontier, state the correct answer, and provide the explanation.

### 2. Never Leak the Answer in Advance
The correct answer and explanatory reasoning must **never** appear in the prompt, option text, or live question callout. Reveal them only after the user submits their answer.

### 3. Immediate Feedback Loop
Immediately upon receiving the learner's response:
- State the verdict clearly:
  - **Correct**: `✓ Correct!`
  - **Incorrect**: `✗ Incorrect.` (note the misconception held)
  - **Don't Know**: `· Knowledge gap identified (no guess made)`
- Show the correct answer.
- Deliver the full `explanation` reinforcing why the unconditional truth or derivation holds.

---

## Gemini Tool Workflow

Use Gemini's `ask_question` tool to administer the quiz:

```json
{
  "questions": [
    {
      "question": "What is true about the type annotation `X | Y` at runtime in Python 3.10+?",
      "options": [
        "It creates a runtime Union object that validates variable assignment",
        "It is a static type hint only; runtime values remain unchanged and unchecked",
        "It wraps the assigned value in a typing.Union container",
        "I don't know"
      ],
      "is_multi_select": false
    }
  ]
}
```

Once the user selects their answer, evaluate against the known correct answer and deliver immediate feedback and explanation in chat and log.

---

## Markdown Logging Format (`md-log` / `learn_log.md`)

Record the quiz in `learn_log.md` using Obsidian callout blocks:

### 1. Quiz Question Block
```markdown
> [!question] Quiz
> What is true about the type annotation `X | Y` at runtime in Python 3.10+?
>
> 1. It creates a runtime Union object that validates variable assignment
> 2. It is a static type hint only; runtime values remain unchanged and unchecked
> 3. It wraps the assigned value in a typing.Union container
> 4. I don't know
```

### 2. Quiz Result Blocks (choose matching outcome)

#### Outcome A: Correct
```markdown
> [!success] Quiz — correct ✓
> Your answer: 2. It is a static type hint only; runtime values remain unchanged and unchecked
> Correct answer: 2
>
> `X | Y` is purely a type hint (PEP 604) evaluated by static checkers like mypy or pyright. At runtime, Python performs zero validation and creates no union wrapper; values remain plain objects.
```

#### Outcome B: Incorrect
```markdown
> [!failure] Quiz — incorrect ✗
> Your answer: 1. It creates a runtime Union object that validates variable assignment
> Correct answer: 2. It is a static type hint only; runtime values remain unchanged and unchecked
>
> Python type annotations do not enforce types at runtime. To branch or validate based on runtime types, explicit `isinstance()` checks are required.
```

#### Outcome C: "I don't know"
```markdown
> [!question] Quiz — I don't know
> Your answer: I don't know
> Correct answer: 2. It is a static type hint only; runtime values remain unchanged and unchecked
>
> `X | Y` is purely a static type annotation (PEP 604). At runtime, Python does not enforce types or create wrapper objects.
```
