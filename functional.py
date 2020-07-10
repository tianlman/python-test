# 函数式编程

# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def f(a):
    return a+2
def add(x, y, f):
    return f(x) + f(y)
print(add(1,2,f))