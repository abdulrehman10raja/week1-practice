import os


def file_exists(path: str) -> bool:
    """Check whether a given file path exists."""
    return os.path.isfile(path)
