
#  常用的2个库是os.path 和 lib.path
import os  # 或者写成from os import path 没有重名的时候可以这样写
from pathlib import Path

print(os.path.abspath('.'))  # 根据相对路径的.来获取当前的绝对路径
print(os.path.abspath('..'))  # 表示相对路径，上一级的目录
print(os.path.exists('\下载'))  # 判断文件是否存在
print(os.path.isfile('\下载'))  # 判断是否是文件
print(os.path.isdir('\下载'))  # 判断是否是目录
# 需要较长的路径，要用路径的拼接，使用
# os.path.join('/tmp/a/', 'b/c')

from libpath import path

p = Path('.')
print(p.resolve())

print(p.is_dir())

# path可以创建文件
from pathlib import Path

q = Path('\下载/a/b/c')
Path.mkdir(q, parents=True)  # parents的功能是如果你的上一级目录不存在，在这里会自动创建，如果上一级目录存在，会创建成功
Path.rmdir(q)  # 只删除了c
q1 = Path('\下载/a/b')
Path.rmdir(q1)  # 删除了b
q2 = Path('\下载/a')
Path.rmdir(q2)  # 删除了a
# 删除的必须是空文件




# 同时执行

from pathlib import Path
q = Path('\下载/a/b/c')
Path.mkdir(q, parents=True)  # parents的功能是如果你的上一级目录不存在，在这里会自动创建，如果上一级目录存在，会创建成功
Path.rmdir(q)  # 只删除了c
q1 = Path('\下载/a/b')
Path.rmdir(q1)  # 删除了b
q2 = Path('\下载/a')
Path.rmdir(q2)  # 删除了a