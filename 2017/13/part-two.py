lines = {}
with open('input.txt') as inputfile:
    for line in inputfile:
        line = line.strip().split('\n')[0].split(': ')
        layer = int(line[0])
        depth = int(line[1])
        lines[layer] = depth


def position(depth, second):
    return second % depth


def isCaught(depth, second):
    return position((depth-1)*2, second) == 1

for j in range(0, 10000000):
    caught = []
    for i in range(0, 99):
        try:
            if isCaught(lines[i], i+1+j):
                caught.append(i)
                continue
        except KeyError:
            continue
    if not caught:
        print j
