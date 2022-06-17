class Monster():
    # 定义怪物类
    def __init__(self, hp=100):  # hp=100是一个初始化的一个值
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物')


class Animals(Monster):  # 继续父类，要在定义类里写上父类
    # 定义普通类
    def __int__(self, hp=1000):
        super().__init__(hp)


class Boss(Monster):
    # boss类怪物
    def _init__(self, hp=200):
        super().__init__(hp)

    def whoami(self):
        print('我是怪物我怕谁')


a1 = Monster(200)
print(a1.hp)
print(a1.run())
a2 = Animals(400)
print(a2.hp)
print(a2.run())
a3 = Boss(800)
a3.whoami()

print('a1的类型是 %s' % (type(a1)))
print('a2的类型是 %s' % (type(a2)))
print('a3的类型是 %s' % (type(a3)))

print(isinstance(a2, Monster))   # 判断父类的关系

print(isinstance(a2, Boss))

# 列表，字符串....都是类 他们的类都是object

print(isinstance('abc', object))
