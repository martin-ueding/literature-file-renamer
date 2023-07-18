import argparse
import pathlib

from .names import clean_name


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", metavar="path", type=pathlib.Path)
    parser.add_argument("--dry", action="store_true")
    options = parser.parse_args()

    for path in options.paths:
        new_stem = clean_name(path.stem)
        if new_stem != path.stem:
            new_path = path.with_stem(new_stem)
            print(f"Renaming `{path.stem.strip()}` to `{new_stem}`.")
            if not options.dry:
                path.rename(new_path)


if __name__ == "__main__":
    main()
