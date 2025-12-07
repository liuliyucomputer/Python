# stat模块详解

stat模块是Python标准库中的一个模块，用于提供文件状态信息的常量和函数。它主要用于解释os模块返回的文件状态信息，提供了更加友好和跨平台的文件属性访问方式。

## 模块概述

stat模块提供了以下主要功能：

- 定义文件状态信息的常量（如文件类型、权限等）
- 提供解析文件状态信息的函数
- 支持跨平台的文件属性访问
- 与os模块配合使用，解释os.stat()等函数返回的文件状态信息

## 基本用法

### 导入模块

```python
import os
import stat
import time
```

### 文件状态信息

```python
# 创建测试文件
with open("stat_test.txt", "w") as f:
    f.write("Test file for stat module")

# 获取文件状态信息
file_stat = os.stat("stat_test.txt")

# 打印文件状态信息
print("文件状态信息:")
print(f"  文件大小: {file_stat.st_size} bytes")
print(f"  硬链接数: {file_stat.st_nlink}")
print(f"  用户ID: {file_stat.st_uid}")
print(f"  组ID: {file_stat.st_gid}")
print(f"  设备ID: {file_stat.st_dev}")
print(f"  索引节点号: {file_stat.st_ino}")
print(f"  文件权限: {file_stat.st_mode}")
print(f"  最后访问时间: {file_stat.st_atime}")
print(f"  最后修改时间: {file_stat.st_mtime}")
print(f"  最后状态改变时间: {file_stat.st_ctime}")
print(f"  块大小: {file_stat.st_blksize}")
print(f"  占用块数: {file_stat.st_blocks}")

# 清理测试文件
os.unlink("stat_test.txt")
```

## 文件类型常量

```python
# 创建不同类型的文件和目录用于测试
os.makedirs("stat_dir", exist_ok=True)
with open("stat_regular.txt", "w") as f:
    f.write("Regular file")

# 获取文件状态信息
regular_stat = os.stat("stat_regular.txt")
dir_stat = os.stat("stat_dir")

# 文件类型检查
print("文件类型检查:")

# 常规文件
if stat.S_ISREG(regular_stat.st_mode):
    print("  stat_regular.txt 是常规文件")

# 目录
if stat.S_ISDIR(dir_stat.st_mode):
    print("  stat_dir 是目录")

# 符号链接
# if stat.S_ISLNK(link_stat.st_mode):
#     print("  stat_link 是符号链接")

# 块设备
# if stat.S_ISBLK(block_stat.st_mode):
#     print("  stat_block 是块设备")

# 字符设备
# if stat.S_ISCHR(char_stat.st_mode):
#     print("  stat_char 是字符设备")

# FIFO管道
# if stat.S_ISFIFO(fifo_stat.st_mode):
#     print("  stat_fifo 是FIFO管道")

# 套接字
# if stat.S_ISSOCK(sock_stat.st_mode):
#     print("  stat_socket 是套接字")

# 清理测试文件和目录
os.unlink("stat_regular.txt")
os.rmdir("stat_dir")
```

## 文件权限常量

```python
# 创建测试文件
with open("stat_perm.txt", "w") as f:
    f.write("Permission test file")

# 设置文件权限
os.chmod("stat_perm.txt", 0o644)  # rw-r--r--

# 获取文件状态信息
file_stat = os.stat("stat_perm.txt")

# 权限检查
print("文件权限检查:")

# 用户权限
user_read = bool(file_stat.st_mode & stat.S_IRUSR)
user_write = bool(file_stat.st_mode & stat.S_IWUSR)
user_exec = bool(file_stat.st_mode & stat.S_IXUSR)
print(f"  用户权限: 读={user_read}, 写={user_write}, 执行={user_exec}")

# 组权限
group_read = bool(file_stat.st_mode & stat.S_IRGRP)
group_write = bool(file_stat.st_mode & stat.S_IWGRP)
group_exec = bool(file_stat.st_mode & stat.S_IXGRP)
print(f"  组权限: 读={group_read}, 写={group_write}, 执行={group_exec}")

# 其他用户权限
other_read = bool(file_stat.st_mode & stat.S_IROTH)
other_write = bool(file_stat.st_mode & stat.S_IWOTH)
other_exec = bool(file_stat.st_mode & stat.S_IXOTH)
print(f"  其他用户权限: 读={other_read}, 写={other_write}, 执行={other_exec}")

# 特殊权限
setuid = bool(file_stat.st_mode & stat.S_ISUID)
setgid = bool(file_stat.st_mode & stat.S_ISGID)
sticky = bool(file_stat.st_mode & stat.S_ISVTX)
print(f"  特殊权限: setuid={setuid}, setgid={setgid}, sticky={sticky}")

# 清理测试文件
os.unlink("stat_perm.txt")
```

## 解析文件模式

```python
# 创建测试文件并设置不同权限
with open("stat_mode.txt", "w") as f:
    f.write("Mode test file")

# 设置不同权限
permissions = [
    (0o755, "rwxr-xr-x (用户可读可写可执行, 组和其他用户可读可执行)"),
    (0o644, "rw-r--r-- (用户可读可写, 组和其他用户可读)"),
    (0o400, "r-------- (只有用户可读)")
]

for perm, desc in permissions:
    os.chmod("stat_mode.txt", perm)
    file_stat = os.stat("stat_mode.txt")
    
    # 使用stat模块解析文件模式
    file_type = stat.S_IFMT(file_stat.st_mode)
    file_perm = stat.S_IMODE(file_stat.st_mode)
    
    print(f"\n权限: {oct(perm)} ({desc})")
    print(f"  文件类型: {oct(file_type)}")
    print(f"  文件权限: {oct(file_perm)}")
    print(f"  用户可执行: {bool(file_perm & stat.S_IXUSR)}")
    print(f"  组可读: {bool(file_perm & stat.S_IRGRP)}")

# 清理测试文件
os.unlink("stat_mode.txt")
```

## 时间转换

```python
# 创建测试文件
with open("stat_time.txt", "w") as f:
    f.write("Time test file")

# 获取文件状态信息
file_stat = os.stat("stat_time.txt")

# 转换时间戳为可读格式
print("文件时间信息:")
print(f"  最后访问时间: {file_stat.st_atime} -> {time.ctime(file_stat.st_atime)}")
print(f"  最后修改时间: {file_stat.st_mtime} -> {time.ctime(file_stat.st_mtime)}")
print(f"  最后状态改变时间: {file_stat.st_ctime} -> {time.ctime(file_stat.st_ctime)}")

# 使用localtime转换为本地时间
print(f"  最后修改时间(本地时间): {time.localtime(file_stat.st_mtime)}")

# 使用gmtime转换为UTC时间
print(f"  最后修改时间(UTC时间): {time.gmtime(file_stat.st_mtime)}")

# 清理测试文件
os.unlink("stat_time.txt")
```

## 高级功能

### 检查文件是否可执行

```python
# 创建测试文件
with open("stat_executable.txt", "w") as f:
    f.write("#!/usr/bin/env python3\nprint('Hello from executable file')")

# 检查文件是否可执行（初始状态）
file_stat = os.stat("stat_executable.txt")
is_executable = bool(file_stat.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
print(f"文件初始状态是否可执行: {is_executable}")

# 设置文件可执行权限
os.chmod("stat_executable.txt", 0o755)

# 再次检查文件是否可执行
file_stat = os.stat("stat_executable.txt")
is_executable = bool(file_stat.st_mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
print(f"文件设置可执行权限后是否可执行: {is_executable}")

# 清理测试文件
os.unlink("stat_executable.txt")
```

### 递归检查目录权限

```python
# 创建测试目录结构
os.makedirs("stat_test_dir/subdir1/subdir2", exist_ok=True)
with open("stat_test_dir/file1.txt", "w") as f:
    f.write("File 1")
with open("stat_test_dir/subdir1/file2.txt", "w") as f:
    f.write("File 2")

# 设置不同的权限
os.chmod("stat_test_dir", 0o755)  # rwxr-xr-x
os.chmod("stat_test_dir/subdir1", 0o700)  # rwx------
os.chmod("stat_test_dir/subdir1/subdir2", 0o555)  # r-xr-xr-x

# 递归检查目录权限
def check_directory_permissions(directory):
    """递归检查目录权限"""
    for root, dirs, files in os.walk(directory):
        root_stat = os.stat(root)
        root_perm = stat.S_IMODE(root_stat.st_mode)
        
        print(f"\n目录: {root}")
        print(f"  权限: {oct(root_perm)}")
        print(f"  用户可写: {bool(root_perm & stat.S_IWUSR)}")
        print(f"  组可读: {bool(root_perm & stat.S_IRGRP)}")
        print(f"  其他可执行: {bool(root_perm & stat.S_IXOTH)}")
        
        for file in files:
            file_path = os.path.join(root, file)
            file_stat = os.stat(file_path)
            file_perm = stat.S_IMODE(file_stat.st_mode)
            print(f"  文件: {file} -> 权限: {oct(file_perm)}")

# 执行权限检查
check_directory_permissions("stat_test_dir")

# 清理测试目录
import shutil
shutil.rmtree("stat_test_dir")
```

### 文件权限比较

```python
# 创建测试文件
with open("stat_compare.txt", "w") as f:
    f.write("Permission comparison test")

# 设置不同权限
os.chmod("stat_compare.txt", 0o644)  # rw-r--r--

# 获取文件权限
file_stat = os.stat("stat_compare.txt")
file_perm = stat.S_IMODE(file_stat.st_mode)

# 比较权限
print("文件权限比较:")

# 检查是否等于特定权限
equals_644 = file_perm == 0o644
print(f"  权限等于 0o644: {equals_644}")

# 检查是否包含特定权限
has_read_perm = bool(file_perm & (stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH))
has_write_perm = bool(file_perm & (stat.S_IWUSR | stat.S_IWGRP | stat.S_IWOTH))
has_exec_perm = bool(file_perm & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
print(f"  包含读权限: {has_read_perm}")
print(f"  包含写权限: {has_write_perm}")
print(f"  包含执行权限: {has_exec_perm}")

# 检查用户是否有读写权限
user_rw = bool(file_perm & (stat.S_IRUSR | stat.S_IWUSR))
print(f"  用户有读写权限: {user_rw}")

# 清理测试文件
os.unlink("stat_compare.txt")
```

## 实际应用示例

### 示例1：批量修改文件权限

```python
import os
import stat

def batch_change_permissions(directory, file_perm=None, dir_perm=None):
    """批量修改目录中文件和目录的权限"""
    for root, dirs, files in os.walk(directory):
        # 修改目录权限
        if dir_perm is not None:
            root_stat = os.stat(root)
            root_type = stat.S_IFMT(root_stat.st_mode)
            if root_type == stat.S_IFDIR:
                os.chmod(root, dir_perm)
                print(f"修改目录权限: {root} -> {oct(dir_perm)}")
        
        # 修改文件权限
        if file_perm is not None:
            for file in files:
                file_path = os.path.join(root, file)
                file_stat = os.stat(file_path)
                file_type = stat.S_IFMT(file_stat.st_mode)
                if file_type == stat.S_IFREG:
                    os.chmod(file_path, file_perm)
                    print(f"修改文件权限: {file_path} -> {oct(file_perm)}")

# 示例
# batch_change_permissions("./my_dir", file_perm=0o644, dir_perm=0o755)
```

### 示例2：查找最近修改的文件

```python
import os
import stat
import time

def find_recently_modified_files(directory, hours=24):
    """查找指定目录中最近指定小时数内修改的文件"""
    # 计算时间阈值
    current_time = time.time()
    time_threshold = current_time - (hours * 3600)
    
    recently_modified = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_stat = os.stat(file_path)
                file_type = stat.S_IFMT(file_stat.st_mode)
                
                # 只检查常规文件
                if file_type == stat.S_IFREG:
                    # 检查修改时间
                    if file_stat.st_mtime >= time_threshold:
                        recently_modified.append((file_path, file_stat.st_mtime))
            except (OSError, PermissionError):
                # 忽略无法访问的文件
                continue
    
    # 按修改时间排序（最新的在前）
    recently_modified.sort(key=lambda x: x[1], reverse=True)
    
    return recently_modified

# 示例
# recent_files = find_recently_modified_files("./my_dir", hours=12)
# print(f"最近12小时内修改的文件 ({len(recent_files)} 个):")
# for file_path, mod_time in recent_files[:10]:  # 只显示前10个
#     print(f"  {file_path} -> {time.ctime(mod_time)}")
```

### 示例3：检查文件是否为符号链接

```python
import os
import stat
import platform

def is_symbolic_link(file_path):
    """检查文件是否为符号链接"""
    try:
        file_stat = os.lstat(file_path)  # 使用lstat()不跟随符号链接
        file_type = stat.S_IFMT(file_stat.st_mode)
        return file_type == stat.S_IFLNK
    except (OSError, FileNotFoundError):
        return False

# 示例（仅在支持符号链接的系统上有效）
if platform.system() != "Windows" or os.name == "posix":
    try:
        # 创建符号链接
        os.symlink("target_file.txt", "link_file.txt")
        
        # 检查是否为符号链接
        print(f"'link_file.txt' 是符号链接: {is_symbolic_link('link_file.txt')}")
        print(f"'target_file.txt' 是符号链接: {is_symbolic_link('target_file.txt')}")
        
        # 清理
        os.unlink("link_file.txt")
    except OSError as e:
        print(f"创建符号链接失败: {e}")
else:
    print("当前系统可能不支持符号链接或需要管理员权限")
```

### 示例4：统计目录中不同类型的文件

```python
import os
import stat

def count_file_types(directory):
    """统计目录中不同类型的文件"""
    file_types = {
        "regular": 0,    # 常规文件
        "directory": 0,  # 目录
        "link": 0,       # 符号链接
        "block": 0,      # 块设备
        "char": 0,       # 字符设备
        "fifo": 0,       # FIFO管道
        "socket": 0,     # 套接字
        "unknown": 0     # 未知类型
    }
    
    for root, dirs, files in os.walk(directory):
        # 统计目录
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                dir_stat = os.lstat(dir_path)
                dir_type = stat.S_IFMT(dir_stat.st_mode)
                
                if dir_type == stat.S_IFDIR:
                    file_types["directory"] += 1
                elif dir_type == stat.S_IFLNK:
                    file_types["link"] += 1
                else:
                    file_types["unknown"] += 1
            except (OSError, PermissionError):
                continue
        
        # 统计文件
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                file_stat = os.lstat(file_path)
                file_type = stat.S_IFMT(file_stat.st_mode)
                
                if file_type == stat.S_IFREG:
                    file_types["regular"] += 1
                elif file_type == stat.S_IFLNK:
                    file_types["link"] += 1
                elif file_type == stat.S_IFBLK:
                    file_types["block"] += 1
                elif file_type == stat.S_IFCHR:
                    file_types["char"] += 1
                elif file_type == stat.S_IFIFO:
                    file_types["fifo"] += 1
                elif file_type == stat.S_ISSOCK:
                    file_types["socket"] += 1
                else:
                    file_types["unknown"] += 1
            except (OSError, PermissionError):
                continue
    
    return file_types

# 示例
# file_counts = count_file_types("./")
# print("文件类型统计:")
# for file_type, count in file_counts.items():
#     print(f"  {file_type}: {count}")
```

## 最佳实践

1. **与os模块配合使用**：stat模块主要用于解释os模块返回的文件状态信息
2. **使用常量代替数字**：使用stat模块定义的常量（如stat.S_IRUSR）代替直接使用数字（如0o400），使代码更具可读性
3. **跨平台考虑**：stat模块提供了跨平台的文件属性访问方式，避免直接使用平台特定的实现
4. **异常处理**：在获取文件状态信息时，捕获并处理可能的异常（如PermissionError、FileNotFoundError等）
5. **使用S_IFMT()获取文件类型**：使用stat.S_IFMT()函数从文件模式中提取文件类型
6. **使用S_IMODE()获取文件权限**：使用stat.S_IMODE()函数从文件模式中提取文件权限
7. **区分st_mtime和st_ctime**：st_mtime表示文件内容最后修改时间，st_ctime表示文件状态最后改变时间
8. **使用lstat()检查符号链接**：使用os.lstat()函数可以检查符号链接本身的属性，而不是跟随符号链接

## 与其他模块的关系

- **os**：stat模块与os模块配合使用，解释os.stat()、os.lstat()等函数返回的文件状态信息
- **os.path**：os.path模块提供了一些基于文件属性的函数，如os.path.isfile()、os.path.isdir()等，这些函数内部可能使用了stat模块
- **shutil**：shutil模块用于高级文件操作，可能会使用stat模块获取和设置文件属性
- **time**：stat模块返回的时间戳可以使用time模块转换为可读格式

## 总结

stat模块是Python标准库中的一个重要模块，用于提供文件状态信息的常量和函数。它主要与os模块配合使用，解释os模块返回的文件状态信息，提供了更加友好和跨平台的文件属性访问方式。

通过stat模块，可以获取和解析文件的类型、权限、大小、修改时间等属性，实现各种文件操作功能。它在文件管理、权限控制、文件系统遍历等场景中有着广泛的应用。