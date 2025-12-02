# queue模块 - Python中的队列实现

## 1. 核心功能概述

`queue`模块提供了多种队列实现，用于在多线程编程中安全地传递消息或任务。这些队列实现都是线程安全的，可以被多个线程同时访问而不需要额外的锁机制。

队列的主要特点：

- **线程安全**：所有队列操作都是原子的，多线程环境下安全使用
- **阻塞操作**：支持阻塞式的get()和put()操作，可以设置超时
- **多种队列类型**：提供不同类型的队列以满足不同的需求
- **生产者-消费者模式**：特别适合实现生产者-消费者设计模式

`queue`模块提供了以下几种队列实现：

1. **Queue**：先进先出(FIFO)队列
2. **LifoQueue**：后进先出(LIFO)队列，也称为栈
3. **PriorityQueue**：优先级队列
4. **SimpleQueue**：简单的无界FIFO队列，不提供任务跟踪

## 2. 基本使用方法

### 2.1 创建和使用Queue (FIFO队列)

```python
import queue

# 创建一个无限大小的队列
fifo_queue = queue.Queue()

# 创建一个最大容量为5的队列
bounded_queue = queue.Queue(maxsize=5)

# 向队列中添加元素
fifo_queue.put('item1')
fifo_queue.put('item2')
fifo_queue.put('item3')

# 从队列中获取元素（默认会阻塞直到有元素可用）
item = fifo_queue.get()
print(f"Got item: {item}")  # 输出: Got item: item1

# 查看队列大小
print(f"Queue size: {fifo_queue.qsize()}")  # 输出: Queue size: 2

# 检查队列是否为空
print(f"Is queue empty? {fifo_queue.empty()}")  # 输出: Is queue empty? False

# 检查队列是否已满
print(f"Is queue full? {fifo_queue.full()}")  # 输出: Is queue full? False

# 标记任务完成（对于消费者来说）
fifo_queue.task_done()

# 等待所有任务完成
fifo_queue.join()
```

### 2.2 创建和使用LifoQueue (LIFO队列/栈)

```python
import queue

# 创建一个LIFO队列
stack = queue.LifoQueue()

# 向栈中添加元素
stack.put('item1')
stack.put('item2')
stack.put('item3')

# 从栈中获取元素（后进先出）
item1 = stack.get()
print(f"Got from stack: {item1}")  # 输出: Got from stack: item3

item2 = stack.get()
print(f"Got from stack: {item2}")  # 输出: Got from stack: item2

item3 = stack.get()
print(f"Got from stack: {item3}")  # 输出: Got from stack: item1

# 标记任务完成
stack.task_done()
stack.task_done()
stack.task_done()
```

### 2.3 创建和使用PriorityQueue (优先级队列)

```python
import queue

# 创建一个优先级队列
priority_queue = queue.PriorityQueue()

# 向优先级队列中添加元素（格式：(优先级, 数据)，优先级数字越小，优先级越高）
priority_queue.put((3, 'task3'))
priority_queue.put((1, 'task1'))
priority_queue.put((2, 'task2'))

# 从优先级队列中获取元素（按照优先级顺序）
priority, task = priority_queue.get()
print(f"Got task with priority {priority}: {task}")  # 输出: Got task with priority 1: task1

priority, task = priority_queue.get()
print(f"Got task with priority {priority}: {task}")  # 输出: Got task with priority 2: task2

priority, task = priority_queue.get()
print(f"Got task with priority {priority}: {task}")  # 输出: Got task with priority 3: task3

# 标记任务完成
priority_queue.task_done()
priority_queue.task_done()
priority_queue.task_done()
```

### 2.4 创建和使用SimpleQueue

```python
import queue

# 创建一个SimpleQueue
simple_queue = queue.SimpleQueue()

# 向SimpleQueue中添加元素
simple_queue.put('item1')
simple_queue.put('item2')

# 从SimpleQueue中获取元素
item = simple_queue.get()
print(f"Got from SimpleQueue: {item}")  # 输出: Got from SimpleQueue: item1

# 检查队列大小
print(f"SimpleQueue size: {simple_queue.qsize()}")  # 输出: SimpleQueue size: 1

# SimpleQueue没有task_done()和join()方法
# SimpleQueue也没有empty()和full()方法
```

### 2.5 阻塞和超时操作

所有队列类型（除了SimpleQueue）都支持阻塞和超时操作：

```python
import queue
import time

# 创建一个最大容量为2的队列
bounded_queue = queue.Queue(maxsize=2)

# 添加元素直到队列满
bounded_queue.put('item1')
bounded_queue.put('item2')

# 添加第三个元素，设置超时为1秒
try:
    print("Trying to put item3 with timeout...")
    bounded_queue.put('item3', timeout=1)
except queue.Full:
    print("Queue is full, put operation timed out")

# 尝试非阻塞式添加
try:
    print("Trying non-blocking put...")
    bounded_queue.put_nowait('item3')
except queue.Full:
    print("Queue is full, non-blocking put failed")

# 从队列中获取元素
item = bounded_queue.get()
print(f"Got item: {item}")

# 现在队列有一个空位，可以添加元素了
bounded_queue.put('item3')
print(f"Successfully added item3 after removing an item")

# 清空队列
bounded_queue.get()
bounded_queue.get()

# 尝试从空队列中获取元素，设置超时
try:
    print("Trying to get from empty queue with timeout...")
    item = bounded_queue.get(timeout=1)
except queue.Empty:
    print("Queue is empty, get operation timed out")

# 尝试非阻塞式获取
try:
    print("Trying non-blocking get...")
    item = bounded_queue.get_nowait()
except queue.Empty:
    print("Queue is empty, non-blocking get failed")
```

## 3. 高级用法

### 3.1 实现自定义优先级队列

可以扩展`PriorityQueue`类来实现自定义的优先级逻辑：

```python
import queue

class CustomPriorityQueue(queue.PriorityQueue):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def put_task(self, task, priority=0, data=None):
        """添加任务到队列"""
        # 格式: (优先级, 计数器, 任务名称, 数据)
        # 计数器确保同优先级任务的插入顺序
        if not hasattr(self, '_counter'):
            self._counter = 0
        self._counter += 1
        self.put((priority, self._counter, task, data))
    
    def get_task(self):
        """从队列中获取任务"""
        priority, counter, task, data = self.get()
        return task, priority, data

# 测试自定义优先级队列
custom_queue = CustomPriorityQueue()

# 添加任务
custom_queue.put_task("write_report", priority=3, data={"deadline": "tomorrow"})
custom_queue.put_task("fix_bug", priority=1, data={"severity": "critical"})
custom_queue.put_task("update_docs", priority=2, data={"section": "api"})
custom_queue.put_task("respond_to_email", priority=1, data={"sender": "client"})

# 获取任务
print("Tasks processed in priority order:")
while not custom_queue.empty():
    task, priority, data = custom_queue.get_task()
    print(f"Priority {priority}: {task} - {data}")
    custom_queue.task_done()
```

### 3.2 使用队列实现工作池模式

可以使用队列来实现工作池模式，其中多个工作线程从队列中获取任务并执行：

```python
import queue
import threading
import time
import random

def worker(worker_id, task_queue):
    """工作线程函数"""
    while True:
        try:
            # 获取任务，设置超时以便定期检查是否应该退出
            task, args = task_queue.get(timeout=1)
            
            if task is None:  # 接收到退出信号
                print(f"Worker {worker_id} received shutdown signal")
                task_queue.task_done()
                break
            
            print(f"Worker {worker_id} started task: {task}")
            # 模拟工作
            result = task(*args)
            print(f"Worker {worker_id} completed task: {task.__name__}, result: {result}")
            
            # 标记任务完成
            task_queue.task_done()
            
        except queue.Empty:
            # 队列为空，继续循环
            continue
        except Exception as e:
            print(f"Worker {worker_id} error: {e}")
            task_queue.task_done()

def create_workers(num_workers, task_queue):
    """创建工作线程池"""
    workers = []
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(i, task_queue))
        t.daemon = True  # 设为守护线程，主线程结束时自动退出
        t.start()
        workers.append(t)
    return workers

def shutdown_workers(num_workers, task_queue):
    """关闭工作线程池"""
    # 向队列发送退出信号
    for _ in range(num_workers):
        task_queue.put((None, None))

# 定义一些任务函数
def process_data(data):
    time.sleep(random.uniform(0.5, 2.0))  # 模拟处理时间
    return f"Processed {data}"

def validate_data(data):
    time.sleep(random.uniform(0.3, 1.0))  # 模拟验证时间
    return f"Validated {data}"

def transform_data(data):
    time.sleep(random.uniform(0.7, 1.5))  # 模拟转换时间
    return f"Transformed {data}"

# 主程序
def main():
    # 创建任务队列
    task_queue = queue.Queue()
    
    # 创建工作线程池
    num_workers = 3
    workers = create_workers(num_workers, task_queue)
    
    # 添加任务到队列
    tasks = [
        (process_data, ("data1",)),
        (validate_data, ("data2",)),
        (transform_data, ("data3",)),
        (process_data, ("data4",)),
        (validate_data, ("data5",)),
        (transform_data, ("data6",)),
        (process_data, ("data7",)),
        (validate_data, ("data8",)),
    ]
    
    for task in tasks:
        task_queue.put(task)
    
    print(f"Added {len(tasks)} tasks to queue")
    
    # 等待所有任务完成
    task_queue.join()
    print("All tasks completed")
    
    # 关闭工作线程池
    shutdown_workers(num_workers, task_queue)
    
    # 等待所有工作线程结束
    for worker_thread in workers:
        worker_thread.join()
    
    print("All workers terminated")

if __name__ == "__main__":
    main()
```

### 3.3 使用队列实现生产者-消费者模式

```python
import queue
import threading
import time
import random

# 创建一个有界队列
buffer = queue.Queue(maxsize=5)
def producer(producer_id, num_items):
    """生产者函数"""
    for i in range(num_items):
        # 生产数据
        item = f"Item-{producer_id}-{i}"
        
        # 尝试将数据放入队列，如果队列满则阻塞
        buffer.put(item)
        print(f"Producer {producer_id} produced {item}, queue size: {buffer.qsize()}")
        
        # 模拟生产间隔
        time.sleep(random.uniform(0.1, 0.5))
    
    print(f"Producer {producer_id} finished producing {num_items} items")

def consumer(consumer_id):
    """消费者函数"""
    items_processed = 0
    
    while True:
        try:
            # 尝试从队列获取数据，如果队列为空则阻塞，设置超时
            item = buffer.get(timeout=2)
            
            # 模拟消费数据
            print(f"Consumer {consumer_id} consumed {item}, queue size: {buffer.qsize()}")
            items_processed += 1
            
            # 标记任务完成
            buffer.task_done()
            
            # 模拟消费间隔
            time.sleep(random.uniform(0.2, 0.7))
            
        except queue.Empty:
            # 如果队列为空且所有生产者已完成，则退出
            if not any(t.is_alive() for t in producer_threads):
                print(f"Consumer {consumer_id} exiting, processed {items_processed} items")
                break

# 主程序
producer_threads = []
consumer_threads = []

# 创建3个生产者线程
for i in range(3):
    t = threading.Thread(target=producer, args=(i, 5))
    producer_threads.append(t)
    t.start()

# 创建2个消费者线程
for i in range(2):
    t = threading.Thread(target=consumer, args=(i,))
    consumer_threads.append(t)
    t.daemon = True  # 设为守护线程，主线程结束时自动退出
    t.start()

# 等待所有生产者完成
for t in producer_threads:
    t.join()

print("All producers have finished")

# 等待队列中的所有任务完成
buffer.join()
print("All items have been processed")

# 等待所有消费者检测到队列空并退出
for t in consumer_threads:
    t.join(timeout=3)  # 给消费者一些时间来检测队列空

print("All consumers have exited")
```

### 3.4 实现带优先级的工作队列

结合优先级队列和工作池模式，可以实现带优先级的工作队列：

```python
import queue
import threading
import time
import random

# 创建优先级队列
priority_queue = queue.PriorityQueue()

# 任务优先级常量
PRIORITY_URGENT = 0
PRIORITY_HIGH = 1
PRIORITY_MEDIUM = 2
PRIORITY_LOW = 3

def worker(worker_id):
    """工作线程函数"""
    while True:
        try:
            # 获取任务，设置超时以便定期检查是否应该退出
            priority, counter, task, args = priority_queue.get(timeout=1)
            
            if task is None:  # 接收到退出信号
                print(f"Worker {worker_id} received shutdown signal")
                priority_queue.task_done()
                break
            
            print(f"Worker {worker_id} started task: {task.__name__} (priority: {priority})")
            # 执行任务
            result = task(*args)
            print(f"Worker {worker_id} completed task: {task.__name__}, result: {result}")
            
            # 标记任务完成
            priority_queue.task_done()
            
        except queue.Empty:
            # 队列为空，继续循环
            continue
        except Exception as e:
            print(f"Worker {worker_id} error: {e}")
            priority_queue.task_done()

def add_task(task, args=(), priority=PRIORITY_MEDIUM):
    """向优先级队列添加任务"""
    # 确保_counter属性存在
    if not hasattr(add_task, '_counter'):
        add_task._counter = 0
    add_task._counter += 1
    
    # 格式: (优先级, 计数器, 任务函数, 参数)
    priority_queue.put((priority, add_task._counter, task, args))
    print(f"Added task: {task.__name__} with priority {priority}")

# 定义一些任务函数
def fix_critical_bug():
    time.sleep(1.0)
    return "Critical bug fixed"

def deploy_new_feature():
    time.sleep(2.0)
    return "New feature deployed"

def update_documentation():
    time.sleep(1.5)
    return "Documentation updated"

def cleanup_logs():
    time.sleep(0.5)
    return "Logs cleaned up"

def run_regression_tests():
    time.sleep(3.0)
    return "Regression tests completed"

# 主程序
def main():
    # 创建3个工作线程
    num_workers = 3
    workers = []
    for i in range(num_workers):
        t = threading.Thread(target=worker, args=(i,))
        t.daemon = True
        t.start()
        workers.append(t)
    
    # 添加不同优先级的任务
    add_task(fix_critical_bug, priority=PRIORITY_URGENT)
    add_task(update_documentation, priority=PRIORITY_LOW)
    add_task(deploy_new_feature, priority=PRIORITY_HIGH)
    add_task(cleanup_logs, priority=PRIORITY_LOW)
    add_task(run_regression_tests, priority=PRIORITY_MEDIUM)
    add_task(fix_critical_bug, priority=PRIORITY_URGENT)  # 另一个紧急bug修复
    
    # 等待所有任务完成
    priority_queue.join()
    print("All tasks completed")
    
    # 向队列发送退出信号
    for _ in range(num_workers):
        add_task(None, priority=PRIORITY_URGENT)  # 优先级最高的退出信号
    
    # 等待所有工作线程结束
    for worker_thread in workers:
        worker_thread.join()
    
    print("All workers terminated")

if __name__ == "__main__":
    main()
```

### 3.5 实现带超时的队列操作

可以封装队列操作，实现带重试和超时功能的队列接口：

```python
import queue
import time
import threading

def put_with_retry(q, item, max_retries=3, retry_delay=1, timeout=None):
    """向队列添加元素，支持重试"""
    retries = 0
    while True:
        try:
            q.put(item, timeout=timeout)
            return True  # 成功添加
        except queue.Full:
            retries += 1
            if retries > max_retries:
                raise  # 超过最大重试次数，抛出异常
            print(f"Queue full, retrying in {retry_delay} seconds... (Attempt {retries}/{max_retries})")
            time.sleep(retry_delay)

def get_with_retry(q, max_retries=3, retry_delay=1, timeout=None):
    """从队列获取元素，支持重试"""
    retries = 0
    while True:
        try:
            return q.get(timeout=timeout)
        except queue.Empty:
            retries += 1
            if retries > max_retries:
                raise  # 超过最大重试次数，抛出异常
            print(f"Queue empty, retrying in {retry_delay} seconds... (Attempt {retries}/{max_retries})")
            time.sleep(retry_delay)

# 测试带重试的队列操作
def test_retry_queue():
    # 创建一个最大容量为2的队列
    q = queue.Queue(maxsize=2)
    
    # 添加元素到队列
    print("Adding first two items...")
    q.put("item1")
    q.put("item2")
    print(f"Queue size: {q.qsize()}")
    
    # 尝试添加第三个元素，应该会触发重试
    print("\nTrying to add third item with retry...")
    
    # 创建一个线程来在2秒后从队列中取出一个元素
    def consumer():
        time.sleep(2)
        item = q.get()
        print(f"Consumer took item: {item}")
        q.task_done()
    
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()
    
    # 尝试添加第三个元素，设置超时为1秒，重试3次
    try:
        put_with_retry(q, "item3", max_retries=3, retry_delay=0.5, timeout=1)
        print("Successfully added item3 after retry")
        print(f"Queue size: {q.qsize()}")
    except queue.Full:
        print("Failed to add item3 after max retries")
    
    consumer_thread.join()

if __name__ == "__main__":
    test_retry_queue()
```

## 4. 实际应用场景

### 4.1 任务调度器

使用队列实现一个简单的任务调度器，可以根据优先级和时间延迟调度任务：

```python
import queue
import threading
import time

class TaskScheduler:
    def __init__(self):
        # 使用优先级队列，优先级为执行时间
        self.task_queue = queue.PriorityQueue()
        self.lock = threading.RLock()  # 可重入锁，用于保护共享状态
        self.scheduler_thread = None
        self.running = False
        self.counter = 0  # 用于保证同时间任务的插入顺序
    
    def start(self):
        """启动调度器"""
        with self.lock:
            if self.running:
                return
            self.running = True
            self.scheduler_thread = threading.Thread(target=self._scheduler_loop)
            self.scheduler_thread.daemon = True
            self.scheduler_thread.start()
            print("Scheduler started")
    
    def stop(self):
        """停止调度器"""
        with self.lock:
            if not self.running:
                return
            self.running = False
            if self.scheduler_thread:
                # 添加一个终止任务以唤醒调度线程
                self.task_queue.put((0, 0, self._stop_task, ()))
                self.scheduler_thread.join(timeout=2)
                print("Scheduler stopped")
    
    def _stop_task(self):
        """终止任务，只用于唤醒调度线程"""
        pass
    
    def _scheduler_loop(self):
        """调度器主循环"""
        while self.running:
            try:
                # 获取下一个任务
                if self.task_queue.empty():
                    time.sleep(0.1)  # 避免忙等
                    continue
                
                # 查看队首任务，但不移除
                with self.lock:
                    if self.task_queue.empty():
                        continue
                    next_run_time, _, task, args = self.task_queue.queue[0]
                
                # 计算需要等待的时间
                current_time = time.time()
                wait_time = max(0, next_run_time - current_time)
                
                if wait_time > 0:
                    # 等待直到任务应该执行
                    time.sleep(min(wait_time, 0.1))  # 最多等待0.1秒，以便可以检查running标志
                    continue
                
                # 任务应该执行了，取出并执行
                _, _, task, args = self.task_queue.get()
                
                # 如果是终止任务，直接标记完成
                if task == self._stop_task:
                    self.task_queue.task_done()
                    continue
                
                # 执行任务
                try:
                    print(f"Executing task {task.__name__} at {time.time():.2f}")
                    task(*args)
                except Exception as e:
                    print(f"Error executing task {task.__name__}: {e}")
                
                # 标记任务完成
                self.task_queue.task_done()
                
            except Exception as e:
                print(f"Scheduler error: {e}")
                time.sleep(0.1)
    
    def schedule(self, task, args=(), delay=0, priority=0):
        """调度任务
        
        Args:
            task: 要执行的函数
            args: 函数参数
            delay: 延迟执行的秒数
            priority: 优先级，数字越小优先级越高
        """
        with self.lock:
            # 计算执行时间
            run_time = time.time() + delay
            # 增加计数器，确保同时间同优先级任务的插入顺序
            self.counter += 1
            # 优先级为(执行时间, priority, counter)，这样可以先按时间排序，再按优先级，最后按插入顺序
            self.task_queue.put((run_time, (priority, self.counter), task, args))
            print(f"Scheduled task {task.__name__} to run at {run_time:.2f} (delay: {delay}s, priority: {priority})")
            return True
    
    def wait_for_completion(self):
        """等待所有任务完成"""
        self.task_queue.join()
        print("All scheduled tasks completed")

# 测试任务调度器
def test_scheduler():
    scheduler = TaskScheduler()
    
    # 定义一些测试任务
    def task1():
        print("Task 1 executed")
    
    def task2(name, value):
        print(f"Task 2 executed with parameters: name={name}, value={value}")
    
    def task3():
        print("Task 3 executed")
    
    # 启动调度器
    scheduler.start()
    
    # 调度任务
    scheduler.schedule(task1, delay=1)  # 1秒后执行
    scheduler.schedule(task2, args=("test", 42), delay=2, priority=1)  # 2秒后执行，优先级1
    scheduler.schedule(task3, delay=1, priority=-1)  # 1秒后执行，优先级-1（更高）
    
    # 等待所有任务完成
    time.sleep(3)  # 给任务一些执行时间
    
    # 停止调度器
    scheduler.stop()

if __name__ == "__main__":
    test_scheduler()
```

### 4.2 日志处理系统

使用队列实现一个异步日志处理系统：

```python
import queue
import threading
import time
import logging
import os
from datetime import datetime

# 配置基本日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AsyncLogger:
    def __init__(self, log_file=None, max_queue_size=1000):
        """初始化异步日志器
        
        Args:
            log_file: 日志文件路径，如果为None则只输出到控制台
            max_queue_size: 日志队列的最大大小
        """
        self.log_queue = queue.Queue(maxsize=max_queue_size)
        self.log_file = log_file
        self.running = False
        self.worker_thread = None
        self.lock = threading.RLock()
        
        # 如果指定了日志文件，确保目录存在
        if log_file:
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)
    
    def start(self):
        """启动日志工作线程"""
        with self.lock:
            if self.running:
                return
            self.running = True
            self.worker_thread = threading.Thread(target=self._log_worker)
            self.worker_thread.daemon = True
            self.worker_thread.start()
            logger.info("AsyncLogger started")
    
    def stop(self, timeout=5):
        """停止日志工作线程
        
        Args:
            timeout: 等待工作线程停止的超时时间（秒）
        """
        with self.lock:
            if not self.running:
                return
            self.running = False
            # 添加一个None任务来唤醒工作线程
            self.log_queue.put(None)
            if self.worker_thread:
                self.worker_thread.join(timeout)
                if self.worker_thread.is_alive():
                    logger.warning("AsyncLogger worker thread did not terminate within timeout")
                else:
                    logger.info("AsyncLogger stopped")
    
    def _log_worker(self):
        """日志工作线程函数"""
        file_handle = None
        
        try:
            # 如果指定了日志文件，打开文件
            if self.log_file:
                file_handle = open(self.log_file, 'a', encoding='utf-8')
            
            while self.running:
                try:
                    # 从队列获取日志消息
                    log_entry = self.log_queue.get(timeout=0.1)
                    
                    # 如果收到None，退出循环
                    if log_entry is None:
                        self.log_queue.task_done()
                        break
                    
                    # 格式化日志消息
                    timestamp, level, message = log_entry
                    formatted_log = f"[{timestamp}] [{level}] {message}\n"
                    
                    # 输出到控制台
                    print(formatted_log, end='')
                    
                    # 输出到文件（如果指定）
                    if file_handle:
                        file_handle.write(formatted_log)
                        file_handle.flush()  # 立即写入文件
                    
                    # 标记任务完成
                    self.log_queue.task_done()
                    
                except queue.Empty:
                    # 队列为空，继续循环
                    continue
                except Exception as e:
                    print(f"Error in log worker: {e}")
                    # 即使出错，也要标记任务完成，避免队列阻塞
                    try:
                        self.log_queue.task_done()
                    except ValueError:
                        pass
                    
        finally:
            # 关闭文件
            if file_handle:
                try:
                    file_handle.close()
                except Exception:
                    pass
    
    def log(self, level, message):
        """记录一条日志
        
        Args:
            level: 日志级别
            message: 日志消息
        """
        try:
            # 获取当前时间
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            
            # 将日志消息添加到队列
            try:
                # 尝试非阻塞式添加，如果队列满则打印警告
                self.log_queue.put_nowait((timestamp, level, message))
            except queue.Full:
                # 队列已满，直接打印到控制台（避免日志丢失）
                print(f"WARNING: Log queue is full, log message may be lost: {message}")
                
        except Exception as e:
            # 如果日志记录失败，直接打印到控制台
            print(f"Failed to log message: {e}, message: {message}")
    
    def debug(self, message):
        """记录调试日志"""
        self.log("DEBUG", message)
    
    def info(self, message):
        """记录信息日志"""
        self.log("INFO", message)
    
    def warning(self, message):
        """记录警告日志"""
        self.log("WARNING", message)
    
    def error(self, message):
        """记录错误日志"""
        self.log("ERROR", message)
    
    def critical(self, message):
        """记录严重错误日志"""
        self.log("CRITICAL", message)
    
    def wait_until_empty(self, timeout=None):
        """等待日志队列为空
        
        Args:
            timeout: 超时时间（秒）
        """
        if timeout is None:
            self.log_queue.join()
        else:
            # 简单的超时实现
            start_time = time.time()
            while not self.log_queue.empty() and (time.time() - start_time) < timeout:
                time.sleep(0.01)

# 测试异步日志器
def test_async_logger():
    # 创建异步日志器
    log_file = os.path.join("logs", "test.log")
    async_logger = AsyncLogger(log_file=log_file)
    
    # 启动日志器
    async_logger.start()
    
    # 记录一些日志
    print("Logging messages...")
    for i in range(10):
        async_logger.info(f"This is test log message #{i}")
        async_logger.debug(f"Debug information #{i}")
        if i % 3 == 0:
            async_logger.warning(f"Warning message #{i}")
        if i % 5 == 0:
            async_logger.error(f"Error message #{i}")
        
        # 模拟一些处理时间
        time.sleep(0.1)
    
    # 等待日志队列为空
    print("Waiting for logs to be processed...")
    async_logger.wait_until_empty(timeout=2)
    
    # 停止日志器
    async_logger.stop()
    print(f"Logs written to {log_file}")

if __name__ == "__main__":
    test_async_logger()
```

### 4.3 多线程数据处理管道

使用多个队列和线程创建一个数据处理管道：

```python
import queue
import threading
import time
import random
import string

class DataProcessor:
    def __init__(self):
        # 创建三个队列，分别用于原始数据、处理中和处理完成
        self.raw_queue = queue.Queue(maxsize=100)
        self.processing_queue = queue.Queue(maxsize=100)
        self.completed_queue = queue.Queue(maxsize=100)
        
        # 线程列表
        self.threads = []
        self.running = False
        
        # 统计信息
        self.stats = {
            "raw_count": 0,
            "processing_count": 0,
            "completed_count": 0,
            "errors": 0
        }
        self.stats_lock = threading.Lock()
    
    def start(self, num_producers=2, num_workers=3):
        """启动数据处理管道
        
        Args:
            num_producers: 生产者线程数量
            num_workers: 工作线程数量
        """
        self.running = True
        
        # 创建生产者线程
        for i in range(num_producers):
            t = threading.Thread(target=self._producer_worker, args=(i,))
            t.daemon = True
            t.start()
            self.threads.append(t)
        
        # 创建工作线程
        for i in range(num_workers):
            t = threading.Thread(target=self._process_worker, args=(i,))
            t.daemon = True
            t.start()
            self.threads.append(t)
        
        # 创建消费者线程（输出结果）
        t = threading.Thread(target=self._consumer_worker)
        t.daemon = True
        t.start()
        self.threads.append(t)
        
        print(f"Data pipeline started with {num_producers} producers and {num_workers} workers")
    
    def stop(self, timeout=5):
        """停止数据处理管道
        
        Args:
            timeout: 等待线程停止的超时时间（秒）
        """
        self.running = False
        
        # 等待所有线程停止
        for t in self.threads:
            if t.is_alive():
                t.join(timeout)
        
        print("Data pipeline stopped")
        print(f"Stats - Raw: {self.stats['raw_count']}, Processing: {self.stats['processing_count']}, Completed: {self.stats['completed_count']}, Errors: {self.stats['errors']}")
    
    def _producer_worker(self, worker_id):
        """生产者工作线程，生成原始数据"""
        while self.running:
            try:
                # 生成随机数据
                data = self._generate_data()
                
                # 添加到原始队列
                self.raw_queue.put(data, timeout=0.1)
                
                # 更新统计信息
                with self.stats_lock:
                    self.stats['raw_count'] += 1
                
                # 随机休眠一小段时间
                time.sleep(random.uniform(0.05, 0.2))
                
            except queue.Full:
                # 队列满，继续尝试
                continue
            except Exception as e:
                print(f"Producer {worker_id} error: {e}")
                with self.stats_lock:
                    self.stats['errors'] += 1
    
    def _generate_data(self):
        """生成随机测试数据"""
        # 生成随机字符串
        length = random.randint(5, 10)
        data = ''.join(random.choice(string.ascii_letters) for _ in range(length))
        # 随机数字
        number = random.randint(1, 1000)
        return {
            "id": random.randint(1000, 9999),
            "text": data,
            "number": number,
            "timestamp": time.time()
        }
    
    def _process_worker(self, worker_id):
        """处理工作线程，处理原始数据"""
        while self.running:
            try:
                # 从原始队列获取数据
                data = self.raw_queue.get(timeout=0.1)
                
                # 更新统计信息
                with self.stats_lock:
                    self.stats['processing_count'] += 1
                
                # 处理数据
                processed_data = self._process_data(data)
                
                # 添加到已完成队列
                self.completed_queue.put(processed_data, timeout=0.1)
                
                # 标记任务完成
                self.raw_queue.task_done()
                
            except queue.Empty:
                # 队列为空，继续尝试
                continue
            except queue.Full:
                # 队列满，放回原始队列
                try:
                    self.raw_queue.put(data, timeout=0.1)
                except:
                    pass
                continue
            except Exception as e:
                print(f"Worker {worker_id} error: {e}")
                # 标记任务完成，避免阻塞
                self.raw_queue.task_done()
                with self.stats_lock:
                    self.stats['errors'] += 1
    
    def _process_data(self, data):
        """处理数据的逻辑"""
        # 模拟处理时间
        time.sleep(random.uniform(0.1, 0.3))
        
        # 简单的处理逻辑：
        # 1. 计算文本长度
        # 2. 计算数字的平方
        # 3. 添加处理时间戳
        processed = data.copy()
        processed["text_length"] = len(data["text"])
        processed["number_squared"] = data["number"] ** 2
        processed["processed_at"] = time.time()
        processed["processing_time"] = processed["processed_at"] - data["timestamp"]
        
        return processed
    
    def _consumer_worker(self):
        """消费者工作线程，处理完成的数据"""
        while self.running:
            try:
                # 从已完成队列获取数据
                data = self.completed_queue.get(timeout=0.1)
                
                # 更新统计信息
                with self.stats_lock:
                    self.stats['completed_count'] += 1
                
                # 输出处理结果（在实际应用中可能会写入数据库或文件）
                if self.stats['completed_count'] % 10 == 0:  # 每10个结果输出一次
                    print(f"Processed item #{self.stats['completed_count']}: ID={data['id']}, "
                          f"Text='{data['text']}' ({data['text_length']} chars), "
                          f"Number={data['number']} → {data['number_squared']}, "
                          f"Processing time: {data['processing_time']:.3f}s")
                
                # 标记任务完成
                self.completed_queue.task_done()
                
            except queue.Empty:
                # 队列为空，继续尝试
                continue
            except Exception as e:
                print(f"Consumer error: {e}")
                # 标记任务完成，避免阻塞
                self.completed_queue.task_done()
                with self.stats_lock:
                    self.stats['errors'] += 1
    
    def wait_for_completion(self):
        """等待所有队列处理完成"""
        self.raw_queue.join()
        self.processing_queue.join()
        self.completed_queue.join()
    
    def get_stats(self):
        """获取当前统计信息"""
        with self.stats_lock:
            return self.stats.copy()

# 测试数据处理管道
def test_data_pipeline():
    pipeline = DataProcessor()
    
    # 启动管道
    pipeline.start(num_producers=2, num_workers=3)
    
    # 运行一段时间
    print("Data pipeline running...")
    for i in range(5):
        time.sleep(1)
        stats = pipeline.get_stats()
        print(f"Second {i+1} - Stats: {stats}")
    
    # 停止管道
    pipeline.stop()

if __name__ == "__main__":
    test_data_pipeline()
```

### 4.4 消息队列系统

使用队列实现一个简单的消息队列系统：

```python
import queue
import threading
import time
import uuid

class MessageQueue:
    def __init__(self):
        # 存储所有队列的字典
        self.queues = {}
        # 锁，用于保护队列字典
        self.lock = threading.RLock()
        # 消费者注册表
        self.consumers = {}
    
    def create_queue(self, queue_name):
        """创建一个新队列
        
        Args:
            queue_name: 队列名称
        
        Returns:
            True 如果队列创建成功，False 如果队列已存在
        """
        with self.lock:
            if queue_name in self.queues:
                return False
            self.queues[queue_name] = queue.Queue()
            return True
    
    def delete_queue(self, queue_name):
        """删除一个队列
        
        Args:
            queue_name: 队列名称
        
        Returns:
            True 如果队列删除成功，False 如果队列不存在
        """
        with self.lock:
            if queue_name not in self.queues:
                return False
            # 删除队列
            del self.queues[queue_name]
            # 同时删除该队列的所有消费者
            if queue_name in self.consumers:
                del self.consumers[queue_name]
            return True
    
    def list_queues(self):
        """列出所有队列名称
        
        Returns:
            队列名称列表
        """
        with self.lock:
            return list(self.queues.keys())
    
    def publish(self, queue_name, message, timeout=None):
        """发布消息到队列
        
        Args:
            queue_name: 队列名称
            message: 要发布的消息
            timeout: 超时时间（秒）
        
        Returns:
            True 如果发布成功，False 如果队列不存在或超时
        """
        with self.lock:
            if queue_name not in self.queues:
                return False
            target_queue = self.queues[queue_name]
        
        # 生成消息ID和时间戳
        message_wrapper = {
            "id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "body": message
        }
        
        try:
            target_queue.put(message_wrapper, timeout=timeout)
            return True
        except queue.Full:
            return False
    
    def subscribe(self, queue_name, callback, max_messages=0):
        """订阅队列，注册回调函数
        
        Args:
            queue_name: 队列名称
            callback: 消息处理回调函数
            max_messages: 最大处理消息数，0表示无限
        
        Returns:
            消费者ID，如果队列不存在则返回None
        """
        with self.lock:
            if queue_name not in self.queues:
                return None
            
            # 生成消费者ID
            consumer_id = str(uuid.uuid4())
            
            # 如果该队列还没有消费者列表，创建一个
            if queue_name not in self.consumers:
                self.consumers[queue_name] = {}
            
            # 创建消费者线程
            stop_event = threading.Event()
            self.consumers[queue_name][consumer_id] = {
                "thread": threading.Thread(
                    target=self._consumer_thread,
                    args=(queue_name, callback, max_messages, stop_event)
                ),
                "stop_event": stop_event
            }
            
            # 启动消费者线程
            self.consumers[queue_name][consumer_id]["thread"].daemon = True
            self.consumers[queue_name][consumer_id]["thread"].start()
            
            return consumer_id
    
    def unsubscribe(self, queue_name, consumer_id):
        """取消订阅
        
        Args:
            queue_name: 队列名称
            consumer_id: 消费者ID
        
        Returns:
            True 如果取消成功，False 如果队列或消费者不存在
        """
        with self.lock:
            if (queue_name not in self.consumers or 
                consumer_id not in self.consumers[queue_name]):
                return False
            
            # 设置停止事件
            self.consumers[queue_name][consumer_id]["stop_event"].set()
            
            # 删除消费者
            del self.consumers[queue_name][consumer_id]
            
            # 如果该队列没有消费者了，删除消费者列表
            if not self.consumers[queue_name]:
                del self.consumers[queue_name]
            
            return True
    
    def _consumer_thread(self, queue_name, callback, max_messages, stop_event):
        """消费者线程函数"""
        processed_count = 0
        
        while not stop_event.is_set() and (max_messages == 0 or processed_count < max_messages):
            try:
                # 获取队列引用
                with self.lock:
                    if queue_name not in self.queues:
                        break
                    target_queue = self.queues[queue_name]
                
                # 尝试获取消息，设置超时以便检查停止事件
                try:
                    message = target_queue.get(timeout=0.1)
                except queue.Empty:
                    continue
                
                # 处理消息
                try:
                    callback(message)
                except Exception as e:
                    print(f"Error processing message {message['id']}: {e}")
                
                # 标记任务完成
                target_queue.task_done()
                processed_count += 1
                
            except Exception as e:
                print(f"Consumer thread error: {e}")
                break
    
    def queue_size(self, queue_name):
        """获取队列大小
        
        Args:
            queue_name: 队列名称
        
        Returns:
            队列中的消息数，如果队列不存在则返回-1
        """
        with self.lock:
            if queue_name not in self.queues:
                return -1
            return self.queues[queue_name].qsize()
    
    def wait_for_empty(self, queue_name, timeout=None):
        """等待队列清空
        
        Args:
            queue_name: 队列名称
            timeout: 超时时间（秒）
        
        Returns:
            True 如果队列为空，False 如果队列不存在或超时
        """
        with self.lock:
            if queue_name not in self.queues:
                return False
            target_queue = self.queues[queue_name]
        
        if timeout is None:
            target_queue.join()
            return True
        else:
            # 简单的超时实现
            start_time = time.time()
            while not target_queue.empty() and (time.time() - start_time) < timeout:
                time.sleep(0.01)
            return target_queue.empty()

# 测试消息队列系统
def test_message_queue():
    # 创建消息队列
    mq = MessageQueue()
    
    # 创建一个队列
    mq.create_queue("test_queue")
    print(f"Created queue 'test_queue'")
    print(f"Available queues: {mq.list_queues()}")
    
    # 定义消息处理回调函数
    received_messages = []
    
    def message_handler(message):
        print(f"Received message: {message}")
        received_messages.append(message)
    
    # 订阅队列
    consumer_id = mq.subscribe("test_queue", message_handler)
    print(f"Subscribed to queue with consumer ID: {consumer_id}")
    
    # 发布一些消息
    for i in range(5):
        message = f"Test message #{i}"
        success = mq.publish("test_queue", message)
        print(f"Published message '{message}': {success}")
    
    # 等待消息被处理
    print("Waiting for messages to be processed...")
    time.sleep(1)
    
    # 检查接收到的消息数量
    print(f"Received {len(received_messages)} messages")
    
    # 取消订阅
    mq.unsubscribe("test_queue", consumer_id)
    print("Unsubscribed from queue")
    
    # 等待队列清空
    mq.wait_for_empty("test_queue")
    print("Queue is empty")
    
    # 删除队列
    mq.delete_queue("test_queue")
    print(f"Deleted queue 'test_queue'")
    print(f"Available queues: {mq.list_queues()}")

if __name__ == "__main__":
    test_message_queue()
```

### 4.5 网页爬虫的URL队列

使用队列实现网页爬虫的URL管理：

```python
import queue
import threading
import time
import random
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup  # 需要安装: pip install beautifulsoup4

class UrlQueue:
    def __init__(self, start_urls, max_depth=3):
        """初始化URL队列
        
        Args:
            start_urls: 起始URL列表
            max_depth: 最大爬取深度
        """
        # 使用优先级队列，优先级为深度
        self.url_queue = queue.PriorityQueue()
        # 已访问的URL集合
        self.visited_urls = set()
        # URL锁，保护visited_urls
        self.url_lock = threading.RLock()
        # 最大深度
        self.max_depth = max_depth
        
        # 添加起始URL到队列
        for url in start_urls:
            self.add_url(url, depth=0)
    
    def add_url(self, url, depth=0):
        """添加URL到队列
        
        Args:
            url: 要添加的URL
            depth: 当前深度
        
        Returns:
            True 如果URL被添加，False 如果URL已访问或超过最大深度
        """
        with self.url_lock:
            # 检查URL是否已访问
            if url in self.visited_urls:
                return False
            
            # 检查深度
            if depth > self.max_depth:
                return False
            
            # 标记URL为已访问（但未实际处理）
            self.visited_urls.add(url)
            
            # 添加到队列
            self.url_queue.put((depth, url))
            return True
    
    def get_url(self, timeout=None):
        """从队列获取URL
        
        Args:
            timeout: 超时时间（秒）
        
        Returns:
            (depth, url) 元组，如果队列为空则返回None
        """
        try:
            return self.url_queue.get(timeout=timeout)
        except queue.Empty:
            return None
    
    def mark_done(self):
        """标记当前任务完成"""
        self.url_queue.task_done()
    
    def join(self):
        """等待队列处理完成"""
        self.url_queue.join()
    
    def size(self):
        """获取队列大小"""
        return self.url_queue.qsize()
    
    def visited_count(self):
        """获取已访问URL数量"""
        with self.url_lock:
            return len(self.visited_urls)

class WebCrawler:
    def __init__(self, start_urls, max_depth=3, num_workers=4, rate_limit=2):
        """初始化网页爬虫
        
        Args:
            start_urls: 起始URL列表
            max_depth: 最大爬取深度
            num_workers: 工作线程数量
            rate_limit: 每秒最多爬取的页面数
        """
        self.url_queue = UrlQueue(start_urls, max_depth)
        self.num_workers = num_workers
        self.rate_limit = rate_limit
        self.running = False
        self.workers = []
        self.results = []
        self.results_lock = threading.RLock()
        
        # 用于速率限制的时间戳队列
        self.timestamps = queue.Queue()
    
    def start(self):
        """启动爬虫"""
        self.running = True
        
        # 创建工作线程
        for i in range(self.num_workers):
            worker = threading.Thread(target=self._worker_thread, args=(i,))
            worker.daemon = True
            worker.start()
            self.workers.append(worker)
        
        print(f"Web crawler started with {self.num_workers} workers")
        print(f"Initial URLs: {self.url_queue.visited_count()}")
    
    def stop(self):
        """停止爬虫"""
        self.running = False
        
        # 等待所有工作线程结束
        for worker in self.workers:
            worker.join()
        
        print(f"Web crawler stopped")
        print(f"Total URLs visited: {self.url_queue.visited_count()}")
        print(f"Total results collected: {len(self.results)}")
    
    def _worker_thread(self, worker_id):
        """工作线程函数"""
        while self.running:
            # 获取URL
            url_item = self.url_queue.get(timeout=1)
            if not url_item:
                continue
            
            depth, url = url_item
            
            try:
                # 速率限制
                self._rate_limit()
                
                print(f"Worker {worker_id} crawling {url} (depth {depth})")
                
                # 爬取网页
                page_data = self._crawl_page(url, depth)
                
                # 保存结果
                if page_data:
                    with self.results_lock:
                        self.results.append(page_data)
                        
            except Exception as e:
                print(f"Worker {worker_id} error crawling {url}: {e}")
            finally:
                # 标记任务完成
                self.url_queue.mark_done()
    
    def _rate_limit(self):
        """实现速率限制"""
        current_time = time.time()
        
        # 移除过期的时间戳
        while not self.timestamps.empty() and current_time - self.timestamps.queue[0] > 1:
            self.timestamps.get()
        
        # 如果队列已满，等待
        if self.timestamps.qsize() >= self.rate_limit:
            oldest_time = self.timestamps.get()
            sleep_time = max(0, 1 - (current_time - oldest_time))
            time.sleep(sleep_time)
            current_time = time.time()
        
        # 添加当前时间戳
        self.timestamps.put(current_time)
    
    def _crawl_page(self, url, depth):
        """爬取单个网页
        
        Args:
            url: 要爬取的URL
            depth: 当前深度
        
        Returns:
            页面数据字典，如果爬取失败则返回None
        """
        try:
            # 发送HTTP请求
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # 如果状态码不是200，抛出异常
            
            # 检查内容类型
            if 'text/html' not in response.headers.get('Content-Type', ''):
                print(f"Skipping non-HTML content: {url}")
                return None
            
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 提取标题
            title = soup.title.string.strip() if soup.title else "No title"
            
            # 提取所有链接
            base_url = urlparse(url)
            links = []
            for a_tag in soup.find_all('a', href=True):
                href = a_tag['href']
                # 转换为绝对URL
                absolute_url = urljoin(url, href)
                # 检查是否是同一域名
                parsed_url = urlparse(absolute_url)
                if parsed_url.netloc == base_url.netloc:
                    links.append(absolute_url)
                    # 如果深度未达到最大值，添加到队列
                    if depth < self.url_queue.max_depth:
                        self.url_queue.add_url(absolute_url, depth + 1)
            
            # 返回页面数据
            return {
                'url': url,
                'title': title,
                'depth': depth,
                'status_code': response.status_code,
                'content_length': len(response.text),
                'links_found': len(links),
                'timestamp': time.time()
            }
            
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            return None
    
    def wait_for_completion(self):
        """等待爬取完成"""
        self.url_queue.join()
        print("All URLs processed")
    
    def get_results(self):
        """获取爬取结果
        
        Returns:
            爬取结果列表
        """
        with self.results_lock:
            return self.results.copy()

# 测试网页爬虫（注意：实际使用时请遵守网站的robots.txt规则）
def test_web_crawler():
    # 注意：以下示例使用了一个公共测试网站
    # 在实际使用时，请确保遵守目标网站的爬虫规则
    start_urls = ["http://quotes.toscrape.com/"]
    
    crawler = WebCrawler(
        start_urls=start_urls,
        max_depth=2,
        num_workers=2,
        rate_limit=1  # 降低爬取速率以避免对服务器造成压力
    )
    
    # 启动爬虫
    crawler.start()
    
    try:
        # 运行一段时间或直到完成
        print("Crawling in progress...")
        
        # 等待一段时间后停止
        time.sleep(20)
        
        # 或者等待爬取完成
        # crawler.wait_for_completion()
        
    except KeyboardInterrupt:
        print("\nCrawling interrupted by user")
    finally:
        # 停止爬虫
        crawler.stop()
        
        # 显示一些结果统计
        results = crawler.get_results()
        print(f"\nCrawling Results Summary:")
        print(f"Total pages crawled: {len(results)}")
        
        if results:
            # 按深度分组统计
            depth_count = {}
            for result in results:
                depth = result['depth']
                depth_count[depth] = depth_count.get(depth, 0) + 1
            
            print("Pages by depth:")
            for depth in sorted(depth_count.keys()):
                print(f"  Depth {depth}: {depth_count[depth]} pages")
            
            # 显示几个爬取的页面
            print("\nFirst 3 crawled pages:")
            for i, result in enumerate(results[:3]):
                print(f"  {i+1}. {result['title']} - {result['url']}")

if __name__ == "__main__":
    # 注意：运行此示例可能会向目标网站发送请求
    # 仅在遵守目标网站规则的情况下运行
    print("This is a web crawler example. Uncomment the last line to run it.")
    # test_web_crawler()
```

### 4.6 线程安全的资源池

使用队列实现一个线程安全的资源池：

```python
import queue
import threading
import time

class ResourcePool:
    def __init__(self, create_resource_func, destroy_resource_func=None, min_size=0, max_size=10, 
                 idle_timeout=300, validation_func=None):
        """初始化资源池
        
        Args:
            create_resource_func: 创建资源的函数
            destroy_resource_func: 销毁资源的函数，如果为None则不执行销毁操作
            min_size: 池中资源的最小数量
            max_size: 池中资源的最大数量
            idle_timeout: 资源空闲超时时间（秒）
            validation_func: 验证资源是否有效的函数
        """
        self.create_resource_func = create_resource_func
        self.destroy_resource_func = destroy_resource_func
        self.min_size = min_size
        self.max_size = max_size
        self.idle_timeout = idle_timeout
        self.validation_func = validation_func
        
        # 可用资源队列，元素为(资源, 创建时间)元组
        self.resources = queue.Queue(maxsize=max_size)
        
        # 锁，用于保护计数器等共享状态
        self.lock = threading.RLock()
        
        # 资源计数
        self.total_created = 0
        self.in_use = 0
        
        # 状态标志
        self.running = True
        
        # 启动资源清理线程
        self.cleanup_thread = threading.Thread(target=self._cleanup_thread_func)
        self.cleanup_thread.daemon = True
        self.cleanup_thread.start()
        
        # 预创建最小数量的资源
        self._precreate_resources()
    
    def _precreate_resources(self):
        """预创建最小数量的资源"""
        for _ in range(self.min_size):
            try:
                resource = self.create_resource_func()
                with self.lock:
                    self.total_created += 1
                self.resources.put((resource, time.time()), block=False)
            except Exception as e:
                print(f"Error pre-creating resource: {e}")
    
    def get_resource(self, timeout=None):
        """从池中获取资源
        
        Args:
            timeout: 超时时间（秒）
        
        Returns:
            资源对象
        
        Raises:
            TimeoutError: 如果在超时时间内没有获取到资源
            RuntimeError: 如果池已关闭
        """
        if not self.running:
            raise RuntimeError("Resource pool is closed")
        
        start_time = time.time()
        remaining_timeout = timeout
        
        while True:
            # 尝试从队列获取资源
            try:
                resource, created_time = self.resources.get(block=True, timeout=remaining_timeout)
                
                # 验证资源是否有效
                if self.validation_func and not self.validation_func(resource):
                    # 资源无效，销毁并继续尝试
                    self._destroy_resource(resource)
                    with self.lock:
                        self.total_created -= 1
                    
                    # 更新剩余超时时间
                    if timeout is not None:
                        elapsed = time.time() - start_time
                        remaining_timeout = max(0, timeout - elapsed)
                        if remaining_timeout <= 0:
                            raise TimeoutError("Timeout waiting for valid resource")
                    continue
                
                # 标记资源为使用中
                with self.lock:
                    self.in_use += 1
                
                return resource
                
            except queue.Empty:
                # 队列为空，尝试创建新资源
                with self.lock:
                    if self.total_created < self.max_size:
                        # 可以创建新资源
                        try:
                            resource = self.create_resource_func()
                            self.total_created += 1
                            self.in_use += 1
                            return resource
                        except Exception as e:
                            print(f"Error creating new resource: {e}")
                            # 继续尝试获取已有的资源
                    
                # 无法创建新资源，检查是否超时
                if timeout is not None:
                    elapsed = time.time() - start_time
                    remaining_timeout = max(0, timeout - elapsed)
                    if remaining_timeout <= 0:
                        raise TimeoutError("Timeout waiting for resource")
                
                # 继续循环尝试
                continue
    
    def release_resource(self, resource):
        """释放资源回池
        
        Args:
            resource: 要释放的资源
        """
        if not self.running:
            # 池已关闭，直接销毁资源
            self._destroy_resource(resource)
            with self.lock:
                self.total_created -= 1
            return
        
        # 标记资源为可用
        with self.lock:
            self.in_use -= 1
        
        # 将资源放回队列
        try:
            self.resources.put((resource, time.time()), block=False)
        except queue.Full:
            # 队列已满，销毁资源
            self._destroy_resource(resource)
            with self.lock:
                self.total_created -= 1
    
    def _destroy_resource(self, resource):
        """销毁资源
        
        Args:
            resource: 要销毁的资源
        """
        if self.destroy_resource_func:
            try:
                self.destroy_resource_func(resource)
            except Exception as e:
                print(f"Error destroying resource: {e}")
    
    def _cleanup_thread_func(self):
        """资源清理线程函数"""
        while self.running:
            time.sleep(10)  # 每10秒清理一次
            
            current_time = time.time()
            idle_resources = []
            
            # 收集空闲超时的资源
            try:
                while True:
                    # 尝试获取资源但不标记为完成
                    try:
                        resource, created_time = self.resources.get(block=False)
                        
                        # 检查资源是否空闲超时
                        if current_time - created_time > self.idle_timeout:
                            # 资源超时，收集起来销毁
                            idle_resources.append(resource)
                        else:
                            # 资源未超时，放回队列
                            self.resources.put((resource, created_time), block=False)
                            # 后面的资源也不会超时，可以退出循环
                            break
                    except queue.Empty:
                        break
            except Exception as e:
                print(f"Error during resource cleanup: {e}")
            
            # 销毁超时资源，但保留最小数量的资源
            with self.lock:
                resources_to_destroy = max(0, len(idle_resources) - self.min_size)
            
            for i in range(resources_to_destroy):
                resource = idle_resources[i]
                self._destroy_resource(resource)
                with self.lock:
                    self.total_created -= 1
    
    def close(self):
        """关闭资源池，销毁所有资源"""
        self.running = False
        
        # 等待清理线程结束
        if self.cleanup_thread.is_alive():
            self.cleanup_thread.join(timeout=2)
        
        # 销毁所有剩余资源
        while True:
            try:
                resource, _ = self.resources.get(block=False)
                self._destroy_resource(resource)
                with self.lock:
                    self.total_created -= 1
                self.resources.task_done()
            except queue.Empty:
                break
    
    def get_stats(self):
        """获取资源池统计信息
        
        Returns:
            包含统计信息的字典
        """
        with self.lock:
            return {
                "total_created": self.total_created,
                "available": self.resources.qsize(),
                "in_use": self.in_use,
                "max_size": self.max_size,
                "min_size": self.min_size
            }

# 测试资源池
def test_resource_pool():
    # 模拟数据库连接类
    class DatabaseConnection:
        def __init__(self, connection_id):
            self.connection_id = connection_id
            self.is_closed = False
            print(f"Database connection {connection_id} created")
        
        def close(self):
            if not self.is_closed:
                self.is_closed = True
                print(f"Database connection {self.connection_id} closed")
        
        def execute(self, query):
            if self.is_closed:
                raise RuntimeError("Connection is closed")
            print(f"Connection {self.connection_id} executing: {query}")
            return f"Result from connection {self.connection_id}"
    
    # 全局连接ID计数器
    connection_counter = 0
    counter_lock = threading.Lock()
    
    # 创建连接函数
    def create_connection():
        nonlocal connection_counter
        with counter_lock:
            connection_counter += 1
            return DatabaseConnection(connection_counter)
    
    # 销毁连接函数
    def destroy_connection(conn):
        conn.close()
    
    # 验证连接函数
    def validate_connection(conn):
        return not conn.is_closed
    
    # 创建资源池
    pool = ResourcePool(
        create_resource_func=create_connection,
        destroy_resource_func=destroy_connection,
        min_size=2,
        max_size=5,
        idle_timeout=5,  # 5秒空闲超时
        validation_func=validate_connection
    )
    
    # 模拟多个线程使用资源池
    def worker(worker_id):
        for i in range(3):
            try:
                # 获取连接
                print(f"Worker {worker_id} trying to get connection...")
                conn = pool.get_resource(timeout=2)
                print(f"Worker {worker_id} got connection {conn.connection_id}")
                
                # 使用连接
                result = conn.execute(f"SELECT * FROM table WHERE id = {i}")
                print(f"Worker {worker_id} query result: {result}")
                
                # 模拟工作
                time.sleep(random.uniform(0.1, 0.5))
                
                # 归还连接
                print(f"Worker {worker_id} releasing connection {conn.connection_id}")
                pool.release_resource(conn)
                
            except Exception as e:
                print(f"Worker {worker_id} error: {e}")
    
    # 创建并启动工作线程
    workers = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(i,))
        workers.append(t)
        t.start()
    
    # 等待工作线程完成
    for t in workers:
        t.join()
    
    # 输出统计信息
    stats = pool.get_stats()
    print(f"\nResource pool stats: {stats}")
    
    # 等待资源超时被清理
    print("\nWaiting for idle resources to be cleaned up...")
    time.sleep(6)
    
    # 再次输出统计信息
    stats = pool.get_stats()
    print(f"\nResource pool stats after cleanup: {stats}")
    
    # 关闭资源池
    print("\nClosing resource pool...")
    pool.close()
    
    print("Test completed")

if __name__ == "__main__":
    test_resource_pool()

## 5. 性能分析

### 5.1 时间复杂度分析

不同队列操作的时间复杂度：

| 操作 | Queue/FIFO | LifoQueue/LIFO | PriorityQueue | SimpleQueue |
|------|------------|----------------|---------------|-------------|
| put | O(1) | O(1) | O(log n) | O(1) |
| get | O(1) | O(1) | O(log n) | O(1) |
| qsize | O(1) | O(1) | O(1) | O(1) |
| empty | O(1) | O(1) | O(1) | 不适用 |
| full | O(1) | O(1) | O(1) | 不适用 |
| task_done | O(1) | O(1) | O(1) | 不适用 |
| join | O(1) | O(1) | O(1) | 不适用 |

**说明：**
- **Queue/FIFO和LifoQueue/LIFO**：这些队列基于collections.deque实现，所以put和get操作都是O(1)时间复杂度
- **PriorityQueue**：这个队列基于heapq模块实现，所以put和get操作都是O(log n)时间复杂度，其中n是队列中的元素数量
- **SimpleQueue**：这个队列也是基于collections.deque实现，但接口更简单，只支持基本的FIFO操作

### 5.2 性能测试代码

下面是一个简单的性能测试程序，可以比较不同队列类型在各种操作下的性能：

```python
import queue
import time
import random

def test_queue_performance(queue_class, size=100000, ops=100000):
    """测试队列性能
    
    Args:
        queue_class: 队列类
        size: 初始队列大小
        ops: 测试操作次数
    """
    print(f"\nTesting {queue_class.__name__}:")
    
    # 创建队列
    if queue_class == queue.PriorityQueue:
        q = queue_class()
    else:
        q = queue_class(maxsize=size * 2)
    
    # 初始化队列
    print(f"Initializing queue with {size} items...")
    start_time = time.time()
    
    if queue_class == queue.PriorityQueue:
        # 对于优先级队列，需要添加(优先级, 数据)对
        for i in range(size):
            q.put((random.randint(1, 100), i))
    else:
        # 对于其他队列，直接添加数据
        for i in range(size):
            q.put(i)
    
    init_time = time.time() - start_time
    print(f"Initialization time: {init_time:.6f} seconds")
    
    # 测试put操作
    print(f"Testing {ops} put operations...")
    start_time = time.time()
    
    if queue_class == queue.PriorityQueue:
        for i in range(ops):
            q.put((random.randint(1, 100), i + size))
    else:
        for i in range(ops):
            q.put(i + size)
    
    put_time = time.time() - start_time
    print(f"Put operations time: {put_time:.6f} seconds")
    print(f"Average put time: {put_time / ops * 1e6:.2f} microseconds per operation")
    
    # 测试get操作
    print(f"Testing {ops} get operations...")
    start_time = time.time()
    
    for _ in range(ops):
        q.get()
    
    get_time = time.time() - start_time
    print(f"Get operations time: {get_time:.6f} seconds")
    print(f"Average get time: {get_time / ops * 1e6:.2f} microseconds per operation")
    
    # 测试混合操作（一半put，一半get）
    print(f"Testing mixed operations ({ops//2} put, {ops//2} get)...")
    start_time = time.time()
    
    for i in range(ops//2):
        if queue_class == queue.PriorityQueue:
            q.put((random.randint(1, 100), i))
        else:
            q.put(i)
        q.get()
    
    mixed_time = time.time() - start_time
    print(f"Mixed operations time: {mixed_time:.6f} seconds")
    print(f"Average mixed operation time: {mixed_time / ops * 1e6:.2f} microseconds per operation")

# 运行性能测试
def run_performance_tests():
    print("Starting queue performance tests...")
    
    # 测试不同的队列类型
    test_queue_performance(queue.Queue, size=10000, ops=100000)
    test_queue_performance(queue.LifoQueue, size=10000, ops=100000)
    test_queue_performance(queue.PriorityQueue, size=10000, ops=50000)  # 优先级队列操作较慢，减少操作次数
    
    print("\nPerformance tests completed!")

if __name__ == "__main__":
    run_performance_tests()
```

## 6. 使用注意事项

### 6.1 线程安全考虑

- **线程安全保证**：`queue`模块中的队列实现都是线程安全的，可以在多线程环境中安全使用
- **避免死锁**：在使用`join()`方法时，确保所有`get()`操作都有对应的`task_done()`调用，否则`join()`会永远阻塞
- **避免竞争条件**：虽然队列操作本身是线程安全的，但在使用队列的上下文代码中可能仍然存在竞争条件，需要根据具体情况使用锁

### 6.2 内存管理

- **设置合理的队列大小**：对于有界队列，设置合适的`maxsize`参数，避免内存溢出
- **及时消费队列**：确保队列中的元素被及时消费，避免队列无限增长
- **处理异常情况**：在异常发生时，确保资源被正确释放，避免队列中残留未处理的任务

### 6.3 超时和阻塞操作

- **避免无限阻塞**：在生产环境中，尽量使用带超时的`put()`和`get()`操作，避免线程无限阻塞
- **非阻塞操作**：使用`put_nowait()`和`get_nowait()`进行非阻塞操作，在队列满或空时会立即抛出异常
- **超时处理**：正确处理超时异常，避免因为超时而导致程序逻辑错误

### 6.4 优先级队列特殊考虑

- **元素比较**：优先级队列中的元素必须是可比较的，通常使用元组(优先级, 数据)形式
- **优先级冲突**：当多个元素具有相同优先级时，队列会使用元组的下一个元素进行比较，可以使用计数器确保同优先级元素的插入顺序
- **性能影响**：优先级队列的`put()`和`get()`操作时间复杂度为O(log n)，在大数据量时性能会低于普通队列

### 6.5 队列选择

- **FIFO队列(Queue)**：适用于需要按照先进先出顺序处理任务的场景
- **LIFO队列(LifoQueue)**：适用于需要按照后进先出顺序处理任务的场景，如深度优先搜索
- **优先级队列(PriorityQueue)**：适用于需要按照优先级处理任务的场景
- **SimpleQueue**：适用于简单的FIFO队列需求，不需要任务跟踪功能

## 7. 总结与最佳实践

### 7.1 主要优势

- **线程安全**：`queue`模块提供的队列实现都是线程安全的，无需额外的锁机制
- **阻塞操作**：支持阻塞式的`put()`和`get()`操作，便于实现生产者-消费者模式
- **多种队列类型**：提供多种队列类型，满足不同的业务需求
- **简单易用**：API设计简单直观，易于学习和使用
- **性能良好**：基于高效的数据结构实现，性能表现良好

### 7.2 最佳实践

- **选择合适的队列类型**：根据实际需求选择最适合的队列类型
- **合理设置队列大小**：对于有界队列，设置合理的`maxsize`参数
- **使用超时机制**：在生产环境中，优先使用带超时的队列操作
- **正确处理异常**：处理队列操作可能抛出的异常，如`queue.Empty`和`queue.Full`
- **避免死锁**：确保所有`get()`操作都有对应的`task_done()`调用
- **资源管理**：在不需要队列时，确保队列中的任务被正确处理，避免资源泄露
- **监控和调优**：监控队列的大小和性能，根据实际情况进行调优

### 7.3 选择使用建议

不同场景下的队列选择建议：

1. **任务调度系统**：使用`PriorityQueue`，根据任务优先级进行调度
2. **生产者-消费者模式**：使用`Queue`，实现标准的先进先出处理
3. **深度优先搜索**：使用`LifoQueue`，实现后进先出的处理顺序
4. **简单消息传递**：使用`SimpleQueue`，简单高效
5. **资源池管理**：使用`Queue`，管理共享资源的分配和回收
6. **限流和缓冲**：使用有界的`Queue`，实现限流和缓冲功能

### 7.4 学习总结

`queue`模块是Python多线程编程中的重要工具，提供了线程安全的队列实现。通过合理使用这些队列，可以有效地实现线程间通信、任务调度、资源管理等功能。在使用过程中，需要注意选择合适的队列类型、设置合理的参数、正确处理异常，并避免死锁和资源泄露等问题。

通过本章节的学习，我们掌握了`queue`模块的核心功能和使用方法，以及在实际应用中的最佳实践。在实际开发中，应该根据具体需求选择合适的队列类型，并结合其他Python功能模块，构建高效、可靠的多线程应用。