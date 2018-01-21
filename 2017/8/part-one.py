from collections import defaultdict
import operator

lines = []
with open('input.txt') as inputfile:
    for line in inputfile:
        lines.append(line.strip().split('\n'))

string_to_value = defaultdict(lambda: 0)
max_value = 0


def processer(string_mod, process, string_amount, string_check, sign, modifier):
    """
    for: o inc 394 if tcy >= -3
    o = string_mod
    inc = process (inc, dec)
    394 = string_amount
    tcy = string_check
    >= = sign (>, <, >=, <=, ==, !=)
    -3 = modifier
    """
    global max_value
    if check_sign_correct(string_to_value[string_check], sign, int(modifier)):
        if process == 'inc':
            string_to_value[string_mod] += int(string_amount)

        else:
            string_to_value[string_mod] -= int(string_amount)

    if max_value < string_to_value[string_mod]:
        max_value = string_to_value[string_mod]


def check_sign_correct(string_check, sign, modifier):
    if sign == '>':
        return string_check > modifier

    elif sign == '>=':
        return string_check >= modifier

    elif sign == '<':
        return string_check < modifier

    elif sign == '<=':
        return string_check <= modifier

    elif sign == '!=':
        return string_check != modifier

    elif sign == '==':
        return string_check == modifier

for line in lines:
    items = line[0].strip().split(' ')
    processer(items[0], items[1], items[2], items[4], items[5], items[6])

max_key = max(string_to_value.iteritems(), key=operator.itemgetter(1))[0]
print string_to_value[max_key]
