tubes = []
letters = ''
steps = 0

x = 0  # up and down
y = 163  # left and right
end = False
direction = 'down'

with open('input.txt') as inputfile:
    for line in inputfile:
        line = line.split('\n')[0]
        add = []
        for char in line:
            add.append(char)
        tubes.append(add)


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


def change_direction(direction):
    global x
    global y
    if tubes[x+1][y] != ' ' and direction != 'up':  # go down
        x += 1
        direction = 'down'
    elif tubes[x-1][y] != ' ' and direction != 'down':  # go up
        x -= 1
        direction = 'up'
    elif tubes[x][y+1] != ' ' and direction != 'left':  # go right
        y += 1
        direction = 'right'
    elif tubes[x][y-1] != ' ' and direction != 'right':  # go left
        y -= 1
        direction = 'left'
    return direction

while not end:
    symbol = tubes[x][y]
    if symbol == '|':
        direction = same_direction(direction)
    elif symbol == '-':
        direction = same_direction(direction)
    elif symbol == '+':
        direction = change_direction(direction)
    elif symbol == ' ':
        end = True
    else:  # a letter
        letters += symbol
        direction = same_direction(direction)
    steps += 1

print letters  # part one
print steps-1  # part two
