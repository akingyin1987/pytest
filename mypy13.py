# 组合


class A1:
    def say(self):
        print("a1")


class B1(A1):
    pass


# 这是继承 （is-a 关系）
b = B1()
b.say()


# 把对象当成属性 ，通过组合的方式 （has-a 关系）
class B2:
    def __init__(self, a):
        self.a1 = a


b2 = B2(A1())
b2.a1.say()
