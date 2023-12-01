# year 2023 day 1
import os
import re

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    return data


def part_a(inp):
    data = parse(inp)
    s = 0
    for line in data:
        line = re.sub("[^0-9]", "", line)
        s += int(line[0] + line[-1])
    return s

replacements = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def part_b(inp):
    data = parse(inp)
    s = 0
    for line in data:
        first_digit = None
        for i in range(len(line)):
            if re.match("[0-9]", line[i]):
                first_digit = line[i]
                break
            for key, value in replacements.items():
                if line[i:i+len(key)] == key:
                    first_digit = value
                    break
            if first_digit:
                break
        last_digit = None
        for i in range(len(line)-1, -1, -1):
            if re.match("[0-9]", line[i]):
                last_digit = line[i]
                break
            for key, value in replacements.items():
                if line[i:i+len(key)] == key:
                    last_digit = value
                    break
            if last_digit:
                break
        s += int(first_digit + last_digit)
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    # print("Testing  (a):", part_a(inp))
    # print("Expected (a):", 142)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "281")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
