lines = []
group_to_value = {}
num_groups = 0
groups = []

with open('input.txt') as inputfile:
    for line in inputfile:
        lines.append(line.strip().split('\n'))

for line in lines:
    key = line[0].split(' <-> ')
    group = int(key[0])
    values = key[1].split(', ')
    group_to_value[group] = values

contains = [0]
for i in range(0, len(lines)):
    if i not in contains:
        num_groups += 1

        contains_num = [i]
        for j in range(0, 50):
            for group, array in group_to_value.iteritems():
                if str(i) in array:
                    contains_num.append(group)
                if group in contains_num:
                    for value in array:
                        contains_num.append(int(value))
        for num in set(contains_num):
            contains.append(num)

print num_groups
