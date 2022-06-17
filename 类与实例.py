'''
# 面向过程编程
username1 = {'name': 'tom', 'hp': '100'}

username2 = {'name': 'jerry', 'hp': '80'}


def print_role(rolename):
    print('name is %s, hp is %s' % (rolename['name'], rolename['hp']))


print_role(username1)
print_role(username2)

'''


# 面向对象编程

class Player():  # 定义一个类        定义的类的名称大写
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def print_role(self):  # 定义一个方法
        print('%s：%s' % (self.name, self.hp))


user1 = Player('tom', 100)  # 类的实例化
user2 = Player('jerry', 80)

user1.print_role()
user2.print_role()
