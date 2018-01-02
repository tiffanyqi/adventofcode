lines = []
with open('input.txt') as inputfile:
    for line in inputfile:
        lines.append(line.strip().split('\n'))

total = 0
for line in lines:
    line = line[0].split(' ')
    if sorted(line) == sorted(list(set(line))):
        total += 1
print total
