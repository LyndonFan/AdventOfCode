inp = 369

lis = [0]
i = 0
vals = []
for k in range(1,500+1):   # 2017+1 for part a)
    i = (i+inp)%len(lis)
    lis.insert(i+1,k)
    i = i+1
    if k%100000==0:
        print(k//100000)
    vals.append(lis[lis.index(0)+1])


# i = lis.index(0)
# print(lis[i-1:i+2])

print(vals)
# for k in range(500):
#     print((inp*k*(k+1)//2))