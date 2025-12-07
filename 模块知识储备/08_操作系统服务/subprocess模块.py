#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subprocess模块 - 子进程管理

subprocess模块提供了创建和管理子进程的功能，允许Python程序执行外部命令、
获取命令输出、与进程进行交互等。

主要功能包括：
- 执行外部命令
- 捕获命令输出
- 重定向输入输出
- 创建管道进行进程间通信
- 管理进程的启动、等待和终止
"""

import subprocess
import os
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. subprocess模块基本介绍")
print("=" * 50)
print("subprocess模块用于创建和管理子进程")
print("它提供了比os.system()更强大、更灵活的功能")

# ===========================
# 2. 执行外部命令
# ===========================
print("\n" + "=" * 50)
print("2. 执行外部命令")
print("=" * 50)

# 使用run()函数执行命令（推荐）
print("演示使用subprocess.run()执行命令:")

# 简单命令执行
if sys.platform == "win32":  # Windows系统
    result = subprocess.run(["echo", "Hello, subprocess!"])
else:  # Linux/macOS系统
    result = subprocess.run(["echo", "Hello, subprocess!"])

print(f"命令执行结果: {result}")
print(f"返回码: {result.returncode}")
print(f"是否执行成功: {result.returncode == 0}")

# 执行带参数的命令
print("\n演示执行带参数的命令:")
try:
    if sys.platform == "win32":
        result = subprocess.run(["dir", "."], shell=True, capture_output=True, text=True)
    else:
        result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
    
    print(f"命令执行成功: {result.returncode == 0}")
    print(f"标准输出:\n{result.stdout}")
except Exception as e:
    print(f"执行命令失败: {e}")

# ===========================
# 3. 捕获命令输出
# ===========================
print("\n" + "=" * 50)
print("3. 捕获命令输出")
print("=" * 50)

# 使用capture_output参数捕获输出
print("演示捕获命令输出:")
try:
    if sys.platform == "win32":
        # Windows上使用ipconfig命令
        result = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True, timeout=5)
    else:
        # Linux/macOS上使用ifconfig命令
        result = subprocess.run(["ifconfig"], capture_output=True, text=True, timeout=5)
    
    print(f"命令执行成功: {result.returncode == 0}")
    
    # 只显示输出的前几行
    lines = result.stdout.split("\n")
    print(f"输出前10行:\n" + "\n".join(lines[:10]))
    if len(lines) > 10:
        print(f"... 共 {len(lines)} 行输出")
        
except subprocess.TimeoutExpired:
    print("命令执行超时")
except Exception as e:
    print(f"执行命令失败: {e}")

# ===========================
# 4. 输入输出重定向
# ===========================
print("\n" + "=" * 50)
print("4. 输入输出重定向")
print("=" * 50)

# 将输出重定向到文件
print("演示将命令输出重定向到文件:")
try:
    output_file = "subprocess_output.txt"
    
    if sys.platform == "win32":
        with open(output_file, "w") as f:
            subprocess.run(["dir", "."], shell=True, stdout=f, text=True)
    else:
        with open(output_file, "w") as f:
            subprocess.run(["ls", "-la"], stdout=f, text=True)
    
    print(f"命令输出已写入文件: {output_file}")
    
    # 读取文件内容
    with open(output_file, "r") as f:
        content = f.read()
        print(f"文件内容:\n{content}")
    
    # 删除测试文件
    os.remove(output_file)
    
except Exception as e:
    print(f"重定向输出失败: {e}")

# 将输入重定向到命令
print("\n演示将输入重定向到命令:")
try:
    # 使用echo命令发送输入到grep命令（Linux/macOS）
    # 或使用echo命令发送输入到findstr命令（Windows）
    if sys.platform == "win32":
        # Windows上没有直接的管道支持，需要使用shell=True
        result = subprocess.run(
            "echo Hello World | findstr World",
            shell=True,
            capture_output=True,
            text=True
        )
    else:
        # Linux/macOS上的管道示例
        grep_process = subprocess.Popen(
            ["grep", "World"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        output, _ = grep_process.communicate("Hello World\n")
        print(f"管道输出: {output.strip()}")
        
    if sys.platform == "win32":
        print(f"命令输出: {result.stdout.strip()}")
        
except Exception as e:
    print(f"输入重定向失败: {e}")

# ===========================
# 5. Popen类的使用
# ===========================
print("\n" + "=" * 50)
print("5. Popen类的使用")
print("=" * 50)

# Popen类提供了更底层的进程控制
print("演示使用Popen类:")
try:
    if sys.platform == "win32":
        # Windows上使用ping命令
        process = subprocess.Popen(
            ["ping", "-n", "3", "127.0.0.1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    else:
        # Linux/macOS上使用ping命令
        process = subprocess.Popen(
            ["ping", "-c", "3", "127.0.0.1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
    
    # 获取输出
    stdout, stderr = process.communicate(timeout=10)
    
    print(f"进程返回码: {process.returncode}")
    print(f"标准输出:\n{stdout}")
    if stderr:
        print(f"标准错误:\n{stderr}")
        
except subprocess.TimeoutExpired:
    process.kill()
    print("命令执行超时")
except Exception as e:
    print(f"执行命令失败: {e}")

# ===========================
# 6. 进程间通信（管道）
# ===========================
print("\n" + "=" * 50)
print("6. 进程间通信（管道）")
print("=" * 50)

print("演示使用管道进行进程间通信:")
try:
    if sys.platform == "win32":
        # Windows上使用shell管道
        cmd = "echo This is a test | findstr test"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(f"管道命令输出: {result.stdout.strip()}")
    else:
        # 创建第一个进程（生成输出）
        p1 = subprocess.Popen(["echo", "This is a test"], stdout=subprocess.PIPE)
        
        # 创建第二个进程（接收输入并处理）
        p2 = subprocess.Popen(["grep", "test"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
        
        # 关闭p1的stdout，因为p2已经不再需要它
        p1.stdout.close()
        
        # 获取最终输出
        output, _ = p2.communicate()
        print(f"管道命令输出: {output.strip()}")
        
except Exception as e:
    print(f"管道通信失败: {e}")

# ===========================
# 7. 超时控制
# ===========================
print("\n" + "=" * 50)
print("7. 超时控制")
print("=" * 50)

print("演示命令超时控制:")
try:
    if sys.platform == "win32":
        # Windows上使用ping命令，设置长时间超时
        result = subprocess.run(
            ["ping", "-n", "10", "127.0.0.1"],
            capture_output=True,
            text=True,
            timeout=2  # 设置2秒超时
        )
    else:
        # Linux/macOS上使用ping命令，设置长时间超时
        result = subprocess.run(
            ["ping", "-c", "10", "127.0.0.1"],
            capture_output=True,
            text=True,
            timeout=2  # 设置2秒超时
        )
    
    print(f"命令执行结果: {result}")
    
except subprocess.TimeoutExpired:
    print("命令执行超时，已自动终止")
except Exception as e:
    print(f"执行命令失败: {e}")

# ===========================
# 8. 高级功能
# ===========================
print("\n" + "=" * 50)
print("8. 高级功能")
print("=" * 50)

# 设置工作目录
print("演示设置命令工作目录:")
try:
    # 获取当前工作目录
    current_dir = os.getcwd()
    print(f"当前工作目录: {current_dir}")
    
    # 创建一个临时目录
    temp_dir = os.path.join(current_dir, "subprocess_test")
    os.makedirs(temp_dir, exist_ok=True)
    
    # 在临时目录中执行命令
    if sys.platform == "win32":
        result = subprocess.run(
            ["dir", "."],
            shell=True,
            cwd=temp_dir,
            capture_output=True,
            text=True
        )
    else:
        result = subprocess.run(
            ["ls", "-la"],
            cwd=temp_dir,
            capture_output=True,
            text=True
        )
    
    print(f"在临时目录中执行命令的输出:\n{result.stdout}")
    
    # 删除临时目录
    os.rmdir(temp_dir)
    
except Exception as e:
    print(f"设置工作目录失败: {e}")

# 设置环境变量
print("\n演示设置命令环境变量:")
try:
    # 创建自定义环境变量
    custom_env = os.environ.copy()
    custom_env["TEST_VAR"] = "test_value"
    
    if sys.platform == "win32":
        # Windows上查看环境变量
        result = subprocess.run(
            ["echo", "%TEST_VAR%"],
            shell=True,
            env=custom_env,
            capture_output=True,
            text=True
        )
    else:
        # Linux/macOS上查看环境变量
        result = subprocess.run(
            ["echo", "$TEST_VAR"],
            env=custom_env,
            capture_output=True,
            text=True
        )
    
    print(f"自定义环境变量值: {result.stdout.strip()}")
    
except Exception as e:
    print(f"设置环境变量失败: {e}")

# ===========================
# 9. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

# 示例1: 批量处理文件
def batch_convert_files(input_dir, output_dir, convert_func):
    """批量转换文件"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    files = os.listdir(input_dir)
    for file in files:
        input_path = os.path.join(input_dir, file)
        output_path = os.path.join(output_dir, file)
        convert_func(input_path, output_path)
        print(f"转换完成: {file}")

# 示例2: 执行shell脚本
def execute_shell_script(script_path, args=None):
    """执行shell脚本"""
    if not os.path.exists(script_path):
        print(f"脚本不存在: {script_path}")
        return False
    
    try:
        cmd = [script_path]
        if args:
            cmd.extend(args)
        
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"脚本执行成功")
        print(f"输出: {result.stdout}")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"脚本执行失败，返回码: {e.returncode}")
        print(f"错误输出: {e.stderr}")
        return False
    except Exception as e:
        print(f"执行脚本时出错: {e}")
        return False

# 示例3: 获取系统信息
def get_system_info():
    """获取系统信息"""
    print("获取系统信息:")
    
    try:
        if sys.platform == "win32":
            # Windows系统信息
            result = subprocess.run(["systeminfo"], capture_output=True, text=True, timeout=10)
            print(f"系统信息:\n{result.stdout[:500]}...")  # 只显示前500个字符
        else:
            # Linux/macOS系统信息
            result = subprocess.run(["uname", "-a"], capture_output=True, text=True)
            print(f"系统信息: {result.stdout.strip()}")
            
            # 获取CPU信息
            result = subprocess.run(["cat", "/proc/cpuinfo"], capture_output=True, text=True)
            print(f"CPU信息:\n{result.stdout[:500]}...")  # 只显示前500个字符
            
    except Exception as e:
        print(f"获取系统信息失败: {e}")

print("示例1: 批量处理文件")
print("示例2: 执行shell脚本")
get_system_info()  # 运行示例3

# 示例4: 使用subprocess实现命令行工具
def simple_grep(pattern, file_path):
    """简单的grep工具实现"""
    try:
        if sys.platform == "win32":
            # Windows上使用findstr
            result = subprocess.run(
                ["findstr", pattern, file_path],
                capture_output=True,
                text=True
            )
        else:
            # Linux/macOS上使用grep
            result = subprocess.run(
                ["grep", pattern, file_path],
                capture_output=True,
                text=True
            )
        
        if result.returncode == 0:
            print(f"找到匹配行:\n{result.stdout}")
        else:
            print(f"未找到匹配行")
            
    except Exception as e:
        print(f"执行grep失败: {e}")

# 测试simple_grep函数
with open("test_grep.txt", "w") as f:
    f.write("Line 1: This is a test\n")
    f.write("Line 2: Another line\n")
    f.write("Line 3: Test line again\n")

simple_grep("test", "test_grep.txt")
os.remove("test_grep.txt")

# ===========================
# 10. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("10. 最佳实践和注意事项")
print("=" * 50)

print("1. 优先使用subprocess.run()函数（Python 3.5+推荐）")
print("2. 使用列表形式传递命令参数，避免shell=True带来的安全风险")
print("3. 当必须使用shell=True时，避免将用户输入直接传递给命令")
print("4. 使用check=True参数自动检查命令执行结果")
print("5. 始终设置合理的超时时间，避免程序无限等待")
print("6. 使用capture_output=True捕获命令输出")
print("7. 使用text=True将输出作为文本而不是字节处理")
print("8. 对于复杂的进程管理，使用Popen类")
print("9. 确保正确关闭文件描述符，避免资源泄漏")
print("10. 考虑跨平台兼容性，不同系统的命令和参数可能不同")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("subprocess模块是Python中管理子进程的强大工具：")
print("- 可以执行外部命令并获取结果")
print("- 支持输入输出重定向和管道")
print("- 提供超时控制和错误处理")
print("- 支持环境变量和工作目录设置")
print("\n熟练掌握subprocess模块可以让Python程序与外部命令和工具进行交互，")
print("扩展Python程序的功能")
