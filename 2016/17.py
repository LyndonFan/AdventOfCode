import hashlib

def md5(x):
    return hashlib.md5(x.encode()).hexdigest()

inp = "njfxhljp"

stack = [(0,0,"")]
units = [[0,-1],[0,1],[-1,0],[1,0]]
dirs = "UDLR"
hasArrived = False
maxLen = 0
# while not hasArrived: # path a)
while len(stack)>0:
    x,y,path = stack.pop(0)
    if x==3 and y==3:
        # hasArrived = True
        maxLen = max(len(path),maxLen)
    else:
        h = md5(inp+path)
        for i in range(4):
            if h[i] in "bcdef":
                newX = x + units[i][0]
                newY = y + units[i][1]
                if 0<=newX<4 and 0<=newY<4:
                    stack.append([newX,newY,path+dirs[i]])
# print(path) # part a)
print(maxLen)