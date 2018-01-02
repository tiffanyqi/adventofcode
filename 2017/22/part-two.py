infections = 0
direction = 'up'
cycles = 10000000
key = []
with open('input.txt') as inputfile:
    for line in inputfile:
        to_add = line.strip().split('\n')[0]
        collect = []
        for item in to_add:
            collect.append(item)
        key.append(collect)


def make_array(key):
    length = cycles / 500
    array = [['.' for x in range(length)] for y in range(length)]
    key_length = len(key)
    start_index = length / 2 - key_length / 2
    x_index = start_index
    y_index = start_index
    for x in key:
        for y in x:
            array[x_index][y_index] = y
            y_index += 1
        y_index = start_index
        x_index += 1
    return array


def turn_left(direction):
    global x
    global y
    if direction == 'right':
        x -= 1
        direction = 'up'
    elif direction == 'up':
        y -= 1
        direction = 'left'
    elif direction == 'left':
        x += 1
        direction = 'down'
    elif direction == 'down':
        y += 1
        direction = 'right'
    return direction


def turn_right(direction):
    global x
    global y
    if direction == 'right':
        x += 1
        direction = 'down'
    elif direction == 'down':
        y -= 1
        direction = 'left'
    elif direction == 'left':
        x -= 1
        direction = 'up'
    elif direction == 'up':
        y += 1
        direction = 'right'
    return direction


def same_direction(direction):
    global x
    global y
    if direction == 'right':
        y += 1
    elif direction == 'up':
        x -= 1
    elif direction == 'left':
        y -= 1
    elif direction == 'down':
        x += 1
    return direction


def reverse_direction(direction):
    global x
    global y
    if direction == 'right':
        y -= 1
        direction = 'left'
    elif direction == 'up':
        x += 1
        direction = 'down'
    elif direction == 'left':
        y += 1
        direction = 'right'
    elif direction == 'down':
        x -= 1
        direction = 'up'
    return direction

array = make_array(key)
x = len(array)/2
y = len(array)/2
for i in range(cycles):
    state = array[x][y]
    if state == '.':
        array[x][y] = 'W'  # clean
        direction = turn_left(direction)
    elif state == 'W':  # weakened
        array[x][y] = '#'
        direction = same_direction(direction)
        infections += 1
    elif state == '#':  # infected
        array[x][y] = 'F'
        direction = turn_right(direction)
    elif state == 'F':  # flagged
        array[x][y] = '.'
        direction = reverse_direction(direction)

print infections
