#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
platform模块 - 系统信息获取

sys模块提供了Python解释器相关的系统信息，
而platform模块则提供了更广泛的系统平台信息获取功能，
可以获取操作系统类型、版本、硬件架构等详细信息。

主要功能包括：
- 获取操作系统信息
- 获取Python解释器信息
- 获取硬件架构信息
- 获取系统版本信息
- 跨平台兼容性检测
"""

import platform
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. platform模块基本介绍")
print("=" * 50)
print("platform模块用于获取系统平台的详细信息")
print("它提供了比sys模块更全面的系统信息获取功能")
print("支持跨平台使用，在Windows、Linux、macOS等系统上均可工作")

# ===========================
# 2. 获取操作系统信息
# ===========================
print("\n" + "=" * 50)
print("2. 获取操作系统信息")
print("=" * 50)

# 获取操作系统名称
print("获取操作系统名称:")
os_name = platform.system()
print(f"操作系统名称: {os_name}")

# 获取操作系统版本
print("\n获取操作系统版本:")
os_version = platform.version()
print(f"操作系统版本: {os_version}")

# 获取操作系统完整信息
print("\n获取操作系统完整信息:")
os_release = platform.release()
os_version_full = platform.version()
os_arch = platform.machine()
print(f"操作系统发布版本: {os_release}")
print(f"操作系统版本: {os_version_full}")
print(f"硬件架构: {os_arch}")

# 获取操作系统平台
print("\n获取操作系统平台:")
platform_name = platform.platform()
print(f"平台信息: {platform_name}")

# 获取Windows系统版本信息
if os_name == "Windows":
    print("\nWindows系统详细信息:")
    win_ver = platform.win32_ver()
    print(f"Windows版本: {win_ver[0]}")
    print(f"Windows服务包: {win_ver[1]}")
    print(f"Windows类型: {win_ver[2]}")
    print(f"Windows构建号: {win_ver[3]}")

# 获取macOS系统版本信息
elif os_name == "Darwin":
    print("\nmacOS系统详细信息:")
    mac_ver = platform.mac_ver()
    print(f"macOS版本: {mac_ver[0]}")
    print(f"macOS版本信息: {mac_ver[1]}")
    print(f"macOS硬件类型: {mac_ver[2]}")

# 获取Linux系统版本信息
elif os_name == "Linux":
    print("\nLinux系统详细信息:")
    linux_dist = platform.dist()  # 已弃用，但仍可使用
    linux_dist_name = platform.linux_distribution()  # 较新的API
    print(f"Linux发行版(旧API): {linux_dist}")
    print(f"Linux发行版(新API): {linux_dist_name}")
    
    # 获取Linux内核版本
    print(f"Linux内核版本: {platform.uname().release}")

# ===========================
# 3. 获取Python解释器信息
# ===========================
print("\n" + "=" * 50)
print("3. 获取Python解释器信息")
print("=" * 50)

# 获取Python版本
print("获取Python版本:")
python_version = platform.python_version()
python_version_tuple = platform.python_version_tuple()
print(f"Python版本: {python_version}")
print(f"Python版本元组: {python_version_tuple}")

# 获取Python构建信息
print("\n获取Python构建信息:")
python_build = platform.python_build()
print(f"Python构建信息: {python_build}")

# 获取Python编译器信息
print("\n获取Python编译器信息:")
python_compiler = platform.python_compiler()
print(f"Python编译器: {python_compiler}")

# 获取Python实现信息
print("\n获取Python实现信息:")
python_implementation = platform.python_implementation()
print(f"Python实现: {python_implementation}")

# 获取Python路径
print("\n获取Python路径:")
python_path = platform.python_path()
print(f"Python路径: {python_path}")

# ===========================
# 4. 获取硬件架构信息
# ===========================
print("\n" + "=" * 50)
print("4. 获取硬件架构信息")
print("=" * 50)

# 获取机器类型
print("获取机器类型:")
machine_type = platform.machine()
print(f"机器类型: {machine_type}")

# 获取处理器信息
print("\n获取处理器信息:")
processor = platform.processor()
print(f"处理器: {processor}")

# 获取CPU信息（在Linux系统上可能需要特殊处理）
print("\n获取CPU信息:")
if os_name == "Linux":
    try:
        with open("/proc/cpuinfo", "r") as f:
            cpu_info = f.read()
        print(f"CPU信息: {cpu_info[:500]}...")  # 只显示前500个字符
    except Exception as e:
        print(f"无法读取CPU信息: {e}")
else:
    print(f"处理器: {platform.processor()}")

# ===========================
# 5. 获取系统全面信息
# ===========================
print("\n" + "=" * 50)
print("5. 获取系统全面信息")
print("=" * 50)

# 获取系统名称
print("系统名称:", platform.system())

# 获取系统版本
print("系统版本:", platform.version())

# 获取系统发布版本
print("系统发布版本:", platform.release())

# 获取机器类型
print("机器类型:", platform.machine())

# 获取节点名称（主机名）
print("节点名称:", platform.node())

# 获取系统平台信息
print("系统平台:", platform.platform())

# 获取uname信息
print("\nuname信息:")
uname_info = platform.uname()
print(f"系统名: {uname_info.system}")
print(f"节点名: {uname_info.node}")
print(f"发布版本: {uname_info.release}")
print(f"版本号: {uname_info.version}")
print(f"机器类型: {uname_info.machine}")
print(f"处理器: {uname_info.processor}")

# ===========================
# 6. 跨平台兼容性检测
# ===========================
print("\n" + "=" * 50)
print("6. 跨平台兼容性检测")
print("=" * 50)

# 检测操作系统类型
def detect_os():
    """检测当前操作系统类型"""
    os_name = platform.system()
    if os_name == "Windows":
        return "Windows"
    elif os_name == "Darwin":
        return "macOS"
    elif os_name == "Linux":
        return "Linux"
    else:
        return f"未知操作系统: {os_name}"

print(f"当前操作系统: {detect_os()}")

# 检测Python版本
def check_python_version(min_version):
    """检查Python版本是否满足最低要求"""
    current_version = tuple(map(int, platform.python_version_tuple()))
    required_version = tuple(map(int, min_version.split(".")))
    
    if current_version >= required_version:
        return True, f"Python版本 {platform.python_version()} 满足要求（需要 {min_version}）"
    else:
        return False, f"Python版本 {platform.python_version()} 不满足要求（需要 {min_version}）"

print(f"\nPython版本检查: {check_python_version("3.6")}")

# 检测64位或32位系统
def is_64bit():
    """检测系统是否为64位"""
    return platform.machine().endswith("64") or platform.architecture()[0] == "64bit"

print(f"\n是否为64位系统: {is_64bit()}")

# ===========================
# 7. 高级功能
# ===========================
print("\n" + "=" * 50)
print("7. 高级功能")
print("=" * 50)

# 获取架构信息
print("获取架构信息:")
arch_info = platform.architecture()
print(f"架构信息: {arch_info}")

# 获取网络节点名称
print("\n获取网络节点名称:")
node_name = platform.node()
print(f"网络节点名称: {node_name}")

# 获取macOS系统的详细信息
if platform.system() == "Darwin":
    print("\nmacOS系统详细信息:")
    mac_info = platform.mac_ver()
    print(f"macOS版本: {mac_info[0]}")
    print(f"macOS内部版本: {mac_info[1]}")
    print(f"macOS硬件: {mac_info[2]}")

# 获取Java虚拟机信息（如果存在）
print("\n获取Java虚拟机信息:")
try:
    java_ver = platform.java_ver()
    print(f"Java版本: {java_ver[0]}")
    print(f"Java虚拟机: {java_ver[1]}")
    print(f"Java供应商: {java_ver[2]}")
except Exception as e:
    print(f"无法获取Java信息: {e}")

# 获取libc信息（在Linux/macOS系统上）
print("\n获取libc信息:")
try:
    libc_ver = platform.libc_ver()
    print(f"libc版本: {libc_ver[0]}")
    print(f"libc版本号: {libc_ver[1]}")
except Exception as e:
    print(f"无法获取libc信息: {e}")

# ===========================
# 8. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("8. 实际应用示例")
print("=" * 50)

# 示例1: 根据操作系统执行不同的操作
def os_specific_operation():
    """根据不同的操作系统执行不同的操作"""
    os_name = platform.system()
    
    if os_name == "Windows":
        print("在Windows系统上执行操作")
        # 这里可以添加Windows特定的代码
    elif os_name == "Darwin":
        print("在macOS系统上执行操作")
        # 这里可以添加macOS特定的代码
    elif os_name == "Linux":
        print("在Linux系统上执行操作")
        # 这里可以添加Linux特定的代码
    else:
        print(f"在未知操作系统 {os_name} 上执行操作")

print("示例1: 根据操作系统执行不同的操作")
os_specific_operation()

# 示例2: 系统信息报告生成
def generate_system_report():
    """生成系统信息报告"""
    report = {}
    
    # 操作系统信息
    report["操作系统"] = platform.system()
    report["操作系统版本"] = platform.version()
    report["操作系统发布"] = platform.release()
    report["硬件架构"] = platform.machine()
    
    # Python信息
    report["Python版本"] = platform.python_version()
    report["Python实现"] = platform.python_implementation()
    report["Python编译器"] = platform.python_compiler()
    
    # 系统信息
    report["平台信息"] = platform.platform()
    report["节点名称"] = platform.node()
    
    return report

print("\n示例2: 系统信息报告生成")
system_report = generate_system_report()
for key, value in system_report.items():
    print(f"{key}: {value}")

# 示例3: 兼容性检查
def check_compatibility():
    """检查系统和Python版本的兼容性"""
    compatibility = {}
    
    # 检查Python版本
    py_ok, py_msg = check_python_version("3.6")
    compatibility["Python版本"] = py_msg
    
    # 检查操作系统
    os_name = platform.system()
    if os_name in ["Windows", "Darwin", "Linux"]:
        compatibility["操作系统"] = f"支持的操作系统: {os_name}"
    else:
        compatibility["操作系统"] = f"可能不支持的操作系统: {os_name}"
    
    # 检查64位支持
    compatibility["64位支持"] = "是" if is_64bit() else "否"
    
    return compatibility

print("\n示例3: 兼容性检查")
compat = check_compatibility()
for key, value in compat.items():
    print(f"{key}: {value}")

# 示例4: 应用程序启动信息显示
def display_app_start_info(app_name, app_version):
    """显示应用程序启动信息"""
    print(f"\n{app_name} v{app_version}")
    print(f"Python {platform.python_version()} on {platform.platform()}")
    print(f"系统: {platform.system()} {platform.release()}, {platform.machine()}")

print("\n示例4: 应用程序启动信息显示")
display_app_start_info("MyApp", "1.0.0")

# 示例5: 日志系统信息记录
def log_system_info():
    """记录系统信息到日志"""
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    
    logging.info(f"系统信息: {platform.platform()}")
    logging.info(f"Python版本: {platform.python_version()}")
    logging.info(f"操作系统: {platform.system()} {platform.release()}")
    logging.info(f"硬件架构: {platform.machine()}")

print("\n示例5: 日志系统信息记录")
log_system_info()

# ===========================
# 9. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("9. 最佳实践和注意事项")
print("=" * 50)

print("1. 使用platform模块获取系统信息比直接解析sys模块输出更可靠")
print("2. 注意platform模块在不同操作系统上的输出可能不同")
print("3. 对于Windows系统，使用platform.win32_ver()获取更详细的版本信息")
print("4. 对于Linux系统，platform.dist()已弃用，考虑使用其他方法获取发行版信息")
print("5. 不要假设platform.processor()在所有系统上都能返回有意义的结果")
print("6. 使用platform.architecture()检测64位系统时要注意其局限性")
print("7. 编写跨平台代码时，使用platform.system()进行条件判断")
print("8. 在应用程序日志中记录系统信息有助于调试和支持")
print("9. 定期检查platform模块的文档，了解API变化")
print("10. 不要依赖platform模块返回的特定字符串格式，因为它们可能随系统更新而变化")

# ===========================
# 10. 总结
# ===========================
print("\n" + "=" * 50)
print("10. 总结")
print("=" * 50)
print("platform模块提供了全面的系统信息获取功能：")
print("- 可以获取操作系统、硬件和Python解释器的详细信息")
print("- 支持跨平台使用，在各种操作系统上都能工作")
print("- 提供了比sys模块更丰富的系统信息")
print("- 可用于兼容性检测、系统报告生成和应用程序信息显示等场景")
print("\n合理使用platform模块可以帮助开发跨平台兼容的应用程序，")
print("并为调试和支持提供有用的系统信息")
