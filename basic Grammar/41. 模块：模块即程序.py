# 12.6 模块：模块即程序

# 1:问大家一个问题：Python支持常量吗？相信很多鱼油的答案都是否定的，但实际上Python内建的命名空间是支持一小部分常量的，比如我们熟悉的True、False、None等，只是Python没有提供定义常量的直接方式而已。那么这一题的要求是创建一个const模块，功能是让Python支持常量。
'''
举个例子，下面是测试代码：

# const 模块就是这道题要求我们自己写的
# const 模块用于让Python支持常量操作
import const

const.NAME = "FishC"
print(const.NAME)

try:
    # 尝试修改常量
    const.NAME = "FishC.com"
except TypeError as Err:
    print(Err)

try:
    # 变量名需要大写
    const.name = "FishC"
except TypeError as Err:
    print(Err)
执行后的结果是：

>>>
FishC
常量无法改变！
常量名必须由大写字母组'成！
'''

''' Tips:
提示一：我们需要一个Const类
提示二：重写Const类的某一个魔法方法，指向当实例对象的属性被修改时的行为
提示三：检查该属性是否已存在
提示四：检查该属性的名字是否为大写
提示五：细心的鱼油可能发现了，怎么我们这个const模块导入之后就把它当对象来使用（const.NAME = "FishC"）了呢？难道模块也可以是一个对象？没错，在Python中无处不对象，到处都是你的对象。使用以下方法可以将你的模块与类A的对象挂钩。
'''

# 参考答案：
import os 
os.chdir('/Users/yasmine/Documents/学习/language/python/基本语法/boxing')

# const 模块就是这道题要求我们自己写的
# const 模块用于让Python支持常量操作
import const

const.NAME = "FishC"
print(const.NAME)

try:
    # 尝试修改常量
    const.NAME = "FishC.com"
except TypeError as Err:
    print(Err)

try:
    # 变量名需要大写
    const.name = "FishC"
except TypeError as Err:
    print(Err)
    
# 本章小节：
'''
模块
1️⃣容器 → 数据的封装
2️⃣函数 → 语句的封装
3️⃣类 → 方法和属性的封装
4️⃣模块 → 模块就是程序
命名空间
在Python中，每个模块都会维护一个独立的命名空间，我们应该将模块名加上，才能够正常使用模块中的函数。
导入模块
1️⃣import 模块名
2️⃣from 模块名 import 函数名
3️⃣import 模块名 as 新名字（推'荐）
'''

