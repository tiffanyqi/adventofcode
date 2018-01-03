groups = ''
with open('input.txt') as inputfile:
    for line in inputfile:
        groups = line

total_score = 0
curr_brace = 0
total_garbage = 0
garbage = False
skip = False

for char in groups:
    if skip:
        skip = False
    elif not skip:
        if garbage:
            total_garbage += 1

        if not garbage and char == '{':
            curr_brace += 1
            total_score += curr_brace
        elif not garbage and char == '}' and curr_brace > 0:
            curr_brace -= 1

        elif char == '!':
            skip = True
            total_garbage -= 1
        elif char == '<':
            garbage = True
        elif char == '>':
            garbage = False
            total_garbage -= 1


print total_garbage
