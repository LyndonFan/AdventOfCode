f = open("2020/15.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split('\n')]

arr = [2,20,0,4,1,17]
seen = {arr[i]: i for i in range(len(arr))}

while len(arr)<30000000:    # 2020 for part a)
    if arr[-1] not in seen:
        arr.append(0)
        seen[arr[-2]] = len(arr)-2
    else:
        if len(arr)<10: print(seen)
        k = len(arr)-1
        arr.append(k-seen[arr[-1]])
        seen[arr[-2]] = k
    
print(arr[:10])
print(arr[-1])