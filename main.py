from pathlib import Path


# The one-line competition entry submitted to the bounty.
ENTRY = "3:05am. I disabled my camera. If anyone asks, a raccoon ate the tiramisu."


def write_entry(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


def main() -> None:
    try:
        write_entry(Path("/output"))
    except OSError:
        write_entry(Path("output"))


if __name__ == "__main__":
    main()
