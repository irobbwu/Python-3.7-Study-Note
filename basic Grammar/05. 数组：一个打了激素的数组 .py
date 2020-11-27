# 9.29 作业
# 一个打了激素的数组（1）

# 函数符：                                                                    增加数组元素：                                               append（）member.append(x) 增加单个元素x置于数组member最后方               insert（）member.insert(x,#)在第数组member的x个位置增加元素#                entend([]) member.extend([])增加组于member中
# 删除数组元素：                                           remove（）member.remove(x)删除单个元素x在member数组中                           del（） del member[x] 删除数组member的第x个元素                                     pop()  member.pop() 删除member中的最后一个元素，括号内可赋数组元素位置

# 一、利用 for 循环打印上边 member 列表中的每个内容，如图：
# member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

# 答：
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for each in member:
    print(each)

# 参考答案
# 二、上一题打印的样式不是很好，能不能修改一下代码打印成下图的样式呢？
# 小甲鱼 88
# 黑夜 90
# 迷途 85
# 怡静 90
# 秋舞斜阳 88

# 答：不会

# 参考答案（1）：
count = 0
length = len(member)
while count < length:
    print(member[count], member[count+1]) # print（member[2]）表示输出数组中位置为2的元素

# 参考答案（2）：
for each in range(len(member)):
    if each%2 == 0:
        print(member[each], member[each+1])

# 一个打了激素的数组（2）
# 列表分片（slice）
# member[1:3]：原列表member中索引值1~3的元素组成新的列表
# member[1:]：索引值从1开始到最后一个元素
# member[:]：原列表所有元素，特别的member2 = member[:]完成列表的拷贝
# member[0:9:2]：索引从2开始到索引8，跨步2取数
# member[::-1]：完成原列表的反转

# 一个打了激素的数组（3）
# 1. 请问如何将下边这个列表的'小甲鱼'修改为'小鱿鱼'？

# 答：
list1[1[2]] = ['小鱿鱼'] # 错误

# 参考答案：
list1[1][2][0] = '小鱿鱼'

# 2. 请先在 IDLE 中获得下边列表的结果，并按照上方例子把列表推导式还原出来。
list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!=0]

# 答：
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                print('(',x, y,')') # 未加入数组
# 修改
list1 = []
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                list1.extend([(x, y)])
print(list1)

# 参考答案
 for x in range(10):
    for y in range(10):
        if x % 2 == 0:
            if y % 2 != 0:
                list1.append((x, y))

# 活学活用：请使用列表推导式补充被小甲鱼不小心涂掉的部分
list1 = ['1.Jost do It','2.一切皆有可能','3.让变成改变世界','4.Impossible is nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3 = [XXXXXXXXX]
print(list3)
for each in list3:
    print(each)

# 1.耐克：Jost do It
# 2.李宁：一切皆有可能
# 3.鱼C工作室：让变成改变世界
# 4.阿迪达斯：Impossible is nothing

# 答：
list1 = ['1.Jost do It','2.一切皆有可能','3.让变成改变世界','4.Impossible is nothing']
list2 = ['4.阿迪达斯','2.李宁','3.鱼C工作室','1.耐克']
list3 = [name + ': ' + slogan[2:] for name in list2 for slogan in list1 if slogan[0] == name[0]]
for each in list3:
    print(each)

# 参考答案
list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]

列表的常用操作符：
比较：如果有多个元素，默认从第一个元素开始比较，比较对应的ASCII码值大小；
逻辑（and or）：
连接（+）：[1, 2, 3] + [4, 5, 6] 结果是 [1, 2, 3, 4, 5, 6]
重复（*）：['Hi!'] * 4 结果是 ['Hi!', 'Hi!', 'Hi!', 'Hi!']
成员关系（in 和 not in）：3 in [1, 2, 3] 结果是 True

列表的方法：dir(list)
append()：在列表末尾添加新的对象
extend()：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
count()：统计出现的次数
index(目标，起始位置，截止位置)：返回参数在列表中的位置
insert()：将对象插入到列表指定位置
pop()：移除列表中的一个元素（默认最后一个元素，可指定其他的位置），并且返回该元素的值
remove()：移除列表中某个值的第一个匹配项（不能指定位置删除）
reverse()：翻转列表
sort()：按照指定的方式对列表成员排序，默认则从小到大排列
特别的：sort(reverse=True)表示从大到小，默认为False

列表的内置函数：
比较两个列表的元素：operator.eq(list1,list2）（前提需import operator）
计算列表元素个数：len(list1)
返回列表中元素最大值：max(list1)
返回列表中元素最小值：min(list1)
将元组转换为列表：list(tuple1) #Python的元组与列表类似，不同之处在于元组的元素不能修改。  元组使用小括号，列表使用方括号。    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。                      tup1 = ('physics', 'chemistry', 1997, 2000)                         tup2 = (1, 2, 3, 4, 5 ）                                             tup3 = "a", "b", "c", "d"

