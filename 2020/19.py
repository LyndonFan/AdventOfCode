from copy import *
from itertools import *
import re

f = open("2020/19.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

k = arr.index("")
rulesInp = arr[:k]
messages = arr[k+1:]

for i in range(len(rulesInp)):
    r = rulesInp[i]
    r = r.replace('"','')
    r = r.split(": ")
    r[1] = r[1].split(" | ")
    for j in range(len(r[1])):
        r[1][j] = r[1][j].split(" ")
    rulesInp[i] = r

rules = {'a':'a','b':'b'}
changed = True
while changed:
    changed = False
    for r in rulesInp:
        if not(r[0] in ['0','11','8']) and not(r[0] in rules) and all(all(x in rules for x in tup) for tup in r[1]):
            print(r)
            res = []
            changed = True
            for tup in r[1]:
                # print([rules[x] for x in tup])
                # print(list(product(*[rules[x] for x in tup])))
                for t in product(*[rules[x] for x in tup]):
                    tempStr = ""
                    # print(t)
                    for s in t:
                        # print(s)
                        tempStr += s
                    res.append(tempStr)
            rules[r[0]] = res
            # print(rules[r[0]])

# print(rules['0'])
# print(len(rules['42']),len(rules['31']))
# print(max(len(m) for m in messages))
count = 0
r42 = "|".join(rules['42'])
r31 = "|".join(rules['31'])
regexs = []
for i in range(1,96//8):
    r = "^({})+({})".format(r42,r42)
    r += "{"+str(i)+"}"
    r += "("+r31+")"
    r += "{"+str(i)+"}$"
    regexs.append(r)

for m in messages:
    # count += any(pat==m for pat in rules['0'])    # part a)
    k = len(m)//8 + 1
    isMatch = False
    for r in regexs:
        isMatch = isMatch or not(re.search(r,m)==None)
    count += isMatch
print(count)