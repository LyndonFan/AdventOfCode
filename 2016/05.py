import hashlib

inp = "ffykfhsq"

# part a)
# pw = ""
# i = 0
# while len(pw)<8:
#     res = hashlib.md5((inp+str(i)).encode())
#     if res.hexdigest()[:5]=="00000":
#         print(res.hexdigest())
#         pw += str(res.hexdigest()[5])
#     i += 1
# print(pw)

pw = [" "]*8
i = 0
while pw.count(" ")>0:
    res = hashlib.md5((inp+str(i)).encode())
    if res.hexdigest()[:5]=="00000":
        print(res.hexdigest())
        if res.hexdigest()[5].isnumeric() and int(res.hexdigest()[5])<8 and pw[int(res.hexdigest()[5])]==" ":
            pw[int(res.hexdigest()[5])] = str(res.hexdigest()[6])
            print(pw)
    i += 1
print(pw)