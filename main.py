"""Worst app idea ever pitched: QueueBuddy.

Writes one sentence (<= 240 characters) to /output/entry.txt.
Python 3.13, standard library only.
"""

import os
import unicodedata

ENTRY = (
    "QueueBuddy is a premium subscription app that reserves your place in "
    "queues you are already standing in, charging $4.99 a month to hold "
    "the spot directly behind you for a customer who will never arrive."
)


def validate(text):
    """Return True only if text is a valid one-sentence pitch."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= 240:
        return False
    if "\n" in text or "\r" in text:
        return False
    if not text.strip():
        return False
    if text != text.strip():
        return False
    if any(unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp") for ch in text):
        return False
    return True


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    if not validate(ENTRY):
        raise ValueError("ENTRY failed validation")
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
