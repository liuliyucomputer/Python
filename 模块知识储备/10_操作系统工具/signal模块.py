#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
signal模块 - 信号处理

signal模块提供了处理操作系统信号的功能。

主要功能包括：
- 注册信号处理函数
- 发送信号到进程
- 处理常见信号如SIGINT、SIGTERM等
- 实现优雅关闭程序

使用场景：
- 优雅关闭程序
- 处理中断信号
- 实现超时控制
- 进程间通信

官方文档：https://docs.python.org/3/library/signal.html
"""

import signal
import time
import os
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. signal模块基本介绍")
print("=" * 50)
print("signal模块用于处理操作系统信号")
print("信号是操作系统传递给进程的中断")
print("用于进程间通信和系统事件通知")
print("适合实现优雅关闭和超时控制")

# ===========================
# 2. 常见信号类型
# ===========================
print("\n" + "=" * 50)
print("2. 常见信号类型")
print("=" * 50)

# 打印常见信号
common_signals = {
    "SIGINT": signal.SIGINT,
    "SIGTERM": signal.SIGTERM,
    "SIGKILL": signal.SIGKILL,
    "SIGALRM": signal.SIGALRM,
    "SIGUSR1": signal.SIGUSR1,
    "SIGUSR2": signal.SIGUSR2,
}

for name, sig in common_signals.items():
    print(f"{name}: {sig}")

# 信号描述
print("\n信号描述:")
print("SIGINT: 中断信号，通常由Ctrl+C产生")
print("SIGTERM: 终止信号，通常用于请求进程终止")
print("SIGKILL: 强制终止信号，无法被捕获或忽略")
print("SIGALRM: 闹钟信号，用于定时器")
print("SIGUSR1/SIGUSR2: 用户自定义信号")

# ===========================
# 3. 注册信号处理函数
# ===========================
print("\n" + "=" * 50)
print("3. 注册信号处理函数")
print("=" * 50)

# 定义信号处理函数
def sigint_handler(signum, frame):
    """处理SIGINT信号"""
    print(f"\n收到信号 {signum} (SIGINT)")
    print("正在优雅退出...")
    sys.exit(0)

# 注册信号处理函数
signal.signal(signal.SIGINT, sigint_handler)

print("已注册SIGINT信号处理函数")
print("尝试按Ctrl+C测试信号处理")
print("(程序将在10秒后自动退出)")

# 等待信号
for i in range(10):
    print(f"等待中... {i+1}")
    time.sleep(1)

print("\n程序正常退出")

# ===========================
# 4. 发送信号
# ===========================
print("\n" + "=" * 50)
print("4. 发送信号")
print("=" * 50)

# 获取当前进程ID
pid = os.getpid()
print(f"当前进程ID: {pid}")

# 定义信号处理函数
def sigusr1_handler(signum, frame):
    """处理SIGUSR1信号"""
    print(f"\n收到信号 {signum} (SIGUSR1)")

# 注册信号处理函数
signal.signal(signal.SIGUSR1, sigusr1_handler)

print("已注册SIGUSR1信号处理函数")
print("向当前进程发送SIGUSR1信号")

# 发送信号到当前进程
os.kill(pid, signal.SIGUSR1)

# 等待信号处理完成
time.sleep(1)

print("信号处理完成")

# ===========================
# 5. 超时控制
# ===========================
print("\n" + "=" * 50)
print("5. 超时控制")
print("=" * 50)

# 定义超时处理函数
def timeout_handler(signum, frame):
    """处理超时信号"""
    print(f"\n收到信号 {signum} (SIGALRM)")
    raise TimeoutError("操作超时")

# 注册超时信号处理函数
signal.signal(signal.SIGALRM, timeout_handler)

# 设置超时
def timeout(seconds):
    """超时装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 设置定时器
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
                # 取消定时器
                signal.alarm(0)
                return result
            except TimeoutError as e:
                # 取消定时器
                signal.alarm(0)
                raise e
        return wrapper
    return decorator

# 测试超时装饰器
@timeout(3)
def long_running_function():
    """长时间运行的函数"""
    print("开始执行长时间运行的函数...")
    time.sleep(5)
    print("函数执行完成")
    return "完成"

# 测试超时功能
print("测试超时功能")
try:
    result = long_running_function()
    print(f"函数结果: {result}")
except TimeoutError as e:
    print(f"函数执行超时: {e}")

# ===========================
# 6. 优雅关闭程序
# ===========================
print("\n" + "=" * 50)
print("6. 优雅关闭程序")
print("=" * 50)

# 定义优雅关闭处理函数
def graceful_shutdown(signum, frame):
    """优雅关闭程序"""
    print(f"\n收到信号 {signum}")
    print("正在执行优雅关闭...")
    
    # 执行清理操作
    print("  保存数据...")
    time.sleep(1)
    print("  关闭连接...")
    time.sleep(1)
    print("  释放资源...")
    time.sleep(1)
    
    print("程序已优雅关闭")
    sys.exit(0)

# 注册多个信号处理函数
for sig in [signal.SIGINT, signal.SIGTERM]:
    signal.signal(sig, graceful_shutdown)

print("已注册优雅关闭信号处理函数")
print("尝试按Ctrl+C或发送SIGTERM信号测试")
print("(程序将在10秒后自动退出)")

# 模拟程序运行
for i in range(10):
    print(f"程序运行中... {i+1}")
    time.sleep(1)

print("\n程序正常退出")

# ===========================
# 7. 忽略信号
# ===========================
print("\n" + "=" * 50)
print("7. 忽略信号")
print("=" * 50)

print("忽略SIGINT信号")
# 忽略SIGINT信号
signal.signal(signal.SIGINT, signal.SIG_IGN)

print("按Ctrl+C将不会中断程序")
print("(程序将在5秒后自动退出)")

for i in range(5):
    print(f"运行中... {i+1}")
    time.sleep(1)

print("\n恢复默认信号处理")
# 恢复默认信号处理
signal.signal(signal.SIGINT, signal.SIG_DFL)

# ===========================
# 8. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("8. 实际应用示例")
print("=" * 50)

# 示例1: 实现超时控制
def run_with_timeout(func, timeout_seconds, *args, **kwargs):
    """带超时控制的函数执行"""
    # 定义超时处理函数
    def timeout_handler(signum, frame):
        raise TimeoutError(f"函数执行超时 ({timeout_seconds}秒)")
    
    # 保存原始信号处理函数
    original_handler = signal.signal(signal.SIGALRM, timeout_handler)
    
    try:
        # 设置定时器
        signal.alarm(timeout_seconds)
        
        # 执行函数
        result = func(*args, **kwargs)
        
        # 取消定时器
        signal.alarm(0)
        
        return result
    except TimeoutError as e:
        # 取消定时器
        signal.alarm(0)
        raise e
    finally:
        # 恢复原始信号处理函数
        signal.signal(signal.SIGALRM, original_handler)

# 测试超时控制
print("示例1: 实现超时控制")
def test_function():
    time.sleep(2)
    return "成功"

try:
    result = run_with_timeout(test_function, 1)
    print(f"函数结果: {result}")
except TimeoutError as e:
    print(f"函数超时: {e}")

try:
    result = run_with_timeout(test_function, 3)
    print(f"函数结果: {result}")
except TimeoutError as e:
    print(f"函数超时: {e}")

# 示例2: 信号处理上下文管理器
import contextlib

@contextlib.contextmanager
def signal_handler(signum, handler):
    """信号处理上下文管理器"""
    # 保存原始处理函数
    original_handler = signal.getsignal(signum)
    
    try:
        # 设置新的处理函数
        signal.signal(signum, handler)
        yield
    finally:
        # 恢复原始处理函数
        signal.signal(signum, original_handler)

# 测试信号处理上下文管理器
print("\n示例2: 信号处理上下文管理器")

def temp_handler(signum, frame):
    print(f"\n临时信号处理函数: {signum}")

print("在上下文管理器外按Ctrl+C会执行默认处理")
time.sleep(2)

with signal_handler(signal.SIGINT, temp_handler):
    print("在上下文管理器内按Ctrl+C会执行临时处理函数")
    time.sleep(3)

print("上下文管理器结束，信号处理已恢复")
time.sleep(2)

# 示例3: 实现看门狗定时器
class Watchdog:
    """看门狗定时器"""
    def __init__(self, timeout_seconds):
        self.timeout_seconds = timeout_seconds
        self.handler = None
        self.original_handler = None
    
    def __enter__(self):
        """开始看门狗"""
        # 定义超时处理函数
        def timeout_handler(signum, frame):
            if self.handler:
                self.handler()
            raise TimeoutError(f"看门狗超时 ({self.timeout_seconds}秒)")
        
        # 保存原始处理函数
        self.original_handler = signal.getsignal(signal.SIGALRM)
        
        # 设置信号处理函数
        signal.signal(signal.SIGALRM, timeout_handler)
        
        # 启动定时器
        signal.alarm(self.timeout_seconds)
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """停止看门狗"""
        # 取消定时器
        signal.alarm(0)
        
        # 恢复原始处理函数
        signal.signal(signal.SIGALRM, self.original_handler)
    
    def reset(self):
        """重置看门狗定时器"""
        signal.alarm(self.timeout_seconds)
    
    def set_handler(self, handler):
        """设置超时处理函数"""
        self.handler = handler

# 测试看门狗定时器
print("\n示例3: 实现看门狗定时器")

def watchdog_callback():
    print("看门狗超时回调函数被调用")

print("测试看门狗定时器")
try:
    with Watchdog(2) as watchdog:
        watchdog.set_handler(watchdog_callback)
        print("看门狗已启动，2秒后超时")
        time.sleep(1)
        print("重置看门狗定时器")
        watchdog.reset()
        time.sleep(3)  # 这会导致超时
        print("看门狗测试通过")
except TimeoutError as e:
    print(f"看门狗超时: {e}")

# ===========================
# 9. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("9. 最佳实践和注意事项")
print("=" * 50)

print("1. 信号处理函数的限制")
print("   - 信号处理函数应该尽量简单")
print("   - 避免在信号处理函数中使用可能阻塞的操作")
print("   - 避免在信号处理函数中使用全局变量")
print("   - 不要在信号处理函数中调用print等可能不是线程安全的函数")

print("\n2. 跨平台兼容性")
print("   - Windows平台对信号的支持有限")
print("   - 某些信号（如SIGUSR1、SIGUSR2）在Windows上不可用")
print("   - 使用信号时需要考虑平台差异")

print("\n3. 信号类型")
print("   - SIGKILL和SIGSTOP信号无法被捕获或忽略")
print("   - 某些信号有默认的处理行为")
print("   - 可以使用signal.SIG_DFL恢复默认处理")
print("   - 可以使用signal.SIG_IGN忽略信号")

print("\n4. 超时控制")
print("   - 信号闹钟（SIGALRM）是实现超时控制的常用方法")
print("   - 在多线程环境中，闹钟信号会发送到任意一个线程")
print("   - 不建议在多线程程序中使用信号闹钟")

print("\n5. 优雅关闭")
print("   - 使用信号处理函数实现程序的优雅关闭")
print("   - 在关闭前执行必要的清理操作")
print("   - 处理SIGINT和SIGTERM信号")

# ===========================
# 10. 总结
# ===========================
print("\n" + "=" * 50)
print("10. 总结")
print("=" * 50)
print("signal模块提供了处理操作系统信号的功能")
print("用于实现优雅关闭、超时控制和进程间通信")

print("\n主要功能:")
print("- 注册和处理信号")
print("- 发送信号到进程")
print("- 实现超时控制")
print("- 优雅关闭程序")
print("- 处理中断信号")

print("\n应用场景:")
print("- 命令行程序的中断处理")
print("- 后台服务的优雅关闭")
print("- 长时间运行操作的超时控制")
print("- 进程间的简单通信")
print("- 实现看门狗机制")

print("\n使用signal模块时，需要注意信号处理函数的限制")
print("和跨平台兼容性问题")
