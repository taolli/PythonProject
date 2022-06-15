import re

# 读取文中的人物名称
f = open('name.txt')
data = f.read()
data0 = data.slipt('|')

# 读取武器名称
f2 = open('weapon.txt')
data2 = f2.read()
i = 1
for line in f2.readlines():
    if i / 2 == 1:
        print(line.strip('\n'))
        i += 1
f3 = open('san guo.txt', encoding='GB18030')
print(f3.read().replace('\n', ''))


# 重复出现次数较多的功能或者操作可以用函数表示

def func(filename):
    print(open(filename).read)
    print('fun test')


# 变量有多个参数时，可以写成
func('name.txt')


def find_item(hero):
    with open('san guo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        print('主角 %s 出现的 %s 次数' % (hero, len(name_num)))

    return len(name_num)


# 读取人物的信息
name_dict = {}
with open('name.txt') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            print(n)
        name_num = find_item(n)
        name_dict[n] = name_num

name_sorted = sorted(name_dict.items(), key=lambda item: (item[1]), reverse=True)
print(name_sorted[0:10])


def find_main_charecters(charecter_name):
    with open('san guo.txt', encoding='GB18030'):
        data = f.read().replace('\n', '')
        name_num = re.findall(charecter_name, data)
        # print('主角 %s 出现了%s 次' %(charecter_name, len(name_num))
        return charecter_name, len(name_num)
name_dict = {}
with open('name.txt', encoding='utf-8') as f:
    for line in f:
        names = line.slipt('|')
        for n in names:
            char_name, char_number = find_main_charecters()
            name_dict[char_name] = char_number
weapon_dict ={}
with open('weapon.txt', encoding='utf-8') as f:
    i = 1
    for line in f:
        if i/2 == 1:
            weapon_name, weapon_number = find_main_charecters(line.strip())
            weapon_dict[weapon_name] = weapon_number
            i += 1

weapon_sorted = sorted(weapon_dict.items(), key=lambda item: (item[1]), reverse=True)
print(weapon_sorted[0:10])
