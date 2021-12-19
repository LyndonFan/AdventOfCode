conv = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg"
]

rev_conv = {
    v: i for i, v in enumerate(conv)
}


def q8a(inp):
    data = inp.split("\n")
    count = 0
    for row in data:
        _, back = row.split(" | ")
        for l in [2, 3, 4, 7]:
            count += sum(len(x) == l for x in back.split(" "))
    return count


keys = "abcdefg"


def q8b(inp):
    data = inp.split("\n")
    res = 0
    for row in data:
        front, back = row.split(" | ")
        front = front.split(" ")
        back = back.split(" ")
        mapping = {k: set(keys) for k in keys}
        seen_lengths = set(len(x) for x in front)
        print(row)
        num_conv = ["" for _ in range(10)]
        front = list(map(set, front))
        num_conv[8] = set(keys)
        num_conv[1] = [x for x in front if len(x) == 2][0]
        num_conv[7] = [x for x in front if len(x) == 3][0]
        num_conv[4] = [x for x in front if len(x) == 4][0]
        num_conv[3] = [x for x in front if len(x) == 5
                       and num_conv[1].difference(x) == set([])][0]
        num_conv[0] = [x for x in front if len(x) == 6
                       and len(x.difference(num_conv[3])) == 2
                       and len(x.intersection(num_conv[1])) == 2][0]

        print(num_conv)

        mapping['a'] = num_conv[7].difference(num_conv[1])
        mapping['d'] = set(keys).difference(num_conv[0])
        mapping['b'] = num_conv[4].difference(mapping['d'])

        adg = set(keys).intersection(*[x for x in front if len(x) == 5])
        # print(adg)
        mapping['g'] = adg.difference(mapping['a'], mapping['d'])

        cde = set([]).union(
            *[set(keys).difference(x) for x in front if len(x) == 6])
        # print(cde)
        mapping['c'] = cde.difference(mapping['d'])
        mapping['e'] = cde.difference(mapping['d'])

        # print(mapping)

        for signal in front:
            for (l, n) in [(2, 1), (3, 7), (4, 4)]:
                if len(signal) == l:
                    for c in keys:
                        if c in conv[n]:
                            mapping[c] = mapping[c].intersection(
                                set(signal))
                        else:
                            mapping[c] = mapping[c].intersection(
                                set(keys).difference(set(signal)))
        for c in mapping:
            if len(mapping[c]) == 1:
                for c_prime in mapping:
                    if c == c_prime:
                        continue
                    mapping[c_prime] = mapping[c_prime].difference(
                        mapping[c])

        assert all(len(v) == 1 for _, v in mapping.items()), mapping
        revmap = {list(v)[0]: k for k, v in mapping.items()}
        s = ""
        for b in back:
            actual_signal = [revmap[c] for c in b]
            actual_signal.sort()
            s += str(rev_conv["".join(actual_signal)])
        res += int(s)
    return res


if __name__ == "__main__":
    with open("8.txt", "r") as f:
        # with open("8test.txt", "r") as f:
        data = f.read().strip()
    print(q8b(data))
