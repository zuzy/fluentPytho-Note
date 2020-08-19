#!/usr/bin/python3
l = ['spam', 'spam', 'eggs', 'spam']

def test_1():
    print(set(l))
    print(list(set(l)))

from unicodedata import name

def test_2():
    s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
    print(s)

if __name__ == '__main__':
    test_1()
    test_2()


