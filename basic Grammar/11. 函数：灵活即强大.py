# 10.7 作业
# 函数：灵活即强大
# 1.编写一个符合以下要求的函数：                                              a) 计算打印所有参数的和乘以基数（base=3）的结果                               b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。

# 答：
def sum3(*param, base = 3):  # 报错：param 输入为元组，pop只能用在列表
    param2 = param
    if param.pop() == 5:
        a = sum(param) * base
    else:
        a = sum(param) * base
    return a

# 修改：
def sum3(*param, base = 3):
    param3 = list(param)
    if param3.pop() == 5:
        base = 5
        a = sum(param) * base
    else:
        a = sum(param) * base
    return a

# 参考答案：
def Sum(*params,base=3):
    result = 0
    for i in params:
        result += i
    result *= base

    print('结果是：', result)

# 2.如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。

# 参考答案（对照‘9.12 了不起的分支循环’）：
#第一种方法：
def Daffodils():
    print('所有的水仙花数为：',end='')
    temp = 100
    while temp < 1000:
        if temp == (temp//100)**3 + ((temp%100)//10)**3 + (temp%10)**3:
            print(temp,end=' ')
            temp += 1
        else:
            temp += 1

Daffodils()

#第二种方法（更好)：
def Nacissus():
    print('所有的水仙花数为：',end='')
    for each in range(100, 1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp % 10) ** 3
            temp = temp // 10  #注意这里是地板除

        if sum == each:
            print(each, end='  ')

Nacissus()

#第三种方法：一行代码
a = [i**3+j**3+k**3 for i in range(1, 10) for j in range(0, 10) for k in range(0, 10) if i*100+j*10+k == i**3+j**3+k**3]
print(a)

# 3.编写一个函数findstr(),该函数统计一个长度为2的子字符串在另一个字符串中出现的次数。例如：假定输入的字符串为"You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.",子字符串为"im"，函数执行后打印“子字母串在目标字符串中共出现3次”

# 答：
def findstr(x):
    for i in x: # for i in x: 若x为字符串，则i为字符串的每一个字母（包括空格）
        if 2 == len(i):
            num = x.count(i)
            print(i,' do show up',num, ' times in the sentence')

# 修改：
def findstr():
    aim = input('What do you want to search?')
    ori = input('Please input original sentence')
    count = 0
    for i in range(len(ori)):
        if aim[0] == ori[i] and aim[1] == ori[i + 1]:
            count = count + 1
    print(aim, 'show up ',count, 'times in the sentence.')

# 参考答案：
#第一种方法
def findstr():
    print('请输入目标字符串：',end='')
    temp = input()
    print('请输入子字符串（两个字符）：',end='')
    comp = input()
    count = 0
    i = 0
    for i in range(len(temp)):
        if temp[i] == comp[0] and temp[i+1] == comp[1]:
            count += 1
            i += 1
        else:
            i += 1
    count = int(count)
    print('子字符串在目标字符串中总共出现 %d 次'%count)
findstr()

#第二种方法：不管大小写
def findStr(desStr, subStr):
    count = 0
    length = len(desStr)
    if subStr not in desStr:
        print('在目标字符串中未找到字符串!')
    else:
        for each1 in range(length):
            if desStr[each1].upper() == subStr[0].upper():
                if desStr[each1+1].upper() == subStr[1].upper():
                    count += 1
                    
        print('子字符串在目标字符串中共出现 %d 次' % count)
 
desStr = input('请输入目标字符串：')
subStr = input('请输入子字符串(两个字符)：')
findStr(desStr, subStr)

分清楚形参和实参
函数文档：是函数的一部分，与解释不同，使用help(函数名)或者 函数名____doc_____（前后分别两个下划线）可以查看到
关键字参数（在一个函数的参数较多的时候作用比较明显）：
给参数的名字下定义，例如：
def F(name,words)
如下两种引用的方法是等价的
F(A,B) = F(words=B,name=A)
默认参数：函数定义时为形参赋初值，函数调用时若没有传递参数，则自动使用初值
收集参数（可变参数）：

