spreadsheet = []
with open('spreadsheet.txt') as inputfile:
    for line in inputfile:
        spreadsheet.append(line.strip().split('\t'))

total = 0
for line in spreadsheet:
    smallest = line[0]
    biggest = 0

    for num in line:
        if int(num) < smallest:
            smallest = int(num)
        if int(num) > biggest:
            biggest = int(num)

    diff = biggest - smallest
    total += diff

return total
