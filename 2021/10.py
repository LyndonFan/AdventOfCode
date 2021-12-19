brackets = {"(": ")", "[": "]", "{": "}", "<": ">"}
rev_brackets = {v: k for k, v in brackets.items()}


def q10a(inp):
    data = inp.split('\n')

    def check_corrupt(line):
        stack = []
        for char in line:
            if char in brackets:
                stack.append(char)
            elif char in rev_brackets:
                if not stack or rev_brackets[char] != stack.pop():
                    return char
        return None

    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    s = 0
    for line in data:
        c = check_corrupt(line)
        if c:
            s += scores[c]
    return s


def q10b(inp):
    data = inp.split('\n')

    score_map = {"(": 1, ")": 1, "[": 2, "]": 2,
                 "{": 3, "}": 3, "<": 4, ">": 4}

    def autocomplete_score(line):
        stack = []
        for char in line:
            if char in brackets:
                stack.append(char)
            elif char in rev_brackets:
                if not stack or rev_brackets[char] != stack.pop():
                    return None
        s = 0
        for char in stack[::-1]:
            s = 5*s + score_map[char]
        return s

    scores = [autocomplete_score(line)
              for line in data if autocomplete_score(line)]
    scores.sort()
    # return middle score
    return scores[len(scores)//2]


if __name__ == "__main__":
    with open("10.txt", "r") as f:
        # with open("10test.txt", "r") as f:
        data = f.read().strip()
    print(q10b(data))
