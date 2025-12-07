# 正则表达式语法参考

正则表达式是一种用于匹配字符串中字符组合的模式，是一种强大的文本处理工具。Python的re模块支持标准的正则表达式语法，本文件将详细介绍正则表达式的各种语法元素。

## 基本元字符

元字符是正则表达式中具有特殊含义的字符，需要使用反斜杠`\`进行转义才能匹配其本身。

| 元字符 | 描述 | 示例 |
|-------|------|------|
| `.` | 匹配除换行符以外的任意单个字符 | `a.b` 匹配 "acb"、"a1b"、"a@b" 等 |
| `^` | 匹配字符串的开头 | `^abc` 匹配以 "abc" 开头的字符串 |
| `$` | 匹配字符串的结尾 | `abc$` 匹配以 "abc" 结尾的字符串 |
| `*` | 匹配前面的字符0次或多次（贪婪匹配） | `a*` 匹配 ""、"a"、"aa"、"aaa" 等 |
| `+` | 匹配前面的字符1次或多次（贪婪匹配） | `a+` 匹配 "a"、"aa"、"aaa" 等 |
| `?` | 匹配前面的字符0次或1次（贪婪匹配） | `a?` 匹配 "" 或 "a" |
| `{n}` | 匹配前面的字符恰好n次 | `a{3}` 匹配 "aaa" |
| `{n,}` | 匹配前面的字符至少n次（贪婪匹配） | `a{2,}` 匹配 "aa"、"aaa"、"aaaa" 等 |
| `{n,m}` | 匹配前面的字符至少n次，最多m次（贪婪匹配） | `a{1,3}` 匹配 "a"、"aa"、"aaa" |
| `*?`, `+?`, `??`, `{n}?`, `{n,}?`, `{n,m}?` | 非贪婪匹配，匹配尽可能少的字符 | `a*?` 匹配尽可能少的 "a" |
| `\` | 转义字符，用于匹配特殊字符本身 | `\.` 匹配点号，`\*` 匹配星号 |
| `[]` | 字符类，匹配方括号中的任意一个字符 | `[abc]` 匹配 "a"、"b" 或 "c" |
| `[^]` | 否定字符类，匹配不在方括号中的任意一个字符 | `[^abc]` 匹配除 "a"、"b"、"c" 以外的任意字符 |
| `|` | 或操作符，匹配两个表达式中的任意一个 | `a|b` 匹配 "a" 或 "b" |
| `()` | 分组，将括号内的表达式作为一个整体 | `(ab)+` 匹配 "ab"、"abab"、"ababab" 等 |
| `(?:)` | 非捕获分组，匹配但不捕获分组内容 | `(?:ab)+` 匹配 "ab"、"abab" 等，但不捕获 "ab" |
| `(?=)` | 正向预查，匹配后面跟着特定内容的位置 | `a(?=b)` 匹配后面跟着 "b" 的 "a" |
| `(?!` | 负向预查，匹配后面不跟着特定内容的位置 | `a(?!b)` 匹配后面不跟着 "b" 的 "a" |
| `(?<=)` | 正向后顾，匹配前面跟着特定内容的位置 | `(?<=b)a` 匹配前面跟着 "b" 的 "a" |
| `(?<!` | 负向后顾，匹配前面不跟着特定内容的位置 | `(?<!b)a` 匹配前面不跟着 "b" 的 "a" |

## 字符类

字符类用于匹配一组字符中的任意一个字符，可以使用方括号`[]`来定义。

### 基本字符类

```python
[abc]      # 匹配 "a"、"b" 或 "c"
[^abc]     # 匹配除 "a"、"b"、"c" 以外的任意字符
[a-z]      # 匹配小写字母
[A-Z]      # 匹配大写字母
[0-9]      # 匹配数字
[a-zA-Z]   # 匹配字母
[a-zA-Z0-9] # 匹配字母和数字
```

### 预定义字符类

Python的re模块提供了一些预定义的字符类，用于匹配常见的字符类型：

| 预定义字符类 | 描述 | 等价于 |
|-------------|------|--------|
| `\d` | 匹配任意数字 | `[0-9]` |
| `\D` | 匹配任意非数字 | `[^0-9]` |
| `\s` | 匹配任意空白字符（空格、制表符、换行符等） | `[ \t\n\r\f\v]` |
| `\S` | 匹配任意非空白字符 | `[^ \t\n\r\f\v]` |
| `\w` | 匹配任意字母、数字或下划线 | `[a-zA-Z0-9_]` |
| `\W` | 匹配任意非字母、数字或下划线 | `[^a-zA-Z0-9_]` |
| `\b` | 匹配单词边界 | 无 |
| `\B` | 匹配非单词边界 | 无 |

## 数量词

数量词用于指定前面的字符或分组的匹配次数：

| 数量词 | 描述 | 示例 |
|-------|------|------|
| `*` | 匹配0次或多次（贪婪匹配） | `a*` 匹配 ""、"a"、"aa"、"aaa" 等 |
| `+` | 匹配1次或多次（贪婪匹配） | `a+` 匹配 "a"、"aa"、"aaa" 等 |
| `?` | 匹配0次或1次（贪婪匹配） | `a?` 匹配 "" 或 "a" |
| `{n}` | 匹配恰好n次 | `a{3}` 匹配 "aaa" |
| `{n,}` | 匹配至少n次（贪婪匹配） | `a{2,}` 匹配 "aa"、"aaa"、"aaaa" 等 |
| `{n,m}` | 匹配至少n次，最多m次（贪婪匹配） | `a{1,3}` 匹配 "a"、"aa"、"aaa" |

### 贪婪匹配与非贪婪匹配

默认情况下，数量词是贪婪的，尽可能匹配更多的字符。在数量词后面加上`?`可以实现非贪婪匹配，尽可能匹配更少的字符：

| 贪婪匹配 | 非贪婪匹配 | 描述 |
|---------|-----------|------|
| `*` | `*?` | 匹配0次或多次，尽可能少 |
| `+` | `+?` | 匹配1次或多次，尽可能少 |
| `?` | `??` | 匹配0次或1次，尽可能少 |
| `{n,}` | `{n,}?` | 匹配至少n次，尽可能少 |
| `{n,m}` | `{n,m}?` | 匹配至少n次，最多m次，尽可能少 |

## 边界匹配

边界匹配用于匹配字符串的边界位置：

| 边界匹配 | 描述 | 示例 |
|---------|------|------|
| `^` | 匹配字符串的开头 | `^abc` 匹配以 "abc" 开头的字符串 |
| `$` | 匹配字符串的结尾 | `abc$` 匹配以 "abc" 结尾的字符串 |
| `\b` | 匹配单词边界 | `\bword\b` 匹配完整的单词 "word" |
| `\B` | 匹配非单词边界 | `\Bword\B` 匹配不在单词边界的 "word" |

## 分组

分组用于将多个字符作为一个整体处理，可以使用圆括号`()`来定义：

### 捕获分组

捕获分组用于匹配并捕获分组的内容，可以通过索引或名称来引用：

```python
(abc)      # 捕获分组，匹配 "abc" 并捕获
(a|b)      # 捕获分组，匹配 "a" 或 "b" 并捕获
(a(bc))    # 嵌套分组，捕获 "a(bc)" 和 "bc"
```

### 命名分组

命名分组用于给分组命名，便于后续引用，可以使用`(?P<name>...)`来定义：

```python
(?P<year>\d{4})    # 命名分组 "year"，匹配4位数字
(?P<month>\d{2})   # 命名分组 "month"，匹配2位数字
(?P<day>\d{2})     # 命名分组 "day"，匹配2位数字
```

### 非捕获分组

非捕获分组用于匹配但不捕获分组的内容，可以使用`(?:...)`来定义：

```python
(?:abc)    # 非捕获分组，匹配 "abc" 但不捕获
(?:a|b)    # 非捕获分组，匹配 "a" 或 "b" 但不捕获
```

## 预查

预查用于匹配特定位置前面或后面的内容，但不包含该内容：

### 正向预查

正向预查用于匹配后面跟着特定内容的位置，可以使用`(?=...)`来定义：

```python
\d+(?=%)    # 匹配后面跟着 "%" 的数字
\w+(?=\s+\w+)    # 匹配后面跟着另一个单词的单词
```

### 负向预查

负向预查用于匹配后面不跟着特定内容的位置，可以使用`(?!...)`来定义：

```python
\d+(?!%)    # 匹配后面不跟着 "%" 的数字
\w+(?!\s+\w+)    # 匹配后面不跟着另一个单词的单词
```

### 正向后顾

正向后顾用于匹配前面跟着特定内容的位置，可以使用`(?<=...)`来定义：

```python
(?<=\$)\d+    # 匹配前面跟着 "$" 的数字
(?<=https?)://    # 匹配前面跟着 "http://" 或 "https://" 的 ":/"
```

### 负向后顾

负向后顾用于匹配前面不跟着特定内容的位置，可以使用`(?<!...)`来定义：

```python
(?<!\$)\d+    # 匹配前面不跟着 "$" 的数字
(?<!https?)://    # 匹配前面不跟着 "http://" 或 "https://" 的 ":/"
```

## 回溯引用

回溯引用用于引用之前捕获的分组内容，可以使用`\1`、`\2`等或命名分组的名称来引用：

### 数字回溯引用

使用`\1`、`\2`等引用之前的捕获分组：

```python
(\w+)\s+\1    # 匹配重复的单词，如 "hello hello"
(\d{2})/(\d{2})/(\d{4})\s+\2/\1/\3    # 匹配日期格式转换，如 "12/01/2023 01/12/2023"
```

### 命名回溯引用

使用`(?P=name)`引用之前的命名分组：

```python
(?P<word>\w+)\s+(?P=word)    # 匹配重复的单词，如 "hello hello"
```

## 修饰符

修饰符用于改变正则表达式的匹配行为，可以在编译正则表达式时指定：

| 修饰符 | 描述 | 简写 |
|-------|------|------|
| re.IGNORECASE | 忽略大小写 | re.I |
| re.MULTILINE | 多行模式，^和$匹配每行的开头和结尾 | re.M |
| re.DOTALL | 点号匹配包括换行符在内的所有字符 | re.S |
| re.VERBOSE | 详细模式，允许正则表达式包含注释和空格 | re.X |
| re.ASCII | 仅ASCII模式，\w、\W、\b、\B、\d、\D、\s、\S仅匹配ASCII字符 | re.A |
| re.UNICODE | Unicode模式，\w、\W、\b、\B、\d、\D、\s、\S匹配Unicode字符 | re.U |
| re.LOCALE | 本地化模式，\w、\W、\b、\B依赖于当前区域设置 | re.L |

## 正则表达式语法示例

### 基础语法示例

```python
import re

# 匹配数字
pattern = re.compile(r'\d+')
result = pattern.findall('123 abc 456 def 789')
print(f"匹配数字: {result}")  # ['123', '456', '789']

# 匹配单词
pattern = re.compile(r'\w+')
result = pattern.findall('hello world! 你好，世界！')
print(f"匹配单词: {result}")  # ['hello', 'world', '你好', '世界']

# 匹配邮箱
pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
result = pattern.findall('联系我：test@example.com 或 admin@sub.example.com')
print(f"匹配邮箱: {result}")  # ['test@example.com', 'admin@sub.example.com']

# 匹配URL
pattern = re.compile(r'https?://[\w\-]+(\.[\w\-]+)+([\w\-.,@?^=%&:/~\+#]*[\w\-@?^=%&/~\+#])?')
result = pattern.findall('访问：https://www.example.com 或 http://sub.example.com/path?param=value')
print(f"匹配URL: {[url[0] + url[1] for url in result]}")  # ['https://www.example.com', 'http://sub.example.com/path?param=value']
```

### 高级语法示例

```python
import re

# 贪婪匹配与非贪婪匹配
pattern1 = re.compile(r'<.*>')  # 贪婪匹配
pattern2 = re.compile(r'<.*?>')  # 非贪婪匹配
result1 = pattern1.match('<div>content</div>').group()
result2 = pattern2.match('<div>content</div>').group()
print(f"贪婪匹配: {result1}")  # <div>content</div>
print(f"非贪婪匹配: {result2}")  # <div>

# 分组与命名分组
pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')
match = pattern.match('2023-12-01')
print(f"完整匹配: {match.group()}")  # 2023-12-01
print(f"年份: {match.group('year')}")  # 2023
print(f"月份: {match.group('month')}")  # 12
print(f"日期: {match.group('day')}")  # 01

# 预查
pattern = re.compile(r'\d+(?=%)')  # 正向预查，匹配后面跟着%的数字
result = pattern.findall('价格: 100% 折扣: 20% 税率: 5%')
print(f"正向预查: {result}")  # ['100', '20', '5']

# 回溯引用
pattern = re.compile(r'(\w+)\s+\1')  # 匹配重复的单词
result = pattern.findall('hello hello world world test')
print(f"回溯引用: {result}")  # ['hello', 'world']
```

## 正则表达式常见模式

### 数据验证

```python
import re

# 邮箱验证
def validate_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

# 电话号码验证
def validate_phone(phone):
    pattern = re.compile(r'^1[3-9]\d{9}$')
    return bool(pattern.match(phone))

# 身份证号码验证
def validate_id_card(id_card):
    pattern = re.compile(r'^[1-9]\d{5}(18|19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}[\dXx]$')
    return bool(pattern.match(id_card))

# 密码强度验证
def validate_password(password):
    # 至少包含一个大写字母、一个小写字母、一个数字和一个特殊字符，长度至少8位
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(pattern.match(password))

# IP地址验证
def validate_ip(ip):
    pattern = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    return bool(pattern.match(ip))
```

### 数据提取

```python
import re

# 提取HTML标签内容
def extract_html_content(html):
    pattern = re.compile(r'<.*?>(.*?)</.*?>', re.DOTALL)
    return pattern.findall(html)

# 提取URL中的域名
def extract_domain(url):
    pattern = re.compile(r'https?://(?:www\.)?([\w\-]+\.[\w\-]+)')
    match = pattern.match(url)
    return match.group(1) if match else None

# 提取日志中的时间戳
def extract_timestamp(log_line):
    pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
    match = pattern.match(log_line)
    return match.group(1) if match else None

# 提取文本中的数字
def extract_numbers(text):
    pattern = re.compile(r'\d+\.?\d*')
    return pattern.findall(text)

# 提取文本中的中文
def extract_chinese(text):
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    return pattern.findall(text)
```

### 数据清洗

```python
import re

# 移除HTML标签
def remove_html_tags(text):
    pattern = re.compile(r'<.*?>')
    return pattern.sub('', text)

# 移除特殊字符
def remove_special_chars(text):
    pattern = re.compile(r'[^\w\s\u4e00-\u9fa5]')
    return pattern.sub('', text)

# 移除多余的空格
def remove_extra_spaces(text):
    pattern = re.compile(r'\s+')
    return pattern.sub(' ', text).strip()

# 标准化日期格式
def standardize_date(date):
    # 将各种日期格式转换为YYYY-MM-DD格式
    patterns = [
        (r'(\d{4})/(\d{2})/(\d{2})', r'\1-\2-\3'),
        (r'(\d{2})/(\d{2})/(\d{4})', r'\3-\1-\2'),
        (r'(\d{4})\.(\d{2})\.(\d{2})', r'\1-\2-\3'),
        (r'(\d{2})\.(\d{2})\.(\d{4})', r'\3-\1-\2'),
        (r'(\d{4})(\d{2})(\d{2})', r'\1-\2-\3')
    ]
    
    standardized_date = date
    for pattern, replacement in patterns:
        standardized_date = re.sub(pattern, replacement, standardized_date)
    
    return standardized_date
```

## 正则表达式性能优化

1. **编译正则表达式**：对于频繁使用的正则表达式，应该使用`re.compile()`编译为模式对象，提高匹配效率

```python
# 推荐
pattern = re.compile(r'\d+')
for text in texts:
    pattern.match(text)

# 不推荐
for text in texts:
    re.match(r'\d+', text)
```

2. **使用更具体的模式**：避免使用过于宽泛的模式，如`.*`，这会导致回溯过多，降低性能

```python
# 推荐
pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

# 不推荐
pattern = re.compile(r'.*@.*\..*')
```

3. **使用非贪婪匹配**：在不需要贪婪匹配的情况下，使用非贪婪匹配可以减少回溯

```python
# 推荐
pattern = re.compile(r'<.*?>')  # 非贪婪匹配

# 不推荐
pattern = re.compile(r'<.*>')  # 贪婪匹配（在复杂HTML中可能导致性能问题）
```

4. **使用预查代替捕获**：对于不需要提取的内容，使用预查可以提高性能

```python
# 推荐
pattern = re.compile(r'\d+(?=%)')  # 正向预查

# 不推荐
pattern = re.compile(r'\d+%')  # 捕获整个匹配项，然后处理
```

5. **使用边界匹配**：使用`^`、`$`、`\b`等边界匹配可以减少不必要的匹配尝试

```python
# 推荐
pattern = re.compile(r'^\d+$')  # 匹配整个字符串是数字

# 不推荐
pattern = re.compile(r'\d+')  # 匹配字符串中的数字，然后检查是否整个字符串匹配
```

6. **避免嵌套量词**：嵌套量词会导致指数级的回溯，应尽量避免

```python
# 避免
pattern = re.compile(r'(a*)*')  # 嵌套量词，可能导致性能问题

# 推荐
pattern = re.compile(r'a*')  # 简单量词
```

7. **使用字符类代替分支**：对于单个字符的匹配，使用字符类比分支更高效

```python
# 推荐
pattern = re.compile(r'[abc]')  # 字符类

# 不推荐
pattern = re.compile(r'a|b|c')  # 分支
```

## 正则表达式调试

Python的re模块提供了`re.DEBUG`修饰符，可以用于调试正则表达式：

```python
import re

pattern = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', re.DEBUG)
```

运行上述代码，会输出正则表达式的解析过程：

```
group name='year'
  DIGIT
    repetition 4 times
literal 45
literal 45
literal 45
```

## 总结

正则表达式是一种强大的文本处理工具，Python的re模块提供了完整的正则表达式支持。本文件详细介绍了正则表达式的各种语法元素，包括基本元字符、字符类、数量词、边界匹配、分组、预查、回溯引用等。

掌握正则表达式的语法对于Python开发者来说是非常重要的，可以帮助开发者更高效地处理文本数据，提高开发效率。在实际应用中，应根据具体需求选择合适的正则表达式语法，并注意性能优化和调试。