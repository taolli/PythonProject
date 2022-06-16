# python的内置函数有filter(), map(), reduce(), zip()

# filter()的用法：
f = [1, 2, 3, 4, 5, 6, 7]
>>> filter(lambda x: x >2, f)
>>> list(filter(lambda x: x >2, f))

# map()的用法：
m = [1, 2, 3, 4]
>>> map(lambda x:x , m)
>>> list(map(lambda x :x, m))
n = [5, 6, 7, 8]
>>> map(lambda x : x + 1, n)
>>> list(map(lambda x : x + 1, n) )

>>> list(map(lambda x,y: x+y, m, n))

# reduce()的用法：
from functools import reduce
reduce(lambda x,y: x + y [1, 2, 3], 1)
>>>(((1+1)+2)+3)

# zip()的用法：
zip((1, 2, 3, 4), (5, 6, 7, 8))
for i in zip((1, 2, 3, 4), (5, 6, 7, 8)):
    print(i)
# 打印结果为：
(1, 5)
(2, 6)
(3, 7)
(4, 8)

dicta = {'a': 'aa', 'b': 'bb'}
dictb = zip(dicta.values(), dicta.keys())
# print(dict)
print(dict(dictb))
# key和value对调
