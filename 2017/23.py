f = open("2017/23.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

reg = {c:0 for c in "abcdefgh"}
reg['a'] = 1
i = 0
mulCount = 0
while i<len(arr):
    cmd = arr[i].split(" ")
    if not(cmd[1] in reg):
        reg[cmd[1]] = int(cmd[1]) if cmd[1].isnumeric() else 0
    if cmd[0]=="set":
        reg[cmd[1]] = reg[cmd[2]] if cmd[2] in reg else int(cmd[2])
    elif cmd[0]=="mul":
        reg[cmd[1]] *= reg[cmd[2]] if cmd[2] in reg else int(cmd[2])
        mulCount += 1
    elif cmd[0]=="sub":
        reg[cmd[1]] -= reg[cmd[2]] if cmd[2] in reg else int(cmd[2])
    elif cmd[0]=="jnz":
        if reg[cmd[1]]!=0:
            i += -1 + (reg[cmd[2]] if cmd[2] in reg else int(cmd[2]))
    i += 1
    print(reg)
print(mulCount)