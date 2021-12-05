import numpy as np


def get_boards(lines, n=5):
    # Get n * n boards from lines of strings containing integers
    boards = []
    for l in lines:
        if l == '':
            continue # We skip the empty lines
        boards.append(l.split())
    num_boards = int(len(boards)//5)

    #Reshape so first axis contains each board:
    return np.reshape(boards, (num_boards, n, n)).astype(int)


def load_input(filename):
    # Load the input file
    with open(filename, 'r') as file:
        s = file.read()
    lines = s.splitlines()
    draws = list(map(int, lines[0].split(',')))
    return draws, get_boards(lines[1:])


# Check if a board has bingo
def find_bingo(boards):
    rows = (boards.sum(axis=1) == 0).any(axis=1)
    cols = (boards.sum(axis=2) == 0).any(axis=1)
    return rows | cols


# Calculate the score from a board
def calculate_score(draw, board):
    return draw * board.sum()

# Score board which finishes in position 'pos'. Assumes the first board in the array finishing at that position
# in the event of a tie
def score_board(draws, boards, pos=0):
    num_boards = len(boards)
    rank = - pos if pos < 0 else num_boards - pos # from 1 to num_boards

    if rank <= 0 or rank > num_boards:
        # Invalid position
        raise ValueError(f"Position '{pos}' out of range for {num_boards} boards")

    for draw in draws:
        boards[boards == draw] = 0 # Strike off draw from boards
        bingo = find_bingo(boards)
        if bingo.any():
            if len(bingo) == rank:
                break # Calculate the score of board at given rank
            elif len(bingo) < rank:
                # If there is a tie somewhere
                raise ValueError(f"No board finished in position {pos}.")
            boards = boards[~bingo] # Discard the boards with bingo

    return calculate_score(draw, boards[bingo][0]) # Assume first board


if __name__ == '__main__':
    # inputfile = "testinput.txt"
    inputfile = "input.txt"
    draws, boards = load_input(inputfile)

    best_score = score_board(draws, boards, pos=0)
    worst_score = score_board(draws, boards, pos=99)
    print(f'Best Score = {best_score}')
    print(f'Worst Score = {worst_score}')


