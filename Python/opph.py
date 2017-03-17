#-*- coding:UTF-8-*-

#-------------------------------__slots__-----------------------------------
#给实例动态绑定一个方法
# from types import MethodType
# class Student(object):
#     pass
# s = Student()
# s.name = 'jas'
#
# def set_age(self, age):
#     self.age = age
# s.set_age1 = MethodType(set_age, s)
# s.set_age1(100)

#给类动态绑定一个方法
#也可以直接定义在类中
# Student.set_score2 = set_age
# print(s.age)
# s.set_score2(200)
# print(s.age)

#使用__slots__限制该类实例能添加的属性
# class Person(object):
#     __slots__ = ('name', 'age')
# person = Person()
# person.name = 'zhangshan'
# person.room = '302'

# 对子类不起作用
# class Asia(Person):
#     pass
# yellow = Asia()
# yellow.name = '301'
# print(yellow.name)

#除非在子类中也定义__slots__,这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
#
# class Africa(Person):
#     __slots__ = ('score')
# black = Africa()
# black.name = '401'
# print(black.name)

#-------------------------------@property---------------------------------------
#把一个方法变成属性调用

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

    def __str__(self):
        return 'student name objec is %s' % self._score

    __repr__ = __str__

student = Student()
student.score  = 60
print(student)
print(student.score)


#--------------------------------__iter__----------------------------------------
class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    def __iter__(self):
        return self
    def next(self):
        self.a , self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration();
        return self.a

for n in Fib():
    print n
