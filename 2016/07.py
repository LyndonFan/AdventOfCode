f = open("2016/07.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

def hasABBA(s):
    ans = False
    for i in range(len(s)-3):
        ans = ans or (s[i]==s[i+3] and s[i+1]==s[i+2] and s[i]!=s[i+1])
    return ans

count = 0
# for r in arr:
#     r = r.replace("["," ").replace("]"," ").split(" ")
#     isOkay = False
#     for i in range(0,len(r),2):
#         isOkay = isOkay or hasABBA(r[i])
#     for i in range(1,len(r),2):
#         isOkay = isOkay and not(hasABBA(r[i]))
#     if isOkay:
#         print(r)
#     count += isOkay

for r in arr:
    r = r.replace("["," ").replace("]"," ").split(" ")
    outside = r[::2]
    inside = r[1::2]
    isOkay = False
    for s in outside:
        for i in range(len(s)-2):
            a = s[i]
            b = s[i+1]
            if s[i]==s[i+2]:
                for t in inside:
                    isOkay = isOkay or b+a+b in t
    count += isOkay
print(count)