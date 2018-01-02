output = "76,1,88,148,166,217,130,0,128,254,16,2,130,71,255,229"
num = 256
curr_list = [i for i in xrange(num)]


def convert_to_ascii(output):
    result = []
    for char in output:
        result.append(ord(char))
    return result


def output_final_list(curr_list, output):
    """
    - take the first value
    - reverse the beginning to the length value of the list
    - move the position and increase the skip value
    """
    copied_list = curr_list[:]
    skip = 0
    position = 0
    for i in range(0, 64):
        for length in output:
            if length > 0:
                last = (position + length) % num
                copied_list = compiled_list(position, last, copied_list)
            position = (position + length + skip) % num
            skip += 1
    return copied_list


def compiled_list(first, last, curr_list):
    list_length = len(curr_list)
    if last > first:
        start_of_curr_list = curr_list[0:first]
        end_of_curr_list = curr_list[last:list_length]
        reversed_list = list(reversed(curr_list[first:last]))
        return start_of_curr_list + reversed_list + end_of_curr_list
    else:
        end_of_curr_list = curr_list[first:list_length]
        start_of_curr_list = curr_list[0:last]
        new_unreversed = end_of_curr_list + start_of_curr_list
        split_point = len(end_of_curr_list)
        reversed_list = list(reversed(new_unreversed))
        return reversed_list[split_point:] + curr_list[last:first] + reversed_list[0:split_point]


def create_hash(final_list):
    dense_hash = []
    value = 0
    for index, num in enumerate(final_list):
        value = value ^ num
        if index % 16 == 15:
            dense_hash.append(value)
            value = 0
    return dense_hash


def convert_hexadecimal(dense_hash):
    output = ''
    for num in dense_hash:
        output += format(num, '02x')
    return output


def create_knot_hash(output):
    final_output = convert_to_ascii(output) + [17, 31, 73, 47, 23]
    final_list = output_final_list(curr_list, final_output)
    dense_hash = create_hash(final_list)
    hexadecimal = convert_hexadecimal(dense_hash)
    return hexadecimal


print create_knot_hash(output)
