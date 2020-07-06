# 多态  没有严格意义上的多态
# 1、方法有多态，属性没有
# 2、方法重写


class Animal:
    def say(self):
        print("这是动物在说话")


class Dog(Animal):
    def say(self):
        print("这是狗在叫")


class Cat(Animal):
    def say(self):
        print("这是猫在叫")


def say(animal):
    if isinstance(animal, Animal):
        print(1)
        animal.say()
    elif isinstance(animal, Dog):
        print(2)
        animal.say()
    elif isinstance(animal, Cat):
        print(3)
        animal.say()


say(Dog())



