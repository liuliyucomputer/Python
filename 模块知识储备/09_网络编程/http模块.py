# http模块 - Python HTTP服务器与客户端编程

Python的`http`模块是一个包含多个子模块的包，提供了HTTP协议的服务器端和客户端实现。本文档将详细介绍http模块的核心功能、使用方法、最佳实践以及实际应用案例。

## 1. 模块概述

`http`模块主要包含以下子模块：

- **http.server**: 提供基本的HTTP服务器实现
- **http.client**: 提供基本的HTTP客户端实现
- **http.cookies**: 处理HTTP cookies
- **http.cookiejar**: 客户端HTTP cookie处理
- **http.HTTPStatus**: 定义HTTP状态码常量
- **http.auth**: 提供HTTP认证功能

## 2. http.server模块

`http.server`模块提供了创建HTTP服务器的类，这些类可以用来构建简单的Web服务器。

### 2.1 核心类

#### 2.1.1 HTTPServer

`HTTPServer`是一个基本的HTTP服务器类，负责监听端口、接受连接并将请求交给处理器处理。

```python
from http.server import HTTPServer

# 创建服务器实例
server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, RequestHandlerClass)

# 启动服务器
print(f"服务器运行在 http://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
```

#### 2.1.2 BaseHTTPRequestHandler

`BaseHTTPRequestHandler`是一个处理HTTP请求的基类，定义了处理不同HTTP方法的接口。

```python
from http.server import BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 处理GET请求
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello World!</h1></body></html>")

    def do_POST(self):
        # 处理POST请求
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        # 处理数据...
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>POST Received!</h1></body></html>")
```

#### 2.1.3 SimpleHTTPRequestHandler

`SimpleHTTPRequestHandler`继承自`BaseHTTPRequestHandler`，提供了简单的文件服务器功能。

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

# 创建简单的文件服务器
server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

print(f"文件服务器运行在 http://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
```

#### 2.1.4 CGIHTTPRequestHandler

`CGIHTTPRequestHandler`继承自`SimpleHTTPRequestHandler`，增加了CGI脚本支持。

```python
from http.server import HTTPServer, CGIHTTPRequestHandler
import os

# 设置CGI目录
os.chdir('.')

server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

# 指定CGI脚本目录
CGIHTTPRequestHandler.cgi_directories = ['/cgi-bin']

print(f"CGI服务器运行在 http://{server_address[0]}:{server_address[1]}")
httpd.serve_forever()
```

### 2.2 HTTP请求处理

#### 2.2.1 请求解析

HTTP请求处理器可以访问以下请求相关的属性：

```python
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 请求路径
        print(f"路径: {self.path}")
        
        # 请求头
        print("请求头:")
        for header, value in self.headers.items():
            print(f"  {header}: {value}")
        
        # 客户端地址
        print(f"客户端地址: {self.client_address}")
        
        # 服务器地址
        print(f"服务器地址: {self.server.server_address}")
        
        # 命令（GET, POST等）
        print(f"命令: {self.command}")
        
        # 版本
        print(f"HTTP版本: {self.request_version}")
        
        # 发送响应
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Request Information</h1></body></html>")
```

#### 2.2.2 获取查询参数

```python
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class QueryHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 解析URL
        parsed_url = urlparse(self.path)
        # 获取查询参数
        query_params = parse_qs(parsed_url.query)
        
        # 打印查询参数
        print(f"查询参数: {query_params}")
        
        # 构建响应
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # 在响应中显示查询参数
        response = f"""
        <html>
        <body>
            <h1>查询参数</h1>
            <ul>
        """
        
        for param, values in query_params.items():
            for value in values:
                response += f"<li>{param}: {value}</li>"
        
        response += """
            </ul>
        </body>
        </html>
        """
        
        self.wfile.write(response.encode('utf-8'))
```

### 2.3 HTTP响应生成

#### 2.3.1 设置状态码

```python
# 成功响应
self.send_response(200)  # 200 OK

# 重定向
self.send_response(301)  # 301 Moved Permanently
self.send_header('Location', '/new-page')

# 客户端错误
self.send_response(404)  # 404 Not Found
self.send_response(400)  # 400 Bad Request

# 服务器错误
self.send_response(500)  # 500 Internal Server Error
```

#### 2.3.2 设置响应头

```python
self.send_response(200)
# 设置内容类型
self.send_header('Content-type', 'text/html; charset=utf-8')
# 设置内容长度
self.send_header('Content-Length', str(len(content)))
# 设置缓存控制
self.send_header('Cache-Control', 'max-age=3600')
# 设置允许的跨域请求
self.send_header('Access-Control-Allow-Origin', '*')
# 结束头部
self.end_headers()
```

#### 2.3.3 发送响应体

```python
# 发送文本
self.wfile.write(b"Hello World")

# 发送HTML
html_content = """
<!DOCTYPE html>
<html>
<head><title>Example</title></head>
<body><h1>Hello World</h1></body>
</html>
"""
self.wfile.write(html_content.encode('utf-8'))

# 发送JSON
import json
data = {"name": "John", "age": 30}
json_content = json.dumps(data)
self.send_header('Content-type', 'application/json')
self.end_headers()
self.wfile.write(json_content.encode('utf-8'))
```

### 2.4 实现RESTful API

下面是一个简单的RESTful API服务器示例：

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs

# 模拟数据库
books = [
    {"id": 1, "title": "Python Basics", "author": "John Smith"},
    {"id": 2, "title": "Web Development", "author": "Jane Doe"}
]

class RESTHandler(BaseHTTPRequestHandler):
    # 处理GET请求
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path_parts = parsed_url.path.strip('/').split('/')
        
        # 获取所有图书
        if len(path_parts) == 1 and path_parts[0] == 'books':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(books).encode('utf-8'))
        
        # 获取单本图书
        elif len(path_parts) == 2 and path_parts[0] == 'books':
            try:
                book_id = int(path_parts[1])
                book = next((b for b in books if b["id"] == book_id), None)
                
                if book:
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps(book).encode('utf-8'))
                else:
                    self.send_error(404, "Book not found")
            except ValueError:
                self.send_error(400, "Invalid book ID")
        
        else:
            self.send_error(404, "Resource not found")
    
    # 处理POST请求
    def do_POST(self):
        if self.path == '/books':
            # 获取内容长度
            content_length = int(self.headers['Content-Length'])
            # 读取请求体
            post_data = self.rfile.read(content_length)
            # 解析JSON
            try:
                new_book = json.loads(post_data)
                # 验证数据
                if not all(key in new_book for key in ['title', 'author']):
                    self.send_error(400, "Missing title or author")
                    return
                
                # 生成新ID
                new_id = max(b['id'] for b in books) + 1 if books else 1
                new_book['id'] = new_id
                # 添加到数据库
                books.append(new_book)
                
                # 返回新创建的图书
                self.send_response(201)  # Created
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(new_book).encode('utf-8'))
            except json.JSONDecodeError:
                self.send_error(400, "Invalid JSON")
        else:
            self.send_error(404, "Resource not found")
    
    # 处理PUT请求
    def do_PUT(self):
        parsed_url = urlparse(self.path)
        path_parts = parsed_url.path.strip('/').split('/')
        
        if len(path_parts) == 2 and path_parts[0] == 'books':
            try:
                book_id = int(path_parts[1])
                book_index = next((i for i, b in enumerate(books) if b["id"] == book_id), None)
                
                if book_index is not None:
                    # 获取请求体
                    content_length = int(self.headers['Content-Length'])
                    put_data = self.rfile.read(content_length)
                    
                    try:
                        updated_data = json.loads(put_data)
                        # 更新图书
                        books[book_index].update(updated_data)
                        # 保留ID
                        books[book_index]['id'] = book_id
                        
                        self.send_response(200)
                        self.send_header('Content-type', 'application/json')
                        self.end_headers()
                        self.wfile.write(json.dumps(books[book_index]).encode('utf-8'))
                    except json.JSONDecodeError:
                        self.send_error(400, "Invalid JSON")
                else:
                    self.send_error(404, "Book not found")
            except ValueError:
                self.send_error(400, "Invalid book ID")
        else:
            self.send_error(404, "Resource not found")
    
    # 处理DELETE请求
    def do_DELETE(self):
        parsed_url = urlparse(self.path)
        path_parts = parsed_url.path.strip('/').split('/')
        
        if len(path_parts) == 2 and path_parts[0] == 'books':
            try:
                book_id = int(path_parts[1])
                book_index = next((i for i, b in enumerate(books) if b["id"] == book_id), None)
                
                if book_index is not None:
                    # 删除图书
                    deleted_book = books.pop(book_index)
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"message": "Book deleted", "book": deleted_book}).encode('utf-8'))
                else:
                    self.send_error(404, "Book not found")
            except ValueError:
                self.send_error(400, "Invalid book ID")
        else:
            self.send_error(404, "Resource not found")
    
    # 启用CORS
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    # 处理OPTIONS请求
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def run_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RESTHandler)
    print(f"REST API服务器运行在 http://{server_address[0]}:{server_address[1]}")
    print("可用端点:")
    print("  GET    /books           - 获取所有图书")
    print("  GET    /books/{id}      - 获取指定ID的图书")
    print("  POST   /books           - 创建新图书")
    print("  PUT    /books/{id}      - 更新指定ID的图书")
    print("  DELETE /books/{id}      - 删除指定ID的图书")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器关闭")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
```

## 3. http.client模块

`http.client`模块提供了HTTP和HTTPS客户端的实现，用于发送HTTP请求。

### 3.1 核心类

#### 3.1.1 HTTPConnection

`HTTPConnection`类用于创建HTTP连接。

```python
import http.client

# 创建连接
conn = http.client.HTTPConnection('www.example.com')

# 发送GET请求
conn.request('GET', '/')

# 获取响应
response = conn.getresponse()

# 打印响应信息
print(f"状态码: {response.status}")
print(f"原因: {response.reason}")
print("响应头:")
for header, value in response.getheaders():
    print(f"  {header}: {value}")

# 读取响应体
data = response.read()
print(f"响应体长度: {len(data)} 字节")
print(f"响应体: {data.decode('utf-8')}")

# 关闭连接
conn.close()
```

#### 3.1.2 HTTPSConnection

`HTTPSConnection`类用于创建HTTPS连接。

```python
import http.client

# 创建HTTPS连接
conn = http.client.HTTPSConnection('www.example.com')

# 发送GET请求
conn.request('GET', '/')

# 获取响应
response = conn.getresponse()

# 打印响应信息
print(f"状态码: {response.status}")
print(f"原因: {response.reason}")

# 读取响应体
data = response.read()
print(f"响应体长度: {len(data)} 字节")

# 关闭连接
conn.close()
```

#### 3.1.3 HTTPResponse

`HTTPResponse`类表示HTTP响应，由`getresponse()`方法返回。

```python
import http.client

conn = http.client.HTTPConnection('www.example.com')
conn.request('GET', '/')
response = conn.getresponse()

# HTTPResponse对象的主要属性和方法
print(f"状态码: {response.status}")
print(f"原因: {response.reason}")
print(f"版本: {response.version}")
print(f"是否已关闭: {response.closed}")
print(f"长度: {response.length}")
print(f"分块编码: {response.chunked}")

# 获取特定响应头
content_type = response.getheader('Content-Type')
print(f"Content-Type: {content_type}")

# 获取所有响应头
headers = response.getheaders()
print("所有响应头:")
for header, value in headers:
    print(f"  {header}: {value}")

# 读取响应体
# 一次读取全部
data = response.read()
# 或者分块读取
# chunk = response.read(1024)  # 读取最多1024字节

# 关闭响应
response.close()
conn.close()
```

### 3.2 发送HTTP请求

#### 3.2.1 GET请求

```python
import http.client

def send_get_request():
    conn = http.client.HTTPConnection('api.example.com')
    
    # 设置请求头
    headers = {
        'User-Agent': 'Python-http.client/3.x',
        'Accept': 'application/json'
    }
    
    # 发送GET请求
    conn.request('GET', '/data?param1=value1&param2=value2', headers=headers)
    
    # 获取响应
    response = conn.getresponse()
    
    # 处理响应
    print(f"GET响应状态码: {response.status}")
    data = response.read()
    print(f"响应数据: {data.decode('utf-8')}")
    
    conn.close()

if __name__ == "__main__":
    send_get_request()
```

#### 3.2.2 POST请求

```python
import http.client
import json

def send_post_request():
    conn = http.client.HTTPConnection('api.example.com')
    
    # 准备POST数据
    post_data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'age': 30
    }
    json_data = json.dumps(post_data)
    
    # 设置请求头
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': len(json_data)
    }
    
    # 发送POST请求
    conn.request('POST', '/submit', json_data, headers)
    
    # 获取响应
    response = conn.getresponse()
    
    # 处理响应
    print(f"POST响应状态码: {response.status}")
    data = response.read()
    print(f"响应数据: {data.decode('utf-8')}")
    
    conn.close()

if __name__ == "__main__":
    send_post_request()
```

#### 3.2.3 PUT请求

```python
import http.client
import json

def send_put_request():
    conn = http.client.HTTPConnection('api.example.com')
    
    # 准备PUT数据
    put_data = {
        'name': 'Updated Name',
        'description': 'Updated description'
    }
    json_data = json.dumps(put_data)
    
    # 设置请求头
    headers = {
        'Content-Type': 'application/json',
        'Content-Length': len(json_data)
    }
    
    # 发送PUT请求
    conn.request('PUT', '/resource/123', json_data, headers)
    
    # 获取响应
    response = conn.getresponse()
    
    # 处理响应
    print(f"PUT响应状态码: {response.status}")
    data = response.read()
    print(f"响应数据: {data.decode('utf-8')}")
    
    conn.close()

if __name__ == "__main__":
    send_put_request()
```

#### 3.2.4 DELETE请求

```python
import http.client

def send_delete_request():
    conn = http.client.HTTPConnection('api.example.com')
    
    # 发送DELETE请求
    conn.request('DELETE', '/resource/123')
    
    # 获取响应
    response = conn.getresponse()
    
    # 处理响应
    print(f"DELETE响应状态码: {response.status}")
    data = response.read()
    print(f"响应数据: {data.decode('utf-8')}")
    
    conn.close()

if __name__ == "__main__":
    send_delete_request()
```

### 3.3 处理HTTP认证

```python
import http.client
import base64

def send_authenticated_request():
    conn = http.client.HTTPConnection('api.example.com')
    
    # 创建认证头
    username = 'user'
    password = 'password'
    auth_string = f"{username}:{password}"
    encoded_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
    
    # 设置请求头
    headers = {
        'Authorization': f'Basic {encoded_auth}'
    }
    
    # 发送请求
    conn.request('GET', '/protected-resource', headers=headers)
    
    # 获取响应
    response = conn.getresponse()
    
    # 处理响应
    print(f"响应状态码: {response.status}")
    data = response.read()
    print(f"响应数据: {data.decode('utf-8')}")
    
    conn.close()

if __name__ == "__main__":
    send_authenticated_request()
```

### 3.4 处理Cookies

```python
import http.client
import json

def handle_cookies():
    conn = http.client.HTTPConnection('api.example.com')
    
    # 第一次请求，获取cookie
    conn.request('GET', '/login?user=test&pass=test')
    response = conn.getresponse()
    
    # 获取set-cookie头
    cookies = response.getheader('Set-Cookie')
    print(f"收到的Cookies: {cookies}")
    
    response.read()  # 必须读取响应体
    
    # 第二次请求，发送cookie
    headers = {
        'Cookie': cookies
    }
    
    conn.request('GET', '/dashboard', headers=headers)
    response = conn.getresponse()
    
    # 处理响应
    print(f"带Cookie的请求响应状态码: {response.status}")
    data = response.read()
    print(f"响应数据: {data.decode('utf-8')}")
    
    conn.close()

if __name__ == "__main__":
    handle_cookies()
```

## 4. http.cookies模块

`http.cookies`模块提供了处理HTTP cookies的功能。

### 4.1 创建和解析Cookies

```python
from http import cookies

def create_cookies():
    # 创建Cookie对象
    c = cookies.SimpleCookie()
    
    # 设置Cookie值
    c['session'] = 'abc123def456'
    c['user_id'] = '1001'
    
    # 设置Cookie属性
    c['session']['domain'] = 'example.com'
    c['session']['path'] = '/'
    c['session']['expires'] = 3600  # 1小时后过期
    c['session']['secure'] = True   # 仅通过HTTPS发送
    c['session']['httponly'] = True # 不能通过JavaScript访问
    c['session']['samesite'] = 'Strict' # 防止CSRF攻击
    
    # 转换为Set-Cookie头格式
    set_cookie_header = c.output(header='Set-Cookie:').strip()
    print("Set-Cookie头:")
    print(set_cookie_header)
    
    # 解析Cookie字符串
    cookie_string = 'session=abc123def456; user_id=1001'
    c2 = cookies.SimpleCookie()
    c2.load(cookie_string)
    
    print("\n解析后的Cookies:")
    for key, morsel in c2.items():
        print(f"{key}: {morsel.value}")

if __name__ == "__main__":
    create_cookies()
```

### 4.2 在HTTP服务器中使用Cookies

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
from http import cookies
import time

def generate_session_id():
    """生成简单的会话ID"""
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=32))

class CookieHandler(BaseHTTPRequestHandler):
    # 会话存储
    sessions = {}
    
    def do_GET(self):
        # 解析请求中的Cookie
        cookies_header = self.headers.get('Cookie', '')
        c = cookies.SimpleCookie()
        c.load(cookies_header)
        
        # 检查是否有会话
        session_id = c.get('session', None)
        
        if session_id and session_id.value in self.sessions:
            # 会话存在
            session_data = self.sessions[session_id.value]
            visits = session_data.get('visits', 0) + 1
            session_data['visits'] = visits
            last_visit = session_data.get('last_visit', time.time())
            session_data['last_visit'] = time.time()
            
            # 发送响应
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = f"""
            <html>
            <body>
                <h1>欢迎回来！</h1>
                <p>会话ID: {session_id.value}</p>
                <p>访问次数: {visits}</p>
                <p>上次访问: {time.ctime(last_visit)}</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))
        else:
            # 创建新会话
            new_session_id = generate_session_id()
            self.sessions[new_session_id] = {
                'visits': 1,
                'last_visit': time.time()
            }
            
            # 设置Cookie
            c = cookies.SimpleCookie()
            c['session'] = new_session_id
            c['session']['path'] = '/'
            c['session']['max-age'] = 86400  # 24小时
            c['session']['httponly'] = True
            
            # 发送响应
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            for morsel in c.values():
                self.send_header('Set-Cookie', morsel.OutputString())
            self.end_headers()
            
            html = f"""
            <html>
            <body>
                <h1>欢迎！</h1>
                <p>新会话已创建</p>
                <p>会话ID: {new_session_id}</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))

def run_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, CookieHandler)
    print(f"Cookie服务器运行在 http://{server_address[0]}:{server_address[1]}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器关闭")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
```

## 5. http.cookiejar模块

`http.cookiejar`模块提供了更高级的客户端Cookie处理功能，通常与`urllib.request`模块一起使用。

### 5.1 创建和管理Cookie Jar

```python
import http.cookiejar

def manage_cookies():
    # 创建CookieJar
    cj = http.cookiejar.CookieJar()
    
    # 添加Cookie
    from http.cookiejar import Cookie
    cookie = Cookie(
        version=0,
        name='session',
        value='abc123',
        port=None,
        port_specified=False,
        domain='example.com',
        domain_specified=True,
        domain_initial_dot=False,
        path='/',
        path_specified=True,
        secure=False,
        expires=1672531199,
        discard=False,
        comment=None,
        comment_url=None,
        rest={'HttpOnly': None},
        rfc2109=False
    )
    cj.set_cookie(cookie)
    
    # 打印所有Cookie
    print("CookieJar中的Cookie:")
    for cookie in cj:
        print(f"  {cookie.name}={cookie.value} (domain={cookie.domain}, path={cookie.path})")
    
    # 保存Cookie到文件
    filename = 'cookies.txt'
    cj.save(filename)
    print(f"\nCookie已保存到: {filename}")
    
    # 从文件加载Cookie
    new_cj = http.cookiejar.CookieJar()
    new_cj.load(filename)
    print("\n从文件加载的Cookie:")
    for cookie in new_cj:
        print(f"  {cookie.name}={cookie.value} (domain={cookie.domain}, path={cookie.path})")

if __name__ == "__main__":
    manage_cookies()
```

### 5.2 与urllib.request结合使用

```python
import urllib.request
import http.cookiejar

def use_cookiejar_with_urllib():
    # 创建CookieJar
    cj = http.cookiejar.CookieJar()
    
    # 创建处理器
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    
    # 使用opener发送请求（会自动处理Cookie）
    response = opener.open('http://www.example.com')
    
    # 打印收到的Cookie
    print("收到的Cookie:")
    for cookie in cj:
        print(f"  {cookie.name}={cookie.value}")
    
    # 发送后续请求（会自动包含Cookie）
    response2 = opener.open('http://www.example.com/dashboard')
    
    # 保存Cookie到文件
    filename = 'cookies.txt'
    cj.save(filename)
    print(f"\nCookie已保存到: {filename}")
    
    # 从文件加载Cookie
    new_cj = http.cookiejar.CookieJar()
    new_cj.load(filename)
    print("\n从文件加载的Cookie:")
    for cookie in new_cj:
        print(f"  {cookie.name}={cookie.value}")

if __name__ == "__main__":
    use_cookiejar_with_urllib()
```

## 6. http.HTTPStatus枚举

`http.HTTPStatus`提供了HTTP状态码的枚举类，使代码更加可读性。

```python
from http import HTTPStatus

def use_http_status():
    # 访问状态码和原因
    print(f"200: {HTTPStatus.OK.value} {HTTPStatus.OK.phrase}")
    print(f"404: {HTTPStatus.NOT_FOUND.value} {HTTPStatus.NOT_FOUND.phrase}")
    print(f"500: {HTTPStatus.INTERNAL_SERVER_ERROR.value} {HTTPStatus.INTERNAL_SERVER_ERROR.phrase}")
    
    # 获取描述
    print(f"\n200描述: {HTTPStatus.OK.description}")
    print(f"404描述: {HTTPStatus.NOT_FOUND.description}")
    
    # 根据状态码获取枚举
    status_code = 403
    try:
        status = HTTPStatus(status_code)
        print(f"\n状态码 {status_code}: {status.phrase}")
    except ValueError:
        print(f"\n未知状态码: {status_code}")
    
    # 检查状态码类型
    print("\n状态码类型:")
    for status in [HTTPStatus.OK, HTTPStatus.FOUND, HTTPStatus.BAD_REQUEST, HTTPStatus.INTERNAL_SERVER_ERROR]:
        print(f"  {status.value} {status.phrase}:")
        print(f"    信息性: {100 <= status.value < 200}")
        print(f"    成功: {200 <= status.value < 300}")
        print(f"    重定向: {300 <= status.value < 400}")
        print(f"    客户端错误: {400 <= status.value < 500}")
        print(f"    服务器错误: {500 <= status.value < 600}")

if __name__ == "__main__":
    use_http_status()
```

## 7. 实际应用示例

### 7.1 简单的Web服务器

下面是一个功能更完整的Web服务器示例：

```python
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import urllib.parse

def get_file_content(file_path):
    """读取文件内容"""
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return None

def get_content_type(file_path):
    """根据文件扩展名返回MIME类型"""
    ext = os.path.splitext(file_path)[1].lower()
    content_types = {
        '.html': 'text/html',
        '.htm': 'text/html',
        '.css': 'text/css',
        '.js': 'application/javascript',
        '.json': 'application/json',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
        '.txt': 'text/plain',
        '.ico': 'image/x-icon'
    }
    return content_types.get(ext, 'application/octet-stream')

class WebServerHandler(BaseHTTPRequestHandler):
    # 网站根目录
    web_root = '.'
    
    def do_GET(self):
        # 解析路径
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # 防止路径遍历攻击
        if '..' in path:
            self.send_error(403, "Forbidden")
            return
        
        # 转换为文件系统路径
        file_path = os.path.join(self.web_root, path.lstrip('/'))
        
        # 如果是目录，尝试提供index.html
        if os.path.isdir(file_path):
            file_path = os.path.join(file_path, 'index.html')
        
        # 读取文件内容
        content = get_file_content(file_path)
        
        if content is not None:
            # 文件存在，发送文件内容
            self.send_response(200)
            self.send_header('Content-type', get_content_type(file_path))
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            self.wfile.write(content)
        else:
            # 文件不存在，发送404响应
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            error_page = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>404 Not Found</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    h1 {{ color: #333; }}
                    p {{ color: #666; }}
                </style>
            </head>
            <body>
                <h1>404 Not Found</h1>
                <p>请求的资源 '{path}' 不存在。</p>
                <hr>
                <p>Python简易Web服务器</p>
            </body>
            </html>
            """
            self.wfile.write(error_page.encode('utf-8'))
    
    def do_HEAD(self):
        # 处理HEAD请求（只返回头信息）
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        if '..' in path:
            self.send_error(403, "Forbidden")
            return
        
        file_path = os.path.join(self.web_root, path.lstrip('/'))
        
        if os.path.isdir(file_path):
            file_path = os.path.join(file_path, 'index.html')
        
        if os.path.exists(file_path):
            self.send_response(200)
            self.send_header('Content-type', get_content_type(file_path))
            self.send_header('Content-Length', str(os.path.getsize(file_path)))
            self.end_headers()
        else:
            self.send_error(404, "Not Found")
    
    def log_message(self, format, *args):
        # 自定义日志格式
        print(f"[{self.log_date_time_string()}] {args[0]} {args[1]} {args[2]}")

def run_web_server():
    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, WebServerHandler)
    
    print(f"Web服务器运行在 http://{server_address[0]}:{server_address[1]}")
    print(f"网站根目录: {os.path.abspath(WebServerHandler.web_root)}")
    print("按Ctrl+C停止服务器")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器关闭")
        httpd.server_close()

if __name__ == "__main__":
    run_web_server()
```

### 7.2 简易API客户端

```python
import http.client
import json
import urllib.parse

class SimpleAPIClient:
    def __init__(self, base_url, secure=False, timeout=None):
        self.base_url = base_url
        self.secure = secure
        self.timeout = timeout
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        self.cookies = {}
    
    def _get_connection(self):
        """获取HTTP连接"""
        conn_class = http.client.HTTPSConnection if self.secure else http.client.HTTPConnection
        return conn_class(self.base_url, timeout=self.timeout)
    
    def _prepare_headers(self, custom_headers=None):
        """准备请求头"""
        headers = self.headers.copy()
        if custom_headers:
            headers.update(custom_headers)
        
        # 添加Cookies
        if self.cookies:
            cookie_string = '; '.join([f"{k}={v}" for k, v in self.cookies.items()])
            headers['Cookie'] = cookie_string
            
        return headers
    
    def _parse_response(self, response):
        """解析响应"""
        # 处理Cookies
        set_cookie = response.getheader('Set-Cookie')
        if set_cookie:
            # 简单解析Cookie（实际应用中可能需要更复杂的解析）
            cookie_parts = set_cookie.split(';')
            for part in cookie_parts:
                if '=' in part:
                    key, value = part.split('=', 1)
                    self.cookies[key.strip()] = value.strip()
        
        # 读取响应体
        content_type = response.getheader('Content-Type', '')
        data = response.read()
        
        # 如果是JSON，尝试解析
        if 'application/json' in content_type and data:
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                pass  # 保持原样
        elif isinstance(data, bytes):
            # 尝试解码为字符串
            try:
                data = data.decode('utf-8')
            except UnicodeDecodeError:
                pass  # 保持为字节
        
        return {
            'status_code': response.status,
            'reason': response.reason,
            'headers': dict(response.getheaders()),
            'data': data
        }
    
    def get(self, endpoint, params=None, headers=None):
        """发送GET请求"""
        # 构建URL
        url = endpoint
        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{endpoint}?{query_string}"
        
        # 发送请求
        conn = self._get_connection()
        try:
            conn.request('GET', url, headers=self._prepare_headers(headers))
            response = conn.getresponse()
            return self._parse_response(response)
        finally:
            conn.close()
    
    def post(self, endpoint, data=None, json_data=None, headers=None):
        """发送POST请求"""
        # 准备请求体
        body = None
        req_headers = self._prepare_headers(headers)
        
        if json_data is not None:
            body = json.dumps(json_data)
            req_headers['Content-Type'] = 'application/json'
        elif data is not None:
            if isinstance(data, dict):
                body = urllib.parse.urlencode(data)
                req_headers['Content-Type'] = 'application/x-www-form-urlencoded'
            else:
                body = str(data)
        
        # 发送请求
        conn = self._get_connection()
        try:
            conn.request('POST', endpoint, body=body, headers=req_headers)
            response = conn.getresponse()
            return self._parse_response(response)
        finally:
            conn.close()
    
    def put(self, endpoint, data=None, json_data=None, headers=None):
        """发送PUT请求"""
        # 准备请求体
        body = None
        req_headers = self._prepare_headers(headers)
        
        if json_data is not None:
            body = json.dumps(json_data)
            req_headers['Content-Type'] = 'application/json'
        elif data is not None:
            if isinstance(data, dict):
                body = urllib.parse.urlencode(data)
                req_headers['Content-Type'] = 'application/x-www-form-urlencoded'
            else:
                body = str(data)
        
        # 发送请求
        conn = self._get_connection()
        try:
            conn.request('PUT', endpoint, body=body, headers=req_headers)
            response = conn.getresponse()
            return self._parse_response(response)
        finally:
            conn.close()
    
    def delete(self, endpoint, headers=None):
        """发送DELETE请求"""
        # 发送请求
        conn = self._get_connection()
        try:
            conn.request('DELETE', endpoint, headers=self._prepare_headers(headers))
            response = conn.getresponse()
            return self._parse_response(response)
        finally:
            conn.close()
    
    def set_auth(self, username, password):
        """设置基本认证"""
        import base64
        auth_string = f"{username}:{password}"
        encoded_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        self.headers['Authorization'] = f'Basic {encoded_auth}'
    
    def set_header(self, name, value):
        """设置请求头"""
        self.headers[name] = value
    
    def clear_cookies(self):
        """清除所有Cookies"""
        self.cookies = {}

# 示例用法
def use_api_client():
    # 创建客户端实例
    client = SimpleAPIClient('jsonplaceholder.typicode.com', secure=True)
    
    print("\n=== 测试GET请求 ===")
    # 发送GET请求
    response = client.get('/posts/1')
    print(f"状态码: {response['status_code']}")
    print(f"数据: {response['data']}")
    
    print("\n=== 测试带参数的GET请求 ===")
    # 带参数的GET请求
    response = client.get('/posts', params={'userId': 1})
    print(f"状态码: {response['status_code']}")
    print(f"返回了 {len(response['data'])} 条记录")
    
    print("\n=== 测试POST请求 ===")
    # 发送POST请求
    post_data = {
        'title': '测试标题',
        'body': '测试内容',
        'userId': 1
    }
    response = client.post('/posts', json_data=post_data)
    print(f"状态码: {response['status_code']}")
    print(f"创建的记录: {response['data']}")
    
    print("\n=== 测试PUT请求 ===")
    # 发送PUT请求
    put_data = {
        'id': 1,
        'title': '更新的标题',
        'body': '更新的内容',
        'userId': 1
    }
    response = client.put('/posts/1', json_data=put_data)
    print(f"状态码: {response['status_code']}")
    print(f"更新后的记录: {response['data']}")
    
    print("\n=== 测试DELETE请求 ===")
    # 发送DELETE请求
    response = client.delete('/posts/1')
    print(f"状态码: {response['status_code']}")

if __name__ == "__main__":
    use_api_client()
```

## 8. 安全考虑

### 8.1 安全最佳实践

1. **避免路径遍历攻击**：
   - 检查和过滤用户输入的路径
   - 使用`os.path.normpath`和检查路径前缀

2. **输入验证**：
   - 验证所有用户输入
   - 过滤特殊字符

3. **使用HTTPS**：
   - 对敏感数据使用`HTTPSConnection`
   - 配置SSL证书

4. **Cookie安全**：
   - 设置`Secure`和`HttpOnly`标志
   - 使用`SameSite`属性防止CSRF攻击

5. **认证和授权**：
   - 实现适当的认证机制
   - 验证用户权限

6. **错误处理**：
   - 避免向客户端泄露敏感错误信息
   - 记录详细错误日志供内部使用

### 8.2 示例：安全的文件服务器

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import urllib.parse
import re

def is_safe_path(base_path, user_path):
    """检查路径是否安全（不允许路径遍历）"""
    # 获取规范化的绝对路径
    base_abs = os.path.abspath(base_path)
    user_abs = os.path.abspath(os.path.join(base_abs, user_path))
    
    # 确保用户路径在基础路径之下
    return user_abs.startswith(base_abs)

class SecureFileHandler(SimpleHTTPRequestHandler):
    # 允许访问的文件扩展名
    ALLOWED_EXTENSIONS = {'.html', '.htm', '.css', '.js', '.json', 
                         '.jpg', '.jpeg', '.png', '.gif', '.txt', '.ico'}
    
    # 禁止访问的文件/目录模式
    DISALLOWED_PATTERNS = [
        re.compile(r'^\.'),  # 隐藏文件/目录
        re.compile(r'\.py$'),  # Python脚本
        re.compile(r'\.php$'),  # PHP脚本
        re.compile(r'\.exe$'),  # 可执行文件
    ]
    
    def do_GET(self):
        # 解析路径
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # 检查是否包含路径遍历字符
        if '..' in path:
            self.send_error(403, "Forbidden - Path traversal detected")
            return
        
        # 检查路径安全性
        if not is_safe_path(self.directory, path.lstrip('/')):
            self.send_error(403, "Forbidden - Path outside allowed directory")
            return
        
        # 检查文件扩展名
        _, ext = os.path.splitext(path)
        if ext and ext.lower() not in self.ALLOWED_EXTENSIONS:
            self.send_error(403, f"Forbidden - File type {ext} not allowed")
            return
        
        # 检查是否匹配禁止的模式
        for pattern in self.DISALLOWED_PATTERNS:
            if pattern.search(path):
                self.send_error(403, "Forbidden - Access denied to this resource")
                return
        
        # 添加安全响应头
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        self.send_header('Content-Security-Policy', "default-src 'self'")
        
        # 调用父类的do_GET方法
        super().do_GET()
    
    def log_message(self, format, *args):
        # 增强日志记录，记录IP地址和用户代理
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', '-')
        print(f"[{self.log_date_time_string()}] {client_ip} {args[0]} {args[1]} {args[2]} {user_agent}")

def run_secure_server():
    server_address = ('localhost', 8080)
    
    # 设置服务器目录
    web_dir = os.path.join(os.path.dirname(__file__), 'webroot')
    os.makedirs(web_dir, exist_ok=True)
    
    # 创建自定义处理器类，设置目录
    class CustomHandler(SecureFileHandler):
        directory = web_dir
    
    httpd = HTTPServer(server_address, CustomHandler)
    
    print(f"安全文件服务器运行在 http://{server_address[0]}:{server_address[1]}")
    print(f"网站根目录: {os.path.abspath(web_dir)}")
    print("按Ctrl+C停止服务器")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器关闭")
        httpd.server_close()

if __name__ == "__main__":
    run_secure_server()
```

## 9. 性能优化

### 9.1 基本性能优化技巧

1. **使用多线程/多进程**：
   - 对于并发请求，使用多线程或多进程处理
   - 使用`socketserver.ThreadingMixIn`或`socketserver.ForkingMixIn`

2. **启用HTTP持久连接**：
   - 使用`HTTPConnection(s, timeout=10)`设置合理的超时
   - 在响应头中设置`Connection: keep-alive`

3. **缓存响应**：
   - 为静态资源设置适当的缓存头
   - 实现ETag或Last-Modified机制

4. **压缩响应**：
   - 使用gzip或deflate压缩文本响应
   - 检查客户端是否支持压缩

5. **限制请求大小**：
   - 防止DoS攻击
   - 合理设置最大内容长度

### 9.2 示例：多线程服务器

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socketserver
import os

class ThreadingHTTPServer(socketserver.ThreadingMixIn, HTTPServer):
    """多线程HTTP服务器"""
    # 设置最大线程数
    daemon_threads = True  # 当主线程退出时，所有子线程也退出
    max_threads = 100  # 可以根据需要调整

class OptimizedHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # 启用HTTP/1.1持久连接
        self.send_header('Connection', 'keep-alive')
        # 设置内容压缩（如果客户端支持）
        accept_encoding = self.headers.get('Accept-Encoding', '')
        if 'gzip' in accept_encoding:
            # 这里简化处理，实际实现需要压缩内容
            # self.send_header('Content-Encoding', 'gzip')
            pass
        # 设置缓存控制（对于静态资源）
        if self.path.endswith(('.js', '.css', '.png', '.jpg', '.jpeg', '.gif', '.ico')):
            self.send_header('Cache-Control', 'max-age=3600')  # 1小时
        super().end_headers()
    
    def do_GET(self):
        # 限制请求大小（实际应该在解析请求体时限制）
        content_length = self.headers.get('Content-Length')
        if content_length and int(content_length) > 1048576:  # 1MB限制
            self.send_error(413, "Request Entity Too Large")
            return
        super().do_GET()

def run_threaded_server():
    server_address = ('localhost', 8080)
    
    # 创建多线程服务器
    httpd = ThreadingHTTPServer(server_address, OptimizedHandler)
    
    print(f"多线程服务器运行在 http://{server_address[0]}:{server_address[1]}")
    print("按Ctrl+C停止服务器")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器关闭")
        httpd.server_close()

if __name__ == "__main__":
    run_threaded_server()
```

## 10. 常见问题与解决方案

### 10.1 服务器相关问题

**问题**: 服务器无法启动，提示端口已被占用
**解决方案**:
- 更改端口号
- 终止占用该端口的进程
- 使用`setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`允许端口复用

**问题**: 客户端无法连接到服务器
**解决方案**:
- 检查防火墙设置
- 确认服务器地址和端口是否正确
- 验证服务器是否正在运行
- 检查服务器绑定的IP地址是否为'0.0.0.0'（允许所有接口访问）

**问题**: 处理大文件时内存占用过高
**解决方案**:
- 分块读取和发送文件
- 使用`sendfile()`方法（在支持的系统上）
- 设置合理的缓冲区大小

### 10.2 客户端相关问题

**问题**: 请求超时
**解决方案**:
- 增加超时时间
- 检查网络连接
- 验证服务器是否响应

**问题**: SSL错误
**解决方案**:
- 确保证书有效
- 对于自签名证书，可以临时禁用验证（不推荐用于生产环境）
- 更新SSL库

**问题**: 编码错误
**解决方案**:
- 确保正确设置了Content-Type头
- 使用正确的字符编码进行解码
- 处理二进制数据时避免解码

## 11. 总结

Python的`http`模块提供了丰富的HTTP编程功能，从基本的服务器和客户端实现到Cookie处理和状态码定义。通过这些模块，可以构建各种网络应用，从简单的Web服务器到复杂的API客户端。

主要模块及其功能：

- **http.server**: 提供HTTP服务器实现，用于创建Web服务器
- **http.client**: 提供HTTP客户端实现，用于发送HTTP请求
- **http.cookies**: 处理HTTP cookies的创建和解析
- **http.cookiejar**: 提供高级客户端Cookie管理
- **http.HTTPStatus**: 定义HTTP状态码常量

在实际应用中，对于简单的任务，可以直接使用`http`模块。对于更复杂的应用，可能需要考虑使用更高级的库，如Flask、Django（服务器端）或Requests（客户端）。这些库基于`http`模块构建，但提供了更简洁、更强大的API。

通过合理使用`http`模块及其子模块，可以有效地实现各种网络通信需求，为Python应用添加网络功能。