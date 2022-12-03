# year 2022 day 2

"""
--- Day 2: Rock Paper Scissors ---The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack storage, a giant Rock Paper Scissors tournament is already in progress.
Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round, the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then, a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw.
Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.
The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.
For example, suppose you were given the following strategy guide:
A Y
B X
C Z

This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
What would your total score be if everything goes exactly according to your strategy guide?

"""


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
    import os

    CWD = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(CWD, "test.txt"), "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", "15")
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "12")
    with open(os.path.join(CWD, "input.txt"), "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
