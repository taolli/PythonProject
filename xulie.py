# 序列包含字符串，元祖，列表
# 记录生肖，根据年份来判断生肖
"""
Chinese_zodiac = '羊猴狗猪鼠牛虎兔龙蛇马'
print(Chinese_zodiac[0:4])
year = 2022
print(year % 12)
print(Chinese_zodiac[year % 12])
print('虎' in Chinese_zodiac)
season_name = ('春季', '夏季', '秋季', '冬季')
season_month = ((12, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
for i in range(13):
    print(i)
for year in range(2020, 2022):
    print(year)
num = 4
while True:
    print(num)
    break
"""
# 列表推导式和字典推导式
# 求出1 到10 之间偶数的平方
alist = []
for i in range(1, 11):
    if (i % 2) == 0:
        alist.append(i*i)
print(alist)
alist = []
for i in range(1, 11):
    if i % 2 == 0:
        alist.append(i*i)
print(alist)
# 等价于
blist = [i * i for i in range(1, 11) if (i % 2) == 0]
print(blist)

z_num = {}
for i in z_num:
    z_num[0] = 0
z_num = {i: 0 for i in z_num}


'''
season_name = '春季'
season_month = (12, 1, 2)
for i in season_month:
    if i == 12:
    print (season _name)
'''

first_quarter = (1, 2, 3)
two_quarter = (4, 5, 6)
three_quarter = (7, 8, 9)
four_quarter = (10, 11, 12)
quarter_month = int(input('请输入月份:'))
if quarter_month in first_quarter:
    print('该月份为第一季度')
elif quarter_month in two_quarter:
    print('该月份为第二季度')
elif quarter_month in three_quarter:
    print('该月份为第三季度')
elif quarter_month in four_quarter:
    print('该月份为第四季度')
else:
    print('请重新输入月份')
season_name = ('春天', '夏天', '秋天', '冬天')  # print(type(season_name))
season_month = int(input('请输入月份:'))
if season_month in range(3, 6):
    print('该月份为春天')
elif season_month in range(6, 9):
    print('该月份为夏天')
elif season_month in range(9, 12):
    print('该月份为秋天')
elif season_month in (12, 1, 2):
    print('该月份为冬天')
else:
    print('月份无效')
# while循环语句
num = 6
while True:
    num -= 1
    if num > 4:
        print(num)
        break


