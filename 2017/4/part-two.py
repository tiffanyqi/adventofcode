lines = []
with open('input.txt') as inputfile:
    for line in inputfile:
        lines.append(line.strip().split('\n'))

total = 0
for line in lines:
    line = line[0].split(' ')
    words = []
    for word in line:
        words.append(''.join(sorted(word)))

    if sorted(words) == sorted(list(set(words))):
        total += 1

print total
