# 10.7 作业
# 函数：python的乐高积木
# 1.编写一个函数power()模拟内建函数pow()，即power(x, y)为计算并返回x的y次幂的值。

def power(x, y):
    return (x ** y)
          
# 参考答案：
def power(x,y):
    result = x**y
    return result
    
print(power(2, 8))

# 2.编写一个函数，利用欧几里得算法求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数

def gcd(x,y):
    c = 1
    while c != 0:
       c = x % y
       x = y
       y = c
    return x

# 参考答案
def gcd(x,y):
    while y:
        t = x % y
        x = y
        y = t
    return x
print(gcd(18,9))


# 3.编写一个将十进制转换为二进制的函数，要求采用“除2取余”的方式，结果与调用bin()一样返回字符串形式。
def transfer(x):
    temp = []
    num = ''
    while x > 1: # 应该修改为>0
        y = x % 2
        x = x // 2
        temp = temp.append(y) # 数组的修改temp = temp.append(y)则返回空值
    while x != []:
        num = num + str(temp.pop())
    return num

# 参考答案：
def DectoBin(num):
    temp = []
    result = ''
    while num:
        x = num % 2  # 取余数，当做个位...十位...百位...以此类推
        num = num // 2  #取整数当做下一次的被除数
        temp.append(x)
    while temp:
        result += str(temp.pop())
    return result

print(DectoBin(444))
