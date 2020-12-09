inp = ".^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^."

maze = [inp]
while len(maze)<400000: # 40 for part a)
    newRow = ""
    for i in range(len(maze[0])):
        l = "." if i==0 else maze[-1][i-1]
        c = maze[-1][i]
        r = "." if i==len(maze[0])-1 else maze[-1][i+1]
        if l+c+r in ["^^.",".^^","^..","..^"]:
            newRow += "^"
        else:
            newRow += "."
    maze.append(newRow)
print(sum(r.count(".") for r in maze))
