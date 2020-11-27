# 8.20 作业
# 一、为用户提供三次机会尝试，机会用完或者用户猜中答案均退出循环

# 答
import random
ser = random.randint(1,10)
sp = input('please input your number?')
guess = int(sp)
i = 3,
while i:
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
    i = i - 1
print('game over')

# 自己改进
import random
sec = random.randint(1,10)
guess = input('Input your number!\nYou have three chances!')
reg = int(guess)
if sec == reg:
    print('Nice')
    print('There is no present')
    print('Game over!')
else:
    if reg < sec:
        print('Smaller a bit!')
        print('Please try again!')
        guess = input('Input your number!')
        reg = int(guess)
        if sec == reg:
            print('Nice')
            print('There is no present')
            print('Game over!')
        else:
            if reg < sec:
                print('Smaller a bit!')
                print('Please try again!')
                guess = input('Input your number!')
                reg = int(guess)
                if sec == reg:
                    print('Nice')
                    print('There is no present')
                    print('Game over!')
                else:
                    print('Wrong again!\nSorry, there is no chance!')
            if reg > sec:
                print('Bigger a bit!')
                print('Please try again!')
                guess = input('Input your number!')
                reg = int(guess)
                if sec == reg:
                    print('Nice')
                    print('There is no present')
                    print('Game over!')
                else:
                    print('Wrong again!\nSorry, there is no chance!') 
    if reg > sec:
        print('Bigger a bit!')
        print('Please try again!\n')
        guess = input('Input your number!')
        reg = int(guess)
        if sec == reg:
            print('Nice')
            print('There is no present')
            print('Game over!')
        else:
            if reg < sec:
                print('Smaller a bit!')
                print('Please try again!')
                guess = input('Input your number!')
                reg = int(guess)
                if sec == reg:
                    print('Nice')
                    print('There is no present')
                    print('Game over!')
                else:
                    print('Wrong again!\nSorry, there is no chance!')
            if reg > sec:
                print('Bigger a bit!')
                print('Please try again!')
                guess = input('Input your number!')
                reg = int(guess)
                if sec == reg:
                    print('Nice')
                    print('There is no present')
                    print('Game over!')
                else:
                    print('Wrong again!\nSorry, there is no chance!')

# 答案
import random
times = 3
secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
# 这里先给guess赋值（赋一个绝对不等于secret的值）
guess = 0
# print()默认是打印完字符串会自动添加一个换行符，end=" "参数告诉print()用空格代替换行
# 嗯，小甲鱼觉得富有创意的你应该会尝试用 end="JJ"？
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")
while (guess != secret) and (times > 0):
    temp = input()
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

# 对照答案模拟
import random
sec = random.randint(1,10)
reg = 0
times = 3 #( = 的意思是赋值， == 的意思是比较是否相等)
while reg != sec and times > 0:
    guess = input('Input your number!\n')
    reg = int(guess)
    if reg == sec:
        print('Nice')
        print('There is no present')
    else:
        print('Wrong.')
        if reg > sec:
              print('Bingger a bit!')
        if reg < sec:
              print('Smaller a bit!')
    times = times - 1
    if times > 0:
        print('Please try again!')
    else:
        print('There is no chance!')
print('Game over!') 

# 二、尝试写代码实现以下截图功能：
# 请输入一个整数:5
#     *****
#    ****
#   ***
#  **

# 答
number = input('Please input a Integer.')
ren = int(number)
while ren > 0:
    print(' ' * ren + '*' * ren)
    ren = ren - 1
# 答案1
temp = input('请输入一个整数:')
number = int(temp)
while number:
    i = number - 1
    while i:
        print(' ', end = '')
        i = i - 1
    j = number
    while j:
        print('*', end = '')
        j = j - 1
    print()
    number = number - 1
# 答案2
num = int(input("请输入一个整数："))
while num:
    print(' '*(num-1)+'*'*num)
    num -= 1
