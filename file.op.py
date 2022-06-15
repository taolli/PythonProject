'''
# 记录课本中的重点组词
file1 = open('name.txt', 'w')
file1.write('蓝天')
file1.close()

file2 = open('name.txt')
file2.read(0)
print(file2.read(1))
file2.close()

file3 = open('name.txt')
# file3.read()
print(file3.read())
file3.close()

file4 = open('name.txt', 'a')
file4.write('白云')
file4.close()
# 写入后再次读取
file5 = open('name.text', 'a')
file5.write('小桥流水')
file5.close()
file6 = open('name.text')
print(file6.read())
file6.close()
'''
# 只读取一行
file7 = open('name.txt')

# (file7.readline())
print(file7.readline())
file7.close()
# 读取所有行加以区别(多行处理）
file8 = open('name.txt')
for line in file8.readlines():
    print(line)
    print('******')
file8.close()
# 文章读取后再次回到开头后再次读取（读取位置）
file9 = open('name.txt')
# file9.tell()
print('当前文件指针的位置 %s' % file9.tell())
print('当前读取到了一个字符,字符的内容是 %s' % file9.read(1))
# file9.tell()
print('当前文件指针的位置 %s' % file9.tell())

'''
# 第一个参数代表偏移位置，第二个参数 0 表示从文件开头偏移 1表示从当前位置偏移， 2表示从文件结尾偏移
file9.seek（5,0)
'''

file9.seek(0)
print('我们进行了seek操作')
print('当前文件指针的位置 %s' % file9.tell())
print('当前读取到了一个字符,字符的内容是 %s' % file9.read(1))
print('当前文件指针的位置 %s' % file9.tell())
file9.close()
