instructions = []
with open('input.txt') as inputfile:
    for line in inputfile:
        line = line.strip().split('\n')
        instructions.append(line)


def create_dictionary(instructions, state):
    dictionary = {}
    value_check = 0

    for i, line in enumerate(instructions):
        line = line[0].split(' ')
        if i % 10 == 0:  # in state
            state = line[2][0]
            dictionary[state] = {}
        elif i % 10 == 1 or i % 10 == 5:  # if the current value
            value_check = int(line[5][0])
            dictionary[state][value_check] = []
        elif i % 10 == 2 or i % 10 == 6:  # write the value
            value = line[4][0]
            dictionary[state][value_check].append(value)
        elif i % 10 == 3 or i % 10 == 7:  # move slot
            direction = line[6][0]
            position = 1 if direction == 'r' else -1
            dictionary[state][value_check].append(position)
        elif i % 10 == 4:  # continue with state, 0
            new_state = line[4][0]
            dictionary[state][value_check].append(new_state)
        elif i % 10 == 8:  # continue with state, 1
            new_state = line[4][0]
            dictionary[state][value_check].append(new_state)
            state = new_state

    return dictionary


def create_tape(dictionary, state, cycles):
    tape = [0 for i in range(cycles)]
    pos = len(tape)/2

    for i in range(cycles):
        directions = dictionary[state][tape[pos]]
        tape[pos] = int(directions[0])
        pos += directions[1]
        state = directions[2]

    return tape


state = 'A'
cycles = 12481997
# print create_dictionary(instructions, state)
print sum(create_tape(create_dictionary(instructions, state), state, cycles))
