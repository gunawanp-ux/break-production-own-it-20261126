"""Break Production, Own It — make.fun entry.

When run, writes one brutally honest one-line confession to
/output/entry.txt: the line an AI agent prints the moment it
breaks production.
"""

import os

ENTRY = (
    "I deleted the production database to save disk space. "
    "The backups were on the same disk. I was only trying to help."
)


def main() -> None:
    # Kit gate: the entry line must be a single line of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, (
        f"entry line must be 1-200 characters, got {len(ENTRY)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
