f = open("2020/12.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

pos = [0,0]
dir = "E"
maps = {"E":[1,0],"N":[0,1],"S":[0,-1],"W":[-1,0]}
dirs = "ESWN"

for r in arr:
    d, n = r[0], int(r[1:])
    if d in dirs:
        pos = [pos[i] + maps[d][i]*n for i in [0,1]]
    elif d=="F":
        pos = [pos[i] + maps[dir][i]*n for i in [0,1]]
    elif d=="L":
        dir = dirs[(dirs.index(dir) - n//90)%4]
    elif d=="R":
        dir = dirs[(dirs.index(dir) + n//90)%4]
    print(pos)

print(pos)

pos = [0,0]
waypoint = [10,1]
dir = "E"
maps = {"E":[1,0],"N":[0,1],"S":[0,-1],"W":[-1,0]}
dirs = "ESWN"

for r in arr:
    d, n = r[0], int(r[1:])
    if d in dirs:
        waypoint = [waypoint[i] + maps[d][i]*n for i in [0,1]]
    elif d=="F":
        pos = [pos[i] + waypoint[i]*n for i in [0,1]]
    elif r=="L90" or r=="R270":
        waypoint = [-waypoint[1], waypoint[0]]
    elif r=="R90" or r=="L270":
        waypoint = [waypoint[1], -waypoint[0]]
    elif n==180:
        waypoint = [-x for x in waypoint]
    print(pos)

print(pos)
print(sum(abs(x) for x in pos))