# 两种打开文件和读取方法

file = open('name.txt')
try:
    for line in file:
        print(line)
finally:
    file.close()


with open('name.txt') as f:
    for line in f:
        print(line)
