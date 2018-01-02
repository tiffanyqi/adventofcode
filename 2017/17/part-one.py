steps = 314
end_num = 50000000
array = [0]
curr_pos = 0
zero_index = 0

for i in range(0, end_num):
    if i == 0:
        curr_pos = 1
    else:
        curr_pos = ((curr_pos + steps) % len(array)) + 1

        if array[curr_pos-1] == 0:
            zero_index = curr_pos-1

    array.insert(curr_pos, i+1)

print array[zero_index+1]
