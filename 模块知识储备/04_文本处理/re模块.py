#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
re模块 - 正则表达式操作

re模块提供了正则表达式匹配操作，是Python中处理文本的强大工具。

主要功能包括：
- 正则表达式匹配
- 字符串搜索和替换
- 分组和捕获
- 编译正则表达式以提高性能
- 多种匹配模式（忽略大小写、多行模式等）

使用场景：
- 文本提取和验证
- 数据清洗和转换
- 日志分析
- 网页爬虫
- 配置文件解析

官方文档：https://docs.python.org/3/library/re.html
"""

import re

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. re模块基本介绍")
print("=" * 50)
print("re模块用于正则表达式匹配操作")
print("提供了强大的文本处理功能")
print("支持复杂的模式匹配和替换")
print("适用于各种文本处理场景")

# ===========================
# 2. 基本用法
# ===========================
print("\n" + "=" * 50)
print("2. 基本用法")
print("=" * 50)

# 简单匹配
test_str = "Hello, Python!"
match = re.search(r"Python", test_str)
if match:
    print(f"匹配成功: '{match.group()}'")
    print(f"匹配位置: {match.start()} - {match.end()}")

# 编译正则表达式
pattern = re.compile(r"\d+")  # 匹配一个或多个数字
test_str = "There are 123 apples and 456 oranges."

# 查找所有匹配
matches = pattern.findall(test_str)
print(f"\n查找所有数字: {matches}")

# 替换匹配
new_str = pattern.sub("NUM", test_str)
print(f"替换后的字符串: {new_str}")

# ===========================
# 3. 正则表达式模式语法
# ===========================
print("\n" + "=" * 50)
print("3. 正则表达式模式语法")
print("=" * 50)

# 字符类
print("字符类:")
print(f"  r'[aeiou]'匹配元音字母: {re.findall(r'[aeiou]', 'Hello World')}")
print(f"  r'[^0-9]'匹配非数字: {re.findall(r'[^0-9]', 'abc123def456')}")
print(f"  r'[a-zA-Z]'匹配字母: {re.findall(r'[a-zA-Z]', 'a1b2c3D4E5F6')}")

# 预定义字符类
print("\n预定义字符类:")
print(f"  r'\d'匹配数字: {re.findall(r'\d', 'abc123def456')}")
print(f"  r'\D'匹配非数字: {re.findall(r'\D', 'abc123def456')}")
print(f"  r'\s'匹配空白字符: {re.findall(r'\s', 'Hello\tWorld\n')}")
print(f"  r'\S'匹配非空白字符: {re.findall(r'\S', 'Hello\tWorld\n')}")
print(f"  r'\w'匹配字母数字下划线: {re.findall(r'\w', 'Hello_World!123')}")
print(f"  r'\W'匹配非字母数字下划线: {re.findall(r'\W', 'Hello_World!123')}")

# 重复
print("\n重复:")
print(f"  r'a*'匹配0次或多次a: {re.findall(r'a*', 'aaabbb')}")
print(f"  r'a+'匹配1次或多次a: {re.findall(r'a+', 'aaabbb')}")
print(f"  r'a?'匹配0次或1次a: {re.findall(r'a?', 'aaabbb')}")
print(f"  r'a{{2}}'匹配2次a: {re.findall(r'a{{2}}', 'aaabbb')}")
print(f"  r'a{{2,4}}'匹配2-4次a: {re.findall(r'a{{2,4}}', 'aaaaabbb')}")
print(f"  r'a{{2,}}'匹配至少2次a: {re.findall(r'a{{2,}}', 'aaaaabbb')}")

# 边界匹配
print("\n边界匹配:")
print(f"  r'^Hello'匹配以Hello开头: {re.findall(r'^Hello', 'Hello World')}")
print(f"  r'World$'匹配以World结尾: {re.findall(r'World$', 'Hello World')}")
print(f"  r'\bHello\b'匹配单词Hello: {re.findall(r'\bHello\b', 'Hello, HelloWorld!')}")

# ===========================
# 4. 常用函数
# ===========================
print("\n" + "=" * 50)
print("4. 常用函数")
print("=" * 50)

# re.search - 搜索第一个匹配
print("re.search:")
result = re.search(r"\d+", "There are 123 apples")
if result:
    print(f"  找到匹配: {result.group()} at {result.span()}")

# re.match - 从字符串开头匹配
print("\nre.match:")
result = re.match(r"Hello", "Hello World")
if result:
    print(f"  开头匹配: {result.group()}")

result = re.match(r"World", "Hello World")
if not result:
    print(f"  开头不匹配: None")

# re.findall - 查找所有匹配
print("\nre.findall:")
results = re.findall(r"\b\w+\b", "Hello, World!")
print(f"  所有单词: {results}")

# re.finditer - 查找所有匹配并返回迭代器
print("\nre.finditer:")
for match in re.finditer(r"\d+", "123 apples and 456 oranges"):
    print(f"  匹配: {match.group()} at {match.span()}")

# re.sub - 替换匹配
print("\nre.sub:")
new_str = re.sub(r"\d+", "[NUMBER]", "123 apples and 456 oranges")
print(f"  替换前: 123 apples and 456 oranges")
print(f"  替换后: {new_str}")

# re.subn - 替换匹配并返回替换次数
print("\nre.subn:")
new_str, count = re.subn(r"\d+", "[NUMBER]", "123 apples and 456 oranges")
print(f"  替换后: {new_str}")
print(f"  替换次数: {count}")

# re.split - 分割字符串
print("\nre.split:")
split_result = re.split(r"\W+", "Hello, World! How are you?")
print(f"  分割结果: {split_result}")

# ===========================
# 5. 分组和捕获
# ===========================
print("\n" + "=" * 50)
print("5. 分组和捕获")
print("=" * 50)

# 基本分组
test_str = "2023-12-25"
pattern = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
match = pattern.search(test_str)

if match:
    print(f"  完整匹配: {match.group()}")
    print(f"  第1组: {match.group(1)} (年)")
    print(f"  第2组: {match.group(2)} (月)")
    print(f"  第3组: {match.group(3)} (日)")
    print(f"  所有分组: {match.groups()}")

# 命名分组
test_str = "John Doe <john.doe@example.com>"
pattern = re.compile(r"(?P<name>\w+\s\w+)\s<(?P<email>[^>]+)>")
match = pattern.search(test_str)

if match:
    print(f"\n  姓名: {match.group('name')}")
    print(f"  邮箱: {match.group('email')}")
    print(f"  所有命名分组: {match.groupdict()}")

# 非捕获分组
test_str = "applepie or appletart"
pattern = re.compile(r"apple(?:pie|tart)")
matches = pattern.findall(test_str)
print(f"\n  非捕获分组匹配: {matches}")

# ===========================
# 6. 编译正则表达式
# ===========================
print("\n" + "=" * 50)
print("6. 编译正则表达式")
print("=" * 50)

# 编译正则表达式
pattern = re.compile(r"\d+")

# 使用编译后的正则表达式
test_str = "123 apples and 456 oranges"

print(f"  查找所有: {pattern.findall(test_str)}")
print(f"  搜索: {pattern.search(test_str).group()}")
print(f"  替换: {pattern.sub('[NUM]', test_str)}")

# 编译标志
print("\n  编译标志:")

# IGNORECASE - 忽略大小写
pattern = re.compile(r"hello", re.IGNORECASE)
print(f"  IGNORECASE: {pattern.findall('Hello HELLO hello')}")

# MULTILINE - 多行模式
pattern = re.compile(r"^hello", re.MULTILINE)
print(f"  MULTILINE: {pattern.findall('hello\nworld\nhello')}")

# DOTALL - 点匹配所有字符（包括换行符）
pattern = re.compile(r"a.b", re.DOTALL)
print(f"  DOTALL: {pattern.findall('a\nb\naXb')}")

# VERBOSE - 详细模式，忽略空格和注释
pattern = re.compile(r"""
    \d{4}  # 年
    -      # 分隔符
    \d{2}  # 月
    -      # 分隔符
    \d{2}  # 日
""", re.VERBOSE)
print(f"  VERBOSE: {pattern.findall('2023-12-25')}")

# ===========================
# 7. 高级特性
# ===========================
print("\n" + "=" * 50)
print("7. 高级特性")
print("=" * 50)

# 贪婪匹配 vs 非贪婪匹配
print("贪婪匹配 vs 非贪婪匹配:")
test_str = "<div>content1</div><div>content2</div>"

# 贪婪匹配
pattern_greedy = re.compile(r"<div>(.*)</div>")
print(f"  贪婪匹配: {pattern_greedy.findall(test_str)}")

# 非贪婪匹配（在重复量词后加?）
pattern_non_greedy = re.compile(r"<div>(.*?)</div>")
print(f"  非贪婪匹配: {pattern_non_greedy.findall(test_str)}")

# 反向引用
print("\n反向引用:")
test_str = "abcabc"
pattern = re.compile(r"(abc)\1")  # 匹配连续的abcabc
print(f"  反向引用匹配: {pattern.findall(test_str)}")

# 零宽断言
print("\n零宽断言:")
test_str = "apple pie, banana cake, cherry tart"

# 正向先行断言
pattern = re.compile(r"\w+(?= pie)")  # 匹配pie前面的单词
print(f"  正向先行断言: {pattern.findall(test_str)}")

# 负向先行断言
pattern = re.compile(r"\w+(?! pie)")  # 匹配不是pie前面的单词
print(f"  负向先行断言: {pattern.findall(test_str)}")

# 正向后行断言
pattern = re.compile(r"(?<=apple )\w+")  # 匹配apple后面的单词
print(f"  正向后行断言: {pattern.findall(test_str)}")

# 负向后行断言
pattern = re.compile(r"(?<!apple )\w+")  # 匹配不是apple后面的单词
print(f"  负向后行断言: {pattern.findall(test_str)}")

# ===========================
# 8. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("8. 实际应用示例")
print("=" * 50)

# 示例1: 验证邮箱地址
def validate_email(email):
    """验证邮箱地址格式"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

print("示例1: 验证邮箱地址")
email_list = [
    "user@example.com",
    "user.name@example.co.uk",
    "user+tag@example.com",
    "invalid-email",
    "@example.com",
    "user@.com"
]

for email in email_list:
    if validate_email(email):
        print(f"  ✅ {email} - 有效")
    else:
        print(f"  ❌ {email} - 无效")

# 示例2: 提取URL
def extract_urls(text):
    """从文本中提取URL"""
    pattern = r"https?://[\w\-.~:/?#[\]@!$&'()*+,;=%]+"
    return re.findall(pattern, text)

print("\n示例2: 提取URL")
test_text = "访问 https://www.example.com 或 http://test.org/page?id=123 查看更多信息"
urls = extract_urls(test_text)
print(f"  提取的URL: {urls}")

# 示例3: 数据清洗
def clean_data(text):
    """清洗文本数据"""
    # 移除多余空格
    text = re.sub(r"\s+", " ", text)
    # 移除特殊字符（保留字母、数字、空格和常见标点）
    text = re.sub(r"[^\w\s.,!?]", "", text)
    # 统一为小写
    text = text.lower()
    return text.strip()

print("\n示例3: 数据清洗")
dirty_text = "  HeLLo!@#$%^&*() World 123   \t\n"
cleaned_text = clean_data(dirty_text)
print(f"  清洗前: '{dirty_text}'")
print(f"  清洗后: '{cleaned_text}'")

# 示例4: 解析日志
print("\n示例4: 解析日志")
log_entry = "2023-12-25 14:30:45 INFO [main] User 'admin' logged in from 192.168.1.1"

# 解析日志的正则表达式
log_pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) \[(\w+)\] (.+)"

match = re.match(log_pattern, log_entry)
if match:
    print(f"  时间: {match.group(1)}")
    print(f"  级别: {match.group(2)}")
    print(f"  线程: {match.group(3)}")
    print(f"  消息: {match.group(4)}")

# 示例5: 替换HTML标签
def strip_html(html):
    """移除HTML标签"""
    # 移除脚本标签
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    # 移除其他HTML标签
    html = re.sub(r"<[^>]+>", "", html)
    # 移除多余空格
    html = re.sub(r"\s+", " ", html)
    return html.strip()

print("\n示例5: 替换HTML标签")
html_text = "<div class='content'><h1>标题</h1><p>内容</p></div>"
plain_text = strip_html(html_text)
print(f"  HTML: {html_text}")
print(f"  纯文本: {plain_text}")

# ===========================
# 9. 性能优化
# ===========================
print("\n" + "=" * 50)
print("9. 性能优化")
print("=" * 50)

print("1. 编译正则表达式")
print("   - 对于频繁使用的正则表达式，编译后可以提高性能")
print("   - 编译后的正则表达式对象可以重复使用")

print("\n2. 避免回溯")
print("   - 尽量使用确定的模式，避免模糊匹配")
print("   - 使用非贪婪匹配时要小心")
print("   - 考虑使用原子分组 (?>...) 避免回溯")

print("\n3. 限制匹配范围")
print("   - 使用^和$限制匹配范围")
print("   - 使用\b限制单词边界")

print("\n4. 使用合适的函数")
print("   - 使用re.match()代替re.search()，如果知道从开头匹配")
print("   - 使用re.finditer()代替re.findall()，如果处理大量匹配")

# ===========================
# 10. 总结
# ===========================
print("\n" + "=" * 50)
print("10. 总结")
print("=" * 50)
print("re模块是Python中处理文本的强大工具")
print("提供了丰富的正则表达式匹配功能")

print("\n主要功能:")
print("- 正则表达式匹配和搜索")
print("- 字符串替换和分割")
print("- 分组和捕获")
print("- 多种匹配模式")
print("- 性能优化选项")

print("\n应用场景:")
print("- 文本提取和验证")
print("- 数据清洗和转换")
print("- 日志分析")
print("- 网页爬虫")
print("- 配置文件解析")

print("\n使用re模块可以高效地处理各种文本处理任务")
print("是Python编程中不可或缺的工具之一")
