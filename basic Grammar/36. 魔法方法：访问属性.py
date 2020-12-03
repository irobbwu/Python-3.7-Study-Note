# 魔法方法：访问熟悉

# 1.请问以下代码的作用是什么？这样写正确吗？（如果不正确，请改正）

def __setattr__(self, name, value):
        self.name =  value + 1
        
# 答：这段代码试图在对象的属性发生赋值操作的时候，将实际的值+1赋值给相应的属性。但这么写法是错误的，因为每当属性被赋值的时候，__ setattr__()会被调用，而里面的self.name = value + 1语句又会再次触发__ setattr__()调用，导致无限递归。

def __setattr__(self, name, value):
        self.__dict__[name]  =  value + 1

def __setattr__(self, name, value):
        super().__setattr__() =  value + 1
        
# 2. 按要求重写魔法方法：访问一个不存在的属性时，不报错并且提示“该属性不存在！”

# 答：        
class Reset:
    def __getattr__(self, x):
        print('attr')
        return 'Don\'t exist!'
    
# 3. 编写Demo类，使得下边代码可以正常运行：   
'''
>>> demo = Demo()
>>> demo.x
'FishC'
>>> demo.x = "X-man"
>>> demo.x
'X-man'
'''
# 答：
class Demo:
    x = 'FishC'

# 参考答案：
>>> class Demo:
    def __getattr__(self, name):
        self.name = 'FishC'
        return self.name
    
>>> demo = Demo()
>>> demo.x
'FishC'
>>> demo.x = "X-man"
>>> demo.x
'X-man'

# 4.修改上班第4题，使之可以正常运行；编写一个Counter类，用于实时检测对象有多少个属性。
'''
>>> c = Counter()
>>> c.x = 1
>>> c.counter
1
>>> c.y = 1
>>> c.z = 1
>>> c.counter
3
>>> del c.x
>>> c.counter
2
'''

# 答：
class Count:
    def __init__(self):
        super().__setattr__('count', 0)
        
    def __setattr__(self, x, value):
        super().__setattr__('count', self.count + 1)
        super().__setattr__(x, value)
    
    def __delattr__(self):
        self.counter -= 1
        # 报错：self.count -= 1又重新赋值，调用了__setattr__

# 参考答案：
>>> class Counter:
    def __init__(self):
        super().__setattr__('counter', 0)
    def __setattr__(self, name, value):
        super().__setattr__('counter', self.counter + 1)
        super().__setattr__(name, value)
    def __delattr__(self, name):
        super().__setattr__('counter', self.counter - 1)
        super().__delattr__(name)
        
# 本章小节：
'''
属性相关的魔法方法
魔法方法	含义
__ getattr__(self, name)	定义当用户试图获取一个不存在的属性时的行为
__ getattribute__(self, name)	定义当该类的属性被访问时的行为
__ setattr__(self, name, value)	定义当一个属性被设置时的行为
__ delattr__(self, value)	定义当一个属性被删除时的行为
属性魔法方法初学者容易犯死循环如何避免？
第一种：用super()来调用基类，比如：super().__ setattr__(name, value)
第二种：给特殊属性__ dict__赋值，比如：self.__ dict__[name] = value
'''
