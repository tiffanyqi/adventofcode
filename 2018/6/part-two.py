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

height = 400
width = 400
grid = [[0 for x in range(height)] for y in range(width)]
max_distance = 10000
number_of_locations = 0

# plot points
for index in range(len(coordinates)):
   coordinate = coordinates[index]
   grid[coordinate[0]][coordinate[1]] = index

# calculate distance
for x in range(width):
   for y in range(height):
      total_distance = 0
      for index in range(len(coordinates)):
         coordinate = coordinates[index]
         distance = manhattan_distance(coordinate[1], coordinate[0], x, y)
         total_distance += distance
      if total_distance < max_distance:
         number_of_locations += 1

print(number_of_locations)
