# 10.12 作业
# 集合：在我的世界你就是唯一

# 1.试尝试将文件（OpenMe.mp3）打印到屏幕上。

# 参考答案
f = open('OpenMe.mp3')
for each_line in f:
    print(each_line , end='')
f.close()

输出结果：

长期使用Windows操作系统的朋友很容易被扩展名所误导，认为扩展名决定文件类型，其实这种观念是错误的！

其实这就跟一个姓张的坏人，尽管把名字改为了“张好人”，但他还是一个坏人是一个道理的^_^

关于文件的扩展名，初学者容易走进的误区：

误区一：文件扩展名是一个文件的必要构成部分

一个文件可以有或没有扩展名，对于打开文件操作，没有扩展名的文件需要选择程序去打开它，有扩展名的文件会自动用设置好的程序（如有）去尝试打开（是“尝试打开”，而不是“打开”的原因参看下面的第2个误区），文件扩展名是一个常规文件的构成部分，但一个文件并不一定需要一个扩展名。

误区二：文件扩展名表明了该文件是何种类型

文件扩展名可以人为设定，扩展名为TXT的文件有可能是一张图片，同样，扩展名为M-P3的文件，依然可能是一个视频。


# 2.编写代码，将上一题中的文件（OpenMe.mp3）保存为新文件（OpenMe. txt）

# 答：
f1 = open('/Users/yasmine/Desktop/fish.mp3')
f2 = open('/Users/yasmine/Desktop/fish.txt', 'w')
f1.seek(0, 0)
for i in f1:
    f2.write(i)
f2.close # 程序写完后记得close文件

# 参考答案：
# 第一种方法：
f1 = open('D:\Python\Python3\OpenMe.mp3')
f2 = open('D:\Python\Python3\OpenMe.txt','x')
for each_line in f1:
    f2.write(each_line)
f1.close()
f2.close()

#第二种方法
f1 = open('D:\Python\Python3\OpenMe.mp3')
f2 = open('D:\Python\Python3\OpenMe2.txt','x')
f2.write(f1.read())
f1.close()
f2.close()



# 本章小节：
打开模式    执行操作
'r'    以只读方式打开文件（默认）
'w'    以写入的方式打开文件，会覆盖已存在的文件（有风险**）
'x'    如果文件已经存在，使用此模式打开将引发异常
'a'    以写入模式打开，如果文件存在，则在末尾追加写入
'b'    以二进制模式打开文件
't'    以文本模式打开（默认）
'+'    可读写模式（可添加到其他模式中使用）
'U'    通用换行符支持

close()    关闭文件
read(size=-1)    从文件读取size个字符（单位是字节，中文算2个字节），   当未给定size或给定负值的时候，读取剩余的所有字符，然后作为字符串返回（注意这里的读取是从文件指针开始读取，而不是从初始位置）
readline()    从文件中读取一整行字符串（包括末尾的换行'\n'）
write(str)    将字符串str写入文件
writelines(seq)    向文件写入字符串序列seq，seq应该是一个返回字符串的可迭代对象
seek(offset, from)    在文件中移动文件指针，   从from（0代表文件起始位置，1代表当前位置，2代表文件末尾）偏移offset个字节
tell()    返回当前文件指针在文件中的位置

