# 浅拷贝与深拷贝

import copy


def testCopy():
    """
     浅拷贝只复制当前对象属性，即只复制自己
    :return:
    """
    a = [10, 20, 30, [1, 2]]
    b = copy.copy(a)
    print(a)
    print(b)
    print("这是浅拷贝")
    b.append(30)
    b[3].append(2)
    print(a)
    print(b)


def testDeepCopy():
    a = [1, 2, 3, [10, 20, 30]]
    b = copy.deepcopy(a)

    print(a)
    print(b)
    print("深拷贝")

    b.append(4)
    b[3].append(40)
    print(a)
    print(b)


testDeepCopy()


def add(a, b, c=20):
    """
     默认值参数必须放到最后
    :param a:
    :param b:
    :param c:
    :return:
    """
    return a + b + c


print(add(1, 2))

# 全名参数调用
print(add(c=1, b=2, a=3))


def fun1(a, b, *c):
    """
    一个星号表示可变参数 即 元组
    :param a:
    :param b:
    :param c:
    :return:
    """
    print(a, b, c)
    for x in c:
        print(x)


fun1(1, 2, 3, 4, 5, 6)


def fun2(a, b, **c):
    """
     两个星号表示 字典
    :param a:
    :param b:
    :param c:
    :return:
    """
    print(a, b, c)
    for k, v in c.items():
        print(k, v)


fun2(1, 2, name="1", age=3, bus="33333")

# lambda 表达式的基本语法 lambda arg1,arg2,arg3... : <表达式>

f = lambda a, b, c: a + b + c

print(f(1, 2, 3))

g = [lambda a: a * 2, lambda b: b * 3, lambda c: c * 4]
print(g[0](1), g[1](2), g[2](3))

