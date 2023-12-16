# year 2023 day 15
import os
import re
from dataclasses import dataclass
from collections import namedtuple

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split(",")
    return data

def hash(input_string: str) -> int:
    val = 0
    for c in input_string:
        val += ord(c)
        val *= 17
        val %= 256
    return val

def part_a(inp):
    data = parse(inp)
    s = 0
    for inp in data:
        s += hash(inp)
    return s

Lens = namedtuple("Lens", ["label", "focal_length"])

def find_lens(box: list[Lens], label: str) -> int:
    for i, lens in enumerate(box):
        if lens.label == label:
            return i
    return -1

def part_b(inp):
    data = parse(inp)
    boxes: list[list[Lens]] = [[] for _ in range(256)]
    for line in data:
        if line.endswith("-"):
            label = line[:-1]
            box_number = hash(label)
            lens_index = find_lens(boxes[box_number], label)
            if lens_index == -1:
                continue
            boxes[box_number].pop(lens_index)
            continue
        label, focal_length_str = line.split("=")
        lens = Lens(label, int(focal_length_str))
        box_number = hash(label)
        lens_index = find_lens(boxes[box_number], label)
        if lens_index == -1:
            boxes[box_number].append(lens)
        else:
            boxes[box_number][lens_index] = lens
    s = 0
    for i, box in enumerate(boxes, 1):
        for j, lns in enumerate(box, 1):
            s += i * j * lns.focal_length
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 1320)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 145)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
