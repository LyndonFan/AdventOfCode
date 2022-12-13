# year 2022 day 8
import os
import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.strip().split("\n")
    data = [[int(c) for c in l] for l in data]
    data = np.array(data)
    return data


def part_a(inp):
    data = parse(inp)
    count = 0
    nrows, ncols = data.shape
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            ck = False
            ck |= i == 0 or v > max(data[:i, j])
            ck |= i + 1 == nrows or v > max(data[i + 1 :, j])
            ck |= j == 0 or v > max(data[i, :j])
            ck |= j + 1 == ncols or v > max(data[i, j + 1 :])
            count += ck
    return count


def inbound(i: int, j: int, nrows: int, ncols: int) -> bool:
    return i >= 0 and j >= 0 and i < nrows and j < ncols


def part_b(inp, debug=False):
    data = parse(inp)
    maxscore = 0
    ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    nrows, ncols = data.shape
    scores = []
    for i, row in enumerate(data):
        scores.append([])
        for j, v in enumerate(row):
            if i == 0 or i == nrows - 1 or j == 0 or j == ncols - 1:
                scores[-1].append(0)
                continue
            score = 1
            if debug:
                print(f"{(i,j)=}", end=" ")
            for dy, dx in ds:
                y, x = i + dy, j + dx
                c = 1
                while inbound(y, x, nrows, ncols) and data[y, x] < data[i, j]:
                    c += 1
                    y += dy
                    x += dx
                if not inbound(y, x, nrows, ncols):
                    c -= 1
                if debug:
                    print(f"{(dy,dx)=}->{c=}", end=" ")
                score *= max(c, 0)
            if debug:
                print(f"{score=}")
            scores[-1].append(score)
            maxscore = max(score, maxscore)
    if debug:
        print("\n".join("".join(map(" {:2} ".format, row)) for row in scores))
    return maxscore


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 21)
    print("Testing  (b):", part_b(inp, True))
    print("Expected (b):", 8)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
