#!/usr/bin/python3

from operator import itemgetter, attrgetter

metro_data = [
    ('tokyo', 'jp', 36.9, (35.68, 139.69)),
    ('delhi ncr', 'in', 21.9, (28.6, 77.2)),
    ('mexico city', 'mx', 20.1, (19.4, -99.13)),
    ('new york', 'us', 20.1, (40.8, -74.02)),
    ('sao paulo', 'br', 19.649, (-23.55, -46.64)),
]

def test():
    for city in sorted(metro_data, key=itemgetter(1)):
        print(city)
    print()
    for city in sorted(metro_data, key=itemgetter(2)):
        print(city)

from collections import namedtuple

def test_2():
    LatLong = namedtuple('LatLong', 'lat long')
    Metropolis = namedtuple('Metropolis', 'name cc pop coord')
    m = [Metropolis(name, cc, pop, LatLong(lat, lon)) for name, cc, pop, (lat, lon) in metro_data]
    print(m)
    name_lat = attrgetter('name', 'coord.long')
    for city in sorted(m, key=attrgetter('coord.long')):
        print(name_lat(city))

if __name__ == '__main__':
    test()
    print()
    test_2()
