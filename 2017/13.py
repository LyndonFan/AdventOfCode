f = open("2017/13.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

layers = {}
for r in arr:
    r = r.split(": ")
    layers[int(r[0])] = int(r[1])

print(sum(i*layers[i]*(i%(2*(layers[i]-1))==0) for i in layers)) # part a)

# part b)
delay = 0
while True:
    isOkay = True
    for i in layers:
        if (i+delay)%(2*(layers[i]-1))==0:
            isOkay = False
            break
    if isOkay:
        print(delay)
        exit()
    delay += 1
