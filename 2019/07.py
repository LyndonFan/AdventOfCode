from intCode import intCode
from itertools import permutations

f = open("2019/07.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split(",")]

maxThurst = 0
# for p in permutations(range(5)):
#     curr = 0
#     p = list(p)
#     for i in range(5):
#         res = intCode(arr,[p[i],curr])
#         print(res[1])
#         curr = res[1][0]
#     maxThurst = max(curr,maxThurst)
# print(maxThurst)

for p in permutations(range(5,10)):
    curr = 0
    seen = []
    p = list(p)
    i = 0
    while True:
        res = intCode(arr,[p[i],curr])
        print(res[1])
        if len(res)==0:
            break
        curr = res[1][0]
        i += 1
        if i%5==0:
            seen.append(curr)
    maxThurst = max(max(seen),maxThurst)
print(maxThurst)