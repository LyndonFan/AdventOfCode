f = open("2016/03.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

count = 0

newArr = []

for ar in arr:
    r = ar.split(" ")
    while "" in r:
        r.pop(r.index(""))
    r = [int(x) for x in r]
    newArr.append(r)

# only needed for part b)
for k in range(len(arr)//3):
    tempArr = [[c for c in r] for r in newArr[3*k:3*k+3]]
    for i in range(3):
        for j in range(3):
            newArr[3*k+i][j] = tempArr[j][i]

for r in newArr:
    count += sum(r)>2*max(r)
print(count)