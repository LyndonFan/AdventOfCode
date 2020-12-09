f = open("2020/07.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split("\n")]

bagRules = {}

for r in arr:
    r = r.split(" contain ")
    bag = r[0][:-5]
    back = r[1]
    if "no other" in back:
        bagRules[bag] = []
    else:
        back = back.split(" ")
        toAdd = []
        for i in range(len(back)//4):
            toAdd.append([back[4*i+1]+" "+back[4*i+2],int(back[4*i])])
        bagRules[bag] = toAdd

res = 0

# print(bagRules.keys())

def canHave(bag):
    isOkay = False
    if not(bag in bagRules): return False
    print(bagRules[bag])
    for b,num in bagRules[bag]:
        if b=="shiny gold":
            return True
        isOkay = isOkay or canHave(b)
    return isOkay

# part a)
# for b in bagRules:
#     if canHave(b):
#         print(b)
#         res += 1
# print(res)

def countBags(bag):
    c = 1
    for b,num in bagRules[bag]:
        c += countBags(b)*num
    return c

print(countBags("shiny gold")-1)