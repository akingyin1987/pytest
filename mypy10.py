class Person:

    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def say(self):
        print("my name is {0},性别：{1}，年龄：{2}".format(self.name, self.__sex, self.__age))


# 这是继承
class Student(Person):
    # 继承 格式： class 子类名(父类1，父类2....)
    def __init__(self, name, age, sex, score):
        # 实现父类的init方法
        # super(Student, self).__init__(name, sex, age)
        Person.__init__(self, name, age, sex)
        self.score = score

    def studentInfo(self):
        self.say()
        # 这两个方法效果一样
        super().say()
        Person.say(self)

        print("分数：{0}".format(self.score))

    def say(self):
        print("这是方法的重写(准确说应该是覆盖)：{0}".format(self.name))

    def __str__(self):
        print("重写——str——方法{0}".format(self.name))
        return "name={0},score={1}".format(self.name, self.score)


# p1 = Person("wangy", 18, "男")
# p1.say()
s1 = Student(name="wangy", age=19, sex="男", score=100)
s1.studentInfo()
s1.say()
# p1.say()
str(s1)

# mro 显示当当前类的结构
print(Person.mro())
print(Student.mro())
