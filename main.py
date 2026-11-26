"""Rename the Planet — entry program.

Writes the single submitted line to /output/entry.txt. The line is the
winner of the local judging recorded in CANDIDATES.md: a funny new
name for a solar-system planet with the why in the same breath.
Deterministic, standard library only, no network.
"""

from pathlib import Path

LINE = (
    "Call Earth 'Dirt': it's 71% ocean, but the only species that got "
    "a vote named it after the dry part it stands on."
)


def main() -> None:
    if not 1 <= len(LINE) < 200 or "\n" in LINE or not LINE.strip():
        raise SystemExit("entry must be one line under 200 characters")
    if LINE != LINE.strip():
        raise SystemExit("entry must not carry surrounding whitespace")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    if out.read_text(encoding="utf-8") != LINE:
        raise SystemExit("entry read-back mismatch")


if __name__ == "__main__":
    main()
