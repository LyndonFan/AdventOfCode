f = open("2020/11.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

# grid = [r for r in arr]
# prevGrid = []

# count = 0
# while (grid != prevGrid):
#     prevGrid = grid
#     newGrid = []
#     for i in range(len(grid)):
#         temp = ""
#         for j in range(len(grid[0])):
#             if grid[i][j] in "L#":
#                 occu = 0

                if grid[i][j]=="L" and occu==0:
                    temp += "#"
                elif grid[i][j]=="#" and occu>=4:
                    temp += "L"
                else:
                    temp += grid[i][j]
#             else:
#                 temp += grid[i][j]
#         newGrid.append(temp)
#     grid = newGrid
#     count += 1

# print(count)
# print(sum(r.count("#") for r in grid))


grid = [r for r in arr]
prevGrid = []

count = 0
while (grid != prevGrid):
    prevGrid = grid
    newGrid = []
    for i in range(len(grid)):
        temp = ""
        for j in range(len(grid[0])):
            if grid[i][j] in "L#":
                occu = 0
                # for part a)
                # for k in [-1,0,1]:
                #     for l in [-1,0,1]:
                #         if not(k==0 and l==0) and 0<=i+k<len(grid) and 0<=j+l<len(grid[0]):
                #             occu += grid[i+k][j+l]=="#"
                for dir in [(-1,1),(-1,0),(-1,-1),(0,1),(0,-1),(1,0),(1,-1),(1,1)]:
                    x = i + dir[0]
                    y = j + dir[1]
                    # alt for part a): just comment out this while loop!
                    while 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==".":
                        x += dir[0]
                        y += dir[1]
                    if 0<=x<len(grid) and 0<=y<len(grid[0]):
                        occu += grid[x][y]=="#"
                if grid[i][j]=="L" and occu==0:
                    temp += "#"
                elif grid[i][j]=="#" and occu>=5:   # 4 for part a)
                    temp += "L"
                else:
                    temp += grid[i][j]
            else:
                temp += grid[i][j]
        newGrid.append(temp)
    grid = newGrid
    count += 1

print(count)
print(sum(r.count("#") for r in grid))