#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
asyncio模块 - 异步编程

asyncio模块提供了基于事件循环的异步编程框架，允许开发者编写高效的并发代码，特别适合I/O密集型任务。

主要功能包括：
- 协程（coroutines）支持
- 事件循环（event loop）
- 异步I/O操作
- 任务（Tasks）和未来（Futures）
- 同步原语（锁、事件、条件变量等）
- 并发控制

使用场景：
- 高并发I/O密集型任务（如网络服务器、爬虫、API调用等）
- 需要高效处理大量并发连接的场景
- 提高程序响应性

官方文档：https://docs.python.org/3/library/asyncio.html
"""

import asyncio
import time
import random

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. asyncio模块基本介绍")
print("=" * 50)
print("asyncio模块提供基于事件循环的异步编程框架")
print("使用协程（coroutines）实现并发，比线程更轻量级")
print("基于单线程的事件循环，避免了线程切换的开销")
print("适用于高并发I/O密集型任务，效率比多线程更高")
print("Python 3.5+引入，是现代Python异步编程的标准")

# ===========================
# 2. 协程基础
# ===========================
print("\n" + "=" * 50)
print("2. 协程基础")
print("=" * 50)

# 示例1: 基本协程
print("示例1: 基本协程")

# 使用async关键字定义协程
async def hello_world():
    print("Hello")
    await asyncio.sleep(1)  # 模拟异步操作
    print("World")

# 运行协程
asyncio.run(hello_world())

# 示例2: 协程返回值
print("\n示例2: 协程返回值")

async def calculate():
    print("开始计算")
    await asyncio.sleep(1)
    return 42

result = asyncio.run(calculate())
print(f"计算结果: {result}")

# 示例3: 协程链
print("\n示例3: 协程链")

async def fetch_data():
    print("获取数据")
    await asyncio.sleep(1)
    return {"data": [1, 2, 3]}

async def process_data(data):
    print("处理数据")
    await asyncio.sleep(0.5)
    return [item * 2 for item in data["data"]]

async def main():
    raw_data = await fetch_data()
    processed_data = await process_data(raw_data)
    print(f"处理后的数据: {processed_data}")

asyncio.run(main())

# ===========================
# 3. 并发执行协程
# ===========================
print("\n" + "=" * 50)
print("3. 并发执行协程")
print("=" * 50)

# 示例4: 使用gather并发执行协程
print("示例4: 使用gather并发执行协程")

async def task(name, delay):
    print(f"任务 {name} 开始")
    await asyncio.sleep(delay)
    print(f"任务 {name} 完成")
    return f"任务 {name} 结果"

async def main_gather():
    # 并发执行多个协程
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3)
    )
    print(f"所有任务完成，结果: {results}")

asyncio.run(main_gather())

# 示例5: 使用wait并发执行协程
print("\n示例5: 使用wait并发执行协程")

async def main_wait():
    # 创建任务列表
    tasks = [
        task("X", 2),
        task("Y", 1),
        task("Z", 3)
    ]
    
    # 等待所有任务完成
    done, pending = await asyncio.wait(tasks)
    
    # 获取结果
    results = []
    for task in done:
        results.append(await task)
    
    print(f"已完成任务结果: {results}")
    print(f"未完成任务: {pending}")

asyncio.run(main_wait())

# ===========================
# 4. 任务（Tasks）
# ===========================
print("\n" + "=" * 50)
print("4. 任务（Tasks）")
print("=" * 50)

# 示例6: 创建和管理任务
print("示例6: 创建和管理任务")

async def long_running_task():
    print("长时间运行的任务开始")
    await asyncio.sleep(3)
    print("长时间运行的任务完成")
    return "长时间任务结果"

async def main_tasks():
    # 创建任务
    task1 = asyncio.create_task(long_running_task())
    
    # 执行其他操作
    print("执行其他操作")
    await asyncio.sleep(1)
    
    # 检查任务状态
    print(f"任务是否完成: {task1.done()}")
    print(f"任务是否正在运行: {task1.running()}")
    
    # 等待任务完成
    result = await task1
    print(f"获取任务结果: {result}")

asyncio.run(main_tasks())

# 示例7: 任务取消
print("\n示例7: 任务取消")

async def cancellable_task():
    try:
        print("可取消任务开始")
        await asyncio.sleep(5)
        print("可取消任务完成")
        return "任务完成"
    except asyncio.CancelledError:
        print("任务被取消")
        raise

async def main_cancel():
    # 创建任务
    task = asyncio.create_task(cancellable_task())
    
    # 等待1秒后取消任务
    await asyncio.sleep(1)
    task.cancel()
    
    try:
        result = await task
        print(f"任务结果: {result}")
    except asyncio.CancelledError:
        print("捕获到任务取消异常")

asyncio.run(main_cancel())

# ===========================
# 5. 异步I/O操作
# ===========================
print("\n" + "=" * 50)
print("5. 异步I/O操作")
print("=" * 50)

# 示例8: 异步文件操作
print("示例8: 异步文件操作")

try:
    async def read_file():
        # 异步读取文件
        async with asyncio.open(__file__, "r") as f:
            content = await f.read()
            return len(content)

    async def write_file():
        # 异步写入文件
        async with asyncio.open("test.txt", "w") as f:
            await f.write("Hello, asyncio!")
            return "文件写入完成"

    async def main_file():
        # 并发执行文件操作
        read_task = asyncio.create_task(read_file())
        write_task = asyncio.create_task(write_file())
        
        # 获取结果
        file_length, write_result = await asyncio.gather(read_task, write_task)
        
        print(f"当前文件长度: {file_length} 字节")
        print(f"写入结果: {write_result}")

    asyncio.run(main_file())

except AttributeError:
    print("注意: Python 3.7+支持异步文件操作")

# 示例9: 异步网络请求（简化版）
print("\n示例9: 异步网络请求（简化版）")

try:
    # 尝试导入aiohttp库
    import aiohttp
    
    async def fetch_url(session, url):
        async with session.get(url) as response:
            return await response.text()
    
    async def main_http():
        urls = [
            "https://www.python.org",
            "https://www.github.com",
            "https://www.google.com"
        ]
        
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_url(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
            
            for url, content in zip(urls, results):
                print(f"{url}: {len(content)} 字节")
    
    print("注意: 需要安装aiohttp库才能运行此示例")
    print("安装命令: pip install aiohttp")
    # asyncio.run(main_http())
    
except ImportError:
    print("注意: aiohttp库未安装，无法演示异步网络请求")

# ===========================
# 6. 同步原语
# ===========================
print("\n" + "=" * 50)
print("6. 同步原语")
print("=" * 50)

# 示例10: 使用Lock进行同步
print("示例10: 使用Lock进行同步")

# 共享变量
shared_counter = 0
lock = asyncio.Lock()

async def increment():
    global shared_counter
    for _ in range(1000):
        async with lock:  # 获取锁
            shared_counter += 1

async def main_lock():
    # 创建多个协程同时修改共享变量
    tasks = [increment() for _ in range(10)]
    await asyncio.gather(*tasks)
    print(f"最终计数器值: {shared_counter}")
    print(f"预期计数器值: {10 * 1000}")

asyncio.run(main_lock())

# 示例11: 使用Event进行同步
print("\n示例11: 使用Event进行同步")

event = asyncio.Event()

async def waiter():
    print("等待事件...")
    await event.wait()  # 等待事件被设置
    print("事件已触发")

async def setter():
    print("准备设置事件")
    await asyncio.sleep(2)
    event.set()  # 设置事件
    print("事件已设置")

async def main_event():
    await asyncio.gather(waiter(), setter())

asyncio.run(main_event())

# 示例12: 使用Condition进行同步
print("\n示例12: 使用Condition进行同步")

condition = asyncio.Condition()
queue = []
MAX_QUEUE_SIZE = 5

async def producer():
    for i in range(10):
        async with condition:
            # 等待队列不满
            while len(queue) >= MAX_QUEUE_SIZE:
                await condition.wait()
            
            # 生产数据
            item = f"项{i+1}"
            queue.append(item)
            print(f"生产: {item}, 队列: {queue}")
            
            # 通知消费者
            condition.notify_all()
        
        await asyncio.sleep(random.uniform(0.1, 0.5))

async def consumer():
    for _ in range(10):
        async with condition:
            # 等待队列不空
            while len(queue) == 0:
                await condition.wait()
            
            # 消费数据
            item = queue.pop(0)
            print(f"消费: {item}, 队列: {queue}")
            
            # 通知生产者
            condition.notify_all()
        
        await asyncio.sleep(random.uniform(0.1, 0.5))

async def main_condition():
    await asyncio.gather(producer(), consumer())

asyncio.run(main_condition())

# ===========================
# 7. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("7. 实际应用示例")
print("=" * 50)

# 示例13: 异步Web服务器
print("示例13: 异步Web服务器")

async def handle_client(reader, writer):
    """处理客户端请求"""
    # 读取请求
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    
    print(f"接收到来自 {addr} 的请求: {message}")
    
    # 模拟处理时间
    await asyncio.sleep(1)
    
    # 发送响应
    response = f"HTTP/1.1 200 OK\nContent-Length: 12\n\nHello World!"
    writer.write(response.encode())
    await writer.drain()
    
    # 关闭连接
    writer.close()
    await writer.wait_closed()

async def main_server():
    # 创建服务器
    server = await asyncio.start_server(handle_client, '127.0.0.1', 8888)
    
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f"服务器运行在 {addrs}")
    
    # 运行服务器（这里只演示，不实际运行）
    print("注意: 服务器不会实际运行，仅展示代码示例")
    # async with server:
    #     await server.serve_forever()

asyncio.run(main_server())

# 示例14: 异步爬虫（简化版）
print("\n示例14: 异步爬虫（简化版）")

async def fetch_page(page_number):
    """模拟爬取页面"""
    print(f"爬取页面 {page_number}")
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return f"页面 {page_number} 的内容"

async def main_crawler():
    # 并发爬取10个页面
    pages = range(1, 11)
    tasks = [fetch_page(page) for page in pages]
    results = await asyncio.gather(*tasks)
    
    print("\n爬取结果:")
    for page, content in zip(pages, results):
        print(f"页面 {page}: {content}")

asyncio.run(main_crawler())

# 示例15: 异步API调用
print("\n示例15: 异步API调用")

async def call_api(endpoint):
    """模拟API调用"""
    print(f"调用API端点: {endpoint}")
    await asyncio.sleep(random.uniform(0.5, 2))
    return f"{endpoint} 的响应数据"

async def main_api():
    endpoints = [
        "/api/users",
        "/api/products",
        "/api/orders",
        "/api/reports",
        "/api/stats"
    ]
    
    # 并发调用多个API
    tasks = [call_api(endpoint) for endpoint in endpoints]
    results = await asyncio.gather(*tasks)
    
    print("\nAPI调用结果:")
    for endpoint, result in zip(endpoints, results):
        print(f"{endpoint}: {result}")

asyncio.run(main_api())

# ===========================
# 8. 与多线程/多进程的比较
# ===========================
print("\n" + "=" * 50)
print("8. 与多线程/多进程的比较")
print("=" * 50)

print("asyncio vs 多线程")
print("- asyncio基于单线程事件循环，避免了线程切换开销")
print("- 协程比线程更轻量级，一个进程可以支持数万个协程")
print("- asyncio不需要线程同步机制，避免了死锁风险")
print("- 多线程受GIL限制，asyncio不受GIL限制")
print("- 多线程适合CPU密集型任务，asyncio适合I/O密集型任务")

print("\nasyncio vs 多进程")
print("- asyncio基于单线程，多进程基于多线程")
print("- asyncio内存消耗更小，多进程内存消耗更大")
print("- asyncio进程间通信更简单，多进程需要专门的通信机制")
print("- 多进程可以充分利用多核CPU，asyncio在单线程中运行")
print("- 多进程适合CPU密集型任务，asyncio适合I/O密集型任务")

# ===========================
# 9. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("9. 最佳实践")
print("=" * 50)

print("1. 协程设计")
print("   - 使用async/await关键字定义协程")
print("   - 避免在协程中使用阻塞操作（如time.sleep()，应使用asyncio.sleep()）")
print("   - 协程函数名应该清晰反映其功能")

print("\n2. 并发控制")
print("   - 使用asyncio.gather()并发执行多个协程")
print("   - 使用asyncio.wait()更精细地控制并发")
print("   - 使用asyncio.Semaphore限制并发数")

print("\n3. 错误处理")
print("   - 使用try/except捕获协程中的异常")
print("   - 处理asyncio.CancelledError异常")
print("   - 使用asyncio.gather(return_exceptions=True)收集异常")

print("\n4. 资源管理")
print("   - 使用async with语句管理异步资源")
print("   - 确保资源正确关闭")
print("   - 使用上下文管理器包装异步操作")

print("\n5. 性能优化")
print("   - 避免在事件循环中执行CPU密集型操作")
print("   - 使用asyncio.to_thread()将CPU密集型操作移到线程池")
print("   - 合理设置并发数，避免过载")

print("\n6. 调试")
print("   - 使用asyncio.run()运行协程")
print("   - 启用调试模式：asyncio.run(main(), debug=True)")
print("   - 使用asyncio.all_tasks()查看所有任务")
print("   - 使用asyncio.current_task()查看当前任务")

# ===========================
# 10. 总结
# ===========================
print("\n" + "=" * 50)
print("10. 总结")
print("=" * 50)
print("asyncio模块提供了强大的异步编程框架")
print("使用协程实现高效的并发，避免了线程切换的开销")
print("基于事件循环的单线程模型，适合高并发I/O密集型任务")

print("\n主要功能:")
print("- 协程支持")
print("- 事件循环")
print("- 异步I/O操作")
print("- 任务和未来")
print("- 同步原语")
print("- 并发控制")

print("\n应用场景:")
print("- 高并发I/O密集型任务")
print("- 网络服务器")
print("- 异步爬虫")
print("- API调用")
print("- 提高程序响应性")

print("\n使用asyncio模块可以显著提高程序的并发能力")
print("是现代Python异步编程的标准选择")
