f = open("2020/06.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n\n")]


res = 0
for r in arr:
    r = r.split("\n")
    ans = set(r[0])
    for s in r[1:]:
        ans = ans.intersection(set(s))
        # use union for part a)
    res += len(ans)
print(res)