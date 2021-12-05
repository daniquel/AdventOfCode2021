import re
import numpy as np

def load_input(filename):
    with open(filename, 'r') as file:
        s = file.read()
    lines = s.splitlines()

    straight_lines = []
    diagonal_lines = []
    for line in lines:
        x1, y1, x2, y2 = re.split(' -> |,', line)
        if int(x1) == int(x2) or int(y1) == int(y2):
            straight_lines.append([(int(x1), int(y1)), (int(x2), int(y2))])
        else:
            diagonal_lines.append([(int(x1), int(y1)), (int(x2), int(y2))])

    return straight_lines, diagonal_lines


def add_line_to_board(board, line):
    (x1, y1), (x2, y2) = line
    if x1 < x2 and y1 == y2:
        for x_point in range(x1, x2 + 1):
            board[x_point][y1] = board[x_point][y1] + 1
    elif x2 < x1 and y1 == y2:
        for x_point in range(x2, x1 + 1):
            board[x_point][y1] = board[x_point][y1] + 1
    elif y1 < y2 and x1 == x2:
        for y_point in range(y1, y2 + 1):
            board[x1][y_point] = board[x1][y_point] + 1
    else: #y2 > y2 and x1 == x2:
        for y_point in range(y2, y1 + 1):
            board[x1][y_point] = board[x1][y_point] + 1
    return board

def add_diag_to_board(board, line):
    (x1, y1), (x2, y2) = line
    zipped = []
    if x1 < x2:
        x_points = list(range(x1, x2 + 1))
        y_points = list(range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1))
        if y1 > y2:
            y_points.reverse()

        zipped = list(zip(x_points, y_points))
    elif x2 < x1:
        x_points = list(range(x2, x1 + 1))
        y_points = list(range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1))
        if y2 > y1:
            y_points.reverse()

        zipped = list(zip(x_points, y_points))

    for (x, y) in zipped:
        board[x][y] = board[x][y] + 1

    return board


def get_count_overlap(board):
    locations = np.where(board >= 2)
    return len(locations[0])


if __name__ == '__main__':
    # inputfile = "testinput.txt"
    inputfile = "input.txt"
    straight, diagonal = load_input(inputfile)
    all = straight + diagonal
    # print(straight)
    max_value = max(int(max(all, key = lambda i: i[1][1])[1][1]) + 1, int(max(all, key = lambda i: i[0][0])[0][0]) + 1)

    board = np.zeros((max_value, max_value), dtype=int)
    # print(board)

    # Add all straight lines to the board
    for elem in straight:
        add_line_to_board(board, elem)

    print(diagonal)
    # Add all diagonal lines to the board
    for elem in diagonal:
        add_diag_to_board(board, elem)

    # print(np.transpose(board))

    print(get_count_overlap(board))