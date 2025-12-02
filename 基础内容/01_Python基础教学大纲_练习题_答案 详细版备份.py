# Python基础教学大纲 第一部分：Python入门 练习题答案（关键字与内置模块极致详细版）

# 1. Python简介
# 1.1 说出Python的三大主要特点。
# 答：简洁易读、跨平台、丰富的第三方库。

# 1.2 简述Python的常见应用领域。
# 答：Web开发、数据分析、人工智能、自动化脚本、科学计算、爬虫等。

# 1.3 查询你当前使用的Python版本，并打印出来。
# 关键字详解：
# import：用于导入模块或包，是Python的关键字。可以导入标准库、第三方库或自定义模块。
# sys：是Python的标准库模块，提供与Python解释器和系统相关的功能。
import sys  # 导入sys模块，sys是系统相关的标准库
print(sys.version)  # sys.version属性，获取当前Python解释器的版本信息
# 其他常用sys功能：sys.argv（命令行参数），sys.path（模块搜索路径），sys.exit()（退出程序）
# 关键字补充：from ... import ...
# from用于从模块中导入指定内容，import后面跟要导入的对象名
from math import pi, sqrt  # 从math模块导入pi和sqrt
print('圆周率:', pi, '开根号:', sqrt(16))

# as关键字：用于给导入的模块或对象起别名
import numpy as np  # numpy是第三方科学计算库，np是别名
# print(np.array([1,2,3]))  # 需要安装numpy后才能运行

# 2. Python的安装和环境配置
# 2.1 写出如何在Windows和Linux下安装Python。
# 答：
# Windows：官网下载Python安装包，双击安装。
# Linux：sudo apt install python3 或 sudo yum install python3

# 2.2 如何使用pip安装第三方库？请举例。
# pip是Python的包管理工具，用于安装和管理第三方库。
# pip install 包名  例如：pip install numpy

# 2.3 如何创建和激活虚拟环境？
# venv是Python内置的虚拟环境管理工具。
# Windows：python -m venv venv  然后 venv\Scripts\activate
# Linux/macOS：python3 -m venv venv  然后 source venv/bin/activate

# 3. 基本语法和数据类型
# 3.1 各数据类型的定义、用法、注意点、特例
# int（整数）：用于表示整数，支持任意精度
int_var = 42
print('int类型:', int_var, type(int_var))
# float（浮点数）：用于表示小数，注意精度问题
float_var = 3.1415
print('float类型:', float_var, type(float_var))
# bool（布尔）：只有True和False，常用于条件判断
bool_var = True
print('bool类型:', bool_var, type(bool_var))
# complex（复数）：形如a+bj，a为实部，b为虚部
complex_var = 2 + 3j
print('complex类型:', complex_var, type(complex_var), '实部:', complex_var.real, '虚部:', complex_var.imag)
# str（字符串）：不可变序列，支持切片、拼接、查找等
str_var = "hello,Python!"
print('str类型:', str_var, type(str_var), '长度:', len(str_var), '首字母:', str_var[0])
# list（列表）：有序可变序列，可存放任意类型
list_var = [1, 2.0, "a", True, 2+3j]
print('list类型:', list_var, type(list_var), '第2个元素:', list_var[1])
# tuple（元组）：有序不可变序列，常用于不可变数据
tuple_var = (1, "b", 3.14)
print('tuple类型:', tuple_var, type(tuple_var), '第1个元素:', tuple_var[0])
# set（集合）：无序不重复元素集，常用于去重和集合运算
set_var = {1, 2, 3, 2, 1}
print('set类型:', set_var, type(set_var))
# dict（字典）：键值对集合，键必须不可变且唯一
my_dict = {"name": "张三", "age": 18}
print('dict类型:', my_dict, type(my_dict), 'name:', my_dict["name"])
# NoneType：表示空值或无值
none_var = None
print('NoneType:', none_var, type(none_var))

# 关键字补充：del
# del用于删除变量、列表元素、字典键等
x = 10
del x  # 删除变量x，后续再访问x会报错
lst = [1,2,3]
del lst[1]  # 删除索引为1的元素
print('del后列表:', lst)
d = {'a':1, 'b':2}
del d['a']  # 删除字典的键'a'
print('del后字典:', d)

# 关键字补充：in, not in
# in用于判断元素是否在序列、集合、字典中
print(2 in lst, 'b' in d)
# not in用于判断元素不在容器中
print(5 not in lst)

# 关键字补充：is, is not
# is判断两个对象是否为同一个对象（内存地址是否相同）
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b, a is c, a == c)  # is为True表示同一对象，==为True表示值相等
print(a is not c)

# 关键字补充：and, or, not
# and逻辑与，or逻辑或，not逻辑非
print(True and False, True or False, not True)

# 关键字补充：if, elif, else
# if用于条件判断，elif是else if的缩写，else为其他情况
num = 5
if num > 0:
    print('正数')
elif num == 0:
    print('零')
else:
    print('负数')

# 关键字补充：for, while, break, continue, pass
# for用于遍历可迭代对象，while用于条件循环
for i in range(3):
    if i == 1:
        continue  # 跳过本次循环
    if i == 2:
        break  # 结束循环
    print('for循环:', i)
else:
    print('for循环正常结束')

n = 0
while n < 2:
    print('while循环:', n)
    n += 1
else:
    print('while循环正常结束')

def empty():
    pass  # pass什么都不做，常用于占位

# 关键字补充：def, return
# def用于定义函数，return用于返回值
def add(x, y):
    """返回x和y的和"""
    return x + y
print('add函数:', add(2,3))

# 关键字补充：lambda
# lambda用于定义匿名函数，只能写一行表达式
f = lambda x, y: x * y
print('lambda函数:', f(2, 4))

# 关键字补充：class
# class用于定义类
class Person:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        print('你好，我是', self.name)
p = Person('小明')
p.say_hello()

# 关键字补充：try, except, finally, raise, assert
try:
    1 / 0
except ZeroDivisionError as e:
    print('捕获异常:', e)
finally:
    print('无论是否异常都会执行finally')
# raise用于主动抛出异常
# assert用于断言条件为真，否则抛出AssertionError
# assert 2 > 3, '2不大于3'

# 关键字补充：with
# with用于上下文管理，常用于文件操作
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('hello')
# with会自动关闭文件，无需手动f.close()

# 关键字补充：global, nonlocal
# global声明全局变量，nonlocal声明外层非全局变量
g_var = 1
def outer():
    x = 2
    def inner():
        global g_var
        nonlocal x
        g_var = 3
        x = 4
    inner()
    print('outer.x:', x)
outer()
print('g_var:', g_var)

# 关键字补充：yield
# yield用于生成器函数，返回一个可迭代对象
def gen():
    yield 1
    yield 2
for v in gen():
    print('yield:', v)

# 关键字补充：import, from, as, del, in, is, not, and, or, if, elif, else, for, while, break, continue, pass, def, return, lambda, class, try, except, finally, raise, assert, with, global, nonlocal, yield, True, False, None
# 这些都是Python的保留关键字，不能作为变量名使用。

# 常用内置模块简介：
# sys：系统相关功能
# os：操作系统相关功能，如文件、目录操作
# math：数学运算
# random：随机数
# datetime：日期时间
# re：正则表达式
# json：JSON数据处理
# collections：高级数据结构
# functools：函数式编程工具
# itertools：迭代器工具
# logging：日志
# requests：第三方HTTP库
# numpy、pandas、matplotlib等：数据科学常用库 