"""
闭包函数
def active():

  def outer(x):

    def inner(y):

      return x ** 3 + y
    
    return inner
  
  arr = []

  for x in range(1,6):

    arr.append(outer(x))

  return arr

f1,f2,f3,f4,f5 = active()

print(f"{f1(1)},{f2(2)},{f3(3)},{f4(4)},{f5(5)}")


nonlocal关键字
def outer_function():

  num = 10
  
  def inner_function():
  
    nonlocal num      # 不使用全局变量的情况下，内层函数可以方便的修改外层函数的变量值
    
    num += 5
    
    return num
    
  return inner_function
  
ans = outer_function()

print(ans())


被装饰的函数含多个参数
def outer_function(func):

  def inner_function(*args,**kw):

    func(*args,**kw)

  return inner_function

def func(*args,**kw):

  print(args)        # 注意不要把*传入 ('java', 'python', 'javascript')
  print(kw)          # {'a': 10, 'b': 20, 'c': 30}

outer_function(func)('java','python','javascript',a = 10,b = 20,c = 30)


多个装饰器
def outer_function_1(func):

    def inner_function_1():

        return "python" + func()
    
    return  inner_function_1      # 第一个装饰器

def outer_function_2(func):

    def inner_function_2():

        return "javascript" + func()

    return inner_function_2        # 第二个装饰器

@outer_function_1
@outer_function_2
# 多个装饰器的装饰过程,距离被装饰函数最近的装饰器先装饰,距离远的装饰器后装饰.
def func():

    return "Vue.js"

print(func())    # pythonjavascriptVue.js


应用装饰器
import time

def outer_function(func):

  def inner_function(*args,**kw):

    time_start = time.time()

    func(*args,**kw)

    time_end = time.time()

    print(f"程序执行用时:{time_end - time_start:.2f}s")

    time.sleep(2)

  return inner_function

@outer_function
def download(filename):

  print(f"{filename}开始下载！")

  time.sleep(5)

  print(f"{filename}下载完成！")

@outer_function
def upload(filename):

  print(f"{filename}开始上传！")

  time.sleep(5)

  print(f"{filename}上传完成！")

download("javascript.py")
upload("python.py")


取消装饰器的作用
from functools import wraps
import time

def outer(func):
    @wraps(func)      # wraps函数也是装饰器,可以保留被装饰之前的函数
    def inner(*args,**kw):

        time_start = time.time()

        func(*args,**kw)

        time_end = time.time()

        print(f"执行时间:{time_end - time_start:.2f}s")

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

# 通过__wrapped__属性获得被装饰之前的函数
download.__wrapped__("javascript.py") 
upload.__wrapped__("python.py")


匿名函数中执行判断
# 为真结果 if条件 else 为假结果
comp = lambda a,b : 'a比b小' if a < b  else 'a >= b'


匿名函数的应用
from functools import reduce    # reduce(func,iterable,initializer)initializer是初始值,即使序列为空,但是有初始值也会返回初始值并不会报错.
res = reduce(lambda x,y:x * y,[1,2,3,4])
print(res)

res = [item for item in filter(lambda x:x > 3,[0,1,2,3,4,5,6,7,89])]    # item for item in filter是filter()函数的取值方式
print(res)


映射函数map(func,seq)
res = map(lambda x:x * 10,[1,2,3,4,5])
print(list(res))


可迭代对象与迭代器
isinstance(object,type)   #  通过该函数确定继承关系,并且能覆盖type()函数判断数据类型的作用

from collections.abc import Iterable
print(isinstance('123',Iterable))    #  True


list_1 = [1,2,3]
list_2 = iter(list_1)     #  iter()调用对象的 __iter__ 方法,并把 __iter__ 方法返回的结果作为自己的返回值

print(next(list_2))   #  1
print(next(list_2))   #  2
print(next(list_2))   #  3


可迭代对象(范围大)与迭代器对象(范围小)区别
对象拥有 __iter__() 方法是可迭代对象,拥有 __iter__ 与 __next__ 方法是迭代器对象.
dir(obj)      #  查找对象的属性方法
from collections.abc import Iterable,Iterator

str = "JavaScript"
print(isinstance(str,Iterable))    #  True  可迭代对象
print(isinstance(str,Iterator))    #  False   可迭代对象

str = iter(str)                    #  用 iter() 转换为迭代器对象
print(isinstance(str_1,Iterator))  #  True  迭代器对象


实现自定义迭代器
class Iterator(object):

    def __init__(self):

        self.num = 0

    def __iter__(self):

        return self         # 实现 __iter__ 方法,返回迭代器对象本身

    def __next__(self):     # 实现 __next__ 方法

        if self.num >= 15:

            raise StopIteration

        self.num += 5

        return self.num

It = Iterator()

for i in It:
    
    print(i)


生成器函数与生成器表达式

生成器表达式与嵌套条件
nums = (x for x in range(20) if x % 2 == 0)     #  创建生成器
for num in nums:
    print(num)


三元表达式与嵌套条件
nums = (x if x % 2 == 0 else 2 * x for x in range(20))
for i in nums:
    print(i)


多层嵌套
is_prime = lambda x:x > 1 and all(x % i != 0 for i in range(2,x))
res = (x for x in range(20) if is_prime(x))
for i in res:
    print(i)


生成器函数
def func(n):

    x = 0

    while x < n:

        yield x      # 暂停并返回当前值

        x += 2       # 恢复后从这里继续执行

for i in func(20):

    print(i)


生成器函数执行过程
1.暂停和恢复:生成器函数在遇到 yield 时会暂停执行,并返回一个值
2.记住状态:暂停时,函数会记住当前的变量值和执行位置
3.继续执行:下次调用时,从上次暂停的位置继续执行

"""
