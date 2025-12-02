# multiprocessing模块 - Python多进程编程详解

Python的`multiprocessing`模块提供了跨平台的多进程编程支持，能够充分利用多核CPU，避免GIL（全局解释器锁）的限制。本文档将详细介绍`multiprocessing`模块的核心功能、使用方法、最佳实践以及实际应用案例。

## 1. 核心功能概览

`multiprocessing`模块的主要功能包括：

- 进程的创建和管理
- 进程间通信机制（队列、管道、共享内存）
- 进程同步原语（锁、事件、条件变量、信号量、栅栏）
- 进程池（用于并行执行任务）
- 进程管理器（用于共享复杂对象）
- 进程本地存储

## 2. 基本进程创建与管理

### 2.1 进程的基本概念

进程是程序在执行过程中分配和管理资源的基本单位，每个进程都有自己独立的内存空间。与线程不同，多进程可以真正实现并行计算，充分利用多核CPU。

### 2.2 创建进程的两种方式

#### 方式一：继承`multiprocessing.Process`类

```python
import multiprocessing
import os
import time

class MyProcess(multiprocessing.Process):
    def __init__(self, process_id, name, delay):
        multiprocessing.Process.__init__(self)
        self.process_id = process_id
        self.name = name
        self.delay = delay
    
    def run(self):
        print(f"进程 {self.name} (ID: {os.getpid()}) 开始执行")
        print_time(self.name, self.delay, 5)
        print(f"进程 {self.name} (ID: {os.getpid()}) 执行完成")

def print_time(process_name, delay, counter):
    while counter:
        time.sleep(delay)
        print(f"{process_name}: {time.ctime(time.time())} (PID: {os.getpid()})")
        counter -= 1

if __name__ == "__main__":
    # 在Windows中，多进程必须在if __name__ == "__main__"块中运行
    print(f"主进程ID: {os.getpid()}")
    
    # 创建新进程
    process1 = MyProcess(1, "Process-1", 1)
    process2 = MyProcess(2, "Process-2", 2)
    
    # 开启新进程
    process1.start()
    process2.start()
    
    # 显示活跃进程
    print(f"活跃进程数量: {len(multiprocessing.active_children())}")
    
    # 等待所有进程完成
    process1.join()
    process2.join()
    
    print("所有子进程已完成，主进程退出")
```

#### 方式二：传入函数对象

```python
import multiprocessing
import os
import time

def print_time(process_name, delay, counter):
    print(f"进程 {process_name} 开始执行，PID: {os.getpid()}")
    while counter:
        time.sleep(delay)
        print(f"{process_name}: {time.ctime(time.time())} (PID: {os.getpid()})")
        counter -= 1
    print(f"进程 {process_name} 执行完成")

if __name__ == "__main__":
    print(f"主进程ID: {os.getpid()}")
    
    # 创建进程
    process1 = multiprocessing.Process(target=print_time, args=("Process-1", 1, 5))
    process2 = multiprocessing.Process(target=print_time, args=("Process-2", 2, 5))
    
    # 启动进程
    process1.start()
    process2.start()
    
    # 等待进程完成
    process1.join()
    process2.join()
    
    print("所有子进程已完成，主进程退出")
```

### 2.3 进程生命周期

进程的生命周期包括以下几个阶段：

1. **创建（New）**：通过`multiprocessing.Process()`创建进程对象
2. **就绪（Ready）**：调用`start()`方法后，进程等待CPU调度
3. **运行（Running）**：进程获得CPU时间片，执行`run()`方法
4. **阻塞（Blocked）**：进程因某些原因暂停执行（如等待I/O、获取锁）
5. **终止（Terminated）**：进程执行完毕或被终止

### 2.4 进程的主要方法

- `start()`：启动进程，调用进程的`run()`方法
- `run()`：进程的主要执行函数，可被子类重写
- `join([timeout])`：等待进程终止，可选超时时间
- `is_alive()`：判断进程是否在运行中
- `terminate()`：强制终止进程
- `kill()`：强制终止进程（Unix-like系统上使用SIGKILL信号）
- `close()`：关闭进程对象，释放资源
- `name/ident`：进程名称/进程ID
- `daemon`：守护进程标志

### 2.5 守护进程与非守护进程

- **守护进程**：当所有非守护进程结束时，守护进程会被强制终止
- **非守护进程**：默认类型，即使主进程结束，非守护进程也会继续执行直到完成

```python
import multiprocessing
import os
import time

def daemon_process():
    print(f"守护进程启动，PID: {os.getpid()}")
    while True:
        print("守护进程运行中...")
        time.sleep(1)

def non_daemon_process():
    print(f"非守护进程启动，PID: {os.getpid()}")
    for i in range(3):
        print(f"非守护进程计数: {i+1}")
        time.sleep(1)
    print("非守护进程结束")

if __name__ == "__main__":
    print(f"主进程ID: {os.getpid()}")
    
    # 创建守护进程
    daemon_proc = multiprocessing.Process(target=daemon_process)
    daemon_proc.daemon = True  # 设置为守护进程
    
    # 创建非守护进程
    non_daemon_proc = multiprocessing.Process(target=non_daemon_process)
    
    # 启动进程
    daemon_proc.start()
    non_daemon_proc.start()
    
    # 主进程等待非守护进程完成
    non_daemon_proc.join()
    print("主进程结束")
    # 此时守护进程会被强制终止
```

## 3. 进程间通信（IPC）机制

由于每个进程都有独立的内存空间，进程间通信需要特殊的机制。`multiprocessing`提供了多种进程间通信方式。

### 3.1 Queue（队列）

`Queue`是进程安全的队列实现，用于在多个进程之间安全地传递消息。

```python
import multiprocessing
import time
import random

def producer(queue, items_count):
    """生产者函数，向队列中放入数据"""
    for i in range(items_count):
        # 生成随机数据
        item = f"Item-{i}-{random.randint(1, 100)}"
        # 放入队列
        queue.put(item)
        print(f"生产者: 放入 {item}，队列大小: {queue.qsize()}")
        # 模拟生产时间
        time.sleep(random.uniform(0.1, 0.5))
    # 放入结束信号
    queue.put(None)
    print("生产者: 完成所有任务")

def consumer(queue, consumer_id):
    """消费者函数，从队列中获取数据"""
    while True:
        # 从队列获取数据
        item = queue.get()
        # 检查是否结束信号
        if item is None:
            # 将结束信号放回队列，供其他消费者使用
            queue.put(None)
            print(f"消费者 {consumer_id}: 收到结束信号")
            break
        print(f"消费者 {consumer_id}: 消费 {item}")
        # 模拟消费时间
        time.sleep(random.uniform(0.2, 0.7))
        # 标记任务完成
        queue.task_done()

if __name__ == "__main__":
    # 创建进程间队列
    queue = multiprocessing.Queue(maxsize=5)
    
    # 创建生产者和消费者进程
    producer_process = multiprocessing.Process(target=producer, args=(queue, 10))
    consumer1_process = multiprocessing.Process(target=consumer, args=(queue, 1))
    consumer2_process = multiprocessing.Process(target=consumer, args=(queue, 2))
    
    # 启动进程
    producer_process.start()
    consumer1_process.start()
    consumer2_process.start()
    
    # 等待生产者完成
    producer_process.join()
    
    # 等待队列中的所有任务被处理
    queue.join()
    
    # 等待消费者完成
    consumer1_process.join()
    consumer2_process.join()
    
    print("所有进程已完成")
```

### 3.2 Pipe（管道）

`Pipe`提供了两个连接端，可以在两个进程之间进行双向通信。

```python
import multiprocessing
import time

def sender(conn, messages):
    """发送数据的进程"""
    print("发送者开始发送数据")
    for message in messages:
        conn.send(message)
        print(f"发送者: 发送 {message}")
        time.sleep(1)
    # 发送结束信号
    conn.send("END")
    print("发送者: 完成发送")
    # 关闭连接
    conn.close()

def receiver(conn):
    """接收数据的进程"""
    print("接收者开始接收数据")
    while True:
        # 接收数据
        message = conn.recv()
        print(f"接收者: 收到 {message}")
        # 检查结束信号
        if message == "END":
            print("接收者: 收到结束信号")
            break
    # 关闭连接
    conn.close()

if __name__ == "__main__":
    # 创建管道，返回两个连接端
    parent_conn, child_conn = multiprocessing.Pipe()
    
    # 要发送的消息
    messages = ["Hello", "World", "Python", "Multiprocessing"]
    
    # 创建发送和接收进程
    sender_process = multiprocessing.Process(target=sender, args=(child_conn, messages))
    receiver_process = multiprocessing.Process(target=receiver, args=(parent_conn,))
    
    # 启动进程
    sender_process.start()
    receiver_process.start()
    
    # 等待进程完成
    sender_process.join()
    receiver_process.join()
    
    print("通信完成")
```

### 3.3 共享内存（Shared Memory）

`multiprocessing`提供了几种共享内存的方式：

#### 3.3.1 Value 和 Array

`Value`和`Array`用于在多个进程之间共享基本数据类型和数组。

```python
import multiprocessing
import time

def increment_value(shared_value, lock):
    """增加共享值"""
    for _ in range(100000):
        # 使用锁保护共享资源
        with lock:
            shared_value.value += 1

def modify_array(shared_array, lock):
    """修改共享数组"""
    for i in range(len(shared_array)):
        with lock:
            shared_array[i] += 1
        time.sleep(0.01)

if __name__ == "__main__":
    # 创建锁
    lock = multiprocessing.Lock()
    
    # 创建共享整数值，'i'表示有符号整型
    shared_counter = multiprocessing.Value('i', 0)
    print(f"初始计数器值: {shared_counter.value}")
    
    # 创建多个进程来增加计数器
    processes = []
    for _ in range(5):
        p = multiprocessing.Process(target=increment_value, args=(shared_counter, lock))
        processes.append(p)
        p.start()
    
    # 等待所有进程完成
    for p in processes:
        p.join()
    
    print(f"最终计数器值: {shared_counter.value} (应为500000)")
    
    # 创建共享数组，'d'表示双精度浮点数
    shared_array = multiprocessing.Array('d', [0.0, 1.0, 2.0, 3.0, 4.0])
    print(f"初始数组值: {list(shared_array)}")
    
    # 创建进程来修改数组
    p = multiprocessing.Process(target=modify_array, args=(shared_array, lock))
    p.start()
    p.join()
    
    print(f"最终数组值: {list(shared_array)}")
```

#### 3.3.2 SharedMemory

Python 3.8+ 引入的`SharedMemory`提供了更灵活的共享内存块。

```python
import multiprocessing
import numpy as np
from multiprocessing import shared_memory
import time

def worker(shm_name, shape, dtype):
    """在共享内存上操作的工作进程"""
    # 访问已存在的共享内存块
    existing_shm = shared_memory.SharedMemory(name=shm_name)
    
    # 创建共享内存的numpy数组视图
    np_array = np.ndarray(shape, dtype=dtype, buffer=existing_shm.buf)
    
    # 修改数组
    print(f"工作进程: 开始修改数组")
    np_array[:] = np_array * 2  # 所有元素乘以2
    print(f"工作进程: 修改后的数组前5个元素: {np_array[:5]}")
    
    # 等待一段时间，以便主进程可以检查变化
    time.sleep(2)
    
    # 关闭共享内存
    existing_shm.close()

if __name__ == "__main__":
    # 创建一个大数组
    size = 1000000
    arr = np.ones(size, dtype=np.float64)
    print(f"主进程: 原始数组前5个元素: {arr[:5]}")
    
    # 创建共享内存
    shm = shared_memory.SharedMemory(create=True, size=arr.nbytes)
    
    # 创建共享内存的numpy数组视图
    shared_arr = np.ndarray(arr.shape, dtype=arr.dtype, buffer=shm.buf)
    
    # 将数据复制到共享内存
    shared_arr[:] = arr[:]
    
    # 创建工作进程
    p = multiprocessing.Process(
        target=worker,
        args=(shm.name, arr.shape, arr.dtype)
    )
    
    # 启动进程
    p.start()
    
    # 等待一段时间，然后检查数组变化
    time.sleep(1)
    print(f"主进程: 工作中检查数组前5个元素: {shared_arr[:5]}")
    
    # 等待进程完成
    p.join()
    
    # 再次检查最终结果
    print(f"主进程: 最终数组前5个元素: {shared_arr[:5]}")
    
    # 释放共享内存
    shm.close()
    shm.unlink()  # 删除共享内存块
```

### 3.4 Manager

`Manager`提供了一种创建可在不同进程之间共享的Python对象的方法，支持列表、字典、命名空间等复杂对象。

```python
import multiprocessing
import time

def modify_data(shared_list, shared_dict, item):
    """修改共享数据"""
    # 修改共享列表
    shared_list.append(item)
    print(f"进程 {multiprocessing.current_process().name}: 添加 {item} 到列表，当前列表: {shared_list}")
    
    # 修改共享字典
    shared_dict[item] = f"Value-{item}"
    print(f"进程 {multiprocessing.current_process().name}: 更新字典，当前字典: {shared_dict}")
    
    time.sleep(0.5)

def access_namespace(shared_namespace):
    """访问共享命名空间"""
    shared_namespace.counter = getattr(shared_namespace, 'counter', 0) + 1
    print(f"进程 {multiprocessing.current_process().name}: 命名空间计数器: {shared_namespace.counter}")
    
    # 添加新属性
    if not hasattr(shared_namespace, 'timestamp'):
        shared_namespace.timestamp = time.time()
    print(f"进程 {multiprocessing.current_process().name}: 命名空间时间戳: {shared_namespace.timestamp}")

if __name__ == "__main__":
    # 创建Manager
    with multiprocessing.Manager() as manager:
        # 创建共享列表和字典
        shared_list = manager.list()
        shared_dict = manager.dict()
        shared_namespace = manager.Namespace()
        
        print("初始共享列表:", shared_list)
        print("初始共享字典:", shared_dict)
        
        # 创建多个进程来修改数据
        processes = []
        for i in range(5):
            p1 = multiprocessing.Process(target=modify_data, args=(shared_list, shared_dict, i))
            p2 = multiprocessing.Process(target=access_namespace, args=(shared_namespace,))
            processes.extend([p1, p2])
            p1.start()
            p2.start()
        
        # 等待所有进程完成
        for p in processes:
            p.join()
        
        print("\n最终共享列表:", shared_list)
        print("最终共享字典:", shared_dict)
        print(f"最终命名空间计数器: {shared_namespace.counter}")
        print(f"最终命名空间时间戳: {shared_namespace.timestamp}")
```

## 4. 进程同步原语

进程同步用于协调多个进程的执行，避免竞态条件和数据不一致。

### 4.1 Lock（互斥锁）

`Lock`确保在同一时间只有一个进程可以访问共享资源。

```python
import multiprocessing
import time

# 共享资源计数器
counter = 0

def increment_counter(lock, iterations):
    global counter
    for _ in range(iterations):
        # 获取锁
        lock.acquire()
        try:
            # 临界区
            current = counter
            time.sleep(0.001)  # 模拟一些处理
            counter = current + 1
        finally:
            # 释放锁
            lock.release()

# 使用上下文管理器（更推荐）
def increment_counter_safe(lock, iterations):
    global counter
    for _ in range(iterations):
        with lock:
            current = counter
            time.sleep(0.001)  # 模拟一些处理
            counter = current + 1

if __name__ == "__main__":
    # 创建锁
    lock = multiprocessing.Lock()
    
    # 创建进程
    processes = []
    iterations = 1000
    
    for _ in range(5):
        # 可以使用increment_counter或increment_counter_safe
        p = multiprocessing.Process(target=increment_counter_safe, args=(lock, iterations))
        processes.append(p)
        p.start()
    
    # 等待所有进程完成
    for p in processes:
        p.join()
    
    print(f"最终计数器值: {counter}")  # 应为5000
```

### 4.2 RLock（可重入锁）

`RLock`允许同一进程多次获取同一个锁。

```python
import multiprocessing

def recursive_function(lock, depth, max_depth):
    if depth > max_depth:
        return
    
    # 获取锁（即使在同一进程中已获取）
    with lock:
        print(f"深度 {depth}: 获取锁")
        # 递归调用
        recursive_function(lock, depth + 1, max_depth)
        print(f"深度 {depth}: 释放锁")

if __name__ == "__main__":
    # 创建可重入锁
    rlock = multiprocessing.RLock()
    
    # 创建进程
    p = multiprocessing.Process(target=recursive_function, args=(rlock, 1, 3))
    p.start()
    p.join()
```

### 4.3 Event（事件）

`Event`是一种简单的进程同步机制，一个进程设置事件，其他进程等待事件被设置。

```python
import multiprocessing
import time

def waiter(event):
    print("等待者: 等待事件触发")
    event.wait()  # 阻塞直到事件被设置
    print("等待者: 事件已触发，继续执行")
    
    # 等待事件重置
    event.clear()
    print("等待者: 等待事件再次触发")
    event.wait(timeout=2)  # 带超时的等待
    if event.is_set():
        print("等待者: 事件再次触发")
    else:
        print("等待者: 超时，事件未触发")

def setter(event):
    print("设置者: 准备触发事件")
    time.sleep(3)
    print("设置者: 触发事件")
    event.set()
    
    # 不重置事件，看看等待者的超时情况
    time.sleep(1)
    print("设置者: 完成")

if __name__ == "__main__":
    # 创建事件
    event = multiprocessing.Event()
    
    # 创建进程
    waiter_process = multiprocessing.Process(target=waiter, args=(event,))
    setter_process = multiprocessing.Process(target=setter, args=(event,))
    
    # 启动进程
    waiter_process.start()
    setter_process.start()
    
    # 等待进程完成
    waiter_process.join()
    setter_process.join()
```

### 4.4 Condition（条件变量）

`Condition`允许进程在特定条件满足时进行等待，在条件满足时被通知。

```python
import multiprocessing
import time
import random

class SharedBuffer:
    def __init__(self, max_size=5):
        self.buffer = []
        self.max_size = max_size
        self.condition = multiprocessing.Condition()
    
    def produce(self, item):
        with self.condition:
            # 等待缓冲区有空间
            while len(self.buffer) >= self.max_size:
                print(f"生产者: 缓冲区已满，等待...")
                self.condition.wait()
            
            # 生产数据
            self.buffer.append(item)
            print(f"生产者: 生产 {item}，缓冲区: {self.buffer}")
            
            # 通知消费者有新数据
            self.condition.notify_all()
    
    def consume(self):
        with self.condition:
            # 等待缓冲区有数据
            while not self.buffer:
                print(f"消费者: 缓冲区为空，等待...")
                self.condition.wait()
            
            # 消费数据
            item = self.buffer.pop(0)
            print(f"消费者: 消费 {item}，缓冲区: {self.buffer}")
            
            # 通知生产者有空间
            self.condition.notify_all()
            return item

def producer_task(buffer, items_count):
    for i in range(items_count):
        item = f"Item-{i}"
        buffer.produce(item)
        time.sleep(random.uniform(0.1, 1.0))

def consumer_task(buffer, items_count):
    for _ in range(items_count):
        buffer.consume()
        time.sleep(random.uniform(0.2, 1.5))

if __name__ == "__main__":
    # 创建共享缓冲区
    buffer = SharedBuffer(max_size=3)
    
    # 创建进程
    producer = multiprocessing.Process(target=producer_task, args=(buffer, 5))
    consumer = multiprocessing.Process(target=consumer_task, args=(buffer, 5))
    
    # 启动进程
    producer.start()
    consumer.start()
    
    # 等待进程完成
    producer.join()
    consumer.join()
```

### 4.5 Semaphore（信号量）

`Semaphore`控制对共享资源的访问数量，允许多个进程同时访问，但限制最大访问数量。

```python
import multiprocessing
import time
import random

def access_resource(semaphore, process_id):
    print(f"进程 {process_id}: 尝试访问资源")
    # 获取信号量
    semaphore.acquire()
    try:
        print(f"进程 {process_id}: 成功访问资源")
        # 模拟资源使用
        time.sleep(random.uniform(0.5, 2.0))
    finally:
        # 释放信号量
        print(f"进程 {process_id}: 释放资源")
        semaphore.release()

if __name__ == "__main__":
    # 创建信号量，最多允许2个进程同时访问
    semaphore = multiprocessing.Semaphore(2)
    
    # 创建进程
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=access_resource, args=(semaphore, i))
        processes.append(p)
        p.start()
        time.sleep(0.1)  # 短暂延迟，让输出更清晰
    
    # 等待所有进程完成
    for p in processes:
        p.join()
```

### 4.6 BoundedSemaphore（有界信号量）

`BoundedSemaphore`确保信号量不会超过初始值，防止过度释放。

```python
import multiprocessing

def test_bounded_semaphore():
    # 创建有界信号量
    bounded_sem = multiprocessing.BoundedSemaphore(2)
    
    # 获取信号量
    print("获取第一个信号量")
    bounded_sem.acquire()
    print("获取第二个信号量")
    bounded_sem.acquire()
    
    # 释放信号量
    print("释放第一个信号量")
    bounded_sem.release()
    print("释放第二个信号量")
    bounded_sem.release()
    
    # 错误：过度释放会引发ValueError
    try:
        print("尝试过度释放")
        bounded_sem.release()
    except ValueError as e:
        print(f"正确捕获异常: {e}")

if __name__ == "__main__":
    # 在主进程中测试，或者可以在子进程中测试
    test_bounded_semaphore()
```

### 4.7 Barrier（栅栏）

`Barrier`同步多个进程，让它们在某个点等待，直到所有进程都到达该点后一起继续执行。

```python
import multiprocessing
import time
import random

def worker(barrier, worker_id):
    print(f"工作者 {worker_id}: 开始执行")
    # 模拟工作
    work_time = random.uniform(1, 3)
    time.sleep(work_time)
    print(f"工作者 {worker_id}: 到达栅栏点 (耗时 {work_time:.2f}s)")
    
    # 等待所有工作者到达
    barrier.wait()
    print(f"工作者 {worker_id}: 通过栅栏，继续执行")
    
    # 再次工作
    time.sleep(random.uniform(0.5, 1.5))
    print(f"工作者 {worker_id}: 完成所有工作")

if __name__ == "__main__":
    # 创建栅栏，需要4个进程到达才能通过
    barrier = multiprocessing.Barrier(4)
    
    # 创建进程
    processes = []
    for i in range(4):
        p = multiprocessing.Process(target=worker, args=(barrier, i))
        processes.append(p)
        p.start()
    
    # 等待所有进程完成
    for p in processes:
        p.join()
    
    print("所有进程已完成")
```

## 5. 进程池（Pool）

`Pool`提供了一种简单的方式来并行执行多个函数调用，管理工作进程池。

### 5.1 基本使用

```python
import multiprocessing
import time
import random

def worker_function(x):
    """工作函数"""
    print(f"进程 {multiprocessing.current_process().name} 处理任务 {x}")
    # 模拟工作负载
    time.sleep(random.uniform(0.5, 2.0))
    result = x * x
    print(f"进程 {multiprocessing.current_process().name} 完成任务 {x}，结果: {result}")
    return result

if __name__ == "__main__":
    # 创建进程池，进程数为CPU核心数
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # 方法1: map - 将函数应用于可迭代对象中的每个元素
        print("\n使用map方法:")
        inputs = [1, 2, 3, 4, 5, 6, 7, 8]
        results1 = pool.map(worker_function, inputs)
        print(f"map结果: {results1}")
        
        # 方法2: apply_async - 异步应用函数
        print("\n使用apply_async方法:")
        futures = [pool.apply_async(worker_function, (x,)) for x in inputs]
        results2 = [future.get() for future in futures]  # 获取结果（会阻塞）
        print(f"apply_async结果: {results2}")
        
        # 方法3: starmap - 支持多参数
        print("\n使用starmap方法:")
        multi_inputs = [(1, 2), (3, 4), (5, 6)]
        def multi_param_func(a, b):
            return a + b
        results3 = pool.starmap(multi_param_func, multi_inputs)
        print(f"starmap结果: {results3}")
        
        # 方法4: imap - 迭代器版本的map
        print("\n使用imap方法:")
        for result in pool.imap(worker_function, inputs):
            print(f"imap结果项: {result}")
    
    # 进程池已自动关闭
    print("\n进程池已关闭")
```

### 5.2 进程池的回调函数

```python
import multiprocessing
import time
import random

# 全局结果列表
results = []
results_lock = multiprocessing.Lock()

def worker_function(x):
    """工作函数"""
    print(f"进程 {multiprocessing.current_process().name} 处理任务 {x}")
    time.sleep(random.uniform(0.5, 1.5))
    result = x * x
    return result

def callback_function(result):
    """回调函数，在任务完成时被调用"""
    print(f"回调函数: 收到结果 {result}")
    with results_lock:
        results.append(result)

def error_callback_function(error):
    """错误回调函数，在任务出错时被调用"""
    print(f"错误回调: 任务失败 {error}")

def failing_function(x):
    """会失败的函数"""
    if x % 3 == 0:
        raise ValueError(f"任务 {x} 故意失败")
    return x * 2

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        # 使用回调函数
        print("\n使用回调函数:")
        futures = []
        for i in range(10):
            future = pool.apply_async(worker_function, (i,), callback=callback_function)
            futures.append(future)
        
        # 等待所有任务完成
        for future in futures:
            future.wait()
        
        print(f"最终结果列表: {results}")
        
        # 使用错误回调
        print("\n使用错误回调:")
        error_futures = []
        for i in range(10):
            future = pool.apply_async(
                failing_function, 
                (i,), 
                callback=callback_function,
                error_callback=error_callback_function
            )
            error_futures.append(future)
        
        # 等待所有任务完成
        for future in error_futures:
            try:
                future.wait()
            except:
                pass  # 错误已经被error_callback处理
```

## 6. 实际应用示例

### 6.1 CPU密集型任务并行处理

```python
import multiprocessing
import time
import math

def is_prime(n):
    """判断一个数是否为素数"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(start, end):
    """找出指定范围内的所有素数"""
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def parallel_prime_search(max_number, num_processes=None):
    """并行搜索素数"""
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()
    
    # 计算每个进程的搜索范围
    chunk_size = max_number // num_processes
    ranges = []
    for i in range(num_processes):
        start = i * chunk_size + 1
        # 确保最后一个进程覆盖所有剩余数字
        end = max_number if i == num_processes - 1 else (i + 1) * chunk_size
        ranges.append((start, end))
    
    # 使用进程池并行处理
    with multiprocessing.Pool(processes=num_processes) as pool:
        # 将每个范围的搜索任务提交给进程池
        results = pool.starmap(find_primes_in_range, ranges)
    
    # 合并结果
    all_primes = []
    for primes in results:
        all_primes.extend(primes)
    
    # 排序结果
    all_primes.sort()
    return all_primes

if __name__ == "__main__":
    max_number = 100000
    
    # 串行执行
    start_time = time.time()
    serial_primes = find_primes_in_range(1, max_number)
    serial_time = time.time() - start_time
    print(f"串行执行: 找到 {len(serial_primes)} 个素数，耗时 {serial_time:.4f} 秒")
    print(f"前10个素数: {serial_primes[:10]}")
    print(f"后10个素数: {serial_primes[-10:]}")
    
    # 并行执行
    start_time = time.time()
    parallel_primes = parallel_prime_search(max_number)
    parallel_time = time.time() - start_time
    print(f"\n并行执行: 找到 {len(parallel_primes)} 个素数，耗时 {parallel_time:.4f} 秒")
    print(f"前10个素数: {parallel_primes[:10]}")
    print(f"后10个素数: {parallel_primes[-10:]}")
    
    # 计算加速比
    speedup = serial_time / parallel_time
    print(f"\n加速比: {speedup:.2f}x")
    print(f"效率: {speedup / multiprocessing.cpu_count() * 100:.1f}%")
```

### 6.2 并行文件处理

```python
import multiprocessing
import os
import time
import shutil

def process_file(file_path, output_dir):
    """处理单个文件"""
    filename = os.path.basename(file_path)
    output_path = os.path.join(output_dir, f"processed_{filename}")
    
    try:
        # 模拟文件处理（例如：读取、转换、写入）
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 模拟处理时间
        time.sleep(0.1)
        
        # 模拟处理结果（例如：转换为大写）
        processed_content = content.upper()
        
        # 写入结果文件
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        print(f"处理完成: {filename} -> processed_{filename}")
        return True
    except Exception as e:
        print(f"处理失败 {filename}: {e}")
        return False

def parallel_file_processor(input_dir, output_dir, num_processes=None):
    """并行处理目录中的所有文件"""
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()
    
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    
    # 获取所有文件
    all_files = []
    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
    
    print(f"找到 {len(all_files)} 个文件需要处理")
    
    # 准备参数列表
    tasks = [(file, output_dir) for file in all_files]
    
    # 使用进程池并行处理
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(process_file, tasks)
    
    # 统计结果
    success_count = sum(results)
    print(f"\n处理完成: 成功 {success_count} 个，失败 {len(results) - success_count} 个")
    return success_count

if __name__ == "__main__":
    # 示例使用（需要先创建一些测试文件）
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base_dir, "test_files")
    output_dir = os.path.join(base_dir, "processed_files")
    
    # 创建测试文件
    print("创建测试文件...")
    os.makedirs(input_dir, exist_ok=True)
    for i in range(50):
        with open(os.path.join(input_dir, f"test_{i}.txt"), 'w') as f:
            f.write(f"This is test file number {i}\n")
            f.write("Contains some sample text for processing.")
    
    # 并行处理文件
    print("\n开始并行处理文件...")
    start_time = time.time()
    success_count = parallel_file_processor(input_dir, output_dir)
    end_time = time.time()
    
    print(f"\n总耗时: {end_time - start_time:.4f} 秒")
    print(f"平均处理时间: {(end_time - start_time) / success_count:.4f} 秒/文件")
    
    # 清理测试文件
    # shutil.rmtree(input_dir)
    # shutil.rmtree(output_dir)
```

### 6.3 分布式计算示例

```python
import multiprocessing
import time
import numpy as np

def compute_chunk(chunk, chunk_id):
    """计算数据块的统计信息"""
    print(f"进程 {chunk_id} 处理数据块，大小: {len(chunk)}")
    
    # 计算统计信息
    result = {
        'chunk_id': chunk_id,
        'sum': np.sum(chunk),
        'mean': np.mean(chunk),
        'min': np.min(chunk),
        'max': np.max(chunk),
        'count': len(chunk)
    }
    
    # 模拟计算时间
    time.sleep(0.5)
    
    return result

def distributed_computation(data, num_processes=None):
    """分布式计算数据集的统计信息"""
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()
    
    # 将数据分割成多个块
    chunk_size = len(data) // num_processes
    chunks = []
    for i in range(num_processes):
        start = i * chunk_size
        end = len(data) if i == num_processes - 1 else (i + 1) * chunk_size
        chunks.append((data[start:end], i))
    
    # 使用进程池并行计算
    with multiprocessing.Pool(processes=num_processes) as pool:
        results = pool.starmap(compute_chunk, chunks)
    
    # 合并结果
    total_sum = sum(r['sum'] for r in results)
    total_count = sum(r['count'] for r in results)
    overall_mean = total_sum / total_count
    overall_min = min(r['min'] for r in results)
    overall_max = max(r['max'] for r in results)
    
    return {
        'total_sum': total_sum,
        'overall_mean': overall_mean,
        'overall_min': overall_min,
        'overall_max': overall_max,
        'total_count': total_count,
        'chunk_results': results
    }

if __name__ == "__main__":
    # 生成大型随机数据集
    data_size = 1000000
    print(f"生成 {data_size:,} 个随机数据点...")
    data = np.random.rand(data_size)
    
    # 串行计算
    start_time = time.time()
    serial_result = {
        'sum': np.sum(data),
        'mean': np.mean(data),
        'min': np.min(data),
        'max': np.max(data),
        'count': len(data)
    }
    serial_time = time.time() - start_time
    print(f"\n串行计算结果:")
    print(f"总和: {serial_result['sum']:.4f}")
    print(f"平均值: {serial_result['mean']:.4f}")
    print(f"最小值: {serial_result['min']:.4f}")
    print(f"最大值: {serial_result['max']:.4f}")
    print(f"计数: {serial_result['count']:,}")
    print(f"耗时: {serial_time:.4f} 秒")
    
    # 并行计算
    start_time = time.time()
    parallel_result = distributed_computation(data)
    parallel_time = time.time() - start_time
    print(f"\n并行计算结果:")
    print(f"总和: {parallel_result['total_sum']:.4f}")
    print(f"平均值: {parallel_result['overall_mean']:.4f}")
    print(f"最小值: {parallel_result['overall_min']:.4f}")
    print(f"最大值: {parallel_result['overall_max']:.4f}")
    print(f"计数: {parallel_result['total_count']:,}")
    print(f"耗时: {parallel_time:.4f} 秒")
    
    # 计算加速比
    speedup = serial_time / parallel_time
    print(f"\n加速比: {speedup:.2f}x")
    print(f"效率: {speedup / multiprocessing.cpu_count() * 100:.1f}%")
```

## 7. 多进程编程最佳实践

### 7.1 避免常见陷阱

1. **忘记使用`if __name__ == "__main__"`**
   - 在Windows中，这是必须的，否则会导致无限递归创建进程
   - 正确做法：将主程序逻辑放在`if __name__ == "__main__"`块中

2. **共享不可序列化的对象**
   - 进程间传递的对象必须可序列化
   - 正确做法：使用`multiprocessing.Queue`、`Pipe`或`Manager`进行进程间通信

3. **过度使用进程**
   - 创建过多进程会导致系统资源耗尽
   - 正确做法：进程数一般不超过CPU核心数的2倍

4. **忽略异常处理**
   - 子进程中的异常不会自动传播到父进程
   - 正确做法：在子进程中捕获异常并适当处理或传递给父进程

### 7.2 性能优化建议

1. **合理设置进程数**
   - CPU密集型任务：进程数 ≈ CPU核心数
   - IO密集型任务：进程数可以适当大于CPU核心数

2. **数据分块大小**
   - 分块不宜太小：会增加进程间通信开销
   - 分块不宜太大：会导致负载不均衡
   - 正确做法：根据实际情况调整分块大小

3. **减少进程间通信**
   - 进程间通信是昂贵的操作
   - 正确做法：尽量减少数据传输，使用共享内存处理大数据

4. **使用进程池重用进程**
   - 避免频繁创建和销毁进程的开销
   - 正确做法：使用`multiprocessing.Pool`管理进程池

### 7.3 进程安全检查清单

- [ ] 使用`if __name__ == "__main__"`保护主程序
- [ ] 所有共享数据都有适当的同步机制
- [ ] 避免在多进程中使用不可序列化的对象
- [ ] 使用适当的进程间通信方式（Queue、Pipe、共享内存等）
- [ ] 设置合理的进程数，避免资源竞争
- [ ] 正确处理子进程的终止和异常
- [ ] 避免循环引用导致的资源泄漏
- [ ] 使用`with`语句自动管理资源（如`Pool`、`Manager`）

## 8. 多线程与多进程的比较

| 特性 | 多线程（threading） | 多进程（multiprocessing） |
|------|---------------------|---------------------------|
| 内存共享 | 共享进程内存 | 独立内存空间 |
| GIL限制 | 受GIL限制，CPU密集型任务性能受限 | 不受GIL限制，可充分利用多核 |
| 进程间通信 | 简单（共享变量、同步原语） | 复杂（需要特殊的IPC机制） |
| 创建开销 | 小 | 大 |
| 上下文切换 | 快 | 慢 |
| 安全性 | 较低（需注意线程安全） | 较高（天然隔离） |
| 调试难度 | 中等 | 较高 |
| 适用场景 | IO密集型任务 | CPU密集型任务、需要隔离的任务 |

## 9. 总结

`multiprocessing`模块提供了强大的多进程编程能力，能够充分利用多核CPU资源，避免GIL的限制。通过多种进程间通信机制和同步原语，可以有效地协调多个进程的执行。

在选择多进程还是多线程时，需要根据具体的应用场景来决定：
- 对于CPU密集型任务，多进程是更好的选择
- 对于IO密集型任务，多线程通常更高效

通过本文档中的示例和最佳实践，您应该能够有效地使用`multiprocessing`模块来开发并行应用程序，充分利用现代计算机的多核性能。