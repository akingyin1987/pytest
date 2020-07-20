# open 函数

# open("文件名",打开方式)
# R = 读 read 模式  w = 写模式，如果文件不存在则会创建
# a = 追加模式  如果文件不存在则会创建，存在则会在最后追加


def writeFileInfo():
    try:
        f = open(r"/Users/akingyin/Downloads/1.txt", "a")
        f.write("这是我写入的数据\n")
        f.close()

    except FileNotFoundError as e:
        print(e)


def openReadFileInfo():
    try:
        with open("/Users/akingyin/Downloads/1.txt", "r") as f:
            line = f.readline()
            readData = [line]

            while line:
                line = f.readline()
                readData.append(line)
                print("str={0}".format(line))
            print("data->{0}".format(readData))
            f.close()
    except FileNotFoundError as e:
        print("1")


writeFileInfo()
openReadFileInfo()
