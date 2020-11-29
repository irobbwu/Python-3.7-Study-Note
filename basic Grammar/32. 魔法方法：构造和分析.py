# 11.27 作业
# 魔法方法：构造和分析

# 课后习题
# 1.小李做事常常丢三落四的，写代码也是一样，常常打开文件又忘记关闭。你能不能写一个FileObject类，给文件对象进行包装，从而确认在删除对象时文件能自动关闭

# 答：
class FileObject:
    def __init__(self, filename):
        self.file = open(filename, 'r+')
        
    def __del__(self):
        self.file.close()
        
# 参考答案
class FileObject:
    '''给文件对象进行包装从而确认在删除时文件流关闭'''
    def __init__(self, filename='sample.txt'):
        # 读写模式打开一个文件
        self.new_file = open(filename, 'r+')
    def __del__(self):
        self.new_file.close()
        del self.new_file  
        
# 2. 按照以下要求，定义一个类实现摄氏度到华氏度的转换（转换公式：华氏度=摄氏度*1.8+32）
# 要求：我们希望这个类尽量简练地实现功能。如下：
>>> print(C2F(32))
89.6

# 答：
class Trans(str):
    def __new__(cls, old_tem):
        new_tem = old_tem * 1.8 +32
        return str.__new__(cls, new_tem)
    
# 参考答案
class C2F(float):
    "摄氏度转换为华氏度"
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg * 1.8 + 32)
    
# 3.定义一个类继承于int类型，并实现一个特殊功能：当传入的参数是字符串的时候，返回该字符串中所有字符的ASCII码的和（使用ord()获取一个字符的ASCII码值）。
        
# 答：
class Int(int):
    def __new__(cls, character):
        if character.isalpha() == True:
            total = 0
            for i in character:
                ASC = ord(i)
                total = ASC + total
            return int.__new__(cls,total)
# 当输入‘ ‘、以及其他类型报错，因为isaplha（）判断的是输入是否全是字母，此时宜用isinstance判断类型。
            
# 参考答案：
class Nint(int):
    def __new__(cls, arg=0):
        if isinstance(arg, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total
        return int.__new__(cls, arg)


# 本章小节  
两个构造方法
1️⃣__ init__(self[,...])
这个方法一般用于初始化一个类。
但是，当实例化一个类的时候, __ init__()并不是第一个被调用的, 第一个被调用的是__ new__()。

class Test(object):
    """
    用于初始化类
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
一般在需要进行初始化的时候才重写__ init__()方法。而且要记住该方法的返回值一定是None（或者也可以理解没有返回值）。

2️⃣__ new__(cls[,...])
__ new__()方法是创建类实例的方法, 创建对象时调用, 返回当前对象的一个实例。下面是当继承一个不可变的类型的时候，它的特征就显得尤为重要了。

>>> class CapStr(str):
      def __new__(cls, string):
          string = string.upper()
          return str.__new__(cls, string)
      
>>> a = CapStr("I love Fishc")    
>>> a     
'I LOVE FISHC'
再看一段代码：

class Demo(object):
    def __init__(self):
        print('__init__() called...')

    def __new__(cls, *args, **kwargs):
        print('__new__() - {cls}'.format(cls=cls))
        return object.__new__(cls, *args, **kwargs)


if __name__ == '__main__':
    de = Demo()
输出：

__new__() - <class '__main__.Demo'>
__init__() called...
发现实例化对象的时候，调用__ init__()初始化之前，先调用了__ new__()方法。
__ new__()必须要有返回值，返回实例化出来的实例，需要注意的是，可以return父类__ new__()出来的实例，也可以直接将object的__ new__()出来的实例返回。
__ init__()有一个参数self，该self参数就是__ new__()返回的实例，__ init__()在__ new__()的基础上可以完成一些其它初始化的动作，__ init__()不需要返回值。
若__ new__()没有正确返回当前类cls的实例，那__ init__()将不会被调用，即使是父类的实例也不行。
我们可以将类比作制造商，__ new__()方法就是前期的原材料购买环节，__ init__()方法就是在有原材料的基础上，加工，初始化商品环节。

一个析构方法
3️⃣__ del__(self)
该方法是当垃圾回收机制回收这个对象时调用的。举个例子：

>>> class C:
      def __init__(self):
          print("我是__init__方法，我被调用了")
      def __del__(self):
          print("我是__del__方法，我被调用了")

>>> c1 = C()      
我是__init__方法，我被调用了
>>> c2 = c1   
>>> c3 = c2
>>> del c1    
>>> del c2    
>>> del c3
我是__del__方法，我被调用了
这里补充下Python垃圾回收机制的内容：

Python中的垃圾回收是以引用计数为主，分代收集为辅。引用计数的缺陷是循环引用的问题。
在Python中，如果一个对象的引用数为0，Python虚拟机就会回收这个对象的内存。
具体关于垃圾回收可参考：http://www.cnblogs.com/Xjng/p/5128269.html

           
            
            