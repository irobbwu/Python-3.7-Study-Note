# 10.9 作业
# 函数：递归

# 1.使用递归编写一个power()函数模拟内建函数pow()，即power(x, y)   为计算并返回x的y次幂的值。

# 答：
def power(x, y):
    if y > 0:
        return x * power(x, y - 1)
    else:
        return 1

# 参考答案：
#常规写法：
def power(x,y):
    result = 1
    for i in range(y):
        result *= x
    return result

#递归写法：
def power(x,y):
    if y == 0:
        return 1
    else:
        return x * power(x,y-1)


# 2.使用递归编写一个函数，利用欧几里得算法求最大公约数，例如gcd(x, y)返回值为参数x和参数y的最大公约数。

# 答：
def gcd(a, b):
    d = a % b
    c = a // b  # 欧几里得算法是gcd（a, b） = gcd(b, a%b)
    if d != 0:
        return gcd(b, c) # 所以此处改为 gcd（b，d）
    else:
        return b
        
# 修改
def gcd2(a, b):
    d = a % b
    c = a // b
    if d != 0:
        return gcd2(b, d)
    else:
        return b

# 参考答案：
def gcd(x,y):
    if y:
        return gcd(y,x%y)
    else:
        return x

# 课堂笔记
递归：是属于算法的范畴。 递归就是函数调用自身的一种行为。

#常规写法：
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i

    return result

number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number, result))

#递归写法：
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
number = int(input('请输入一个正整数：'))
result = factorial(number)
print("%d 的阶乘是：%d" % (number, result))
