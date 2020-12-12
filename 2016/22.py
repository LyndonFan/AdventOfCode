f = open("2016/22.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

# Filesystem Size Used Avail Use%
# (x)__-(y)__ Size Used Avail Use%
arr = [x.split(" ") for x in arr]
count = 0
seen = set([])
for i in range(len(arr)):
    A = arr[i]
    if int(A[2])>0:
        for j in range(len(arr)):
            if i!=j:
                B = arr[j]
                if int(A[2])<int(B[3]):
                    count += 1
                    seen.add((i,j))
print(count)
print(len(seen))

# actual values mostly don't matter
grid = [] # coordinates are [x][y]
for i in range(35):
    grid.append([])
    for j in range(27):
        row = [int(x) for x in arr[27*i+j][1:]]
        grid[-1].append(row)

res = []
for i in range(35):
    temp = ""
    for j in range(27):
        if i==34 and j==0:
            temp += "G"
        elif grid[i][j][3]>=90:
            temp += "#"
        elif grid[i][j][3]==0:
            temp += "_"
        elif grid[i][j][3]>=30:
            temp += "-"
        else:
            temp += "."
    res.append(temp)
print("\n".join(res))

# Resulting grid (transposed from original):
# ---------------------------
# -------#-------------------
# -------#-------------------
# -------#------------_------
# -------#-------------------
# ...                     ...
# -------#-------------------
# G------#-------------------

# now solve problem by inspection:
# first get blank to space just above G, then swap.
# Then go around G to get it just above G and swap.
# This gets us to the situation above but G has moved 1 step.
# So we repeat the procedure until G arrives at node (0,0).
# The total is then:
# 3 + 20 (getting _ to 0,0 initially) + 33 (getting just above G) + 1 (the swap)
# + 5 * 33 (x-coor of G after above)
# = 222