# 正则表达式实际应用示例

本文件包含了正则表达式在实际开发中的各种应用示例，涵盖了数据验证、数据提取、数据清洗、日志分析、网页爬虫等多个领域。通过这些示例，您可以更好地理解正则表达式的实际应用场景和使用方法。

## 1. 数据验证

### 1.1 邮箱验证

```python
import re

def validate_email(email):
    """验证邮箱格式"""
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

# 测试邮箱验证
emails = [
    'test@example.com',
    'test.email@example.com',
    'test+email@example.com',
    'test@sub.example.com',
    'test@example',
    'test@.com',
    '@example.com'
]

print("=== 邮箱验证 ===")
for email in emails:
    is_valid = validate_email(email)
    print(f"{email}: {'有效' if is_valid else '无效'}")
```

### 1.2 电话号码验证

```python
import re

def validate_phone(phone):
    """验证电话号码格式"""
    # 支持多种格式：13812345678、010-12345678、(010)12345678、010 12345678
    pattern = re.compile(r'^(?:1[3-9]\d{9}|0\d{2,3}[\-\s]?\d{7,8}|\(0\d{2,3}\)\d{7,8})$')
    return bool(pattern.match(phone))

# 测试电话号码验证
phones = [
    '13812345678',
    '15987654321',
    '010-12345678',
    '(010)12345678',
    '010 12345678',
    '12345678901',
    '1381234567',
    '138123456789'
]

print("\n=== 电话号码验证 ===")
for phone in phones:
    is_valid = validate_phone(phone)
    print(f"{phone}: {'有效' if is_valid else '无效'}")
```

### 1.3 身份证号码验证

```python
import re

def validate_id_card(id_card):
    """验证身份证号码格式"""
    # 支持18位身份证号码，最后一位可以是数字或X/x
    pattern = re.compile(r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$')
    return bool(pattern.match(id_card))

# 测试身份证号码验证
id_cards = [
    '110101199001011234',
    '11010119900101123X',
    '11010119900101123x',
    '1101011990010112',
    '1101011990010112345',
    '110101199013011234'
]

print("\n=== 身份证号码验证 ===")
for id_card in id_cards:
    is_valid = validate_id_card(id_card)
    print(f"{id_card}: {'有效' if is_valid else '无效'}")
```

### 1.4 密码强度验证

```python
import re

def validate_password(password):
    """验证密码强度"""
    # 至少包含一个大写字母、一个小写字母、一个数字和一个特殊字符，长度至少8位
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(pattern.match(password))

# 测试密码强度验证
passwords = [
    'Password123!',
    'password123!',
    'PASSWORD123!',
    'Password123',
    'Password!',
    '12345678!',
    'Pass1!'
]

print("\n=== 密码强度验证 ===")
for password in passwords:
    is_valid = validate_password(password)
    print(f"{password}: {'强密码' if is_valid else '弱密码'}")
```

### 1.5 IP地址验证

```python
import re

def validate_ip(ip):
    """验证IP地址格式"""
    pattern = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    return bool(pattern.match(ip))

# 测试IP地址验证
ips = [
    '192.168.1.1',
    '10.0.0.1',
    '255.255.255.0',
    '256.255.255.0',
    '192.168.1',
    '192.168.1.1.1'
]

print("\n=== IP地址验证 ===")
for ip in ips:
    is_valid = validate_ip(ip)
    print(f"{ip}: {'有效' if is_valid else '无效'}")
```

## 2. 数据提取

### 2.1 提取URL

```python
import re

def extract_urls(text):
    """从文本中提取URL"""
    pattern = re.compile(r'https?://[\w\-]+(\.[\w\-]+)+([\w\-.,@?^=%&:/~\+#]*[\w\-@?^=%&/~\+#])?')
    return pattern.findall(text)

# 测试提取URL
text = '访问我们的网站：https://www.example.com 和 https://sub.example.com/path?param=value 了解更多信息。'

urls = extract_urls(text)
print("\n=== 提取URL ===")
for url in urls:
    full_url = f"{url[0]}{url[1]}"
    print(full_url)
```

### 2.2 提取IP地址

```python
import re

def extract_ips(text):
    """从文本中提取IP地址"""
    pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    return pattern.findall(text)

# 测试提取IP地址
text = '服务器IP地址：192.168.1.1 和 10.0.0.1，网关：192.168.1.254。'

ips = extract_ips(text)
print("\n=== 提取IP地址 ===")
for ip in ips:
    print(ip)
```

### 2.3 提取日期

```python
import re

def extract_dates(text):
    """从文本中提取日期"""
    # 支持多种日期格式：2023-12-01、12/02/2023、20231203
    pattern = re.compile(r'\b(?:\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{4}\d{2}\d{2})\b')
    return pattern.findall(text)

# 测试提取日期
text = '今天是2023-12-01，明天是12/02/2023，后天是20231203。'

dates = extract_dates(text)
print("\n=== 提取日期 ===")
for date in dates:
    print(date)
```

### 2.4 提取电话号码

```python
import re

def extract_phones(text):
    """从文本中提取电话号码"""
    pattern = re.compile(r'1[3-9]\d{9}|0\d{2,3}[\-\s]?\d{7,8}|\(0\d{2,3}\)\d{7,8}')
    return pattern.findall(text)

# 测试提取电话号码
text = '联系电话：13812345678 或 010-12345678，也可以拨打(020)87654321。'

phones = extract_phones(text)
print("\n=== 提取电话号码 ===")
for phone in phones:
    print(phone)
```

### 2.5 提取邮箱地址

```python
import re

def extract_emails(text):
    """从文本中提取邮箱地址"""
    pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    return pattern.findall(text)

# 测试提取邮箱地址
text = '联系邮箱：test@example.com 和 admin@sub.example.com，也可以发送邮件到support@company.com。'

emails = extract_emails(text)
print("\n=== 提取邮箱地址 ===")
for email in emails:
    print(email)
```

## 3. 数据清洗

### 3.1 移除HTML标签

```python
import re

def remove_html_tags(text):
    """移除HTML标签"""
    pattern = re.compile(r'<.*?>')
    return pattern.sub('', text)

# 测试移除HTML标签
html = '<div class="content">Hello, World! <p>你好，世界！</p> <a href="https://www.example.com">访问我们的网站</a></div>'

cleaned_text = remove_html_tags(html)
print("\n=== 移除HTML标签 ===")
print(f"清洗前: {html}")
print(f"清洗后: {cleaned_text}")
```

### 3.2 移除特殊字符

```python
import re

def remove_special_chars(text):
    """移除特殊字符，只保留字母、数字、空格和中文"""
    pattern = re.compile(r'[^\w\s\u4e00-\u9fa5]')
    return pattern.sub('', text)

# 测试移除特殊字符
text = 'Hello, World! 你好，世界！123 #@$%^&*()_+-=[]{}|;\':",./<>?'

cleaned_text = remove_special_chars(text)
print("\n=== 移除特殊字符 ===")
print(f"清洗前: {text}")
print(f"清洗后: {cleaned_text}")
```

### 3.3 移除多余的空格

```python
import re

def remove_extra_spaces(text):
    """移除多余的空格"""
    pattern = re.compile(r'\s+')
    return pattern.sub(' ', text).strip()

# 测试移除多余的空格
text = '  Hello   World!   你好，   世界！  '

cleaned_text = remove_extra_spaces(text)
print("\n=== 移除多余的空格 ===")
print(f"清洗前: '{text}'")
print(f"清洗后: '{cleaned_text}'")
```

### 3.4 标准化日期格式

```python
import re

def standardize_date(date):
    """标准化日期格式，将各种日期格式转换为YYYY-MM-DD格式"""
    patterns = [
        (r'(\d{4})/(\d{2})/(\d{2})', r'\1-\2-\3'),  # YYYY/MM/DD
        (r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2'),  # MM/DD/YYYY
        (r'(\d{4})\.(\d{2})\.(\d{2})', r'\1-\2-\3'),  # YYYY.MM.DD
        (r'(\d{2})\.(\d{2})\.(\d{4})', r'\3-\1-\2'),  # MM.DD.YYYY
        (r'(\d{4})(\d{2})(\d{2})', r'\1-\2-\3')  # YYYYMMDD
    ]
    
    standardized_date = date
    for pattern, replacement in patterns:
        standardized_date = re.sub(pattern, replacement, standardized_date)
    
    return standardized_date

# 测试标准化日期格式
dates = [
    '2023/12/01',
    '12/02/2023',
    '2023.12.03',
    '12.04.2023',
    '20231205',
    '2023-12-06'
]

print("\n=== 标准化日期格式 ===")
for date in dates:
    standardized_date = standardize_date(date)
    print(f"{date} → {standardized_date}")
```

### 3.5 提取纯数字

```python
import re

def extract_numbers(text):
    """从文本中提取纯数字"""
    pattern = re.compile(r'\d+')
    return list(map(int, pattern.findall(text)))

# 测试提取纯数字
text = '价格：100元，折扣：20%，数量：5个，总价：500元。'

numbers = extract_numbers(text)
print("\n=== 提取纯数字 ===")
print(f"文本: {text}")
print(f"数字: {numbers}")
```

## 4. 日志分析

### 4.1 解析日志行

```python
import re

def parse_log(log_line):
    """解析日志行"""
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(\w+)\s+(.*)')
    match = pattern.match(log_line)
    
    if match:
        return {
            'timestamp': match.group(1),
            'level': match.group(2),
            'module': match.group(3),
            'message': match.group(4)
        }
    else:
        return None

# 测试解析日志行
log_lines = [
    '2023-12-01 10:00:00 INFO main 程序启动',
    '2023-12-01 10:01:00 ERROR database 数据库连接失败',
    '2023-12-01 10:02:00 WARNING network 网络连接超时',
    '2023-12-01 10:03:00 DEBUG api API请求: /users'
]

print("\n=== 解析日志行 ===")
for log_line in log_lines:
    parsed_log = parse_log(log_line)
    if parsed_log:
        print(f"时间戳: {parsed_log['timestamp']}")
        print(f"日志级别: {parsed_log['level']}")
        print(f"模块: {parsed_log['module']}")
        print(f"消息: {parsed_log['message']}")
        print()
```

### 4.2 统计日志级别

```python
import re

def count_log_levels(logs):
    """统计不同日志级别的数量"""
    pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+(\w+)')
    levels = {}
    
    for log in logs:
        match = pattern.match(log)
        if match:
            level = match.group(1)
            levels[level] = levels.get(level, 0) + 1
    
    return levels

# 测试统计日志级别
logs = [
    '2023-12-01 10:00:00 INFO main 程序启动',
    '2023-12-01 10:01:00 ERROR database 数据库连接失败',
    '2023-12-01 10:02:00 WARNING network 网络连接超时',
    '2023-12-01 10:03:00 DEBUG api API请求: /users',
    '2023-12-01 10:04:00 INFO database 数据库连接成功',
    '2023-12-01 10:05:00 ERROR api API请求失败'
]

log_levels = count_log_levels(logs)
print("\n=== 统计日志级别 ===")
for level, count in log_levels.items():
    print(f"{level}: {count}")
```

### 4.3 提取错误日志

```python
import re

def extract_error_logs(logs):
    """提取错误日志"""
    pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\s+ERROR\s+(.*)')
    error_logs = []
    
    for log in logs:
        match = pattern.match(log)
        if match:
            error_logs.append(log)
    
    return error_logs

# 测试提取错误日志
logs = [
    '2023-12-01 10:00:00 INFO main 程序启动',
    '2023-12-01 10:01:00 ERROR database 数据库连接失败',
    '2023-12-01 10:02:00 WARNING network 网络连接超时',
    '2023-12-01 10:03:00 DEBUG api API请求: /users',
    '2023-12-01 10:04:00 INFO database 数据库连接成功',
    '2023-12-01 10:05:00 ERROR api API请求失败'
]

error_logs = extract_error_logs(logs)
print("\n=== 提取错误日志 ===")
for log in error_logs:
    print(log)
```

## 5. 网页爬虫

### 5.1 提取网页标题

```python
import re

def extract_title(html):
    """从HTML中提取网页标题"""
    pattern = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)
    match = pattern.search(html)
    return match.group(1) if match else None

# 测试提取网页标题
html = '<!DOCTYPE html><html><head><title>测试网页</title></head><body><h1>Hello, World!</h1></body></html>'

title = extract_title(html)
print("\n=== 提取网页标题 ===")
print(f"HTML: {html}")
print(f"标题: {title}")
```

### 5.2 提取网页链接

```python
import re

def extract_links(html):
    """从HTML中提取网页链接"""
    pattern = re.compile(r'<a\s+href=["\'](.*?)["\'].*?>(.*?)</a>', re.IGNORECASE)
    return pattern.findall(html)

# 测试提取网页链接
html = '<div><a href="https://www.example.com">Example</a><a href="https://sub.example.com">Sub Example</a></div>'

links = extract_links(html)
print("\n=== 提取网页链接 ===")
for href, text in links:
    print(f"文本: {text}, 链接: {href}")
```

### 5.3 提取图片链接

```python
import re

def extract_images(html):
    """从HTML中提取图片链接"""
    pattern = re.compile(r'<img\s+src=["\'](.*?)["\'].*?>', re.IGNORECASE)
    return pattern.findall(html)

# 测试提取图片链接
html = '<div><img src="https://www.example.com/image1.jpg" alt="Image 1"><img src="https://www.example.com/image2.jpg" alt="Image 2"></div>'

images = extract_images(html)
print("\n=== 提取图片链接 ===")
for image in images:
    print(image)
```

## 6. 文本处理

### 6.1 提取中文

```python
import re

def extract_chinese(text):
    """从文本中提取中文"""
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    return pattern.findall(text)

# 测试提取中文
text = 'Hello, 世界！This is a 测试 text。'

chinese = extract_chinese(text)
print("\n=== 提取中文 ===")
print(f"文本: {text}")
print(f"中文: {chinese}")
```

### 6.2 提取英文单词

```python
import re

def extract_english_words(text):
    """从文本中提取英文单词"""
    pattern = re.compile(r'[a-zA-Z]+')
    return pattern.findall(text)

# 测试提取英文单词
text = 'Hello, 世界！This is a 测试 text。'

words = extract_english_words(text)
print("\n=== 提取英文单词 ===")
print(f"文本: {text}")
print(f"英文单词: {words}")
```

### 6.3 替换重复单词

```python
import re

def remove_duplicate_words(text):
    """移除重复的单词"""
    pattern = re.compile(r'(\b\w+\b)\s+\1', re.IGNORECASE)
    while pattern.search(text):
        text = pattern.sub(r'\1', text)
    return text

# 测试替换重复单词
text = 'Hello hello world world test test test.'

cleaned_text = remove_duplicate_words(text)
print("\n=== 替换重复单词 ===")
print(f"替换前: {text}")
print(f"替换后: {cleaned_text}")
```

### 6.4 转换大小写

```python
import re

def capitalize_sentences(text):
    """将句子的首字母大写"""
    pattern = re.compile(r'(?:^|[.!?]\s+)(\w)')
    return pattern.sub(lambda match: match.group(1).upper(), text)

# 测试转换大小写
text = 'hello world. this is a test! how are you?'

capitalized_text = capitalize_sentences(text)
print("\n=== 转换大小写 ===")
print(f"转换前: {text}")
print(f"转换后: {capitalized_text}")
```

## 7. 高级应用

### 7.1 解析JSON格式

```python
import re

def parse_simple_json(json_str):
    """解析简单的JSON字符串"""
    # 简单的JSON解析，只处理字符串、数字、布尔值和null
    pattern = re.compile(r'"(.*?)"\s*:\s*(["\'].*?["\']|\d+\.?\d*|true|false|null)')
    matches = pattern.findall(json_str)
    
    result = {}
    for key, value in matches:
        # 处理字符串值
        if value.startswith('"') and value.endswith('"'):
            result[key] = value[1:-1]
        # 处理数字值
        elif re.match(r'\d+\.?\d*', value):
            result[key] = float(value) if '.' in value else int(value)
        # 处理布尔值
        elif value.lower() == 'true':
            result[key] = True
        elif value.lower() == 'false':
            result[key] = False
        # 处理null值
        elif value.lower() == 'null':
            result[key] = None
    
    return result

# 测试解析JSON格式
json_str = '{"name": "张三", "age": 18, "is_student": true, "score": 95.5, "address": null}'

parsed_json = parse_simple_json(json_str)
print("\n=== 解析JSON格式 ===")
print(f"JSON字符串: {json_str}")
print(f"解析结果: {parsed_json}")
```

### 7.2 验证信用卡号

```python
import re

def validate_credit_card(card_number):
    """验证信用卡号"""
    # 移除空格和连字符
    card_number = re.sub(r'[\s-]', '', card_number)
    
    # 验证格式
    pattern = re.compile(r'^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|3[0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})$')
    if not pattern.match(card_number):
        return False
    
    # Luhn算法验证
    digits = list(map(int, card_number))
    check_sum = 0
    
    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        check_sum += digit
    
    return check_sum % 10 == 0

# 测试验证信用卡号
credit_cards = [
    '4111 1111 1111 1111',
    '5555 5555 5555 4444',
    '3782 822463 10005',
    '3530 111333300000',
    '6011 1111 1111 1117',
    '4111 1111 1111 1112'
]

print("\n=== 验证信用卡号 ===")
for card in credit_cards:
    is_valid = validate_credit_card(card)
    print(f"{card}: {'有效' if is_valid else '无效'}")
```

### 7.3 提取HTML表格内容

```python
import re

def extract_table(html):
    """从HTML中提取表格内容"""
    # 提取表格行
    row_pattern = re.compile(r'<tr>(.*?)</tr>', re.DOTALL | re.IGNORECASE)
    rows = row_pattern.findall(html)
    
    table = []
    for row in rows:
        # 提取单元格
        cell_pattern = re.compile(r'<t[hd]>(.*?)</t[hd]>', re.DOTALL | re.IGNORECASE)
        cells = cell_pattern.findall(row)
        # 移除HTML标签
        cells = [re.sub(r'<.*?>', '', cell).strip() for cell in cells]
        table.append(cells)
    
    return table

# 测试提取HTML表格内容
html = '''
<table>
  <tr>
    <th>姓名</th>
    <th>年龄</th>
    <th>性别</th>
  </tr>
  <tr>
    <td>张三</td>
    <td>18</td>
    <td>男</td>
  </tr>
  <tr>
    <td>李四</td>
    <td>20</td>
    <td>女</td>
  </tr>
</table>
'''

table = extract_table(html)
print("\n=== 提取HTML表格内容 ===")
for row in table:
    print(row)
```

## 总结

正则表达式是一种强大的文本处理工具，在实际开发中有广泛的应用。本文件包含了正则表达式在数据验证、数据提取、数据清洗、日志分析、网页爬虫、文本处理等多个领域的实际应用示例。通过这些示例，您可以更好地理解正则表达式的实际应用场景和使用方法。

在实际应用中，您应该根据具体需求选择合适的正则表达式，并注意正则表达式的性能优化。对于复杂的正则表达式，您可以使用`re.DEBUG`修饰符进行调试，以确保正则表达式的正确性和性能。

希望这些示例能够帮助您更好地掌握正则表达式的实际应用，提高您的文本处理能力。