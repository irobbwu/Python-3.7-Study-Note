# 11.21 作业
# 类和对象

# 课后习题：
1. 按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
平日票价100元
周末票价为平日的120%
儿童半票

class Ticket_price():
    ticket_usual = 100
    ticket_uweekend = 120
    ticket_child = 50
    ticket_cweekend = 60
    
    def __init__(self, adults, children, date):
        if 0 < date <= 5:
            total_price = adults * self.ticket_usual\
             + children * self.ticket_child
            print(total_price)
        elif 5 < date <= 7:
            total_price = adults * self.ticket_uweekend\
             + children * self.ticket_cweekend
            print(total_price)
        else:
            print('Wrong sytnax inputting')
>>>a = Ticket_price(2, 1, 6)
>>>a = Ticket_price(2, 1, 3)
            
# 参考答案：
class Ticket:
    def __init__(self, weekend=False, child=False):
        self.price = 100
        if weekend:
            self.increase = 1.2
        else:
            self.increase = 1
        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self, num):
        return self.price * self.increase * self.discount * num

>>> adult = Ticket()
>>> child = Ticket(child=True)
>>> print("2个大人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))

>>> adult2 = Ticket(weekend=True)
>>> child2 = Ticket(weekend=True, child=True)
>>> print("2个大人 + 1个小孩周末票价为：%.2f" % (adult2.calcPrice(2) + child2.calcPrice(1)))

输出:
2个大人 + 1个小孩平日票价为：250.00
2个大人 + 1个小孩周末票价为：300.00

2. 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。（初学者不一定可以完整实现，但请务必先自己动手，你会从中学到很多）
游戏场景为范围(x,y)为 0<=x<=10，0<=y<=10
游戏生成1只乌龟和10条鱼
它们的移动方向均随机
乌龟的最大移动能力为2(可以随机选择1还是2),鱼儿的最大移动能力为1
当移动到场景边缘,自动向反方向移动
乌龟初始化体力为100（上限）
乌龟每移动一次,体力消耗1
当乌龟和鱼坐标重叠,乌龟吃掉鱼，乌龟体力增加20
鱼暂不计算体力
当乌龟体力值为0(挂掉)或鱼儿的数量为0游戏结束

# 参考答案：
import random as r

class Turtle:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置随机
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        # 随机计算方向并移动到新的位置(x, y)
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查移动后是否超出场景x轴边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        # 体力消耗
        self.power -= 1
        # 返回移动后的新位置
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        # 随机计算方向并移动到新的位置(x, y)
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        # 检查移动后是否超出场景x轴边界
        if new_x < 0:
            self.x = 0 - new_x
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x
        # 检查移动后是否超出场景y轴边界
        if new_y < 0:
            self.y = 0 - new_y
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y
        # 返回移动后的新位置
        return (self.x, self.y)

# 开始测试数据
turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼都吃完了，游戏结束！")
        break
    if not turtle.power:
        print("乌龟体力耗尽，挂了！")
        break

    #游戏开始
    #首先乌龟迈出第一步
    print("乌龟移动前坐标：", (turtle.x ,turtle.y)) #乌龟移动前   
    turtle.move()
    print("乌龟移动后坐标：", (turtle.x ,turtle.y)) #乌龟移动后
    for item in fish:
        print("鱼移动前坐标：", (item.x ,item.y))
        item.move()  # 感觉鱼的移动前后的坐标差有问题
        print("鱼移动后坐标：", (item.x ,item.y))
        if item.x==turtle.x and item.y==turtle.y:
            turtle.eat()
            fish.remove(item)
            print("死了一只鱼")
            print("乌龟最新体力值为 %d"%turtle.power)   
            

# 本章小节
 Python中self用法详解

（转载自https://blog.csdn.net/CLHugh/article/details/75000104）

在介绍Python的self用法之前，先来介绍下Python中的类和实例……

我们知道，面向对象最重要的概念就是类（class）和实例（instance），类是抽象的模板，比如学生这个抽象的事物，可以用一个Student类来表示。而实例是根据类创建出来的一个个具体的“对象”，每一个对象都从类中继承有相同的方法，但各自的数据可能不同。

1、以Student类为例，在Python中，定义类如下：


class Student(object):
    pass
（object）表示该类从哪个类继承下来的，object类是所有类都会继承的类。

2、实例：定义好了类，就可以通过Student类创建出Student的实例，创建实例是通过类名+()实现：

student = Student()
3、由于类起到模板的作用，因此，可以在创建实例的时候，把我们认为必须绑定的属性强制填写进去。这里就用到Python当中的一个内置方法__ init__方法，例如在Student类时，把name、score等属性绑上去:

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
这里注意：（1）、__ init__方法的第一参数永远是self，表示创建的类实例本身，因此，在__ init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。（2）、有了__init __方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init __方法匹配的参数，但self不需要传，Python解释器会自己把实例变量传进去：

>>>student = Student("Hugh", 99)
>>>student.name
"Hugh"
>>>student.score
99
另外，这里self就是指类本身，self.name就是Student类的属性变量，是Student类所有。而name是外部传来的参数，不是Student类所自带的。故，self.name = name的意思就是把外部传来的参数name的值赋值给Student类自己的属性变量self.name。

4、和普通函数相比，在类中定义函数只有一点不同，就是第一参数永远是类的本身实例变量self，并且调用时，不用传递该参数。除此之外，类的方法（函数）和普通函数没啥区别，你既可以用默认参数、可变参数或者关键字参数（args是可变参数，args接收的是一个tuple，*kw是关键字参数，kw接收的是一个dict）。

5、既然Student类实例本身就拥有这些数据，那么要访问这些数据，就没必要从外面的函数去访问，而可以直接在Student类的内部定义访问数据的函数（方法），这样，就可以把“数据”封装起来。这些封装数据的函数是和Student类本身是关联起来的，称之为类的方法：

class Student(obiect):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print "%s: %s" % (self.name, self.score)
>>>student = Student("Hugh", 99)
>>>student.print_score
Hugh: 99
这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score。而如何打印，都是在Student类的内部定义的，这些数据和逻辑被封装起来了，调用很容易，但却不知道内部实现的细节。

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线，在Python中，实例的变量名如果以两个下划线开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print "%s: %s" %(self.__name,self.__score)
改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：

>>> student = Student('Hugh', 99)
>>> student.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'
这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：

class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：

class Student(object):
    ...

    def set_score(self, score):
        self.__score = score
需要注意的是，在Python中，变量名类似__ xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__ name__、__ score__这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

封装的另一个好处是可以随时给Student类增加新的方法，比如：get_grade:

class Student(object):
    ...
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
同样的，get_grade方法可以直接在实例变量上调用，不需要知道内部实现细节：

>>> student.get_grade()
'A'
6、self的仔细用法
(1)、self代表类的实例，而非类。

class Test:
    def ppr(self):
        print(self)
        print(self.__class__)

t = Test()
t.ppr()
执行结果：
<__main__.Test object at 0x000000000284E080>
<class '__main__.Test'>
从上面的例子中可以很明显的看出，self代表的是类的实例。而self.__ class__则指向类。
注意：把self换成this，结果也一样，但Python中最好用约定俗成的self。

（2）、self可以不写吗？
在Python解释器的内部，当我们调用t.ppr()时，实际上Python解释成Test.ppr(t)，也就是把self替换成了类的实例。

class Test:
    def ppr():
        print(self)

t = Test()
t.ppr()
运行结果如下：

Traceback (most recent call last):
  File "cl.py", line 6, in <module>
    t.ppr()
TypeError: ppr() takes 0 positional arguments but 1 was given
运行时提醒错误如下：ppr在定义时没有参数，但是我们运行时强行传了一个参数。

由于上面解释过了t.ppr()等同于Test.ppr(t)，所以程序提醒我们多传了一个参数t。

这里实际上已经部分说明了self在定义时不可以省略。

当然，如果我们的定义和调用时均不传类实例是可以的，这就是类方法。

class Test:
    def ppr():
        print(__class__)

Test.ppr()

运行结果：
<class '__main__.Test'>
（3）、在继承时，传入的是哪个实例，就是那个传入的实例，而不是指定义了self的类的实例。

class Parent:
    def pprt(self):
        print(self)

class Child(Parent):
    def cprt(self):
        print(self)
c = Child()
c.cprt()
c.pprt()
p = Parent()
p.pprt()
运行结果：

<__main__.Child object at 0x0000000002A47080>
<__main__.Child object at 0x0000000002A47080>
<__main__.Parent object at 0x0000000002A47240>
解释：
运行c.cprt()时应该没有理解问题，指的是Child类的实例。
但是在运行c.pprt()时，等同于Child.pprt(c)，所以self指的依然是Child类的实例，由于self中没有定义pprt()方法，所以沿着继承树往上找，发现在父类Parent中定义了pprt()方法，所以就会成功调用。
（4）、在描述符类中，self指的是描述符类的实例。

class Desc:
    def __get__(self, ins, cls):
        print('self in Desc: %s ' % self )
        print(self, ins, cls)
class Test:
    x = Desc()
    def prt(self):
        print('self in Test: %s' % self)
t = Test()
t.prt()
t.x
运行结果如下：

self in Test: <__main__.Test object at 0x0000000002A570B8>
self in Desc: <__main__.Desc object at 0x000000000283E208>
<__main__.Desc object at 0x000000000283E208> <__main__.Test object at 0x0000000002A570B8> <class '__main__.Test'>
这里主要的疑问应该在：Desc类中定义的self不是应该是调用它的实例t吗？怎么变成了Desc类的实例了呢？
因为这里调用的是t.x，也就是说是Test类的实例t的属性x，由于实例t中并没有定义属性x，所以找到了类属性x，而该属性是描述符属性，为Desc类的实例而已，所以此处并没有顶用Test的任何方法。

那么我们如果直接通过类来调用属性x也可以得到相同的结果。

下面是把t.x改为Test.x运行的结果。

self in Test: <__main__.Test object at 0x00000000022570B8>
self in Desc: <__main__.Desc object at 0x000000000223E208>
<__main__.Desc object at 0x000000000223E208> None <class '__main__.Test'>
           






