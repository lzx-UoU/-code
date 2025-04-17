"""
python实现文件基本操作
try:

    path = 'C:\\Users\\15179\\hello.python.py1.py'

except:

    print("无法打开文件")

else:

    f_name = open(path,"w")

print(f_name.read())  #从文件开头开始读，没有指定读取字节数时，read()会读取文件中所有字节。

print(f_name.write("hello world!"))   # write()会把新写的内容覆盖掉原来的文件内容。

f_name = open(path,"r",encoding = 'UTF-8')

print(f_name.read())

f_name = open(path,"a")   # 新内容会写入已有内容后面，不会覆盖原有文件内容。

print(f_name.write("\nwelcome!"))   #如果追加的内容需要在下一行，只需要在追加的内容前面用换行符"\n"即可。

f_name = open(path,"r")

print(f_name.readline())   # readline()在读取到换行符时返回单行字符串，文件结尾时返回空字符串。

#如果传递给open函数的文件名不存在，"w"、"a"就会创建一个新的空文件，然后执行写入与追加。

path = 'C:\\Users\\15179\\hello.python.py1.py'

f_name = open(path,"w")

str_list = ['hello world\n','welcome\n','welcome']

print(f"{f_name.writelines(str_list)}")   # writelines()把所有字符串写入文件中

对文件按行操作
def read_file(path):

    with open(path,"r") as f:

        for line in f:

            yield line.strip()    #一次只读取一行内容防止资源浪费.

for line in read_file("xxx.txt"):

    print(f"{line}")

使用fileInput实现懒加载式迭代

import fileInput

path = 'C:\\Users\\15179\\python语言基础.py'

for line in fileInput.input(path):    #文件的打开与关闭被封装在input方法内部

    print(f"{line}")

对象的序列化和反序列化

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

import json
#将字典处理成JSON格式（以字符串形式存在）
my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
print(json.dumps(my_dict))


import json
#将字典处理成JSON格式并写入文本文件,执行下面的代码，会创建data.json文件
my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open("data.json","w") as file:

    json.dump(my_dict,file)


# 读取下面创建的data.json文件，将JSON格式的数据还原成Python中的字典.
with open("data.json","r") as file:

    print(json.load(file))

读写csv文件
import random
import csv

with open("scores.csv","w") as file:

    writer = csv.writer(file)   #csv.writer()返回一个writer对象,通过对象的writerow方法写入csv文件.

    writer.writerow(["姓名","语文","数学","英语"])

    names = ["荣耀","华为","苹果","联想"]

    for name in names:

        scores = [random.randint(60,101) for _ in range(3)]

        scores.insert(0,name)   #把姓名插入到列表开头,形成[姓名 语文 数学 英语]形式.

        writer.writerow(scores)

with open("scores.csv","r") as file:

    reader = csv.reader(file)   #csv.reader()创建一个迭代器,通过循环遍历读取文件数据.

    for data_list in reader:    #对csv.reader()对象循环取值时,返回的是列表对象,该列表对象包含一行中所有的字段.

        for i in data_list:     #把列表对象中的字段元素取出.

            print(i,end = "\t")

        print()

#文件定位操作

with open("data.txt","w") as file:

    file.write("hello world,hello pycharm")

with open("data.txt", "r") as file:

    file.read()

    position = file.tell()    #tell()返回文件内的当前位置

    print(position)

    position = file.seek(0,0)   #seek(offset [,from])方法改变当前文件的位置.offset变量表示要移动的字节数.From变量指定开始移动字节的参考位置.
                                #如果from被设为0,这意味着将文件的开头作为移动字节的参考位置.如果设为1,则使用当前的位置作为参考位置.如果它被设为2,那么该文件的末尾将作为参考位置.
    print(file.read())
"""