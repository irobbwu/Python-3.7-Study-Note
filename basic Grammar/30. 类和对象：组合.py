# 11.25 作业
# 类和对象

# 课后习题
# 1.思考这一讲学习的内容，请动手在一个类中定义一个变量，用于跟踪类有多少个实例被创建（当实例化一个对象，这个变量+1，当销毁一个对象，这个变量自动-1）。

# 答：
class Count:
    count = 0
    def __init__(self):
        count += 1

UnboundLocalError: local variable 'count' referenced before assignment
# __init__是面向对象的，对象中没有count输入所以无法找到，修改方法参照参考答案

# 答案：
class C:
    count = 0
    def __init__(self):
        C.count += 1
    def __del__(self):
        C.count -= 1
        
# 2.定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特征的数据结构。至少需要有以下办法
isEmpty()	判断当前栈是否为空（返回True或False）
push()	往栈的顶部压入一个数据项
pop()	从栈顶弹出一个数据项（并在栈中删除）
top()	显示当前栈顶的一个数据项
botton()	显示当前栈底的一个数据项

class Stack:
    def __init__(self):
        self.store = []
        
    def isEmpty(self):
        if len(self.store) == 0:
            print('True')
        else:
            print('False')
            
    def push(self, x):
        self.store.append(x)
        
    def pop(self):
        self.store.pop(x)
        
    def top(self):
        print(self.store[-1])
        
    def botton(self):
        print(self.store[0])
    
    def showStack(self):
        print(self.store)
        
# 参考答案：
class Stack():
    def __init__(self, start=[]):
        self.stack = []
        for x in start:
            self.push(x)

    def isEmpty(self):  # 判断是否为空
        return not self.stack

    def push(self, obj):  # 入栈
        print("成功入栈数据：", obj)
        self.stack.append(obj)

    def pop(self):  # 出栈
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("成功出栈数据：", self.stack[-1])
            return self.stack.pop()

    def top(self):  # 显示第一个栈顶数据
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("栈顶数据为：", end="")
            return self.stack[-1]

    def bottom(self):  # 显示栈底数据
        if not self.stack:
            print("警告：栈为空！")
        else:
            print("栈底数据为：", end="")
            return self.stack[0]

    def showStack(self): # 展示栈内的所有数据（自己附加上去的方法，为了方便看栈内还有哪些数据）
        print("目前栈内的所有数据为：", end="")
        return self.stack[:]


s = Stack([])
print(s.isEmpty())  # True
s.push('1')
s.push('2')
s.push('3')
s.push('4')
s.push('5')
print(s.showStack())
print(s.top())  # 栈顶是5
s.pop()  # 5被弹出，栈顶变成4
print(s.showStack())
print(s.top())
print(s.bottom())

        