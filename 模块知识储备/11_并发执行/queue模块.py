#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
queue模块 - 线程安全的队列实现

queue模块提供了线程安全的队列数据结构，用于在多线程环境中安全地传递数据。

主要功能包括：
- FIFO队列（先进先出）
- LIFO队列（后进先出/栈）
- 优先级队列
- 队列大小限制
- 超时支持
- 线程安全的put和get操作

使用场景：
- 生产者-消费者模式
- 任务调度和管理
- 线程间通信
- 工作池实现

官方文档：https://docs.python.org/3/library/queue.html
"""

import queue
import threading
import time
import random

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. queue模块基本介绍")
print("=" * 50)
print("queue模块提供线程安全的队列数据结构")
print("支持FIFO、LIFO和优先级队列三种模式")
print("所有操作都是线程安全的，可直接用于多线程环境")
print("提供超时机制，避免线程无限阻塞")
print("适用于生产者-消费者模式和任务调度")

# ===========================
# 2. FIFO队列 (Queue)
# ===========================
print("\n" + "=" * 50)
print("2. FIFO队列 (Queue)")
print("=" * 50)

# 示例1: 基本的FIFO队列操作
print("示例1: 基本的FIFO队列操作")

# 创建一个无界队列
fifo_queue = queue.Queue()

# 入队操作
fifo_queue.put("第一个元素")
fifo_queue.put("第二个元素")
fifo_queue.put("第三个元素")

# 获取队列大小
print(f"队列大小: {fifo_queue.qsize()}")

# 出队操作
while not fifo_queue.empty():
    item = fifo_queue.get()
    print(f"出队元素: {item}")
    fifo_queue.task_done()  # 标记任务完成

print(f"队列是否为空: {fifo_queue.empty()}")

# 示例2: 有界队列和阻塞操作
print("\n示例2: 有界队列和阻塞操作")

# 创建一个大小为3的有界队列
bounded_queue = queue.Queue(maxsize=3)

def producer(name):
    for i in range(5):
        item = f"{name}-{i+1}"
        print(f"生产者 {name} 尝试放入: {item}")
        bounded_queue.put(item)  # 当队列满时会阻塞
        print(f"生产者 {name} 成功放入: {item}, 队列大小: {bounded_queue.qsize()}")
        time.sleep(random.uniform(0.1, 0.3))

def consumer(name):
    for i in range(10):
        item = bounded_queue.get()  # 当队列为空时会阻塞
        print(f"消费者 {name} 获取: {item}, 队列大小: {bounded_queue.qsize()}")
        time.sleep(random.uniform(0.3, 0.6))
        bounded_queue.task_done()

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

# 等待生产者完成
producer1.join()
producer2.join()

# 等待队列中的所有项目被处理
bounded_queue.join()

print("所有生产者和消费者完成操作")

# ===========================
# 3. LIFO队列 (LifoQueue)
# ===========================
print("\n" + "=" * 50)
print("3. LIFO队列 (LifoQueue)")
print("=" * 50)

# 示例3: 基本的LIFO队列操作
print("示例3: 基本的LIFO队列操作")

# 创建LIFO队列（栈）
lifo_queue = queue.LifoQueue()

# 入栈操作
lifo_queue.put("第一个元素")
lifo_queue.put("第二个元素")
lifo_queue.put("第三个元素")

print(f"栈大小: {lifo_queue.qsize()}")

# 出栈操作
while not lifo_queue.empty():
    item = lifo_queue.get()
    print(f"出栈元素: {item}")
    lifo_queue.task_done()

# 示例4: LIFO队列在撤销操作中的应用
print("\n示例4: LIFO队列在撤销操作中的应用")

class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = queue.LifoQueue()  # 用于撤销操作的LIFO队列
    
    def add_text(self, new_text):
        # 保存当前状态到撤销栈
        self.undo_stack.put(self.text)
        self.text += new_text
        print(f"添加文本: '{new_text}'，当前文本: '{self.text}'")
    
    def undo(self):
        if not self.undo_stack.empty():
            previous_state = self.undo_stack.get()
            self.text = previous_state
            print(f"撤销操作，当前文本: '{self.text}'")
        else:
            print("没有可撤销的操作")

# 使用文本编辑器
editor = TextEditor()
editor.add_text("Hello")
editor.add_text(", ")
editor.add_text("World")
editor.undo()  # 撤销 "World"
editor.undo()  # 撤销 ", "
editor.add_text(" Python")

# ===========================
# 4. 优先级队列 (PriorityQueue)
# ===========================
print("\n" + "=" * 50)
print("4. 优先级队列 (PriorityQueue)")
print("=" * 50)

# 示例5: 基本的优先级队列操作
print("示例5: 基本的优先级队列操作")

# 创建优先级队列
priority_queue = queue.PriorityQueue()

# 入队操作（元素格式: (优先级, 数据)，优先级数值越小，优先级越高）
priority_queue.put((3, "低优先级任务"))
priority_queue.put((1, "高优先级任务"))
priority_queue.put((2, "中优先级任务"))
priority_queue.put((1, "另一个高优先级任务"))

print(f"优先级队列大小: {priority_queue.qsize()}")

# 出队操作（按优先级顺序）
while not priority_queue.empty():
    priority, item = priority_queue.get()
    print(f"出队元素: 优先级={priority}, 数据={item}")
    priority_queue.task_done()

# 示例6: 优先级队列在任务调度中的应用
print("\n示例6: 优先级队列在任务调度中的应用")

class Task:
    def __init__(self, name, priority, duration):
        self.name = name
        self.priority = priority  # 数值越小，优先级越高
        self.duration = duration
    
    def __lt__(self, other):
        # 用于PriorityQueue比较任务优先级
        return self.priority < other.priority
    
    def __str__(self):
        return f"{self.name} (优先级: {self.priority}, 耗时: {self.duration}秒)"

def task_worker(task_queue):
    while True:
        try:
            task = task_queue.get(timeout=1)
            print(f"开始执行任务: {task}")
            time.sleep(task.duration)
            print(f"完成任务: {task}")
            task_queue.task_done()
        except queue.Empty:
            break

# 创建任务队列和工作线程
task_queue = queue.PriorityQueue()
worker_thread = threading.Thread(target=task_worker, args=(task_queue,))

# 添加任务
for i in range(5):
    priority = random.randint(1, 5)  # 随机优先级
    duration = random.uniform(0.5, 2)  # 随机执行时间
    task = Task(f"任务{i+1}", priority, duration)
    task_queue.put(task)
    print(f"添加任务: {task}")

# 启动工作线程
worker_thread.start()

# 等待所有任务完成
task_queue.join()

# 等待工作线程结束
worker_thread.join()

print("所有任务处理完成")

# ===========================
# 5. 超时机制
# ===========================
print("\n" + "=" * 50)
print("5. 超时机制")
print("=" * 50)

# 示例7: 入队和出队的超时操作
print("示例7: 入队和出队的超时操作")

# 创建大小为2的有界队列
timeout_queue = queue.Queue(maxsize=2)

try:
    # 入队操作，设置超时时间
    timeout_queue.put("元素1", timeout=1)
    timeout_queue.put("元素2", timeout=1)
    print("成功放入前两个元素")
    
    # 尝试放入第三个元素，超时1秒
    timeout_queue.put("元素3", timeout=1)
    print("成功放入第三个元素")
except queue.Full:
    print("队列已满，放入操作超时")

try:
    # 出队操作，设置超时时间
    item = timeout_queue.get(timeout=0.5)
    print(f"成功获取元素: {item}")
    item = timeout_queue.get(timeout=0.5)
    print(f"成功获取元素: {item}")
    
    # 尝试获取第三个元素，超时0.5秒
    item = timeout_queue.get(timeout=0.5)
    print(f"成功获取元素: {item}")
except queue.Empty:
    print("队列为空，获取操作超时")

# 示例8: 非阻塞操作
print("\n示例8: 非阻塞操作")

non_blocking_queue = queue.Queue(maxsize=1)

# 非阻塞入队
try:
    non_blocking_queue.put("元素1", block=False)
    print("成功放入元素1")
    non_blocking_queue.put("元素2", block=False)
    print("成功放入元素2")
except queue.Full:
    print("队列已满，非阻塞入队失败")

# 非阻塞出队
try:
    item = non_blocking_queue.get(block=False)
    print(f"成功获取元素: {item}")
    item = non_blocking_queue.get(block=False)
    print(f"成功获取元素: {item}")
except queue.Empty:
    print("队列为空，非阻塞出队失败")

# ===========================
# 6. 生产者-消费者模式完整实现
# ===========================
print("\n" + "=" * 50)
print("6. 生产者-消费者模式完整实现")
print("=" * 50)

# 创建工作队列和结果队列
work_queue = queue.Queue(maxsize=10)
result_queue = queue.Queue()

# 控制标志
STOP_SIGNAL = "STOP"
NUM_PRODUCERS = 3
NUM_CONSUMERS = 2
NUM_ITEMS = 15

def producer(producer_id):
    """生产者函数"""
    for i in range(NUM_ITEMS // NUM_PRODUCERS):
        # 生成项目
        item = f"{producer_id}-{i+1}"
        
        # 放入工作队列
        work_queue.put(item)
        print(f"生产者 {producer_id} 生产了: {item}")
        
        # 随机休眠
        time.sleep(random.uniform(0.1, 0.5))
    
    print(f"生产者 {producer_id} 完成任务")

def consumer(consumer_id):
    """消费者函数"""
    processed_count = 0
    
    while True:
        try:
            # 从工作队列获取项目，超时1秒
            item = work_queue.get(timeout=1)
            
            # 检查是否是停止信号
            if item == STOP_SIGNAL:
                # 重新放入停止信号，以便其他消费者也能看到
                work_queue.put(STOP_SIGNAL)
                break
            
            # 模拟处理时间
            time.sleep(random.uniform(0.2, 0.8))
            
            # 处理结果
            result = f"processed-{item}"
            result_queue.put(result)
            
            processed_count += 1
            print(f"消费者 {consumer_id} 处理了: {item} -> {result}")
            
            # 标记任务完成
            work_queue.task_done()
            
        except queue.Empty:
            # 队列为空，退出循环
            break
    
    print(f"消费者 {consumer_id} 完成任务，共处理 {processed_count} 个项目")

# 创建并启动生产者线程
producers = []
for i in range(NUM_PRODUCERS):
    p = threading.Thread(target=producer, args=(f"P{i+1}",))
    producers.append(p)
    p.start()

# 创建并启动消费者线程
consumers = []
for i in range(NUM_CONSUMERS):
    c = threading.Thread(target=consumer, args=(f"C{i+1}",))
    consumers.append(c)
    c.start()

# 等待所有生产者完成
for p in producers:
    p.join()

# 向工作队列添加停止信号
work_queue.put(STOP_SIGNAL)

# 等待所有消费者完成
for c in consumers:
    c.join()

# 收集并打印结果
print("\n处理结果:")
results = []
while not result_queue.empty():
    results.append(result_queue.get())

results.sort()
for result in results:
    print(f"  {result}")

print(f"\n总共处理了 {len(results)} 个项目")

# ===========================
# 7. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("7. 实际应用示例")
print("=" * 50)

# 示例9: 任务调度器
print("示例9: 任务调度器")

class TaskScheduler:
    def __init__(self):
        self.task_queue = queue.Queue()
        self.is_running = False
        self.worker_thread = None
    
    def add_task(self, task_func, *args, **kwargs):
        """添加任务到队列"""
        task = (task_func, args, kwargs)
        self.task_queue.put(task)
        print(f"添加任务: {task_func.__name__}")
    
    def _worker(self):
        """工作线程函数"""
        while self.is_running or not self.task_queue.empty():
            try:
                # 获取任务，超时1秒
                task_func, args, kwargs = self.task_queue.get(timeout=1)
                
                # 执行任务
                print(f"开始执行任务: {task_func.__name__}")
                result = task_func(*args, **kwargs)
                print(f"任务执行完成: {task_func.__name__}, 结果: {result}")
                
                # 标记任务完成
                self.task_queue.task_done()
                
            except queue.Empty:
                continue
    
    def start(self):
        """启动调度器"""
        if not self.is_running:
            self.is_running = True
            self.worker_thread = threading.Thread(target=self._worker)
            self.worker_thread.start()
            print("调度器已启动")
    
    def stop(self):
        """停止调度器"""
        if self.is_running:
            self.is_running = False
            if self.worker_thread:
                self.worker_thread.join()
            print("调度器已停止")
    
    def wait_completion(self):
        """等待所有任务完成"""
        self.task_queue.join()

# 定义一些任务函数
def task1():
    time.sleep(1)
    return "Task 1 completed"

def task2(name):
    time.sleep(0.5)
    return f"Task 2 completed for {name}"

def task3(a, b):
    time.sleep(1.5)
    return f"Task 3 completed: {a} + {b} = {a + b}"

# 使用任务调度器
scheduler = TaskScheduler()
scheduler.start()

# 添加任务
scheduler.add_task(task1)
scheduler.add_task(task2, "Alice")
scheduler.add_task(task3, 10, 20)
scheduler.add_task(task1)
scheduler.add_task(task2, "Bob")

# 等待所有任务完成
scheduler.wait_completion()

# 停止调度器
scheduler.stop()

# 示例10: 并行下载管理器
print("\n示例10: 并行下载管理器")

def download_file(url):
    """模拟下载文件"""
    print(f"开始下载: {url}")
    time.sleep(random.uniform(0.5, 2))  # 模拟下载时间
    return f"{url} 下载完成"

class DownloadManager:
    def __init__(self, max_workers=3):
        self.max_workers = max_workers
        self.download_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.workers = []
        self.is_running = False
    
    def add_download(self, url):
        """添加下载任务"""
        self.download_queue.put(url)
    
    def _worker(self):
        """下载工作线程"""
        while self.is_running or not self.download_queue.empty():
            try:
                url = self.download_queue.get(timeout=1)
                result = download_file(url)
                self.result_queue.put(result)
                self.download_queue.task_done()
            except queue.Empty:
                continue
    
    def start(self):
        """启动下载管理器"""
        if not self.is_running:
            self.is_running = True
            # 创建并启动工作线程
            for i in range(self.max_workers):
                worker = threading.Thread(target=self._worker)
                self.workers.append(worker)
                worker.start()
    
    def stop(self):
        """停止下载管理器"""
        if self.is_running:
            self.is_running = False
            for worker in self.workers:
                worker.join()
            self.workers.clear()
    
    def wait_completion(self):
        """等待所有下载完成"""
        self.download_queue.join()
        
        # 收集结果
        results = []
        while not self.result_queue.empty():
            results.append(self.result_queue.get())
        
        return results

# 使用下载管理器
manager = DownloadManager(max_workers=2)

# 添加下载任务
urls = [
    "http://example.com/file1.txt",
    "http://example.com/file2.txt",
    "http://example.com/file3.txt",
    "http://example.com/file4.txt",
    "http://example.com/file5.txt"
]

for url in urls:
    manager.add_download(url)

# 启动下载并等待完成
manager.start()
results = manager.wait_completion()
manager.stop()

print("\n下载结果:")
for result in results:
    print(f"  {result}")

# ===========================
# 8. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("8. 最佳实践和注意事项")
print("=" * 50)

print("1. 线程安全使用")
print("   - queue模块的所有操作都是线程安全的，可以直接用于多线程环境")
print("   - 不要在队列操作之外修改队列内容")
print("   - 避免在队列元素中共享可变对象，除非能确保线程安全")

print("\n2. 队列大小管理")
print("   - 对于生产者速度可能超过消费者的场景，使用有界队列(maxsize>0)")
print("   - 无界队列可能导致内存耗尽，谨慎使用")
print("   - 根据系统资源和性能需求调整队列大小")

print("\n3. 超时机制")
print("   - 使用超时参数(put/get)避免线程无限阻塞")
print("   - 根据应用场景选择合适的超时时间")
print("   - 考虑使用block=False进行非阻塞操作")

print("\n4. 任务完成标记")
print("   - 每次调用get()后，应调用task_done()标记任务完成")
print("   - 使用join()等待所有任务完成")
print("   - 确保task_done()的调用次数与get()一致")

print("\n5. 异常处理")
print("   - 捕获queue.Empty和queue.Full异常")
print("   - 在线程中处理异常，避免线程意外终止")
print("   - 考虑使用守护线程或显式停止机制")

print("\n6. 性能考虑")
print("   - 队列操作虽然线程安全，但存在锁开销")
print("   - 避免在队列中存储过大的对象")
print("   - 考虑批量处理以减少队列操作次数")

print("\n7. 选择合适的队列类型")
print("   - FIFO队列: 一般的任务调度，生产者-消费者模式")
print("   - LIFO队列: 撤销操作，递归处理")
print("   - 优先级队列: 基于优先级的任务调度")

# ===========================
# 9. 与其他模块的比较
# ===========================
print("\n" + "=" * 50)
print("9. 与其他模块的比较")
print("=" * 50)

print("queue vs collections.deque")
print("- queue模块提供线程安全的队列实现")
print("- collections.deque提供更高效的双端队列，但不是线程安全的")
print("- queue有更多的同步机制和超时支持")
print("- deque适用于单线程环境，queue适用于多线程环境")

print("\nqueue vs asyncio.Queue")
print("- queue模块适用于多线程编程")
print("- asyncio.Queue适用于异步编程(协程)")
print("- 两者都提供类似的API，但底层实现不同")
print("- queue使用线程锁，asyncio.Queue使用事件循环")

print("\nqueue vs multiprocessing.Queue")
print("- queue模块适用于多线程间通信")
print("- multiprocessing.Queue适用于多进程间通信")
print("- multiprocessing.Queue需要序列化数据")
print("- queue的性能通常比multiprocessing.Queue好")

# ===========================
# 10. 总结
# ===========================
print("\n" + "=" * 50)
print("10. 总结")
print("=" * 50)
print("queue模块提供了线程安全的队列数据结构")
print("支持FIFO、LIFO和优先级队列三种模式")
print("所有操作都是线程安全的，可直接用于多线程环境")
print("提供超时机制，避免线程无限阻塞")

print("\n主要功能:")
print("- 线程安全的队列操作")
print("- 队列大小限制")
print("- 超时支持")
print("- 任务完成标记")
print("- 多种队列类型")

print("\n应用场景:")
print("- 生产者-消费者模式")
print("- 任务调度和管理")
print("- 线程间通信")
print("- 工作池实现")
print("- 并行处理")

print("\nqueue模块是Python多线程编程中实现线程间通信和任务管理的重要工具")
print("合理使用queue模块可以简化多线程编程，提高代码的可靠性和可维护性")
