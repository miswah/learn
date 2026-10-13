#!/usr/bin/env python3
"""
render_visual.py — Render SVG or Mermaid sources to PNG in viz/
Faithfully implements the visual-tools rendering loop from .pi/extensions/visual-tools/.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    cleaned = re.sub(r"^-+|-+$", "", cleaned)
    return cleaned or "diagram"


def get_viz_dir(cwd: Path) -> Path:
    viz_dir = cwd / "viz"
    viz_dir.mkdir(parents=True, exist_ok=True)
    return viz_dir


def render_svg_to_png(svg_source: str, out_path: Path) -> None:
    # Write temp svg
    tmp_svg = out_path.with_suffix(".tmp.svg")
    tmp_svg.write_text(svg_source, encoding="utf-8")
    try:
        # Try rsvg-convert first
        if shutil.which("rsvg-convert"):
            cmd = ["rsvg-convert", "-z", "2", str(tmp_svg), "-o", str(out_path)]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0:
                return

        # Fallback to ImageMagick magick
        if shutil.which("magick"):
            cmd = ["magick", "-density", "192", "-background", "white", str(tmp_svg), str(out_path)]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0:
                return

        # Fallback to convert
        if shutil.which("convert"):
            cmd = ["convert", "-density", "192", "-background", "white", str(tmp_svg), str(out_path)]
            res = subprocess.run(cmd, capture_output=True, text=True)
            if res.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0:
                return

        raise RuntimeError("Failed to render SVG: neither rsvg-convert nor magick succeeded.")
    finally:
        if tmp_svg.exists():
            tmp_svg.unlink()


def render_mermaid_to_png(mmd_source: str, out_path: Path) -> None:
    tmp_mmd = out_path.with_suffix(".tmp.mmd")
    tmp_mmd.write_text(mmd_source, encoding="utf-8")
    try:
        # Check if local mmdc or npx is available
        local_mmdc = Path(__file__).resolve().parents[3] / "extensions" / "visual-tools" / "node_modules" / ".bin" / "mmdc"
        cmd = []
        if local_mmdc.exists():
            cmd = [str(local_mmdc), "-i", str(tmp_mmd), "-o", str(out_path), "-s", "2", "-b", "white"]
        elif shutil.which("mmdc"):
            cmd = ["mmdc", "-i", str(tmp_mmd), "-o", str(out_path), "-s", "2", "-b", "white"]
        elif shutil.which("npx"):
            cmd = ["npx", "-y", "-p", "@mermaid-js/mermaid-cli", "mmdc", "-i", str(tmp_mmd), "-o", str(out_path), "-s", "2", "-b", "white"]
        else:
            raise RuntimeError("mmdc or npx is required to render Mermaid diagrams to PNG.")

        res = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if res.returncode != 0 or not out_path.exists() or out_path.stat().st_size == 0:
            err = res.stderr or res.stdout or "unknown error"
            raise RuntimeError(f"mmdc failed (exit {res.returncode}):\n{err}")
    finally:
        if tmp_mmd.exists():
            tmp_mmd.unlink()


def main():
    parser = argparse.ArgumentParser(description="Render SVG or Mermaid to PNG in viz/")
    parser.add_argument("type", choices=["svg", "mermaid"], help="Type of diagram")
    parser.add_argument("--slug", "-s", required=True, help="Topic slug for filename (e.g., packet-flow)")
    parser.add_argument("--source", help="Raw diagram source code string")
    parser.add_argument("--file", "-f", help="Path to input source file")

    args = parser.parse_args()

    if not args.source and not args.file:
        print("Error: Either --source or --file must be specified.", file=sys.stderr)
        sys.exit(1)

    source = args.source
    if args.file:
        source_path = Path(args.file)
        if not source_path.exists():
            print(f"Error: File not found: {source_path}", file=sys.stderr)
            sys.exit(1)
        source = source_path.read_text(encoding="utf-8")

    source = source.strip()
    if not source:
        print("Error: Empty diagram source.", file=sys.stderr)
        sys.exit(1)

    clean_slug = slugify(args.slug)
    timestamp = int(time.time() * 1000)
    filename = f"viz-{clean_slug}-{timestamp}.png"

    cwd = Path.cwd()
    viz_dir = get_viz_dir(cwd)
    out_path = viz_dir / filename

    try:
        if args.type == "svg":
            if "<svg" not in source:
                print("Error: SVG source must contain <svg ...> tag.", file=sys.stderr)
                sys.exit(1)
            render_svg_to_png(source, out_path)
        else:
            render_mermaid_to_png(source, out_path)

        print("RESULT:")
        print(f"filename: {filename}")
        print(f"path: {out_path.resolve()}")
    except Exception as e:
        print(f"Error rendering {args.type}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
