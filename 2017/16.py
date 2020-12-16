f = open("2017/16.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split(',')]

dancers = list("abcdefghijklmnop")

seen = []
# part a)
for r in arr:
    if r[0]=="s":
        k = int(r[1:])
        dancers = dancers[-k:] + dancers[:-k]
    elif r[0]=="x":
        i,j = [int(x) for x in r[1:].split("/")]
        dancers[i], dancers[j] = dancers[j], dancers[i]
    else:
        i,j = [dancers.index(x) for x in r[1:].split("/")]
        dancers[i], dancers[j] = dancers[j], dancers[i]

# part b) can't brute force...

# if dancers in seen:
#     i = seen.index(dancers)
#     m = k-i+1
#     res = seen[i + (10000000-i)%m]
#     print("".join(res))
#     exit()
# seen.append(dancers)
# print(len(seen))
# if k%10000==0:
#     print(k//10000)



# oneIter = list("pkgnhomelfdibjac")
# move = {i:dancers.index(oneIter[i]) for i in range(len(dancers))}

# print(list(range(len(dancers))))
# print(move)

print("".join(dancers))