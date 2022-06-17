import re

p = re.compile('a')
print(p.match('a'))

p = re.compile('li')
print(p.match('ll'))

# 在做匹配多个字符时引入特殊字符

p = re.compile('map')
print(p.match('map'))

p = re.compile('ma*p')
print(p.match('maaaaaaaap'))

