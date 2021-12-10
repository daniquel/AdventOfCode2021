from collections import defaultdict, Counter

def read_lines(inputfile):
    with open(inputfile) as file:
        return file.read().splitlines()


if __name__ == '__main__':
    # inputfile = "testinput.txt"
    inputfile = "input.txt"
    lines = read_lines(inputfile)


    count = Counter()

    openingcharacters = ['{', '(', '[', '<']
    closingcharacters = ['}', ')', ']', '>']

    scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}

    pairs = [("{", "}"), ("(", ")"), ("[", "]"), ("<", ">")]

    numbers = {")": 1, "]": 2, "}": 3, ">": 4}

    total_score = 0
    for line in lines:
        opened = []
        print(line)
        for c in line:
            if c in openingcharacters:
                opened.append(c)
            else:
                i = openingcharacters.index(opened.pop())
                if c != closingcharacters[i]:
                    print(c)
                    total_score += scoring[c]
                    break

    print(total_score)