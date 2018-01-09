a_start = 618
b_start = 814

a_factor = 16807
b_factor = 48271

product = 2147483647
total = 0


def calculate_next_value(start, factor, product):
    return start * factor % product


def convert_to_binary(number):
    return '{0:08b}'.format(number)


def compare_last_sixteen(one, two):
    return str(one)[-16:] == str(two)[-16:]

for i in range(0, 40000000):
    a = calculate_next_value(a_start, a_factor, product)
    b = calculate_next_value(b_start, b_factor, product)
    bin_a = convert_to_binary(a)
    bin_b = convert_to_binary(b)
    if compare_last_sixteen(bin_a, bin_b):
        total += 1
    a_start = a
    b_start = b

print total
