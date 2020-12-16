f = open("2020/14.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split('\n')]

mem = {}
mask = "X"*36

def toBin(x):
    val = bin(int(x))[2:]
    val = "0"*(36 - len(val)) + val
    return val

def possibleAddress(m):
    if not("X" in m):
        return [m]
    i = m.index("X")
    res = []
    for k in "01":
        newM = m[:i]+k+m[i+1:]
        res += possibleAddress(newM)
    return res

for r in arr:
    if r[:4]=="mask":
        mask = r.split(" = ")[1]
    else:
        r = r.replace("mem","").replace("[","").replace("]","")
        r = r.split(" = ")
        # # part a)
        # val = bin(int(r[1]))[2:]
        # val = "0"*(36 - len(val)) + val
        # for i in range(36):
        #     if mask[i]!="X":
        #         val = val[:i]+mask[i]+val[i+1:]
        #     mem[r[0]] = int(val)
        add = toBin(r[0])
        for i in range(36):
            if mask[i]!="0":
                add = add[:i]+mask[i]+add[i+1:]
        print(add)
        for a in possibleAddress(add):
            mem[int(a,2)] = int(r[1])

# print(mem)
print(sum(mem.values()))