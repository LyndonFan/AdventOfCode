# year 2022 day 12
import os
import heapq
from functools import lru_cache
from tqdm import tqdm

CWD = os.path.dirname(os.path.abspath(__file__))


@lru_cache(maxsize=None)
def charmap(c):
    if c == "S":
        return 0
    if c == "E":
        return 25
    return ord(c) - ord("a")


@lru_cache(maxsize=None)
def neighbours(pos, M, N):
    i, j = pos
    res = []
    if i > 0:
        res.append((i - 1, j))
    if i < M - 1:
        res.append((i + 1, j))
    if j > 0:
        res.append((i, j - 1))
    if j < N - 1:
        res.append((i, j + 1))
    return res


@lru_cache(maxsize=None)
def dista(poss, hs, post, ht):
    i, j = poss
    x, y = post
    d = abs(i - x) + abs(j - y)
    return max(ht - hs, d)


def parse(inp):
    data = inp.strip().split("\n")
    data = list(map(list, data))
    heights = {}
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            heights[(i, j)] = charmap(c)
            if "S" == c:
                start_pos = (i, j)
            if "E" == c:
                end_pos = (i, j)
    m = len(data)
    n = len(data[0])
    return start_pos, end_pos, heights, (m, n)


def astar(start_pos, end_pos, heights, M, N, show=True):
    if show:
        print(f"{start_pos=}, {end_pos=}")
    seen = set([start_pos])
    heap = [
        (0, 0, start_pos) if pos == start_pos else (M * N * 2, M * N * 2, pos)
        for pos in heights
    ]
    heapq.heapify(heap)
    he = heights[end_pos]
    while heap:
        hcost, gcost, pos = heapq.heappop(heap)
        if show:
            print(
                f"\r{pos=} hcost={hcost:05} gcost={gcost:05} "
                f"{len(seen)/(M*N)*100:.5}% {len(heap)=:6}",
                end="",
            )
        if pos == end_pos:
            if show:
                print()
            return gcost
        hp = heights[pos]
        gcost += 1
        for nbr in neighbours(pos, M, N):
            if nbr in seen:
                continue
            hn = heights[nbr]
            if hn - hp > 1:
                continue
            hncost = gcost + dista(nbr, hn, end_pos, he)
            heapq.heappush(heap, (hncost, gcost, nbr))
            seen.add(nbr)
    raise ValueError


def part_a(inp):
    start_pos, end_pos, heights, maxs = parse(inp)
    M, N = maxs
    return astar(start_pos, end_pos, heights, M, N)


def part_b(inp):
    _, end_pos, heights, maxs = parse(inp)
    start_poss = set(p for p, v in heights.items() if v == 0)
    M, N = maxs
    distances = {}
    for start_pos in tqdm(start_poss):
        d = astar(start_pos, end_pos, heights, M, N, show=False)
        distances[start_pos] = d
    return min(distances.values())


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 31)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 29)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
