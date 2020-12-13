f = open("2017/12.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

pipes = {}
for r in arr:
    r = r.split(" <-> ")
    pipes[r[0]] = r[1].split(", ")

# part a)
# seen = set()
# stack = ["0"]
# while len(stack)>0:
#     curr = stack.pop(0)
#     new = set(pipes[curr]).difference(seen)
#     seen = seen.union(set(pipes[curr]))
#     stack += list(new)
# print(len(seen))

groups = []
while len(pipes)>0:
    seen = set()
    stack = [min(pipes)]
    while len(stack)>0:
        curr = stack.pop(0)
        new = set(pipes[curr]).difference(seen)
        seen = seen.union(set(pipes[curr]))
        stack += list(new)
    groups.append(seen)
    for s in seen:
        pipes.pop(s,None)
print(len(groups))