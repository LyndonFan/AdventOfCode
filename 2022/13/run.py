# year 2022 day 13
import os
import json
from functools import cmp_to_key
from typing import Literal, TypeAlias, Union

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    return data

NestedList: TypeAlias = int | list["NestedList"]

def cmp_nested_list(a: NestedList, b: NestedList) -> Union[Literal[0], Literal[-1], Literal[1]]:
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return 0
        return -1 if a < b else 1
    if isinstance(a, int):
        a = [a]
    if isinstance(b, int):
        b = [b]
    for i in range(min(len(a), len(b))):
        c = cmp_nested_list(a[i], b[i])
        if c != 0:
            return c
    if len(a) == len(b):
        return 0
    return -1 if len(a) < len(b) else 1

def part_a(inp):
    data = parse(inp)
    pairs = [(a,b) for a,b in zip(data[::3], data[1::3])]
    s = 0
    for i, (a,b) in enumerate(pairs):
        a, b = json.loads(a), json.loads(b)
        cmp = cmp_nested_list(a, b)
        if cmp == -1:
            s += i+1
    return s

def part_b(inp):
    data = parse(inp)
    packs = [json.loads(x) for x in data if x]
    packs.append([2])
    packs.append([6])
    packs.sort(key=cmp_to_key(cmp_nested_list))
    return (packs.index([2])+1) * (packs.index([6])+1)


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 13)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "140")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
