# 类
class Student:
    company = "这是类属性"  # 类属性所有实例对象都可访问

    count = 0

    # 这是类的构造函数
    def __init__(self, name="gg", age=19, sex="男"):
        self.name = name
        self.age = age

        # 以两个下划线定义的属性 为"私有"属性
        # 可以通过：下划线+类名+属性名访问（实际上 此属性名即是承的这名称，可通过 dir 方法查看）
        self.__sex = sex

    # 第一个参数必须是当前实例
    def say(self):
        Student.count = Student.count + 1
        print("{0}说，我的年龄是：{1}，显示类属性{2},调用次数{3}"
              .format(self.name, self.age, Student.company, Student.count))

    # 类方法,第一个参数必须是当前类
    @classmethod
    def testClass(cls):
        print("这是类方法:{0}".format(cls.company))

    # 这是静态方法，不需要类或实例参数
    @staticmethod
    def add(a, b):
        print(a + b)

    def __fun2(self, a, b):
        print("这是私有方法{0},{1},{2},{3}".format(a, b, self.name, self.__sex))

    # property 装饰器，使用起来与属性一致(实际上存的是方法名的属性)，主要 提供 get set 方法
    @property
    def getName(self):
        return self.name

    # 相当于为getName 赋值
    @getName.setter
    def getName(self, name):
        self.name = name
        print("这是set 方法,name={0}".format(name))

    # def setName(self, name):
    #     print("这是set 方法,name={0}".format(name))
    #     self.name = name



s1 = Student(age=22)

# idea  是不会给提示的，所以不建议用此方法使用
print(s1._Student__sex)
s1._Student__fun2(2, 3)
s1.say()
print(id(s1.say()))

# 将对象模具富裕 stu
stu = Student
s2 = stu(name="wang", age=11)
s2.getName = "1233333"
s2.say()
s2.testClass()
print("这是装饰器={0}".format(s2.getName))

s2.add(1, 2)

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
