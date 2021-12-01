filename = "input.txt"
testinput = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


# Function to read the input from the input file
def read_input():
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines


# Solution to the first part of the challenge
def part1():
    lines = read_input()

    # Set the count and first measurement
    count = 0
    prev_measurement = lines[0]

    # Loop through all measurements starting from the second element in the list
    for measurement in lines[1:]:
        # If the current measurement is bigger than the previous measurement
        if int(measurement) > int(prev_measurement):
            count = count + 1
        prev_measurement = measurement

    return count


# Solution to the second part of the challenge
def part2():
    # Get input
    lines = read_input()

    # Get combined measurements:
    first = lines[0]
    second = lines[1]
    comb_measurements = []

    for element in lines[2:]:
        sum = int(first) + int(second) + int(element)
        comb_measurements.append(sum)
        first = second
        second = element

    # Determine if current window is larger than previous
    prev_window = comb_measurements[0]
    count = 0
    for window in comb_measurements[1:]:
        if window > prev_window:
            count = count + 1
        prev_window = window

    return count


# Main method to execute
if __name__ == '__main__':
    print("Result Part 1:", part1())
    print("Result Part 2:", part2())


