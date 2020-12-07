f = open("2016/12.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

reg = {x:0 for x in "abcd"}
reg["c"] = 1 # only for part b)
i = 0
while i < len(arr):
    r = arr[i].split(" ")
    if r[0]=="cpy":
        if r[1] in reg:
            reg[r[2]] = reg[r[1]]
        else:
            reg[r[2]] = int(r[1])
    elif r[0]=="inc":
        reg[r[1]]+=1
    elif r[0]=="dec":
        reg[r[1]]-=1
    elif r[0]=="jnz":
        if (r[1] in reg and reg[r[1]]!=0) or (r[1].isnumeric() and int(r[1])!=0):
            i += int(r[2]) - 1
    i += 1
print(reg)