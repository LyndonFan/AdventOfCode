f = open("2016/08.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

screen = [[False for _ in range(50)] for _ in range(6)]

def show():
    for row in screen:
        print("".join("#" if c else "." for c in row))
    print("-"*len(screen[0]))

for r in arr:
    show()
    if r[:4] == "rect":
        w,h = [int(x) for x in r[5:].split("x")]
        for i in range(h):
            for j in range(w):
                screen[i][j] = True
    else:
        d = r[7]
        coor, shift = [int(x) for x in r.split("=")[1].split(" by ")]
        if d=="c":
            newcol = [screen[(i-shift)%len(screen)][coor] for i in range(len(screen))]
            for i in range(len(screen)):
                screen[i][coor] = newcol[i]
        else:
            newrow = [screen[coor][(i-shift)%len(screen[0])] for i in range(len(screen[0]))]
            for i in range(len(screen[0])):
                screen[coor][i] = newrow[i]
show()
print(sum(sum(r) for r in screen))

