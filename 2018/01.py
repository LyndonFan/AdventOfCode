f = open("2018/01.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split("\n")]


seen = []
curr = 0
for x in arr:
    seen.append(curr)
    curr += x
lapChange = curr
tuples = []
for i in range(len(seen)):
    for j in range(len(seen)):
        diff = seen[i]-seen[j]
        if i!=j and diff>0 and diff%lapChange==0:
            tuples.append([diff//lapChange,j,i])
tuples.sort()
print(tuples[0])
print(seen[tuples[0][2]])