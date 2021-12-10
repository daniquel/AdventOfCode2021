import math

def read_lines(inputfile):
    with open(inputfile) as file:
        return file.read().splitlines()

def directions(x, y, w, h):
    if x - 1 >= 0:
        yield x - 1, y
    if x + 1 < w:
        yield x + 1, y
    if y - 1 >= 0:
        yield x, y - 1
    if y + 1 < h:
        yield x, y + 1

if __name__ == '__main__':

    lines = read_lines("input.txt")

    grid = [list(map(int, line)) for line in lines]
    w, h = len(grid[0]), len(grid)

    lows = []
    for x in range(w):
        for y in range(h):
            v = grid[y][x]

            for xx, yy in directions(x, y, w, h):
                if grid[yy][xx] <= v:
                    break
            else:
                lows.append((x, y))


    def dfs(x, y, v, been):
        if (x, y) in been or v == 9:
            return
        else:
            been.add((x, y))

        for xx, yy in directions(x, y, w, h):
            if grid[yy][xx] <= v:
                continue
            else:
                dfs(xx, yy, grid[yy][xx], been)


    sizes = []
    for x, y in lows:
        been = set()
        dfs(x, y, grid[y][x], been)
        sizes.append(len(been))

    sizes.sort()

    print(math.prod(sizes[-3:]))