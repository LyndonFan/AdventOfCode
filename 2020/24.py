from copy import *

f = open("2020/24.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

# use coordinates borrowed from online:
# see implementation of first part

blackTiles = set()
for r in arr:
    coor = (0,0)
    i = 0
    while i<len(r):
        dir = r[i]
        if dir in "ns":
            dir = r[i:i+2]
            i += 1
        if dir=="e":
            coor = (coor[0]+1, coor[1])
        elif dir=="w":
            coor = (coor[0]-1, coor[1])
        elif dir=="ne":
            coor = (coor[0], coor[1]+1)
        elif dir=="se":
            coor = (coor[0]+1, coor[1]-1)
        elif dir=="sw":
            coor = (coor[0], coor[1]-1)
        elif dir=="nw":
            coor = (coor[0]-1, coor[1]+1)
        i += 1
    if coor in blackTiles:
        blackTiles.remove(coor)
    else:
        blackTiles.add(coor)

print(len(blackTiles))

def neighbour(c):
    res = []
    for n in [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]:
        res.append((c[0]+n[0],c[1]+n[1]))
    return set(res)
for _ in range(100):
    newBlackTiles = set()
    consideredTiles = blackTiles
    for b in blackTiles:
        consideredTiles = consideredTiles.union(neighbour(b))
    for t in consideredTiles:
        s = neighbour(t).intersection(blackTiles)
        if t in blackTiles:
            if len(s)==1 or len(s)==2:
                newBlackTiles.add(t)
        else:
            if len(s)==2:
                newBlackTiles.add(t)
    blackTiles = newBlackTiles
print(len(blackTiles))