f = open("2017/08.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

reg = {}
maxVal = 0
for r in arr:
    r = r.split(" ")
    instn = r[:3]
    cond = r[-3:]
    if not (instn[0] in reg):
        reg[instn[0]] = 0
    if not (cond[0] in reg):
        reg[cond[0]] = 0
    cond[0] = "reg[\""+cond[0]+"\"]"
    cond = " ".join(cond)
    if eval(cond):
        reg[instn[0]] += int(r[2]) * (1 if r[1]=="inc" else -1)
    maxVal = max(maxVal, max(reg.values()))
print(maxVal)   # just max(reg.values()) here for part a)