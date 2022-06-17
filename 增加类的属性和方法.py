class Player():  # 定义一个类
    def __init__(self, name, hp, occupation):
        self.__name = name  # 变量被称为属性    #当属性不被这个实例化引用的时候，在属性前加__,在方法里修改
        self.hp = hp
        self.occupation = occupation

    def print_role(self):  # 定义一个方法
        print('%s:%s %s' % (self.__name, self.hp, self.occupation))

    def Updatename(self, newname):
        self.newname = newname


class Monster():
    """ 定义一个怪物类 """
    pass  # 在这个类什么都不写又不让程序报错，可以加个pass


user1 = Player('tom', 100, 'warrior')  # 类的实例化
user2 = Player('jerry', 80, 'Master')

user1.print_role()
user2.print_role()

user1.updateName = 'wilson'
user1.print_role()


user1.__name = 'aaa'   # 不能通过赋值的方法去改变，要在类的方法里去修改这个属性
# print(user1.name)
user1.print_role()

