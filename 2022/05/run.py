# year YEAR day 5

"""
--- Day 5: Supply Stacks ---The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.
The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.
The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.
They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.
Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:
[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:
        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:
        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:
        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.
After the rearrangement procedure completes, what crate ends up on top of each stack?

"""
import os
import re

CWD = os.path.dirname(os.path.abspath(__file__))


def parse(inp):
    stack_pic, moves = inp.split("\n\n")
    moves = moves.split("\n")
    move_pat = re.compile(r"move ([0-9]+) from ([0-9]+) to ([0-9]+)")
    moves = [tuple(map(int, move_pat.search(m).groups())) for m in moves]

    lines = stack_pic.split("\n")
    stack_nums, lines = lines[-1], lines[:-1]
    stack_nums = [int(x) for x in stack_nums.split(" ") if x]
    stacks = {n: [] for n in stack_nums}
    for l in lines[::-1]:
        for i, c in zip(stack_nums, l[1::4]):
            if c != " ":
                stacks[i].append(c)
    return stacks, moves


def part_a(inp):
    stacks, moves = parse(inp)
    for n, s, t in moves:
        crates = stacks[s][-n:]
        stacks[s] = stacks[s][:-n]
        stacks[t] = stacks[t] + crates[::-1]
    res = ""
    for i in range(1, len(stacks) + 1):
        res += stacks[i][-1]
    return res


def part_b(inp):
    stacks, moves = parse(inp)
    for n, s, t in moves:
        crates = stacks[s][-n:]
        stacks[s] = stacks[s][:-n]
        stacks[t] = stacks[t] + crates
    res = ""
    for i in range(1, len(stacks) + 1):
        res += stacks[i][-1]
    return res


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", "CMZ")
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", "MCD")
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
