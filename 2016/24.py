from heapq import *
from itertools import *

f = open("2016/24.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

grid = arr
positions = [[] for _  in range(8)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not (grid[i][j] in ".#"):
            positions[int(grid[i][j])] = [i,j]

lengths = {}

def dist(pos1,pos2):
    return sum(abs(pos1[k] - pos2[k]) for k in [0,1])

# bfs too slow, have to use A*
for i in range(len(positions)-1):
    for j in range(i+1,len(positions)):
        print(i,j)
        target = positions[j]
        seen = set()
        h = []
        heappush(h, (dist(positions[i],target),0,positions[i]))
        prevg = -1
        prevd = -1
        while True:
            g,d,pos = heappop(h)
            d *= -1 # implicitly explores paths which have more work in them
            # if i==0 and j==6 and (g!=prevg or d!=prevd):
            #     print(g,d)
            #     prevg = g
            #     prevd = d
            x,y = pos
            if pos == target:
                lengths[(i,j)] = d
                lengths[(j,i)] = d
                print((i,j),":",d)
                break
            seen.add((x,y))
            for dir in [[1,0],[0,1],[-1,0],[0,-1]]:
                x1 = x+dir[0]
                y1 = y+dir[1]
                if 0<=x1<len(grid) and 0<=y1<len(grid[0]) and grid[x1][y1]!="#" and not((x1,y1) in seen):
                    heappush(h, (dist([x1,y1],target)+d+1,-(d+1),[x1,y1]))
print(lengths)
            
shortestPath = []
minLength = 500*len(positions) # large const
for p in permutations(range(1,len(positions))):
    p = [0]+list(p)+[0] # +[0] for part b) 
    pl = sum(lengths[(p[i],p[i+1])] for i in range(len(p)-1))
    if pl<minLength:
        shortestPath = [x for x in p]
        minLength = pl
print(shortestPath)
print(minLength)