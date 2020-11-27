# 10.12 作业
# 集合：在我的世界你就是唯一

# 课堂作业：将小甲鱼和客服的话分开
r = open('/Users/yasmine/Documents/学习/python/files/record.txt')
def new_file():
    boy_name = 'boy_' + str(count) + '.txt'
    boy_txt = open(boy_name, 'w')
    boy_txt.writelines(boy)
    girl_name = 'girl_' + str(count) + '.txt'
    girl_txt = open(girl_name, 'w')
    girl_txt.writelines(girl)
    boy_txt.close()
    girl_txt.close()

boy = []
girl = []
count = 1

for each_line in r:
    if each_line[:3] != '===':
        (name, text) = each_line.split(':', 1)
        if name == '小甲鱼':
            boy.append(text)
        elif name == '小客服':
            girl.append(text)
    else:
        new_file()
        count += 1

new_file()

# 1. 编写一个程序，接受用户的输入并保存为新的文件，程序实现如图：
请输入一个文件名：something.txt
请输入内容【单独输入‘:w’保存退出】
dsfdsfdsfsdf
sdfsdfsfdsf
sdfsdfsdfsdf

sdfsdfsdffd
sdfsdfsfdsfsdfsdf
sdfsdfsfdsf
sdfsdfsfdsf

:w

# 答：
def new_file():
    details = input('Please input details in the file[Input ‘：w’ only to save and exit.]')
    create_file = open(name, 'w')
    create_file2 = open('assistance.txt', 'w')
    while details != ':w':
        create_file2.write(details + '\n')
        details = input()
    create_file2.close
    create_file2 = open('assistance.txt')
    for i in create_file2:
        if i[:2] != ':w': # 直接i != ‘：w’ 即可，因为单独输入，即为一行
            create_file.writelines(i)
        else:
            create_file.close
            break
    print('The file has been created.')
    
name = input('Please input your file name')
new_file()

# 代码修改优化：
def new_file():
    details = input('Please input details in the file[Input ‘：w’ only to save and exit.]')
    create_file = open(name, 'w')
    while details != ':w':
        create_file.write(details + '\n')
        details = input()
    create_file.close
    print('The file has been created.')

name = input('Please input your file name')
new_file()

# 参考答案：
def filewrite(file_name):
    print('请输入内容【单独输入‘:w’保存退出】：')
    f = open(file_name, 'w')
    while True:
        a = input()
        if a != ':w':
            f.write('%s\n' % a)  # 注意这里有换行符
        else:
            break

    f.close()


file_name = input('请输入文件名：')
filewrite(file_name)


# 2. 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个    不同字符的位置，程序实现如图：

Please input the 1st file name you want to make a comparison
1.txt
Please input the 2ed file name you want to make a comparison
2.txt
The 2ed line is different
The 6ed line is different
The 7ed line is different
There are 3 didderence between the two files

# 答：
def comparison(x, y):
    obj1 = open(x)
    obj2 = open(y)
    list_obj2 = list(obj2)
    line_count = 0
    for i in obj1:
        line_count += 1
        if i != list_obj2[line_count - 1]:
            print('The %ded line is different'%line_count)
            count += 1
         print('There are %d didderence between the two files'%count)
    # 想把总计打在分步上面可以借助列表代替
    obj1.close()
    obj2.close()
        
    
    
file1 = input('Please input the 1st file name you want to make a comparison\n')
file2 = input('Please input the 2ed file name you want to make a comparison\n')
comparison(file1, file2)

# 修改：
def comparison(x, y):
    obj1 = open(x)
    obj2 = open(y)
    list_obj2 = list(obj2)
    count = 0
    line_count = 0
    list_assist = []
    for i in obj1:
        line_count += 1
        if i != list_obj2[line_count - 1]:
            count += 1
            list_assist.append(line_count)
    print('There are %d didderence between the two files'%len(list_assist))
    for j in list_assist:
        print('The %ded line is different'%j)
    
    obj1.close()
    obj2.close()
    
file1 = input('Please input the 1st file name you want to make a comparison\n')
file2 = input('Please input the 2ed file name you want to make a comparison\n')
comparison(file1, file2)

# 参考答案：
def file_compare(file1, file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0  # 统计行数
    differ = []  # 统计不一样的数量
    for line1 in f1:
        line2 = f2.readline()
        count += 1
        if line1 != line2:
            differ.append(count)

    f1.close()
    f2.close()
    return differ


file1 = input('请输入需要比较的头一个文件名：')
file2 = input('请输入需要比较的另一个文件名：')

differ = file_compare(file1, file2)

if len(differ) == 0:
    print('两个文件完全一样！')
else:
    print('两个文件共有【%d】处不同：' % len(differ))
    print(differ)
    for each in differ:
        print('第%d行不一样' % each)

# 3.编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上，    程序实现如图

# 答：
def vision(x):
    aim_file = open(file_name)
    count = 0
    for i in aim_file:
        count += 1
        if count <= x:
            print(i, end = '')
    aim_file.close




file_name = input('Please input the file name you want to open')
num = int(input('Please input the line'))
vision(num)

# 参考答案：
# 第一种方法
def file_print(file, num):
    f = open(file)
    print('''文件%s的前%d行的内容如下：''' % (file, num))
    for i in range(num):
        print(f.readline())
    f.close()


file_name = input('请输入要打开的文件（C:\\test.txt）：')
num = int(input('请输入需要显示该文件前几行：'))
file_print(file_name, num)

# 第二种方法
def file_view(file_name, line_nun):
    print('\n文件%s的前%s的内容如下：\n' % (file_name, line_num))
    f = open(file_name)
    for i in range(int(line_num)):
        print(f.readline(), end='')
    f.close()


file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
line_num = input('请输入需要显示该文件前几行：')
file_view(file_name, line_num)

# 4.呃，不得不说我们的用户变得越来越刁钻了。要求在上一题的基础上扩展，用户可以随意输入   需要显示的行数。（如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容）

# 答：
file_name = input('Please input the file name you want to open')
aim_file = open(file_name)
num = input('Please input the row interval(like(12:25))')
[num1,num2] = num.split(':')
if num1 == '':
    num1 = 0
if num2 == '':
    num2 = len(list(aim_file)) # 对文件操作很可能会改变文件的索引值 list为例
num1 = int(num1)
num2 = int(num2)
count = 0
for i in aim_file:
    count += 1
    if num1 <= count <= num2:
            print(i, end = '')
aim_file.close

# 修改：
file_name = input('Please input the file name you want to open')
aim_file = open(file_name)
num = input('Please input the row interval(like(12:25))')
[num1,num2] = num.split(':')
if num1 == '':
    num1 = 0
if num2 == '':
    num2 = len(list(aim_file))
    aim_file.seek(0,0)
num1 = int(num1)
num2 = int(num2)
print(aim_file.tell())
count = 0
for i in aim_file:
    count += 1
    if num1 <= count <= num2:
            print(i, end = '')
aim_file.close()

# 参考答案：
def file_print(file, paragraph):
    (start, end) = paragraph.split(':')
    if start == '':
        start = 1
    else:
        start = int(start)
    if end == '':
        end = -1
    else:
        end = int(end)

    f = open(file)
    if start == 1:
        if end == -1:
            print('''文件%s的从开头到结束的内容如下：''' % file)
        else:
            print('''文件%s的从开头到第%d行的内容如下：''' % (file, end))
    else:
        if end == -1:
            print('''文件%s的从%d行到结束的内容如下：''' % (file, start))
        else:
            print('''文件%s的从第%d行到第%d行的内容如下：''' % (file, start, end))

    for i in range(start - 1):
        f.readline()
    num = end - start + 1
    if num < 0:
        print(f.read())
    else:
        for i in range(num):
            print(f.readline())
    f.close()


file_name = input(r'请输入要打开的文件（C:\\test.txt）：')
paragraph = input('请输入需要显示的行数【格式如13：21或：21或21：】：')
while paragraph == '':
    paragraph = input('输入有误，请重新输入：')
file_print(file_name, paragraph)

# 5.编写一个程序，实现“全部替换”功能
请输入文件名：33.txt
请输入需要替换的单词或字符：小丑鱼
请输入新的单词或字符：小甲鱼

文件 33.txt 中共有19个【小丑鱼】
您确定要把所有的【小丑鱼】替换为【小甲鱼】吗？
【YES/NO】：YES

# 答：
def replace(file, word1, word2):
    a = open(file)
    count = 0
    global assist
    assist = []
    for i in a:
        num = i.count(word1)
        count += num
    print('The %s shows up %d times in the %s'%(word1, count, file))
    order = input('Are you sure to change all %s to %s [Yes or No]'%(word1, word2))
    if order.upper() == 'YES': # 输出为none， 在上面329行用过了a，则文件的索引值改变, 最好在使用文件时一次把命令写完，或者每次用完a后加a.seek(0, 0)
        for i in a:
            if word1 in i:
                new_sen = i.replace(word1, word2)
                print(new_sen)
                assist.append(new_sen)
            else:
                assist.append(i)
        a.close()
        a = open(file, 'w')
        a.writelines(assist)
        a.close()
    elif order.upper == 'NO':
        print('Exit')
        return None
    
file = input('Input the file you want to open')
word1 = input('Input the word replaced you want to')
word2 = input('Input the word you want to replace')
replace(file, word1, word2)

# 修改
def replace(file, word1, word2):
    a = open(file)
    count = 0
    global assist
    assist = []
    for i in a:
        num = i.count(word1)
        count += num
        if word1 in i:
            new = i.replace(word1, word2)
            assist.append(new)
        else:
            assist.append(i)
    a.close()
    print('The %s shows up %d times in the %s'%(word1, count, file))
    order = input('Are you sure to change all %s to %s [Yes or No]'%(word1, word2))
    a = open(file, 'w')
    if order.upper() == 'YES':
        a.writelines(assist)
    else:
        print('wrong input')
    a.close()
  
    
file = input('Input the file you want to open')
word1 = input('Input the word replaced you want to')
word2 = input('Input the word you want to replace')
replace(file, word1, word2)

# 参考答案
def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for each_line in f_read:
        if rep_word in each_line:
            count += each_line.count(rep_word)  # count感觉应该用这个
            each_line = each_line.replace(rep_word, new_word)
        content.append(each_line)

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (file_name, count, rep_word, rep_word, new_word))

    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()


file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)
