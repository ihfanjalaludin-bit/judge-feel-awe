"""Write a short relaxing text to entry.txt.

The program is deterministic: it always writes the same text, using
only the Python standard library and no network access. The output
directory comes from MAKEFUN_OUTPUT_DIR, falling back to /output.
The directory itself is never removed.
"""

import os

TEXT = (
    "Below the harbour, where the light thins to green, a whale moves "
    "through cold water, unhurried. A hundred years on the same slow "
    "road, older than the harbour. The wind comes and goes above. It "
    "keeps no count of days. The sea carries it, and nothing asks it "
    "to be anywhere else."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
