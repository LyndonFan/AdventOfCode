f = open("2017/01.txt","r")
inp = f.read()
f.close()

count = 0
for i in range(len(inp)):
    if inp[i]==inp[(i+len(inp)//2)%len(inp)]:   # +1 for a)
        count += int(inp[i])
print(count)