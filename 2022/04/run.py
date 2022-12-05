# year YEAR day 4


import os

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")

    def parse_line(line):
        rp, rq = line.split(",")
        ps, pt = map(int, rp.split("-"))
        qs, qt = map(int, rq.split("-"))
        return [(ps, pt), (qs, qt)]

    data = list(map(parse_line, data))

    return data


def part_a(inp):
    data = parse(inp)
    s = 0
    for (ps, pt), (qs, qt) in data:
        if ps <= qs and qt <= pt:
            s += 1
        elif qs <= ps and pt <= qt:
            s += 1
    return s


def part_b(inp):
    data = parse(inp)
    s = 0
    for (ps, pt), (qs, qt) in data:
        if ps <= qt and qs <= pt:
            s += 1
        elif qs <= pt and ps <= qt:
            s += 1
    return s


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 2)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 4)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
