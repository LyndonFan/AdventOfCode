# year 2023 day 12
import os
from math import factorial
from itertools import combinations
from tqdm import tqdm

CWD = os.path.dirname(os.path.abspath(__file__))

def parse(inp):
    lines = inp.split("\n")
    data = []
    for line in lines:
        row, numbers = line.split(" ")
        row = list(row)
        numbers = [int(x) for x in numbers.split(",")]
        data.append((row, numbers))
    return data

def nCr(n: int, r: int) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))

BRUTE_FORCE_THRESHOLD = 100000

EMPTY_CHAR = "."
FILL_CHAR = "#"
UNKNOWN_CHAR = "?"

def match_clues(row: list[str], clues: list[int]):
    if any(c == UNKNOWN_CHAR for c in row):
        return False
    if sum(c == FILL_CHAR for c in row) != sum(clues):
        return False
    row_index = 0
    clue_index = 0
    while row_index < len(row) and clue_index < len(clues):
        while row_index < len(row) and row[row_index] == EMPTY_CHAR:
            row_index += 1
        if row_index == len(row):
            return False
        start_fill = row_index
        while row_index < len(row) and row[row_index] == FILL_CHAR:
            row_index += 1
        if row_index - start_fill != clues[clue_index]: 
            return False
        clue_index += 1
        if row_index < len(row):
            row_index += 1
    return clue_index == len(clues)

def preprocess(current_row: list[str], clues: list[int]) -> list[str]:
    index = 0
    clue_index = 0
    filled_start_index = -1
    while index < len(current_row) and current_row[index] != UNKNOWN_CHAR:
        if current_row[index] == FILL_CHAR:
            if filled_start_index == -1:
                filled_start_index = index
        else:
            if filled_start_index != -1 and index - filled_start_index == clues[clue_index]:
                clue_index += 1
                filled_start_index = -1
        index += 1
    if index > 0:
        if filled_start_index != -1:
            index = filled_start_index
        concerned_row = [x for x in current_row[index:]]
        concerned_row = preprocess(concerned_row, clues[clue_index:])
        current_row = current_row[:index] + concerned_row
        return current_row
    
    index = len(current_row) - 1
    clue_index = len(clues) - 1
    filled_end_index = -1
    while index >= 0 and current_row[index] != UNKNOWN_CHAR:
        if current_row[index] == FILL_CHAR:
            if filled_end_index == -1:
                filled_end_index = index
        else:
            if filled_end_index != -1 and filled_end_index - index == clues[clue_index]:
                clue_index -= 1
                filled_end_index = -1
        index -= 1
    if index < len(current_row) - 1:
        if filled_end_index != -1:
            index = filled_end_index
        concerned_row = [x for x in current_row[:index+1]]
        concerned_row = preprocess(concerned_row, clues[:clue_index+1])
        current_row = concerned_row + current_row[index+1:]
        return current_row
    
    min_needed = sum(clues) + len(clues) - 1
    diff = len(current_row) - min_needed
    if diff < max(clues):
        min_strings = [
            UNKNOWN_CHAR * min(c, diff) + FILL_CHAR * max(0, c - diff)
            for c in clues
        ]
        min_string = UNKNOWN_CHAR.join(min_strings)
        for i, c in enumerate(min_string):
            if c == FILL_CHAR and current_row[i] == UNKNOWN_CHAR:
                current_row[i] = FILL_CHAR
        min_strings = [
            FILL_CHAR * max(0, c - diff) + UNKNOWN_CHAR * min(c, diff)
            for c in clues
        ]
        min_string = UNKNOWN_CHAR.join(min_strings)
        for i, c in enumerate(min_string):
            if c == FILL_CHAR and current_row[i-len(min_string)] == UNKNOWN_CHAR:
                current_row[i-len(min_string)] = FILL_CHAR
    if EMPTY_CHAR in current_row:
        first_empty = current_row.index(EMPTY_CHAR)
        if FILL_CHAR in current_row[:first_empty]:
            for i in range(first_empty - clues[0], clues[0]):
                if current_row[i] == UNKNOWN_CHAR:
                    current_row[i] = FILL_CHAR
        last_empty = -1
        while current_row[last_empty] != EMPTY_CHAR:
            last_empty -= 1
        if last_empty < -1 and FILL_CHAR in current_row[last_empty+1:]:
            for i in range(-clues[-1], last_empty + 1 + clues[-1]):
                if current_row[i] == UNKNOWN_CHAR:
                    current_row[i] = FILL_CHAR
    return current_row

cache = {}

def count_possible_solutions(
    current_row: list[str],
    clues: list[int]
) -> int:
    # row already satisfies the clue
    if sum(c == FILL_CHAR for c in current_row) == sum(clues):
        return 1
    if sum(c == FILL_CHAR for c in current_row) > sum(clues):
        return 0
    if sum(c != EMPTY_CHAR for c in current_row) < sum(clues):
        return 0
    # only way is to fill entire row
    if sum(clues) + len(clues) - 1 == len(current_row):
        return 1
    if sum(clues) + len(clues) - 1 > len(current_row):
        return 0
    key = ("".join(current_row), ",".join(map(str,clues)))
    if key in cache:
        return cache[key]
    
    # print("".join(current_row), clues)
    old_row = "".join(current_row)
    current_row = preprocess(current_row, clues)
    if "".join(current_row) != old_row:
        print(f"{','.join(map(str,clues))}\n{old_row}\n{''.join(current_row)}")
        ans = count_possible_solutions(current_row, clues)
        cache[key] = ans
        return ans
    
    n_groups = len(clues)
    n_flexible_empty = len(current_row) - sum(clues) - (n_groups - 1)
    if nCr(n_flexible_empty + n_groups - 1, n_groups - 1) <= BRUTE_FORCE_THRESHOLD:
        count = 0
        for tup in combinations(range(n_groups + n_flexible_empty), n_groups):
            test_row = [EMPTY_CHAR for _ in range(n_groups + n_flexible_empty)]
            for i, (idx, clue) in enumerate(zip(tup, clues)):
                test_row[idx] = FILL_CHAR * clue
                if i < n_groups - 1:
                    test_row[idx] += EMPTY_CHAR
            test_row = "".join(test_row)
            possible = all(
                expected == actual or actual == UNKNOWN_CHAR
                for expected, actual in zip(test_row, current_row)
            )
            count += possible
        cache[key] = count
        return count
    missing_fills = sum(clues) - sum(c == FILL_CHAR for c in current_row)
    if nCr(sum(c == UNKNOWN_CHAR for c in current_row), missing_fills) <= BRUTE_FORCE_THRESHOLD:
        count = 0
        unknown_indexes = [i for i, c in enumerate(current_row) if c == UNKNOWN_CHAR]
        for tup in combinations(unknown_indexes, missing_fills):
            test_row = [x for x in current_row]
            for i in tup:
                test_row[i] = FILL_CHAR
            for i in set(unknown_indexes) - set(tup):
                test_row[i] = EMPTY_CHAR
            possible = match_clues(test_row, clues)
            count += possible
        cache[key] = count
        return count
    return 0


def part_a(inp):
    data = parse(inp)
    res = 0
    for row, clue in tqdm(data):
        x = count_possible_solutions(row, clue)
        # print(f"{''.join(row)} {','.join(map(str, clue))} {x}")
        res += x
    return res 


def part_b(inp):
    data = parse(inp)
    res = 0
    computed = 0
    for row, clue in tqdm(data):
        x = count_possible_solutions(row*5, clue*5)
        # print(f"{''.join(row)} {','.join(map(str, clue))} {x}")
        res += x
        if x>0:
            computed += 1
    print(f"Computed {computed: 3}/{len(data)} solutions")
    return res 


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    # print("Testing  (a):", part_a(inp))
    # print("Expected (a):", 21)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 525152)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    # print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
