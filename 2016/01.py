f = open("2016/01.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split(", ")]

# part a)
# unitVectors = [(0,1),(1,0),(0,-1),(-1,0)]
# dir = 0
# pos = [0,0]
# for r in arr:
#     dir = (dir + (1 if r[0]=="R" else -1))%4
#     pos = [pos[i]+unitVectors[dir][i]*int(r[1:]) for i in [0,1]]
#     print(pos)
# print(sum(abs(x) for x in pos))

unitVectors = [(0,1),(1,0),(0,-1),(-1,0)]
dir = 0
pos = [0,0]
seen = [[0,0]]
for r in arr:
    dir = (dir + (1 if r[0]=="R" else -1))%4
    for _ in range(int(r[1:])):
        pos = [pos[i]+unitVectors[dir][i] for i in [0,1]]
        if pos in seen:
            print(pos)
            print(sum(abs(x) for x in pos))
            exit()
        seen.append(pos)
