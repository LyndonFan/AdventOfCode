# year 2022 day 9
import os

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.strip().split("\n")
    data = [line.split(" ") for line in data]
    data = [(d, int(n)) for d, n in data]
    return data


def update(newhpos, tpos):
    nhx, nhy = newhpos
    tx, ty = tpos
    if max(abs(nhx - tx), abs(nhy - ty)) <= 1:
        return tpos
    if nhx - tx >= 2:
        tx += 1
        ty = nhy
    elif tx - nhx >= 2:
        tx -= 1
        ty = nhy
    elif nhy - ty >= 2:
        ty += 1
        tx = nhx
    elif ty - nhy >= 2:
        ty -= 1
        tx = nhx
    return (tx, ty)


def move(d, pos):
    x, y = pos
    if d == "R":
        x += 1
    elif d == "L":
        x -= 1
    elif d == "U":
        y += 1
    elif d == "D":
        y -= 1
    return (x, y)


def simulate(d, hpos, tpos):
    hx, hy = hpos
    tx, ty = tpos
    if d == "R":
        hx += 1
        if hx - tx >= 2:
            tx += 1
            ty = hy
    elif d == "L":
        hx -= 1
        if tx - hx >= 2:
            tx -= 1
            ty = hy
    elif d == "U":
        hy += 1
        if hy - ty >= 2:
            ty += 1
            tx = hx
    elif d == "D":
        hy -= 1
        if ty - hy >= 2:
            ty -= 1
            tx = hx
    return (hx, hy), (tx, ty)


def part_a(inp):
    data = parse(inp)
    hpos = (0, 0)
    tpos = (0, 0)
    seen = set([(0, 0)])
    for d, n in data:
        for _ in range(n):
            hpos, tpos = simulate(d, hpos, tpos)
            seen.add(tpos)
    return len(seen)


def part_b(inp):
    data = parse(inp)
    poss = [(0, 0) for _ in range(10)]
    seen = set([(0, 0)])
    for d, n in data:
        for _ in range(n):
            nposs = []
            pos = move(d, poss[0])
            nposs.append(pos)
            for lpos in poss[1:]:
                pos = update(pos, lpos)
                nposs.append(pos)
            poss = nposs
            seen.add(poss[-1])
    return len(seen)


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    # print("Testing  (a):", part_a(inp))
    # print("Expected (a):", 13)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 36)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    # print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
