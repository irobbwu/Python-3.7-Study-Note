#!/usr/bin/python
# -*- coding:utf-8 -*-
import time as t


class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()结束计时！"
        print("计时开始……")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()开始计时！")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
        # 为下一轮计算初始化变量
        self.begin = 0
        self.end = 0
        print(self.prompt)

    # 调用实例直接显示结果
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    # 计算两次计时器对象之和
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

# 优化：
#!/usr/bin/python
# -*- coding:utf-8 -*-
import time as t


class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.borrow = [1, 12, 31, 24, 60, 60]
        self.prompt = "未开始计时！"
        self.lasted = []
        self.begin = 0
        self.end = 0

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()结束计时！"
        print("计时开始……")

    # 停止计时
    def stop(self):
        if not self.begin:
            print("提示：请先调用start()开始计时！")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束！")

    # 内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            temp = self.end[index] - self.begin[index]
            # 低位不够减，需要向高位借位
            if temp < 0:
                # 测试高位是否有得借，没得借的话再向高位借……
                i = 1
                while self.lasted[index-i] < 1:
                    self.lasted[index-i] += self.borrow[index-i] - 1
                    self.lasted[index-i-1] -= 1
                    i += 1
                self.lasted.append(self.borrow[index] + temp)
                self.lasted[index-1] -= 1
            else:
                self.lasted.append(temp)

        # 由于高位随时会被借位，所以打印要放在最后
        for index in range(6):
            if self.lasted[index]:
                self.prompt += str(self.lasted[index]) + self.unit[index]

        # 为下一轮计算初始化变量
        self.begin = 0
        self.end = 0
        print(self.prompt)

    # 调用实例直接显示结果
    def __str__(self):
        return self.prompt
    __repr__ = __str__

    # 计算两次计时器对象之和
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt

'''
t1 = MyTimer()
t2 = MyTimer()
t1.start()
t.sleep(65)
t1.stop()
t2.start()
t.sleep(15)
t2.stop()
print(t1 + t2)
'''

# 既然咱都做到了这一步，那不如再深入以下，再次改进我们的代码，让它能够统计一个函数运行若干次的时间。
import time as t

class ProcessTimer:
    def __init__(self,function, default = 1000000):
        self.prompt = 'The timer hasn\'t been began'
        self.start = 0
        self.end = 0
        self.default = default
        self.function = function
    def __str__(self):
        return self.prompt
    
    def processing(self):
        self.start = t.perf_counter()
        while self.default:
            self.function()
            self.default -= 1
        self.end = t.perf_counter()
        self.lasted = self.end - self.start
        self.prompt = 'The processing lasted %0.2f'%self.lasted
        
    def __add__(self, other):
        new = self.lasted - other.lasted
        prompt = 'The processing lasted %0.2f'%new
        return promt
    
def test():
    text = 'I love fish.c.com'
    char = 'o'
    if char in text:
        pass

'''
t1 = ProcessTimer(test)
t1.timing()
print(t1)
t2 = ProcessTimer(test, 100000000)
t2.timing()
print(t2)
'''

# 本章小节
'''
通常在一段程序的前后都用上time.time(),然后进行相减就可以得到一段程序的运行时间，不过python提供了更强大的计时库：timeit
'''

#导入timeit.timeit
from timeit import timeit  

#看执行1000000次x=1的时间：
timeit('x=1')

#看x=1的执行时间，执行1次(number可以省略，默认值为1000000)：
timeit('x=1', number=1)

#看一个列表生成器的执行时间,执行1次：
timeit('[i for i in range(10000)]', number=1)

#看一个列表生成器的执行时间,执行10000次：
timeit('[i for i in range(100) if i%2==0]', number=10000)

'''
测试一个函数的执行时间：
'''
from timeit import timeit

def func():
    s = 0
    for i in range(1000):
        s += i
    print(s)

# timeit(函数名_字符串，运行环境_字符串，number=运行次数)
t = timeit('func()', 'from __main__ import func', number=1000)
print(t)
