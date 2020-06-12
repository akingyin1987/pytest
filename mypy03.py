import math


def add(a, b):
    '''p这是函数说明，可以用help 调用'''
    print("*" * 10)
    return a + b


help(add.__doc__)

print(id(add))
print(type(add))
value = add("1", "2")
print(value)


def dis(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def sqr(x, y):
    return math.sqrt(x ** 2 + y ** 2)


print(dis(0, 0, 3, 4))
print(sqr(3, 4))

testfun = add
print(testfun(1, 2))

a = 100  # 全局变量 一般当作常量使用，作用域为当前模块


def fun01():
    """
     11111111111111
    :return:
    """
    b = 1
    a = 1
    add(a, b)
    print(locals())
    print(globals())


fun01()
