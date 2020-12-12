f = open("2016/23.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

reg = {x:0 for x in "abcd"}
reg["a"] = 7
i = 0
while i < len(arr):
    r = arr[i].split(" ")
    if i<10: print(i,r)
    if r[0]=="cpy":
        if r[2] in reg:
            if r[1] in reg:
                reg[r[2]] = reg[r[1]]
            else:
                reg[r[2]] = int(r[1])
    elif r[0]=="inc":
        if r[1] in reg:
            reg[r[1]]+=1
    elif r[0]=="dec":
        if r[1] in reg:
            reg[r[1]]-=1
    elif r[0]=="jnz":
        if (r[1] in reg and reg[r[1]]!=0) or (r[1].isnumeric() and int(r[1])!=0):
            i += reg[r[2]] if r[2] in reg else int(r[2])
            i -= 1
    elif r[0]=="tgl":
        toggleIndex = i + (int(r[1]) if r[1].isnumeric() else reg[r[1]])
        if 0<=toggleIndex<len(arr):
            instn = arr[toggleIndex][:3]
            if arr[toggleIndex].count(" ")==1:
                arr[toggleIndex] = ("dec" if instn=="inc" else "inc") + arr[toggleIndex][3:]
            else:
                arr[toggleIndex] = ("cpy" if instn=="jnz" else "jnz") + arr[toggleIndex][3:]
    i += 1
    if i<20:    print(reg)
print(reg)

# by inspecting the instructions with extra prints
# we see a:5040 before entering the "second part"
# Note 11736 - 5040 = 72*93
# where 72,93 are values present
# and 5040 = 7!, so we guess
# 12! + 72*93 = 479008296
# Also the hint that bunnies "multiply" sorta helped here...