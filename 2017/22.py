f = open("2017/22.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

n = (len(arr)-1)//2
infected = set()
weakened = set()
flagged = set()
pos = (0,0)
dirMap = {"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}
dir = "U"
dirOrder = "URDL"   # +1 for turn right
for y in range(len(arr)):
    for x in range(len(arr)):
        if arr[y][x]=="#":
            infected.add((x-n,n-y))
count = 0
for _ in range(10000000):   # 10000 for part a)
    i = dirOrder.index(dir)
    # part a) -- only infected and clean
    # if pos in infected:
    #     infected.remove(pos)
    #     i += 1
    # else:
    #     infected.add(pos)
    #     count += 1
    #     i -= 1
    if pos in infected:
        infected.remove(pos)
        flagged.add(pos)
        i += 1
    elif pos in flagged:
        flagged.remove(pos)
        i += 2
    elif pos in weakened:
        weakened.remove(pos)
        infected.add(pos)
        count += 1
    else:
        weakened.add(pos)
        i -= 1
    dir = dirOrder[i%4]
    pos = tuple(pos[k]+dirMap[dir][k] for k in [0,1])
print(count)
