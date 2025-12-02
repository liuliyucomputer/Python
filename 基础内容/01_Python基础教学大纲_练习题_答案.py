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
print("1",True and False, True or False, not True) #只有两个都为True才为True，否则为False。这里是False。
#True or False：逻辑或（or），只要有一个为True就为True。这里是True。
# not True：逻辑非（not），True取反就是False。
# 关键字补充：if, elif, else
# if用于条件判断，elif是else if的缩写，else为其他情况
num = 5
if num > 0:
    print('正数')
elif num == 0:
    print('零')
else:
    print('负数')
name = 'Bob'
if name == 'Alice':
    print('Hi, Alice')
elif name == 'Bob':
    print('Hi, Bob')
else:
    print('Who are you?')
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
for j in range(3):
    if j == 0:
        pass  # 占位符，不执行任何操作
    print('for循环:', j)
    if j == 1:
        print()  # 打印空行
    if j == 2:
        print('break')
        break
else: # 注意位置 意义不一样
    print('continue')
    
n = 0
while n < 2:
    print('while循环:', n)
    n += 1
else:
    print('while循环正常结束')

def empty():
    print('空函数pass前')
    pass  # pass什么都不做，常用于占位
    print('空函数pass后')
# 关键字补充：def, return
empty()  # 空函数
# def用于定义函数，return用于返回值
def add(x, y):
    """返回x和y的和"""
    return x + y
print('add函数:', add(2,3))

# 关键字补充：lambda
# lambda用于定义匿名函数，只能写一行表达式
f = lambda x, y: x * y
print('lambda函数:', f(2, 4))
f= lambda x: x**2 
print('lambda函数:', f(3))
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
    print('无论是否异常都会执行finally 一定执行')
# raise用于主动抛出异常
# assert用于断言条件为真，否则抛出AssertionError
# assert 2 > 3, '2不大于3'
def check_age(age):
    # 若年龄为负数，主动抛出ValueError
    if age < 0:
        raise ValueError("年龄不能为负数！请输入有效的年龄值。")
    # 若年龄超过150，主动抛出ValueError
    elif age > 150:
        raise ValueError("年龄过大，不符合常理！")
    else:
        print(f"输入的年龄 {age} 有效。")

# 测试正常情况
try:
    check_age(25)  # 输出：输入的年龄 25 有效。
except ValueError as e:
    print(f"错误：{e}")

# 测试异常情况1：年龄为负数
try:
    check_age(-5)
except ValueError as e:
    print(f"错误：{e}")  # 输出：错误：年龄不能为负数！请输入有效的年龄值。

# 测试异常情况2：年龄过大
try:
    check_age(200)
except ValueError as e:
    print(f"错误：{e}")  # 输出：错误：年龄过大，不符合常理！
# 关键字补充：with
# with用于上下文管理，常用于文件操作
with open('test.txt', 'w', encoding='utf-8') as file:
    file.write('hello')
    
with open('test.txt', 'r', encoding='utf-8') as f:
    f.read()  # 读取文件内容
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
    print('g_var:', g_var)
outer()
print('g_var:', g_var)

# 关键字补充：yield
# yield用于生成器函数，返回一个可迭代对象
def shengchengqi():
    yield 1
    yield 2
    yield 3
for v in shengchengqi():    
    print('yield:', v)
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

# =====================
# 数值类型（int, float, complex, bool）所有操作与组合（每行详细注释）
# =====================

# int（整数）
# 定义：int用于表示整数，支持正负和0，精度无限。
a = 10  # a赋值为10，int类型
b = -5  # b赋值为-5，int类型
c = 0   # c赋值为0，int类型
x = y = z = 1  # 链式赋值，x、y、z都为1
m, n = 2, 3  # 解包赋值，m为2，n为3
m, n = n, m  # 交换变量，m为3，n为2

# 算术运算符：
print('加:', a + b)      # + 加法运算符，两数相加
print('减:', a - b)      # - 减法运算符，两数相减
print('乘:', a * b)      # * 乘法运算符，两数相乘
print('除:', a / 3)      # / 除法运算符，结果为float
print('整除:', a // 3)   # // 整除运算符，取商的整数部分
print('取余:', a % 3)    # % 取余运算符，取余数
print('幂:', a ** 2)     # ** 幂运算符，a的2次方

# 比较运算符：
print('等于:', a == b)   # == 判断两值是否相等
print('不等于:', a != b) # != 判断两值是否不等
print('大于:', a > b)    # > 判断左值是否大于右值
print('小于等于:', a <= b) # <= 判断左值是否小于等于右值

# 位运算符：
print('按位与:', a & 2)  # & 按位与，二进制位都为1则为1
print('按位或:', a | 2)  # | 按位或，二进制位有一个为1则为1
print('按位异或:', a ^ 2) # ^ 按位异或，不同为1
print('左移:', a << 1)   # << 左移，二进制左移一位
print('右移:', a >> 1)   # >> 右移，二进制右移一位
print('按位取反:', ~a)   # ~ 按位取反，所有位取反

# 类型转换：
print('转float:', float(a))  # float() 将int转为float
print('转str:', str(a))      # str() 将int转为str
print('转bool:', bool(a))    # bool() 非零为True，零为False

# int与float混合运算：
print('int+float:', a + 2.5)  # int和float相加，结果为float

# int与bool混合运算：
print('int+bool:', a + True, a + False)  # True视为1，False视为0

# int与complex混合运算：
print('int+complex:', a + (1+2j))  # int和复数相加，结果为complex

# float（浮点数）
f1 = 3.5  # f1赋值为3.5，float类型
f2 = -2.1 # f2赋值为-2.1，float类型
print('float加:', f1 + f2)  # float加法
print('float乘:', f1 * 2)   # float乘法
f3 = 1.23e4  # 科学计数法，等于12300.0
print('科学计数:', f3)
print('0.1+0.2:', 0.1 + 0.2)  # 浮点数精度陷阱
print('float转int:', int(f1))  # float转int，截断小数部分

# complex（复数）
z1 = 1 + 2j  # z1为复数，实部1虚部2
z2 = 2 - 3j  # z2为复数，实部2虚部-3
print('复数加:', z1 + z2)  # 复数加法
print('复数乘:', z1 * z2)  # 复数乘法
print('实部:', z1.real, '虚部:', z1.imag)  # .real/.imag属性
print('复数等于:', z1 == z2)  # 复数只能==和!=
print('复数转str:', str(z1))  # complex转str

# bool（布尔）
bl1 = True   # True布尔真
bl2 = False  # False布尔假
print('bool加:', bl1 + 2)  # True视为1
print('bool与:', bl1 and bl2)  # and逻辑与，两个都为True才为True
print('bool或:', bl1 or bl2)   # or逻辑或，有一个为True就为True
print('bool非:', not bl1)      # not逻辑非，取反
print('bool与float:', bl1 + 1.5)  # True视为1
print('bool与complex:', bl2 + (2+3j))  # False视为0
if bl1:  # if关键字，条件判断
    print('bl1为真')

# =====================
# 基本语法全覆盖（赋值、解包、链式赋值、交换、运算符、推导式等）（每行详细注释）
# =====================

x = 5  # 赋值，将5赋给x
# 链式赋值：
a = b = c = 7  # a、b、c都为7
# 解包赋值：
x, y, z = 1, 2, 3  # x=1, y=2, z=3
# 交换变量值：
x, y = y, x  # 交换x和y的值

# 运算符定义与示例：
# + 加法：a + b
# - 减法：a - b
# * 乘法：a * b
# / 除法：a / b
# // 整除：a // b
# % 取余：a % b
# ** 幂：a ** b
# == 等于：a == b
# != 不等于：a != b
# > 大于：a > b
# < 小于：a < b
# >= 大于等于：a >= b
# <= 小于等于：a <= b
# and 逻辑与：a and b
# or 逻辑或：a or b
# not 逻辑非：not a
# & 按位与：a & b
# | 按位或：a | b
# ^ 按位异或：a ^ b
# ~ 按位取反：~a
# << 左移：a << n
# >> 右移：a >> n
# in 成员运算：x in y
# not in 非成员运算：x not in y
# is 身份运算：a is b
# is not 非身份运算：a is not b

# 推导式：
lst = [i*i for i in range(5)]  # 列表推导式，生成0~4的平方
# for关键字，遍历序列
# in关键字，判断成员关系
# range()内置函数，生成整数序列
# []表示列表
# i*i表达式，计算平方

dct = {i: i*i for i in range(3)}  # 字典推导式，键为i，值为i的平方
# {}表示字典，i: i*i为键值对
st = {i for i in range(3)}  # 集合推导式，生成0~2的集合
# {}表示集合
print('推导式:', lst, dct, st)
gen = (i for i in range(3))  # 生成器推导式，生成0~2的生成器
print('生成器:', gen)  # 打印生成器对象
for v in gen :
    print(v)
# ()表示生成器

print('推导式:', lst, dct, st, list(gen))  # list()将生成器转为列表

# 复合赋值运算符：
a = 2  # 赋值
a += 3  # a = a + 3，+=为加法赋值运算符
print('a+=3:', a)

# 注释：# 单行注释，'''多行注释'''
# 文档字符串：函数、类、模块开头用三引号写说明
def foo():  # def定义函数，foo为函数名
    """这是一个文档字符串，描述函数用途"""
    pass  # pass占位，什么都不做

# 变量命名规则：只能用字母、数字、下划线，不能以数字开头，区分大小写，不能用关键字

# 变量作用域：LEGB规则（Local、Enclosing、Global、Built-in）
# LEGB四个作用域
# L - Local（局部作用域）
# 当前函数内部定义的变量。
# 只在函数内部有效。
# E - Enclosing（嵌套作用域）
# 外层（嵌套）函数的作用域。
# 只在嵌套函数中有效。
# G - Global（全局作用域）
# 当前模块（文件）最外层定义的变量。
# 在整个模块中都有效。
# B - Built-in（内建作用域）
# Python内置的名字，比如len、print、int等。
# global声明全局变量，nonlocal声明外层变量

# 语句结束符：Python每行一条语句，行末不用分号，多个语句可用分号隔开
x = 1; y = 2  # 两条语句用分号隔开

# 输入输出：
# input()获取用户输入，print()输出
# s = input('请输入内容：')  # input函数，获取用户输入
print('输出内容')  # print函数，输出内容 

# =====================
# Python虚拟环境相关指令与详细说明
# =====================

# 虚拟环境（virtual environment）用于为每个项目创建独立的Python包和依赖环境，避免不同项目间的包冲突。
# Python 3.3+内置venv模块，推荐使用。

# 1. 创建虚拟环境
# Windows:
# python -m venv venv  # 用python解释器调用venv模块，在当前目录创建名为venv的虚拟环境文件夹
# Linux/macOS:
# python3 -m venv venv  # 用python3解释器调用venv模块

# 2. 激活虚拟环境
# Windows:
# venv\Scripts\activate  # 运行此脚本激活虚拟环境，命令行前会出现(venv)提示
# Linux/macOS:
# source venv/bin/activate  # 用source命令激活虚拟环境

# 3. 退出虚拟环境
# deactivate  # 任何平台下都可用，退出当前虚拟环境，恢复到全局Python环境

# 4. 删除虚拟环境
# 直接删除虚拟环境文件夹即可（如rm -rf venv或在资源管理器中删除venv文件夹）

# 5. 在虚拟环境中安装包
# pip install 包名  # 在激活的虚拟环境下安装包，只影响当前环境
# pip list  # 查看当前虚拟环境已安装的包
# pip freeze  # 导出当前环境所有包及版本
# pip freeze > requirements.txt  # 保存依赖列表到文件
# pip install -r requirements.txt  # 根据依赖文件批量安装包

# 6. 查看python解释器路径
# which python  # Linux/macOS，显示当前激活环境的python路径
# where python  # Windows，显示当前激活环境的python路径
# python -V 或 python --version  # 查看当前python版本

# 7. 常见注意事项
# - 每个项目建议单独创建虚拟环境，避免包冲突。
# - 激活虚拟环境后，pip、python等命令都只作用于该环境。
# - requirements.txt用于团队协作和环境还原。
# - venv文件夹可自定义名称，但常用venv、.venv、env等。
# - 有些IDE（如PyCharm、VSCode）可自动识别和管理虚拟环境。 