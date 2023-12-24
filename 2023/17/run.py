# year 2023 day 17
import os
import re
import heapq
from typing import Callable
from collections import namedtuple


CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    data = inp.split("\n")
    rows = [[int(x) for x in line] for line in data]
    return rows

Node = namedtuple("Node", [
    "f_score",
    "current_heat",
    "consecutive_straights",
    "position",
    "direction",
    "parent_position",
    "parent_direction",
])

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
turn_left = {
    UP: LEFT,
    LEFT: DOWN,
    DOWN: RIGHT,
    RIGHT: UP
}
turn_right = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP
}
direction_index = {
    UP: 0,
    RIGHT: 1,
    DOWN: 2,
    LEFT: 3,
}

def create_heuristic(goal: tuple[int, int]) -> Callable[tuple[int, int], int]:
    def heuristic(position: tuple[int, int]) -> int:
        return abs(position[0] - goal[0]) + abs(position[1] - goal[1])
    return heuristic


def min_heat(data: list[list[int]], max_straight_before_turn: int = 3) -> int:
    m = len(data)
    n = len(data[0])
    h = create_heuristic((m - 1, n - 1))
    seen_positions: set[tuple[tuple[int, int], int]] = set()
    parents: dict[tuple[tuple[int, int], int], tuple[tuple[int, int], int]] = {}
    heap = [
        Node(h((0, 0)), 0, 0, (0, 0), d, (0, 0), d)
        for d in [DOWN, RIGHT]
    ]
    while heap:
        current = heapq.heappop(heap)
        print(f"pos={current.position} heat={current.current_heat}", end="\r")
        if current.position == (m - 1, n - 1):
            path = []
            curr_key = (current.position, direction_index[current.direction])
            print()
            breakpoint()
            while curr_key[0] != (0, 0):
                print(f"{curr_key=}", end="\r")
                path.append(curr_key)
                curr_key = parents[curr_key]
            return current.current_heat, path
        if (current.position, direction_index[current.direction]) in seen_positions:
            continue
        if current.position[0] < 0 or current.position[0] >= m or current.position[1] < 0 or current.position[1] >= n:
            continue
        seen_positions.add((current.position, direction_index[current.direction]))
        parents[(current.position, direction_index[current.direction])] = (current.parent_position, direction_index[current.parent_direction])
        new_directions = [
            turn_left[current.direction],
            turn_right[current.direction],
            current.direction
        ]
        for new_dir in new_directions:
            if new_dir == current.direction and current.consecutive_straights >= max_straight_before_turn:
                continue
            new_pos = (current.position[0] + new_dir[0], current.position[1] + new_dir[1])
            if new_pos[0] >= 0 and new_pos[0] < m and new_pos[1] >= 0 and new_pos[1] < n:
                new_heat = current.current_heat + data[new_pos[0]][new_pos[1]]
                new_node = Node(
                    new_heat + h(new_pos),
                    new_heat,
                    current.consecutive_straights + 1 if new_dir == current.direction else 0,
                    new_pos,
                    new_dir,
                    current.position,
                    current.direction
                )
                parents[(new_node.position, direction_index[new_node.direction])] = (current.position, direction_index[current.direction])
                heapq.heappush(heap, new_node)
    return -1


def part_a(inp):
    data = parse(inp)
    res, path = min_heat(data, 3)
    breakpoint()
    return res


def part_b(inp):
    data = parse(inp)
    return 0


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 102)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "B_RESPONSE")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
