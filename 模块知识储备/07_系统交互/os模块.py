# os模块详解

os模块是Python中用于与操作系统交互的标准库，提供了丰富的系统功能接口，包括文件系统操作、进程管理、环境变量管理等。

## 模块概述

os模块提供了以下主要功能：

- 文件和目录操作（创建、删除、重命名、遍历等）
- 进程管理（执行系统命令、获取进程信息等）
- 环境变量管理（获取、设置、删除环境变量等）
- 路径操作（路径拼接、分隔、规范化等）
- 权限管理（文件权限设置、获取等）
- 系统信息获取（CPU、内存、磁盘等）

## 基本用法

### 导入模块

```python
import os
```

### 路径操作

```python
# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 切换工作目录
os.chdir("../")
print(f"切换后的工作目录: {os.getcwd()}")

# 路径拼接
path1 = "dir1"
path2 = "file.txt"
full_path = os.path.join(path1, path2)
print(f"拼接后的路径: {full_path}")

# 分割路径
dir_name, file_name = os.path.split(full_path)
print(f"目录名: {dir_name}, 文件名: {file_name}")

# 获取文件扩展名
base_name, ext_name = os.path.splitext(file_name)
print(f"基名: {base_name}, 扩展名: {ext_name}")

# 获取绝对路径
abs_path = os.path.abspath("file.txt")
print(f"绝对路径: {abs_path}")

# 规范化路径
norm_path = os.path.normpath("dir1/../dir2/file.txt")
print(f"规范化路径: {norm_path}")

# 获取父目录
parent_dir = os.path.dirname(full_path)
print(f"父目录: {parent_dir}")

# 获取文件名
file_name = os.path.basename(full_path)
print(f"文件名: {file_name}")
```

### 文件操作

```python
# 创建文件
with open("test.txt", "w") as f:
    f.write("Hello, World!")

# 文件重命名
os.rename("test.txt", "new_test.txt")

# 删除文件
os.remove("new_test.txt")

# 检查文件是否存在
if os.path.exists("new_test.txt"):
    print("文件存在")
else:
    print("文件不存在")

# 检查是否为文件
print(f"是否为文件: {os.path.isfile("file.txt")}")

# 检查是否为目录
print(f"是否为目录: {os.path.isdir("dir1")}")

# 获取文件大小
if os.path.isfile("file.txt"):
    print(f"文件大小: {os.path.getsize("file.txt")} bytes")

# 获取文件修改时间
if os.path.isfile("file.txt"):
    mtime = os.path.getmtime("file.txt")
    print(f"文件修改时间: {mtime}")
    print(f"文件修改时间(格式化): {os.path.getmtime("file.txt")}")

# 获取文件创建时间
if os.path.isfile("file.txt"):
    ctime = os.path.getctime("file.txt")
    print(f"文件创建时间: {ctime}")
```

### 目录操作

```python
# 创建目录
os.mkdir("new_dir")

# 创建多级目录
os.makedirs("dir1/dir2/dir3", exist_ok=True)

# 列出目录内容
print(f"目录内容: {os.listdir("dir1")}")

# 删除空目录
os.rmdir("new_dir")

# 删除非空目录
os.removedirs("dir1/dir2/dir3")  # 只删除空目录链

# 遍历目录树
for root, dirs, files in os.walk("."):
    print(f"\n根目录: {root}")
    print(f"子目录: {dirs}")
    print(f"文件: {files}")
```

### 环境变量管理

```python
# 获取所有环境变量
env_vars = os.environ
print(f"环境变量数量: {len(env_vars)}")

# 获取特定环境变量
path_var = os.environ.get("PATH")
print(f"PATH环境变量: {path_var[:100]}...")  # 只显示前100个字符

# 设置环境变量
os.environ["MY_VAR"] = "my_value"
print(f"MY_VAR环境变量: {os.environ.get("MY_VAR")}")

# 删除环境变量
if "MY_VAR" in os.environ:
    del os.environ["MY_VAR"]
    print(f"MY_VAR环境变量是否存在: {'MY_VAR' in os.environ}")

# 获取系统路径分隔符
print(f"路径分隔符: {os.pathsep}")

# 获取目录分隔符
print(f"目录分隔符: {os.sep}")
```

### 进程管理

```python
# 执行系统命令
result = os.system("dir")  # Windows
# result = os.system("ls -la")  # Linux/Mac
print(f"命令执行结果: {result}")

# 获取环境变量
print(f"HOME环境变量: {os.environ.get("HOME")}")

# 获取当前进程ID
pid = os.getpid()
print(f"当前进程ID: {pid}")

# 获取父进程ID
ppid = os.getppid()
print(f"父进程ID: {ppid}")

# 终止进程
# os.kill(pid, signal.SIGTERM)  # 需要导入signal模块
```

### 文件权限管理

```python
# 获取文件权限（Windows上可能无法正常工作）
if os.path.isfile("file.txt"):
    try:
        mode = os.stat("file.txt").st_mode
        print(f"文件权限模式: {mode:o}")  # 八进制表示
    except Exception as e:
        print(f"获取文件权限失败: {e}")

# 设置文件权限（Windows上可能无法正常工作）
try:
    os.chmod("file.txt", 0o755)  # 设置为rwxr-xr-x
    print("文件权限设置成功")
except Exception as e:
    print(f"设置文件权限失败: {e}")
```

### 系统信息获取

```python
# 获取系统信息
print(f"操作系统名称: {os.name}")  # nt表示Windows, posix表示Linux/Mac

# 获取环境变量
print(f"TEMP环境变量: {os.environ.get("TEMP")}")
print(f"TMP环境变量: {os.environ.get("TMP")}")

# 获取换行符
print(f"换行符: {repr(os.linesep)}")  # \r\n表示Windows, \n表示Linux/Mac

# 获取CPU数量
print(f"CPU数量: {os.cpu_count()}")
```

## 高级功能

### 符号链接

```python
# 创建符号链接（Windows上需要管理员权限）
try:
    os.symlink("file.txt", "link.txt")
    print("符号链接创建成功")
    
    # 检查是否为符号链接
    print(f"是否为符号链接: {os.path.islink("link.txt")}")
    
    # 获取符号链接指向的目标
    if os.path.islink("link.txt"):
        print(f"符号链接目标: {os.readlink("link.txt")}")
        
    # 删除符号链接
    os.unlink("link.txt")
    print("符号链接删除成功")
except Exception as e:
    print(f"符号链接操作失败: {e}")
```

### 临时文件和目录

```python
# 创建临时文件
import tempfile

temp_file = tempfile.NamedTemporaryFile(delete=False)
temp_file_name = temp_file.name
print(f"临时文件路径: {temp_file_name}")
temp_file.close()

# 创建临时目录
temp_dir = tempfile.mkdtemp()
print(f"临时目录路径: {temp_dir}")

# 清理临时文件和目录
os.unlink(temp_file_name)
os.rmdir(temp_dir)
print("临时文件和目录清理成功")
```

### 磁盘空间信息

```python
# 获取磁盘空间信息（需要使用shutil模块）
import shutil

# 获取磁盘使用情况
total, used, free = shutil.disk_usage(".")

print(f"总磁盘空间: {total // (2**30)} GB")
print(f"已使用磁盘空间: {used // (2**30)} GB")
print(f"可用磁盘空间: {free // (2**30)} GB")
```

### 内存信息

```python
# 获取内存信息（Windows上可以使用psutil模块）
try:
    import psutil
    
    # 获取内存使用情况
    memory = psutil.virtual_memory()
    print(f"总内存: {memory.total // (2**30)} GB")
    print(f"可用内存: {memory.available // (2**30)} GB")
    print(f"已使用内存: {memory.used // (2**30)} GB")
    print(f"内存使用率: {memory.percent}%")
except ImportError:
    print("psutil模块未安装，无法获取内存信息")
```

## 实际应用示例

### 示例1：批量重命名文件

```python
import os

def batch_rename_files(directory, prefix="file_", suffix=""):
    """批量重命名目录中的文件"""
    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在")
        return
    
    # 遍历目录中的文件
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # 排序文件
    files.sort()
    
    # 重命名文件
    for i, file_name in enumerate(files):
        # 获取文件扩展名
        _, ext = os.path.splitext(file_name)
        
        # 构建新文件名
        new_name = f"{prefix}{i+1:03d}{suffix}{ext}"
        
        # 构建旧路径和新路径
        old_path = os.path.join(directory, file_name)
        new_path = os.path.join(directory, new_name)
        
        # 重命名文件
        os.rename(old_path, new_path)
        print(f"重命名: {file_name} -> {new_name}")

# 示例
# batch_rename_files("./images", prefix="photo_", suffix="_2023")
```

### 示例2：查找特定扩展名的文件

```python
import os

def find_files_by_extension(directory, extensions):
    """查找目录中特定扩展名的文件"""
    # 确保extensions是列表
    if isinstance(extensions, str):
        extensions = [extensions]
    
    # 标准化扩展名
    extensions = [ext.lower() if ext.startswith(".") else f".{ext.lower()}" for ext in extensions]
    
    found_files = []
    
    # 遍历目录树
    for root, _, files in os.walk(directory):
        for file_name in files:
            # 检查文件扩展名
            if os.path.splitext(file_name)[1].lower() in extensions:
                # 添加到结果列表
                found_files.append(os.path.join(root, file_name))
    
    return found_files

# 示例
# python_files = find_files_by_extension("./", [".py", ".pyw"])
# print(f"找到 {len(python_files)} 个Python文件:")
# for file in python_files[:10]:  # 只显示前10个
#     print(f"  {file}")
```

### 示例3：计算目录大小

```python
import os

def calculate_directory_size(directory):
    """计算目录大小"""
    total_size = 0
    
    # 遍历目录树
    for root, _, files in os.walk(directory):
        for file in files:
            # 构建文件路径
            file_path = os.path.join(root, file)
            
            # 累加文件大小
            try:
                total_size += os.path.getsize(file_path)
            except OSError:
                # 跳过无法访问的文件
                continue
    
    return total_size

def format_size(size_bytes):
    """格式化文件大小"""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"

# 示例
dir_size = calculate_directory_size("./")
print(f"当前目录大小: {format_size(dir_size)}")
```

### 示例4：创建目录结构

```python
import os

def create_directory_structure(base_dir, structure):
    """创建目录结构"""
    for item in structure:
        if isinstance(item, str):
            # 创建目录
            dir_path = os.path.join(base_dir, item)
            os.makedirs(dir_path, exist_ok=True)
            print(f"创建目录: {dir_path}")
        elif isinstance(item, dict):
            # 创建嵌套目录结构
            for dir_name, sub_structure in item.items():
                dir_path = os.path.join(base_dir, dir_name)
                os.makedirs(dir_path, exist_ok=True)
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

1. **使用os.path模块进行路径操作**：os.path模块提供了跨平台的路径操作函数，避免了手动拼接路径的问题
2. **使用os.makedirs创建多级目录**：os.makedirs可以创建多级目录，并支持exist_ok参数避免目录已存在的错误
3. **使用os.walk遍历目录树**：os.walk提供了一种简单的方式遍历目录树中的所有文件和子目录
4. **处理文件权限时考虑平台差异**：不同平台的文件权限机制不同，需要注意兼容性
5. **使用环境变量时考虑默认值**：使用os.environ.get()获取环境变量时，可以提供默认值
6. **避免硬编码路径分隔符**：使用os.sep或os.path.join避免硬编码路径分隔符
7. **清理临时文件**：使用tempfile模块创建临时文件时，确保在使用后清理
8. **处理异常**：在执行文件操作时，捕获并处理可能的异常

## 与其他模块的关系

- **os.path**：os模块的子模块，提供路径操作功能
- **shutil**：提供高级文件操作功能，如文件复制、移动、归档等
- **tempfile**：提供临时文件和目录的创建和管理功能
- **subprocess**：提供执行系统命令和管理子进程的功能
- **pathlib**：Python 3.4+ 提供的路径操作库，提供面向对象的路径操作API

## 总结

os模块是Python中用于与操作系统交互的核心模块，提供了丰富的文件和目录操作、进程管理、环境变量管理等功能。通过os模块，可以编写跨平台的Python程序，与操作系统进行交互。

在实际应用中，os模块常用于文件和目录管理、系统命令执行、环境变量配置等场景。对于更高级的文件操作，可以结合shutil、tempfile等模块使用。