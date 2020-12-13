f = open("2017/11.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split(",")]

dirs = "n ne se s sw nw".split(" ")

def count(s):
    i = 0
    while list(s.values()).count(0)<4:
        if s[dirs[i]] >= s[dirs[(i+3)%6]]:
            s[dirs[i]] -= s[dirs[(i+3)%6]]
            s[dirs[(i+3)%6]] = 0
        else:
            s[dirs[(i+3)%6]] -= s[dirs[i]]
            s[dirs[i]] = 0
        for k in [2,-2]:
            if s[dirs[i]] >= s[dirs[(i+k)%6]]:
                s[dirs[i]] -= s[dirs[(i+k)%6]]
                s[dirs[(i+k//2)%6]] += s[dirs[(i+k)%6]]
                s[dirs[(i+k)%6]] = 0
            else:
                s[dirs[(i+k)%6]] -= s[dirs[i]]
                s[dirs[(i+k//2)%6]] += s[dirs[i]]
                s[dirs[i]] = 0
        i += 1
    return sum(s.values())

steps = {d:arr.count(d) for d in dirs}
print(count(steps))

steps = {d:0 for d in dirs}
maxDist = 0
for d in arr:
    steps[d] += 1
    maxDist = max(count(steps),maxDist)
print(maxDist)
        