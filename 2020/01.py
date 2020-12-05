f = open("2020/01.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split('\n')]

for i in range(len(arr)-2):
    for j in range(i,len(arr)-1):
        for k in range(j,len(arr)):
            if arr[i]+arr[j]+arr[k]==2020:
                print(arr[i]*arr[j]*arr[k])