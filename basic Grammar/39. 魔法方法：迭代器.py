# 魔法方法：迭代器

# 1.写一个迭代器，要求输出至今为止的所有闰年。如：
import time as t

class Leapyear:
    def __init__(self, x = 4):
        self.x = x
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.x = self.x + 4
        if self.x > t.localtime()[0]:
            raise StopIteration
        return self.x

# 参考答案：
import datetime as dt

class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year

    def isLeapYear(self, year):
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1

        temp = self.now
        self.now -= 1

        return temp

ly = LeapYear()
for i in ly:
    if i > 2000:
        print(i)
    else:
        break
       
    
# 2.要求自己写一个MyRev类，功能与reversed()相同（内置函数reversed(seq)，是返回一个迭代器，是序列seq的逆序显示）。例如：

'''
>>> myRev = MyRev("FishC")
>>>for i in myRev:
      print(i, end=' ')
'''

class MyRev:
    def __init__(self, data):
        self.list1 = []
        for i in data:
            self.list1.append(i)
        self.num = len(self.list1)
        print(self.list1)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num = 0:
            raise StopIteration
        self.num = self.num - 1
        return self.list1[self.num]
        
# 本章小节：
'''
迭代器的魔法方法
__ iter__()：返回迭代器本身；
__ next__()：这里写迭代的规律。
举个例子：
'''

class Fibs:
    def __init__(self, n=20):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > self.n:
            raise StopIteration
        return self.a

fibs = Fibs(20)
for each in fibs:
    print(each)

'''
输出：

1
1
2
3
5
8
13
'''
