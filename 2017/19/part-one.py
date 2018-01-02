graph = []
letters = []
possible_symbols = ['|', '-']

x = 0  # up and down
y = 5  # left and right
down = 1
right = 1
prev_symbol = ''
prev_step = 0
end = False


with open('input.txt') as inputfile:
    for line in inputfile:
        line = line.split('\n')[0]
        add = []
        for char in line:
            add.append(char)
        graph.append(add)

while not end:
    symbol = graph[x][y]
    print symbol, x, y
    if symbol == '|':
        x += down
    elif symbol == '-':
        y += right
    elif symbol == ' ':
        end = True
    elif symbol == '+':
        if graph[x-1][y] != ' ' and graph[x-1][y] != prev_symbol:
            down = -1
            x += down
        elif graph[x+1][y] != ' ' and graph[x+1][y] != prev_symbol:
            down = 1
            x += down
        elif graph[x][y-1] != ' ' and graph[x][y-1] != prev_symbol:
            right = -1
            y += right
        elif graph[x][y+1] != ' ' and graph[x][y+1] != prev_symbol:
            right = -1
            y += right

    else:
        letters.append(symbol)
        if prev_symbol == '|':
            x += down
        elif prev_symbol == '-':
            y += right


    prev_symbol = symbol

print letters
