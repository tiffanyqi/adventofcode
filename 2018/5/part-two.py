import string

# original_chain = 'dabAcCaCBAcCcaDA'
with open('input.txt') as inputfile:
    original_chain = inputfile.read()

shortest_chain_length = 1000000000
for letter in string.ascii_lowercase:
    chain = original_chain
    last_chain = ''
    chain = chain.replace(letter, '')
    chain = chain.replace(letter.capitalize(), '')
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
    if len(chain) < shortest_chain_length:
        shortest_chain_length = len(chain)

print(shortest_chain_length)
