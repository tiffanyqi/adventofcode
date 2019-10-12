frequencies = []
with open('input.txt') as inputfile:
    for line in inputfile:
        frequency = line.strip().split('\n')[0]
        frequencies.append(frequency)


start = 0
reached_frequencies = [start]
freq_dict = {}

# do the calculation
for cycle in range(0, 100):
    for frequency in frequencies:
        sign = frequency[0]
        number = int(frequency[1:])
        if sign == '+':
            start += number
        else:
            start -= number

        if start in reached_frequencies:
            print('the answer is', start)
            break

        reached_frequencies.append(start)

# tally frequencies
for frequency in reached_frequencies:
    if frequency not in freq_dict:
        freq_dict[frequency] = 1
    else:
        freq_dict[frequencies] += 1

# find frequency that is double
for key, value in freq_dict.items():
    if value > 1:
        print(key)
