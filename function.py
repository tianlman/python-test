# Python内置了很多有用的函数，我们可以直接调用。
# 调用函数
# 绝对值的函数abs() max()
print(abs(-100))  # 100
# 数据类型转换
# int()函数可以把其他数据类型转换为整数：
# print('1'+1) #报错
print(int("1") + 1)  # 2
print(int(12.34))  # 12
print(float("12.34") + 0.1)  # 12.44
print(str(1.23))  # '1.23'
print(bool(1))  # True
print(bool(""))  # Fasle
print(hex(255))  # 0xff  hex()函数把一个整数转换成十六进制表示的字符串
print(hex(1000))
print(hex(255), "\n", hex(1000))
# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# list.pop(obj=list[-1])       //默认为 index=-1，删除最后一个列表值。
sentence=['All', 'good', 'things', 'come', 'to' ,'those', 'who', 'wait.']
print("默认为 index=-1，删除最后一个列表值：",sentence.pop(-1),"\n")
print("默认删除最后一个列表值： ",sentence.pop(),"\n")
print("删除第一个元素：",sentence.pop(0),"\n")
print("删除第三个元素：",sentence.pop(2),"\n")
print("输出剩余元素：",sentence)
# 定义函数
from unit import bubble_sort

print(bubble_sort([3, 2, 5, 9, 8, 6, 7]))
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print(move(100, 100, 60, math.pi / 6))
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0
#  +bx+c=0 的两个解。
# 提示：
# 一元二次方程的求根公式为：
# 计算平方根可以调用math.sqrt()函数：
# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。

# isinstance() 与 type() 区别：

# type() 不会认为子类是一种父类类型，不考虑继承关系。

# isinstance() 会认为子类是一种父类类型，考虑继承关系。

# 如果要判断两个类型是否相同推荐使用 isinstance()。
# : 一元二次方程 ax^2 + bx + c = 0 有两个正实根的充要条件是 (1)b^2 - 4ac ≥ 0 (2)ab < 0 (3)ac > 0 三个条件同时满足。
def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(
        b, (int, float) or not isinstance(c, (int, float))
    ):
        raise TypeError("bad operand type")
    mark = b ** 2 - 4 * a * c
    # mark1= a * b
    # mark2 =a * c
    if mark < 0:
        print("方程无实根")
        return
    else:
        x1 = (-1 * b + math.sqrt(mark)) / (2 * a)
        x2 = (-1 * b - math.sqrt(mark)) / (2 * a)
        return x1, x2


print(quadratic(0.5, 2, 0.5))


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(2))
print(power(2, 3))

# 函数的参数改为可变参数：定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2))  # 5
print(calc())  # 0

# 关键字参数 函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
def person(name, age, **kw):
    print(kw)
    print("name:", name, "age:", age, "other:", kw)


extra = {"city": "Beijing", "job": "Engineer"}
person("Jack", 24, city=extra["city"], job=extra["job"])
person("Jack", 24, city=extra["city"])
person(
    "Jack", 24, **extra
)  # **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。 
def person1(name, age, *, city, job):
    print(name, age, city, job)
person1('Jack', 24, city='Beijing', job='Engineer')
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)
person2('Jack', 24,(1,2,3),  job='Engineer',city='Beijing',) #Jack 24 ([1, 2, 3],) Beijing Engineer
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

# 参数组合
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw,'参数组合1')

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw,'参数组合2')

# tuple和dict
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

f1(*args, **kw)
args = (1, 2, 3)

f2(*args, **kw)

for key in (1,2,3,4,5):
     print(key)
    

# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
def product(*args):
    print(args,'args')
    if len(args)==0:
         raise TypeError('At least one real number is needed')
    sum = 1
    for key in  list(args):
        print(key)
        if not isinstance(key,(int,float)):
            raise TypeError('Bad operand type')
        sum = sum *key
    return sum    
print(product(*(1,2,3,4,5,6,7,8,9)))
# 参数总结：
""" Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。 """

# 递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
# 使用递归函数需要注意防止栈溢出。
# 解决递归调用栈溢出的方法是通过尾递归优化，
""" 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中 """
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact_iter(5,1))

def moveABC(n,a,b,c):
#此函数作用是把n个盘子从a移到c n-1看做整体  
    if n==1:  #如果只有一个盘子，直接移动即可
        print('.............')
        print(a,'-->',c)
    else:   #如果有多个盘子 把 n-1个从a到b a上最后一个最大的 a到c 然后是剩下n-1从b-c
        moveABC(n-1,a,c,b)     #先把n-1个盘子从a移到b
        print(a,'-->',c)       #再把最后一个盘子从a移到c
        moveABC(n-1,b,a,c)     #最后把n-1个盘子从b移到c
moveABC(3,'a','b','c')