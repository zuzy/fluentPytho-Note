#!/usr/bin/python3
import sys, re

WORD_RE = re.compile(r'\w+')

def main():
    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # !这是一种很不好的实现！
                # 提取word出现的情况，如果没有记录就返回 []
                occurrences = index.get(word, [])
                # 把新的位置添加在列表后面
                occurrences.append(location)
                # 把新的列表放回字典，这里又一次查询操作
                index[word] = occurrences
    # sorted函数的 key= 参数没有调用 str.upper，而是把这个方法的引用传递给sorted，在排序的时候单词会规范成同一格式
    # 一等函数的一个示例
    for word in sorted(index, key=str.upper):
        print(word, index[word])

def main_2():
    index = {}
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                # ! setdefault 获取单词出现的列表，如果不存在，把单词和一个空列表放进映射，然后返回这个空列表，避免二次查找
                index.setdefault(word, []).append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])

import collections
def main_3():
    index = collections.defaultdict(list)
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                index[word].append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])

def test_strkeydict(obj):
    d = obj([('2', 'two'), ('4', 'four')])
    print(isinstance(d, dict))
    try:
        print(d['2'])
        print(d[2])
        print(d[4])
        print(d[1])
    except Exception as e:
        print(e)

    try:
        print(d.get('2'))
        print(d.get('1'))
        print(d.get('1', "N/A"))
    except Exception as e:
        print(e)
    
    print((1 in d))
    print((2 in d))


def main_self_dict():
    class StrKeyDict0(dict):
        
        def __missing__(self, key):
            # ! 判断key是否是str的一个实例
            if isinstance(key, str):
                raise KeyError("key error", key)
            return self[str(key)]
        
        def get(self, key, default=None):
            try:
                return self[key]
            except KeyError:
                return default
        
        def __contains__(self, key):
            return key in self.keys() or str(key) in self.keys()
        
        # def __setitem__(self, key, value):
        #     self[str(key)] = value
    
    test_strkeydict(StrKeyDict0)
    # s[wwer] = 123

def main_self_dict_new():
    # ! 相比于上一个实现 StrKeyDict0，这里继承于UserDict。
    # ! 比dict多了一个data属性描述dict实例，而且可以自己实现 __setitem__ 
    class StrKeyDict(collections.UserDict):

        def __missing__(self, key):
            if isinstance(key, str):
                raise KeyError(key)
            return self[str(key)]
        
        def __contains__(self, key):
            return str(key) in self.data
        
        def __setitem__(self, key, item):
            self.data[str(key)] = item
    
    test_strkeydict(StrKeyDict)


if __name__ == '__main__':
    # main()
    # main_2()
    # main_3()
    main_self_dict()
    # main_self_dict_new()
