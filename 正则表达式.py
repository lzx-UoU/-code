"""
正则表达式语法

1.  re.match(<regex>,<string>)     匹配字符串开头,如果匹配成功,返回match对象,否则返回None

2.  re.search(<regex>,<string>)    扫描查找模式匹配的第一个位置,找到匹配项则返回match对象,否则返回None

3.  re.findall(<regex>,<string>)   返回字符串中所有正则表达式匹配项的列表

    re.findall(r'#(\w+)#', '#foo#.#bar#.#baz#')    

    for i in re.finditer(r'#(\w+)#', '#foo#.#bar#.#baz#'):

        print(i)

4.  re.finditer(<regex>,<string>)   在字符串中找到正则表达式所匹配的所有子串,并把它们作为一个迭代器返回,通过循环获得匹配项

5.  re.sub(<regex>, <repl>, <string>,count)     将字符串的匹配部分替换为指定的替换字符串,count指定替换的最大次数,默认值为0,表示替换所有匹配项
    re.sub(r'(\w+),bar,baz,(\w+)',r'\2,bar,baz,\1','foo,bar,baz,qux')

    <repl>可以是一个函数,该函数接受一个匹配对象作为参数,并返回一个字符串,该字符串将替换匹配项


6.断言

正向断言:(?=...),用于断言当前匹配位置的右侧是否满足某个条件,如果满足则匹配成功
负向断言:(?!...),用于断言当前匹配位置的右侧是否不满足某个条件,如果不满足则匹配成功
反向肯定断言:(?<=...),用于断言当前匹配位置的左侧是否满足某个条件,如果满足则匹配成功
反向否定断言:(?<!...),用于断言当前匹配位置的左侧是否不满足某个条件,如果不满足则匹配成功

断言必须指定固定长度的匹配项,不能使用量词,否则会报错
re.search('(?<=a{m,n})xx', 'aaaxx')

7.编译正则表达式

    re_emile = re.compile(r'^[0-9a-zA-Z\_]{0,11}\@\d+\.(com|cn)$')    预编正则表达式
    re_emile.match(<string>)     支持对字符串切片搜索


正则表达式细节

1.  re.search('^From', 'From Here to Eternity').span()          返回匹配成功对象的开始索引、结束索引
    re.search('^From', 'From Here to From Eternity')           '^From'匹配式,匹配的是开头的'From',不匹配句中的'From','\A'作用类型于'^'

2.  re.search('bar$', 'foobar')                                '$'表示匹配字符串的结尾,所以'bar$'匹配的是'foobar'中的'bar','\Z'作用类型于'$'

3.  re.search(r'\bclass\b','no class at all classroom')        \b表示单词边界,所以只匹配'class'.
    re.search(r'\Bfoo\B', 'barfoobaz')                         \B表示非单词边界,所以只匹配'foo'.

4.  re.search('\.', 'foo.bar')          '.'是正则表达式中的特殊字符,表示匹配任意字符,所以要匹配'.'本身,需要使用转义字符'\'
    re.search(r'\.', 'foo.bar')         'r'是原生字符串,作用是让字符串中的'\'当成普通字符处理

5.贪婪匹配

    re.search('<.+>', '%<foo> <bar> <baz>%')      默认情况下,正则表达式中的量词都是贪婪匹配
    re.search('<.+?>', '%<foo> <bar> <baz>%')     在量词后面加上'?'把贪婪匹配改为非贪婪匹配

6.  re.search('x-{3}x', 'x---x')
    re.search('x{foo}y', 'x{foo}y')           当{m,n}作为匹配表达式,如果省略m、n和逗号,则大括号不再用作元字符
    re.search('x{a:b}y', 'x{a:b}y')

7.捕获组
    
    groups():返回一个元组,其中包含从正则表达式匹配中捕获的所有组
    group(n1,n2,...):返回一个字符串,只包含第<n1><n2>...个捕获的匹配项,如果省略n或者n = 0,则包含从正则表达式匹配中捕获的所有组

8.创建非捕获组(?:<regex>)

    re.search('(\w+),(?:\w+),(\w+)', 'foo,quux,baz')   只捕获第一个和第三个分组,第二个分组不捕获

9.指定注释(?#...)

    re.search('bar(?#This is a comment) *baz', 'foo bar baz qux')   注释不会影响正则表达式的匹配,注释内容不会被捕获

10.指定要匹配的一组分项选择('|'...)

    re.search('foo|grault', 'foograult')

11.创建命名分组(?P<name>...)

    m = re.match(r"(?P<year>\d{4})-(?P<month>\d{2})", "2023-10")
    m.group("year"/"month")            可以通过其符号名称来获取特定捕获的组

12.使匹配不区分大小写(re.I)
    re.search('a+', 'aaaAAA', re.I)    可以匹配'aaaAAA'

13.使字符串开头和字符串结尾的锚点在嵌入的换行符处匹配(re.M)
    re.search('^baz', 'foo\nbar\nbaz')
    re.search('^bar', 'foo\nbar\nbaz', re.M)       上面正则表达式匹配失败,下面正则表达式匹配成功

14.使'.'元字符匹配换行符(re.S、re.DOTALL)
    re.search('foo.bar', 'foo\nbar', re.DOTALL/re.S)
    re.search('foo.bar', 'foo\nbar')  

15.match对象的属性和方法

    match.group([<group1>, ...])      从匹配项中返回指定的捕获组(捕获的组从1开始),使用多个参数,返回指定的所有组的元组,给定的参数可以多次出现,可以按任意顺序指定任何捕获的组
    match.span([<grp>])               返回匹配项的开始索引和结束索引,如果指定<grp>,则返回给定组的开始、结束索引,如果没有指定<grp>,则返回整个匹配项的开始、结束索引


import re

def f(object):

    s = object.group(0)

    if s.isdigit():

        return s + '000'
    
    return s.upper()

# print(re.sub(r'(\d+)', f, 'foo 123 bar 456 baz 789'))       根据函数规则返回字符串替换匹配项


re_obj = re.compile(r'\d+')

s = 'foo123barbaz123'

# print(re_obj.search(s[6:9]))
# print(re_obj.findall(s[3:]))      切片操作


re_obj = re.compile('^bar')

s = 'foobarbaz'

# print(re_obj.search(s, 3))              即使它出现在子字符串的开头,从字符3开始,但它不是整个字符串的开头,因此匹配失败

s = re.search(r'(\d+),(\d+),(\d+)?','123,456,')

print(s.groups())

# print(s.groups(default='0000'))      如果没有捕获组,则返回默认值None,如果指定了默认值,则返回指定默认值

# print(s.lastindex)          包含最后捕获组的索引

print(s[s.lastindex])

# obj.start()  obj.end()      返回匹配项的开始和结束索引  

r = '123,456'

s = re.search(r'(\d+),(\d+)',r)

print(s.start())

print(s.end())

print(s)

print(r[s.start():s.end()])
"""