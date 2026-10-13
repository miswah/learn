#!/usr/bin/env python3
"""
log_entry.py — Append formatted Obsidian callout blocks to learn_log.md
Faithfully matches the md-log format from .pi/extensions/md-log.ts.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional


def append_to_file(filepath: Path, block: str) -> None:
    current = ""
    if filepath.exists():
        current = filepath.read_text(encoding="utf-8")
    
    prefix = "\n\n" if current.strip() else ""
    new_content = current + prefix + block.strip() + "\n"
    filepath.write_text(new_content, encoding="utf-8")


def format_callout(callout_type: str, title: str, body_lines: List[str]) -> str:
    lines = [f"> [!{callout_type}] {title}"]
    for line in body_lines:
        lines.append(">" if not line.strip() else f"> {line}")
    return "\n".join(lines)


def format_user_block(text: str) -> str:
    return f"> [!quote] YOU\n\n{text.strip()}"


def format_assistant_block(text: str, name: str = "PI") -> str:
    return f"> [!abstract] {name}\n\n{text.strip()}"


def format_question_block(label: str, question: str, options: Optional[List[str]] = None, context: Optional[str] = None) -> str:
    body: List[str] = []
    for line in question.strip().splitlines():
        body.append(line)
    if context and context.strip():
        body.append("")
        for line in context.strip().splitlines():
            body.append(line)
    if options:
        body.append("")
        for i, opt in enumerate(options, 1):
            body.append(f"{i}. {opt}")
    return format_callout("question", label, body)


def format_answer_block(answer: str) -> str:
    return format_callout("example", "Answer", [answer.strip()])


def format_quiz_result_block(
    status: str,
    user_answer: str,
    correct_answer: str,
    explanation: Optional[str] = None,
    note: Optional[str] = None,
) -> str:
    status_lower = status.lower()
    if status_lower in ("dont_know", "dontknow", "unknown"):
        callout_type = "question"
        title = "Quiz — I don't know"
        body = ["Your answer: I don't know", f"Correct answer: {correct_answer}"]
    elif status_lower in ("correct", "success", "true"):
        callout_type = "success"
        title = "Quiz — correct ✓"
        body = [f"Your answer: {user_answer}", f"Correct answer: {correct_answer}"]
    else:
        callout_type = "failure"
        title = "Quiz — incorrect ✗"
        body = [f"Your answer: {user_answer}", f"Correct answer: {correct_answer}"]

    if note and note.strip():
        body.append("")
        body.append(f"Note: {note.strip()}")

    if explanation and explanation.strip():
        body.append("")
        for line in explanation.strip().splitlines():
            body.append(line)

    return format_callout(callout_type, title, body)


def main():
    parser = argparse.ArgumentParser(description="Append formatted entries to a study log file.")
    parser.add_argument("--file", "-f", default="learn_log.md", help="Target markdown file (default: learn_log.md)")
    
    subparsers = parser.add_subparsers(dest="command", required=True)

    # user
    p_user = subparsers.add_parser("user", help="Append a user quote block")
    p_user.add_argument("content", help="User message content")

    # assistant
    p_assistant = subparsers.add_parser("assistant", help="Append an assistant response block")
    p_assistant.add_argument("content", help="Assistant message content")
    p_assistant.add_argument("--name", default="PI", help="Speaker name (PI, GEMINI, etc.)")

    # question (ask-user-question)
    p_q = subparsers.add_parser("question", help="Append a directional question block")
    p_q.add_argument("question", help="The question text")
    p_q.add_argument("--option", "-o", action="append", default=[], help="Answer option (repeatable)")
    p_q.add_argument("--context", "-c", help="Optional context")

    # answer
    p_a = subparsers.add_parser("answer", help="Append an answer block to a directional question")
    p_a.add_argument("answer", help="Selected answer")

    # quiz-question
    p_qq = subparsers.add_parser("quiz-question", help="Append a quiz question block")
    p_qq.add_argument("question", help="The quiz question text")
    p_qq.add_argument("--option", "-o", action="append", default=[], help="Answer option (repeatable)")
    p_qq.add_argument("--context", "-c", help="Optional context")

    # quiz-result
    p_qr = subparsers.add_parser("quiz-result", help="Append a quiz evaluation result block")
    p_qr.add_argument("--status", choices=["correct", "incorrect", "dont_know"], required=True)
    p_qr.add_argument("--user-answer", required=True, help="User's selected option")
    p_qr.add_argument("--correct-answer", required=True, help="Correct option")
    p_qr.add_argument("--explanation", help="Explanation for the question")
    p_qr.add_argument("--note", help="Optional user note")

    # raw
    p_raw = subparsers.add_parser("raw", help="Append raw markdown block")
    p_raw.add_argument("content", help="Markdown content")

    args = parser.parse_args()
    target_path = Path(args.file)

    if args.command == "user":
        block = format_user_block(args.content)
    elif args.command == "assistant":
        block = format_assistant_block(args.content, name=args.name)
    elif args.command == "question":
        block = format_question_block("Question", args.question, args.option, args.context)
    elif args.command == "answer":
        block = format_answer_block(args.answer)
    elif args.command == "quiz-question":
        block = format_question_block("Quiz", args.question, args.option, args.context)
    elif args.command == "quiz-result":
        block = format_quiz_result_block(
            status=args.status,
            user_answer=args.user_answer,
            correct_answer=args.correct_answer,
            explanation=args.explanation,
            note=args.note,
        )
    elif args.command == "raw":
        block = args.content
    else:
        sys.exit(1)

    append_to_file(target_path, block)
    print(f"Logged entry to {target_path}")


if __name__ == "__main__":
    main()
