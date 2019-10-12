ids = []
with open('input.txt') as inputfile:
    for line in inputfile:
        id = line.strip().split('\n')[0]
        ids.append(id)

def find_ids():
  for first_id in ids:
    for second_id in ids:
      differ_letter_amount = 0
      for num in range(0, len(first_id)):
        if first_id[num] != second_id[num]:
          differ_letter_amount += 1

      if differ_letter_amount == 1:
        print(first_id, second_id)
        return [first_id, second_id]

correct_ids = find_ids()
letters = ''
first_id = correct_ids[0]
second_id = correct_ids[1]

for num in range(0, len(first_id)):
  if first_id[num] == second_id[num]:
    letters += first_id[num]

print(letters)
