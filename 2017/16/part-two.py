program = ''
with open('input.txt') as inputfile:
    for line in inputfile:
        program = line.split(',')

lineup = 'abcdefghijklmnop'
looped = 0

dictionary = {}
values = []


def swap(lineup, first, second):
    positions = sorted([first, second])
    first = positions[0]
    second = positions[1]

    lineup = lineup[0:first] + lineup[second] + lineup[first+1:second] + lineup[first] + lineup[second+1:]
    return lineup

for i in range(0, 1000):
    for group in program:
        instruction = group[0]

        if instruction == 's':
            size = len(lineup)-int(group[1:])
            lineup = lineup[size:] + lineup[0:size]

        elif instruction == 'x':
            swaps = group[1:].split('/')
            first_pos = int(swaps[0])
            second_pos = int(swaps[1])
            lineup = swap(lineup, first_pos, second_pos)

        elif instruction == 'p':
            swaps = group[1:].split('/')
            first_pos = lineup.index(swaps[0])
            second_pos = lineup.index(swaps[1])
            lineup = swap(lineup, first_pos, second_pos)

    try:
        if dictionary[lineup]:
            looped = i-1
            break
    except KeyError:
        dictionary[lineup] = i
        values.append(lineup)


print values[(1000000000 % looped)-1]
