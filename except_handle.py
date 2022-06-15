# 异常捕获
# year = int(input('请输入年份：'))
from netaddr.core import a

try:
    year = int(input('请输入年份：'))
except ValueError:
    print('年份要输入数字')
# 可以捕获多个异常
# except (ValueError, AttributeError, KeyError, NameError):  多个异常时写出元祖的格式
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print('0不能做除数 %s' % e)

try:
    print(1 / a)
except Exception as e:
    print('%s' % e)

# 自己定义错误的提示信息，在python中用raise
try:
    raise NameError('hello error')
except NameError:
    print('hi error')

try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()
