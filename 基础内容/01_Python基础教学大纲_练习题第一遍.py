'''
Author: 刘礼宇 1605010842@qq.com
Date: 2025-07-21 04:02:06
LastEditors: 刘礼宇 1605010842@qq.com
LastEditTime: 2025-07-21 23:59:23
FilePath: \Python\基础内容\01_Python基础教学大纲_练习题.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# Python基础教学大纲 第一部分：Python入门 练习题

# 1. Python简介
# 1.1 说出Python的三大主要特点。
print("简洁易读跨平台，丰富的第三方库")

# 1.2 简述Python的常见应用领域。
print("Web开发，数据分析，机器学习，科学计算，爬虫，游戏开发")

# 1.3 查询你当前使用的Python版本，并打印出来。
import sys
print(sys.version)

# 2. Python的安装和环境配置
# 2.1 写出如何在Windows和Linux下安装Python。
# 2.2 如何使用pip安装第三方库？请举例。
print("pin isntall 包名 ")

# 2.3 如何创建和激活虚拟环境？
print("python -m venv 虚拟环境名")
print("venv/Scripts/activate")

# 3. 基本语法和数据类型

 # 3.1 声明一个变量并赋值为你的姓名。
name="liuliyu"
print(name)

# 3.2 声明两个整数变量并相加，打印结果。
a=10;b=20;print(a+b)

# 3.3 声明一个浮点数变量并输出其类型。
c=3.14;print(type(c))

# 3.4 创建一个复数变量并打印其实部和虚部。
d=3+4j;print("实部real:",d.real,"虚部imag:",d.imag)

# 3.5 创建一个字符串变量，输出其长度。
e="hello world, This is fist python program"
print(len(e))

# 3.6 字符串拼接与重复：将两个字符串拼接并重复3次。
f="hello"+"world"*3;print(f)
s1="hello";s2="world";s3=(s1+s2)*3;s4=s1+s2*3;print(s3,s4)
# 3.7 创建一个包含3个元素的列表，并访问第2个元素。
l=[a,2,3.23];print(l)
# 3.8 创建一个元组，尝试修改其元素并观察报错。
t=(1,2,3)
a=1,2,3;print(a)
t=1,2,3
a[0]=100;print(a)

# 3.9 创建一个字典，添加和删除一个键值对。
d={name="liuliyu",age=20,gender="male"};print(d)
d["name1"]="liuliyu1";print(d)
del d["name"];print(d)
d.pop("age");print(d)
# 3.10 创建一个集合，添加和删除元素。
# 3.11 将字符串"123"转换为整数，将整数456转换为字符串。
# 3.12 用type()函数分别输出int、float、str、list、dict、set、tuple的类型。

# 4. 控制流
# 4.1 编写if语句判断一个数是正数、负数还是零。
# 4.2 用for循环打印1到10。
# 4.3 用while循环计算1到100的和。
# 4.4 用break语句提前结束循环。
# 4.5 用continue语句跳过偶数，只打印1到10中的奇数。
# 4.6 用pass语句定义一个空函数。 