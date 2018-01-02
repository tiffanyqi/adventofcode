from queue_program import parse

program = []
one_dictionary = {}
one_frequencies = {}
two_dictionary = {}
two_frequencies = {}
with open('input.txt') as inputfile:
    for line in inputfile:
        program.append(line.strip().split('\n'))

print parse(program, one_dictionary, one_frequencies)
