#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
textwrap模块 - 文本包装和格式化

textwrap模块提供了用于文本包装和格式化的功能，可以将长文本按照指定宽度自动换行，并提供了多种格式化选项。

主要功能包括：
- 文本自动换行
- 文本缩进和填充
- 段落格式化
- 去除多余空白
- 文本截断

使用场景：
- 命令行界面文本输出
- 文本报告生成
- 文档格式化
- 日志输出
- 邮件正文格式化

官方文档：https://docs.python.org/3/library/textwrap.html
"""

import textwrap

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. textwrap模块基本介绍")
print("=" * 50)
print("textwrap模块用于文本包装和格式化")
print("支持文本自动换行、缩进、填充等操作")
print("适用于各种文本排版场景")
print("可以生成美观的文本输出")

# ===========================
# 2. 基本用法
# ===========================
print("\n" + "=" * 50)
print("2. 基本用法")
print("=" * 50)

# 示例文本
long_text = "这是一段非常长的文本，需要使用textwrap模块进行包装和格式化。textwrap模块可以将长文本按照指定的宽度自动换行，使文本更易于阅读和排版。"

# 使用fill()函数进行文本包装
wrapped_text = textwrap.fill(long_text, width=40)
print("原始文本:")
print(long_text)
print("\n包装后的文本 (宽度40):")
print(wrapped_text)

# 使用wrap()函数获取换行后的列表
wrapped_lines = textwrap.wrap(long_text, width=30)
print("\nwrap()结果 (宽度30):")
for line in wrapped_lines:
    print(f"  '{line}'")

# ===========================
# 3. 文本缩进
# ===========================
print("\n" + "=" * 50)
print("3. 文本缩进")
print("=" * 50)

# 基本缩进
indented_text = textwrap.fill(long_text, width=40, initial_indent="  ", subsequent_indent="    ")
print("带缩进的文本:")
print(indented_text)

# dedent()函数去除共同缩进
indented_code = """
    def hello():
        print("Hello, World!")
        for i in range(5):
            print(i)
"""

print("\n原始代码 (带缩进):")
print(indented_code)

# 去除共同缩进
dedented_code = textwrap.dedent(indented_code)
print("dedent()后:")
print(dedented_code)

# ===========================
# 4. 文本填充
# ===========================
print("\n" + "=" * 50)
print("4. 文本填充")
print("=" * 50)

# 使用fill()函数填充文本
test_text = "Python是一种强大的编程语言，广泛应用于Web开发、数据分析、人工智能等领域。"

# 不同宽度的填充
for width in [20, 30, 40]:
    filled = textwrap.fill(test_text, width=width)
    print(f"\n宽度{width}:")
    print(filled)

# 结合缩进和填充
filled_indented = textwrap.fill(
    test_text,
    width=30,
    initial_indent="* ",
    subsequent_indent="  "
)
print("\n带缩进的填充:")
print(filled_indented)

# ===========================
# 5. 文本截断
# ===========================
print("\n" + "=" * 50)
print("5. 文本截断")
print("=" * 50)

# 使用shorten()函数截断文本
long_text = "这是一段非常长的文本，我们需要将其截断为较短的摘要。"

# 基本截断
shortened = textwrap.shorten(long_text, width=30)
print(f"原始文本: {long_text}")
print(f"截断后: {shortened}")

# 指定占位符
shortened = textwrap.shorten(long_text, width=25, placeholder="...")
print(f"截断后(自定义占位符): {shortened}")

# 不考虑单词边界
shortened = textwrap.shorten(long_text, width=25, placeholder="...", break_long_words=True)
print(f"截断后(打断单词): {shortened}")

# ===========================
# 6. 高级功能
# ===========================
print("\n" + "=" * 50)
print("6. 高级功能")
print("=" * 50)

# 使用TextWrapper类
wrapper = textwrap.TextWrapper(
    width=35,
    initial_indent="  ",
    subsequent_indent="    ",
    expand_tabs=True,
    replace_whitespace=True,
    fix_sentence_endings=True,
    break_long_words=False,
    break_on_hyphens=True
)

# 包装文本
wrapped = wrapper.wrap(long_text)
print("TextWrapper包装结果:")
for line in wrapped:
    print(line)

# 直接使用fill方法
filled = wrapper.fill(long_text)
print("\nTextWrapper.fill结果:")
print(filled)

# 配置参数
print("\nTextWrapper配置参数:")
print(f"  width: {wrapper.width}")
print(f"  initial_indent: {repr(wrapper.initial_indent)}")
print(f"  subsequent_indent: {repr(wrapper.subsequent_indent)}")
print(f"  expand_tabs: {wrapper.expand_tabs}")
print(f"  replace_whitespace: {wrapper.replace_whitespace}")
print(f"  fix_sentence_endings: {wrapper.fix_sentence_endings}")
print(f"  break_long_words: {wrapper.break_long_words}")
print(f"  break_on_hyphens: {wrapper.break_on_hyphens}")

# ===========================
# 7. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("7. 实际应用示例")
print("=" * 50)

# 示例1: 命令行帮助文本格式化
def format_help_text(help_text, width=80):
    """格式化命令行帮助文本"""
    # 创建文本包装器
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent="  ",
        subsequent_indent="    "
    )
    
    # 包装并返回
    return wrapper.fill(help_text)

print("示例1: 命令行帮助文本格式化")
help_text = "这是一个命令行工具的帮助信息，详细说明了工具的使用方法和参数选项。该工具支持多种操作模式，包括创建、删除、更新和查询功能。用户可以通过命令行参数指定操作类型和相关选项。"

print(format_help_text(help_text))

# 示例2: 生成文档段落
def generate_paragraph(text, width=60):
    """生成格式化的文档段落"""
    wrapper = textwrap.TextWrapper(
        width=width,
        fix_sentence_endings=True,
        break_long_words=False
    )
    
    return wrapper.fill(text)

print("\n示例2: 生成文档段落")
document_text = "Python是一种广泛使用的解释型、高级和通用的编程语言。Python支持多种编程范式，包括结构化编程、面向对象编程、函数式编程和命令式编程。它具有动态类型系统和垃圾回收功能，自动管理内存使用，并且其本身拥有一个巨大而广泛的标准库。"

print(generate_paragraph(document_text))

# 示例3: 代码块格式化
def format_code_block(code, width=80, indent=4):
    """格式化代码块"""
    # 去除共同缩进
    dedented = textwrap.dedent(code)
    
    # 创建文本包装器
    wrapper = textwrap.TextWrapper(
        width=width,
        break_long_words=False
    )
    
    # 包装每一行
    wrapped_lines = []
    for line in dedented.splitlines():
        if line.strip() == "":
            wrapped_lines.append("")
        else:
            wrapped_lines.extend(wrapper.wrap(line))
    
    # 添加缩进
    indented_lines = [" " * indent + line for line in wrapped_lines]
    
    return "\n".join(indented_lines)

print("\n示例3: 代码块格式化")
code_example = """
def long_function_name(parameter_one, parameter_two, parameter_three, parameter_four):
    """这是一个很长的函数定义，参数很多，需要进行格式化处理。"""
    result = parameter_one + parameter_two * parameter_three - parameter_four
    print(f"计算结果: {result}")
    return result
"""

print("原始代码:")
print(code_example)

print("\n格式化后的代码:")
print(format_code_block(code_example))

# 示例4: 生成带标题的文本块
def generate_text_block(title, content, width=70):
    """生成带标题的文本块"""
    # 生成标题行
    title_line = f"{title}:"
    separator = "=" * width
    
    # 格式化内容
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent="  ",
        subsequent_indent="    "
    )
    formatted_content = wrapper.fill(content)
    
    # 组合结果
    result = f"{separator}\n{title_line}\n{separator}\n{formatted_content}\n{separator}"
    
    return result

print("\n示例4: 生成带标题的文本块")
title = "项目介绍"
content = "这是一个使用Python开发的文本处理工具集，包含了多种文本操作功能，如文本包装、格式化、解析等。工具集提供了简单易用的API接口，方便用户进行各种文本处理操作。"

print(generate_text_block(title, content))

# 示例5: 生成列表项
def generate_list(items, width=60, bullet="- "):
    """生成格式化的列表"""
    # 创建文本包装器
    wrapper = textwrap.TextWrapper(
        width=width,
        initial_indent=bullet,
        subsequent_indent="  " * len(bullet)
    )
    
    # 包装并返回
    wrapped_items = []
    for item in items:
        wrapped_items.append(wrapper.fill(item))
    
    return "\n".join(wrapped_items)

print("\n示例5: 生成列表项")
list_items = [
    "Python是一种高级编程语言，具有简洁的语法和强大的功能。",
    "Python支持多种编程范式，包括面向对象、函数式和过程式编程。",
    "Python拥有丰富的标准库，可以满足各种开发需求。",
    "Python广泛应用于Web开发、数据分析、人工智能等领域。"
]

print(generate_list(list_items))

# ===========================
# 8. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("8. 最佳实践")
print("=" * 50)

print("1. 宽度选择")
print("   - 根据目标输出环境选择合适的宽度")
print("   - 命令行界面通常选择72-80个字符")
print("   - 文档通常选择60-70个字符")

print("\n2. 缩进使用")
print("   - 合理使用initial_indent和subsequent_indent")
print("   - 保持一致的缩进风格")
print("   - 对于列表和代码块，使用适当的缩进层次")

print("\n3. 文本处理")
print("   - 使用dedent()去除共同缩进")
print("   - 对于长单词，考虑是否需要打断")
print("   - 使用fix_sentence_endings确保句子正确结束")

print("\n4. 性能考虑")
print("   - 对于大量文本，考虑使用TextWrapper对象重复使用")
print("   - 避免在循环中重复创建TextWrapper对象")

print("\n5. 特殊场景")
print("   - 对于代码块，使用dedent()处理")
print("   - 对于列表，使用适当的项目符号和缩进")
print("   - 对于标题和分隔线，使用固定宽度")

# ===========================
# 9. 总结
# ===========================
print("\n" + "=" * 50)
print("9. 总结")
print("=" * 50)
print("textwrap模块提供了强大的文本包装和格式化功能")
print("可以生成美观易读的文本输出")

print("\n主要功能:")
print("- 文本自动换行")
print("- 文本缩进和填充")
print("- 段落格式化")
print("- 去除多余空白")
print("- 文本截断")

print("\n应用场景:")
print("- 命令行界面文本输出")
print("- 文本报告生成")
print("- 文档格式化")
print("- 日志输出")
print("- 邮件正文格式化")

print("\n使用textwrap模块可以提高文本的可读性和美观度")
print("是Python中文本处理的重要工具之一")
