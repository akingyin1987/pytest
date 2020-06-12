# eval 函数  函数用来执行一个字符串表达式，并返回表达式的值。


"""
 expression -- 表达式。
globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。
"""
eval("print('abc')")

a = 1
b = 2
print(eval("a+b"))
print(eval("a+b", dict(a=10, b=39)))
print(eval("a+b", dict(a=10, b=39), locals()))
