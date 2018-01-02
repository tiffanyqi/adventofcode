particles = []
with open('input.txt') as inputfile:
    for line in inputfile:
        particles.append(line.strip().split('\n'))


def create_dictionary(particles):
    dictionary = {}
    for i, particle in enumerate(particles):
        items = particle[0].split(', ')
        positions = items[0].strip().split('<')[1].split('>')[0].split(',')
        dictionary[i] = {
            'p': positions,
            'v': items[1].strip().split('<')[1].split('>')[0].split(','),
            'a': items[2].strip().split('<')[1].split('>')[0].split(','),
        }

    return dictionary

dictionary = create_dictionary(particles)
for iters in range(1000):
    positions = {}
    for particle in dictionary:
        try:
            p = dictionary[particle]['p']
            v = dictionary[particle]['v']
            a = dictionary[particle]['a']
            dictionary[particle]['v'] = [int(v[0])+int(a[0]), int(v[1])+int(a[1]), int(v[2])+int(a[2])]
            v = dictionary[particle]['v']  # necessary to update new velocity
            dictionary[particle]['p'] = [int(p[0])+int(v[0]), int(p[1])+int(v[1]), int(p[2])+int(v[2])]

            p = str(dictionary[particle]['p'])
            try:
                positions[p].append(particle)

            except KeyError:
                positions[p] = [particle]

        except TypeError:
            pass

    for p in positions:
        if len(positions[p]) > 1:
            for r in positions[p]:
                dictionary[r] = []
                print 'collision! ' + str(r)

total = 0
for key in dictionary:
    if dictionary[key] != []:
        total += 1

print total
