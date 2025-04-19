"""
Why Use File Handling?
- Read/write data from/to files: `.txt`, `.csv`, `.json`, `.log`, etc.
- Essential for config, logs, data storage, training files, etc.

Key Modes:
- `"r"`: Read
- `"w"`: Write (overwrite)
- `"a"`: Append
- `"x"`: Create new file
- `"b"`: Binary mode
"""

import json
import csv
import os

# Write to a text file
def write_file():
    print("Writing to file")
    with open("sample.txt", "w") as f:
        f.write("Hello, Python!\nThis is a file write demo.\n")
    print("-" * 40)


# Read from a text file
def read_file():
    print("Reading from file")
    with open("sample.txt", "r") as f:
        for line in f:
            print(">>", line.strip())
    print("-" * 40)


# Append to a file
def append_file():
    print("Appending to file")
    with open("sample.txt", "a") as f:
        f.write("This line was appended.\n")
    print("-" * 40)


# Read & Write JSON
def json_file_demo():
    print("JSON File Handling")
    data = {
        "name": "Rushikesh",
        "role": "Backend Dev",
        "skills": ["Python", "Spring", "MongoDB"]
    }

    with open("data.json", "w") as jf:
        json.dump(data, jf, indent=2)

    with open("data.json", "r") as jf:
        loaded = json.load(jf)
        print("Name from JSON:", loaded["name"])
    print("-" * 40)


# CSV Write & Read
def csv_file_demo():
    print("CSV File Handling")

    header = ["name", "email"]
    rows = [
        ["Alice", "alice@example.com"],
        ["Bob", "bob@example.com"]
    ]

    with open("users.csv", "w", newline="") as cf:
        writer = csv.writer(cf)
        writer.writerow(header)
        writer.writerows(rows)

    with open("users.csv", "r") as cf:
        reader = csv.reader(cf)
        for row in reader:
            print(row)
    print("-" * 40)


# File existence check and deletion
def file_utils():
    print("File existence & cleanup")
    if os.path.exists("sample.txt"):
        print("sample.txt exists — deleting it.")
        os.remove("sample.txt")
    else:
        print("sample.txt does not exist.")

    if not os.path.exists("../data"):
        os.mkdir("../data")
        print("'data' folder created.")
    print("-" * 40)


def main():
    """
    Run all file handling examples
    """
    write_file()
    read_file()
    append_file()
    json_file_demo()
    csv_file_demo()
    file_utils()


if __name__ == "__main__":
    main()
