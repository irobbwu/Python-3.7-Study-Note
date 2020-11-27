# 11.21 作业
# 类和对象

# 课堂笔记
class Turtle: 
# The class name convention in Python starts with a capital letter
    '---Instance of a class---'
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = 'big mouth'
    
    # 方法
    def climb(self):
        print('I\'m climbing hard')
    
    def run(self):
        print('I\'m climbing quickly')

# 三大特点：
#   1.封装：信息隐蔽技术
#   2.继承：子类自动共享腐类之间的数据和方法
#   3.多态
        
# 课后习题
# 1.按照以下提示尝试定义一个Person类并生成实例对象。
属性：姓名（默认姓名为“小甲鱼”）
方法：打印姓名
提示：方法中对属性的引用形式需加上self，如self.name)    

class Person:
    
    def __init__(self, name = 'little fish'):
        self.name = name
    
    def way(self):
        print(self.name)
        
>>> a = Person()
>>> a.way()

# 参考答案
class Person:
    name = '小甲鱼'

    def printName(self):
        print(self.name) # 此处的self.name表示对属性对引用
        
# 2. 按照以下提示尝试定义一个矩形类并生成类实例对象。
属性：长和宽
方法：设置长和宽 -> setRect(self)，获得长和宽 -> getRect(self)，获得面积 -> getArea(self)
提示：方法中对属性的引用形式需加上self，如self.width

class Length:
    length = 5
    width = 2
    
    def setRect(self):
        print('Please input the number of the length and the width')
        self.length = float(input('Please input the number of the lenth'))
        self.width = float(input('please input the number of the width'))
        # input输为字符串，需要注意
    def getRect(self):
        print('The lenth is %f'%self.length)
        print('The width is %f'%self.width)
        
    def getArea(self):
        print('The area is %d m^2'%(self.length * self.width))
        
# 参考答案
class Rectangle:
    length = 5
    width = 4

    def setRect(self):
        print("请输入矩形的长和宽")
        self.length = float(input("长："))
        self.width = float(input("宽："))

    def getRect(self):
        print("这个矩形的长是：%.2f，宽是：%.2f" % (self.length, self.width))

    def getArea(self):
        return self.length * self.width
    
# 本章小节
对象：对象是人们要进行研究的任何事物，它不仅能表示具体的事物，还能表示抽象的规则、计划或事件。对象具有状态，一个对象用数据值来描述它的状态。对象还有操作，用于改变对象的状态，对象及其操作就是对象的行为。对象实现了数据和操作的结合，使数据和操作封装于对象的统一体中。
类：具有相同特性（数据元素）和行为（功能）的对象的抽象就是类。因此，对象的抽象是类，类的具体化就是对象，也可以说类的实例是对象，类实际上就是一种数据类型。类具有属性，它是对象的状态的抽象，用数据结构来描述类的属性。类具有操作，它是对象的行为的抽象，用操作名和实现该操作的方法来描述。


        
        