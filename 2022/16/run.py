# year 2022 day 16
import os
import re
from dataclasses import dataclass
from typing import List

CWD = os.path.dirname(os.path.abspath(__file__))

line_pat = re.compile(
    r"Valve ([A-Z]+) has flow rate=([0-9]+); tunnels lead to valves (([A-Z]+)(, [A-Z]+)*)"
)


@dataclass
class Valve:
    name: str
    flow_rate: int
    neighbours: List[str]
    open: bool = False


def parse(inp):
    data = inp.split("\n")
    for 
    return data


def part_a(inp):
    data = parse(inp)
    return 0


def part_b(inp):
    data = parse(inp)
    return 0


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 1651)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "B_RESPONSE")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
