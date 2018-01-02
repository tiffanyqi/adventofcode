steps = 314
end_num = 50000000
array = [0]
curr_pos = 0
zero_index = 0

for i in range(1, end_num+1):
    curr_pos = ((curr_pos + steps) % i) + 1
    if curr_pos - 1 == 0:
        zero_index = i-1

print zero_index + 1
