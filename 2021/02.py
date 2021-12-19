def q2a(data):
    horizontal_position = 0
    depth = 0
    for instruction in data:
        n = int(instruction.split(" ")[1])
        if instruction[0] == 'f':
            horizontal_position += n
        elif instruction[0] == 'd':
            depth += n
        elif instruction[0] == 'u':
            depth -= n
    return horizontal_position * depth


def q2b(data):
    horizontal_position = 0
    depth = 0
    aim = 0
    for instruction in data:
        n = int(instruction.split(" ")[1])
        if instruction[0] == 'f':
            horizontal_position += n
            depth += n * aim
        elif instruction[0] == 'd':
            aim += n
        elif instruction[0] == 'u':
            aim -= n
    return horizontal_position * depth


if __name__ == "__main__":
    with open("2.txt", "r") as f:
        data = f.read().split("\n")
    print(q2b(data))
