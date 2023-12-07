# year 2023 day 7
import os

from hand import Hand, JokerHand

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.strip().split("\n")
    hands = []
    for line in data:
        hands.append((line.split(" ")[0], int(line.split(" ")[1])))
    return hands


def part_a(inp):
    hands = parse(inp)
    hands = [Hand(h[0], h[1]) for h in hands]
    hands.sort(key=lambda h: h.score)
    score = sum((i+1) * h.bid for i, h in enumerate(hands))
    return score


def part_b(inp):
    hands = parse(inp)
    hands = [JokerHand(h[0], h[1]) for h in hands]
    hands.sort(key=lambda h: h.score)
    score = sum((i+1) * h.bid for i, h in enumerate(hands))
    return score


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 6440)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 5905)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
