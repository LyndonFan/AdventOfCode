f = open("2020/04.txt","r")
inp = f.read()
f.close()
arr = [x for x in inp.split('\n\n')]

res = 0
reqs = "byr iyr eyr hgt hcl ecl pid".split(" ")
for p in arr:
    p = p.replace(" ","\n").split("\n")
    ps = {}
    for trib in p:
        t = trib.split(":")
        ps[t[0]] = t[1]
    isOkay = True
    for r in reqs:
        if isOkay and r in ps:
            if r=="byr":
                isOkay = isOkay and len(ps[r])==4 and ps[r].isnumeric() and int(ps[r])>=1920 and int(ps[r])<=2002
            elif r=="iyr":
                isOkay = isOkay and len(ps[r])==4 and ps[r].isnumeric() and int(ps[r])>=2010 and int(ps[r])<=2020
            elif r=="eyr":
                isOkay = isOkay and len(ps[r])==4 and ps[r].isnumeric() and int(ps[r])>=2020 and int(ps[r])<=2030
            elif r=="pid":
                isOkay = isOkay and len(ps[r])==9 and ps[r].isnumeric()
            elif r=="ecl":
                isOkay = isOkay and ps[r] in "amb blu brn gry grn hzl oth".split(" ")
            elif r=="hgt":
                isOkay = isOkay and len(ps[r])>=2 and ps[r][-2:] in ["cm","in"]
                if isOkay:
                    num = ps[r][:-2]
                    if ps[r][-2:]=="cm":
                        isOkay = num.isnumeric() and int(num)>=150 and int(num)<=193
                    elif ps[r][-2:]=="in":
                        isOkay = num.isnumeric() and int(num)>=59 and int(num)<=76
            elif r=="hcl":
                isOkay = isOkay and len(ps[r])==7 and ps[r][0]=="#"
                for i in range(1,7):
                    isOkay = isOkay and ps[r][i] in "1234567890abcdef"
        else:
            isOkay = False
    if isOkay:
        print(ps)
    res += isOkay

print(res)