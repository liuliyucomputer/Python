# string模块 - 字符串操作工具
# 功能作用：提供各种字符串常量和用于处理字符串的工具函数
# 使用情景：字符串分析、格式化、处理和操作
# 注意事项：string模块中的大部分函数已被字符串方法取代，但常量和某些工具函数仍有用

import string

# 模块概述
"""
string模块提供了与字符串处理相关的常量和函数，主要包括：
- 预定义的字符串常量（如字母、数字、标点符号等）
- 用于字符串格式化的模板类
- 字符分类函数（如判断字符是否为字母、数字等）
- 其他字符串工具函数

虽然Python的字符串类型(str)已经提供了丰富的方法，但string模块的常量和某些功能在特定场景下仍然非常有用。
"""

# 1. 字符串常量
print("=== 字符串常量 ===")

# 所有ASCII字母（小写）
print(f"string.ascii_lowercase: {string.ascii_lowercase}")

# 所有ASCII字母（大写）
print(f"string.ascii_uppercase: {string.ascii_uppercase}")

# 所有ASCII字母（小写+大写）
print(f"string.ascii_letters: {string.ascii_letters}")

# 所有ASCII数字
print(f"string.digits: {string.digits}")

# 所有ASCII标点符号
print(f"string.punctuation: {string.punctuation}")

# 所有ASCII可打印字符
print(f"string.printable: {string.printable}")

# 所有ASCII空白字符
print(f"string.whitespace: {repr(string.whitespace)}")
print()

# 2. 字符分类函数
def demonstrate_character_classification():
    """演示字符分类函数"""
    print("=== 字符分类函数 ===")
    
    # 注意：这些函数在Python 3中已移至str类型的方法，但为了完整性仍然展示
    
    test_chars = ['a', 'Z', '5', '!', ' ', '\t', '\n', '你']
    
    print("字符分类示例:")
    for char in test_chars:
        print(f"字符 '{char}':")
        print(f"  isalnum: {char.isalnum()}")  # 是否为字母或数字
        print(f"  isalpha: {char.isalpha()}")  # 是否为字母
        print(f"  isdigit: {char.isdigit()}")  # 是否为数字
        print(f"  islower: {char.islower()}")  # 是否为小写
        print(f"  isupper: {char.isupper()}")  # 是否为大写
        print(f"  isspace: {char.isspace()}")  # 是否为空白字符
        print(f"  isprintable: {char.isprintable()}")  # 是否为可打印字符
        print(f"  isascii: {char.isascii()}")  # 是否为ASCII字符（Python 3.7+）
        print()
    
    # 注意：Python 3中，string模块不再提供isdigit等函数，而是使用字符串方法
    # 下面是如何使用string常量进行字符检查
    print("使用string常量进行字符检查:")
    for char in test_chars:
        print(f"字符 '{char}':")
        print(f"  小写字母: {char in string.ascii_lowercase}")
        print(f"  大写字母: {char in string.ascii_uppercase}")
        print(f"  数字: {char in string.digits}")
        print(f"  标点符号: {char in string.punctuation}")
        print(f"  空白字符: {char in string.whitespace}")
        print()

# 3. 字符串模板（Template类）
def demonstrate_templates():
    """演示字符串模板"""
    print("=== 字符串模板 ===")
    
    # 创建模板
    template = string.Template("Hello, $name! Welcome to $place.")
    
    # 替换变量
    result = template.substitute(name="World", place="Python")
    print(f"替换后: {result}")
    
    # 使用字典进行替换
    data = {"name": "Alice", "place": "Wonderland"}
    result = template.substitute(data)
    print(f"使用字典替换: {result}")
    
    # 处理缺失键
    try:
        template.substitute(name="Bob")  # 缺少place
    except KeyError as e:
        print(f"KeyError: {e}")
    
    # 使用safe_substitute处理缺失键（不会抛出异常）
    result = template.safe_substitute(name="Bob")
    print(f"使用safe_substitute: {result}")
    
    # 自定义定界符和标识符
    class MyTemplate(string.Template):
        delimiter = '#'  # 自定义定界符
        idpattern = '[a-z]+_[a-z]+'  # 自定义标识符模式
    
    my_template = MyTemplate("Hello, #first_name!")
    try:
        my_template.substitute(first_name="John")
    except ValueError as e:
        print(f"ValueError: {e} (因为自定义了idpattern)")
    
    my_template = MyTemplate("Hello, #user_name!")
    result = my_template.substitute(user_name="John")
    print(f"使用自定义模板: {result}")
    print()

# 4. 格式化字符串
print("=== 格式化字符串 ===")

# 使用字符串的format方法（推荐）
name = "Python"
age = 30
print(f"使用format: Hello, {name}! You are {age} years old.")

# 使用f-strings（Python 3.6+，推荐）
print(f"使用f-strings: Hello, {name}! You are {age} years old.")

# 使用Template类
print(f"使用Template: {string.Template('Hello, $name! You are $age years old.').substitute(name=name, age=age)}")

# 格式化规范示例
pi = 3.1415926535
print(f"pi = {pi:.2f}")  # 保留2位小数
print(f"pi = {pi:10.4f}")  # 宽度10，保留4位小数
print(f"age = {age:03d}")  # 3位数字，不足补0
print(f"percentage = {0.75:.0%}")  # 百分比格式
print(f"scientific = {pi:e}")  # 科学计数法
print()

# 5. 实际应用示例
def practical_examples():
    """演示实际应用示例"""
    print("=== 实际应用示例 ===")
    
    # 1. 密码生成
    import random
    
    def generate_password(length=12, use_uppercase=True, use_digits=True, use_punctuation=True):
        """生成随机密码"""
        chars = string.ascii_lowercase
        
        if use_uppercase:
            chars += string.ascii_uppercase
        if use_digits:
            chars += string.digits
        if use_punctuation:
            chars += string.punctuation
        
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
    
    print("生成随机密码:")
    print(f"默认密码 (12位): {generate_password()}")
    print(f"简单密码 (8位): {generate_password(8, use_punctuation=False)}")
    print(f"强密码 (16位): {generate_password(16)}")
    
    # 2. 文本清理
    def clean_text(text):
        """清理文本，只保留字母、数字和空格"""
        cleaned = []
        for char in text:
            if char.isalnum() or char.isspace():
                cleaned.append(char)
            else:
                cleaned.append(' ')
        return ''.join(cleaned)
    
    text = "Hello! This is a test-text, with numbers 123 and symbols @#$."
    print(f"\n原始文本: {text}")
    print(f"清理后: {clean_text(text)}")
    
    # 3. 文本分析
    def analyze_text(text):
        """分析文本字符组成"""
        stats = {
            'total_chars': len(text),
            'uppercase': 0,
            'lowercase': 0,
            'digits': 0,
            'punctuation': 0,
            'whitespace': 0,
            'other': 0
        }
        
        for char in text:
            if char.isupper():
                stats['uppercase'] += 1
            elif char.islower():
                stats['lowercase'] += 1
            elif char.isdigit():
                stats['digits'] += 1
            elif char in string.punctuation:
                stats['punctuation'] += 1
            elif char.isspace():
                stats['whitespace'] += 1
            else:
                stats['other'] += 1
        
        return stats
    
    text = "Hello World! 123测试文本"
    stats = analyze_text(text)
    print(f"\n文本分析统计:")
    for key, value in stats.items():
        print(f"{key}: {value}")
    
    # 4. 模板邮件生成
    def generate_email(template_str, **kwargs):
        """使用模板生成邮件"""
        template = string.Template(template_str)
        return template.safe_substitute(**kwargs)
    
    email_template = """
    Subject: 关于您的订单 $order_id
    
    亲爱的 $customer_name：
    
    感谢您在我们网站上的购买！您的订单 $order_id 已确认。
    订单总额：$amount
    预计发货日期：$ship_date
    
    如有任何问题，请随时联系我们。
    
    祝好，
    客户服务团队
    """
    
    email_data = {
        "order_id": "ORD-12345",
        "customer_name": "张三",
        "amount": "¥299.00",
        "ship_date": "2023-12-15"
    }
    
    print(f"\n生成的邮件:")
    print(generate_email(email_template, **email_data))
    print()

# 6. 高级字符串操作
def advanced_string_operations():
    """演示高级字符串操作"""
    print("=== 高级字符串操作 ===")
    
    # 1. 字符串分割与连接
    text = "apple,banana,orange,grape"
    fruits = text.split(',')
    print(f"原始字符串: {text}")
    print(f"分割后: {fruits}")
    print(f"连接后: {'-'.join(fruits)}")
    
    # 2. 去除空白字符
    text = "   Hello, World!   \n"
    print(f"原始字符串: {repr(text)}")
    print(f"去除首尾空白: {repr(text.strip())}")
    print(f"去除左侧空白: {repr(text.lstrip())}")
    print(f"去除右侧空白: {repr(text.rstrip())}")
    
    # 3. 字符串替换
    text = "Hello, World!"
    print(f"原始字符串: {text}")
    print(f"替换 'World' 为 'Python': {text.replace('World', 'Python')}")
    print(f"替换所有 'l' 为 '*': {text.replace('l', '*')}")
    print(f"只替换第一个 'l': {text.replace('l', '*', 1)}")
    
    # 4. 字符串查找
    text = "Hello, World!"
    print(f"原始字符串: {text}")
    print(f"查找 'World': {text.find('World')}")
    print(f"查找 'Python': {text.find('Python')}")
    print(f"从位置5开始查找 'l': {text.find('l', 5)}")
    print(f"rfind 'l': {text.rfind('l')}")  # 从右侧查找
    print(f"startswith 'Hello': {text.startswith('Hello')}")
    print(f"endswith '!': {text.endswith('!')}")
    
    # 5. 字符大小写转换
    text = "Hello, World!"
    print(f"原始字符串: {text}")
    print(f"全大写: {text.upper()}")
    print(f"全小写: {text.lower()}")
    print(f"首字母大写: {text.capitalize()}")
    print(f"每个单词首字母大写: {text.title()}")
    print(f"大小写反转: {text.swapcase()}")
    print()

# 7. 字符串和字节串
def demonstrate_bytes():
    """演示字符串和字节串的转换"""
    print("=== 字符串和字节串 ===")
    
    # 字符串转字节串
    text = "Hello, 世界!"
    bytes_utf8 = text.encode('utf-8')
    bytes_gbk = text.encode('gbk')
    
    print(f"原始字符串: {text}")
    print(f"UTF-8编码: {bytes_utf8}")
    print(f"GBK编码: {bytes_gbk}")
    
    # 字节串转字符串
    text_utf8 = bytes_utf8.decode('utf-8')
    text_gbk = bytes_gbk.decode('gbk')
    
    print(f"UTF-8解码: {text_utf8}")
    print(f"GBK解码: {text_gbk}")
    
    # 错误处理
    try:
        # 尝试用错误的编码解码
        bytes_utf8.decode('ascii')
    except UnicodeDecodeError as e:
        print(f"解码错误: {e}")
    
    # 使用错误处理模式
    result = bytes_utf8.decode('ascii', errors='replace')
    print(f"替换错误字符: {result}")
    
    result = bytes_utf8.decode('ascii', errors='ignore')
    print(f"忽略错误字符: {result}")
    print()

# 8. 注意事项和最佳实践
"""
1. **选择合适的字符串格式化方法**：
   - Python 3.6+: 优先使用f-strings（最简洁、可读性最高）
   - Python 3.0-3.5: 使用str.format()方法
   - 需要避免注入攻击的场景: 使用string.Template（更安全）

2. **字符串连接效率**：
   - 少量字符串连接: 使用+运算符
   - 大量字符串连接: 使用''.join([...])或f-strings（效率更高）

3. **字符编码注意事项**：
   - 处理文本时始终明确编码
   - 文件读写时指定编码
   - 网络通信时注意编码转换

4. **安全考虑**：
   - 处理用户输入时注意转义特殊字符
   - 使用Template类处理可能包含用户输入的模板

5. **string模块常量的使用**：
   - 避免手动定义字符集，使用string模块提供的常量
   - 例如: 使用string.digits而非'0123456789'

6. **性能优化**：
   - 对于频繁的字符串操作，考虑使用列表或io.StringIO
   - 对于大量文本处理，考虑使用正则表达式
"""

def demonstrate_best_practices():
    """演示最佳实践"""
    print("=== 最佳实践示例 ===")
    
    # 1. 字符串格式化选择
    name = "Python"
    version = 3.10
    
    print("字符串格式化方法对比:")
    # f-strings (Python 3.6+)
    print(f"f-strings: {name} {version}")
    
    # str.format()
    print(f"str.format(): {name} {{}}".format(version))
    
    # %运算符（不推荐）
    print(f"%运算符: %s %s" % (name, version))
    
    # Template类（安全场景）
    template = string.Template("$name $version")
    print(f"Template: {template.substitute(name=name, version=version)}")
    
    # 2. 字符串连接效率对比
    import time
    
    print("\n字符串连接效率对比:")
    words = ["word" + str(i) for i in range(10000)]
    
    # 使用+运算符
    start = time.time()
    result = ""
    for word in words:
        result += word
    time_plus = time.time() - start
    print(f"使用+运算符: {time_plus:.6f}秒")
    
    # 使用join方法
    start = time.time()
    result = "".join(words)
    time_join = time.time() - start
    print(f"使用join方法: {time_join:.6f}秒")
    print(f"join方法比+运算符快 {time_plus/time_join:.2f}倍")
    
    # 3. 安全的模板处理
    print("\n安全的模板处理:")
    # 用户输入可能包含恶意内容
    user_input = "${os.system('rm -rf /')}"
    
    # 不安全的方式（如果允许用户格式化字符串）
    print("使用f-strings处理用户输入（不安全示例，不要在实际代码中使用）:")
    # 下面的代码会尝试执行系统命令（如果被允许）
    # print(f"用户输入: {user_input}")  # 这只是示例，不会真正执行
    print("注意: 允许用户格式化字符串可能导致注入攻击")
    
    # 安全的方式使用Template
    template = string.Template("用户输入: $input")
    result = template.substitute(input=user_input)
    print(f"使用Template处理用户输入: {result}")
    print("Template类会将'$'视为普通字符，除非它是有效的变量名")
    
    # 4. 使用string常量
    print("\n使用string常量:")
    # 不好的做法
    digits_manual = '0123456789'
    
    # 好的做法
    digits_constant = string.digits
    
    print(f"手动定义数字字符: {digits_manual}")
    print(f"使用string常量: {digits_constant}")
    print(f"两者相等: {digits_manual == digits_constant}")
    print()

# 运行演示代码
if __name__ == "__main__":
    print("Python string模块演示\n")
    
    demonstrate_character_classification()
    demonstrate_templates()
    practical_examples()
    advanced_string_operations()
    demonstrate_bytes()
    demonstrate_best_practices()
    
    print("演示完成！")