# 高级特性


# 切片


L = ["Michael", "Sarah", "Tracy", "Bob", "Jack"]
# 去前三元素
print(
    L[0:3]
)  # ['Michael', 'Sarah', 'Tracy'] 从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。 如果第一个索引是0，还可以省略：L[:3]
print(L[-2:])  # ['Bob', 'Jack'] 记住倒数第一个元素的索引是-1。

L1 = list(range(100))
# 前10个数，每两个取一个： 间隔一个
# print(L1[:10:2])  #[0, 2, 4, 6, 8]
# 甚至什么都不写，只写[:]就可以原样复制一个list：
# print(L1[:]) #[0,1,2,3,....,99]
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
# print((0, 1, 2, 3, 4, 5)[:3])  #(0, 1, 2)
# print((0, 1, 2, 3, 4, 5)[:5:2])  #(0, 2, 4)  前5个数，每两个取一个： 间隔一个

# 字符串也可以切片
print("ABCDEFG"[:3])  # ABC
print("ABCDEFG"[::2])  # ACEG  每两个取一个 间隔一个取值


def trim(s):  # 去收尾空格
    if not isinstance(s, str):
        raise TypeError("bad operand type")
    if len(s) == 0:
        return s
    while s[-1:] == " ":
        s = s[:-1]
    while s[:1] == " ":
        s = s[1:]
    return s


print(trim(" as  d fg g "))


def trimAll(s):  # 去全部空格
    stt = ""
    if not isinstance(s, str):
        raise TypeError("bad operand type")
    if len(s) == 0:
        return s
    for key in s:
        if (key) != " ":
            stt = stt + key
    return stt


print(trimAll(" as  d fg g "))


# 迭代(遍历)

# dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections.abc import Iterable ,Iterator
print(isinstance("abc", Iterable))  # str是否可迭代
# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(["A", "B", "C"]):
    print(i, value)


def findMinAndMax(L):
    if len(L) == 0:
        print("list为空")
    max = 0
    min = 0
    for key in L:
        while key > max:
            max = key
        while key < min:
            min = key

    return (max, min)


print(findMinAndMax([]))


# 列表生成式  即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。


print([x * x for x in range(1, 11)])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 相当于下面
L2 = []
for x in range(1, 11):
    L2.append(x * x)
print(L2)
# 还可以使用两层循环，可以生成全排列：
print(
    [m + n for m in "ABC" for n in "XYZ"]
)  # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

import os  # 导入os模块，模块的概念后面讲到

print([d for d in os.listdir(".")])  # os.listdir可以列出文件和目录

# for循环其实可以同时使用两个甚至多个变量，比如   dict   的   items()   可以同时迭代  key  和  value  ：
# 列表生成式也可以使用两个变量来生成list：
d = {"x": "A", "y": "B", "z": "C"}
print([key + "=" + v for key, v in d.items()])  # ['x=A', 'y=B', 'z=C']
print([key + v for key, v in enumerate(range(0, 3))])  # [0,1,2] =>[0, 2, 4]

# 最后把一个list中所有的字符串变成小写：
low = ["Hello", "World", "IBM", "Apple"]
print([s.lower() for s in low])  # ['hello', 'world', 'ibm', 'apple']

# if ... else...
print([x for x in range(1, 11) if x % 2 == 0])  # [2, 4, 6, 8, 10]
# for前面的部分是一个表达式，它必须根据x计算出一个结果。因此，考察表达式：x if x % 2 == 0，它无法根据x计算出结果，因为缺少else，必须加上else：
print(
    [x if x % 2 == 0 else -x for x in range(1, 11)]
)  # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
# 可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。

list1 = ["Hello", "World", 18, "Apple", None]
print([key.lower() if isinstance(key, str) else key for key in list1])


# 生成器
# 
#  要创建一个generator，有很多种方法。第一种方法很简单，只要把一个  列表生成式的[]  改成()，就创建了一个generator：
g = (x * x for x in range(10))
print(g)  # <generator object <genexpr> at 0x000002B2DA06B9E0>

# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值： 我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2
# 
for key in g:
    print(key,'g')
# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
def fib(max):
     n, a, b = 0, 0, 1
     while n < max:
         a, b = b, a + b
         n = n + 1
         return 'done'

# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fibg(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
g = fibg(6)
print(g)#<generator object fibg at 0x000001D2CFA6BBA0>
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value) #辅抓return值
        break

def triangles():
    N=[1] #初始化为杨辉三角的每一行为一个list
    while True:
        # print(N)
        yield N         #yield 实现记录功能，没有下一个next将跳出循环，
        S=N[:]        #将list N赋给S，通过S计算每一行
        S.append(0)    #将list添加0，作为最后一个元素，长度增加1
        # print(S,'S')
        N=[S[i-1]+S[i] for i in range(len(S))] #通过S来计算得出N 列表生成式的[]ggit
# N=[S[i-1]+S[i] for i in range(len(S))]
#  设上一个N为[1,1]
#  则S=[1,1,0]
#  通过式子可以得出
#  N=[1,2,1]
k=triangles()
print(next(triangles())) #[1] #你这个是每次都返回一个新的生成器，你需要把生成器赋给一个变量，像k = triangles()，然后每次next(k)这样就会正常了
print(next(triangles())) #[1]
print(next(triangles())) #[1]
print(next(k)) #[1]
print(next(k)) #[1,1]
print(next(k)) #[1,2,1]

# 迭代器
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 一类是集合数据类型，如list [1,2,3,4]、tuple (1,2,3,4)、dict {"a":1,"b":2}、set {1,2,3,4}、str '1111' 等；
# 一类是generator，包括生成器和带yield的generator function。
# 可以使用isinstance()判断一个对象是否是Iterable对象：
print(isinstance([],Iterable)) #True
print(isinstance((),Iterable)) #True
print(isinstance('',Iterable)) #True
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance((x for x in range(10)), Iterator)) #true
print(isinstance([], Iterator)) #False
print(isinstance(iter([]),Iterator)) #True
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。