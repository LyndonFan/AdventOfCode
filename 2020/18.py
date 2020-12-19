from copy import *

f = open("2020/18.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

def evalExpr(s):
    s = s.strip()
    print(s)
    if not("(" in s):
        s = s.split(" ")
        # for i in range((len(s)-1)//2):
        #     if s[2*i+1]=="+":
        #         n += int(s[2*i+2])
        #     else:
        #         n *= int(s[2*i+2])
        # return n
        while "+" in s:
            i = s.index("+")
            s[i-1] = str(int(s[i-1]) + int(s[i+1]))
            s.pop(i)
            s.pop(i)
        return eval(" ".join(s))
    i = s.index("(")
    lvl = 1
    j = i+1
    while lvl>0:
        lvl += s[j]=="("
        lvl -= s[j]==")"
        j += 1
    newS = s[:i] + str(evalExpr(s[i+1:j-1])) + s[j:]
    return evalExpr(newS)

res = 0
for r in arr:
    res += evalExpr(r)
print(res)