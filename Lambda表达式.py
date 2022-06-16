
def true():
    return True


true()


# 可以写在一起
def true(): return True


# 写成lambda
var = lambda: True


def add(x, y):
    return x + y


# 写成lambda
var = lambda x, y: x + y

var = lambda x: x <= ('month', 'day')


def fun1(x):
    return x <= ('month', 'day')


var1 = lambda item: item[1]


def fun2(item):
    return item[1]


adict = {'a': 'aa', 'b': 'bb'}
for i in adict.items():
    fun2(i)

f = [12, 15, 16, 18, 20, 22, 24, 27]
for i in f:
    print(lambda i: i % 3 == 0)

# lambda表达式：lambda argument_list（参数列表）:expersion

c = lambda x, y, z: x * y * z
