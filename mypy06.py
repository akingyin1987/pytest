# 递归

def factoriald(num):
    if num <= 1:
        return 1
    else:
        return num * factoriald(num - 1)


print(factoriald(10))


def factoriald1(num):
    a = 1
    for x in range(1, num + 1):
        a = a * x
    print(a)


factoriald1(10)


# 嵌套函数

def fun1():
    print(" fun 1 ")

    def fun2():
        print(" fun 2")

    fun2()


fun1()

# nonlocal 关键子，声明外部函数的局部变量 与 global 关键字一样

a = 10


def outer():
    b = 10

    def inner():
        nonlocal b
        global a
        print(b)
        a = 20
        b = 30
    inner()
    print("{0},{1}".format(a, b))

outer()
