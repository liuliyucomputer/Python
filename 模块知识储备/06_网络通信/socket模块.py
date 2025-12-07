# socket模块详解

socket模块是Python中用于网络编程的核心模块，提供了底层的套接字编程接口，支持TCP和UDP协议，可以用于创建各种网络应用程序。

## 模块概述

socket模块包含了一系列用于创建、配置和操作套接字的函数和类，主要功能包括：
- 创建不同类型的套接字（TCP、UDP等）
- 配置套接字选项
- 建立网络连接
- 发送和接收数据
- 关闭连接

## 基本概念

### 套接字类型

- **SOCK_STREAM**：TCP套接字，提供可靠的、面向连接的通信
- **SOCK_DGRAM**：UDP套接字，提供不可靠的、无连接的通信
- **SOCK_RAW**：原始套接字，允许直接访问底层协议

### 地址族

- **AF_INET**：IPv4地址族
- **AF_INET6**：IPv6地址族
- **AF_UNIX**：Unix域套接字

## 基本用法

### 导入模块

```python
import socket
```

### 创建TCP服务器

```python
import socket

# 创建TCP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
host = ''  # 绑定所有可用的接口
port = 12345
s.bind((host, port))

# 监听连接
s.listen(5)  # 最大连接数为5
print(f"服务器正在监听端口 {port}...")

while True:
    # 接受连接
    client_socket, client_address = s.accept()
    print(f"接收到来自 {client_address} 的连接")
    
    # 接收数据
    data = client_socket.recv(1024)
    if not data:
        break
    
    print(f"接收到数据: {data.decode('utf-8')}")
    
    # 发送响应
    response = "Hello, client! I received your message."
    client_socket.sendall(response.encode('utf-8'))
    
    # 关闭连接
    client_socket.close()
    print(f"与 {client_address} 的连接已关闭")

# 关闭服务器套接字
# s.close()  # 服务器通常不会主动关闭
```

### 创建TCP客户端

```python
import socket

# 创建TCP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
host = 'localhost'
port = 12345
s.connect((host, port))

# 发送数据
message = "Hello, server!"
s.sendall(message.encode('utf-8'))

# 接收响应
data = s.recv(1024)
print(f"接收到服务器响应: {data.decode('utf-8')}")

# 关闭连接
s.close()
```

### 创建UDP服务器

```python
import socket

# 创建UDP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定地址和端口
host = ''
port = 12346
s.bind((host, port))

print(f"UDP服务器正在监听端口 {port}...")

while True:
    # 接收数据
    data, client_address = s.recvfrom(1024)
    print(f"接收到来自 {client_address} 的数据: {data.decode('utf-8')}")
    
    # 发送响应
    response = "Hello, UDP client!"
    s.sendto(response.encode('utf-8'), client_address)
    print(f"已向 {client_address} 发送响应")

# 关闭服务器套接字
# s.close()
```

### 创建UDP客户端

```python
import socket

# 创建UDP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 服务器地址
host = 'localhost'
port = 12346

# 发送数据
message = "Hello, UDP server!"
s.sendto(message.encode('utf-8'), (host, port))

# 接收响应
data, server_address = s.recvfrom(1024)
print(f"接收到服务器响应: {data.decode('utf-8')}")

# 关闭连接
s.close()
```

## 高级功能

### 设置套接字选项

```python
import socket

# 创建TCP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置SO_REUSEADDR选项，允许端口重用
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 设置接收超时
s.settimeout(5.0)

# 获取套接字选项
reuse_addr = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
print(f"SO_REUSEADDR选项值: {reuse_addr}")

# 关闭套接字
s.close()
```

### 使用上下文管理器

```python
import socket

# 使用with语句自动关闭套接字
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('www.example.com', 80))
    s.sendall(b'GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n')
    data = s.recv(1024)
    print(f"接收到数据: {data.decode('utf-8')}")
```

### 处理二进制数据

```python
import socket
import struct

# 创建UDP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 12347

s.bind(('', port))
print(f"UDP服务器正在监听端口 {port}，处理二进制数据...")

while True:
    # 接收二进制数据
    data, addr = s.recvfrom(1024)
    
    # 解析二进制数据（假设包含一个整数和一个浮点数）
    unpacked_data = struct.unpack('if', data)
    print(f"接收到二进制数据: {data}")
    print(f"解析后的数据: 整数={unpacked_data[0]}, 浮点数={unpacked_data[1]}")
    
    # 发送响应
    response = struct.pack('f', unpacked_data[1] * 2)
    s.sendto(response, addr)
    print(f"已向 {addr} 发送响应: {response}")

# 关闭套接字
# s.close()
```

### 处理大文件传输

```python
import socket
import os

# 文件服务器
def file_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 12348))
        s.listen(5)
        print("文件服务器正在监听端口 12348...")
        
        while True:
            client_socket, addr = s.accept()
            print(f"接收到来自 {addr} 的连接")
            
            # 接收文件名
            filename = client_socket.recv(1024).decode('utf-8')
            if not filename:
                client_socket.close()
                continue
            
            print(f"客户端请求下载文件: {filename}")
            
            # 检查文件是否存在
            if not os.path.exists(filename):
                client_socket.sendall(b'File not found')
                client_socket.close()
                continue
            
            # 发送文件大小
            file_size = os.path.getsize(filename)
            client_socket.sendall(str(file_size).encode('utf-8'))
            
            # 等待客户端确认
            client_socket.recv(1024)
            
            # 发送文件内容
            with open(filename, 'rb') as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    client_socket.sendall(data)
            
            print(f"文件 {filename} 已发送完成")
            client_socket.close()

# 文件客户端
def file_client(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12348))
        
        # 发送文件名
        s.sendall(filename.encode('utf-8'))
        
        # 接收文件大小
        file_size_data = s.recv(1024)
        if file_size_data == b'File not found':
            print(f"文件 {filename} 不存在")
            return
        
        file_size = int(file_size_data.decode('utf-8'))
        print(f"文件大小: {file_size} 字节")
        
        # 发送确认
        s.sendall(b'OK')
        
        # 接收文件内容
        received_size = 0
        with open(f'client_{filename}', 'wb') as f:
            while received_size < file_size:
                data = s.recv(1024)
                if not data:
                    break
                f.write(data)
                received_size += len(data)
                print(f"已接收: {received_size}/{file_size} 字节 ({received_size/file_size*100:.2f}%)")
        
        print(f"文件 {filename} 下载完成")

# 创建测试文件
with open('test_file.txt', 'w') as f:
    for i in range(1000):
        f.write(f"This is line {i} of the test file.\n")

# 启动文件服务器（需要在单独的进程或线程中运行）
# file_server()

# 运行客户端下载文件
# file_client('test_file.txt')
```

## 实际应用示例

### 示例1：简单的HTTP服务器

```python
import socket

def simple_http_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 8080))
        s.listen(5)
        print("简单HTTP服务器正在监听端口 8080...")
        
        while True:
            client_socket, addr = s.accept()
            
            # 接收HTTP请求
            request = client_socket.recv(1024).decode('utf-8')
            print(f"接收到请求:\n{request}")
            
            # 解析请求路径
            request_lines = request.split('\r\n')
            if request_lines:
                path = request_lines[0].split()[1]
            else:
                path = '/'
            
            # 准备响应
            response_body = f"<html><body><h1>Simple HTTP Server</h1><p>Request path: {path}</p></body></html>"
            response_headers = [
                "HTTP/1.1 200 OK",
                "Content-Type: text/html",
                f"Content-Length: {len(response_body)}",
                "Connection: close",
                "",
            ]
            
            response = '\r\n'.join(response_headers) + response_body
            
            # 发送响应
            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()

# 启动HTTP服务器
# simple_http_server()
```

### 示例2：网络聊天室

```python
import socket
import threading

# 客户端列表
clients = []

# 处理客户端连接
def handle_client(client_socket, client_address):
    print(f"客户端 {client_address} 已连接")
    
    # 广播新用户加入
    broadcast(f"用户 {client_address} 加入了聊天室", client_socket)
    
    try:
        while True:
            # 接收消息
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            
            print(f"从 {client_address} 接收消息: {message}")
            
            # 广播消息
            broadcast(f"{client_address}: {message}", client_socket)
    
    except Exception as e:
        print(f"与 {client_address} 的连接出现错误: {e}")
    
    finally:
        # 移除客户端
        clients.remove(client_socket)
        broadcast(f"用户 {client_address} 离开了聊天室", None)
        client_socket.close()
        print(f"客户端 {client_address} 已断开连接")

# 广播消息给所有客户端
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode('utf-8'))
            except:
                # 移除无法发送的客户端
                clients.remove(client)

# 启动聊天室服务器
def chat_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 12349))
        s.listen(10)
        print("聊天室服务器正在监听端口 12349...")
        print("客户端可以连接到 localhost:12349")
        
        while True:
            client_socket, client_address = s.accept()
            clients.append(client_socket)
            
            # 为每个客户端创建线程
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.daemon = True
            client_thread.start()

# 启动聊天室服务器
# chat_server()
```

## 常见问题和解决方案

### 端口被占用

**问题**：运行服务器时出现 `Address already in use` 错误。

**解决方案**：
1. 使用不同的端口
2. 设置 `SO_REUSEADDR` 选项
3. 等待端口释放

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

### 连接超时

**问题**：客户端连接服务器时出现超时。

**解决方案**：
1. 检查服务器是否正在运行
2. 检查防火墙设置
3. 检查网络连接
4. 设置合理的超时时间

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10.0)  # 设置10秒超时
try:
    s.connect(('localhost', 12345))
except socket.timeout:
    print("连接超时")
except Exception as e:
    print(f"连接错误: {e}")
```

### 数据不完整

**问题**：接收数据时只收到部分数据。

**解决方案**：
1. 循环接收数据直到收到完整的数据
2. 使用固定长度的消息头

```python
def recv_all(socket, size):
    """接收指定大小的数据"""
    data = b''
    while len(data) < size:
        packet = socket.recv(size - len(data))
        if not packet:
            return None
        data += packet
    return data

# 使用示例
# full_data = recv_all(client_socket, expected_size)
```

## 最佳实践

1. **使用上下文管理器**：使用 `with` 语句自动关闭套接字
2. **设置超时**：避免程序在网络操作上无限期阻塞
3. **处理异常**：捕获并处理网络操作可能引发的异常
4. **使用线程/进程**：为每个客户端连接创建独立的线程或进程
5. **限制数据大小**：避免接收过大的数据导致内存问题
6. **使用非阻塞I/O**：对于高性能应用，考虑使用非阻塞I/O或异步I/O

## 与其他模块的关系

- **asyncio**：提供异步网络I/O功能，适合高性能网络应用
- **urllib**：基于socket模块，提供更高级的HTTP客户端功能
- **http**：基于socket模块，提供HTTP服务器和客户端功能
- **threading/multiprocessing**：用于处理多个客户端连接

## 总结

socket模块是Python网络编程的基础，提供了底层的套接字编程接口。通过socket模块，可以创建各种网络应用程序，包括服务器、客户端、HTTP服务器、聊天室等。

熟练掌握socket模块的使用，需要了解网络通信的基本原理、TCP和UDP协议的特点，以及如何处理各种网络异常情况。在实际应用中，还可以结合其他模块（如asyncio、threading等）来提高程序的性能和可靠性。