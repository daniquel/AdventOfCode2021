
def read_input_into_matrix(input_file):
    with open(input_file, 'r') as f:
        l = [[int(num) for num in list(line.replace("\n", ''))] for line in f]
    return l

def directions(x, y, w, h):
    if x - 1 >= 0:
        yield x - 1, y
    if x + 1 < w:
        yield x + 1, y
    if y - 1 >= 0:
        yield x, y - 1
    if y + 1 < h:
        yield x, y + 1

def get_low_points(matrix):
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

    return total


if __name__ == '__main__':
    inputfile = "testinput.txt"
    matrix = read_input_into_matrix(inputfile)


    print(get_low_points(matrix))
    # total = 0
    # for x in range(w):
    #     for y in range(h):
    #         v = grid[y][x]
    #
    #         for xx, yy in dirs(x, y, w, h):
    #             if grid[yy][xx] <= v:
    #                 break
    #         else:
    #             total += v + 1
    #
    # print(total)