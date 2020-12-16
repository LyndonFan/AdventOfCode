from copy import *

f = open("2020/16.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

info = arr[:arr.index("")]
myTicket = arr[arr.index("your ticket:")+1]
nearbyTickets = arr[arr.index("nearby tickets:")+1:]

# print(info)

ranges = []
for r in info:
    r = r.split(": ")[1]
    r = r.split(" or ")
    tempr = []
    for tup in r:
        a,b = tup.split("-")
        tempr.append([int(a),int(b)])
    ranges.append(tempr)

# print(ranges)

# res = 0
myTicket = [int(x) for x in myTicket.split(",")]
validTickets = [myTicket]
for t in nearbyTickets:
    t = [int(x) for x in t.split(",")]
    isValid = True
    for x in t:
        isOkay = False
        for rngs in ranges:
            for r in rngs:
                isOkay = isOkay or r[0]<=x<=r[1]
        # if not(isOkay):
        #     print(t,x)
        #     res += x
        isValid = isValid and isOkay
    if isValid:
        validTickets.append(t)
# print(res)

keys = list(zip(info,ranges))
possKeys = [deepcopy(keys) for _ in keys]
for t in validTickets:
    for i in range(len(t)):
        for name,rngs in possKeys[i]:
            if not(rngs[0][0]<=t[i]<=rngs[0][1] or rngs[1][0]<=t[i]<=rngs[1][1]):
                possKeys[i].pop(possKeys[i].index((name,rngs)))
isSolved = all(len(ls)==1 for ls in possKeys)
for _ in range(len(possKeys)):
    for i in range(len(possKeys)):
        if len(possKeys[i])==1:
            for j in range(len(possKeys)):
                if not (i==j) and possKeys[i][0] in possKeys[j]:
                    possKeys[j].pop(possKeys[j].index(possKeys[i][0]))
for i in range(len(possKeys)):
    print(possKeys[i], myTicket[i])
# print(list(zip([pk[0] for pk in possKeys],myTicket)))
print("-"*50)
res = 1
for i in range(len(possKeys)):
    if "departure" in possKeys[i][0][0]:
        res *= myTicket[i]
        print(possKeys[i], myTicket[i])
print(res)