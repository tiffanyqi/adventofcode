farthest = 0
dictionary = {
    'ne': 0,
    'se': 0,
    'n': 0,
    'nw': 0,
    'sw': 0,
    's': 0
}
paths = []
with open('input.txt') as inputfile:
    for line in inputfile:
        for direction in line.split(','):
            paths.append(direction)

for path in paths:
    dictionary[path] += 1

s = dictionary['s'] - dictionary['n']
sw = dictionary['sw'] - dictionary['ne']
nw = dictionary['nw'] - dictionary['se']

print s + sw
