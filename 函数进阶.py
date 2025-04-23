"""
#闭包函数
def funa():

    def outer(x):

        def inner(y):

            return x ** 2 + y

        return inner

    fs = []

    for i in range(1,4):

        fs.append(outer(i))

    return fs

f1,f2,f3 = funa()

print(f'{f1(1)},{f2(2)},{f3(3)}')

#nonlocal关键字
def outer():

    x = 100

    def inner():

        nonlocal x   #在嵌套函数内修改外部函数的局部变量(global是修改全局变量)

        x = 200

    inner()

    print(x)

outer()

#被装饰的函数含多个参数
def outer(funa):

    def inner(*args,**kw):

        funa(*args,**kw)

    return inner

def funa(*args,**kw):

    print(args)

    print(kw)

outer(funa)('haha','heihei',name = 'luo',age = 21)


#多个装饰器
def outer_1(fn):

    def inner_1():

        return '我' + fn() + '很晚'

    return inner_1      #第一个装饰器

def outer_2(fn):

    def inner_2():

        return '有一天' + fn() + '导致第二天很困'

    return inner_2     #第二个装饰器

@outer_2
@outer_1
def func():

    return '学习python知识'

print(func())          #多个装饰器的装饰过程，距离被装饰的函数最近的装饰器(outer_1)先装饰，距离远的装饰器(outer_2)后装饰.

#装饰器应用
import time

def outer(func):

    def inner(*args,**kw):

        start = time.time()

        res = func(*args,**kw)

        end = time.time()

        print(f"执行用时:{end - start:.2f}s")

        time.sleep(2)

    return inner

@outer
def download(filename):

    print(f"{filename}下载开始")

    time.sleep(5)

    print(f"{filename}下载完成")



@outer
def upload(filename):

    print(f"{filename}上传开始")

    time.sleep(6)

    print(f"{filename}上传结束")


download("mysql.py")
upload("python.py")

#取消装饰器的作用
from functools import wraps

import time

def outer(func):

    @wraps(func)    #wraps函数也是一个装饰器，可以保留被装饰之前的函数
    def inner(*args,**kw):

        start = time.time()

        res = func(*args,**kw)

        end = time.time()

        print(f"执行时间:{end - start:.2f}s")

    return inner

@outer
def download(filename):

    print(f"{filename}下载开始")

    time.sleep(5)

    print(f"{filename}下载完成")



@outer
def upload(filename):

    print(f"{filename}开始上传")

    time.sleep(5)

    print(f"{filename}上传结束")


download.__wrapped__("mysql.py")   #通过__wrapped__属性获得被装饰之前的函数
upload.__wrapped__("python.py")

#匿名函数与判断
#为真结果 if条件 else 为假结果
comp = lambda a,b : 'a比b小' if a < b  else 'a >= b'

res = [item for item in filter(lambda x:x > 3,[0,1,2,3,4,5,6,7,89])]    # item for item in filter是filter()函数的取值方式

print(res)

#匿名函数的应用
from functools import reduce    # reduce(func,iterable,initializer)initializer是初始值，即使序列为空，但是有初始值也会返回初始值并不会报错.

res = reduce(lambda x,y:x * y,[1,2,3,4])

print(res)

#映射函数map(func,seq)

res = map(lambda x:x * 10,[1,2,3,4,5])

print(list(res))

可迭代对象与迭代器

type()         #判断数据类型

isinstance(object,type)   #可以通过该函数确定继承关系，并且能用type()函数做判断的也可以用该函数。

from collections.abc import Iterable   #导入模块

print(isinstance('123',Iterable))    #True

list_1 = [1,2,3]

list_2 = iter(list_1) #iter()调用对象的__iter__(),并把__iter__()方法返回的结果作为自己的返回值

print(list_2)         #打印可迭代对象的内存地址

print(next(list_2))   #1

print(next(list_2))   #2

print(next(list_2))   #3

可迭代对象(范围大)与迭代器对象(范围小)的区别

str_1 = "hello python"

from collections.abc import Iterable,Iterator

print(isinstance(str_1,Iterable))   #True

print(isinstance(str_1,Iterator))   #False

str_1 = iter(str_1)                 #用iter()转换为迭代器对象(Iterator)

print(isinstance(str_1,Iterator))   #True

object拥有__iter__()方法是可迭代对象，拥有__iter__()与__next__()方法是迭代器对象

dir(obj)    #查找对象的属性方法

自定义迭代器类

class MyIterator(object):

    def __init__(self):

        self.x = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.x >= 15:

            raise StopIteration

        else:

            self.x += 1

            return self.x

my = MyIterator()

for i in my:

    print(i)

生成器函数与生成器表达式

生成器表达式与嵌套条件

nums = (x for x in range(21) if x % 2 == 0)   #直接创建一个生成器

for num in nums:

    print(num)

三元表达式与嵌套条件

nums = (x if x % 2 == 0 else 2 * x for x in range(21))

for i in nums:

    print(i)

多层嵌套

is_prime = lambda x:x > 1 and all(x % i != 0 for i in range(2,x))

res = (x for x in range(21) if is_prime(x))

for i in res:

    print(i)

生成器函数

def func(n):

    x = 0

    while x < n:

        yield x    # 暂停并返回当前值

        x += 2     # 恢复后从这里继续执行

for i in func(20):

    print(i)

生成器函数执行过程

1.暂停和恢复：生成器函数在遇到 yield 时会暂停执行，并返回一个值。

2.记住状态：暂停时，函数会记住当前的变量值和执行位置。

3.继续执行：下次调用时，从上次暂停的位置继续执行。

def func(n):

    x = 1

    while x < n:

        yield x

        x += 1

print(next(func(3)))   #1

print(next(func(3)))   #1

#注意:这两次打印结果一样是因为这本质上是在重新调用函数，所以当遇到yield时返回的值都是一样的，正确方式如下面所示。

f = func(3)

print(next(f))   #1

print(next(f))   #2
"""






