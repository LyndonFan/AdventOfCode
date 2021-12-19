# day 12 solutions

"""
--- Day 12: Passage Pathing ---
With your submarine's subterranean subsystems subsisting suboptimally, the only way you're getting out of this cave anytime soon is by finding a path yourself. Not just a path - the only way to know if you've found the best path is to find all of them.

Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves (your puzzle input). For example:

start-A
start-b
A-c
A-b
b-d
A-end
b-end
This is a list of how all of the caves are connected. You start in the cave named start, and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d - that is, you can move between them.

So, the above cave system looks roughly like this:

    start
    /   \
c--A-----b--d
    \   /
     end
Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

Given these rules, there are 10 paths through this example cave system:

start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,end
start,A,c,A,b,A,end
start,A,c,A,b,end
start,A,c,A,end
start,A,end
start,b,A,c,A,end
start,b,A,end
start,b,end
(Each line in the above list corresponds to a single path; the caves visited by that path are listed in the order they are visited and separated by commas.)

Note that in this cave system, cave d is never visited by any path: to do so, cave b would need to be visited twice (once on the way to cave d and a second time when returning from cave d), and since cave b is small, this is not allowed.

Here is a slightly larger example:

dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
The 19 paths through it are as follows:

start,HN,dc,HN,end
start,HN,dc,HN,kj,HN,end
start,HN,dc,end
start,HN,dc,kj,HN,end
start,HN,end
start,HN,kj,HN,dc,HN,end
start,HN,kj,HN,dc,end
start,HN,kj,HN,end
start,HN,kj,dc,HN,end
start,HN,kj,dc,end
start,dc,HN,end
start,dc,HN,kj,HN,end
start,dc,end
start,dc,kj,HN,end
start,kj,HN,dc,HN,end
start,kj,HN,dc,end
start,kj,HN,end
start,kj,dc,HN,end
start,kj,dc,end
Finally, this even larger example has 226 paths through it:

fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
How many paths through this cave system are there that visit small caves at most once?
"""


def q12a(inp):
    data = inp.split("\n")
    data = list(map(lambda x: x.split("-"), data))
    vertices = set(v for tup in data for v in tup)
    edges = set(map(tuple, data))
    neighbours = {v: set() for v in vertices}
    for v1, v2 in edges:
        neighbours[v1].add(v2)
        neighbours[v2].add(v1)
    print(neighbours)
    # items in queue are (current, path inc. current, visited small caves)
    queue = [("start", ["start"], set())]
    numpaths = 0
    while queue:
        current, path, visited = queue.pop(0)
        if current == "start" and path != ["start"]:
            continue
        if current == "end":
            # print(path)
            numpaths += 1
            continue
        if current.lower() == current and current in visited:
            continue
        if current.lower() == current:
            new_visited = visited.union(set([current]))
        else:
            new_visited = set(list(visited))
        for neighbour in neighbours[current]:
            queue.append(
                (neighbour, path + [neighbour], new_visited))

    return numpaths


def q12b(inp):
    data = inp.split("\n")
    data = list(map(lambda x: x.split("-"), data))
    vertices = set(v for tup in data for v in tup)
    edges = set(map(tuple, data))
    neighbours = {v: set() for v in vertices}
    for v1, v2 in edges:
        neighbours[v1].add(v2)
        neighbours[v2].add(v1)
    # print(neighbours)
    # items in queue are (current, path inc. current, visited small caves, double visited caves)
    queue = [("start", ["start"], set(), None)]
    numpaths = 0
    paths = []
    while queue:
        current, path, visited, double_visited = queue.pop(0)
        if current == "start" and path != ["start"]:
            continue
        if current == "end":
            # print(path)
            paths.append(path)
            numpaths += 1
            continue
        new_double_visited = double_visited
        new_visited = visited.copy()
        if current.lower() == current:
            if current in visited:
                if double_visited is not None:
                    continue
                new_double_visited = current
            new_visited.add(current)
        for neighbour in neighbours[current]:
            queue.append(
                (neighbour, path + [neighbour], new_visited, new_double_visited))
    # paths.sort(key=lambda x: ",".join(x))
    # print("\n".join(",".join(x) for x in paths))
    return numpaths


if __name__ == "__main__":
    with open("12test.txt", "r") as f:
        data = f.read().strip()
    print("Testing  (a):", q12a(data))
    print("Expected (a):", 10)
    print("Testing  (b):", q12b(data))
    print("Expected (b):", 36)
    with open("12.txt", "r") as f:
        data = f.read().strip()
    print("Actual   (a): ", q12a(data))
    print("Actual   (b): ", q12b(data))
