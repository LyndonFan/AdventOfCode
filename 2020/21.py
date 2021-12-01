f = open("2020/21.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

algcandidates = {}
ingredientsCount = {}
for r in arr:
    ingredients, alg = r.split(" (contains ")
    alg = alg[:-1].split(", ")
    ingredients = ingredients.split(" ")
    for a in alg:
        if not(a in algcandidates):
            algcandidates[a] = set(ingredients)
        else:
            algcandidates[a] = algcandidates[a].intersection(set(ingredients))
    for ing in ingredients:
        try:
            ingredientsCount[ing] += 1
        except:
            ingredientsCount[ing] = 1
print(algcandidates)

progress = True
found = set()
while progress:
    progress = False
    for a in algcandidates:
        if len(algcandidates[a])==1 and not(a in found):
            progress = True
            found.add(a)
            algcandidates[a] = list(algcandidates[a])
            elem = algcandidates[a][0]
            for b in algcandidates:
                if a!=b and elem in algcandidates[b]:
                    algcandidates[b].remove(elem)
    print(algcandidates)

s = sum(ingredientsCount[ing] for ing in ingredientsCount)
for a in algcandidates:
    for e in algcandidates[a]:
        s -= ingredientsCount[e]
print(s)

pairs = [(a,algcandidates[a][0]) for a in algcandidates]
pairs.sort()
print(",".join(p[1] for p in pairs))