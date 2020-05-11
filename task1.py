#coding:utf-8

###过滤列表中大于0的数据####
import timeit
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

#方法一
a = list(filter(lambda x:x>0,data))
print(a)


#方法二列表解析
#列表解析 List Comprehensions

#表达式：[expression for iter_val in iterable if cond_expr]
#[expression]：最后执行的结果
#[for iter_val in iterable]：这个可以是一个多层循环
#[if cond_expr]：两个for间是不能有判断语句的，判断语句只能在最后；顺序不定，默认是左到右。
c = [x for x in data if x>0]
print(c)

#总结列表解析比filter函数加载要快