#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
string模块 - 字符串操作工具

string模块提供了字符串操作的常量和工具函数，是Python中处理字符串的基础模块之一。

主要功能包括：
- 字符串常量（如大小写字母、数字、标点符号等）
- 字符串格式化工具
- 模板字符串
- 字符分类和转换函数

使用场景：
- 字符串生成和验证
- 文本格式化
- 字符编码转换
- 密码生成
- 数据清洗

官方文档：https://docs.python.org/3/library/string.html
"""

import string
import random

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. string模块基本介绍")
print("=" * 50)
print("string模块提供字符串操作的常量和工具函数")
print("包含各种字符串常量和辅助函数")
print("是Python字符串处理的基础模块之一")
print("适用于各种字符串操作场景")

# ===========================
# 2. 字符串常量
# ===========================
print("\n" + "=" * 50)
print("2. 字符串常量")
print("=" * 50)

# 小写字母
print(f"string.ascii_lowercase: {string.ascii_lowercase}")

# 大写字母
print(f"string.ascii_uppercase: {string.ascii_uppercase}")

# 大小写字母
print(f"string.ascii_letters: {string.ascii_letters}")

# 十进制数字
print(f"string.digits: {string.digits}")

# 十六进制数字
print(f"string.hexdigits: {string.hexdigits}")

# 八进制数字
print(f"string.octdigits: {string.octdigits}")

# 标点符号
print(f"string.punctuation: {string.punctuation}")

# 所有可打印字符
print(f"string.printable: {string.printable}")

# 空白字符
print(f"string.whitespace: {repr(string.whitespace)}")

# ===========================
# 3. 字符串格式化
# ===========================
print("\n" + "=" * 50)
print("3. 字符串格式化")
print("=" * 50)

# 使用format方法格式化字符串
name = "Alice"
age = 30
city = "New York"

# 基本格式化
formatted_str = "My name is {}, I'm {} years old, and I live in {}.".format(name, age, city)
print(f"基本格式化: {formatted_str}")

# 位置参数
formatted_str = "My name is {0}, I'm {1} years old, and I live in {2}. {0} is a great name!".format(name, age, city)
print(f"位置参数: {formatted_str}")

# 关键字参数
formatted_str = "My name is {name}, I'm {age} years old, and I live in {city}!".format(name=name, age=age, city=city)
print(f"关键字参数: {formatted_str}")

# 格式规范
pi = 3.14159265359

print(f"\n格式规范:")
print(f"  保留两位小数: {pi:.2f}")
print(f"  保留四位小数: {pi:.4f}")
print(f"  宽度为10，右对齐: {pi:10.2f}")
print(f"  宽度为10，左对齐: {pi:<10.2f}")
print(f"  宽度为10，居中对齐: {pi:^10.2f}")
print(f"  带千位分隔符: {123456789:,.2f}")
print(f"  百分比格式: {0.75:.2%}")
print(f"  科学计数法: {123456789:.2e}")
print(f"  二进制: {42:b}")
print(f"  八进制: {42:o}")
print(f"  十六进制: {42:x}")

# ===========================
# 4. f-strings (Python 3.6+)
# ===========================
print("\n" + "=" * 50)
print("4. f-strings (Python 3.6+)")
print("=" * 50)

# f-strings 基本用法
print(f"My name is {name}, I'm {age} years old, and I live in {city}!")

# f-strings 格式规范
print(f"\nf-strings 格式规范:")
print(f"  保留两位小数: {pi:.2f}")
print(f"  宽度为10，右对齐: {pi:10.2f}")
print(f"  宽度为10，左对齐: {pi:<10.2f}")
print(f"  宽度为10，居中对齐: {pi:^10.2f}")
print(f"  带千位分隔符: {123456789:,.2f}")
print(f"  百分比格式: {0.75:.2%}")

# f-strings 表达式
x = 10
y = 20
print(f"\nf-strings 表达式:")
print(f"  {x} + {y} = {x + y}")
print(f"  {x} * {y} = {x * y}")
print(f"  {name.upper()} has {len(name)} letters")

# ===========================
# 5. string.Template
# ===========================
print("\n" + "=" * 50)
print("5. string.Template")
print("=" * 50)

# 创建模板
template = string.Template("Hello, $name! Welcome to $place.")

# 替换变量
result = template.substitute(name="Alice", place="Python World")
print(f"Template替换: {result}")

# 使用字典替换
data = {"name": "Bob", "place": "Programming Universe"}
result = template.substitute(data)
print(f"Template字典替换: {result}")

# 安全替换（忽略不存在的变量）
template = string.Template("Hello, $name! Welcome to $place. Your score is $score.")
try:
    result = template.substitute(name="Charlie")
    print(f"直接替换: {result}")
except KeyError as e:
    print(f"直接替换出错: {e}")

# 使用safe_substitute
result = template.safe_substitute(name="Charlie")
print(f"安全替换: {result}")

# ===========================
# 6. 字符分类
# ===========================
print("\n" + "=" * 50)
print("6. 字符分类")
print("=" * 50)

# 测试字符类型
test_chars = ['a', 'Z', '5', '@', ' ', '\t']

print("字符分类测试:")
for char in test_chars:
    print(f"  '{char}':")
    print(f"    isalpha(): {char.isalpha()}")
    print(f"    isdigit(): {char.isdigit()}")
    print(f"    isalnum(): {char.isalnum()}")
    print(f"    islower(): {char.islower()}")
    print(f"    isupper(): {char.isupper()}")
    print(f"    isspace(): {char.isspace()}")
    print(f"    isprintable(): {char.isprintable()}")

# ===========================
# 7. 字符串方法
# ===========================
print("\n" + "=" * 50)
print("7. 字符串方法")
print("=" * 50)

# 字符串转换
test_str = "Hello World!"
print(f"原始字符串: {test_str}")
print(f"  upper(): {test_str.upper()}")
print(f"  lower(): {test_str.lower()}")
print(f"  title(): {test_str.title()}")
print(f"  capitalize(): {test_str.capitalize()}")
print(f"  swapcase(): {test_str.swapcase()}")

# 字符串判断
test_str = "Python123"
print(f"\n字符串判断:")
print(f"  startsWith('Py'): {test_str.startswith('Py')}")
print(f"  endsWith('3'): {test_str.endswith('3')}")
print(f"  contains('tho'): {'tho' in test_str}")
print(f"  isalpha(): {test_str.isalpha()}")
print(f"  isalnum(): {test_str.isalnum()}")

# 字符串查找和替换
test_str = "Hello World! Hello Python!"
print(f"\n字符串查找和替换:")
print(f"  find('Hello'): {test_str.find('Hello')}")
print(f"  rfind('Hello'): {test_str.rfind('Hello')}")
print(f"  index('Hello'): {test_str.index('Hello')}")
print(f"  replace('Hello', 'Hi'): {test_str.replace('Hello', 'Hi')}")

# 字符串分割和连接
test_str = "apple,banana,orange"
print(f"\n字符串分割和连接:")
print(f"  split(','): {test_str.split(',')}")

# 字符串连接
fruits = ['apple', 'banana', 'orange']
print(f"  join: {'-'.join(fruits)}")

# 字符串修剪
test_str = "   Hello World!   \t\n"
print(f"\n字符串修剪:")
print(f"  原始: {repr(test_str)}")
print(f"  strip(): {repr(test_str.strip())}")
print(f"  lstrip(): {repr(test_str.lstrip())}")
print(f"  rstrip(): {repr(test_str.rstrip())}")
print(f"  strip(' H!'): {repr(test_str.strip(' H!'))}")

# ===========================
# 8. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("8. 实际应用示例")
print("=" * 50)

# 示例1: 生成随机密码
def generate_password(length=12, include_special=True):
    """生成随机密码"""
    characters = string.ascii_letters + string.digits
    if include_special:
        characters += string.punctuation
    
    # 确保密码包含至少一个小写字母、一个大写字母和一个数字
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    
    # 添加剩余字符
    password += [random.choice(characters) for _ in range(length - 3)]
    
    # 打乱密码顺序
    random.shuffle(password)
    
    return ''.join(password)

print("示例1: 生成随机密码")
print(f"  简单密码: {generate_password(8, include_special=False)}")
print(f"  复杂密码: {generate_password(16)}")
print(f"  超强密码: {generate_password(20)}")

# 示例2: 格式化表格
def format_table(data, headers):
    """格式化表格输出"""
    # 计算每列的最大宽度
    widths = [len(header) for header in headers]
    for row in data:
        for i, col in enumerate(row):
            widths[i] = max(widths[i], len(str(col)))
    
    # 创建分隔线
    separator = "+" + "+" .join("-" * (w + 2) for w in widths) + "+"
    
    # 格式化输出
    result = []
    result.append(separator)
    
    # 输出表头
    header_line = "|"
    for header, width in zip(headers, widths):
        header_line += f" {header:^{width}} |"
    result.append(header_line)
    result.append(separator)
    
    # 输出数据行
    for row in data:
        row_line = "|"
        for col, width in zip(row, widths):
            row_line += f" {str(col):^{width}} |"
        result.append(row_line)
    result.append(separator)
    
    return "\n".join(result)

print("\n示例2: 格式化表格")
data = [
    ("Alice", 30, "New York"),
    ("Bob", 25, "London"),
    ("Charlie", 35, "Paris"),
    ("David", 40, "Tokyo")
]
headers = ("Name", "Age", "City")

print(format_table(data, headers))

# 示例3: 驼峰命名转换
def snake_to_camel(snake_str):
    """将蛇形命名转换为驼峰命名"""
    components = snake_str.split('_')
    # 首字母小写，其余单词首字母大写
    return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(camel_str):
    """将驼峰命名转换为蛇形命名"""
    # 使用正则表达式在大写字母前添加下划线
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str)
    return snake_str.lower()

print("\n示例3: 命名转换")
snake_case = "hello_world_example"
camel_case = "helloWorldExample"

print(f"  蛇形转驼峰: {snake_case} -> {snake_to_camel(snake_case)}")
print(f"  驼峰转蛇形: {camel_case} -> {camel_to_snake(camel_case)}")

# 示例4: 文本对齐
def align_text(text, width=80, align="left"):
    """文本对齐"""
    lines = text.split('\n')
    aligned_lines = []
    
    for line in lines:
        if align == "left":
            aligned = line.ljust(width)
        elif align == "right":
            aligned = line.rjust(width)
        elif align == "center":
            aligned = line.center(width)
        else:
            aligned = line
        aligned_lines.append(aligned)
    
    return '\n'.join(aligned_lines)

print("\n示例4: 文本对齐")
test_text = "Hello\nWorld\nPython"

print("左对齐:")
print(align_text(test_text, 20, "left"))

print("\n右对齐:")
print(align_text(test_text, 20, "right"))

print("\n居中对齐:")
print(align_text(test_text, 20, "center"))

# 示例5: 字符串验证
def validate_password(password):
    """验证密码强度"""
    if len(password) < 8:
        return "密码太短，至少需要8个字符"
    
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    strength = 0
    feedback = []
    
    if has_lower:
        strength += 1
    else:
        feedback.append("需要包含小写字母")
    
    if has_upper:
        strength += 1
    else:
        feedback.append("需要包含大写字母")
    
    if has_digit:
        strength += 1
    else:
        feedback.append("需要包含数字")
    
    if has_special:
        strength += 1
    else:
        feedback.append("需要包含特殊字符")
    
    if strength == 4:
        return "密码强度: 强"
    elif strength == 3:
        return f"密码强度: 中\n建议: {', '.join(feedback)}"
    else:
        return f"密码强度: 弱\n建议: {', '.join(feedback)}"

print("\n示例5: 密码强度验证")
passwords = [
    "password",
    "Password123",
    "Pass@word123",
    "P@ssw0rd!2023"
]

for pwd in passwords:
    print(f"  密码 '{pwd}':")
    print(f"    {validate_password(pwd)}")

# ===========================
# 9. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("9. 最佳实践")
print("=" * 50)

print("1. 字符串拼接")
print("   - 对于少量字符串，使用+运算符简单直观")
print("   - 对于大量字符串，使用join()方法更高效")
print("   - 避免在循环中使用+拼接字符串")

print("\n2. 字符串格式化")
print("   - Python 3.6+ 推荐使用f-strings，简洁易读")
print("   - 对于复杂的格式化需求，使用format()方法")
print("   - 对于用户提供的模板，使用string.Template更安全")

print("\n3. 字符集使用")
print("   - 使用string.ascii_letters代替手动输入大小写字母")
print("   - 使用string.digits代替'0123456789'")
print("   - 使用string.punctuation获取所有标点符号")

print("\n4. 性能考虑")
print("   - 字符串是不可变的，修改操作会创建新字符串")
print("   - 对于频繁修改的字符串，考虑使用list或io.StringIO")
print("   - 预计算字符串长度可以避免重复计算")

print("\n5. 安全性")
print("   - 避免使用eval()处理用户输入的字符串")
print("   - 使用string.Template处理用户提供的模板")
print("   - 对用户输入的字符串进行适当的验证和转义")

# ===========================
# 10. 总结
# ===========================
print("\n" + "=" * 50)
print("10. 总结")
print("=" * 50)
print("string模块是Python字符串处理的基础模块")
print("提供了丰富的字符串常量和工具函数")

print("\n主要功能:")
print("- 各种字符串常量（字母、数字、标点等）")
print("- 多种字符串格式化方法")
print("- 模板字符串支持")
print("- 字符分类和转换功能")

print("\n应用场景:")
print("- 字符串生成和验证")
print("- 文本格式化")
print("- 密码生成")
print("- 数据清洗")
print("- 字符编码转换")

print("\n使用string模块可以提高字符串处理的效率和安全性")
print("是Python编程中不可或缺的基础模块之一")
