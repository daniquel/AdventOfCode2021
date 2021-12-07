
def age_fish(fishlist):
    new_fishes = []
    for elem in range(0, len(fishlist)):
        if fishlist[elem] == 0: #New fish!
            new_fishes.append(8)
            fishlist[elem] = 6
        else:
            fishlist[elem] = fishlist[elem] - 1

    fishlist = fishlist + new_fishes
    return fishlist

def check_days(days, initial_list):

    fish_list = initial_list
    for d in range (0, days):
        print(d)
        fish_list = age_fish(fish_list)

    return fish_list


def read_fish_list(inputfile):
    with open(inputfile, 'r') as file:
        s = file.read()
    lines = [int(x) for x in s.split(',')]
    return lines


if __name__ == '__main__':
    # input_file = 'testinput.txt'
    input_file = 'input.txt'
    days = 256

    fish_list = read_fish_list(input_file)
    final_fish_list = check_days(days, fish_list)
    print(len(final_fish_list))
