f = open("2018/02.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

twocounts = 0
threecounts = 0

# for boxid in arr:
#     incrementtwo = False
#     incrementthree = False
#     for c in set(boxid):
#         count = boxid.count(c)
#         incrementtwo = incrementtwo or count==2
#         incrementthree = incrementthree or count==3
#     twocounts += 1*incrementtwo
#     threecounts += 1*incrementthree
# print(twocounts * threecounts)

for i in range(len(arr)-1):
    for j in range(i,len(arr)):
        diffs = sum(arr[i][k]!=arr[j][k] for k in range(len(arr[0])))
        if diffs==1:
            print(arr[i])
            print(arr[j])
            exit()