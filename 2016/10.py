f = open("2016/10.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

bots = {}

def addValTo(val,botNum):
    if botNum in bots:
        bots[botNum].append(val)
    else:
        bots[botNum] = [val]

instructions = []

for r in arr:
    if "goes" in r:
        r = r.replace("value ","").split(" goes to ")
        addValTo(int(r[0]),r[1])
    else:
        r = r.replace(" gives low to "," and high to ").split(" and high to ")
        if r[0] in bots and len(bots[r[0]])==2:
            addValTo(r[1],min(bots[r[0]]))
            addValTo(r[2],max(bots[r[0]]))
            bots[r[0]] = []
        instructions.append(r)

print(bots)

while not("output 0" in bots and "output 1" in bots and "output 2" in bots):
    for r in instructions:
        if r[0] in bots and len(bots[r[0]])==2:
            print(r,bots[r[0]])
            if set(bots[r[0]])==set([61,17]):
                print(r[0])
                # exit() # for part a)
            addValTo(min(bots[r[0]]),r[1])
            addValTo(max(bots[r[0]]),r[2])
            bots[r[0]] = []
            print(bots)
res = 1
for i in range(3):
    res *= bots["output "+str(i)][0]
print(res)