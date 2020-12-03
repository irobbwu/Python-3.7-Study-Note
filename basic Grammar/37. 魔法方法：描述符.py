# 魔法方法：描述符

'''
魔法方法	含义
__ get__(self, instance, owner)	用于访问属性，它返回属性的值
__ set__(self, instance, value)	将在属性分配操作中调用，不返回任何内容
__ delete__(self, instance)	控制删除操作，不返回任何内容
'''

# 1.按要求编写描述符MyDes：当类的属性被访问、修改或设置的时候，分别作出提醒。

答：其实如果大家自己认真思考了代码，会发现我们这里的描述符起到的作用是间接地保存指定变量的数据。

# 答：
class MyDes:
    def __init__(self, initval=None, name=None):
        self.val = initval
        self.name = name

    def __get__(self, instance, owner):
        print("正在获取变量：", self.name)
        return self.name

    def __set__(self, instance, value):
        print("正在修改变量：", self.name)
        self.name = value

    def __delattr__(self, instance):
        print("正在删除变量：", self.name)
        print("┗|｀O′|┛ 嗷~~这个变量没法删除~")
        
# 2.按要求编写描述符MyDes：记录指定变量的读取和写入操作，并将记录以及触发时间保存到文件。

import time as t

class MyDos:
    def __init__(self, name = 'x', inite = None):
        file = open('/Users/yasmine/Documents/学习/language/python/write_record.txt', 'a')
        self.name = name
        self.inite = inite
        file.close()
        
    def __get__(self, instance, owner):
        file = open('/Users/yasmine/Documents/学习/language/python/write_record.txt', 'a')
        file.write('%s = %d was read at %s\n'%(self.name, self.inite, t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())))
        file.close()
        return self.inite
    
    def __set__(self, instance, value):
        self.inite = value
        file = open('/Users/yasmine/Documents/学习/language/python/write_record.txt', 'a')
        file.write('%s = %d was inserted at %s\n'%(self.name, self.inite, t.strftime('%Y-%m-%d %H:%M:%S', t.localtime())))
        file.close()
        
class Record:
    x = MyDos()
    
>>> a = Record()
>>> a.x = 1
>>> a.x

# 本章小节
描述符property()函数
一句话解释：描述符就是将某种特殊类型的类的实例指派给另一个类的属性。
>>> class MyDescriptor:
    # self是描述符自身的实例；instance是这个描述符的拥有着所在类的实例，在这里也就是Test类的实例；owner是这个描述符的拥有者所在的类本身
    def __get__(self, instance, owner):
        print("getting...", self, instance, owner)
    # 参数value是等号右边的值，就是下面的'X-man'
    def __set__(self, instance, value):
        print("setting...", self, instance, value)
    def __delete__(self, instance):
        print("delete...", self, instance)

        
>>> class Test:
    x = MyDescriptor()

    
>>> test = Test()
>>> test.x
getting... <__main__.MyDescriptor object at 0x000001A2EA6D86D8> <__main__.Test object at 0x000001A2EA668278> <class '__main__.Test'>
>>> test
<__main__.Test object at 0x000001A2EA668278>
>>> Test
<class '__main__.Test'>
>>> test.x = 'X-man'
setting... <__main__.MyDescriptor object at 0x000001A2EA6D86D8> <__main__.Test object at 0x000001A2EA668278> X-man
>>> del test.x
delete... <__main__.MyDescriptor object at 0x000001A2EA6D86D8> <__main__.Test object at 0x000001A2EA668278>
>>> 
自定义property
>>> class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self, instance, owner):
        return self.fget(instance)
    def __set__(self, instance, value):
        self.fset(instance, value)
    def __delete__(self, instance):
        self.fdel(instance)

>>> class C:
    def __init__(self):
        self._x = None  # 你想声明为私有的方法和属性前加上单下划线,以提示该属性和方法不应在外部调用
    def getX(self):
        return self._x
    def setX(self, value):
        self._x = value
    def delX(self):
        del self._x
    x = MyProperty(getX, setX, delX)

>>> c = C()
>>> c.x = 'X-man'
>>> c.x
'X-man'
>>> c._x
'X-man'
>>> del c.x
>>> c._x
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    c._x
AttributeError: 'C' object has no attribute '_x'
>>> 
下面举一个摄氏与华氏相互转换的例子：

>>> class Celsius:
    def __init__(self, value=26.0):
        self.value  = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

        
>>> class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32
    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

        
>>> class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

    
>>> temp = Temperature()
>>> temp.cel
26.0
>>> temp.fah
78.80000000000001
>>> temp.fah = 100
>>> temp.cel
37.77777777777778

