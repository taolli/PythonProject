# if条件语句和while/for循环语句
n = 5
while n > 4:  # 当while遇到循环时，首先在boolean context中<布尔计算的表达式>进行评估,评估布尔值是否符合条件，如果符合，继续下一步的执行
    n -= 1  # 输出的是计算式
    print(n)
n = 5
while n > 0:
    n -= 1  # n=4,n=3,n=2,n=1,n=0
    print(n)
n = 4
while n > 0:
    n -= 1
    print(n)
n = 3
while n > 0:
    n -= 1
    print(n)
n = 2
while n > 0:
    n -= 1
    print(n)
n = 1
while n > 0:
    n -= 1
    print(n)
n = 0
while n > 0:  # 不进行循环
    n -= 1
    print(n)

n = 7
while n > 8:  # 当while遇到循环时，首先在boolean context中<布尔计算的表达式>进行评估,评估布尔值是否符合条件，如果不符合，循环体不会被执行
    n += 1
    print(n)

n = 9
while n > 5:
    n += 2
    print(n)
    break

n = 10
while n > 7:
    n += 3
    if n == 22:
        print(n)
        break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
        print(n)

n = 11
while n < 3:
    n -= 1
    if n == 6:
        print(n)

a_list = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for each_key in a_list.keys():
    print(a_list)

b_list = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for each_key in b_list.keys():
    print(b_list)
    break
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{} * {} = {}'.format(j, i, j*i), end('\t'))
        print('\n')
'''
for i in range(1, 10):
    for j in range(1, i + 1):
        print('{} * {} = {}'.format(j, i, j*i))
        print('\n')