#!/usr/bin/python3 

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)

def test():
    s = 6
    fact = factorial
    l = list(map(fact, range(s)))
    print(l)
    l1 = [fact(n) for n in range(s)]
    print(l1)
    l2 = list(map(fact, filter(lambda n: n % 2, range(s))))
    print(l2)
    l3 = [fact(n) for n in range(s) if n % 2]
    print(l3)


if __name__ == '__main__':
    test()
