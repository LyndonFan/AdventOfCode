f = open("2016/09.txt","r")
inp = f.read()
f.close()
# arr = [x for x in inp.split("\n")]

# part a)
res = ""
i = 0
while i<len(inp):
    if inp[i]!="(":
        res += inp[i]
        i += 1
    else:
        j = inp.index(")",i)
        repeatLen, repeatTimes = [int(x) for x in inp[i+1:j].split("x")]
        repeatString = inp[j+1:j+1+repeatLen]
        res += repeatString * repeatTimes
        i = j+1+repeatLen
print(len(res))

# part b)
def recurLen(s):
    if not("(" in s):
        return len(s)
    resLen = 0
    i = 0
    while i < len(s):
        if s[i]=="(":
            j = s.index(")",i)
            repeatLen, repeatTimes = [int(x) for x in s[i+1:j].split("x")]
            repeatString = s[j+1:j+1+repeatLen]
            resLen += recurLen(repeatString) * repeatTimes
            i = j+1+repeatLen
        else:
            resLen += 1
            i += 1
    return resLen
print(recurLen(inp))