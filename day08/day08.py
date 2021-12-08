import itertools

def read_input(input_file):
    outputfirst = []
    outputsecond = []
    with open(input_file, 'r') as file:
        s = file.readlines()
    for line in s:
        first, second = (line.rstrip("\n")).split(' | ')
        outputfirst = outputfirst + first.split(' ')
        outputsecond = outputsecond + second.split(' ')
    print(outputfirst)
    print(outputsecond)
    return outputfirst, outputsecond

def get_number_of_unique_digits(list):
    count = 0
    for elem in list:
        if len(elem) in [2, 4, 3, 7]:
            count = count + 1
    return count

def substitute(pattern: str, mapping: dict[str, str]) -> str:
    """
    Substitute each character in pattern with the corresponding value in mapping and sort alphabetically
    Args:
        pattern: The pattern to substitute.
        mapping: The mapping to use.
    Returns:
        The substituted pattern.
    """
    return "".join(sorted(mapping[char] for char in pattern))


def data(input_file):
    total = 0
    patterns = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }

    with open(input_file, 'r') as file:
        s = file.read().splitlines()

    for line in s:
        ten_patterns, four_digits = line.split(" | ")
        ten_patterns = ten_patterns.split(" ")
        four_digits = four_digits.split(" ")

        # Find which of the patterns each corresponds to:
        perms = itertools.permutations("abcdefg")
        for perm in perms:
            mapping = dict(zip(perm, "abcdefg"))
            reverse_mapping = {v: k for k , v in mapping.items()}

            #substitute each pattern with the corresponding value
            decoded_set = set (
                substitute(pattern, mapping) for pattern in patterns.keys()
            )
            ten_pattern_set = set("".join(sorted(pattern)) for pattern in ten_patterns)

            if decoded_set == ten_pattern_set:
                # determine which digits each pattern corresponds to:
                output = "".join(patterns[substitute(digit, reverse_mapping)] for digit in four_digits)
                total += int(output)

    print(total)

if __name__ == '__main__':
    # inputfile = "testinput.txt"
    inputfile = "input.txt"
    # input, output = read_input(inputfile)
    # count = get_number_of_unique_digits(output)
    # print(count)
    data(inputfile)