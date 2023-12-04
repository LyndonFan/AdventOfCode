# year 2023 day 4
import os
import re
from dataclasses import dataclass
from typing import Union, Any

CWD = os.path.dirname(os.path.abspath(__file__))

CARD_ID_RE = re.compile("^Card +(\d+): ")

class Card:
    def __init__(self, line: str):
        self.card_id = re.search(CARD_ID_RE, line).group(1)
        numbers = line.split(":")[1].strip()
        winners, ours = numbers.split("|")
        self.winning_numbers = [
            int(x) for x in re.split("\ +", winners.strip()) if x
        ]
        self.our_numbers = [
            int(x) for x in re.split("\ +", ours.strip()) if x
        ]
        matches = set(self.our_numbers) & set(self.winning_numbers)
        self.num_matches = len(matches)
    
    @property
    def score(self) -> int:
        if self.num_matches == 0:
            return 0
        return 1 << (self.num_matches - 1)
        

def parse(inp):
    data = inp.split("\n")
    cards = [Card(row) for row in data if row]
    return cards


def part_a(inp):
    cards = parse(inp)
    return sum(c.score for c in cards)


def part_b(inp):
    cards = parse(inp)
    counts = [1] * len(cards)
    for i, card in enumerate(cards):
        # print(f"Card {card.card_id} has {card.num_matches} matches")
        for k in range(card.num_matches):
            counts[i+k+1] += counts[i]
    # print(counts)
    return sum(counts)


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 13)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 30)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
