# python 数据结构的性能

# 列表 List
# my_list = [1,2,3,4,5,6,7]
''' 
    1. 索引和分派到一个索引位置这两个操作，无论列表有多大，操作花费的时间都相同，O(1)
        print(my_list[0])
        print(my_list[5])
    
    2. 扩充list，append  也是O(1)
 '''
# import timeit
# from timeit import Timer

# def test1():
#     my_list = []
#     for i in range(1000):
#         my_list = my_list + [i]

# def test2():
#     my_list = []
#     for i in range(1000):
#         my_list.append(i)

# def test3():
#     my_list = [i for i in range(1000)]

# def test4():
#     my_list = list(range(1000))

# t1 = Timer("test1()","from __main__ import test1")
# print("连接",t1.timeit(number=1000),"秒")

# t2 = Timer("test2()","from __main__ import test2")
# print("append",t2.timeit(number=1000),"秒")

# t3 = Timer("test3()","from __main__ import test3")
# print("列表推导式",t3.timeit(number=1000),"秒")

# t4 = Timer("test4()","from __main__ import test4")
# print("list range",t4.timeit(number=1000),"秒")


'''
    ----------- 测试pop()删除列表第一个元素和pop(0) 删除列表最后一个元素-----------
    pop()   O(1)
    pop(i)  O(n)
'''

import timeit
from timeit import Timer

l = list(range(2000000))
pop_zero = Timer("l.pop(0)","from __main__ import l")
print("pop_zero",pop_zero.timeit(number=1000),"秒")


pop_end = Timer("l.pop()","from __main__ import l")
print("pop_end",pop_end.timeit(number=1000),"秒")