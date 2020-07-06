# 测试对象
# 浅拷贝
# 深拷贝

import copy


class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calculate(self):
        print("cpu 对象：", self)


class Screen:
    def show(self):
        print("screen对象：", self)


# 浅拷贝 被复制对象的对象类只会被引用
c1 = CPU()
s1 = Screen()
m1 = MobilePhone(c1, s1)
m2 = copy.copy(m1)


print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)

# 深拷贝 被复制的对象所有复制一次
m3 = copy.deepcopy(m1)
print(m1, m1.cpu, m1.screen)
print(m3, m3.cpu, m3.screen)
