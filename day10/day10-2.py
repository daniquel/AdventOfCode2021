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

    scores = []
    for line in lines:
        opened = []
        print(line)
        for c in line:
            if c in openingcharacters:
                opened.append(c)
            else:
                i = openingcharacters.index(opened[-1])
                if c != closingcharacters[i]:
                    break
                else:
                    opened.pop()
        else:
            ls = 0
            while opened:
                c = closingcharacters[openingcharacters.index(opened.pop())]
                ls = ls * 5 + numbers[c]
            print(ls)
            scores.append(ls)
    scores.sort()
    print(scores[len(scores)//2])