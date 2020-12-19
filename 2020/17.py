from copy import *

f = open("2020/17.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

active = set()

bound = (len(arr)+1)//2
print(bound)

for y in range(len(arr)):
    for x in range(len(arr[0])):
        if arr[y][x]=="#":
            # active.add((x-bound,y-bound,0))
            active.add((x-bound,y-bound,0,0))

# def neighbours(pos):
#     x,y,z = pos
#     res = []
#     for i in range(-1,2):
#         for j in range(-1,2):
#             for k in range(-1,2):
#                 if i!=0 or j!=0 or k!=0:
#                     res.append((x+i,y+j,z+k))
#     return res

# for it in range(6):
#     bound += 1
#     newActive = set()
#     for pos in active:
#         s = set(neighbours(pos)).intersection(active)
#         if len(s)==2 or len(s)==3:
#             newActive.add(pos)
#     for x in range(-bound,bound+1):
#         for y in range(-bound, bound+1):
#             for z in range(-bound, bound+1):
#                 s = set(neighbours((x,y,z))).intersection(active)
#                 if len(s)==3:
#                     newActive.add((x,y,z))
#     active = newActive

def neighbours(pos):
    x,y,z,w = pos
    res = []
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                for l in range(-1,2):
                    if i!=0 or j!=0 or k!=0 or l!=0:
                        res.append((x+i,y+j,z+k,w+l))
    return res

for it in range(6):
    bound += 1
    newActive = set()
    for pos in active:
        s = set(neighbours(pos)).intersection(active)
        if len(s)==2 or len(s)==3:
            newActive.add(pos)
    for x in range(-bound,bound+1):
        for y in range(-bound, bound+1):
            for z in range(-bound, bound+1):
                for w in range(-bound, bound+1):
                    s = set(neighbours((x,y,z,w))).intersection(active)
                    if len(s)==3:
                        newActive.add((x,y,z,w))
    active = newActive

print(len(active))