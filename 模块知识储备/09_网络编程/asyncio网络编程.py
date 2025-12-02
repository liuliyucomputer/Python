"""
asyncio网络编程详解

asyncio是Python 3.4引入的标准库，专为异步I/O操作设计，特别适用于网络编程场景。
本模块详细介绍asyncio在网络编程中的应用，包括异步套接字、异步服务器、异步HTTP客户端等。
"""

## 目录

1. [概述](#概述)
2. [基础概念](#基础概念)
   - 事件循环
   - 协程（Coroutines）
   - Future 和 Task
   - 异步上下文管理器
3. [异步网络基础](#异步网络基础)
   - 异步套接字
   - 流（Streams）
4. [异步TCP客户端](#异步TCP客户端)
5. [异步TCP服务器](#异步TCP服务器)
6. [异步HTTP客户端](#异步HTTP客户端)
7. [异步HTTP服务器](#异步HTTP服务器)
8. [高级网络功能](#高级网络功能)
   - 异步DNS解析
   - SSL/TLS支持
   - 超时处理
   - 信号处理
9. [性能优化](#性能优化)
10. [实际应用示例](#实际应用示例)
    - 聊天服务器
    - 异步代理服务器
    - 并发网络爬虫
11. [与其他异步框架的比较](#与其他异步框架的比较)
12. [最佳实践](#最佳实践)
13. [常见问题](#常见问题)
14. [总结](#总结)

## 概述

asyncio提供了编写单线程并发代码的基础设施，使用协程、事件循环和异步I/O操作。在网络编程中，asyncio的主要优势在于：

- **高效I/O多路复用**：能够处理大量并发连接，而无需为每个连接创建线程
- **简化异步代码**：使用`async/await`语法，使异步代码看起来更像同步代码
- **内置网络原语**：提供了高级异步网络API，简化了异步服务器和客户端的开发
- **可组合性**：协程可以轻松组合，构建复杂的异步应用

## 基础概念

### 2.1 事件循环

事件循环是asyncio的核心，负责调度协程、处理I/O事件、运行异步任务等。

```python
import asyncio

async def main():
    print("Hello, asyncio!")
    await asyncio.sleep(1)  # 非阻塞延迟
    print("After sleep")

# 获取默认事件循环
loop = asyncio.get_event_loop()

# 运行协程直到完成
loop.run_until_complete(main())

# 关闭事件循环
loop.close()

# Python 3.7+ 更简洁的写法
# asyncio.run(main())
```

### 2.2 协程（Coroutines）

协程是一种特殊的函数，使用`async def`定义，可以使用`await`暂停执行，等待其他协程完成。

```python
import asyncio

async def fetch_data(delay):
    print(f"开始获取数据，延迟{delay}秒")
    await asyncio.sleep(delay)
    print(f"数据获取完成，延迟{delay}秒")
    return f"数据结果_{delay}"

async def process_data(data):
    print(f"开始处理数据: {data}")
    await asyncio.sleep(0.5)
    print(f"数据处理完成: {data}")
    return f"处理后的_{data}"

async def main():
    # 串行执行
    data1 = await fetch_data(1)
    result1 = await process_data(data1)
    
    data2 = await fetch_data(2)
    result2 = await process_data(data2)
    
    print(f"最终结果: {result1}, {result2}")

asyncio.run(main())
```

### 2.3 Future 和 Task

- **Future**：表示一个尚未完成的异步操作的结果
- **Task**：Future的子类，用于在事件循环中执行协程

```python
import asyncio

async def compute(x, y):
    print(f"计算 {x} + {y}")
    await asyncio.sleep(1)
    return x + y

async def main():
    # 创建任务
    task1 = asyncio.create_task(compute(1, 2))
    task2 = asyncio.create_task(compute(3, 4))
    
    # 等待多个任务完成
    results = await asyncio.gather(task1, task2)
    print(f"结果: {results}")

asyncio.run(main())
```

### 2.4 异步上下文管理器

异步上下文管理器允许在异步操作中使用`async with`语句。

```python
import asyncio

class AsyncFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    async def __aenter__(self):
        print(f"打开文件: {self.filename}")
        # 模拟异步文件打开
        await asyncio.sleep(0.1)
        self.file = open(self.filename, self.mode)
        return self.file
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"关闭文件: {self.filename}")
        if self.file:
            self.file.close()
        # 模拟异步清理
        await asyncio.sleep(0.1)
        return False  # 不抑制异常

async def main():
    async with AsyncFile("example.txt", "w") as f:
        f.write("Hello, asyncio!")

asyncio.run(main())
```

## 异步网络基础

### 3.1 异步套接字

asyncio提供了对套接字的异步封装，支持TCP、UDP等协议。

```python
import asyncio
import socket

async def connect_with_asyncio(host, port):
    # 创建异步套接字
    reader, writer = await asyncio.open_connection(host, port)
    
    # 发送数据
    message = "Hello from asyncio!\r\n"
    writer.write(message.encode())
    await writer.drain()  # 确保数据被发送
    
    # 接收数据
    data = await reader.read(100)  # 读取最多100字节
    print(f"收到: {data.decode()}")
    
    # 关闭连接
    writer.close()
    await writer.wait_closed()

async def main():
    await connect_with_asyncio("example.com", 80)

asyncio.run(main())
```

### 3.2 流（Streams）

Streams是asyncio提供的高级I/O抽象，包括：
- `StreamReader`：用于异步读取
- `StreamWriter`：用于异步写入

```python
import asyncio

async def tcp_client():
    reader, writer = await asyncio.open_connection(
        'localhost', 8888)
    
    # 发送数据
    writer.write(b'Hello World!\n')
    await writer.drain()
    
    # 接收响应
    data = await reader.readline()
    print(f'Received: {data.decode()!r}')
    
    # 关闭连接
    writer.close()
    await writer.wait_closed()

async def main():
    await tcp_client()

# 注意：这个示例需要一个运行在8888端口的服务器
# asyncio.run(main())
```

## 异步TCP客户端

下面是一个完整的异步TCP客户端示例，展示了如何处理连接、发送和接收数据。

```python
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AsyncTCPClient:
    def __init__(self, host, port, timeout=10):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.reader = None
        self.writer = None
        self.connected = False
    
    async def connect(self):
        """建立连接"""
        try:
            self.reader, self.writer = await asyncio.wait_for(
                asyncio.open_connection(self.host, self.port), 
                timeout=self.timeout
            )
            self.connected = True
            logger.info(f"已连接到 {self.host}:{self.port}")
            return True
        except Exception as e:
            logger.error(f"连接失败: {e}")
            return False
    
    async def send(self, data):
        """发送数据"""
        if not self.connected:
            if not await self.connect():
                return False
        
        try:
            self.writer.write(data)
            await self.writer.drain()
            logger.debug(f"已发送: {data}")
            return True
        except Exception as e:
            logger.error(f"发送失败: {e}")
            self.connected = False
            return False
    
    async def receive(self, max_bytes=1024):
        """接收数据"""
        if not self.connected:
            return None
        
        try:
            data = await asyncio.wait_for(
                self.reader.read(max_bytes), 
                timeout=self.timeout
            )
            if not data:  # 连接已关闭
                self.connected = False
                return None
            
            logger.debug(f"已接收: {data}")
            return data
        except Exception as e:
            logger.error(f"接收失败: {e}")
            self.connected = False
            return None
    
    async def send_and_receive(self, data, max_bytes=1024):
        """发送数据并等待响应"""
        if await self.send(data):
            return await self.receive(max_bytes)
        return None
    
    async def close(self):
        """关闭连接"""
        if self.writer:
            self.writer.close()
            await self.writer.wait_closed()
        self.connected = False
        logger.info("连接已关闭")
    
    async def __aenter__(self):
        """支持异步上下文管理器"""
        await self.connect()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """退出异步上下文管理器"""
        await self.close()

async def test_tcp_client():
    async with AsyncTCPClient('echo.websocket.org', 80) as client:
        # 发送HTTP请求
        request = b"""GET / HTTP/1.1\r\n""
        request += f"Host: echo.websocket.org\r\n".encode()
        request += b"Connection: close\r\n\r\n"
        
        response = await client.send_and_receive(request, max_bytes=4096)
        if response:
            print(f"HTTP响应:\n{response.decode('utf-8')[:500]}...")

# asyncio.run(test_tcp_client())
```

## 异步TCP服务器

下面是一个异步TCP回显服务器的示例：

```python
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AsyncTCPServer:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        self.server = None
    
    async def handle_client(self, reader, writer):
        """处理客户端连接"""
        addr = writer.get_extra_info('peername')
        logger.info(f"新连接来自 {addr}")
        
        try:
            while True:
                # 接收数据
                data = await reader.read(1024)
                if not data:  # 客户端关闭连接
                    break
                
                message = data.decode().strip()
                logger.info(f"收到来自 {addr} 的消息: {message}")
                
                # 回显消息
                response = f"回显: {message}\n".encode()
                writer.write(response)
                await writer.drain()
                
                logger.info(f"已回复 {addr}")
                
        except asyncio.CancelledError:
            logger.info(f"客户端连接 {addr} 已取消")
        except Exception as e:
            logger.error(f"处理客户端 {addr} 时出错: {e}")
        finally:
            # 关闭连接
            writer.close()
            await writer.wait_closed()
            logger.info(f"客户端连接 {addr} 已关闭")
    
    async def start(self):
        """启动服务器"""
        self.server = await asyncio.start_server(
            self.handle_client, 
            self.host, 
            self.port
        )
        
        addr = self.server.sockets[0].getsockname()
        logger.info(f"服务器启动在 {addr[0]}:{addr[1]}")
        
        async with self.server:
            await self.server.serve_forever()
    
    def stop(self):
        """停止服务器"""
        if self.server:
            logger.info("正在停止服务器...")
            self.server.close()

async def main():
    server = AsyncTCPServer()
    await server.start()

# 运行服务器
# asyncio.run(main())
```

## 异步HTTP客户端

asyncio可以与aiohttp库结合，实现强大的异步HTTP客户端功能。

首先需要安装aiohttp：`pip install aiohttp`

```python
import asyncio
import aiohttp
import time

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status

async def fetch_all(urls, timeout=30):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=timeout)) as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(fetch(session, url))
            tasks.append(task)
        
        # 并发执行所有请求
        return await asyncio.gather(*tasks, return_exceptions=True)

async def main():
    urls = [
        'https://www.python.org',
        'https://www.google.com',
        'https://www.github.com',
        'https://www.stackoverflow.com',
        'https://www.wikipedia.org'
    ]
    
    start_time = time.time()
    results = await fetch_all(urls)
    elapsed = time.time() - start_time
    
    print(f"全部请求完成，耗时: {elapsed:.2f}秒")
    
    for i, (result, url) in enumerate(zip(results, urls)):
        if isinstance(result, Exception):
            print(f"URL {url} 请求失败: {result}")
        else:
            content, status = result
            print(f"URL {url}\n状态码: {status}\n内容长度: {len(content)}字节\n")

# asyncio.run(main())
```

## 异步HTTP服务器

使用aiohttp创建异步HTTP服务器：

```python
from aiohttp import web
import asyncio

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = f"Hello, {name}!"
    return web.Response(text=text)

async def json_handler(request):
    data = {
        'status': 'success',
        'message': 'Async HTTP server is working!',
        'timestamp': asyncio.get_event_loop().time()
    }
    return web.json_response(data)

async def setup_routes(app):
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)
    app.router.add_get('/api/status', json_handler)

async def main():
    app = web.Application()
    await setup_routes(app)
    
    # 启动服务器
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    
    print("HTTP服务器启动在 http://localhost:8080")
    
    # 保持运行
    while True:
        await asyncio.sleep(3600)

# 运行服务器
# web.run_app(main())
```

## 高级网络功能

### 8.1 异步DNS解析

asyncio提供了异步DNS解析功能，避免在DNS查询时阻塞事件循环。

```python
import asyncio
import socket

async def resolve_host(hostname):
    # 异步DNS解析
    try:
        # 使用asyncio的getaddrinfo
        results = await asyncio.get_event_loop().getaddrinfo(
            hostname, None, 
            proto=socket.IPPROTO_TCP
        )
        
        # 提取IP地址
        ip_addresses = []
        for family, type_, proto, canonname, sockaddr in results:
            ip_addresses.append(sockaddr[0])
        
        return ip_addresses
    except Exception as e:
        print(f"DNS解析失败: {e}")
        return []

async def main():
    hostnames = [
        'www.python.org',
        'www.google.com', 
        'www.github.com'
    ]
    
    for hostname in hostnames:
        ip_addresses = await resolve_host(hostname)
        print(f"{hostname} 的IP地址: {', '.join(ip_addresses)}")

# asyncio.run(main())
```

### 8.2 SSL/TLS支持

asyncio支持SSL/TLS加密连接，用于安全通信。

```python
import asyncio
import ssl

async def secure_tcp_client():
    # 创建SSL上下文
    ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    # 验证服务器证书
    # ssl_context.check_hostname = True
    # ssl_context.verify_mode = ssl.CERT_REQUIRED
    
    # 连接到HTTPS服务器
    reader, writer = await asyncio.open_connection(
        'www.python.org', 443, 
        ssl=ssl_context
    )
    
    # 发送HTTP请求
    writer.write(b"""GET / HTTP/1.1\r\n""")
    writer.write(b"Host: www.python.org\r\n")
    writer.write(b"Connection: close\r\n\r\n")
    await writer.drain()
    
    # 读取响应
    response = await reader.read(4096)
    print(f"收到响应: {response.decode('utf-8')[:500]}...")
    
    # 关闭连接
    writer.close()
    await writer.wait_closed()

# asyncio.run(secure_tcp_client())
```

### 8.3 超时处理

使用`asyncio.wait_for`或`asyncio.wait`设置超时，避免操作无限等待。

```python
import asyncio

async def slow_operation():
    print("开始慢速操作...")
    await asyncio.sleep(3)
    print("慢速操作完成")
    return "操作结果"

async def main():
    try:
        # 设置2秒超时
        result = await asyncio.wait_for(slow_operation(), timeout=2)
        print(f"结果: {result}")
    except asyncio.TimeoutError:
        print("操作超时!")

# asyncio.run(main())
```

### 8.4 信号处理

在异步服务器中处理信号，以便优雅地关闭。

```python
import asyncio
import signal

class SignalHandler:
    def __init__(self):
        self.shutdown = False
    
    def register(self, loop):
        # 注册SIGINT和SIGTERM信号处理
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, self.handle_signal)
    
    def handle_signal(self):
        print("收到关闭信号，正在优雅关闭...")
        self.shutdown = True
    
    async def wait_for_shutdown(self):
        # 等待关闭信号
        while not self.shutdown:
            await asyncio.sleep(0.1)

async def main():
    loop = asyncio.get_event_loop()
    signal_handler = SignalHandler()
    signal_handler.register(loop)
    
    print("服务器正在运行，按Ctrl+C关闭...")
    await signal_handler.wait_for_shutdown()
    print("服务器已关闭")

# asyncio.run(main())
```

## 性能优化

### 9.1 连接池管理

使用连接池复用TCP连接，减少连接建立和关闭的开销。

```python
import asyncio
import aiohttp
import time

async def fetch_with_session(session, url):
    """使用共享的会话发送请求"""
    async with session.get(url) as response:
        return await response.text()

async def many_requests_with_pool():
    # 创建一个共享的会话（连接池）
    timeout = aiohttp.ClientTimeout(total=30, connect=5, sock_connect=5, sock_read=10)
    
    async with aiohttp.ClientSession(timeout=timeout) as session:
        urls = [f"https://httpbin.org/delay/0.1" for _ in range(50)]
        
        start_time = time.time()
        tasks = [fetch_with_session(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        elapsed = time.time() - start_time
        
        print(f"使用连接池: 50个请求耗时 {elapsed:.2f}秒")

async def many_requests_without_pool():
    # 不使用连接池，每次创建新会话
    urls = [f"https://httpbin.org/delay/0.1" for _ in range(10)]  # 减少请求数量以避免超时
    
    start_time = time.time()
    
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                await response.text()
    
    elapsed = time.time() - start_time
    print(f"不使用连接池: 10个请求耗时 {elapsed:.2f}秒")

async def main():
    await many_requests_with_pool()
    await many_requests_without_pool()

# asyncio.run(main())
```

### 9.2 并发控制

使用信号量限制并发请求数量，避免对服务器造成过大压力。

```python
import asyncio
import aiohttp
import time

async def fetch_with_semaphore(semaphore, session, url):
    """使用信号量限制并发"""
    async with semaphore:  # 获取信号量
        async with session.get(url) as response:
            await asyncio.sleep(0.1)  # 模拟处理时间
            return await response.text()

async def controlled_concurrency():
    # 创建连接池和信号量
    async with aiohttp.ClientSession() as session:
        # 限制最多5个并发请求
        semaphore = asyncio.Semaphore(5)
        
        urls = [f"https://httpbin.org/get?i={i}" for i in range(20)]
        
        start_time = time.time()
        tasks = [fetch_with_semaphore(semaphore, session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        elapsed = time.time() - start_time
        
        print(f"受控并发: 20个请求耗时 {elapsed:.2f}秒")
        print(f"成功请求数: {len(results)}")

# asyncio.run(controlled_concurrency())
```

### 9.3 流控和批处理

对大量数据进行流式处理和批处理，减少内存使用。

```python
import asyncio
import json

async def stream_processor(reader, batch_size=100):
    """流式处理数据"""
    buffer = []
    processed_count = 0
    
    while True:
        # 异步读取一行数据
        line = await reader.readline()
        if not line:
            break
        
        try:
            # 解析JSON数据
            data = json.loads(line)
            buffer.append(data)
            
            # 当缓冲区达到批处理大小时，处理一批数据
            if len(buffer) >= batch_size:
                await process_batch(buffer)
                processed_count += len(buffer)
                buffer = []
                print(f"已处理批次，累计: {processed_count}")
                
        except json.JSONDecodeError:
            print(f"解析错误: {line}")
    
    # 处理剩余数据
    if buffer:
        await process_batch(buffer)
        processed_count += len(buffer)
    
    print(f"处理完成，总共处理: {processed_count}条数据")

async def process_batch(batch):
    """模拟批处理操作"""
    # 模拟处理时间
    await asyncio.sleep(0.1)
    # 这里可以执行实际的数据处理逻辑
    pass

async def main():
    # 模拟文件读取器
    class MockReader:
        def __init__(self):
            self.data = [json.dumps({"id": i, "value": f"data_{i}"}) + "\n" for i in range(1000)]
            self.index = 0
        
        async def readline(self):
            if self.index < len(self.data):
                line = self.data[self.index].encode()
                self.index += 1
                return line
            return b''
    
    reader = MockReader()
    await stream_processor(reader)

# asyncio.run(main())
```

## 实际应用示例

### 10.1 聊天服务器

下面是一个基于asyncio的简单聊天服务器示例：

```python
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ChatServer:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        self.clients = set()
        self.server = None
    
    async def handle_client(self, reader, writer):
        """处理客户端连接"""
        addr = writer.get_extra_info('peername')
        logger.info(f"新客户端连接: {addr}")
        
        # 添加到客户端集合
        self.clients.add((reader, writer))
        
        try:
            # 发送欢迎消息
            welcome_msg = f"欢迎加入聊天室! 当前在线: {len(self.clients)}\n".encode()
            writer.write(welcome_msg)
            await writer.drain()
            
            # 通知其他客户端
            await self.broadcast(f"用户 {addr[0]}:{addr[1]} 加入了聊天室", exclude=writer)
            
            # 处理消息
            while True:
                data = await reader.readline()
                if not data:  # 客户端关闭连接
                    break
                
                message = data.decode().strip()
                if message:  # 忽略空消息
                    logger.info(f"来自 {addr} 的消息: {message}")
                    # 广播消息给所有客户端
                    await self.broadcast(f"{addr[0]}:{addr[1]}: {message}")
        
        except asyncio.CancelledError:
            logger.info(f"客户端 {addr} 连接已取消")
        except Exception as e:
            logger.error(f"处理客户端 {addr} 时出错: {e}")
        finally:
            # 从客户端集合中移除
            self.clients.discard((reader, writer))
            # 关闭连接
            writer.close()
            await writer.wait_closed()
            # 通知其他客户端
            await self.broadcast(f"用户 {addr[0]}:{addr[1]} 离开了聊天室")
            logger.info(f"客户端 {addr} 已断开连接，当前在线: {len(self.clients)}")
    
    async def broadcast(self, message, exclude=None):
        """广播消息给所有客户端"""
        message_bytes = (message + "\n").encode()
        
        # 创建所有写入任务
        tasks = []
        for reader, writer in self.clients:
            if writer != exclude:
                # 复制writer引用，避免闭包问题
                tasks.append(self._send_to_client(writer, message_bytes))
        
        # 并发发送消息
        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)
    
    async def _send_to_client(self, writer, message):
        """发送消息给单个客户端"""
        try:
            writer.write(message)
            await writer.drain()
        except Exception as e:
            addr = writer.get_extra_info('peername')
            logger.error(f"发送消息给 {addr} 失败: {e}")
            # 清理断开的连接
            for r, w in list(self.clients):
                if w == writer:
                    self.clients.discard((r, w))
                    try:
                        w.close()
                        await w.wait_closed()
                    except:
                        pass
                    break
    
    async def start(self):
        """启动服务器"""
        self.server = await asyncio.start_server(
            self.handle_client, 
            self.host, 
            self.port
        )
        
        addr = self.server.sockets[0].getsockname()
        logger.info(f"聊天服务器启动在 {addr[0]}:{addr[1]}")
        
        async with self.server:
            await self.server.serve_forever()
    
    def stop(self):
        """停止服务器"""
        if self.server:
            logger.info("正在停止服务器...")
            self.server.close()

# 简单的聊天客户端
class ChatClient:
    def __init__(self, host='localhost', port=8888, nickname=None):
        self.host = host
        self.port = port
        self.nickname = nickname or f"user_{id(self)}"
        self.reader = None
        self.writer = None
    
    async def connect(self):
        """连接到服务器"""
        try:
            self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
            print(f"已连接到聊天服务器 {self.host}:{self.port}")
            return True
        except Exception as e:
            print(f"连接服务器失败: {e}")
            return False
    
    async def receive_messages(self):
        """接收并显示消息"""
        try:
            while True:
                data = await self.reader.readline()
                if not data:
                    print("连接已关闭")
                    break
                
                message = data.decode().strip()
                print(f"\r{message}")
                print(f"{self.nickname}> ", end="", flush=True)
        except Exception as e:
            print(f"接收消息出错: {e}")
    
    async def send_messages(self):
        """发送用户输入的消息"""
        try:
            while True:
                message = await asyncio.to_thread(input, f"{self.nickname}> ")
                if message.lower() in ["exit", "quit", "/exit", "/quit"]:
                    break
                
                self.writer.write((message + "\n").encode())
                await self.writer.drain()
        except Exception as e:
            print(f"发送消息出错: {e}")
    
    async def run(self):
        """运行客户端"""
        if not await self.connect():
            return
        
        # 同时运行接收和发送任务
        receive_task = asyncio.create_task(self.receive_messages())
        send_task = asyncio.create_task(self.send_messages())
        
        # 等待发送任务完成（用户输入exit）
        await send_task
        
        # 取消接收任务
        receive_task.cancel()
        
        # 关闭连接
        self.writer.close()
        await self.writer.wait_closed()
        print("客户端已关闭")

async def main():
    # 这里可以选择运行服务器或客户端
    # 启动服务器: server = ChatServer(); await server.start()
    # 运行客户端: client = ChatClient(nickname="Alice"); await client.run()
    pass

# asyncio.run(main())
```

### 10.2 异步代理服务器

下面是一个基于asyncio的简单HTTP代理服务器：

```python
import asyncio
import logging
import socket
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AsyncProxyServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.server = None
    
    async def handle_client(self, client_reader, client_writer):
        """处理客户端连接"""
        client_addr = client_writer.get_extra_info('peername')
        logger.info(f"新连接来自 {client_addr}")
        
        try:
            # 读取客户端请求
            request_line = await client_reader.readline()
            if not request_line:
                return
            
            # 解析请求行
            request_line = request_line.decode('utf-8').strip()
            logger.debug(f"请求行: {request_line}")
            
            # 解析HTTP方法、URL和协议版本
            parts = request_line.split(' ', 2)
            if len(parts) != 3:
                client_writer.close()
                await client_writer.wait_closed()
                return
            
            method, url, version = parts
            
            # 解析URL
            parsed_url = urlparse(url)
            target_host = parsed_url.netloc.split(':')[0] if ':' in parsed_url.netloc else parsed_url.netloc
            target_port = int(parsed_url.netloc.split(':')[1]) if ':' in parsed_url.netloc else 80
            
            logger.info(f"代理请求: {method} {target_host}:{target_port}{parsed_url.path}")
            
            # 读取并转发剩余的请求头
            headers = await client_reader.readuntil(b"\r\n\r\n")
            
            # 构建新的请求头（替换Host头）
            new_request_line = f"{method} {parsed_url.path} {version}\r\n"
            new_request = new_request_line.encode('utf-8') + headers
            
            # 连接目标服务器
            try:
                target_reader, target_writer = await asyncio.open_connection(target_host, target_port)
                
                # 转发请求到目标服务器
                target_writer.write(new_request)
                await target_writer.drain()
                
                # 双向转发数据
                async def forward_data(reader, writer):
                    try:
                        while True:
                            data = await reader.read(8192)
                            if not data:
                                break
                            writer.write(data)
                            await writer.drain()
                    except Exception as e:
                        logger.error(f"转发数据错误: {e}")
                    finally:
                        writer.close()
                
                # 创建两个任务：客户端->目标 和 目标->客户端
                client_to_target = asyncio.create_task(forward_data(client_reader, target_writer))
                target_to_client = asyncio.create_task(forward_data(target_reader, client_writer))
                
                # 等待任一方向的数据传输完成
                done, pending = await asyncio.wait(
                    [client_to_target, target_to_client],
                    return_when=asyncio.FIRST_COMPLETED
                )
                
                # 取消未完成的任务
                for task in pending:
                    task.cancel()
                    
            except Exception as e:
                logger.error(f"连接目标服务器错误 {target_host}:{target_port}: {e}")
                error_response = b"""
HTTP/1.1 502 Bad Gateway
Content-Type: text/html
Content-Length: 120

<html>
<body><h1>502 Bad Gateway</h1>
<p>无法连接到目标服务器: %s</p>
</body></html>
""" % str(e).encode()
                client_writer.write(error_response)
                await client_writer.drain()
        
        except Exception as e:
            logger.error(f"处理客户端 {client_addr} 时出错: {e}")
        finally:
            # 确保客户端连接已关闭
            client_writer.close()
            await client_writer.wait_closed()
            logger.info(f"客户端连接 {client_addr} 已关闭")
    
    async def start(self):
        """启动代理服务器"""
        self.server = await asyncio.start_server(
            self.handle_client, 
            self.host, 
            self.port
        )
        
        addr = self.server.sockets[0].getsockname()
        logger.info(f"HTTP代理服务器启动在 {addr[0]}:{addr[1]}")
        
        async with self.server:
            await self.server.serve_forever()

async def main():
    proxy_server = AsyncProxyServer()
    await proxy_server.start()

# asyncio.run(main())
```

### 10.3 并发网络爬虫

下面是一个使用asyncio和aiohttp的并发网络爬虫示例：

```python
import asyncio
import aiohttp
import time
import re
from urllib.parse import urljoin, urlparse
from collections import deque
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AsyncWebCrawler:
    def __init__(self, max_depth=2, max_concurrent=10, user_agent='AsyncCrawler/1.0'):
        self.max_depth = max_depth  # 最大爬取深度
        self.max_concurrent = max_concurrent  # 最大并发连接数
        self.user_agent = user_agent  # 用户代理
        self.visited_urls = set()  # 已访问的URL集合
        self.url_queue = deque()  # URL队列
        self.semaphore = asyncio.Semaphore(max_concurrent)  # 控制并发
        self.session = None
    
    async def _setup_session(self):
        """设置HTTP会话"""
        timeout = aiohttp.ClientTimeout(total=30, connect=5, sock_connect=5, sock_read=10)
        self.session = aiohttp.ClientSession(
            timeout=timeout,
            headers={
                'User-Agent': self.user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
            }
        )
    
    async def _close_session(self):
        """关闭HTTP会话"""
        if self.session:
            await self.session.close()
    
    def _is_valid_url(self, url, base_url):
        """检查URL是否有效且在同一域名下"""
        parsed = urlparse(url)
        base_parsed = urlparse(base_url)
        
        # 确保URL有协议、域名，且在同一域名下
        return (parsed.scheme in ('http', 'https') and 
                parsed.netloc == base_parsed.netloc and 
                not url in self.visited_urls)
    
    async def _fetch_page(self, url, depth):
        """爬取单个页面"""
        if depth > self.max_depth or url in self.visited_urls:
            return []
        
        async with self.semaphore:
            self.visited_urls.add(url)
            logger.info(f"正在爬取: {url} (深度: {depth})")
            
            try:
                async with self.session.get(url, allow_redirects=True) as response:
                    if response.status != 200:
                        logger.warning(f"获取页面失败: {url}, 状态码: {response.status}")
                        return []
                    
                    # 检查内容类型
                    content_type = response.headers.get('Content-Type', '')
                    if not content_type.startswith('text/html'):
                        logger.info(f"跳过非HTML内容: {url}, 内容类型: {content_type}")
                        return []
                    
                    # 读取页面内容
                    html = await response.text()
                    
                    # 提取所有链接
                    links = re.findall(r'href=["\'](.*?)["\']', html)
                    
                    # 规范化链接
                    normalized_links = []
                    for link in links:
                        absolute_url = urljoin(url, link)
                        if self._is_valid_url(absolute_url, url):
                            normalized_links.append(absolute_url)
                    
                    logger.info(f"从 {url} 发现 {len(normalized_links)} 个新链接")
                    return normalized_links
                    
            except Exception as e:
                logger.error(f"爬取 {url} 时出错: {e}")
                return []
    
    async def crawl(self, start_url):
        """开始爬取"""
        # 设置会话
        await self._setup_session()
        
        try:
            # 初始化队列
            self.url_queue.append((start_url, 0))  # (URL, 深度)
            
            while self.url_queue:
                url, depth = self.url_queue.popleft()
                
                # 爬取当前页面
                new_links = await self._fetch_page(url, depth)
                
                # 添加新链接到队列
                for link in new_links:
                    self.url_queue.append((link, depth + 1))
            
            logger.info(f"爬取完成，共访问 {len(self.visited_urls)} 个URL")
            return self.visited_urls
            
        finally:
            # 确保关闭会话
            await self._close_session()
    
    async def __aenter__(self):
        """支持异步上下文管理器"""
        await self._setup_session()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """退出异步上下文管理器"""
        await self._close_session()

async def main():
    crawler = AsyncWebCrawler(max_depth=2, max_concurrent=5)
    
    start_time = time.time()
    try:
        visited_urls = await crawler.crawl('https://python.org')
        elapsed = time.time() - start_time
        
        print(f"\n爬取完成!")
        print(f"总耗时: {elapsed:.2f}秒")
        print(f"爬取URL数量: {len(visited_urls)}")
        print(f"前10个URL:")
        for i, url in enumerate(list(visited_urls)[:10], 1):
            print(f"{i}. {url}")
            
    except KeyboardInterrupt:
        print("爬取被用户中断")

# asyncio.run(main())
```

## 与其他异步框架的比较

| 特性 | asyncio | Twisted | Tornado | gevent | Trio |
|------|---------|---------|---------|--------|------|
| 语言 | Python | Python | Python | Python | Python |
| 类型 | 标准库 | 第三方库 | 第三方库 | 第三方库 | 第三方库 |
| API风格 | async/await | 回调/Deferred | 回调/coroutine | 同步风格 | async/await |
| 学习曲线 | 中等 | 陡峭 | 中等 | 平缓 | 中等 |
| 性能 | 优秀 | 良好 | 良好 | 优秀 | 优秀 |
| 生态系统 | 丰富 | 丰富 | 中等 | 丰富 | 发展中 |
| 官方支持 | 是 | 否 | 否 | 否 | 否 |
| 适用场景 | 通用异步编程 | 复杂网络应用 | Web应用 | 同步代码改造 | 注重可维护性的异步应用 |

## 最佳实践

### 11.1 代码组织

1. **使用异步上下文管理器**：使用`async with`管理资源，确保资源正确释放。

```python
async def process_data():
    async with aiohttp.ClientSession() as session:
        # 使用session
        pass
```

2. **使用异步迭代器**：对于需要异步迭代的数据。

```python
class AsyncDataLoader:
    async def __aiter__(self):
        return self
    
    async def __anext__(self):
        data = await self.fetch_next_item()
        if data is None:
            raise StopAsyncIteration
        return data
```

3. **模块化**：将异步操作封装到类和函数中，提高代码可维护性。

### 11.2 性能优化

1. **使用连接池**：对于HTTP请求，重用`ClientSession`。

2. **限制并发**：使用信号量控制并发请求数量。

3. **避免阻塞操作**：使用`asyncio.to_thread()`或`loop.run_in_executor()`处理CPU密集型任务。

```python
import asyncio
import concurrent.futures

def cpu_intensive_task(data):
    # CPU密集型操作
    result = 0
    for i in range(1000000):
        result += i
    return result

async def process_with_executor(data):
    loop = asyncio.get_event_loop()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, cpu_intensive_task, data)
    return result
```

4. **使用`asyncio.gather()`**：并发执行多个异步任务。

### 11.3 错误处理

1. **使用`try/except`捕获异常**：特别是网络操作可能出现的各种异常。

```python
async def fetch_data(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    except aiohttp.ClientError as e:
        print(f"HTTP客户端错误: {e}")
    except asyncio.TimeoutError:
        print("请求超时")
    except json.JSONDecodeError:
        print("响应不是有效的JSON")
    return None
```

2. **使用`asyncio.gather(return_exceptions=True)`**：允许部分任务失败而不影响其他任务。

3. **实现重试机制**：对于临时网络故障，实现自动重试。

```python
async def fetch_with_retry(url, max_retries=3, delay=1):
    retries = 0
    while retries < max_retries:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()
                    return await response.text()
        except Exception as e:
            retries += 1
            if retries == max_retries:
                raise
            print(f"请求失败，{retries}/{max_retries} 次重试，{delay}秒后重试...")
            await asyncio.sleep(delay)
```

### 11.4 调试技巧

1. **使用`asyncio.debug()`**：启用异步调试模式。

```python
import asyncio
asyncio.run(main(), debug=True)
```

2. **使用`asyncio.all_tasks()`**：查看所有运行中的任务。

```python
def dump_tasks():
    tasks = asyncio.all_tasks()
    print(f"当前运行中的任务数: {len(tasks)}")
    for task in tasks:
        print(f"  {task.get_name()} - {task.done()}")
```

3. **使用日志记录**：记录关键操作和错误。

4. **使用`asyncio.current_task()`**：获取当前正在执行的任务。

## 常见问题

### 12.1 常见错误及解决方案

1. **`RuntimeError: Event loop is closed`**
   - 原因：尝试在事件循环关闭后使用它。
   - 解决方案：确保所有异步操作在事件循环关闭前完成。

2. **`asyncio.TimeoutError`**
   - 原因：操作超时。
   - 解决方案：调整超时设置，实现重试机制。

3. **`aiohttp.ClientConnectorError`**
   - 原因：无法连接到服务器。
   - 解决方案：检查网络连接和服务器状态，实现重试机制。

4. **阻塞事件循环**
   - 原因：在协程中执行阻塞操作。
   - 解决方案：使用`asyncio.to_thread()`或`loop.run_in_executor()`处理阻塞操作。

5. **任务未取消**
   - 原因：程序退出时任务仍在运行。
   - 解决方案：正确管理任务生命周期，使用`task.cancel()`取消任务。

### 12.2 性能问题

1. **内存泄漏**
   - 症状：长时间运行后内存使用不断增长。
   - 解决方案：避免循环引用，确保任务正确取消，使用弱引用管理回调。

2. **CPU使用率高**
   - 症状：事件循环占用大量CPU。
   - 解决方案：检查是否有紧密循环，添加适当的延迟，避免不必要的轮询。

3. **任务堆积**
   - 症状：大量任务在队列中等待执行。
   - 解决方案：限制并发数量，使用背压机制，优化任务执行效率。

## 总结

asyncio为Python提供了强大的异步编程支持，特别适合网络编程场景。通过本模块的学习，我们了解了：

- asyncio的核心概念：事件循环、协程、任务和Future
- 异步网络编程的基础：异步套接字和流
- 如何实现异步TCP客户端和服务器
- 如何使用asyncio与其他库（如aiohttp）结合进行HTTP通信
- 高级网络功能：SSL/TLS、超时处理、信号处理等
- 性能优化技术：连接池、并发控制、流控等
- 实际应用示例：聊天服务器、代理服务器、并发爬虫
- 最佳实践和常见问题解决方案

asyncio的出现极大地简化了Python中的异步编程，使开发人员能够编写高效、可扩展的网络应用，同时保持代码的可读性和可维护性。随着Python异步生态系统的不断发展，asyncio将在网络编程领域发挥越来越重要的作用。

对于初学者，建议从简单的示例开始，逐步掌握异步编程的思维方式，避免常见的陷阱（如阻塞事件循环）。对于有经验的开发者，可以深入学习asyncio的高级功能，如自定义事件循环策略、异步上下文管理器等，以构建更复杂、更高效的异步应用。

最后，无论使用哪种异步编程框架，都应该始终关注代码的可维护性、错误处理和性能优化，这样才能开发出高质量的网络应用。

# 代码示例运行说明

本模块中的代码示例大多需要在Python 3.7+环境下运行。部分示例需要安装额外的库，如`aiohttp`。

安装所需依赖：
```
pip install aiohttp
```

运行服务器示例时，请注意端口占用问题，确保示例中使用的端口没有被其他程序占用。

对于网络请求示例，需要确保网络连接可用。在运行爬虫示例时，请遵守相关网站的robots.txt规则和使用条款。

要运行某个代码示例，请取消注释示例末尾的运行语句，如：
```python
# asyncio.run(main())
```
改为：
```python
asyncio.run(main())
```

或者创建一个新的Python文件，将示例代码复制过去，然后执行该文件。

希望本模块能帮助您更好地理解和应用Python的异步网络编程！