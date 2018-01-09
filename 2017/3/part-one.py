"""
37  35  34  33  32  31
17  16  15  14  13  30
18   5   4   3  12  29
19   6   1   2  11  28
20   7   8   9  10  27
21  22  23  24  25  26 ...

2, 10, 18
"""
input = 325489

def get_northeast(steps):
    difference = 2
    count = 0
    start = 1
    while start < steps:
    	start += difference
	difference += 8
	count += 1
    # current position, total northeasts
    return [start-difference+8, count]

def get_northwest(steps):
    difference = 4
    start = 1
    count = 0
    while start < steps:
        start += difference
        difference += 8
        count += 1
    # current position, total northwests
    return [start-difference+8, count]

counts = get_northwest(input)[1]*2 - 2
distance = input - get_northwest(input)[0]
total = counts + counts - distance
print total
