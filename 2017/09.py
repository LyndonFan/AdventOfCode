f = open("2017/09.txt","r")
inp = f.read()
f.close()

inp = list(inp)
score = 0
lvl = 0
isGarbage = False
garbageCount = 0
while len(inp)>0:
    s = inp.pop(0)
    if isGarbage and s not in "!>":
        garbageCount += 1
    elif isGarbage and s=="!":
        inp.pop(0)
    elif isGarbage and s==">":
        isGarbage = False
    elif not(isGarbage) and s=="<":
        isGarbage = True
    elif s=="{":
        lvl += 1
    elif s=="}":
        score += lvl
        lvl -= 1
print(score)
print(garbageCount)
    