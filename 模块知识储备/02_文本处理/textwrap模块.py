# textwrap模块 - 文本换行和格式化
# 功能作用：提供文本换行、缩进、截断等格式化功能
# 使用情景：文本格式化、段落包装、代码文档格式化等
# 注意事项：textwrap模块适用于纯文本的格式化，不适用于HTML等标记语言

import textwrap

# 模块概述
"""
textwrap模块提供了用于格式化文本段落的功能，主要包括：
- 文本换行：将长文本分割成指定宽度的多行
- 文本缩进：为文本添加统一的缩进
- 文本修剪：移除文本前后的空白
- 文本填充：将多行文本填充成指定宽度的段落

textwrap模块特别适用于生成控制台输出、格式化日志消息、处理文档文本等场景。
"""

# 1. 基本的文本换行
print("=== 基本的文本换行 ===")

# 示例文本
long_text = "这是一个非常长的文本段落，我们需要将其换行以适应指定的宽度。文本换行在显示长文本内容时非常重要，可以提高可读性。"

# 使用fill方法进行文本换行
wrapped_text = textwrap.fill(long_text, width=40)
print(f"宽度为40的文本换行结果:\n{wrapped_text}")
print()

# 调整宽度
wrapped_text_narrow = textwrap.fill(long_text, width=20)
print(f"宽度为20的文本换行结果:\n{wrapped_text_narrow}")
print()

# 2. 文本缩进
print("=== 文本缩进 ===")

# 使用indent方法添加缩进
indented_text = textwrap.indent(long_text, '    ')
print(f"添加4个空格缩进的文本:\n{indented_text}")
print()

# 使用不同的缩进字符
indented_text_tab = textwrap.indent(long_text, '> ')
print(f"使用'> '作为缩进的文本:\n{indented_text_tab}")
print()

# 条件缩进（只缩进不以特定字符开头的行）
multi_line_text = "第一行\n- 项目1\n- 项目2\n- 项目3"
conditionally_indented = textwrap.indent(multi_line_text, '  ', lambda line: not line.startswith('-'))
print(f"条件缩进结果（只缩进不以'-'开头的行）:\n{conditionally_indented}")
print()

# 3. dedent方法 - 移除公共缩进
print("=== dedent方法 - 移除公共缩进 ===")

indented_code = """
    def example():
        print("这是一个示例函数")
        if True:
            print("条件为真")
"""

# 移除公共缩进
dedented_code = textwrap.dedent(indented_code)
print(f"原始代码（带缩进）:\n{indented_code}")
print(f"移除公共缩进后:\n{dedented_code}")
print()

# 4. 文本截断
print("=== 文本截断 ===")

# 使用shorten方法截断文本
very_long_text = "这是一段非常长的文本，我们需要将其截断以适应有限的显示空间。截断后的文本通常会在末尾添加省略号，表示被截断了。" * 3

shortened_text = textwrap.shorten(very_long_text, width=100, placeholder="...")
print(f"截断后的文本（宽度100）:\n{shortened_text}")
print()

# 调整截断宽度和占位符
shortened_text_custom = textwrap.shorten(very_long_text, width=50, placeholder="[...]继续阅读")
print(f"自定义截断（宽度50，自定义占位符）:\n{shortened_text_custom}")
print()

# 5. TextWrapper类 - 更高级的控制
print("=== TextWrapper类 - 更高级的控制 ===")

# 创建TextWrapper对象
wrapper = textwrap.TextWrapper(
    width=30,            # 每行宽度
    expand_tabs=True,    # 将制表符扩展为空格
    tabsize=4,           # 制表符宽度
    replace_whitespace=True,  # 替换空白字符为单个空格
    fix_sentence_endings=False,  # 不尝试修复句子结尾
    break_long_words=True,  # 可以在单词中间换行
    break_on_hyphens=True,  # 可以在连字符处换行
    initial_indent='',   # 第一行缩进
    subsequent_indent='',  # 后续行缩进
    wrap_algorithm='greedy'  # 换行算法
)

# 使用TextWrapper对象
wrapped_with_object = wrapper.fill(long_text)
print(f"使用TextWrapper对象的换行结果（宽度30）:\n{wrapped_with_object}")
print()

# 修改TextWrapper的属性
wrapper.width = 40
wrapper.initial_indent = "  "
wrapper.subsequent_indent = "    "

wrapped_with_indent = wrapper.fill(long_text)
print(f"修改后的TextWrapper结果（宽度40，带缩进）:\n{wrapped_with_indent}")
print()

# 6. 实际应用示例
def practical_examples():
    """演示实际应用示例"""
    print("=== 实际应用示例 ===")
    
    # 1. 创建文档段落
    def format_paragraph(paragraph, width=70):
        """格式化文档段落"""
        # 先dedent移除可能的公共缩进，再fill进行换行
        return textwrap.fill(textwrap.dedent(paragraph).strip(), width=width)
    
    doc_paragraph = """
        这是一个文档段落的示例。在编写技术文档时，我们通常希望文本具有良好的格式和可读性。
        通过使用textwrap模块，我们可以确保文档的每一行都有适当的长度，并且整体排版整洁。
    """
    
    formatted_doc = format_paragraph(doc_paragraph)
    print("格式化的文档段落:")
    print(formatted_doc)
    print()
    
    # 2. 创建带缩进的引用文本
    def format_quote(quote, author, width=60):
        """格式化引用文本"""
        wrapped_quote = textwrap.fill(quote, width=width-2)
        indented_quote = textwrap.indent(wrapped_quote, '> ')
        attribution = f"\n-- {author}"
        return indented_quote + attribution
    
    famous_quote = "生活就像骑自行车，要保持平衡，你必须不断前进。"
    author = "阿尔伯特·爱因斯坦"
    
    formatted_quote = format_quote(famous_quote, author)
    print("格式化的引用文本:")
    print(formatted_quote)
    print()
    
    # 3. 创建带缩进的列表
    def format_list(items, width=60):
        """格式化列表"""
        result = []
        for i, item in enumerate(items, 1):
            # 创建带编号的行
            line = f"{i}. {item}"
            # 使用TextWrapper进行格式化
            wrapper = textwrap.TextWrapper(
                width=width,
                initial_indent="",
                subsequent_indent="  "  # 后续行缩进
            )
            result.append(wrapper.fill(line))
        return '\n'.join(result)
    
    shopping_list = [
        "牛奶和鸡蛋",
        "面包和黄油",
        "水果（苹果、香蕉、橙子）",
        "蔬菜（西红柿、黄瓜、生菜）",
        "大米和面条，用于晚餐"
    ]
    
    formatted_list = format_list(shopping_list)
    print("格式化的列表:")
    print(formatted_list)
    print()
    
    # 4. 创建帮助文本
    def format_help_text(command, description, options, width=70):
        """格式化命令帮助文本"""
        help_text = []
        
        # 命令和描述
        header = f"{command}: {description}"
        help_text.append(textwrap.fill(header, width=width))
        help_text.append("")
        
        # 选项部分
        help_text.append("选项:")
        for option, opt_desc in options.items():
            # 格式化选项行
            option_line = f"  {option}: {opt_desc}"
            wrapper = textwrap.TextWrapper(
                width=width,
                initial_indent="",
                subsequent_indent="    "  # 选项描述的缩进
            )
            help_text.append(wrapper.fill(option_line))
        
        return '\n'.join(help_text)
    
    command_help = format_help_text(
        "format_text",
        "格式化文本为指定宽度",
        {
            "--width N": "设置输出文本的宽度，默认为70",
            "--indent N": "设置缩进空格数，默认为0",
            "--no-wrap": "不进行文本换行",
            "--truncate": "截断过长的文本"
        }
    )
    
    print("格式化的帮助文本:")
    print(command_help)
    print()
    
    # 5. 代码块格式化
    def format_code_block(code, language="python", width=80):
        """格式化代码块"""
        # 首先移除公共缩进
        dedented_code = textwrap.dedent(code).strip()
        
        # 检查代码是否需要换行（这里只是简单示例，实际代码格式化更复杂）
        lines = dedented_code.splitlines()
        formatted_lines = []
        
        for line in lines:
            if len(line) > width:
                # 这里可以根据语言特性进行更智能的换行
                # 简单处理：在逗号处换行
                parts = line.split(", ")
                wrapped_line = parts[0]
                for part in parts[1:]:
                    if len(wrapped_line + ", " + part) > width:
                        formatted_lines.append(wrapped_line + ",")
                        wrapped_line = "    " + part  # 添加缩进
                    else:
                        wrapped_line += ", " + part
                formatted_lines.append(wrapped_line)
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    sample_code = """
        def long_function_name(parameter1, parameter2, parameter3, parameter4, parameter5):
            # 这是一个带有很长参数列表的函数
            result = parameter1 + parameter2 + parameter3 + parameter4 + parameter5
            return result
    """
    
    formatted_code = format_code_block(sample_code, width=50)
    print("格式化的代码块:")
    print(formatted_code)
    print()

# 7. 高级用法和自定义
print("=== 高级用法和自定义 ===")

# 1. 自定义TextWrapper类
class CustomWrapper(textwrap.TextWrapper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def _wrap_chunks(self, chunks):
        """重写_wrap_chunks方法以自定义换行行为"""
        lines = super()._wrap_chunks(chunks)
        # 这里可以对生成的行进行额外处理
        return lines

# 使用自定义包装器
custom_wrapper = CustomWrapper(width=30)
wrapped_custom = custom_wrapper.fill(long_text)
print(f"使用自定义包装器的结果:\n{wrapped_custom}")
print()

# 2. 结合使用dedent和fill
mixed_usage = textwrap.fill(
    textwrap.dedent("""
        这是一个多行文本
        带有不同级别的缩进
        我们希望移除公共缩进
        并将其格式化为单个段落
    """).strip(),
    width=40
)
print(f"结合dedent和fill的结果:\n{mixed_usage}")
print()

# 3. 处理特殊文本格式
def format_special_text(text, width=60, bullet="•"):
    """处理带有项目符号的文本"""
    # 按行分割文本
    lines = text.splitlines()
    result = []
    
    for line in lines:
        line = line.strip()
        if line.startswith("-") or line.startswith("*") or line.startswith("•"):
            # 这是一个项目符号行
            content = line[1:].strip()
            # 创建带项目符号的格式
            wrapper = textwrap.TextWrapper(
                width=width,
                initial_indent=f"{bullet} ",
                subsequent_indent="  "
            )
            result.append(wrapper.fill(content))
        else:
            # 普通文本行
            result.append(textwrap.fill(line, width=width))
    
    return '\n'.join(result)

special_text = """
- 这是第一个项目，它包含一些详细的描述信息，可能会很长
- 这是第二个项目，同样可能包含较长的描述文本
这是一个普通的文本段落，需要正常格式化
- 这是第三个项目，继续列表
"""

formatted_special = format_special_text(special_text)
print(f"格式化的特殊文本（项目符号）:\n{formatted_special}")
print()

# 8. 注意事项和最佳实践
"""
1. **性能考虑**：
   - 对于大量文本的处理，创建TextWrapper对象并重用它比重复调用函数更高效
   - 复杂的格式化操作可能影响性能，对于非常大的文本需要考虑效率

2. **文本编码**：
   - textwrap模块适用于Unicode文本，但需要注意某些Unicode字符的宽度计算
   - 在处理非ASCII字符时，可能需要考虑字符宽度的问题

3. **不同换行算法**：
   - Python 3.6+支持多种换行算法，默认为'greedy'
   - 可以尝试不同的算法以获得更好的换行效果

4. **dedent的注意事项**：
   - dedent只移除每行共同的前导空白
   - 如果文本的行有不同的缩进级别，只会移除所有行共有的缩进部分

5. **与其他文本处理工具的结合**：
   - textwrap可以与re模块结合使用，实现更复杂的文本处理
   - 对于HTML或其他标记语言，建议使用专门的库而不是textwrap

6. **处理长单词**：
   - 对于长单词，可以设置break_long_words=False来避免在单词中间换行
   - 这种情况下，可能会产生超长行，需要额外处理

7. **句子结尾识别**：
   - fix_sentence_endings=True可以尝试识别句子结尾并进行适当的空格处理
   - 但这种识别可能不准确，特别是对于非英语文本
"""

def demonstrate_best_practices():
    """演示最佳实践"""
    print("=== 最佳实践示例 ===")
    
    # 1. 重用TextWrapper对象以提高性能
    print("重用TextWrapper对象:")
    import time
    
    # 创建一些长文本
    long_texts = [long_text * 10 for _ in range(100)]
    
    # 不重用TextWrapper
    start = time.time()
    for text in long_texts:
        textwrap.fill(text, width=50)
    time_without_reuse = time.time() - start
    print(f"不重用TextWrapper: {time_without_reuse:.6f}秒")
    
    # 重用TextWrapper
    wrapper = textwrap.TextWrapper(width=50)
    start = time.time()
    for text in long_texts:
        wrapper.fill(text)
    time_with_reuse = time.time() - start
    print(f"重用TextWrapper: {time_with_reuse:.6f}秒")
    print(f"性能提升: {(time_without_reuse/time_with_reuse):.2f}倍")
    print()
    
    # 2. 处理长单词
    print("处理长单词:")
    text_with_long_word = "这是一个包含超长单词的文本，如pneumonoultramicroscopicsilicovolcanoconiosis（一种肺部疾病），我们需要决定是否在单词中间换行。"
    
    # 默认允许在单词中间换行
    wrapper_break = textwrap.TextWrapper(width=30)
    result_break = wrapper_break.fill(text_with_long_word)
    print(f"允许在单词中间换行:\n{result_break}")
    print()
    
    # 不允许在单词中间换行
    wrapper_no_break = textwrap.TextWrapper(width=30, break_long_words=False)
    result_no_break = wrapper_no_break.fill(text_with_long_word)
    print(f"不允许在单词中间换行（可能产生超长行）:\n{result_no_break}")
    print()
    
    # 3. 处理非ASCII文本
    print("处理非ASCII文本:")
    non_ascii_text = "这是一个包含非ASCII字符的文本，如中文、日文（こんにちは）、韩文（안녕하세요）等。"
    
    wrapped_non_ascii = textwrap.fill(non_ascii_text, width=30)
    print(f"非ASCII文本换行:\n{wrapped_non_ascii}")
    print()
    
    # 4. 正确使用dedent
    print("正确使用dedent:")
    mixed_indent_text = """
        第一行有4个空格
      第二行有2个空格
        第三行有4个空格
    """
    
    print(f"原始文本:\n{mixed_indent_text}")
    dedented_mixed = textwrap.dedent(mixed_indent_text)
    print(f"dedent后:\n{dedented_mixed}")
    print("注意：dedent只移除所有行共有的前导空白，这里所有行至少有2个空格，所以只移除2个空格")
    print()
    
    # 5. 结合re模块处理复杂文本
    print("结合re模块处理复杂文本:")
    import re
    
    complex_text = "标题：示例文档\n作者：测试用户\n\n这是第一段内容。这是第二段内容，可能很长需要换行。\n\n列表：\n1. 第一项\n2. 第二项\n3. 第三项"
    
    # 使用re分割不同部分
    sections = re.split(r'\n\n+', complex_text)
    formatted_sections = []
    
    for section in sections:
        if section.startswith("标题：") or section.startswith("作者："):
            # 标题和作者部分保持原样
            formatted_sections.append(section)
        elif "列表：" in section:
            # 处理列表部分
            list_content = section.split("列表：\n")[1]
            formatted_list = format_list(list_content.split("\n"))
            formatted_sections.append("列表：\n" + formatted_list)
        else:
            # 普通文本段落进行格式化
            formatted_sections.append(textwrap.fill(section, width=40))
    
    result = "\n\n".join(formatted_sections)
    print(f"复杂文本格式化结果:\n{result}")
    print()

# 运行演示代码
if __name__ == "__main__":
    print("Python textwrap模块演示\n")
    
    # 运行基本演示
    # 实际应用示例
    practical_examples()
    # 高级用法和最佳实践
    demonstrate_best_practices()
    
    print("演示完成！")