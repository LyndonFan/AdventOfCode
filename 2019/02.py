f = open("2019/02.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split(",")]

def intCode(inpArr):
    arr = [x for x in inpArr]
    pointer = 0
    while arr[pointer]!=99:
        op = arr[pointer]
        if op==1 or op==2:
            a = arr[arr[pointer+1]]
            b = arr[arr[pointer+2]]
            pos = arr[pointer+3]
            arr[pos] = (a+b) if op==1 else (a*b)
            pointer += 4
        else:
            raise AssertionError("Unseen opcode: "+str(op))
        # print(arr)
        # print(pointer)
    return arr

for i in range(100):
    for j in range(100):
        arr[1] = i
        arr[2] = j
        res = intCode(arr)[0]
        if res==19690720:
            print(100*i+j)
            exit()

