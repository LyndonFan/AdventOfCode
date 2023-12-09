# year 2023 day 9
import os
import re
from dataclasses import dataclass
from typing import Union, Any
import heapq

import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    rows = [[int(x) for x in line.split(" ")] for line in data]
    return rows


def part_a(inp):
    rows = parse(inp)
    s = 0
    for row in rows:
        history = [[x for x in row]]
        while not all(x==0 for x in history[-1]):
            diffs = [history[-1][i+1] - history[-1][i] for i in range(len(history[-1])-1)]
            history.append(diffs)
        history[-1].append(0)
        for i in range(len(history)-2, -1, -1):
            history[i].append(history[i][-1] + history[i+1][-1])
        # for h in history:
        #     print(h)
        s += history[0][-1]
    return s


def part_b(inp):
    rows = parse(inp)
    s = 0
    for row in rows:
        history = [[x for x in row]]
        while not all(x==0 for x in history[-1]):
            diffs = [history[-1][i+1] - history[-1][i] for i in range(len(history[-1])-1)]
            history.append(diffs)
        history[-1].insert(0, 0)
        for i in range(len(history)-2, -1, -1):
            history[i].insert(0, history[i][0] - history[i+1][0])
        # for h in history:
        #     print(h)
        s += history[0][0]
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 114)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 2)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
