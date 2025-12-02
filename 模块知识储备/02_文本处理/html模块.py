# html模块 - HTML实体处理和转义

'''
html模块提供了用于处理HTML实体的函数，可以进行HTML文本的转义和反转义，避免在处理HTML内容时出现语法错误。
'''

import html

# 1. 核心功能介绍
print("=== html模块核心功能 ===")
print("- 将普通文本中的特殊字符转义为HTML实体")
print("- 将HTML实体反转义回普通文本")
print("- 处理HTML字符引用")

# 2. 主要函数
def show_escape_unescape():
    """示例1: 基本的转义和反转义"""
    # 原始文本包含HTML特殊字符
    text = '<script>alert("XSS攻击");</script>'
    
    print("\n=== 基本转义示例 ===")
    print(f"原始文本: {text}")
    
    # 转义HTML特殊字符
    escaped = html.escape(text)
    print(f"转义后: {escaped}")
    
    # 反转义HTML实体
    unescaped = html.unescape(escaped)
    print(f"反转义后: {unescaped}")

def show_escape_attributes():
    """示例2: 转义HTML属性值"""
    # 需要在HTML属性中使用的值
    attr_value = 'John "Smith" & Sons'
    
    print("\n=== 属性转义示例 ===")
    print(f"原始属性值: {attr_value}")
    
    # 转义HTML属性值（引号也被转义）
    escaped_attr = html.escape(attr_value, quote=True)
    print(f"转义后: {escaped_attr}")
    
    # 模拟生成HTML标签
    html_tag = f'<div data-name="{escaped_attr}">内容</div>'
    print(f"生成的HTML标签: {html_tag}")

def show_unescape_entities():
    """示例3: 反转义各种HTML实体"""
    # 包含不同类型HTML实体的文本
    entity_text = '''
    &lt;p&gt;这是一个段落&lt;/p&gt;
    &amp; 表示 & 符号
    &quot; 表示 引号
    &apos; 表示 单引号
    &lt; &gt; 表示 尖括号
    &eacute; 表示 é
    &#x2603; 表示 ☃
    &#9731; 表示 ★
    '''
    
    print("\n=== 实体反转义示例 ===")
    print(f"包含实体的文本:\n{entity_text}")
    
    # 反转义所有HTML实体
    unescaped = html.unescape(entity_text)
    print(f"反转义后:\n{unescaped}")

def show_mixed_content():
    """示例4: 处理混合内容"""
    # 混合了HTML标签和实体的内容
    mixed_content = '''
    <h1>Python &amp; HTML处理</h1>
    <p>这是一个包含&amp;lt;script&amp;gt;标签的示例，确保安全显示。</p>
    <div data-info="数据包含&amp;quot;引号&amp;quot;和&amp;amp;符号"></div>
    '''
    
    print("\n=== 混合内容处理 ===")
    print(f"原始混合内容:\n{mixed_content}")
    
    # 反转义内容
    unescaped = html.unescape(mixed_content)
    print(f"反转义后:\n{unescaped}")
    
    # 只转义文本部分，保留HTML结构（这需要更复杂的处理）
    # 简单演示如何重新转义部分内容
    simple_text = "我需要转义 < > & 这些符号"
    print(f"\n对普通文本转义: {html.escape(simple_text)}")

# 3. 使用情景
def usage_scenarios():
    print("\n=== html模块使用情景 ===")
    print("1. 防止XSS（跨站脚本）攻击，确保用户输入安全显示")
    print("2. 生成有效的HTML内容，确保特殊字符正确显示")
    print("3. 解析和处理HTML内容时的实体转换")
    print("4. 在网页模板中安全地插入动态内容")
    print("5. 处理从数据库或文件读取的可能包含HTML实体的文本")
    print("6. 构建API返回的HTML格式响应")

# 4. 注意事项
def notes():
    print("\n=== html模块注意事项 ===")
    print("1. html.escape()默认只转义<>&三个字符，quote=True参数会额外转义引号")
    print("2. html.unescape()可以处理命名实体(&amp;)、十进制实体(&#38;)和十六进制实体(&#x26;)")
    print("3. 对于需要保留HTML结构同时转义文本内容的情况，建议使用专用的HTML解析库如BeautifulSoup")
    print("4. 在Web应用中，始终对用户输入进行适当的转义处理，防止XSS攻击")
    print("5. 注意html模块不提供完整的HTML解析功能，仅处理实体转义")

# 5. 综合示例
def comprehensive_example():
    """综合示例：构建一个简单的安全HTML生成器"""
    class SimpleHTMLBuilder:
        """简单的HTML生成器，自动处理转义"""
        
        def create_element(self, tag, content='', **attrs):
            """创建HTML元素"""
            # 构建属性字符串
            attrs_str = ''
            for attr, value in attrs.items():
                attrs_str += f' {attr}="{html.escape(value, quote=True)}"'
            
            # 转义内容
            escaped_content = html.escape(content)
            
            return f'<{tag}{attrs_str}>{escaped_content}</{tag}>'
        
        def create_unescaped_element(self, tag, content='', **attrs):
            """创建HTML元素，内容不转义（谨慎使用）"""
            attrs_str = ''
            for attr, value in attrs.items():
                attrs_str += f' {attr}="{html.escape(value, quote=True)}"'
            
            return f'<{tag}{attrs_str}>{content}</{tag}>'
    
    # 使用示例
    builder = SimpleHTMLBuilder()
    
    print("\n=== 安全HTML生成器示例 ===")
    
    # 安全处理用户输入
    user_input = '<script>alert("危险操作");</script>'
    paragraph = builder.create_element('p', f'用户输入: {user_input}')
    print(f"安全段落元素:\n{paragraph}")
    
    # 创建带属性的元素
    link = builder.create_element('a', '访问Python官网', href='https://python.org', title='Python & 编程')
    print(f"\n链接元素:\n{link}")
    
    # 创建表格行
    row = builder.create_element('tr')
    cell1 = builder.create_element('td', '数据1')
    cell2 = builder.create_element('td', '数据2 > 数据1')
    
    print(f"\n表格单元格:\n{cell1}\n{cell2}")

# 执行示例
if __name__ == "__main__":
    show_escape_unescape()
    show_escape_attributes()
    show_unescape_entities()
    show_mixed_content()
    usage_scenarios()
    notes()
    comprehensive_example()
