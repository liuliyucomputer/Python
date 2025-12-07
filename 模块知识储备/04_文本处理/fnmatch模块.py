#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fnmatch模块 - Unix文件名模式匹配

fnmatch模块提供了Unix shell风格的文件名模式匹配功能，支持通配符的使用。

主要功能包括：
- 文件名模式匹配
- 大小写敏感/不敏感的匹配
- 支持常见通配符（*、?、[]、[!]）
- 可用于过滤文件名列表

使用场景：
- 文件系统操作中的文件名匹配
- 批量文件处理
- 文件搜索和过滤
- 配置文件中的模式匹配

官方文档：https://docs.python.org/3/library/fnmatch.html
"""

import fnmatch
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. fnmatch模块基本介绍")
print("=" * 50)
print("fnmatch模块用于Unix shell风格的文件名模式匹配")
print("支持通配符的使用")
print("提供了简单易用的文件名匹配功能")
print("可用于文件系统操作中的文件名过滤")

# ===========================
# 2. 通配符说明
# ===========================
print("\n" + "=" * 50)
print("2. 通配符说明")
print("=" * 50)

print("fnmatch模块支持的通配符:")
print("* : 匹配任意数量的字符，包括零个字符")
print("? : 匹配任意单个字符")
print("[seq] : 匹配seq中的任意字符")
print("[!seq] : 匹配不在seq中的任意字符")
print("[a-z] : 匹配指定范围内的任意字符")

# ===========================
# 3. 基本用法
# ===========================
print("\n" + "=" * 50)
print("3. 基本用法")
print("=" * 50)

# 示例文件名
filenames = [
    'file.txt',
    'file.py',
    'file1.txt',
    'file2.py',
    'test.txt',
    'test.py',
    'data.csv',
    'config.ini',
    'image.jpg',
    'image.png',
    'document.pdf'
]

print("示例文件名列表:")
for filename in filenames:
    print(f"  {filename}")

# 使用fnmatch.fnmatch()进行匹配
print("\n匹配所有.txt文件:")
txt_files = [f for f in filenames if fnmatch.fnmatch(f, '*.txt')]
for f in txt_files:
    print(f"  {f}")

# 匹配所有.py文件
print("\n匹配所有.py文件:")
py_files = [f for f in filenames if fnmatch.fnmatch(f, '*.py')]
for f in py_files:
    print(f"  {f}")

# 匹配file开头的文件
print("\n匹配file开头的文件:")
file_files = [f for f in filenames if fnmatch.fnmatch(f, 'file*')]
for f in file_files:
    print(f"  {f}")

# 匹配file后跟一个字符的文件
print("\n匹配file后跟一个字符的文件:")
file_1char_files = [f for f in filenames if fnmatch.fnmatch(f, 'file?.txt')]
for f in file_1char_files:
    print(f"  {f}")

# 匹配指定范围内的文件
print("\n匹配file1或file2的文件:")
specific_files = [f for f in filenames if fnmatch.fnmatch(f, 'file[12].*')]
for f in specific_files:
    print(f"  {f}")

# 匹配不在指定范围内的文件
print("\n匹配不是.txt或.py的文件:")
other_files = [f for f in filenames if fnmatch.fnmatch(f, '*[!txtpy]')]
for f in other_files:
    print(f"  {f}")

# ===========================
# 4. 大小写不敏感匹配
# ===========================
print("\n" + "=" * 50)
print("4. 大小写不敏感匹配")
print("=" * 50)

# 示例文件名（包含大小写）
mixed_filenames = [
    'File.txt',
    'FILE.PY',
    'file.TXT',
    'test.Py',
    'Data.csv'
]

print("包含大小写的文件名列表:")
for filename in mixed_filenames:
    print(f"  {filename}")

# 使用fnmatch.fnmatchcase()进行大小写敏感匹配
print("\n大小写敏感匹配 *.txt:")
sensitive_match = [f for f in mixed_filenames if fnmatch.fnmatchcase(f, '*.txt')]
for f in sensitive_match:
    print(f"  {f}")

# 使用fnmatch.fnmatch()进行大小写不敏感匹配（依赖于操作系统）
print("\n大小写不敏感匹配 *.txt:")
insensitive_match = [f for f in mixed_filenames if fnmatch.fnmatch(f, '*.txt')]
for f in insensitive_match:
    print(f"  {f}")

# ===========================
# 5. 转换为正则表达式
# ===========================
print("\n" + "=" * 50)
print("5. 转换为正则表达式")
print("=" * 50)

# 使用fnmatch.translate()将模式转换为正则表达式
pattern = '*.txt'
regex = fnmatch.translate(pattern)
print(f"将 '{pattern}' 转换为正则表达式: {regex}")

# 使用正则表达式进行匹配
import re
regex_pattern = re.compile(regex)
regex_match = [f for f in filenames if regex_pattern.match(f)]
print(f"\n使用正则表达式匹配 '{pattern}':")
for f in regex_match:
    print(f"  {f}")

# 转换更复杂的模式
complex_pattern = 'file[1-9].*.py'
complex_regex = fnmatch.translate(complex_pattern)
print(f"\n将 '{complex_pattern}' 转换为正则表达式: {complex_regex}")

# ===========================
# 6. 与os模块结合使用
# ===========================
print("\n" + "=" * 50)
print("6. 与os模块结合使用")
print("=" * 50)

print("当前目录下的文件:")
try:
    # 获取当前目录下的所有文件
    current_files = os.listdir('.')
    
    # 过滤出所有.py文件
    py_files = [f for f in current_files if fnmatch.fnmatch(f, '*.py')]
    print("\n当前目录下的.py文件:")
    for f in py_files:
        print(f"  {f}")
        
    # 过滤出所有.txt文件
    txt_files = [f for f in current_files if fnmatch.fnmatch(f, '*.txt')]
    print("\n当前目录下的.txt文件:")
    for f in txt_files:
        print(f"  {f}")
        
    # 过滤出以test开头的文件
    test_files = [f for f in current_files if fnmatch.fnmatch(f, 'test*')]
    print("\n当前目录下以test开头的文件:")
    for f in test_files:
        print(f"  {f}")
        
except Exception as e:
    print(f"错误: {e}")

# ===========================
# 7. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("7. 实际应用示例")
print("=" * 50)

# 示例1: 批量重命名文件
def batch_rename_files(directory, pattern, new_pattern):
    """
    批量重命名匹配模式的文件
    
    Args:
        directory: 目标目录
        pattern: 匹配模式
        new_pattern: 新文件名模式（使用{num}作为序号占位符）
    """
    try:
        # 获取匹配的文件列表
        files = [f for f in os.listdir(directory) if fnmatch.fnmatch(f, pattern)]
        files.sort()
        
        # 重命名文件
        for i, filename in enumerate(files):
            # 生成新文件名
            new_name = new_pattern.format(num=i+1)
            
            # 构建完整路径
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            
            # 重命名文件
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_name}")
        
        return f"成功重命名 {len(files)} 个文件"
        
    except Exception as e:
        return f"错误: {e}"

print("示例1: 批量重命名文件")
# 注意：这里只是展示函数定义，不会实际执行重命名操作
print("函数: batch_rename_files(directory, pattern, new_pattern)")
print("用法: batch_rename_files('./images', '*.jpg', 'image{num}.jpg')")

# 示例2: 统计目录中不同类型的文件
def count_file_types(directory):
    """
    统计目录中不同类型的文件数量
    
    Args:
        directory: 目标目录
    
    Returns:
        文件类型统计字典
    """
    try:
        file_types = {}
        
        # 获取目录中的所有文件
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        # 统计文件类型
        for filename in files:
            # 获取文件扩展名
            _, ext = os.path.splitext(filename)
            ext = ext.lower()  # 转换为小写
            
            # 更新统计
            if ext not in file_types:
                file_types[ext] = 0
            file_types[ext] += 1
        
        return file_types
        
    except Exception as e:
        return f"错误: {e}"

print("\n示例2: 统计目录中不同类型的文件")
# 获取当前目录的文件类型统计
file_stats = count_file_types('.')
print("当前目录的文件类型统计:")
for ext, count in file_stats.items():
    print(f"  {ext}: {count} 个文件")

# 示例3: 递归查找匹配的文件
def find_files(directory, pattern):
    """
    递归查找目录中匹配模式的文件
    
    Args:
        directory: 起始目录
        pattern: 匹配模式
    
    Returns:
        匹配的文件路径列表
    """
    matched_files = []
    
    try:
        # 遍历目录
        for root, dirs, files in os.walk(directory):
            # 过滤匹配的文件
            for filename in files:
                if fnmatch.fnmatch(filename, pattern):
                    # 构建完整路径
                    full_path = os.path.join(root, filename)
                    matched_files.append(full_path)
        
        return matched_files
        
    except Exception as e:
        return f"错误: {e}"

print("\n示例3: 递归查找匹配的文件")
print("函数: find_files(directory, pattern)")
print("用法: find_files('.', '*.py')")
print("将递归查找当前目录及其子目录中的所有.py文件")

# 示例4: 过滤配置文件中的模式
def filter_config_patterns(config_lines, patterns):
    """
    过滤配置文件中匹配模式的行
    
    Args:
        config_lines: 配置文件行列表
        patterns: 匹配模式列表
    
    Returns:
        匹配的行列表
    """
    matched_lines = []
    
    for line in config_lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue  # 跳过空行和注释行
        
        # 检查是否匹配任何模式
        for pattern in patterns:
            if fnmatch.fnmatch(line, pattern):
                matched_lines.append(line)
                break
    
    return matched_lines

print("\n示例4: 过滤配置文件中的模式")
# 示例配置行
config_lines = [
    '# 配置文件示例',
    'server.host = localhost',
    'server.port = 8080',
    'database.url = mysql://localhost:3306/db',
    'database.user = root',
    'database.password = secret',
    'log.file = app.log',
    'log.level = INFO'
]

# 过滤数据库相关配置
patterns = ['database.*']
db_configs = filter_config_patterns(config_lines, patterns)
print("数据库相关配置:")
for config in db_configs:
    print(f"  {config}")

# 示例5: 批量文件处理
def batch_process_files(directory, pattern, processor_func):
    """
    批量处理匹配模式的文件
    
    Args:
        directory: 目标目录
        pattern: 匹配模式
        processor_func: 处理函数，接收文件路径作为参数
    
    Returns:
        处理结果列表
    """
    results = []
    
    try:
        # 获取匹配的文件列表
        files = [f for f in os.listdir(directory) if fnmatch.fnmatch(f, pattern)]
        
        # 处理每个文件
        for filename in files:
            file_path = os.path.join(directory, filename)
            result = processor_func(file_path)
            results.append((filename, result))
        
        return results
        
    except Exception as e:
        return f"错误: {e}"

print("\n示例5: 批量文件处理")
print("函数: batch_process_files(directory, pattern, processor_func)")
print("用法示例: 批量压缩.jpg文件")
print("batch_process_files('./images', '*.jpg', compress_image)")

# ===========================
# 8. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("8. 最佳实践")
print("=" * 50)

print("1. 明确大小写需求")
print("   - 使用fnmatch()进行平台相关的大小写匹配")
print("   - 使用fnmatchcase()进行严格的大小写敏感匹配")
print("   - 在跨平台应用中，明确指定大小写处理方式")

print("\n2. 模式选择")
print("   - 使用*匹配任意字符序列")
print("   - 使用?匹配单个字符")
print("   - 使用[]匹配特定字符集")
print("   - 使用[!]匹配不在字符集中的字符")

print("\n3. 与其他模块结合")
print("   - 与os模块结合进行文件系统操作")
print("   - 与os.walk()结合进行递归文件搜索")
print("   - 使用translate()将模式转换为正则表达式")

print("\n4. 性能考虑")
print("   - 对于大量文件，使用os.listdir()获取列表后再过滤")
print("   - 避免在循环中重复编译正则表达式")
print("   - 对于复杂模式，考虑使用专门的正则表达式")

print("\n5. 安全注意事项")
print("   - 验证用户输入的模式，避免路径遍历攻击")
print("   - 在处理用户提供的模式时，考虑使用白名单")
print("   - 注意文件名中可能包含的特殊字符")

# ===========================
# 9. 总结
# ===========================
print("\n" + "=" * 50)
print("9. 总结")
print("=" * 50)
print("fnmatch模块提供了Unix shell风格的文件名模式匹配功能")
print("支持通配符的使用")

print("\n主要功能:")
print("- 文件名模式匹配")
print("- 大小写敏感/不敏感的匹配")
print("- 支持常见通配符")
print("- 可用于过滤文件名列表")

print("\n应用场景:")
print("- 文件系统操作中的文件名匹配")
print("- 批量文件处理")
print("- 文件搜索和过滤")
print("- 配置文件中的模式匹配")

print("\n使用fnmatch模块可以轻松实现文件名的模式匹配")
print("是Python中文件系统操作的重要工具之一")
