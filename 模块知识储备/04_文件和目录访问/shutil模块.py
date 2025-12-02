"""
# shutil模块详解：高级文件操作

shutil模块是Python标准库中提供的高级文件操作工具，构建在os模块之上，提供了更便捷的文件和目录操作函数。shutil模块的名称来源于"shell utilities"，主要功能包括文件复制、移动、删除、归档以及目录树操作等。通过shutil模块，Python程序可以轻松执行复杂的文件管理任务。

## 1. 核心功能概览

shutil模块的主要功能可以分为以下几类：

1. **文件复制操作**：复制文件、复制文件权限、复制文件状态信息等
2. **文件移动操作**：移动文件、重命名文件等
3. **目录操作**：递归复制目录树、删除目录树等
4. **文件归档**：创建和提取压缩文件（如ZIP、TAR等）
5. **文件系统空间信息**：获取磁盘使用情况等
6. **高级文件操作**：查找相同文件、复制整个目录结构等

## 2. 文件复制操作

### 2.1 基本文件复制

```python
import shutil
import os

def basic_file_copy_demo():
    # 创建源文件
    source_file = "source.txt"
    destination_file = "destination.txt"
    
    with open(source_file, 'w') as f:
        f.write("这是要复制的文件内容")
    
    print(f"创建源文件: {source_file}")
    
    # 基本的文件复制
    shutil.copy(source_file, destination_file)
    print(f"复制到: {destination_file}")
    
    # 验证复制是否成功
    with open(destination_file, 'r') as f:
        content = f.read()
    print(f"目标文件内容: {content}")
    
    # 清理文件
    os.remove(source_file)
    os.remove(destination_file)
    print("清理完成")

# 运行示例
basic_file_copy_demo()
```

### 2.2 复制文件权限和状态

```python
import shutil
import os
import stat

def copy_file_metadata_demo():
    source_file = "source_meta.txt"
    destination_file = "destination_meta.txt"
    
    # 创建源文件
    with open(source_file, 'w') as f:
        f.write("测试文件元数据")
    
    print(f"创建源文件: {source_file}")
    
    # 修改源文件权限（仅在类Unix系统上有效）
    if os.name != 'nt':  # 非Windows系统
        os.chmod(source_file, stat.S_IRUSR | stat.S_IWUSR)  # 仅用户可读写
        print(f"修改源文件权限为用户可读写")
    
    # 复制文件内容和权限
    shutil.copy2(source_file, destination_file)
    print(f"使用copy2复制到: {destination_file} (保留元数据)")
    
    # 比较文件的修改时间
    src_stat = os.stat(source_file)
    dst_stat = os.stat(destination_file)
    
    print(f"\n源文件修改时间: {src_stat.st_mtime}")
    print(f"目标文件修改时间: {dst_stat.st_mtime}")
    print(f"修改时间相同: {src_stat.st_mtime == dst_stat.st_mtime}")
    
    # 清理文件
    os.remove(source_file)
    os.remove(destination_file)
    print("清理完成")

# 运行示例
copy_file_metadata_demo()
```

### 2.3 复制文件对象

```python
import shutil
import os

def copy_file_objects_demo():
    source_file = "source_obj.txt"
    destination_file = "destination_obj.txt"
    
    # 创建源文件
    with open(source_file, 'w') as f:
        f.write("这是通过文件对象复制的内容")
    
    print(f"创建源文件: {source_file}")
    
    # 使用文件对象复制
    with open(source_file, 'rb') as src, open(destination_file, 'wb') as dst:
        shutil.copyfileobj(src, dst)
    
    print(f"使用copyfileobj复制到: {destination_file}")
    
    # 验证复制是否成功
    with open(destination_file, 'r') as f:
        content = f.read()
    print(f"目标文件内容: {content}")
    
    # 清理文件
    os.remove(source_file)
    os.remove(destination_file)
    print("清理完成")

# 运行示例
copy_file_objects_demo()
```

## 3. 文件移动和重命名

```python
import shutil
import os

def file_move_rename_demo():
    # 创建测试文件
    original_file = "original.txt"
    with open(original_file, 'w') as f:
        f.write("这是一个测试文件")
    
    print(f"创建原始文件: {original_file}")
    
    # 重命名文件（在同一目录）
    renamed_file = "renamed.txt"
    shutil.move(original_file, renamed_file)
    print(f"重命名为: {renamed_file}")
    
    # 创建目标目录
    target_dir = "target_directory"
    os.makedirs(target_dir, exist_ok=True)
    print(f"创建目标目录: {target_dir}")
    
    # 移动文件到新目录
    target_path = os.path.join(target_dir, renamed_file)
    shutil.move(renamed_file, target_dir)
    print(f"移动到: {target_path}")
    
    # 验证移动是否成功
    moved_path = os.path.join(target_dir, renamed_file)
    exists = os.path.exists(moved_path)
    print(f"文件移动后是否存在: {exists}")
    
    # 清理文件和目录
    os.remove(moved_path)
    os.rmdir(target_dir)
    print("清理完成")

# 运行示例
file_move_rename_demo()
```

## 4. 目录操作

### 4.1 递归复制目录

```python
import shutil
import os

def recursive_directory_copy_demo():
    # 创建源目录结构
    src_dir = "source_directory"
    os.makedirs(os.path.join(src_dir, "subdir"), exist_ok=True)
    
    # 在源目录中创建文件
    with open(os.path.join(src_dir, "file1.txt"), 'w') as f:
        f.write("根目录中的文件")
    
    with open(os.path.join(src_dir, "subdir", "file2.txt"), 'w') as f:
        f.write("子目录中的文件")
    
    print(f"创建源目录结构: {src_dir}")
    print("源目录内容:")
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            print(f"  {os.path.join(root, file)}")
    
    # 目标目录
    dst_dir = "destination_directory"
    
    # 递归复制整个目录树
    shutil.copytree(src_dir, dst_dir)
    print(f"\n递归复制到: {dst_dir}")
    
    # 验证复制是否成功
    print("\n目标目录内容:")
    for root, dirs, files in os.walk(dst_dir):
        for file in files:
            print(f"  {os.path.join(root, file)}")
    
    # 清理目录
    shutil.rmtree(src_dir)
    shutil.rmtree(dst_dir)
    print("\n清理完成")

# 运行示例
recursive_directory_copy_demo()
```

### 4.2 删除目录树

```python
import shutil
import os
import time

def directory_removal_demo():
    # 创建测试目录结构
    test_dir = "test_directory"
    os.makedirs(os.path.join(test_dir, "level1", "level2"), exist_ok=True)
    
    # 在目录中创建一些文件
    with open(os.path.join(test_dir, "file1.txt"), 'w') as f:
        f.write("文件1")
    
    with open(os.path.join(test_dir, "level1", "file2.txt"), 'w') as f:
        f.write("文件2")
    
    with open(os.path.join(test_dir, "level1", "level2", "file3.txt"), 'w') as f:
        f.write("文件3")
    
    print(f"创建测试目录结构: {test_dir}")
    print("目录结构:")
    for root, dirs, files in os.walk(test_dir):
        print(f"  目录: {root}")
        for file in files:
            print(f"    文件: {file}")
    
    # 使用shutil.rmtree删除整个目录树
    print("\n开始删除目录...")
    start_time = time.time()
    shutil.rmtree(test_dir)
    end_time = time.time()
    
    print(f"目录删除完成，耗时: {end_time - start_time:.4f} 秒")
    print(f"目录是否仍然存在: {os.path.exists(test_dir)}")

# 运行示例
directory_removal_demo()
```

## 5. 文件归档操作

### 5.1 创建压缩文件

```python
import shutil
import os
import zipfile

def create_archive_demo():
    # 创建测试文件和目录
    source_dir = "archive_source"
    os.makedirs(source_dir, exist_ok=True)
    
    with open(os.path.join(source_dir, "file1.txt"), 'w') as f:
        f.write("文件1内容")
    
    with open(os.path.join(source_dir, "file2.txt"), 'w') as f:
        f.write("文件2内容")
    
    print(f"创建源目录和文件: {source_dir}")
    
    # 创建ZIP归档
    zip_filename = "archive.zip"
    shutil.make_archive("archive", "zip", source_dir)
    print(f"创建ZIP归档: {zip_filename}")
    
    # 验证ZIP文件是否创建成功
    if os.path.exists(zip_filename):
        print(f"ZIP文件大小: {os.path.getsize(zip_filename)} 字节")
        
        # 查看ZIP文件内容
        print("ZIP文件内容:")
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            for item in zip_ref.namelist():
                print(f"  {item}")
    
    # 清理
    shutil.rmtree(source_dir)
    os.remove(zip_filename)
    print("清理完成")

# 运行示例
create_archive_demo()
```

### 5.2 解压文件

```python
import shutil
import os
import zipfile

def extract_archive_demo():
    # 创建一个测试ZIP文件
    zip_filename = "test_extract.zip"
    source_files = ["file1.txt", "file2.txt"]
    
    # 创建测试文件
    for file in source_files:
        with open(file, 'w') as f:
            f.write(f"这是{file}的内容")
    
    # 创建ZIP文件
    with zipfile.ZipFile(zip_filename, 'w') as zip_ref:
        for file in source_files:
            zip_ref.write(file)
    
    print(f"创建测试ZIP文件: {zip_filename}")
    
    # 清理原始文件
    for file in source_files:
        os.remove(file)
    
    # 解压到指定目录
    extract_dir = "extracted_files"
    os.makedirs(extract_dir, exist_ok=True)
    
    shutil.unpack_archive(zip_filename, extract_dir)
    print(f"解压到目录: {extract_dir}")
    
    # 验证解压结果
    print("解压文件:")
    for root, _, files in os.walk(extract_dir):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"  {file_path}")
            with open(file_path, 'r') as f:
                content = f.read()
            print(f"    内容: {content}")
    
    # 清理
    os.remove(zip_filename)
    shutil.rmtree(extract_dir)
    print("清理完成")

# 运行示例
extract_archive_demo()
```

## 6. 文件系统空间信息

```python
import shutil

def disk_usage_demo():
    # 获取磁盘使用情况
    # 可以指定路径，默认为当前磁盘
    total, used, free = shutil.disk_usage('.')
    
    # 格式化输出（转换为GB）
    def format_size(size_bytes):
        return f"{size_bytes / (1024**3):.2f} GB"
    
    print(f"磁盘使用情况:")
    print(f"  总大小: {format_size(total)}")
    print(f"  已使用: {format_size(used)}")
    print(f"  可用空间: {format_size(free)}")
    print(f"  使用百分比: {used / total * 100:.1f}%")

# 运行示例
disk_usage_demo()
```

## 7. 高级应用示例

### 7.1 安全的文件复制函数

```python
import shutil
import os
import time

def safe_copy(src, dst, overwrite=False, backup=False):
    """
    安全地复制文件，支持覆盖检查和备份功能
    
    参数:
        src: 源文件路径
        dst: 目标文件路径或目录
        overwrite: 如果目标文件存在，是否覆盖
        backup: 如果覆盖，是否备份原文件
    
    返回:
        bool: 复制是否成功
    """
    # 检查源文件是否存在
    if not os.path.isfile(src):
        print(f"错误: 源文件 '{src}' 不存在")
        return False
    
    # 如果目标是目录，则使用源文件的名称
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    
    # 检查目标文件是否已存在
    if os.path.exists(dst):
        if not overwrite:
            print(f"错误: 目标文件 '{dst}' 已存在，且未设置覆盖")
            return False
        
        # 创建备份
        if backup:
            backup_ext = f".bak_{int(time.time())}"
            backup_path = dst + backup_ext
            shutil.copy2(dst, backup_path)
            print(f"创建备份: {backup_path}")
    
    try:
        # 复制文件（保留元数据）
        shutil.copy2(src, dst)
        print(f"成功复制: '{src}' -> '{dst}'")
        return True
    except Exception as e:
        print(f"复制失败: {e}")
        return False

# 测试安全复制函数
def test_safe_copy():
    # 创建测试文件
    src_file = "test_safe_src.txt"
    dst_file = "test_safe_dst.txt"
    
    with open(src_file, 'w') as f:
        f.write("源文件内容")
    
    print("=== 测试1: 基本复制 ===")
    safe_copy(src_file, dst_file)
    
    print("\n=== 测试2: 不覆盖已存在文件 ===")
    with open(src_file, 'w') as f:
        f.write("更新的源文件内容")
    safe_copy(src_file, dst_file, overwrite=False)
    
    print("\n=== 测试3: 覆盖并备份 ===")
    safe_copy(src_file, dst_file, overwrite=True, backup=True)
    
    print("\n=== 测试4: 复制到目录 ===")
    test_dir = "test_dir"
    os.makedirs(test_dir, exist_ok=True)
    safe_copy(src_file, test_dir)
    
    # 清理
    os.remove(src_file)
    os.remove(dst_file)
    # 删除备份文件
    for file in os.listdir('.'):
        if file.startswith(dst_file + ".bak_"):
            os.remove(file)
    # 删除目录中的文件和目录本身
    os.remove(os.path.join(test_dir, os.path.basename(src_file)))
    os.rmdir(test_dir)
    print("\n清理完成")

# 运行测试
test_safe_copy()
```

### 7.2 目录同步工具

```python
import shutil
import os
import filecmp

def sync_directories(src_dir, dst_dir, delete_extraneous=False):
    """
    同步源目录到目标目录
    
    参数:
        src_dir: 源目录路径
        dst_dir: 目标目录路径
        delete_extraneous: 是否删除目标目录中源目录不存在的文件
    """
    # 确保源目录存在
    if not os.path.isdir(src_dir):
        print(f"错误: 源目录 '{src_dir}' 不存在")
        return
    
    # 确保目标目录存在
    os.makedirs(dst_dir, exist_ok=True)
    
    # 比较目录
    dcmp = filecmp.dircmp(src_dir, dst_dir)
    
    # 复制新增或修改的文件
    for filename in dcmp.left_only + dcmp.diff_files:
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)
        
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"复制: '{src_path}' -> '{dst_path}'")
    
    # 递归同步子目录
    for subdir in dcmp.common_dirs:
        sub_src = os.path.join(src_dir, subdir)
        sub_dst = os.path.join(dst_dir, subdir)
        sync_directories(sub_src, sub_dst, delete_extraneous)
    
    # 删除目标目录中源目录不存在的文件
    if delete_extraneous:
        for filename in dcmp.right_only:
            path = os.path.join(dst_dir, filename)
            if os.path.isfile(path):
                os.remove(path)
                print(f"删除: '{path}'")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"删除目录: '{path}'")

# 测试目录同步功能
def test_directory_sync():
    # 创建源目录和文件
    src_dir = "sync_source"
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(os.path.join(src_dir, "subdir"), exist_ok=True)
    
    with open(os.path.join(src_dir, "file1.txt"), 'w') as f:
        f.write("文件1内容")
    
    with open(os.path.join(src_dir, "file2.txt"), 'w') as f:
        f.write("文件2内容")
    
    with open(os.path.join(src_dir, "subdir", "file3.txt"), 'w') as f:
        f.write("子目录文件内容")
    
    # 创建目标目录和一些初始文件
    dst_dir = "sync_destination"
    os.makedirs(dst_dir, exist_ok=True)
    
    with open(os.path.join(dst_dir, "old_file.txt"), 'w') as f:
        f.write("旧文件内容")
    
    print("=== 初始同步 ===")
    sync_directories(src_dir, dst_dir)
    
    # 更新源文件
    with open(os.path.join(src_dir, "file1.txt"), 'w') as f:
        f.write("更新后的文件1内容")
    
    # 添加新文件到源目录
    with open(os.path.join(src_dir, "file4.txt"), 'w') as f:
        f.write("新文件内容")
    
    print("\n=== 更新同步 ===")
    sync_directories(src_dir, dst_dir, delete_extraneous=True)
    
    # 清理
    shutil.rmtree(src_dir)
    shutil.rmtree(dst_dir)
    print("\n清理完成")

# 运行测试
test_directory_sync()
```

### 7.3 查找重复文件

```python
import os
import hashlib
import shutil

def get_file_hash(file_path, block_size=65536):
    """计算文件的MD5哈希值"""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read(block_size)
        while buf:
            hasher.update(buf)
            buf = file.read(block_size)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    """查找目录中的重复文件"""
    # 存储文件哈希值和对应路径
    hash_map = {}
    
    # 遍历目录中的所有文件
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                # 计算文件哈希值
                file_hash = get_file_hash(file_path)
                
                # 如果哈希值已存在，则找到重复文件
                if file_hash in hash_map:
                    hash_map[file_hash].append(file_path)
                else:
                    hash_map[file_hash] = [file_path]
            except (IOError, PermissionError) as e:
                print(f"无法读取文件 {file_path}: {e}")
    
    # 过滤出重复文件
    duplicates = {hash_val: paths for hash_val, paths in hash_map.items() if len(paths) > 1}
    return duplicates

def remove_duplicate_files(duplicates, keep_first=False):
    """
    删除重复文件
    
    参数:
        duplicates: 重复文件字典，键为哈希值，值为文件路径列表
        keep_first: 是否保留每个重复组中的第一个文件
    """
    files_removed = 0
    
    for hash_val, paths in duplicates.items():
        print(f"\n找到重复文件组 (哈希值: {hash_val}):")
        for i, path in enumerate(paths):
            print(f"  {i + 1}. {path}")
        
        # 决定要删除哪些文件
        to_remove = paths[1:] if keep_first else paths[:-1]
        
        # 删除文件
        for path in to_remove:
            try:
                os.remove(path)
                print(f"  删除: {path}")
                files_removed += 1
            except (IOError, PermissionError) as e:
                print(f"  无法删除 {path}: {e}")
    
    return files_removed

# 测试重复文件查找功能
def test_duplicate_finder():
    # 创建测试目录
    test_dir = "duplicate_test"
    os.makedirs(test_dir, exist_ok=True)
    
    # 创建内容相同的文件
    content = "这是重复的文件内容"
    
    # 创建3个重复文件
    duplicate_files = [
        os.path.join(test_dir, "file1.txt"),
        os.path.join(test_dir, "file2.txt"),
        os.path.join(test_dir, "subdir", "file3.txt")
    ]
    
    # 确保子目录存在
    os.makedirs(os.path.join(test_dir, "subdir"), exist_ok=True)
    
    # 创建重复文件
    for file_path in duplicate_files:
        with open(file_path, 'w') as f:
            f.write(content)
    
    # 创建一个唯一文件
    with open(os.path.join(test_dir, "unique.txt"), 'w') as f:
        f.write("这是唯一的内容")
    
    print("=== 查找重复文件 ===")
    duplicates = find_duplicate_files(test_dir)
    
    if duplicates:
        print(f"找到 {len(duplicates)} 组重复文件")
        print("\n=== 模拟删除重复文件 ===")
        # 注意：这里只是演示，不会真正删除文件
        for hash_val, paths in duplicates.items():
            print(f"重复组 (哈希值: {hash_val}):")
            for path in paths:
                print(f"  {path}")
    else:
        print("未找到重复文件")
    
    # 清理测试目录
    shutil.rmtree(test_dir)
    print("\n清理完成")

# 运行测试
test_duplicate_finder()
```

## 8. 注意事项和最佳实践

1. **错误处理**：
   - 文件操作可能抛出多种异常，如`IOError`、`PermissionError`、`FileNotFoundError`等
   - 始终使用try-except捕获可能的异常
   - 对于大文件操作，考虑添加超时或进度监控

2. **跨平台兼容性**：
   - 注意Windows和Unix/Linux系统的路径分隔符差异
   - 避免使用硬编码的路径分隔符
   - 在Windows上，注意文件名大小写不敏感的特性

3. **文件权限**：
   - 复制文件时，使用`shutil.copy2()`保留文件权限和元数据
   - 在不同用户间复制文件时，注意权限变化
   - 处理只读文件时，可能需要先修改权限

4. **大文件操作**：
   - 对于大文件，考虑使用`shutil.copyfileobj()`并设置缓冲区大小
   - 监控复制进度，避免长时间无响应
   - 考虑使用多进程或异步操作来提高大文件处理效率

5. **安全考虑**：
   - 避免在没有验证的情况下覆盖现有文件
   - 复制可执行文件时，注意保留其执行权限
   - 在处理用户提供的文件路径时，防止路径遍历攻击

6. **性能优化**：
   - 对于大量小文件，批量操作比单个操作更高效
   - 使用`shutil.copytree()`的`ignore`参数跳过不需要复制的文件
   - 对于不需要保留元数据的场景，`shutil.copy()`比`shutil.copy2()`略快

## 9. 总结

shutil模块是Python中强大的高级文件操作工具，提供了丰富的函数用于文件复制、移动、删除和归档等操作。通过shutil模块，Python程序可以轻松执行复杂的文件管理任务，而无需关心底层实现细节。

主要优势包括：
- 提供了比os模块更高级、更便捷的文件操作接口
- 支持递归操作，可以处理整个目录树
- 提供文件归档和解压功能
- 支持文件元数据的复制和保留
- 跨平台兼容性，适用于不同操作系统

在实际应用中，shutil模块常用于文件备份、目录同步、数据迁移、软件安装等场景。与os模块结合使用，可以实现几乎所有的文件和目录操作需求。掌握shutil模块的使用，对于编写健壮、高效的文件管理程序至关重要。