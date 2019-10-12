claims = []
with open('input.txt') as inputfile:
    for line in inputfile:
        claim = line.strip().split('\n')[0].split(' ')
        location = claim[2].split(',')
        dimensions = claim[3].split('x')
        claims.append({
            'id': int(claim[0][1:]),
            'left': int(location[0]),
            'top': int(location[1][:-1]),
            'wide': int(dimensions[0]),
            'tall': int(dimensions[1]),
        })

height = 1000
width = 1000
fabric = [[0 for x in range(width)] for y in range(width)] 
for claim in claims:
    # (x, y) is the top leftmost corner
    x = claim['left']
    y = claim['top']
    x_start = x
    y_start = y

    for left_move in range(claim['wide']):
        for down_move in range(claim['tall']):
            fabric[x_start+left_move][y_start+down_move] += 1

    x_start = x
    y_start = y

overlap = 0
for x in fabric:
    for y in x:
        if y > 1:
            overlap += 1

print(overlap)
