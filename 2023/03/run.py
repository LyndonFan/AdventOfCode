# year 2023 day 3
import os
import re
from dataclasses import dataclass
from typing import Union, Any
import heapq

import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    return data


def part_a(inp):
    data = parse(inp)
    s = 0
    for i, row in enumerate(data):
        j = 0
        while j < len(row):
            if row[j] not in "1234567890":
                j += 1
                continue
            start_index = j
            end_index = j+1
            while end_index < len(row) and row[end_index] in "1234567890":
                end_index += 1
            # print(i, j, row[start_index:end_index])
            touch_symbol = False
            if i > 0:
                for k in range(max(0, start_index-1), min(end_index+1, len(row))):
                    if data[i-1][k] not in "1234567890.":
                        touch_symbol = True
                        # print("touch at", i-1, k)
                        break
            if i < len(data)-1:
                for k in range(max(0, start_index-1), min(end_index+1, len(row))):
                    if data[i+1][k] not in "1234567890.":
                        touch_symbol = True
                        # print("touch at", i+1, k)
                        break
            if j > 0 and row[start_index-1] not in "1234567890.":
                touch_symbol = True
                # print("touch at", i, j-1)
            if end_index < len(row) and row[end_index] not in "1234567890.":
                touch_symbol = True
                # print("touch at", i, end_index)
            if touch_symbol:
                s += int(row[start_index:end_index])
            j = end_index+1
    return s


def part_b(inp):
    data = parse(inp)
    gears = {}
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == "*":
                gears[(i,j)] = []
    for i, row in enumerate(data):
        j = 0
        while j < len(row):
            if row[j] not in "1234567890":
                j += 1
                continue
            start_index = j
            end_index = j+1
            while end_index < len(row) and row[end_index] in "1234567890":
                end_index += 1
            number = int(row[start_index:end_index])
            if i > 0:
                for k in range(max(0, start_index-1), min(end_index+1, len(row))):
                    if (i-1, k) in gears:
                        gears[(i-1, k)].append(number)
            if i < len(data)-1:
                for k in range(max(0, start_index-1), min(end_index+1, len(row))):
                    if (i+1, k) in gears:
                        gears[(i+1, k)].append(number)
            if (i, j-1) in gears:
                gears[(i, j-1)].append(number)
            if (i, end_index) in gears:
                gears[(i, end_index)].append(number)
            j = end_index+1
    s = 0
    for vs in gears.values():
        if len(vs) == 2:
            s += vs[0] * vs[1]
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 4361)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 467835)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
