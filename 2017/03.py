inp = 361527

# part a)

# n = 0
# while (2*n+1)**2<=inp:
#     n += 1
# n -= 1
# pos = [n+1,-n]

# num = (2*n+1)**2+1
# print("Going up")
# for _ in range(-n,n+2):
#     num += 1
#     pos[1] += 1
#     if num==inp:
#         print(pos)
#         print(sum(abs(x) for x in pos))
#         exit()
# print("Going left")
# for _ in range(-n+1,n+2):
#     num += 1
#     pos[0] -= 1
#     if num==inp:
#         print(pos)
#         print(sum(abs(x) for x in pos))
#         exit()
# print("Going down")
# for _ in range(-n,n+2):
#     num += 1
#     pos[1] -= 1
#     if num==inp:
#         print(pos)
#         print(sum(abs(x) for x in pos))
#         exit()
# print("Going right")
# for _ in range(-n+1,n+2):
#     num += 1
#     pos[0] += 1
#     if num==inp:
#         print(pos)
#         print(sum(abs(x) for x in pos))
#         exit()

pos = (0,0)
n = 0
vals = {(0,0):1}
while vals[pos]<=inp:
    x,y = pos
    if pos == (n,-n):
        pos = (n+1,-n)
        n += 1
    elif x==n and y<n:
        pos = (x,y+1)
    elif y==n and x>-n:
        pos = (x-1,y)
    elif x==-n and y>-n:
        pos = (x,y-1)
    elif y==-n and x<n:
        pos = (x+1,y)
    x,y = pos
    newVal = sum(sum(vals[(x+i,y+j)] if (x+i,y+j) in vals else 0 for j in range(-1,2)) for i in range(-1,2))
    # print(" ".join(" ".join(str((x+i,y+j)) if (x+i,y+j) in vals else "" for j in range(-1,2)) for i in range(-1,2)))
    vals[pos] = newVal
print(pos,vals[pos])
maxLen = len(str(vals[pos]))
# for i in range(-n,n+1):
#     print(" ".join(
#         str(vals[(i,j)]).rjust(maxLen) if (i,j) in vals else (" "*maxLen)
#     for j in range(-n,n+1)))