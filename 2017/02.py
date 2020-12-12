f = open("2017/02.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

count = 0
for r in arr:
    r = r.split("\t")
    while "" in r:
        r.pop(r.index(""))
    r = [int(x) for x in r]
    # count += max(r) - min(r) # part a)
    for i in range(len(r)):
        for j in range(len(r)):
            if i!=j:
                if r[i]%r[j]==0:
                    count += r[i]//r[j]
print(count)