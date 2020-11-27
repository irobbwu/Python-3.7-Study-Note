# 10.10 作业
# 字典：当索引不好用时

# 设计一个通讯录程序：
print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1:查询联系人资料 ---|')
print('|--- 2:插入新的联系人 ---|')
print('|--- 3:删除已有的联系人 ---|')
print('|--- 4:查看所有通讯录 ---|')
print('|--- 5:退出通讯录程序 ---|')


contacts = dict()

while True:
    instr = input('\n请输入相关的指令编号：')

    if instr.isdigit():
        instr = int(instr)
    else:
        print('抱歉，您的输入有误，请重新输入！')

    if instr == 1:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print('姓名\t手机号码')
            print(name + '\t' + contacts[name])
        else:
            print('抱歉，您输入的姓名不在通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        if name in contacts:
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + ': ' + contacts[name])
            if input('是否修改用户资料（YES/NO)：').upper() == 'YES':
                contacts[name] = input('请输入用户联系电话：')
        else:
            contacts[name] = input('请输入用户联系电话：')
            print('保持联系人' + name + '成功！')

    if instr == 3:
        name = input('请输入联系人姓名：')
        if name in contacts:
            del(contacts[name])
        else:
            print('您输入的联系人不存在。')

    if instr == 4:
        print('姓名\t手机号码')
        for key, value in contacts.items():
            print(key, value)

    if instr == 5:
        break

print('|--- 感谢使用通讯录程序！ ---|')
