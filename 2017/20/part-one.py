def calculate_distance(x, y, z):
    return abs(x) + abs(y) + abs(z)


class Particle:
    """Particle class"""
    def __init__(self, num, pos, vel, accel):
        self.px = int(pos[0])
        self.py = int(pos[1])
        self.pz = int(pos[2])
        self.vx = int(vel[0])
        self.vy = int(vel[1])
        self.vz = int(vel[2])
        self.ax = int(accel[0])
        self.ay = int(accel[1])
        self.az = int(accel[2])
        self.d = calculate_distance(int(pos[0]), int(pos[1]), int(pos[2]))
        self.num = int(num)

particles = []
with open('input.txt') as inputfile:
    num = 0
    for line in inputfile:
        particle = line.strip().split('\n')
        items = particle[0].split(', ')
        positions = items[0].strip().split('<')[1].split('>')[0].split(',')
        velocities = items[1].strip().split('<')[1].split('>')[0].split(',')
        accels = items[2].strip().split('<')[1].split('>')[0].split(',')
        particles.append(Particle(num, positions, velocities, accels))
        num += 1

for iters in range(500):
    for p in particles:
        p.vx = p.vx + p.ax
        p.vy = p.vy + p.ay
        p.vz = p.vz + p.az
        p.px = p.px + p.vx
        p.py = p.py + p.vy
        p.pz = p.pz + p.vz
        p.d = calculate_distance(p.px, p.py, p.pz)

closest_distance = 100000000
closest_particle = 0
for particle in particles:
    distance = particle.d
    if abs(distance) < abs(closest_distance):
        closest_distance = distance
        closest_particle = particle

print closest_particle.num
