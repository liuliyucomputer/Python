#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
subprocess模块 - 子进程管理

subprocess模块允许在Python脚本中创建新的进程，连接到它们的输入/输出/错误管道，并获取它们的返回码。

主要功能包括：
- 执行外部命令和程序
- 连接到进程的标准输入、输出和错误
- 获取进程的返回码
- 处理进程间通信
- 支持多种执行模式（同步/异步）

使用场景：
- 执行系统命令和脚本
- 管理子进程的生命周期
- 与外部程序进行交互
- 构建命令行工具和自动化脚本

官方文档：https://docs.python.org/3/library/subprocess.html
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
print("提供了更安全、更灵活的方式执行外部命令")
print("替代了旧的os.system(), os.spawn*()等函数")
print("适合执行系统命令和与外部程序交互")

# ===========================
# 2. 基本用法：run()函数
# ===========================
print("\n" + "=" * 50)
print("2. 基本用法：run()函数")
print("=" * 50)

# 执行简单命令
print("执行简单命令 'dir' (Windows)")
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print(f"返回码: {result.returncode}")
print(f"标准输出:\n{result.stdout}")
print(f"标准错误:\n{result.stderr}")

# 执行带有参数的命令
print("\n执行带有参数的命令 'echo Hello World'")
result = subprocess.run(["echo", "Hello", "World"], shell=True, capture_output=True, text=True)
print(f"返回码: {result.returncode}")
print(f"输出: {result.stdout.strip()}")

# 检查命令执行结果
print("\n检查命令执行结果")
try:
    # 执行不存在的命令，会抛出异常
    subprocess.run(["nonexistent_command"], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    print(f"命令执行失败: {e}")
    print(f"返回码: {e.returncode}")
    print(f"错误信息: {e.stderr}")

# ===========================
# 3. 输入/输出处理
# ===========================
print("\n" + "=" * 50)
print("3. 输入/输出处理")
print("=" * 50)

# 捕获标准输出
print("捕获标准输出")
result = subprocess.run(["echo", "Hello Python"], capture_output=True, text=True)
print(f"输出: {result.stdout.strip()}")

# 捕获标准错误
print("\n捕获标准错误")
result = subprocess.run(["dir", "nonexistent_file"], shell=True, capture_output=True, text=True)
print(f"错误信息: {result.stderr.strip()}")

# 将输出重定向到文件
print("\n将输出重定向到文件")
with open("output.txt", "w") as f:
    subprocess.run(["echo", "写入文件的内容"], stdout=f, text=True)

# 读取输出文件
with open("output.txt", "r") as f:
    content = f.read()
    print(f"文件内容: {content.strip()}")

# 清理临时文件
os.remove("output.txt")

# 向子进程发送输入
print("\n向子进程发送输入")
result = subprocess.run(
    ["grep", "Python"], 
    input="Hello\nPython\nWorld", 
    capture_output=True, 
    text=True
)
print(f"匹配结果: {result.stdout.strip()}")

# ===========================
# 4. Popen类 - 高级用法
# ===========================
print("\n" + "=" * 50)
print("4. Popen类 - 高级用法")
print("=" * 50)

# 基本Popen用法
print("基本Popen用法")
process = subprocess.Popen(
    ["echo", "Popen示例"], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    text=True
)

# 获取输出
stdout, stderr = process.communicate()
print(f"返回码: {process.returncode}")
print(f"输出: {stdout.strip()}")

# 实时读取输出
print("\n实时读取输出")
process = subprocess.Popen(
    ["ping", "www.baidu.com", "-n", "3"], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    text=True
)

# 实时读取输出行
print("Ping结果:")
while True:
    line = process.stdout.readline()
    if not line:
        break
    print(f"  {line.strip()}")

# 等待进程完成
process.wait()
print(f"返回码: {process.returncode}")

# 异步执行命令
print("\n异步执行命令")
process = subprocess.Popen(
    ["timeout", "5", "ping", "www.baidu.com"], 
    shell=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE, 
    text=True
)

# 检查进程是否在运行
print(f"进程是否在运行: {process.poll() is None}")

# 等待进程完成
stdout, stderr = process.communicate()
print(f"返回码: {process.returncode}")
print(f"输出:\n{stdout}")

# ===========================
# 5. 环境变量
# ===========================
print("\n" + "=" * 50)
print("5. 环境变量")
print("=" * 50)

# 继承父进程的环境变量
print("继承父进程的环境变量")
result = subprocess.run(["echo", "%PATH%"], shell=True, capture_output=True, text=True)
print(f"PATH环境变量前100个字符: {result.stdout[:100]}...")

# 设置自定义环境变量
print("\n设置自定义环境变量")
env = os.environ.copy()
env["MY_VARIABLE"] = "Hello from custom environment"

result = subprocess.run(
    ["echo", "%MY_VARIABLE%"], 
    shell=True, 
    env=env, 
    capture_output=True, 
    text=True
)
print(f"自定义环境变量值: {result.stdout.strip()}")

# ===========================
# 6. 工作目录
# ===========================
print("\n" + "=" * 50)
print("6. 工作目录")
print("=" * 50)

# 获取当前工作目录
current_dir = os.getcwd()
print(f"当前工作目录: {current_dir}")

# 在指定目录执行命令
print("\n在指定目录执行命令")
result = subprocess.run(
    ["dir"], 
    shell=True, 
    cwd="C:/", 
    capture_output=True, 
    text=True
)
print(f"C:/目录内容前100个字符: {result.stdout[:100]}...")

# ===========================
# 7. 高级功能
# ===========================
print("\n" + "=" * 50)
print("7. 高级功能")
print("=" * 50)

# 管道通信
print("管道通信")
# 示例：ls | grep .py
process1 = subprocess.Popen(
    ["dir", "/B"], 
    shell=True, 
    stdout=subprocess.PIPE, 
    text=True
)

process2 = subprocess.Popen(
    ["findstr", ".py"], 
    stdin=process1.stdout, 
    stdout=subprocess.PIPE, 
    text=True
)

# 关闭process1的stdout，避免死锁
process1.stdout.close()

# 获取结果
output, _ = process2.communicate()
print(f"Python文件: {output.strip()}")

# 超时处理
print("\n超时处理")
try:
    result = subprocess.run(
        ["ping", "www.baidu.com", "-n", "10"], 
        shell=True, 
        capture_output=True, 
        text=True, 
        timeout=3
    )
    print(f"输出: {result.stdout.strip()}")
except subprocess.TimeoutExpired as e:
    print(f"命令执行超时: {e}")
    print(f"已获取的输出: {e.stdout.strip()}")

# ===========================
# 8. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("8. 实际应用示例")
print("=" * 50)

# 示例1: 执行系统命令并获取结果
def run_command(cmd, shell=False):
    """执行系统命令并返回结果"""
    try:
        result = subprocess.run(
            cmd, 
            shell=shell, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return {
            "success": True,
            "output": result.stdout.strip(),
            "error": ""
        }
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "output": e.stdout.strip(),
            "error": e.stderr.strip()
        }

# 演示示例1
print("示例1: 执行系统命令")
result = run_command(["echo", "测试命令执行"])
print(f"结果: {result}")

# 示例2: 批量重命名文件
def batch_rename_files(directory, old_ext, new_ext):
    """批量重命名文件扩展名"""
    try:
        # 切换到目标目录
        original_dir = os.getcwd()
        os.chdir(directory)
        
        # 执行重命名命令
        if sys.platform.startswith('win'):
            # Windows命令
            cmd = f"ren *{old_ext} *{new_ext}"
        else:
            # Linux/macOS命令
            cmd = f"rename 's/{old_ext}$/{new_ext}/' *{old_ext}"
        
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=True
        )
        
        # 恢复原工作目录
        os.chdir(original_dir)
        
        return {
            "success": True,
            "message": f"成功将所有.{old_ext}文件重命名为.{new_ext}"
        }
    except Exception as e:
        # 恢复原工作目录
        os.chdir(original_dir)
        return {
            "success": False,
            "message": f"重命名失败: {str(e)}"
        }

# 示例3: 检查网络连接
def check_network_connection(host="www.baidu.com", timeout=5):
    """检查网络连接"""
    try:
        if sys.platform.startswith('win'):
            # Windows ping命令
            cmd = ["ping", host, "-n", "1", "-w", str(timeout * 1000)]
        else:
            # Linux/macOS ping命令
            cmd = ["ping", host, "-c", "1", "-W", str(timeout)]
        
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return True
    except:
        return False

# 演示示例3
print("\n示例3: 检查网络连接")
if check_network_connection():
    print("网络连接正常")
else:
    print("网络连接失败")

# 示例4: 备份文件
def backup_file(file_path):
    """备份文件"""
    backup_path = f"{file_path}.bak"
    try:
        if sys.platform.startswith('win'):
            # Windows复制命令
            cmd = ["copy", file_path, backup_path]
        else:
            # Linux/macOS复制命令
            cmd = ["cp", file_path, backup_path]
        
        subprocess.run(
            cmd, 
            shell=True, 
            check=True
        )
        return {
            "success": True,
            "backup_path": backup_path
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"备份失败: {str(e)}"
        }

# ===========================
# 9. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("9. 最佳实践和注意事项")
print("=" * 50)

print("1. 安全性")
print("   - 避免使用shell=True，特别是当命令包含用户输入时")
print("   - 恶意用户可能通过shell注入攻击系统")
print("   - 当必须使用shell=True时，确保命令不包含用户输入")

print("\n2. 避免死锁")
print("   - 当同时捕获stdout和stderr时，使用communicate()而不是直接读取")
print("   - 直接读取可能导致缓冲区满而死锁")
print("   - communicate()会安全地处理输入和输出")

print("\n3. 错误处理")
print("   - 使用check=True参数来检查命令执行结果")
print("   - 使用try-except捕获CalledProcessError异常")
print("   - 始终检查返回码和错误信息")

print("\n4. 跨平台兼容性")
print("   - 不同操作系统的命令可能不同")
print("   - 使用sys.platform检查当前操作系统")
print("   - 为不同平台提供不同的命令实现")

print("\n5. 资源管理")
print("   - 使用Popen时，确保正确关闭文件描述符")
print("   - 使用with语句或手动关闭文件对象")
print("   - 避免创建过多的子进程")

print("\n6. 性能考虑")
print("   - 子进程创建和通信会有性能开销")
print("   - 避免在循环中频繁创建子进程")
print("   - 考虑使用线程或异步I/O代替子进程")

# ===========================
# 10. 总结
# ===========================
print("\n" + "=" * 50)
print("10. 总结")
print("=" * 50)
print("subprocess模块是Python中用于管理子进程的强大工具")
print("提供了简单的run()函数和灵活的Popen类")

print("\n主要功能:")
print("- 执行外部命令和程序")
print("- 管理子进程的输入和输出")
print("- 设置环境变量和工作目录")
print("- 处理命令执行错误和超时")
print("- 支持进程间通信")

print("\n应用场景:")
print("- 执行系统命令和脚本")
print("- 管理外部程序")
print("- 构建命令行工具")
print("- 自动化系统管理任务")
print("- 与其他语言编写的程序交互")

print("\n使用subprocess模块时，务必注意安全性和跨平台兼容性")
print("遵循最佳实践，避免常见的陷阱")
