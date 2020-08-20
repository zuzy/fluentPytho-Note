#!/usr/bin/python3

from inspect import signature

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
    print(tag('br'))
    print()
    print(tag('p', 'hello'))
    print()
    print(tag('p', 'hello', 'world'))
    print()
    print(tag('p', 'hello', id=3))
    print()
    print(tag('p', 'hello', 'world', cls='sidebar'))
    print()
    print(tag(content='testing', name='img'))
    print()
    my_tag = {
        'name':'img',
        'title':'sunset',
        'src':'sunset.jpg',
        'cls':'framed'
    }
    print(tag(**my_tag))

    sig = signature(tag)
    print(sig)

if __name__ == '__main__':
    main()
    