actualinp = "165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153"
inp = [int(x) for x in actualinp.replace(" ","").split(",")]

# lis = list(range(256))
# skipSize = 0
# i = 0
# for k in inp:
#     lis = (lis[:k])[::-1] + lis[k:]
#     s = (k+skipSize)%len(lis)
#     lis = lis[s:] + lis[:s]
#     i = (i+k+skipSize)%len(lis)
#     skipSize += 1
#     # print(lis)
#     # templis = lis[-i:] + lis[:-i]
#     # print(templis)
# print(lis[-i%len(lis)]*lis[(-i+1)%len(lis)])

inp = [ord(x) for x in actualinp]
inp += [17, 31, 73, 47, 23]

def knotHash(input):
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

print(knotHash(inp))