from datetime import datetime

def manhattan_distance(xa, ya, xb, yb):
   return abs(xa - xb) + abs(ya - yb)

def isEdge(x, y, width, length):
   if x == 0 or y == 0:
      return True
   elif x == width -1 or y == length - 1:
      return True
   else:
      return False


coordinates = []
with open('input.txt') as inputfile:
    for line in inputfile:
         c = line.split(', ')
         coordinates.append([int(c[0]), int(c[1])])

height = 400 # 400
width = 400 # 400
grid = [[0 for x in range(height)] for y in range(width)]

# plot points
for index in range(len(coordinates)):
   coordinate = coordinates[index]
   grid[coordinate[0]][coordinate[1]] = index

# plot directions
for x in range(width):
   for y in range(height):
      min_distance = 100000
      min_index = 0
      for index in range(len(coordinates)):
         coordinate = coordinates[index]
         distance = manhattan_distance(coordinate[1], coordinate[0], x, y)
         if distance < min_distance:
            min_distance = distance
            min_index = index
         elif distance == min_distance:
            min_index = ''
      grid[x][y] = min_index

# count area
areas = {}
for x in range(width):
   for y in range(height):
      value = grid[x][y]
      if value is not '':
         if value in areas:
            areas[value]['area'] += 1
            areas[value]['isEdge'] = isEdge(x, y, width, height) or areas[value]['isEdge']
         else:
            areas[value] = {
               'area': 1,
               'isEdge': isEdge(x, y, width, height)
            }

max_area = 0
for _item, value in areas.items():
   if not value['isEdge'] and max_area < value['area']:
      max_area = value['area']

print(max_area)
