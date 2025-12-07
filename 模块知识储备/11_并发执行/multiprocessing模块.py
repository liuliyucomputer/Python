#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
multiprocessing模块 - 多进程编程

multiprocessing模块提供了多进程编程的支持，允许程序同时执行多个进程，绕过Python的GIL限制，充分利用多核CPU。

主要功能包括：
- 创建和管理进程
- 进程间通信（队列、管道、共享内存等）
- 进程同步（锁、事件、条件变量等）
- 进程池
- 进程本地存储

使用场景：
- CPU密集型任务（如计算密集型应用）
- 需要充分利用多核CPU的场景
- 避免GIL限制的高性能计算

官方文档：https://docs.python.org/3/library/multiprocessing.html
"""

import multiprocessing
import time
import random
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. multiprocessing模块基本介绍")
print("=" * 50)
print("multiprocessing模块用于多进程编程，允许程序同时执行多个进程")
print("每个进程都有自己独立的Python解释器和内存空间，不受GIL限制")
print("适用于CPU密集型任务，可以充分利用多核CPU")
print("进程间通信需要使用专门的机制，如队列、管道等")

# ===========================
# 2. 进程创建和管理
# ===========================
print("\n" + "=" * 50)
print("2. 进程创建和管理")
print("=" * 50)

# 示例1: 通过函数创建进程
def print_numbers(name, count):
    """打印数字的函数，用于进程执行"""
    print(f"{name} - PID: {os.getpid()} - 父进程PID: {os.getppid()}")
    for i in range(count):
        print(f"{name}: {i}")
        time.sleep(0.1)

print("示例1: 通过函数创建进程")
# 创建进程
process1 = multiprocessing.Process(target=print_numbers, args=("进程1", 5))
process2 = multiprocessing.Process(target=print_numbers, args=("进程2", 5))

# 启动进程
process1.start()
process2.start()

# 等待进程完成
process1.join()
process2.join()

print("两个进程都已完成")

# 示例2: 通过继承Process类创建进程
class MyProcess(multiprocessing.Process):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        self.count = count
    
    def run(self):
        """进程执行的方法"""
        print(f"{self.name} - PID: {os.getpid()} - 父进程PID: {os.getppid()}")
        for i in range(self.count):
            print(f"{self.name}: {i}")
            time.sleep(0.1)

print("\n示例2: 通过继承Process类创建进程")
# 创建进程
process3 = MyProcess("进程3", 5)
process4 = MyProcess("进程4", 5)

# 启动进程
process3.start()
process4.start()

# 等待进程完成
process3.join()
process4.join()

print("两个进程都已完成")

# 示例3: 进程属性和方法
print("\n示例3: 进程属性和方法")

process5 = multiprocessing.Process(target=print_numbers, args=("进程5", 3), name="自定义进程名")
print(f"进程名称: {process5.name}")
print(f"进程PID: {process5.pid}")
print(f"进程是否活跃: {process5.is_alive()}")

# 启动进程
process5.start()
print(f"进程是否活跃: {process5.is_alive()}")
print(f"进程PID: {process5.pid}")

# 等待进程完成
process5.join()
print(f"进程是否活跃: {process5.is_alive()}")
print(f"进程退出码: {process5.exitcode}")

# ===========================
# 3. 进程间通信
# ===========================
print("\n" + "=" * 50)
print("3. 进程间通信")
print("=" * 50)

# 示例4: 使用Queue进行进程间通信
print("示例4: 使用Queue进行进程间通信")

def producer(queue):
    """生产者进程，向队列中放入数据"""
    for i in range(10):
        data = f"数据{i+1}"
        queue.put(data)
        print(f"生产者 - PID {os.getpid()}: 放入 {data}")
        time.sleep(random.uniform(0.1, 0.5))

def consumer(queue):
    """消费者进程，从队列中取出数据"""
    while True:
        try:
            # 从队列获取数据，超时2秒
            data = queue.get(timeout=2)
            print(f"消费者 - PID {os.getpid()}: 取出 {data}")
            time.sleep(random.uniform(0.1, 0.5))
            queue.task_done()
        except multiprocessing.queues.Empty:
            # 队列为空，退出进程
            print(f"消费者 - PID {os.getpid()}: 队列已空，退出")
            break

# 创建队列
queue = multiprocessing.Queue()

# 创建进程
producer_process = multiprocessing.Process(target=producer, args=(queue,))
consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

# 启动进程
producer_process.start()
consumer_process.start()

# 等待生产者完成
producer_process.join()

# 等待队列中的数据被处理完
queue.join()

# 通知消费者退出
consumer_process.terminate()
consumer_process.join()

# 示例5: 使用Pipe进行进程间通信
print("\n示例5: 使用Pipe进行进程间通信")

def sender(conn):
    """发送进程，通过管道发送数据"""
    messages = ["Hello", "World", "Python", "Multiprocessing"]
    for msg in messages:
        conn.send(msg)
        print(f"发送者 - PID {os.getpid()}: 发送 {msg}")
        time.sleep(random.uniform(0.1, 0.5))
    conn.close()

def receiver(conn):
    """接收进程，通过管道接收数据"""
    while True:
        try:
            msg = conn.recv()
            print(f"接收者 - PID {os.getpid()}: 接收 {msg}")
            time.sleep(random.uniform(0.1, 0.5))
        except EOFError:
            print(f"接收者 - PID {os.getpid()}: 管道已关闭，退出")
            break

# 创建管道（返回两个连接对象）
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

# 示例6: 使用共享内存进行进程间通信
print("\n示例6: 使用共享内存进行进程间通信")

def update_shared_value(shared_value):
    """更新共享内存值"""
    print(f"进程 {os.getpid()}: 初始值 {shared_value.value}")
    shared_value.value += 10
    print(f"进程 {os.getpid()}: 更新后的值 {shared_value.value}")
    time.sleep(0.5)

# 创建共享内存
shared_value = multiprocessing.Value('i', 5)  # 'i' 表示整数类型

print(f"父进程: 初始共享值 {shared_value.value}")

# 创建多个进程
processes = []
for i in range(3):
    p = multiprocessing.Process(target=update_shared_value, args=(shared_value,))
    processes.append(p)
    p.start()

# 等待所有进程完成
for p in processes:
    p.join()

print(f"父进程: 最终共享值 {shared_value.value}")

# 示例7: 使用Manager进行进程间通信
print("\n示例7: 使用Manager进行进程间通信")

def update_shared_dict(shared_dict):
    """更新共享字典"""
    shared_dict[os.getpid()] = f"进程 {os.getpid()} 的数据"
    time.sleep(0.5)

def update_shared_list(shared_list):
    """更新共享列表"""
    shared_list.append(os.getpid())
    time.sleep(0.5)

# 创建Manager
manager = multiprocessing.Manager()

# 创建共享数据结构
shared_dict = manager.dict()
shared_list = manager.list()

# 创建进程
processes = []
for i in range(5):
    p1 = multiprocessing.Process(target=update_shared_dict, args=(shared_dict,))
    p2 = multiprocessing.Process(target=update_shared_list, args=(shared_list,))
    processes.append(p1)
    processes.append(p2)
    p1.start()
    p2.start()

# 等待所有进程完成
for p in processes:
    p.join()

print(f"共享字典内容: {shared_dict}")
print(f"共享列表内容: {shared_list}")

# ===========================
# 4. 进程同步
# ===========================
print("\n" + "=" * 50)
print("4. 进程同步")
print("=" * 50)

# 示例8: 使用Lock进行进程同步
print("示例8: 使用Lock进行进程同步")

# 共享变量
shared_counter = multiprocessing.Value('i', 0)
lock = multiprocessing.Lock()

def increment_counter():
    for _ in range(1000):
        with lock:  # 获取锁
            shared_counter.value += 1
        time.sleep(0.001)  # 模拟处理时间

# 创建多个进程
processes = []
for i in range(5):
    p = multiprocessing.Process(target=increment_counter)
    processes.append(p)
    p.start()

# 等待所有进程完成
for p in processes:
    p.join()

print(f"最终计数器值: {shared_counter.value}")
print(f"预期计数器值: {5 * 1000}")

# 示例9: 使用Semaphore进行进程同步
print("\n示例9: 使用Semaphore进行进程同步")

semaphore = multiprocessing.Semaphore(2)  # 允许最多2个进程同时访问

def access_resource(name):
    with semaphore:
        print(f"{name} - PID {os.getpid()}: 正在访问资源")
        time.sleep(random.uniform(0.5, 1.5))  # 模拟资源访问时间
        print(f"{name} - PID {os.getpid()}: 已释放资源")

# 创建多个进程
processes = []
for i in range(5):
    p = multiprocessing.Process(target=access_resource, args=(f"进程{i+1}",))
    processes.append(p)
    p.start()

# 等待所有进程完成
for p in processes:
    p.join()

# 示例10: 使用Event进行进程同步
print("\n示例10: 使用Event进行进程同步")

event = multiprocessing.Event()

def waiter(name):
    print(f"{name} - PID {os.getpid()}: 正在等待事件...")
    event.wait()  # 等待事件被设置
    print(f"{name} - PID {os.getpid()}: 收到事件通知，继续执行")

def setter(name):
    print(f"{name} - PID {os.getpid()}: 正在准备设置事件...")
    time.sleep(2)  # 模拟准备时间
    event.set()  # 设置事件
    print(f"{name} - PID {os.getpid()}: 已设置事件")

# 创建进程
waiter1 = multiprocessing.Process(target=waiter, args=("等待进程1",))
waiter2 = multiprocessing.Process(target=waiter, args=("等待进程2",))
setter1 = multiprocessing.Process(target=setter, args=("设置进程",))

# 启动进程
waiter1.start()
waiter2.start()
time.sleep(0.5)
setter1.start()

# 等待所有进程完成
waiter1.join()
waiter2.join()
setter1.join()

# ===========================
# 5. 进程池
# ===========================
print("\n" + "=" * 50)
print("5. 进程池")
print("=" * 50)

# 示例11: 使用Pool进行进程池操作
print("示例11: 使用Pool进行进程池操作")

def worker_function(x):
    """进程池工作函数"""
    print(f"进程 {os.getpid()}: 处理 {x}")
    time.sleep(random.uniform(0.5, 1.5))  # 模拟处理时间
    return x * x

# 创建进程池（默认使用CPU核心数）
pool = multiprocessing.Pool()

# 示例11.1: 使用map方法
print("\n使用map方法:")
inputs = [1, 2, 3, 4, 5]
results = pool.map(worker_function, inputs)
print(f"map结果: {results}")

# 示例11.2: 使用imap方法（惰性求值）
print("\n使用imap方法:")
for result in pool.imap(worker_function, inputs):
    print(f"imap结果: {result}")

# 示例11.3: 使用apply方法（同步调用）
print("\n使用apply方法:")
result = pool.apply(worker_function, (10,))
print(f"apply结果: {result}")

# 示例11.4: 使用apply_async方法（异步调用）
print("\n使用apply_async方法:")
async_result = pool.apply_async(worker_function, (20,))
# 获取结果（会阻塞直到结果可用）
result = async_result.get()
print(f"apply_async结果: {result}")

# 关闭进程池（不再接受新任务）
pool.close()

# 等待所有任务完成
pool.join()

# ===========================
# 6. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("6. 实际应用示例")
print("=" * 50)

# 示例12: 多进程并行计算
print("示例12: 多进程并行计算")

def calculate_factorial(n):
    """计算阶乘"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return f"{n}! = {result}"

def calculate_fibonacci(n):
    """计算斐波那契数"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return f"F({n}) = {a}"

def calculate_prime(n):
    """检查是否为素数"""
    if n <= 1:
        return f"{n} 不是素数"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} 不是素数，能被 {i} 整除"
    return f"{n} 是素数"

# 创建进程池
pool = multiprocessing.Pool()

# 定义计算任务
tasks = [
    (calculate_factorial, 20),
    (calculate_fibonacci, 30),
    (calculate_prime, 1000000007),
    (calculate_factorial, 15),
    (calculate_fibonacci, 25),
    (calculate_prime, 999999937)
]

# 提交任务并获取结果
results = []
for func, arg in tasks:
    result = pool.apply_async(func, (arg,))
    results.append(result)

# 关闭进程池
pool.close()

# 获取结果
print("计算结果:")
for result in results:
    print(f"  {result.get()}")

# 等待所有任务完成
pool.join()

# 示例13: 多进程批量处理文件
print("\n示例13: 多进程批量处理文件")

def process_file(file_path):
    """模拟处理文件"""
    print(f"进程 {os.getpid()}: 开始处理 {file_path}")
    time.sleep(random.uniform(1, 3))  # 模拟文件处理时间
    return f"{file_path} 处理完成"

# 模拟文件列表
files = [f"file{i}.txt" for i in range(10)]

# 创建进程池
pool = multiprocessing.Pool(processes=4)  # 指定4个进程

# 使用map处理文件
results = pool.map(process_file, files)

# 关闭进程池
pool.close()
pool.join()

# 打印结果
print("文件处理结果:")
for result in results:
    print(f"  {result}")

# 示例14: 多进程Web服务器（简化版）
print("\n示例14: 多进程Web服务器（简化版）")

def handle_request(client_id):
    """处理客户端请求"""
    print(f"进程 {os.getpid()}: 处理客户端 {client_id} 的请求")
    time.sleep(random.uniform(0.5, 1.5))  # 模拟处理时间
    print(f"进程 {os.getpid()}: 完成客户端 {client_id} 的请求")

def start_web_server():
    """启动Web服务器"""
    print("Web服务器已启动，正在监听请求...")
    
    # 创建进程池
    pool = multiprocessing.Pool(processes=3)
    
    # 模拟处理10个客户端请求
    for client_id in range(1, 11):
        pool.apply_async(handle_request, (client_id,))
        time.sleep(0.2)  # 模拟请求间隔
    
    # 关闭进程池
    pool.close()
    pool.join()
    
    print("所有请求处理完成，服务器关闭")

start_web_server()

# ===========================
# 7. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("7. 最佳实践")
print("=" * 50)

print("1. 进程数量选择")
print("   - 对于CPU密集型任务，进程数不应超过CPU核心数")
print("   - 对于I/O密集型任务，进程数可以适当超过CPU核心数")
print("   - 使用multiprocessing.cpu_count()获取CPU核心数")

print("\n2. 进程间通信")
print("   - 优先使用Queue，它比Pipe更安全，支持多个生产者和消费者")
print("   - 对于简单的一对一通信，可以使用Pipe")
print("   - 对于共享简单数据，使用Value或Array")
print("   - 对于复杂数据结构，使用Manager")

print("\n3. 进程同步")
print("   - 避免过多的同步，这会降低并行性能")
print("   - 使用适当的同步机制：Lock、Semaphore、Event、Condition等")
print("   - 尽量减少共享资源的使用")

print("\n4. 进程池使用")
print("   - 对于大量小任务，使用进程池可以减少进程创建和销毁的开销")
print("   - 合理设置进程池大小")
print("   - 记得关闭进程池")

print("\n5. 错误处理")
print("   - 捕获子进程中的异常，避免进程异常退出")
print("   - 使用try-except包裹关键代码")
print("   - 使用日志记录进程执行情况")

print("\n6. 性能考量")
print("   - 进程创建和销毁有开销，避免频繁创建进程")
print("   - 进程间通信有开销，尽量减少通信次数和数据量")
print("   - 对于CPU密集型任务，充分利用多核CPU")

# ===========================
# 8. 与threading模块的比较
# ===========================
print("\n" + "=" * 50)
print("8. 与threading模块的比较")
print("=" * 50)

print("multiprocessing vs threading:")
print("- multiprocessing不受GIL限制，threading受GIL限制")
print("- multiprocessing适用于CPU密集型任务，threading适用于I/O密集型任务")
print("- multiprocessing进程间通信需要专门机制，threading可以直接访问共享内存")
print("- multiprocessing内存消耗更大，threading内存消耗较小")
print("- multiprocessing进程间相互独立，一个进程崩溃不影响其他进程")
print("- threading线程间共享内存，一个线程崩溃可能导致整个进程崩溃")

# ===========================
# 9. 总结
# ===========================
print("\n" + "=" * 50)
print("9. 总结")
print("=" * 50)
print("multiprocessing模块提供了强大的多进程编程支持")
print("允许程序充分利用多核CPU，绕过Python的GIL限制")

print("\n主要功能:")
print("- 创建和管理进程")
print("- 进程间通信（Queue、Pipe、共享内存等）
print("- 进程同步（Lock、Semaphore、Event等）")
print("- 进程池管理")
print("- 进程本地存储")

print("\n应用场景:")
print("- CPU密集型任务")
print("- 高性能计算")
print("- 批量数据处理")
print("- 多客户端服务")

print("\n使用multiprocessing模块可以显著提高程序的并行性能")
print("但需要注意进程间通信和同步的开销")
