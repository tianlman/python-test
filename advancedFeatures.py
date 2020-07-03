# 高级特性


# 切片 


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 去前三元素
print(L[0:3]) #['Michael', 'Sarah', 'Tracy'] 从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。 如果第一个索引是0，还可以省略：L[:3]
print(L[-2:]) #['Bob', 'Jack'] 记住倒数第一个元素的索引是-1。

L1 = list(range(100))
# 前10个数，每两个取一个： 间隔一个
# print(L1[:10:2])  #[0, 2, 4, 6, 8]
# 甚至什么都不写，只写[:]就可以原样复制一个list：
# print(L1[:]) #[0,1,2,3,....,99]
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
# print((0, 1, 2, 3, 4, 5)[:3])  #(0, 1, 2)
# print((0, 1, 2, 3, 4, 5)[:5:2])  #(0, 2, 4)  前5个数，每两个取一个： 间隔一个

# 字符串也可以切片
print('ABCDEFG'[:3]) #ABC
print('ABCDEFG'[::2]) #ACEG  每两个取一个 间隔一个取值
def trim(s): #去收尾空格
    if not isinstance(s,str):
        raise TypeError('bad operand type')
    if len(s) == 0:
        return s
    while s[-1:]==' ':
        s=s[:-1]
    while s[:1]==' ':
        s=s[1:]
    return s
print(trim(' as  d fg g '))

def trimAll(s): #去全部空格
    stt=''
    if not isinstance(s,str):
        raise TypeError('bad operand type')
    if len(s) == 0:
        return s
    for key in s:
        if(key) !=' ':
            stt = stt+key
    return stt
print(trimAll(' as  d fg g '))


# 迭代(遍历)
            
# dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections.abc import Iterable

print(isinstance('abc', Iterable)) # str是否可迭代
# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)

def findMinAndMax(L):
    if len(L) ==0:
        print('list为空')
    max = 0
    min = 0
    for key in L:
        while key>max:
            max = key
        while key<min:
            min = key
    
    return (max,min)

print(findMinAndMax([]))
        
