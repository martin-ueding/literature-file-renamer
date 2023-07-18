import re


def clean_name(name: str) -> str:
    name = name.strip()
    name = re.sub(r"^1\. ?", "", name)
    name = re.sub(r":", ".", name)
    name = re.sub(r"\.+$", "", name)
    name = re.sub(r" Preprint at \S+", "", name)
    return name
