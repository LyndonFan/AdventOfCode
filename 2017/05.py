f = open("2017/05.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split("\n")]

res = 0
i = 0
while i < len(arr):
    change = -1 if arr[i]>=3 else 1 # just 1 in a)
    arr[i] += change
    i += arr[i]-change
    res += 1

print(res)