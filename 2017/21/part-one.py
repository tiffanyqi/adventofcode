rules = []  # with input
pixel_grid = [
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#']
]
iterations = 2
with open('input.txt') as inputfile:
    for line in inputfile:
        to_add = line.strip().split('\n')[0]
        rules.append(to_add)

"""
1. break up the pixel grid into pieces
2. take each piece and enhance it
3. put them back together
4. do this multiple times
"""


def modify(pixel_grid, pieces):
    size = len(pixel_grid)
    # for y in pixel_grid:
    #     for x in pixel_grid:

    # break_up(pixel_grid, pieces)
    enhance(pixel_grid)

    return pixel_grid


def enhance(pixel_grid):
    return 'hi'


for i in range(iterations):
    size = len(pixel_grid)
    if size % 2 == 0:
        pixel_grid = modify(pixel_grid, 2)
    elif size % 3 == 0:
        pixel_grid = modify(pixel_grid, 3)

print len(pixel_grid)
