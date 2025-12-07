# Python re模块详细指南

## 一、模块概述

`re`模块是Python标准库中用于正则表达式操作的核心模块，提供了强大的字符串匹配、查找、替换和分割功能。正则表达式是一种用于描述字符串模式的工具，能够高效地处理复杂的文本处理任务，如数据验证、文本提取、内容替换等。

## 二、基本概念

1. **正则表达式**：用于描述字符串模式的语法规则
2. **模式(pattern)**：正则表达式定义的匹配模板
3. **匹配对象(match object)**：成功匹配后返回的对象，包含匹配的详细信息
4. **分组(group)**：将匹配的部分内容分组，便于提取和引用
5. **锚点(anchor)**：用于定位匹配位置（如行首、行尾）
6. **量词(quantifier)**：指定匹配次数（如0次或1次、1次或多次、0次或多次）
7. **转义字符(escape character)**：用于匹配特殊字符本身

## 三、基本语法

### 1. 字符匹配

| 语法 | 描述 |
|------|------|
| `\d` | 匹配任意数字，等价于`[0-9]` |
| `\D` | 匹配任意非数字，等价于`[^0-9]` |
| `\w` | 匹配任意字母、数字或下划线，等价于`[a-zA-Z0-9_]` |
| `\W` | 匹配任意非字母、数字或下划线，等价于`[^a-zA-Z0-9_]` |
| `\s` | 匹配任意空白字符（空格、制表符、换行符等） |
| `\S` | 匹配任意非空白字符 |
| `.` | 匹配任意字符（除换行符外） |
| `[abc]` | 匹配a、b或c中的任意一个字符 |
| `[^abc]` | 匹配除a、b、c外的任意一个字符 |
| `[a-z]` | 匹配任意小写字母 |
| `[A-Z]` | 匹配任意大写字母 |
| `[0-9]` | 匹配任意数字 |

### 2. 量词

| 语法 | 描述 |
|------|------|
| `*` | 匹配0次或多次 |
| `+` | 匹配1次或多次 |
| `?` | 匹配0次或1次 |
| `{n}` | 匹配恰好n次 |
| `{n,}` | 匹配至少n次 |
| `{n,m}` | 匹配n到m次 |
| `*?`, `+?`, `??`, `{n,m}?` | 非贪婪匹配（尽可能少匹配） |

### 3. 锚点

| 语法 | 描述 |
|------|------|
| `^` | 匹配字符串开头 |
| `$` | 匹配字符串结尾 |
| `\b` | 匹配单词边界 |
| `\B` | 匹配非单词边界 |

### 4. 分组和引用

| 语法 | 描述 |
|------|------|
| `(...)` | 捕获组，将匹配的内容分组并保存 |
| `(?:...)` | 非捕获组，仅分组不保存匹配内容 |
| `(?P<name>...)` | 命名捕获组，为分组指定名称 |
| `\1`, `\2`, ... | 反向引用，引用前面捕获组的匹配内容 |
| `(?P=name)` | 命名反向引用，引用前面命名捕获组的匹配内容 |

### 5. 特殊字符

| 语法 | 描述 |
|------|------|
| `\` | 转义字符，用于匹配特殊字符本身 |
| `|` | 或操作，匹配左侧或右侧的模式 |
| `()` | 分组操作符 |
| `[]` | 字符类操作符 |
| `{}` | 量词操作符 |

## 四、基本用法

### 1. 导入模块

```python
import re
```

### 2. 编译正则表达式

```python
# 编译正则表达式模式
pattern = re.compile(r'\d+')  # 匹配一个或多个数字

# 使用编译后的模式进行匹配
result = pattern.match('123abc')
print(result)  # <re.Match object; span=(0, 3), match='123'>
```

### 3. 匹配方法

#### 3.1 match()方法

```python
# match()方法：从字符串开头开始匹配
pattern = re.compile(r'\d+')

# 匹配成功返回Match对象
result = pattern.match('123abc')
print(result)  # <re.Match object; span=(0, 3), match='123'>
print(result.group())  # 123
print(result.span())  # (0, 3)

# 匹配失败返回None
result = pattern.match('abc123')
print(result)  # None
```

#### 3.2 search()方法

```python
# search()方法：在整个字符串中查找第一个匹配项
pattern = re.compile(r'\d+')

# 查找字符串中的第一个数字
result = pattern.search('abc123def456')
print(result)  # <re.Match object; span=(3, 6), match='123'>
print(result.group())  # 123
```

#### 3.3 findall()方法

```python
# findall()方法：查找所有匹配项，返回列表
pattern = re.compile(r'\d+')

# 查找字符串中的所有数字
results = pattern.findall('abc123def456')
print(results)  # ['123', '456']

# 带分组的findall()
pattern = re.compile(r'(\d+)-(\w+)')
results = pattern.findall('123-abc,456-def')
print(results)  # [('123', 'abc'), ('456', 'def')]
```

#### 3.4 finditer()方法

```python
# finditer()方法：查找所有匹配项，返回迭代器
pattern = re.compile(r'\d+')

# 查找字符串中的所有数字
results = pattern.finditer('abc123def456')
for result in results:
    print(result.group(), result.span())  # 123 (3, 6)  # 456 (9, 12)
```

### 4. 替换方法

#### 4.1 sub()方法

```python
# sub()方法：替换匹配的内容
pattern = re.compile(r'\d+')

# 将数字替换为'X'
result = pattern.sub('X', 'abc123def456')
print(result)  # abcXdefX

# 限制替换次数
result = pattern.sub('X', 'abc123def456', count=1)
print(result)  # abcXdef456

# 使用函数进行替换
def replace_func(match):
    return str(int(match.group()) * 2)

result = pattern.sub(replace_func, 'abc123def456')
print(result)  # abc246def912
```

#### 4.2 subn()方法

```python
# subn()方法：替换匹配的内容，返回替换后的字符串和替换次数
pattern = re.compile(r'\d+')

result, count = pattern.subn('X', 'abc123def456')
print(result)  # abcXdefX
print(count)  # 2
```

### 5. 分割方法

```python
# split()方法：根据匹配的内容分割字符串
pattern = re.compile(r'\d+')

# 使用数字分割字符串
result = pattern.split('abc123def456ghi')
print(result)  # ['abc', 'def', 'ghi']

# 限制分割次数
result = pattern.split('abc123def456ghi', maxsplit=1)
print(result)  # ['abc', 'def456ghi']
```

### 6. 匹配对象(Match Object)

```python
# 匹配对象的常用方法
pattern = re.compile(r'(\w+) (\w+)')
result = pattern.match('Hello World')

# 获取匹配的整个字符串
print(result.group())  # Hello World

# 获取第一个分组
print(result.group(1))  # Hello

# 获取第二个分组
print(result.group(2))  # World

# 获取所有分组
print(result.groups())  # ('Hello', 'World')

# 获取匹配的起始位置
print(result.start())  # 0

# 获取匹配的结束位置
print(result.end())  # 11

# 获取匹配的起止位置
print(result.span())  # (0, 11)

# 获取第一个分组的起止位置
print(result.span(1))  # (0, 5)
```

## 五、高级用法

### 1. 分组和命名分组

```python
# 分组
pattern = re.compile(r'(\d{3})-(\d{3}-\d{4})')
result = pattern.match('123-456-7890')
print(result.group())  # 123-456-7890
print(result.group(1))  # 123
print(result.group(2))  # 456-7890

# 命名分组
pattern = re.compile(r'(?P<area_code>\d{3})-(?P<phone_number>\d{3}-\d{4})')
result = pattern.match('123-456-7890')
print(result.group('area_code'))  # 123
print(result.group('phone_number'))  # 456-7890

# 使用命名分组进行替换
pattern = re.compile(r'(?P<first>\w+) (?P<last>\w+)')
result = pattern.sub(r'\g<last>, \g<first>', 'John Doe')
print(result)  # Doe, John
```

### 2. 非贪婪匹配

```python
# 贪婪匹配（默认）
pattern = re.compile(r'<.*>')
result = pattern.match('<div>content</div>')
print(result.group())  # <div>content</div>  # 匹配了整个字符串

# 非贪婪匹配
pattern = re.compile(r'<.*?>')
result = pattern.match('<div>content</div>')
print(result.group())  # <div>  # 只匹配了第一个标签

# 其他非贪婪量词
pattern = re.compile(r'a{1,3}?')  # 匹配1到3个a，但尽可能少匹配
result = pattern.match('aaa')
print(result.group())  # a
```

### 3. 断言(Assertion)

```python
# 正向先行断言：匹配后面跟着特定模式的内容
pattern = re.compile(r'\w+(?=\s+\d+)')  # 匹配后面跟着数字的单词
result = pattern.search('apple 100 banana 200')
print(result.group())  # apple

# 负向先行断言：匹配后面不跟着特定模式的内容
pattern = re.compile(r'\w+(?!\s+\d+)')  # 匹配后面不跟着数字的单词
result = pattern.search('apple 100 banana')
print(result.group())  # banana

# 正向后行断言：匹配前面是特定模式的内容
pattern = re.compile(r'(?<=\$)\d+')  # 匹配前面是$的数字
result = pattern.search('Price: $100')
print(result.group())  # 100

# 负向后行断言：匹配前面不是特定模式的内容
pattern = re.compile(r'(?<!\$)\d+')  # 匹配前面不是$的数字
result = pattern.search('Price: $100, Quantity: 5')
print(result.group())  # 5
```

### 4. 标志(Flags)

```python
# 不区分大小写
pattern = re.compile(r'hello', re.IGNORECASE)
result = pattern.match('Hello World')
print(result.group())  # Hello

# 多行模式：^和$匹配每行的开头和结尾
pattern = re.compile(r'^\w+', re.MULTILINE)
text = 'Line 1\nLine 2\nLine 3'
results = pattern.findall(text)
print(results)  # ['Line', 'Line', 'Line']

# 点号匹配所有字符（包括换行符）
pattern = re.compile(r'.+', re.DOTALL)
text = 'Line 1\nLine 2'
result = pattern.match(text)
print(result.group())  # Line 1\nLine 2

# 详细模式：允许正则表达式包含注释和空白
pattern = re.compile(r'''\d{3}  # 区号
                         -      # 分隔符
                         \d{3}  # 前缀
                         -      # 分隔符
                         \d{4}  # 后缀''', re.VERBOSE)
result = pattern.match('123-456-7890')
print(result.group())  # 123-456-7890

# 组合标志
pattern = re.compile(r'^hello', re.IGNORECASE | re.MULTILINE)
```

### 5. 反向引用

```python
# 使用反向引用匹配重复的单词
pattern = re.compile(r'(\w+)\s+\1')
result = pattern.search('hello hello world')
print(result.group())  # hello hello

# 使用反向引用匹配HTML标签
pattern = re.compile(r'<(\w+)>.*?</\1>')
result = pattern.search('<div>content</div>')
print(result.group())  # <div>content</div>

# 使用命名反向引用
pattern = re.compile(r'(?P<tag>\w+)>.*?</(?P=tag)>')
result = pattern.search('<div>content</div>')
print(result.group())  # <div>content</div>
```

## 六、实际应用示例

### 1. 数据验证

```python
# 验证邮箱地址
def is_valid_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

# 测试示例
emails = ['user@example.com', 'user.name@example.com', 'user+tag@example.co.uk', 'invalid-email', 'user@']
for email in emails:
    print(f"{email}: {'有效' if is_valid_email(email) else '无效'}")

# 验证手机号码
def is_valid_phone(phone):
    pattern = re.compile(r'^1[3-9]\d{9}$')  # 中国手机号格式
    return bool(pattern.match(phone))

# 测试示例
phones = ['13812345678', '15987654321', '12345678901', '1381234567']
for phone in phones:
    print(f"{phone}: {'有效' if is_valid_phone(phone) else '无效'}")

# 验证身份证号码
def is_valid_id_card(id_card):
    pattern = re.compile(r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$')
    return bool(pattern.match(id_card))

# 测试示例
id_cards = ['110101199001011234', '11010119900101123X', '1101011990010112', '110101199013011234']
for id_card in id_cards:
    print(f"{id_card}: {'有效' if is_valid_id_card(id_card) else '无效'}")
```

### 2. 文本提取

```python
# 提取URL中的域名
def extract_domain(url):
    pattern = re.compile(r'https?://(?:www\.)?([^/]+)')
    match = pattern.search(url)
    return match.group(1) if match else None

# 测试示例
urls = ['https://www.example.com', 'http://example.org/path', 'https://subdomain.example.net/page.html']
for url in urls:
    print(f"{url} -> {extract_domain(url)}")

# 提取文本中的所有邮箱地址
def extract_emails(text):
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    return pattern.findall(text)

# 测试示例
text = '联系我们：support@example.com 或 sales@company.org'
emails = extract_emails(text)
print(f"提取的邮箱：{emails}")

# 提取HTML中的所有链接
def extract_links(html):
    pattern = re.compile(r'<a\s+href="([^"]+)"[^>]*>')
    return pattern.findall(html)

# 测试示例
html = '<a href="https://www.example.com">Example</a> <a href="http://example.org">Another</a>'
links = extract_links(html)
print(f"提取的链接：{links}")
```

### 3. 内容替换

```python
# 替换文本中的敏感词
def censor_text(text, sensitive_words):
    # 创建敏感词正则表达式
    pattern = re.compile(r'|'.join(re.escape(word) for word in sensitive_words), re.IGNORECASE)
    # 替换为星号
    return pattern.sub(lambda m: '*' * len(m.group()), text)

# 测试示例
text = '这是一个测试，包含敏感词和不良内容'
sensitive_words = ['敏感词', '不良']
censored_text = censor_text(text, sensitive_words)
print(f"原文本：{text}")
print(f"过滤后：{censored_text}")

# 格式化日期
def format_date(text):
    # 将YYYY-MM-DD格式转换为MM/DD/YYYY
    pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
    return pattern.sub(r'\2/\3/\1', text)

# 测试示例
date_text = '今天是2023-12-25，明天是2023-12-26'
formatted_text = format_date(date_text)
print(f"原日期：{date_text}")
print(f"格式化后：{formatted_text}")

# 移除HTML标签
def remove_html_tags(html):
    pattern = re.compile(r'<[^>]+>')
    return pattern.sub('', html)

# 测试示例
html_text = '<h1>标题</h1><p>段落内容</p>'
plain_text = remove_html_tags(html_text)
print(f"HTML：{html_text}")
print(f"纯文本：{plain_text}")
```

### 4. 日志分析

```python
# 分析访问日志，提取IP地址和访问时间
def parse_access_log(log_line):
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\]')
    match = pattern.match(log_line)
    if match:
        return {
            'ip': match.group(1),
            'time': match.group(2)
        }
    return None

# 测试示例
log_line = '192.168.1.1 - - [25/Dec/2023:14:30:45 +0800] "GET /index.html HTTP/1.1" 200 1234'
parsed = parse_access_log(log_line)
print(f"IP地址：{parsed['ip']}")
print(f"访问时间：{parsed['time']}")

# 统计日志中每个IP的访问次数
def count_ip_visits(log_file):
    from collections import Counter
    pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
    ip_counts = Counter()
    
    with open(log_file, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                ip_counts[match.group(1)] += 1
    
    return ip_counts

# 使用示例
# ip_counts = count_ip_visits('access.log')
# for ip, count in ip_counts.most_common(10):
#     print(f"{ip}: {count}次访问")
```

### 5. 数据清洗

```python
# 清洗电话号码（统一格式）
def clean_phone_number(phone):
    # 移除所有非数字字符
    pattern = re.compile(r'\D')
    clean = pattern.sub('', phone)
    
    # 添加适当的格式
    if len(clean) == 11 and clean.startswith('1'):  # 中国手机号
        return f'{clean[:3]}-{clean[3:7]}-{clean[7:]}'
    elif len(clean) == 10:  # 美国手机号
        return f'({clean[:3]}) {clean[3:6]}-{clean[6:]}'
    return clean

# 测试示例
phones = ['13812345678', '159-8765-4321', '+86 138 1234 5678', '123-4567-8901']
for phone in phones:
    print(f"{phone} -> {clean_phone_number(phone)}")

# 清洗文本中的多余空格
def clean_whitespace(text):
    # 将多个空格替换为一个空格
    pattern = re.compile(r'\s+')
    return pattern.sub(' ', text).strip()

# 测试示例
text = '  这是   一段  有  多余空格  的  文本  '  
clean_text = clean_whitespace(text)
print(f"原文本：'{text}'")
print(f"清洗后：'{clean_text}'")

# 移除文本中的特殊字符
def remove_special_chars(text, keep_chars=''):
    # 保留字母、数字、空格和指定的特殊字符
    pattern = re.compile(r'[^a-zA-Z0-9\s' + re.escape(keep_chars) + ']')
    return pattern.sub('', text)

# 测试示例
text = 'Hello, World! 你好，世界！123@#$'
clean_text = remove_special_chars(text, keep_chars=',.!')
print(f"原文本：{text}")
print(f"清洗后：{clean_text}")
```

## 七、最佳实践

1. **编译正则表达式**：对于重复使用的正则表达式，使用`re.compile()`编译可以提高性能
2. **使用原始字符串**：使用`r''`原始字符串可以避免转义字符的问题
3. **保持正则表达式简洁**：复杂的正则表达式难以维护，考虑拆分或使用其他方法
4. **测试正则表达式**：使用在线工具（如regex101.com）测试正则表达式的正确性
5. **处理边界情况**：考虑所有可能的输入情况，避免意外匹配
6. **使用分组提取数据**：使用分组和命名分组便于提取和引用匹配内容
7. **注意贪婪匹配**：根据需要使用非贪婪量词（`*?`, `+?`, `??`）
8. **使用标志简化模式**：如`re.IGNORECASE`、`re.MULTILINE`等
9. **避免过度使用正则表达式**：对于简单的文本处理任务，使用字符串方法可能更高效
10. **添加注释**：对于复杂的正则表达式，使用`re.VERBOSE`标志添加注释提高可读性

## 八、与其他模块的关系

1. **string模块**：
   - `string`模块提供了一些字符串常量，如`string.ascii_letters`、`string.digits`等
   - 可以与正则表达式结合使用，如`[{}]`.format(string.ascii_letters)

2. **textwrap模块**：
   - `textwrap`模块用于文本格式化
   - 可以与正则表达式结合使用，如先使用正则表达式提取文本，再使用`textwrap`格式化

3. **html模块**：
   - `html`模块用于HTML转义和解转义
   - 可以与正则表达式结合使用，如提取HTML内容后进行转义处理

4. **json模块**：
   - `json`模块用于JSON数据处理
   - 可以与正则表达式结合使用，如验证JSON格式或提取JSON数据

## 九、总结

`re`模块是Python中处理正则表达式的核心模块，提供了强大的字符串匹配、查找、替换和分割功能。通过掌握正则表达式的语法和`re`模块的使用，可以高效地处理各种复杂的文本处理任务，如数据验证、文本提取、内容替换等。

正则表达式是一把双刃剑，虽然功能强大，但过度复杂的正则表达式会降低代码的可读性和维护性。在实际应用中，应根据任务需求选择合适的工具，对于简单的文本处理任务，使用字符串方法可能更高效；对于复杂的模式匹配任务，正则表达式则是更好的选择。

通过结合`re`模块的各种方法和正则表达式的高级特性，可以编写出高效、灵活的文本处理代码，解决各种实际应用中的文本处理问题。