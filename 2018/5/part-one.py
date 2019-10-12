from datetime import datetime

# original_chain = 'dabAcCaCBAcCcaDA'
with open('input.txt') as inputfile:
    original_chain = inputfile.read()

chain = original_chain
last_chain = ''
while chain != last_chain:
    last_chain = chain
    for num in range(len(chain)):
        try:
            first_letter = chain[num]
            second_letter = chain[num+1]
            if (first_letter != second_letter and (first_letter.capitalize() == second_letter or second_letter.capitalize() == first_letter)):
                chain = chain[0:num] + chain[num+2:len(chain)]
        except IndexError:
            break

print(len(chain))
