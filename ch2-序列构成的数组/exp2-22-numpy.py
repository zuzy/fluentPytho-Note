#!/usr/bin/python3
import numpy

def test_numpy():
    a = numpy.arange(12)
    print(type(a), a.shape, a)
    a.shape = 3, 4
    print(a)
    print(a[2])
    print(a[:, 1])
    print(a.transpose())
    print(a)

# def test_numpy_file():
#     floats = numpy.loadtxt('floats.bin')
#     print(floats[-3:])

if __name__ == '__main__':
    test_numpy()
    # test_numpy_file()
