infections = 0
direction = 'up'
cycles = 10000
key = []
with open('input.txt') as inputfile:
    for line in inputfile:
        to_add = line.strip().split('\n')[0]
        collect = []
        for item in to_add:
            collect.append(item)
        key.append(collect)


def make_array(key):
    length = cycles
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

array = make_array(key)
x = len(array)/2
y = len(array)/2
for i in range(cycles):
    state = array[x][y]
    if state == '#':
        array[x][y] = '.'
        direction = turn_right(direction)
    elif state == '.':
        array[x][y] = '#'
        direction = turn_left(direction)
        infections += 1

print infections
