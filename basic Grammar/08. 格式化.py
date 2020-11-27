# 9.30 作业
# 格式化
%c    格式化字符及其ASCII码
%s    格式化字符串
%d    格式化整数
%o    格式化无符号八进制数
%x    格式化无符号十六进制数
%X    格式化无符号十六进制数（大写）
%f    格式化定点数，可指定小数点后的精度
%e    用科学计数法格式化定点数
%E    作用同%e，用科学计数法格式化定点数
%g    根据值的大小决定使用%f或者%e
%G    作用同%g，根据值的大小决定使用%F或者%E

\'    单引号
\"    双引号
\a    发出系统响铃声
\b    退格符
\n    换行符
\t    横向制表符（TAB）
\v    纵向制表符
\r    回车符
\f    换页符
\o    八进制数代表的字符
\x    十六进制数代表的字符
\0    表示一个空字符
\\    反斜杠

m.n    m是显示的最小总宽度，n是小数点后的位数
-    用于左对齐
+    在正数前面显示加号（+）
#    在八进制数前面显示 '0o'，在十六进制数前面显示 '0x' 或 '0X'
0    显示的数字前面填充 '0' 取代空格

# 作业
# 一.编写一个进制转换程序，程序演示如下（提示，十进制转换二进制可以用bin()这个BIF）：
# 答：
while True:
    num = input('Plaese input a integer.(Input Q to end):')
    if num == 'Q': # 可以用upper（）函数改成小写q也可以结束程序
        print('END')
        break
    else:
        number = int(num)
        number16 = '%#x' % number
        number8 = '%#o' % number
        number2 = bin(number)
        print('Decimal -> Hexadecimal:', number, '->',number16)
        print('Decimal -> Octal:', number, '->',number8)
        print('Decimal -> Octal:', number, '->',number2)
        
# 修改：
while True:
    num = input('Plaese input a integer.(Input Q to end):')
    num2 = num.upper()
    if num2 == 'Q' :
        print('END')
        break
    else:
        number = int(num)
        number16 = '%#x' % number
        number8 = '%#o' % number
        number2 = bin(number)
        print('Decimal -> Hexadecimal:', number, '->',number16)
        print('Decimal -> Octal:', number, '->',number8)
        print('Decimal -> Octal:', number, '->',number2)

# 参考答案：
num = input("请输入一个整数（输入Q结束程序）：")
while num.upper() != 'Q':
    if num.isdigit():
        num = int(num)
        print('十进制 -> 十六进制：%d -> %#x'%(num,num))
        print('十进制 -> 八进制：%d -> %#o'%(num,num))
        print('十进制 -> 二进制：%d -> '%num,bin(num))
        num = input("请输入一个整数（输入Q结束程序）：")
    else:
        if num == 'Q':
            break
        else:
            num = input("输入不合法，请输入一个整数（输入Q结束程序）：")

# 课程记录
、>>> "{0} love {1}.{2}".format("I", "FishC", "com")
'I love FishC.com'
>>> "{a} love {b}.{c}".format(a = "I", b = "FishC", c = "com")
'I love FishC.com'
