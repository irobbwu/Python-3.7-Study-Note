# 9.12 作业
# 了不起的分支循环（1）
加载背景音乐
播放背景音乐（设置单曲循环）
我方飞机诞生
interval = 0
 
while True:
    if 用户是否点击了关闭按钮:
        退出程序
    interval += 1
    if interval == 50:
        interval = 0
        小飞机诞生
    小飞机移动一个位置
    屏幕刷新
 
    if 用户鼠标产生移动:
        我方飞机中心位置 = 用户鼠标位置
        屏幕刷新
 
    if 我方飞机与小飞机发生肢体冲突:
        我方挂，播放撞机音乐
        修改我方飞机图案
        打印"Game Over"
        停止背景音乐，最好淡出

# 了不起的分支循环（2）
# 一、按照100分制，90分以上成绩为A，80到90为B，60到80为C，60以下为D，写一个程序，当用户输入分数，自动转换为ABCD的形式打印。

# 答
score = int(input('请输入一个分数：'))
if 80 > score >= 60:
    print('C')
if 90 > score >= 80:
    print('B')
if 60 > score >= 0:
    print('D')
if 100 >= score >= 90:
    print('A')
else:
    print('输入错误！')

# 参考答案
score = int(input('请输入一个分数：'))
if 80 > score >= 60:
    print('C')
elif 90 > score >= 80:
    print('B')
elif 60 > score >= 0:
    print('D')
elif 100 >= score >= 90:
    print('A')
else:
    print('输入错误！')# elif 的好处是避免计算机重复运算导致的算力浪费，如果选用全是if的语句，则需运算5次
    
# 二、请将以下代码修改为三元操作符实现：
x, y, z = 6, 5, 4
if x < y:
    small = x
    if z < small:
        small = z
elif y < z:
    small = y
else:
    small = z

# 答
small = x if(x < y and z > x) else y if(y < z else z)

# 了不起的分支循环（3）
# 一、设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。：

# 答
pas = input('please input your password\n')
corpas = '1234'
times = 3

while times > 1:
    if '*' in pas:
        print('Please don\'t input * in password')
        pas = input('please re-input your password')
        continue
    if pas == corpas:
        print('right')
        break
    else:
        print('wrong, you remain three chances')
        pas = input('wrong, please re-input your password')
    times = times - 1
    
# 参考答案
count = 3
password = 'FishC.com'

while count:
  passwd = input('请输入密码：')
  if passwd == password:
      print('密码正确，进入程序......')
      break
  elif '*' in passwd:
      print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
      continue
  else:
      print('密码输入错误！您还有', count-1, '次机会！', end=' ')
  count -= 1

# 二、编写一个程序，求 100~999 之间的所有水仙花数。如果一个 3位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。：

# 答
# 不会（参考答案自己写一遍）
for i in range(100, 1000):
    sum = 0
    num = i
    while num > 0:
        sum = sum + (num%10)**3
        num = num//10
    if sum == i:
        print(i)
        
# 参考答案
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10         # 注意这里要使用地板除哦~
    if sum == i:
        print(i)

# 三、有红、黄、绿三种颜色的求，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。

# 答：
member = ['red', 'red', 'red', 'yellow', 'yellow', 'yellow', 'green', 'green', 'green', 'green', 'green', 'green']
for i in range (1, 496): # 思路错误，题目中只要求颜色搭配，不需要将每一种都写出来
    
print('red\tyellow\tgreen\t')
for i in range(0,4):
    for o in range(0,4):
        for p in range(0,7):
            if i + o + p == 8:
                print (i +'\t' + o + '\t' + p +'\t') # 字符串才可以用+拼接

# 参考答案
print('red\tyellow\tgreen')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
               # 注意，下边不是字符串拼接，因此不用“+”哦~
                print(red, '\t', yellow, '\t', green)
