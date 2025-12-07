# Python os.path模块详解

import os.path
import os
import time

# 1. 模块概述
print("=== 1. os.path模块概述 ===")
print("os.path模块提供了路径处理功能，用于解析和构建文件路径。")
print("该模块的主要特点：")
print("- 跨平台路径处理，自动适应不同操作系统的路径分隔符")
print("- 提供路径解析、拼接、拆分等功能")
print("- 支持绝对路径和相对路径转换")
print("- 提供文件存在性、类型检查等功能")
print("- 获取文件属性（大小、修改时间等）")
print()

# 2. 路径分隔符
print("=== 2. 路径分隔符 ===")

print(f"os.path.sep = {repr(os.path.sep)}")  # 主路径分隔符
print(f"os.path.altsep = {repr(os.path.altsep)}")  # 备用路径分隔符
print(f"os.path.extsep = {repr(os.path.extsep)}")  # 文件扩展名分隔符
print(f"os.path.pathsep = {repr(os.path.pathsep)}")  # 路径列表分隔符
print(f"os.path.linesep = {repr(os.path.linesep)}")  # 行分隔符
print()

# 3. 路径拼接
print("=== 3. 路径拼接 ===")

# 使用os.path.join拼接路径
path1 = os.path.join('dir1', 'dir2', 'file.txt')
print(f"os.path.join('dir1', 'dir2', 'file.txt') = {repr(path1)}")

# 处理绝对路径
path2 = os.path.join('dir1', '/dir2', 'file.txt')
print(f"os.path.join('dir1', '/dir2', 'file.txt') = {repr(path2)}")  # /dir2/file.txt

# 处理空字符串
path3 = os.path.join('dir1', '', 'file.txt')
print(f"os.path.join('dir1', '', 'file.txt') = {repr(path3)}")  # dir1/file.txt

# 处理'.'和'..'
path4 = os.path.join('dir1', '.', 'dir2', '..', 'file.txt')
print(f"os.path.join('dir1', '.', 'dir2', '..', 'file.txt') = {repr(path4)}")  # dir1/file.txt
print()

# 4. 路径拆分
print("=== 4. 路径拆分 ===")

# 拆分路径为目录和文件名
full_path = os.path.join('dir1', 'dir2', 'file.txt')
dir_name, base_name = os.path.split(full_path)
print(f"完整路径: {repr(full_path)}")
print(f"os.path.split(full_path) = ({repr(dir_name)}, {repr(base_name)})")

# 拆分文件名和扩展名
root, ext = os.path.splitext(base_name)
print(f"os.path.splitext(base_name) = ({repr(root)}, {repr(ext)})")

# 拆分多级路径
path_parts = []
temp_path = full_path
while True:
    temp_path, part = os.path.split(temp_path)
    if part:
        path_parts.insert(0, part)
    else:
        if temp_path:
            path_parts.insert(0, temp_path)
        break
print(f"路径的所有部分: {path_parts}")
print()

# 5. 绝对路径和相对路径
print("=== 5. 绝对路径和相对路径 ===")

# 获取当前工作目录
cwd = os.getcwd()
print(f"当前工作目录: {repr(cwd)}")

# 转换为绝对路径
rel_path = '../dir/file.txt'
abs_path = os.path.abspath(rel_path)
print(f"相对路径 {repr(rel_path)} 的绝对路径: {repr(abs_path)}")

# 检查是否为绝对路径
print(f"os.path.isabs(rel_path) = {os.path.isabs(rel_path)}")
print(f"os.path.isabs(abs_path) = {os.path.isabs(abs_path)}")

# 获取相对路径
path1 = os.path.join(cwd, 'dir1')
path2 = os.path.join(cwd, 'dir2')
try:
    rel_path = os.path.relpath(path1, path2)
    print(f"从 {repr(path2)} 到 {repr(path1)} 的相对路径: {repr(rel_path)}")
    
    rel_path = os.path.relpath(path2, path1)
    print(f"从 {repr(path1)} 到 {repr(path2)} 的相对路径: {repr(rel_path)}")
except ValueError as e:
    print(f"获取相对路径失败: {e}")
print()

# 6. 路径规范化
print("=== 6. 路径规范化 ===")

# 规范化路径
path = os.path.join('dir1', '.', 'dir2', '..', './dir3', 'file.txt')
print(f"原始路径: {repr(path)}")

# 使用os.path.normpath规范化
norm_path = os.path.normpath(path)
print(f"os.path.normpath(path) = {repr(norm_path)}")

# 使用os.path.abspath规范化并转换为绝对路径
abs_norm_path = os.path.abspath(path)
print(f"os.path.abspath(path) = {repr(abs_norm_path)}")

# 处理多个分隔符
multi_sep_path = 'dir1//dir2///file.txt'
norm_multi_path = os.path.normpath(multi_sep_path)
print(f"处理多个分隔符: {repr(multi_sep_path)} -> {repr(norm_multi_path)}")
print()

# 7. 文件和目录检查
print("=== 7. 文件和目录检查 ===")

# 创建测试文件和目录
os.makedirs('test_dir', exist_ok=True)
with open('test_file.txt', 'w') as f:
    f.write('test content')

# 检查文件或目录是否存在
print(f"os.path.exists('test_file.txt') = {os.path.exists('test_file.txt')}")
print(f"os.path.exists('test_dir') = {os.path.exists('test_dir')}")
print(f"os.path.exists('non_existent') = {os.path.exists('non_existent')}")

# 检查是否为文件
print(f"os.path.isfile('test_file.txt') = {os.path.isfile('test_file.txt')}")
print(f"os.path.isfile('test_dir') = {os.path.isfile('test_dir')}")

# 检查是否为目录
print(f"os.path.isdir('test_dir') = {os.path.isdir('test_dir')}")
print(f"os.path.isdir('test_file.txt') = {os.path.isdir('test_file.txt')}")

# 检查是否为符号链接（Windows可能需要管理员权限）
if os.name != 'nt':  # Windows不支持符号链接
    try:
        os.symlink('test_file.txt', 'test_link.txt')
        print(f"os.path.islink('test_link.txt') = {os.path.islink('test_link.txt')}")
        os.remove('test_link.txt')
    except Exception as e:
        print(f"符号链接操作失败: {e}")
else:
    print("Windows系统可能不支持符号链接操作")

# 检查是否为挂载点
print(f"os.path.ismount('/') = {os.path.ismount('/')}")  # Unix系统根目录
if os.name == 'nt':
    print(f"os.path.ismount('C:/') = {os.path.ismount('C:/')}")  # Windows C盘

# 清理测试文件和目录
os.remove('test_file.txt')
os.rmdir('test_dir')
print()

# 8. 文件属性获取
print("=== 8. 文件属性获取 ===")

# 创建测试文件
with open('test_attr.txt', 'w') as f:
    f.write('test content for attributes')

# 获取文件大小
print(f"os.path.getsize('test_attr.txt') = {os.path.getsize('test_attr.txt')} bytes")

# 获取文件时间
print(f"os.path.getctime('test_attr.txt') = {os.path.getctime('test_attr.txt')}")  # 创建时间
print(f"os.path.getmtime('test_attr.txt') = {os.path.getmtime('test_attr.txt')}")  # 修改时间
print(f"os.path.getatime('test_attr.txt') = {os.path.getatime('test_attr.txt')}")  # 访问时间

# 转换时间戳为可读格式
print(f"创建时间(可读): {time.ctime(os.path.getctime('test_attr.txt'))}")
print(f"修改时间(可读): {time.ctime(os.path.getmtime('test_attr.txt'))}")
print(f"访问时间(可读): {time.ctime(os.path.getatime('test_attr.txt'))}")

# 睡眠1秒，修改文件
import time
time.sleep(1)
with open('test_attr.txt', 'a') as f:
    f.write('\nadditional content')

print(f"修改后时间: {time.ctime(os.path.getmtime('test_attr.txt'))}")

# 清理测试文件
os.remove('test_attr.txt')
print()

# 9. 路径组件获取
print("=== 9. 路径组件获取 ===")

# 创建测试路径
full_path = os.path.join('dir1', 'dir2', 'file.txt')
print(f"测试路径: {repr(full_path)}")

# 获取路径的最后一部分（文件名或目录名）
base_name = os.path.basename(full_path)
print(f"os.path.basename(full_path) = {repr(base_name)}")

# 获取路径的目录部分
dir_name = os.path.dirname(full_path)
print(f"os.path.dirname(full_path) = {repr(dir_name)}")

# 同时获取目录和文件名
dir_name2, base_name2 = os.path.split(full_path)
print(f"os.path.split(full_path) = ({repr(dir_name2)}, {repr(base_name2)})")

# 获取驱动器名（Windows）
if os.name == 'nt':
    drive, rest = os.path.splitdrive('C:/dir/file.txt')
    print(f"os.path.splitdrive('C:/dir/file.txt') = ({repr(drive)}, {repr(rest)})")

# 获取通用路径组件
generic_path = os.path.join(os.path.sep, 'dir1', 'dir2', 'file.txt')
print(f"通用路径: {repr(generic_path)}")
print(f"basename: {repr(os.path.basename(generic_path))}")
print(f"dirname: {repr(os.path.dirname(generic_path))}")
print()

# 10. 路径比较
print("=== 10. 路径比较 ===")

# 比较两个路径是否指向同一文件
path1 = 'file.txt'
path2 = './file.txt'

# 创建测试文件
with open(path1, 'w') as f:
    f.write('test content')

# 使用os.path.samefile比较
print(f"os.path.samefile(path1, path2) = {os.path.samefile(path1, path2)}")

# 使用os.path.sameopenfile比较（需要文件描述符）
fd1 = os.open(path1, os.O_RDONLY)
fd2 = os.open(path2, os.O_RDONLY)
print(f"os.path.sameopenfile(fd1, fd2) = {os.path.sameopenfile(fd1, fd2)}")
os.close(fd1)
os.close(fd2)

# 使用os.path.realpath比较
print(f"os.path.realpath(path1) = {repr(os.path.realpath(path1))}")
print(f"os.path.realpath(path2) = {repr(os.path.realpath(path2))}")
print(f"os.path.realpath(path1) == os.path.realpath(path2) = {os.path.realpath(path1) == os.path.realpath(path2)}")

# 清理测试文件
os.remove(path1)
print()

# 11. 路径扩展
print("=== 11. 路径扩展 ===")

# 扩展用户主目录
print(f"os.path.expanduser('~') = {repr(os.path.expanduser('~'))}")
print(f"os.path.expanduser('~/dir/file.txt') = {repr(os.path.expanduser('~/dir/file.txt'))}")

# 扩展环境变量
print(f"os.path.expandvars('$HOME/dir/file.txt') = {repr(os.path.expandvars('$HOME/dir/file.txt'))}")
print(f"os.path.expandvars('%USERPROFILE%/dir/file.txt') = {repr(os.path.expandvars('%USERPROFILE%/dir/file.txt'))}")  # Windows
print()

# 12. 实际应用示例
print("=== 12. 实际应用示例 ===")

# 示例1：获取文件的扩展名
def get_file_extension(filename):
    """获取文件的扩展名（不含点）"""
    _, ext = os.path.splitext(filename)
    return ext.lstrip('.').lower()

print("获取文件扩展名示例:")
print(f"get_file_extension('file.txt') = {get_file_extension('file.txt')}")
print(f"get_file_extension('document.PDF') = {get_file_extension('document.PDF')}")
print(f"get_file_extension('archive.tar.gz') = {get_file_extension('archive.tar.gz')}")
print(f"get_file_extension('no_extension') = {get_file_extension('no_extension')}")

# 示例2：查找目录下所有特定类型的文件
def find_files_by_extension(directory, extensions):
    """查找目录下所有指定扩展名的文件"""
    found_files = []
    if not os.path.exists(directory):
        return found_files
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            ext = get_file_extension(file)
            if ext in extensions:
                found_files.append(os.path.join(root, file))
    return found_files

# 创建测试目录结构
os.makedirs('test_dir/subdir', exist_ok=True)
with open('test_dir/file.txt', 'w') as f:
    f.write('test text file')
with open('test_dir/image.jpg', 'w') as f:
    f.write('test image file')
with open('test_dir/subdir/document.pdf', 'w') as f:
    f.write('test pdf file')
with open('test_dir/subdir/data.csv', 'w') as f:
    f.write('test csv file')

print("\n查找特定扩展名的文件示例:")
txt_files = find_files_by_extension('test_dir', ['txt'])
print(f"找到的txt文件: {txt_files}")

image_files = find_files_by_extension('test_dir', ['jpg', 'png', 'gif'])
print(f"找到的图片文件: {image_files}")

# 清理测试目录
def remove_directory(directory):
    """递归删除目录"""
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            os.rmdir(os.path.join(root, dir))
    os.rmdir(directory)

remove_directory('test_dir')

# 示例3：检查文件是否为旧文件
def is_old_file(filename, days=30):
    """检查文件是否超过指定天数没有修改"""
    if not os.path.isfile(filename):
        return False
    
    current_time = time.time()
    file_mtime = os.path.getmtime(filename)
    days_in_seconds = days * 24 * 60 * 60
    
    return current_time - file_mtime > days_in_seconds

# 创建测试文件
with open('recent_file.txt', 'w') as f:
    f.write('recent file')

print("\n检查文件是否为旧文件示例:")
print(f"is_old_file('recent_file.txt', days=1) = {is_old_file('recent_file.txt', days=1)}")
print(f"is_old_file('non_existent.txt') = {is_old_file('non_existent.txt')}")

# 清理测试文件
os.remove('recent_file.txt')

# 示例4：获取文件的相对路径
def get_relative_path(file_path, base_path=None):
    """获取文件相对于base_path的相对路径"""
    if base_path is None:
        base_path = os.getcwd()
    
    abs_file_path = os.path.abspath(file_path)
    abs_base_path = os.path.abspath(base_path)
    
    return os.path.relpath(abs_file_path, abs_base_path)

# 创建测试文件
with open('test_relative.txt', 'w') as f:
    f.write('test file')

print("\n获取相对路径示例:")
print(f"get_relative_path('test_relative.txt') = {repr(get_relative_path('test_relative.txt'))}")
print(f"get_relative_path('test_relative.txt', '.') = {repr(get_relative_path('test_relative.txt', '.'))}")
if os.path.dirname(os.getcwd()):
    print(f"get_relative_path('test_relative.txt', '..') = {repr(get_relative_path('test_relative.txt', '..'))}")

# 清理测试文件
os.remove('test_relative.txt')
print()

# 13. 最佳实践
print("=== 13. 最佳实践 ===")

print("1. 始终使用os.path.join()拼接路径，而不是字符串拼接")
print("   # 推荐:")
print("   path = os.path.join('dir', 'subdir', 'file.txt')")
print("   # 不推荐:")
print("   path = 'dir/subdir/file.txt'  # 不跨平台")
print("   path = 'dir' + '/' + 'subdir' + '/' + 'file.txt'  # 不跨平台")

print("\n2. 使用os.path.abspath()或os.path.realpath()获取绝对路径")
print("   abs_path = os.path.abspath('relative/path')")

print("\n3. 使用os.path.exists()和os.path.isfile()/os.path.isdir()检查文件/目录")
print("   if os.path.exists(path) and os.path.isfile(path):")
print("       # 处理文件")

print("\n4. 使用os.path.splitext()获取文件扩展名")
print("   root, ext = os.path.splitext(filename)")

print("\n5. 对于Python 3.4+，考虑使用pathlib模块进行面向对象的路径操作")
print("   from pathlib import Path")
print("   path = Path('dir') / 'subdir' / 'file.txt'")

print("\n6. 使用异常处理包装文件操作")
print("   try:")
print("       os.remove('file.txt')")
print("   except FileNotFoundError:")
print("       pass")

print("\n7. 避免硬编码路径分隔符")
print("   # 推荐:")
print("   path = os.path.join('dir', 'file.txt')")
print("   # 不推荐:")
print("   path = 'dir/file.txt'  # Windows使用'\\'")

print("\n8. 使用os.path.normpath()规范化路径")
print("   norm_path = os.path.normpath('dir/./subdir/../file.txt')")
print()

# 14. 常见错误和陷阱
print("=== 14. 常见错误和陷阱 ===")

print("1. 忽略路径分隔符的差异")
print("   Windows使用'\\'，Unix使用'/'")
print("   解决方法：使用os.path.join()拼接路径")

print("\n2. 使用字符串拼接构建路径")
print("   # 错误:")
print("   path = 'dir' + '/' + 'file.txt'")
print("   # 正确:")
print("   path = os.path.join('dir', 'file.txt')")

print("\n3. 不检查文件是否存在就操作")
print("   # 错误:")
print("   os.remove('non_existent.txt')  # 会抛出FileNotFoundError")
print("   # 正确:")
print("   if os.path.exists('file.txt'):")
print("       os.remove('file.txt')")

print("\n4. 混淆相对路径和绝对路径")
print("   # 错误:")
print("   open('file.txt')  # 相对于当前工作目录")
print("   # 正确:")
print("   import os")
print("   open(os.path.join(os.getcwd(), 'file.txt'))")

print("\n5. 不规范化路径导致的问题")
print("   path = 'dir/./subdir/../file.txt'  # 包含不必要的.和..")
print("   norm_path = os.path.normpath(path)  # 规范化为'dir/file.txt'")

print("\n6. 在Windows上使用Unix路径")
print("   # 错误:")
print("   path = '/dir/file.txt'  # Windows不识别")
print("   # 正确:")
print("   path = os.path.join('dir', 'file.txt')  # 自动使用正确的分隔符")
print()

# 15. 与pathlib模块的比较
print("=== 15. 与pathlib模块的比较 ===")

print("| 特性 | os.path模块 | pathlib模块 |")
print("|------|------------|-------------|")
print("| 接口风格 | 函数式 | 面向对象 |")
print("| 链式调用 | 不支持 | 支持 |")
print("| 可读性 | 一般 | 高 |")
print("| 跨平台性 | 好 | 优秀 |")
print("| 功能完整性 | 高 | 高 |")
print("| Python版本支持 | 所有 | 3.4+")
print("| 代码简洁性 | 一般 | 高 |")

print("\nos.path模块示例:")
print("   import os.path")
print("   path = os.path.join('dir', 'subdir', 'file.txt')")
print("   if os.path.exists(path) and os.path.isfile(path):")
print("       print(os.path.getsize(path))")

print("\npathlib模块示例:")
print("   from pathlib import Path")
print("   path = Path('dir') / 'subdir' / 'file.txt'")
print("   if path.exists() and path.is_file():")
print("       print(path.stat().st_size)")
print()

# 16. 总结
print("=== 16. os.path模块总结 ===")
print("os.path模块是Python中处理文件路径的核心模块，提供了丰富的路径操作功能。")
print("主要优势：")
print("- 跨平台路径处理，自动适应不同操作系统的路径分隔符")
print("- 提供完整的路径解析、拼接、拆分功能")
print("- 支持文件存在性、类型检查")
print("- 可以获取文件的各种属性")
print("- 与Python标准库的其他模块良好集成")
print()
print("主要劣势：")
print("- 函数式接口，使用起来不够直观")
print("- 不支持链式调用")
print("- 某些功能在不同平台上有差异")
print()
print("使用建议：")
print("- 在Python 3.4+中，推荐使用pathlib模块进行面向对象的路径操作")
print("- 在需要兼容旧版本Python时，使用os.path模块")
print("- 始终使用os.path.join()拼接路径，确保跨平台兼容性")
print("- 使用异常处理包装文件操作，提高代码健壮性")
