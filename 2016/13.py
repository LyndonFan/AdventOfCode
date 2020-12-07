inp = 1350

def isWall(x,y):
    n = x*x + 3*x + 2*x*y + y + y*y + inp
    n = bin(n)[2:]
    return sum(int(x) for x in n)%2==1

maze = []

for y in range(51):
    maze.append([isWall(x,y) for x in range(51)])

seen = [(1,1)]
stack = [((1,1),0)]
while True:
    print(stack)
    pos, d = stack.pop(0)
    # part a)
    # if pos==[39,31]:
    #     print(d)
    #     exit()
    # part b)
    if d==50:
        print(len(set(seen)))
        exit()
    for dir in [[0,1],[1,0],[0,-1],[-1,0]]:
        y,x = pos[0]+dir[0], pos[1]+dir[1]
        if not((y,x) in seen) and 0<=y<len(maze) and 0<=x<len(maze[0]) and not(maze[y][x]):
            stack.append(((y,x),d+1))
            seen.append((y,x))
    for y in range(51):
        print("".join("*" if (y,x) in seen else ("#" if maze[y][x] else ".") for x in range(51)))
    print("-"*51)
