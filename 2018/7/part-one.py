steps = []
with open('test.txt') as inputfile:
    for line in inputfile:
        c = line.split(' ')
        first_step = c[1]
        second_step = c[7]
        steps.append([first_step, second_step])

already_available_steps = []
order = ''
count = 0

# figure out which steps aren't available
while count < len(steps):
    all_possible_steps = []
    possible_steps = []
    not_available_steps = []
    available_steps = []
    step_added = ''

    for step in steps:
        if step[0] not in already_available_steps:
            not_available_steps.append(step[1])
            # create a set of possible steps
            possible_steps.append(step[0])
            possible_steps.append(step[1])
        all_possible_steps.append(step[0])
        all_possible_steps.append(step[1])

    set_of_not_available_steps = set(not_available_steps)
    set_of_possible_steps = set(possible_steps)
    set_of_all_possible_steps = set(all_possible_steps)

    # of all the possible steps, figure out which are available
    for step in set_of_possible_steps:
        if step not in set_of_not_available_steps:
            available_steps.append(step)

    # if all the first_steps are accounted for, account for the second_steps
    for step in set_of_all_possible_steps:
        if step not in possible_steps and step not in already_available_steps and len(set_of_not_available_steps) == 0:
            available_steps.append(step)

    # add the step
    if len(available_steps) > 0:
        available_steps.sort()
        step_added = available_steps.pop(0)

    order += step_added
    already_available_steps.append(step_added)
    count += 1

    print(order, available_steps, set_of_possible_steps, set_of_not_available_steps)
