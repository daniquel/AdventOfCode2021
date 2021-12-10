import math

def read_lines(inputfile):
    with open(inputfile) as file:
        return file.read().splitlines()


def directions(x, y, w, h):
    if x - 1 >= 0:
        yield x-1, y
    if x + 1 < w:
        yield x+1, y
    if y - 1 >= 0:
        yield x, y-1
    if y + 1 < h:
        yield x, y+1

def part_1():
    lines = read_lines("input.txt")

    matrix = [list(map(int, line)) for line in lines]
    w, h = len(matrix[0]), len(matrix)

    total = 0
    for x in range(w):
        for y in range(h):
            v = matrix[y][x]

            for xx, yy in directions(x, y, w, h):
                if matrix[yy][xx] <= v:
                    break
            else:
                total += v + 1

    print(total)



def part_2():
    lines = read_lines("input.txt")

    matrix = [list(map(int, line)) for line in lines]
    w, h = len(matrix[0]), len(matrix)

    lows = []
    for x in range(w):
        for y in range(h):
            v = matrix[y][x]

            for xx, yy in directions(x, y, w, h):
                if matrix[yy][xx] <= v:
                    break
            else:
                lows.append((x, y))


    sizes = []
    for x, y in lows:
        been = set()
        dfs(x, y, matrix[y][x], been, matrix)
        sizes.append(len(been))

    sizes.sort()

    print(math.prod(sizes[-3:]))

if __name__ == '__main__':
    part_2()
