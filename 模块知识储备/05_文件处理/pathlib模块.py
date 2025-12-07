# pathlib模块详解

pathlib模块是Python 3.4+中引入的用于路径操作的现代模块，提供了面向对象的路径处理接口，使文件和目录操作更加直观和方便。

## 模块概述

pathlib模块提供了两种主要的路径类：
- **Path**：通用路径类，自动适应不同的操作系统
- **PosixPath**：Unix/Linux风格的路径类
- **WindowsPath**：Windows风格的路径类

这些类提供了丰富的方法用于路径操作、文件处理和目录管理，使代码更加简洁易读。

## 基本用法

### 导入模块

```python
from pathlib import Path
```

### 创建Path对象

```python
# 创建当前目录的Path对象
current_dir = Path('.')
print(f"当前目录: {current_dir}")
print(f"当前目录绝对路径: {current_dir.absolute()}")

# 创建指定路径的Path对象
# Windows路径
desktop_path = Path('C:/Users/Username/Desktop')
print(f"Windows桌面路径: {desktop_path}")

# Unix/Linux路径
# home_path = Path('/home/username')

# 使用字符串拼接路径
project_path = Path('g:/Python/模块知识储备')
file_path = project_path / '05_文件处理' / 'example.txt'
print(f"文件路径: {file_path}")
```

### 路径属性

```python
# 创建一个Path对象
path = Path('g:/Python/模块知识储备/05_文件处理/example.txt')

# 获取路径的各个部分
print(f"完整路径: {path}")
print(f"路径名称: {path.name}")
print(f"文件名称: {path.stem}")
print(f"文件扩展名: {path.suffix}")
print(f"父目录: {path.parent}")
print(f"驱动器: {path.drive}")
print(f"根目录: {path.root}")
print(f"相对路径部分: {path.relative_to('g:/Python')}")
```

### 路径检查

```python
# 创建Path对象
existing_path = Path('g:/Python/模块知识储备/05_文件处理')
non_existing_path = Path('g:/Python/模块知识储备/non_existing')

# 检查路径是否存在
print(f"existing_path是否存在: {existing_path.exists()}")
print(f"non_existing_path是否存在: {non_existing_path.exists()}")

# 检查路径类型
print(f"existing_path是否是目录: {existing_path.is_dir()}")
print(f"existing_path是否是文件: {existing_path.is_file()}")
print(f"existing_path是否是符号链接: {existing_path.is_symlink()}")
print(f"existing_path是否是块设备: {existing_path.is_block_device()}")
print(f"existing_path是否是字符设备: {existing_path.is_char_device()}")
print(f"existing_path是否是FIFO: {existing_path.is_fifo()}")
print(f"existing_path是否是套接字: {existing_path.is_socket()}")
```

## 文件操作

### 创建文件

```python
# 创建一个新文件
file_path = Path('g:/Python/模块知识储备/05_文件处理/new_file.txt')
file_path.touch()
print(f"文件已创建: {file_path}")

# 创建文件时设置权限（Windows上可能不生效）
# file_path.touch(mode=0o644)
```

### 写入文件

```python
# 写入文本内容
file_path = Path('g:/Python/模块知识储备/05_文件处理/text_file.txt')
file_path.write_text('Hello, Pathlib!\n这是一个测试文件。')
print(f"文本内容已写入: {file_path}")

# 写入二进制内容
binary_file_path = Path('g:/Python/模块知识储备/05_文件处理/binary_file.bin')
binary_file_path.write_bytes(b'\x00\x01\x02\x03\x04\x05')
print(f"二进制内容已写入: {binary_file_path}")
```

### 读取文件

```python
# 读取文本内容
file_path = Path('g:/Python/模块知识储备/05_文件处理/text_file.txt')
content = file_path.read_text()
print(f"文件内容:\n{content}")

# 读取二进制内容
binary_file_path = Path('g:/Python/模块知识储备/05_文件处理/binary_file.bin')
binary_content = binary_file_path.read_bytes()
print(f"二进制文件内容: {binary_content}")
```

### 删除文件

```python
# 删除文件
file_path = Path('g:/Python/模块知识储备/05_文件处理/new_file.txt')
file_path.unlink()
print(f"文件已删除: {file_path}")

# 安全删除（如果文件不存在不会引发异常）
non_existing_path = Path('g:/Python/模块知识储备/05_文件处理/non_existing.txt')
non_existing_path.unlink(missing_ok=True)
print(f"尝试删除不存在的文件（已忽略）")
```

### 文件信息

```python
# 获取文件信息
file_path = Path('g:/Python/模块知识储备/05_文件处理/text_file.txt')

# 获取文件大小
file_size = file_path.stat().st_size
print(f"文件大小: {file_size} 字节")

# 获取文件修改时间
import time
mtime = file_path.stat().st_mtime
print(f"文件修改时间: {time.ctime(mtime)}")

# 获取文件创建时间（Windows）
ctime = file_path.stat().st_ctime
print(f"文件创建时间: {time.ctime(ctime)}")

# 获取文件访问时间
atime = file_path.stat().st_atime
print(f"文件访问时间: {time.ctime(atime)}")
```

## 目录操作

### 创建目录

```python
# 创建单个目录
new_dir = Path('g:/Python/模块知识储备/05_文件处理/new_dir')
new_dir.mkdir(exist_ok=True)
print(f"目录已创建: {new_dir}")

# 创建嵌套目录
nested_dir = Path('g:/Python/模块知识储备/05_文件处理/level1/level2/level3')
nested_dir.mkdir(parents=True, exist_ok=True)
print(f"嵌套目录已创建: {nested_dir}")
```

### 遍历目录

```python
# 遍历当前目录的所有文件和子目录
current_dir = Path('g:/Python/模块知识储备/05_文件处理')
print("目录内容:")
for item in current_dir.iterdir():
    if item.is_dir():
        print(f"  [目录] {item.name}")
    else:
        print(f"  [文件] {item.name} ({item.stat().st_size} 字节)")

# 遍历目录中的特定类型文件
print("\nPython文件:")
for file in current_dir.glob('*.py'):
    print(f"  {file.name}")

# 递归遍历所有子目录中的特定类型文件
print("\n所有子目录中的Python文件:")
for file in current_dir.rglob('*.py'):
    print(f"  {file}")
```

### 删除目录

```python
# 删除空目录
empty_dir = Path('g:/Python/模块知识储备/05_文件处理/new_dir')
empty_dir.rmdir()
print(f"空目录已删除: {empty_dir}")

# 删除非空目录需要使用shutil模块
import shutil
non_empty_dir = Path('g:/Python/模块知识储备/05_文件处理/level1')
shutil.rmtree(non_empty_dir)
print(f"非空目录已删除: {non_empty_dir}")
```

## 高级功能

### 路径匹配

```python
# 创建Path对象
dir_path = Path('g:/Python/模块知识储备/05_文件处理')

# 使用glob匹配文件
print("匹配所有.txt文件:")
for file in dir_path.glob('*.txt'):
    print(f"  {file}")

# 使用rglob递归匹配
print("\n递归匹配所有.py文件:")
for file in dir_path.rglob('*.py'):
    print(f"  {file}")

# 使用通配符匹配
print("\n匹配所有以'text'开头的文件:")
for file in dir_path.glob('text*'):
    print(f"  {file}")

# 使用?匹配单个字符
print("\n匹配所有以单个字符开头，.txt结尾的文件:")
for file in dir_path.glob('?.txt'):
    print(f"  {file}")
```

### 路径替换

```python
# 创建Path对象
file_path = Path('g:/Python/模块知识储备/05_文件处理/example.txt')

# 替换文件扩展名
new_file_path = file_path.with_suffix('.md')
print(f"替换扩展名后的路径: {new_file_path}")

# 替换文件名
new_file_path = file_path.with_stem('new_example')
print(f"替换文件名后的路径: {new_file_path}")

# 替换父目录
new_file_path = file_path.parent.parent / '06_网络通信' / file_path.name
print(f"替换父目录后的路径: {new_file_path}")
```

### 路径比较

```python
# 创建Path对象
path1 = Path('g:/Python/模块知识储备/05_文件处理/example.txt')
path2 = Path('g:/Python/模块知识储备/05_文件处理/example.txt')
path3 = Path('g:/Python/模块知识储备/05_文件处理/different.txt')

# 比较路径是否相等
print(f"path1 == path2: {path1 == path2}")
print(f"path1 == path3: {path1 == path3}")

# 比较路径的排序
paths = [path3, path1, path2]
sorted_paths = sorted(paths)
print(f"排序后的路径: {sorted_paths}")
```

### 链接操作

```python
# 创建原始文件
original_file = Path('g:/Python/模块知识储备/05_文件处理/original.txt')
original_file.write_text('This is the original file.')

# 创建硬链接（Windows上需要管理员权限）
# hard_link = Path('g:/Python/模块知识储备/05_文件处理/hard_link.txt')
# original_file.link_to(hard_link)

# 创建符号链接
sym_link = Path('g:/Python/模块知识储备/05_文件处理/sym_link.txt')
original_file.symlink_to(sym_link)
print(f"符号链接已创建: {sym_link}")
print(f"符号链接是否存在: {sym_link.exists()}")
print(f"符号链接指向的文件: {sym_link.resolve()}")
```

## 实际应用示例

### 示例1：批量重命名文件

```python
def batch_rename(directory, old_suffix, new_suffix):
    """批量重命名文件的扩展名"""
    dir_path = Path(directory)
    for file in dir_path.glob(f'*{old_suffix}'):
        new_file = file.with_suffix(new_suffix)
        file.rename(new_file)
        print(f"重命名: {file.name} -> {new_file.name}")

# 创建测试文件
for i in range(5):
    file_path = Path(f'g:/Python/模块知识储备/05_文件处理/test_{i}.txt')
    file_path.write_text(f'This is test file {i}.')

# 批量重命名文件
print("批量重命名文件:")
batch_rename('g:/Python/模块知识储备/05_文件处理', '.txt', '.md')
```

### 示例2：统计目录大小

```python
def get_directory_size(directory):
    """计算目录的总大小"""
    dir_path = Path(directory)
    total_size = 0
    for file in dir_path.rglob('*'):
        if file.is_file():
            total_size += file.stat().st_size
    return total_size

# 计算目录大小
size = get_directory_size('g:/Python/模块知识储备/05_文件处理')
print(f"目录大小: {size} 字节 = {size / 1024:.2f} KB = {size / (1024*1024):.2f} MB")
```

### 示例3：查找最近修改的文件

```python
def find_recently_modified_files(directory, days=7):
    """查找最近指定天数内修改的文件"""
    import datetime
    dir_path = Path(directory)
    recent_files = []
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
    
    for file in dir_path.rglob('*'):
        if file.is_file():
            mtime = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            if mtime > cutoff_date:
                recent_files.append((file, mtime))
    
    # 按修改时间排序
    recent_files.sort(key=lambda x: x[1], reverse=True)
    return recent_files

# 查找最近修改的文件
print("最近修改的文件:")
recent_files = find_recently_modified_files('g:/Python/模块知识储备/05_文件处理')
for file, mtime in recent_files[:10]:  # 显示最近10个文件
    print(f"  {file.name} - {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
```

### 示例4：创建文件备份

```python
def create_backup(file_path):
    """创建文件的备份"""
    file = Path(file_path)
    if not file.exists():
        print(f"文件不存在: {file}")
        return None
    
    # 创建备份文件路径
    backup_path = file.with_name(f"{file.stem}_backup{file.suffix}")
    
    # 复制文件内容
    backup_path.write_bytes(file.read_bytes())
    print(f"备份已创建: {backup_path}")
    return backup_path

# 创建文件备份
test_file = Path('g:/Python/模块知识储备/05_文件处理/text_file.txt')
backup_file = create_backup(test_file)
```

### 示例5：文件差异比较

```python
def compare_files(file1_path, file2_path):
    """比较两个文件的内容是否相同"""
    file1 = Path(file1_path)
    file2 = Path(file2_path)
    
    if not file1.exists():
        print(f"文件不存在: {file1}")
        return False
    if not file2.exists():
        print(f"文件不存在: {file2}")
        return False
    
    return file1.read_bytes() == file2.read_bytes()

# 创建测试文件
file1 = Path('g:/Python/模块知识储备/05_文件处理/file1.txt')
file2 = Path('g:/Python/模块知识储备/05_文件处理/file2.txt')
file1.write_text('Hello, World!')
file2.write_text('Hello, World!')

# 比较文件
if compare_files(file1, file2):
    print("文件内容相同")
else:
    print("文件内容不同")
```

## 与os.path的比较

| 操作 | os.path | pathlib |
|------|---------|---------|
| 创建路径 | os.path.join('a', 'b') | Path('a') / 'b' |
| 获取文件名 | os.path.basename(path) | path.name |
| 获取目录名 | os.path.dirname(path) | path.parent |
| 检查文件是否存在 | os.path.exists(path) | path.exists() |
| 检查是否是目录 | os.path.isdir(path) | path.is_dir() |
| 检查是否是文件 | os.path.isfile(path) | path.is_file() |
| 获取文件大小 | os.path.getsize(path) | path.stat().st_size |
| 获取修改时间 | os.path.getmtime(path) | path.stat().st_mtime |
| 遍历目录 | os.listdir(path) | list(path.iterdir()) |

## 最佳实践

1. **使用Path对象代替字符串**：Path对象提供了更丰富的方法和属性，使代码更易读和维护。
2. **使用/操作符拼接路径**：避免使用字符串拼接，可以自动处理不同操作系统的路径分隔符。
3. **使用exists()检查路径**：在操作文件或目录前，先检查路径是否存在。
4. **使用glob和rglob查找文件**：比os.listdir()更灵活和强大。
5. **使用with_suffix()和with_stem()修改文件名**：比字符串操作更安全和方便。
6. **使用read_text()和write_text()处理文本文件**：自动处理编码问题。

## 清理示例文件

```python
# 清理示例文件
import os
import shutil

# 获取当前目录
current_dir = Path('g:/Python/模块知识储备/05_文件处理')

# 删除示例文件
for file in current_dir.glob('*.txt') + current_dir.glob('*.md') + current_dir.glob('*.bin'):
    file.unlink()

# 删除创建的目录
for dir in current_dir.iterdir():
    if dir.is_dir() and 'level1' in dir.name:
        shutil.rmtree(dir)

print("示例文件和目录已清理")
```

## 总结

pathlib模块是Python中用于路径操作和文件管理的现代工具，提供了面向对象的接口，使代码更加简洁、易读和跨平台兼容。熟练掌握pathlib模块的使用，可以提高文件和目录操作的效率和代码质量。

pathlib模块的主要优势包括：
- 面向对象的设计，使代码更易读和维护
- 自动适应不同操作系统的路径风格
- 丰富的方法用于路径操作和文件处理
- 强大的文件查找和匹配功能
- 与现代Python编程风格一致

在Python 3.4+的项目中，推荐使用pathlib模块代替传统的os.path模块，以获得更好的开发体验和代码质量。