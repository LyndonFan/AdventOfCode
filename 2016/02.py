f = open("2016/02.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

res = ""
# buttons = "123\n456\n789".split("\n") # part a)
buttons = "  1  \n 234 \n56789\n ABC \n  D  ".split("\n")
start = [2,0] # [1,1] # part a)
unitVectors = {"R":(0,1),"D":(1,0),"L":(0,-1),"U":(-1,0)}

for r in arr:
    for c in r:
        newPos = [start[i]+unitVectors[c][i] for i in [0,1]]
        # if 0<=newPos[0]<=2 and 0<=newPos[1]<=2: # part a)
        if abs(newPos[0]-2)+abs(newPos[1]-2)<=2 and 0<=newPos[0]<=4 and 0<=newPos[1]<=4:
            start = newPos
    res += str(buttons[start[0]][start[1]])
print(res)