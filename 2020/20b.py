import copy

f = open("2020/20out.txt","r")
inp = f.read()
f.close()
inp = inp.replace("-","").replace("|","")
arr = [x for x in inp.split("\n")]
while "" in arr:
    arr.pop(arr.index(""))
print(len(arr),len(arr[0]))
for i in reversed(range(12)):
    arr.pop(10*i+9)
    arr.pop(10*i)
print(len(arr),len(arr[0]))
for i in range(len(arr)):
    arr[i] = list(arr[i])
    for j in reversed(range(12)):
        arr[i].pop(10*j+9)
        arr[i].pop(10*j)
print(len(arr),len(arr[0]))

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

patternInput = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
patternInput = patternInput.split("\n")[1:]

pattern = set([])
height = len(patternInput)
width = len(patternInput[0])

for y in range(len(patternInput)):
    for x in range(len(patternInput[y])):
        if patternInput[y][x]=="#":
            pattern.add((x,y))
print(pattern)
count = 0
for k in range(4):
    for opt in ["","f"]:
        tempTs = orient(arr,str(k)+opt)
        # print(str(i)+opt)
        # print("\n".join("".join(r) for r in tempTs))
        # print("-"*len(tempTs))
        for y in range(len(arr)-height):
            for x in range(len(arr[0])-width):
                print("\n".join("".join(r[x:x+width]) for r in tempTs[y:y+height]))
                print("\n".join(patternInput))
                print("-"*width)
                hasPattern = True
                for i,j in pattern:
                    # if hasPattern and not(arr[y+j][x+i]=="#"):
                    #     print(x,y,i,j,arr[y+j][x+i])
                    hasPattern = hasPattern and tempTs[y+j][x+i]=="#"
                count += hasPattern
print(count)
print(sum(r.count("#") for r in arr) - len(pattern)*count)
