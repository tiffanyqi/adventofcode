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
# populate the fabric
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

# do it again, but check the fabric this time
for claim in claims:
    # (x, y) is the top leftmost corner
    x = claim['left']
    y = claim['top']
    x_start = x
    y_start = y
    the_one = True

    for left_move in range(claim['wide']):
        for down_move in range(claim['tall']):
            x_pos = x_start+left_move
            y_pos = y_start+down_move
            if fabric[x_pos][y_pos] != 1:
                the_one = False
                break
    if the_one:
        print(claim['id'])
        break

    x_start = x
    y_start = y
