# _del_ 析构函数主要用来对象销毁，
# _call_  可调用方法

# python 方法没有重载，相同名的方法以最后的一个为有效，


class Person:

    def __del__(self):
        print("销毁对象：{0}".format(self))

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("name={0},age={1}".format(self.name, self.age))

    def say(self, name1):
        print("name={0},name1={1}".format(self.name, name1))

    def __call__(self, *args, **kwargs):
        print("这是call方法：{0}，{1}".format(args, kwargs))


def play_game(person):
    print("{0}在玩游戏".format(person.name))


p1 = Person("1", "2")

# 方法或函数实际上调用的是 __call__函数


# 以第二个相同名字的方法为有效
p1.say("2")

play_game(p1)

# 将play_game 方法赋予 Person  方法的动态性
Person.play_game = play_game

p1.play_game()

Person.play_game(p1)


def say(person):
    print("这是方法的修改")


# 类的原方法已被个性替换
Person.say = say

p1.say()

# 调用了call 方法
p1(1, 2, 3, name=1, age=2, b=3)

# 回收此对象
del p1
