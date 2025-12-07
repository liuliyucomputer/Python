#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shlex模块 - 命令行参数解析工具

shlex模块提供了用于解析和生成类似shell的命令行参数的功能。

主要功能包括：
- 将字符串解析为命令行参数列表
- 处理带引号的参数
- 支持转义字符
- 生成符合shell语法的字符串
- 支持不同的shell风格

使用场景：
- 命令行参数解析
- 命令行字符串生成
- 处理配置文件中的命令行格式
- 与subprocess模块结合使用

官方文档：https://docs.python.org/3/library/shlex.html
"""

import shlex
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. shlex模块基本介绍")
print("=" * 50)
print("shlex模块用于解析和生成类似shell的命令行参数")
print("支持处理带引号的参数和转义字符")
print("与subprocess模块结合使用非常方便")
print("适合处理复杂的命令行参数")

# ===========================
# 2. 基本用法
# ===========================
print("\n" + "=" * 50)
print("2. 基本用法")
print("=" * 50)

# 使用shlex.split解析命令行字符串
command_str = "ls -l 'my documents'"
args = shlex.split(command_str)

print(f"原始命令字符串: {command_str}")
print(f"解析后的参数列表: {args}")

# 使用shlex.quote生成安全的命令行参数
unsafe_arg = "file name with spaces & special chars"
safe_arg = shlex.quote(unsafe_arg)

print(f"\n不安全的参数: {unsafe_arg}")
print(f"安全的命令行参数: {safe_arg}")

# ===========================
# 3. shlex.split() 高级用法
# ===========================
print("\n" + "=" * 50)
print("3. shlex.split() 高级用法")
print("=" * 50)

# 处理不同类型的引号
mixed_quotes = 'echo "Hello world" \'Python\''
args = shlex.split(mixed_quotes)
print(f"混合引号: {mixed_quotes}")
print(f"解析结果: {args}")

# 处理转义字符
escaped_str = "echo Hello\\nWorld"
args = shlex.split(escaped_str)
print(f"\n转义字符: {escaped_str}")
print(f"解析结果: {args}")

# 处理复杂的命令行
complex_cmd = 'python -c "print(\"Hello\", \"World\")" --verbose'
args = shlex.split(complex_cmd)
print(f"\n复杂命令: {complex_cmd}")
print(f"解析结果: {args}")

# ===========================
# 4. shlex.quote() 用法
# ===========================
print("\n" + "=" * 50)
print("4. shlex.quote() 用法")
print("=" * 50)

# 安全引用各种类型的字符串
strings_to_quote = [
    "normal_string",
    "string with spaces",
    "string with'single'quotes",
    "string with\"double\"quotes",
    "string with\nnewline",
    "string with $dollar sign",
    "string with ; semicolon",
    "string with & ampersand",
    "string with * wildcard",
    "string with ! exclamation"
]

print("不同字符串的安全引用结果:")
for s in strings_to_quote:
    quoted = shlex.quote(s)
    print(f"  '{s}' -> {quoted}")

# ===========================
# 5. shlex.shlex 类
# ===========================
print("\n" + "=" * 50)
print("5. shlex.shlex 类")
print("=" * 50)

# 创建shlex对象
test_str = "command --option value 'quoted string'"
lex = shlex.shlex(test_str)

# 逐个获取标记
print("逐个获取标记:")
tokens = list(lex)
print(f"  标记列表: {tokens}")

# 配置shlex对象
print("\n配置shlex对象:")
lex = shlex.shlex("command 'with spaces' --option=value")
lex.whitespace_split = True  # 只按空白分割，不处理引号

print(f"  whitespace_split=True:")
print(f"    标记列表: {list(lex)}")

# 使用posix模式
lex = shlex.shlex("command 'with spaces' --option=value", posix=True)
print(f"  posix=True:")
print(f"    标记列表: {list(lex)}")

# ===========================
# 6. 自定义分隔符和引号
# ===========================
print("\n" + "=" * 50)
print("6. 自定义分隔符和引号")
print("=" * 50)

# 自定义引号
config_str = "key1='value with spaces' key2=\"another value\""
lex = shlex.shlex(config_str)
lex.quotes = "'\""  # 默认引号
lex.wordchars += "="  # 允许等号作为单词字符

print(f"配置字符串: {config_str}")
print(f"解析结果: {list(lex)}")

# 自定义分隔符
csv_str = "field1,field2,'field,3','field\"4'"
lex = shlex.shlex(csv_str)
lex.whitespace = ','  # 使用逗号作为分隔符
lex.whitespace_split = True

print(f"\nCSV字符串: {csv_str}")
print(f"解析结果: {list(lex)}")

# ===========================
# 7. 与subprocess模块结合使用
# ===========================
print("\n" + "=" * 50)
print("7. 与subprocess模块结合使用")
print("=" * 50)

# 示例1: 使用shlex.split解析命令字符串
command_str = "ls -la /home/user/Documents"
args = shlex.split(command_str)

print(f"命令字符串: {command_str}")
print(f"subprocess参数: {args}")

# 示例2: 使用shlex.quote确保参数安全
filename = "my file.txt"
safe_filename = shlex.quote(filename)
command = f"cat {safe_filename}"

print(f"\n文件名: {filename}")
print(f"安全的命令: {command}")
print(f"参数列表: {shlex.split(command)}")

# ===========================
# 8. 解析配置文件
# ===========================
print("\n" + "=" * 50)
print("8. 解析配置文件")
print("=" * 50)

# 模拟配置文件内容
config_content = '''
# This is a comment
command = run 'with spaces'
option = value1 value2 value3
path = /home/user "My Documents"
'''  

# 使用shlex解析配置文件
print("配置文件内容:")
print(config_content)

print("\n解析配置文件:")
lex = shlex.shlex(config_content)
lex.whitespace = " "  # 只使用空格作为分隔符
lex.whitespace_split = True
lex.commenters = "#"  # 支持#注释

# 跳过空白行
tokens = [token for token in lex if token.strip()]

print(f"解析的标记: {tokens}")

# 构建配置字典
config = {}
i = 0
while i < len(tokens):
    if tokens[i] == '=':
        key = tokens[i-1]
        value = []
        i += 1
        while i < len(tokens) and tokens[i] != '=':
            value.append(tokens[i])
            i += 1
        config[key] = ' '.join(value)
    else:
        i += 1

print(f"\n配置字典: {config}")

# ===========================
# 9. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

# 示例1: 命令行工具参数解析
def command_line_parser():
    """命令行工具参数解析示例"""
    import subprocess
    
    # 模拟从用户输入获取命令
    user_input = "python script.py --input 'data file.txt' --output result.txt --verbose"
    
    print(f"用户输入命令: {user_input}")
    
    # 解析命令行参数
    args = shlex.split(user_input)
    print(f"解析后的参数列表: {args}")
    
    # 执行命令（仅模拟）
    print("\n执行命令:")
    # subprocess.run(args)  # 实际使用时取消注释
    print(f"命令执行成功: {args[0]} {args[1]}...")

# 测试命令行工具参数解析
print("示例1: 命令行工具参数解析")
command_line_parser()

# 示例2: 安全的命令构建
def safe_command_builder():
    """安全的命令构建示例"""
    import subprocess
    
    # 可能包含不安全字符的参数
    user_provided = "file with spaces & special chars.txt"
    output_file = "output.txt"
    
    print(f"用户提供的文件名: {user_provided}")
    
    # 构建安全的命令
    command = ["cat", user_provided, "|", "grep", "pattern"]
    
    # 错误的做法：直接拼接字符串
    unsafe_cmd = f"cat {user_provided} | grep pattern"
    print(f"\n错误做法（不安全）: {unsafe_cmd}")
    
    # 正确的做法1：使用参数列表
    print(f"正确做法1（参数列表）: {command}")
    
    # 正确的做法2：使用shlex.quote
    safe_cmd = f"cat {shlex.quote(user_provided)} | grep pattern"
    print(f"正确做法2（shlex.quote）: {safe_cmd}")
    
    # 执行命令（仅模拟）
    print("\n执行安全命令:")
    # subprocess.run(["cat", user_provided])  # 实际使用时取消注释
    print(f"命令执行成功")

# 测试安全的命令构建
print("\n示例2: 安全的命令构建")
safe_command_builder()

# 示例3: 命令行参数生成
def command_generator():
    """命令行参数生成示例"""
    # 需要执行的命令和参数
    cmd = "rsync"
    options = ["-avz", "--exclude='*.tmp'", "--delete"]
    source = "/home/user/data/"
    destination = "server:/remote/data/"
    
    # 构建命令列表
    command_list = [cmd] + options + [source, destination]
    
    print(f"命令列表: {command_list}")
    
    # 生成命令字符串（用于显示或日志）
    command_str = " ".join(shlex.quote(arg) for arg in command_list)
    
    print(f"生成的命令字符串: {command_str}")
    
    # 验证解析后的命令列表是否与原始一致
    parsed_back = shlex.split(command_str)
    print(f"\n解析后的命令列表: {parsed_back}")
    print(f"是否与原始一致: {command_list == parsed_back}")

# 测试命令行参数生成
print("\n示例3: 命令行参数生成")
command_generator()

# 示例4: 解析复杂的命令行
def complex_command_parser():
    """解析复杂的命令行示例"""
    complex_cmd = '''
    python -c "
    import sys
    print('Hello from Python', sys.argv[1])
    " -- 'argument with spaces'
    '''
    
    print(f"复杂命令字符串:\n{complex_cmd}")
    
    # 去除多余的空白和换行
    cleaned_cmd = " ".join(line.strip() for line in complex_cmd.splitlines() if line.strip())
    
    print(f"\n清理后的命令: {cleaned_cmd}")
    
    # 解析命令
    args = shlex.split(cleaned_cmd)
    
    print(f"\n解析后的参数列表: {args}")
    
    # 分组参数
    print(f"\n命令分组:")
    print(f"  解释器: {args[0]}")
    print(f"  选项: {args[1]}")
    print(f"  Python代码: {args[2]}")
    print(f"  分隔符: {args[3]}")
    print(f"  传递给Python的参数: {args[4]}")

# 测试解析复杂的命令行
print("\n示例4: 解析复杂的命令行")
complex_command_parser()

# ===========================
# 10. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("10. 最佳实践和注意事项")
print("=" * 50)

print("1. 安全使用")
print("   - 始终使用shlex.quote()处理用户输入的参数")
print("   - 避免直接拼接命令字符串")
print("   - 优先使用参数列表而不是字符串命令")

print("\n2. 参数解析")
print("   - 使用shlex.split()解析命令行字符串")
print("   - 注意处理不同类型的引号")
print("   - 了解转义字符的处理方式")

print("\n3. 与subprocess结合")
print("   - subprocess模块推荐使用参数列表")
print("   - shlex.split()是生成参数列表的好方法")
print("   - 对于复杂命令，使用shlex解析更可靠")

print("\n4. 配置文件解析")
print("   - shlex可以用于解析简单的配置文件")
print("   - 注意设置适当的分隔符和注释字符")
print("   - 对于复杂的配置文件，考虑使用专门的配置解析库")

print("\n5. 平台差异")
print("   - shlex默认使用POSIX shell语法")
print("   - 在Windows上使用时注意兼容性")
print("   - 使用posix参数控制解析行为")

print("\n6. 性能考虑")
print("   - shlex的性能开销很小")
print("   - 对于简单的参数解析，可以使用split()方法")
print("   - 对于复杂的情况，使用shlex更可靠")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("shlex模块提供了强大的命令行参数解析和生成功能")
print("是处理命令行字符串的理想工具")

print("\n主要功能:")
print("- 将字符串解析为命令行参数列表")
print("- 生成安全的命令行参数")
print("- 处理各种引号和转义字符")
print("- 支持自定义分隔符和引号")
print("- 与subprocess模块完美结合")

print("\n应用场景:")
print("- 命令行工具开发")
print("- 配置文件解析")
print("- 安全的命令构建")
print("- 复杂命令行参数处理")

print("\n使用shlex模块可以提高命令行工具的安全性和可靠性")
print("是Python中处理命令行字符串的重要工具")
