# 12.5 作业

# 1.要求实现一个功能与reversed()相同的生成器，例如：
'''
>>> for i in myRev("FishC")
          print(i, end=' ')

ChsiF
'''

# 答：
def myRev(x):
    for i in range(len(x)):
        yield x[-i-1]
        
# 参考答案：
>>> def myRev(data):
    # 这里用range生成data的倒序索引
    # 注意，range的结束位置是不包含的
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
>>> for i in myRev("FishC.com"):
    print(i, end=' ')
    
m o c . C h s i F 

# 2.10以内的素数之和是：2+3+5+7=17，那么请编写程序，计算2000000以内的素数之和？

# 答：
def sumpr(n):
    x = 2
    sumprime = 17
    while x <= n:
        if x%2 != 0 and x%3 != 0 and x%5 != 0 and x%7 != 0:
            sumprime = sumprime + x
        x += 1
    return sumprime

'''
错误
素数判断规则错误
'''

# 参考答案：
import math

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2
    for next_prime in get_primes(3):  # 2是第一个素数，3是第二个素数，接下来靠+1往上走，靠素数判断方法判断是不是素数，是的话就累加
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

if __name__ == '__main__':
    solve()
            
# 本章小节：
'''
生成器更深入了解请点击
https://fishc.com.cn/thread-56023-1-1.html      
'''
        
    
        