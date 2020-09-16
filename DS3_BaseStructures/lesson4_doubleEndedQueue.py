'''
     栈      后进先出   从低到高排列的书      顶（进出）    底  append | pop
     队列    先进先出   排队打饭（不许插队）  rear（进） | front（出）
    双端队列   倆端成为队首（front）和队尾（rear）元素可以从倆端插入（加），也可以从倆端删除（取）
    
     
    抽象数据类型(ADT)
        Deque()         创建一个空双端对列，无参数，返回值为Deque对象
        addFront(item)  在队首插入一个元素，参数为待插入元素，无返回值
        addRear(item)   在队尾插入一个元素，参数为待插入元素，无返回值
        removeFront()   在队首移出一个元素，无参数，返回该移出的元素，双端队列会被改变
        removeRear()    在队尾移出一个元素，无参数，返回该移出的元素，双端队列会被改变
        isEmpty()       判断双端队列是否为空，无参数，返回布尔值
        size()          返回双端队列中数据项的个数，无参数，返回值为整型数值  
'''

# class Deque:
#     def __init__(self):
#         self.items = []
#     def isEmpty(self):
#         return self.items == []
#     def size(self):
#         return len(self.items)
#     def addFront(self,item):
#         self.items.append(item)
#     def addRear(self,item):
#         self.items.insert(0,item)
#     def removeFront(self):
#         return self.items.pop()
#     def removeRear(self):
#         return self.items.pop(0)


# d = Deque()
# print(d.isEmpty())
# d.addRear(666)
# d.addRear(777)
# d.addFront(888)
# d.addFront(999)
# print(d.size())
# print(d.isEmpty())
# d.addRear(8.4)
# print(d.removeRear())
# print(d.removeFront())




'''
    leetcode  简单第9题   判断一个整数是否是回文数（回文词）
    回文词：上海自来水来自海上    山西运煤车煤运西山   roor   madam
    网上交流交上网，微群对话对群微。
    满园春色春园满，机待人来人待机。
    回文数：123321
    编写一个算法来检查放入的字符串是否是回文词
    -----------------------
rear       roor              front
    -----------------------
    r         ==            r
    o         ==            o
'''

from pythonds.basic.deque import Deque

def palChecker(aString):
    charDeque = Deque()
    for ch in aString:
        charDeque.addFront(ch)

    stillEqual = True
    while charDeque.size() > 1 and stillEqual: 
        first_ch = charDeque.removeFront()
        last_ch = charDeque.removeRear()

        if first_ch != last_ch:
            stillEqual = False
    
    return stillEqual



print(palChecker("madam"))
print(palChecker("lalalalalal"))
print(palChecker("满园春色春园满"))
print(palChecker("网上交流交上网"))
print(palChecker("微群对话对群微"))
print(palChecker("机待人来人待机"))
print(palChecker("山西运煤车煤运西山"))
print(palChecker("上海自来水来自海上"))

