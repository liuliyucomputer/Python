#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
threading模块 - 多线程编程

threading模块提供了创建和管理线程的功能，允许在一个进程内同时执行多个任务。

主要功能包括：
- 线程的创建和启动
- 线程同步（锁、信号量、事件等）
- 线程通信（队列等）
- 线程本地存储
- 线程池（Python 3.2+）

使用场景：
- I/O密集型任务（如文件读写、网络请求等）
- 需要并发执行但不需要大量内存隔离的任务
- 提高程序响应性

官方文档：https://docs.python.org/3/library/threading.html
"""

import threading
import time
import random
import queue
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. threading模块基本介绍")
print("=" * 50)
print("threading模块提供创建和管理线程的功能")
print("允许在一个进程内同时执行多个任务")
print("线程共享进程的内存空间，但有独立的执行栈")
print("受GIL（全局解释器锁）限制，同一时间只能有一个线程执行Python字节码")
print("适合I/O密集型任务，不适合CPU密集型任务")
print(f"当前进程ID: {os.getpid()}")

# ===========================
# 2. 线程创建与启动
# ===========================
print("\n" + "=" * 50)
print("2. 线程创建与启动")
print("=" * 50)

# 示例1: 使用Thread类创建线程
print("示例1: 使用Thread类创建线程")

def thread_function(name):
    print(f"线程 {name} 开始")
    time.sleep(1)
    print(f"线程 {name} 结束")

# 创建线程
thread1 = threading.Thread(target=thread_function, args=("A",))
thread2 = threading.Thread(target=thread_function, args=("B",))

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

print("主线程结束")

# 示例2: 继承Thread类创建线程
print("\n示例2: 继承Thread类创建线程")

class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def run(self):
        print(f"自定义线程 {self.name} 开始")
        time.sleep(1)
        print(f"自定义线程 {self.name} 结束")

# 创建并启动线程
thread3 = MyThread("C")
thread4 = MyThread("D")

thread3.start()
thread4.start()

thread3.join()
thread4.join()

print("主线程结束")

# 示例3: 线程参数传递
print("\n示例3: 线程参数传递")

def worker(**kwargs):
    name = kwargs.get("name", "未知")
    count = kwargs.get("count", 5)
    
    for i in range(count):
        print(f"{name} 执行第 {i+1} 次")
        time.sleep(0.5)

# 使用关键字参数
thread5 = threading.Thread(target=worker, kwargs={"name": "工作线程", "count": 3})
thread5.start()
thread5.join()

# ===========================
# 3. 线程同步 - 锁
# ===========================
print("\n" + "=" * 50)
print("3. 线程同步 - 锁")
print("=" * 50)

# 示例4: 使用Lock保护共享资源
print("示例4: 使用Lock保护共享资源")

# 共享变量
shared_counter = 0
lock = threading.Lock()

def increment_counter():
    global shared_counter
    for _ in range(1000):
        with lock:  # 自动获取和释放锁
            shared_counter += 1

# 创建多个线程
threads = []
for i in range(10):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print(f"最终计数器值: {shared_counter}")
print(f"预期计数器值: {10 * 1000}")

# 示例5: 使用RLock（可重入锁）
print("\n示例5: 使用RLock（可重入锁）")

rlock = threading.RLock()

def nested_function():
    with rlock:
        print("在嵌套函数中获取了RLock")

def outer_function():
    with rlock:
        print("在外部函数中获取了RLock")
        nested_function()

thread6 = threading.Thread(target=outer_function)
thread6.start()
thread6.join()

# ===========================
# 4. 线程同步 - 信号量
# ===========================
print("\n" + "=" * 50)
print("4. 线程同步 - 信号量")
print("=" * 50)

# 示例6: 使用Semaphore限制并发数
print("示例6: 使用Semaphore限制并发数")

# 创建信号量，限制最多3个线程同时执行
max_concurrent = 3
semaphore = threading.Semaphore(max_concurrent)

def limited_function(name):
    with semaphore:
        print(f"线程 {name} 进入临界区")
        time.sleep(random.uniform(0.5, 1.5))
        print(f"线程 {name} 离开临界区")

# 创建10个线程
threads = []
for i in range(10):
    thread = threading.Thread(target=limited_function, args=(f"T{i}",))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print("所有线程执行完成")

# ===========================
# 5. 线程同步 - 事件
# ===========================
print("\n" + "=" * 50)
print("5. 线程同步 - 事件")
print("=" * 50)

# 示例7: 使用Event进行线程通信
print("示例7: 使用Event进行线程通信")

# 创建事件
event = threading.Event()

def wait_for_event(name):
    print(f"线程 {name} 等待事件")
    event.wait()  # 等待事件被设置
    print(f"线程 {name} 收到事件信号")

def trigger_event():
    print("触发线程开始工作")
    time.sleep(2)
    print("触发事件")
    event.set()  # 设置事件

# 创建线程
thread7 = threading.Thread(target=wait_for_event, args=("等待者1",))
thread8 = threading.Thread(target=wait_for_event, args=("等待者2",))
thread9 = threading.Thread(target=trigger_event)

# 启动线程
thread7.start()
thread8.start()
thread9.start()

# 等待所有线程完成
thread7.join()
thread8.join()
thread9.join()

# 重置事件（可选）
event.clear()

# ===========================
# 6. 线程同步 - 条件变量
# ===========================
print("\n" + "=" * 50)
print("6. 线程同步 - 条件变量")
print("=" * 50)

# 示例8: 使用Condition进行生产者-消费者模式
print("示例8: 使用Condition进行生产者-消费者模式")

# 共享队列
product_queue = []
max_queue_size = 5

# 创建条件变量
condition = threading.Condition()

def producer(name):
    for i in range(10):
        with condition:
            # 等待队列不满
            while len(product_queue) >= max_queue_size:
                print(f"队列已满，生产者 {name} 等待")
                condition.wait()  # 释放锁并等待
            
            # 生产产品
            product = f"产品{i+1}"
            product_queue.append(product)
            print(f"生产者 {name} 生产: {product}, 队列: {product_queue}")
            
            # 通知消费者
            condition.notify_all()
        
        time.sleep(random.uniform(0.1, 0.5))

def consumer(name):
    for i in range(10):
        with condition:
            # 等待队列不空
            while len(product_queue) == 0:
                print(f"队列空，消费者 {name} 等待")
                condition.wait()  # 释放锁并等待
            
            # 消费产品
            product = product_queue.pop(0)
            print(f"消费者 {name} 消费: {product}, 队列: {product_queue}")
            
            # 通知生产者
            condition.notify_all()
        
        time.sleep(random.uniform(0.1, 0.5))

# 创建生产者和消费者线程
producer1 = threading.Thread(target=producer, args=("P1",))
producer2 = threading.Thread(target=producer, args=("P2",))
consumer1 = threading.Thread(target=consumer, args=("C1",))
consumer2 = threading.Thread(target=consumer, args=("C2",))

# 启动线程
producer1.start()
producer2.start()
consumer1.start()
consumer2.start()

# 等待所有线程完成
producer1.join()
producer2.join()
consumer1.join()
consumer2.join()

print("生产消费活动结束")

# ===========================
# 7. 线程通信 - 队列
# ===========================
print("\n" + "=" * 50)
print("7. 线程通信 - 队列")
print("=" * 50)

# 示例9: 使用Queue进行线程通信
print("示例9: 使用Queue进行线程通信")

# 创建线程安全的队列
message_queue = queue.Queue(maxsize=10)

def message_producer(name):
    for i in range(5):
        message = f"消息 {i+1} 来自 {name}"
        message_queue.put(message)
        print(f"生产者 {name} 发送: {message}")
        time.sleep(random.uniform(0.1, 0.5))

def message_consumer(name):
    for i in range(10):
        message = message_queue.get()
        print(f"消费者 {name} 接收: {message}")
        message_queue.task_done()  # 标记任务完成
        time.sleep(random.uniform(0.2, 0.8))

# 创建生产者和消费者线程
producer_a = threading.Thread(target=message_producer, args=("A",))
producer_b = threading.Thread(target=message_producer, args=("B",))
consumer_x = threading.Thread(target=message_consumer, args=("X",))
consumer_y = threading.Thread(target=message_consumer, args=("Y",))

# 启动线程
producer_a.start()
producer_b.start()
consumer_x.start()
consumer_y.start()

# 等待所有生产者完成
producer_a.join()
producer_b.join()

# 等待队列中的所有消息被处理
message_queue.join()

print("所有消息处理完成")

# ===========================
# 8. 线程本地存储
# ===========================
print("\n" + "=" * 50)
print("8. 线程本地存储")
print("=" * 50)

# 示例10: 使用ThreadLocal存储线程私有数据
print("示例10: 使用ThreadLocal存储线程私有数据")

# 创建线程本地存储
local_data = threading.local()

def thread_specific_data(name):
    # 设置线程本地数据
    local_data.value = f"{name}的私有数据"
    print(f"线程 {name} 设置本地数据: {local_data.value}")
    
    # 模拟处理时间
    time.sleep(0.5)
    
    # 读取线程本地数据
    print(f"线程 {name} 读取本地数据: {local_data.value}")

# 创建线程
thread10 = threading.Thread(target=thread_specific_data, args=("T1",))
thread11 = threading.Thread(target=thread_specific_data, args=("T2",))

thread10.start()
thread11.start()

thread10.join()
thread11.join()

# ===========================
# 9. 线程池
# ===========================
print("\n" + "=" * 50)
print("9. 线程池")
print("=" * 50)

# 示例11: 使用ThreadPoolExecutor（来自concurrent.futures模块）
print("示例11: 使用ThreadPoolExecutor")

from concurrent.futures import ThreadPoolExecutor

def task_function(task_id):
    print(f"开始执行任务 {task_id}")
    time.sleep(random.uniform(0.5, 1.5))
    print(f"完成任务 {task_id}")
    return f"任务 {task_id} 的结果"

# 创建线程池，最大工作线程数为4
with ThreadPoolExecutor(max_workers=4) as executor:
    # 提交任务
    tasks = [executor.submit(task_function, i) for i in range(10)]
    
    # 获取结果
    for future in tasks:
        result = future.result()
        print(f"获取结果: {result}")

# ===========================
# 10. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("10. 实际应用示例")
print("=" * 50)

# 示例12: 多线程下载文件
print("示例12: 多线程下载文件")

# 模拟下载函数
def download_file(url, file_name):
    print(f"开始下载 {url} 到 {file_name}")
    time.sleep(random.uniform(1, 2.5))  # 模拟下载时间
    print(f"完成下载 {file_name}")
    return f"{file_name} 已下载"

# 要下载的文件列表
files_to_download = [
    ("https://example.com/file1.txt", "file1.txt"),
    ("https://example.com/file2.txt", "file2.txt"),
    ("https://example.com/file3.txt", "file3.txt"),
    ("https://example.com/file4.txt", "file4.txt"),
    ("https://example.com/file5.txt", "file5.txt")
]

# 使用线程池下载
with ThreadPoolExecutor(max_workers=3) as executor:
    # 提交下载任务
    futures = [executor.submit(download_file, url, file_name) 
              for url, file_name in files_to_download]
    
    # 获取下载结果
    results = [future.result() for future in futures]
    
    print("\n下载结果:")
    for result in results:
        print(result)

# 示例13: 多线程处理任务队列
print("\n示例13: 多线程处理任务队列")

# 创建任务队列
task_queue = queue.Queue()
result_queue = queue.Queue()

def task_worker(worker_id):
    while True:
        try:
            # 从队列获取任务，超时1秒
            task = task_queue.get(timeout=1)
            
            # 处理任务
            print(f"工作线程 {worker_id} 处理任务: {task}")
            time.sleep(random.uniform(0.5, 1.5))  # 模拟处理时间
            result = f"任务 {task} 的处理结果"
            
            # 将结果放入结果队列
            result_queue.put(result)
            task_queue.task_done()  # 标记任务完成
            
        except queue.Empty:
            # 队列为空，退出循环
            break

# 创建工作线程
num_workers = 4
workers = []
for i in range(num_workers):
    worker = threading.Thread(target=task_worker, args=(i,))
    workers.append(worker)
    worker.start()

# 添加任务到队列
for i in range(10):
    task_queue.put(i+1)

# 等待所有任务完成
task_queue.join()

# 收集结果
results = []
while not result_queue.empty():
    results.append(result_queue.get())

# 等待所有工作线程结束
for worker in workers:
    worker.join()

print("\n任务处理结果:")
for result in results:
    print(result)

# 示例14: 简单的多线程Web服务器
print("\n示例14: 简单的多线程Web服务器")

try:
    import http.server
    import socketserver
    
    # 定义请求处理器
    class MyHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, World! This is a multi-threaded server.")
    
    # 配置服务器
    PORT = 8888
    Handler = MyHandler
    
    # 创建多线程服务器
    with socketserver.ThreadingTCPServer(("", PORT), Handler) as httpd:
        print(f"多线程Web服务器运行在端口 {PORT}")
        print("注意: 服务器不会实际运行，仅展示代码示例")
        # httpd.serve_forever()  # 取消注释以实际运行服务器
        
except ImportError:
    print("注意: 无法导入所需模块，无法演示Web服务器示例")

# ===========================
# 11. 线程安全与最佳实践
# ===========================
print("\n" + "=" * 50)
print("11. 线程安全与最佳实践")
print("=" * 50)

print("1. 线程安全")
print("   - 避免共享可变状态")
print("   - 使用线程同步机制保护共享资源")
print("   - 优先使用线程安全的数据结构（如queue.Queue）")

print("\n2. 避免死锁")
print("   - 避免嵌套锁")
print("   - 按固定顺序获取锁")
print("   - 设置锁的超时时间")

print("\n3. 线程管理")
print("   - 始终使用join()等待线程完成")
print("   - 避免创建过多线程")
print("   - 考虑使用线程池管理线程")

print("\n4. 性能考虑")
print("   - 线程适合I/O密集型任务")
print("   - CPU密集型任务应考虑使用多进程")
print("   - 减少线程间通信，通信开销较大")

print("\n5. 调试技巧")
print("   - 使用logging模块记录线程活动")
print("   - 使用threading.enumerate()查看所有活动线程")
print("   - 使用threading.active_count()查看活动线程数")

# ===========================
# 12. 与multiprocessing的比较
# ===========================
print("\n" + "=" * 50)
print("12. 与multiprocessing的比较")
print("=" * 50)

print("threading vs multiprocessing")
print("1. 内存使用")
print("   - threading: 线程共享进程内存，内存使用较少")
print("   - multiprocessing: 每个进程有独立内存空间，内存使用较多")

print("\n2. CPU利用率")
print("   - threading: 受GIL限制，同一时间只能有一个线程执行Python代码")
print("   - multiprocessing: 不受GIL限制，可以充分利用多核CPU")

print("\n3. 通信开销")
print("   - threading: 线程间通信通过共享内存，开销较小")
print("   - multiprocessing: 进程间通信需要序列化和反序列化，开销较大")

print("\n4. 安全性")
print("   - threading: 共享内存可能导致竞态条件，需要同步机制")
print("   - multiprocessing: 独立内存空间更安全，不易出现竞态条件")

print("\n5. 适用场景")
print("   - threading: I/O密集型任务")
print("   - multiprocessing: CPU密集型任务")

# ===========================
# 13. 总结
# ===========================
print("\n" + "=" * 50)
print("13. 总结")
print("=" * 50)
print("threading模块提供了创建和管理线程的功能")
print("适合I/O密集型任务，提高程序响应性")
print("受GIL限制，不适合CPU密集型任务")

print("\n主要功能:")
print("- 线程的创建和启动")
print("- 线程同步机制（锁、信号量、事件、条件变量）")
print("- 线程通信（队列）")
print("- 线程本地存储")
print("- 线程池")

print("\n应用场景:")
print("- 文件读写")
print("- 网络请求")
print("- 提高GUI应用程序响应性")
print("- 简单的并发任务处理")

print("\n使用threading模块可以实现高效的并发编程")
print("但需要注意线程安全和避免死锁等问题")
