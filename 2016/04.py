f = open("2016/04.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

count = 0

allchars = "abcdefghijklmnopqrstuvwxyz"
alpha = list("abcdefghijklmnopqrstuvwxyz")

for r in arr:
    head, checksum = r.split("[")
    checksum = list(checksum[:-1])
    head = head.split("-")
    secID = int(head[-1])
    head = "".join(head[:-1])
    alpha.sort(key = lambda x: (-head.count(x),x))
    print(alpha[:5],checksum)
    if alpha[:5]==checksum:
        count += secID
        newString = r.split("[")[0]
        for i in range(26):
            newString = newString.replace(allchars[i],allchars[(i+secID)%26].upper())
        print(secID, newString)
print(count)

# ['h', 'm', 'x', 'k', 'a'] ['h', 'm', 'x', 'k', 'a']
# 267 NORTHPOLE-OBJECT-STORAGE-267