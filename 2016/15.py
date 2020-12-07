f = open("2016/15.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

discs = []
for r in arr:
    r = r.split(" ")
    discs.append([int(r[1][1:]), int(r[3]), int(r[-1][:-1])])
k = 0
isOkay = False
while not(isOkay):
    isOkay = True
    for i, base, pos in discs:
        isOkay = isOkay and (k+i+pos)%base==0
    k += 1
print(k-1)

# the last line is extra for part b)