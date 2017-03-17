# -*- coding:UTF-8 -*-
from collections import Iterable
from types import MethodType
#-------------------------------slice--------------------------------
# L = ["Young", "Vin", "Jas","Nacy","Neil","Ting"]
# sliceL = L[0:2]
# sliceL = L[:2]
# sliceL = L[-3:-1]
# print(sliceL)

#list
# L = list(range(0,99))
# print(L[10:15])
# print(L[:10:3])
# print(L[:])

#tuple
# print((1,3,4,6)[:2])

#string
# print('banfkglk;sjglk'[:4])

#-------------------------------Iteration-----------------------------------
dic = {"Young":"y","Vin":"t","Jas":"w"}
MyName = "Jasmine"
print(isinstance(dic, Iterable))
print(isinstance(MyName, Iterable))

for key in dic:
    print(key)

for key, value in dic.items():
    print(key, value)

for i, value in enumerate(MyName):
    print(i, value)

#---------------------------------List comprehensions---------------------------
print([x * x for x in range(1,10)])
print([x + y for x in "ABC" for y in "abc"])

Names = ["Jas", 2, "Vin","Young"]
LowerNames = []
def lowerStr(s):
    if isinstance(s, str):
        return s.lower()
    else:
        return s
print([lowerStr(name) for name in Names])

#------------------------------generator/Iterator-----------------------------------------
iterator = (x for x in range(1,10))
print(iterator.next())
print(iterator.next())
#
# if isinstance(iterator, Iterable):
#     for value in iterator:
#         print(value)
def testIterator():
    print("input 1")
    yield
    print("inuput 2")
    yield
    print("input 3")
    yield
test = testIterator()
next(test)
next(test)
next(test)
