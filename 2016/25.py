f = open("2016/25.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

def computer(inp):
    reg = {x:0 for x in "abcd"}
    reg["a"] = inp
    i = 0
    output = []
    count = 0
    while i < len(arr) and count<100000 and len(output) < 10:
        r = arr[i].split(" ")
        # if i<10: print(i,r)
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
        elif r[0]=="out":
            output.append(reg[r[1]] if r[1] in reg else int(r[1]))
        i += 1
        count += 1
        # print(i,reg,output)
    return i, output

k = 1
while True:
    res = computer(k)
    _, output = res
    print(k,output)
    if len(output)>0 and output == [0,1]*((len(output))//2):
        exit()
    k += 1