import math


def determine_fuel_part2(position, crablist):
    count = 0
    for crab in crablist:
        if crab != position:
            n = abs(crab - position)
            fuel = (n * (n+1)) / 2
            count = count + fuel
    return count


def determine_fuel(position, crablist):
    count = 0
    for crab in crablist:
        if crab != position:
            fuel = abs(crab - position)
            count = count + fuel
    return count


def try_all_positions(crablist):
    sum = math.inf
    for i in range (min(crablist), max(crablist)):
        count = determine_fuel_part2(i, crablist)
        if count < sum:
            sum = count

    return sum


def load_input(input_file):
    with open(input_file, 'r') as file:
        s = file.read()
    lines = [int(x) for x in s.split(',')]
    return lines


if __name__ == '__main__':
    # input_file = "testinput.txt"
    input_file = "input.txt"
    input = load_input(input_file)
    print(try_all_positions(input))
