# year 2022 day 7
import os
import re

CWD = os.path.dirname(os.path.abspath(__file__))

file_pattern = re.compile("(dir|[0-9]+) ([^\n]+)")


def parse(inp):
    lines = inp.strip("\n$ ").split("\n$ ")
    children = {}
    parent = {}
    size = {}
    curr_path = []
    for l in lines:
        if l[:2] == "cd":
            dir = l[3:]
            if dir == "..":
                curr_path.pop()
            else:
                curr_path.append(dir)
            continue
        childs = []
        for s, f in file_pattern.findall(l):
            c = tuple(curr_path + [f])
            childs.append(c)
            parent[c] = tuple(curr_path)
            if s != "dir":
                size[c] = int(s)
        children[tuple(curr_path)] = childs

    return {
        "children": children,
        "parent": parent,
        "size": size,
    }


def part_a(inp):
    data = parse(inp)
    children = data["children"]
    size = data["size"]

    stack = [(("/",), "exp")]
    while stack:
        dir, act = stack.pop()
        if act == "sum":
            size[dir] = sum(size[c] for c in children[dir])
        elif dir in size:
            continue
        else:
            stack.append((dir, "sum"))
            stack += [(c, "exp") for c in children[dir]]

    ans = 0
    for d in children:
        if size[d] <= 100000:
            ans += size[d]

    return ans


def part_b(inp):
    data = parse(inp)
    children = data["children"]
    size = data["size"]

    stack = [(("/",), "exp")]
    while stack:
        dir, act = stack.pop()
        if act == "sum":
            size[dir] = sum(size[c] for c in children[dir])
        elif dir in size:
            continue
        else:
            stack.append((dir, "sum"))
            stack += [(c, "exp") for c in children[dir]]

    revsize = {v: k for k, v in size.items()}
    all_sizes = list(revsize.keys())
    all_sizes.sort()

    TOTAL_AVAILABLE = 70000000
    NEED_UNUSED = 30000000
    CURR_USED = size[("/",)]
    MIN_FILE_SIZE = CURR_USED - (TOTAL_AVAILABLE - NEED_UNUSED)
    for s in all_sizes:
        if s >= MIN_FILE_SIZE:
            dir = revsize[s]
            if dir in children:
                return s

    raise ValueError("Unable to find file large enough...?")


if __name__ == "__main__":
    with open(f"{CWD}/test.txt", "r") as f:
        inp = f.read().strip()
    print("Testing  (a):", part_a(inp))
    print("Expected (a):", 95437)
    print("Testing  (b):", part_b(inp))
    print("Expected (b):", 24933642)
    with open(f"{CWD}/input.txt", "r") as f:
        inp = f.read().strip()
    print("Actual   (a):", part_a(inp))
    print("Actual   (b):", part_b(inp))
