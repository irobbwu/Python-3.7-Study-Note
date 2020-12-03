# 魔法方法：定制序列

0.你知道Python基于序列的三大容器类指的是什么吗？

答：列表（List）、元组（Tuple）、字符串（String）。

1.Python允许我们自己定义容器，如果你想要定制一个不可变的容器（像String），你就不能定义什么方法？

答：如果你想要定制一个不可变的容器，你就不能定义像__ setitem__()和__ delitem__()方法，这两个会修改容器中的数据的方法。

2.如果希望定制的容器支持reversed()内置方法，那么你应该定义什么方法？

答：应该定义__ reversed__()方法，提供对内置函数reversed()的支持。

3.既然是容器，必须要提供能够查询“容器”的方法，那么请问需要定义什么方法呢？

答：在Python中，我们通过len()内置函数来查询容器的“容量”，所以容器应该定义__ len__()方法。

4.通过定义哪些方法使得容器支持读、写和删除的操作？

答：读是__ getitem__()；写是__ setitem__()；删除时__ delitem__()。

5.为什么小甲鱼说“在Python中的协议就显得不那么正式？”

答：在Python中，协议更像一种指南。这点像我们之前在课后作业中提到的“鸭子类型”。当看到一只鸟走起来像鸭子、游泳起来像鸭子、叫起来也像鸭子，那么这只鸟就可以被称为鸭子。Python就是这样，并不会严格要求你一定要怎样去做，而是让你靠着自觉和经验把事情做好。

编程题

0.根据课堂上的例子，定制一个列表，同样要求记录列表中每个元素被访问的次数，这一次我们希望定制的列表功能更加全面一些，比如支持append()、pop()、extend()原生列表所拥有的方法。你应该如何修改呢？

要求1：实现获取、设置和删除一个元素的行为（删除一个元素的时候对应的计数器也会被删除）
要求2：增加counter(index)方法，返回index参数所指定的元素次数的访问次数
要求3：实现append()、pop()、remove()、insert()、clear()和reverse()方法（重写这些方法时注意考虑计数器的对应改变）
答：我们先看下课堂上的例子：
>>> class CountList:
    def __init__(self, *args):  # 可变数量的参数
        self.values = [x for x in args]  # 把参数转换成列表
        self.count = { }.fromkeys(range(len(self.values)), 0)  # 给字典初始化
        # 这里是有列表的下表作为字典的键，注意不能用元素作为字典的键
        # 因为列表的不同下标可能有值一样的元素，但字典不能有两个相同的键
    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

    
>>> c1 = CountList(1, 3, 5, 7, 9)
>>> c2 = CountList(2, 4, 6, 8, 10)
>>> c1[1]
3
>>> c2[1]
4
>>> c1[1] + c2[2]
9
>>> c1.count
{0: 0, 1: 2, 2: 0, 3: 0, 4: 0}
>>> c2.count
{0: 0, 1: 1, 2: 1, 3: 0, 4: 0}
答：为了实现那么多的功能，我们不能再用字典来存放元素的计数了，因为对于列表来说，如果你删除其中一个元素，那么其他元素的下标都会发生相应的变化（利用下标作为键的字典肯定就不能应对自如）。因此，我们改用一个列表来存放对应的元素的计数。
下边是CountList类继承并严重依赖其父类（list）的行为，并按要求重写了一些方法。
代码清单：

class CountList(list):
    def __init__(self, *args):
        super().__init__(args)
        self.count = []
        for i in args:
            self.count.append(0)

    def __len__(self):
        return len(self.count)

    def __getitem__(self, key):
        self.count[key] += 1
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        self.count[key] += 1
        super().__setitem__(key, value)

    def __delitem__(self, key):
        del self.count[key]
        super().__delitem__(key)

    def counter(self, key):  # 根据下标返回访问的次数
        return self.count[key]

    def append(self, value):
        self.count.append(0)
        super().append(value)

    def pop(self, key=-1):
        del self.count[key]
        return super().pop(key)

    def remove(self, value):
        key = super().index(value)
        del self.count[key]
        super().remove(value)

    def insert(self, key, value):
        self.count.insert(key, 0)
        super().insert(key, value)

    def clear(self):
        self.count.clear()
        super().clear()

    def reverse(self):
        self.count.reverse()
        super().reverse()

c1 = CountList(1, 2, 3, 4, 5, 6)
c1[1]
c1[1]
c1[1]
print(c1)
print(c1.count)
print("*"*30)
print(c1.counter(1))
print("*"*30)
c1.append(99)
print(c1)
print(c1.count)
print("*"*30)
c1.pop()
print(c1)
print(c1.count)
print("*"*30)
c1.remove(5)
print(c1)
print(c1.count)
print("*"*30)
c1.insert(2, 55)
print(c1)
print(c1.count)
print("*"*30)
c1.reverse()
print(c1)
print(c1.count)
print("*"*30)
c1.clear()
print(c1)
print(c1.count)
输出：

[1, 2, 3, 4, 5, 6]
[0, 3, 0, 0, 0, 0]
******************************
3
******************************
[1, 2, 3, 4, 5, 6, 99]
[0, 3, 0, 0, 0, 0, 0]
******************************
[1, 2, 3, 4, 5, 6]
[0, 3, 0, 0, 0, 0]
******************************
[1, 2, 3, 4, 6]
[0, 3, 0, 0, 0]
******************************
[1, 2, 55, 3, 4, 6]
[0, 3, 0, 0, 0, 0]
******************************
[6, 4, 3, 55, 2, 1]
[0, 0, 0, 0, 3, 0]
******************************
[]
[]
1.请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！

定制容器类相关的魔法方法
魔法方法	含义
__ len__(self)	定义当被len()函数调用时的行为（返回容器中元素的个数）
__ getitem__(self, value)	定义获取容器中指定元素的行为，相当于self[key]
__ setitem__(self, key, value)	定义设置容器中指定元素的行为，相当于self[key]=value
__ delitem__(self, key)	定义删除容器中指定元素的行为，相当于del self[key]
__ iter__(self)	定义当迭代容器中的元素的行为
__ reversed__(self)	定义当被reversed()函数调用时的行为
__ contains__(self, item)	定义当使用成员测试运算符（in或not in）时的行为
