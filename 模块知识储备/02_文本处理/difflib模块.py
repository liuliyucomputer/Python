# difflib模块 - 计算序列间的差异和相似性

'''
difflib模块提供了用于比较序列（如文本、列表等）的类和函数，帮助用户找出序列之间的差异、生成差异报告，以及创建相似性比较。
'''

import difflib

# 1. 核心功能介绍
print("=== difflib模块核心功能 ===")
print("- 计算文本差异并生成各种格式的差异报告")
print("- 查找相似或匹配的项")
print("- 计算序列的相似度")

# 2. 主要类和函数
def show_diff_example():
    """示例1: 生成文本差异比较"""
    text1 = ['我喜欢Python', 'Python是一种很好的编程语言', '它很容易学习']
    text2 = ['我非常喜欢Python', 'Python是一种强大的编程语言', '它很容易且有趣']
    
    # 创建差异生成器
    d = difflib.Differ()
    diff = list(d.compare(text1, text2))
    
    print("\n=== 文本差异比较 ===")
    print('\n'.join(diff))
    
    # 生成统一格式的差异（unified diff）
    diff = difflib.unified_diff(text1, text2, fromfile='original.txt', tofile='modified.txt')
    print("\n=== 统一格式差异 ===")
    print('\n'.join(diff))

def show_get_close_matches():
    """示例2: 查找最接近的匹配项"""
    words = ['apple', 'banana', 'orange', 'peach', 'pear']
    
    # 查找相似的单词
    print("\n=== 查找相似匹配 ===")
    print(f"'appel'的相似匹配: {difflib.get_close_matches('appel', words)}")
    print(f"'bananna'的相似匹配: {difflib.get_close_matches('bananna', words)}")
    print(f"'oragne'的相似匹配: {difflib.get_close_matches('oragne', words)}")
    
    # 指定n参数限制返回数量
    print(f"'ap'的前2个相似匹配: {difflib.get_close_matches('ap', words, n=2)}")

def show_sequence_matcher():
    """示例3: 使用SequenceMatcher计算序列相似度"""
    s1 = 'Python编程'
    s2 = 'Python编程学习'
    
    # 创建序列匹配器
    matcher = difflib.SequenceMatcher(None, s1, s2)
    
    print("\n=== 序列相似度 ===")
    print(f"两个字符串的相似度: {matcher.ratio():.2f}")
    
    # 获取匹配的块
    print("匹配块:")
    for block in matcher.get_matching_blocks():
        i, j, size = block
        print(f"  位置 ({i}, {j}), 长度: {size}, 匹配文本: '{s1[i:i+size]}'")

def show_html_diff():
    """示例4: 生成HTML格式的差异报告"""
    text1 = 'Python是一种编程语言。\n它很流行。'
    text2 = 'Python是一种强大的编程语言。\n它非常流行。'
    
    # 生成HTML差异
    d = difflib.HtmlDiff()
    html_diff = d.make_file(text1.splitlines(), text2.splitlines())
    
    print("\n=== HTML差异报告（前100个字符） ===")
    print(html_diff[:100] + '...')

# 3. 使用情景
def usage_scenarios():
    print("\n=== difflib使用情景 ===")
    print("1. 版本控制系统中的代码比较")
    print("2. 拼写检查和自动更正建议")
    print("3. 文本文件的变更追踪")
    print("4. 相似项目的查找和去重")
    print("5. 生成代码审查报告")

# 4. 注意事项
def notes():
    print("\n=== difflib注意事项 ===")
    print("1. 对于非常大的文本，计算差异可能会消耗大量内存和时间")
    print("2. get_close_matches的相似度阈值默认为0.6，可以通过cutoff参数调整")
    print("3. SequenceMatcher在处理空格和换行符时可能需要额外的处理")
    print("4. HTML差异报告需要在浏览器中查看才能正确显示格式")
    print("5. 对于二进制数据，应该先转换为适当的格式再进行比较")

# 5. 综合示例
def comprehensive_example():
    """综合示例：比较两个版本的代码并提供相似性分析"""
    old_code = '''
def calculate_sum(a, b):
    """计算两个数的和"""
    return a + b

def calculate_product(a, b):
    """计算两个数的积"""
    return a * b
'''
    
    new_code = '''
def calculate_sum(a, b):
    """计算两个数的和"""
    return a + b

def calculate_product(a, b):
    """计算两个数的积"""
    return a * b

def calculate_difference(a, b):
    """计算两个数的差"""
    return a - b
'''
    
    # 计算相似度
    matcher = difflib.SequenceMatcher(None, old_code, new_code)
    
    print("\n=== 代码版本比较综合示例 ===")
    print(f"版本相似度: {matcher.ratio():.2f}")
    
    # 显示差异
    diff = difflib.unified_diff(
        old_code.splitlines(), 
        new_code.splitlines(),
        fromfile='v1.py', 
        tofile='v2.py'
    )
    print("\n代码变更:")
    print('\n'.join(diff))

# 执行示例
if __name__ == "__main__":
    show_diff_example()
    show_get_close_matches()
    show_sequence_matcher()
    show_html_diff()
    usage_scenarios()
    notes()
    comprehensive_example()
