# 10.10 作业
# 递归：这帮小兔崽子

# 课堂练习题：斐波那契数列
# 迭代算法：
def fi1(x):
    if x == 1 or x == 2:
        print('The number of rabbits is 1')
    else:
        n1 = 1
        n2 = 1
        n3 = 0
        i = 2
        while i < x:
            n3 = n2 + n1
            n1 = n2
            n2 = n3
            i = i + 1
        print('The number of rabbits is %d'%n2)

# 递归算法
def fi1(x):
    if x == 1 or x == 2:
        return 1
    else:
        return fi1(x - 1) + fi1(x - 2)

num = int(input('Please input the number to caculate the number of rabbits in the month'))
print('The number of rabbits is', fi1(num))

# 如果直接在程序中输入fi1()而不是print（fi1（））则fi1（）返回值不会在程序中显示

# 1.使用递归编写一个十进制转换为二进制的函数（要求采用“除2取余”的方式， 结果与调用bin（）一样返回字符串形式）

# 答：
y = []
def str1(x):
    if x == 0:
        y.append(x%2)
        print(y)
    else:
        return str1(x//2) # 编程错误，无法运行

# 参考答案：
def binB(num):
    # 剥洋葱思路
    # 每一次都要做两件事 num // 2; num % 2
    # 先预设一个空字符串: result
    result = ''

    if num:
        # 开始剥洋葱 num // 2，直到洋葱皮剥完为止
        # 当到最后一层（num = 1 ）
        # 开始把洋葱还原，返回 num % 2, 有点类似于出栈
        result = binB( num // 2)
        return result + str(num % 2)
    else:
        # 还原到最外面（实际是在剥到最后一片式，还原回去所有的result），出结果
        return result

# 修改：
y = []
def str1(x):
    if x > 0:
        y.append(x % 2)
        str1(x // 2)
    else:
        y.reverse()
        print(y)

# 2.写一个函数get_digits(n)，将参数n分解出每个位的数字并按顺序存放到列表中。 举例：get_digits(12345)==>[1,2,3,4,5]

# 答：
y = []
def get_digits(x):
    if x:
        y.append(x % 10)
        get_digits(x // 10)
    else:
        y.reverse()
        print(y)

# 参考答案：
result = []
def get_digits(n):
    if n > 0:
        result.insert(0, n % 10)
        get_digits(n // 10)

get_digits(123)
print(result)

# 3.回文联
def huiwen(temp,start,end):
    if start > end:
        return 1
    else:
        if temp[start] == temp[end]:
            return huiwen(temp,start+1,end-1)
        else:
            0

temp = input('请输入一段文字：')
length = len(temp)
end = length-1
if huiwen(temp,0,end):
    print('%s是一个回文字符串！'%temp)
else:
    print('%s不是一个回文字符串！'%temp)

# 4.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数， 他说比第三个人大两岁,  问第三个人，又说比第二个人大两岁，问第二个人，  又说比第1个人大两岁。 最后问第一个人，他说是10岁。请问第5个人多大？

# 答：
def age(x,i = 5):
    if i == 1:
        print(x)
    else:
        x = x + 2
        age(x, i - 1)

# 参考答案
def age(n):
    if n == 1:
        return 10
    else:
        return age(n-1) + 2

print("第五个人的岁数是%d岁" % age(5))

# 本节总结
汉诺塔
def hanoi(n,x,y,z):
    if n == 1:
        print(x,'->',z)
    else:
        hanoi(n-1,x,z,y)#将x上的前n-1个盘移动到y上
        print(x,'->',z)#将x上的n盘移动到z上
        hanoi(n-1,y,x,z)#将y盘上的n-1个盘移动到z上

n = int(input('请输入汉诺塔的层数：'))
hanoi(n,'X','Y','Z')
