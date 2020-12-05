count = 0
for pw in range(264360,746325+1):
    pw = str(pw)
    isOkay = True
    for i in range(5):
        isOkay = isOkay and int(pw[i])<=int(pw[i+1])
    if isOkay:
        isOkay = False
        for i in range(5):
            # isOkay = isOkay or pw[i]==pw[i+1] # part a)
            isOkay = isOkay or (pw[i]==pw[i+1] and ((i==4) or pw[i+1]!=pw[i+2]) and ((i==0) or pw[i]!=pw[i-1]))
    count += isOkay

print(count)