# Python glob模块详解

import glob
import os
import fnmatch

# 1. 模块概述
print("=== 1. glob模块概述 ===")
print("glob模块提供了文件模式匹配功能，用于查找符合特定模式的文件路径名。")
print("该模块的主要特点：")
print("- 支持Unix风格的路径模式扩展")
print("- 提供通配符匹配功能，包括*、?和[]")
print("- 支持递归匹配（Python 3.5+）")
print("- 返回匹配的文件路径列表")
print("- 可以结合正则表达式使用")
print("- 与os模块和pathlib模块良好集成")
print()

# 2. 基本通配符
print("=== 2. 基本通配符 ===")

print("glob模块支持的通配符：")
print("- *：匹配任意数量的字符，不包括路径分隔符")
print("- ?：匹配单个字符，不包括路径分隔符")
print("- []：匹配括号内的任意单个字符，不包括路径分隔符")
print("- [!]：匹配不在括号内的任意单个字符，不包括路径分隔符")
print()

# 3. 基本用法
print("=== 3. 基本用法 ===")

# 创建测试文件结构
os.makedirs("test_glob", exist_ok=True)
os.makedirs("test_glob/subdir1", exist_ok=True)
os.makedirs("test_glob/subdir2", exist_ok=True)

# 创建测试文件
files = [
    "test_glob/file1.txt",
    "test_glob/file2.txt",
    "test_glob/file3.md",
    "test_glob/doc1.txt",
    "test_glob/doc2.txt",
    "test_glob/subdir1/file4.txt",
    "test_glob/subdir1/image1.jpg",
    "test_glob/subdir2/file5.txt",
    "test_glob/subdir2/image2.jpg",
    "test_glob/a.txt",
    "test_glob/b.txt",
    "test_glob/c.py",
    "test_glob/aa.txt",
    "test_glob/bb.txt",
    "test_glob/cc.py"
]

for file_path in files:
    with open(file_path, "w") as f:
        f.write("test content")

# 使用*匹配所有文件
print("1. 使用*匹配所有文件：")
all_files = glob.glob("test_glob/*")
print(f"glob.glob('test_glob/*') = {all_files}")

# 使用*.txt匹配所有txt文件
print("\n2. 使用*.txt匹配所有txt文件：")
txt_files = glob.glob("test_glob/*.txt")
print(f"glob.glob('test_glob/*.txt') = {txt_files}")

# 使用file*匹配所有以file开头的文件
print("\n3. 使用file*匹配所有以file开头的文件：")
file_files = glob.glob("test_glob/file*")
print(f"glob.glob('test_glob/file*') = {file_files}")

# 使用?匹配单个字符
print("\n4. 使用?匹配单个字符：")
single_char = glob.glob("test_glob/?.txt")
print(f"glob.glob('test_glob/?.txt') = {single_char}")

# 使用[]匹配指定字符
print("\n5. 使用[]匹配指定字符：")
spec_char = glob.glob("test_glob/[ab].txt")
print(f"glob.glob('test_glob/[ab].txt') = {spec_char}")

# 使用[!]匹配不在指定范围内的字符
print("\n6. 使用[!]匹配不在指定范围内的字符：")
not_spec = glob.glob("test_glob/[!ab].txt")
print(f"glob.glob('test_glob/[!ab].txt') = {not_spec}")

# 使用[a-z]匹配字母范围
print("\n7. 使用[a-z]匹配字母范围：")
alpha_range = glob.glob("test_glob/[a-z].txt")
print(f"glob.glob('test_glob/[a-z].txt') = {alpha_range}")

# 使用[0-9]匹配数字范围
print("\n8. 使用[0-9]匹配数字范围：")
numeric_range = glob.glob("test_glob/file[0-9].txt")
print(f"glob.glob('test_glob/file[0-9].txt') = {numeric_range}")
print()

# 4. 递归匹配
print("=== 4. 递归匹配 ===")

# 使用**进行递归匹配（Python 3.5+）
print("1. 使用**进行递归匹配所有txt文件：")
recursive_txt = glob.glob("test_glob/**/*.txt", recursive=True)
print(f"glob.glob('test_glob/**/*.txt', recursive=True) = {recursive_txt}")

# 递归匹配所有文件
print("\n2. 递归匹配所有文件：")
recursive_all = glob.glob("test_glob/**/*", recursive=True)
print(f"glob.glob('test_glob/**/*', recursive=True) = {recursive_all}")

# 递归匹配特定目录下的文件
print("\n3. 递归匹配subdir开头的目录下的jpg文件：")
recursive_subdir = glob.glob("test_glob/**/subdir*/image*.jpg", recursive=True)
print(f"glob.glob('test_glob/**/subdir*/image*.jpg', recursive=True) = {recursive_subdir}")
print()

# 5. 不区分大小写匹配
print("=== 5. 不区分大小写匹配 ===")

# 创建大小写混合的文件
os.makedirs("test_case", exist_ok=True)
with open("test_case/File.txt", "w") as f:
    f.write("test content")
with open("test_case/DOC.txt", "w") as f:
    f.write("test content")
with open("test_case/image.jpg", "w") as f:
    f.write("test content")
with open("test_case/IMAGE.PNG", "w") as f:
    f.write("test content")

# 使用fnmatch结合glob实现不区分大小写匹配
print("1. 使用fnmatch结合glob实现不区分大小写匹配：")
import fnmatch
case_insensitive = [f for f in glob.glob("test_case/*") if fnmatch.fnmatch(f, "test_case/*[Ff][Ii][Ll][Ee]*")]
print(f"不区分大小写匹配file：{case_insensitive}")

# 使用os.listdir和fnmatch实现不区分大小写匹配
print("\n2. 使用os.listdir和fnmatch实现不区分大小写匹配：")
files = os.listdir("test_case")
case_insensitive = [f for f in files if fnmatch.fnmatchcase(f, "*.TXT")]
print(f"区分大小写匹配*.TXT：{case_insensitive}")

case_insensitive = [f for f in files if fnmatch.fnmatch(f, "*.TXT")]
print(f"不区分大小写匹配*.TXT：{case_insensitive}")

# 使用正则表达式实现不区分大小写匹配
print("\n3. 使用正则表达式实现不区分大小写匹配：")
import re
pattern = re.compile(r"^image\.(jpg|png)$", re.IGNORECASE)
case_insensitive = [f for f in files if pattern.match(f)]
print(f"不区分大小写匹配image.jpg或image.png：{case_insensitive}")
print()

# 6. 排序匹配结果
print("=== 6. 排序匹配结果 ===")

# 匹配结果默认顺序可能不确定
print("1. 默认匹配顺序：")
txt_files = glob.glob("test_glob/*.txt")
print(f"glob.glob('test_glob/*.txt') = {txt_files}")

# 手动排序匹配结果
print("\n2. 手动排序匹配结果：")
txt_files_sorted = sorted(glob.glob("test_glob/*.txt"))
print(f"sorted(glob.glob('test_glob/*.txt')) = {txt_files_sorted}")

# 按修改时间排序
print("\n3. 按文件修改时间排序：")
txt_files = glob.glob("test_glob/*.txt")
txt_files_sorted_by_mtime = sorted(txt_files, key=os.path.getmtime)
print(f"按修改时间排序：{txt_files_sorted_by_mtime}")

# 按文件大小排序
print("\n4. 按文件大小排序：")
txt_files_sorted_by_size = sorted(txt_files, key=os.path.getsize)
print(f"按文件大小排序：{txt_files_sorted_by_size}")

# 逆序排序
print("\n5. 逆序排序：")
txt_files_reverse = sorted(glob.glob("test_glob/*.txt"), reverse=True)
print(f"逆序排序：{txt_files_reverse}")
print()

# 7. 与pathlib模块结合使用
print("=== 7. 与pathlib模块结合使用 ===")

from pathlib import Path

# 使用pathlib的glob方法
print("1. 使用pathlib的glob方法：")
p = Path("test_glob")
for file in p.glob("*.txt"):
    print(f"  {file}")

# 使用pathlib的rglob方法（递归匹配）
print("\n2. 使用pathlib的rglob方法：")
for file in p.rglob("*.txt"):
    print(f"  {file}")

# 比较glob模块和pathlib模块
print("\n3. 比较glob模块和pathlib模块：")
glob_result = glob.glob("test_glob/*.txt")
pathlib_result = list(p.glob("*.txt"))

print(f"glob模块结果类型：{type(glob_result[0]) if glob_result else None}")
print(f"pathlib模块结果类型：{type(pathlib_result[0]) if pathlib_result else None}")

# 使用pathlib的相对路径
print("\n4. 使用pathlib的相对路径：")
relative_path = Path(".") / "test_glob"
for file in relative_path.glob("*.txt"):
    print(f"  {file}")
print()

# 8. 高级用法
print("=== 8. 高级用法 ===")

# 匹配隐藏文件
print("1. 匹配隐藏文件：")
# 创建隐藏文件
with open("test_glob/.hidden.txt", "w") as f:
    f.write("hidden content")

# 匹配所有隐藏文件
hidden_files = glob.glob("test_glob/.*")
print(f"glob.glob('test_glob/.*') = {hidden_files}")

# 匹配隐藏的txt文件
hidden_txt = glob.glob("test_glob/.?.txt") + glob.glob("test_glob/.*.txt")
print(f"隐藏的txt文件：{hidden_txt}")

# 匹配特定长度的文件名
print("\n2. 匹配特定长度的文件名：")
# 匹配3个字符的txt文件
specific_length = glob.glob("test_glob/???/*.txt")
print(f"3个字符目录下的txt文件：{specific_length}")

# 匹配多种扩展名
print("\n3. 匹配多种扩展名：")
multi_ext = []
extensions = ["*.txt", "*.md", "*.py"]
for ext in extensions:
    multi_ext.extend(glob.glob(f"test_glob/{ext}"))
print(f"多种扩展名的文件：{multi_ext}")

# 使用glob.iglob进行迭代匹配
print("\n4. 使用glob.iglob进行迭代匹配：")
print("glob.iglob('test_glob/*.txt')返回迭代器：")
for file in glob.iglob("test_glob/*.txt"):
    print(f"  {file}")

# 使用glob.iglob递归匹配
print("\n5. 使用glob.iglob递归匹配：")
print("glob.iglob('test_glob/**/*.txt', recursive=True)返回迭代器：")
for file in glob.iglob("test_glob/**/*.txt", recursive=True):
    print(f"  {file}")
print()

# 9. 性能考虑
print("=== 9. 性能考虑 ===")

print("1. 匹配大量文件时的性能：")
print("   - 使用glob.iglob()代替glob.glob()可以减少内存使用")
print("   - 避免过度使用递归匹配(**)，因为它会遍历所有子目录")
print("   - 尽可能缩小匹配范围，避免全局匹配")

print("\n2. 内存使用比较：")
print("   - glob.glob()：返回所有匹配结果的列表，占用较多内存")
print("   - glob.iglob()：返回迭代器，逐个生成匹配结果，占用较少内存")

print("\n3. 递归匹配的性能：")
print("   - 递归匹配会遍历所有子目录，可能影响性能")
print("   - 只在必要时使用recursive=True")

print("\n4. 替代方案：")
print("   - 对于复杂的匹配需求，可以考虑使用os.walk()")
print("   - 对于非常复杂的模式，可以结合正则表达式使用")
print()

# 10. 实际应用示例
print("=== 10. 实际应用示例 ===")

# 示例1：批量处理特定类型的文件
def batch_process_files(directory, pattern, process_func):
    """批量处理匹配特定模式的文件"""
    for file_path in glob.glob(f"{directory}/{pattern}"):
        print(f"处理文件：{file_path}")
        process_func(file_path)

# 定义处理函数
def process_file(file_path):
    """简单的文件处理函数"""
    with open(file_path, "a") as f:
        f.write("\nProcessed by batch_process_files")

print("1. 批量处理文件示例：")
batch_process_files("test_glob", "*.txt", process_file)
print("文件已处理")

# 示例2：统计特定类型文件的数量和大小
def count_and_size(directory, pattern):
    """统计匹配特定模式的文件数量和总大小"""
    files = glob.glob(f"{directory}/{pattern}")
    count = len(files)
    total_size = sum(os.path.getsize(f) for f in files)
    return count, total_size

print("\n2. 统计文件示例：")
count, size = count_and_size("test_glob", "*.txt")
print(f"txt文件数量：{count}")
print(f"txt文件总大小：{size} bytes")

# 示例3：查找最近修改的文件
def find_recent_files(directory, pattern, n=5):
    """查找最近修改的n个文件"""
    files = glob.glob(f"{directory}/{pattern}")
    # 按修改时间排序（最新的在前）
    files_sorted = sorted(files, key=os.path.getmtime, reverse=True)
    return files_sorted[:n]

print("\n3. 查找最近修改的文件示例：")
recent_files = find_recent_files("test_glob", "*.txt", 3)
print("最近修改的3个txt文件：")
for file in recent_files:
    mtime = os.path.getmtime(file)
    print(f"  {file} - 修改时间：{mtime}")

# 示例4：递归查找空文件
def find_empty_files(directory):
    """递归查找空文件"""
    empty_files = []
    for file_path in glob.iglob(f"{directory}/**/*", recursive=True):
        if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
            empty_files.append(file_path)
    return empty_files

print("\n4. 查找空文件示例：")
empty_files = find_empty_files("test_glob")
print(f"空文件：{empty_files}")

# 示例5：批量重命名文件
def batch_rename(directory, pattern, new_pattern):
    """批量重命名匹配特定模式的文件"""
    import re
    
    for file_path in glob.glob(f"{directory}/{pattern}"):
        filename = os.path.basename(file_path)
        directory_path = os.path.dirname(file_path)
        
        # 使用正则表达式替换文件名
        new_filename = re.sub(pattern.split("*")[-1], new_pattern, filename)
        new_file_path = os.path.join(directory_path, new_filename)
        
        os.rename(file_path, new_file_path)
        print(f"重命名：{file_path} -> {new_file_path}")

print("\n5. 批量重命名文件示例：")
batch_rename("test_glob", "file*.txt", "newfile{}.txt")
print("文件已重命名")
print()

# 11. 最佳实践
print("=== 11. 最佳实践 ===")

print("1. 始终使用绝对路径进行匹配")
print("   # 推荐:")
print("   import os")
print("   directory = os.path.abspath('path/to/dir')")
print("   files = glob.glob(os.path.join(directory, '*.txt'))")
print("   # 不推荐:")
print("   files = glob.glob('path/to/dir/*.txt')  # 相对路径可能不稳定")

print("\n2. 使用glob.iglob()处理大量文件")
print("   for file in glob.iglob('large_directory/*.txt'):")
print("       # 处理文件")

print("\n3. 结合os.path模块使用")
print("   for file in glob.glob('*.txt'):")
print("       if os.path.isfile(file):")
print("           # 确保是文件而不是目录")

print("\n4. 对匹配结果进行排序")
print("   files = sorted(glob.glob('*.txt'))")

print("\n5. 避免过度使用递归匹配")
print("   # 只在必要时使用")
print("   files = glob.glob('directory/**/*.txt', recursive=True)")

print("\n6. 使用正则表达式处理复杂模式")
print("   import re")
print("   pattern = re.compile(r'^file\d+\.txt$')")
print("   files = [f for f in os.listdir('.') if pattern.match(f)]")

print("\n7. 考虑使用pathlib模块")
print("   from pathlib import Path")
print("   files = list(Path('directory').glob('*.txt'))")

print("\n8. 处理隐藏文件时要特别注意")
print("   hidden_files = glob.glob('.*')  # 匹配所有隐藏文件和目录")
print("   hidden_files = [f for f in glob.glob('.*') if os.path.isfile(f)]  # 只匹配隐藏文件")

print("\n9. 处理多种扩展名时使用循环")
print("   extensions = ['*.txt', '*.md', '*.py']")
print("   files = []")
print("   for ext in extensions:")
print("       files.extend(glob.glob(ext))")

print("\n10. 使用异常处理包装文件操作")
print("   try:")
print("       files = glob.glob('path/to/files/*.txt')")
print("   except Exception as e:")
print("       print(f'Error: {e}')")
print()

# 12. 常见错误和陷阱
print("=== 12. 常见错误和陷阱 ===")

print("1. 路径分隔符问题")
print("   # 错误:")
print("   files = glob.glob('path/to/dir/*.txt')  # 在Windows上可能不工作")
print("   # 正确:")
print("   import os")
print("   files = glob.glob(os.path.join('path', 'to', 'dir', '*.txt'))")

print("\n2. 忘记处理子目录")
print("   # 错误:")
print("   files = glob.glob('dir/*.txt')  # 只匹配dir目录下的txt文件")
print("   # 正确:")
print("   files = glob.glob('dir/**/*.txt', recursive=True)  # 匹配所有子目录下的txt文件")

print("\n3. 匹配结果包含目录")
print("   # 错误:")
print("   for file in glob.glob('dir/*'):")
print("       with open(file) as f:  # 如果file是目录会抛出异常")
print("           # 处理文件")
print("   # 正确:")
print("   for file in glob.glob('dir/*'):")
print("       if os.path.isfile(file):")
print("           with open(file) as f:")
print("               # 处理文件")

print("\n4. 递归匹配性能问题")
print("   # 错误:")
print("   files = glob.glob('large_directory/**/*', recursive=True)  # 可能很慢")
print("   # 正确:")
print("   files = []")
print("   for root, dirs, filenames in os.walk('large_directory'):")
print("       for filename in filenames:")
print("           if filename.endswith('.txt'):")
print("               files.append(os.path.join(root, filename))")

print("\n5. 不区分大小写匹配问题")
print("   # 错误:")
print("   files = glob.glob('*.TXT')  # 只匹配大写TXT文件")
print("   # 正确:")
print("   import fnmatch")
print("   files = [f for f in os.listdir('.') if fnmatch.fnmatch(f, '*.TXT')]")

print("\n6. 路径包含特殊字符")
print("   # 错误:")
print("   files = glob.glob('dir/[abc].txt')  # 如果目录包含[]会抛出异常")
print("   # 正确:")
print("   import re")
print("   pattern = re.compile(r'dir/\[abc\]\.txt')")
print("   files = [f for f in os.listdir('.') if pattern.match(f)]")

print("\n7. 匹配隐藏文件")
print("   # 错误:")
print("   files = glob.glob('*.txt')  # 不会匹配隐藏文件")
print("   # 正确:")
print("   files = glob.glob('.*.txt')  # 匹配隐藏的txt文件")
print("   files = [f for f in glob.glob('.*') if os.path.isfile(f)]  # 匹配所有隐藏文件")

print("\n8. 匹配结果顺序不确定")
print("   # 错误:")
print("   files = glob.glob('*.txt')")
print("   print(files[0])  # 顺序可能变化")
print("   # 正确:")
print("   files = sorted(glob.glob('*.txt'))")
print("   print(files[0])  # 顺序确定")
print()

# 13. 清理测试文件
print("=== 13. 清理测试文件 ===")

# 清理test_glob目录
def remove_directory(directory):
    """递归删除目录"""
    import shutil
    try:
        shutil.rmtree(directory)
        print(f"目录 {directory} 已删除")
    except Exception as e:
        print(f"删除目录 {directory} 失败: {e}")

remove_directory("test_glob")
remove_directory("test_case")

print("所有测试文件已清理")
print()

# 14. 总结
print("=== 14. glob模块总结 ===")
print("glob模块是Python中用于文件模式匹配的重要模块，提供了Unix风格的路径模式扩展功能。")
print("主要优势：")
print("- 简单易用的API设计")
print("- 支持Unix风格的通配符")
print("- 提供递归匹配功能（Python 3.5+）")
print("- 返回匹配的文件路径列表")
print("- 与os模块和pathlib模块良好集成")
print("- 可以结合正则表达式使用")
print()
print("主要劣势：")
print("- 不支持复杂的匹配模式")
print("- 递归匹配可能影响性能")
print("- 默认不区分大小写（在不同平台上可能有差异）")
print("- 匹配结果顺序不确定")
print()
print("使用建议：")
print("- 对于简单的文件匹配需求，使用glob模块")
print("- 对于复杂的匹配需求，结合正则表达式使用")
print("- 处理大量文件时使用glob.iglob()减少内存使用")
print("- 总是对匹配结果进行排序")
print("- 结合os.path模块确保文件操作的安全性")
print("- 在Python 3.4+中，可以考虑使用pathlib模块的glob方法")
print("- 注意跨平台兼容性问题")
