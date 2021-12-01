import copy

f = open("2020/20.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n\n")]

print(len(arr))
n = int(len(arr)**0.5)
info = {}
seenBorders = {}
for r in arr:
	r = r.split("\n")
	name, ts = r[0], r[1:]
	borders = {"0":list(ts[0]), "2":list(ts[-1])[::-1]}
	borders["1"] = [row[-1] for row in ts]
	borders["3"] = [row[0] for row in ts]
	for i in range(4):
		borders[str(i)+"f"] = borders[str(i)][::-1]
	for b in borders:
		borders[b] = "".join(borders[b])
	tid = int(name[5:-1])
	info[tid] = {"tile":ts, "borders": borders}
	for k in borders:
	   		s = borders[k]
	   		try:
	   			seenBorders[s].append((tid,k))
	   		except:
	   			seenBorders[s] = [(tid,k)]

idCount = {tid: 0 for tid in info}
for s in seenBorders:
	if len(seenBorders[s]) + len(seenBorders[s[::-1]])==2:
		# print(s, seenBorders[s])
		tid = seenBorders[s][0][0]
		idCount[tid] += 1

res = 1
for tid in idCount:
	if idCount[tid]==4:
		print(tid)
		res *= tid
print(res)

dirs = [(0,-1),(1,0),(0,1),(-1,0)]

def rotate(ts):
	tileLength = len(ts)
	return ["".join(ts[x][tileLength-1-y] for x in range(tileLength)) for y in range(tileLength)]

def orient(ts,ori):
	newTs = copy.deepcopy(ts)
	for _ in range(int(ori[0])):
		newTs = rotate(newTs)
	if "f" in ori:
		return [r[::-1] for r in newTs]
	return newTs

def convert(idm):
	y = 0
	res = []
	while y < len(idm) and idm[y].count((0,"-1")) < len(idm[y]):
		x = 0
		for _ in range(10):
			res.append("")
		while x < len(idm) and idm[y][x]!=(0,"-1"):
			tid, ori = idm[y][x]
			ts = info[tid]['tile']
			ts = orient(ts, ori)
			for i in range(10):
				res[-10+i] += ts[i] + "|"
			x += 1
		res.append("-"*len(res[-1]))
		y += 1
	return res

matchOriMap = {}
for i,d in enumerate(dirs):
	for k in range(4):
		matchOriMap[(d,str(k))] = str((k+2-i)%4)
		matchOriMap[(d,str(k)+"f")] = str((k-2+i)%4)+"f"

used = set([1091])
idMap = [[(0,"-1") for _ in range(n)] for _ in range(n)]
idMap[0][0] = (1091,"2")

logf = open("2020/20log.txt","r")
oris = logf.read().split(",")
while "" in oris:
	oris.pop(oris.index(""))
logf.close()
logf = open("2020/20log.txt","a")

while any((0,"-1") in r for r in idMap):
	for y in range(n):
		for x in range(n):
			if idMap[y][x] != (0,"-1"):
				tid,ori = idMap[y][x]
				print(x,y,tid,ori)
				print(info[tid])
				for d in dirs:
					if 0<=x+d[0]<n and 0<=y+d[1]<n and idMap[y+d[1]][x+d[0]]==(0,"-1"):
						edgeId = int(ori[0])
						edgeId += dirs.index(d) * (-1 if "f" in ori else 1)
						edgeId = edgeId%4
						edgeId = str(edgeId) + ori[1:]
						edge = info[tid]['borders'][edgeId]
						edge = edge[::-1]
						print(d,"".join(edge))
						possTiles = seenBorders[edge]
						for pt in possTiles:
							if pt[0]==tid or pt[0] in used:
								possTiles.pop(possTiles.index(pt))
						if len(possTiles)==1:
							newTId, corrEdgeId = possTiles[0]
							if len(oris)>0:
								corrEdgeId = oris.pop(0)
							else:
								for r in convert(idMap):
									print(r)
								print("New tile at",(x+d[0],y+d[1]))
								print("\n".join(convert([[(newTId,"0")]])))
								corrEdgeId = input()
								logf.write(","+corrEdgeId)
							used.add(newTId)
							idMap[y+d[1]][x+d[0]] = (newTId, corrEdgeId)
							print(x+d[0], y+d[1], (newTId, matchOriMap[(d,corrEdgeId)]))
						else:
							print(possTiles)
							print(seenBorders[edge])
							print(seenBorders[edge[::-1]])
							exit()

outf = open("2020/20out.txt","w+")
outf.write("\n".join(convert(idMap)))
outf.close()
