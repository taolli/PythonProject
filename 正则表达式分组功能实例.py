import re
'''
p = re.compile('...')
print(p.match('avc'))   # 匹配单个字符

p = re.compile('.{4}')
print(p.match('asdf'))    # 匹配多个字符


# 匹配一个年月日，并把年月日取出

p = re.compile('....-..-..')
print(p.match('2022-06-24'))





# 换一种写法

p = re.compile('....-.-..')
print(p.match('2022-6-24'))    #需要不断变换

# 使用\d来匹配
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2022-06-24'))

# 为什么加r
print('\n')  # 换行符
print('\nxy\n')
print(r'\nxy\n')  #不转义，加r

# 取出匹配的某一部分

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2022-06-24').group())  # 取出年月日

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2022-06-24').group(1))  # 取出年

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2022-06-24').group(2))  # 取出月

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2022-06-24').group(3))  # 取出日

p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2022-06-24').groups())  # 取出所有

# 赋给变量取出
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2022-06-24').groups())
year, month, day = p.match('2022-06-24').groups()
print(year)
print(month)
print(day)
print(year, month, day)

# 正则表达式库函数match和search的区别
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('aa2022-06-24bb').groups())  # 匹配的字符串要和正则是一一对应的


p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.search('aa2022-06-24bb'))      # search通常用作在函数中搜索指定的字符创，match通常是完全匹配后用作分组

'''
# 正则表达式库替换函数sub()的实例
# sub('c', '*', 'abcd')   sub的写法是后面跟着三个参数，第一个参数是需要匹配的匹配规则（用元字符表示），第二个参数把字符串替换成什么样的内容，第三个参数要替换的字符串

phone = '123-456-789 # 这是手机号码'
p2 = re.sub(r'#.*$', '', phone)  # 替换里面的字符串
print(p2)
p3 = re.sub(r'\D', '', p2)     # 替换里面的-
print(p3)

# findall()函数可以进行匹配多次
