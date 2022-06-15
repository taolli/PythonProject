# 关键字函数
'''
print('asdf')
print('asdf', 'ty_ty', 123)
print('asd', end='over')


def func(a, s, d):
    print('a = %a' % a)
    print('s = %s' % s)
    print('d = %d' % d)


func(1, s=3, d=4)

'''


# func(1, 3, 4)


# 取得参数的个数
def howlong(first, *other):
    # return len(first) + len(other)
    print(1 + len(other))


howlong(134, 5678, 709, 'ok')
