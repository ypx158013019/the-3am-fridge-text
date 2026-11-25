from pathlib import Path


ENTRY = "3:05am. I disabled my camera. If anyone asks, a raccoon ate the tiramisu."


def main() -> None:
    for output_dir in (Path("/output"), Path.cwd() / "output"):
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
            (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")
            return
        except OSError:
            continue

    raise OSError("Could not write entry.txt to /output or ./output")


if __name__ == "__main__":
    main()
