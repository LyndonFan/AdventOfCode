f = open("2020/08.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

# part a)
# instructions = list(zip(range(len(arr)),arr))
# seen = []
# i = 0
# val = 0
# while True:
#     r = arr[i]
#     if (i,r) in seen:
#         print(val)
#         exit()
#     else:
#         seen.append((i,r))
#         r = r.split(" ")
#         if r[0]=="nop":
#             i += 1
#         elif r[0]=="jmp":
#             i += int(r[1])
#         else:
#             val += int(r[1])
#             i += 1
#         print(i,val)


for j in range(len(arr)):
    row = arr[j]
    if row[:3] in ["nop","jmp"]:
        newInstruction = ("nop" if row[:3]=="jmp" else "jmp")+row[3:]
        newarr = [newInstruction if k==j else arr[k] for k in range(len(arr))]
        hasRepeat = False
        instructions = list(zip(range(len(newarr)),newarr))
        seen = []
        i = 0
        val = 0
        while not(hasRepeat) and i < len(arr):
            r = newarr[i]
            if (i,r) in seen:
                hasRepeat = True
                # print(val)
                # exit()
            else:
                seen.append((i,r))
                r = r.split(" ")
                if r[0]=="nop":
                    i += 1
                elif r[0]=="jmp":
                    i += int(r[1])
                else:
                    val += int(r[1])
                    i += 1
                # print(i,val)
        if not(hasRepeat):
            print(val)


