import time
# time模块进行日期和时间查看
print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d'))    # 使用格式化输出
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y%m%d'))

import datetime
# datetime用于日期和时间的修改
print(datetime.datetime.now())
new_time = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + new_time)

one_day = datetime.datetime(2021, 6, 27)
new_day = datetime.timedelta(days=10)
print(one_day + new_day)

new_time = datetime.timedelta(hours=10)
print(datetime.datetime.now() + new_time)


# 数学相关库 math 和 random
# random是一个产生随机数的一个库  用于软件测试和密码学

import random
print(random.randint(1, 5))
print(random.choice(['as', 'de', 'er']))

# random是根据有限定条件的抽取出想要的随机数

# 使用命令行对文件夹和文件操作  常用的库是os.path 和 path.lib

# ls  查看文件中的内容
# ls-l 查看文件和文件夹  开头是—的是文件，以d开头的是文件夹
# pwd 查看当前位置
# cd \ 绝对路径，\代表根目录
# cd ..  访问上一级目录   相对路径
# mkdir a  创建文件夹  mkdir/tmp/a/b/c/d
# mkdir -p  创建一个文件件
# rmdir 删除文件夹
# rm-rf 删除多级文件夹



