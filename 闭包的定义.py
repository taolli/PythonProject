# 先了解闭包
def func():
    a = 1
    b = 2
    return a + b
    print(func())  # 一般函数


def sum(a):
    def add(b):
        return a + b

    return add  # 这个就是闭包，外部函数被内部函数调用


num1 = func()
num2 = sum(2)
print(type(num1))  # 类型是整数
print(type(num2))  # 类型是函数
'''
<class 'int'>
<class 'function'>
'''

# add 函数名称或函数的引用
# add() 函数的调用
'''
def counter():
    cn_num = [0]

    def add_one():
        cn_num[0] += 1
        return cn_num[0]

    return add_one


num1 = counter()
print(num1())
print(num1())
print(num1())
print(num1())
print(num1())
print(num1())

'''


def counter(FIRST=0):  # 为函数做定义
    cn_num = [FIRST]

    def add_one():
        cn_num[0] += 1
        return cn_num[0]

    return add_one


num5 = counter(5)
num10 = counter(10)
print(num5())
print(num5())
print(num5())
print(num10())
print(num10())
print(num10())
