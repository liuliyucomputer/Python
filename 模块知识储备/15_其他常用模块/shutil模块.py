# Python shutil模块详细指南

## 一、模块概述

`shutil`（shell utilities）模块是Python标准库中提供高级文件和目录操作功能的模块。它扩展了`os`模块的功能，提供了更方便的文件和目录复制、移动、删除、归档等操作。`shutil`模块的设计目标是提供跨平台的文件操作功能，使得Python程序能够轻松地执行复杂的文件系统操作。

## 二、基本概念

1. **文件操作**：复制、移动、重命名、删除文件
2. **目录操作**：复制、移动、重命名、删除目录（包括非空目录）
3. **文件归档**：创建和提取压缩文件（如ZIP、TAR等）
4. **文件元数据**：复制文件的元数据（如权限、修改时间等）
5. **磁盘使用**：获取磁盘使用情况
6. **文件系统操作**：执行文件系统级别的操作

## 三、基本用法

### 1. 导入模块

```python
import shutil
```

### 2. 文件操作

#### 2.1 复制文件

```python
# 基本的文件复制
shutil.copy('源文件.txt', '目标文件.txt')  # 复制文件内容和权限
shutil.copy2('源文件.txt', '目标文件.txt')  # 复制文件内容和所有元数据（包括修改时间、权限等）
shutil.copyfile('源文件.txt', '目标文件.txt')  # 仅复制文件内容，不复制元数据
shutil.copyfileobj(open('源文件.txt', 'rb'), open('目标文件.txt', 'wb'))  # 从文件对象复制到文件对象

# 使用示例
shutil.copy2('g:/Python/模块知识储备/15_其他常用模块/os模块.py', 'g:/Python/模块知识储备/15_其他常用模块/os_copy.py')
print("文件复制成功")
```

#### 2.2 移动文件

```python
# 移动文件
shutil.move('源文件.txt', '目标文件.txt')  # 移动文件（可跨文件系统）
shutil.move('源文件.txt', '目标目录/')  # 移动文件到目标目录

# 使用示例
shutil.move('g:/Python/模块知识储备/15_其他常用模块/os_copy.py', 'g:/Python/模块知识储备/15_其他常用模块/os_moved.py')
print("文件移动成功")
```

#### 2.3 删除文件

```python
# 删除文件（可使用os.unlink或os.remove）
import os
os.remove('文件.txt')  # 删除单个文件
os.unlink('文件.txt')  # 删除单个文件（与remove功能相同）

# 使用示例
if os.path.exists('g:/Python/模块知识储备/15_其他常用模块/os_moved.py'):
    os.remove('g:/Python/模块知识储备/15_其他常用模块/os_moved.py')
    print("文件删除成功")
```

### 3. 目录操作

#### 3.1 复制目录

```python
# 复制目录（包括内容）
shutil.copytree('源目录', '目标目录')  # 递归复制目录及其内容
shutil.copytree('源目录', '目标目录', symlinks=True)  # 复制符号链接本身而非其指向的文件
shutil.copytree('源目录', '目标目录', ignore=shutil.ignore_patterns('*.pyc', '__pycache__'))  # 忽略指定模式的文件

# 使用示例
shutil.copytree('g:/Python/模块知识储备/15_其他常用模块', 'g:/Python/模块知识储备/15_其他常用模块_copy')
print("目录复制成功")
```

#### 3.2 移动目录

```python
# 移动目录
shutil.move('源目录', '目标目录')  # 移动目录（可跨文件系统）
shutil.move('源目录', '新目录名')  # 重命名目录

# 使用示例
shutil.move('g:/Python/模块知识储备/15_其他常用模块_copy', 'g:/Python/模块知识储备/15_其他常用模块_moved')
print("目录移动成功")
```

#### 3.3 删除目录

```python
# 删除目录（包括非空目录）
shutil.rmtree('目录名')  # 递归删除目录及其内容
shutil.rmtree('目录名', ignore_errors=True)  # 忽略删除错误
shutil.rmtree('目录名', onerror=lambda func, path, exc_info: print(f"删除失败: {path}"))  # 自定义错误处理

# 使用示例
shutil.rmtree('g:/Python/模块知识储备/15_其他常用模块_moved')
print("目录删除成功")
```

### 4. 归档操作

#### 4.1 创建归档文件

```python
# 创建ZIP归档
shutil.make_archive('归档文件名', 'zip', '源目录')  # 创建ZIP格式归档

# 创建TAR归档
shutil.make_archive('归档文件名', 'tar', '源目录')  # 创建TAR格式归档
shutil.make_archive('归档文件名', 'gztar', '源目录')  # 创建TGZ格式归档
shutil.make_archive('归档文件名', 'bztar', '源目录')  # 创建TBZ2格式归档
shutil.make_archive('归档文件名', 'xztar', '源目录')  # 创建TXZ格式归档

# 使用示例
shutil.make_archive('g:/Python/模块知识储备/15_其他常用模块_archive', 'zip', 'g:/Python/模块知识储备/15_其他常用模块')
print("归档文件创建成功")
```

#### 4.2 提取归档文件

```python
# 提取归档文件
shutil.unpack_archive('归档文件.zip', '目标目录')  # 自动检测归档格式并提取
shutil.unpack_archive('归档文件.tar.gz', '目标目录', 'gztar')  # 指定归档格式并提取

# 使用示例
shutil.unpack_archive('g:/Python/模块知识储备/15_其他常用模块_archive.zip', 'g:/Python/模块知识储备/15_其他常用模块_extracted')
print("归档文件提取成功")

# 清理临时文件
import os
os.remove('g:/Python/模块知识储备/15_其他常用模块_archive.zip')
shutil.rmtree('g:/Python/模块知识储备/15_其他常用模块_extracted')
```

#### 4.3 获取支持的归档格式

```python
# 获取支持的归档格式
formats = shutil.get_archive_formats()
print("支持的归档格式:")
for format, description in formats:
    print(f"  {format}: {description}")

# 获取支持的解压缩格式
extract_formats = shutil.get_unpack_formats()
print("支持的解压缩格式:")
for format, extensions, description in extract_formats:
    print(f"  {format}: {extensions} - {description}")
```

### 5. 磁盘使用情况

```python
# 获取磁盘使用情况
disk_usage = shutil.disk_usage('g:/')
print(f"磁盘总空间: {disk_usage.total / (1024 ** 3):.2f} GB")
print(f"已使用空间: {disk_usage.used / (1024 ** 3):.2f} GB")
print(f"可用空间: {disk_usage.free / (1024 ** 3):.2f} GB")
print(f"使用率: {disk_usage.used / disk_usage.total * 100:.1f}%")
```

### 6. 文件元数据操作

#### 6.1 复制文件元数据

```python
# 复制文件元数据
shutil.copystat('源文件.txt', '目标文件.txt')  # 复制文件权限、修改时间等元数据
shutil.copymode('源文件.txt', '目标文件.txt')  # 仅复制文件权限

# 使用示例
shutil.copyfile('g:/Python/模块知识储备/15_其他常用模块/os模块.py', 'g:/Python/模块知识储备/15_其他常用模块/os_metadata.py')
shutil.copystat('g:/Python/模块知识储备/15_其他常用模块/os模块.py', 'g:/Python/模块知识储备/15_其他常用模块/os_metadata.py')
print("文件元数据复制成功")

# 清理临时文件
import os
os.remove('g:/Python/模块知识储备/15_其他常用模块/os_metadata.py')
```

#### 6.2 获取文件权限

```python
# 获取文件权限
import stat
file_path = 'g:/Python/模块知识储备/15_其他常用模块/os模块.py'
permissions = stat.filemode(os.stat(file_path).st_mode)
print(f"文件权限: {permissions}")
```

### 7. 其他功能

#### 7.1 获取终端大小

```python
# 获取终端大小
terminal_size = shutil.get_terminal_size()
print(f"终端宽度: {terminal_size.columns}")
print(f"终端高度: {terminal_size.lines}")
```

#### 7.2 复制树（高级）

```python
# 使用copy_tree复制目录（较copytree更灵活）
# 注意：copy_tree是shutil的内部函数，可能在未来版本中变化
from shutil import _copytree as copy_tree
copy_tree('源目录', '目标目录', symlinks=True, ignore=None)
```

## 四、高级用法

### 1. 自定义复制过滤器

```python
# 自定义复制过滤器
def custom_ignore(src, names):
    """自定义忽略规则：忽略.pyc文件和__pycache__目录"""
    ignore_list = []
    for name in names:
        if name.endswith('.pyc') or name == '__pycache__':
            ignore_list.append(name)
    return ignore_list

# 使用自定义过滤器复制目录
shutil.copytree('g:/Python/模块知识储备/15_其他常用模块', 'g:/Python/模块知识储备/15_其他常用模块_filtered', ignore=custom_ignore)
print("使用自定义过滤器复制目录成功")

# 清理临时目录
shutil.rmtree('g:/Python/模块知识储备/15_其他常用模块_filtered')
```

### 2. 批量文件操作

```python
# 批量复制文件
def batch_copy_files(source_dir, target_dir, extension):
    """批量复制指定扩展名的文件"""
    import os
    # 创建目标目录（如果不存在）
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    copied_files = []
    for file in os.listdir(source_dir):
        if file.endswith(extension):
            source_path = os.path.join(source_dir, file)
            target_path = os.path.join(target_dir, file)
            shutil.copy2(source_path, target_path)
            copied_files.append(target_path)
            print(f"复制文件: {file}")
    
    return copied_files

# 使用示例
source_dir = 'g:/Python/模块知识储备/15_其他常用模块'
target_dir = 'g:/Python/模块知识储备/15_其他常用模块_py_files'
extension = '.py'
copied_files = batch_copy_files(source_dir, target_dir, extension)
print(f"共复制了{len(copied_files)}个{extension}文件")

# 清理临时目录
shutil.rmtree(target_dir)
```

### 3. 文件系统备份

```python
# 文件系统备份
def backup_filesystem(source_dir, backup_dir, include_extensions=None, exclude_dirs=None):
    """备份文件系统"""
    import os
    import datetime
    
    # 创建备份目录（如果不存在）
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # 生成备份文件名
    now = datetime.datetime.now()
    backup_name = f"backup_{now.strftime('%Y%m%d_%H%M%S')}"
    backup_path = os.path.join(backup_dir, backup_name)
    
    # 定义忽略规则
    def ignore_func(src, names):
        ignore_list = []
        for name in names:
            full_path = os.path.join(src, name)
            # 忽略指定目录
            if exclude_dirs and name in exclude_dirs:
                ignore_list.append(name)
            # 如果指定了扩展名，则只包含指定扩展名的文件
            elif include_extensions and os.path.isfile(full_path) and not any(name.endswith(ext) for ext in include_extensions):
                ignore_list.append(name)
        return ignore_list
    
    try:
        # 复制目录
        shutil.copytree(source_dir, backup_path, ignore=ignore_func)
        print(f"备份成功: {backup_path}")
        return backup_path
    except Exception as e:
        print(f"备份失败: {e}")
        return None

# 使用示例
source_dir = 'g:/Python/模块知识储备/15_其他常用模块'
backup_dir = 'g:/Python/备份'
include_extensions = ['.py', '.md']
exclude_dirs = ['__pycache__']
backup_path = backup_filesystem(source_dir, backup_dir, include_extensions, exclude_dirs)

# 清理临时备份
if backup_path:
    shutil.rmtree(backup_path)
    print("临时备份已清理")
```

### 4. 比较目录内容

```python
# 比较两个目录的内容
def compare_directories(dir1, dir2):
    """比较两个目录的内容"""
    import os
    import filecmp
    
    # 使用filecmp比较目录
    dcmp = filecmp.dircmp(dir1, dir2)
    
    # 打印比较结果
    print(f"仅在{dir1}中的文件: {dcmp.left_only}")
    print(f"仅在{dir2}中的文件: {dcmp.right_only}")
    print(f"两边都有的文件: {dcmp.common}")
    print(f"两边都有的子目录: {dcmp.common_dirs}")
    print(f"内容不同的文件: {dcmp.diff_files}")
    print(f"元数据不同的文件: {dcmp.funny_files}")
    
    # 递归比较子目录
    for subdir in dcmp.common_dirs:
        print(f"\n比较子目录: {subdir}")
        compare_directories(os.path.join(dir1, subdir), os.path.join(dir2, subdir))

# 使用示例
# 创建两个测试目录
os.makedirs('g:/Python/模块知识储备/15_其他常用模块/test1')
os.makedirs('g:/Python/模块知识储备/15_其他常用模块/test2')

# 创建测试文件
with open('g:/Python/模块知识储备/15_其他常用模块/test1/file1.txt', 'w') as f:
    f.write('内容1')
with open('g:/Python/模块知识储备/15_其他常用模块/test2/file1.txt', 'w') as f:
    f.write('内容2')
with open('g:/Python/模块知识储备/15_其他常用模块/test1/file2.txt', 'w') as f:
    f.write('内容3')

# 比较目录
compare_directories('g:/Python/模块知识储备/15_其他常用模块/test1', 'g:/Python/模块知识储备/15_其他常用模块/test2')

# 清理测试目录
shutil.rmtree('g:/Python/模块知识储备/15_其他常用模块/test1')
shutil.rmtree('g:/Python/模块知识储备/15_其他常用模块/test2')
```

### 5. 大文件复制（分块）

```python
# 大文件复制（分块）
def copy_large_file(src_path, dst_path, chunk_size=1024*1024):  # 1MB块
    """分块复制大文件"""
    with open(src_path, 'rb') as src_file:
        with open(dst_path, 'wb') as dst_file:
            while True:
                chunk = src_file.read(chunk_size)
                if not chunk:
                    break
                dst_file.write(chunk)
    print(f"大文件复制成功: {src_path} -> {dst_path}")

# 使用示例
# 创建一个大文件（模拟）
# with open('g:/Python/模块知识储备/15_其他常用模块/large_file.txt', 'wb') as f:
#     f.write(b'0' * 1024 * 1024 * 10)  # 10MB文件

# 复制大文件
# copy_large_file('g:/Python/模块知识储备/15_其他常用模块/large_file.txt', 'g:/Python/模块知识储备/15_其他常用模块/large_file_copy.txt')

# 清理大文件
# os.remove('g:/Python/模块知识储备/15_其他常用模块/large_file.txt')
# os.remove('g:/Python/模块知识储备/15_其他常用模块/large_file_copy.txt')
```

## 五、实际应用示例

### 1. 自动备份系统

```python
# 自动备份系统
import os
import datetime
import shutil

def auto_backup(source_dirs, backup_dir, max_backups=5):
    """自动备份多个目录，保留最近N个备份"""
    # 创建备份目录（如果不存在）
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # 生成备份文件名
    now = datetime.datetime.now()
    backup_name = f"backup_{now.strftime('%Y%m%d_%H%M%S')}"
    backup_path = os.path.join(backup_dir, backup_name)
    os.makedirs(backup_path)
    
    # 备份每个源目录
    for source_dir in source_dirs:
        dir_name = os.path.basename(source_dir)
        target_dir = os.path.join(backup_path, dir_name)
        try:
            shutil.copytree(source_dir, target_dir)
            print(f"备份成功: {source_dir} -> {target_dir}")
        except Exception as e:
            print(f"备份失败{source_dir}: {e}")
    
    # 清理旧备份
    backups = sorted(os.listdir(backup_dir), reverse=True)
    if len(backups) > max_backups:
        for old_backup in backups[max_backups:]:
            old_backup_path = os.path.join(backup_dir, old_backup)
            try:
                shutil.rmtree(old_backup_path)
                print(f"清理旧备份: {old_backup_path}")
            except Exception as e:
                print(f"清理旧备份失败{old_backup_path}: {e}")
    
    return backup_path

# 使用示例
source_dirs = ['g:/Python/模块知识储备/15_其他常用模块']
backup_dir = 'g:/Python/自动备份'
backup_path = auto_backup(source_dirs, backup_dir, max_backups=3)
print(f"自动备份完成: {backup_path}")
```

### 2. 文件同步工具

```python
# 简单的文件同步工具
def sync_directories(source_dir, target_dir):
    """同步源目录到目标目录"""
    import os
    import filecmp
    
    # 创建目标目录（如果不存在）
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # 获取源目录和目标目录的内容
    source_files = set(os.listdir(source_dir))
    target_files = set(os.listdir(target_dir))
    
    # 复制新文件或更新已更改的文件
    for file in source_files:
        source_path = os.path.join(source_dir, file)
        target_path = os.path.join(target_dir, file)
        
        if os.path.isfile(source_path):
            if file not in target_files or not filecmp.cmp(source_path, target_path):
                shutil.copy2(source_path, target_path)
                print(f"复制/更新文件: {file}")
        elif os.path.isdir(source_path):
            # 递归同步子目录
            sync_directories(source_path, target_path)
    
    # 删除目标目录中不存在于源目录的文件
    for file in target_files:
        if file not in source_files:
            target_path = os.path.join(target_dir, file)
            if os.path.isfile(target_path):
                os.remove(target_path)
                print(f"删除文件: {file}")
            elif os.path.isdir(target_path):
                shutil.rmtree(target_path)
                print(f"删除目录: {file}")

# 使用示例
# 创建测试目录
os.makedirs('g:/Python/模块知识储备/15_其他常用模块/source')
os.makedirs('g:/Python/模块知识储备/15_其他常用模块/target')

# 创建测试文件
with open('g:/Python/模块知识储备/15_其他常用模块/source/file1.txt', 'w') as f:
    f.write('内容1')
with open('g:/Python/模块知识储备/15_其他常用模块/target/file2.txt', 'w') as f:
    f.write('内容2')

# 同步目录
sync_directories('g:/Python/模块知识储备/15_其他常用模块/source', 'g:/Python/模块知识储备/15_其他常用模块/target')

# 清理测试目录
shutil.rmtree('g:/Python/模块知识储备/15_其他常用模块/source')
shutil.rmtree('g:/Python/模块知识储备/15_其他常用模块/target')
```

### 3. 归档管理系统

```python
# 归档管理系统
import os
import datetime
import shutil

def archive_files(files, archive_dir):
    """归档文件到指定目录"""
    # 创建归档目录（如果不存在）
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    # 生成归档文件名
    now = datetime.datetime.now()
    archive_name = f"archive_{now.strftime('%Y%m%d_%H%M%S')}"
    archive_path = os.path.join(archive_dir, archive_name)
    os.makedirs(archive_path)
    
    # 复制文件到归档目录
    archived_files = []
    for file in files:
        if os.path.exists(file):
            file_name = os.path.basename(file)
            target_path = os.path.join(archive_path, file_name)
            shutil.copy2(file, target_path)
            archived_files.append(target_path)
            print(f"归档文件: {file} -> {target_path}")
    
    # 创建ZIP归档
    zip_path = shutil.make_archive(archive_path, 'zip', archive_path)
    print(f"创建ZIP归档: {zip_path}")
    
    # 清理临时归档目录
    shutil.rmtree(archive_path)
    
    return zip_path

# 使用示例
files_to_archive = ['g:/Python/模块知识储备/15_其他常用模块/os模块.py', 'g:/Python/模块知识储备/15_其他常用模块/shutil模块.py']
archive_dir = 'g:/Python/归档'
zip_path = archive_files(files_to_archive, archive_dir)
print(f"归档完成: {zip_path}")

# 清理临时归档
os.remove(zip_path)
```

## 六、最佳实践

1. **跨平台兼容性**：
   - 始终使用`os.path.join`拼接路径，避免硬编码路径分隔符
   - 使用`shutil.copy2`而非`shutil.copy`以保留文件元数据
   - 避免使用平台特定的文件操作命令

2. **错误处理**：
   - 捕获`shutil`操作可能抛出的异常（如`OSError`、`IOError`）
   - 使用`ignore_errors=True`或自定义`onerror`处理删除错误
   - 验证文件/目录存在性后再执行操作

3. **性能优化**：
   - 对于大文件，使用分块复制（如`copy_large_file`）
   - 避免在循环中频繁创建和删除目录
   - 使用`shutil.copytree`而非手动递归复制目录

4. **安全考虑**：
   - 验证用户输入的路径，避免路径遍历攻击
   - 限制文件操作的权限范围
   - 加密敏感文件后再归档

5. **资源管理**：
   - 使用`with`语句处理文件对象，确保文件正确关闭
   - 清理临时文件和目录
   - 限制备份文件的数量，避免磁盘空间耗尽

6. **代码可读性**：
   - 封装重复的文件操作逻辑为函数
   - 使用有意义的变量名和函数名
   - 添加详细的文档字符串

## 七、与其他模块的关系

1. **os模块**：
   - `shutil`模块扩展了`os`模块的功能
   - `os`提供基础的文件和目录操作，`shutil`提供更高级的操作
   - 两者通常结合使用，如使用`os.path`处理路径，使用`shutil`执行复制、移动等操作

2. **pathlib模块**：
   - `pathlib`提供了面向对象的路径操作
   - 可以与`shutil`结合使用，如`shutil.copy2(pathlib.Path('src'), pathlib.Path('dst'))`

3. **zipfile/tarfile模块**：
   - `zipfile`和`tarfile`提供更高级的归档操作
   - `shutil.make_archive`和`shutil.unpack_archive`内部使用这些模块
   - 对于复杂的归档需求，建议直接使用这些模块

4. **filecmp模块**：
   - `filecmp`模块用于比较文件和目录
   - 可以与`shutil`结合使用，如在同步目录时比较文件内容

5. **tempfile模块**：
   - `tempfile`模块用于创建临时文件和目录
   - 可以与`shutil`结合使用，如临时存储复制的文件

## 八、总结

`shutil`模块是Python标准库中功能强大的高级文件操作模块，提供了丰富的功能来处理文件和目录的复制、移动、删除、归档等操作。通过掌握该模块的使用，可以使Python程序能够轻松地执行复杂的文件系统操作，提高程序的效率和可维护性。

从简单的文件复制到复杂的目录同步，从归档文件创建到磁盘使用情况查询，`shutil`模块提供了全面的文件系统操作功能。结合`os`、`pathlib`、`zipfile`等模块，可以实现更复杂和高级的文件系统交互功能。

在使用`shutil`模块时，需要注意跨平台兼容性、错误处理、性能优化等问题，遵循最佳实践，编写出高效、安全、可移植的Python程序。