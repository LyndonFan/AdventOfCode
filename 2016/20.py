f = open("2016/20.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

ranges = [[int(x) for x in r.split("-")] for r in arr]
ranges.sort()

# minAllowed = 0
# for r in ranges:
#     if r[0]<=minAllowed<=r[1]:
#         minAllowed = r[1]+1
# print(minAllowed)

i = 0
while i < len(ranges):
    j = 1
    currRangeMax = ranges[i][1]
    while i+j<len(ranges) and currRangeMax+1>=ranges[i+j][0]:
        currRangeMax = max(currRangeMax,ranges[i+j][1])
        j += 1
    newRange = [ranges[i][0],currRangeMax]
    ranges[i] = newRange
    for _ in range(j-1):
        ranges.pop(i+1)
    i += 1
print(ranges)
maxIP = 4294967295 + 1
print(maxIP - sum(r[1]-r[0]+1 for r in ranges))
