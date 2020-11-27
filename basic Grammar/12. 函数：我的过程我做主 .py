# 10.8 作业
# 函数：我的地盘我做主

# 1.编写一个函数，判断传入的字符串参数是否为“回文联”（回文联即用回文形式写成的对联，既可顺读，也可倒读。例如：上海自来水来自海上）。

# 答：
def str1(sen1):
    list_sen1 = list(sen1)
    sen2 = list_sen1[:]
    if sen2 == list_sen1.reverse(): # list_sen1.reverse()返回空值，所以无法判断
        print('This sentence is back to the federation')
    else:
        print('This sentence is not back to the federation')

sen = input('please input your sentence to insure whether the sentence is back to the federation.\n')
str1(sen)

# 修改
def str1(sen1):
    list_sen1 = list(sen1)
    sen2 = list_sen1[:]
    list_sen1.reverse()
    if sen2 == list_sen1:
        print('This sentence is same when it is reversed')
    else:
        print('This sentence is not same when it is reversed')

sen = input('please input your sentence to insure whether the sentence is same when it is reversed .\n')
str1(sen)

# 参考答案：
# 第一种方法
def palindrome(string):
    length = len(string)
    last = length-1
    length //= 2
    flag = 1
    for each in range(length):
        if string[each] != string[last]:
            flag = 0
        last -= 1
    if flag == 1:
        return 1
    else:
        return 0
string = input('请输入一句话：')
if palindrome(string) == 1:
    print('是回文联!')
else:
    print('不是回文联！')

# 第二种方法
def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return '是回文联'
    else:
        return '不是回文联'

print(palindrome('1234abcdedcba4321'))

# 2.编写一个函数，分别统计出传入字符串参数（可能不只一个参数）的英文字母、空格、数字和其它字符的个数

# 答：
def cou(*x):
    str1 = list(x)
    count_str = 0
    count_blank = 0
    count_number = 0
    count_others = 0
    for i in str1: # 只能做单个字符串输入的查询,若str1为单个字符串，则i为字符串中每一个索引单位，即单个字母；若str1为列表或元组，则i为索引对应的每一个索引单位，即单个整体单位
        if i.isalpha() == True:
            count_str = count_str + 1
        elif i == ' ':
            count_blank += 1
        elif i.isdigit() == True:
            count_number += 1
        else:
            count_others += 1
    return print('The number of str is ', count_str,'\n','The number of blank is',\
                 count_blank, '\n', 'The number of number is', count_number,'\n', \
                 'The number of others is', count_others)

sen = input('please input your sentence')
cou(*sen)

# 修改：
def cou(*x):
    str1 = list(x)
    for j in str1:
        count_str = 0
        count_blank = 0
        count_number = 0
        count_others = 0
        for i in j:
            if i.isalpha() == True:
                count_str = count_str + 1
            elif i == ' ':
                count_blank += 1
            elif i.isdigit() == True:
                count_number += 1
            else:
                count_others += 1
        print('The %ded sentence has %d strs and %d blank and %d numbers and %d others'%(str1.index(j) + 1, count_str, count_blank, count_number, count_others)) # 注意： 索引值是从0开始，所以str1.index(j)需要 + 1
        
函数与过程：过程（procedure）是简单的，特殊且没有返回值的；函数（Function）有返回值， Python严格来说只有函数没有过程
返回值可以是一个int类型，可以返回一个列表，可以返回一个元组
局部变量：在局部生效如在函数中定义的变量
全局变量：作用于整个模块。函数内若试图修改全局变量，Python会新建一个同名局部变量用于存储修改值，原全局变量的值不变



