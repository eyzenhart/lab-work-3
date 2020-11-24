from math import pi


def find_farthest_orbit(list_of_orbits):
    max_s = max([i[0] * i[1] * pi for i in list_of_orbits if i[0] != i[1]])
    return [i for i in list_of_orbits if max_s == i[0] * i[1] * pi]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
