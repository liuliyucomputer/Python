# shutil模块详解

# shutil模块提供了一系列高级文件操作功能，是Python中文件处理的重要模块之一。

## 模块概述

# shutil模块包含了一系列用于文件和目录操作的函数，这些函数可以：
# - 复制文件和目录
# - 移动文件和目录
# - 删除文件和目录
# - 归档和压缩文件
# - 获取磁盘使用信息
# - 权限管理

## 基本用法

### 导入模块

```python
import shutil
```

### 文件复制

#### shutil.copy()
# 复制文件内容和权限，不复制元数据（如修改时间、访问时间等）。

```python
# 复制文件
source = 'g:/Python/模块知识储备/05_文件处理/README.md'
destination = 'g:/Python/模块知识储备/05_文件处理/README_copy.md'
shutil.copy(source, destination)
print(f"已复制文件: {source} -> {destination}")
```

#### shutil.copy2()
# 复制文件内容、权限和元数据（如修改时间、访问时间等）。

```python
# 复制文件并保留元数据
source = 'g:/Python/模块知识储备/05_文件处理/README.md'
destination = 'g:/Python/模块知识储备/05_文件处理/README_copy2.md'
shutil.copy2(source, destination)
print(f"已复制文件并保留元数据: {source} -> {destination}")
```

#### shutil.copyfile()
# 仅复制文件内容，不复制权限和元数据。

```python
# 仅复制文件内容
source = 'g:/Python/模块知识储备/05_文件处理/README.md'
destination = 'g:/Python/模块知识储备/05_文件处理/README_copyfile.md'
shutil.copyfile(source, destination)
print(f"已复制文件内容: {source} -> {destination}")
```

### 目录操作

#### shutil.copytree()
# 递归复制整个目录树。

```python
# 递归复制目录（注意：此示例仅用于演示，实际运行会创建新目录）
# source_dir = 'g:/Python/模块知识储备/05_文件处理'
# dest_dir = 'g:/Python/模块知识储备/05_文件处理_copy'
# shutil.copytree(source_dir, dest_dir)
# print(f"已复制目录: {source_dir} -> {dest_dir}")
```

#### shutil.rmtree()
递归删除整个目录树。

```python
# 递归删除目录（注意：此示例仅用于演示，实际运行会删除目录）
# dir_to_delete = 'g:/Python/模块知识储备/05_文件处理_copy'
# shutil.rmtree(dir_to_delete)
# print(f"已删除目录: {dir_to_delete}")
```

#### shutil.move()
移动文件或目录，也可用于重命名。

```python
# 移动文件（注意：此示例仅用于演示，实际运行会移动文件）
# source = 'g:/Python/模块知识储备/05_文件处理/README_copy.md'
# destination = 'g:/Python/模块知识储备/05_文件处理/moved_files/README_copy.md'
# shutil.move(source, destination)
# print(f"已移动文件: {source} -> {destination}")

# 重命名文件（注意：此示例仅用于演示，实际运行会重命名文件）
# old_name = 'g:/Python/模块知识储备/05_文件处理/README_copy2.md'
# new_name = 'g:/Python/模块知识储备/05_文件处理/README_renamed.md'
# shutil.move(old_name, new_name)
# print(f"已重命名文件: {old_name} -> {new_name}")
```

### 归档和压缩

#### shutil.make_archive()
创建归档文件（如ZIP、TAR等）。

```python
# 创建ZIP归档文件
# base_name = 'g:/Python/模块知识储备/05_文件处理_archive'
# format = 'zip'
# root_dir = 'g:/Python/模块知识储备/05_文件处理'
# archive_name = shutil.make_archive(base_name, format, root_dir)
# print(f"已创建归档文件: {archive_name}")

# 创建TAR归档文件
# base_name = 'g:/Python/模块知识储备/05_文件处理_archive'
# format = 'tar'
# root_dir = 'g:/Python/模块知识储备/05_文件处理'
# archive_name = shutil.make_archive(base_name, format, root_dir)
# print(f"已创建归档文件: {archive_name}")
```

#### shutil.unpack_archive()
解压缩归档文件。

```python
# 解压缩归档文件（注意：此示例仅用于演示，实际运行需要有归档文件）
# archive_name = 'g:/Python/模块知识储备/05_文件处理_archive.zip'
# extract_dir = 'g:/Python/模块知识储备/05_文件处理_extracted'
# shutil.unpack_archive(archive_name, extract_dir)
# print(f"已解压缩归档文件: {archive_name} -> {extract_dir}")
```

### 磁盘使用信息

#### shutil.disk_usage()
获取磁盘使用信息，返回一个命名元组，包含总空间、已用空间和可用空间（以字节为单位）。

```python
# 获取磁盘使用信息
disk_usage = shutil.disk_usage('g:/')
print(f"总空间: {disk_usage.total} 字节 = {disk_usage.total/(1024*1024*1024):.2f} GB")
print(f"已用空间: {disk_usage.used} 字节 = {disk_usage.used/(1024*1024*1024):.2f} GB")
print(f"可用空间: {disk_usage.free} 字节 = {disk_usage.free/(1024*1024*1024):.2f} GB")
```

### 权限管理

#### shutil.chown()
更改文件或目录的所有者和组（仅在Unix系统上可用）。

```python
# 更改文件所有者和组（仅在Unix系统上可用）
# path = 'g:/Python/模块知识储备/05_文件处理/README.md'
# shutil.chown(path, user='new_owner', group='new_group')
```

## 高级功能

### 忽略模式

在复制目录时，可以使用忽略模式来排除某些文件或目录。

```python
# 使用忽略模式复制目录
def ignore_py_files(dir, files):
    return [f for f in files if f.endswith('.py')]

# source_dir = 'g:/Python/模块知识储备/05_文件处理'
# dest_dir = 'g:/Python/模块知识储备/05_文件处理_no_py'
# shutil.copytree(source_dir, dest_dir, ignore=ignore_py_files)
# print(f"已复制目录（忽略.py文件）: {source_dir} -> {dest_dir}")
```

### 进度跟踪

在复制大文件时，可以使用回调函数来跟踪复制进度。

```python
# 带进度跟踪的文件复制
def copy_with_progress(src, dst, buffer_size=1024*1024):
    """带进度跟踪的文件复制函数"""
    import os
    
    total_size = os.path.getsize(src)
    copied_size = 0
    
    with open(src, 'rb') as fsrc:
        with open(dst, 'wb') as fdst:
            while True:
                buffer = fsrc.read(buffer_size)
                if not buffer:
                    break
                fdst.write(buffer)
                copied_size += len(buffer)
                
                # 计算并显示进度
                progress = (copied_size / total_size) * 100
                print(f"复制进度: {progress:.2f}%", end='\r')
    
    print(f"\n已复制文件: {src} -> {dst}")
    print(f"文件大小: {total_size} 字节")

# 使用示例
# source = 'g:/Python/模块知识储备/05_文件处理/README.md'
# destination = 'g:/Python/模块知识储备/05_文件处理/README_progress.md'
# copy_with_progress(source, destination)
```

## 实际应用示例

### 示例1：批量备份文件

```python
def backup_files(file_list, backup_dir):
    """批量备份文件到指定目录"""
    import os
    
    # 确保备份目录存在
    os.makedirs(backup_dir, exist_ok=True)
    
    backup_count = 0
    for file_path in file_list:
        if os.path.exists(file_path):
            # 获取文件名
            filename = os.path.basename(file_path)
            # 构建备份文件路径
            backup_path = os.path.join(backup_dir, filename)
            # 复制文件并保留元数据
            shutil.copy2(file_path, backup_path)
            backup_count += 1
            print(f"已备份: {file_path} -> {backup_path}")
        else:
            print(f"警告: 文件不存在，跳过备份: {file_path}")
    
    return backup_count

# 使用示例
files_to_backup = [
    'g:/Python/模块知识储备/05_文件处理/README.md',
    'g:/Python/模块知识储备/05_文件处理/os.path模块.py',
    'g:/Python/模块知识储备/05_文件处理/shutil模块.py'
]
backup_directory = 'g:/Python/模块知识储备/05_文件处理_backup'

backed_up = backup_files(files_to_backup, backup_directory)
print(f"\n共备份了 {backed_up} 个文件")
```

### 示例2：清理临时文件

```python
def clean_temp_files(directory, extensions=None, max_age_days=7):
    """清理指定目录下的临时文件"""
    import os
    import time
    
    current_time = time.time()
    max_age_seconds = max_age_days * 24 * 60 * 60
    deleted_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件扩展名
            if extensions and not any(file.endswith(ext) for ext in extensions):
                continue
                
            file_path = os.path.join(root, file)
            try:
                # 获取文件修改时间
                mtime = os.path.getmtime(file_path)
                # 检查文件是否超过最大保留时间
                if current_time - mtime > max_age_seconds:
                    os.remove(file_path)
                    deleted_count += 1
                    print(f"已删除过期文件: {file_path}")
            except Exception as e:
                print(f"删除文件时出错 {file_path}: {e}")
    
    return deleted_count

# 使用示例
temp_directory = 'g:/Python/模块知识储备/05_文件处理'
temp_extensions = ['.tmp', '.log', '.bak']
max_age = 30  # 30天

# 注意：此示例仅用于演示，实际运行会删除文件
# deleted = clean_temp_files(temp_directory, temp_extensions, max_age)
# print(f"\n共删除了 {deleted} 个临时文件")
```

### 示例3：创建差异备份

```python
def create_differential_backup(source_dir, target_dir):
    """创建差异备份，仅复制源目录中比目标目录中对应文件更新的文件"""
    import os
    
    # 确保目标目录存在
    os.makedirs(target_dir, exist_ok=True)
    
    copied_count = 0
    for root, dirs, files in os.walk(source_dir):
        # 计算相对路径
        rel_path = os.path.relpath(root, source_dir)
        target_root = os.path.join(target_dir, rel_path)
        
        # 创建目标目录
        os.makedirs(target_root, exist_ok=True)
        
        for file in files:
            source_file = os.path.join(root, file)
            target_file = os.path.join(target_root, file)
            
            # 检查目标文件是否存在
            if os.path.exists(target_file):
                # 比较文件修改时间
                source_mtime = os.path.getmtime(source_file)
                target_mtime = os.path.getmtime(target_file)
                
                # 只有当源文件更新时才复制
                if source_mtime > target_mtime:
                    shutil.copy2(source_file, target_file)
                    copied_count += 1
                    print(f"已更新文件: {source_file} -> {target_file}")
            else:
                # 目标文件不存在，直接复制
                shutil.copy2(source_file, target_file)
                copied_count += 1
                print(f"已复制新文件: {source_file} -> {target_file}")
    
    return copied_count

# 使用示例（注意：此示例仅用于演示，实际运行会创建备份）
# source_directory = 'g:/Python/模块知识储备/05_文件处理'
# target_directory = 'g:/Python/模块知识储备/05_文件处理_backup'
# 
# copied = create_differential_backup(source_directory, target_directory)
# print(f"\n共备份了 {copied} 个文件")
```

## 最佳实践

1. **使用shutil.copy2()代替shutil.copy()**，保留文件元数据。
2. **在删除目录前进行确认**，shutil.rmtree()会递归删除整个目录树，使用时要特别小心。
3. **使用忽略模式优化目录复制**，在复制目录时排除不需要的文件或目录。
4. **处理大文件时使用进度跟踪**，提高用户体验。
5. **在操作文件前检查路径存在性**，避免因路径不存在导致的错误。

## 与其他模块的关系

- **os模块**：shutil模块依赖于os模块，提供了更高级的文件操作功能。
- **os.path模块**：shutil模块与os.path模块配合使用，可以完成更复杂的文件路径处理任务。
- **zipfile和tarfile模块**：这些模块提供了更底层的归档和压缩功能，可以与shutil模块配合使用。

## 总结

shutil模块是Python中处理文件和目录的高级模块，提供了丰富的功能用于复制、移动、删除、归档和压缩文件等操作。熟练掌握shutil模块的使用，可以使文件操作更加高效和方便。

通过结合shutil模块与其他文件处理模块（如os、os.path、zipfile等），可以完成各种复杂的文件处理任务，如批量备份、清理临时文件、创建差异备份等。