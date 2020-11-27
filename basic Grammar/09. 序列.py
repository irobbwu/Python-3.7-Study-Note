# 10.1 作业
# 序列
1）list()：把一个可迭代的对象转换为列表
2）tuple([iterable])：把一个可迭代的对象转化为元组
3）str(obj)：把obj对象转化为字符串
4）max(),min()：返回序列或者参数集合中的最大或最小值
5）sum(iterable[,start=0])：返回序列iterable和可选参数start的总和
6）sorted()：返回排序的列表，默认从小到大
7）reversed()：翻转
8）enumerate()：枚举，生成由每个元素索引值和元素组成的元组
9）zip()：返回各个参数的序列组成的元组

# 1.猜想一下 min() 这个BIF的实现过程：

# 答：
不会

# 参考答案
def min(x):
    least = x[0]
    for each in x:
        if each < least:
            least = each
    return least
print(min('123456789'))


# 2.视频中我们说 sum() 这个BIF有个缺陷，就是如果参数里有字符串类型的话就会报错，请写出一个新的实现过程，自动“无视”参数里的字符串并返回正确的计算结果。

# 答：
number = [1,23,23,23,2,312,3,213,13,'sd']
number2 = str(number)
while number2.isdigit() != True: # number2.isdigit()函数只能在字符串中使用
    for each in number2:
        if each.isdigit() != True:
            number
            number = number2.remove(each)
sum(number)

# 参考答案：
def sum(x):
    result = 0
    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue
    return result
print(sum([1, 2.1, 2.3, 'a', '1', True]))

