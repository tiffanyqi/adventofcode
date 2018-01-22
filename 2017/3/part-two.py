input = 325489
array = [[0 for x in range(10)] for y in range(10)]
start = 1
x = 4
y = 4
row = 1
count = 1
num = 2
direction = 'right'


def same_direction(direction):
    global x
    global y
    if direction == 'right':
        y += 1
    elif direction == 'left':
        y -= 1
    elif direction == 'up':
        x -= 1
    elif direction == 'down':
        x += 1
    return direction


def change_direction(direction):
    if direction == 'right':
        direction = 'up'
    elif direction == 'up':
        direction = 'left'
    elif direction == 'left':
        direction = 'down'
    elif direction == 'down':
        direction = 'right'
    return direction


def add_to_array(start, direction):
    global x
    global y
    global array
    global count

    array[x][y] = start
    direction = same_direction(direction)
    start = array[x+1][y] + array[x-1][y] + array[x][y+1] + array[x][y-1] + array[x+1][y+1] + array[x-1][y-1] + array[x-1][y+1] + array[x+1][y-1]
    count += 1
    return start


while start < input:
    loop_count = 0
    while row > loop_count:
        start = add_to_array(start, direction)
        loop_count += 1

        if start > input:
            print start
            break

    if count == num**2:
        start = add_to_array(start, direction)
        num += 1
        row += 1

    direction = change_direction(direction)
