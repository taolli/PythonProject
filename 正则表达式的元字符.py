# . 匹配任意的单个字符
# ^ 表示是以什么样的内容做开头，一般用于搜索和替换功能
# $ 表示以什么样的内容做结尾，从后面向前面匹配，一般用于文件和目录的处理
# * 表示匹配前面的字符出现0次到多次
# + 表示前面的字符出现1次到多次
# ? 表示前面的字符出现0次到1次
# {m} 表示前面的字符出现指定的次数  m表示大括号里要有内容
# {m.n}
# [] 表示中括号里的任意一个字符匹配成功，剩下的字符都能匹配成功
# |  表示字符选择左边或右边，一般和()括号用在一起
# 转义字符 \d \D \s
# \d 表示匹配的内容是一串数字    和[0-9]+的功能是一样的
# \D 匹配不包含数字的
# \s 表示匹配的字符串，只包含a-z的字符串
# () 表示进行分组
# (2022)-(06)-(23).group()
# ^$ 表示这一行是空行
# .*? 表示不使用贪婪模式 适用于编写网页上内容的匹配

import re

p = re.compile('.')
print(p.match('aaaa'))
p = re.compile('.....')  # 使用多个.匹配 ，如果.多于要匹配的字符，是匹配不上的
print(p.match('aaaa'))

# p = re.compile('jpg$')
p = re.compile('ca*t')
print(p.match('ct'))     # 匹配0次

p = re.compile('ca*t')
print(p.match('caaaaat'))  # 匹配多次

p = re.compile('c?t')
print(p.match('cat'))

p = re.compile('ca{5}t')
print(p.match('caaaaat'))

p = re.compile('ca{6}t')
print(p.match('caaaaat'))    # 匹配多于要匹配的字符是失败的

p = re.compile('ca{4,6}t')   # 匹配字母a出现4次到6次
print(p.match('caaaaat'))

'''
c[bcd]t
cat
cbt
cct
cdt
'''