# 10.8 作业
# 函数：内嵌函数和闭包
# 1.找字符串的密码。密码要求如下：                                 1>.密码为1个小写字母                                 2>.密码左右2边有且只有3个大写字母

# 参考答案
str1 = '''AAAbCCC#'''
countA = 0
countB = 0
countC = 0
target=0
length = len(str1)
for i in range(length):
    if str1[i] == '\n':
        continue
    if str1[i].isupper():
        if countB == 1:
            countC += 1
            countA = 0
        else:
            countA += 1
        if i<length-1:
            continue
    if str1[i].islower() and countA == 3:
        countB = 1
        countA = 0
        target = i
        continue
    if (str1[i].isupper()==False or i==length-1) and countC == 3:
        print(str1[target], end='')
    
    countA = 0
    countB = 0
    countC = 0





