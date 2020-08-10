#!/usr/bin/python3

symbols = '1！@#！￥@#%@#》《。，……'

# 2-1
def test_2_1():
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    print(codes)

# 2-2
def test_2_2():
    codes = [ord(symbol) for symbol in symbols]
    print(codes)

# 2-3
def test_2_3():
    beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
    print(beyond_ascii)
    beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
    print(beyond_ascii)

# 2-4 笛卡尔积
def descartes():
    colors = ['black', 'white']
    sizes = ['S', 'M', 'L']
    # tshirts = [(color, size) for color in colors for size in sizes]
    # tshirts = [(color, size) for color in colors
    #                             for size in sizes]
    tshirts = [(color, size) for size in sizes
                                for color in colors]
    print(tshirts)
    for color in colors:
        for size in sizes:
            print((color, size))

# 2-5
def test_2_5():
    t = tuple(ord(s) for s in symbols)
    print(t)
    import array
    a = array.array('I', (ord(s) for s in symbols))
    print(a)

def test_2_6():
    colors = 'black white'.split()
    sizes = 'S M L'.split()
    for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
        print(tshirt)

'''
- 元组：不可变的列表，还用于没有字段名的记录！
元组是一些字段的集合，这些字段的数量和位置信息非常重要！
所以函数的参数都是元组？
'''
def test_2_7():
    lax_coordinates = (33.9, -118.4)
    city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8914)
    traveler_ids = [('USA', '3119'), ('BRA', 'CE342'), ('ESP', 'XDA205')]
    for passport in sorted(traveler_ids):
        print("%s/%s" % (passport))
    for country, _ in traveler_ids:
        print(country)

if __name__ == '__main__':
    # descartes()
    # test_2_5()
    # test_2_6()
    test_2_7()