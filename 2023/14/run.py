# year 2023 day 14
import os
from tqdm import tqdm
CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.strip().split("\n")
    data = [list(line) for line in data]
    return data

ROUND_ROCK = "O"
CUBE_ROCK = "#"
EMPTY_SPACE = "."

cache = {}

def roll_to_right(line: list[str]) -> list[str]:
    key = "".join(line)
    if key in cache:
        return list(cache[key])
    prev_stop = -1
    num_rocks = 0
    n = len(line)
    for i in range(n):
        if line[i] != CUBE_ROCK:
            num_rocks += line[i] == ROUND_ROCK
            continue
        for d in range(num_rocks):
            line[i-1-d] = ROUND_ROCK
        for h in range(i-1-num_rocks, prev_stop, -1):
            line[h] = EMPTY_SPACE
        prev_stop = i
        num_rocks = 0
    for d in range(num_rocks):
        line[n-1-d] = ROUND_ROCK
    for h in range(n-1-num_rocks, prev_stop, -1):
        line[h] = EMPTY_SPACE
    cache[key] = "".join(line)
    return line
        

def load_on_north_beams(lines: list[list[str]]) -> int:
    n = len(lines)
    s = 0
    for i, row in enumerate(lines):
        s += row.count(ROUND_ROCK) * (n-i)
    return s

def part_a(inp):
    data = parse(inp)
    n = len(data)
    # len(data[0]) == n # input is square
    # for line in data:
    #     print("".join(line))
    # print("=" * n)
    for i in range(n):
        line = [data[j][i] for j in range(n-1, -1, -1)]
        line = roll_to_right(line)
        for j in range(n):
            data[n-1-j][i] = line[j]
    # for line in data:
    #     print("".join(line))
    load = load_on_north_beams(data)
    return load


def part_b(inp):
    data = parse(inp)
    NUM_CYCLES = 1000000000
    n = len(data)
    load_values = []
    for cycle in tqdm(range(NUM_CYCLES)):
        start_state = "\n".join("".join(line) for line in data)
        # roll to north
        for i in range(n):
            line = [data[j][i] for j in range(n-1, -1, -1)]
            line = roll_to_right(line)
            for j in range(n):
                data[n-1-j][i] = line[j]
        # roll to west
        for i in range(n):
            line = data[i][::-1]
            line = roll_to_right(line)
            data[i] = line[::-1]
        # roll to south
        for i in range(n):
            line = [data[j][i] for j in range(n)]
            line = roll_to_right(line)
            for j in range(n):
                data[j][i] = line[j]
        # roll to east
        for i in range(n):
            line = data[i]
            line = roll_to_right(line)
            data[i] = line
        if start_state == "\n".join("".join(line) for line in data):
            break
        load = load_on_north_beams(data)
        load_values.append(load)
        if cycle == 0 or cycle%1000 != 0:
            continue
        for cycle_length in range(1, len(load_values)//100):
            is_cycle = True
            offset = cycle_length * 100
            for cycle_num in range(100):
                for cycle_index in range(cycle_length):
                    if load_values[cycle_num*cycle_length+cycle_index-offset] != load_values[cycle_index-cycle_length]:
                        is_cycle = False
                        break
                if not is_cycle:
                    break
            if is_cycle:
                cycle_values = load_values[-cycle_length:]
                num_repeat = 1 + (NUM_CYCLES - len(load_values)) // cycle_length
                load_values += cycle_values * num_repeat
    return load_values[NUM_CYCLES-1]


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 136)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 64)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
