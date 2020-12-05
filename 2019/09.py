f = open("2019/09.txt","r")
inp = f.read()
f.close()
arr = [int(x) for x in inp.split(",")]

def intCode(inpArr,inputs = []):
    global pointer
    arr = {i:inpArr[i] for i in range(len(inpArr))}
    outputs = []
    relbase = 0
    pointer = 0
    print(arr)

    def process(mode,isLastPos = False):
        global pointer
        pointer += 1
        if mode==0:
            pointTo = arr[pointer]
        elif mode==1:
            pointTo = pointer
        elif mode==2:
            pointTo = arr[pointer] + relbase
        else:
            raise AssertionError("Mode should be 0,1,2: "+str(mode))
        if not(pointTo in arr):
            arr[pointTo] = 0
        print(mode, pointer, pointTo, arr[pointTo])
        return pointTo if isLastPos else arr[pointTo]

    while arr[pointer]%100!=99:
        op = arr[pointer]
        if op%100 in [1,2,7,8]:
            a = process((op//100)%10)
            b = process((op//1000)%10)
            pos = process((op//10000)%10, True)
            options = {1:a+b, 2:a*b, 7: (int)(a<b), 8: (int)(a==b)}
            print(a,b,pos)
            arr[pos] = options[op%100]
            pointer += 1
        elif op%100==3:
            pointer += 1
            pos = arr[pointer]
            print("Input",inputs[0],"used")
            arr[pos] = inputs.pop()
            pointer += 1
        elif op%100==4:
            val = process(op//100,True)
            outputs.append(arr[val])
            pointer += 1
            print("Outputs:",outputs)
        elif op%100==5 or op%100==6:
            para = process((op//100)%10)
            pos = process((op//1000)%10)
            if (op%100==5 and para!=0) or (op%100==6 and para==0):
                pointer = pos
            else:
                pointer += 1
        elif op%100==9:
            para = process((op//100)%10)
            relbase += para
            pointer += 1
            print("Relbase is now",relbase)
        else:
            raise AssertionError("Unseen opcode: "+str(op))
        if not(pointer in arr):
            arr[pointer] = 0
        print(arr)
        print(pointer)
    return arr, outputs

# arr = [104,1125899906842624,99]

resarr, out = intCode(arr,[1])
print(out)
