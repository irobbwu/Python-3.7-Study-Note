# 10.13 作业
# 文件系统：一个高大上的东西

# 1.编写一个程序，统计当前目录下每个文件类型的文件数，程序实现如图：
Please input the path you want to look up   /Users/yasmine/Documents/学习/python
The txt files under the path is 8
The png files under the path is 0
The py files under the path is 1
The docx files under the path is 0
The folder files under the path is 3

# 答：
def count_file(path):
    import os
    txt_count = 0
    png_count = 0
    py_count = 0
    docx_count = 0
    folder_count = 0
    all_files = os.listdir(path)
    for i in all_files:
        (name, extension) = os.path.splitext(i)
        if extension == '.txt':
            txt_count += 1
        elif extension == '.png':
            png_count += 1
        elif extension == '.py':
            py_count += 1
        elif extension == '.docx':
            docx_count += 1
        elif extension == '':
            folder_count += 1
    print('The txt files under the path is %d'%txt_count)
    print('The png files under the path is %d'%png_count)
    print('The py files under the path is %d'%py_count)
    print('The docx files under the path is %d'%docx_count)
    print('The folder files under the path is %d'%folder_count)

path = input('Please input the path you want to look up')
count_file(path)

# 参考答案：
import os

all_files = os.listdir(os.curdir)  # 使用os.curdir表示当前目录更标准
type_dict = dict()  # 先定一个空字典来存放{'后缀名': 数量}

for each_file in all_files:
    if os.path.isdir(each_file):
        type_dict.setdefault('文件夹', 0)  # 当原字典中无该键时，则新增该键和对于的值，并返回键值
        type_dict['文件夹'] += 1
    else:
        ext = os.path.splitext(each_file)[1]  # 返回的是元组，获取文件的后缀名=ext
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))
    
# 根据参考答案修改：
def count_file(path):
    import os
    all_files = os.listdir(path)
    folder_count = 0
    sum_ext = []
    for i in all_files:
        (name, extension) = os.path.splitext(i)
        if extension == '':
                        folder_count += 1
         # 分为空不一定就是文件夹格式，比如.DS_Store
         # 改进：if os.path.isdir(i):    # 此时的i只是文件名字，当其为文件名字是，要改变其路径，加入os.chdir(path)         folder_count += 1
        else:
            sum_ext.append(extension.replace('.', ''))
    sum_extset = set(sum_ext)
    for j in list(sum_extset):
        file_count = sum_ext.count(j)
        print('The %s files under the path is %d'%(j, file_count))
    print('The folder files under the path is %d'%folder_count)

path = input('Please input the path you want to look up')
count_file(path)

# 修改：
def count_file(path):
    import os
    os.chdir(path)
    all_files = os.listdir(path)
    folder_count = 0
    sum_ext = []
    for i in all_files:
        (name, extension) = os.path.splitext(i)
        if os.path.isdir(i):
            folder_count += 1
        else:
            sum_ext.append(extension.replace('.', ''))
    sum_extset = set(sum_ext)
    for j in list(sum_extset):
        file_count = sum_ext.count(j)
        print('The [%s] files under the path is %d'%(j, file_count))
    print('The folder files under the path is %d'%folder_count)

path = input('Please input the path you want to look up')
count_file(path)


# 2.编写一个程序，计算当前文件夹下所有文件的大小，程序实现如图：
boy_4.txt [283 Bytes]
boy_1.txt [105 Bytes]
practice.py [276 Bytes]
boy_2.txt [160 Bytes]
Homework [832 Bytes]
2.txt [64 Bytes]
files [160 Bytes]
1.txt [66 Bytes]
girl_4.txt [718 Bytes]
girl_1.txt [271 Bytes]
girl_2.txt [524 Bytes]

# 答：
def size_file(path):
    import os
    os.chdir(path)
    all_files = os.listdir(path)
    for i in all_files:
        size = os.path.getsize(i)
        print(i,'[%s Bytes]'%size)
    

path = input('Please input the path you want to look up')
size_file(path)

# 模仿使用字典：
def size_file(path):
    import os
    os.chdir(path)
    dic_help = {}
    all_files = os.listdir(path)
    for i in all_files:
        dic_help[i] = os.path.getsize(i)
        print(i,'[%d Bytes]'%dic_help.get(i))

path = input('Please input the path you want to look up')
size_file(path)

# 参考答案：
import os

def file_size():
    file_name = os.listdir(os.curdir)
    dict1 = dict()

    for each_file in file_name:
        if os.path.isfile(each_file):
            dict1.setdefault(each_file, os.path.getsize(each_file))
            print('%s的大小为：【%d Bytes】' % (each_file, dict1[each_file]))

file_size()

# 3.编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索，程序实现如图：
Please input the path you want to look up/Users/yasmine/Documents/学习/language/python
Please input the file you want to look up1.txt
/Users/yasmine/Documents/学习/language/python/1.txt
/Users/yasmine/Documents/学习/language/python/1/1.txtx
/Users/yasmine/Documents/学习/language/python/Homework/1.txt
/Users/yasmine/Documents/学习/language/python/files/1.txt
# 答：
def search_file(path, name):
    import os
    os.chdir(path)
    list_file = os.listdir(path)
    print(list_file)
    if name in list_file:
        print(path + '/' + name)
    for i in list_file:
        if os.path.isdir(i):
            print(i)
            path = path + '/' + i
            search_file(path, name) # 递归后没有返回上一层目录，导致name一直在新的path下操作，os.path.isdir()无法判断，若是多层目录，os.dir()是全局设置

path = input('Please input the path you want to look up')
file_name = input('Please input the file you want to look up')
search_file(path, file_name)


def search_file(path, name):
    import os
    os.chdir(path)
   
    if name in os.listdir(os.curdir):
        print(path + '/' + name)
    for i in os.listdir(os.curdir):
        if os.path.isdir(i):
            path = path + '/' + i
            search_file(path, name)
            os.chdir(os.pardir)

path = input('Please input the path you want to look up')
file_name = input('Please input the file you want to look up')
search_file(path, file_name) # 报错：


# 参考答案：
import os

def search_file(start_dir, target):
    os.chdir(start_dir)  # 切换当前工作目录

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file)  # 使用os.sep使程序更标准
        if os.path.isdir(each_file):
            search_file(each_file, target)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录

start_dir = input('请输入待查找的初始目录：')
target = input('请输入需要查找的目标文件：')
search_file(start_dir, target)

# 4.编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹内）所有的视频格式文件（要求查找mp4, rmvb, avi的格式即可），并把创建一个文件（vedioList.txt）存放所有找到的文件的路径，程序实现如图：

# 答：
import os

def search():
    os.chdir(path)
    newfiles = open('/Users/yasmine/Documents/学习/language/python/vediolist.txt', 'w')
    video_list = []
    for i in os.walk(path):
        for l in i[2]:
            if os.path.splitext(l)[1] in ['.mp4', '.rmvb', '.avi']:
                video_list.append(i[0] + '/' + l)
    for j in video_list:
        newfiles.write(j + '\n')
    newfiles.close()

print('This program is to look for all videos in the path you input.')
path = input('Please input your path.')
search()

# 参考答案：
import os

vedio_list = []

def search_file(start_dir):
    os.chdir(start_dir)
    for each_file in os.listdir(os.curdir):
        if os.path.isfile(each_file):
            file_ext = os.path.splitext(each_file)[1]
            if file_ext in ['.mp4', '.rmvb', '.avi']:
                vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)
        if os.path.isdir(each_file):
            search_file(each_file)  # 递归调用
            os.chdir(os.pardir)  # 递归调用后切记返回上一层目录
    return vedio_list

start_dir = input('请输入待查找的初始目录：')
vedio_list = search_file(start_dir)
f = open(os.getcwd() + os.sep + 'VedioList.txt', 'w')
f.writelines(vedio_list)
f.close()


# 5. 编写一个程序，用户输入关键字，查找当前文件夹内（如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有该关键字的文本文件（.txt后缀），要求显示该文件所在的位置以及关键字在文件中的具体位置（第几行第几个字符），程序实现如图：

# 答：
import os

def keyword(x):
    os.chdir(path)
    for i in os.listdir(os.curdir):
        (name, extention) = os.path.splitext(i)
        x_assist = list(x)
        if extention == '.txt':
            file = open(i)
            line = 0
            count = 0
            file_location = []
            location = []
            for j in file:
                line += 1
                if x in j:
                    count += 1
                    num = 0
                    for k in j:
                        num += 1
                        if x_assist[0] == k:
                            if x_assist[:] == j[num - 1 : num - 1 + len(x)]:
                                file_location.append(number)
                    print('The %sed line %sed word is what you are looking for in the file'%(line,file_location))
            file.close()
        elif os.path.isdir(i):
            keyword(i)
            os.chdir(os.pardir) # 报错，递归太多，程序崩溃

x = input('Please the keyword you want to look up.')
path = input('Please input the path you want to look up')
keyword(x)

# 参考答案：
import os


def print_pos(key_dict):  # 负责打印
    keys = key_dict.keys()
    keys = sorted(keys)  # 由于字典是无序的，我们这里对行数进行排序
    for each_key in keys:
        print('关键字出现在第 %s 行，第 %s 个位置。' % (each_key, str(key_dict[each_key])))


def pos_in_line(line, key):
    pos = []
    begin = line.find(key)
    while begin != -1:
        pos.append(begin + 1)  # 用户的角度是从1开始数
        begin = line.find(key, begin + 1)  # 从下一个位置继续查找

    return pos


def search_in_file(file_name, key):
    f = open(file_name)
    count = 0  # 记录行数
    key_dict = dict()  # 字典，用户存放key所在具体行数对应具体位置

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key)  # key在每行对应的位置
            key_dict[count] = pos

    f.close()
    return key_dict


def search_files(key, detail):
    all_files = os.walk(os.getcwd())
    txt_files = []

    for i in all_files:
        for each_file in i[2]:
            if os.path.splitext(each_file)[1] == '.txt':  # 根据后缀判断是否文本文件
                each_file = os.path.join(i[0], each_file)
                txt_files.append(each_file)

    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key)
        if key_dict:
            print('================================================================')
            print('在文件【%s】中找到关键字【%s】' % (each_txt_file, key))
            if detail in ['YES', 'Yes', 'yes', 'Y', 'y']:
                print_pos(key_dict)


key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字【%s】在文件中的具体位置（YES/NO）：' % key)
search_files(key, detail)

# 修改：
import os

def search(words):
    os.chdir(path)
    for l in os.walk(path):
        for i in l[2]:
            if os.path.splitext(i)[1] == '.txt':
                line = 0
                count = 0
                file = open(l[0] + '/' + i) # 极其注意文件位置，要不然极容易找不到文件
                file_location = []
                for j in file:
                    line += 1  # 行数逻辑混乱，应该是每一行都重新算字的排序顺序
                    if words in j:
                        count += 1
                        num = 0
                        for k in j:
                            num += 1
                            if x[0] == k:
                                if x == j[num - 1 : num - 1 + len(x)]:
                                    file_location.append(num)
                file.close()
                if count:
                    print(i[0])
                    print('The %ded line %sed word is what you are looking for in the %s/%s'%(line, file_location, l[0], i))
path = input('Please input the path you want to look up')
x = input('Please the keyword you want to look up.')
search(x)

# 修改改正：
import os

def search(words):
    os.chdir(path)
    for l in os.walk(path):
        for i in l[2]:
            if os.path.splitext(i)[1] == '.txt':
                line = 0
                file = open(l[0] + '/' + i) # 极其注意文件位置，要不然极容易找不到文件
                for j in file:
                    line += 1
                    count = 0
                    file_location = []
                    if words in j:
                        count += 1
                        num = 0
                        for k in j:
                            num += 1
                            if x[0] == k:
                                if x == j[num - 1 : num - 1 + len(x)]:
                                    file_location.append(num)
                    if count:
                        print('The %ded line %sed word is what you are looking for in the %s/%s'%(line, file_location, l[0], i))
                    
path = input('Please input the path you want to look up')
x = input('Please the keyword you want to look up.')
search(x)


# 本节小结：
OS模块中关于文件/目录常用的函数使用方法
函数名    使用方法
getcwd()    返回当前工作目录
chdir()    改变工作目录
listdir(path='.')    列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）
mkdir(path)    创建单层目录，如果目录已存在抛出异常
makedirs(path)    递归创建多层目录，如果该目录已存在则抛出异常，注意：'E:\a\b'和'E:\a\c'并不会冲突）
remove(path)    删除文件
rmdir(path)    删除单层目录，如果该目录非空则抛出异常
removedirs(path)    递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常
rename(old,new)    将文件old重命名为new
system(command)    运行系统的shell命令
walk(top)    遍历top参数指定路径下的所有子目录，并将结果返回一个三元组（路径，[目录]，[文件]）
以下是支持路径操作中常用到的一些定义，支持所有平台

函数名    使用方法
os.curdir    指代当前目录
os.pardir    指代上一级目录
os.sep    输出操作系统特定的路径分隔符（在Windows下为'\'，Linux下为'/'）
os.linesep    当前平台使用的行终止符（在Windows下为'\r\n'，Linux下为'\n'）
os.name    指代当前使用的操作系统（包括'posix'、'nt'、'mac'、'os2'、'ce'、'java'）

os.path模块中关于路径常用的函数使用办法
函数名    使用方法
basename(path)    去掉目录路径，单独返回文件名
dirname(path)    去掉文件名，单独返回目录路径
join(path1[,path2[,...]])    将path1和path2各部分组合成一个路径名
split(path)    分割文件名和路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在
splitext(path)    分离文件名和扩展名，返回(f_name, f_extension)元组。
getsize(file)    返回指定文件的尺寸，单位是字节
getatime(file)    返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
getctime(file)    返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
getmtime(file)    返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）
以下为函数返回True或False

函数名    使用方法
exists(path)    判断指定路径（目录或文件）是否存在
isabs(path)    判断指定路径是否为绝对路径
isdir(path)    判断指定路径是否存在且是一个目录
isfile(path)    判断指定路径是否存在且是一个文件
islink(path)    判断指定路径是否存在且是一个符号链接
ismount(path)    判断指定路径是否存在且是一个挂载点
samefile(path1,path2)    判断path1和path2两个路径是否指向同一个文件

