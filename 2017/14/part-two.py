from knot_hash import create_knot_hash

puzzle_input = 'hxtvlmkl'
num = 8
array = [puzzle_input + '-' + str(i) for i in xrange(num)]
output = []
regions = 0

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


def is_edge(i, j):
    return i == 0 or j == 0 or i == (num-1) or j == (num-1)


def add_regions(i, j):
    global regions
    regions += 1

# for inp in array:
#     hexadecimal = create_knot_hash(inp)
#     result = []
#     for char in hexadecimal:
#         for num in hex_to_bit[char]:
#             result.append(num)
#     output.append(result)

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

for i, array in enumerate(output):
    for j, num in enumerate(array):

        if num == 1:
            print i, j

            # if is_edge(i, j):

            if i == 0:
                down = output[i][j+1]
                if j == 0:
                    right = output[i+1][j]
                    if right == 0 and down == 0:
                        add_regions(i, j)

                elif j == (num-1):
                    left = output[i][j-1]
                    if left == 0 and down == 0:
                        add_regions(i, j)

                else:
                    left = output[i][j-1]
                    right = output[i+1][j]
                    if left == 0 and down == 0 and right == 0:
                        add_regions(i, j)

            elif i == (num-1):
                up = output[i-1][j]
                if j == 0:
                    right = output[i][j+1]
                    if right == 0 and up == 0:
                        add_regions(i, j)

                elif j == (num-1):
                    left = output[i][j-1]
                    if left == 0 and up == 0:
                        add_regions(i, j)

                else:
                    left = output[i][j+1]
                    right = output[i][j-1]
                    if left == 0 and right == 0 and up == 0:
                        add_regions(i, j)

            elif j == 0:
                down = output[i][j+1]
                if i == 0:
                    right = output[i+1][j]
                    if right == 0 and down == 0:
                        add_regions(i, j)

                elif i == (num-1):
                    left = output[i-1][j]
                    if left == 0 and down == 0:
                        add_regions(i, j)

                else:
                    left = output[i-1][j]
                    right = output[i+1][j]
                    if left == 0 and down == 0 and right == 0:
                        add_regions(i, j)

            elif j == (num-1):
                up = output[i][j-1]
                if i == 0:
                    right = output[i+1][j]
                    if right == 0 and up == 0:
                        add_regions(i, j)

                elif i == (num-1):
                    left = output[i-1][j]
                    if left == 0 and up == 0:
                        add_regions(i, j)

                else:
                    left = output[i-1][j]
                    right = output[i+1][j]
                    if left == 0 and right == 0 and up == 0:
                        add_regions(i, j)

            else:
                left = output[i-1][j]
                right = output[i+1][j]
                up = output[i][j-1]
                down = output[i][j+1]
                if left == 0 and right == 0 and up == 0 and down == 0:
                    add_regions(i, j)

print regions
