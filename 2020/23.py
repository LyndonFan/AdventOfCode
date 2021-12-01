inp = 583976241

inp = [int(x) for x in str(inp)]
inp += list(range(max(inp)+1,1000000+1))    # only for part 2
n = max(inp)

# part a)
# for i in range(100):
#     print(i)
#     oldCup = inp[i%len(inp)]
#     pickup = [inp[(i+j)%len(inp)] for j in range(1,4)]
#     for p in pickup:
#         inp.pop(inp.index(p))
#     newCup = oldCup - 1
#     while not(newCup in inp):
#         newCup -= 1
#         if newCup<=0:
#             newCup = n
#     k = inp.index(newCup)
#     inp = inp[:k+1] + pickup + inp[k+1:]
#     while inp[i%len(inp)]!=oldCup:
#         inp = inp[1:] + inp[:1]
# # print(inp)
# k = inp.index(1)
# print(inp[k+1]*inp[k+2])

class Cup:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
cups = {v: Cup(v,None) for v in inp}
for i in range(len(inp)):
    cups[inp[i]].next = cups[inp[(i+1)%len(inp)]]
curr = cups[inp[0]]
for t in range(10000000):
    print(t)
    firstCup = curr.next
    thirdCup = curr.next.next.next
    curr.next = thirdCup.next
    targetVal = curr.val - 1
    if targetVal<=0:
        targetVal = n
    while targetVal in {firstCup.val, firstCup.next.val, thirdCup.val}:
        targetVal -= 1
        if targetVal<=0:
            targetVal = n
    dest = cups[targetVal]
    thirdCup.next = dest.next
    dest.next = firstCup
    curr = curr.next

target = cups[1]
print(target.next.val * target.next.next.val)