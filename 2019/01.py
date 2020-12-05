f = open("2019/01.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split("\n")]

# part a)
# print(sum(x//3 - 2 for x in arr))

def recurFuel(x):
    return 0 if x<=0 else max(0,x//3 - 2)+recurFuel(x//3-2)

print(sum(recurFuel(x) for x in arr))