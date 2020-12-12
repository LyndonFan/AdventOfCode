import hashlib

inp = "jlmsuwbz"

# part a)
# k = 0
# keys = []
# while len(keys)<64:
#     h = hashlib.md5((inp+str(k)).encode()).hexdigest()
#     i = 0
#     while i<len(h)-3 and not(h[i]==h[i+1] and h[i+1]==h[i+2]):
#         i += 1
#     if i<len(h)-3:
#         j = 1
#         c = h[i]
#         isOkay = False
#         while j<=1000 and not(isOkay):
#             newH = hashlib.md5((inp+str(k+j)).encode()).hexdigest()
#             isOkay = isOkay or c*5 in newH
#             j += 1
#         if isOkay:
#             keys.append(k)
#     k += 1
# print(keys)
# print(keys[63])

# doesn't work for part b) for some reason...
hashes = []
for k in range(27000):
    h = inp+str(k)
    for _ in range(2017):
        h = hashlib.md5(h.encode()).hexdigest()
    if inp=="abc" and k==0:
        print(h)
    i = 0
    while i<len(h)-3 and not(h[i]==h[i+1] and h[i+1]==h[i+2]):
        i += 1
    if h[i]==h[i+1] and h[i+1]==h[i+2]:
        hashes.append((k,h[i],h))
print(hashes)
keys = []
while len(hashes)>0 and len(keys)<64:
    k,c,h = hashes.pop(0)
    # print(k,c,h)
    i = 0
    isOkay = False
    while not(isOkay) and i<len(hashes) and hashes[i][0]-k<=1000:
        isOkay = c*5 in hashes[i][2]
        i += 1
    if isOkay:
        # print(k,c,h,hashes[i-1][2])
        keys.append(k)
print(keys)
print(len(keys), keys[-1])

# ans is not 22453 or 22668...