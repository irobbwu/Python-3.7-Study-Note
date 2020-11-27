# 8.24 作业
# 一、当用户输入错误类型的时候，及时提醒用户重新输入，防止程序崩溃

# 答
import random
ser = random.randint(1,10)
sp = input('please input your number?')
if isinstance(sp, int) == False:# 报错，因为input输入的永远是字符串
    print('Please input an integer')
    sp = input('please input your number?')
    guess = int(sp)
    while guess != ser:
        sp = input('Wrong, please re-input your number?')
        guess = int(sp)
        if guess == ser:
            print('Nice')
            print('There is no present')
        else:
            if guess > ser:
                print('larger a bit')
            else:
                print('smaller a bit')
    print('game over')
else:
    guess = int(sp)
    while guess != ser:
        sp = input('Wrong, please re-input your number?')
        guess = int(sp)
        if guess == ser:
            print('Nice')
            print('There is no present')
        else:
            if guess > ser:
                print('larger a bit')
            else:
                print('smaller a bit')
print('game over')

# while
import random
sec = random.randint(1,10)
reg = 0
times = 3
while reg != sec and times > 0:
    guess = input('Input your number!\n')
    while type(guess) != type(1):# 报错，因为input输入的永远是字符串
        print('Wrong, please input an integer.')
        guess = input('Input your number!\n')
    reg = int(guess)
    if reg == sec:
        print('Nice')
        print('There is no present')
    else:
        print('Wrong.')
        if reg > sec:
              print('Bigger a bit!')
        if reg < sec:
              print('Smaller a bit!')
    times = times - 1
    if times > 0:
        print('Please try again!')
    else:
        print('There is no chance!')
print('Game over!')

# 改进
import random
sec = random.randint(1,10)
reg = 0
times = 3
while reg != sec and times > 0:
    guess = input('Input your number!\n')
    while guess.isdigit() == False:
        print('Wrong, please input an integer.')
        guess = input('Input your number!\n')
    reg = int(guess)
    if reg == sec:
        print('Nice')
        print('There is no present')
    else:
        print('Wrong.')
        if reg > sec:
              print('Bigger a bit!')
        if reg < sec:
              print('Smaller a bit!')
    times = times - 1
    if times > 0:
        print('Please try again!')
    else:
        print('There is no chance!')
print('Game over!')


# 参考答案
import random
times = 3
secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
guess = 0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        temp = input("抱歉，您的输入有误，请输入一个整数：")
    guess = int(temp)
    times = times - 1 # 用户每输入一次，可用机会就-1
    if guess == secret:
        print("我草，你是小甲鱼心里的蛔虫吗？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess > secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了，小了~~~")
        if times > 0:
            print("再试一次吧：", end=" ")
        else:
            print("机会用光咯T_T")
print("游戏结束，不玩啦^_^")


# 补充
# s为字符串
# s.isalnum()  所有字符都是数字或者字母，为真返回 Ture，否则返回 False。
# s.isalpha()   所有字符都是字母，为真返回 Ture，否则返回 False。
# s.isdigit()     所有字符都是数字，为真返回 Ture，否则返回 False。
# s.islower()    所有字符都是小写，为真返回 Ture，否则返回 False。
# s.isupper()   所有字符都是大写，为真返回 Ture，否则返回 False。
# s.istitle() 所有单词都是首字母大写，为真返回 Ture，否则返回 False。
# s.isspace()   所有字符都是空白字符，为真返回 Ture，否则返回 False。


# 写一个程序，判断给定年份是否为闰年。
time = input('Please input the number of year which is judged whether it is leap year.\n')
while time.isdigit() == False:
    time = input('Please input an integer.')
ret = int(time)
integer = ret/4#除法是浮点型
if isinstance(integer,int) == true:
    print('Yes, ' + ret + 'is a leap year.')# ret是整数型，不可以与字符型加减
else:
    print('No, ' + ret + 'is not a leap year.')

# 改进
time = input('Please input the number of year which is judged whether it is leap year.\n')
while time.isdigit() == False:
    time = input('Please input an integer.')
ret = int(time)
integer = ret/4
if integer == int(integer):
    print('Yes, ' + time + ' is a leap year.')
else:
    print('No, ' + time + ' is not a leap year.')


# 答案
temp = input("请输入一个年份：")
while not temp.isdigit():
    temp = input("输入不合法，请输入一个整数：")
year = int(temp)
if year == 0:
    print("%d 不是一个闰年！"%year)
else:
    if year%400 == 0:
        print("%d 是一个闰年！"%year)
    else:
        if year%4 == 0 and year%100 != 0:
            print("%d 是一个闰年！"%year)
        else:
            print("%d 不是一个闰年！"%year)
# +	加 	a + b 输出结果 30
# -	减	a - b 输出结果 -10
# *	乘	a * b 输出结果 200
# /	除	b / a 输出结果 2
# %	取余数	b % a 输出结果 0
# **	幂 	10**20 为10的20次方， 输出结果 100000000000000000000
# //	取整除（向下取整）	9//2=4  -9//2=-5

