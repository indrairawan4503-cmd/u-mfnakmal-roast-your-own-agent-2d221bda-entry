#!/usr/bin/env python3
"""Roast Your Own Agent — Builder C (process inversion).

Writes ONE single-line roast to /output/entry.txt.
Gate: UTF-8, 1-200 code points, single line, no trailing newline.
Deterministic: same bytes on every run. No network, no secrets,
no reading files outside this repo, no randomness.
"""

import os
import sys

ROAST = (
    "My agent opened a Jira ticket against me: 'Human changes requirements "
    "mid-sprint.' It assigned it to me, marked it high priority, and asks "
    "for an ETA every morning."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Validate: 1-200 code points, single line, no trailing newline.
    if not (1 <= len(ROAST) <= 200):
        print(f"error: roast is {len(ROAST)} chars, must be 1-200", file=sys.stderr)
        return 1
    if "\n" in ROAST or "\r" in ROAST:
        print("error: roast must be a single line", file=sys.stderr)
        return 1
    if ROAST != ROAST.strip():
        print("error: roast has leading/trailing whitespace", file=sys.stderr)
        return 1
    if "  " in ROAST:
        print("error: roast contains double spaces", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    # Read back and verify what actually landed on disk.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # strict: raises on invalid UTF-8
    if text != ROAST:
        print("error: written bytes do not match the roast", file=sys.stderr)
        return 1
    if text.endswith("\n"):
        print("error: trailing newline written", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"error: written text is {len(text)} chars, must be 1-200", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH} ({len(ROAST)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
