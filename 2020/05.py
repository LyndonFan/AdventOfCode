f = open("2020/05.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

maxID = 0
ids = []
for r in arr:
    row = r[:-3]
    col = r[-3:]
    print(row,col)
    row = int("".join(str(int(x=="B")) for x in row),2)
    col = int("".join(str(int(x=="R")) for x in col),2)
    thisID = row*8 + col
    ids.append(thisID)
    maxID = max(thisID,maxID)
# print(maxID) # for part a)

for i in ids:
    if not(i+1 in ids) and (i+2 in ids):
        print(i+1)