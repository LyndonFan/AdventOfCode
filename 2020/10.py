f = open("2020/10.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split("\n")]

arr.sort()
arr = [0] + arr
arr.append(arr[-1]+3)

# part a)
dists = [0,0,0,0]
for i in range(1,len(arr)):
    dists[arr[i]-arr[i-1]] += 1
print(dists)
print(dists[1]*dists[3])

# part b)
counts = [1]
for i in range(1,len(arr)):
    c = 0
    for j in range(1,4):
        if i-j>=0 and arr[i]-arr[i-j]<=3:
            c += counts[i-j]
    counts.append(c)
print(counts[-1])
