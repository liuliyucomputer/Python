# queue模块 - 队列数据结构和线程同步
# 功能作用：提供线程安全的队列实现，用于在多线程环境中进行数据交换和线程同步
# 使用情景：生产者-消费者模式、任务调度、多线程数据处理流水线、线程池实现等
# 注意事项：队列是线程安全的，但不是进程安全的；需要注意阻塞和超时参数的使用；队列大小限制可能导致阻塞；在多进程环境中应使用multiprocessing.Queue

import queue
import threading
import time
import random
import sys
from collections import deque

# 模块概述
"""
queue模块提供了线程安全的队列实现，主要用于在多线程环境中安全地交换数据。
该模块实现了三种类型的队列：

1. Queue - 先进先出队列(FIFO)：元素按照添加顺序被检索
2. LifoQueue - 后进先出队列(LIFO)：类似于栈，最后添加的元素最先被检索
3. PriorityQueue - 优先级队列：元素按照优先级顺序被检索，最低优先级的元素最先被检索

这些队列都实现了锁原语，因此可以安全地在多线程环境中使用。
此外，该模块还提供了两种专用对象：

4. SimpleQueue - 简单队列，是一个无界的FIFO队列，没有大小限制
5. Empty 和 Full 异常 - 用于处理队列操作时可能出现的异常

queue模块适用于生产者-消费者模式、任务调度系统、多线程数据处理流水线等场景，
是Python多线程编程中实现线程间通信的重要工具。
"""

# 1. 基本队列类型
print("=== 1. 基本队列类型 ===")

def basic_queue_types():
    """演示queue模块中基本队列类型的使用"""
    print("queue模块提供三种主要队列类型：\n")
    
    # 1. Queue - 先进先出队列
    print("1. Queue - 先进先出队列 (FIFO)")
    print("   - 元素按照添加顺序被检索")
    print("   - 类似排队，先来先服务")
    
    # 创建一个最大容量为3的队列
    fifo_queue = queue.Queue(maxsize=3)
    print(f"创建最大容量为3的FIFO队列: {fifo_queue}")
    
    # 添加元素到队列
    print("添加元素到队列:")
    for i in range(1, 4):
        fifo_queue.put(i)
        print(f"  放入: {i}, 队列大小: {fifo_queue.qsize()}")
    
    # 检查队列是否已满
    print(f"队列是否已满: {fifo_queue.full()}")
    
    # 从队列中获取元素
    print("从队列中获取元素:")
    while not fifo_queue.empty():
        item = fifo_queue.get()
        print(f"  获取: {item}, 队列大小: {fifo_queue.qsize()}")
    
    print(f"队列是否为空: {fifo_queue.empty()}")
    
    # 2. LifoQueue - 后进先出队列
    print("\n2. LifoQueue - 后进先出队列 (LIFO)")
    print("   - 最后添加的元素最先被检索")
    print("   - 类似栈的操作")
    
    # 创建一个后进先出队列
    lifo_queue = queue.LifoQueue(maxsize=3)
    print(f"创建最大容量为3的LIFO队列: {lifo_queue}")
    
    # 添加元素到队列
    print("添加元素到队列:")
    for i in range(1, 4):
        lifo_queue.put(i)
        print(f"  放入: {i}, 队列大小: {lifo_queue.qsize()}")
    
    # 从队列中获取元素 (注意顺序与FIFO不同)
    print("从队列中获取元素 (注意顺序):")
    while not lifo_queue.empty():
        item = lifo_queue.get()
        print(f"  获取: {item}, 队列大小: {lifo_queue.qsize()}")
    
    # 3. PriorityQueue - 优先级队列
    print("\n3. PriorityQueue - 优先级队列")
    print("   - 元素按照优先级排序，最低优先级的元素最先被检索")
    print("   - 元素通常是(优先级, 数据)的元组，优先级为可比较的数值")
    
    # 创建一个优先级队列
    priority_queue = queue.PriorityQueue(maxsize=4)
    print(f"创建最大容量为4的优先级队列: {priority_queue}")
    
    # 添加元素到队列 (优先级, 数据)
    print("添加元素到队列 (优先级, 数据):")
    priority_queue.put((3, '中等优先级任务'))
    print(f"  放入: (3, '中等优先级任务'), 队列大小: {priority_queue.qsize()}")
    
    priority_queue.put((1, '高优先级任务'))
    print(f"  放入: (1, '高优先级任务'), 队列大小: {priority_queue.qsize()}")
    
    priority_queue.put((5, '低优先级任务'))
    print(f"  放入: (5, '低优先级任务'), 队列大小: {priority_queue.qsize()}")
    
    priority_queue.put((3, '另一个中等优先级任务'))
    print(f"  放入: (3, '另一个中等优先级任务'), 队列大小: {priority_queue.qsize()}")
    
    # 从队列中获取元素 (按优先级顺序)
    print("从队列中获取元素 (按优先级顺序):")
    while not priority_queue.empty():
        priority, task = priority_queue.get()
        print(f"  获取: (优先级={priority}, 任务='{task}'), 队列大小: {priority_queue.qsize()}")
    
    # 4. SimpleQueue - 简单队列
    print("\n4. SimpleQueue - 简单队列")
    print("   - 无界的FIFO队列，没有大小限制")
    print("   - 提供put()和get()方法，但没有task_done()和join()方法")
    
    # 创建一个简单队列
    simple_queue = queue.SimpleQueue()
    print(f"创建简单队列: {simple_queue}")
    
    # 添加元素到队列
    print("添加元素到队列:")
    for i in range(1, 4):
        simple_queue.put(i)
        print(f"  放入: {i}")
    
    # 从队列中获取元素
    print("从队列中获取元素:")
    for _ in range(3):
        item = simple_queue.get()
        print(f"  获取: {item}")
    
    # 注意SimpleQueue没有qsize()、full()和empty()方法
    print("注意: SimpleQueue不提供qsize(), full()和empty()方法")
    
    # 5. 队列异常
    print("\n5. 队列异常")
    print("   - Empty: 当队列空时调用get()且block=False时抛出")
    print("   - Full: 当队列满时调用put()且block=False时抛出")
    
    # 创建一个容量为1的队列
    small_queue = queue.Queue(maxsize=1)
    
    # 添加一个元素使队列满
    small_queue.put('item')
    print("队列已添加一个元素，现在已满")
    
    # 测试Full异常
    print("测试Full异常:")
    try:
        small_queue.put('another item', block=False)
    except queue.Full:
        print("  捕获到Full异常: 队列已满")
    
    # 清空队列
    small_queue.get()
    print("队列已清空")
    
    # 测试Empty异常
    print("测试Empty异常:")
    try:
        small_queue.get(block=False)
    except queue.Empty:
        print("  捕获到Empty异常: 队列为空")

# 运行基本队列类型演示
basic_queue_types()
print()

# 2. 队列的高级方法
print("=== 2. 队列的高级方法 ===")

def queue_advanced_methods():
    """演示队列的高级方法"""
    print("队列对象提供的高级方法：\n")
    
    # 1. task_done() 和 join() 方法
    print("1. task_done() 和 join() 方法")
    print("   - task_done(): 通知队列一个任务已完成处理")
    print("   - join(): 阻塞直到队列中所有任务都被处理完成")
    
    # 创建一个队列
    work_queue = queue.Queue()
    
    # 模拟工作线程处理队列中的任务
    def worker():
        """模拟工作线程"""
        print(f"  工作线程 {threading.current_thread().name} 启动")
        while True:
            try:
                task = work_queue.get(timeout=2)  # 设置超时以避免永久阻塞
                print(f"  工作线程 {threading.current_thread().name} 处理任务: {task}")
                # 模拟工作
                time.sleep(0.5)
                work_queue.task_done()  # 通知任务完成
                print(f"  工作线程 {threading.current_thread().name} 完成任务: {task}")
            except queue.Empty:
                print(f"  工作线程 {threading.current_thread().name} 超时退出")
                break
    
    # 创建两个工作线程
    for i in range(2):
        t = threading.Thread(target=worker, name=f"Worker-{i+1}")
        t.daemon = True  # 设置为守护线程，主程序结束时自动终止
        t.start()
    
    # 添加任务到队列
    print("添加任务到队列:")
    for i in range(1, 6):
        task = f"任务-{i}"
        work_queue.put(task)
        print(f"  添加任务: {task}")
    
    # 等待所有任务完成
    print("等待所有任务完成...")
    work_queue.join()
    print("所有任务已完成")
    
    # 给工作线程一点时间来检测队列为空
    time.sleep(1)
    
    # 2. put() 和 get() 的阻塞和超时参数
    print("\n2. put() 和 get() 的阻塞和超时参数")
    print("   - block=True: 当队列满/空时阻塞")
    print("   - block=False: 当队列满/空时立即抛出异常")
    print("   - timeout: 设置阻塞的最大时间")
    
    # 创建一个容量为2的队列
    small_queue = queue.Queue(maxsize=2)
    
    # 添加元素使队列满
    small_queue.put('item1')
    small_queue.put('item2')
    print("队列已满")
    
    # 测试 put() 方法的超时参数
    print("测试put()的超时参数:")
    try:
        start_time = time.time()
        print(f"  尝试添加元素，超时时间设置为1秒...")
        small_queue.put('item3', timeout=1)
    except queue.Full:
        elapsed = time.time() - start_time
        print(f"  捕获到Full异常，耗时: {elapsed:.2f}秒")
    
    # 清空队列
    small_queue.get()
    small_queue.get()
    print("队列已清空")
    
    # 测试 get() 方法的超时参数
    print("测试get()的超时参数:")
    try:
        start_time = time.time()
        print(f"  尝试获取元素，超时时间设置为1秒...")
        small_queue.get(timeout=1)
    except queue.Empty:
        elapsed = time.time() - start_time
        print(f"  捕获到Empty异常，耗时: {elapsed:.2f}秒")
    
    # 3. 非阻塞操作
    print("\n3. 非阻塞操作 (block=False)")
    print("   - 队列满/空时不等待，立即返回或抛出异常")
    
    # 测试非阻塞 put()
    print("测试非阻塞put():")
    small_queue.put('item1')
    small_queue.put('item2')
    print("  队列已满")
    
    try:
        print("  尝试非阻塞添加元素...")
        small_queue.put('item3', block=False)
    except queue.Full:
        print("  捕获到Full异常: 队列已满")
    
    # 测试非阻塞 get()
    print("测试非阻塞get():")
    small_queue.get(block=False)
    small_queue.get(block=False)
    print("  队列已清空")
    
    try:
        print("  尝试非阻塞获取元素...")
        small_queue.get(block=False)
    except queue.Empty:
        print("  捕获到Empty异常: 队列为空")
    
    # 4. qsize(), empty() 和 full() 方法
    print("\n4. qsize(), empty() 和 full() 方法")
    print("   - qsize(): 返回队列中的元素数量")
    print("   - empty(): 检查队列是否为空")
    print("   - full(): 检查队列是否已满")
    
    # 创建一个容量为3的队列
    status_queue = queue.Queue(maxsize=3)
    
    # 初始状态
    print("初始状态:")
    print(f"  队列大小: {status_queue.qsize()}")
    print(f"  队列为空: {status_queue.empty()}")
    print(f"  队列已满: {status_queue.full()}")
    
    # 添加一个元素
    status_queue.put('item1')
    print("添加一个元素后:")
    print(f"  队列大小: {status_queue.qsize()}")
    print(f"  队列为空: {status_queue.empty()}")
    print(f"  队列已满: {status_queue.full()}")
    
    # 添加两个更多元素使队列满
    status_queue.put('item2')
    status_queue.put('item3')
    print("添加两个更多元素使队列满后:")
    print(f"  队列大小: {status_queue.qsize()}")
    print(f"  队列为空: {status_queue.empty()}")
    print(f"  队列已满: {status_queue.full()}")
    
    # 注意：这些方法在多线程环境中不是线程安全的
    print("注意: qsize(), empty()和full()在多线程环境中不是完全可靠的，")
    print("因为在调用方法和使用结果之间，队列的状态可能已被其他线程改变。")
    print("建议使用阻塞操作和超时来代替这些方法进行同步。")

# 运行队列高级方法演示
queue_advanced_methods()
print()

# 3. 实际应用示例
print("=== 3. 实际应用示例 ===")

def queue_practical_examples():
    """队列模块的实际应用示例"""
    print("队列模块在实际应用中的使用场景：\n")
    
    # 示例1: 生产者-消费者模式
    print("示例1: 生产者-消费者模式")
    print("   - 生产者生成数据并放入队列")
    print("   - 消费者从队列中获取数据并处理")
    
    # 创建任务队列
    task_queue = queue.Queue(maxsize=5)
    
    # 设置结束标志
    finished = False
    
    # 生产者函数
    def producer():
        """生产者函数，生成任务"""
        producer_name = threading.current_thread().name
        print(f"生产者 {producer_name} 启动")
        
        for i in range(1, 11):
            # 模拟生成任务的时间
            time.sleep(random.uniform(0.1, 0.5))
            
            # 创建任务
            task = f"任务-{i} ({producer_name})"
            
            # 将任务放入队列
            print(f"{producer_name} 生成: {task}")
            task_queue.put(task)
            print(f"{producer_name} 队列大小: {task_queue.qsize()}")
        
        print(f"生产者 {producer_name} 完成")
    
    # 消费者函数
    def consumer():
        """消费者函数，处理任务"""
        global finished
        consumer_name = threading.current_thread().name
        print(f"消费者 {consumer_name} 启动")
        
        while not finished:
            try:
                # 从队列中获取任务，设置超时以定期检查结束标志
                task = task_queue.get(timeout=1)
                
                # 模拟处理任务的时间
                print(f"{consumer_name} 开始处理: {task}")
                time.sleep(random.uniform(0.3, 0.8))
                
                # 标记任务完成
                task_queue.task_done()
                print(f"{consumer_name} 完成处理: {task}")
            except queue.Empty:
                # 队列为空，继续循环检查结束标志
                pass
    
    # 创建并启动生产者线程
    producer_threads = []
    for i in range(2):
        t = threading.Thread(target=producer, name=f"Producer-{i+1}")
        producer_threads.append(t)
        t.start()
    
    # 创建并启动消费者线程
    consumer_threads = []
    for i in range(3):
        t = threading.Thread(target=consumer, name=f"Consumer-{i+1}")
        consumer_threads.append(t)
        t.daemon = True  # 设置为守护线程
        t.start()
    
    # 等待所有生产者完成
    for t in producer_threads:
        t.join()
    
    # 等待队列中的所有任务完成
    print("等待所有任务处理完成...")
    task_queue.join()
    
    # 设置结束标志，让消费者线程退出
    finished = True
    print("所有任务已处理完成")
    
    # 给消费者线程一点时间来退出
    time.sleep(0.5)
    
    # 示例2: 任务调度器
    print("\n示例2: 简单的任务调度器")
    print("   - 使用优先级队列根据任务优先级进行调度")
    
    # 任务优先级
    PRIORITY_HIGH = 1
    PRIORITY_MEDIUM = 2
    PRIORITY_LOW = 3
    
    # 创建优先级队列
    scheduler_queue = queue.PriorityQueue()
    
    # 任务类
    class Task:
        def __init__(self, name, priority, execution_time=0):
            self.name = name
            self.priority = priority
            self.execution_time = execution_time  # 模拟执行时间（秒）
            self.created_at = time.time()
        
        def __lt__(self, other):
            # 优先级队列基于此方法排序
            # 首先按优先级排序，优先级相同时按创建时间排序（FCFS）
            if self.priority == other.priority:
                return self.created_at < other.created_at
            return self.priority < other.priority
        
        def __repr__(self):
            priority_names = {1: "高", 2: "中", 3: "低"}
            return f"Task(name='{self.name}', priority={priority_names.get(self.priority, '未知')}, time={self.execution_time}s)"
    
    # 添加任务到调度器
    def add_task(name, priority, execution_time=0):
        task = Task(name, priority, execution_time)
        scheduler_queue.put(task)
        print(f"添加任务: {task}")
    
    # 调度器函数
    def scheduler():
        print("调度器启动")
        
        while not scheduler_queue.empty():
            # 获取优先级最高的任务
            task = scheduler_queue.get()
            print(f"执行任务: {task}")
            
            # 模拟任务执行
            time.sleep(task.execution_time)
            
            print(f"任务完成: {task.name}")
        
        print("所有任务已执行完成")
    
    # 添加一些任务
    add_task("系统备份", PRIORITY_LOW, 0.5)
    add_task("用户登录", PRIORITY_HIGH, 0.2)
    add_task("数据库查询", PRIORITY_MEDIUM, 0.3)
    add_task("邮件通知", PRIORITY_LOW, 0.4)
    add_task("文件保存", PRIORITY_HIGH, 0.1)
    add_task("日志记录", PRIORITY_MEDIUM, 0.2)
    
    # 执行调度器
    scheduler()
    
    # 示例3: 线程池实现
    print("\n示例3: 简单的线程池实现")
    print("   - 使用队列管理工作线程和任务")
    
    class ThreadPool:
        def __init__(self, num_threads):
            self.tasks = queue.Queue()
            self.workers = []
            self.running = True
            
            # 创建指定数量的工作线程
            for i in range(num_threads):
                worker = threading.Thread(target=self._worker, name=f"Worker-{i+1}")
                worker.daemon = True
                self.workers.append(worker)
                worker.start()
            
            print(f"线程池初始化完成，创建了 {num_threads} 个工作线程")
        
        def _worker(self):
            """工作线程函数"""
            worker_name = threading.current_thread().name
            while self.running:
                try:
                    # 获取任务，设置超时以检查running标志
                    func, args, kwargs = self.tasks.get(timeout=0.5)
                    
                    try:
                        # 执行任务
                        print(f"{worker_name} 开始执行任务: {func.__name__}")
                        func(*args, **kwargs)
                    except Exception as e:
                        print(f"{worker_name} 执行任务时出错: {e}")
                    finally:
                        # 标记任务完成
                        self.tasks.task_done()
                except queue.Empty:
                    # 队列为空，继续循环检查running标志
                    pass
        
        def submit(self, func, *args, **kwargs):
            """提交任务到线程池"""
            if not self.running:
                raise RuntimeError("线程池已关闭")
            
            self.tasks.put((func, args, kwargs))
            print(f"任务提交: {func.__name__}, 队列大小: {self.tasks.qsize()}")
        
        def wait_completion(self):
            """等待所有任务完成"""
            self.tasks.join()
            print("所有任务已完成")
        
        def shutdown(self):
            """关闭线程池"""
            self.running = False
            # 等待所有工作线程退出
            for worker in self.workers:
                worker.join()
            print("线程池已关闭")
    
    # 测试函数
    def test_function(name, sleep_time):
        """用于测试的函数"""
        print(f"函数 {name} 开始执行，将休眠 {sleep_time} 秒")
        time.sleep(sleep_time)
        print(f"函数 {name} 执行完成")
    
    # 创建线程池
    pool = ThreadPool(num_threads=3)
    
    # 提交任务
    for i in range(1, 6):
        sleep_time = random.uniform(0.2, 0.8)
        pool.submit(test_function, f"任务-{i}", sleep_time)
    
    # 等待所有任务完成
    pool.wait_completion()
    
    # 关闭线程池
    pool.shutdown()
    
    # 示例4: 使用队列进行批处理
    print("\n示例4: 使用队列进行批处理")
    print("   - 收集数据，然后批量处理")
    
    # 配置
    BATCH_SIZE = 3
    
    # 创建队列
    data_queue = queue.Queue()
    batch_queue = queue.Queue()
    
    # 数据生成器
    def data_generator():
        """模拟数据生成"""
        print("数据生成器启动")
        
        for i in range(1, 10):
            data = f"数据-{i}"
            print(f"生成: {data}")
            data_queue.put(data)
            time.sleep(random.uniform(0.1, 0.3))  # 模拟数据到达间隔
        
        # 发送结束标志
        data_queue.put(None)
        print("数据生成完成")
    
    # 批处理器
    def batcher():
        """收集数据并批量处理"""
        print("批处理器启动")
        
        batch = []
        while True:
            try:
                # 获取数据，设置超时
                data = data_queue.get(timeout=1)
                
                # 检查结束标志
                if data is None:
                    # 处理剩余数据
                    if batch:
                        batch_queue.put(batch.copy())
                        print(f"提交最后一批数据: {batch}")
                    # 转发结束标志
                    batch_queue.put(None)
                    break
                
                # 添加到批次
                batch.append(data)
                print(f"添加到批次: {data}, 批次大小: {len(batch)}")
                
                # 如果批次达到指定大小，提交处理
                if len(batch) >= BATCH_SIZE:
                    batch_queue.put(batch.copy())
                    print(f"提交批次: {batch}")
                    batch.clear()
                    
            except queue.Empty:
                # 如果超时且批次不为空，提交当前批次
                if batch:
                    batch_queue.put(batch.copy())
                    print(f"超时，提交当前批次: {batch}")
                    batch.clear()
    
    # 数据处理器
    def data_processor():
        """处理批次数据"""
        print("数据处理器启动")
        
        while True:
            try:
                # 获取批次，设置超时
                batch = batch_queue.get(timeout=1)
                
                # 检查结束标志
                if batch is None:
                    break
                
                # 处理批次
                print(f"处理批次: {batch}")
                # 模拟处理时间
                time.sleep(random.uniform(0.5, 1.0))
                print(f"批次处理完成: {batch}")
                
            except queue.Empty:
                # 队列为空，继续循环
                pass
    
    # 启动线程
    generator_thread = threading.Thread(target=data_generator)
    batcher_thread = threading.Thread(target=batcher)
    processor_thread = threading.Thread(target=data_processor)
    
    generator_thread.start()
    batcher_thread.start()
    processor_thread.start()
    
    # 等待所有线程完成
    generator_thread.join()
    batcher_thread.join()
    processor_thread.join()
    
    print("批处理流程完成")

# 运行实际应用示例
queue_practical_examples()
print()

# 4. 线程安全性和注意事项
print("=== 4. 线程安全性和注意事项 ===")

def queue_thread_safety():
    """讨论队列的线程安全性和使用注意事项"""
    print("队列的线程安全性和使用注意事项：\n")
    
    # 线程安全性
    print("1. 线程安全性")
    print("   - Queue, LifoQueue, PriorityQueue 和 SimpleQueue 都是线程安全的")
    print("   - 这些队列实现了锁机制，可以安全地在多线程环境中使用")
    print("   - 多个线程可以同时调用队列的方法而不会导致数据损坏")
    
    # 非线程安全检查方法
    print("\n2. 非线程安全的检查方法")
    print("   - qsize(), empty() 和 full() 方法在多线程环境中不是完全可靠的")
    print("   - 在调用这些方法和使用结果之间，队列状态可能已被其他线程改变")
    print("   - 示例问题场景:")
    print("     * 检查队列非空后调用get()，但此时队列可能已被其他线程取空")
    print("     * 检查队列未满后调用put()，但此时队列可能已被其他线程填满")
    print("   - 解决方案: 使用带超时的阻塞操作代替状态检查")
    
    # 进程安全性
    print("\n3. 进程安全性")
    print("   - queue模块的队列对象不是进程安全的")
    print("   - 在多进程环境中，应使用 multiprocessing.Queue")
    print("   - multiprocessing.Queue 专门设计用于进程间通信")
    
    # 死锁风险
    print("\n4. 死锁风险")
    print("   - 在多线程环境中使用队列时可能发生死锁")
    print("   - 常见死锁场景:")
    print("     * 工作线程未调用task_done()，导致join()永久阻塞")
    print("     * 多个线程互相等待对方完成操作")
    print("   - 避免死锁的方法:")
    print("     * 始终在处理完任务后调用task_done()")
    print("     * 使用超时参数避免永久阻塞")
    print("     * 确保线程间没有循环依赖")
    
    # 内存消耗
    print("\n5. 内存消耗")
    print("   - 无界队列（maxsize=0）可能会导致内存问题")
    print("   - 如果生产者速度远快于消费者，队列可能会无限增长")
    print("   - 建议设置合理的队列大小限制")
    print("   - 使用阻塞操作让生产者在队列满时暂停")
    
    # 超时处理
    print("\n6. 超时处理")
    print("   - 合理设置超时参数可以避免线程永久阻塞")
    print("   - 超时参数允许线程定期检查终止条件")
    print("   - 示例模式:")
    print("     * 使用全局标志或事件来通知线程退出")
    print("     * 在线程循环中使用超时的队列操作")
    print("     * 定期检查终止条件")
    
    # 异常处理
    print("\n7. 异常处理")
    print("   - 始终捕获Queue.Empty和Queue.Full异常")
    print("   - 在线程函数中使用try-except来处理可能的异常")
    print("   - 避免异常导致线程意外终止")
    
    # 守护线程
    print("\n8. 守护线程")
    print("   - 工作线程通常应设为守护线程（daemon=True）")
    print("   - 这样当主程序退出时，工作线程也会自动终止")
    print("   - 注意: 守护线程中的未完成操作会被强制终止")
    
    # 代码示例: 安全的工作线程模式
    print("\n9. 安全的工作线程模式示例")
    print("   - 使用事件通知线程退出")
    print("   - 使用超时避免永久阻塞")
    print("   - 正确处理异常")
    
    # 演示安全的工作线程模式
    print("\n演示安全的工作线程模式:")
    
    # 创建队列和退出事件
    safe_queue = queue.Queue(maxsize=5)
    exit_event = threading.Event()
    
    def safe_worker():
        """安全的工作线程函数"""
        worker_name = threading.current_thread().name
        print(f"安全工作线程 {worker_name} 启动")
        
        while not exit_event.is_set():
            try:
                # 使用超时获取任务，定期检查退出事件
                task = safe_queue.get(timeout=0.5)
                
                try:
                    # 处理任务
                    print(f"{worker_name} 处理任务: {task}")
                    time.sleep(0.2)  # 模拟工作
                except Exception as e:
                    print(f"{worker_name} 处理任务时出错: {e}")
                finally:
                    # 始终标记任务完成
                    safe_queue.task_done()
                    print(f"{worker_name} 完成任务: {task}")
            except queue.Empty:
                # 队列为空，继续循环检查退出事件
                pass
        
        print(f"安全工作线程 {worker_name} 退出")
    
    # 启动工作线程
    worker_thread = threading.Thread(target=safe_worker, name="SafeWorker")
    worker_thread.daemon = True
    worker_thread.start()
    
    # 添加一些任务
    for i in range(1, 6):
        task = f"安全任务-{i}"
        safe_queue.put(task)
        print(f"添加任务: {task}")
        time.sleep(0.1)
    
    # 等待所有任务处理完成
    safe_queue.join()
    print("所有任务已处理完成")
    
    # 设置退出事件，让工作线程退出
    exit_event.set()
    print("设置退出事件")
    
    # 等待工作线程退出
    worker_thread.join(timeout=1)
    print("工作线程已退出")

# 运行线程安全性和注意事项讨论
queue_thread_safety()
print()

# 5. 与其他队列实现的比较
print("=== 5. 与其他队列实现的比较 ===")

def queue_comparison():
    """比较不同的队列实现"""
    print("Python中不同队列实现的比较：\n")
    
    # 1. queue模块 vs collections.deque
    print("1. queue模块 vs collections.deque")
    print("   - queue模块:")
    print("     * 线程安全")
    print("     * 提供阻塞操作和超时机制")
    print("     * 支持任务完成通知(task_done/join)")
    print("     * 有FIFO、LIFO和优先级队列变体")
    print("     * 性能稍低（由于锁开销）")
    print("   - collections.deque:")
    print("     * 不是线程安全的")
    print("     * 无阻塞操作")
    print("     * 双端队列，支持从两端高效添加/删除元素")
    print("     * 性能更高")
    print("     * 适用于单线程环境或需要手动同步的场景")
    
    # 性能比较
    print("\n性能比较:")
    
    # 创建队列
    import time
    
    # 测量deque性能
    deq = deque()
    start_time = time.time()
    for i in range(100000):
        deq.append(i)
    for i in range(100000):
        deq.popleft()
    deque_time = time.time() - start_time
    print(f"deque (单线程): {deque_time:.6f}秒 (100,000次添加/删除)")
    
    # 测量Queue性能
    q = queue.Queue()
    start_time = time.time()
    for i in range(100000):
        q.put(i)
    for i in range(100000):
        q.get()
    queue_time = time.time() - start_time
    print(f"Queue: {queue_time:.6f}秒 (100,000次添加/删除)")
    print(f"性能差异: Queue比deque慢约{queue_time/deque_time:.1f}倍")
    
    # 2. queue.Queue vs multiprocessing.Queue
    print("\n2. queue.Queue vs multiprocessing.Queue")
    print("   - queue.Queue:")
    print("     * 用于线程间通信")
    print("     * 使用线程锁实现同步")
    print("     * 不支持进程间通信")
    print("   - multiprocessing.Queue:")
    print("     * 用于进程间通信")
    print("     * 使用进程间通信(IPC)机制")
    print("     * 也可用于线程间通信，但有额外开销")
    print("     * 支持进程池和分布式处理")
    
    # 3. 自定义队列 vs 标准库队列
    print("\n3. 自定义队列 vs 标准库队列")
    print("   - 标准库队列:")
    print("     * 经过充分测试和优化")
    print("     * 线程安全")
    print("     * 维护良好")
    print("     * 推荐用于大多数应用场景")
    print("   - 自定义队列:")
    print("     * 可以针对特定需求进行优化")
    print("     * 可以添加特殊功能")
    print("     * 需要自行实现线程安全")
    print("     * 风险较高，容易引入微妙的并发错误")
    
    # 4. 队列选择指南
    print("\n4. 队列选择指南")
    print("   - 单线程环境:")
    print("     * 一般用途: collections.deque")
    print("     * 需要优先级: heapq模块")
    print("   - 多线程环境:")
    print("     * 基本队列操作: queue.Queue")
    print("     * LIFO操作: queue.LifoQueue")
    print("     * 优先级处理: queue.PriorityQueue")
    print("     * 简单通信: queue.SimpleQueue")
    print("   - 多进程环境:")
    print("     * 进程间通信: multiprocessing.Queue")
    print("     * 共享内存: multiprocessing.Manager().Queue()")
    print("   - 分布式系统:")
    print("     * 需要使用消息队列系统，如RabbitMQ, Redis等")

# 运行队列比较
queue_comparison()
print()

# 6. 高级用例和设计模式
print("=== 6. 高级用例和设计模式 ===")

def queue_advanced_patterns():
    """队列的高级用例和设计模式"""
    print("使用队列的高级设计模式：\n")
    
    # 1. 流水线模式
    print("1. 流水线模式")
    print("   - 使用多个队列连接多个处理阶段")
    print("   - 每个阶段专注于特定的处理任务")
    print("   - 适用于复杂的数据处理流程")
    
    # 演示流水线模式
    print("\n演示简单的三阶段流水线:")
    
    # 创建三个队列
    stage1_queue = queue.Queue(maxsize=5)
    stage2_queue = queue.Queue(maxsize=5)
    stage3_queue = queue.Queue(maxsize=5)
    
    # 结束标志
    pipeline_finished = False
    
    # 阶段1: 数据生成
    def stage1_producer():
        """第一阶段: 数据生成"""
        print("阶段1: 数据生成器启动")
        
        for i in range(1, 8):
            data = f"原始数据-{i}"
            print(f"阶段1: 生成 {data}")
            stage1_queue.put(data)
            time.sleep(random.uniform(0.2, 0.5))  # 模拟生成时间
        
        # 发送结束标志
        stage1_queue.put(None)
        print("阶段1: 数据生成完成")
    
    # 阶段2: 数据处理
    def stage2_processor():
        """第二阶段: 数据处理"""
        print("阶段2: 数据处理器启动")
        
        while not pipeline_finished:
            try:
                # 获取数据，设置超时
                data = stage1_queue.get(timeout=0.5)
                
                # 检查结束标志
                if data is None:
                    # 转发结束标志到下一阶段
                    stage2_queue.put(None)
                    break
                
                # 处理数据
                processed_data = f"处理后-{data}"
                print(f"阶段2: 处理 {data} -> {processed_data}")
                time.sleep(random.uniform(0.3, 0.7))  # 模拟处理时间
                
                # 将处理后的数据放入下一阶段队列
                stage2_queue.put(processed_data)
                
            except queue.Empty:
                # 队列为空，继续循环检查结束标志
                pass
        
        print("阶段2: 数据处理完成")
    
    # 阶段3: 结果输出
    def stage3_consumer():
        """第三阶段: 结果输出"""
        print("阶段3: 结果输出器启动")
        
        while not pipeline_finished:
            try:
                # 获取数据，设置超时
                data = stage2_queue.get(timeout=0.5)
                
                # 检查结束标志
                if data is None:
                    break
                
                # 处理结果
                print(f"阶段3: 输出 {data}")
                time.sleep(random.uniform(0.1, 0.4))  # 模拟输出时间
                
            except queue.Empty:
                # 队列为空，继续循环检查结束标志
                pass
        
        print("阶段3: 结果输出完成")
    
    # 启动流水线线程
    stage1_thread = threading.Thread(target=stage1_producer)
    stage2_thread = threading.Thread(target=stage2_processor)
    stage3_thread = threading.Thread(target=stage3_consumer)
    
    stage1_thread.start()
    stage2_thread.start()
    stage3_thread.start()
    
    # 等待所有阶段完成
    stage1_thread.join()
    stage2_thread.join()
    
    # 设置结束标志
    pipeline_finished = True
    stage3_thread.join()
    
    print("流水线处理完成")
    
    # 2. 优先级队列的自定义排序
    print("\n2. 优先级队列的自定义排序")
    print("   - 自定义任务类的比较方法")
    print("   - 实现复杂的优先级逻辑")
    
    # 自定义任务类示例
    print("\n自定义任务类示例:")
    
    class CustomTask:
        def __init__(self, name, priority, deadline=0, resource_required=1):
            self.name = name
            self.priority = priority  # 1-5, 数字越小优先级越高
            self.deadline = deadline  # 截止时间（秒），0表示无截止时间
            self.resource_required = resource_required  # 所需资源数
            self.created_at = time.time()
        
        def __lt__(self, other):
            # 首先按优先级排序
            if self.priority != other.priority:
                return self.priority < other.priority
            
            # 优先级相同时，按截止时间排序（有截止时间的优先）
            if self.deadline > 0 and other.deadline > 0:
                # 计算剩余时间
                self_remaining = max(0, self.deadline - (time.time() - self.created_at))
                other_remaining = max(0, other.deadline - (time.time() - other.created_at))
                return self_remaining < other_remaining
            elif self.deadline > 0:
                return True
            elif other.deadline > 0:
                return False
            
            # 都没有截止时间时，按创建时间排序（先到先服务）
            return self.created_at < other.created_at
        
        def __repr__(self):
            deadline_str = f"(剩余{max(0, self.deadline - (time.time() - self.created_at)):.1f}s)" if self.deadline > 0 else "(无截止时间)"
            return f"Task({self.name}, 优先级={self.priority}, 资源={self.resource_required}) {deadline_str}"
    
    # 创建优先级队列并添加任务
    custom_queue = queue.PriorityQueue()
    
    # 添加一些任务
    custom_queue.put(CustomTask("紧急修复", 1, deadline=10))
    custom_queue.put(CustomTask("常规更新", 3, deadline=0))
    custom_queue.put(CustomTask("资源密集型任务", 2, resource_required=3))
    custom_queue.put(CustomTask("即将到期任务", 3, deadline=5))
    custom_queue.put(CustomTask("高优先级任务", 2, deadline=0))
    
    # 处理任务
    print("按自定义优先级处理任务:")
    while not custom_queue.empty():
        task = custom_queue.get()
        print(f"  处理: {task}")
        time.sleep(0.5)  # 模拟处理时间
    
    # 3. 限流队列
    print("\n3. 限流队列")
    print("   - 控制处理速率")
    print("   - 防止过载")
    print("   - 实现流量控制")
    
    # 限流队列示例
    print("\n限流队列示例:")
    
    class RateLimitedQueue(queue.Queue):
        def __init__(self, maxsize=0, rate_limit=5):
            super().__init__(maxsize)
            self.rate_limit = rate_limit  # 每秒最多处理的项目数
            self.last_process_time = 0  # 上次处理时间
        
        def get(self, block=True, timeout=None):
            """获取元素，应用速率限制"""
            # 获取元素
            item = super().get(block, timeout)
            
            # 计算需要等待的时间以维持速率限制
            current_time = time.time()
            elapsed = current_time - self.last_process_time
            required_interval = 1.0 / self.rate_limit
            
            if elapsed < required_interval:
                # 需要等待以维持速率限制
                wait_time = required_interval - elapsed
                time.sleep(wait_time)
            
            # 更新最后处理时间
            self.last_process_time = time.time()
            
            return item
    
    # 创建限流队列
    rate_queue = RateLimitedQueue(maxsize=10, rate_limit=3)  # 每秒最多处理3个项目
    
    # 添加任务
    for i in range(1, 6):
        rate_queue.put(f"限流任务-{i}")
        print(f"添加限流任务: 限流任务-{i}")
    
    # 处理任务
    print("按每秒3个的速率处理任务:")
    start_time = time.time()
    while not rate_queue.empty():
        item = rate_queue.get()
        elapsed = time.time() - start_time
        print(f"  时间 {elapsed:.2f}s: 处理 {item}")
    
    # 4. 延迟队列
    print("\n4. 延迟队列")
    print("   - 任务在指定时间后才可用")
    print("   - 适用于定时任务、重试机制等")
    
    # 简单的延迟队列实现
    print("\n简单的延迟队列实现:")
    
    class DelayedQueue:
        def __init__(self):
            self.queue = queue.PriorityQueue()
        
        def put(self, item, delay=0):
            """添加延迟任务
            
            Args:
                item: 要处理的任务
                delay: 延迟时间（秒）
            """
            # 计算任务可用时间
            available_time = time.time() + delay
            # 使用(可用时间, 随机数, 任务)作为优先级队列的元素
            # 随机数用于打破相同可用时间的平局
            self.queue.put((available_time, random.random(), item))
            print(f"添加延迟任务: {item} (延迟 {delay}秒)")
        
        def get(self, block=True, timeout=None):
            """获取可用的任务
            
            Args:
                block: 是否阻塞等待
                timeout: 最长等待时间（秒）
            
            Returns:
                任务对象
            """
            start_time = time.time()
            
            while True:
                # 检查队列是否为空
                if self.queue.empty():
                    if block:
                        # 如果队列为空且需要阻塞，等待直到有任务
                        if timeout is not None:
                            # 计算剩余超时时间
                            elapsed = time.time() - start_time
                            if elapsed >= timeout:
                                raise queue.Empty
                            time.sleep(min(0.1, timeout - elapsed))
                        else:
                            # 无超时限制，短暂休眠后重试
                            time.sleep(0.1)
                        continue
                    else:
                        raise queue.Empty
                
                # 查看队列中最早的任务（不取出）
                available_time, _, item = self.queue.queue[0]
                current_time = time.time()
                
                # 检查任务是否可用
                if current_time >= available_time:
                    # 任务可用，取出并返回
                    self.queue.get()
                    return item
                else:
                    # 任务尚未可用，计算需要等待的时间
                    wait_time = available_time - current_time
                    
                    if block:
                        if timeout is not None:
                            # 计算剩余超时时间
                            elapsed = time.time() - start_time
                            if elapsed >= timeout:
                                raise queue.Empty
                            
                            # 取较小的等待时间
                            wait_time = min(wait_time, timeout - elapsed)
                        
                        # 等待直到任务可用或超时
                        time.sleep(wait_time)
                    else:
                        # 非阻塞模式，立即抛出异常
                        raise queue.Empty
        
        def empty(self):
            """检查队列是否为空（不考虑延迟）"""
            return self.queue.empty()
    
    # 创建延迟队列
    delayed_queue = DelayedQueue()
    
    # 添加延迟任务
    delayed_queue.put("立即任务", delay=0)
    delayed_queue.put("延迟1秒任务", delay=1)
    delayed_queue.put("延迟2秒任务", delay=2)
    delayed_queue.put("延迟0.5秒任务", delay=0.5)
    
    # 处理延迟任务
    print("处理延迟任务:")
    start_time = time.time()
    
    try:
        while True:
            # 尝试获取任务，设置较长的超时
            item = delayed_queue.get(block=True, timeout=3)
            elapsed = time.time() - start_time
            print(f"  时间 {elapsed:.2f}s: 处理 {item}")
    except queue.Empty:
        print("所有延迟任务已处理完成")

# 运行高级用例和设计模式
try:
    queue_advanced_patterns()
except Exception as e:
    print(f"运行高级用例时出错: {e}")
    print("这可能是由于线程调度或超时设置导致的")

print()

# 7. 总结和最佳实践
print("=== 7. 总结和最佳实践 ===")

def queue_summary():
    """队列模块的总结和最佳实践"""
    print("queue模块总结：\n")
    
    # 功能总结
    print("功能总结：")
    print("1. 线程安全的队列实现")
    print("2. 支持FIFO、LIFO和优先级队列")
    print("3. 提供阻塞操作和超时机制")
    print("4. 实现了任务完成通知机制")
    print("5. 适用于多线程环境中的数据交换\n")
    
    # 最佳实践
    print("最佳实践：")
    print("1. 选择合适的队列类型:")
    print("   - 标准顺序处理: Queue (FIFO)")
    print("   - 后进先出处理: LifoQueue (栈)")
    print("   - 优先级处理: PriorityQueue")
    print("   - 简单通信: SimpleQueue")
    print("2. 设置合理的队列大小限制:")
    print("   - 避免使用无界队列（maxsize=0）")
    print("   - 根据实际负载设置合适的队列容量")
    print("3. 使用超时参数:")
    print("   - 避免线程永久阻塞")
    print("   - 允许定期检查终止条件")
    print("4. 正确处理任务完成:")
    print("   - 始终在处理完任务后调用task_done()")
    print("   - 使用join()等待所有任务完成")
    print("5. 异常处理:")
    print("   - 捕获Queue.Empty和Queue.Full异常")
    print("   - 在线程函数中使用try-except来避免意外退出")
    print("6. 线程管理:")
    print("   - 使用守护线程或提供明确的退出机制")
    print("   - 避免在工作线程中执行无限阻塞操作")
    print("7. 性能考虑:")
    print("   - 对于单线程环境，考虑使用collections.deque")
    print("   - 对于多进程环境，使用multiprocessing.Queue")
    print("8. 复杂场景:")
    print("   - 使用流水线模式处理复杂任务")
    print("   - 实现自定义队列满足特殊需求\n")
    
    # 常见错误
    print("常见错误和避免方法：")
    print("1. 忘记调用task_done(): 导致join()永久阻塞")
    print("2. 使用无界队列: 可能导致内存耗尽")
    print("3. 忽略超时设置: 可能导致线程永久阻塞")
    print("4. 错误使用队列类型: 例如，在需要优先级处理时使用FIFO队列")
    print("5. 在多进程环境中使用queue.Queue: 应使用multiprocessing.Queue")
    print("6. 过度依赖qsize()/empty()/full(): 这些方法在多线程环境中不可靠")
    print("7. 未处理异常: 导致工作线程意外终止\n")
    
    # 版本兼容性
    print("版本兼容性：")
    print(f"当前Python版本: {sys.version}")
    print("- Queue、LifoQueue和PriorityQueue在所有Python版本中可用")
    print("- SimpleQueue在Python 3.7+中新增")
    print("- 所有功能在不同平台上表现一致")

# 运行总结和最佳实践
queue_summary()

print("\n=== 8. 完整导入和使用指南 ===")
print("queue模块的导入方式：")
print("""
# 导入整个模块
import queue

# 导入特定类和异常
from queue import Queue, LifoQueue, PriorityQueue, SimpleQueue, Empty, Full
""")

print("\n使用示例：")
print("""
# 创建队列
q = queue.Queue(maxsize=10)  # 创建最大容量为10的FIFO队列

# 添加元素
q.put(item, block=True, timeout=None)  # 阻塞直到有空间或超时

# 获取元素
item = q.get(block=True, timeout=None)  # 阻塞直到有元素或超时

# 任务完成通知
q.task_done()  # 标记任务完成
q.join()  # 等待所有任务完成

# 检查状态（多线程环境中不可靠）
size = q.qsize()
is_empty = q.empty()
is_full = q.full()
""")

print("\n总结：queue模块是Python多线程编程中线程间通信的重要工具，")
print("通过提供线程安全的队列实现，使得在多线程环境中交换数据变得简单和安全。")
print("熟练使用这些队列类型和方法，可以构建高效、可靠的多线程应用程序。")