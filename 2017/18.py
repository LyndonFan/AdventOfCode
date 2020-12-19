f = open("2017/18.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

# reg = {}
# i = 0
# while True:
#     cmd = arr[i].split(" ")
#     if not(cmd[1] in reg):
#         reg[cmd[1]] = 0
#     if cmd[0]=="set":
#         reg[cmd[1]] = reg[cmd[2]] if cmd[2] in reg else int(cmd[2])
#     elif cmd[0]=="add":
#         reg[cmd[1]] += reg[cmd[2]] if cmd[2] in reg else int(cmd[2])
#     elif cmd[0]=="mul":
#         reg[cmd[1]] *= reg[cmd[2]] if cmd[2] in reg else int(cmd[2])
#     elif cmd[0]=="mod":
#         reg[cmd[1]] = reg[cmd[1]] % (reg[cmd[2]] if cmd[2] in reg else int(cmd[2]))
#     elif cmd[0]=="jgz":
#         if reg[cmd[1]]>0:
#             i += -1 + (reg[cmd[2]] if cmd[2] in reg else int(cmd[2]))
#     elif cmd[0]=="rcv":
#         if reg[cmd[1]]!=0:
#             print(reg["snd"])
#             exit()
#     elif cmd[0]=="snd":
#         reg["snd"] = reg[cmd[1]]
#     i += 1
#     print(i)

regs = [{'p':0},{'p':1}]
indicies = [0,0]
sendCount = [0,0]
queues = [[],[]]
isWaiting = [False, False]
while True:
    for k in [0,1]:
        i = indicies[k]
        cmd = arr[i].split(" ")
        if not(cmd[1] in regs[k] or cmd[1].isnumeric()):
            regs[k][cmd[1]] = 0
        if cmd[0]=="set":
            regs[k][cmd[1]] = regs[k][cmd[2]] if cmd[2] in regs[k] else int(cmd[2])
        elif cmd[0]=="add":
            regs[k][cmd[1]] += regs[k][cmd[2]] if cmd[2] in regs[k] else int(cmd[2])
        elif cmd[0]=="mul":
            regs[k][cmd[1]] *= regs[k][cmd[2]] if cmd[2] in regs[k] else int(cmd[2])
        elif cmd[0]=="mod":
            regs[k][cmd[1]] = regs[k][cmd[1]] % (regs[k][cmd[2]] if cmd[2] in regs[k] else int(cmd[2]))
        elif cmd[0]=="jgz":
            if (cmd[1].isnumeric() and int(cmd[1])>0) or regs[k][cmd[1]]>0:
                i += -1 + (regs[k][cmd[2]] if cmd[2] in regs[k] else int(cmd[2]))
        elif cmd[0]=="rcv":
            if len(queues[k])==0:
                isWaiting[k] = True
                i -= 1
            else:
                isWaiting[k] = False
                regs[k][cmd[1]] = queues[k].pop(0)
        elif cmd[0]=="snd":
            queues[1-k].append(regs[k][cmd[1]] if cmd[1] in regs[k] else int(cmd[1]))
            sendCount[k] += 1
        i += 1
        indicies[k] = i
        print(i)
    if all(isWaiting):
        print(sendCount)
        exit()