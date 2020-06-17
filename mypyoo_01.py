# 类
class Student:

    # 这是类的构造函数
    def __init__(self, name="gg", age=19):
        self.name = name
        self.age = age

    def say(self):
        print("{0}说，我的年龄是：{1}".format(self.name, self.age))


s1 = Student(age=22)
s1.say()
print(id(s1.say()))

# 解释器会翻译成以下执行
Student.say(s1)
print(id(Student.say(s1)))

# 获取所有属性
print(dir(s1))

# 获取属性字典
print(s1.__dir__())


# pass 空语句

def funPass():
    pass


# 判断 实例 是否是此类的
print(isinstance(s1, Student))
