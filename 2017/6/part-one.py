import math

original_array = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]


def redistribution():
    array = original_array
    total = 1
    arrays = [[]]
    arrays[0] = list(array)
    length = len(array)

    while True:
        distribute = max(array)
        curr_index = array.index(distribute)
        give = int(math.ceil(max(array) / float(length)))
        array[curr_index] = 0 if (distribute - give * (length - 1)) < 0 else (distribute - give * (length - 1))
        remaining = distribute
        index = curr_index

        while remaining:
            if index == length-1:
                index = 0
            else:
                index += 1

            array[index] = array[index] + give
            remaining -= 1

        print array
        for arr in arrays:
            if arr[:] == array:
                return total

        total += 1
        arrays += [list(array)]

print redistribution()
