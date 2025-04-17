"""
素数的输出

n1 = int(input("请输入前范围的数"))

n2 = int(input("请输入后范围的数"))

fs = []

def is_prime(num):

    if num < 2:

        return False

    for j in range(2,num):

        if num % j == 0:

            return False

    return True

for i in range (n1,n2 + 1):

    if is_prime(i):

        fs.append(i)

print("素数列表:",fs)


斐波那契数列

def fibo(num):

    if num == 1:

        return [0]

    elif num == 2:

        return [0,1]

    else:

        fs = [0,1]

        for i in range(2,num):

            fs[i - 1] + fs[i - 2]

            fs.append(fs[i - 1] + fs[i - 2])

    return fs

num = int(input("请输入一个自然数"))

print(f"{fibo(num)}")


出行建议

class WeatherSearch(object):

    def __init__(self, input_time):

        self.input_time = input_time

    def search_visibility(self):

        visibility = 0

        if self.input_time == "daytime":

            visibility = 2

        if self.input_time == "night":

            visibility = 7

        return visibility

    def search_temp(self):

        temp = 0

        if self.input_time == "daytime":

            temp = 26

        if self.input_time == "night":

            temp = 16

        return temp


class OuterAdvice(WeatherSearch):

    def __init__(self, input_time):

        WeatherSearch.__init__(self, input_time)

    def search_temp(self):   # 重写父类的方法

        vehicle = " "

        if self.input_time == "daytime":

            vehicle = "bike"

        if self.input_time == "night":

            vehicle = "taxi"

        return vehicle

    def advice(self):

        visibility = self.search_visibility()

        if visibility == 2:

            print("天气很好适合出门")

        elif visibility == 7:

            print("天气一般不建议出门")

        else:

            print("超出我的建议能力范围无法给你建议")

check = OuterAdvice("night")
print(check.search_temp())
check.advice()

思路:父类封装能见度与温度两个方法,子类继承父类的方法.子类可以自定义方法或重写父类方法,实现自身需求.子类重写父类的search_temp方法实现自己的需求,继承父类search_visibility方法返回整体的建议



工资结算系统
class Employee(object):

    def __init__(self,name):

        self.name = name

    def monthly_salary(self):

        pass

class BM(Employee):

    def __int__(self,name):

        super().__init__(name)

    def monthly_salary(self):

        return 15000

class Programmer(Employee):

    def __int__(self,name,working_hour = 0):

        super().__init__(name)

        self.working_hour = working_hour

    def monthly_salary(self):

        return 200 * self.working_hour

class Salesman(Employee):

    def __init__(self,name,sales = 0):

        super().__init__(name)

        self.sales = sales

    def monthly_salary(self):

        return 1800 + self.sales * 0.05

map = {}

for emp in map:

    if isinstance(emp,Programmer):

        emp.working_hour = int(input(f"请输入{emp.name}工作时长: "))

        print(f"本月工资为:{emp.monthly_salary()}元")

    elif isinstance(emp,Salesman):

        emp.sales = float(input(f"请输入{emp.name}的销售额: "))

        print(f'本月工资为:{emp.monthly_salary():.2f}元')

思路:子类通过对父类方法的继承与重写实现子类自身的任务实现.有两个子类需要传入变量值计算函数结果,使用 isinstance()函数判断员工对象的类型再算出他们各自的工资


扑克牌游戏
import  random

class Card(object):

    def __init__(self,suit,rank):

        self.suit = suit    #初始化花色

        self.rank = rank    #初始化点数

    def __str__(self):

        return f"{self.rank['value']} of {self.suit}"

class Deck(object):

    def __init__(self):

        self.cards = []

    def build(self):

        suits = ["Hearts","Diamonds","Clubs","Spades"]

        ranks = [
            {"value":"3","score":3},
            {"value":"4","score":4},
            {"value":"5","score":5},
            {"value":"6","score":6},
            {"value":"7","score":7},
            {"value":"8","score":8},
            {"value":"9","score":9},
            {"value":"10","score":10},
            {"value":"J","score":11},
            {"value":"Q","score":12},
            {"value":"K","score":13},
            {"value":"A","score":14},
            {"value":"2","score":15},
        ]

        for suit in suits:

            for rank in ranks:

                self.cards.append(Card(suit,rank))

    def shuffle(self):    #洗牌方法

        random.shuffle(self.cards)

    def deal(self):       #摸牌方法

        if len(self.cards) == 0:

            return None

        return self.cards.pop()

class Player(object):

    def __init__(self,name):

        self.name = name

        self.hand = []   #初始化玩家手中的手牌

    def draw(self,Deck):

        self.hand.append(Deck.deal())   #调用摸牌方法

    def show_hand(self):

        print(self.hand.pop())

    def discard(self,index):    #弃牌方法

        if len(self.hand) == 0:

            return None

        return self.hand.pop(index)

class PokerGame(object):

    def __init__(self):

        self.players = []

        self.deck = Deck()

    def player(self,name):

        self.players.append(Player(name))

    def start_game(self):

        pass

    def play_round(self):

        pass

    def victory(self):

        pass

if __name__ == "__main__":

    pass

思路:完成一个扑克牌游戏的构建上需要定义Card、Deck、Player、PokerGame类,然后根据定义的类在内部构造需要实现的函数
"""















        

        

                
