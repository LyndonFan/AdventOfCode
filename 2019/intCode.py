def intCode(inpArr,inputs = [], start = 0):
    arr = [x for x in inpArr]
    outputs = []
    pointer = start
    while arr[pointer]%100!=99:
        op = arr[pointer]
        if op%100==1 or op%100==2:
            a = arr[pointer+1] if (op//100)%10 else arr[arr[pointer+1]] 
            b = arr[pointer+2] if (op//1000)%10 else arr[arr[pointer+2]]
            pos = arr[pointer+3]
            arr[pos] = (a+b) if op%100==1 else (a*b)
            pointer += 4
        elif op%100==3:
            try:
                inp = inputs.pop(0)
                pos = arr[pointer+1]
                arr[pos] = inp
                pointer += 2
            except:
                print("Ran out of inputs")
                return arr, outputs, pointer
        elif op%100==4:
            pos = arr[pointer+1]
            outputs.append(arr[pos])
            pointer += 2
        elif op%100==5 or op%100==6:
            para = arr[pointer+1] if (op//100)%10 else arr[arr[pointer+1]]
            pos = arr[pointer+2] if (op//1000)%10 else arr[arr[pointer+2]]
            if (op%100==5 and para!=0) or (op%100==6 and para==0):
                pointer = pos
            else:
                pointer += 3
        elif op%100==7 or op%100==8:
            a = arr[pointer+1] if (op//100)%10 else arr[arr[pointer+1]] 
            b = arr[pointer+2] if (op//1000)%10 else arr[arr[pointer+2]]
            pos = arr[pointer+3]
            arr[pos] = (int) ((a<b) if op%100==7 else (a==b))
            pointer += 4
        else:
            raise AssertionError("Unseen opcode: "+str(op))
        print(arr)
        print(pointer)
    return arr, outputs