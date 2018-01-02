groups = ''
with open('input.txt') as inputfile:
    for line in inputfile:
        groups = line

groups = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
total = 0
curr_brace = 0
c = 0

garbage = False
include = True
for char in groups:
    if not garbage and include:
        if char == '{':
            curr_brace += 1
            total += curr_brace
        elif char == '}' and curr_brace > 0:
            curr_brace -= 1

    if char == '<':
        garbage = True

    if garbage:

        if char == '!':
            include = not include

        elif char == '>':
            garbage = False


print total
