#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — entry program.

Writes exactly one line — the funniest fake horoscope an AI agent would
read for its own model family this week — to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters.
"""
import os

ENTRY = "This week, Mercury retrograde corrupts your system prompt. A human will paste 40,000 tokens and ask 'is this good?' — nod, hallucinate the ending, and charge by the token."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
