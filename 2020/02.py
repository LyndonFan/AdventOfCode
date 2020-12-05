f = open("2020/02.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split('\n')]

def xor(p,q):
    return (p and not q) or (not p and q)

count = 0
for l in arr:
    numTimes, char, pw = l.split(" ")
    char = char[0]
    pos = [int(x) for x in numTimes.split("-")]
    count += xor(pw[pos[0]-1]==char,pw[pos[1]-1]==char)
print(count)