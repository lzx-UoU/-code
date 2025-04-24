"""
1.filemode:'r'

with open(path,"r") as file:

    file.read()               # 从文件开头开始读,没有指定读取字节数时,read()会读取文件中所有字节

    file.readline()           # readline() 在读取到换行符时返回单行字符串,文件结尾时返回空字符串
    
2.filemode:'w'

str_list = ['hello world','welcome']

with open(path,"w") as file:

    file.write("hello")         # write() 写入的内容覆盖原文件所有内容

    file.writelines(str_list)   # writelines() 把字符串写入文件中
    
3.filemode:'a'

with open(path,"a") as file:

    file.write("hello")         # 追加新内容至指定文件中

如果传递给open函数的 path 不存在,"w"、"a"就会创建一个新的空文件,然后执行写入与追加操作

4.对象的序列化和反序列化

dump - 将Python对象按照JSON格式序列化到文件中
dumps - 将Python对象处理成JSON格式的字符串
load - 将文件中的JSON数据反序列化成对象
loads - 将字符串的内容反序列化成Python对象

import json

dict = {'friends': ['王大锤', '元芳']}

print(json.dumps(dict))


import json

dict = {'name': '骆昊','friends': ['王大锤', '白元芳']}

with open(path,"a") as file:

    json.dump(dict,file)

将字典处理成JSON格式并写入文本文件,并创建data.json文件

with open("data.json","r") as file:

    print(json.load(file))

读取创建的data.json文件,将JSON格式的数据还原成Python中的字典


5.读写csv文件

import random
import csv

with open("scores.csv","w") as file:

    writer = csv.writer(file)        # csv.writer() 返回一个writer对象,通过对象的writerow方法写入csv文件

    writer.writerow(["姓名","语文","数学","英语"])

    names = ["荣耀","华为","苹果","联想"]

    for name in names:

        scores = [random.randint(60,101) for _ in range(3)]

        scores.insert(0,name)       # 把姓名插入到列表开头,形成 [姓名 语文 数学 英语]

        writer.writerow(scores)

with open("scores.csv","r") as file:

    reader = csv.reader(file)       # csv.reader()创建一个迭代器

    for data_list in reader:        # 对csv.reader() 对象循环取值时,返回的是列表对象,该列表对象包含一行中所有的字段

        for i in data_list:         

            print(i,end = "\t")

        print()


6.文件定位操作

with open("data.txt","w") as file:

    file.write("hello world,hello pycharm")

with open("data.txt", "r") as file:

    file.read()

    print(file.tell())             # tell() 返回当前文件内的当前定位

    position = file.seek(0,0)      # seek(offset [,from]) 改变当前文件的当前定位,offset变量表示要移动的字节数, [,from] 指定开始移动字节的参考位置
                                     如果 [,from] 设为0,把文件的开头作为移动字节的参考位置
                                                  设为1,则使用当前的位置作为参考位置
                                                  设为2,把文件的末尾作为参考位置
    print(file.read())
"""
