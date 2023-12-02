# year 2023 day 2
import os
import re
from dataclasses import dataclass
from typing import Union, Any, NamedTuple, Iterable
import heapq

import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    return data

Draw = NamedTuple("Draw", [("red", int), ("green", int), ("blue", int)])

@dataclass
class Game:
    game_id: int
    draws: list[Draw]

def parse_draw(results: str) -> Draw:
    counts = {c: 0 for c in "red green blue".split()}
    for res in re.findall("\d+ (?:red|blue|green)", results):
        n, color = res.split(" ")
        counts[color] = int(n)
    return Draw(**counts)

def parse_game(line: str) -> Game:
    game_id = re.search("^Game (\d+): ", line).group(1)
    draw_results = re.findall("((?:\d+ (?:red|blue|green)(?:, )?){1,3})", line)
    draws = [parse_draw(res) for res in draw_results]
    game = Game(int(game_id), draws)
    return game

def part_a(inp):
    data = parse(inp)
    MAX_COUNTS = {"red": 12, "green": 13, "blue": 14}
    s = 0
    for line in data:
        game = parse_game(line)
        possible = True
        for draw in game.draws:
            for color, count in draw._asdict().items():
                if count > MAX_COUNTS[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            s += game.game_id
    return s


def part_b(inp):
    data = parse(inp)
    s = 0
    for line in data:
        game = parse_game(line)
        min_possible = {"red": 0, "green": 0, "blue": 0}
        for draw in game.draws:
            for color, count in draw._asdict().items():
                if count > min_possible[color]:
                    min_possible[color] = count
        s += min_possible["red"] * min_possible["green"] * min_possible["blue"]
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 8)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 2286)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
