# Python os模块详解

import os
import sys

# 1. 模块概述
print("=== 1. os模块概述 ===")
print("os模块提供了与操作系统交互的功能，包括文件和目录操作、环境变量访问、进程管理等。")
print("该模块的主要特点：")
print("- 提供跨平台的操作系统接口")
print("- 支持文件和目录的创建、删除、重命名等操作")
print("- 提供环境变量访问和管理功能")
print("- 支持进程管理和系统命令执行")
print("- 提供文件权限管理功能")
print()

# 2. 操作系统相关信息
print("=== 2. 操作系统相关信息 ===")

# 操作系统名称
print(f"os.name = {os.name}")  # 'posix', 'nt', 'java'等

# 操作系统特定的终止信号
print(f"os.sep = {repr(os.sep)}")  # 路径分隔符
print(f"os.altsep = {repr(os.altsep)}")  # 备用路径分隔符
print(f"os.extsep = {repr(os.extsep)}")  # 文件扩展名分隔符
print(f"os.pathsep = {repr(os.pathsep)}")  # 路径列表分隔符
print(f"os.linesep = {repr(os.linesep)}")  # 行分隔符

# 系统类型
print(f"sys.platform = {sys.platform}")  # 'win32', 'linux', 'darwin'等

# 环境变量
print(f"os.environ.get('PATH')[:50]... = {os.environ.get('PATH')[:50]}...")  # 环境变量PATH
print(f"os.environ.get('HOME') = {os.environ.get('HOME')}")  # 主目录
print()

# 3. 工作目录操作
print("=== 3. 工作目录操作 ===")

# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 改变工作目录
try:
    os.chdir('..')
    print(f"改变后工作目录: {os.getcwd()}")
    # 改回原目录
    os.chdir(current_dir)
    print(f"改回原工作目录: {os.getcwd()}")
except FileNotFoundError as e:
    print(f"改变目录失败: {e}")

# 创建目录
print("\n创建目录操作：")
test_dir = 'test_directory'
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"创建目录: {test_dir}")

# 创建多级目录
nested_dir = 'level1/level2/level3'
if not os.path.exists(nested_dir):
    os.makedirs(nested_dir)
    print(f"创建多级目录: {nested_dir}")

# 删除目录
if os.path.exists(test_dir):
    os.rmdir(test_dir)
    print(f"删除目录: {test_dir}")

# 删除多级目录
if os.path.exists(nested_dir):
    os.removedirs(nested_dir)
    print(f"删除多级目录: {nested_dir}")
print()

# 4. 文件操作
print("=== 4. 文件操作 ===")

# 创建测试文件
test_file = 'test.txt'
with open(test_file, 'w') as f:
    f.write('Hello, os module!')
    print(f"创建文件: {test_file}")

# 重命名文件
new_name = 'renamed_test.txt'
os.rename(test_file, new_name)
print(f"重命名文件: {test_file} -> {new_name}")

# 复制文件（注意：os模块没有直接的copy函数，需要使用shutil模块）
import shutil
copy_name = 'copied_test.txt'
shutil.copy(new_name, copy_name)
print(f"复制文件: {new_name} -> {copy_name}")

# 删除文件
if os.path.exists(new_name):
    os.remove(new_name)
    print(f"删除文件: {new_name}")

if os.path.exists(copy_name):
    os.remove(copy_name)
    print(f"删除文件: {copy_name}")
print()

# 5. 目录内容操作
print("=== 5. 目录内容操作 ===")

# 获取目录内容
print(f"当前目录内容: {os.listdir('.')}")

# 遍历目录树
print("\n遍历当前目录树：")
for root, dirs, files in os.walk('.'):
    level = root.replace('.', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files[:3]:  # 只显示前3个文件
        print(f"{subindent}{file}")
    if len(files) > 3:
        print(f"{subindent}... 等{len(files)}个文件")
    break  # 只显示一级目录
print()

# 6. 文件属性操作
print("=== 6. 文件属性操作 ===")

# 创建测试文件
test_file = 'test_attr.txt'
with open(test_file, 'w') as f:
    f.write('Test file for attributes')

# 获取文件属性
print(f"文件存在性: {os.path.exists(test_file)}")
print(f"是文件: {os.path.isfile(test_file)}")
print(f"是目录: {os.path.isdir(test_file)}")
print(f"文件大小: {os.path.getsize(test_file)} bytes")

# 获取文件时间
import time
print(f"创建时间: {time.ctime(os.path.getctime(test_file))}")
print(f"修改时间: {time.ctime(os.path.getmtime(test_file))}")
print(f"访问时间: {time.ctime(os.path.getatime(test_file))}")

# 删除测试文件
os.remove(test_file)
print(f"删除测试文件: {test_file}")
print()

# 7. 文件权限管理
print("=== 7. 文件权限管理 ===")

# 创建测试文件
test_file = 'test_perm.txt'
with open(test_file, 'w') as f:
    f.write('Test file for permissions')

# 获取文件权限
if os.name != 'nt':  # Windows不支持os.chmod
    try:
        mode = os.stat(test_file).st_mode
        print(f"文件权限: {oct(mode)[-3:]}")
        
        # 修改文件权限
        os.chmod(test_file, 0o755)  # rwxr-xr-x
        new_mode = os.stat(test_file).st_mode
        print(f"修改后权限: {oct(new_mode)[-3:]}")
    except Exception as e:
        print(f"权限操作失败: {e}")
else:
    print("Windows系统不支持os.chmod操作")

# 删除测试文件
os.remove(test_file)
print(f"删除测试文件: {test_file}")
print()

# 8. 环境变量操作
print("=== 8. 环境变量操作 ===")

# 获取环境变量
print(f"USER环境变量: {os.environ.get('USER')}")
print(f"USERNAME环境变量: {os.environ.get('USERNAME')}")
print(f"TEMP环境变量: {os.environ.get('TEMP')}")

# 设置环境变量
os.environ['MY_TEST_VAR'] = 'test_value'
print(f"设置的环境变量: {os.environ.get('MY_TEST_VAR')}")

# 删除环境变量
if 'MY_TEST_VAR' in os.environ:
    del os.environ['MY_TEST_VAR']
    print(f"删除环境变量MY_TEST_VAR后: {os.environ.get('MY_TEST_VAR')}")
print()

# 9. 系统命令执行
print("=== 9. 系统命令执行 ===")

# os.system() - 执行系统命令并返回退出状态
print("执行系统命令 'echo Hello World':")
status = os.system('echo Hello World')
print(f"命令退出状态: {status}")

# os.popen() - 执行系统命令并返回文件对象
print("\n执行系统命令 'dir'/'ls -la':")
if os.name == 'nt':
    cmd = 'dir'
else:
    cmd = 'ls -la'
    
try:
    with os.popen(cmd) as f:
        output = f.read()
        print(f"命令输出:\n{output[:500]}...")  # 只显示前500个字符
except Exception as e:
    print(f"命令执行失败: {e}")

# 注意：在Python 3.5+中，推荐使用subprocess模块替代os.system()和os.popen()
print("\n注意：在Python 3.5+中，推荐使用subprocess模块替代os.system()和os.popen()")
print()

# 10. 进程管理
print("=== 10. 进程管理 ===")

# 获取当前进程ID
print(f"当前进程ID: {os.getpid()}")

# 获取父进程ID
print(f"父进程ID: {os.getppid()}")

# 进程优先级（Windows和Unix有所不同）
try:
    if os.name == 'nt':
        print(f"进程优先级: {os.getpriority(os.PRIO_PROCESS, os.getpid())}")
    else:
        print(f"进程优先级: {os.nice(0)}")  # 获取当前nice值
except Exception as e:
    print(f"获取进程优先级失败: {e}")

# 终止进程
print("注意：os.kill()和os.abort()可以终止进程，但需谨慎使用")
print()

# 11. 路径操作
print("=== 11. 路径操作 ===")

# 获取当前工作目录
print(f"当前工作目录: {os.getcwd()}")

# 绝对路径
print(f"相对路径'..'的绝对路径: {os.path.abspath('..')}")

# 规范化路径
print(f"规范化路径'./dir/../file.txt': {os.path.normpath('./dir/../file.txt')}")

# 路径拆分
full_path = os.path.join(os.getcwd(), 'subdir', 'file.txt')
print(f"完整路径: {full_path}")
dir_name, base_name = os.path.split(full_path)
print(f"目录名: {dir_name}")
print(f"基名: {base_name}")

# 文件名和扩展名拆分
root, ext = os.path.splitext(base_name)
print(f"文件名: {root}")
print(f"扩展名: {ext}")

# 路径拼接
new_path = os.path.join('dir1', 'dir2', 'file.txt')
print(f"路径拼接: {new_path}")
print()

# 12. 文件描述符操作
print("=== 12. 文件描述符操作 ===")

# 创建测试文件
test_file = 'test_fd.txt'

# 使用os.open()打开文件
fd = os.open(test_file, os.O_WRONLY | os.O_CREAT)
print(f"文件描述符: {fd}")

# 使用文件描述符写入
os.write(fd, b'Test data written using os.write()')

# 关闭文件描述符
os.close(fd)
print("关闭文件描述符")

# 使用os.open()读取文件
fd = os.open(test_file, os.O_RDONLY)
data = os.read(fd, 100)
print(f"读取的数据: {data.decode()}")
os.close(fd)

# 删除测试文件
os.remove(test_file)
print(f"删除测试文件: {test_file}")
print()

# 13. 实际应用示例
print("=== 13. 实际应用示例 ===")

# 示例1：批量重命名文件
def batch_rename(directory, prefix, extension):
    """批量重命名指定目录下的文件"""
    if not os.path.exists(directory):
        print(f"目录不存在: {directory}")
        return
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print(f"找到 {len(files)} 个文件")
    
    for i, filename in enumerate(files):
        old_path = os.path.join(directory, filename)
        new_filename = f"{prefix}_{i+1}.{extension}"
        new_path = os.path.join(directory, new_filename)
        
        try:
            os.rename(old_path, new_path)
            print(f"重命名: {filename} -> {new_filename}")
        except Exception as e:
            print(f"重命名失败 {filename}: {e}")

# 创建测试目录和文件
test_dir = 'test_rename'
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    
    # 创建测试文件
    for i in range(3):
        with open(os.path.join(test_dir, f'file{i+1}.txt'), 'w') as f:
            f.write(f'Test content {i+1}')

print("批量重命名示例:")
batch_rename(test_dir, 'document', 'txt')

# 清理测试目录
for file in os.listdir(test_dir):
    os.remove(os.path.join(test_dir, file))
os.rmdir(test_dir)
print(f"清理测试目录: {test_dir}")

# 示例2：统计目录大小
def get_directory_size(directory):
    """计算目录大小"""
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

dir_size = get_directory_size('.')
print(f"\n当前目录大小: {dir_size} bytes = {dir_size / 1024:.2f} KB")

# 示例3：查找指定扩展名的文件
def find_files(directory, extension, recursive=True):
    """查找指定扩展名的文件"""
    found_files = []
    if recursive:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extension):
                    found_files.append(os.path.join(root, file))
    else:
        for file in os.listdir(directory):
            if file.endswith(extension) and os.path.isfile(os.path.join(directory, file)):
                found_files.append(os.path.join(directory, file))
    return found_files

py_files = find_files('.', '.py', recursive=False)[:5]  # 只找当前目录的前5个Python文件
print(f"\n当前目录下的Python文件: {py_files}")
print()

# 14. 安全注意事项
print("=== 14. 安全注意事项 ===")

print("1. 避免使用os.system()执行用户输入的命令，容易受到命令注入攻击")
print("   推荐使用subprocess模块并将命令参数化")

print("\n2. 路径处理时要注意路径遍历攻击")
print("   例如：用户输入 '../etc/passwd' 可能访问系统文件")

print("\n3. 文件权限管理要谨慎")
print("   避免将敏感文件设置为世界可写")

print("\n4. 环境变量操作可能影响系统安全")
print("   避免将敏感信息存储在环境变量中")

print("\n5. 进程管理功能要谨慎使用")
print("   os.kill()等函数可能导致系统不稳定")
print()

# 15. 最佳实践
print("=== 15. 最佳实践 ===")

print("1. 使用os.path模块处理路径，确保跨平台兼容性")
print("   path = os.path.join('dir', 'subdir', 'file.txt')")

print("\n2. 对于Python 3.4+，推荐使用pathlib模块进行面向对象的路径操作")
print("   from pathlib import Path")
print("   path = Path('dir') / 'subdir' / 'file.txt'")

print("\n3. 使用异常处理包装文件操作")
print("   try:")
print("       os.remove('file.txt')")
print("   except FileNotFoundError:")
print("       pass")

print("\n4. 在Python 3.5+中，使用subprocess模块替代os.system()和os.popen()")
print("   import subprocess")
print("   result = subprocess.run(['echo', 'Hello'], capture_output=True, text=True)")

print("\n5. 使用os.walk()遍历目录树时，注意处理符号链接")
print("   for root, dirs, files in os.walk(directory, followlinks=False):")

print("\n6. 避免硬编码路径分隔符")
print("   使用os.sep或os.path.join()替代'/或'\\'")
print()

# 16. 总结
print("=== 16. os模块总结 ===")
print("os模块是Python中与操作系统交互的核心模块，提供了丰富的功能。")
print("主要功能包括：")
print("- 文件和目录的创建、删除、重命名等操作")
print("- 工作目录管理")
print("- 文件属性和权限管理")
print("- 环境变量访问和管理")
print("- 进程管理")
print("- 系统命令执行")
print("- 路径操作")
print()
print("在Python 3.4+中，推荐使用pathlib模块进行路径操作，")
print("使用subprocess模块执行系统命令，这些模块提供了更现代、更安全的API。")
print()
print("os模块虽然功能强大，但使用时需要注意安全问题和跨平台兼容性。")
