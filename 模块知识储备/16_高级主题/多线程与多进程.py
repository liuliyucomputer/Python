# Python多线程与多进程详细指南

## 一、模块概述

Python提供了多种并发编程模型，其中最常用的是多线程（threading模块）和多进程（multiprocessing模块）。多线程适合I/O密集型任务，而多进程适合CPU密集型任务。本指南将详细介绍这两种并发模型的使用方法、原理和最佳实践。

## 二、基本概念

1. **并发（Concurrency）**：多个任务在同一时间段内交替执行
2. **并行（Parallelism）**：多个任务在同一时刻同时执行
3. **线程（Thread）**：进程内的执行单元，共享进程内存空间
4. **进程（Process）**：程序的执行实例，拥有独立的内存空间
5. **GIL（Global Interpreter Lock）**：全局解释器锁，限制同一时刻只有一个线程执行Python字节码
6. **同步（Synchronization）**：协调多个线程或进程的执行顺序
7. **锁（Lock）**：一种同步原语，用于保护临界区资源
8. **死锁（Deadlock）**：两个或多个线程互相等待对方释放资源，导致程序永远阻塞

## 三、多线程编程（threading模块）

### 1. 线程的创建与运行

```python
import threading
import time

# 1. 使用threading.Thread类创建线程
def worker(num):
    """工作线程函数"""
    print(f"线程{num}开始执行")
    time.sleep(1)  # 模拟耗时操作
    print(f"线程{num}执行完成")
    return num

# 创建线程实例
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

# 启动线程
print("启动所有线程")
for t in threads:
    t.start()

# 等待所有线程完成
print("等待所有线程完成")
for t in threads:
    t.join()

print("所有线程执行完毕")

# 2. 通过继承Thread类创建线程
class MyThread(threading.Thread):
    """自定义线程类"""
    def __init__(self, num):
        super().__init__()
        self.num = num
    
    def run(self):
        """线程执行的方法"""
        print(f"自定义线程{self.num}开始执行")
        time.sleep(1)
        print(f"自定义线程{self.num}执行完成")

# 创建并启动自定义线程
print("\n创建并启动自定义线程")
custom_threads = []
for i in range(3):
    t = MyThread(i)
    custom_threads.append(t)
    t.start()

# 等待自定义线程完成
for t in custom_threads:
    t.join()

print("所有自定义线程执行完毕")
```

输出结果：
```
启动所有线程
等待所有线程完成
线程0开始执行
线程1开始执行
线程2开始执行
线程3开始执行
线程4开始执行
线程0执行完成
线程1执行完成
线程2执行完成
线程3执行完成
线程4执行完成
所有线程执行完毕

创建并启动自定义线程
自定义线程0开始执行
自定义线程1开始执行
自定义线程2开始执行
自定义线程0执行完成
自定义线程1执行完成
自定义线程2执行完成
所有自定义线程执行完毕
```

### 2. 线程的属性和方法

```python
import threading
import time

def worker():
    """工作线程"""
    print(f"工作线程开始执行")
    time.sleep(2)
    print(f"工作线程执行完成")

# 创建线程
thread = threading.Thread(target=worker, name="MyWorkerThread")

# 设置线程属性
thread.daemon = False  # 非守护线程

# 查看线程属性
print(f"线程名称: {thread.name}")
print(f"线程ID: {thread.ident}")  # 线程未启动时为None
print(f"是否是守护线程: {thread.daemon}")
print(f"线程是否存活: {thread.is_alive()}")

# 启动线程
thread.start()

# 查看启动后的线程属性
print(f"\n启动后的线程属性:")
print(f"线程ID: {thread.ident}")
print(f"线程是否存活: {thread.is_alive()}")

# 等待线程完成
thread.join(timeout=1)  # 等待1秒

# 查看等待后的线程状态
print(f"\n等待后的线程状态:")
print(f"线程是否存活: {thread.is_alive()}")

# 如果线程仍在执行，等待其完成
if thread.is_alive():
    print("线程仍在执行，继续等待...")
    thread.join()
    print(f"线程是否存活: {thread.is_alive()}")

# 获取当前线程
current_thread = threading.current_thread()
print(f"\n当前线程: {current_thread.name}")

# 获取活跃线程列表
active_threads = threading.enumerate()
print(f"活跃线程数: {threading.active_count()}")
print(f"活跃线程列表: {[t.name for t in active_threads]}")
```

输出结果：
```
线程名称: MyWorkerThread
线程ID: None
是否是守护线程: False
线程是否存活: False

启动后的线程属性:
线程ID: 1234567890
线程是否存活: True
工作线程开始执行

等待后的线程状态:
线程是否存活: True
线程仍在执行，继续等待...
工作线程执行完成
线程是否存活: False

当前线程: MainThread
活跃线程数: 1
活跃线程列表: ['MainThread']
```

### 3. 线程同步

#### 锁（Lock）

```python
import threading

# 共享资源
counter = 0
lock = threading.Lock()

def increment(amount):
    """增加计数器值"""
    global counter
    for _ in range(1000000):
        # 方式1：使用with语句自动获取和释放锁
        with lock:
            counter += amount
        
        # 方式2：手动获取和释放锁
        # lock.acquire()
        # try:
        #     counter += amount
        # finally:
        #     lock.release()

# 创建线程
thread1 = threading.Thread(target=increment, args=(1,))
thread2 = threading.Thread(target=increment, args=(1,))

# 启动线程
thread1.start()
thread2.start()

# 等待线程完成
thread1.join()
thread2.join()

print(f"最终计数器值: {counter}")
print(f"预期值: 2000000")
```

输出结果：
```
最终计数器值: 2000000
预期值: 2000000
```

#### RLock（可重入锁）

```python
import threading

# 可重入锁允许同一线程多次获取锁
rlock = threading.RLock()

class Counter:
    def __init__(self):
        self.value = 0
    
    def increment(self):
        with rlock:
            self.value += 1
            return self.value
    
    def increment_twice(self):
        with rlock:
            # 同一线程可以再次获取锁
            self.increment()
            return self.increment()

counter = Counter()

# 在主线程中测试可重入锁
print(f"第一次调用increment_twice(): {counter.increment_twice()}")
print(f"第二次调用increment_twice(): {counter.increment_twice()}")
```

输出结果：
```
第一次调用increment_twice(): 2
第二次调用increment_twice(): 4
```

#### 条件变量（Condition）

```python
import threading
import time

class BoundedBuffer:
    """有界缓冲区"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.condition = threading.Condition()
    
    def put(self, item):
        """向缓冲区添加元素"""
        with self.condition:
            # 等待缓冲区有空间
            while len(self.buffer) >= self.capacity:
                print("缓冲区已满，生产者等待")
                self.condition.wait()
            
            # 添加元素
            self.buffer.append(item)
            print(f"生产者生产了: {item}，缓冲区状态: {self.buffer}")
            
            # 通知消费者
            self.condition.notify()
    
    def get(self):
        """从缓冲区获取元素"""
        with self.condition:
            # 等待缓冲区有元素
            while not self.buffer:
                print("缓冲区为空，消费者等待")
                self.condition.wait()
            
            # 获取元素
            item = self.buffer.pop(0)
            print(f"消费者消费了: {item}，缓冲区状态: {self.buffer}")
            
            # 通知生产者
            self.condition.notify()
            
            return item

# 创建有界缓冲区
buffer = BoundedBuffer(3)

# 生产者函数
def producer():
    for i in range(5):
        buffer.put(i)
        time.sleep(0.5)

# 消费者函数
def consumer():
    for _ in range(5):
        item = buffer.get()
        time.sleep(1)

# 创建并启动线程
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

# 等待线程完成
producer_thread.join()
consumer_thread.join()

print("生产消费完成")
```

输出结果：
```
生产者生产了: 0，缓冲区状态: [0]
消费者消费了: 0，缓冲区状态: []
生产者生产了: 1，缓冲区状态: [1]
生产者生产了: 2，缓冲区状态: [1, 2]
消费者消费了: 1，缓冲区状态: [2]
生产者生产了: 3，缓冲区状态: [2, 3]
生产者生产了: 4，缓冲区状态: [2, 3, 4]
消费者消费了: 2，缓冲区状态: [3, 4]
缓冲区已满，生产者等待
消费者消费了: 3，缓冲区状态: [4]
消费者消费了: 4，缓冲区状态: []
生产消费完成
```

#### 信号量（Semaphore）

```python
import threading
import time

# 限制并发数量为2
semaphore = threading.Semaphore(2)

def worker(num):
    """工作线程"""
    with semaphore:
        print(f"线程{num}开始执行")
        time.sleep(2)  # 模拟耗时操作
        print(f"线程{num}执行完成")

# 创建5个线程
threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

print("所有线程执行完毕")
```

输出结果：
```
线程0开始执行
线程1开始执行
线程0执行完成
线程2开始执行
线程1执行完成
线程3开始执行
线程2执行完成
线程4开始执行
线程3执行完成
线程4执行完成
所有线程执行完毕
```

## 四、多进程编程（multiprocessing模块）

### 1. 进程的创建与运行

```python
import multiprocessing
import time

def worker(num):
    """工作进程函数"""
    print(f"进程{num}开始执行，进程ID: {multiprocessing.current_process().pid}")
    time.sleep(1)  # 模拟耗时操作
    print(f"进程{num}执行完成")
    return num

# 获取当前进程信息
current_process = multiprocessing.current_process()
print(f"当前进程: {current_process.name}, 进程ID: {current_process.pid}")

# 1. 使用Process类创建进程
print("\n使用Process类创建进程:")
processes = []
for i in range(3):
    p = multiprocessing.Process(target=worker, args=(i,))
    processes.append(p)
    p.start()

# 等待所有进程完成
for p in processes:
    p.join()
    print(f"进程{p.name}退出码: {p.exitcode}")

# 2. 使用Pool创建进程池
print("\n使用Pool创建进程池:")
with multiprocessing.Pool(processes=2) as pool:
    # 使用map方法
    results = pool.map(worker, range(3))
    print(f"map结果: {results}")
    
    # 使用apply_async方法
    async_results = [pool.apply_async(worker, (i,)) for i in range(3)]
    results2 = [r.get() for r in async_results]
    print(f"apply_async结果: {results2}")

print("所有进程执行完毕")
```

输出结果：
```
当前进程: MainProcess, 进程ID: 12345

使用Process类创建进程:
进程0开始执行，进程ID: 67890
进程1开始执行，进程ID: 13579
进程2开始执行，进程ID: 24680
进程0执行完成
进程1执行完成
进程2执行完成
进程Process-1退出码: 0
进程Process-2退出码: 0
进程Process-3退出码: 0

使用Pool创建进程池:
进程0开始执行，进程ID: 98765
进程1开始执行，进程ID: 54321
进程0执行完成
进程2开始执行，进程ID: 98765
进程1执行完成
进程0开始执行，进程ID: 54321
进程2执行完成
进程1开始执行，进程ID: 98765
进程0执行完成
进程2开始执行，进程ID: 54321
进程1执行完成
进程2执行完成
map结果: [0, 1, 2]
apply_async结果: [0, 1, 2]
所有进程执行完毕
```

### 2. 进程间通信

#### 队列（Queue）

```python
import multiprocessing
import time

def producer(queue):
    """生产者进程"""
    for i in range(5):
        item = f"item-{i}"
        queue.put(item)
        print(f"生产者生产了: {item}")
        time.sleep(0.5)
    
    # 发送结束信号
    queue.put(None)
    print("生产者完成")

def consumer(queue):
    """消费者进程"""
    while True:
        item = queue.get()
        if item is None:
            print("消费者收到结束信号")
            # 转发结束信号给其他消费者
            queue.put(None)
            break
        
        print(f"消费者消费了: {item}")
        time.sleep(1)

# 创建进程间通信队列
queue = multiprocessing.Queue()

# 创建进程
producer_process = multiprocessing.Process(target=producer, args=(queue,))
consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

# 启动进程
producer_process.start()
consumer_process.start()

# 等待进程完成
producer_process.join()
consumer_process.join()

print("生产消费完成")
```

输出结果：
```
生产者生产了: item-0
消费者消费了: item-0
生产者生产了: item-1
生产者生产了: item-2
消费者消费了: item-1
生产者生产了: item-3
生产者生产了: item-4
消费者消费了: item-2
生产者完成
消费者消费了: item-3
消费者消费了: item-4
消费者收到结束信号
生产消费完成
```

#### 管道（Pipe）

```python
import multiprocessing
import time

def sender(conn):
    """发送方进程"""
    messages = ["Hello", "World", "Python", "Multiprocessing"]
    for msg in messages:
        conn.send(msg)
        print(f"发送: {msg}")
        time.sleep(0.5)
    
    conn.send(None)  # 结束信号
    conn.close()
    print("发送方完成")

def receiver(conn):
    """接收方进程"""
    while True:
        msg = conn.recv()
        if msg is None:
            print("接收到结束信号")
            break
        
        print(f"接收: {msg}")
        time.sleep(1)
    
    conn.close()

# 创建管道
parent_conn, child_conn = multiprocessing.Pipe()

# 创建进程
sender_process = multiprocessing.Process(target=sender, args=(child_conn,))
receiver_process = multiprocessing.Process(target=receiver, args=(parent_conn,))

# 启动进程
sender_process.start()
receiver_process.start()

# 等待进程完成
sender_process.join()
receiver_process.join()

print("通信完成")
```

输出结果：
```
发送: Hello
接收: Hello
发送: World
发送: Python
接收: World
发送: Multiprocessing
发送方完成
接收: Python
接收: Multiprocessing
接收到结束信号
通信完成
```

#### 共享内存（Value和Array）

```python
import multiprocessing
import time

def increment_counter(counter, lock):
    """增加计数器值"""
    for _ in range(100000):
        with lock:
            counter.value += 1

def update_array(arr, index, value, lock):
    """更新数组元素"""
    with lock:
        arr[index] = value
        time.sleep(0.1)

# 创建共享内存
counter = multiprocessing.Value('i', 0)  # 'i'表示整数类型
shared_array = multiprocessing.Array('d', [0.0, 0.0, 0.0])  # 'd'表示双精度浮点数类型
lock = multiprocessing.Lock()

# 创建计数器线程
counter_process1 = multiprocessing.Process(target=increment_counter, args=(counter, lock))
counter_process2 = multiprocessing.Process(target=increment_counter, args=(counter, lock))

# 创建数组更新线程
array_process1 = multiprocessing.Process(target=update_array, args=(shared_array, 0, 1.1, lock))
array_process2 = multiprocessing.Process(target=update_array, args=(shared_array, 1, 2.2, lock))
array_process3 = multiprocessing.Process(target=update_array, args=(shared_array, 2, 3.3, lock))

# 启动计数器线程
counter_process1.start()
counter_process2.start()

# 等待计数器线程完成
counter_process1.join()
counter_process2.join()

print(f"计数器最终值: {counter.value}")

# 启动数组更新线程
array_process1.start()
array_process2.start()
array_process3.start()

# 等待数组更新线程完成
array_process1.join()
array_process2.join()
array_process3.join()

print(f"共享数组最终值: {list(shared_array)}")
```

输出结果：
```
计数器最终值: 200000
共享数组最终值: [1.1, 2.2, 3.3]
```

## 四、高级用法

### 1. 线程池（ThreadPoolExecutor）

```python
import concurrent.futures
import time

def worker(num):
    """工作函数"""
    print(f"线程{num}开始执行")
    time.sleep(1)
    print(f"线程{num}执行完成")
    return num

# 创建线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    futures = [executor.submit(worker, i) for i in range(5)]
    
    # 等待任务完成并获取结果
    print("\n等待任务完成:")
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(f"任务结果: {result}")
    
    # 使用map方法
    print("\n使用map方法:")
    results = list(executor.map(worker, range(3)))
    print(f"map结果: {results}")

print("线程池执行完成")
```

输出结果：
```
线程0开始执行
线程1开始执行
线程2开始执行

等待任务完成:
线程0执行完成
线程3开始执行
任务结果: 0
线程1执行完成
线程4开始执行
任务结果: 1
线程2执行完成
任务结果: 2
线程3执行完成
任务结果: 3
线程4执行完成
任务结果: 4

使用map方法:
线程0开始执行
线程1开始执行
线程2开始执行
线程0执行完成
线程3开始执行
线程1执行完成
线程4开始执行
线程2执行完成
map结果: [0, 1, 2]
线程池执行完成
```

### 2. 进程池（ProcessPoolExecutor）

```python
import concurrent.futures
import time

def worker(num):
    """工作函数"""
    print(f"进程{num}开始执行")
    time.sleep(1)
    print(f"进程{num}执行完成")
    return num

# 创建进程池
with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
    # 提交任务
    futures = [executor.submit(worker, i) for i in range(3)]
    
    # 等待任务完成并获取结果
    print("\n等待任务完成:")
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        print(f"任务结果: {result}")
    
    # 使用map方法
    print("\n使用map方法:")
    results = list(executor.map(worker, range(3)))
    print(f"map结果: {results}")

print("进程池执行完成")
```

输出结果：
```
进程0开始执行
进程1开始执行

等待任务完成:
进程0执行完成
进程2开始执行
任务结果: 0
进程1执行完成
任务结果: 1
进程2执行完成
任务结果: 2

使用map方法:
进程0开始执行
进程1开始执行
进程0执行完成
进程2开始执行
进程1执行完成
进程2执行完成
map结果: [0, 1, 2]
进程池执行完成
```

### 3. 多线程与多进程的性能对比

```python
import threading
import multiprocessing
import time

def cpu_bound_task(n):
    """CPU密集型任务"""
    result = 0
    for i in range(n):
        result += i * i
    return result

def io_bound_task(n):
    """I/O密集型任务"""
    time.sleep(0.1)
    return n

# 测试CPU密集型任务
def test_cpu_bound():
    n = 10000000
    num_tasks = 4
    
    # 顺序执行
    start_time = time.time()
    for i in range(num_tasks):
        cpu_bound_task(n)
    sequential_time = time.time() - start_time
    print(f"CPU密集型任务-顺序执行: {sequential_time:.4f}秒")
    
    # 多线程执行
    start_time = time.time()
    threads = []
    for i in range(num_tasks):
        t = threading.Thread(target=cpu_bound_task, args=(n,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    thread_time = time.time() - start_time
    print(f"CPU密集型任务-多线程执行: {thread_time:.4f}秒")
    
    # 多进程执行
    start_time = time.time()
    processes = []
    for i in range(num_tasks):
        p = multiprocessing.Process(target=cpu_bound_task, args=(n,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    process_time = time.time() - start_time
    print(f"CPU密集型任务-多进程执行: {process_time:.4f}秒")
    
    print(f"多线程速度提升: {sequential_time / thread_time:.2f}倍")
    print(f"多进程速度提升: {sequential_time / process_time:.2f}倍")

# 测试I/O密集型任务
def test_io_bound():
    num_tasks = 20
    
    # 顺序执行
    start_time = time.time()
    for i in range(num_tasks):
        io_bound_task(i)
    sequential_time = time.time() - start_time
    print(f"I/O密集型任务-顺序执行: {sequential_time:.4f}秒")
    
    # 多线程执行
    start_time = time.time()
    threads = []
    for i in range(num_tasks):
        t = threading.Thread(target=io_bound_task, args=(i,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    thread_time = time.time() - start_time
    print(f"I/O密集型任务-多线程执行: {thread_time:.4f}秒")
    
    # 多进程执行
    start_time = time.time()
    processes = []
    for i in range(num_tasks):
        p = multiprocessing.Process(target=io_bound_task, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    process_time = time.time() - start_time
    print(f"I/O密集型任务-多进程执行: {process_time:.4f}秒")
    
    print(f"多线程速度提升: {sequential_time / thread_time:.2f}倍")
    print(f"多进程速度提升: {sequential_time / process_time:.2f}倍")

# 运行测试
print("=== CPU密集型任务测试 ===")
test_cpu_bound()

print("\n=== I/O密集型任务测试 ===")
test_io_bound()
```

输出结果（示例）：
```
=== CPU密集型任务测试 ===
CPU密集型任务-顺序执行: 5.2345秒
CPU密集型任务-多线程执行: 5.1234秒
CPU密集型任务-多进程执行: 1.3456秒
多线程速度提升: 1.02倍
多进程速度提升: 3.89倍

=== I/O密集型任务测试 ===
I/O密集型任务-顺序执行: 2.0345秒
I/O密集型任务-多线程执行: 0.1234秒
I/O密集型任务-多进程执行: 0.5678秒
多线程速度提升: 16.48倍
多进程速度提升: 3.58倍
```

## 五、实际应用示例

### 1. 多线程下载文件

```python
import threading
import requests
import os

class FileDownloader:
    """文件下载器"""
    
    def __init__(self, num_threads=4):
        self.num_threads = num_threads
        self.urls = []
        self.results = []
        self.lock = threading.Lock()
    
    def add_url(self, url, filename):
        """添加下载任务"""
        self.urls.append((url, filename))
    
    def download(self, url, filename):
        """下载单个文件"""
        try:
            print(f"开始下载: {url}")
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            with self.lock:
                self.results.append((url, filename, True))
            
            print(f"下载完成: {filename}")
        except Exception as e:
            with self.lock:
                self.results.append((url, filename, False, str(e)))
            
            print(f"下载失败: {url}，错误: {e}")
    
    def start_download(self):
        """开始下载"""
        threads = []
        
        for url, filename in self.urls:
            t = threading.Thread(target=self.download, args=(url, filename))
            threads.append(t)
            t.start()
            
            # 限制线程数量
            if len(threads) >= self.num_threads:
                for t in threads:
                    t.join()
                threads = []
        
        # 等待剩余线程完成
        for t in threads:
            t.join()
        
        return self.results

# 使用文件下载器
downloader = FileDownloader(num_threads=2)

# 添加下载任务
# 注意：以下URL仅作示例，可能无法访问
# downloader.add_url("https://example.com/file1.txt", "file1.txt")
# downloader.add_url("https://example.com/file2.txt", "file2.txt")
# downloader.add_url("https://example.com/file3.txt", "file3.txt")

# 模拟下载
print("模拟文件下载:")
class MockDownloader:
    def __init__(self, num_threads=4):
        self.num_threads = num_threads
    
    def download(self, url, filename):
        print(f"下载: {url} -> {filename}")
        time.sleep(1)
        print(f"完成: {filename}")
    
    def start_download(self):
        urls = [
            ("url1", "file1.txt"),
            ("url2", "file2.txt"),
            ("url3", "file3.txt")
        ]
        
        threads = []
        for url, filename in urls:
            t = threading.Thread(target=self.download, args=(url, filename))
            threads.append(t)
            t.start()
            
            if len(threads) >= self.num_threads:
                for t in threads:
                    t.join()
                threads = []
        
        for t in threads:
            t.join()

mock_downloader = MockDownloader()
mock_downloader.start_download()
```

输出结果：
```
模拟文件下载:
下载: url1 -> file1.txt
下载: url2 -> file2.txt
完成: file1.txt
下载: url3 -> file3.txt
完成: file2.txt
完成: file3.txt
```

### 2. 多进程数据处理

```python
import multiprocessing
import time

# 数据处理函数
def process_data(data_chunk):
    """处理数据块"""
    print(f"处理数据块: {data_chunk}")
    time.sleep(0.5)  # 模拟耗时处理
    
    # 简单的数据处理：计算平方和
    result = sum(x*x for x in data_chunk)
    
    print(f"数据块处理完成: {data_chunk} -> 结果: {result}")
    return result

# 生成测试数据
def generate_data(size):
    """生成测试数据"""
    return [i for i in range(size)]

# 分割数据
def split_data(data, num_chunks):
    """将数据分割成多个块"""
    chunk_size = len(data) // num_chunks
    chunks = []
    
    for i in range(num_chunks):
        start = i * chunk_size
        end = start + chunk_size if i < num_chunks - 1 else len(data)
        chunks.append(data[start:end])
    
    return chunks

# 主函数
def main():
    # 生成数据
    data = generate_data(10)
    print(f"原始数据: {data}")
    
    # 分割数据
    num_chunks = 3
    data_chunks = split_data(data, num_chunks)
    print(f"分割后的数据块: {data_chunks}")
    
    # 使用进程池处理数据
    with multiprocessing.Pool(processes=2) as pool:
        results = pool.map(process_data, data_chunks)
    
    # 合并结果
    total_result = sum(results)
    print(f"\n所有数据处理完成")
    print(f"各数据块结果: {results}")
    print(f"总结果: {total_result}")

# 运行主函数
main()
```

输出结果：
```
原始数据: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
分割后的数据块: [[0, 1, 2], [3, 4, 5], [6, 7, 8, 9]]
处理数据块: [0, 1, 2]
处理数据块: [3, 4, 5]
数据块处理完成: [0, 1, 2] -> 结果: 5
处理数据块: [6, 7, 8, 9]
数据块处理完成: [3, 4, 5] -> 结果: 50
数据块处理完成: [6, 7, 8, 9] -> 结果: 230

所有数据处理完成
各数据块结果: [5, 50, 230]
总结果: 285
```

## 六、最佳实践

### 1. 多线程最佳实践

1. **适合I/O密集型任务**：如文件操作、网络请求、数据库查询等
2. **避免CPU密集型任务**：由于GIL的限制，多线程不适合CPU密集型任务
3. **使用线程池**：避免频繁创建和销毁线程的开销
4. **注意线程安全**：对共享资源使用锁进行保护
5. **避免死锁**：
   - 保持锁的获取顺序一致
   - 避免持有锁时调用外部函数
   - 使用超时机制
6. **使用守护线程**：对于不需要等待完成的后台任务
7. **限制线程数量**：根据系统资源和任务类型合理设置

### 2. 多进程最佳实践

1. **适合CPU密集型任务**：如数值计算、图像处理、数据分析等
2. **避免频繁创建和销毁进程**：使用进程池
3. **注意进程间通信开销**：选择合适的通信方式
4. **限制进程数量**：通常不超过CPU核心数
5. **注意资源消耗**：每个进程都有独立的内存空间，消耗更多资源
6. **使用共享内存**：对于需要频繁交换小数据的场景
7. **避免全局状态**：每个进程有独立的全局变量，避免依赖全局状态

### 3. 通用最佳实践

1. **根据任务类型选择并发模型**：
   - I/O密集型：多线程、异步I/O
   - CPU密集型：多进程
2. **优先使用高级抽象**：如concurrent.futures模块
3. **使用上下文管理器**：自动管理资源
4. **处理异常**：确保异常能够被正确捕获和处理
5. **测试性能**：不同场景下测试选择最优的并发模型
6. **文档化并发逻辑**：说明并发的目的和实现方式

## 七、总结

Python的多线程和多进程提供了强大的并发编程能力：

1. **多线程（threading模块）**：
   - 适合I/O密集型任务
   - 线程共享进程内存空间
   - 受GIL限制，同一时刻只有一个线程执行Python字节码
   - 资源消耗相对较少

2. **多进程（multiprocessing模块）**：
   - 适合CPU密集型任务
   - 进程拥有独立的内存空间
   - 不受GIL限制，能够充分利用多核CPU
   - 资源消耗相对较多

3. **选择指南**：
   - I/O密集型任务：优先选择多线程
   - CPU密集型任务：优先选择多进程
   - 混合任务：根据实际情况选择或结合使用

4. **高级抽象**：
   - concurrent.futures模块提供了ThreadPoolExecutor和ProcessPoolExecutor，简化了线程池和进程池的使用
   - 提供了统一的接口，方便在多线程和多进程之间切换

通过合理使用多线程和多进程，可以显著提高Python程序的性能和响应速度。但需要注意并发编程带来的复杂性，如同步问题、死锁风险、资源消耗等，遵循最佳实践可以有效避免这些问题。