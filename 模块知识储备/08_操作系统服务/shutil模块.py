#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
shutil模块 - 高级文件操作

shutil模块提供了高级文件操作功能，包括文件复制、移动、删除、归档等。
它是os模块的补充，提供了更便捷的文件处理方法。

主要功能包括：
- 文件和目录的复制、移动和删除
- 高级文件操作（如权限保留）
- 归档和压缩操作
- 磁盘使用情况查询
"""

import shutil
import os
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. shutil模块基本介绍")
print("=" * 50)
print("shutil模块提供了高级文件操作功能")
print("它是os模块的补充，提供了更便捷的文件处理方法")

# ===========================
# 2. 文件复制
# ===========================
print("\n" + "=" * 50)
print("2. 文件复制")
print("=" * 50)

# 创建一个测试文件
print("创建测试文件...")
with open("source.txt", "w") as f:
    f.write("Hello, shutil! This is a test file.")

# 基本复制
print("\n演示基本文件复制:")
shutil.copy("source.txt", "destination.txt")
print(f"源文件是否存在: {os.path.exists('source.txt')}")
print(f"目标文件是否存在: {os.path.exists('destination.txt')}")

# 查看文件内容
with open("destination.txt", "r") as f:
    content = f.read()
    print(f"目标文件内容: {content}")

# 复制并保留元数据
print("\n演示复制并保留元数据:")
shutil.copy2("source.txt", "destination_with_metadata.txt")

# 检查文件元数据
import time
print(f"源文件修改时间: {time.ctime(os.path.getmtime('source.txt'))}")
print(f"目标文件修改时间: {time.ctime(os.path.getmtime('destination_with_metadata.txt'))}")

# 复制文件到目录
print("\n演示复制文件到目录:")
os.makedirs("test_dir", exist_ok=True)
shutil.copy("source.txt", "test_dir/")
print(f"文件是否复制到目录: {os.path.exists('test_dir/source.txt')}")

# ===========================
# 3. 目录操作
# ===========================
print("\n" + "=" * 50)
print("3. 目录操作")
print("=" * 50)

# 创建测试目录结构
print("创建测试目录结构...")
os.makedirs("dir1/subdir1", exist_ok=True)
os.makedirs("dir1/subdir2", exist_ok=True)
with open("dir1/file1.txt", "w") as f:
    f.write("File in dir1")
with open("dir1/subdir1/file2.txt", "w") as f:
    f.write("File in subdir1")

# 复制目录
print("\n演示复制目录:")
shutil.copytree("dir1", "dir2")
print(f"源目录是否存在: {os.path.exists('dir1')}")
print(f"目标目录是否存在: {os.path.exists('dir2')}")
print(f"子目录是否复制: {os.path.exists('dir2/subdir1/file2.txt')}")

# 复制目录时过滤文件
print("\n演示复制目录时过滤文件:")
def ignore_txt_files(src, names):
    """忽略.txt文件"""
    return [name for name in names if name.endswith('.txt')]

shutil.copytree("dir1", "dir3", ignore=ignore_txt_files)
print(f"目录是否复制: {os.path.exists('dir3')}")
print(f".txt文件是否被过滤: {os.path.exists('dir3/file1.txt')}")
print(f"子目录是否存在: {os.path.exists('dir3/subdir1')}")

# ===========================
# 4. 文件和目录移动
# ===========================
print("\n" + "=" * 50)
print("4. 文件和目录移动")
print("=" * 50)

# 移动文件
print("演示移动文件:")
shutil.move("destination.txt", "test_dir/")
print(f"文件是否移动到目录: {os.path.exists('test_dir/destination.txt')}")
print(f"原位置文件是否存在: {os.path.exists('destination.txt')}")

# 重命名文件（移动的一种特殊情况）
print("\n演示重命名文件:")
shutil.move("source.txt", "renamed_source.txt")
print(f"重命名后文件是否存在: {os.path.exists('renamed_source.txt')}")
print(f"原名称文件是否存在: {os.path.exists('source.txt')}")

# 移动目录
print("\n演示移动目录:")
shutil.move("dir2", "test_dir/")
print(f"目录是否移动到test_dir: {os.path.exists('test_dir/dir2')}")
print(f"原位置目录是否存在: {os.path.exists('dir2')}")

# ===========================
# 5. 文件和目录删除
# ===========================
print("\n" + "=" * 50)
print("5. 文件和目录删除")
print("=" * 50)

# 删除文件
print("演示删除文件:")
shutil.os.remove("destination_with_metadata.txt")  # shutil没有直接删除文件的函数，使用os.remove
print(f"文件是否被删除: {not os.path.exists('destination_with_metadata.txt')}")

# 删除目录（必须为空）
print("\n演示删除空目录:")
os.makedirs("empty_dir", exist_ok=True)
os.rmdir("empty_dir")  # shutil没有直接删除空目录的函数，使用os.rmdir
print(f"空目录是否被删除: {not os.path.exists('empty_dir')}")

# 删除目录及其内容
print("\n演示删除目录及其内容:")
shutil.rmtree("dir3")
print(f"目录及其内容是否被删除: {not os.path.exists('dir3')}")

# ===========================
# 6. 归档和压缩
# ===========================
print("\n" + "=" * 50)
print("6. 归档和压缩")
print("=" * 50)

# 创建归档文件（tar格式）
print("演示创建归档文件 (tar格式):")
tar_archive = shutil.make_archive("archive", "tar", "dir1")
print(f"tar归档文件是否创建: {os.path.exists(tar_archive)}")
print(f"tar归档文件路径: {tar_archive}")

# 创建压缩归档文件（tar.gz格式）
print("\n演示创建压缩归档文件 (tar.gz格式):")
tar_gz_archive = shutil.make_archive("archive", "gztar", "dir1")
print(f"tar.gz归档文件是否创建: {os.path.exists(tar_gz_archive)}")
print(f"tar.gz归档文件路径: {tar_gz_archive}")

# 创建zip格式归档文件
print("\n演示创建zip格式归档文件:")
zip_archive = shutil.make_archive("archive", "zip", "dir1")
print(f"zip归档文件是否创建: {os.path.exists(zip_archive)}")
print(f"zip归档文件路径: {zip_archive}")

# 解压归档文件
print("\n演示解压归档文件:")
extract_dir = "extracted_archive"
os.makedirs(extract_dir, exist_ok=True)
shutil.unpack_archive(zip_archive, extract_dir)
print(f"归档文件是否解压: {os.path.exists(extract_dir)}")
print(f"解压后的文件是否存在: {os.path.exists(f'{extract_dir}/dir1/file1.txt')}")

# ===========================
# 7. 磁盘使用情况
# ===========================
print("\n" + "=" * 50)
print("7. 磁盘使用情况")
print("=" * 50)

# 获取磁盘使用情况
print("演示获取磁盘使用情况:")
disk_usage = shutil.disk_usage(".")
print(f"总容量: {disk_usage.total / (1024**3):.2f} GB")
print(f"已使用: {disk_usage.used / (1024**3):.2f} GB")
print(f"可用空间: {disk_usage.free / (1024**3):.2f} GB")
print(f"使用率: {disk_usage.used / disk_usage.total * 100:.1f}%")

# ===========================
# 8. 其他高级功能
# ===========================
print("\n" + "=" * 50)
print("8. 其他高级功能")
print("=" * 50)

# 获取系统磁盘分区
print("演示获取系统磁盘分区:")
try:
    disk_partitions = shutil.disk_partitions()
    print(f"磁盘分区数量: {len(disk_partitions)}")
    for partition in disk_partitions:
        print(f"分区: {partition.device} -> 挂载点: {partition.mountpoint} -> 文件系统: {partition.fstype}")
except AttributeError:
    print("当前Python版本不支持disk_partitions()函数")

# 获取文件系统的总容量和可用空间
print("\n演示获取特定路径的磁盘使用情况:")
current_dir_usage = shutil.disk_usage(".")
print(f"当前目录所在磁盘总容量: {current_dir_usage.total / (1024**3):.2f} GB")
print(f"当前目录所在磁盘可用空间: {current_dir_usage.free / (1024**3):.2f} GB")

# 复制文件对象
print("\n演示复制文件对象:")
with open("renamed_source.txt", "rb") as src_file:
    with open("copy_from_object.txt", "wb") as dst_file:
        shutil.copyfileobj(src_file, dst_file)

print(f"通过文件对象复制的文件是否存在: {os.path.exists('copy_from_object.txt')}")
with open("copy_from_object.txt", "r") as f:
    content = f.read()
    print(f"复制的文件内容: {content}")

# 查看支持的归档格式
print("\n演示查看支持的归档格式:")
print(f"支持的归档格式: {shutil.get_archive_formats()}")
print(f"支持的解压格式: {shutil.get_unpack_formats()}")

# ===========================
# 9. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

# 示例1: 备份文件
def backup_file(file_path, backup_dir="backups"):
    """备份文件到指定目录"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return False
    
    # 创建备份目录
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # 获取文件名
    file_name = os.path.basename(file_path)
    
    # 创建带时间戳的备份文件名
    import datetime
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file_name = f"{file_name}.backup_{timestamp}"
    backup_path = os.path.join(backup_dir, backup_file_name)
    
    # 复制文件
    try:
        shutil.copy2(file_path, backup_path)
        print(f"文件已备份到: {backup_path}")
        return True
    except Exception as e:
        print(f"备份文件失败: {e}")
        return False

# 测试备份功能
print("示例1: 备份文件")
backup_file("renamed_source.txt")

# 示例2: 批量重命名文件
def batch_rename(directory, old_ext, new_ext):
    """批量重命名文件扩展名"""
    if not os.path.exists(directory):
        print(f"目录不存在: {directory}")
        return 0
    
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            old_path = os.path.join(directory, filename)
            new_filename = filename.replace(old_ext, new_ext)
            new_path = os.path.join(directory, new_filename)
            shutil.move(old_path, new_path)
            count += 1
            print(f"重命名: {old_path} -> {new_path}")
    
    print(f"共重命名 {count} 个文件")
    return count

# 测试批量重命名功能
print("\n示例2: 批量重命名文件")
os.makedirs("rename_test", exist_ok=True)
for i in range(3):
    with open(f"rename_test/file{i}.txt", "w") as f:
        f.write(f"Test file {i}")

batch_rename("rename_test", ".txt", ".md")

# 示例3: 清理临时文件
def cleanup_temp_files(directory, days=7):
    """清理指定目录下超过指定天数的临时文件"""
    if not os.path.exists(directory):
        print(f"目录不存在: {directory}")
        return 0
    
    count = 0
    import time
    current_time = time.time()
    days_in_seconds = days * 24 * 60 * 60
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_mtime = os.path.getmtime(file_path)
            if current_time - file_mtime > days_in_seconds:
                try:
                    os.remove(file_path)
                    count += 1
                    print(f"已删除临时文件: {file_path}")
                except Exception as e:
                    print(f"删除文件失败 {file_path}: {e}")
    
    print(f"共清理 {count} 个临时文件")
    return count

# 示例4: 磁盘空间监控
def check_disk_space(path=".", threshold=10):
    """检查磁盘空间，如果可用空间低于阈值则发出警告"""
    try:
        usage = shutil.disk_usage(path)
        total = usage.total
        free = usage.free
        used = usage.used
        
        free_percent = (free / total) * 100
        
        print(f"磁盘使用情况:")
        print(f"  总容量: {total / (1024**3):.2f} GB")
        print(f"  已使用: {used / (1024**3):.2f} GB")
        print(f"  可用空间: {free / (1024**3):.2f} GB")
        print(f"  可用百分比: {free_percent:.1f}%")
        
        if free_percent < threshold:
            print(f"警告: 磁盘可用空间低于 {threshold}%")
            return False
        else:
            print(f"磁盘空间充足 (>{threshold}%)")
            return True
            
    except Exception as e:
        print(f"检查磁盘空间失败: {e}")
        return False

# 测试磁盘空间监控功能
print("\n示例4: 磁盘空间监控")
check_disk_space(".", threshold=20)

# ===========================
# 10. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("10. 最佳实践和注意事项")
print("=" * 50)

print("1. 复制文件时优先使用shutil.copy2()保留文件元数据")
print("2. 使用shutil.copytree()时注意过滤不需要的文件")
print("3. 删除目录时使用shutil.rmtree()要格外小心，它会递归删除所有内容")
print("4. 创建归档文件时选择合适的格式，考虑跨平台兼容性")
print("5. 在处理大文件时，使用shutil.copyfileobj()并指定缓冲区大小可以提高性能")
print("6. 始终在操作文件前检查文件是否存在")
print("7. 备份重要文件时使用带时间戳的命名方式")
print("8. 使用try-except块捕获可能的异常")
print("9. 注意权限问题，确保程序有足够的权限执行文件操作")
print("10. 跨平台开发时注意不同操作系统的文件路径分隔符差异")

# ===========================
# 11. 清理测试文件
# ===========================
print("\n" + "=" * 50)
print("11. 清理测试文件")
print("=" * 50)

# 列出所有测试文件和目录
test_files = [
    "renamed_source.txt",
    "copy_from_object.txt",
    "archive.tar",
    "archive.tar.gz",
    "archive.zip",
    "test_dir",
    "dir1",
    "extracted_archive",
    "backups",
    "rename_test"
]

# 清理测试文件
print("清理测试文件和目录...")
for item in test_files:
    if os.path.exists(item):
        if os.path.isdir(item):
            shutil.rmtree(item)
        else:
            os.remove(item)
        print(f"已清理: {item}")

print("所有测试文件和目录已清理完成")

# ===========================
# 12. 总结
# ===========================
print("\n" + "=" * 50)
print("12. 总结")
print("=" * 50)
print("shutil模块提供了丰富的高级文件操作功能：")
print("- 文件和目录的复制、移动和删除")
print("- 支持保留文件元数据")
print("- 归档和压缩操作")
print("- 磁盘使用情况查询")
print("\n熟练掌握shutil模块可以让文件操作更加便捷高效，")
print("特别适合需要处理大量文件或进行复杂文件操作的场景")
