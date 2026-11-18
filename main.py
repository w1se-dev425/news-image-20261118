"""news-image-20261118 entry (Python 3.13, standard library only).

Writes one image summing up Wednesday 18 November 2026's world news to
/output/entry.png: a newspaper front page (masthead, hero illustration of
the day's lead story, four more stories and a briefs strip) composed from
that day's top stories. The program itself only copies the bundled image
`entry.png` (held in this repository) to the output path, so it is fully
deterministic: no randomness, no network, no clock reads; two runs write
identical bytes.
"""

import os
import shutil
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, OUTPUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
