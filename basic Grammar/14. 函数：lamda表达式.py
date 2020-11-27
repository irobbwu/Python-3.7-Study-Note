# 10.9 作业
# 函数：lambda表达式

# 1. 用filter()函数和lambda表达式快速求出100以内所有3的倍数？

# 答：
filter(lambda x: x if x % 3 == 0;range(100)) # 报错，如果用if函数需要用else None 或者 else Flase

# 参考答案：
a = list(filter(lambda x:x%3 == 0,range(1,100)))
print(a)

b = list(filter(lambda x:not(x%3),range(1,100)))
print(b)

c = list(filter(lambda x:x if x%3==0 else None,range(100)))
print(c)

# 2.>>> list(zip([1,3,5,7,9],[2,4,6,8,10]))                                >>> [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]    但如果我希望打包的形式是灵活多变的列表而不是元祖（希望是[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]这种形式），你能做到吗？（采用map和lambda的表达式）

# 答：
x = [1,3,5,7,9]
y = [2,4,6,8,10]
list(map(lambda i: [x[i],y[i]],range(min(len(x), len(y)))))

# 参考答案：
list(map(lambda x,y : [x,y],[1,3,5,7,9],[2,4,6,8,10]))

# 本节内容
lambda表达式的作用：
1）Python写一些执行脚本时，使用lambda就可以省下定义函数的过程，比如说我们只是需要写一个简单的脚本来管理服务器时间，我们就不需要专门定义一个函数然后再写调用，使用lambda就可以使得代码更加精简。
2）对于一些比较抽象并且整个程序执行下来只需要调用一两次的函数，有时候我们个函数起个名字也是比较头疼的问题，使用lambda就不需要考虑命名问题。
3）简化代码的可读性，由于普通的函数阅读经常要跳到开头def定义部分，使用lambda函数可以省去这样的步骤。

2、两个重要的BIF
1）filter(function or None,iterable)：两个参数为函数和可迭代的序列，函数定义了过滤的规则，默认过滤出真的部分。
2）map(function or None,iterable)：同filter()的两个参数相同，这个内置函数的作用是：将序列的每一个元素作为函数的参数进行运算加工，直到可迭代序列的每个元素都加工完毕，返回所有加工后的元素构成的新序列。


