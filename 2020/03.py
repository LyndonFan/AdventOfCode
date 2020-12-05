f = open("2020/03.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split('\n')]

res = 1
patterns = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for p in patterns:
    temp = 0
    print(p)
    for i in range(0,len(arr),p[1]):
        temp += arr[i][(p[0]*i//p[1])%len(arr[i])]=="#"
    print(temp)
    res *= temp

print(res)