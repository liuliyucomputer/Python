# Python基础教学大纲 第一部分：Python入门 练习题答案

# 1. Python简介
# 1.1 说出Python的三大主要特点。
# 答：简洁易读、跨平台、丰富的第三方库。

# 1.2 简述Python的常见应用领域。
# 答：Web开发、数据分析、人工智能、自动化脚本、科学计算、爬虫等。

# 1.3 查询你当前使用的Python版本，并打印出来。
import sys
print(sys.version)

# 2. Python的安装和环境配置
# 2.1 写出如何在Windows和Linux下安装Python。
# 答：
# Windows：官网下载Python安装包，双击安装。
# Linux：sudo apt install python3 或 sudo yum install python3

# 2.2 如何使用pip安装第三方库？请举例。
# 答：pip install 包名  例如：pip install numpy

# 2.3 如何创建和激活虚拟环境？
# 答：
# Windows：python -m venv venv  然后 venv\Scripts\activate
# Linux/macOS：python3 -m venv venv  然后 source venv/bin/activate

# 3. 基本语法和数据类型
# 3.1 声明一个变量并赋值为你的姓名。
name = "张三"

# 3.2 声明两个整数变量并相加，打印结果。
a = 10
b = 20
print(a + b)

# 3.3 声明一个浮点数变量并输出其类型。
f = 3.14
print(type(f))

# 3.4 创建一个复数变量并打印其实部和虚部。
z = 2 + 3j
print(z.real, z.imag)

# 3.5 创建一个字符串变量，输出其长度。
s = "hello world"
print(len(s))

# 3.6 字符串拼接与重复：将两个字符串拼接并重复3次。
s1 = "abc"
s2 = "123"
print((s1 + s2) * 3)

# 3.7 创建一个包含3个元素的列表，并访问第2个元素。
lst = [1, 2, 3]
print(lst[1])

# 3.8 创建一个元组，尝试修改其元素并观察报错。
tpl = (1, 2, 3)
# tpl[0] = 10  # 会报错：'tuple' object does not support item assignment

# 3.9 创建一个字典，添加和删除一个键值对。
d = {"a": 1, "b": 2}
d["c"] = 3
print(d)
d.pop("a")
print(d)

# 3.10 创建一个集合，添加和删除元素。
s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s)

# 3.11 将字符串"123"转换为整数，将整数456转换为字符串。
num = int("123")
str_num = str(456)
print(num, str_num)

# 3.12 用type()函数分别输出int、float、str、list、dict、set、tuple的类型。
print(type(1), type(1.0), type("a"), type([1]), type({"a":1}), type({1,2}), type((1,)))

# 4. 控制流
# 4.1 编写if语句判断一个数是正数、负数还是零。
x = -5
if x > 0:
    print("正数")
elif x < 0:
    print("负数")
else:
    print("零")

# 4.2 用for循环打印1到10。
for i in range(1, 11):
    print(i)

# 4.3 用while循环计算1到100的和。
sum_ = 0
i = 1
while i <= 100:
    sum_ += i
    i += 1
print(sum_)

# 4.4 用break语句提前结束循环。
for i in range(10):
    if i == 5:
        break
    print(i)

# 4.5 用continue语句跳过偶数，只打印1到10中的奇数。
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)

# 4.6 用pass语句定义一个空函数。
def empty_func():
    pass 