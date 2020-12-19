f = open("2017/19.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

pos = [arr[0].index("|"),0]
di = [0,1]
letters = ""
steps = 0

while arr[pos[1]][pos[0]] != " ":
    if not (arr[pos[1]][pos[0]] in "+-|"):
        letters += arr[pos[1]][pos[0]]
    if arr[pos[1]][pos[0]] == "+":
        if di[0]==0:
            di = [-1,0] if arr[pos[1]][pos[0]+1]==" " else [1,0]
        else:
            di = [0,-1] if arr[pos[1]+1][pos[0]]==" " else [0,1]
    pos = [pos[i]+di[i] for i in [0,1]]
    steps += 1
    # for i in range(len(arr)):
    #     print("".join("["+arr[i][j]+"]" if i==pos[1] and j==pos[0] else " "+arr[i][j]+" " for j in range(len(arr[i]))))
print(letters,steps)