f = open("2016/21.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

inp = list("abcdefgh")

for r in arr:
    r = r.split(" ")
    if r[0]=="swap":
        i = int(r[2]) if r[1]=="position" else inp.index(r[2])
        j = int(r[-1]) if r[-2]=="position" else inp.index(r[-1])
        inp[i], inp[j] = inp[j], inp[i]
        print("swap",i,j,":",inp)
    elif r[0]=="reverse":
        indicies = [int(r[2]),int(r[-1])]
        i,j = min(indicies), max(indicies)
        inp = inp[:i] + (inp[i:j+1])[::-1] + inp[j+1:]
        print("reverse",i,j,":",inp)
    elif r[0]=="rotate":
        if r[1]=="based":
            i = inp.index(r[-1])
            i += 1 + (i>=4)
            inp = inp[-i:] + inp[:-i]
            print("rotate right",i,":",inp)
        else:
            i = int(r[2])
            if r[1]=="right":
                inp = inp[-i:] + inp[:-i]
            else:
                inp = inp[i:] + inp[:i]
            print("rotate",r[1],i,":",inp)
    else:
        i = int(r[2])
        j = int(r[-1])
        inp.insert(j,inp.pop(i))
        print("move",i,j,':',inp)
print("".join(inp))