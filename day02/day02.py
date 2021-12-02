filename = "input.txt"
# filename = "testinput.txt"


# Function to read the input from the input file
def read_input():
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


# Solution to the first part of the challenge
def part1():
    lines = read_input()

    # Set initial horizontal position and depth to 0.
    hor_pos = 0
    depth = 0

    # Loop through each line and execute the action
    for line in lines:
        action, amount = line.split(" ")
        if action == "forward":
            hor_pos = hor_pos + int(amount)
        elif action == "down":
            depth = depth + int(amount)
        elif action == "up":
            depth = depth - int(amount)

    return hor_pos * depth


# Solution for the second part of the challenge
def part2():
    lines = read_input()

    # Set initial horizontal position, depth and aim to 0.
    hor_pos = 0
    depth = 0
    aim = 0

    # Loop through all lines in the input textfile and perform calculations.
    for line in lines:
        action, amount = line.split(" ")
        if action == "forward":
            hor_pos = hor_pos + int(amount)
            depth = depth + (aim * int(amount))
        elif action == "down":
            aim = aim + int(amount)
        elif action == "up":
            aim = aim - int(amount)

    return hor_pos * depth


# Main method to execute
if __name__ == '__main__':
    print(part1())
    print(part2())
