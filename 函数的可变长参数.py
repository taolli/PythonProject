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

# 函数的变量作用域   #函数外部变量
var1 = 123


def function():
    print(var1)


function()

var2 = 234  # 函数内部变量


def function():
    var2 = 345
    print(var2)  # 输出的是内部变量


function()
print(var2)  # 输出的是外部变量

var3 = 456                 # 定义全局变量


def function():
    global var3
    var3 = 456
    print(var3)


function()
print(var3)


for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={}\t'.format(j, i, j*i), end='')
    print()
