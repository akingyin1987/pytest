# 异常
# -*- coding: UTF-8 -*-

import traceback

try:
    print("测试异常")
    a = 3 / 0

    # with 关键字，上下文管理器，系统自动管理资源,主要用于处理IO ，网络等
    with open("/Users/akingyin/Downloads/1.txt", "r") as f:
        content = f.readline()
        print("content={0}".format(content))

except ZeroDivisionError as e:
    print("出错了,{0}".format(e))

    # 将异常信息打印出来
    traceback.print_exc()
    # 将异常信息自动输出到指定文件
    with open("/Users/akingyin/Downloads/1.txt", "a") as f:
        traceback.print_exc(file=f)

except ValueError as e1:
    print("异常，不能将字符串转为数字")
except NameError:
    print("异常，变量不存在")
except BaseException as e:
    print("底级异常", e)
    # traceback 打印异常详情，需要导入
    traceback.print_exc()
else:
    print("没有进入异常，则会执行 else")
finally:
    print("无论是否发生异常，都会执行 finally 模块")

# fromat 函数

print("{0} {1}".format("hello", "work"))
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))

# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

# 保留N位有效数字  	{:.2f}
a = 3.1415928
b = 1
c = -1
print("保留两位有效数字：{0:.2f},{1:.2f}".format(a, b))

# 带符号 保留小数点后几位有效数字
print("带符号保留小数点后两位有效数字：{0:+.2f}".format(a))

# 带符号 保留小数点后几位
print("带符号：{0:+.2f}".format(c))

# 不带小数
print("不带小数：{0:.0f}".format(a))

# 数字补0（填充左边，宽度为2）
print("数字补零，填充左边{0:0>2d}".format(b))

# 数字补X （填充右边，宽度为2）
print("数字补零，填充左边：{0:x<2d}".format(b))

# 以逗号分隔的数字格式
print("以逗号分隔：{0:,}".format(100000))

# 百分比格式
print("百分比格式：{0:.2%}".format(0.24))

# 指数记法
print("指数记法：{0:.2e}".format(100000000))

# 进制
'{:b}'.format(11)  # 二进制
'{:d}'.format(11)  # 十进制
'{:o}'.format(11)  # 八进制
'{:x}'.format(11)  # 16进制
'{:#x}'.format(11)  # 16进制格式
'{:#X}'.format(11)  # 16进制大写格式
