# pathlib模块详解

pathlib模块是Python 3.4+中引入的用于路径操作的标准库，提供了面向对象的路径操作API，使路径处理更加直观和简洁。

## 模块概述

pathlib模块提供了以下主要功能：

- 面向对象的路径表示
- 跨平台的路径操作（Windows、Linux、macOS）
- 路径拼接、分割、规范化等操作
- 文件和目录的创建、删除、重命名等操作
- 文件属性和元数据访问
- 路径匹配和查找
- 文件系统遍历

## 基本用法

### 导入模块

```python
from pathlib import Path
import os
```

### 路径表示

```python
# 创建Path对象
# 当前目录
current_dir = Path(".")
print(f"当前目录: {current_dir}")
print(f"当前目录（绝对路径）: {current_dir.absolute()}")

# 家目录
home_dir = Path.home()
print(f"家目录: {home_dir}")

# 当前工作目录
cwd = Path.cwd()
print(f"当前工作目录: {cwd}")

# 路径拼接
file_path = current_dir / "subdir" / "file.txt"
print(f"拼接后的路径: {file_path}")

# 字符串路径转换为Path对象
str_path = "C:/Users/user/Documents/file.txt"
path_obj = Path(str_path)
print(f"字符串路径转换为Path对象: {path_obj}")
```

### 路径属性

```python
# 创建测试文件
os.makedirs("test_dir/subdir", exist_ok=True)
with open("test_dir/file.txt", "w") as f:
    f.write("Test file content")

# 创建Path对象
file_path = Path("test_dir/file.txt")
dir_path = Path("test_dir")

# 获取路径各部分
print(f"文件名: {file_path.name}")
print(f"文件扩展名: {file_path.suffix}")
print(f"无扩展名的文件名: {file_path.stem}")
print(f"父目录: {file_path.parent}")
print(f"父目录的父目录: {file_path.parent.parent}")
print(f"驱动名（Windows）: {file_path.drive}")
print(f"根目录: {file_path.root}")
print(f"相对路径: {file_path.relative_to(Path.cwd())}")

# 检查路径类型
print(f"{file_path} 是文件: {file_path.is_file()}")
print(f"{file_path} 是目录: {file_path.is_dir()}")
print(f"{file_path} 是符号链接: {file_path.is_symlink()}")
print(f"{file_path} 存在: {file_path.exists()}")

# 获取文件信息
if file_path.exists() and file_path.is_file():
    print(f"文件大小: {file_path.stat().st_size} bytes")
    print(f"文件修改时间: {file_path.stat().st_mtime}")
    print(f"文件权限: {file_path.stat().st_mode:o}")  # 八进制表示

# 清理测试文件和目录
import shutil
shutil.rmtree("test_dir")
```

### 文件操作

```python
# 创建文件
file_path = Path("new_file.txt")
file_path.write_text("Hello, Pathlib!")
print(f"文件已创建: {file_path}")

# 读取文件
content = file_path.read_text()
print(f"文件内容: {content}")

# 写入二进制内容
file_path.write_bytes(b"Binary content")
content = file_path.read_bytes()
print(f"二进制内容: {content}")

# 重命名文件
new_file_path = file_path.with_name("renamed_file.txt")
file_path.rename(new_file_path)
print(f"文件已重命名为: {new_file_path}")

# 替换文件扩展名
new_ext_path = new_file_path.with_suffix(".md")
new_file_path.rename(new_ext_path)
print(f"文件扩展名已更改为: {new_ext_path}")

# 删除文件
new_ext_path.unlink()
print(f"文件已删除: {new_ext_path}")
```

### 目录操作

```python
# 创建目录
new_dir = Path("new_directory")
new_dir.mkdir(exist_ok=True)
print(f"目录已创建: {new_dir}")

# 创建多级目录
new_dirs = Path("dir1/dir2/dir3")
new_dirs.mkdir(parents=True, exist_ok=True)
print(f"多级目录已创建: {new_dirs}")

# 列出目录内容
parent_dir = Path("dir1")
print(f"目录 {parent_dir} 内容:")
for item in parent_dir.iterdir():
    print(f"  {item.name} {'(目录)' if item.is_dir() else '(文件)'}")

# 遍历目录树
print(f"\n遍历目录树 {parent_dir}:")
for root, dirs, files in os.walk(parent_dir):
    level = root.replace(str(parent_dir), '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{subindent}{file}")

# 删除目录
new_dir.rmdir()
print(f"目录已删除: {new_dir}")

# 递归删除目录（pathlib不提供直接递归删除功能，使用shutil模块）
shutil.rmtree("dir1")
print(f"递归删除目录: dir1")
```

## 高级功能

### 路径匹配

```python
# 创建测试文件和目录
os.makedirs("patterns_dir/subdir", exist_ok=True)
for i in range(3):
    with open(f"patterns_dir/file{i}.txt", "w") as f:
        f.write(f"File {i}")
    with open(f"patterns_dir/file{i}.py", "w") as f:
        f.write(f"# Python file {i}")

with open("patterns_dir/subdir/another.txt", "w") as f:
    f.write("Another file")

# 创建Path对象
dir_path = Path("patterns_dir")

# 匹配当前目录下的.txt文件
print("当前目录下的.txt文件:")
for file in dir_path.glob("*.txt"):
    print(f"  {file}")

# 匹配所有子目录下的.txt文件
print("\n所有子目录下的.txt文件:")
for file in dir_path.rglob("*.txt"):
    print(f"  {file}")

# 匹配特定模式的文件
print("\n匹配file[0-1].*")
for file in dir_path.glob("file[0-1].*"):
    print(f"  {file}")

# 清理测试目录
shutil.rmtree("patterns_dir")
```

### 路径操作

```python
# 创建测试文件
os.makedirs("operations_dir/subdir", exist_ok=True)
with open("operations_dir/file.txt", "w") as f:
    f.write("Test file")

# 创建Path对象
file_path = Path("operations_dir/file.txt")
dir_path = Path("operations_dir")

# 计算相对路径
relative_path = file_path.relative_to(dir_path)
print(f"{file_path} 相对于 {dir_path} 的路径: {relative_path}")

# 规范化路径
normalized_path = Path("operations_dir/../operations_dir/file.txt").resolve()
print(f"规范化路径: {normalized_path}")

# 检查路径是否是另一个路径的子路径
is_subpath = file_path.is_relative_to(dir_path)
print(f"{file_path} 是 {dir_path} 的子路径: {is_subpath}")

# 复制文件（pathlib不提供直接复制功能，使用shutil模块）
copy_path = dir_path / "file_copy.txt"
shutil.copy2(file_path, copy_path)
print(f"文件已复制到: {copy_path}")

# 移动文件
move_path = dir_path / "subdir" / "file_moved.txt"
file_path.rename(move_path)
print(f"文件已移动到: {move_path}")

# 清理测试目录
shutil.rmtree("operations_dir")
```

### 文件属性和元数据

```python
# 创建测试文件
with open("metadata.txt", "w") as f:
    f.write("Metadata test file")

file_path = Path("metadata.txt")

# 获取文件统计信息
stat_info = file_path.stat()
print(f"文件大小: {stat_info.st_size} bytes")
print(f"文件创建时间: {stat_info.st_ctime}")
print(f"文件修改时间: {stat_info.st_mtime}")
print(f"文件访问时间: {stat_info.st_atime}")
print(f"文件权限: {stat_info.st_mode:o}")
print(f"文件所有者ID: {stat_info.st_uid}")
print(f"文件组ID: {stat_info.st_gid}")

# 获取文件类型
print(f"文件类型: {stat_info.st_mode & 0o170000:o}")

# 获取符号链接指向的目标（如果是符号链接）
# if file_path.is_symlink():
#     print(f"符号链接目标: {file_path.readlink()}")

# 清理测试文件
file_path.unlink()
```

## 实际应用示例

### 示例1：查找特定类型的文件

```python
from pathlib import Path

def find_files_by_extension(directory, extensions):
    """查找目录中特定扩展名的文件"""
    # 确保extensions是列表
    if isinstance(extensions, str):
        extensions = [extensions]
    
    # 标准化扩展名
    extensions = [ext.lower() if ext.startswith(".") else f".{ext.lower()}" for ext in extensions]
    
    found_files = []
    
    # 创建Path对象
    dir_path = Path(directory)
    
    # 遍历目录树
    for file_path in dir_path.rglob("*.*"):
        if file_path.suffix.lower() in extensions:
            found_files.append(file_path)
    
    return found_files

# 示例
# python_files = find_files_by_extension("./", [".py", ".pyw"])
# print(f"找到 {len(python_files)} 个Python文件:")
# for file in python_files[:10]:  # 只显示前10个
#     print(f"  {file}")
```

### 示例2：批量重命名文件

```python
from pathlib import Path
import os

def batch_rename_files(directory, prefix="file_", suffix=""):
    """批量重命名目录中的文件"""
    # 创建Path对象
    dir_path = Path(directory)
    
    if not dir_path.exists() or not dir_path.is_dir():
        print(f"错误: {directory} 不是有效的目录")
        return
    
    # 获取目录中的文件
    files = [f for f in dir_path.iterdir() if f.is_file()]
    
    # 排序文件
    files.sort()
    
    # 重命名文件
    for i, file in enumerate(files, 1):
        # 获取文件扩展名
        ext = file.suffix
        
        # 构建新文件名
        new_name = f"{prefix}{i:03d}{suffix}{ext}"
        new_path = file.parent / new_name
        
        # 重命名文件
        file.rename(new_path)
        print(f"重命名: {file.name} -> {new_name}")

# 示例
# batch_rename_files("./images", prefix="photo_", suffix="_2023")
```

### 示例3：统计目录大小

```python
from pathlib import Path

def get_directory_size(directory):
    """计算目录大小"""
    # 创建Path对象
    dir_path = Path(directory)
    
    if not dir_path.exists() or not dir_path.is_dir():
        return 0
    
    total_size = 0
    
    # 遍历目录树
    for file_path in dir_path.rglob("*.*"):
        if file_path.is_file():
            total_size += file_path.stat().st_size
    
    return total_size

def format_size(size_bytes):
    """格式化文件大小"""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

# 示例
# dir_size = get_directory_size("./")
# print(f"当前目录大小: {format_size(dir_size)}")
```

### 示例4：创建目录结构

```python
from pathlib import Path

def create_directory_structure(base_dir, structure):
    """创建目录结构"""
    # 创建Path对象
    base_path = Path(base_dir)
    
    for item in structure:
        if isinstance(item, str):
            # 创建目录
            dir_path = base_path / item
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"创建目录: {dir_path}")
        elif isinstance(item, dict):
            # 创建嵌套目录结构
            for dir_name, sub_structure in item.items():
                dir_path = base_path / dir_name
                dir_path.mkdir(parents=True, exist_ok=True)
                print(f"创建目录: {dir_path}")
                
                # 递归创建子目录结构
                create_directory_structure(dir_path, sub_structure)

# 示例
# structure = [
#     "data",
#     "docs",
#     {
#         "src": [
#             "modules",
#             "tests",
#             "utils"
#         ]
#     },
#     "output"
# ]

# create_directory_structure("./project", structure)
```

## 最佳实践

1. **使用Path对象代替字符串路径**：Path对象提供了丰富的方法和属性，使路径操作更加直观和安全
2. **使用/操作符拼接路径**：使用/操作符拼接路径比字符串拼接更加安全和跨平台
3. **使用with_name()和with_suffix()重命名文件**：这些方法提供了安全的文件重命名方式
4. **使用glob()和rglob()查找文件**：这些方法提供了强大的路径匹配功能
5. **使用resolve()获取绝对路径**：resolve()方法可以获取规范化的绝对路径
6. **使用is_file()和is_dir()检查路径类型**：这些方法提供了安全的路径类型检查
7. **结合shutil模块使用**：pathlib模块不提供所有文件操作功能，需要结合shutil模块使用
8. **处理异常**：在进行文件操作时，捕获并处理可能的异常，如权限错误、文件不存在等

## 与其他模块的关系

- **os**：pathlib模块提供了os模块路径操作的面向对象替代方案
- **os.path**：pathlib模块的很多功能与os.path模块相似，但提供了更加直观的API
- **shutil**：pathlib模块可以与shutil模块结合使用，提供完整的文件操作功能
- **glob**：pathlib的glob()和rglob()方法提供了glob模块的功能
- **fnmatch**：pathlib的match()方法提供了fnmatch模块的功能

## 总结

pathlib模块是Python 3.4+中引入的强大路径操作库，提供了面向对象的路径表示和丰富的文件系统操作功能。通过pathlib模块，可以编写更加清晰、简洁和跨平台的路径操作代码。

在实际应用中，pathlib模块常用于文件和目录管理、文件查找、路径匹配、文件系统遍历等场景。与传统的os.path模块相比，pathlib提供了更加直观和安全的API，是Python 3中推荐的路径操作方式。