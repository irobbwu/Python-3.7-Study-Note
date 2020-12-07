# 12.6 模块：__name__ == '__main__'
    
# 本章小节：
'''
__ name__ = '__ main__'
'''
# p13_7.py
def c2f(cel):
    fah = cel * 1.8 +32
    return fah

def f2c(fah):
    cel = (fah - 32) / 1.8
    return cel

def test():
    print("测试，0摄氏度 = %.2f 华氏度" % c2f(0))
    print("测试，0华氏度 = %.2f 摄氏度" % f2c(0))

if __name__ == '__main__':
    test()
# 上面代码确保只有单独运行p13_7.py时才会执行test()函数。

'''
搜索路径
写好的模块应该放在哪里？我们可以放在和导入这个模块文件的源代码同一个文件夹内。
还可以自己定义路径。
'''
>>> import sys
>>> sys.path
['', '/Users/liujin/Documents', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/easygui-0.98.0_UNRELEASED-py3.7.egg']
>>> sys.path.append('/Users/liujin/Documents/virtualenv3.7Demo/ven2')
>>> sys.path
['', '/Users/liujin/Documents', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python37.zip', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages', '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/easygui-0.98.0_UNRELEASED-py3.7.egg', '/Users/liujin/Documents/virtualenv3.7Demo/ven2']
>>> import p13_7 as tc
>>> print("32摄氏度 = %.2f 华氏度" % tc.c2f(32))
32摄氏度 = 89.60 华氏度
'''
包
1️⃣创建一个文件夹，用于存放相关的模块，文件夹的名字即包的名字；
2️⃣在文件夹中创建一个__ init__.py模块文件，内容可以为空；
3️⃣将相关的模块放入文件夹中。
'''

