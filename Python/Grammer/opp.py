#-*-coding:utf8-*-
#-------------------------------类和实例-----------------------------------
#class 关键字
# class Student(object):
#     pass
#
# hight = Student()
# print(hight)
# #绑定属性1
# hight.name = "jas"
# hight.age = 20
# print(hight.name)

#绑定属性2,创建实例的就把属性绑定到实例上
# __init__
# 第一个参数永远是self ,self指向创建的实例本身
# class Student(object):
#     def __init__(self,name, score):
#         print(self)
#         self.name = name
#         self.score = score
#
# bart = Student("jas", 20)
# print(bart.name)

#数据封装
# class Student(object):
#     def __init__(self,name, score):
#         print(self)
#         self.name = name
#         self.score = score
#     def print_score(self):
#         print('%s : %s' % (self.name, self.score))
#
# bart = Student("jas", 20)
# bart.print_score()  #可以直接在实例上调用，不需要知道内部实现细节

#-------------------------------访问限制-----------------------------------
#__ 私有变量， 不可直接访问
# 如果想修改或者获取怎么做？
# class Student(object):
#     def __init__(self,name, score):
#         print(self)
#         self.__name = name
#         self.__score = score
#     def print_score(self):
#         print('%s : %s' % (self.__name, self.__score))
#     #获取
#     def get_name(self):
#         return self.__name
#     def get_score(self):
#         return self.__score
#     #修改 why ?  可以对参数进行检查
#     def set_score(self, score):
#         if 0 < score < 100:
#             self.__score = score
#         else:
#             raise ValueError('bad score')
#
#
# bart = Student("jas", 20)
#
# # print(bart.__name)
# # print(bart.get_name())
# bart.set_score(50)
# print(bart.get_score())
# # 或者
# print(bart._Student__score)
#
# #注意
# bart.__name = 'young'
# print(bart.__name)
# print(bart.get_name())
#
# #-------------------------------继承和多态-----------------------------------
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
# class Dog(Animal):
#     # def run(self):
#         # print('dog is running...')
#     def eat(self):
#         print('dog is eating')
#
# class Cat(Animal):
#     # def run(self):
#         # print('cat is running...')
#     def eat(self):
#         print('cat is eating')
#     pass
#
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()
#
# print(isinstance(dog, Animal))
# print(isinstance(dog, Dog))

#-------------------------------获取对象信息-----------------------------------
import types
def fn():
    pass
#判断对象是数据类型
# print(type(123) == type("154"))
# print(type(123) == int)
# print(type(123) == str)
#判断对象是函数
# print(type(fn) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x:x) == types.LambdaType)
#或者
# print(isinstance([1,3,4],(list,str)))
# print(isinstance('1', str) and isinstance(2, int))

#获取对象的属性和方法
# print(dir('acc'))
# class Test():
#     def __len__(self):
#         return 100
# test = Test()
# print(len(test))

# 操作一个对象的状态
# class MyTest():
#     def __init__(self):
#         self.x = 9
#     def add(self):
#         return self.x + self.x
# mytest = MyTest()

# 操作对象的属性
# print(hasattr(mytest, 'x'))
# if hasattr(mytest, 'x'):
#     setattr(mytest, 'x', 10)
#     print(mytest.x)
#     print(getattr(mytest,'x'))
#     print(mytest.add())

# 操作对象的方法
# fn1 = getattr(mytest, 'add')
# print(fn1())

#-------------------------------实例属性和类属性---------------------------------
# 给类绑定属性:直接在类中定义属性
class People(object):
    age = '10'
    def __init__(self, name):
        self.name = name
person = People('vin')
print(person.age)

person.age = 20
print(person.age)
print(People.age)

#实例属性会屏蔽类属性
