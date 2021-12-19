from math import *


def q7a(inp):
    data = inp.split(',')
    data = [int(x) for x in data]
    data.sort()
    # counts = {p: data.count(p) for p in set(data)}
    # mean = sum(data) / len(data)
    m = len(data)//2
    lower = data[m]
    upper = data[m+1]
    if sum(abs(x-lower) for x in data) < sum(abs(x-upper) for x in data):
        print(lower)
        return sum(abs(x-lower) for x in data)
    else:
        print(upper)
        return sum(abs(x-upper) for x in data)


def q7b(inp):
    data = inp.split(',')
    data = [int(x) for x in data]
    print(min(data), max(data))
    data.sort()
    counts = {p: data.count(p) for p in set(data)}
    # mean = sum(data) / len(data)

    def evaluate(x):
        return sum(abs(x-p)*(abs(x-p)+1)//2 for p in data)
    holder = -1
    record = evaluate(-1)
    for i in range(min(data), max(data)+1):
        if evaluate(i) < record:
            record = evaluate(i)
            holder = i
    print(holder)
    return record


if __name__ == "__main__":
    with open("7.txt", "r") as f:
        # with open("7test.txt", "r") as f:
        data = f.read().strip()
    print(q7b(data))
