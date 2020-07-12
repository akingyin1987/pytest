# 工厂模式


class CarFactory:

    def create_car(self, brand):

        if brand == "奔驰":
            return Benz()
        elif brand == "宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "无品牌无法创建"


class Benz:
    pass


class BMW:
    pass


class BYD:
    pass


c = CarFactory().create_car("宝马")


# 单例模式
class MySingleton:
    __obj = None
    __init_flat = True

    # 需要重写__new__ 方法
    def __new__(cls, *args, **kwargs):
        if cls.__obj is None:
            cls.__obj = object.__new__(cls)

        return cls.__obj

    def __int__(self, name):
        if MySingleton.__init_flat:
            self.name = name


a = MySingleton("a")
b = MySingleton("b")

print(dir(a))
print(a.name)
print(b)
