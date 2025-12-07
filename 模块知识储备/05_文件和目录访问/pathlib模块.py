# Python pathlib模块详解

from pathlib import Path
import os
import time

# 1. 模块概述
print("=== 1. pathlib模块概述 ===")
print("pathlib模块提供了面向对象的路径操作接口，是Python 3.4+中推荐的路径处理方式。")
print("该模块的主要特点：")
print("- 面向对象的API设计，使用链式调用提高代码可读性")
print("- 统一的路径表示，自动适应不同操作系统的路径分隔符")
print("- 提供路径解析、拼接、拆分等功能")
print("- 支持文件和目录的创建、删除、移动、复制等操作")
print("- 内置文件属性获取和比较功能")
print("- 支持相对路径和绝对路径转换")
print()

# 2. 路径对象创建
print("=== 2. 路径对象创建 ===")

# 使用Path构造函数创建路径对象
p1 = Path("file.txt")
p2 = Path("dir", "subdir", "file.txt")
p3 = Path("dir/subdir/file.txt")

print(f"Path('file.txt') = {p1}")
print(f"Path('dir', 'subdir', 'file.txt') = {p2}")
print(f"Path('dir/subdir/file.txt') = {p3}")

# 使用 / 运算符拼接路径
p4 = Path("dir") / "subdir" / "file.txt"
print(f"Path('dir') / 'subdir' / 'file.txt' = {p4}")

# 创建绝对路径
base_dir = Path("/home/user")  # Unix系统
base_dir_windows = Path("C:/Users/User")  # Windows系统

print(f"绝对路径: {base_dir}")
print(f"Windows绝对路径: {base_dir_windows}")

# 获取当前工作目录
current_dir = Path.cwd()
print(f"当前工作目录: {current_dir}")

# 获取用户主目录
home_dir = Path.home()
print(f"用户主目录: {home_dir}")
print()

# 3. 路径属性
print("=== 3. 路径属性 ===")

p = Path("dir", "subdir", "file.txt")
print(f"路径: {p}")

print(f"p.name = {p.name}")  # 文件名或目录名
print(f"p.suffix = {p.suffix}")  # 文件扩展名
print(f"p.stem = {p.stem}")  # 不包含扩展名的文件名
print(f"p.parent = {p.parent}")  # 父目录
print(f"p.parents = {list(p.parents)}")  # 所有父目录
print(f"p.parts = {p.parts}")  # 路径的各个组成部分

# 扩展属性
ext_p = Path("archive.tar.gz")
print(f"\n带多重扩展名的路径: {ext_p}")
print(f"ext_p.name = {ext_p.name}")
print(f"ext_p.suffix = {ext_p.suffix}")  # 最后一个扩展名
print(f"ext_p.suffixes = {ext_p.suffixes}")  # 所有扩展名
print(f"ext_p.stem = {ext_p.stem}")  # 不包含最后一个扩展名的部分

# 获取驱动器名（Windows）
if os.name == 'nt':
    win_p = Path("C:/Users/User/Documents/file.txt")
    print(f"\nWindows路径: {win_p}")
    print(f"win_p.drive = {win_p.drive}")  # 驱动器名
print()

# 4. 路径拼接与分解
print("=== 4. 路径拼接与分解 ===")

# 使用 / 运算符拼接路径
p1 = Path("dir1")
p2 = p1 / "dir2" / "dir3" / "file.txt"
print(f"Path('dir1') / 'dir2' / 'dir3' / 'file.txt' = {p2}")

# 使用joinpath方法拼接路径
p3 = Path("dir1").joinpath("dir2", "dir3", "file.txt")
print(f"Path('dir1').joinpath('dir2', 'dir3', 'file.txt') = {p3}")

# 分解路径为各个部分
p4 = Path("/home/user/documents/file.txt")
print(f"\n路径分解: {p4.parts}")

# 获取各级父目录
print(f"\n各级父目录:")
for i, parent in enumerate(p4.parents):
    print(f"  父目录 {i+1}: {parent}")
print()

# 5. 路径转换
print("=== 5. 路径转换 ===")

# 转换为绝对路径
p = Path("../dir/file.txt")
abs_p = p.absolute()
print(f"相对路径: {p}")
print(f"绝对路径: {abs_p}")

# 转换为规范化路径
p = Path("dir/./subdir/../file.txt")
norm_p = p.resolve()
print(f"\n原始路径: {p}")
print(f"规范化路径: {norm_p}")

# 转换为相对路径
base_dir = Path("/home/user")
target_dir = Path("/home/user/documents/files")
rel_p = target_dir.relative_to(base_dir)
print(f"\n从 {base_dir} 到 {target_dir} 的相对路径: {rel_p}")

# 转换为字符串
p = Path("dir", "file.txt")
str_p = str(p)
print(f"\n路径对象: {p}")
print(f"字符串表示: {str_p}")
print(f"类型: {type(str_p)}")

# 转换为文件URI
uri_p = p.as_uri()
print(f"\n文件URI: {uri_p}")
print()

# 6. 文件和目录检查
print("=== 6. 文件和目录检查 ===")

# 创建测试文件和目录
os.makedirs("test_dir", exist_ok=True)
with open("test_file.txt", "w") as f:
    f.write("test content")

# 路径存在性检查
p_file = Path("test_file.txt")
p_dir = Path("test_dir")
p_nonexistent = Path("nonexistent.txt")

print(f"p_file.exists() = {p_file.exists()}")
print(f"p_dir.exists() = {p_dir.exists()}")
print(f"p_nonexistent.exists() = {p_nonexistent.exists()}")

# 文件类型检查
print(f"\np_file.is_file() = {p_file.is_file()}")
print(f"p_dir.is_file() = {p_dir.is_file()}")

print(f"p_file.is_dir() = {p_file.is_dir()}")
print(f"p_dir.is_dir() = {p_dir.is_dir()}")

# 检查是否为符号链接（Windows可能需要管理员权限）
if os.name != 'nt':  # Windows不支持符号链接
    try:
        os.symlink("test_file.txt", "test_link.txt")
        p_link = Path("test_link.txt")
        print(f"\np_link.is_symlink() = {p_link.is_symlink()}")
        print(f"p_link.resolve() = {p_link.resolve()}")
        os.remove("test_link.txt")
    except Exception as e:
        print(f"符号链接操作失败: {e}")
else:
    print("\nWindows系统可能不支持符号链接操作")

# 检查是否为挂载点
print(f"\nPath('/').is_mount() = {Path('/').is_mount()}")  # Unix系统根目录
if os.name == 'nt':
    print(f"Path('C:/').is_mount() = {Path('C:/').is_mount()}")  # Windows C盘

# 检查是否为绝对路径
print(f"\np_file.is_absolute() = {p_file.is_absolute()}")
print(f"p_file.absolute().is_absolute() = {p_file.absolute().is_absolute()}")

# 清理测试文件和目录
os.remove("test_file.txt")
os.rmdir("test_dir")
print()

# 7. 文件和目录操作
print("=== 7. 文件和目录操作 ===")

# 创建目录
print("创建目录:")
Path("dir1").mkdir(exist_ok=True)
print(f"Path('dir1').mkdir() = 目录已创建")

# 创建多级目录
Path("dir2", "subdir1", "subdir2").mkdir(parents=True, exist_ok=True)
print(f"Path('dir2', 'subdir1', 'subdir2').mkdir(parents=True) = 多级目录已创建")

# 创建文件
print("\n创建文件:")
p = Path("file1.txt")
p.write_text("Hello, pathlib!")
print(f"p.write_text('Hello, pathlib!') = 文件已创建")
print(f"p.read_text() = {repr(p.read_text())}")

# 二进制文件操作
p_bin = Path("binary.bin")
p_bin.write_bytes(b"Hello, binary!")
print(f"\np_bin.write_bytes(b'Hello, binary!') = 二进制文件已创建")
print(f"p_bin.read_bytes() = {p_bin.read_bytes()}")

# 文件重命名
print("\n文件重命名:")
p.rename("file1_renamed.txt")
p_renamed = Path("file1_renamed.txt")
print(f"p.rename('file1_renamed.txt') = 文件已重命名")
print(f"p_renamed.read_text() = {repr(p_renamed.read_text())}")

# 文件移动
print("\n文件移动:")
p_renamed.rename(Path("dir1") / "file_moved.txt")
p_moved = Path("dir1", "file_moved.txt")
print(f"p_renamed.rename(Path('dir1') / 'file_moved.txt') = 文件已移动")
print(f"p_moved.exists() = {p_moved.exists()}")

# 文件复制（需要shutil模块）
print("\n文件复制:")
import shutil
shutil.copy(p_moved, Path("dir2") / "file_copied.txt")
p_copied = Path("dir2", "file_copied.txt")
print(f"shutil.copy(p_moved, Path('dir2') / 'file_copied.txt') = 文件已复制")
print(f"p_copied.read_text() = {repr(p_copied.read_text())}")

# 删除文件
print("\n删除文件:")
p_bin.unlink()
print(f"p_bin.unlink() = 二进制文件已删除")
print(f"p_bin.exists() = {p_bin.exists()}")

# 删除目录
print("\n删除目录:")
Path("dir2", "subdir1", "subdir2").rmdir()  # 只能删除空目录
print(f"Path('dir2', 'subdir1', 'subdir2').rmdir() = 空目录已删除")

# 清理所有测试文件和目录
print("\n清理测试文件和目录:")
p_moved.unlink()
p_copied.unlink()
Path("dir2", "subdir1").rmdir()
Path("dir2").rmdir()
Path("dir1").rmdir()
print("所有测试文件和目录已清理")
print()

# 8. 文件属性获取
print("=== 8. 文件属性获取 ===")

# 创建测试文件
with open("test_attr.txt", "w") as f:
    f.write("test content for attributes")

p = Path("test_attr.txt")

# 获取文件大小
print(f"p.stat().st_size = {p.stat().st_size} bytes")

# 获取文件时间
print(f"p.stat().st_ctime = {p.stat().st_ctime} (创建时间)")
print(f"p.stat().st_mtime = {p.stat().st_mtime} (修改时间)")
print(f"p.stat().st_atime = {p.stat().st_atime} (访问时间)")

# 转换时间戳为可读格式
print(f"创建时间(可读): {time.ctime(p.stat().st_ctime)}")
print(f"修改时间(可读): {time.ctime(p.stat().st_mtime)}")
print(f"访问时间(可读): {time.ctime(p.stat().st_atime)}")

# 获取文件权限
print(f"\np.stat().st_mode = {oct(p.stat().st_mode)} (文件权限)")

# 获取文件所有者（Unix系统）
if os.name != 'nt':
    import pwd
    owner = pwd.getpwuid(p.stat().st_uid).pw_name
    print(f"文件所有者: {owner}")

# 快速获取修改时间
print(f"\np.lstat().st_mtime = {p.lstat().st_mtime} (不跟随符号链接的修改时间)")

# 清理测试文件
p.unlink()
print()

# 9. 目录遍历
print("=== 9. 目录遍历 ===")

# 创建测试目录结构
os.makedirs("test_dir/subdir1", exist_ok=True)
os.makedirs("test_dir/subdir2", exist_ok=True)

with open("test_dir/file1.txt", "w") as f:
    f.write("file1 content")
with open("test_dir/file2.txt", "w") as f:
    f.write("file2 content")
with open("test_dir/subdir1/file3.txt", "w") as f:
    f.write("file3 content")
with open("test_dir/subdir1/file4.txt", "w") as f:
    f.write("file4 content")
with open("test_dir/subdir2/file5.txt", "w") as f:
    f.write("file5 content")

p = Path("test_dir")

# 列出目录内容
print("列出目录内容:")
for item in p.iterdir():
    print(f"  {item}")

# 递归遍历目录（深度优先）
print("\n递归遍历目录（深度优先）:")
for item in p.glob("**/*"):
    print(f"  {item}")

# 按模式匹配文件
print("\n匹配所有.txt文件:")
for item in p.glob("**/*.txt"):
    print(f"  {item}")

# 使用rglob进行递归匹配
print("\n使用rglob匹配所有.txt文件:")
for item in p.rglob("*.txt"):
    print(f"  {item}")

# 匹配特定模式
print("\n匹配file1和file2:")
for item in p.glob("file[12].txt"):
    print(f"  {item}")

# 清理测试目录
print("\n清理测试目录:")
for item in p.rglob("*"):
    if item.is_file():
        item.unlink()
    elif item.is_dir():
        item.rmdir()
p.rmdir()
print("测试目录已清理")
print()

# 10. 路径比较
print("=== 10. 路径比较 ===")

# 创建测试文件
with open("file.txt", "w") as f:
    f.write("test content")

# 比较路径对象
p1 = Path("file.txt")
p2 = Path("./file.txt")
p3 = Path("../" + os.path.basename(os.getcwd()), "file.txt")

print(f"p1 = {p1}")
print(f"p2 = {p2}")
print(f"p3 = {p3}")

# 使用 == 比较
print(f"p1 == p2 = {p1 == p2}")
print(f"p1 == p3 = {p1 == p3}")

# 使用is_relative_to比较
print(f"p1.is_relative_to(Path('.')) = {p1.is_relative_to(Path('.'))}")

# 使用samefile比较
print(f"p1.samefile(p2) = {p1.samefile(p2)}")
print(f"p1.samefile(p3) = {p1.samefile(p3)}")

# 路径排序
paths = [Path("file3.txt"), Path("file1.txt"), Path("file2.txt")]
print(f"\n排序前: {paths}")
paths.sort()
print(f"排序后: {paths}")

# 清理测试文件
p1.unlink()
print()

# 11. 高级功能
print("=== 11. 高级功能 ===")

# 分割路径
p = Path("dir/subdir/file.txt")
print(f"路径: {p}")
print(f"p.with_name('newfile.txt') = {p.with_name('newfile.txt')}")  # 替换文件名
print(f"p.with_suffix('.md') = {p.with_suffix('.md')}")  # 替换扩展名
print(f"p.with_stem('newstem') = {p.with_stem('newstem')}")  # 替换文件名部分（Python 3.9+）

# 文件锁定
print("\n文件锁定:")
from pathlib import Path
import fcntl

p = Path("lock.txt")
p.write_text("lock content")

with p.open() as f:
    try:
        fcntl.flock(f, fcntl.LOCK_EX)
        print("文件已锁定")
        # 执行需要锁定的操作
        time.sleep(1)
        print("文件操作完成")
    finally:
        fcntl.flock(f, fcntl.LOCK_UN)
        print("文件已解锁")

# 清理测试文件
p.unlink()
print()

# 12. 实际应用示例
print("=== 12. 实际应用示例 ===")

# 示例1：批量重命名文件
def batch_rename(directory, old_ext, new_ext):
    """批量重命名目录中指定扩展名的文件"""
    directory = Path(directory)
    for file in directory.glob(f"*.{old_ext}"):
        new_file = file.with_suffix(f".{new_ext}")
        file.rename(new_file)
        print(f"重命名: {file.name} -> {new_file.name}")

# 测试批量重命名
print("批量重命名示例:")
Path("rename_test").mkdir(exist_ok=True)
for i in range(3):
    Path(f"rename_test/file{i}.txt").write_text(f"content {i}")

batch_rename("rename_test", "txt", "md")

# 清理测试目录
for file in Path("rename_test").glob("*"):
    file.unlink()
Path("rename_test").rmdir()

# 示例2：统计目录大小
def get_directory_size(directory):
    """计算目录的总大小（字节）"""
    directory = Path(directory)
    total_size = 0
    for file in directory.rglob("*"):
        if file.is_file():
            total_size += file.stat().st_size
    return total_size

# 测试目录大小统计
print("\n目录大小统计示例:")
Path("size_test", "subdir").mkdir(parents=True, exist_ok=True)
Path("size_test/file1.txt").write_text("x" * 100)
Path("size_test/file2.txt").write_text("x" * 200)
Path("size_test/subdir/file3.txt").write_text("x" * 300)

size = get_directory_size("size_test")
print(f"目录大小: {size} bytes")

# 清理测试目录
for file in Path("size_test").rglob("*"):
    if file.is_file():
        file.unlink()
    elif file.is_dir():
        file.rmdir()
Path("size_test").rmdir()

# 示例3：查找最近修改的文件
def find_recently_modified(directory, num_files=5):
    """查找目录中最近修改的n个文件"""
    directory = Path(directory)
    files = []
    for file in directory.rglob("*"):
        if file.is_file():
            files.append((file.stat().st_mtime, file))
    
    # 按修改时间排序（最新的在前）
    files.sort(reverse=True, key=lambda x: x[0])
    
    return [file for _, file in files[:num_files]]

# 测试查找最近修改的文件
print("\n查找最近修改的文件示例:")
Path("recent_test", "subdir").mkdir(parents=True, exist_ok=True)

# 创建不同时间修改的文件
for i in range(5):
    file = Path(f"recent_test/file{i}.txt")
    file.write_text(f"content {i}")
    time.sleep(0.1)  # 间隔0.1秒创建文件

recent_files = find_recently_modified("recent_test")
print("最近修改的文件:")
for file in recent_files:
    print(f"  {file} - 修改时间: {time.ctime(file.stat().st_mtime)}")

# 清理测试目录
for file in Path("recent_test").rglob("*"):
    if file.is_file():
        file.unlink()
    elif file.is_dir():
        file.rmdir()
Path("recent_test").rmdir()
print()

# 13. 与os.path模块的比较
print("=== 13. 与os.path模块的比较 ===")

print("| 功能 | os.path模块 | pathlib模块 |")
print("|------|------------|-------------|")
print("| 接口风格 | 函数式 | 面向对象 |")
print("| 路径拼接 | os.path.join(a, b) | Path(a) / b |")
print("| 路径分解 | os.path.split(p) | (p.parent, p.name) |")
print("| 扩展名获取 | os.path.splitext(p)[1] | p.suffix |")
print("| 文件存在检查 | os.path.exists(p) | p.exists() |")
print("| 文件大小 | os.path.getsize(p) | p.stat().st_size |")
print("| 目录创建 | os.makedirs(p) | p.mkdir(parents=True) |")
print("| 文件读取 | open(p).read() | p.read_text() |")
print("| 目录遍历 | os.walk(p) | p.glob('**/*') |")
print("| 路径比较 | os.path.samefile(p1, p2) | p1.samefile(p2) |")
print("| 路径规范化 | os.path.normpath(p) | p.resolve() |")

print("\nos.path示例:")
print("   import os.path")
print("   path = os.path.join('dir', 'file.txt')")
print("   if os.path.exists(path) and os.path.isfile(path):")
print("       content = open(path).read()")
print("       size = os.path.getsize(path)")
print("       print(f'File size: {size} bytes')")

print("\npathlib示例:")
print("   from pathlib import Path")
print("   path = Path('dir') / 'file.txt'")
print("   if path.exists() and path.is_file():")
print("       content = path.read_text()")
print("       size = path.stat().st_size")
print("       print(f'File size: {size} bytes')")
print()

# 14. 最佳实践
print("=== 14. 最佳实践 ===")

print("1. 使用pathlib代替os.path进行路径操作")
print("   pathlib提供了更直观的面向对象接口，代码可读性更高")

print("\n2. 使用 / 运算符拼接路径")
print("   path = Path('dir') / 'subdir' / 'file.txt'")
print("   避免使用字符串拼接，确保跨平台兼容性")

print("\n3. 使用Path.home()和Path.cwd()获取标准路径")
print("   home_dir = Path.home()")
print("   current_dir = Path.cwd()")

print("\n4. 使用mkdir(parents=True)创建多级目录")
print("   Path('dir1', 'dir2', 'dir3').mkdir(parents=True, exist_ok=True)")

print("\n5. 使用write_text/read_text进行文本文件操作")
print("   path = Path('file.txt')")
print("   path.write_text('Hello')")
print("   content = path.read_text()")

print("\n6. 使用glob/rglob进行目录遍历")
print("   for file in Path('dir').rglob('*.txt'):")
print("       print(file)")

print("\n7. 使用resolve()获取规范化绝对路径")
print("   norm_path = Path('dir/./subdir/../file.txt').resolve()")

print("\n8. 使用with_name()和with_suffix()修改文件名和扩展名")
print("   new_file = Path('file.txt').with_suffix('.md')")

print("\n9. 使用try-except处理文件操作异常")
print("   try:")
print("       Path('file.txt').unlink()")
print("   except FileNotFoundError:")
print("       pass")

print("\n10. 考虑向后兼容性")
print("    如果需要支持Python 3.4以下版本，使用os.path模块")
print()

# 15. 常见错误和陷阱
print("=== 15. 常见错误和陷阱 ===")

print("1. 忘记处理文件存在性")
print("   # 错误:")
print("   Path('file.txt').unlink()  # 文件不存在时会抛出异常")
print("   # 正确:")
print("   try:")
print("       Path('file.txt').unlink()")
print("   except FileNotFoundError:")
print("       pass")

print("\n2. 目录创建时忘记设置parents=True")
print("   # 错误:")
print("   Path('dir1', 'dir2').mkdir()  # dir1不存在时会抛出异常")
print("   # 正确:")
print("   Path('dir1', 'dir2').mkdir(parents=True)")

print("\n3. 混淆相对路径和绝对路径")
print("   # 错误:")
print("   Path('file.txt')  # 相对于当前工作目录")
print("   # 正确:")
print("   Path.cwd() / 'file.txt'  # 明确的绝对路径")

print("\n4. 在Windows上使用Unix路径分隔符")
print("   # 错误:")
print("   Path('/dir/file.txt')  # Windows不识别")
print("   # 正确:")
print("   Path('dir') / 'file.txt'  # 自动使用正确的分隔符")

print("\n5. 路径对象与字符串混用")
print("   # 错误:")
print("   path = Path('dir') + '/file.txt'  # 类型错误")
print("   # 正确:")
print("   path = Path('dir') / 'file.txt'")

print("\n6. 忽略文件操作的异常")
print("   # 错误:")
print("   Path('file.txt').write_text('content')  # 可能因权限问题失败")
print("   # 正确:")
print("   try:")
print("       Path('file.txt').write_text('content')")
print("   except PermissionError:")
print("       print('Permission denied')")
print()

# 16. 总结
print("=== 16. pathlib模块总结 ===")
print("pathlib模块是Python 3.4+中推荐的路径处理方式，提供了面向对象的API设计。")
print("主要优势：")
print("- 面向对象的API设计，提高代码可读性和可维护性")
print("- 统一的路径表示，自动适应不同操作系统")
print("- 丰富的文件和目录操作功能")
print("- 内置文件属性获取和比较功能")
print("- 支持链式调用，代码更简洁")
print("- 与Python标准库的其他模块良好集成")
print()
print("主要劣势：")
print("- 仅支持Python 3.4+")
print("- 对于习惯了os.path函数式风格的用户需要适应")
print("- 某些高级功能仍需要结合其他模块使用（如文件复制需要shutil）")
print()
print("使用建议：")
print("- 在Python 3.4+项目中，优先使用pathlib模块进行路径操作")
print("- 对于需要向后兼容的项目，可以使用os.path模块或六模块（six）进行兼容处理")
print("- 结合上下文管理器使用文件操作，确保资源正确释放")
print("- 使用异常处理包装文件操作，提高代码健壮性")
