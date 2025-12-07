# http模块详解

http模块是Python中用于处理HTTP协议的标准库，提供了HTTP客户端和服务器功能，包括http.client、http.server、http.cookies等子模块。

## 模块概述

http模块包含以下主要子模块：

- **http.client**：HTTP客户端功能，用于发送HTTP请求
- **http.server**：HTTP服务器功能，用于创建简单的HTTP服务器
- **http.cookies**：处理HTTP cookies
- **http.cookiejar**：管理HTTP cookies的存储和使用
- **http.auth**：HTTP认证功能
- **http.HTTPStatus**：HTTP状态码常量

## http.client子模块

http.client子模块提供了HTTP客户端功能，用于发送HTTP请求。

### 基本用法

```python
import http.client

# 创建HTTP连接
conn = http.client.HTTPSConnection("www.example.com")

# 发送GET请求
conn.request("GET", "/")

# 获取响应
response = conn.getresponse()

# 打印响应状态和头信息
print(f"状态码: {response.status}")
print(f"响应头: {response.getheaders()}")

# 读取响应内容
content = response.read()
print(f"响应内容: {content.decode('utf-8')}")

# 关闭连接
conn.close()
```

### 发送POST请求

```python
import http.client
import json

# 创建HTTPS连接
conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

# 准备POST数据
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
headers = {
    "Content-type": "application/json"
}

# 发送POST请求
conn.request("POST", "/posts", json.dumps(payload), headers)

# 获取响应
response = conn.getresponse()
print(f"状态码: {response.status}")
print(f"响应内容: {response.read().decode('utf-8')}")

# 关闭连接
conn.close()
```

### 发送带参数的请求

```python
import http.client
import urllib.parse

# 创建HTTP连接
conn = http.client.HTTPConnection("httpbin.org")

# 准备查询参数
params = urllib.parse.urlencode({"name": "Python", "version": 3.8})

# 发送请求
conn.request("GET", f"/get?{params}")

# 获取响应
response = conn.getresponse()
print(f"状态码: {response.status}")
print(f"响应内容: {response.read().decode('utf-8')}")

# 关闭连接
conn.close()
```

## http.server子模块

http.server子模块提供了HTTP服务器功能，用于创建简单的HTTP服务器。

### 创建基本HTTP服务器

```python
import http.server
import socketserver

# 定义端口
PORT = 8000

# 创建服务器
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"服务器正在运行，端口 {PORT}")
    print(f"访问地址: http://localhost:{PORT}")
    httpd.serve_forever()
```

### 创建自定义HTTP服务器

```python
import http.server
import socketserver

# 自定义请求处理器
class MyHandler(http.server.BaseHTTPRequestHandler):
    # 处理GET请求
    def do_GET(self):
        # 设置响应状态码
        self.send_response(200)
        
        # 设置响应头
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # 发送响应内容
        response = f"""
        <html>
        <head><title>自定义HTTP服务器</title></head>
        <body>
        <h1>Hello, World!</h1>
        <p>请求路径: {self.path}</p>
        <p>客户端地址: {self.client_address[0]}</p>
        <p>请求方法: {self.command}</p>
        </body>
        </html>
        """
        self.wfile.write(response.encode("utf-8"))
    
    # 处理POST请求
    def do_POST(self):
        # 获取请求体长度
        content_length = int(self.headers['Content-Length'])
        
        # 读取请求体
        post_data = self.rfile.read(content_length)
        
        # 设置响应状态码
        self.send_response(200)
        
        # 设置响应头
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # 发送响应内容
        response = f"""
        <html>
        <head><title>POST请求处理</title></head>
        <body>
        <h1>POST请求已接收</h1>
        <p>请求路径: {self.path}</p>
        <p>请求体: {post_data.decode('utf-8')}</p>
        </body>
        </html>
        """
        self.wfile.write(response.encode("utf-8"))

# 定义端口
PORT = 8001

# 创建服务器
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"自定义服务器正在运行，端口 {PORT}")
    print(f"访问地址: http://localhost:{PORT}")
    httpd.serve_forever()
```

### 创建多线程HTTP服务器

```python
import http.server
import socketserver
import threading

# 定义端口
PORT = 8002

# 创建多线程服务器
Handler = http.server.SimpleHTTPRequestHandler

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

with ThreadedTCPServer(("", PORT), Handler) as httpd:
    print(f"多线程服务器正在运行，端口 {PORT}")
    print(f"访问地址: http://localhost:{PORT}")
    httpd.serve_forever()
```

## http.cookies子模块

http.cookies子模块用于处理HTTP cookies。

### 基本用法

```python
import http.cookies

# 创建Cookie
cookie = http.cookies.SimpleCookie()

# 添加Cookie项
cookie["name"] = "Python"
cookie["version"] = "3.8"
cookie["expires"] = "Fri, 31-Dec-2025 23:59:59 GMT"

# 设置Cookie属性
cookie["name"]["path"] = "/"
cookie["name"]["secure"] = "True"
cookie["name"]["httponly"] = "True"

# 生成Set-Cookie头
print("Set-Cookie头:")
print(cookie.output())

# 解析Cookie头
cookie_string = "name=Python; version=3.8; expires=Fri, 31-Dec-2025 23:59:59 GMT"
cookie = http.cookies.SimpleCookie(cookie_string)

# 获取Cookie值
print(f"\n解析后的Cookie:")
for key, morsel in cookie.items():
    print(f"{key}: {morsel.value}")
    print(f"  Path: {morsel['path']}")
    print(f"  Secure: {morsel['secure']}")
    print(f"  HttpOnly: {morsel['httponly']}")
```

## http.cookiejar子模块

http.cookiejar子模块用于管理HTTP cookies的存储和使用。

### 基本用法

```python
import http.cookiejar
import urllib.request

# 创建CookieJar
cookie_jar = http.cookiejar.CookieJar()

# 创建opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

# 发送请求
response = opener.open("http://www.example.com")

# 查看Cookie
print("收到的Cookie:")
for cookie in cookie_jar:
    print(f"{cookie.name}={cookie.value}")
    print(f"  Domain: {cookie.domain}")
    print(f"  Path: {cookie.path}")
    print(f"  Expires: {cookie.expires}")
```

### 保存和加载Cookie

```python
import http.cookiejar
import urllib.request

# 创建FileCookieJar
cookie_jar = http.cookiejar.MozillaCookieJar("cookies.txt")

# 创建opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))

# 发送请求
response = opener.open("http://www.example.com")

# 保存Cookie到文件
cookie_jar.save()
print("Cookie已保存到cookies.txt")

# 加载Cookie
new_cookie_jar = http.cookiejar.MozillaCookieJar()
new_cookie_jar.load("cookies.txt")
print("\n从文件加载的Cookie:")
for cookie in new_cookie_jar:
    print(f"{cookie.name}={cookie.value}")
```

## http.HTTPStatus子模块

http.HTTPStatus子模块提供了HTTP状态码常量。

### 基本用法

```python
import http.HTTPStatus

# 打印所有HTTP状态码
print("HTTP状态码:")
for status in http.HTTPStatus:
    print(f"{status.value} {status.phrase}: {status.description}")

# 检查状态码类型
print(f"\n状态码200是否是成功: {http.HTTPStatus.OK.value == 200}")
print(f"状态码404是否是客户端错误: {400 <= http.HTTPStatus.NOT_FOUND.value < 500}")
print(f"状态码500是否是服务器错误: {500 <= http.HTTPStatus.INTERNAL_SERVER_ERROR.value < 600}")
```

## 实际应用示例

### 示例1：简单的Web API客户端

```python
import http.client
import json

class GitHubAPI:
    def __init__(self):
        self.conn = http.client.HTTPSConnection("api.github.com")
        self.headers = {
            "User-Agent": "Python-http.client"
        }
    
    def get_user(self, username):
        """获取GitHub用户信息"""
        self.conn.request("GET", f"/users/{username}", headers=self.headers)
        response = self.conn.getresponse()
        
        if response.status == 200:
            return json.loads(response.read().decode("utf-8"))
        else:
            return {
                "error": True,
                "status": response.status,
                "message": response.read().decode("utf-8")
            }
    
    def get_repos(self, username):
        """获取GitHub用户的仓库列表"""
        self.conn.request("GET", f"/users/{username}/repos", headers=self.headers)
        response = self.conn.getresponse()
        
        if response.status == 200:
            return json.loads(response.read().decode("utf-8"))
        else:
            return {
                "error": True,
                "status": response.status,
                "message": response.read().decode("utf-8")
            }
    
    def close(self):
        """关闭连接"""
        self.conn.close()

# 使用示例
github = GitHubAPI()

# 获取用户信息
user = github.get_user("octocat")
if "error" not in user:
    print(f"用户名: {user['login']}")
    print(f"姓名: {user['name']}")
    print(f"仓库数量: {user['public_repos']}")
    print(f"关注者: {user['followers']}")
    print(f"位置: {user['location']}")

# 获取仓库列表
repos = github.get_repos("octocat")
if "error" not in repos:
    print(f"\n仓库列表 ({len(repos)}个):")
    for repo in repos[:5]:  # 只显示前5个
        print(f"- {repo['name']}: {repo['description']}")

# 关闭连接
github.close()
```

### 示例2：文件下载服务器

```python
import http.server
import socketserver
import os

class FileDownloadHandler(http.server.SimpleHTTPRequestHandler):
    def list_directory(self, path):
        """自定义目录列表"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        response = f"""
        <html>
        <head><title>文件下载服务器</title></head>
        <body>
        <h1>文件下载服务器</h1>
        <p>当前目录: {path}</p>
        <ul>
        """
        
        try:
            entries = os.listdir(path)
        except OSError:
            self.send_error(404, "No permission to list directory")
            return None
        
        for name in entries:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            
            response += f"<li><a href='{linkname}'>{displayname}</a></li>"
        
        response += """
        </ul>
        </body>
        </html>
        """
        
        self.wfile.write(response.encode("utf-8"))
        return None

# 定义端口
PORT = 8003

# 设置当前目录为服务器根目录
os.chdir(".")

# 创建服务器
with socketserver.TCPServer(("", PORT), FileDownloadHandler) as httpd:
    print(f"文件下载服务器正在运行，端口 {PORT}")
    print(f"访问地址: http://localhost:{PORT}")
    print(f"服务器根目录: {os.getcwd()}")
    httpd.serve_forever()
```

### 示例3：API服务器

```python
import http.server
import socketserver
import json
import http.HTTPStatus

class APIServer(http.server.BaseHTTPRequestHandler):
    # 模拟数据
    books = [
        {"id": 1, "title": "Python编程", "author": "张三", "price": 59.9},
        {"id": 2, "title": "Java编程", "author": "李四", "price": 69.9},
        {"id": 3, "title": "C++编程", "author": "王五", "price": 79.9}
    ]
    
    def _send_response(self, status, data):
        """发送JSON响应"""
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    def do_GET(self):
        """处理GET请求"""
        if self.path == "/books":
            # 获取所有书籍
            self._send_response(http.HTTPStatus.OK, {"books": self.books})
        elif self.path.startswith("/books/"):
            # 获取单本书籍
            try:
                book_id = int(self.path.split("/")[-1])
                book = next((b for b in self.books if b["id"] == book_id), None)
                if book:
                    self._send_response(http.HTTPStatus.OK, {"book": book})
                else:
                    self._send_response(http.HTTPStatus.NOT_FOUND, {"error": "Book not found"})
            except ValueError:
                self._send_response(http.HTTPStatus.BAD_REQUEST, {"error": "Invalid book ID"})
        else:
            self._send_response(http.HTTPStatus.NOT_FOUND, {"error": "Not found"})
    
    def do_POST(self):
        """处理POST请求"""
        if self.path == "/books":
            # 创建新书籍
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length).decode("utf-8"))
            
            # 验证数据
            if "title" not in post_data or "author" not in post_data:
                self._send_response(http.HTTPStatus.BAD_REQUEST, {"error": "Title and author are required"})
                return
            
            # 创建新书籍
            new_id = max(b["id"] for b in self.books) + 1
            new_book = {
                "id": new_id,
                "title": post_data["title"],
                "author": post_data["author"],
                "price": post_data.get("price", 0.0)
            }
            self.books.append(new_book)
            
            self._send_response(http.HTTPStatus.CREATED, {"book": new_book})
        else:
            self._send_response(http.HTTPStatus.NOT_FOUND, {"error": "Not found"})
    
    def do_PUT(self):
        """处理PUT请求"""
        if self.path.startswith("/books/"):
            # 更新书籍
            try:
                book_id = int(self.path.split("/")[-1])
                book_index = next((i for i, b in enumerate(self.books) if b["id"] == book_id), None)
                
                if book_index is None:
                    self._send_response(http.HTTPStatus.NOT_FOUND, {"error": "Book not found"})
                    return
                
                # 读取请求体
                content_length = int(self.headers['Content-Length'])
                put_data = json.loads(self.rfile.read(content_length).decode("utf-8"))
                
                # 更新书籍
                self.books[book_index].update(put_data)
                
                self._send_response(http.HTTPStatus.OK, {"book": self.books[book_index]})
            except ValueError:
                self._send_response(http.HTTPStatus.BAD_REQUEST, {"error": "Invalid book ID"})
        else:
            self._send_response(http.HTTPStatus.NOT_FOUND, {"error": "Not found"})
    
    def do_DELETE(self):
        """处理DELETE请求"""
        if self.path.startswith("/books/"):
            # 删除书籍
            try:
                book_id = int(self.path.split("/")[-1])
                book_index = next((i for i, b in enumerate(self.books) if b["id"] == book_id), None)
                
                if book_index is None:
                    self._send_response(http.HTTPStatus.NOT_FOUND, {"error": "Book not found"})
                    return
                
                # 删除书籍
                deleted_book = self.books.pop(book_index)
                
                self._send_response(http.HTTPStatus.OK, {"message": "Book deleted", "book": deleted_book})
            except ValueError:
                self._send_response(http.HTTPStatus.BAD_REQUEST, {"error": "Invalid book ID"})
        else:
            self._send_response(http.HTTPStatus.NOT_FOUND, {"error": "Not found"})

# 定义端口
PORT = 8004

# 创建服务器
with socketserver.TCPServer(("", PORT), APIServer) as httpd:
    print(f"API服务器正在运行，端口 {PORT}")
    print(f"访问地址: http://localhost:{PORT}")
    print("API端点:")
    print("  GET    /books          - 获取所有书籍")
    print("  GET    /books/:id      - 获取单本书籍")
    print("  POST   /books          - 创建新书籍")
    print("  PUT    /books/:id      - 更新书籍")
    print("  DELETE /books/:id      - 删除书籍")
    httpd.serve_forever()
```

## 最佳实践

1. **使用HTTPS**：尽量使用HTTPS连接，提高通信安全性
2. **处理异常**：捕获并处理网络异常和HTTP错误
3. **设置超时**：为HTTP请求设置超时时间，避免无限期阻塞
4. **使用上下文管理器**：使用`with`语句自动关闭连接
5. **验证输入**：对用户输入进行验证，避免安全问题
6. **使用JSON格式**：在API中使用JSON格式，提高数据交换效率
7. **设置合适的Content-Type**：根据请求体类型设置正确的Content-Type头

## 与其他模块的关系

- **urllib.request**：基于http.client，提供更高级的HTTP客户端功能
- **requests**：第三方库，提供更简洁的HTTP客户端API
- **Flask/Django**：第三方Web框架，提供更强大的HTTP服务器功能

## 总结

http模块是Python中处理HTTP协议的标准库，提供了HTTP客户端和服务器功能。通过http.client可以发送HTTP请求，通过http.server可以创建简单的HTTP服务器。http.cookies和http.cookiejar模块用于处理和管理HTTP cookies。

在实际应用中，http模块可以用于创建简单的API服务器、文件下载服务器、Web客户端等。对于更复杂的Web应用，可以考虑使用Flask、Django等第三方Web框架。