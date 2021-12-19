# day 14 solutions

"""
--- Day 14: Extended Polymerization ---The incredible pressures at this depth are starting to put a strain on your submarine. The submarine has polymerization equipment that would produce suitable materials to reinforce the submarine, and the nearby volcanically-active caves should even have the necessary input elements in sufficient quantities.
The submarine manual contains instructions for finding the optimal polymer formula; specifically, it offers a polymer template and a list of pair insertion rules (your puzzle input). You just need to work out what polymer would result after repeating the pair insertion process a few times.
For example:
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

The first line is the polymer template - this is the starting point of the process.
The following section defines the pair insertion rules. A rule like AB -> C means that when elements A and B are immediately adjacent, element C should be inserted between them. These insertions all happen simultaneously.
So, starting with the polymer template NNCB, the first step simultaneously considers all three pairs:

The first pair (NN) matches the rule NN -> C, so element C is inserted between the first N and the second N.
The second pair (NC) matches the rule NC -> B, so element B is inserted between the N and the C.
The third pair (CB) matches the rule CB -> H, so element H is inserted between the C and the B.

Note that these pairs overlap: the second element of one pair is the first element of the next pair. Also, because all pairs are considered simultaneously, inserted elements are not considered to be part of a pair until the next step.
After the first step of this process, the polymer becomes NCNBCHB.
Here are the results of a few steps using the above rules:
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

This polymer grows quickly. After step 5, it has length 97; After step 10, it has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H occurs 161 times, and N occurs 865 times; taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.
Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

"""
from tqdm import tqdm


def q14a(inp):
    data = inp.split("\n")
    polymer = data[0]
    rules = data[2:]
    rules = {x.split(" ")[0]: x.split(" ")[2] for x in rules}
    print(polymer)
    print(len(rules))
    for _ in range(10):
        new_polymer = ""
        for i in range(len(polymer)):
            if polymer[i:i+2] in rules:  # i=-1 --> not in rules
                new_polymer += polymer[i] + \
                    rules[polymer[i:i+2]]
            else:
                new_polymer += polymer[i]
        polymer = new_polymer
        print(len(polymer))
    counts = {c: polymer.count(c) for c in set(polymer)}
    print(counts)
    return counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)]


def q14b(inp):
    data = inp.split("\n")
    polymer = data[0]
    rules = data[2:]
    rules = {x.split(" ")[0]: x.split(" ")[2] for x in rules}
    print(polymer)
    pair_counts = {}
    for i in range(len(polymer)-1):
        try:
            pair_counts[polymer[i:i+2]] += 1
        except KeyError:
            pair_counts[polymer[i:i+2]] = 1

    front_char = polymer[0]
    back_char = polymer[-1]

    for _ in range(40):
        new_pair_counts = {}
        for pair in pair_counts:
            if pair in rules:
                c = rules[pair]
                fp, bp = pair[0]+c, c+pair[1]
                try:
                    new_pair_counts[fp] += pair_counts[pair]
                except KeyError:
                    new_pair_counts[fp] = pair_counts[pair]
                try:
                    new_pair_counts[bp] += pair_counts[pair]
                except KeyError:
                    new_pair_counts[bp] = pair_counts[pair]
            else:
                try:
                    new_pair_counts[pair] += pair_counts[pair]
                except KeyError:
                    new_pair_counts[pair] = pair_counts[pair]
        pair_counts = new_pair_counts

    counts = {c: 0 for p in pair_counts for c in p}
    for pair in pair_counts:
        counts[pair[0]] += pair_counts[pair]
        counts[pair[1]] += pair_counts[pair]
    counts[front_char] += 1
    counts[back_char] += 1
    for c in counts:
        counts[c] = counts[c]//2
    return counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)]


if __name__ == "__main__":
    with open("14test.txt", "r") as f:
        data = f.read().strip()
    print("Testing  (a):", q14a(data))
    print("Expected (a):", 1588)
    print("Testing  (b):", q14b(data))
    print("Expected (b):", 2188189693529)
    with open("14.txt", "r") as f:
        data = f.read().strip()
    print("Actual   (a): ", q14a(data))
    print("Actual   (b): ", q14b(data))
