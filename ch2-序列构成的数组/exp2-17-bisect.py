#!/usr/bin/python3
import bisect
import random
import sys

HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}     {2}{0:<2d}'

'''
bisect.besect 是 bisect_right的别名，
bisect(haystack, needle) 在haystack（干草垛）里面搜索needle（针）的位置，该位置满足的条件是：
    把needle插入这个位置之后，haystack还能保持升序。
    也就是说这个函数返回的位置前面的值，都小于或等于needle的值。
    haystack必须是一个有序的序列。
1. index = bisect(haystack, needle) 查找位置
2. haystack.insert(index, needle) 插入新值
或者直接使用insort一步到位。
'''

def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * ' | '
        print(ROW_FMT.format(needle, position, offset))

def demo_bisect():
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect
    
    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

'''
insort 和 bisect 一样，有lo和hi两个可选参数控制查找范围，它也有一个变体：insort_left，它背后的就是bisect_left。

'''

def demo_insort():
    SIZE=7
    random.seed(1729)

    my_list = []
    for i in range(SIZE):
        new_item = random.randrange(2 * SIZE)
        bisect.insort(my_list, new_item)
        print('%2d ->' %new_item, my_list)
    

if __name__ == '__main__':
    # demo_bisect()
    demo_insort()