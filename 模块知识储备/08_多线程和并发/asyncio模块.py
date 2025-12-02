# asyncio模块 - Python异步编程详解

Python的`asyncio`模块是用于编写并发代码的库，使用异步I/O和协程实现。它提供了一套完整的异步编程框架，适用于高并发I/O密集型任务，如网络服务、爬虫和数据库操作等。本文档将详细介绍`asyncio`模块的核心概念、使用方法、最佳实践以及实际应用案例。

## 1. 核心功能概览

`asyncio`模块的主要功能包括：

- **协程（Coroutines）**：使用`async/await`语法定义的特殊函数
- **事件循环（Event Loop）**：协程的执行环境，负责调度和管理协程
- **任务（Tasks）**：对协程的封装，可以跟踪协程的执行状态
- **Future**：表示异步操作的最终结果
- **异步I/O操作**：支持套接字、子进程、文件等异步I/O
- **同步原语**：提供异步版本的锁、信号量、事件等
- **队列**：异步队列，用于协程间通信
- **流（Streams）**：高级异步I/O抽象

## 2. 基本概念

### 2.1 协程（Coroutines）

协程是`asyncio`的核心概念，是一种特殊的函数，可以在执行过程中暂停，让其他协程执行，之后再恢复执行。

- 使用`async def`定义协程函数
- 使用`await`表达式暂停协程执行，等待其他异步操作完成
- 协程函数调用不会立即执行，而是返回一个协程对象

```python
import asyncio

# 定义协程函数
async def hello_world():
    print("Hello")
    # 暂停执行，等待1秒
    await asyncio.sleep(1)
    print("World")

# 获取协程对象
coro = hello_world()

# 运行协程
asyncio.run(hello_world())  # Python 3.7+
```

### 2.2 事件循环（Event Loop）

事件循环是`asyncio`的核心组件，负责：

- 执行和调度协程
- 处理I/O事件
- 运行异步任务
- 处理回调函数

```python
import asyncio

async def main():
    print("事件循环示例")
    await asyncio.sleep(1)
    print("完成")

# 获取当前事件循环（较旧的方式）
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()

# Python 3.7+ 推荐方式
asyncio.run(main())
```

### 2.3 任务（Tasks）

任务是对协程的封装，用于并发执行协程。当一个协程被封装为任务后，事件循环会自动调度其执行。

```python
import asyncio

async def task_function(name, delay):
    print(f"任务 {name} 开始执行")
    await asyncio.sleep(delay)
    print(f"任务 {name} 完成")
    return f"任务 {name} 的结果"

async def main():
    # 创建任务
    task1 = asyncio.create_task(task_function("A", 1))
    task2 = asyncio.create_task(task_function("B", 2))
    
    print("两个任务已创建")
    
    # 等待任务完成并获取结果
    result1 = await task1
    result2 = await task2
    
    print(f"结果1: {result1}")
    print(f"结果2: {result2}")

asyncio.run(main())
```

### 2.4 Future

`Future`是一个表示异步操作最终结果的对象，与`concurrent.futures.Future`类似。通常，开发者不会直接创建`Future`对象，而是由`asyncio`内部使用。

```python
import asyncio

async def set_future_result(future):
    await asyncio.sleep(1)
    future.set_result("Future已完成")

async def main():
    # 创建Future对象
    future = asyncio.Future()
    
    # 创建一个任务来设置Future的结果
    asyncio.create_task(set_future_result(future))
    
    print("等待Future完成...")
    # 等待Future完成并获取结果
    result = await future
    print(f"获取到结果: {result}")

asyncio.run(main())
```

## 3. 基本用法

### 3.1 运行协程

```python
import asyncio

async def main():
    print("开始")
    await asyncio.sleep(1)
    print("结束")

# Python 3.7+ 推荐的运行方式
asyncio.run(main())

# 或者使用事件循环（旧方式）
# loop = asyncio.new_event_loop()
# asyncio.set_event_loop(loop)
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()
```

### 3.2 并发运行协程

`asyncio.gather()`函数可以并发运行多个协程，并等待它们全部完成。

```python
import asyncio
import time

async def fetch_data(delay, data_id):
    print(f"开始获取数据 {data_id}")
    await asyncio.sleep(delay)
    print(f"完成获取数据 {data_id}")
    return f"数据 {data_id} 的结果"

async def main():
    start_time = time.time()
    
    # 并发运行多个协程
    results = await asyncio.gather(
        fetch_data(2, "A"),
        fetch_data(1, "B"),
        fetch_data(3, "C")
    )
    
    end_time = time.time()
    print(f"所有数据获取完成，总耗时: {end_time - start_time:.2f}秒")
    print(f"结果: {results}")

asyncio.run(main())
```

### 3.3 创建和管理任务

```python
import asyncio

async def task_function(task_id):
    print(f"任务 {task_id} 开始")
    await asyncio.sleep(1)
    print(f"任务 {task_id} 完成")
    return f"任务 {task_id} 的结果"

async def main():
    # 创建任务
    task1 = asyncio.create_task(task_function(1))
    task2 = asyncio.create_task(task_function(2))
    
    # 检查任务状态
    print(f"任务1已创建: {task1}")
    print(f"任务2已创建: {task2}")
    print(f"任务1是否已完成: {task1.done()}")
    
    # 等待任务完成
    await task1
    print(f"任务1是否已完成: {task1.done()}")
    print(f"任务1的结果: {task1.result()}")
    
    # 等待任务2完成
    result2 = await task2
    print(f"任务2的结果: {result2}")

asyncio.run(main())
```

### 3.4 超时处理

使用`asyncio.wait_for()`可以为异步操作设置超时。

```python
import asyncio

async def slow_operation():
    print("开始耗时操作")
    await asyncio.sleep(3)
    print("耗时操作完成")
    return "操作成功"

async def main():
    try:
        # 设置2秒超时
        result = await asyncio.wait_for(slow_operation(), timeout=2)
        print(f"结果: {result}")
    except asyncio.TimeoutError:
        print("操作超时")

asyncio.run(main())
```

### 3.5 等待多个任务

使用`asyncio.wait()`可以等待多个任务完成，提供更灵活的控制。

```python
import asyncio

async def task_function(task_id, delay):
    print(f"任务 {task_id} 开始，延迟 {delay}秒")
    await asyncio.sleep(delay)
    print(f"任务 {task_id} 完成")
    return f"任务 {task_id} 的结果"

async def main():
    # 创建任务
    tasks = [
        asyncio.create_task(task_function(1, 3)),
        asyncio.create_task(task_function(2, 1)),
        asyncio.create_task(task_function(3, 2))
    ]
    
    # 等待第一个任务完成
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )
    
    print(f"已完成的任务数: {len(done)}")
    print(f"未完成的任务数: {len(pending)}")
    
    # 处理已完成的任务
    for task in done:
        print(f"完成的任务结果: {await task}")
    
    # 继续等待剩余任务完成
    await asyncio.wait(pending)
    print("所有任务已完成")

asyncio.run(main())
```

## 4. 异步I/O操作

### 4.1 异步文件操作

注意：Python的标准库对文件I/O的异步支持有限，通常需要使用第三方库如`aiofiles`。

```python
import asyncio
import aiofiles  # 需要安装: pip install aiofiles

async def read_file(filename):
    async with aiofiles.open(filename, 'r', encoding='utf-8') as f:
        content = await f.read()
        print(f"读取文件 {filename} 完成，内容长度: {len(content)} 字符")
        return content

async def write_file(filename, content):
    async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
        await f.write(content)
        print(f"写入文件 {filename} 完成")

async def main():
    # 写入测试文件
    test_content = "这是一个异步文件操作测试。\n包含多行文本。"
    await write_file("test.txt", test_content)
    
    # 读取文件
    content = await read_file("test.txt")
    print(f"读取的内容:\n{content}")

    # 并发读取多个文件
    filenames = ["test1.txt", "test2.txt", "test3.txt"]
    
    # 先创建这些文件
    for i, filename in enumerate(filenames):
        await write_file(filename, f"这是文件 {i+1} 的内容。")
    
    # 并发读取
    contents = await asyncio.gather(*[read_file(f) for f in filenames])
    print(f"\n并发读取的结果数量: {len(contents)}")

asyncio.run(main())
```

### 4.2 异步网络请求

使用`aiohttp`库进行异步HTTP请求：

```python
import asyncio
import aiohttp  # 需要安装: pip install aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        status = response.status
        content = await response.text()
        print(f"URL: {url}, 状态码: {status}, 内容长度: {len(content)} 字符")
        return {
            'url': url,
            'status': status,
            'content_length': len(content)
        }

async def main():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/status/200"
    ]
    
    # 创建一个ClientSession
    async with aiohttp.ClientSession() as session:
        # 并发获取所有URL
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
        # 打印结果
        print("\n所有请求完成，结果汇总:")
        for result in results:
            print(f"URL: {result['url']}, 状态码: {result['status']}, 内容长度: {result['content_length']}")

asyncio.run(main())
```

### 4.3 异步TCP服务器

```python
import asyncio

async def handle_client(reader, writer):
    # 获取客户端地址
    addr = writer.get_extra_info('peername')
    print(f"客户端连接: {addr}")
    
    while True:
        try:
            # 读取客户端发送的数据
            data = await reader.readline()
            if not data:  # 连接关闭
                break
            
            message = data.decode().strip()
            print(f"收到来自 {addr} 的消息: {message}")
            
            # 回复客户端
            response = f"已收到: {message}\n"
            writer.write(response.encode())
            await writer.drain()
            
            # 检查是否退出
            if message.lower() == 'exit':
                break
                
        except Exception as e:
            print(f"处理客户端 {addr} 时出错: {e}")
            break
    
    # 关闭连接
    print(f"客户端 {addr} 断开连接")
    writer.close()
    await writer.wait_closed()

async def main():
    # 创建服务器
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888
    )
    
    # 获取服务器地址
    addr = server.sockets[0].getsockname()
    print(f"服务器运行在 {addr}")
    print("按 Ctrl+C 停止服务器")
    
    # 运行服务器
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("服务器已停止")
```

### 4.4 异步TCP客户端

```python
import asyncio

async def tcp_client():
    try:
        # 连接服务器
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        print("已连接到服务器")
        print("输入消息发送到服务器，输入'exit'退出")
        
        while True:
            # 获取用户输入
            message = input("请输入消息: ")
            
            # 发送消息给服务器
            writer.write(f"{message}\n".encode())
            await writer.drain()
            
            # 读取服务器回复
            data = await reader.readline()
            response = data.decode().strip()
            print(f"服务器回复: {response}")
            
            # 检查是否退出
            if message.lower() == 'exit':
                break
                
    except ConnectionRefusedError:
        print("无法连接到服务器，请确保服务器正在运行")
    except Exception as e:
        print(f"客户端出错: {e}")
    finally:
        # 关闭连接
        if 'writer' in locals():
            print("关闭连接")
            writer.close()
            await writer.wait_closed()

asyncio.run(tcp_client())
```

## 5. 异步同步原语

`asyncio`提供了异步版本的同步原语，用于协调多个协程的执行。

### 5.1 异步锁（Lock）

```python
import asyncio

# 共享资源
counter = 0
# 创建异步锁
lock = asyncio.Lock()

async def increment_counter(name, iterations):
    global counter
    print(f"任务 {name} 开始执行")
    
    for i in range(iterations):
        # 获取锁
        async with lock:
            # 临界区
            current = counter
            await asyncio.sleep(0.01)  # 模拟一些处理
            counter = current + 1
            print(f"任务 {name}：将计数器从 {current} 增加到 {counter}")
    
    print(f"任务 {name} 执行完成")

async def main():
    # 创建多个任务
    tasks = [
        asyncio.create_task(increment_counter("A", 100)),
        asyncio.create_task(increment_counter("B", 100)),
        asyncio.create_task(increment_counter("C", 100))
    ]
    
    # 等待所有任务完成
    await asyncio.gather(*tasks)
    
    print(f"所有任务完成，最终计数器值: {counter}")  # 应为300

asyncio.run(main())
```

### 5.2 异步事件（Event）

```python
import asyncio

# 创建事件
ready_event = asyncio.Event()

async def waiter(name):
    print(f"等待者 {name}：等待事件触发")
    # 等待事件被设置
    await ready_event.wait()
    print(f"等待者 {name}：事件已触发，继续执行")
    # 可以进行下一步操作
    await asyncio.sleep(1)
    print(f"等待者 {name}：执行完成")

async def setter():
    print("设置者：准备触发事件")
    # 模拟一些准备工作
    await asyncio.sleep(3)
    print("设置者：触发事件")
    # 设置事件
    ready_event.set()
    
    # 可以重置事件
    await asyncio.sleep(2)
    print("设置者：重置事件")
    ready_event.clear()
    
    # 再次触发事件
    await asyncio.sleep(1)
    print("设置者：再次触发事件")
    ready_event.set()

async def main():
    # 创建等待者和设置者任务
    waiter_tasks = [asyncio.create_task(waiter(i)) for i in range(3)]
    setter_task = asyncio.create_task(setter())
    
    # 等待所有任务完成
    await asyncio.gather(*waiter_tasks, setter_task)
    
    print("所有任务完成")

asyncio.run(main())
```

### 5.3 异步条件变量（Condition）

```python
import asyncio

class AsyncQueue:
    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size
        self.condition = asyncio.Condition()
    
    async def put(self, item):
        async with self.condition:
            # 等待队列有空间
            while len(self.items) >= self.max_size:
                print(f"队列已满，等待空间: {self.items}")
                await self.condition.wait()
            
            # 添加项目
            self.items.append(item)
            print(f"放入项目: {item}, 队列: {self.items}")
            
            # 通知等待的消费者
            self.condition.notify_all()
    
    async def get(self):
        async with self.condition:
            # 等待队列有项目
            while not self.items:
                print("队列为空，等待项目")
                await self.condition.wait()
            
            # 移除并返回项目
            item = self.items.pop(0)
            print(f"获取项目: {item}, 队列: {self.items}")
            
            # 通知等待的生产者
            self.condition.notify_all()
            return item

async def producer(queue, items):
    for item in items:
        await queue.put(item)
        await asyncio.sleep(0.5)  # 模拟生产间隔
    
    # 放入结束标记
    await queue.put(None)
    print("生产者完成")

async def consumer(queue, name):
    while True:
        item = await queue.get()
        # 检查结束标记
        if item is None:
            # 放回结束标记供其他消费者使用
            await queue.put(None)
            print(f"消费者 {name} 收到结束信号")
            break
        
        print(f"消费者 {name} 处理项目: {item}")
        await asyncio.sleep(1)  # 模拟消费时间

async def main():
    # 创建异步队列
    queue = AsyncQueue(max_size=3)
    
    # 创建生产者和消费者任务
    producer_task = asyncio.create_task(producer(queue, range(1, 10)))
    consumer_tasks = [
        asyncio.create_task(consumer(queue, "A")),
        asyncio.create_task(consumer(queue, "B"))
    ]
    
    # 等待所有任务完成
    await asyncio.gather(producer_task, *consumer_tasks)
    
    print("所有任务完成")

asyncio.run(main())
```

### 5.4 异步信号量（Semaphore）

```python
import asyncio

# 创建信号量，最多允许2个协程同时访问
semaphore = asyncio.Semaphore(2)

async def access_resource(name, delay):
    print(f"任务 {name} 尝试访问资源")
    # 获取信号量
    async with semaphore:
        print(f"任务 {name} 获得资源访问权限")
        # 模拟资源使用
        await asyncio.sleep(delay)
        print(f"任务 {name} 释放资源访问权限")
    
    print(f"任务 {name} 完成")

async def main():
    # 创建多个任务
    tasks = [
        asyncio.create_task(access_resource("A", 3)),
        asyncio.create_task(access_resource("B", 2)),
        asyncio.create_task(access_resource("C", 4)),
        asyncio.create_task(access_resource("D", 1)),
        asyncio.create_task(access_resource("E", 2))
    ]
    
    # 等待所有任务完成
    await asyncio.gather(*tasks)
    
    print("所有任务完成")

asyncio.run(main())
```

### 5.5 异步栅栏（Barrier）

```python
import asyncio
import random

# 创建栅栏，需要4个协程到达才能通过
barrier = asyncio.Barrier(4)

async def worker(name):
    print(f"工作者 {name} 开始工作")
    # 模拟工作时间
    work_time = random.uniform(1, 3)
    await asyncio.sleep(work_time)
    print(f"工作者 {name} 到达栅栏点 (耗时 {work_time:.2f}s)")
    
    # 等待所有工作者到达
    await barrier.wait()
    print(f"工作者 {name} 通过栅栏，继续工作")
    
    # 再次工作
    await asyncio.sleep(random.uniform(0.5, 1.5))
    print(f"工作者 {name} 完成所有工作")

async def main():
    # 创建工作者任务
    tasks = [asyncio.create_task(worker(i)) for i in range(4)]
    
    # 等待所有任务完成
    await asyncio.gather(*tasks)
    
    print("所有工作者完成工作")

asyncio.run(main())
```

## 6. 异步队列

`asyncio`提供了异步队列，用于在协程之间安全地传递数据。

```python
import asyncio
import random

async def producer(queue, producer_id, items_count):
    for i in range(items_count):
        # 生成数据
        item = f"生产者{producer_id}-项目{i}"
        
        # 放入队列
        await queue.put(item)
        print(f"生产者 {producer_id} 放入: {item}, 队列大小: {queue.qsize()}")
        
        # 随机休眠，模拟生产间隔
        await asyncio.sleep(random.uniform(0.1, 0.5))
    
    print(f"生产者 {producer_id} 完成")

async def consumer(queue, consumer_id):
    while True:
        try:
            # 从队列获取数据，设置超时
            item = await asyncio.wait_for(queue.get(), timeout=2)
            print(f"消费者 {consumer_id} 取出: {item}, 队列大小: {queue.qsize()}")
            
            # 模拟处理时间
            await asyncio.sleep(random.uniform(0.2, 0.7))
            
            # 标记任务完成
            queue.task_done()
            
        except asyncio.TimeoutError:
            # 超时，检查队列是否已加入完成标记
            if queue.empty():
                print(f"消费者 {consumer_id} 超时且队列为空，退出")
                break

async def main():
    # 创建容量为5的队列
    queue = asyncio.Queue(maxsize=5)
    
    # 创建生产者任务
    producers = [
        asyncio.create_task(producer(queue, 1, 10)),
        asyncio.create_task(producer(queue, 2, 10))
    ]
    
    # 创建消费者任务
    consumers = [
        asyncio.create_task(consumer(queue, 1)),
        asyncio.create_task(consumer(queue, 2)),
        asyncio.create_task(consumer(queue, 3))
    ]
    
    # 等待所有生产者完成
    await asyncio.gather(*producers)
    print("所有生产者完成")
    
    # 等待队列中的所有项目被处理
    await queue.join()
    print("队列已清空")
    
    # 取消所有消费者任务
    for consumer_task in consumers:
        consumer_task.cancel()
    
    # 等待消费者任务被取消
    await asyncio.gather(*consumers, return_exceptions=True)
    print("所有消费者已退出")

asyncio.run(main())
```

## 7. 高级应用模式

### 7.1 异步迭代器和异步上下文管理器

#### 7.1.1 异步迭代器

```python
import asyncio

class AsyncCounter:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    # 使类成为异步迭代器
    def __aiter__(self):
        return self
    
    # 定义异步next方法
    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        
        # 保存当前值
        value = self.current
        # 增加计数器
        self.current += 1
        # 模拟异步操作
        await asyncio.sleep(0.5)
        return value

async def main():
    print("开始异步迭代")
    # 使用异步for循环
    async for i in AsyncCounter(1, 6):
        print(f"异步迭代获取值: {i}")
    print("异步迭代完成")

asyncio.run(main())
```

#### 7.1.2 异步上下文管理器

```python
import asyncio

class AsyncResource:
    def __init__(self, name):
        self.name = name
    
    # 定义异步进入上下文方法
    async def __aenter__(self):
        print(f"获取资源: {self.name}")
        # 模拟资源初始化
        await asyncio.sleep(0.5)
        print(f"资源 {self.name} 已准备好")
        return self
    
    # 定义异步退出上下文方法
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"释放资源: {self.name}")
        # 模拟资源清理
        await asyncio.sleep(0.5)
        print(f"资源 {self.name} 已释放")
    
    async def use(self):
        print(f"使用资源: {self.name}")
        await asyncio.sleep(1)

async def main():
    # 使用异步上下文管理器
    async with AsyncResource("数据库连接") as resource:
        await resource.use()
    print("上下文管理完成")

asyncio.run(main())
```

### 7.2 异步生成器

```python
import asyncio

async def async_generator(start, end, delay=0.5):
    """异步生成器函数"""
    current = start
    while current < end:
        # 生成当前值
        yield current
        # 增加计数器
        current += 1
        # 模拟异步操作
        await asyncio.sleep(delay)

async def main():
    print("开始异步生成器")
    # 使用异步for循环遍历异步生成器
    async for value in async_generator(1, 6):
        print(f"异步生成器产生值: {value}")
    print("异步生成器完成")
    
    # 也可以将异步生成器的结果收集到列表中
    results = [value async for value in async_generator(10, 15, 0.1)]
    print(f"收集的结果: {results}")

asyncio.run(main())
```

### 7.3 任务取消

```python
import asyncio

async def long_running_task():
    print("长时间运行的任务开始")
    try:
        # 模拟长时间运行的任务
        for i in range(10):
            print(f"任务执行中... {i+1}/10")
            await asyncio.sleep(1)
        return "任务成功完成"
    except asyncio.CancelledError:
        print("任务被取消")
        # 可以在这里进行清理工作
        await asyncio.sleep(0.5)  # 模拟清理时间
        print("任务清理完成")
        raise  # 重新抛出异常，让调用者知道任务已被取消

async def main():
    # 创建任务
    task = asyncio.create_task(long_running_task())
    
    # 等待3秒后取消任务
    await asyncio.sleep(3)
    print("准备取消任务")
    task.cancel()
    
    try:
        # 等待任务完成（或被取消）
        result = await task
        print(f"任务结果: {result}")
    except asyncio.CancelledError:
        print("捕获到任务取消异常")
    
    print("主程序继续执行")

asyncio.run(main())
```

### 7.4 错误传播和处理

```python
import asyncio

async def task_with_error(error_type):
    print(f"开始执行可能出错的任务: {error_type}")
    await asyncio.sleep(0.5)
    
    if error_type == "ValueError":
        raise ValueError("任务产生的值错误")
    elif error_type == "TypeError":
        raise TypeError("任务产生的类型错误")
    elif error_type == "RuntimeError":
        raise RuntimeError("任务产生的运行时错误")
    
    return "任务成功完成"

async def main():
    # 创建多个可能出错的任务
    tasks = [
        asyncio.create_task(task_with_error("ValueError")),
        asyncio.create_task(task_with_error("TypeError")),
        asyncio.create_task(task_with_error("Success"))
    ]
    
    # 方式1: 逐个等待并处理异常
    print("\n方式1: 逐个等待任务")
    for i, task in enumerate(tasks):
        try:
            result = await task
            print(f"任务 {i+1} 成功: {result}")
        except Exception as e:
            print(f"任务 {i+1} 失败: {type(e).__name__} - {e}")
    
    # 方式2: 使用gather并处理异常
    print("\n方式2: 使用gather和return_exceptions")
    new_tasks = [
        asyncio.create_task(task_with_error("RuntimeError")),
        asyncio.create_task(task_with_error("Success"))
    ]
    
    # 使用return_exceptions=True让gather捕获异常并返回它们，而不是传播
    results = await asyncio.gather(*new_tasks, return_exceptions=True)
    
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"任务 {i+1} 失败: {type(result).__name__} - {result}")
        else:
            print(f"任务 {i+1} 成功: {result}")

asyncio.run(main())
```

## 8. 实际应用示例

### 8.1 异步Web爬虫

```python
import asyncio
import aiohttp
from bs4 import BeautifulSoup  # 需要安装: pip install beautifulsoup4
import time
import os

async def fetch_page(session, url):
    """获取网页内容"""
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"获取 {url} 失败，状态码: {response.status}")
                return None
    except Exception as e:
        print(f"获取 {url} 异常: {e}")
        return None

async def parse_page(html, url):
    """解析网页内容，提取链接"""
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        # 处理相对URL
        if href.startswith('/'):
            # 简单处理相对URL，实际项目中可能需要更复杂的URL处理
            from urllib.parse import urljoin
            href = urljoin(url, href)
        
        # 只保留同一域名的链接（简单示例）
        if href.startswith(url.split('/')[0] + '//' + url.split('/')[2]):
            links.append(href)
    
    return links

async def save_page(url, html, output_dir):
    """保存网页内容到文件"""
    if not html:
        return
    
    # 创建安全的文件名
    filename = url.replace('://', '_').replace('/', '_').replace(':', '_')[:200] + '.html'
    filepath = os.path.join(output_dir, filename)
    
    try:
        # 使用aiofiles异步写入文件
        import aiofiles
        async with aiofiles.open(filepath, 'w', encoding='utf-8') as f:
            await f.write(html)
        print(f"已保存: {url} -> {filename}")
    except Exception as e:
        print(f"保存 {url} 失败: {e}")

async def crawl(url, max_depth=2, max_pages=10, output_dir="./crawled_pages"):
    """异步爬取网站"""
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 已爬取和待爬取的URL集合
    crawled_urls = set()
    urls_to_crawl = [(url, 0)]  # (url, depth)
    
    # 创建aiohttp会话
    async with aiohttp.ClientSession() as session:
        while urls_to_crawl and len(crawled_urls) < max_pages:
            # 获取下一个要爬取的URL和深度
            current_url, depth = urls_to_crawl.pop(0)
            
            # 如果已爬取或超过深度限制，跳过
            if current_url in crawled_urls or depth >= max_depth:
                continue
            
            print(f"\n爬取: {current_url} (深度: {depth})")
            
            # 获取网页内容
            html = await fetch_page(session, current_url)
            if html:
                # 保存网页
                await save_page(current_url, html, output_dir)
                # 解析网页获取链接
                links = await parse_page(html, current_url)
                
                # 添加新的URL到待爬取列表
                for link in links:
                    if link not in crawled_urls and not any(l[0] == link for l in urls_to_crawl):
                        urls_to_crawl.append((link, depth + 1))
            
            # 标记为已爬取
            crawled_urls.add(current_url)
            print(f"已爬取: {len(crawled_urls)}/{max_pages}, 待爬取: {len(urls_to_crawl)}")
            
            # 避免请求过快
            await asyncio.sleep(0.5)
    
    print(f"\n爬虫完成。总共爬取了 {len(crawled_urls)} 个页面。")

async def main():
    # 选择一个安全的测试网站
    test_url = "https://httpbin.org/"
    
    start_time = time.time()
    await crawl(
        url=test_url,
        max_depth=1,
        max_pages=5,
        output_dir="./crawled_pages"
    )
    end_time = time.time()
    
    print(f"爬取耗时: {end_time - start_time:.2f} 秒")

if __name__ == "__main__":
    asyncio.run(main())
```

### 8.2 异步数据库操作

使用`aiosqlite`进行异步SQLite操作：

```python
import asyncio
import aiosqlite  # 需要安装: pip install aiosqlite
import random
import time

async def init_database(db_path):
    """初始化数据库"""
    async with aiosqlite.connect(db_path) as db:
        # 创建表
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                email TEXT
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL,
                category TEXT
            )
        ''')
        await db.commit()
        print("数据库初始化完成")

async def insert_users(db_path, count):
    """异步插入用户数据"""
    async with aiosqlite.connect(db_path) as db:
        users = []
        for i in range(count):
            name = f"用户{i+1}"
            age = random.randint(18, 65)
            email = f"user{i+1}@example.com"
            users.append((name, age, email))
        
        # 批量插入
        await db.executemany(
            "INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
            users
        )
        await db.commit()
        print(f"已插入 {count} 条用户数据")

async def insert_products(db_path, count):
    """异步插入产品数据"""
    async with aiosqlite.connect(db_path) as db:
        categories = ["电子产品", "服装", "食品", "书籍", "家居用品"]
        products = []
        
        for i in range(count):
            name = f"产品{i+1}"
            price = round(random.uniform(10.0, 1000.0), 2)
            category = random.choice(categories)
            products.append((name, price, category))
        
        # 批量插入
        await db.executemany(
            "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
            products
        )
        await db.commit()
        print(f"已插入 {count} 条产品数据")

async def query_users_by_age(db_path, min_age, max_age):
    """异步查询特定年龄范围的用户"""
    async with aiosqlite.connect(db_path) as db:
        async with db.execute(
            "SELECT id, name, age, email FROM users WHERE age BETWEEN ? AND ?",
            (min_age, max_age)
        ) as cursor:
            users = await cursor.fetchall()
            print(f"查询到 {len(users)} 位年龄在 {min_age}-{max_age} 之间的用户")
            # 打印前5条记录
            for i, user in enumerate(users[:5]):
                print(f"用户{i+1}: ID={user[0]}, 姓名={user[1]}, 年龄={user[2]}, 邮箱={user[3]}")
            return users

async def update_user_ages(db_path, min_id, max_id, increment):
    """异步更新用户年龄"""
    async with aiosqlite.connect(db_path) as db:
        # 更新年龄
        result = await db.execute(
            "UPDATE users SET age = age + ? WHERE id BETWEEN ? AND ?",
            (increment, min_id, max_id)
        )
        await db.commit()
        affected_rows = result.rowcount
        print(f"已更新 {affected_rows} 位用户的年龄，每人增加 {increment} 岁")
        return affected_rows

async def main():
    db_path = "example.db"
    
    # 初始化数据库
    await init_database(db_path)
    
    # 并发插入数据
    print("\n并发插入数据...")
    start_time = time.time()
    await asyncio.gather(
        insert_users(db_path, 1000),
        insert_products(db_path, 2000)
    )
    insert_time = time.time() - start_time
    print(f"数据插入耗时: {insert_time:.2f} 秒")
    
    # 查询数据
    print("\n查询数据...")
    await query_users_by_age(db_path, 30, 50)
    
    # 更新数据
    print("\n更新数据...")
    await update_user_ages(db_path, 1, 500, 1)
    
    # 再次查询，验证更新
    print("\n更新后的查询...")
    await query_users_by_age(db_path, 30, 50)
    
    print("\n数据库操作完成")

if __name__ == "__main__":
    asyncio.run(main())
```

### 8.3 异步WebSocket服务器

```python
import asyncio
import websockets

# 存储所有连接的客户端
connected_clients = set()

async def handle_client(websocket, path):
    # 添加客户端到集合
    connected_clients.add(websocket)
    client_address = websocket.remote_address
    print(f"客户端连接: {client_address}")
    print(f"当前连接数: {len(connected_clients)}")
    
    try:
        # 向新客户端发送欢迎消息
        await websocket.send(f"欢迎连接到WebSocket服务器！当前在线: {len(connected_clients)} 人")
        
        # 广播有新客户端连接
        await broadcast_message(f"系统: 用户 {client_address} 加入了聊天室")
        
        # 处理客户端消息
        async for message in websocket:
            print(f"收到来自 {client_address} 的消息: {message}")
            # 广播消息给所有客户端
            await broadcast_message(f"用户 {client_address}: {message}")
            
    except websockets.exceptions.ConnectionClosedError:
        print(f"客户端 {client_address} 意外断开连接")
    except Exception as e:
        print(f"处理客户端 {client_address} 时出错: {e}")
    finally:
        # 从集合中移除客户端
        connected_clients.remove(websocket)
        print(f"客户端 {client_address} 断开连接")
        print(f"当前连接数: {len(connected_clients)}")
        
        # 广播客户端离开
        await broadcast_message(f"系统: 用户 {client_address} 离开了聊天室")

async def broadcast_message(message):
    """广播消息给所有连接的客户端"""
    if connected_clients:
        # 创建发送任务列表
        send_tasks = [client.send(message) for client in connected_clients]
        # 并发发送消息，忽略可能的错误
        await asyncio.gather(*send_tasks, return_exceptions=True)

async def main():
    # 创建WebSocket服务器
    async with websockets.serve(handle_client, "localhost", 8765):
        print("WebSocket服务器启动在 ws://localhost:8765")
        print("按 Ctrl+C 停止服务器")
        # 保持服务器运行
        await asyncio.Future()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("服务器已停止")
```

## 9. 性能优化与最佳实践

### 9.1 避免阻塞操作

在异步代码中，任何阻塞操作都会阻塞整个事件循环，导致其他协程无法执行。

**错误示例**：
```python
async def blocking_operation():
    # 同步文件IO会阻塞事件循环
    with open("large_file.txt", "r") as f:
        content = f.read()  # 阻塞操作
    return content
```

**正确做法**：
```python
async def non_blocking_operation():
    # 使用异步文件IO
    import aiofiles
    async with aiofiles.open("large_file.txt", "r") as f:
        content = await f.read()  # 非阻塞操作
    return content

# 或者对于无法异步化的阻塞操作，使用线程池
async def run_blocking_in_executor():
    loop = asyncio.get_running_loop()
    with open("large_file.txt", "r") as f:
        content = await loop.run_in_executor(
            None,  # 使用默认线程池
            f.read  # 传递函数对象
        )
    return content
```

### 9.2 使用异步版本的库

尽量使用异步版本的库，而不是同步库。常见的异步库包括：

- `aiohttp`：异步HTTP客户端/服务器
- `aiosqlite`：异步SQLite数据库
- `aioredis`：异步Redis客户端
- `aiomysql`/`asyncpg`：异步MySQL/PostgreSQL客户端
- `aiofiles`：异步文件操作
- `websockets`：异步WebSocket

### 9.3 合理设计任务粒度

- **任务粒度过大**：会导致事件循环被长时间占用，其他任务等待时间过长
- **任务粒度过小**：会增加调度开销
- **最佳实践**：将大型任务拆分为多个小任务，使用`asyncio.sleep(0)`让出控制权

```python
async def large_task():
    # 拆分为多个小步骤
    for i in range(10):
        # 执行一部分工作
        print(f"执行步骤 {i+1}")
        # 让出控制权，让其他协程有机会执行
        await asyncio.sleep(0)
```

### 9.4 避免过度使用锁

虽然`asyncio`提供了异步锁，但过度使用会影响并发性能。

**优化建议**：
- 尽量减少共享状态
- 使用不可变对象
- 只在必要时使用锁保护临界区
- 考虑使用队列进行协程间通信，而不是共享状态

### 9.5 正确处理异常

在异步代码中，异常处理尤为重要，因为未处理的异常可能会导致任务静默失败。

**最佳实践**：
- 为所有异步操作添加适当的异常处理
- 使用`asyncio.gather(return_exceptions=True)`收集异常而不是传播
- 为长时间运行的任务添加超时
- 在取消任务时进行适当的清理

### 9.6 使用异步上下文管理器

异步上下文管理器可以确保资源的正确获取和释放，即使在发生异常的情况下。

```python
async def use_resource():
    # 正确使用异步上下文管理器
    async with AsyncResource() as resource:
        await resource.operation()
    # 资源会被自动释放，即使operation()抛出异常
```

## 10. asyncio与其他并发方式的比较

| 并发方式 | 优势 | 劣势 | 适用场景 |
|---------|------|------|----------|
| **asyncio** | 单线程异步，高并发，低开销，IO密集型性能好 | 编程模型复杂，学习曲线陡峭，需要异步支持 | 高并发IO操作，如网络服务、爬虫、数据库操作 |
| **threading** | 多线程，编程模型相对简单，不需要修改现有代码 | GIL限制，线程切换开销，上下文切换成本高 | IO密集型任务，需要使用同步库 |
| **multiprocessing** | 多进程，绕过GIL，充分利用多核CPU | 进程间通信复杂，开销大，内存占用高 | CPU密集型任务，需要完全隔离的执行环境 |
| **concurrent.futures** | 高级API，使用简单，统一接口 | 灵活性较低，高级控制有限 | 快速实现简单并行任务 |

## 11. 总结

`asyncio`模块为Python提供了强大的异步编程能力，特别适合处理高并发的I/O密集型任务。通过协程、事件循环和异步I/O操作，可以在单线程中实现并发处理，避免了多线程的上下文切换开销和GIL限制。

要有效地使用`asyncio`，需要掌握以下核心概念：

1. **协程**：使用`async/await`语法定义和使用
2. **事件循环**：协程的执行环境，负责调度和管理
3. **任务**：对协程的封装，用于并发执行
4. **异步I/O**：非阻塞的输入/输出操作
5. **同步原语**：用于协程间同步和通信

在实际应用中，需要注意避免阻塞操作，使用异步版本的库，并正确处理异常。通过合理设计异步程序，可以充分发挥`asyncio`的优势，构建高性能的并发应用。