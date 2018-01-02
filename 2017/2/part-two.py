spreadsheet = []
with open('spreadsheet.txt') as inputfile:
    for line in inputfile:
        spreadsheet.append(line.strip().split('\t'))

total = 0
for line in spreadsheet:
    for first_num in line:
        for second_num in line[1:]:
            if int(first_num) % int(second_num) == 0 and first_num != second_num:
                total += (int(first_num) / int(second_num))
print total
