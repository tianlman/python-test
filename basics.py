


# list列表  range(2)生成1,2整数 
# 第一天一分钱 ，第二天两分钱， 第三天4分钱  ....一次下去n天一共要给多少块
L = int(input("天数："))
sum = 0
for key in list(range(L)): #for 循环 
    sum = sum + 2 ** key
total = sum / 100
print("%s 天的总和为：%.3f %s" % (L, total, "块"))
# print(list(range(L)))

# while 循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue   # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
m=1
while m <= 100:
    if m > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(m)
    m = m + 1


# tuple 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
t = ("a", "b", ["A", "B"])
# t[0] = '1'#报错
t[2][0] = "X" #tuple不可修改但是list可以修改
t[2][1] = "Y"
print(t,'tuple') 


# if  elif else
height = 1.75
weight = 80.5
bmi = weight /height**2
print('%.2f ' % bmi)
if bmi <18.5:
    print('过轻')
elif 18.5<bmi <25:
    print('正常')
elif 25<bmi <28:
    print('过重')
elif 28<bmi <32:
    print('严重肥胖')
else:
    print('严重肥胖')

# dict dict的key必须是不可变对象
d = {"Michael": 95, "Bob": 75, "Tracy": 85}
# 判断key是否存在方法 d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# 1、 'key' in d 返回True 或者False
# 2、 d.get(key)  key不存在返回None  或者指定value   d.get('Thomas', -1)  返回指定值
print(d.get("Bob"), d.get("11"))  # 75 None
print(d.get("Michael1", 7))  # 返回7
print(d["Michael"])  # key不存在时候报错
print(d)  # {'Michael': 95, 'Bob': 75, 'Tracy': 85}

# set 无序和无重复元素的集合 两个set可以做数学意义上的交集、并集等操作：  set和dict的唯一区别仅在于没有存储对应的value
#   set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合：
# add() # 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：  remove() 删除
s = set([1, 2, 3, 3, 4, 5])  # 重复元素在set中自动被过滤：
print(s)  # {1, 2, 3, 4, 5}
s.add(9)
print(s)  # {1, 2, 3, 4, 5,9}
s.remove(1)
print(s)  # {2, 3, 4, 5,9}
s1 = set([1, 2, 8, 9, 10])
print(s & s1)  # {9, 2}交集
print(s | s1)  # {1, 2, 3, 4, 5, 8, 9, 10}并集

