# year 2023 day 10
import os
from dataclasses import dataclass
from enum import Enum

CWD = os.path.dirname(os.path.abspath(__file__))

class Tile(Enum):
    NORTH_SOUTH = "|"
    EAST_WEST = "-"
    GROUND = "."
    NORTH_EAST = "L"
    NORTH_WEST = "J"
    SOUTH_EAST = "F"
    SOUTH_WEST = "7"
    START = "S"

    def neighbours(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        i, j = pos
        return {
            Tile.NORTH_SOUTH: [(i+1,j), (i-1,j)],
            Tile.EAST_WEST: [(i,j+1), (i,j-1)],
            Tile.NORTH_EAST: [(i,j+1), (i-1,j)],
            Tile.NORTH_WEST: [(i,j-1), (i-1,j)],
            Tile.SOUTH_EAST: [(i,j+1), (i+1,j)],
            Tile.SOUTH_WEST: [(i,j-1), (i+1,j)],
        }.get(self, [])

    @classmethod
    def SOUTH_TILES(cls) -> list["Tile"]:
        return [cls.NORTH_SOUTH, cls.SOUTH_EAST, cls.SOUTH_WEST]
    
    @classmethod
    def NORTH_TILES(cls) -> list["Tile"]:
        return [cls.NORTH_SOUTH, cls.NORTH_EAST, cls.NORTH_WEST]
    
    @classmethod
    def EAST_TILES(cls) -> list["Tile"]:
        return [cls.EAST_WEST, cls.SOUTH_EAST, cls.NORTH_EAST]
    
    @classmethod
    def WEST_TILES(cls) -> list["Tile"]:
        return [cls.EAST_WEST, cls.SOUTH_WEST, cls.NORTH_WEST]

class Field:
    def __init__(self, lines: list[str]):
        self.lines = [list(line) for line in lines]
        self.width = len(lines[0])
        self.height = len(lines)
        self.start = None
        for i,row in enumerate(lines):
            for j,cell in enumerate(row):
                if cell == Tile.START.value:
                    self.start = (i,j)
                    break
            if self.start is not None:
                break
        if self.start is None:
            raise Exception("Could not find start")
        self._update_start_tile()
    
    def _update_start_tile(self):
        start_tile_type = self._find_start_tile_type(self.start)
        start_i, start_j = self.start
        self.lines[start_i][start_j] = start_tile_type.value
    
    def _find_start_tile_type(self, pos: tuple[int, int]) -> Tile:
        possible = {t: True for t in Tile}
        possible[Tile.START] = False
        possible[Tile.GROUND] = False
        i,j = pos
        if i>0:
            if Tile(self.lines[i-1][j]) not in Tile.SOUTH_TILES():
                for t in Tile.NORTH_TILES():
                    possible[t] = False
        if i < self.height-1:
            if Tile(self.lines[i+1][j]) not in Tile.NORTH_TILES():
                for t in Tile.SOUTH_TILES():
                    possible[t] = False
        if j > 0:
            if Tile(self.lines[i][j-1]) not in Tile.EAST_TILES():
                for t in Tile.WEST_TILES():
                    possible[t] = False
        if j < self.width-1:
            if Tile(self.lines[i][j+1]) not in Tile.WEST_TILES():
                for t in Tile.EAST_TILES():
                    possible[t] = False
        if sum(possible.values()) != 1:
            raise Exception(f"Could not find start tile type: {possible}")
        for t in possible:
            if possible[t]:
                return t
    
    def neighbours(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        return Tile(self.lines[pos[0]][pos[1]]).neighbours(pos)

def parse(inp):
    data = inp.split("\n")
    return Field(data)


def part_a(inp):
    field = parse(inp)
    seen = set()
    count = 0
    queue = [field.start]
    while len(queue) > 1 or count == 0:
        new_queue = []
        count += 1
        for pos in queue:
            if pos in seen:
                continue
            seen.add(pos)
            new_queue.extend(field.neighbours(pos))
        queue = list(set(new_queue) - seen)
    return count


def part_b(inp):
    field = parse(inp)
    loop_tiles = set()
    queue = [field.start]
    while queue:
        new_queue = []
        for pos in queue:
            if pos in loop_tiles:
                continue
            loop_tiles.add(pos)
            new_queue.extend(field.neighbours(pos))
        queue = list(set(new_queue) - loop_tiles)
    row_scan_in_loop = set()
    for i, row in enumerate(field.lines):
        curr_in_loop = False
        edge_start_tile = None
        for j, cell in enumerate(row):
            curr_tile = Tile(cell)
            if (i,j) in loop_tiles:
                if curr_tile == Tile.NORTH_SOUTH:
                    curr_in_loop = not curr_in_loop
                    edge_start_tile = None
                elif curr_tile == Tile.SOUTH_EAST or curr_tile == Tile.NORTH_EAST:
                    edge_start_tile = curr_tile
                elif edge_start_tile:
                    if edge_start_tile == Tile.SOUTH_EAST and curr_tile == Tile.NORTH_WEST:
                        curr_in_loop = not curr_in_loop
                    elif edge_start_tile == Tile.NORTH_EAST and curr_tile == Tile.SOUTH_WEST:
                        curr_in_loop = not curr_in_loop
                    if curr_tile != Tile.EAST_WEST:
                        edge_start_tile = None
            if curr_in_loop:
                row_scan_in_loop.add((i,j))
    col_scan_in_loop = set()
    for j in range(field.width):
        curr_in_loop = False
        edge_start_tile = None
        for i in range(field.height):
            if (i,j) in loop_tiles:
                curr_tile = Tile(field.lines[i][j])
                if curr_tile == Tile.EAST_WEST:
                    curr_in_loop = not curr_in_loop
                    edge_start_tile = None
                elif curr_tile == Tile.SOUTH_EAST or curr_tile == Tile.SOUTH_WEST:
                    edge_start_tile = curr_tile
                elif edge_start_tile:
                    if edge_start_tile == Tile.SOUTH_EAST and curr_tile == Tile.NORTH_WEST:
                        curr_in_loop = not curr_in_loop
                    elif edge_start_tile == Tile.SOUTH_WEST and curr_tile == Tile.NORTH_EAST:
                        curr_in_loop = not curr_in_loop
                    if curr_tile != Tile.NORTH_SOUTH:
                        edge_start_tile = None
            if curr_in_loop:
                col_scan_in_loop.add((i,j))
    actual_in_loop = row_scan_in_loop & col_scan_in_loop
    actual_in_loop -= loop_tiles
    # for row in field.lines:
    #     print("".join(row))
    # to_print_sets = [
    #     row_scan_in_loop - loop_tiles,
    #     col_scan_in_loop - loop_tiles,
    #     actual_in_loop,
    # ]
    # for st in to_print_sets:
    #     print("=" * field.width)
    #     for i, row in enumerate(field.lines):
    #         for j, cell in enumerate(row):
    #             if (i,j) in st:
    #                 print("*", end="")
    #             elif (i,j) in loop_tiles:
    #                 print(cell, end="")
    #             else:
    #                 print(" ", end="")
    #         print()
    return len(actual_in_loop)


if __name__ == "__main__":
    with open(f"{CWD}/test_a.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 4)
    with open(f"{CWD}/test_b.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 4)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
