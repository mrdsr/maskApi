#coding:utf-8
<<<<<<< HEAD
# print("Test")
from random import randint

data = [randint(-10,10) for _ in range(10)]
print(data)
# random_number_0 = [[randint(0,8) for i in range(2)] for j in range(12)]
# print(random_number_0)

#filter(function, iterable)
#function -- 判断函数。 iterable -- 可迭代对象。

#关于filter()方法, python3和python2有一点不同

#Python2.x 中返回的是过滤后的列表, 而 Python3 中返回到是一个 filter 类。

#filter 类实现了 __iter__ 和 __next__ 方法, 可以看成是一个迭代器, 有惰性运算的特性, 相对 Python2.x 提升了性能, 可以节约内存。
a = list(filter(lambda x:x>0,data))
print(a)
