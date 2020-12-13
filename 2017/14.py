inp = "xlqgujun"

# copied from 10.py
def knotHash(input):
    input += [17, 31, 73, 47, 23]
    lis = list(range(256))
    skipSize = 0
    i = 0
    for _ in range(64):
        for k in input:
            lis = (lis[:k])[::-1] + lis[k:]
            s = (k+skipSize)%len(lis)
            lis = lis[s:] + lis[:s]
            i = (i+k+skipSize)%len(lis)
            skipSize += 1
    lis = lis[-i:] + lis[:-i]
    h = ""
    for i in range(16):
        r = 0
        for v in lis[16*i:16*(i+1)]:
            r = r ^ v
        h += ("0"+hex(r)[2:] if r<16 else hex(r)[2:])
    return h

res = 0
grid = []
for i in range(128):
    h = knotHash([ord(x) for x in inp+"-"+str(i)])
    for j in range(len(h)):
        res += bin(int(h[j],16)).count("1")
    showarr = [bin(int(h[j],16))[2:] for j in range(len(h))]
    for j in range(len(h)):
        showarr[j] = "0"*(4-len(showarr[j])) + showarr[j]
        showarr[j] = showarr[j].replace("0",".").replace("1","#")
    grid.append(list("".join(showarr)))
print(res)

print("\n".join("".join(g[:8]) for g in grid[:8]))

cc = 0
for i in range(128):
    for j in range(128):
        if grid[i][j]=="#":
            cc += 1
            stack = [(i,j)]
            while len(stack)>0:
                x,y = stack.pop(0)
                if grid[x][y]=="#":
                    grid[x][y] = cc
                    for d in [(0,1),(1,0),(-1,0),(0,-1)]:
                        x1 = x+d[0]
                        y1 = y+d[1]
                        if 0<=x1<128 and 0<=y1<128:
                            stack.append((x1,y1))

print("\n".join("".join(" "*(4-len(str(x)))+str(x) for x in g[:8]) for g in grid[:8]))

print(cc)
