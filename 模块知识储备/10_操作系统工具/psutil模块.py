#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
psutil模块 - 系统信息获取和进程管理

psutil是一个跨平台的Python库，用于获取系统信息和管理进程。

主要功能包括：
- CPU使用率和统计信息
- 内存使用情况
- 磁盘空间和I/O统计
- 网络连接和统计
- 进程列表和进程信息
- 系统启动时间
- 用户登录信息

使用场景：
- 系统监控和性能分析
- 进程管理工具
- 系统资源使用报告
- 自动化系统管理脚本

安装方法：
pip install psutil
"""

import psutil
import datetime
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. psutil模块基本介绍")
print("=" * 50)
print("psutil是一个跨平台的系统信息获取和进程管理库")
print("支持Windows、Linux、macOS等多种操作系统")
print("提供了简洁易用的API接口")
print("适合用于系统监控和管理")

# ===========================
# 2. CPU信息
# ===========================
print("\n" + "=" * 50)
print("2. CPU信息")
print("=" * 50)

# 获取CPU逻辑核心数
print(f"CPU逻辑核心数: {psutil.cpu_count()}")

# 获取CPU物理核心数
print(f"CPU物理核心数: {psutil.cpu_count(logical=False)}")

# 获取CPU使用率（每秒刷新一次）
print("\nCPU使用率:")
for i in range(3):
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"  总使用率: {cpu_percent}%")
    
    # 获取每个CPU核心的使用率
    per_cpu = psutil.cpu_percent(interval=0, percpu=True)
    print(f"  各核心使用率: {per_cpu}")

# 获取CPU统计信息
cpu_stats = psutil.cpu_stats()
print("\nCPU统计信息:")
print(f"  上下文切换次数: {cpu_stats.ctx_switches}")
print(f"  中断次数: {cpu_stats.interrupts}")
print(f"  软中断次数: {cpu_stats.soft_interrupts}")
print(f"  系统调用次数: {cpu_stats.syscalls}")

# ===========================
# 3. 内存信息
# ===========================
print("\n" + "=" * 50)
print("3. 内存信息")
print("=" * 50)

# 获取内存使用情况
memory = psutil.virtual_memory()
print(f"总内存: {memory.total / (1024**3):.2f} GB")
print(f"可用内存: {memory.available / (1024**3):.2f} GB")
print(f"已使用内存: {memory.used / (1024**3):.2f} GB")
print(f"内存使用率: {memory.percent}%")
print(f"缓冲内存: {memory.buffers / (1024**3):.2f} GB")
print(f"缓存内存: {memory.cached / (1024**3):.2f} GB")

# 获取交换内存信息
swap = psutil.swap_memory()
print("\n交换内存信息:")
print(f"总交换内存: {swap.total / (1024**3):.2f} GB")
print(f"已使用交换内存: {swap.used / (1024**3):.2f} GB")
print(f"可用交换内存: {swap.free / (1024**3):.2f} GB")
print(f"交换内存使用率: {swap.percent}%")

# ===========================
# 4. 磁盘信息
# ===========================
print("\n" + "=" * 50)
print("4. 磁盘信息")
print("=" * 50)

# 获取磁盘分区信息
print("磁盘分区信息:")
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"\n  设备: {partition.device}")
    print(f"  挂载点: {partition.mountpoint}")
    print(f"  文件系统类型: {partition.fstype}")
    print(f"  选项: {partition.opts}")
    
    # 获取分区使用情况
    try:
        usage = psutil.disk_usage(partition.mountpoint)
        print(f"  总空间: {usage.total / (1024**3):.2f} GB")
        print(f"  已使用: {usage.used / (1024**3):.2f} GB")
        print(f"  可用空间: {usage.free / (1024**3):.2f} GB")
        print(f"  使用率: {usage.percent}%")
    except PermissionError:
        print("  无法访问该分区的使用情况")

# 获取磁盘I/O统计
print("\n磁盘I/O统计:")
disk_io = psutil.disk_io_counters()
print(f"  读取次数: {disk_io.read_count}")
print(f"  写入次数: {disk_io.write_count}")
print(f"  读取字节数: {disk_io.read_bytes / (1024**3):.2f} GB")
print(f"  写入字节数: {disk_io.write_bytes / (1024**3):.2f} GB")
print(f"  读取时间: {disk_io.read_time} ms")
print(f"  写入时间: {disk_io.write_time} ms")

# ===========================
# 5. 网络信息
# ===========================
print("\n" + "=" * 50)
print("5. 网络信息")
print("=" * 50)

# 获取网络I/O统计
print("网络I/O统计:")
net_io = psutil.net_io_counters()
print(f"  发送字节数: {net_io.bytes_sent / (1024**3):.2f} GB")
print(f"  接收字节数: {net_io.bytes_recv / (1024**3):.2f} GB")
print(f"  发送包数: {net_io.packets_sent}")
print(f"  接收包数: {net_io.packets_recv}")
print(f"  发送错误数: {net_io.errin}")
print(f"  接收错误数: {net_io.errout}")
print(f"  丢弃包数: {net_io.dropin + net_io.dropout}")

# 获取网络接口信息
print("\n网络接口信息:")
net_if_addrs = psutil.net_if_addrs()
for interface_name, addresses in net_if_addrs.items():
    print(f"\n  接口名称: {interface_name}")
    for address in addresses:
        print(f"    地址类型: {address.family.name}")
        print(f"    IP地址: {address.address}")
        if address.netmask:
            print(f"    子网掩码: {address.netmask}")
        if address.broadcast:
            print(f"    广播地址: {address.broadcast}")

# 获取网络连接信息
print("\n网络连接信息（前10个）:")
try:
    connections = psutil.net_connections()
    count = 0
    for conn in connections:
        if count >= 10:
            break
        print(f"\n  连接ID: {conn.fd}")
        print(f"  状态: {conn.status}")
        print(f"  本地地址: {conn.laddr}")
        print(f"  远程地址: {conn.raddr}")
        print(f"  进程ID: {conn.pid}")
        count += 1
    
    if count == 0:
        print("  没有找到网络连接")
except PermissionError:
    print("  无法访问网络连接信息（需要管理员权限）")

# ===========================
# 6. 系统信息
# ===========================
print("\n" + "=" * 50)
print("6. 系统信息")
print("=" * 50)

# 获取系统启动时间
boot_time = psutil.boot_time()
boot_time_datetime = datetime.datetime.fromtimestamp(boot_time)
current_time = datetime.datetime.now()
up_time = current_time - boot_time_datetime

print(f"系统启动时间: {boot_time_datetime.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"系统运行时间: {up_time}")

# 获取登录用户信息
print("\n当前登录用户:")
users = psutil.users()
for user in users:
    print(f"  用户名: {user.name}")
    print(f"  终端: {user.terminal}")
    print(f"  登录时间: {datetime.datetime.fromtimestamp(user.started).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  远程IP: {user.host}")

# ===========================
# 7. 进程管理
# ===========================
print("\n" + "=" * 50)
print("7. 进程管理")
print("=" * 50)

# 获取所有进程ID
print(f"当前运行的进程数量: {len(psutil.pids())}")

# 获取当前进程信息
current_process = psutil.Process(os.getpid())
print(f"\n当前进程信息:")
print(f"  进程ID: {current_process.pid}")
print(f"  进程名称: {current_process.name()}")
print(f"  进程路径: {current_process.exe()}")
print(f"  命令行参数: {current_process.cmdline()}")
print(f"  进程状态: {current_process.status()}")
print(f"  进程创建时间: {datetime.datetime.fromtimestamp(current_process.create_time()).strftime('%Y-%m-%d %H:%M:%S')}")

# 获取进程资源使用情况
print(f"\n当前进程资源使用情况:")
print(f"  CPU使用率: {current_process.cpu_percent(interval=1)}%")
print(f"  内存使用率: {current_process.memory_percent()}%")
mem_info = current_process.memory_info()
print(f"  内存使用量: {mem_info.rss / (1024**2):.2f} MB")

# 遍历并显示前5个进程信息
print("\n前5个进程信息:")
for i, pid in enumerate(psutil.pids()[:5]):
    try:
        process = psutil.Process(pid)
        print(f"\n  进程 {i+1}:")
        print(f"    进程ID: {process.pid}")
        print(f"    进程名称: {process.name()}")
        print(f"    进程状态: {process.status()}")
        print(f"    CPU使用率: {process.cpu_percent(interval=0.1)}%")
        print(f"    内存使用率: {process.memory_percent()}%")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print(f"\n  进程 {i+1}: 无法访问")

# ===========================
# 8. 进程搜索和过滤
# ===========================
print("\n" + "=" * 50)
print("8. 进程搜索和过滤")
print("=" * 50)

# 根据进程名称搜索进程
def search_process_by_name(name):
    """根据进程名称搜索进程"""
    matching_processes = []
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
            if name.lower() in process.name().lower():
                matching_processes.append(process)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return matching_processes

# 搜索包含python的进程
python_processes = search_process_by_name("python")
print(f"包含'python'的进程数量: {len(python_processes)}")

# 显示搜索结果
for i, process in enumerate(python_processes[:3]):
    try:
        print(f"\n  Python进程 {i+1}:")
        print(f"    进程ID: {process.pid}")
        print(f"    进程名称: {process.name()}")
        print(f"    命令行: {' '.join(process.cmdline())}")
        print(f"    内存使用: {process.memory_info().rss / (1024**2):.2f} MB")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print(f"\n  Python进程 {i+1}: 无法访问")

# ===========================
# 9. 系统监控示例
# ===========================
print("\n" + "=" * 50)
print("9. 系统监控示例")
print("=" * 50)

# 简单的系统监控函数
def system_monitor(interval=2, count=3):
    """简单的系统监控"""
    print(f"系统监控启动 (间隔: {interval}秒, 次数: {count})")
    for i in range(count):
        print(f"\n--- 监控结果 {i+1} ---")
        
        # CPU使用率
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"CPU使用率: {cpu_percent}%")
        
        # 内存使用情况
        memory = psutil.virtual_memory()
        print(f"内存使用率: {memory.percent}%")
        print(f"可用内存: {memory.available / (1024**3):.2f} GB")
        
        # 磁盘使用情况（系统盘）
        try:
            if os.name == 'nt':  # Windows
                disk_usage = psutil.disk_usage('C:')
            else:  # Linux/macOS
                disk_usage = psutil.disk_usage('/')
            print(f"磁盘使用率: {disk_usage.percent}%")
            print(f"可用磁盘空间: {disk_usage.free / (1024**3):.2f} GB")
        except PermissionError:
            print("无法获取磁盘使用情况")

# 运行系统监控
system_monitor()

# ===========================
# 10. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("10. 实际应用示例")
print("=" * 50)

# 示例1: 查找占用CPU最高的进程
def find_top_cpu_processes(count=5):
    """查找占用CPU最高的进程"""
    processes = []
    
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
            # 获取进程CPU使用率
            cpu_percent = process.cpu_percent(interval=0.1)
            if cpu_percent > 0:
                processes.append((cpu_percent, process))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    # 按CPU使用率排序
    processes.sort(reverse=True, key=lambda x: x[0])
    
    # 返回前count个进程
    return processes[:count]

# 示例2: 查找占用内存最高的进程
def find_top_memory_processes(count=5):
    """查找占用内存最高的进程"""
    processes = []
    
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
            # 获取进程内存使用率
            memory_percent = process.memory_percent()
            if memory_percent > 0:
                processes.append((memory_percent, process))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    # 按内存使用率排序
    processes.sort(reverse=True, key=lambda x: x[0])
    
    # 返回前count个进程
    return processes[:count]

# 示例3: 检查进程是否运行
def is_process_running(process_name):
    """检查指定名称的进程是否正在运行"""
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)
            if process_name.lower() in process.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False

# 演示应用示例
print("示例1: 占用CPU最高的进程:")
top_cpu_processes = find_top_cpu_processes()
for i, (cpu_percent, process) in enumerate(top_cpu_processes):
    try:
        print(f"  {i+1}. {process.name()} (PID: {process.pid}) - {cpu_percent}%")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print(f"  {i+1}. 未知进程 - {cpu_percent}%")

print("\n示例2: 占用内存最高的进程:")
top_memory_processes = find_top_memory_processes()
for i, (memory_percent, process) in enumerate(top_memory_processes):
    try:
        print(f"  {i+1}. {process.name()} (PID: {process.pid}) - {memory_percent}%")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print(f"  {i+1}. 未知进程 - {memory_percent}%")

print("\n示例3: 检查进程是否运行:")
process_names = ["python", "chrome", "explorer", "notepad"]
for name in process_names:
    is_running = is_process_running(name)
    print(f"  {name}: {'正在运行' if is_running else '未运行'}")

# ===========================
# 11. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("11. 最佳实践和注意事项")
print("=" * 50)

print("1. 权限问题")
print("   - 某些系统信息和进程操作需要管理员/root权限")
print("   - 在Windows上需要以管理员身份运行脚本")
print("   - 在Linux上需要使用sudo权限")

print("\n2. 性能影响")
print("   - 频繁调用某些函数（如cpu_percent）会影响系统性能")
print("   - 合理设置interval参数，避免过度采样")
print("   - 仅获取必要的信息，避免不必要的系统调用")

print("\n3. 跨平台兼容性")
print("   - psutil提供了跨平台的API，但某些功能可能有平台差异")
print("   - 在不同操作系统上测试代码")
print("   - 使用条件语句处理平台特定的功能")

print("\n4. 异常处理")
print("   - 进程可能随时终止，导致psutil.NoSuchProcess异常")
print("   - 某些进程可能无法访问，导致psutil.AccessDenied异常")
print("   - 始终使用try-except块处理异常")

print("\n5. 资源管理")
print("   - Process对象占用系统资源，不需要时应及时释放")
print("   - 避免在循环中创建大量Process对象")

# ===========================
# 12. 总结
# ===========================
print("\n" + "=" * 50)
print("12. 总结")
print("=" * 50)
print("psutil是一个功能强大的系统信息获取和进程管理库")
print("提供了丰富的API接口，支持多种操作系统")
print("\n主要功能:")
print("- CPU信息获取和使用率监控")
print("- 内存和交换内存使用情况")
print("- 磁盘空间和I/O统计")
print("- 网络连接和流量统计")
print("- 进程列表和进程信息获取")
print("- 系统信息和用户登录信息")
print("\npsutil适用于:")
print("- 系统监控和性能分析工具")
print("- 进程管理和调度脚本")
print("- 系统资源使用报告生成")
print("- 自动化系统管理任务")
print("\n通过psutil，您可以轻松地创建各种系统管理和监控工具")
print("提高系统管理的效率和自动化程度")
