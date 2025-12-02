"""
# os模块详解：操作系统接口

os模块是Python与操作系统交互的核心模块，提供了大量用于处理文件和目录、进程管理、环境变量等操作系统相关功能的函数。通过os模块，Python程序可以跨平台地访问操作系统功能，实现文件操作、目录遍历、进程控制等任务。

## 1. 核心功能概览

os模块的主要功能可以分为以下几类：

1. **文件和目录操作**：创建、删除、重命名文件和目录，改变工作目录等
2. **路径操作**：路径分割、连接、绝对路径获取等（主要通过os.path子模块）
3. **进程管理**：执行系统命令、管理子进程等
4. **环境变量操作**：获取和设置环境变量
5. **用户和权限**：获取用户信息、修改文件权限等
6. **设备管理**：获取设备信息、磁盘使用情况等

## 2. 基础路径操作

### 2.1 路径分隔符和常量

```python
import os

# 获取当前操作系统的路径分隔符（Windows为'\', Unix为'/'）
print(f"路径分隔符: {os.sep}")

# 获取当前操作系统的路径分隔符（用于PATH环境变量等）
print(f"路径分隔符（PATH）: {os.pathsep}")

# 获取当前操作系统的换行符
print(f"换行符: {repr(os.linesep)}")

# 获取当前操作系统的名称
print(f"操作系统名称: {os.name}")  # Windows返回'nt'，Unix/Linux返回'posix'
```

### 2.2 当前工作目录操作

```python
import os

# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 改变当前工作目录
try:
    os.chdir('..')  # 切换到父目录
    print(f"新的工作目录: {os.getcwd()}")
    
    # 切回原来的目录
    os.chdir(current_dir)
except OSError as e:
    print(f"改变目录失败: {e}")
```

## 3. 文件操作

### 3.1 文件重命名和删除

```python
import os

def file_operations_demo():
    # 创建一个临时文件用于测试
    test_file = "test_file.txt"
    with open(test_file, 'w') as f:
        f.write("这是一个测试文件")
    
    print(f"创建文件: {test_file}")
    
    # 重命名文件
    new_name = "renamed_file.txt"
    os.rename(test_file, new_name)
    print(f"重命名为: {new_name}")
    
    # 删除文件
    os.remove(new_name)
    print(f"删除文件: {new_name}")
    
    # 检查文件是否存在
    exists = os.path.exists(new_name)
    print(f"文件是否存在: {exists}")

# 运行示例
file_operations_demo()
```

### 3.2 文件属性

```python
import os
import time

def file_attributes_demo():
    # 创建测试文件
    test_file = "test_attr.txt"
    with open(test_file, 'w') as f:
        f.write("测试文件属性")
    
    # 获取文件大小（字节）
    file_size = os.path.getsize(test_file)
    print(f"文件大小: {file_size} 字节")
    
    # 获取文件访问时间
    access_time = os.path.getatime(test_file)
    print(f"文件访问时间: {time.ctime(access_time)}")
    
    # 获取文件修改时间
    modify_time = os.path.getmtime(test_file)
    print(f"文件修改时间: {time.ctime(modify_time)}")
    
    # 获取文件创建时间（在某些系统上可能与修改时间相同）
    create_time = os.path.getctime(test_file)
    print(f"文件创建时间: {time.ctime(create_time)}")
    
    # 清理测试文件
    os.remove(test_file)

# 运行示例
file_attributes_demo()
```

## 4. 目录操作

### 4.1 目录创建、重命名和删除

```python
import os

def directory_operations_demo():
    # 创建单个目录
    new_dir = "new_directory"
    os.mkdir(new_dir)
    print(f"创建目录: {new_dir}")
    
    # 创建多级目录
    nested_dir = os.path.join(new_dir, "nested", "deep")
    os.makedirs(nested_dir)
    print(f"创建嵌套目录: {nested_dir}")
    
    # 重命名目录
    renamed_dir = "renamed_directory"
    os.rename(new_dir, renamed_dir)
    print(f"重命名目录: {new_dir} -> {renamed_dir}")
    
    # 删除空目录（只能删除空目录）
    os.rmdir(os.path.join(renamed_dir, "nested", "deep"))
    os.rmdir(os.path.join(renamed_dir, "nested"))
    
    # 删除整个目录树（递归删除）
    os.rmdir(renamed_dir)  # 因为现在是空目录了
    print(f"删除目录: {renamed_dir}")
    
    # 或者使用shutil.rmtree()删除非空目录
    # import shutil
    # shutil.rmtree(renamed_dir)

# 运行示例
directory_operations_demo()
```

### 4.2 目录内容列出

```python
import os

def list_directory_contents(path='.'):
    print(f"目录内容 ({path}):")
    
    # 列出目录中的所有文件和子目录
    items = os.listdir(path)
    for item in items:
        # 获取完整路径
        full_path = os.path.join(path, item)
        # 判断是否为目录
        if os.path.isdir(full_path):
            print(f"[目录] {item}")
        else:
            print(f"[文件] {item}")
    
    # 使用os.scandir()获取更详细的信息
    print("\n使用scandir():")
    with os.scandir(path) as entries:
        for entry in entries:
            if entry.is_dir():
                print(f"[目录] {entry.name}")
            else:
                print(f"[文件] {entry.name}, 大小: {entry.stat().st_size} 字节")

# 运行示例
list_directory_contents('.')
```

## 5. 路径处理（os.path子模块）

### 5.1 路径判断和操作

```python
import os

def path_operations_demo():
    # 路径判断
    test_path = "test_file.txt"
    
    # 创建测试文件
    with open(test_path, 'w') as f:
        f.write("测试")
    
    # 检查路径是否存在
    exists = os.path.exists(test_path)
    print(f"路径存在: {exists}")
    
    # 检查是否为文件
    is_file = os.path.isfile(test_path)
    print(f"是文件: {is_file}")
    
    # 检查是否为目录
    is_dir = os.path.isdir(test_path)
    print(f"是目录: {is_dir}")
    
    # 获取绝对路径
    abs_path = os.path.abspath(test_path)
    print(f"绝对路径: {abs_path}")
    
    # 获取规范化路径
    norm_path = os.path.normpath("some/path/../to/file")
    print(f"规范化路径: {norm_path}")
    
    # 路径分割
    dir_name, base_name = os.path.split(abs_path)
    print(f"目录名: {dir_name}")
    print(f"文件名: {base_name}")
    
    # 分离文件扩展名
    name, ext = os.path.splitext(base_name)
    print(f"文件名(不含扩展名): {name}")
    print(f"扩展名: {ext}")
    
    # 路径连接
    joined_path = os.path.join("parent", "child", "file.txt")
    print(f"连接的路径: {joined_path}")
    
    # 清理测试文件
    os.remove(test_path)

# 运行示例
path_operations_demo()
```

## 6. 环境变量操作

```python
import os

def environment_variables_demo():
    # 获取所有环境变量
    print("所有环境变量:")
    for key, value in os.environ.items():
        print(f"{key}: {value}")
        # 只打印前5个环境变量
        if len(list(os.environ.keys())[:list(os.environ.keys()).index(key)+1]) >= 5:
            break
    
    # 获取特定环境变量
    path_var = os.environ.get('PATH')
    print(f"\nPATH环境变量 (前100个字符): {path_var[:100]}...")
    
    # 设置环境变量（仅对当前进程有效）
    os.environ['MY_CUSTOM_VAR'] = 'custom_value'
    print(f"\n自定义环境变量: {os.environ.get('MY_CUSTOM_VAR')}")
    
    # 删除环境变量
    if 'MY_CUSTOM_VAR' in os.environ:
        del os.environ['MY_CUSTOM_VAR']
        print(f"删除后，自定义环境变量存在: {'MY_CUSTOM_VAR' in os.environ}")

# 运行示例
environment_variables_demo()
```

## 7. 进程管理

### 7.1 执行系统命令

```python
import os

def process_management_demo():
    # 获取当前进程ID
    pid = os.getpid()
    print(f"当前进程ID: {pid}")
    
    # 获取父进程ID
    ppid = os.getppid()
    print(f"父进程ID: {ppid}")
    
    # 在Windows上执行dir命令，在Unix上执行ls命令
    if os.name == 'nt':  # Windows
        command = 'dir'
    else:  # Unix/Linux
        command = 'ls -la'
    
    print(f"\n执行命令: {command}")
    # 使用os.system执行命令
    exit_code = os.system(command)
    print(f"命令退出码: {exit_code}")
    
    # 使用os.popen获取命令输出
    with os.popen(command) as pipe:
        output = pipe.read()
    print(f"\n命令输出 (前200个字符):\n{output[:200]}...")

# 运行示例
process_management_demo()
```

### 7.2 文件描述符和文件操作

```python
import os

def file_descriptor_demo():
    # 创建测试文件
    test_file = "fd_test.txt"
    
    # 使用低级别文件描述符操作文件
    # 打开文件（O_WRONLY = 只写模式，O_CREAT = 如果文件不存在则创建）
    flags = os.O_WRONLY | os.O_CREAT
    fd = os.open(test_file, flags)
    
    # 写入数据
    os.write(fd, b"Hello, using file descriptor!")
    
    # 关闭文件描述符
    os.close(fd)
    
    # 重新打开文件进行读取
    fd = os.open(test_file, os.O_RDONLY)
    
    # 读取数据
    data = os.read(fd, 100)  # 读取最多100个字节
    print(f"读取的数据: {data.decode('utf-8')}")
    
    # 关闭文件描述符
    os.close(fd)
    
    # 删除测试文件
    os.remove(test_file)

# 运行示例
file_descriptor_demo()
```

## 8. 高级应用示例

### 8.1 递归遍历目录树

```python
import os

def traverse_directory(directory):
    """递归遍历目录树"""
    print(f"\n遍历目录: {directory}")
    
    try:
        # 使用os.walk遍历目录树
        for root, dirs, files in os.walk(directory):
            print(f"\n当前目录: {root}")
            
            # 打印子目录
            print(f"子目录: {dirs}")
            
            # 打印文件
            print(f"文件: {files}")
            
            # 只遍历两层目录
            if root.count(os.sep) >= directory.count(os.sep) + 1:
                dirs[:] = []  # 清空dirs列表，停止进一步递归
    except Exception as e:
        print(f"遍历目录时出错: {e}")

# 运行示例
traverse_directory('.')
```

### 8.2 批量文件重命名

```python
import os
import re

def batch_rename(directory, pattern, replacement):
    """批量重命名文件"""
    print(f"\n批量重命名目录: {directory}")
    print(f"查找模式: {pattern}")
    print(f"替换为: {replacement}")
    
    renamed_count = 0
    
    try:
        # 创建正则表达式模式
        regex = re.compile(pattern)
        
        # 遍历目录中的文件
        for filename in os.listdir(directory):
            # 检查是否为文件
            if os.path.isfile(os.path.join(directory, filename)):
                # 应用替换
                new_name = regex.sub(replacement, filename)
                
                # 如果文件名发生变化，则重命名
                if new_name != filename:
                    old_path = os.path.join(directory, filename)
                    new_path = os.path.join(directory, new_name)
                    
                    # 确保新文件名不存在
                    counter = 1
                    base, ext = os.path.splitext(new_path)
                    while os.path.exists(new_path):
                        new_path = f"{base}_{counter}{ext}"
                        counter += 1
                    
                    # 执行重命名
                    os.rename(old_path, new_path)
                    print(f"重命名: {filename} -> {os.path.basename(new_path)}")
                    renamed_count += 1
    except Exception as e:
        print(f"批量重命名时出错: {e}")
    
    print(f"\n重命名完成，共重命名 {renamed_count} 个文件")

# 运行示例（在实际使用时取消注释并修改参数）
# 创建一些测试文件
# for i in range(5):
#     with open(f"test_{i}.txt", 'w') as f:
#         f.write(f"Test file {i}")

# 重命名示例
# batch_rename('.', r'test_', 'document_')
```

### 8.3 监控文件和目录变化

```python
import os
import time

def monitor_directory(directory, interval=2):
    """监控目录变化（简单实现）"""
    print(f"开始监控目录: {directory}")
    print(f"按 Ctrl+C 停止监控")
    
    # 初始状态
    previous_state = {}
    
    # 获取目录状态
    def get_directory_state(path):
        state = {}
        for root, dirs, files in os.walk(path):
            for name in files:
                filepath = os.path.join(root, name)
                try:
                    # 获取文件的修改时间和大小
                    stat = os.stat(filepath)
                    state[filepath] = (stat.st_mtime, stat.st_size)
                except Exception as e:
                    print(f"无法访问文件 {filepath}: {e}")
        return state
    
    # 初始扫描
    previous_state = get_directory_state(directory)
    
    try:
        while True:
            # 等待一段时间
            time.sleep(interval)
            
            # 新状态
            current_state = get_directory_state(directory)
            
            # 检查新增的文件
            new_files = set(current_state.keys()) - set(previous_state.keys())
            for file in new_files:
                print(f"[新增] {file}")
            
            # 检查删除的文件
            deleted_files = set(previous_state.keys()) - set(current_state.keys())
            for file in deleted_files:
                print(f"[删除] {file}")
            
            # 检查修改的文件
            modified_files = []
            for file in set(previous_state.keys()) & set(current_state.keys()):
                if previous_state[file] != current_state[file]:
                    modified_files.append(file)
            for file in modified_files:
                print(f"[修改] {file}")
            
            # 更新状态
            previous_state = current_state
    
    except KeyboardInterrupt:
        print("\n监控停止")

# 运行示例（在实际使用时取消注释）
# monitor_directory('.')
```

## 9. 注意事项和最佳实践

1. **跨平台兼容性**：
   - 使用os.path.join()而不是硬编码路径分隔符
   - 使用os.path.exists()、os.path.isfile()等函数进行路径检查
   - 注意Windows和Unix/Linux系统的差异

2. **错误处理**：
   - 文件操作可能抛出OSError等异常，务必使用try-except捕获
   - 使用os.path.exists()检查路径是否存在后再操作
   - 处理权限错误和资源不可用的情况

3. **安全性**：
   - 避免直接拼接用户输入到文件路径中（防止路径遍历攻击）
   - 使用os.path.normpath()规范化路径
   - 对用户输入进行验证和清理

4. **性能考量**：
   - 使用os.scandir()代替os.listdir()获取目录内容（更高效）
   - 对于大文件，使用文件描述符级别的操作
   - 避免在循环中重复获取相同的路径信息

5. **资源管理**：
   - 确保所有打开的文件和文件描述符都被正确关闭
   - 使用with语句管理文件资源
   - 避免创建过多的临时文件

## 10. 总结

os模块是Python与操作系统交互的强大工具，提供了丰富的函数用于文件操作、目录管理、进程控制和环境变量访问等任务。通过合理使用os模块，Python程序可以实现与操作系统的紧密集成，执行各种系统级任务。

主要优势包括：
- 跨平台兼容性，使代码可以在不同操作系统上运行
- 强大的文件和目录操作功能
- 进程管理和系统命令执行能力
- 环境变量和系统配置访问

在实际应用中，os模块通常与其他模块（如shutil、pathlib等）结合使用，以实现更复杂的文件和系统操作。对于需要与操作系统交互的Python程序，os模块是一个不可或缺的工具。