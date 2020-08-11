#!/usr/bin/python3
from array import array
from random import random
from time import perf_counter as pc

def test_array():
    floats = array('d', (random() for _ in range(10**7)))
    print(floats[-1])
    t0 = pc()
    fp = open('floats.bin', 'wb')
    floats.tofile(fp)
    fp.close()
    print(pc() - t0)

    floats2 = array('d')
    t0 = pc()
    fp = open('floats.bin', 'rb')
    floats2.fromfile(fp, 10**7)
    fp.close()
    print(pc() - t0, floats2[-1], floats[-1] == floats2[-1])

def test_memoryview():
    numbers = array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(memv, len(memv), memv[0])
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    memv_oct[5] = 4
    print(numbers)

if __name__ == '__main__':
    # test_array()
    test_memoryview()