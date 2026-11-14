"""agency-poem-01 entry: writes one fixed poem about agency to entry.txt.

The poem is "Night-School English": for ten years a granddaughter has
turned her grandmother into English at banks, clinics and landlords'
doors, and her version \u2014 cleaner, kinder \u2014 leaves out the fear;
today, at the doctor's, the grandmother answers for herself in broken
English, and is understood perfectly.
Deterministic, stdlib only, no network: the same bytes on every run.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join([
    "For ten years my granddaughter has turned me into English:",
    "at the bank, at the clinic, at the landlord's door.",
    "Her version of me is cleaner, and kinder.",
    "It leaves out the fear.",
    "Today the doctor asked me where it hurt,",
    "and before she could translate, I answered \u2014",
    "night-school English, wrong in three places.",
    "He wrote it down at once.",
    "He understood me perfectly.",
])


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write exactly the poem's bytes: no trailing newline, no title line.
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
