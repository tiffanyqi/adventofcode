long_number = ''
with open('num.txt') as inputfile:
    for line in inputfile:
        long_number = line.strip().split(',')[0]

total = 0
prev_char = ''
for char in long_number:
    if char == prev_char:
        total += int(char)
    prev_char = char

print total + 5
