import json
from utils.file_handler import read_text_file, write_json_file, read_json_file
from utils.validators import file_exists

write_json_file("sample.json", {"name": "Abdul", "week": 1})

if file_exists("sample.json"):
    data = read_json_file("sample.json")
    print(data)

from utils.file_handler import read_csv_file

rows = read_csv_file("sample.csv")
print(rows)

from utils.file_handler import read_text_file

try:
    content = read_text_file("does_not_exist.txt")
    print(content)
except FileNotFoundError:
    print(
        "Error: could not find 'does_not_exist.txt'. Check that the file path is correct."
    )

try:
    data = read_json_file("broken.json")
    print(data)
except FileNotFoundError:
    print("Error: the JSON file was not found.")
except json.JSONDecodeError:
    print("Error: the file exists but is not valid JSON.")
