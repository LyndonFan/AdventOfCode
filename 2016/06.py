f = open("2016/06.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

res = ""
for i in range(len(arr[0])):
    r = [x[i] for x in arr]
    counts = {r.count(x):x for x in r}
    res += counts[min(counts.keys())] # max for part a)
print(res)