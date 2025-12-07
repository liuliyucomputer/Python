#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
difflib模块 - 文本差异比较和处理

difflib模块提供了用于比较序列之间差异的类和函数，特别是用于处理文本差异的功能。

主要功能包括：
- 文本行差异比较
- 文本字符差异比较
- 生成统一格式的差异报告
- 生成HTML格式的差异报告
- 序列匹配

使用场景：
- 版本控制系统的差异显示
- 文档对比工具
- 代码审查工具
- 数据同步工具
- 测试结果比对

官方文档：https://docs.python.org/3/library/difflib.html
"""

import difflib

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. difflib模块基本介绍")
print("=" * 50)
print("difflib模块用于比较序列之间的差异")
print("特别是用于文本差异的比较和处理")
print("提供多种格式的差异输出")
print("支持行级和字符级的比较")

# ===========================
# 2. 基本用法
# ===========================
print("\n" + "=" * 50)
print("2. 基本用法")
print("=" * 50)

# 示例文本
text1 = """
Hello, World!
This is a test file.
Python is great.
Programming is fun.
"""

text2 = """
Hello, Python!
This is a sample file.
Python is awesome.
Coding is fun.
New line added.
"""

# 将文本拆分为行
lines1 = text1.splitlines(keepends=True)
lines2 = text2.splitlines(keepends=True)

# 生成差异
print("原始文本1:")
print(text1)

print("原始文本2:")
print(text2)

# ===========================
# 3. 生成统一格式差异
# ===========================
print("\n" + "=" * 50)
print("3. 生成统一格式差异")
print("=" * 50)

# 使用unified_diff生成统一格式差异
unified_diff = difflib.unified_diff(
    lines1,
    lines2,
    fromfile='text1.txt',
    tofile='text2.txt',
    lineterm=''
)

print("统一格式差异:")
print(''.join(unified_diff))

# ===========================
# 4. 生成上下文格式差异
# ===========================
print("\n" + "=" * 50)
print("4. 生成上下文格式差异")
print("=" * 50)

# 使用context_diff生成上下文格式差异
context_diff = difflib.context_diff(
    lines1,
    lines2,
    fromfile='text1.txt',
    tofile='text2.txt',
    lineterm=''
)

print("上下文格式差异:")
print(''.join(context_diff))

# ===========================
# 5. 生成HTML格式差异
# ===========================
print("\n" + "=" * 50)
print("5. 生成HTML格式差异")
print("=" * 50)

# 使用HtmlDiff生成HTML格式差异
html_diff = difflib.HtmlDiff()
html_content = html_diff.make_file(
    lines1,
    lines2,
    fromdesc='text1.txt',
    todesc='text2.txt'
)

print("生成HTML格式差异文件 (diff.html)")
with open('diff.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# ===========================
# 6. 字符级差异比较
# ===========================
print("\n" + "=" * 50)
print("6. 字符级差异比较")
print("=" * 50)

# 示例字符串
str1 = "Hello, World!"
str2 = "Hello, Python!"

# 使用SequenceMatcher比较字符串
matcher = difflib.SequenceMatcher(None, str1, str2)

print(f"字符串1: {str1}")
print(f"字符串2: {str2}")
print(f"相似度: {matcher.ratio():.2f}")
print(f"快速相似度: {matcher.quick_ratio():.2f}")
print(f"真实相似度: {matcher.real_quick_ratio():.2f}")

# 获取匹配块
print("\n匹配块:")
for block in matcher.get_matching_blocks():
    print(f"  位置: ({block.a}, {block.b}, {block.size})")
    print(f"    str1: '{str1[block.a:block.a+block.size]}'")
    print(f"    str2: '{str2[block.b:block.b+block.size]}'")

# ===========================
# 7. 差异生成器
# ===========================
print("\n" + "=" * 50)
print("7. 差异生成器")
print("=" * 50)

# 使用Differ生成差异
print("Differ生成的差异:")
differ = difflib.Differ()
diff = list(differ.compare(lines1, lines2))
for line in diff:
    print(line, end='')

# ===========================
# 8. 高级功能
# ===========================
print("\n" + "=" * 50)
print("8. 高级功能")
print("=" * 50)

# 自定义差异比较
print("自定义差异比较:")

# 忽略大小写的比较
matcher_ignore_case = difflib.SequenceMatcher(lambda x: x.lower(), "Hello World", "hello python")
print(f"忽略大小写的相似度: {matcher_ignore_case.ratio():.2f}")

# 忽略特定字符的比较
def is_junk(c):
    return c in " 	,.!"

matcher_ignore_junk = difflib.SequenceMatcher(is_junk, "Hello, World!", "Hello Python!")
print(f"忽略特定字符的相似度: {matcher_ignore_junk.ratio():.2f}")

# 生成带行号的差异
print("\n带行号的统一格式差异:")
unified_diff_with_numbers = difflib.unified_diff(
    lines1,
    lines2,
    fromfile='text1.txt',
    tofile='text2.txt',
    lineterm='',
    n=2  # 显示2行上下文
)
print(''.join(unified_diff_with_numbers))

# ===========================
# 9. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

# 示例1: 比较两个文件并生成差异报告
def compare_files(file1_path, file2_path, output_format='unified'):
    """比较两个文件并生成差异报告"""
    try:
        with open(file1_path, 'r', encoding='utf-8') as f1:
            lines1 = f1.readlines()
        
        with open(file2_path, 'r', encoding='utf-8') as f2:
            lines2 = f2.readlines()
        
        if output_format == 'unified':
            diff = difflib.unified_diff(
                lines1, lines2,
                fromfile=file1_path,
                tofile=file2_path,
                lineterm=''
            )
        elif output_format == 'context':
            diff = difflib.context_diff(
                lines1, lines2,
                fromfile=file1_path,
                tofile=file2_path,
                lineterm=''
            )
        elif output_format == 'html':
            html_diff = difflib.HtmlDiff()
            return html_diff.make_file(lines1, lines2, file1_path, file2_path)
        else:
            return "不支持的输出格式"
        
        return ''.join(diff)
        
    except FileNotFoundError as e:
        return f"错误: {e}"

print("示例1: 比较两个文件并生成差异报告")
# 先创建两个测试文件
with open('test1.txt', 'w', encoding='utf-8') as f:
    f.write(text1)

with open('test2.txt', 'w', encoding='utf-8') as f:
    f.write(text2)

# 比较文件
file_diff = compare_files('test1.txt', 'test2.txt')
print("文件差异:")
print(file_diff)

# 示例2: 查找最相似的字符串
def find_most_similar(target, candidates):
    """在候选字符串中查找与目标字符串最相似的"""
    best_match = None
    best_ratio = 0.0
    
    for candidate in candidates:
        ratio = difflib.SequenceMatcher(None, target, candidate).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = candidate
    
    return best_match, best_ratio

print("\n示例2: 查找最相似的字符串")
target = "python programming"
candidates = [
    "python code",
    "java programming",
    "python programming language",
    "c++ coding"
]

match, ratio = find_most_similar(target, candidates)
print(f"目标: '{target}'")
print(f"最相似的: '{match}' (相似度: {ratio:.2f})")

# 示例3: 生成差异摘要
def generate_diff_summary(text1, text2):
    """生成差异摘要"""
    lines1 = text1.splitlines()
    lines2 = text2.splitlines()
    
    differ = difflib.Differ()
    diff = list(differ.compare(lines1, lines2))
    
    # 统计差异
    added = sum(1 for line in diff if line.startswith('+'))
    removed = sum(1 for line in diff if line.startswith('-'))
    unchanged = sum(1 for line in diff if line.startswith(' '))
    
    # 生成摘要
    summary = {
        'added': added,
        'removed': removed,
        'unchanged': unchanged,
        'total': len(diff)
    }
    
    return summary, diff

print("\n示例3: 生成差异摘要")
summary, diff = generate_diff_summary(text1, text2)
print(f"差异统计:")
print(f"  添加行: {summary['added']}")
print(f"  删除行: {summary['removed']}")
print(f"  未修改行: {summary['unchanged']}")
print(f"  总行数: {summary['total']}")

# 示例4: 字符级差异高亮
def highlight_chars_diff(str1, str2):
    """高亮显示两个字符串之间的字符级差异"""
    matcher = difflib.SequenceMatcher(None, str1, str2)
    
    result = []
    pos1 = pos2 = 0
    
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'equal':
            result.append(f"{str1[i1:i2]}")
        elif tag == 'replace':
            result.append(f"[R]{str1[i1:i2]}→{str2[j1:j2]}[R]")
        elif tag == 'delete':
            result.append(f"[D]{str1[i1:i2]}[D]")
        elif tag == 'insert':
            result.append(f"[I]{str2[j1:j2]}[I]")
    
    return ''.join(result)

print("\n示例4: 字符级差异高亮")
str1 = "Python is great!"
str2 = "Python is awesome!"

highlighted = highlight_chars_diff(str1, str2)
print(f"字符串1: {str1}")
print(f"字符串2: {str2}")
print(f"差异高亮: {highlighted}")
print("[R] - 替换, [D] - 删除, [I] - 插入")

# 示例5: 生成补丁文件
def generate_patch(file1, file2, patch_file):
    """生成补丁文件"""
    with open(file1, 'r', encoding='utf-8') as f1:
        lines1 = f1.readlines()
    
    with open(file2, 'r', encoding='utf-8') as f2:
        lines2 = f2.readlines()
    
    unified_diff = difflib.unified_diff(
        lines1, lines2,
        fromfile=file1,
        tofile=file2,
        lineterm=''
    )
    
    with open(patch_file, 'w', encoding='utf-8') as f:
        f.write(''.join(unified_diff))
    
    return f"补丁文件已生成: {patch_file}"

print("\n示例5: 生成补丁文件")
print(generate_patch('test1.txt', 'test2.txt', 'changes.patch'))

# ===========================
# 10. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("10. 最佳实践")
print("=" * 50)

print("1. 选择合适的比较粒度")
print("   - 对于大文本，使用行级比较")
print("   - 对于小文本，使用字符级比较")
print("   - 根据需要选择合适的差异输出格式")

print("\n2. 处理大文件")
print("   - 分块处理大文件")
print("   - 避免一次性加载整个文件")
print("   - 使用生成器处理差异")

print("\n3. 性能优化")
print("   - 使用quick_ratio()进行快速近似比较")
print("   - 设置junk参数忽略无关字符")
print("   - 对于不需要精确结果的场景，使用real_quick_ratio()")

print("\n4. 输出格式选择")
print("   - unified_diff: 适用于命令行输出")
print("   - context_diff: 提供更多上下文信息")
print("   - HtmlDiff: 适用于Web界面显示")
print("   - Differ: 适用于简单的文本差异查看")

print("\n5. 错误处理")
print("   - 处理文件不存在的情况")
print("   - 处理编码问题")
print("   - 验证输入数据的格式")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("difflib模块提供了强大的文本差异比较功能")
print("支持多种格式的差异输出")

print("\n主要功能:")
print("- 文本行差异比较")
print("- 文本字符差异比较")
print("- 生成统一格式差异")
print("- 生成上下文格式差异")
print("- 生成HTML格式差异")
print("- 序列相似度计算")

print("\n应用场景:")
print("- 版本控制系统的差异显示")
print("- 文档对比工具")
print("- 代码审查工具")
print("- 数据同步工具")
print("- 测试结果比对")
print("- 拼写纠错和相似字符串查找")

print("\n使用difflib模块可以轻松实现文本差异的比较和处理")
print("是Python中文本处理和版本控制相关应用的重要工具")
