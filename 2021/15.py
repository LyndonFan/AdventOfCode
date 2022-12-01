# day 15 solutions

"""
--- Day 15: Chiton ---You've almost reached the exit of the cave, but the walls are getting closer together. Your submarine can barely still fit, though; the main problem is that the walls of the cave are covered in chitons, and it would be best not to bump any of them.
The cavern is large, but has a very low ceiling, restricting your motion to two dimensions. The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout the cave (your puzzle input). For example:
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

You start in the top left position, your destination is the bottom right position, and you cannot move diagonally. The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels of each position you enter (that is, don't count the risk level of your starting position unless you enter it; leaving it adds no risk to your total).
Your goal is to find a path with the lowest total risk. In this example, a path with the lowest total risk is highlighted here:
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581

The total risk of this path is 40 (the starting position is never entered, so its risk is not counted).
What is the lowest total risk of any path from the top left to the bottom right?

"""
import numpy as np
from heapq import heappush, heappop, heapify


def q15a(inp):
    data = inp.split("\n")
    data = [[int(x) for x in y] for y in data]
    # use a* to find the shortest path
    # from top left to bottom right
    # use manhattan distance
    # use a min heap to find the next node with the least risk
    # return the total risk of the path

    # heap is (f(n), g(n), n)))
    seen = set()
    heap = [(len(data)+len(data[0]), 0, (0, 0))]
    heapify(heap)
    done = False
    cost = 0
    while not done:
        f, g, n = heappop(heap)
        if n == (len(data)-1, len(data[0])-1):
            cost = g
            done = True
        else:
            seen.add(n)
            # , (n[0]-1, n[1]), (n[0], n[1]-1)]:
            for x, y in [(n[0]+1, n[1]), (n[0], n[1]+1)]:
                if 0 <= x < len(data) and 0 <= y < len(data[0]) and (x, y) not in seen:
                    new_g = g + data[x][y]
                    new_f = new_g + len(data)+len(data[0]) - x - y
                    heappush(heap, (new_f, new_g, (x, y)))
    return cost


def q15b(inp):
    data = inp.split("\n")
    data = [[int(x) for x in y] for y in data]

    arr = np.array(data)
    arr_copy = arr.copy()
    for i in range(4):
        arr_copy = arr_copy+1
        arr_copy[arr_copy > 9] = 1
        arr = np.concatenate((arr, arr_copy), axis=0)
    arr_copy = arr.copy()
    for i in range(4):
        arr_copy = arr_copy+1
        arr_copy[arr_copy > 9] = 1
        arr = np.concatenate((arr, arr_copy), axis=1)

    data = arr.tolist()
    if len(data) < 100:
        print("\n".join(["".join(str(x) for x in y) for y in data]))
    else:
        print(len(data))

    # use dijsktra to find the shortest path
    # from top left to bottom right
    # use manhattan distance
    # use a min heap to find the next node with the least risk
    # return the total risk of the path

    seen = set()
    heap = [(0, (0, 0))]
    heapify(heap)
    done = False
    cost = 0
    while not done:
        d, n = heappop(heap)
        seen.add(n)
        if n == (len(data)-1, len(data[0])-1):
            cost = d
            done = True
        else:
            for x, y in [(n[0]+1, n[1]), (n[0], n[1]+1), (n[0]-1, n[1]), (n[0], n[1]-1)]:
                if 0 <= x < len(data) and 0 <= y < len(data[0]) and (x, y) not in seen:
                    heappush(heap, (d + data[x][y], (x, y)))
    return cost


if __name__ == "__main__":
    with open("15test.txt", "r") as f:
        data = f.read().strip()
    print("Testing  (a):", q15a(data))
    print("Expected (a):", 40)
    print("Testing  (b):", q15b(data))
    print("Expected (b):", 315)
    with open("15.txt", "r") as f:
        data = f.read().strip()
    print("Actual   (a):", q15a(data))
    print("Actual   (b):", q15b(data))
