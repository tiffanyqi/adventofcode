array = []
with open('input.txt') as inputfile:
    for line in inputfile:
        array.append(int(line.strip().split('\n')[0]))


def jumps():
    total = 0
    start = 0
    while True:
        try:
            increment = array[start]
            array[start] = increment + 1
            start = increment + start
            total += 1

        except IndexError:
            return total

print jumps()
