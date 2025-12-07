#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sys模块 - Python解释器接口

sys模块提供了与Python解释器交互的功能，包括命令行参数、标准输入输出、
模块导入路径、Python解释器信息等。

主要功能包括：
- 命令行参数处理
- 标准输入输出控制
- 模块导入路径管理
- Python解释器信息获取
- 系统退出控制
- 内存管理相关功能
"""

import sys
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. sys模块基本介绍")
print("=" * 50)
print("sys模块提供了与Python解释器交互的功能")
print(f"Python版本: {sys.version}")
print(f"Python版本信息: {sys.version_info}")

# ===========================
# 2. 命令行参数处理
# ===========================
print("\n" + "=" * 50)
print("2. 命令行参数处理")
print("=" * 50)

# 获取命令行参数
print(f"命令行参数列表: {sys.argv}")
print(f"参数数量: {len(sys.argv)}")

# 示例：如果直接运行此脚本，可以传递参数测试
# 例如：python sys模块.py arg1 arg2 arg3

# 示例：处理命令行参数
if len(sys.argv) > 1:
    print(f"第一个参数: {sys.argv[1]}")
    print(f"第二个参数: {sys.argv[2] if len(sys.argv) > 2 else '无'}")
else:
    print("未传递命令行参数")

# ===========================
# 3. 标准输入输出
# ===========================
print("\n" + "=" * 50)
print("3. 标准输入输出")
print("=" * 50)

# 标准输出（stdout）
print("这是使用print函数的输出")
sys.stdout.write("这是使用sys.stdout.write的输出\n")

# 标准错误（stderr）
sys.stderr.write("这是使用sys.stderr.write的错误输出\n")

# 标准输入（stdin）
print("\n请输入一些文本（按Enter结束）:")
try:
    input_text = sys.stdin.readline()
    print(f"您输入的是: {input_text.strip()}")
except KeyboardInterrupt:
    print("\n输入被中断")

# 重定向标准输出
print("\n演示标准输出重定向:")
try:
    # 保存原始stdout
    original_stdout = sys.stdout
    
    # 重定向到文件
    with open("sys_output.txt", "w") as f:
        sys.stdout = f
        print("这条消息将被写入文件")
        print("而不是显示在控制台")
    
    # 恢复原始stdout
    sys.stdout = original_stdout
    print("标准输出已恢复")
    
    # 读取并重定向的内容
    with open("sys_output.txt", "r") as f:
        content = f.read()
        print(f"文件中的内容: {content}")
    
    # 删除测试文件
    os.remove("sys_output.txt")
    
except Exception as e:
    print(f"重定向输出时出错: {e}")
    # 确保恢复原始stdout
    sys.stdout = sys.stdout

# ===========================
# 4. 模块导入路径
# ===========================
print("\n" + "=" * 50)
print("4. 模块导入路径")
print("=" * 50)

# 获取模块导入路径
print("模块导入路径:")
for path in sys.path:
    print(f"- {path}")

# 添加自定义路径
print("\n添加自定义路径到sys.path:")
custom_path = "./custom_modules"
if custom_path not in sys.path:
    sys.path.append(custom_path)
    print(f"已添加路径: {custom_path}")
    print(f"新的sys.path长度: {len(sys.path)}")

# ===========================
# 5. Python解释器信息
# ===========================
print("\n" + "=" * 50)
print("5. Python解释器信息")
print("=" * 50)

# Python版本信息
print(f"Python版本: {sys.version}")
print(f"Python版本元组: {sys.version_info}")
print(f"Python版本主号: {sys.version_info.major}")
print(f"Python版本次号: {sys.version_info.minor}")
print(f"Python版本修订号: {sys.version_info.micro}")

# Python安装路径
print(f"Python可执行文件路径: {sys.executable}")
print(f"Python内置模块路径: {sys.prefix}")
print(f"Python包含路径: {sys.base_prefix}")

# 平台信息
print(f"平台名称: {sys.platform}")
print(f"操作系统名称: {os.name}")

# 最大整数大小
print(f"最大整数大小: {sys.maxsize}")

# 默认递归深度
print(f"默认递归深度限制: {sys.getrecursionlimit()}")

# ===========================
# 6. 系统退出
# ===========================
print("\n" + "=" * 50)
print("6. 系统退出")
print("=" * 50)

print("sys.exit()用于退出Python程序")
print("可以指定退出状态码，0表示成功，非0表示错误")

# 示例：演示sys.exit()
def demo_exit():
    print("这是一个演示sys.exit()的函数")
    print("将在3秒后退出...")
    import time
    time.sleep(0.5)  # 缩短等待时间以便演示
    print("演示结束，不会真的退出程序")
    # sys.exit(0)  # 注释掉，避免退出程序

demo_exit()

# ===========================
# 7. 内存管理
# ===========================
print("\n" + "=" * 50)
print("7. 内存管理")
print("=" * 50)

# 获取对象的引用计数
x = [1, 2, 3]
y = x
print(f"列表对象的引用计数: {sys.getrefcount(x)}")  # 注意：getrefcount本身会增加一次引用

# 垃圾回收相关
try:
    import gc
    print(f"自动垃圾回收是否启用: {gc.isenabled()}")
except Exception as e:
    print(f"获取垃圾回收信息失败: {e}")

# 最大Unicode字符
print(f"最大Unicode字符: {sys.maxunicode}")

# ===========================
# 8. 其他有用的功能
# ===========================
print("\n" + "=" * 50)
print("8. 其他有用的功能")
print("=" * 50)

# 获取当前线程的线程ID
print(f"当前线程ID: {sys.thread_info}")

# 获取Python实现信息
print(f"Python实现: {sys.implementation}")

# 获取文件系统编码
print(f"文件系统编码: {sys.getfilesystemencoding()}")

# 获取默认编码
print(f"默认编码: {sys.getdefaultencoding()}")

# 获取递归深度
print(f"当前递归深度: {sys.getrecursionlimit()}")

# 设置递归深度
try:
    sys.setrecursionlimit(10000)
    print(f"新的递归深度限制: {sys.getrecursionlimit()}")
    # 恢复默认值
    sys.setrecursionlimit(1000)
except Exception as e:
    print(f"设置递归深度失败: {e}")

# ===========================
# 9. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

# 示例1: 简单的命令行参数解析
def simple_arg_parser():
    """简单的命令行参数解析器"""
    if len(sys.argv) < 2:
        print("用法: python sys模块.py [选项]")
        print("选项:")
        print("  --help     显示帮助信息")
        print("  --version  显示Python版本")
        return
    
    arg = sys.argv[1]
    if arg == "--help":
        print("这是帮助信息")
    elif arg == "--version":
        print(f"Python版本: {sys.version}")
    else:
        print(f"未知选项: {arg}")

print("示例1: 命令行参数解析")
simple_arg_parser()

# 示例2: 进度条实现
def progress_bar(total, current):
    """使用sys.stdout实现进度条"""
    bar_length = 50
    percent = float(current) / total
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f'\r进度: |{bar}| {percent:.1%} 完成 ({current}/{total})')
    sys.stdout.flush()

print("\n\n示例2: 进度条演示")
try:
    total = 100
    for i in range(total + 1):
        progress_bar(total, i)
        import time
        time.sleep(0.01)  # 模拟耗时操作
sys.stdout.write('\n')
except KeyboardInterrupt:
    sys.stdout.write('\n操作被中断\n')

# 示例3: 自定义模块导入
print("\n示例3: 自定义模块导入路径")
def add_module_path(path):
    """添加自定义模块导入路径"""
    if not os.path.exists(path):
        print(f"路径不存在: {path}")
        return False
    
    if path not in sys.path:
        sys.path.insert(0, path)  # 插入到最前面，优先搜索
        print(f"已添加模块路径: {path}")
        return True
    else:
        print(f"路径已存在于sys.path中: {path}")
        return False

# 演示添加模块路径
test_path = "./test_modules"
if not os.path.exists(test_path):
    os.makedirs(test_path)
    print(f"创建了测试目录: {test_path}")
    
    # 创建一个简单的测试模块
    with open(os.path.join(test_path, "test_module.py"), "w") as f:
        f.write("def hello():\n    return 'Hello from custom module!'")
    
    # 添加模块路径
    add_module_path(test_path)
    
    # 尝试导入模块
    try:
        import test_module
        print(f"成功导入自定义模块: {test_module.hello()}")
    except ImportError as e:
        print(f"导入模块失败: {e}")
    
    # 清理
    os.remove(os.path.join(test_path, "test_module.py"))
    os.rmdir(test_path)
    print(f"已清理测试目录: {test_path}")

# ===========================
# 10. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("10. 最佳实践和注意事项")
print("=" * 50)

print("1. 使用sys.argv处理命令行参数时，注意索引0是脚本名称")
print("2. 对于复杂的命令行参数解析，推荐使用argparse模块")
print("3. 重定向标准输出后，记得恢复原始的sys.stdout")
print("4. 在添加自定义模块路径时，优先使用virtualenv或pip进行包管理")
print("5. 不要随意修改sys.path，可能会导致模块导入冲突")
print("6. 使用sys.exit()时，指定合适的退出状态码（0表示成功）")
print("7. 避免修改默认递归深度，可能导致栈溢出")
print("8. 使用sys.stderr输出错误信息，便于日志分离")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("sys模块是Python解释器的接口，提供了丰富的功能：")
print("- 命令行参数处理")
print("- 标准输入输出控制")
print("- 模块导入路径管理")
print("- Python解释器信息获取")
print("- 系统退出控制")
print("- 内存管理相关功能")
print("\n熟练掌握sys模块可以让Python程序更好地与解释器交互，")
print("实现更多高级功能")
