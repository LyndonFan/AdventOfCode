def q9a(inp):
    data = inp.split('\n')
    risk = 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            is_risky = True
            for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if 0 <= x < len(data) and 0 <= y < len(data[0]) and int(data[x][y]) <= int(data[i][j]):
                    is_risky = False
            if is_risky:
                risk += 1 + int(char)
    return risk


def q9b(inp):
    data = inp.split('\n')
    risk = 0
    low_points = []
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            is_risky = True
            for x, y in [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]:
                if 0 <= x < len(data) and 0 <= y < len(data[0]) and int(data[x][y]) <= int(data[i][j]):
                    is_risky = False
            if is_risky:
                low_points.append((i, j))
    basin = {pt: set([pt]) for pt in low_points}
    for i, j in low_points:
        lvl = int(data[i][j])+1
        while lvl < 9:
            old_basin = [p for p in basin[(i, j)]]
            for i_new, j_new in old_basin:
                for x, y in [(i_new, j_new+1), (i_new, j_new-1), (i_new+1, j_new), (i_new-1, j_new)]:
                    if 0 <= x < len(data) and 0 <= y < len(data[0]) and int(data[x][y]) <= lvl:
                        basin[(i, j)].add((x, y))
            lvl += 1

    # visualize basins
    # basin_string = [["." for _ in range(len(data[0]))]
    #                 for _ in range(len(data))]
    # for k, pt in enumerate(low_points):
    #     for i, j in basin[pt]:
    #         basin_string[i][j] = chr(ord('A')+k)
    # for line in basin_string:
    #     print("".join(line))
    ###

    low_points.sort(key=lambda pt: len(basin[pt]), reverse=True)
    print([(pt, len(basin[pt])) for pt in low_points][:10])
    return len(basin[low_points[0]]) * len(basin[low_points[1]]) * len(basin[low_points[2]])


if __name__ == "__main__":
    with open("09.txt", "r") as f:
        # with open("09test.txt", "r") as f:
        data = f.read().strip()
    print(q9b(data))
