import argparse
import pathlib

from .names import clean_name


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    rename_parser = subparsers.add_parser("rename")
    rename_parser.set_defaults(func=main_rename)
    rename_parser.add_argument("paths", nargs="+", metavar="path", type=pathlib.Path)
    rename_parser.add_argument("--dry", action="store_true")

    organize_parser = subparsers.add_parser("organize")
    organize_parser.set_defaults(func=main_organize)
    organize_parser.add_argument("path", type=pathlib.Path)

    options = parser.parse_args()
    options.func(options)


def main_rename(options: argparse.Namespace) -> None:
    for path in options.paths:
        new_stem = clean_name(path.stem)
        if new_stem != path.stem:
            new_path = path.with_stem(new_stem)
            print(f"Renaming `{path.stem.strip()}` to `{new_stem}`.")
            if not options.dry:
                path.rename(new_path)


def organize_path(root: pathlib.Path, path: pathlib.Path) -> None:
    if path.is_dir():
        for subpath in path.iterdir():
            organize_path(root, subpath)
    elif path.is_file():
        new_stem = clean_name(path.stem)
        first_letter = new_stem[0].upper()
        new_path = root / first_letter / f"{new_stem}{path.suffix}"
        if path != new_path:
            print(f"Moving `{path}` to `{new_path}`.")
            new_path.parent.mkdir(exist_ok=True)
            path.rename(new_path)
    else:
        raise RuntimeError("Only directories and files are supported.")


def main_organize(options: argparse.Namespace) -> None:
    root: pathlib.Path = options.path
    assert root.is_dir(), r"Root {root} needs to be a directory."
    organize_path(root, root)


if __name__ == "__main__":
    main()
