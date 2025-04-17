"""
class Student(object):

    #__slots__ = ("name","score")     指定类中的属性,使类中只能有name与score属性,动态添加其他属性会引发异常

    def __init__(self,name,score):

        self.__name = name

        self.__score = score

    def info(self):

        print(f"学生信息:{self.__name},{self.__score}")

stu = Student("xm",100)
stu.sex = "男"                    # 动态添加类属性
print(f"info:{stu._Student__name},{stu.sex},{stu._Student__score}")   # 私有实例变量不能从外部直接访问是因为对外把__score变量改为了_Student__score,所以依然能够通过_Student__score访问__score变量

stu._Student__score = 90         # 可以通过给stu._Student__score赋值修改类内部的私有实例变量的值
print(f"info:{stu._Student__score}")


继承
class House:

    def __init__(self,name):

        self.name = name

    def run(self):

        print('马跑')

    def __show_info(self):

        print(f'马的名字:{self.name}')

class Donkey:

    def __init__(self,name):

        self.name = name

    def run(self):

        print('驴跑')

    def show_info(self):

        print(f'驴的名字:{self.name}')

    def roll(self):

        print('驴打滚')

class Mule(House,Donkey):

    def __init__(self,name,age):

        super().__init__(name)    #继承父类的属性name(父类的构造方法需要在子类的构造方法中专门调用)

        self.age = age

    def show_info(self):     #当子类与父类存在相同实例方法时，子类的方法会覆盖父类的方法。

        return '名字:{} 年龄:{}'.format(self.name,self.age)

m = Mule('骡宝莉',5)
m.run()
m.roll()
print(m.show_info())     #子类只会全部继承父类的非私有的功能(公有功能)，并且只能调用父类的非私有的功能。


多态统一性

class Animal(object):

    def eat(self):

        print('动物会觅食')

class Dog(Animal):

    def eat(self):

        print('狗会吃骨头')

class Cat(Animal):

    def eat(self):

        print('猫会吃猫粮')

def test(obj):    #定义一个统一的接口，实现一个接口多种实现。

    obj.eat()


异常处理

def exception(x,y):

    try:

        a = x / y

        print("a =",a)

    except Exception:   #万能异常Exception,捕获任意异常.

        print("出现异常,异常信息:被除数为0")

exception(2,0)  #虽然出现异常，但因为异常被捕获，所以后续的代码可以正常运行。

异常传递

def dunc(x,y):   #子函数

    res = x / y

    return res

def funa():     #主函数

    return dunc(10,0)

try:

    funa()

except Exception:

    print("出现异常")

print(funa())
"""