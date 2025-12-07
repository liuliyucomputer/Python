# Python fileinput模块详解

import fileinput
import os
import sys

# 1. 模块概述
print("=== 1. fileinput模块概述 ===")
print("fileinput模块提供了一个简单的接口来处理多个输入文件的内容，特别适合命令行工具和批处理任务。")
print("该模块的主要特点：")
print("- 可以同时处理多个文件")
print("- 支持从标准输入读取内容")
print("- 提供行号跟踪")
print("- 支持文件的原地修改")
print("- 提供灵活的文件迭代方式")
print("- 支持文件编码设置")
print("- 可以跳过首行或特定行")
print("- 与命令行参数无缝集成")
print()

# 2. 基本用法
print("=== 2. 基本用法 ===")

# 创建测试文件
os.makedirs("test_files", exist_ok=True)
test_files = [
    "test_files/file1.txt",
    "test_files/file2.txt",
    "test_files/file3.txt"
]

for i, file_path in enumerate(test_files, 1):
    with open(file_path, "w") as f:
        f.write(f"文件 {i} 行 1\n")
        f.write(f"文件 {i} 行 2\n")
        f.write(f"文件 {i} 行 3\n")

print("2.1 迭代处理多个文件：")
# 使用fileinput.input()迭代处理多个文件
for line in fileinput.input(files=test_files):
    print(f"  文件: {fileinput.filename()}, 行号: {fileinput.lineno()}, 内容: {line.rstrip()}")

print()

print("2.2 处理命令行参数中的文件：")
# 注意：在实际脚本中，fileinput.input()会自动处理命令行参数中的文件
# 这里我们模拟命令行参数
import sys
from io import StringIO

# 保存原始命令行参数
original_argv = sys.argv.copy()

# 模拟命令行参数
argv_backup = sys.argv
sys.argv = [sys.argv[0]] + test_files

try:
    # 使用fileinput.input()处理命令行参数中的文件
    print("  模拟处理命令行参数中的文件：")
    for line in fileinput.input():
        print(f"    文件: {fileinput.filename()}, 行号: {fileinput.lineno()}, 内容: {line.rstrip()}")
finally:
    # 恢复原始命令行参数
    sys.argv = argv_backup

print()

print("2.3 从标准输入读取：")
# 注意：这个示例需要用户输入，这里我们模拟标准输入
import sys
from io import StringIO

# 保存原始标准输入
original_stdin = sys.stdin

# 模拟标准输入
stdin_backup = sys.stdin
sys.stdin = StringIO("标准输入行 1\n标准输入行 2\n标准输入行 3")

try:
    # 使用fileinput.input()从标准输入读取
    print("  模拟从标准输入读取：")
    for line in fileinput.input(files='-'):  # '-'表示标准输入
        print(f"    内容: {line.rstrip()}")
finally:
    # 恢复原始标准输入
    sys.stdin = stdin_backup

print()

# 3. 高级特性
print("=== 3. 高级特性 ===")

print("3.1 文件内的行号：")
for line in fileinput.input(files=test_files):
    print(f"  文件: {fileinput.filename()}, ")
    print(f"    全局行号: {fileinput.lineno()}, ")
    print(f"    文件内行号: {fileinput.filelineno()}, ")
    print(f"    内容: {line.rstrip()}")

print()

print("3.2 检测文件边界：")
for line in fileinput.input(files=test_files):
    if fileinput.isfirstline():
        print(f"  === 开始处理文件: {fileinput.filename()} ===")
    print(f"    行 {fileinput.filelineno()}: {line.rstrip()}")
    if fileinput.isstdin():
        print(f"    来自标准输入")

print()

print("3.3 文件编码设置：")
# 创建一个UTF-8编码的文件
utf8_file = "test_files/utf8_file.txt"
with open(utf8_file, "w", encoding="utf-8") as f:
    f.write("中文内容行 1\n")
    f.write("中文内容行 2\n")

# 使用指定编码处理文件
for line in fileinput.input(files=[utf8_file], encoding="utf-8"):
    print(f"  UTF-8文件: {fileinput.filename()}, 行 {fileinput.filelineno()}: {line.rstrip()}")

print()

print("3.4 文件的原地修改：")
# 创建一个用于修改的文件
modify_file = "test_files/modify.txt"
with open(modify_file, "w") as f:
    f.write("原始行 1\n")
    f.write("原始行 2\n")
    f.write("原始行 3\n")

print(f"  修改前的文件内容：")
with open(modify_file, "r") as f:
    print(f.read())

# 使用inplace=True进行原地修改
for line in fileinput.input(files=[modify_file], inplace=True):
    # 处理每一行，这里将"原始"替换为"修改后"
    line = line.replace("原始", "修改后")
    # 注意：在inplace模式下，必须打印处理后的行
    print(line.rstrip())

print(f"  修改后的文件内容：")
with open(modify_file, "r") as f:
    print(f.read())

print()

# 4. 实用函数
print("=== 4. 实用函数 ===")

print("4.1 fileinput.input()：")
print("   创建一个FileInput实例，是模块的主要入口点")
print("   参数：")
print("   - files: 要处理的文件列表，默认为命令行参数")
print("   - inplace: 是否原地修改文件，默认为False")
print("   - backup: 原地修改时的备份扩展名，默认为None")
print("   - mode: 文件打开模式，默认为'r'")
print("   - openhook: 自定义文件打开钩子")
print("   - encoding: 文件编码")
print("   - errors: 编码错误处理方式")

print()

print("4.2 fileinput.filename()：")
print("   返回当前正在处理的文件的名称")
print("   示例：")
for line in fileinput.input(files=test_files[:1]):
    print(f"   当前文件: {fileinput.filename()}")
    break

print()

print("4.3 fileinput.lineno()：")
print("   返回当前处理的行的全局行号")

print("4.4 fileinput.filelineno()：")
print("   返回当前处理的行在当前文件中的行号")

print("4.5 fileinput.isfirstline()：")
print("   判断当前行是否是文件的第一行")

print("4.6 fileinput.isstdin()：")
print("   判断当前行是否来自标准输入")

print("4.7 fileinput.nextfile()：")
print("   关闭当前文件并移动到下一个文件")
print("   示例：")
for line in fileinput.input(files=test_files[:2]):
    print(f"   文件: {fileinput.filename()}, 行: {fileinput.filelineno()}, 内容: {line.rstrip()}")
    if fileinput.filelineno() == 2:
        print("   提前结束当前文件处理")
        fileinput.nextfile()

print()

print("4.8 fileinput.close()：")
print("   关闭FileInput实例，释放资源")

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")

print("5.1 批量文件替换：")
def batch_replace(files, search_str, replace_str, encoding="utf-8"):
    """批量替换文件中的字符串"""
    print(f"  批量替换：将 '{search_str}' 替换为 '{replace_str}'")
    print(f"  处理的文件：{files}")
    
    count = 0
    for line in fileinput.input(files=files, inplace=True, encoding=encoding):
        new_line = line.replace(search_str, replace_str)
        if new_line != line:
            count += 1
        print(new_line.rstrip())
    
    print(f"  替换完成，共替换 {count} 处")

# 创建测试文件
replace_files = [
    "test_files/replace1.txt",
    "test_files/replace2.txt"
]

for i, file_path in enumerate(replace_files, 1):
    with open(file_path, "w") as f:
        f.write(f"这是替换测试文件 {i}\n")
        f.write(f"包含需要替换的关键词 test\n")
        f.write(f"test 会被替换为 replaced\n")

# 执行批量替换
batch_replace(replace_files, "test", "replaced")

# 显示替换结果
print(f"  替换后的文件内容：")
for file_path in replace_files:
    print(f"  === {file_path} ===")
    with open(file_path, "r") as f:
        print(f.read())

print()

print("5.2 统计文件行数：")
def count_lines(files):
    """统计多个文件的总行数"""
    total_lines = 0
    file_stats = {}
    
    for line in fileinput.input(files=files):
        total_lines += 1
        current_file = fileinput.filename()
        if current_file not in file_stats:
            file_stats[current_file] = 0
        file_stats[current_file] += 1
    
    print(f"  总行数：{total_lines}")
    print(f"  各文件行数：")
    for file_path, lines in file_stats.items():
        print(f"    {file_path}: {lines} 行")
    
    return total_lines, file_stats

# 执行行数统计
count_lines(test_files)

print()

print("5.3 提取特定行：")
def extract_lines(files, line_numbers):
    """提取多个文件中的特定行号的行"""
    result = {}
    
    for line in fileinput.input(files=files):
        current_file = fileinput.filename()
        current_lineno = fileinput.filelineno()
        
        if current_lineno in line_numbers:
            if current_file not in result:
                result[current_file] = {}
            result[current_file][current_lineno] = line.rstrip()
    
    print(f"  提取的行：")
    for file_path, lines in result.items():
        print(f"    文件: {file_path}")
        for lineno, content in lines.items():
            print(f"      行 {lineno}: {content}")
    
    return result

# 提取第2行和第3行
extract_lines(test_files, [2, 3])

print()

print("5.4 生成文件差异报告：")
def generate_diff(file1, file2, output_file=None):
    """生成两个文件的差异报告"""
    import difflib
    
    # 读取两个文件的内容
    with open(file1, 'r') as f1:
        lines1 = f1.readlines()
    
    with open(file2, 'r') as f2:
        lines2 = f2.readlines()
    
    # 生成差异
    diff = difflib.unified_diff(lines1, lines2, fromfile=file1, tofile=file2)
    
    # 输出差异
    if output_file:
        with open(output_file, 'w') as f:
            f.writelines(diff)
        print(f"  差异已保存到: {output_file}")
    else:
        print(f"  生成 {file1} 和 {file2} 的差异：")
        for line in diff:
            print(f"    {line.rstrip()}")

# 创建两个差异文件
diff_file1 = "test_files/diff1.txt"
diff_file2 = "test_files/diff2.txt"

with open(diff_file1, "w") as f:
    f.write("行 1\n")
    f.write("行 2\n")
    f.write("行 3\n")
    f.write("行 4\n")

with open(diff_file2, "w") as f:
    f.write("行 1\n")
    f.write("修改后的行 2\n")
    f.write("行 3\n")
    f.write("行 4\n")
    f.write("新增的行 5\n")

# 生成差异报告
generate_diff(diff_file1, diff_file2)

print()

print("5.5 日志文件分析：")
def analyze_logs(log_files, keyword, encoding="utf-8"):
    """分析日志文件中的关键词"""
    print(f"  分析日志文件中的关键词: {keyword}")
    print(f"  处理的日志文件: {log_files}")
    
    matches = []
    for line in fileinput.input(files=log_files, encoding=encoding):
        if keyword in line:
            matches.append({
                "file": fileinput.filename(),
                "lineno": fileinput.lineno(),
                "content": line.rstrip()
            })
    
    print(f"  共找到 {len(matches)} 处匹配：")
    for match in matches[:5]:  # 只显示前5个匹配
        print(f"    文件: {match['file']}, 行: {match['lineno']}, 内容: {match['content']}")
    
    if len(matches) > 5:
        print(f"    ... 还有 {len(matches) - 5} 个匹配未显示")
    
    return matches

# 创建测试日志文件
log_files = [
    "test_files/app.log",
    "test_files/error.log"
]

with open(log_files[0], "w") as f:
    f.write("INFO: 应用程序启动\n")
    f.write("WARNING: 内存使用过高\n")
    f.write("INFO: 处理请求\n")
    f.write("ERROR: 数据库连接失败\n")

with open(log_files[1], "w") as f:
    f.write("ERROR: 文件读取失败\n")
    f.write("INFO: 重新连接数据库\n")
    f.write("ERROR: 网络超时\n")

# 分析日志文件
analyze_logs(log_files, "ERROR")

print()

# 6. 高级技巧
print("=== 6. 高级技巧 ===")

print("6.1 使用contextlib.redirect_stdout：")
import contextlib
import io

def capture_fileinput_output(files):
    """捕获fileinput的输出"""
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        for line in fileinput.input(files=files):
            print(f"{fileinput.filename()}:{fileinput.lineno()}: {line.rstrip()}")
    return output.getvalue()

# 捕获fileinput的输出
output = capture_fileinput_output(test_files[:1])
print(f"  捕获的输出：")
print(output)

print()

print("6.2 使用fileinput.hook_compressed处理压缩文件：")
# 注意：需要安装gzip和bz2模块（Python标准库）
# 这里我们创建一个简单的示例
print("  使用fileinput.hook_compressed处理压缩文件：")
print("  示例：")
print("  # 处理gz压缩文件")
print("  for line in fileinput.input(files=['data.gz'], openhook=fileinput.hook_compressed):")
print("      print(line)")

print()

print("6.3 自定义文件打开钩子：")
def custom_openhook(filename, mode):
    """自定义文件打开钩子"""
    print(f"  自定义打开文件: {filename}，模式: {mode}")
    return open(filename, mode, encoding="utf-8")

for line in fileinput.input(files=test_files[:1], openhook=custom_openhook):
    print(f"    文件内容: {line.rstrip()}")

print()

print("6.4 与正则表达式结合使用：")
import re

def search_pattern(files, pattern, encoding="utf-8"):
    """在文件中搜索正则表达式模式"""
    regex = re.compile(pattern)
    matches = []
    
    for line in fileinput.input(files=files, encoding=encoding):
        if regex.search(line):
            matches.append({
                "file": fileinput.filename(),
                "lineno": fileinput.lineno(),
                "content": line.rstrip()
            })
    
    return matches

# 搜索包含数字的行
pattern = r"\d+"
matches = search_pattern(test_files, pattern)

print(f"  搜索包含数字的行 (模式: {pattern}):")
for match in matches:
    print(f"    文件: {match['file']}, 行: {match['lineno']}, 内容: {match['content']}")

print()

# 7. 最佳实践
print("=== 7. 最佳实践 ===")

print("1. 使用with语句管理FileInput实例：")
print("   with fileinput.input(files=files) as f:")
print("       for line in f:")
print("           # 处理行")

print("\n2. 明确指定文件编码：")
print("   for line in fileinput.input(files=files, encoding='utf-8'):")
print("       # 处理行")

print("\n3. 使用inplace=True时注意备份：")
print("   # 使用backup参数创建备份文件")
print("   for line in fileinput.input(files=files, inplace=True, backup='.bak'):")
print("       # 处理行")

print("\n4. 避免在循环中修改files参数：")
print("   # 错误：")
print("   files = ['file1.txt']")
print("   for line in fileinput.input(files=files):")
print("       files.append('file2.txt')  # 不会被处理")

print("\n5. 使用fileinput.nextfile()提前结束当前文件处理：")
print("   for line in fileinput.input(files=files):")
print("       if some_condition:")
print("           fileinput.nextfile()")

print("\n6. 结合命令行参数使用：")
print("   # 在脚本中直接使用fileinput.input()处理命令行参数")
print("   for line in fileinput.input():")
print("       # 处理行")

print("\n7. 注意文件路径的处理：")
print("   # 使用绝对路径或确保当前工作目录正确")
print("   import os")
print("   files = [os.path.abspath(f) for f in files]")

print("\n8. 考虑性能问题：")
print("   # 对于大文件，考虑使用更高效的处理方式")
print("   # 避免在循环中进行复杂的操作")

print("\n9. 使用fileinput模块构建命令行工具：")
print("   # 示例：实现类似grep的功能")
print("   import sys")
print("   import re")
print("   ")
print("   if len(sys.argv) < 2:")
print("       print(\"Usage: python grep.py pattern [files]\")
print("       sys.exit(1)")
print("   ")
print("   pattern = sys.argv[1]")
print("   files = sys.argv[2:] if len(sys.argv) > 2 else ['-']")
print("   ")
print("   regex = re.compile(pattern)")
print("   for line in fileinput.input(files=files):")
print("       if regex.search(line):")
print("           print(f'{fileinput.filename()}:{fileinput.lineno()}: {line.rstrip()}')")

print()

# 8. 常见错误和陷阱
print("=== 8. 常见错误和陷阱 ===")

print("1. 在inplace模式下忘记打印处理后的行：")
print("   # 错误：")
print("   for line in fileinput.input(files=files, inplace=True):")
print("       line = line.replace('a', 'b')")
print("       # 忘记打印处理后的行，导致文件内容丢失")
print("   ")
print("   # 正确：")
print("   for line in fileinput.input(files=files, inplace=True):")
print("       line = line.replace('a', 'b')")
print("       print(line.rstrip())")

print("\n2. 处理编码问题：")
print("   # 错误：处理非UTF-8编码的文件")
print("   for line in fileinput.input(files=files):")
print("       # 可能导致UnicodeDecodeError")
print("   ")
print("   # 正确：指定文件编码")
print("   for line in fileinput.input(files=files, encoding='gbk'):")
print("       # 处理行")

print("\n3. 文件路径问题：")
print("   # 错误：文件路径不存在或不正确")
print("   files = ['nonexistent.txt']")
print("   for line in fileinput.input(files=files):")
print("       # 抛出FileNotFoundError")
print("   ")
print("   # 正确：检查文件是否存在")
print("   import os")
print("   files = ['file1.txt', 'file2.txt']")
print("   existing_files = [f for f in files if os.path.exists(f)]")
print("   for line in fileinput.input(files=existing_files):")
print("       # 处理行")

print("\n4. 命令行参数冲突：")
print("   # 错误：脚本本身的参数与fileinput的文件参数冲突")
print("   # 例如脚本使用 -v 参数表示 verbose")
print("   files = sys.argv[1:]  # 会包含 -v")
print("   ")
print("   # 正确：使用argparse处理命令行参数")
print("   import argparse")
print("   parser = argparse.ArgumentParser()")
print("   parser.add_argument('-v', '--verbose', action='store_true')")
print("   parser.add_argument('files', nargs='*', default=['-'])")
print("   args = parser.parse_args()")
print("   ")
print("   for line in fileinput.input(files=args.files):")
print("       # 处理行")

print("\n5. 文件权限问题：")
print("   # 错误：在inplace模式下没有写入权限")
print("   for line in fileinput.input(files=files, inplace=True):")
print("       # 抛出PermissionError")
print("   ")
print("   # 正确：检查文件权限")
print("   import os")
print("   for f in files:")
print("       if not os.access(f, os.W_OK):")
print("           print(f'没有写入权限: {f}')")

print("\n6. 关闭FileInput实例：")
print("   # 错误：创建FileInput实例后没有关闭")
print("   fi = fileinput.input(files=files)")
print("   for line in fi:")
print("       # 处理行")
print("   # 忘记关闭fi")
print("   ")
print("   # 正确：使用with语句或手动关闭")
print("   with fileinput.input(files=files) as fi:")
print("       for line in fi:")
print("           # 处理行")

print()

# 9. 总结
print("=== 9. 总结 ===")
print("fileinput模块是Python中处理多个文件的强大工具，特别适合用于命令行工具和批处理任务。")
print()
print("主要功能：")
print("- 同时处理多个文件")
print("- 支持从标准输入读取内容")
print("- 提供行号跟踪（全局和文件内）")
print("- 支持文件的原地修改")
print("- 提供灵活的文件迭代方式")
print("- 支持文件编码设置")
print("- 可以跳过首行或特定行")
print("- 与命令行参数无缝集成")
print()
print("优势：")
print("- 简化了多文件处理的代码")
print("- 提供了丰富的功能和灵活的配置选项")
print("- 与Python的其他模块良好集成")
print("- 跨平台兼容性好")
print()
print("应用场景：")
print("- 命令行工具开发")
print("- 批量文件处理")
print("- 日志文件分析")
print("- 文件内容替换")
print("- 数据提取和转换")
print("- 文件差异比较")
print()
print("通过合理使用fileinput模块，可以大大提高多文件处理的效率和代码的可读性。")

# 清理测试文件
import shutil
shutil.rmtree("test_files")
