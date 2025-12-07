# Python fnmatch模块详解

import fnmatch
import os
import glob

# 1. 模块概述
print("=== 1. fnmatch模块概述 ===")
print("fnmatch模块提供了文件名匹配功能，使用类似于Unix shell的通配符模式。")
print("该模块的主要特点：")
print("- 提供文件名的通配符匹配功能")
print("- 支持Unix shell风格的通配符模式")
print("- 提供大小写敏感和不敏感的匹配选项")
print("- 支持路径名的匹配")
print("- 可以与os模块和glob模块结合使用")
print("- 提供批量文件名匹配功能")
print("- 与Unix shell的匹配规则兼容")
print()

# 2. 通配符模式
print("=== 2. 通配符模式 ===")
print("fnmatch支持以下通配符模式：")
print("- *: 匹配任意数量的字符（包括零个字符）")
print("- ?: 匹配单个字符")
print("-[seq]: 匹配seq中的任意单个字符")
print("-[!seq]: 匹配不在seq中的任意单个字符")
print("-{a,b,c}: 匹配a、b或c中的任意一个（Python 3.11+）")
print()

# 3. fnmatch函数
print("=== 3. fnmatch函数 ===")
print("fnmatch.fnmatch(filename, pattern): 测试文件名是否匹配指定的模式")
print()

# 基本匹配示例
print("1. 基本匹配示例：")
print(f"fnmatch('file.txt', '*.txt') = {fnmatch.fnmatch('file.txt', '*.txt')}")
print(f"fnmatch('file.txt', '*.md') = {fnmatch.fnmatch('file.txt', '*.md')}")
print(f"fnmatch('file.txt', 'file.?') = {fnmatch.fnmatch('file.txt', 'file.?')}")
print(f"fnmatch('file.txt', 'file.??') = {fnmatch.fnmatch('file.txt', 'file.??')}")
print(f"fnmatch('file.txt', 'file.t?t') = {fnmatch.fnmatch('file.txt', 'file.t?t')}")

# 字符集匹配
print("\n2. 字符集匹配示例：")
print(f"fnmatch('file.txt', 'file.[tT]xt') = {fnmatch.fnmatch('file.txt', 'file.[tT]xt')}")
print(f"fnmatch('file.txt', 'file.[a-z]xt') = {fnmatch.fnmatch('file.txt', 'file.[a-z]xt')}")
print(f"fnmatch('file.txt', 'file.[!a-z]xt') = {fnmatch.fnmatch('file.txt', 'file.[!a-z]xt')}")

# 多个模式匹配（Python 3.11+）
print("\n3. 多个模式匹配示例：")
try:
    print(f"fnmatch('file.txt', 'file.{txt,md}') = {fnmatch.fnmatch('file.txt', 'file.{txt,md}')}")
    print(f"fnmatch('file.md', 'file.{txt,md}') = {fnmatch.fnmatch('file.md', 'file.{txt,md}')}")
except SyntaxError:
    print("注意：{a,b,c}模式需要Python 3.11+")

# 路径名匹配
print("\n4. 路径名匹配示例：")
print(f"fnmatch('dir/file.txt', '*.txt') = {fnmatch.fnmatch('dir/file.txt', '*.txt')}")
print(f"fnmatch('dir/file.txt', 'dir/*.txt') = {fnmatch.fnmatch('dir/file.txt', 'dir/*.txt')}")
print(f"fnmatch('dir/subdir/file.txt', 'dir/*/*.txt') = {fnmatch.fnmatch('dir/subdir/file.txt', 'dir/*/*.txt')}")
print()

# 4. fnmatchcase函数
print("=== 4. fnmatchcase函数 ===")
print("fnmatch.fnmatchcase(filename, pattern): 测试文件名是否匹配指定的模式（大小写敏感）")
print()

print("1. 大小写敏感匹配示例：")
print(f"fnmatchcase('File.txt', '*.txt') = {fnmatch.fnmatchcase('File.txt', '*.txt')}")
print(f"fnmatchcase('File.txt', '*.TXT') = {fnmatch.fnmatchcase('File.txt', '*.TXT')}")
print(f"fnmatchcase('file.TXT', '*.txt') = {fnmatch.fnmatchcase('file.TXT', '*.txt')}")

print("\n2. 与fnmatch的对比：")
print(f"fnmatch('File.txt', '*.TXT') = {fnmatch.fnmatch('File.txt', '*.TXT')}")  # 平台相关
print(f"fnmatchcase('File.txt', '*.TXT') = {fnmatch.fnmatchcase('File.txt', '*.TXT')}")  # 始终大小写敏感

print("\n3. Windows vs Unix：")
print(f"在当前平台({os.name})上：")
print(f"fnmatch('File.txt', '*.TXT') = {fnmatch.fnmatch('File.txt', '*.TXT')}")
print(f"fnmatchcase('File.txt', '*.TXT') = {fnmatch.fnmatchcase('File.txt', '*.TXT')}")
print()

# 5. filter函数
print("=== 5. filter函数 ===")
print("fnmatch.filter(names, pattern): 返回names列表中匹配pattern的所有名称")
print()

# 过滤文件名列表
print("1. 过滤文件名列表：")
file_list = [
    "file.txt",
    "file.md",
    "image.jpg",
    "document.pdf",
    "file_backup.txt",
    "archive.zip"
]

print(f"原始文件列表: {file_list}")
print(f"匹配'*.txt': {fnmatch.filter(file_list, '*.txt')}")
print(f"匹配'file*': {fnmatch.filter(file_list, 'file*')}")
print(f"匹配'*.{txt,md}'（Python 3.11+）: ", end="")
try:
    print(fnmatch.filter(file_list, '*.{txt,md}'))
except SyntaxError:
    print("需要Python 3.11+")

# 过滤目录内容
print("\n2. 过滤目录内容：")
# 创建测试文件
for f in file_list:
    open(f, 'w').close()

# 列出当前目录中的文件
current_files = os.listdir('.')
print(f"当前目录文件: {current_files}")
print(f"匹配'*.txt': {fnmatch.filter(current_files, '*.txt')}")

# 清理测试文件
for f in file_list:
    os.remove(f)
print()

# 6. translate函数
print("=== 6. translate函数 ===")
print("fnmatch.translate(pattern): 将通配符模式转换为正则表达式")
print()

# 转换通配符模式为正则表达式
print("1. 转换通配符模式：")
patterns = [
    "*.txt",
    "file.*",
    "file?.txt",
    "file[0-9].txt",
    "file[!0-9].txt",
    "dir/*/*.txt"
]

for pattern in patterns:
    regex = fnmatch.translate(pattern)
    print(f"模式: {pattern:<20} 正则表达式: {regex}")

# 使用转换后的正则表达式
print("\n2. 使用转换后的正则表达式：")
import re

pattern = "*.txt"
regex_pattern = fnmatch.translate(pattern)
regex = re.compile(regex_pattern)

print(f"模式: {pattern}")
print(f"正则表达式: {regex_pattern}")
print(f"匹配'file.txt': {bool(regex.match('file.txt'))}")
print(f"匹配'file.md': {bool(regex.match('file.md'))}")
print(f"匹配'dir/file.txt': {bool(regex.match('dir/file.txt'))}")
print()

# 7. 与glob模块的比较
print("=== 7. 与glob模块的比较 ===")
print("fnmatch和glob都提供文件名匹配功能，但有不同的用途：")
print()

print("1. fnmatch模块：")
print("   - 用于测试单个文件名是否匹配模式")
print("   - 可以过滤已有的文件名列表")
print("   - 不直接访问文件系统")
print("   - 提供大小写敏感和不敏感的匹配选项")

print("\n2. glob模块：")
print("   - 用于查找文件系统中匹配模式的文件")
print("   - 直接访问文件系统")
print("   - 返回匹配的文件路径列表")
print("   - 基于fnmatch实现")

print("\n3. 结合使用示例：")
print("   # 使用glob查找所有.txt文件")
print("   txt_files = glob.glob('*.txt')")
print("   print(txt_files)")
print()
print("   # 使用fnmatch过滤特定模式")
print("   import fnmatch")
print("   filtered = fnmatch.filter(txt_files, 'file*.txt')")
print("   print(filtered)")
print()

# 8. 实际应用示例
print("=== 8. 实际应用示例 ===")

# 示例1：批量重命名文件
def batch_rename(directory, pattern, replacement):
    """批量重命名匹配模式的文件"""
    import os
    import re
    
    # 将fnmatch模式转换为正则表达式
    regex_pattern = fnmatch.translate(pattern)
    regex = re.compile(regex_pattern)
    
    # 遍历目录中的文件
    for filename in os.listdir(directory):
        if fnmatch.fnmatch(filename, pattern):
            # 生成新文件名
            new_filename = regex.sub(replacement, filename)
            
            # 构建完整路径
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            
            # 重命名文件
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_filename}")

print("1. 批量重命名文件示例：")
# 创建测试文件
os.makedirs("test_rename", exist_ok=True)
test_files = [
    "file_01.txt",
    "file_02.txt",
    "file_03.txt",
    "image_01.jpg",
    "image_02.jpg"
]

for f in test_files:
    open(os.path.join("test_rename", f), 'w').close()

# 批量重命名
print("重命名前的文件:", os.listdir("test_rename"))
batch_rename("test_rename", "file_*.txt", "document_\g<0>")
print("重命名后的文件:", os.listdir("test_rename"))

# 清理测试文件
for f in os.listdir("test_rename"):
    os.remove(os.path.join("test_rename", f))
os.rmdir("test_rename")

# 示例2：过滤日志文件
def filter_logs(log_files, level="ERROR"):
    """过滤包含特定日志级别的日志文件"""
    import re
    
    filtered_files = []
    
    for log_file in log_files:
        # 使用fnmatch匹配日志文件
        if fnmatch.fnmatch(log_file, "*.log"):
            try:
                with open(log_file, 'r') as f:
                    content = f.read()
                    # 检查是否包含指定日志级别
                    if re.search(f"{level}", content):
                        filtered_files.append(log_file)
            except:
                pass
    
    return filtered_files

print("\n2. 过滤日志文件示例：")
# 创建测试日志文件
test_logs = [
    "app.log",
    "error.log",
    "access.log",
    "debug.log"
]

for f in test_logs:
    with open(f, 'w') as log_file:
        if f == "error.log":
            log_file.write("ERROR: Something went wrong\n")
            log_file.write("INFO: Application started\n")
        else:
            log_file.write("INFO: Application started\n")

# 过滤日志文件
print("所有日志文件:", test_logs)
print("包含ERROR级别的日志文件:", filter_logs(test_logs, "ERROR"))

# 清理测试文件
for f in test_logs:
    os.remove(f)

# 示例3：查找特定文件类型
def find_files(directory, patterns, recursive=False):
    """查找目录中匹配任意模式的文件"""
    import os
    
    found_files = []
    
    # 遍历目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件是否匹配任何模式
            for pattern in patterns:
                if fnmatch.fnmatch(file, pattern):
                    found_files.append(os.path.join(root, file))
                    break
        
        # 如果不是递归查找，只处理当前目录
        if not recursive:
            break
    
    return found_files

print("\n3. 查找特定文件类型示例：")
# 创建测试目录结构
os.makedirs("test_find/docs", exist_ok=True)
os.makedirs("test_find/images", exist_ok=True)

# 创建测试文件
test_files = [
    ("test_find", "file.txt"),
    ("test_find", "file.md"),
    ("test_find/docs", "document.pdf"),
    ("test_find/docs", "report.docx"),
    ("test_find/images", "image.jpg"),
    ("test_find/images", "image.png")
]

for dir, file in test_files:
    open(os.path.join(dir, file), 'w').close()

# 查找文件
print("查找.txt和.md文件（非递归）:")
result = find_files("test_find", ["*.txt", "*.md"], recursive=False)
for file in result:
    print(f"  {file}")

print("\n查找所有文档文件（递归）:")
result = find_files("test_find", ["*.txt", "*.md", "*.pdf", "*.docx"], recursive=True)
for file in result:
    print(f"  {file}")

# 清理测试文件和目录
for root, dirs, files in os.walk("test_find", topdown=False):
    for file in files:
        os.remove(os.path.join(root, file))
    for dir in dirs:
        os.rmdir(os.path.join(root, dir))
os.rmdir("test_find")

# 示例4：文件分类
def categorize_files(directory, categories):
    """根据模式将文件分类到不同的类别"""
    import os
    
    categorized = {category: [] for category in categories}
    categorized["other"] = []  # 未分类的文件
    
    # 遍历目录中的文件
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            categorized_file = False
            # 检查文件是否匹配任何类别模式
            for category, patterns in categories.items():
                for pattern in patterns:
                    if fnmatch.fnmatch(file, pattern):
                        categorized[category].append(file)
                        categorized_file = True
                        break
                if categorized_file:
                    break
            
            # 如果没有匹配的类别，放到other中
            if not categorized_file:
                categorized["other"].append(file)
    
    return categorized

print("\n4. 文件分类示例：")
# 创建测试文件
os.makedirs("test_categorize", exist_ok=True)
test_files = [
    "report.txt",
    "data.csv",
    "image.jpg",
    "image.png",
    "document.pdf",
    "presentation.pptx",
    "code.py",
    "code.js",
    "archive.zip",
    "notes.txt"
]

for f in test_files:
    open(os.path.join("test_categorize", f), 'w').close()

# 定义分类规则
categories = {
    "documents": ["*.txt", "*.pdf", "*.pptx"],
    "images": ["*.jpg", "*.png", "*.gif"],
    "data": ["*.csv", "*.json"],
    "code": ["*.py", "*.js", "*.java"],
    "archives": ["*.zip", "*.rar", "*.tar.gz"]
}

# 分类文件
result = categorize_files("test_categorize", categories)
for category, files in result.items():
    print(f"{category}: {files}")

# 清理测试文件和目录
for f in test_files:
    os.remove(os.path.join("test_categorize", f))
os.rmdir("test_categorize")
print()

# 9. 最佳实践
print("=== 9. 最佳实践 ===")

print("1. 使用fnmatchcase()确保跨平台一致性")
print("   # fnmatch()的大小写敏感性取决于平台")
print("   # fnmatchcase()始终大小写敏感")
print("   import fnmatch")
print("   fnmatchcase('File.txt', '*.txt')  # True")
print("   fnmatchcase('File.txt', '*.TXT')  # False")

print("\n2. 结合glob模块使用")
print("   import glob
   import fnmatch")
print("   # 使用glob查找所有.txt文件")
print("   txt_files = glob.glob('*.txt')")
print("   # 使用fnmatch进一步过滤")
print("   filtered = fnmatch.filter(txt_files, 'file*.txt')")

print("\n3. 使用translate()转换为正则表达式")
print("   import fnmatch
   import re")
print("   # 将fnmatch模式转换为正则表达式")
print("   regex_pattern = fnmatch.translate('*.txt')")
print("   regex = re.compile(regex_pattern)")
print("   # 使用正则表达式进行更复杂的匹配")
print("   matches = [f for f in files if regex.match(f)]")

print("\n4. 批量处理文件时使用filter()")
print("   import fnmatch")
print("   files = ['file.txt', 'file.md', 'image.jpg']")
print("   # 过滤出所有.txt文件")
print("   txt_files = fnmatch.filter(files, '*.txt')")

print("\n5. 使用多个模式匹配")
print("   import fnmatch")
print("   files = ['file.txt', 'file.md', 'image.jpg', 'image.png']")
print("   # 匹配.txt和.md文件")
print("   text_files = []")
print("   for file in files:")
print("       if fnmatch.fnmatch(file, '*.txt') or fnmatch.fnmatch(file, '*.md'):")
print("           text_files.append(file)")

print("\n6. 注意路径分隔符")
print("   import fnmatch")
print("   # fnmatch会将路径作为整体进行匹配")
print("   fnmatch.fnmatch('dir/file.txt', '*.txt')  # True")
print("   fnmatch.fnmatch('dir/file.txt', 'dir/*.txt')  # True")
print("   fnmatch.fnmatch('dir/subdir/file.txt', 'dir/*.txt')  # False")

print("\n7. 避免复杂的模式")
print("   # 过于复杂的fnmatch模式会降低可读性")
print("   # 考虑使用正则表达式替代")
print("   import re")
print("   # 复杂的fnmatch模式")
print("   # pattern = 'file[0-9][0-9]-[A-Z].txt'")
print("   # 对应的正则表达式")
print("   # regex = r'file\d{2}-[A-Z]\.txt'")

print("\n8. 处理文件名中的特殊字符")
print("   # 文件名中的*、?等特殊字符需要转义")
print("   import fnmatch")
print("   import re")
print("   # 使用re.escape()转义特殊字符")
print("   filename = 'file*.txt'  # 包含*的文件名")
print("   pattern = re.escape(filename)")
print("   fnmatch.fnmatch('file*.txt', pattern)  # True")
print()

# 10. 常见错误和陷阱
print("=== 10. 常见错误和陷阱 ===")

print("1. 大小写敏感性问题")
print("   # 在Windows上，fnmatch()是大小写不敏感的")
print("   # 在Unix/Linux上，fnmatch()是大小写敏感的")
print("   # 解决方法：使用fnmatchcase()确保一致性")
print("   import fnmatch")
print("   fnmatchcase('File.txt', '*.TXT')  # 始终返回False")

print("\n2. 路径分隔符处理")
print("   # fnmatch不会特殊处理路径分隔符")
print("   import fnmatch")
print("   # 这会匹配'dir/file.txt'")
print("   fnmatch.fnmatch('dir/file.txt', 'dir/*.txt')  # True")
print("   # 这不会匹配'dir/subdir/file.txt'")
print("   fnmatch.fnmatch('dir/subdir/file.txt', 'dir/*.txt')  # False")

print("\n3. 特殊字符转义")
print("   # 文件名中的*、?等特殊字符会被当作通配符处理")
print("   import fnmatch")
print("   # 这不会匹配名为'file*.txt'的文件")
print("   fnmatch.fnmatch('file*.txt', 'file*.txt')  # 可能匹配多个文件")
print("   # 解决方法：使用re.escape()转义特殊字符")

print("\n4. 空字符串匹配")
print("   # *会匹配零个或多个字符")
print("   import fnmatch")
print("   fnmatch.fnmatch('', '*')  # True")
print("   fnmatch.fnmatch('.txt', '*.txt')  # True (匹配以.txt结尾的文件)")

print("\n5. 字符集范围")
print("   # 字符集[0-9]匹配0到9之间的任意单个字符")
print("   import fnmatch")
print("   fnmatch.fnmatch('file1.txt', 'file[0-9].txt')  # True")
print("   fnmatch.fnmatch('file12.txt', 'file[0-9].txt')  # False (12是两个字符)")

print("\n6. 与正则表达式的混淆")
print("   # fnmatch模式与正则表达式不同")
print("   import fnmatch")
print("   import re")
print("   # fnmatch模式: '*.txt'")
print("   # 正则表达式: '.*\\.txt$'")
print("   # 转换方法")
print("   regex_pattern = fnmatch.translate('*.txt')")

print("\n7. 递归匹配")
print("   # fnmatch不支持递归匹配子目录")
print("   # 解决方法：结合os.walk()使用")
print("   import os
   import fnmatch")
print("   for root, dirs, files in os.walk('dir'):")
print("       for file in files:")
print("           if fnmatch.fnmatch(file, '*.txt'):")
print("               print(os.path.join(root, file))")

print("\n8. 性能问题")
print("   # 对于大量文件的匹配，fnmatch可能效率不高")
print("   # 解决方法：使用更高效的模式匹配方法")
print("   import glob
   # 使用glob直接查找文件，比fnmatch+os.walk更高效")
print("   txt_files = glob.glob('**/*.txt', recursive=True)")
print()

# 11. 总结
print("=== 11. fnmatch模块总结 ===")
print("fnmatch模块提供了文件名匹配功能，使用类似于Unix shell的通配符模式。")
print()
print("主要功能：")
print("- fnmatch(): 测试文件名是否匹配模式（大小写敏感性平台相关）")
print("- fnmatchcase(): 测试文件名是否匹配模式（始终大小写敏感）")
print("- filter(): 过滤列表中匹配模式的文件名")
print("- translate(): 将通配符模式转换为正则表达式")
print()
print("优势：")
print("- 使用简单，语法与Unix shell兼容")
print("- 提供大小写敏感和不敏感的匹配选项")
print("- 可以与其他文件操作模块结合使用")
print("- 轻量级，性能较好")
print()
print("劣势：")
print("- 功能相对简单，不支持复杂的匹配规则")
print("- 大小写敏感性取决于平台")
print("- 不直接支持递归匹配")
print("- 特殊字符处理需要额外注意")
print()
print("应用场景：")
print("- 文件名过滤和匹配")
print("- 文件分类和整理")
print("- 批量文件操作")
print("- 日志文件分析")
print("- 文件系统搜索")
print()
print("在实际开发中，fnmatch模块常用于简单的文件名匹配任务，")
print("对于复杂的匹配需求，可以考虑使用正则表达式或其他专门的文件搜索工具。")
