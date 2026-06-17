import json
import csv


def read_text_file(path: str) -> str:
    """Read a text file and return its contents as a string."""
    with open(path, "r") as f:
        return f.read()


def read_json_file(path: str) -> dict:
    """Read a JSON file and return its contents as a dictionary."""
    with open(path, "r") as f:
        return json.load(f)


def write_json_file(path: str, data: dict) -> None:
    """Write a dictionary to a file as JSON."""
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def read_csv_file(path: str) -> list:
    """Read a CSV file and return its rows as a list of dictionaries."""
    with open(path, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        return list(reader)
