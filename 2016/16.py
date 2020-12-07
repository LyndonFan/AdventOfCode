inp = "00111101111101000"

while len(inp)<35651584: # 272 for part a)
    temp = "".join(list(inp))
    for tup in ["0B","1A","A0","B1"]:
        temp = temp.replace(tup[0],tup[1])
    inp = inp + "0" + temp[::-1]
inp = inp[:35651584] # 272 for part a)

while len(inp)%2==0:
    inp = "".join(str(int(inp[2*i]==inp[2*i+1])) for i in range(len(inp)//2))

print(inp)