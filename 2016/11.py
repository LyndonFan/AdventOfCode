from itertools import *

f = open("2016/11.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

floors = [set(x.split(" ")) for x in arr]
for i in range(4):
    if "" in floors[i]:
        floors[i].remove("")
print(floors)

seen = []
elements = "OTPRC"
stack = [(0,0,floors,[])]

def isFinal(state):
    return sum(len(state[i]) for i in [0,1,2])==0

def isValid(state):
    for i in range(4):
        for e in elements:
            if e+"M" in state[i] and not(e+"G" in state[i]):
                for g in state[i]:
                    if "G" in g:
                        return False
    return True

while not(isFinal(stack[0][2])):
    s,e,f,prev = stack.pop(0)
    if isValid(f) and not((e,f) in seen):
        seen.append((e,f))
        for d in [1,-1]:
            if 0<=e+d<4:
                for takeNum in [1,2]:
                    for toTake in combinations(f[e],takeNum):
                        newCurrent = f[e].difference(toTake)
                        newNext = f[e+d].union(toTake)
                        newF = [x for x in f]
                        newF[e] = newCurrent
                        newF[e+d] = newNext
                        stack.append((s+1,e+d,newF,prev+[(e,f)]))
    print(s,len(stack))

def printBuilding(args):
    ele, fs = args
    for i in range(3,-1,-1):
        print(("E" if ele==i else " ")+" "+" ".join(list(sorted(fs[i]))))
print(stack[0][0])
print("-"*20)
for row in stack[0][-1]:
    printBuilding(row)
    print("-"*20)

# okay I didn't run it on the full input, but ran it twice:
# once without the Ru and Co parts,
# another without the Co parts.
# First gave sol of 23 steps, 2nd gave sol of 35 steps.
# So by guessing the extra pair gives same amount of extra work,
# The ans to part a) is 35+(35-23) = 47.
# For part b), we have 2 extra pairs, so ans is 47+12*2 = 71