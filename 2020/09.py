f = open("2020/09.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split("\n")]

preambleLen = 25

for i in range(len(arr)-preambleLen-1):
    prevArr = arr[i:i+preambleLen]
    canbeSummed = False
    for j in range(preambleLen):
        canbeSummed = canbeSummed or arr[i+preambleLen]-arr[i+j] in prevArr[j+1:]
    if not(canbeSummed):
        print(arr[i+preambleLen])

# part a) 10884537

for i in range(len(arr)):
    tempArr = []
    j = 0
    while i+j<len(arr) and sum(tempArr)<10884537:
        tempArr.append(arr[i+j])
        j += 1
    if sum(tempArr)==10884537:
        print(max(tempArr)+min(tempArr))