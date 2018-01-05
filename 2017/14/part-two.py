from knot_hash import create_knot_hash

puzzle_input = 'hxtvlmkl'

output = [
    [1, 1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1, 0]
]
    # [1,  1,  0,  2,  0, 3, 0, 0],
    # [0,  1,  0,  2,  0, 3, 0, 4],
    # [0,  0,  0,  0,  5, 0, 6, 0],
    # [10, 0,  11, 0,  5, 5, 0, 7],
    # [0,  11, 11, 0,  5, 0, 0, 0],
    # [11, 11, 0,  0,  5, 0, 0, 8],
    # [0,  11, 0,  0,  0, 9, 0, 0],
    # [11, 11, 0,  12, 0, 9, 9, 0]

hex_to_bit = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'a': [1, 0, 1, 0],
    'b': [1, 0, 1, 1],
    'c': [1, 1, 0, 0],
    'd': [1, 1, 0, 1],
    'e': [1, 1, 1, 0],
    'f': [1, 1, 1, 1],
}


def create_output(puzzle_input):
    output = []
    num = 128
    array = [puzzle_input + '-' + str(i) for i in xrange(num)]

    for inp in array:
        hexadecimal = create_knot_hash(inp)
        result = []
        for char in hexadecimal:
            for num in hex_to_bit[char]:
                result.append(num)
        output.append(result)
    return output


def transform(output):
    """
    0100
    1101
    0110
    becomes
    1->5
    4->5
    5->1,4,9
    7->7
    9->5,10
    10->9
    """
    num = 0
    group_to_value = {}
    for x_i, x in enumerate(output):
        for y_i, y in enumerate(x):
            if y == 1:
                group_to_value[num] = find_connections(output, x_i, y_i, num)
            num += 1
    return group_to_value


def find_connections(output, x, y, num):
    connections = []
    size = len(output)
    try:
        if output[x-1][y] == 1 and x - 1 >= 0:
            connections.append(num-size)
    except IndexError:
        pass

    try:
        if output[x+1][y] == 1:
            connections.append(num+size)
    except IndexError:
        pass

    try:
        if output[x][y-1] == 1 and y - 1 >= 0:
            connections.append(num-1)
    except IndexError:
        pass

    try:
        if output[x][y+1]:
            connections.append(num+1)
    except IndexError:
        pass

    if connections == []:
        return [num]
    return connections


def calculate(dictionary):
    """
    using hint from reddit, using algorithm from day 12
    """
    num_groups = 0
    contains = []

    for i in range(128*128):
        try:
            dictionary[i]
            if i not in contains:
                num_groups += 1

                contains_num = [i]
                for j in range(50):
                    for group, array in dictionary.iteritems():
                        if i != group:
                            if i in array:
                                contains_num.append(group)
                            if group in contains_num:
                                for value in array:
                                    contains_num.append(value)
                for num in set(contains_num):
                    contains.append(num)
        except KeyError:
            pass

    return num_groups

print calculate(transform(create_output(puzzle_input)))
