#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
glob模块 - 路径名模式匹配

glob模块提供了根据Unix shell风格的通配符匹配路径名的功能，比fnmatch模块更强大，因为它可以递归地搜索目录。

主要功能包括：
- 路径名模式匹配
- 支持递归目录搜索（**）
- 支持常见通配符（*、?、[]、[!]）
- 返回匹配的文件路径列表

使用场景：
- 文件系统中的批量文件操作
- 递归查找文件
- 按模式过滤文件
- 批量处理特定类型的文件

官方文档：https://docs.python.org/3/library/glob.html
"""

import glob
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. glob模块基本介绍")
print("=" * 50)
print("glob模块用于根据Unix shell风格的通配符匹配路径名")
print("支持递归目录搜索")
print("比fnmatch模块更强大，因为它可以直接处理路径")
print("返回匹配的文件路径列表")

# ===========================
# 2. 通配符说明
# ===========================
print("\n" + "=" * 50)
print("2. 通配符说明")
print("=" * 50)

print("glob模块支持的通配符:")
print("* : 匹配任意数量的字符，包括零个字符")
print("? : 匹配任意单个字符")
print("[seq] : 匹配seq中的任意字符")
print("[!seq] : 匹配不在seq中的任意字符")
print("** : 匹配任意数量的目录（需要recursive=True）")
print("[a-z] : 匹配指定范围内的任意字符")

# ===========================
# 3. 基本用法
# ===========================
print("\n" + "=" * 50)
print("3. 基本用法")
print("=" * 50)

print("当前目录下的文件:")
# 获取当前目录下的所有文件
current_files = glob.glob('*')
for file in current_files:
    print(f"  {file}")

# 获取当前目录下的所有.py文件
print("\n当前目录下的所有.py文件:")
py_files = glob.glob('*.py')
for file in py_files:
    print(f"  {file}")

# 获取当前目录下的所有.txt文件
print("\n当前目录下的所有.txt文件:")
txt_files = glob.glob('*.txt')
for file in txt_files:
    print(f"  {file}")

# 获取名称中包含特定字符的文件
print("\n当前目录下名称中包含'模块'的文件:")
module_files = glob.glob('*模块*')
for file in module_files:
    print(f"  {file}")

# 使用?通配符
print("\n当前目录下以'模块.py'结尾，前面有两个字符的文件:")
short_files = glob.glob('??模块.py')
for file in short_files:
    print(f"  {file}")

# 使用[]通配符
print("\n当前目录下名称以r或s开头的.py文件:")
rs_files = glob.glob('[rs]*.py')
for file in rs_files:
    print(f"  {file}")

# 使用[!]通配符
print("\n当前目录下名称不以数字开头的.py文件:")
non_num_files = glob.glob('[!0-9]*.py')
for file in non_num_files:
    print(f"  {file}")

# ===========================
# 4. 递归目录搜索
# ===========================
print("\n" + "=" * 50)
print("4. 递归目录搜索")
print("=" * 50)

print("递归搜索当前目录及其子目录下的所有.py文件:")
all_py_files = glob.glob('**/*.py', recursive=True)
for file in all_py_files:
    print(f"  {file}")

# 递归搜索当前目录及其子目录下的所有.txt文件
print("\n递归搜索当前目录及其子目录下的所有.txt文件:")
all_txt_files = glob.glob('**/*.txt', recursive=True)
for file in all_txt_files:
    print(f"  {file}")

# 递归搜索特定目录结构
print("\n递归搜索当前目录及其子目录下，名称为test的文件:")
test_files = glob.glob('**/test*', recursive=True)
for file in test_files:
    print(f"  {file}")

# ===========================
# 5. 与os.path结合使用
# ===========================
print("\n" + "=" * 50)
print("5. 与os.path结合使用")
print("=" * 50)

print("获取绝对路径:")
py_files = glob.glob('*.py')
for file in py_files:
    absolute_path = os.path.abspath(file)
    print(f"  {file} -> {absolute_path}")

print("\n获取文件大小:")
for file in py_files:
    size = os.path.getsize(file)
    print(f"  {file}: {size} 字节")

print("\n获取文件修改时间:")
for file in py_files:
    mtime = os.path.getmtime(file)
    import time
    formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
    print(f"  {file}: {formatted_time}")

# ===========================
# 6. 高级用法
# ===========================
print("\n" + "=" * 50)
print("6. 高级用法")
print("=" * 50)

# 使用glob.iglob()进行惰性匹配
print("使用glob.iglob()进行惰性匹配:")
iglob_files = glob.iglob('*.py')
print(f"iglob_files类型: {type(iglob_files)}")
print("匹配的文件:")
for file in iglob_files:
    print(f"  {file}")

# 递归惰性匹配
print("\n递归惰性匹配所有.py文件:")
iglob_recursive = glob.iglob('**/*.py', recursive=True)
for file in iglob_recursive:
    print(f"  {file}")

# 区分文件和目录
print("\n当前目录下的所有目录:")
dirs = [d for d in glob.glob('*') if os.path.isdir(d)]
for dir in dirs:
    print(f"  {dir}")

print("\n当前目录下的所有文件:")
files = [f for f in glob.glob('*') if os.path.isfile(f)]
for file in files:
    print(f"  {file}")

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
        files = glob.glob(os.path.join(directory, pattern))
        files.sort()
        
        # 重命名文件
        for i, file_path in enumerate(files):
            # 获取文件名和目录
            dir_name, filename = os.path.split(file_path)
            
            # 生成新文件名
            new_name = new_pattern.format(num=i+1)
            
            # 构建完整路径
            new_path = os.path.join(dir_name, new_name)
            
            # 重命名文件
            os.rename(file_path, new_path)
            print(f"重命名: {filename} -> {new_name}")
        
        return f"成功重命名 {len(files)} 个文件"
        
    except Exception as e:
        return f"错误: {e}"

print("示例1: 批量重命名文件")
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
        
        # 递归获取所有文件
        all_files = glob.glob(os.path.join(directory, '**', '*'), recursive=True)
        files = [f for f in all_files if os.path.isfile(f)]
        
        # 统计文件类型
        for file_path in files:
            # 获取文件扩展名
            _, ext = os.path.splitext(file_path)
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

# 示例3: 查找大文件
def find_large_files(directory, min_size_mb):
    """
    查找目录中大于指定大小的文件
    
    Args:
        directory: 目标目录
        min_size_mb: 最小文件大小（MB）
    
    Returns:
        大文件路径和大小列表
    """
    try:
        large_files = []
        min_size_bytes = min_size_mb * 1024 * 1024
        
        # 递归获取所有文件
        all_files = glob.glob(os.path.join(directory, '**', '*'), recursive=True)
        
        for file_path in all_files:
            if os.path.isfile(file_path):
                size = os.path.getsize(file_path)
                if size > min_size_bytes:
                    large_files.append((file_path, size / (1024 * 1024)))
        
        # 按大小排序
        large_files.sort(key=lambda x: x[1], reverse=True)
        
        return large_files
        
    except Exception as e:
        return f"错误: {e}"

print("\n示例3: 查找大文件")
print("函数: find_large_files(directory, min_size_mb)")
print("用法: find_large_files('.', 10)  # 查找大于10MB的文件")
print("返回值: 包含文件路径和大小的元组列表")

# 示例4: 批量处理文件
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
    try:
        # 获取匹配的文件列表
        files = glob.glob(os.path.join(directory, pattern))
        
        # 处理每个文件
        results = []
        for file_path in files:
            result = processor_func(file_path)
            results.append((file_path, result))
        
        return results
        
    except Exception as e:
        return f"错误: {e}"

print("\n示例4: 批量处理文件")
print("函数: batch_process_files(directory, pattern, processor_func)")
print("用法示例: 批量压缩图片")
print("batch_process_files('./images', '*.jpg', compress_image)")

# 示例5: 生成文件列表报告
def generate_file_report(directory, output_file):
    """
    生成目录的文件列表报告
    
    Args:
        directory: 目标目录
        output_file: 输出报告文件
    """
    try:
        # 递归获取所有文件
        all_files = glob.glob(os.path.join(directory, '**', '*'), recursive=True)
        files = [f for f in all_files if os.path.isfile(f)]
        
        # 生成报告
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"文件列表报告 - {directory}\n")
            f.write(f"总文件数: {len(files)}\n\n")
            
            for file_path in sorted(files):
                # 获取相对路径
                rel_path = os.path.relpath(file_path, directory)
                
                # 获取文件信息
                size = os.path.getsize(file_path)
                mtime = os.path.getmtime(file_path)
                
                # 格式化时间
                import time
                formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))
                
                # 写入报告
                f.write(f"{rel_path}\n")
                f.write(f"  大小: {size} 字节\n")
                f.write(f"  修改时间: {formatted_time}\n")
                f.write("\n")
        
        return f"报告已生成: {output_file}"
        
    except Exception as e:
        return f"错误: {e}"

print("\n示例5: 生成文件列表报告")
print("函数: generate_file_report(directory, output_file)")
print("用法: generate_file_report('.', 'file_report.txt')")
print("生成包含文件路径、大小和修改时间的报告")

# ===========================
# 8. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("8. 最佳实践")
print("=" * 50)

print("1. 递归搜索的使用")
print("   - 使用**进行递归搜索时，必须设置recursive=True")
print("   - 递归搜索可能会消耗较多资源，只在需要时使用")
print("   - 对于深层目录结构，考虑使用os.walk()进行更精细的控制")

print("\n2. 路径处理")
print("   - 使用os.path.join()构建路径，避免平台差异")
print("   - 使用os.path.abspath()获取绝对路径")
print("   - 使用os.path.relpath()获取相对路径")

print("\n3. 性能考虑")
print("   - 对于大量文件，使用glob.iglob()进行惰性匹配")
print("   - 避免不必要的递归搜索")
print("   - 对于复杂的匹配模式，考虑使用正则表达式")

print("\n4. 错误处理")
print("   - 处理文件权限问题")
print("   - 处理不存在的目录")
print("   - 处理符号链接循环")

print("\n5. 安全注意事项")
print("   - 验证用户输入的模式，避免路径遍历攻击")
print("   - 在处理用户提供的模式时，考虑使用白名单")
print("   - 注意文件名中可能包含的特殊字符")

# ===========================
# 9. 与fnmatch模块的比较
# ===========================
print("\n" + "=" * 50)
print("9. 与fnmatch模块的比较")
print("=" * 50)

print("glob模块 vs fnmatch模块:")
print("- glob模块处理路径名，fnmatch模块处理字符串")
print("- glob模块支持递归搜索，fnmatch模块不支持")
print("- glob模块返回匹配的路径列表，fnmatch模块返回布尔值")
print("- glob模块更适合文件系统操作，fnmatch模块更适合字符串匹配")

# ===========================
# 10. 总结
# ===========================
print("\n" + "=" * 50)
print("10. 总结")
print("=" * 50)
print("glob模块提供了强大的路径名模式匹配功能")
print("支持递归目录搜索")

print("\n主要功能:")
print("- 路径名模式匹配")
print("- 递归目录搜索")
print("- 支持常见通配符")
print("- 返回匹配的文件路径列表")

print("\n应用场景:")
print("- 文件系统中的批量文件操作")
print("- 递归查找文件")
print("- 按模式过滤文件")
print("- 批量处理特定类型的文件")
print("- 生成文件列表报告")

print("\n使用glob模块可以轻松实现复杂的文件系统操作")
print("是Python中文件处理的重要工具之一")
