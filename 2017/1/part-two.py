long_number = ''
with open('num.txt') as inputfile:
    for line in inputfile:
        long_number = line.strip().split(',')[0]

total = 0
half_length = len(long_number) / 2
for index, char in enumerate(long_number[:half_length]):
    if char == long_number[index+half_length]:
        total += int(char)
print total * 2
