
def q3a(data):
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        count0 = sum(x[i] == '0' for x in data)
        count1 = len(data) - count0
        gamma += "0" if count0 > count1 else "1"
        epsilon += "1" if count0 > count1 else "0"
    return int(gamma, 2) * int(epsilon, 2)


def q3b(data):
    xs = [x for x in data]
    i = 0
    oxygen = ""
    while len(xs) > 1:
        count0 = sum(x[i] == '0' for x in xs)
        count1 = len(xs) - count0
        if count1 >= count0:
            xs = [x for x in xs if x[i] == '1']
        else:
            xs = [x for x in xs if x[i] == '0']
        i += 1
    oxygen = xs[0]
    xs = [x for x in data]
    i = 0
    co2 = ""
    while len(xs) > 1:
        count0 = sum(x[i] == '0' for x in xs)
        count1 = len(xs) - count0
        if count0 <= count1:
            xs = [x for x in xs if x[i] == '0']
        else:
            xs = [x for x in xs if x[i] == '1']
        i += 1
    co2 = xs[0]
    print(oxygen, co2)
    return int(oxygen, 2) * int(co2, 2)


if __name__ == "__main__":
    with open("3.txt", "r") as f:
        data = f.read().split("\n")
    print(q3b(data))
