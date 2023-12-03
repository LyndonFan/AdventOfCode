# year 2022 day 9
import os
from typing import Optional

CWD = os.path.dirname(os.path.abspath(__file__))


class Node:
    def __init__(self, x: int, y: int, child: Optional["Node"] = None):
        self.x = x
        self.y = y
        self.child = child

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def move(self, target_x, target_y):
        self.x = target_x
        self.y = target_y
        if self.child:
            self.child.update(self.x, self.y)

    def update(self, parent_x, parent_y):
        if abs(self.x - parent_x) <= 1 and abs(self.y - parent_y) <= 1:
            return
        if self.x == parent_x or self.y == parent_y:
            if self.x == parent_x:
                if self.y > parent_y:
                    self.y -= 1
                else:
                    self.y += 1
            if self.y == parent_y:
                if self.x > parent_x:
                    self.x -= 1
                else:
                    self.x += 1
        else:
            if self.x > parent_x:
                self.x -= 1
            else:
                self.x += 1
            if self.y > parent_y:
                self.y -= 1
            else:
                self.y += 1
        if self.child:
            self.child.update(self.x, self.y)


class Chain:
    def __init__(self, start_x: int, start_y: int, num_nodes: int):
        self.nodes = [Node(start_x, start_y) for _ in range(num_nodes)]
        for i in range(1, len(self.nodes)):
            self.nodes[i - 1].child = self.nodes[i]

    def __repr__(self):
        return " -> ".join([str(n) for n in self.nodes])

    @property
    def tail_pos(self) -> tuple[int, int]:
        return self.nodes[-1].x, self.nodes[-1].y

    def move(self, d: str):
        d_pos = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0),
        }[d]
        self.nodes[0].move(self.nodes[0].x + d_pos[0], self.nodes[0].y + d_pos[1])


def parse(inp):
    data = inp.strip().split("\n")
    data = [line.split(" ") for line in data]
    data = [(d, int(n)) for d, n in data]
    return data


def part_a(inp):
    data = parse(inp)
    chain = Chain(0, 0, 2)
    seen = set([(0, 0)])
    for d, n in data:
        for _ in range(n):
            chain.move(d)
            seen.add(chain.tail_pos)
    return len(seen)


def part_b(inp):
    data = parse(inp)
    chain = Chain(0, 0, 10)
    seen = set([(0, 0)])
    for d, n in data:
        for _ in range(n):
            chain.move(d)
            seen.add(chain.tail_pos)
    return len(seen)


if __name__ == "__main__":
    with open(f"{CWD}/test_a.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 13)
    with open(f"{CWD}/test_b.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 36)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
