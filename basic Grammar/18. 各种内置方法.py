# 10.12 作业
# 字典：各种内置方法

# 尝试编写一个用户登录程序（这次尝试将功能封装成函数），程序实现如图：
|---新建用户: N/n---|
｜---登录账号: E/e---|
｜---退出程序:Q/q---｜
｜---请输入指令代码：n
请输入用户名：小甲鱼
请输入密码：1234
注册成功，赶紧试试吧！
|---新建用户: N/n---|
｜---登录账号: E/e---|
｜---退出程序:Q/q---｜
｜---请输入指令代码：n
请输入用户名：小甲鱼
此用户已经使用，请重新输入：小鱿鱼
请输入密码：1234
注册成功，赶紧试试吧！
|---新建用户: N/n---|
｜---登录账号: E/e---|
｜---退出程序:Q/q---｜
｜---请输入指令代码：e
请输入用户名：小甲鱼
请输入密码：1234
欢迎进入xxoo系统，请点击右上角结束程序！
|---新建用户: N/n---|
｜---登录账号: E/e---|
｜---退出程序:Q/q---｜
｜---请输入指令代码：q

# 答：
storage = {}
while True:
    key = input('|---新建用户: N/n---|\n｜---登录账号: E/e---|\n｜---退出程序:\
Q/q---｜\n｜---请输入指令代码：')
    if key.upper() == 'N':
        user = input('请输入用户名：')
        if user in storage:
            user = input('此用户已经使用，请重新输入：')
        password = input('请输入密码：')
        print('注册成功，赶紧试试吧！')
        storage[user] = password
    elif key.upper() == 'E':
        user = input('请输入用户名：')
        if user not in storage:
            user=input('此用户名不存在，请重新输入：')
        password = input('请输入密码：')
        if storage[user] == password:
            print('欢迎进入xxoo系统，请点击右上角结束程序！')
    elif key.upper() == 'Q':
        break
    else:
        print('输入错误，请重试')
    
# 参考答案：
def load():
    dict1 = {'小甲鱼':'FishC'}
    while 1:
        key = input('''
|--- 新建用户：N/n ---|
|--- 登录帐号：E/e ---|
|--- 退出程序：Q/q ---|
|--- 请输入指令代码：''')
        if key == 'N' or key == 'n':
            temp_name = input('请输入用户名：')
            while temp_name in dict1:
                temp_name = input('此用户名已经被使用，请重新输入：')
 
            temp_password = input('请输入密码：')
            dict1[temp_name] = temp_password
            print('注册成功，赶紧试试登录吧^_^')
            continue
 
        elif key == 'E' or key == 'e':
            temp_name = input('请输入用户名:')
            while temp_name not in dict1:
                temp_name = input('您输入的用户名不存在，请重新输入：')
            temp_password = input('请输入密码：')
            while temp_password != dict1[temp_name]:
                temp_password = input('密码错误，请重新输入：')
            print('欢迎进入系统，请点右上角的X结束程序！')
            continue
 
        elif key == 'Q' or key == 'q':
            break
 
 
load()


# 课堂内容：
dict()是一个工厂函数，调用后会生成该类型的实例
>>> a = dict()
>>> type(a)
<class 'dict'>

字典的一种内建方法：dict1.fromkeys()，用于创建并返回一个新的字典
>>> dict1 = {}
>>> dict1.fromkeys((1,2,3))
{1: None, 2: None, 3: None}
>>> dict2 = {}
>>> dict2.fromkeys((1,2,3),"Number")
{1: 'Number', 2: 'Number', 3: 'Number'}
>>> dict3 = {}
>>> dict3.fromkeys((1,2,3), ("one","two","three"))
{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}

访问字典的方法：
1）dict1.keys() 返回键
2） dict1.values() 返回值
3）dict1.items() 返回键值对（也就是项）
4）dict1.get() 对应键的值不存在的话返回一个None，这样程序就不会报错
5）key in dict1 查找的是键，而不是值
6）dict1.clear() 清空字典，不建议使用直接赋空值的方法：dict1 = {}
7）dict1.copy()：浅拷贝（见练习题5）
8）dict1.pop()：给定键弹出相应值
9）dict1.popitem()：返回并删除字典中的最后一对键和值（包括键和值）
10）dict1.setdefault()：找不到给定键对应的值话会自动在字典中创建一个基于该键的项  （区别于dict1.get()的结果）
11）dict1.update()：根据一个字典或映射关系去更新另一个字典
收集参数时用**表示将参数们打包成字典的形式。之前介绍过以元组的形式组合，这一课介绍了以字典的形式打包

