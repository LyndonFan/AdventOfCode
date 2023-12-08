# year 2023 day 8
import os
import re
from dataclasses import dataclass
from typing import Union, Any
import heapq

import numpy as np

CWD = os.path.dirname(os.path.abspath(__file__))

class Network:
    def __init__(self, lines: list[tuple[str, str, str]]):
        self.network = {
            node: [left, right]
            for node, left, right in lines
        }
    
    def move_with(self, start: str, target: str, instructions: str) -> int:
        pos = start
        i = 0
        while pos != target:
            if instructions[i%len(instructions)] == "R":
                pos = self.network[pos][1]
            else:
                pos = self.network[pos][0]
            i += 1
        return i
    
    def sim_move_with(self, instructions: str) -> int:
        print(len(instructions))
        positions = [node for node in self.network if node.endswith("A")]
        offsets = []
        cycles = []
        for i, start_pos in enumerate(positions):
            pos = start_pos
            num_steps = 0
            while not pos.endswith("Z"):
                instructions_index = int(instructions[num_steps%len(instructions)] == "R")
                pos = self.network[pos][instructions_index]
                num_steps += 1
            first_z_pos = pos
            offset = num_steps
            offsets.append(offset)
            cycle = []
            while not (pos == first_z_pos and num_steps % len(instructions) == offset % len(instructions)) or num_steps == offset:
                cycle.append(pos)
                instructions_index = int(instructions[num_steps%len(instructions)] == "R")
                pos = self.network[pos][instructions_index]
                num_steps += 1
            cycles.append(cycle)
        for i in range(len(positions)):
            print(offsets[i], len(cycles[i]), len(cycles[i]) // len(instructions))
        cycle_len_multiple = len(instructions)
        for c in cycles:
            cycle_len_multiple *= len(c) // len(instructions)
        print(cycle_len_multiple)
        # not sure why it works? :shrugs:
        return cycle_len_multiple
        max_offset = max(offsets)
        ends_with_z_arrays = []
        for i in range(len(positions)):
            arr = [p.endswith("Z") for p in cycles[i]]
            arr = arr[max_offset%len(arr):] + arr[:max_offset%len(arr)]
            np_arr = np.tile(np.array(arr), cycle_len_multiple // len(arr))
            ends_with_z_arrays.append(np_arr)
        np_ends_with_z_arrays = np.array(ends_with_z_arrays)
        all_z = np.all(np_ends_with_z_arrays, axis=0)
        return max_offset + all_z.argmax()

def parse(inp):
    data = inp.split("\n")
    instructions = data[0]
    lines = [re.match("^([A-Z0-9]{3}) = \(([A-Z0-9]{3}), ([A-Z0-9]{3})\)$", line).groups() for line in data[2:]]
    network = Network(lines)
    return instructions, network


def part_a(inp):
    instructions, network = parse(inp)
    i = network.move_with("AAA", "ZZZ", instructions)
    return i


def part_b(inp):
    instructions, network = parse(inp)
    num_steps = network.sim_move_with(instructions)
    return num_steps


if __name__ == "__main__":
    with open(f"{CWD}/test_a1.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 2)
    with open(f"{CWD}/test_a2.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 6)
    with open(f"{CWD}/test_b.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 6)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
