ids = []
with open('input.txt') as inputfile:
    for line in inputfile:
        id = line.strip().split('\n')[0]
        ids.append(id)

ids_with_two_letters = 0
ids_with_three_letters = 0

for id in ids:
  letters = {}
  # add up the letters
  for letter in id:
    if letter not in letters:
      letters[letter] = 1
    else:
      letters[letter] += 1

  # count the letters
  two = 0
  three = 0
  for key, value in letters.items():
    if value == 2:
      two += 1
    elif value == 3:
      three += 1

  if two > 0:
    ids_with_two_letters += 1
  if three > 0:
    ids_with_three_letters += 1

print(ids_with_two_letters * ids_with_three_letters)
