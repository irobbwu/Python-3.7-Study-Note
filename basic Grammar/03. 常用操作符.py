# 8.24 作业
# 一、请写一个程序打印出 0~100 所有的奇数

iret = int(100)
while ret > 0:
    if ret % 2 != 0:
        print(ret)
    ret = ret -1


# 参考答案
i = 0
while i <= 100:
    if i % 2 != 0:
        print(i, end=' ')
        i += 1
    else:
        i += 1


# 有一个长阶梯，若每步上2阶，最后剩1阶；
# 若每步上3阶，最后剩2阶；若每步上5阶，最后剩4阶；
# 若每步上6阶，最后剩5阶；只有每步上7阶，最后刚好一阶也不剩。
x = 1
while 200> x > 0:
    if (x % 2 == 1 and x % 5 == 4) and (x % 3 == 2 and x % 6 == 5) and x % 7 == 0:
        print(x)
        x = x + 1
    else:
        x = x + 1


# 答案
x = 7
i = 1
flag = 0

while i <= 100:
    if (x%2 == 1) and (x%3 == 2) and (x%5 == 4) and (x%6==5):
        flag = 1
    else:
        x = 7 * (i+1) # 根据题意，x一定是7的整数倍，所以每次乘以7
    i += 1

if flag == 1:
    print('阶梯数是：', x)
else:
    print('在程序限定的范围内找不到答案！')
