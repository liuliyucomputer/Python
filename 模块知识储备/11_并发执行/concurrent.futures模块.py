#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
concurrent.futures模块 - 高级并发编程接口

concurrent.futures模块提供了高级并发编程接口，简化了多线程和多进程编程。它是对threading和multiprocessing模块的封装，提供了更易用的API。

主要功能包括：
- ThreadPoolExecutor: 线程池执行器
- ProcessPoolExecutor: 进程池执行器
- Future对象: 表示异步执行的结果
- 统一的接口: 支持线程和进程的相同API

使用场景：
- 简化多线程和多进程编程
- 批量处理任务
- 异步执行任务
- 提高程序性能

官方文档：https://docs.python.org/3/library/concurrent.futures.html
"""

import concurrent.futures
import time
import random
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. concurrent.futures模块基本介绍")
print("=" * 50)
print("concurrent.futures模块提供高级并发编程接口，封装了threading和multiprocessing模块")
print("主要包含ThreadPoolExecutor和ProcessPoolExecutor两个执行器")
print("使用Future对象表示异步执行的结果")
print("提供统一的API，支持线程和进程的无缝切换")

# ===========================
# 2. ThreadPoolExecutor
# ===========================
print("\n" + "=" * 50)
print("2. ThreadPoolExecutor")
print("=" * 50)

# 示例1: 基本使用
print("示例1: ThreadPoolExecutor基本使用")

def task(n):
    """简单任务函数"""
    print(f"线程 {threading.current_thread().name}: 处理 {n}")
    time.sleep(random.uniform(0.5, 1.5))
    return n * n

# 导入threading模块
try:
    import threading
except ImportError:
    print("threading模块导入失败")

# 创建线程池（默认使用5个线程）
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    results = [executor.submit(task, i) for i in range(1, 6)]
    
    # 获取结果
    for future in concurrent.futures.as_completed(results):
        result = future.result()
        print(f"获取到结果: {result}")

# 示例2: 使用map方法
print("\n示例2: 使用map方法")

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 使用map方法批量处理任务
    inputs = [1, 2, 3, 4, 5]
    results = executor.map(task, inputs)
    
    # 获取结果
    for result in results:
        print(f"map结果: {result}")

# 示例3: 使用submit和as_completed
print("\n示例3: 使用submit和as_completed")

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 创建任务字典
    future_to_task = {executor.submit(task, i): i for i in range(1, 6)}
    
    # 按照任务完成顺序获取结果
    for future in concurrent.futures.as_completed(future_to_task):
        task_number = future_to_task[future]
        try:
            result = future.result()
            print(f"任务 {task_number} 完成，结果: {result}")
        except Exception as e:
            print(f"任务 {task_number} 失败，错误: {e}")

# ===========================
# 3. ProcessPoolExecutor
# ===========================
print("\n" + "=" * 50)
print("3. ProcessPoolExecutor")
print("=" * 50)

# 示例4: 基本使用
print("示例4: ProcessPoolExecutor基本使用")

def cpu_intensive_task(n):
    """CPU密集型任务"""
    print(f"进程 {os.getpid()}: 处理 {n}")
    result = 0
    for i in range(n * 1000000):
        result += i
    return result

# 创建进程池（默认使用CPU核心数）
with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    # 提交任务
    results = [executor.submit(cpu_intensive_task, i) for i in range(1, 6)]
    
    # 获取结果
    for future in concurrent.futures.as_completed(results):
        result = future.result()
        print(f"获取到结果: {result}")

# 示例5: 使用map方法
print("\n示例5: 使用map方法")

with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    # 使用map方法批量处理任务
    inputs = [1, 2, 3, 4, 5]
    results = executor.map(cpu_intensive_task, inputs)
    
    # 获取结果
    for result in results:
        print(f"map结果: {result}")

# ===========================
# 4. Future对象
# ===========================
print("\n" + "=" * 50)
print("4. Future对象")
print("=" * 50)

# 示例6: Future对象的基本使用
print("示例6: Future对象的基本使用")

def delayed_task(n):
    """延迟任务"""
    time.sleep(n)
    return f"延迟 {n} 秒完成"

# 创建线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    # 提交任务，获取Future对象
    future = executor.submit(delayed_task, 2)
    
    # 检查Future对象状态
    print(f"Future是否完成: {future.done()}")
    print(f"Future是否正在运行: {future.running()}")
    print(f"Future是否已取消: {future.cancelled()}")
    
    # 等待结果
    result = future.result()
    print(f"获取结果: {result}")
    
    # 再次检查状态
    print(f"Future是否完成: {future.done()}")

# 示例7: Future对象的异常处理
print("\n示例7: Future对象的异常处理")

def error_task():
    """抛出异常的任务"""
    time.sleep(1)
    raise ValueError("任务执行出错")

# 创建线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(error_task)
    
    try:
        result = future.result()
        print(f"获取结果: {result}")
    except Exception as e:
        print(f"捕获到异常: {type(e).__name__}: {e}")

# ===========================
# 5. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("5. 实际应用示例")
print("=" * 50)

# 示例8: 多线程下载文件
print("示例8: 多线程下载文件")

def download_file(filename, url, delay):
    """模拟下载文件"""
    print(f"下载 {filename} 从 {url}")
    time.sleep(delay)  # 模拟下载时间
    return f"{filename} 下载完成"

# 文件列表
files_to_download = [
    ("file1.txt", "https://example.com/file1.txt", 2),
    ("file2.txt", "https://example.com/file2.txt", 1),
    ("file3.txt", "https://example.com/file3.txt", 3),
    ("file4.txt", "https://example.com/file4.txt", 2),
    ("file5.txt", "https://example.com/file5.txt", 1)
]

# 创建线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    futures = {executor.submit(download_file, filename, url, delay): filename 
              for filename, url, delay in files_to_download}
    
    # 获取结果
    for future in concurrent.futures.as_completed(futures):
        filename = futures[future]
        try:
            result = future.result()
            print(f"{result}")
        except Exception as e:
            print(f"{filename} 下载失败: {e}")

# 示例9: 多进程并行计算
print("\n示例9: 多进程并行计算")

def calculate_fibonacci(n):
    """计算斐波那契数"""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def calculate_factorial(n):
    """计算阶乘"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def calculate_prime(n):
    """检查是否为素数"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 创建进程池
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    # 提交不同类型的计算任务
    future1 = executor.submit(calculate_fibonacci, 30)
    future2 = executor.submit(calculate_factorial, 20)
    future3 = executor.submit(calculate_prime, 1000000007)
    future4 = executor.submit(calculate_fibonacci, 25)
    
    # 获取结果
    futures = [future1, future2, future3, future4]
    for future in concurrent.futures.as_completed(futures):
        try:
            result = future.result()
            print(f"计算结果: {result}")
        except Exception as e:
            print(f"计算失败: {e}")

# 示例10: 批量处理图像
print("\n示例10: 批量处理图像")

def process_image(image_path):
    """模拟图像处理"""
    print(f"处理图像: {image_path}")
    time.sleep(random.uniform(1, 2))  # 模拟处理时间
    return f"{image_path} 处理完成"

# 图像列表
images = [f"image{i}.jpg" for i in range(1, 11)]

# 创建线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 使用map方法批量处理
    results = executor.map(process_image, images)
    
    # 统计处理结果
    completed = 0
    for result in results:
        print(f"  {result}")
        completed += 1
    
    print(f"\n共处理 {completed} 张图像")

# 示例11: 异步Web请求
print("\n示例11: 异步Web请求")

# 尝试导入requests模块
try:
    import requests
    
    def fetch_url(url):
        """获取URL内容"""
        print(f"获取 {url}")
        response = requests.get(url, timeout=5)
        return f"{url}: {response.status_code} - {len(response.text)} 字节"
    
    # URL列表
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.google.com",
        "https://www.microsoft.com",
        "https://www.apple.com"
    ]
    
    # 创建线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # 提交任务
        futures = {executor.submit(fetch_url, url): url for url in urls}
        
        # 获取结果
        for future in concurrent.futures.as_completed(futures):
            url = futures[future]
            try:
                result = future.result()
                print(f"  {result}")
            except Exception as e:
                print(f"  {url} 请求失败: {e}")
    
except ImportError:
    print("requests模块未安装，无法演示Web请求")

# ===========================
# 6. ThreadPoolExecutor vs ProcessPoolExecutor
# ===========================
print("\n" + "=" * 50)
print("6. ThreadPoolExecutor vs ProcessPoolExecutor")
print("=" * 50)

print("ThreadPoolExecutor")
print("- 基于线程，共享内存空间")
print("- 受GIL限制，同一时间只能有一个线程执行Python代码")
print("- 适用于I/O密集型任务（如网络请求、文件读写）")
print("- 线程创建和切换开销较小")
print("- 内存消耗较小")

print("\nProcessPoolExecutor")
print("- 基于进程，每个进程有独立的内存空间")
print("- 不受GIL限制，可以充分利用多核CPU")
print("- 适用于CPU密集型任务（如计算密集型应用）")
print("- 进程创建和切换开销较大")
print("- 内存消耗较大")

print("\n统一接口")
print("- 两个执行器使用相同的API")
print("- 可以无缝切换，只需修改执行器类型")
print("- 提高代码的可维护性和可扩展性")

# ===========================
# 7. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("7. 最佳实践")
print("=" * 50)

print("1. 选择合适的执行器")
print("   - I/O密集型任务使用ThreadPoolExecutor")
print("   - CPU密集型任务使用ProcessPoolExecutor")
print("   - 可以通过简单修改执行器类型进行性能调优")

print("\n2. 合理设置线程/进程数量")
print("   - ThreadPoolExecutor: 对于I/O密集型任务，可以设置较多线程（如CPU核心数的2-4倍）")
print("   - ProcessPoolExecutor: 对于CPU密集型任务，通常设置为CPU核心数")
print("   - 使用os.cpu_count()获取CPU核心数")

print("\n3. 正确使用上下文管理器")
print("   - 使用with语句自动管理执行器的生命周期")
print("   - 确保资源正确释放")

print("\n4. 异常处理")
print("   - 捕获Future.result()可能抛出的异常")
print("   - 在任务函数内部添加异常处理")
print("   - 避免异常导致整个程序崩溃")

print("\n5. 任务设计")
print("   - 任务应该是独立的，避免共享状态")
print("   - 任务执行时间不宜过长")
print("   - 合理划分任务粒度")

print("\n6. 性能优化")
print("   - 避免任务间的频繁通信")
print("   - 减少锁的使用")
print("   - 合理使用缓存")

# ===========================
# 8. 与其他模块的比较
# ===========================
print("\n" + "=" * 50)
print("8. 与其他模块的比较")
print("=" * 50)

print("concurrent.futures vs threading/multiprocessing")
print("- concurrent.futures提供更高级的API，简化编程")
print("- threading/multiprocessing提供更底层的控制")
print("- concurrent.futures隐藏了线程/进程的创建和管理细节")
print("- threading/multiprocessing适用于需要精细控制的场景")

print("\nconcurrent.futures vs asyncio")
print("- concurrent.futures基于线程/进程，asyncio基于协程")
print("- concurrent.futures更适合CPU密集型或需要使用现有同步库的场景")
print("- asyncio更适合I/O密集型任务，效率更高")
print("- concurrent.futures提供更简单的API，asyncio提供更强大的功能")

# ===========================
# 9. 总结
# ===========================
print("\n" + "=" * 50)
print("9. 总结")
print("=" * 50)
print("concurrent.futures模块提供了高级并发编程接口")
print("简化了多线程和多进程编程，提高了开发效率")

print("\n主要功能:")
print("- ThreadPoolExecutor: 线程池执行器")
print("- ProcessPoolExecutor: 进程池执行器")
print("- Future对象: 表示异步执行的结果")
print("- 统一的API: 支持线程和进程的无缝切换")

print("\n应用场景:")
print("- 简化多线程和多进程编程")
print("- 批量处理任务")
print("- 异步执行任务")
print("- 提高程序性能")

print("\n使用concurrent.futures模块可以轻松实现并发编程")
print("是Python中处理并发任务的首选工具之一")
