# re模块 - 正则表达式操作
# 功能作用：提供正则表达式的匹配、搜索、替换等功能
# 使用情景：文本搜索、文本替换、数据验证、信息提取等
# 注意事项：正则表达式的性能与表达式复杂度密切相关，需要注意效率和可读性

import re

# 模块概述
"""
re模块提供了与正则表达式相关的功能，主要包括：
- 匹配和搜索功能（match, search, findall等）
- 替换功能（sub, subn）
- 分割功能（split）
- 编译正则表达式（compile）
- 其他辅助功能

正则表达式是一种用于匹配字符串模式的工具，具有强大的文本处理能力。
"""

# 1. 基本匹配函数
print("=== 基本匹配函数 ===")

# re.match - 从字符串开头匹配
text = "Hello, World!"
match_result = re.match(r'Hello', text)
if match_result:
    print(f"match匹配成功: {match_result.group()}")
else:
    print("match匹配失败")

# 尝试匹配不在开头的模式
match_result = re.match(r'World', text)
if match_result:
    print(f"match匹配成功: {match_result.group()}")
else:
    print("match匹配失败（World不在开头）")

# re.search - 搜索整个字符串中的第一个匹配
search_result = re.search(r'World', text)
if search_result:
    print(f"search匹配成功: {search_result.group()}")
    print(f"匹配位置: {search_result.start()}-{search_result.end()}")
else:
    print("search匹配失败")

# re.findall - 查找所有匹配
text = "apple, banana, apple, orange"
all_matches = re.findall(r'apple', text)
print(f"findall匹配结果: {all_matches}")
print(f"匹配数量: {len(all_matches)}")

# re.finditer - 返回匹配对象的迭代器
for match in re.finditer(r'apple', text):
    print(f"finditer匹配: {match.group()} 在位置 {match.start()}")
print()

# 2. 正则表达式模式语法
def demonstrate_pattern_syntax():
    """演示正则表达式模式语法"""
    print("=== 正则表达式模式语法 ===")
    
    # 字符匹配
    print("字符匹配:")
    pattern = r'abc'
    text1 = "abc123"
    text2 = "a1b2c3"
    print(f"模式 '{pattern}' 在 '{text1}' 中匹配: {bool(re.search(pattern, text1))}")
    print(f"模式 '{pattern}' 在 '{text2}' 中匹配: {bool(re.search(pattern, text2))}")
    
    # 字符类
    print("\n字符类:")
    pattern = r'[aeiou]'  # 匹配任何一个元音字母
    text = "Hello World!"
    vowels = re.findall(pattern, text, re.IGNORECASE)  # 忽略大小写
    print(f"文本中的元音字母: {vowels}")
    
    # 否定字符类
    pattern = r'[^aeiou]'  # 匹配任何非元音字母
    consonants = re.findall(pattern, text, re.IGNORECASE)
    print(f"文本中的非元音字符: {consonants}")
    
    # 预定义字符类
    print("\n预定义字符类:")
    text = "Hello123!\nWorld"
    print(f"原始文本: {repr(text)}")
    print(f"所有数字: {re.findall(r'\\d', text)}")  # 数字
    print(f"所有非数字: {re.findall(r'\\D', text)}")  # 非数字
    print(f"所有空白字符: {re.findall(r'\\s', text)}")  # 空白字符
    print(f"所有非空白字符: {re.findall(r'\\S', text)}")  # 非空白字符
    print(f"所有单词字符: {re.findall(r'\\w', text)}")  # 单词字符
    print(f"所有非单词字符: {re.findall(r'\\W', text)}")  # 非单词字符
    
    # 量词
    print("\n量词:")
    text = "aaaabbbbcccc"
    print(f"原始文本: {text}")
    print(f"a+: {re.findall(r'a+', text)}")  # 一个或多个a
    print(f"b*: {re.findall(r'b*', text)}")  # 零个或多个b
    print(f"c?: {re.findall(r'c?', text)}")  # 零个或一个c
    print(f"a{3}: {re.findall(r'a{3}', text)}")  # 正好3个a
    print(f"a{2,4}: {re.findall(r'a{2,4}', text)}")  # 2到4个a
    print(f"a{2,}: {re.findall(r'a{2,}', text)}")  # 至少2个a
    
    # 边界匹配
    print("\n边界匹配:")
    text = "Hello World"
    print(f"^Hello: {bool(re.search(r'^Hello', text))}")  # 以Hello开头
    print(f"World$: {bool(re.search(r'World$', text))}")  # 以World结尾
    print(f"\bWorld\b: {bool(re.search(r'\\bWorld\\b', text))}")  # 单词边界
    print(f"\bWor: {bool(re.search(r'\\bWor', text))}")  # 单词边界
    
    # 分组
    print("\n分组:")
    text = "John Smith (30 years old)"
    pattern = r'(\\w+) (\\w+) \((\\d+) years old\)'
    match = re.search(pattern, text)
    if match:
        print(f"完整匹配: {match.group()}")
        print(f"第一个分组 (名): {match.group(1)}")
        print(f"第二个分组 (姓): {match.group(2)}")
        print(f"第三个分组 (年龄): {match.group(3)}")
        print(f"所有分组: {match.groups()}")
    
    # 非捕获分组
    pattern = r'(\\w+) (\\w+) \((?:\\d+) years old\)'
    match = re.search(pattern, text)
    if match:
        print(f"\n使用非捕获分组后的所有分组: {match.groups()}")
    
    # 命名分组
    pattern = r'(?P<first>\\w+) (?P<last>\\w+) \((?P<age>\\d+) years old\)'
    match = re.search(pattern, text)
    if match:
        print(f"\n使用命名分组:")
        print(f"通过名称获取first: {match.group('first')}")
        print(f"通过名称获取age: {match.group('age')}")
        print(f"所有命名分组: {match.groupdict()}")
    print()

# 3. 编译正则表达式
def demonstrate_compilation():
    """演示编译正则表达式"""
    print("=== 编译正则表达式 ===")
    
    # 编译正则表达式模式
    pattern = re.compile(r'\\d+')
    text = "There are 123 apples and 456 oranges."
    
    # 使用编译后的模式
    print(f"findall: {pattern.findall(text)}")
    
    match = pattern.search(text)
    if match:
        print(f"search: {match.group()}")
    
    # 编译时设置标志
    pattern_case_insensitive = re.compile(r'hello', re.IGNORECASE)
    text = "HELLO World!"
    print(f"不区分大小写匹配: {bool(pattern_case_insensitive.search(text))}")
    
    # 多行模式
    text = "Line 1:\nhello\nLine 3:\nworld"
    pattern_multiline = re.compile(r'^hello', re.MULTILINE)
    print(f"多行模式匹配: {bool(pattern_multiline.search(text))}")
    
    # DOTALL模式（让.匹配换行符）
    text = "Start\nMiddle\nEnd"
    pattern_dotall = re.compile(r'Start.*End', re.DOTALL)
    print(f"DOTALL模式匹配: {bool(pattern_dotall.search(text))}")
    
    # 组合标志
    pattern_combined = re.compile(r'^hello.*world$', re.MULTILINE | re.DOTALL | re.IGNORECASE)
    print(f"组合标志编译: {pattern_combined.flags}")
    print()

# 4. 替换功能
def demonstrate_replacement():
    """演示替换功能"""
    print("=== 替换功能 ===")
    
    # re.sub - 替换匹配的文本
    text = "Hello, World! Hello, Python!"
    new_text = re.sub(r'Hello', 'Hi', text)
    print(f"原始文本: {text}")
    print(f"替换后: {new_text}")
    
    # 限制替换次数
    new_text_limit = re.sub(r'Hello', 'Hi', text, count=1)
    print(f"只替换第一个: {new_text_limit}")
    
    # 使用函数进行替换
    def replace_with_length(match):
        word = match.group()
        return str(len(word))
    
    text_with_numbers = re.sub(r'\\w+', replace_with_length, text)
    print(f"用单词长度替换: {text_with_numbers}")
    
    # 使用捕获组进行替换
    text = "John Smith"
    new_text = re.sub(r'(\\w+) (\\w+)', r'\\2, \\1', text)  # 交换名和姓
    print(f"交换名和姓: {new_text}")
    
    # 使用命名捕获组进行替换
    new_text_named = re.sub(r'(?P<first>\\w+) (?P<last>\\w+)', r'\\g<last>, \\g<first>', text)
    print(f"使用命名组交换: {new_text_named}")
    
    # re.subn - 返回替换后的文本和替换次数
    text = "apple banana apple orange apple"
    new_text, count = re.subn(r'apple', 'fruit', text)
    print(f"\n替换统计:")
    print(f"替换后文本: {new_text}")
    print(f"替换次数: {count}")
    print()

# 5. 分割功能
def demonstrate_split():
    """演示分割功能"""
    print("=== 分割功能 ===")
    
    # 基本分割
    text = "apple,banana,orange,grape"
    fruits = re.split(r',', text)
    print(f"原始文本: {text}")
    print(f"分割结果: {fruits}")
    
    # 使用多个分隔符
    text = "apple, banana; orange grape"
    fruits = re.split(r'[,;\\s]+', text)
    print(f"\n多个分隔符分割:")
    print(f"原始文本: {text}")
    print(f"分割结果: {fruits}")
    
    # 限制分割次数
    fruits_limited = re.split(r'[,;\\s]+', text, maxsplit=2)
    print(f"限制分割次数为2: {fruits_limited}")
    
    # 保留分隔符（使用捕获组）
    text = "Section 1: Introduction\nSection 2: Methods\nSection 3: Results"
    parts = re.split(r'(Section \\d+:)', text)
    print(f"\n保留分隔符:")
    print(f"原始文本:\n{text}")
    print(f"分割结果: {parts}")
    
    # 使用编译后的模式分割
    pattern = re.compile(r'\\s+')
    text = "Hello   World    Python"
    words = pattern.split(text)
    print(f"\n使用编译模式分割空白:")
    print(f"原始文本: {repr(text)}")
    print(f"分割结果: {words}")
    print()

# 6. 实际应用示例
def practical_examples():
    """演示实际应用示例"""
    print("=== 实际应用示例 ===")
    
    # 1. 电子邮件验证
    def validate_email(email):
        """验证电子邮件地址格式"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    emails = [
        "user@example.com",  # 有效
        "first.last@domain.co.uk",  # 有效
        "user@localhost",  # 无效（顶级域名太短）
        "user@-domain.com",  # 无效（域名不能以-开头）
        "user@domain..com",  # 无效（连续点）
        "user@.com"  # 无效（缺少域名）
    ]
    
    print("电子邮件验证:")
    for email in emails:
        print(f"{email}: {'有效' if validate_email(email) else '无效'}")
    
    # 2. 提取URL中的域名
    def extract_domain(url):
        """从URL中提取域名"""
        pattern = r'^(?:https?://)?(?:www\\.)?([a-zA-Z0-9.-]+)'
        match = re.match(pattern, url)
        return match.group(1) if match else None
    
    urls = [
        "https://www.example.com/path",
        "http://example.org",
        "www.test-site.net",
        "ftp://ftp.server.com"
    ]
    
    print("\n提取域名:")
    for url in urls:
        domain = extract_domain(url)
        print(f"URL: {url} -> 域名: {domain}")
    
    # 3. 从文本中提取电话号码（简单示例）
    def extract_phone_numbers(text):
        """从文本中提取电话号码"""
        pattern = r'\\b\\d{3}[-.\\s]?\\d{3}[-.\\s]?\\d{4}\\b'
        return re.findall(pattern, text)
    
    text = "请联系我们：123-456-7890 或 (987) 654-3210，也可以发送邮件到info@example.com"
    phones = extract_phone_numbers(text)
    print("\n提取电话号码:")
    print(f"原始文本: {text}")
    print(f"提取的电话号码: {phones}")
    
    # 4. 清理HTML标签
    def remove_html_tags(text):
        """移除文本中的HTML标签"""
        pattern = r'<[^>]+>'
        return re.sub(pattern, '', text)
    
    html_text = "<p>这是一个<strong>HTML</strong>示例文本。<a href='https://example.com'>链接</a></p>"
    clean_text = remove_html_tags(html_text)
    print("\n清理HTML标签:")
    print(f"原始HTML: {html_text}")
    print(f"清理后: {clean_text}")
    
    # 5. 驼峰命名法转下划线命名法
    def camel_to_snake(name):
        """将驼峰命名法转换为下划线命名法"""
        # 在大写字母前添加下划线（除了第一个字符）
        name = re.sub(r'(?<!^)(?=[A-Z])', '_', name)
        return name.lower()
    
    camel_names = ["camelCase", "PascalCase", "HTMLParser", "getHTTPResponse"]
    print("\n驼峰命名法转下划线命名法:")
    for name in camel_names:
        print(f"{name} -> {camel_to_snake(name)}")
    print()

# 7. 高级正则表达式技术
def advanced_techniques():
    """演示高级正则表达式技术"""
    print("=== 高级正则表达式技术 ===")
    
    # 1. 正向先行断言和负向先行断言
    print("先行断言:")
    text = "apple applepie appletree"
    
    # 匹配后面跟pie的apple
    pattern = r'apple(?=pie)'
    matches = re.findall(pattern, text)
    print(f"匹配后面跟pie的apple: {matches}")
    
    # 匹配后面不跟pie的apple
    pattern = r'apple(?!pie)'
    matches = re.findall(pattern, text)
    print(f"匹配后面不跟pie的apple: {matches}")
    
    # 2. 正向后行断言和负向后行断言（Python 3.5+）
    print("\n后行断言:")
    text = "Python 2.7 Python 3.10 Python 3.9"
    
    # 匹配前面是Python的数字
    pattern = r'(?<=Python )\\d+\\.\\d+'
    matches = re.findall(pattern, text)
    print(f"匹配前面是Python的版本号: {matches}")
    
    # 匹配前面不是Python 3的数字
    pattern = r'(?<!Python 3\\.)\\d+'
    matches = re.findall(pattern, text)
    print(f"匹配前面不是Python 3.的数字: {matches}")
    
    # 3. 贪婪与非贪婪匹配
    print("\n贪婪与非贪婪匹配:")
    text = "<tag>content1</tag><tag>content2</tag>"
    
    # 贪婪匹配（默认）
    pattern_greedy = r'<tag>.*</tag>'
    match_greedy = re.search(pattern_greedy, text)
    print(f"贪婪匹配: {match_greedy.group() if match_greedy else '无匹配'}")
    
    # 非贪婪匹配
    pattern_non_greedy = r'<tag>.*?</tag>'
    matches_non_greedy = re.findall(pattern_non_greedy, text)
    print(f"非贪婪匹配: {matches_non_greedy}")
    
    # 4. 回溯控制
    print("\n回溯控制:")
    text = "aaaaa"
    
    # 使用原子组（Python不直接支持，但可以使用占有量词模拟）
    # 占有量词不支持，这里演示普通量词
    pattern = r'(a+)(a+)'  # 可能导致回溯
    match = re.search(pattern, text)
    if match:
        print(f"分组1: {match.group(1)}, 分组2: {match.group(2)}")
    
    # 5. 递归模式（Python不直接支持，但可以使用re模块的一些技巧）
    print("\n递归模式（有限支持）:")
    # 简单的括号匹配示例（不能处理嵌套括号）
    text = "(a + b) * (c - d)"
    pattern = r'\\([^()]*)\\)'
    matches = re.findall(pattern, text)
    print(f"括号内容: {matches}")
    print()

# 8. 性能优化和注意事项
"""
1. **编译正则表达式**：
   - 对于重复使用的正则表达式，使用re.compile()预编译以提高性能
   - 预编译的正则表达式会被缓存，但显式编译更清晰且效率更高

2. **避免回溯**：
   - 复杂的正则表达式可能导致大量回溯，影响性能
   - 使用非贪婪量词、占有量词（如果支持）和原子组减少回溯

3. **具体优于模糊**：
   - 使用具体的模式而非过于宽泛的模式
   - 例如：使用\\d+而不是.+来匹配数字

4. **避免过度使用正则**：
   - 对于简单的字符串操作，使用字符串方法（如str.replace()）更高效
   - 正则表达式适合复杂的模式匹配

5. **注意转义**：
   - 在字符串中使用反斜杠需要适当转义（或使用原始字符串r""）
   - 特殊字符（如. ^ $ * + ? {} [] \ | ( )）需要转义

6. **测试和调试**：
   - 使用在线工具（如regex101.com）测试正则表达式
   - 使用re.DEBUG标志帮助理解正则表达式的执行

7. **安全考虑**：
   - 避免使用用户提供的正则表达式（可能导致ReDoS攻击）
   - 限制正则表达式的执行时间
"""

def demonstrate_performance_tips():
    """演示性能优化技巧"""
    print("=== 性能优化和最佳实践 ===")
    
    # 1. 编译正则表达式的性能对比
    import time
    
    pattern_str = r'\\d+'
    text = "Sample text with numbers 123, 456, and 789." * 1000
    iterations = 1000
    
    print("编译vs非编译性能对比:")
    
    # 不编译
    start = time.time()
    for _ in range(iterations):
        re.findall(pattern_str, text)
    time_without_compile = time.time() - start
    print(f"不编译: {time_without_compile:.6f}秒")
    
    # 编译
    compiled_pattern = re.compile(pattern_str)
    start = time.time()
    for _ in range(iterations):
        compiled_pattern.findall(text)
    time_with_compile = time.time() - start
    print(f"编译: {time_with_compile:.6f}秒")
    print(f"编译后的性能提升: {(time_without_compile/time_with_compile):.2f}倍")
    
    # 2. 避免回溯的模式对比
    print("\n避免回溯的模式对比:")
    
    # 可能导致回溯的模式
    backtracking_pattern = r'(a+)(a+)(a+)'  # 多个贪婪量词可能导致回溯
    optimized_pattern = r'(a+)(a+)(a+)'  # 这里只是示例，实际优化需要具体分析
    complex_text = "a" * 1000
    
    # 3. 使用具体模式而非模糊模式
    print("\n具体模式vs模糊模式:")
    text = "User ID: 12345, Name: John, Age: 30"
    
    # 使用模糊模式
    vague_pattern = r'ID: (.+),'
    vague_match = re.search(vague_pattern, text)
    if vague_match:
        print(f"模糊模式匹配: {vague_match.group(1)}")
    
    # 使用具体模式
    specific_pattern = r'ID: (\\d+),'  # 只匹配数字
    specific_match = re.search(specific_pattern, text)
    if specific_match:
        print(f"具体模式匹配: {specific_match.group(1)}")
    
    # 4. 简单字符串操作vs正则表达式
    print("\n简单字符串操作vs正则表达式:")
    text = "Hello, World! Hello, Python!"
    
    # 使用字符串方法
    start = time.time()
    for _ in range(iterations):
        text.replace("Hello", "Hi")
    time_str_method = time.time() - start
    print(f"字符串replace方法: {time_str_method:.6f}秒")
    
    # 使用正则表达式
    replace_pattern = re.compile(r'Hello')
    start = time.time()
    for _ in range(iterations):
        replace_pattern.sub("Hi", text)
    time_regex = time.time() - start
    print(f"正则表达式sub方法: {time_regex:.6f}秒")
    print(f"简单替换时字符串方法更快: {(time_regex/time_str_method):.2f}倍")
    
    # 5. 使用re.DEBUG标志
    print("\n使用re.DEBUG标志:")
    # 注意：这里只是展示如何使用，实际输出会很长
    # re.compile(r'\\d+', re.DEBUG)
    print("re.compile(pattern, re.DEBUG) 会显示正则表达式的详细执行计划")
    print()

# 运行演示代码
if __name__ == "__main__":
    print("Python re模块演示\n")
    
    demonstrate_pattern_syntax()
    demonstrate_compilation()
    demonstrate_replacement()
    demonstrate_split()
    practical_examples()
    advanced_techniques()
    demonstrate_performance_tips()
    
    print("演示完成！")