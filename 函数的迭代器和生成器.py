# 迭代器函数 next() iter()
alist = [1, 2, 3, 4]
it = iter(alist)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
# print(next(it))   # 迭代完成，再次进行迭代就报异常 exception


# 生成器函数 yield
for i in range(10, 20, 2):
    print(i)

'''
for k in range(11, 21, 0.5):
    print(k)                     # range函数当有3个参数时，第三个参数表示步长只能使用整数
'''
for t in (12, 20.5):
    print(t)


# 自定义生成器函数

def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in frange(12, 25, 0.8):
    print(i)

blist = [3, 4, 5]
i = iter(blist)
print(next(i))
print(next(i))
