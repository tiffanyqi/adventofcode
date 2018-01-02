child_to_parent = {}
parent_to_child = {}
keys_to_value = {}

with open('input.txt') as inputfile:
    for line in inputfile:
        for item in line:
            item = line.strip().split(' -> ')
            keys = item[0].strip().split(' ')
            parent = keys[0]
            value = int(keys[1][1:-1])
            keys_to_value[parent] = value

            try:
                babies = item[1].strip().split(', ')
                parent_to_child[parent] = [babies[0:], value]
                for baby in babies[0:]:
                    child_to_parent[baby] = [parent, value]
            except IndexError:
                pass


def tree_to_root():
    start = 'ejlbps'
    total = keys_to_value[start]
    while True:
        try:
            print start
            start = child_to_parent[start][0]
            total += child_to_parent[start][1]
        except KeyError:
            print start
            return total


def tree_to_child():
    root = 'dtacyn'
    start = 'dtacyn'
    total = keys_to_value[start]
    while True:
        try:
            print start
            start = parent_to_child[start][0][0]
            total += parent_to_child[start][1]
        except:
            print start
            return total

print tree_to_child()
