filename = "input.txt"
# filename = "testinput.txt"


# Function to read the input from the input file
def read_input():
    with open(filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
    return lines

def part1():

    lines = read_input()
    print(len(lines[0]))
    count = []
    gammarate = ""
    epsilonrate = ""
    for i in range(0,len(lines[0])):
        for elem in lines:
            count.append(elem[i])

        if count.count('1') > count.count('0'):
            gammarate = gammarate + '1'
            epsilonrate = epsilonrate + '0'
        else:
            gammarate = gammarate + '0'
            epsilonrate = epsilonrate + '1'

        count = []

    gamm = int(gammarate, 2)
    eps = int(epsilonrate,2)

    print("Power consumption:")
    print(gamm * eps)

def get_most_used(elements, index):
    count = {0: [], 1: []}
    for elem in elements:
        if elem[index] == '0':
            count[0].append(elem)
        else:  # elem[i] == '1':
            count[1].append(elem)

    if len(count[0]) > len(count[1]):
        return count[0]
    else:
        return count[1]

def get_least_used(elements, index):
    count = {0: [], 1: []}
    for elem in elements:
        if elem[index] == '0':
            count[0].append(elem)
        else:  # elem[i] == '1':
            count[1].append(elem)

    if len(count[1]) >= len(count[0]):
        return count[0]
    else:
        return count[1]

def part2():
    lines = read_input()
    oxy = 0
    co2 = 0

    # newlines = []
    # for elem in lines:
    #     newlines.append(elem[0])
    length = len(lines[0])
    for i in range(0, length):
        curr_lines = get_most_used(lines, i)
        lines = curr_lines

        if len(curr_lines) == 1:
            oxy = int(curr_lines[0],2)

    lines = read_input()
    for i in range(0, length):
        curr_lines = get_least_used(lines, i)
        lines = curr_lines

        if len(curr_lines) == 1:
            co2 = int(curr_lines[0],2)

    return oxy, co2



# Main method to execute
if __name__ == '__main__':
    oxy, co2 = part2()
    print(oxy * co2)
