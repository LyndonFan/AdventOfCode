f = open("2019/03.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

seens = [[],[]]
seenSteps = [{},{}]

for i in [0,1]:
    r = arr[i].split(",")
    start = (0,0)
    steps = 0 # ignore for part a)
    for tup in r:
        print(tup)
        dir, num = tup[0], int(tup[1:])
        newPos = []
        if dir=="R":
            newPos += [(start[0]+i,start[1]) for i in range(1,num+1)]
            start = (start[0]+num,start[1])
        if dir=="L":
            newPos += [(start[0]-i,start[1]) for i in range(1,num+1)]
            start = (start[0]-num,start[1])
        if dir=="U":
            newPos += [(start[0],start[1]+i) for i in range(1,num+1)]
            start = (start[0],start[1]+num)
        if dir=="D":
            newPos += [(start[0],start[1]-i) for i in range(1,num+1)]
            start = (start[0],start[1]-num)
        seens[i] += newPos
        for j in range(1,num+1):
            if not(newPos[j-1] in seenSteps[i]):
                seenSteps[i][newPos[j-1]] = steps+j
        steps += num
    seens[i] = set(seens[i])

crosses = list(seens[0].intersection(seens[1]))
# crosses.sort(key = lambda t: abs(t[0])+abs(t[1])) # for part a)
# print(sum(abs(x) for x in crosses[0])) # for part a)
crosses.sort(key = lambda t: seenSteps[0][t]+seenSteps[1][t])
print(crosses[0])
print(seenSteps[0][crosses[0]]+seenSteps[1][crosses[0]])