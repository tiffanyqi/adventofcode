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
            'd': calculate_distance(positions)
        }

    return dictionary


def calculate_distance(positions):
    return abs(int(positions[0])) + abs(int(positions[1])) + abs(int(positions[2]))


dictionary = create_dictionary(particles)
for iters in range(10000):
    for particle in dictionary:
        p = dictionary[particle]['p']
        v = dictionary[particle]['v']
        a = dictionary[particle]['a']
        dictionary[particle]['v'] = [int(v[0])+int(a[0]), int(v[1])+int(a[1]), int(v[2])+int(a[2])]
        dictionary[particle]['p'] = [int(p[0])+int(v[0]), int(p[1])+int(v[1]), int(p[2])+int(v[2])]
        dictionary[particle]['d'] = calculate_distance(p)

closest_distance = 100000000
closest_particle = 0
for particle in dictionary:
    distance = dictionary[particle]['d']
    if abs(distance) < abs(closest_distance):
        closest_distance = distance
        closest_particle = particle

print closest_particle
