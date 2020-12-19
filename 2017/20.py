f = open("2017/20.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

distFunctions = []
partPolys = []
print(len(arr))
for n, r in enumerate(arr):
    for c in "pva=<>":
        r = r.replace(c,"")
    r = r.split(", ")
    r = [[int(x) for x in a.split(",")] for a in r]
    r = r[::-1]
    polys = []
    for i in range(3):
        polys.append([r[0][i]/2, r[0][i]/2+r[1][i], r[2][i]])
    partPolys.append(polys)
    polys = [sum(abs(polys[i][j]) for i in [0,1,2]) for j in [0,1,2]]
    distFunctions.append(polys+[n])

# distFunctions for part a)
# distFunctions.sort()
# print(distFunctions[0])

# print(partPolys)

particles = set(range(len(arr)))
for t in range(1,50):
    positions = {}
    for p in particles:
        pos = [sum(partPolys[p][d][k] * t**(2-k) for k in [0,1,2]) for d in [0,1,2]]
        pos = tuple(pos)
        try:
            positions[pos].add(p)
        except:
            positions[pos] = set([p])
    # print(positions)
    for po in positions:
        if len(positions[po])>1:
            print(t,po,positions[po])
            particles = particles.difference(positions[po])
print(len(particles))
