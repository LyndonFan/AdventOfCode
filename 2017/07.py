f = open("2017/07.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

trees = {}
parent = {}
for r in arr:
    r = r.replace("(","").replace(")","").split(" -> ")
    front = r[0].split(" ")
    back = r[1].split(", ") if len(r)>1 else []
    trees[front[0]] = (int(front[1]),back)
    for t in back:
        parent[t] = front[0]

c = front[0]
while c in parent:
    c = parent[c]
print(c)

bottom = "vtzay"

def weight(t):
    w, children = trees[t]
    return w + sum(weight(c) for c in children)

def findBalance(t):
    _, children = trees[t]
    if len(children)<2:
        return False
    for c in children:
        res = findBalance(c)
        if res:
            return res
    weights = [weight(c) for c in children]
    vals = list(set(weights))
    if len(vals)==1:
        return False
    if weights.count(vals[0])==1:
        outlier = vals[0]
        common = vals[1]
    else:
        outlier = vals[1]
        common = vals[0]
    i = weights.index(outlier)
    return trees[children[i]][0] + common - outlier

print(findBalance(bottom))
    
