#!/usr/bin/python3

from functools import partial


def tag(name, *content, cls=None, **attrs):
    ''' 生成一个或多个html标签 '''
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, val) 
                    for attr, val in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % 
                (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def main():
    picture = partial(tag, 'img', cls='pic-frame')
    pic = picture(src='wumpus.jpeg')
    print(pic)
    print(picture)
    print(picture.func)
    print(picture.args)
    print(picture.keywords)

if __name__ == '__main__':
    main()
