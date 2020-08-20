#!/usr/bin/python3

from functools import reduce

def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))

def main():
    # print(fact(4))
    print("\n".join(("{}! -> {}".format(n, fact(n))) for n in range(1, 10)))
    print("\n".join("%d! -> %d" %(n, fact(n)) for n in range(1, 10)))
    

if __name__ == '__main__':
    main()
