f = open("2017/21.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

pattern = """.#.
..#
###"""
pattern = pattern.split("\n")

def xflip(pat):
    return [r[::-1] for r in pat]

def yflip(pat):
    return pat[::-1]

def rot90(pat):
    k = len(pat)
    return ["".join(pat[j][k-1-i] for j in range(k)) for i in range(k)]

def allPatterns(pat):
    pats = [pat, xflip(pat), yflip(pat), rot90(rot90(pat))]
    pats += [rot90(p) for p in pats]
    return pats

rules = {}
for r in arr:
    inp, out = r.split(" => ")
    for pat in allPatterns(inp.split("/")):
        rules["/".join(pat)] = out

for _ in range(18): # 5 for part a)
    n = 2 if len(pattern)%2==0 else 3
    blocks = []
    for i in range(len(pattern)//n):
        blocks.append([])
        for j in range(len(pattern)//n):
            b = [p[n*j:n*j+n] for p in pattern[i*n:i*n+n]]
            # print("/".join(b), rules["/".join(b)])
            blocks[-1].append(rules["/".join(b)].split("/"))
    newPattern = [[" " for _ in range(len(pattern)//n*(n+1))] for _ in range(len(pattern)//n*(n+1))]
    # print(blocks)
    for y in range(len(pattern)//n):
        for x in range(len(pattern)//n):
            for j in range(n+1):
                for i in range(n+1):
                    newPattern[y*(n+1)+j][x*(n+1)+i] = blocks[y][x][j][i]
    pattern = ["".join(p) for p in newPattern]
    # print("\n".join(pattern))

print(sum(p.count("#") for p in pattern))