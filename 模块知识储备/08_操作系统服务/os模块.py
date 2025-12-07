#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
os模块 - 操作系统接口

os模块提供了与操作系统交互的功能，包括文件系统操作、环境变量、进程管理等。
它是Python中与操作系统交互的核心模块之一。

主要功能包括：
- 文件和目录操作
- 路径操作
- 环境变量
- 进程管理
- 权限管理
- 系统信息获取
"""

import os
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. os模块基本介绍")
print("=" * 50)
print("os模块提供了与操作系统交互的功能")
print(f"当前操作系统: {os.name}")
print(f"当前工作目录: {os.getcwd()}")

# ===========================
# 2. 路径操作
# ===========================
print("\n" + "=" * 50)
print("2. 路径操作")
print("=" * 50)

# 获取当前目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 创建路径
path = os.path.join(current_dir, "test", "subdir")
print(f"创建的路径: {path}")

# 检查路径是否存在
print(f"路径是否存在: {os.path.exists(path)}")

# 创建目录（递归创建）
os.makedirs(path, exist_ok=True)
print(f"创建目录后，路径是否存在: {os.path.exists(path)}")

# 获取路径的各个部分
print(f"路径的目录部分: {os.path.dirname(path)}")
print(f"路径的文件名部分: {os.path.basename(path)}")
print(f"路径的绝对路径: {os.path.abspath(path)}")

# 检查是否是目录或文件
print(f"是否是目录: {os.path.isdir(path)}")
print(f"是否是文件: {os.path.isfile(path)}")

# 获取文件大小
# 创建一个测试文件
with open(os.path.join(path, "test.txt"), "w") as f:
    f.write("Hello, os module!")

file_path = os.path.join(path, "test.txt")
print(f"文件大小: {os.path.getsize(file_path)} 字节")

# 获取文件的修改时间
import time
mod_time = os.path.getmtime(file_path)
print(f"文件修改时间: {time.ctime(mod_time)}")

# ===========================
# 3. 文件和目录操作
# ===========================
print("\n" + "=" * 50)
print("3. 文件和目录操作")
print("=" * 50)

# 列出目录内容
print(f"目录内容: {os.listdir(path)}")

# 重命名文件
new_file_path = os.path.join(path, "renamed_test.txt")
os.rename(file_path, new_file_path)
print(f"重命名后文件是否存在: {os.path.exists(new_file_path)}")

# 复制文件（注意：os模块没有直接的复制函数，需要使用shutil模块）

# 删除文件
os.remove(new_file_path)
print(f"删除文件后，文件是否存在: {os.path.exists(new_file_path)}")

# 删除目录
os.rmdir(os.path.join(path, "subdir"))  # 只能删除空目录
print(f"删除子目录后，子目录是否存在: {os.path.exists(os.path.join(path, 'subdir'))}")

# 递归删除目录（包括内容）
os.rmdir(path)  # 现在path是空的，可以删除
print(f"删除目录后，目录是否存在: {os.path.exists(path)}")

# ===========================
# 4. 环境变量
# ===========================
print("\n" + "=" * 50)
print("4. 环境变量")
print("=" * 50)

# 获取所有环境变量
print("环境变量示例:")
for key, value in os.environ.items():
    if key in ["PATH", "HOME", "USER", "TEMP"]:
        print(f"{key}: {value}")

# 获取特定环境变量
path_env = os.environ.get("PATH")
print(f"\nPATH环境变量长度: {len(path_env)} 字符")

# 设置环境变量（临时，只在当前进程有效）
os.environ["TEST_VAR"] = "test_value"
print(f"设置的环境变量TEST_VAR: {os.environ.get('TEST_VAR')}")

# ===========================
# 5. 进程管理
# ===========================
print("\n" + "=" * 50)
print("5. 进程管理")
print("=" * 50)

# 获取当前进程ID
print(f"当前进程ID: {os.getpid()}")

# 获取父进程ID
print(f"父进程ID: {os.getppid()}")

# 执行系统命令
print("\n执行系统命令示例:")
if os.name == "nt":  # Windows
    # 使用os.system执行命令
    result = os.system("dir /w")
    print(f"命令执行结果: {result}")
else:  # Linux/macOS
    result = os.system("ls -la")
    print(f"命令执行结果: {result}")

# 使用os.popen读取命令输出
print("\n使用os.popen读取命令输出:")
if os.name == "nt":
    with os.popen("echo %PATH% | findstr /i python") as pipe:
        output = pipe.read()
        print(f"Python路径: {output.strip()}")
else:
    with os.popen("echo $PATH | grep -i python") as pipe:
        output = pipe.read()
        print(f"Python路径: {output.strip()}")

# ===========================
# 6. 权限管理
# ===========================
print("\n" + "=" * 50)
print("6. 权限管理")
print("=" * 50)

# 创建一个测试文件
with open("test_perm.txt", "w") as f:
    f.write("Test file for permissions")

# 获取文件权限（Windows上表现不同）
if os.name != "nt":  # 非Windows系统
    import stat
    file_stats = os.stat("test_perm.txt")
    file_mode = file_stats.st_mode
    print(f"文件权限: {oct(file_mode)[-3:]}")
    
    # 修改文件权限
    os.chmod("test_perm.txt", stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    file_stats = os.stat("test_perm.txt")
    print(f"修改后文件权限: {oct(file_stats.st_mode)[-3:]}")
else:
    print("Windows系统权限管理与Unix不同，使用ACL")

# 删除测试文件
os.remove("test_perm.txt")

# ===========================
# 7. 系统信息获取
# ===========================
print("\n" + "=" * 50)
print("7. 系统信息获取")
print("=" * 50)

# 获取系统相关信息
print(f"操作系统名称: {os.name}")
print(f"系统分隔符: {os.sep}")
print(f"路径分隔符: {os.pathsep}")
print(f"行终止符: {repr(os.linesep)}")

# 获取登录用户名
if os.name == "nt":
    print(f"登录用户名: {os.environ.get('USERNAME', 'Unknown')}")
else:
    print(f"登录用户名: {os.environ.get('USER', 'Unknown')}")

# ===========================
# 8. 高级功能
# ===========================
print("\n" + "=" * 50)
print("8. 高级功能")
print("=" * 50)

# 工作目录切换
original_dir = os.getcwd()
os.chdir(os.path.dirname(os.getcwd()))  # 切换到父目录
print(f"切换后工作目录: {os.getcwd()}")
os.chdir(original_dir)  # 切换回原目录
print(f"切换回原目录: {os.getcwd()}")

# 符号链接（Windows需要管理员权限）
try:
    if os.name != "nt" or (sys.platform == "win32" and hasattr(os, "symlink")):
        with open("target.txt", "w") as f:
            f.write("Target file for symlink")
        
        # 创建符号链接
        os.symlink("target.txt", "link.txt")
        print(f"符号链接是否存在: {os.path.exists('link.txt')}")
        
        # 读取符号链接内容
        with open("link.txt", "r") as f:
            content = f.read()
            print(f"符号链接指向的文件内容: {content}")
        
        # 删除符号链接
        os.unlink("link.txt")
        os.remove("target.txt")
except Exception as e:
    print(f"创建符号链接失败: {e}")

# ===========================
# 9. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

# 示例1: 遍历目录树
def traverse_directory(directory):
    """遍历目录树并打印文件信息"""
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            print(f"{subindent}{file} ({size} bytes)")

# 遍历当前目录的前两层
print("遍历当前目录结构:")
try:
    traverse_directory(".")
except Exception as e:
    print(f"遍历目录失败: {e}")

# 示例2: 批量重命名文件
def batch_rename(directory, old_ext, new_ext):
    """批量重命名文件扩展名"""
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(old_ext):
            old_path = os.path.join(directory, filename)
            new_filename = filename.replace(old_ext, new_ext)
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            count += 1
            print(f"重命名: {old_path} -> {new_path}")
    print(f"共重命名 {count} 个文件")

# 示例3: 创建临时目录并操作
def temp_directory_example():
    """创建临时目录并进行操作"""
    # 创建临时目录
    temp_dir = os.path.join(os.getcwd(), "temp_example")
    os.makedirs(temp_dir, exist_ok=True)
    
    # 创建测试文件
    for i in range(3):
        file_path = os.path.join(temp_dir, f"test_{i}.txt")
        with open(file_path, "w") as f:
            f.write(f"Test content {i}")
    
    print(f"在临时目录 {temp_dir} 中创建了3个测试文件")
    
    # 清理临时目录
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        os.remove(file_path)
    os.rmdir(temp_dir)
    print(f"临时目录 {temp_dir} 已清理")

temp_directory_example()

# ===========================
# 10. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("10. 最佳实践和注意事项")
print("=" * 50)

print("1. 使用os.path.join()构建路径，避免硬编码路径分隔符")
print("2. 始终检查文件/目录是否存在再进行操作")
print("3. 使用try-except处理可能的异常")
print("4. 注意跨平台兼容性，特别是Windows和Unix系统的差异")
print("5. 操作文件/目录后及时清理资源")
print("6. 谨慎使用递归删除操作")
print("7. 避免使用os.system()执行外部命令，优先使用subprocess模块")
print("8. 处理大文件时要考虑内存限制")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("os模块是Python与操作系统交互的核心模块，提供了丰富的功能：")
print("- 文件和目录操作")
print("- 路径管理")
print("- 环境变量处理")
print("- 进程管理")
print("- 系统信息获取")
print("- 权限管理")
print("\n熟练掌握os模块可以让Python程序更好地与操作系统交互，")
print("实现更多高级功能")
