import math

original_array = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]


def redistribution_2():
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

        for i, arr in enumerate(arrays):
            if arr[:] == [0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10] and i != 4289:
                print i
                return total

        total += 1
        arrays += [list(array)]

print redistribution_2()
