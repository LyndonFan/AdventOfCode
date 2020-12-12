f = open("2017/06.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split("\t")]
print(arr)

seen = []
cycles = 0
while not(arr in seen):
    seen.append([x for x in arr])
    i = arr.index(max(arr))
    c = arr[i]
    arr[i] = 0
    print(i,c)
    if c>=len(arr):
        m = c//len(arr)
        for j in range(len(arr)):
            arr[j] += m
        c -= m*len(arr)
    while c>0:
        i = (i+1)%len(arr)
        arr[i] += 1
        c -= 1
    cycles += 1
    print(arr)
print(cycles)
print(len(seen) - seen.index(arr))
