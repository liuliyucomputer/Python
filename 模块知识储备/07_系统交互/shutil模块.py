# shutil模块详解

shutil模块是Python中用于高级文件操作的标准库，提供了文件复制、移动、删除、归档等功能，扩展了os模块的文件操作能力。

## 模块概述

shutil模块提供了以下主要功能：

- 文件和目录的复制、移动
- 目录的创建和删除
- 文件和目录的权限管理
- 文件归档和压缩（如ZIP、TAR等）
- 磁盘使用情况查询
- 高级文件操作（如复制权限、复制元数据等）

## 基本用法

### 导入模块

```python
import shutil
import os
```

### 文件操作

```python
# 复制文件
source = "source.txt"
destination = "destination.txt"

# 创建源文件
with open(source, "w") as f:
    f.write("Hello, World!")

# 复制文件
shutil.copy(source, destination)
print(f"文件已从 {source} 复制到 {destination}")

# 复制文件并保留元数据（权限、修改时间等）
shutil.copy2(source, destination + ".copy2")
print(f"文件已从 {source} 复制到 {destination}.copy2，并保留元数据")

# 复制文件内容和权限（不包括其他元数据）
shutil.copyfile(source, destination + ".copyfile")
print(f"文件内容已从 {source} 复制到 {destination}.copyfile")

# 移动文件（相当于重命名）
new_destination = "new_destination.txt"
shutil.move(destination, new_destination)
print(f"文件已从 {destination} 移动到 {new_destination}")

# 删除文件（shutil不提供直接删除文件的功能，使用os模块）
os.remove(source)
os.remove(new_destination)
os.remove(destination + ".copy2")
os.remove(destination + ".copyfile")
print("所有文件已删除")
```

### 目录操作

```python
# 创建测试目录和文件
os.makedirs("source_dir/subdir", exist_ok=True)
with open("source_dir/file1.txt", "w") as f:
    f.write("File 1")
with open("source_dir/subdir/file2.txt", "w") as f:
    f.write("File 2")

# 复制目录（包括所有内容）
shutil.copytree("source_dir", "destination_dir")
print("目录已复制")

# 移动目录
shutil.move("destination_dir", "new_destination_dir")
print("目录已移动")

# 删除目录（包括所有内容）
shutil.rmtree("source_dir")
shutil.rmtree("new_destination_dir")
print("目录已删除")
```

### 权限管理

```python
# 创建测试文件
with open("test.txt", "w") as f:
    f.write("Test file")

# 获取文件权限
stat_info = os.stat("test.txt")
print(f"文件权限: {stat_info.st_mode:o}")  # 八进制表示

# 复制文件权限
shutil.copymode("test.txt", "test_copy.txt")
stat_info_copy = os.stat("test_copy.txt")
print(f"复制后的文件权限: {stat_info_copy.st_mode:o}")

# 复制文件元数据
shutil.copystat("test.txt", "test_copy.txt")
stat_info_copy = os.stat("test_copy.txt")
print(f"复制元数据后的文件权限: {stat_info_copy.st_mode:o}")
print(f"复制元数据后的文件修改时间: {stat_info_copy.st_mtime}")

# 清理文件
os.remove("test.txt")
os.remove("test_copy.txt")
```

### 磁盘使用情况

```python
# 获取磁盘使用情况
total, used, free = shutil.disk_usage(".")

print(f"总磁盘空间: {total / (2**30):.2f} GB")
print(f"已使用磁盘空间: {used / (2**30):.2f} GB")
print(f"可用磁盘空间: {free / (2**30):.2f} GB")
print(f"磁盘使用率: {used / total * 100:.2f}%")
```

### 文件归档和压缩

```python
# 创建测试目录和文件
os.makedirs("archive_dir/subdir", exist_ok=True)
with open("archive_dir/file1.txt", "w") as f:
    f.write("File 1")
with open("archive_dir/subdir/file2.txt", "w") as f:
    f.write("File 2")

# 创建ZIP归档
shutil.make_archive("archive", "zip", "archive_dir")
print("ZIP归档已创建")

# 创建TAR归档
shutil.make_archive("archive", "tar", "archive_dir")
print("TAR归档已创建")

# 创建TAR.GZ归档
shutil.make_archive("archive", "gztar", "archive_dir")
print("TAR.GZ归档已创建")

# 提取归档
shutil.unpack_archive("archive.zip", "extracted_dir")
print("ZIP归档已提取")

# 清理文件和目录
shutil.rmtree("archive_dir")
shutil.rmtree("extracted_dir")
os.remove("archive.zip")
os.remove("archive.tar")
os.remove("archive.tar.gz")
print("所有测试文件已清理")
```

## 高级功能

### 忽略文件和目录

```python
# 创建测试目录和文件
os.makedirs("ignore_dir/subdir", exist_ok=True)
with open("ignore_dir/file1.txt", "w") as f:
    f.write("File 1")
with open("ignore_dir/file2.pyc", "w") as f:
    f.write("Compiled Python file")
with open("ignore_dir/subdir/file3.txt", "w") as f:
    f.write("File 3")
with open("ignore_dir/subdir/.gitignore", "w") as f:
    f.write(".pyc
__pycache__/")

# 定义忽略模式
def ignore_pyc_files(directory, files):
    return [f for f in files if f.endswith(".pyc") or f == "__pycache__"]

# 复制目录并忽略特定文件
shutil.copytree("ignore_dir", "ignore_dir_copy", ignore=ignore_pyc_files)
print("目录已复制，忽略了.pyc文件")

# 查看复制后的目录内容
for root, dirs, files in os.walk("ignore_dir_copy"):
    print(f"\n目录: {root}")
    for file in files:
        print(f"  文件: {file}")

# 清理目录
shutil.rmtree("ignore_dir")
shutil.rmtree("ignore_dir_copy")
```

### 高级归档操作

```python
# 创建ZIP归档并添加更多元数据
import zipfile

# 创建归档文件
with zipfile.ZipFile("custom_archive.zip", "w", zipfile.ZIP_DEFLATED) as zf:
    # 添加文件
    zf.write("source.txt")
    
    # 添加文件并指定归档中的名称
    zf.write("source.txt", "archived_file.txt")
    
    # 从字符串添加文件
    zf.writestr("string_file.txt", "Content from string")
    
    # 添加目录
    zf.write("subdir", "archived_subdir")

print("自定义ZIP归档已创建")

# 查看归档内容
with zipfile.ZipFile("custom_archive.zip", "r") as zf:
    print("归档内容:")
    for name in zf.namelist():
        print(f"  {name}")

# 清理归档文件
os.remove("custom_archive.zip")
```

### 复制文件树

```python
# 创建测试目录结构
os.makedirs("tree_dir/subdir1/subsubdir", exist_ok=True)
os.makedirs("tree_dir/subdir2", exist_ok=True)
with open("tree_dir/file1.txt", "w") as f:
    f.write("File 1")
with open("tree_dir/subdir1/file2.txt", "w") as f:
    f.write("File 2")
with open("tree_dir/subdir1/subsubdir/file3.txt", "w") as f:
    f.write("File 3")
with open("tree_dir/subdir2/file4.txt", "w") as f:
    f.write("File 4")

# 复制整个目录树
shutil.copytree("tree_dir", "tree_dir_copy")
print("目录树已复制")

# 移动整个目录树
shutil.move("tree_dir_copy", "tree_dir_moved")
print("目录树已移动")

# 清理目录
shutil.rmtree("tree_dir")
shutil.rmtree("tree_dir_moved")
```

## 实际应用示例

### 示例1：批量复制文件

```python
import shutil
import os

def batch_copy_files(source_dir, destination_dir, extensions=None):
    """批量复制目录中特定扩展名的文件"""
    # 创建目标目录
    os.makedirs(destination_dir, exist_ok=True)
    
    # 遍历源目录
    copied_files = 0
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # 检查文件扩展名
            if extensions is None or os.path.splitext(file)[1].lower() in extensions:
                # 构建源文件路径
                source_file = os.path.join(root, file)
                
                # 构建目标文件路径（保持相同的目录结构）
                relative_path = os.path.relpath(root, source_dir)
                destination_file = os.path.join(destination_dir, relative_path, file)
                
                # 创建目标目录
                os.makedirs(os.path.dirname(destination_file), exist_ok=True)
                
                # 复制文件
                shutil.copy2(source_file, destination_file)
                copied_files += 1
                print(f"已复制: {source_file} -> {destination_file}")
    
    return copied_files

# 示例
# source_dir = "./source"
# destination_dir = "./destination"
# extensions = [".py", ".txt"]  # 复制Python和文本文件
# 
# copied = batch_copy_files(source_dir, destination_dir, extensions)
# print(f"\n共复制了 {copied} 个文件")
```

### 示例2：备份目录

```python
import shutil
import os
import datetime

def backup_directory(source_dir, backup_dir=None):
    """备份目录到ZIP归档"""
    # 如果没有指定备份目录，使用源目录的父目录
    if backup_dir is None:
        backup_dir = os.path.dirname(source_dir)
    
    # 创建备份目录
    os.makedirs(backup_dir, exist_ok=True)
    
    # 构建备份文件名（包含时间戳）
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{os.path.basename(source_dir)}_{timestamp}"
    backup_path = os.path.join(backup_dir, backup_name)
    
    # 创建备份归档
    backup_archive = shutil.make_archive(backup_path, "zip", source_dir)
    
    print(f"目录已备份到: {backup_archive}")
    return backup_archive

# 示例
# source_dir = "./my_project"
# backup_dir = "./backups"
# 
# backup_file = backup_directory(source_dir, backup_dir)
```

### 示例3：清理临时文件

```python
import shutil
import os
import tempfile

def cleanup_temp_files(temp_dir=None, older_than_days=7):
    """清理临时文件"""
    if temp_dir is None:
        temp_dir = tempfile.gettempdir()
    
    if not os.path.exists(temp_dir):
        print(f"临时目录 {temp_dir} 不存在")
        return
    
    # 计算时间阈值
    threshold = datetime.datetime.now() - datetime.timedelta(days=older_than_days)
    
    files_deleted = 0
    dirs_deleted = 0
    
    # 遍历临时目录
    for root, dirs, files in os.walk(temp_dir, topdown=False):  # 从下往上遍历
        # 删除旧文件
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # 获取文件修改时间
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                
                # 如果文件超过阈值，删除
                if mtime < threshold:
                    os.remove(file_path)
                    files_deleted += 1
                    print(f"已删除旧文件: {file_path}")
            except Exception as e:
                print(f"删除文件 {file_path} 失败: {e}")
        
        # 删除空目录
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                # 尝试删除目录（只有空目录才能被删除）
                os.rmdir(dir_path)
                dirs_deleted += 1
                print(f"已删除空目录: {dir_path}")
            except OSError:
                # 目录不为空，跳过
                pass
            except Exception as e:
                print(f"删除目录 {dir_path} 失败: {e}")
    
    print(f"\n清理完成: 删除了 {files_deleted} 个文件和 {dirs_deleted} 个目录")
    return files_deleted, dirs_deleted

# 示例
# cleanup_temp_files(older_than_days=1)
```

### 示例4：同步目录

```python
import shutil
import os

def sync_directories(source_dir, destination_dir):
    """同步源目录到目标目录"""
    # 确保目标目录存在
    os.makedirs(destination_dir, exist_ok=True)
    
    # 获取源目录和目标目录的文件列表
    source_files = set()
    for root, _, files in os.walk(source_dir):
        for file in files:
            relative_path = os.path.relpath(root, source_dir)
            source_files.add(os.path.join(relative_path, file))
    
    destination_files = set()
    for root, _, files in os.walk(destination_dir):
        for file in files:
            relative_path = os.path.relpath(root, destination_dir)
            destination_files.add(os.path.join(relative_path, file))
    
    # 复制新增或修改的文件
    copied_files = 0
    for file in source_files:
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(destination_dir, file)
        
        # 如果目标文件不存在或源文件更新
        if not os.path.exists(destination_path) or \
           os.path.getmtime(source_path) > os.path.getmtime(destination_path):
            
            # 创建目标目录
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            
            # 复制文件
            shutil.copy2(source_path, destination_path)
            copied_files += 1
            print(f"已复制: {file}")
    
    # 删除目标目录中源目录不存在的文件
    deleted_files = 0
    for file in destination_files - source_files:
        destination_path = os.path.join(destination_dir, file)
        os.remove(destination_path)
        deleted_files += 1
        print(f"已删除: {file}")
    
    print(f"\n同步完成: 复制了 {copied_files} 个文件，删除了 {deleted_files} 个文件")
    return copied_files, deleted_files

# 示例
# source_dir = "./source"
# destination_dir = "./destination"
# 
# sync_directories(source_dir, destination_dir)
```

## 最佳实践

1. **使用shutil.copy2保留文件元数据**：对于重要文件，使用shutil.copy2可以保留文件的权限、修改时间等元数据
2. **使用shutil.copytree复制目录**：shutil.copytree可以递归复制整个目录结构
3. **使用ignore参数忽略特定文件**：在复制目录时，可以使用ignore参数忽略不需要复制的文件或目录
4. **使用shutil.disk_usage监控磁盘空间**：在进行大量文件操作前，可以检查磁盘空间是否充足
5. **使用shutil.make_archive创建归档**：shutil.make_archive提供了简单的方式创建各种格式的归档文件
6. **处理异常**：在进行文件操作时，捕获并处理可能的异常，如权限错误、磁盘空间不足等
7. **使用绝对路径**：使用绝对路径可以避免相对路径带来的问题
8. **清理临时文件**：在使用临时文件后，确保及时清理，避免占用磁盘空间

## 与其他模块的关系

- **os**：shutil模块依赖于os模块，提供了更高级的文件操作功能
- **zipfile**：提供了更详细的ZIP归档操作功能
- **tarfile**：提供了TAR归档操作功能
- **tempfile**：提供了临时文件和目录的创建功能
- **pathlib**：Python 3.4+ 提供的路径操作库，可以与shutil模块结合使用

## 总结

shutil模块是Python中用于高级文件操作的核心模块，提供了文件复制、移动、删除、归档等功能。通过shutil模块，可以方便地进行各种文件和目录操作，扩展了os模块的功能。

在实际应用中，shutil模块常用于文件备份、目录同步、文件归档、临时文件清理等场景。与os模块结合使用，可以完成几乎所有的文件系统操作任务。