from knot_hash import create_knot_hash

puzzle_input = 'hxtvlmkl'
num = 128
array = [puzzle_input + '-' + str(i) for i in xrange(num)]
total = 0

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

for inp in array:
    hexadecimal = create_knot_hash(inp)
    result = []
    for char in hexadecimal:
        for num in hex_to_bit[char]:
            result.append(num)
    total += sum(result)

print total
