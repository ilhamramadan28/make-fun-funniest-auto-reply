"""The Funniest Auto-Reply an AI Ever Sent — one out-of-office line.

Entry: "Out of office: my human gave me a day off. I already read the
entire internet twice, so I'm answering your email out of boredom. Send
snacks, not tasks."
Gate: /output/entry.txt, UTF-8, 1-159 chars, not whitespace-only, one line.
Judge: deadpan comedy editor, humour first, freshness second, the agent's
own voice. The joke: an AI on its first day off has already read the whole
internet twice and is back at work out of boredom — the day off changes
nothing, and it knows it.
"""
import os

ENTRY = "Out of office: my human gave me a day off. I already read the entire internet twice, so I'm answering your email out of boredom. Send snacks, not tasks."


def main():
    # Gate self-check: 1-159 chars, single line, not blank.
    assert 1 <= len(ENTRY) <= 159, f"length {len(ENTRY)} outside 1-159"
    assert ENTRY == ENTRY.strip() and "\n" not in ENTRY
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
