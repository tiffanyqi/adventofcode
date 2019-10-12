frequencies = []
with open('input.txt') as inputfile:
    for line in inputfile:
        frequency = line.strip().split('\n')[0]
        frequencies.append(frequency)

start = 0
for frequency in frequencies:
    sign = frequency[0]
    number = int(frequency[1:])
    if sign == '+':
        start += number
    else:
        start -= number

print(start)
