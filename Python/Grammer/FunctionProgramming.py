#-*-coding:utf8-*-
from  collections import Iterable

#-----------------------------------map----------------------------------------
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
# def Capitalize(s):
#     lowerStr = s.lower()
#     return lowerStr.capitalize()
# input = map(Capitalize, ['adam', 'LISA', 'barT'])
# print(input)

#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# def prod(list):
#     def add(x, y):
#         return x + y
#     return reduce(add, list)
# prodResult = prod([1,2,3,4,5])
# print(prodResult)

#-----------------------------------filter--------------------------------------
#计算素数
#先构造一个从3开始的奇数序列
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
# _odd = _odd_iter()
# if isinstance(_odd, Iterable):
    # for value in _odd:
        # print(value)
#--------------------------------- sorted---------------------------------------
#假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# l1 = sorted(L, key = lambda s:s[0])
# print(l1)

#--------------------------------- 返回函数--------------------------------------
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# def cals_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
#
# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         print(ax)
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f1 = lazy_sum(1,2,4,5,7,8)
# f2 = lazy_sum(1,2,4,5,7,8)
#
# print(f1)
# print(f1())
#
# print(f2)
# print(f2())

#Closure
# def count():
#     fs = []
#     for i in range(1,4):
#         # print(i)
#         def f():
#             return i * i
#         # print(f)
#         print(fs)
#         fs.append(f)
#     return fs
# f1,f2,f3 = count()
# print(f1())
# print(f2())
# print(f3())

# def func(name):
#     def inner_func(age):
#         print(name, age)
#     return inner_func
# f = func("zhangsan")
# f(20)

#闭包中是不能修改外部作用域的局部变量的
# def foo():
#     m = 0
#     def foo1():
#         m = 1
#         print("hahai")
#         print m
#     foo1()
#     print m
# foo()

#经典错误代码 1
# def foo2():
#     a = 1
#     def bar():
#         a = a + 1
#         print(bar)
#         print(a)
#         return a
#     print(a)
#     return bar
#  foo2()

#解决办法：
# def foo():
#     a = [1]
#     def bar():
#         a[0] = a[0] + 1
#         print('bar')
#         print(a[0])
#         return a[0]
#     print(a[0])
#     return bar
# foo()

#经典错误代码2
# flist = []
# for i in range(3):
#     def foo(x):
#         print x + i
#     flist.append(foo)
# for f in flist:
#  f(2)
#解决方法
# for i in range(3):
#     def foo(x,y=i):
#         print x + y
#     flist.append(foo)
# for f in flist:
#     f(2)

#-----------------------------------匿名函数--------------------------------------
#不需要显式地定义函数
#因为函数没有名字，不必担心函数名冲突
# f = lambda x : x * 2
# print(f(4))

#-----------------------------------装饰器--------------------------------------

# def now():
#     print("122222")
#定义一个打印日志的decorator
#假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#方法1：
# def log(func):
#     def wrapper():
#         print('call %s(): ' % func.__name__)
#         return func()
#     return wrapper
#
# @log
# def now():
#     print("122222")
# now() #相当于log(now)

#如果装饰器本身需要传入参数
# import functools
# def log(text):
#     def decorator(func):
#         #原始函数的__name__等属性复制到wrapper()函数中
#         @functools.wraps(func)
#         def wrapper():
#             print(text)
#             print('call %s(): ' % func.__name__)
#             return func()
#         return wrapper
#     return decorator
#
# @log('text')
# def now():
#     print("122222")
# now()  # 相当于log('text')(now)
# print(now.__name__)

#-----------------------------------偏函数--------------------------------------
#使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单
# import functools
#eg1:
# print(int('1345'))
# print(int('1345', 8))
# def int2(x, base=2):
#     return int(x,base)
# a = int2("1345", 8)
# print(a)
# c = functools.partial(int, base=2)
# print(c('1345', base=8))
#
#eg2:
# def add(a, b):
#     return a + b
# d = functools.partial(add, 100)
# print(d(200))
