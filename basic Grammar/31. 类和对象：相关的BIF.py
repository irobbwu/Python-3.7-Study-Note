# 11.27 作业
# 类和对象

# 本章小节
# 1.思考这一讲学习的内容，请动手在一个类中定义一个变量，用于跟踪类有多少个实例被创建（当实例化一个对象，这个变量+1，当销毁一个对象，这个变量自动-1）。

# 答：
issubclass(class, classinfo)
如果第一个参数是第二个参数的一个子类，则返回True，否则返回False：
1️⃣一个类被认为是其自身的子类。
2️⃣classinfo可以是类对象组成的元组，只要class是其中任何一个候选类的子类，则返回True。
3️⃣在其他情况下，会抛出一个TypeError异常。
>>> class A:
    pass

>>> class B(A):
    pass

>>> issubclass(B,A)
True
>>> issubclass(B,B)
True
>>> issubclass(B,object)
True
>>> class C:
    pass

>>> issubclass(B,C)
False
>>> issubclass(B,(A,C))
True
>>> issubclass(B,111)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    issubclass(B,111)
TypeError: issubclass() arg 2 must be a class or tuple of classes
isinstance(object, classinfo)
如果第一个参数是第二个参数的实例对象，则返回True，否则返回False：
1️⃣如果object是classinfo的子类的一个实例，也符号条件。
2️⃣如果第一个参数不是对象，则永远返回False。
3️⃣classinfo可以是类对象组成的元组，只要object是其中任何一个候选对象的实例，则返回True。
4️⃣如果第二个参数不是类或者由类对象组成的元组，会抛出一个TypeError异常。
>>> class A:
    pass

>>> class B(A):
    pass

>>> class C:
    pass

>>> issubclass(B,C)
False
>>> b1 = B()
>>> isinstance(b1,B)
True
>>> isinstance(b1,A)
True
>>> isinstance(b1,C)
False
>>> isinstance(b1,object)
True
>>> isinstance(b1,(A,B,C))
True
>>> isinstance(111,A)
False
>>> isinstance(b1,111)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    isinstance(b1,111)
TypeError: isinstance() arg 2 must be a type or tuple of types
hasattr(object, name)
attr即attribute的缩写，属性的意思。其作用就是测试一下对象里是否有指定的属性。
第一个参数是对象，第二个参数是属性名（属性的字符串名字），举个例子：
>>> class C:
    def __init__(self, x=0):
        self.x = x

        
>>> c1 = C()
>>> hasattr(c1, 'x')
True
>>> hasattr(c1, 'y')
False
getattr(object, name[, default])
返回对象指定的属性值，如果指定的属性不存在，则返回default（可选参数）的值；若没有设置default参数，则抛出AttributeError异常。
>>> class C:
    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

>>> c1 =C()
>>> getattr(c1, 'x')
0
>>> getattr(c1, 'y')
1
>>> getattr(c1, 'z')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    getattr(c1, 'z')
AttributeError: 'C' object has no attribute 'z'
>>> getattr(c1, 'z', '您访问的属性不存在')
'您访问的属性不存在'
setattr(object, name, value)
用来设置对象中指定属性的值，如果指定的属性不存在，则新建属性并赋值。
>>> setattr(c1, 'x', 111)  # 原来有的覆盖
>>> getattr(c1, 'x')
111
>>> setattr(c1, 'z', 2)  # 没有新建并赋值
>>> getattr(c1, 'z')
2
delattr(object, name)
用来删除对象中指定的属性，如果属性不存在，则抛出AttributeError异常。
>>> delattr(c1, 'x')
>>> delattr(c1, 'y')
>>> delattr(c1, 'z')
>>> delattr(c1, 'aaa')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    delattr(c1, 'aaa')
AttributeError: aaa
>>> 
property(fget=None, fset=None, fdel=None, doc=None)
用来通过属性来设置属性。
>>> class C:
    def __init__(self, size=10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x= property(getSize, setSize, delSize)

>>> c = C()
>>> c.x
10
>>> c.x = 12
>>> c.x
12
>>> c.size
12
>>> del c.x
>>> c.size
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    c.size
AttributeError: 'C' object has no attribute 'size'
property()函数中的三个函数分别对应的是获取属性的方法、设置属性的方法以及删除属性的方法，这样一来，外部的对象就可以通过访问x的方式，来达到获取、设置或删除属性的目的。

当需要更改上例中的getSize、setSize或delSize函数的名称时，如果这些方法是作为接口让用户调用的，那么对用户而言就要修改自己调用的方法名，很麻烦，使用了proprty()后，用户就不需担心这种问题了。
