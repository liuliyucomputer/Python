# markupsafe模块 - 安全的HTML和XML转义

'''
markupsafe模块提供了安全的HTML和XML转义功能，特别适用于模板系统。它提供了Markup类来标记安全的HTML内容，并提供了自动转义功能。

注意：markupsafe不是Python标准库的一部分，而是一个常用的第三方库。
'''

# 模拟markupsafe模块的核心功能
# 在实际使用中需要安装: pip install markupsafe

class Markup(str):
    """表示安全的HTML/XML内容的字符串子类"""
    
    def __new__(cls, base="", encoding=None, errors="strict"):
        if isinstance(base, Markup):
            return base
        if isinstance(base, bytes):
            if encoding is None:
                encoding = 'utf-8'
            base = base.decode(encoding, errors)
        return super().__new__(cls, base)
    
    def __add__(self, other):
        """连接两个字符串，自动转义非Markup对象"""
        if isinstance(other, Markup):
            return Markup(str(self) + str(other))
        return Markup(str(self) + escape(other))
    
    def __radd__(self, other):
        """右连接，自动转义非Markup对象"""
        if isinstance(other, Markup):
            return Markup(str(other) + str(self))
        return Markup(escape(other) + str(self))
    
    def __mod__(self, arg):
        """格式化操作，自动转义非Markup参数"""
        if isinstance(arg, tuple):
            arg = tuple(_escape_if_not_markup(x) for x in arg)
        else:
            arg = _escape_if_not_markup(arg)
        return Markup(str(self) % arg)
    
    def format(self, *args, **kwargs):
        """format方法，自动转义非Markup参数"""
        args = tuple(_escape_if_not_markup(x) for x in args)
        kwargs = {k: _escape_if_not_markup(v) for k, v in kwargs.items()}
        return Markup(super().format(*args, **kwargs))
    
    def escape(self):
        """转义自身内容"""
        return Markup(escape(str(self)))
    
    def unescape(self):
        """反转义自身内容"""
        from html import unescape
        return Markup(unescape(str(self)))
    
    def striptags(self):
        """移除HTML标签，保留纯文本"""
        import re
        stripped = re.sub(r'<[^>]*>', '', str(self))
        return Markup(stripped)

def _escape_if_not_markup(s):
    """如果不是Markup对象则转义"""
    if isinstance(s, Markup):
        return s
    return escape(s)

def escape(s):
    """转义HTML特殊字符"""
    if hasattr(s, '__html__'):
        return s.__html__()
    if not isinstance(s, str):
        s = str(s)
    return Markup(s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;'))

def soft_unicode(s):
    """将对象转换为Unicode字符串"""
    if isinstance(s, str):
        return s
    try:
        return str(s)
    except UnicodeError:
        return repr(s)

# 1. 核心功能介绍
print("=== markupsafe模块核心功能 ===")
print("- 提供安全的HTML/XML转义功能")
print("- Markup类用于标记安全的HTML内容")
print("- 支持自动转义非安全内容")
print("- 适用于模板系统中的安全内容处理")

# 2. 主要函数和类的使用
def show_markup_basic():
    """示例1: Markup类的基本使用"""
    print("\n=== Markup类基本使用 ===")
    
    # 创建Markup对象
    safe_html = Markup("<p>这是安全的HTML</p>")
    print(f"Markup对象: {safe_html}")
    
    # 普通字符串会被转义
    unsafe = "<script>alert('XSS')</script>"
    escaped = escape(unsafe)
    print(f"转义后: {escaped}")
    
    # Markup对象与普通字符串拼接
    combined = safe_html + " 添加一些 " + unsafe
    print(f"拼接后(自动转义): {combined}")

def show_formatting():
    """示例2: 格式化和模板字符串"""
    print("\n=== 格式化和模板字符串 ===")
    
    # 使用%操作符（自动转义非Markup参数）
    template = Markup("<div>%s</div>")
    user_input = "<script>危险代码</script>"
    result = template % user_input
    print(f"使用%格式化: {result}")
    
    # 使用format方法
    template2 = Markup("<div>{0} 和 {1}</div>")
    result2 = template2.format("安全内容", "<script>危险</script>")
    print(f"使用format格式化: {result2}")
    
    # 使用f-string（需要手动处理）
    safe_part = Markup("<strong>安全</strong>")
    unsafe_part = "<script>危险</script>"
    result3 = Markup(f"混合内容: {safe_part} 和 {escape(unsafe_part)}")
    print(f"使用f-string: {result3}")

def show_html_manipulation():
    """示例3: HTML操作方法"""
    print("\n=== HTML操作方法 ===")
    
    # 转义方法
    text = Markup("<p>已经是安全的</p>")
    escaped = text.escape()
    print(f"转义已安全的内容: {escaped}")
    
    # 反转义方法
    escaped_text = Markup("&lt;p&gt;转义的内容&lt;/p&gt;")
    unescaped = escaped_text.unescape()
    print(f"反转义内容: {unescaped}")
    
    # 移除标签
    html_with_tags = Markup("<p>这是<strong>加粗</strong>的文本</p>")
    plain_text = html_with_tags.striptags()
    print(f"移除标签后: {plain_text}")

def show_custom_classes():
    """示例4: 自定义具有__html__方法的类"""
    print("\n=== 自定义HTML安全类 ===")
    
    class SafeUser:
        def __init__(self, username, email):
            self.username = username
            self.email = email
        
        def __html__(self):
            """自定义HTML表示"""
            return f'<span class="user">{escape(self.username)}</span>'
    
    user = SafeUser("admin<script>", "admin@example.com")
    safe_user = escape(user)
    print(f"自定义对象的安全HTML: {safe_user}")

# 3. 使用情景
def usage_scenarios():
    print("\n=== markupsafe使用情景 ===")
    print("1. Web应用中的模板渲染，防止XSS攻击")
    print("2. 在HTML中安全地包含用户生成的内容")
    print("3. 构建动态HTML内容的安全框架")
    print("4. 与Jinja2、Flask等框架配合使用")
    print("5. 生成XML文档时的安全处理")

# 4. 注意事项
def notes():
    print("\n=== markupsafe注意事项 ===")
    print("1. markupsafe是第三方库，需要使用pip install markupsafe安装")
    print("2. 不要随意将不可信的内容标记为安全（使用Markup()包装）")
    print("3. 在使用f-string时，需要显式调用escape()函数处理不安全内容")
    print("4. 对于复杂的HTML处理，可能需要结合其他库如BeautifulSoup")
    print("5. striptags()方法只是简单移除标签，不保证完全清除所有潜在的XSS威胁")

# 5. 综合示例 - 简单的模板渲染器
def comprehensive_example():
    """综合示例：简单的安全模板渲染器"""
    class SimpleTemplateRenderer:
        """简单的模板渲染器，使用markupsafe保证安全"""
        
        def render_template(self, template, **context):
            """渲染模板，自动转义上下文变量"""
            # 转义所有上下文变量
            safe_context = {}
            for key, value in context.items():
                if isinstance(value, Markup):
                    safe_context[key] = value
                else:
                    safe_context[key] = escape(value)
            
            # 创建安全的模板字符串
            safe_template = Markup(template)
            
            # 格式化模板
            return safe_template.format(**safe_context)
    
    # 使用示例
    renderer = SimpleTemplateRenderer()
    
    print("\n=== 安全模板渲染器示例 ===")
    
    # 定义模板
    user_template = """
    <div class="user-profile">
        <h2>{username}</h2>
        <p>Email: {email}</p>
        <p>Bio: {bio}</p>
        <div class="custom-html">{custom_html}</div>
    </div>
    """
    
    # 渲染模板
    result = renderer.render_template(
        user_template,
        username="hacker<script>",
        email="hacker@example.com",
        bio="I love <script>alert('XSS')</script>",
        custom_html=Markup("<p>这是<strong>安全</strong>的HTML</p>")
    )
    
    print(f"渲染结果:\n{result}")

# 执行示例
if __name__ == "__main__":
    show_markup_basic()
    show_formatting()
    show_html_manipulation()
    show_custom_classes()
    usage_scenarios()
    notes()
    comprehensive_example()
