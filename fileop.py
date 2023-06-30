import re


def read_file(filename: str, lines: int) -> None:
    with open(filename, "rt") as file:
        for i in range(0, lines):
            print(file.readline(), end="")


def count_occurrence(filename: str, text: str) -> int:
    with open(filename, "rt") as file:
        data = file.read()
        matches = re.findall(text, data)
        print(f"The text or word occurs {len(matches)} times in the file.")
    return len(matches)


read_file("correlation.py", 20)

count_occurrence("correlation.py", "sum")
