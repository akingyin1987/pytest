# try:
#     with open(r"1.txt", "w", encoding="utf-8") as f:
#         strs = ("1", "2", "3")
#         f.writelines(strs)
# except BaseException as e:
#     print(e)
# finally:
#     print("这里就不需要关闭了，用了with 会自动关闭")

with open(r"1.txt", "r", encoding="utf-8") as f:
    str1 = f.read(2)  # 读取一个字符,不传参数则会读取完
    print("str=" + str1)
    #  str1 = f.readline()  # 读取一行

    # 按每行遍历  方式1 至到读取的为空
    while True:
        fragment = f.readline()
        if not fragment:
            break
        else:
            print(fragment, end="")

with open(r"1.txt", "r", encoding="utf-8") as f:
    # 通过迭代器自动读取每一行
    for a in f:
        print(a, end="迭代器")
