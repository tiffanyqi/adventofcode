program = []
dictionary = {}
times_mul = 0
with open('input.txt') as inputfile:
    for line in inputfile:
        program.append(line.strip().split('\n'))

index = 0
while index <= len(program):
    p = program[index][0].split(' ')
    op = p[0]
    letter = p[1]

    try:
        dictionary[letter]
    except KeyError:
        dictionary[letter] = 0

    value = p[2]
    try:
        value = int(value)
    except ValueError:
        value = int(dictionary[value])

    if op == 'set':
        dictionary[letter] = value
    elif op == 'sub':
        dictionary[letter] -= value
    elif op == 'mul':
        dictionary[letter] *= value
        times_mul += 1
    elif op == 'jnz' and dictionary[letter] != 0:
        index += value - 1

    index += 1
    print index, p[0], value, dictionary

print times_mul
