# Python shutil模块详解

import shutil
import os
import tempfile
import time

# 1. 模块概述
print("=== 1. shutil模块概述 ===")
print("shutil模块提供了高级文件和目录操作功能，构建在os模块之上。")
print("该模块的主要特点：")
print("- 提供文件复制、移动、删除等高级操作")
print("- 支持目录的递归复制和删除")
print("- 提供文件和目录的权限管理")
print("- 支持文件压缩和归档操作")
print("- 提供磁盘使用情况统计功能")
print("- 支持文件元数据的复制")
print("- 与os模块和pathlib模块良好集成")
print()

# 2. 文件复制操作
print("=== 2. 文件复制操作 ===")

# 创建测试文件
with open("source.txt", "w") as f:
    f.write("Hello, shutil!")

# 基本文件复制
print("1. 基本文件复制：")
shutil.copy("source.txt", "dest.txt")
print("shutil.copy('source.txt', 'dest.txt') = 文件已复制")
print(f"源文件内容: {open('source.txt').read()}")
print(f"目标文件内容: {open('dest.txt').read()}")

# 复制文件和权限
print("\n2. 复制文件和权限：")
shutil.copy2("source.txt", "dest2.txt")
print("shutil.copy2('source.txt', 'dest2.txt') = 文件和权限已复制")

# 复制文件内容（不复制元数据）
print("\n3. 复制文件内容：")
shutil.copyfile("source.txt", "dest3.txt")
print("shutil.copyfile('source.txt', 'dest3.txt') = 文件内容已复制")

# 复制文件对象
print("\n4. 复制文件对象：")
with open("source.txt", "rb") as src, open("dest4.txt", "wb") as dst:
    shutil.copyfileobj(src, dst)
print("shutil.copyfileobj(src, dst) = 文件对象已复制")

# 复制文件的符号链接
print("\n5. 复制文件的符号链接：")
if os.name != 'nt':  # Windows不支持符号链接
    try:
        os.symlink("source.txt", "link.txt")
        shutil.copy2("link.txt", "link_copy.txt")
        print("shutil.copy2('link.txt', 'link_copy.txt') = 符号链接已复制")
        os.remove("link.txt")
        os.remove("link_copy.txt")
    except Exception as e:
        print(f"符号链接操作失败: {e}")
else:
    print("Windows系统可能不支持符号链接操作")

# 清理测试文件
for f in ["source.txt", "dest.txt", "dest2.txt", "dest3.txt", "dest4.txt"]:
    if os.path.exists(f):
        os.remove(f)
print()

# 3. 目录操作
print("=== 3. 目录操作 ===")

# 创建测试目录结构
os.makedirs("src_dir/subdir", exist_ok=True)
with open("src_dir/file1.txt", "w") as f:
    f.write("file1 content")
with open("src_dir/subdir/file2.txt", "w") as f:
    f.write("file2 content")

# 复制目录（仅复制内容）
print("1. 复制目录内容：")
shutil.copytree("src_dir", "dest_dir")
print("shutil.copytree('src_dir', 'dest_dir') = 目录已复制")
print(f"目标目录结构: {list(os.walk('dest_dir'))}")

# 复制目录并过滤文件
print("\n2. 复制目录并过滤文件：")

def ignore_py_files(dir, files):
    """忽略.py文件"""
    return [f for f in files if f.endswith('.py')]

# 创建一个.py文件用于测试
with open("src_dir/test.py", "w") as f:
    f.write("# Python file")

shutil.copytree("src_dir", "dest_dir2", ignore=ignore_py_files)
print("shutil.copytree('src_dir', 'dest_dir2', ignore=ignore_py_files) = 带过滤的目录复制")
print(f"目标目录结构: {list(os.walk('dest_dir2'))}")

# 移动文件或目录
print("\n3. 移动文件或目录：")
shutil.move("dest_dir2", "moved_dir")
print("shutil.move('dest_dir2', 'moved_dir') = 目录已移动")

# 重命名目录
print("\n4. 重命名目录：")
shutil.move("moved_dir", "renamed_dir")
print("shutil.move('moved_dir', 'renamed_dir') = 目录已重命名")

# 删除目录（递归）
print("\n5. 删除目录（递归）：")
shutil.rmtree("dest_dir")
shutil.rmtree("renamed_dir")
print("shutil.rmtree('dest_dir') = 目录已删除")
print("shutil.rmtree('renamed_dir') = 目录已删除")

# 清理测试目录
shutil.rmtree("src_dir")
print()

# 4. 文件元数据操作
print("=== 4. 文件元数据操作 ===")

# 创建测试文件
with open("file.txt", "w") as f:
    f.write("metadata test")

# 获取文件元数据
print("1. 获取文件元数据：")
stat_info = os.stat("file.txt")
print(f"文件大小: {stat_info.st_size} bytes")
print(f"创建时间: {stat_info.st_ctime}")
print(f"修改时间: {stat_info.st_mtime}")

# 复制文件元数据
print("\n2. 复制文件元数据：")
with open("file2.txt", "w") as f:
    f.write("new file")

shutil.copystat("file.txt", "file2.txt")
print("shutil.copystat('file.txt', 'file2.txt') = 文件元数据已复制")

# 比较元数据
stat1 = os.stat("file.txt")
stat2 = os.stat("file2.txt")
print(f"源文件修改时间: {stat1.st_mtime}")
print(f"目标文件修改时间: {stat2.st_mtime}")

# 复制文件和所有元数据
print("\n3. 复制文件和所有元数据：")
shutil.copy2("file.txt", "file3.txt")
print("shutil.copy2('file.txt', 'file3.txt') = 文件和元数据已复制")

# 清理测试文件
for f in ["file.txt", "file2.txt", "file3.txt"]:
    if os.path.exists(f):
        os.remove(f)
print()

# 5. 权限管理
print("=== 5. 权限管理 ===")

# 创建测试文件
with open("permission.txt", "w") as f:
    f.write("permission test")

# 获取当前权限
print("1. 获取当前权限：")
current_mode = os.stat("permission.txt").st_mode
print(f"当前权限: {oct(current_mode)}")

# 修改权限（Unix系统）
if os.name != 'nt':
    print("\n2. 修改文件权限：")
    shutil.chown("permission.txt", user="nobody")  # 可能需要管理员权限
    print("shutil.chown('permission.txt', user='nobody') = 文件所有者已修改")
else:
    print("\n2. Windows系统权限管理可能不同")

# 清理测试文件
os.remove("permission.txt")
print()

# 6. 磁盘使用情况
print("=== 6. 磁盘使用情况 ===")

# 获取磁盘使用情况
print("1. 获取磁盘使用情况：")
disk_usage = shutil.disk_usage("/")  # Unix系统
print(f"总空间: {disk_usage.total} bytes")
print(f"已用空间: {disk_usage.used} bytes")
print(f"可用空间: {disk_usage.free} bytes")

# 获取可用空间百分比
free_percent = (disk_usage.free / disk_usage.total) * 100
print(f"可用空间百分比: {free_percent:.2f}%")

# Windows系统
if os.name == 'nt':
    print("\n2. Windows系统磁盘使用情况：")
    disk_usage_c = shutil.disk_usage("C:/")
    print(f"C盘总空间: {disk_usage_c.total} bytes")
    print(f"C盘已用空间: {disk_usage_c.used} bytes")
    print(f"C盘可用空间: {disk_usage_c.free} bytes")
print()

# 7. 归档和压缩操作
print("=== 7. 归档和压缩操作 ===")

# 创建测试目录结构
os.makedirs("archive_dir/subdir", exist_ok=True)
with open("archive_dir/file1.txt", "w") as f:
    f.write("file1 content")
with open("archive_dir/subdir/file2.txt", "w") as f:
    f.write("file2 content")

# 创建zip归档
print("1. 创建zip归档：")
shutil.make_archive("archive", "zip", "archive_dir")
print("shutil.make_archive('archive', 'zip', 'archive_dir') = zip归档已创建")

# 创建tar归档
print("\n2. 创建tar归档：")
shutil.make_archive("archive", "tar", "archive_dir")
print("shutil.make_archive('archive', 'tar', 'archive_dir') = tar归档已创建")

# 创建gzip压缩的tar归档
print("\n3. 创建gzip压缩的tar归档：")
shutil.make_archive("archive", "gztar", "archive_dir")
print("shutil.make_archive('archive', 'gztar', 'archive_dir') = gztar归档已创建")

# 解压归档
print("\n4. 解压归档：")
shutil.unpack_archive("archive.zip", "extracted_dir")
print("shutil.unpack_archive('archive.zip', 'extracted_dir') = 归档已解压")
print(f"解压后的目录结构: {list(os.walk('extracted_dir'))}")

# 获取支持的归档格式
print("\n5. 支持的归档格式：")
print(f"归档格式: {shutil.get_archive_formats()}")
print(f"解压格式: {shutil.get_unpack_formats()}")

# 清理测试文件和目录
shutil.rmtree("archive_dir")
shutil.rmtree("extracted_dir")
for f in ["archive.zip", "archive.tar", "archive.tar.gz"]:
    if os.path.exists(f):
        os.remove(f)
print()

# 8. 临时文件和目录
print("=== 8. 临时文件和目录 ===")

# 与tempfile模块结合使用
print("1. 创建临时目录：")
temp_dir = tempfile.mkdtemp()
print(f"tempfile.mkdtemp() = 创建临时目录: {temp_dir}")

# 在临时目录中创建文件
with open(os.path.join(temp_dir, "temp.txt"), "w") as f:
    f.write("temporary file")

# 清理临时目录
print("\n2. 清理临时目录：")
shutil.rmtree(temp_dir)
print(f"shutil.rmtree('{temp_dir}') = 临时目录已清理")

# 创建临时文件
print("\n3. 创建临时文件：")
temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_file.write(b"temporary content")
temp_file.close()
print(f"临时文件路径: {temp_file.name}")

# 复制临时文件内容
with open(temp_file.name, "rb") as f:
    content = f.read()
print(f"临时文件内容: {content}")

# 删除临时文件
os.unlink(temp_file.name)
print("临时文件已删除")
print()

# 9. 高级文件操作
print("=== 9. 高级文件操作 ===")

# 创建测试目录结构
os.makedirs("advanced_dir/subdir1", exist_ok=True)
os.makedirs("advanced_dir/subdir2", exist_ok=True)
with open("advanced_dir/file1.txt", "w") as f:
    f.write("file1 content")
with open("advanced_dir/subdir1/file2.txt", "w") as f:
    f.write("file2 content")

# 移动目录内容
print("1. 移动目录内容：")
shutil.move("advanced_dir/subdir1", "advanced_dir/subdir3")
print("shutil.move('advanced_dir/subdir1', 'advanced_dir/subdir3') = 目录已移动")
print(f"目录结构: {list(os.walk('advanced_dir'))}")

# 复制目录内容（不包括父目录）
print("\n2. 复制目录内容：")
shutil.copytree("advanced_dir/subdir3", "advanced_dir/subdir4", dirs_exist_ok=True)  # Python 3.8+
print("shutil.copytree('advanced_dir/subdir3', 'advanced_dir/subdir4') = 目录内容已复制")

# 删除所有文件和目录
print("\n3. 删除所有文件和目录：")
shutil.rmtree("advanced_dir")
print("shutil.rmtree('advanced_dir') = 目录已删除")
print()

# 10. 实际应用示例
print("=== 10. 实际应用示例 ===")

# 示例1：备份文件
def backup_file(file_path, backup_dir="backups"):
    """备份文件到指定目录"""
    import datetime
    
    # 创建备份目录
    os.makedirs(backup_dir, exist_ok=True)
    
    # 生成备份文件名（包含时间戳）
    filename = os.path.basename(file_path)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"{filename}.{timestamp}.bak"
    backup_path = os.path.join(backup_dir, backup_filename)
    
    # 复制文件
    shutil.copy2(file_path, backup_path)
    print(f"文件已备份到: {backup_path}")
    return backup_path

print("1. 备份文件示例：")
# 创建测试文件
with open("to_backup.txt", "w") as f:
    f.write("文件备份测试")

# 备份文件
backup_file("to_backup.txt")

# 示例2：批量复制文件
def batch_copy(source_dir, dest_dir, pattern="*.txt"):
    """批量复制匹配特定模式的文件"""
    import glob
    
    # 创建目标目录
    os.makedirs(dest_dir, exist_ok=True)
    
    # 复制文件
    for file_path in glob.glob(os.path.join(source_dir, pattern)):
        dest_file = os.path.join(dest_dir, os.path.basename(file_path))
        shutil.copy2(file_path, dest_file)
        print(f"复制: {file_path} -> {dest_file}")

print("\n2. 批量复制文件示例：")
# 创建测试目录和文件
os.makedirs("source_dir", exist_ok=True)
for i in range(3):
    with open(os.path.join("source_dir", f"file{i}.txt"), "w") as f:
        f.write(f"file{i} content")

# 批量复制文件
batch_copy("source_dir", "dest_batch")

# 示例3：清理临时文件
def clean_temp_files(directory, days=7):
    """清理指定天数前的临时文件"""
    import time
    
    cutoff_time = time.time() - (days * 24 * 60 * 60)
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) < cutoff_time:
                os.remove(file_path)
                print(f"已删除: {file_path}")

print("\n3. 清理临时文件示例：")
# 创建测试临时文件
os.makedirs("temp_clean", exist_ok=True)
with open(os.path.join("temp_clean", "old.txt"), "w") as f:
    f.write("old file")

# 修改文件时间为30天前
old_file_path = os.path.join("temp_clean", "old.txt")
old_time = time.time() - (30 * 24 * 60 * 60)
os.utime(old_file_path, (old_time, old_time))

# 清理临时文件
clean_temp_files("temp_clean", days=15)

# 示例4：创建归档
def create_archive(source_dir, archive_name):
    """创建目录的归档文件"""
    # 自动选择归档格式（基于扩展名）
    archive_format = os.path.splitext(archive_name)[1][1:]
    if not archive_format:
        archive_format = "zip"  # 默认zip格式
    
    archive_path = shutil.make_archive(
        os.path.splitext(archive_name)[0],
        archive_format,
        source_dir
    )
    
    print(f"归档已创建: {archive_path}")
    return archive_path

print("\n4. 创建归档示例：")
# 创建测试目录和文件
os.makedirs("to_archive/subdir", exist_ok=True)
with open(os.path.join("to_archive", "file1.txt"), "w") as f:
    f.write("file1 content")
with open(os.path.join("to_archive", "subdir", "file2.txt"), "w") as f:
    f.write("file2 content")

# 创建归档
create_archive("to_archive", "archive_example.zip")

# 清理测试文件和目录
os.remove("to_backup.txt")
shutil.rmtree("backups")
shutil.rmtree("source_dir")
shutil.rmtree("dest_batch")
shutil.rmtree("temp_clean")
shutil.rmtree("to_archive")
os.remove("archive_example.zip")
print()

# 11. 最佳实践
print("=== 11. 最佳实践 ===")

print("1. 始终使用异常处理包装文件操作")
print("   try:")
print("       shutil.copy('source.txt', 'dest.txt')")
print("   except FileNotFoundError:")
print("       print('源文件不存在')")
print("   except PermissionError:")
print("       print('权限不足')")

print("\n2. 使用shutil.copy2()替代shutil.copy()")
print("   # shutil.copy2()会复制文件元数据（修改时间、权限等）")
print("   shutil.copy2('source.txt', 'dest.txt')")

print("\n3. 谨慎使用shutil.rmtree()")
print("   # 该函数会递归删除目录及其所有内容，没有确认提示")
print("   if os.path.exists('directory'):")
print("       shutil.rmtree('directory')")

print("\n4. 使用备份功能保护重要文件")
print("   # 在修改或删除重要文件前创建备份")
print("   shutil.copy2('important.txt', 'important.txt.bak')")

print("\n5. 结合pathlib模块使用")
print("   from pathlib import Path")
print("   source = Path('source.txt')")
print("   dest = Path('dest.txt')")
print("   shutil.copy2(source, dest)")

print("\n6. 注意跨平台兼容性")
print("   # Windows和Unix系统的路径分隔符和权限管理不同")
print("   import os")
print("   path = os.path.join('dir', 'file.txt')")

print("\n7. 使用shutil.disk_usage()监控磁盘空间")
print("   # 在执行大量文件操作前检查磁盘空间")
print("   usage = shutil.disk_usage('/')")
print("   if usage.free < required_space:")
print("       print('磁盘空间不足')")

print("\n8. 选择合适的归档格式")
print("   # 根据需求选择归档格式")
print("   - zip: 跨平台兼容性好")
print("   - tar: Unix系统常用")
print("   - gztar: 压缩率高")
print("   - bztar: 更高的压缩率")

print("\n9. 使用shutil.copytree()的ignore参数过滤文件")
print("   def ignore_patterns(*patterns):")
print("       def _ignore_patterns(dir, files):")
print("           return [f for f in files if any(fnmatch.fnmatch(f, p) for p in patterns)]")
print("       return _ignore_patterns")
print("   shutil.copytree('source', 'dest', ignore=ignore_patterns('*.pyc', '__pycache__'))")

print("\n10. 定期清理临时文件")
print("    # 避免临时文件占用过多磁盘空间")
print("    import tempfile")
print("    with tempfile.TemporaryFile() as f:")
print("        f.write(b'temporary content')")
print("    # 文件会自动删除")
print()

# 12. 常见错误和陷阱
print("=== 12. 常见错误和陷阱 ===")

print("1. 目标目录不存在")
print("   # 错误:")
print("   shutil.copy('source.txt', 'nonexistent/dir/dest.txt')  # 会抛出异常")
print("   # 正确:")
print("   import os")
print("   os.makedirs('nonexistent/dir', exist_ok=True)")
print("   shutil.copy('source.txt', 'nonexistent/dir/dest.txt')")

print("\n2. 覆盖现有文件")
print("   # 错误:")
print("   shutil.copy('source.txt', 'existing.txt')  # 会覆盖现有文件")
print("   # 正确:")
print("   if not os.path.exists('existing.txt'):")
print("       shutil.copy('source.txt', 'existing.txt')")

print("\n3. 权限不足")
print("   # 错误:")
print("   shutil.copy('source.txt', '/root/dest.txt')  # 可能没有权限")
print("   # 正确:")
print("   try:")
print("       shutil.copy('source.txt', '/root/dest.txt')")
print("   except PermissionError:")
print("       print('Permission denied')")

print("\n4. 递归删除错误的目录")
print("   # 错误:")
print("   shutil.rmtree('/')  # 会删除整个根目录")
print("   # 正确:")
print("   # 始终检查目录路径")
print("   dir_path = 'safe_directory'")
print("   if dir_path and dir_path != '/':")
print("       shutil.rmtree(dir_path)")

print("\n5. 复制符号链接的目标而不是链接本身")
print("   # 错误:")
print("   shutil.copy('link.txt', 'link_copy.txt')  # 复制的是链接目标的内容")
print("   # 正确:")
print("   import os")
print("   os.symlink(os.readlink('link.txt'), 'link_copy.txt')  # 复制符号链接本身")

print("\n6. 归档格式不支持")
print("   # 错误:")
print("   shutil.make_archive('archive', 'rar', 'dir')  # rar格式可能不支持")
print("   # 正确:")
print("   # 检查支持的归档格式")
print("   print(shutil.get_archive_formats())")

print("\n7. 文件过大导致复制失败")
print("   # 错误:")
print("   shutil.copy('large_file.iso', 'dest.iso')  # 可能因磁盘空间不足失败")
print("   # 正确:")
print("   # 复制前检查磁盘空间")
print("   import os")
print("   file_size = os.path.getsize('large_file.iso')")
print("   usage = shutil.disk_usage('/')")
print("   if usage.free > file_size:")
print("       shutil.copy('large_file.iso', 'dest.iso')")

print("\n8. 跨设备复制失败")
print("   # 错误:")
print("   shutil.move('source.txt', '/mnt/usb/dest.txt')  # 跨设备移动可能失败")
print("   # 正确:")
print("   # 跨设备时先复制再删除")
print("   shutil.copy2('source.txt', '/mnt/usb/dest.txt')")
print("   os.remove('source.txt')")
print()

# 13. 总结
print("=== 13. shutil模块总结 ===")
print("shutil模块是Python中用于高级文件和目录操作的重要模块，构建在os模块之上。")
print("主要优势：")
print("- 提供简单易用的高级文件操作接口")
print("- 支持目录的递归复制和删除")
print("- 提供文件和目录的权限管理")
print("- 支持文件压缩和归档操作")
print("- 提供磁盘使用情况统计功能")
print("- 支持文件元数据的复制")
print("- 与os模块和pathlib模块良好集成")
print()
print("主要劣势：")
print("- 某些功能在不同平台上有差异")
print("- 缺乏交互式操作（如确认提示）")
print("- 处理大文件时可能消耗大量内存")
print("- 部分功能需要管理员权限")
print()
print("使用建议：")
print("- 在需要高级文件操作时使用shutil模块")
print("- 结合异常处理提高代码健壮性")
print("- 谨慎使用递归删除功能")
print("- 注意跨平台兼容性问题")
print("- 定期清理临时文件和目录")
print("- 在执行大量文件操作前检查磁盘空间")
print("- 结合pathlib模块使用，提高代码可读性")
