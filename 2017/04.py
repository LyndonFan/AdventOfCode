f = open("2017/04.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

count = 0
for pw in arr:
    pw = pw.split(" ")
    pw = ["".join(sorted(x)) for x in pw] # part b) only
    count += len(pw) == len(set(pw))
print(count)