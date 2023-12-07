# year 2023 day 6
import os
import re
from math import ceil, floor

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    return data


def part_a(inp):
    lines = parse(inp)
    times = re.split(" +", lines[0].split(":")[1].strip())
    distances = re.split(" +", lines[1].split(":")[1].strip())
    data = [(int(t), int(d)) for t,d in zip(times, distances)]
    # given (t,d), we want
    # x * (t-x) = hold_time * speed = distance_travelled > d
    # 0 > x^2 - tx + d
    # root = -(t +/- sqrt(t^2 - 4d))/2
    # x \in ((t-sqrt(t^2-4d))/2, (t+sqrt(t^2-4d))/2)
    prod = 1
    for t,d in data:
        det = (t*t - 4*d)**0.5
        lower_bound = ceil((t-det)/2)
        if (t-det)/2 == lower_bound:
            lower_bound += 1
        upper_bound = floor((t+det)/2)
        if (t+det)/2 == upper_bound:
            upper_bound -= 1
        prod *= upper_bound - lower_bound + 1
    return prod


def part_b(inp):
    lines = parse(inp)
    t = int(lines[0].split(":")[1].replace(" ",""))
    d = int(lines[1].split(":")[1].replace(" ",""))
    det = (t*t - 4*d)**0.5
    lower_bound = ceil((t-det)/2)
    if (t-det)/2 == lower_bound:
        lower_bound += 1
    upper_bound = floor((t+det)/2)
    if (t+det)/2 == upper_bound:
        upper_bound -= 1
    return upper_bound - lower_bound + 1


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 288)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 71503)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
