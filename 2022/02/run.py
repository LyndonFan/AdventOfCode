# year 2022 day 2
import os

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    data = [x.split(" ") for x in data]
    return data


# key is (opp, you)
# value is 1 for your win, 0 for tie, -1 for opp win
play = {
    ("R", "R"): 0,
    ("R", "P"): 1,
    ("R", "S"): -1,
    ("P", "R"): -1,
    ("P", "P"): 0,
    ("P", "S"): 1,
    ("S", "R"): 1,
    ("S", "P"): -1,
    ("S", "S"): 0,
}
score = {"R": 1, "P": 2, "S": 3}


def part_a(inp):
    data = parse(inp)
    opp_map = {"A": "R", "B": "P", "C": "S"}
    you_map = {"X": "R", "Y": "P", "Z": "S"}

    def play_points(opp: str, you: str) -> int:
        opp = opp_map[opp]
        you = you_map[you]
        return score[you] + 3 * (1 + play[(opp, you)])

    s = 0
    for o, y in data:
        s += play_points(o, y)

    return s


def part_b(inp):
    data = parse(inp)
    opp_map = {"A": "R", "B": "P", "C": "S"}
    code_map = {"X": -1, "Y": 0, "Z": 1}
    you_map = {}
    for c in "XYZ":
        you_map[c] = {o: y for o in "RPS" for y in "RPS" if play[(o, y)] == code_map[c]}
    print(you_map)

    def play_points(opp: str, you: str) -> int:
        opp = opp_map[opp]
        you = you_map[you][opp]
        return score[you] + 3 * (1 + play[(opp, you)])

    s = 0
    for o, y in data:
        s += play_points(o, y)

    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", "15")
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "12")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
