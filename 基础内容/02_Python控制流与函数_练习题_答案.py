# Python基础教学大纲 第二部分：控制流与函数 练习题与答案（极致详细版）

# =====================
# 1. 条件语句 if/elif/else
# =====================
# else if = elif
# if语句用于条件判断，elif是else if的缩写，else为其他情况。
# 语法：
# if 条件1:
#     代码块1
# elif 条件2:
#     代码块2
# else:
#     代码块3

x = 10  # 定义变量x为10
if x > 0:  # 判断x是否大于0
    print('x是正数')  # 条件成立时执行
elif x == 0:  # 判断x是否等于0
    print('x是零')
else:  # 以上条件都不成立时执行
    print('x是负数')
a = 1 
if a > 0:
    print('a是正数')
elif a == 0:
    print('a是零')
else: 
    print('a是负数')

# 支持多条件判断
score = 85
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 60:
    print('及格')
else:
    print('不及格')

# if语句可以嵌套
age = 20
if age >= 18:
    if age < 60:
        print('成年人')
    else:
        print('老年人')
else:
    print('未成年人')

# =====================
# 2. 循环语句 for/while/break/continue/pass
# =====================

# for循环用于遍历可迭代对象
for i in range(3):  # range(3)生成0,1,2
    print('for循环:', i)

# while循环用于条件循环
n = 0
while n < 3:
    print('while循环:', n)
    n += 1  # n自增1

# break用于提前结束循环
for i in range(5):
    if i == 3:
        break  # i等于3时跳出循环
    print('break示例:', i)

# continue用于跳过本次循环
for i in range(5):
    if i % 2 == 0:
        continue  # 跳过偶数
    print('continue示例:', i)

# pass用于占位，什么都不做
for i in range(2):
    if i == 0:
        pass  # 占位符
    print('pass示例:', i)
for i in range(2):
    if i == 0:
        pass 
    print('pass示例:', i)
# for...else和while...else结构
for i in range(3):
    if i == 1:
        break
    print('for...else:', i)
else:
    print('for循环正常结束才会执行else')

for i in range(3):
    if i == 1:
        break
    print('1111111111111111111111111111111111111111111111for...else:', i)
else:
    print('for循环正常结束才会执行else')


n = 0
while n < 2:
    print('while...else:', n)
    n += 1
else:
    print('while循环正常结束才会执行else')

# =====================
# 3. 函数定义、参数、返回值、作用域、lambda
# =====================

# def用于定义函数，return用于返回值
# 形参：函数定义时的变量名，实参：调用时传入的值

def add(a, b):  # 定义函数add，接收两个参数a和b
    """返回a和b的和"""
    return a + b  # 返回结果

result = add(3, 5)  # 调用add函数，传入3和5
print('add函数结果:', result)

# 默认参数
def greet(name, msg='你好'):
    print(msg, name)
greet('小明')  # 使用默认参数

# 关键字参数
def info(name, age):
    print(f"姓名:{name}, 年龄:{age}")
info(age=20, name='张三')  # 关键字参数可不按顺序

# 可变参数 *args, **kwargs
# *args接收任意数量的位置参数，类型为元组
def show_args(*args):
    print('args:', args)
show_args(1, 2, 3)
# **kwargs接收任意数量的关键字参数，类型为字典
def show_kwargs(**kwargs):
    print('kwargs:', kwargs)
show_kwargs(a=1, b=2)

# 作用域与global/nonlocal
x = 1  # 全局变量
def outer():
    x = 2  # 外层变量
    def inner():
        nonlocal x  # 声明使用外层变量x
        x = 3
    inner()
    print('outer.x:', x)
outer()
print('全局x:', x)

y = 1
def change_global():
    global y  # 声明使用全局变量y
    y = 100
change_global()
print('全局y:', y)

# lambda匿名函数
f = lambda x, y: x + y  # 定义匿名函数，返回x+y
print('lambda结果:', f(2, 3))

# map/filter/reduce/zip/enumerate
lst = [1, 2, 3, 4]
print('map:', list(map(lambda x: x*2, lst)))  # map对每个元素乘2
print('filter:', list(filter(lambda x: x%2==0, lst)))  # filter筛选偶数
from functools import reduce
print('reduce:', reduce(lambda x, y: x+y, lst))  # reduce累加
print('zip:', list(zip(['a','b'], [1,2])))  # zip打包
print('enumerate:', list(enumerate(['a','b','c'])))  # enumerate带索引

# 文档字符串和注释
# 单行注释用#，多行注释用三引号'''
# 函数、类、模块开头可用三引号写文档字符串

def example():
    '''这是一个文档字符串，描述example函数用途'''
    pass

# 变量命名、缩进、语句结束符、输入输出等规则同上章节 