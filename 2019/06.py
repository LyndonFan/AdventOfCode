f = open("2019/06.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

rels = {}
planets = []
for l in arr:
    l = l.split(")")
    rels[l[1]] = l[0]
    planets += l

planets = set(planets)

# part a)
# count = 0
# for p in planets:
#     curr = p
#     temp = 0
#     while curr in rels:
#         temp += 1
#         curr = rels[curr]
#     count += temp
# print(count)

def findPath(start):
    path = [start]
    curr = start
    while curr in rels:
        curr = rels[curr]
        path += [curr]
    return path[::-1]   # first is always COM

myPath = findPath("YOU")
sanPath = findPath("SAN")
while myPath[0]==sanPath[0]:
    myPath.pop(0)
    sanPath.pop(0)
print(len(myPath)+len(sanPath)-2)
        
    