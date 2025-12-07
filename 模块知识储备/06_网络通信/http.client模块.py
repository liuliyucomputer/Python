# http.client模块详解

http.client是Python中用于处理HTTP请求的标准库，提供了HTTP客户端功能，用于连接HTTP服务器、发送请求和接收响应。

## 模块概述

http.client模块提供了HTTPConnection、HTTPSConnection等类，用于实现HTTP客户端功能，支持以下主要操作：

- 连接HTTP服务器
- 发送HTTP请求（GET、POST、PUT、DELETE等）
- 设置请求头
- 处理请求参数和表单数据
- 接收和解析HTTP响应
- 处理HTTPS连接

## 基本用法

### 发送GET请求

```python
import http.client

def send_get_request():
    """发送GET请求"""
    # 创建HTTP连接
    conn = http.client.HTTPSConnection("api.example.com")
    
    # 发送GET请求
    conn.request("GET", "/users")
    
    # 获取响应
    response = conn.getresponse()
    
    # 打印响应状态码
    print(f"状态码: {response.status}")
    print(f"响应原因: {response.reason}")
    
    # 获取响应头
    print("响应头:")
    for header, value in response.getheaders():
        print(f"  {header}: {value}")
    
    # 获取响应内容
    data = response.read()
    print(f"响应内容: {data.decode('utf-8')}")
    
    # 关闭连接
    conn.close()

# 示例
send_get_request()
```

### 发送POST请求

```python
import http.client
import json

def send_post_request():
    """发送POST请求"""
    # 创建HTTP连接
    conn = http.client.HTTPSConnection("api.example.com")
    
    # 请求参数
    payload = {
        "name": "张三",
        "email": "zhangsan@example.com",
        "age": 30
    }
    
    # 转换为JSON格式
    json_payload = json.dumps(payload)
    
    # 设置请求头
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_access_token"
    }
    
    # 发送POST请求
    conn.request("POST", "/users", body=json_payload, headers=headers)
    
    # 获取响应
    response = conn.getresponse()
    
    # 打印响应信息
    print(f"状态码: {response.status}")
    print(f"响应原因: {response.reason}")
    
    # 获取响应内容
    data = response.read()
    print(f"响应内容: {data.decode('utf-8')}")
    
    # 关闭连接
    conn.close()

# 示例
send_post_request()
```

### 使用上下文管理器

```python
import http.client

def send_request_with_context():
    """使用上下文管理器发送请求"""
    # 使用with语句自动关闭连接
    with http.client.HTTPSConnection("api.example.com") as conn:
        # 发送GET请求
        conn.request("GET", "/users")
        
        # 获取响应
        response = conn.getresponse()
        
        # 打印响应信息
        print(f"状态码: {response.status}")
        print(f"响应内容: {response.read().decode('utf-8')}")

# 示例
send_request_with_context()
```

## 高级功能

### 设置请求头

```python
import http.client

def set_request_headers():
    """设置请求头"""
    with http.client.HTTPSConnection("api.example.com") as conn:
        # 设置多种请求头
        headers = {
            "User-Agent": "Python-http.client/3.7",
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer your_access_token",
            "X-Custom-Header": "custom-value"
        }
        
        # 发送请求
        conn.request("GET", "/users", headers=headers)
        
        # 获取响应
        response = conn.getresponse()
        print(f"状态码: {response.status}")
        print(f"响应内容: {response.read().decode('utf-8')}")

# 示例
set_request_headers()
```

### 发送表单数据

```python
import http.client
import urllib.parse

def send_form_data():
    """发送表单数据"""
    with http.client.HTTPSConnection("api.example.com") as conn:
        # 表单数据
        form_data = {
            "username": "zhangsan",
            "password": "123456",
            "remember": "true"
        }
        
        # 编码表单数据
        encoded_data = urllib.parse.urlencode(form_data)
        
        # 设置请求头
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        # 发送POST请求
        conn.request("POST", "/login", body=encoded_data, headers=headers)
        
        # 获取响应
        response = conn.getresponse()
        print(f"状态码: {response.status}")
        print(f"响应内容: {response.read().decode('utf-8')}")

# 示例
send_form_data()
```

### 发送文件

```python
import http.client
import os
import mimetypes

def send_file():
    """发送文件"""
    # 文件路径
    file_path = "test.txt"
    file_name = os.path.basename(file_path)
    
    # 读取文件内容
    with open(file_path, "rb") as f:
        file_content = f.read()
    
    # 设置请求头
    content_type, encoding = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = "application/octet-stream"
    
    headers = {
        "Content-Type": content_type,
        "Content-Disposition": f"attachment; filename={file_name}"
    }
    
    # 发送POST请求
    with http.client.HTTPSConnection("api.example.com") as conn:
        conn.request("POST", "/upload", body=file_content, headers=headers)
        
        # 获取响应
        response = conn.getresponse()
        print(f"状态码: {response.status}")
        print(f"响应内容: {response.read().decode('utf-8')}")

# 示例
send_file()
```

### 发送多部分表单数据

```python
import http.client
import os
import mimetypes

def send_multipart_form_data():
    """发送多部分表单数据"""
    # 边界字符串
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    
    # 文件路径
    file_path = "test.txt"
    file_name = os.path.basename(file_path)
    
    # 表单字段
    fields = {
        "username": "zhangsan",
        "email": "zhangsan@example.com"
    }
    
    # 构建请求体
    body = []
    
    # 添加表单字段
    for field_name, field_value in fields.items():
        body.append(f"--{boundary}")
        body.append(f"Content-Disposition: form-data; name=\"{field_name}\"")
        body.append("")
        body.append(field_value)
    
    # 添加文件
    content_type, encoding = mimetypes.guess_type(file_path)
    if content_type is None:
        content_type = "application/octet-stream"
    
    body.append(f"--{boundary}")
    body.append(f"Content-Disposition: form-data; name=\"file\"; filename=\"{file_name}\"")
    body.append(f"Content-Type: {content_type}")
    body.append("")
    
    # 读取文件内容
    with open(file_path, "rb") as f:
        file_content = f.read()
    
    # 合并请求体
    body_bytes = "\r\n".join(body).encode("utf-8")
    body_bytes += b"\r\n"
    body_bytes += file_content
    body_bytes += b"\r\n--" + boundary.encode("utf-8") + b"--\r\n"
    
    # 设置请求头
    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Content-Length": str(len(body_bytes))
    }
    
    # 发送POST请求
    with http.client.HTTPSConnection("api.example.com") as conn:
        conn.request("POST", "/upload", body=body_bytes, headers=headers)
        
        # 获取响应
        response = conn.getresponse()
        print(f"状态码: {response.status}")
        print(f"响应内容: {response.read().decode('utf-8')}")

# 示例
send_multipart_form_data()
```

### 处理响应

```python
import http.client

def handle_response():
    """处理响应"""
    with http.client.HTTPSConnection("api.example.com") as conn:
        # 发送GET请求
        conn.request("GET", "/users")
        
        # 获取响应
        response = conn.getresponse()
        
        # 获取响应状态码
        print(f"状态码: {response.status}")
        
        # 获取响应原因
        print(f"响应原因: {response.reason}")
        
        # 获取响应头
        print("响应头:")
        for header, value in response.getheaders():
            print(f"  {header}: {value}")
        
        # 获取特定响应头
        content_type = response.getheader("Content-Type")
        print(f"\nContent-Type: {content_type}")
        
        # 获取响应版本
        print(f"HTTP版本: {response.version}")
        
        # 获取响应内容
        content_length = response.getheader("Content-Length")
        if content_length:
            # 按指定长度读取
            data = response.read(int(content_length))
        else:
            # 读取所有内容
            data = response.read()
        
        print(f"响应内容: {data.decode('utf-8')}")

# 示例
handle_response()
```

### 发送其他HTTP方法请求

```python
import http.client
import json

def send_http_methods():
    """发送其他HTTP方法请求"""
    with http.client.HTTPSConnection("api.example.com") as conn:
        # 发送PUT请求
        put_data = {"name": "李四", "email": "lisi@example.com"}
        conn.request("PUT", "/users/1", body=json.dumps(put_data), headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        print(f"PUT请求状态码: {response.status}")
        response.read()  # 消耗响应内容
        
        # 发送DELETE请求
        conn.request("DELETE", "/users/1")
        response = conn.getresponse()
        print(f"DELETE请求状态码: {response.status}")
        response.read()
        
        # 发送PATCH请求
        patch_data = {"email": "updated@example.com"}
        conn.request("PATCH", "/users/1", body=json.dumps(patch_data), headers={"Content-Type": "application/json"})
        response = conn.getresponse()
        print(f"PATCH请求状态码: {response.status}")
        response.read()

# 示例
send_http_methods()
```

## 错误处理

```python
import http.client
import socket

def handle_errors():
    """处理错误"""
    try:
        with http.client.HTTPSConnection("api.example.com", timeout=5) as conn:
            conn.request("GET", "/nonexistent")
            response = conn.getresponse()
            
            # 处理不同状态码
            if response.status == 200:
                print("请求成功")
            elif response.status == 404:
                print("资源不存在")
            elif response.status == 500:
                print("服务器内部错误")
            else:
                print(f"请求失败，状态码: {response.status}")
                
            print(f"响应内容: {response.read().decode('utf-8')}")
            
    except http.client.HTTPException as e:
        print(f"HTTP异常: {e}")
    except socket.timeout as e:
        print(f"连接超时: {e}")
    except socket.error as e:
        print(f"Socket错误: {e}")
    except Exception as e:
        print(f"其他异常: {e}")

# 示例
handle_errors()
```

## 实际应用示例

### 示例1：调用天气API

```python
import http.client
import json

def get_weather(city):
    """调用天气API获取天气信息"""
    # API配置
    api_key = "your_api_key"
    
    with http.client.HTTPSConnection("api.weatherapi.com") as conn:
        # 构建请求URL
        url = f"/v1/current.json?key={api_key}&q={city}&aqi=no"
        
        # 发送GET请求
        conn.request("GET", url)
        
        # 获取响应
        response = conn.getresponse()
        
        if response.status == 200:
            # 解析JSON响应
            data = json.loads(response.read().decode("utf-8"))
            
            # 提取天气信息
            location = data["location"]["name"]
            country = data["location"]["country"]
            temp_c = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            wind_kph = data["current"]["wind_kph"]
            humidity = data["current"]["humidity"]
            
            # 打印天气信息
            print(f"城市: {location}, {country}")
            print(f"温度: {temp_c}°C")
            print(f"天气: {condition}")
            print(f"风速: {wind_kph} km/h")
            print(f"湿度: {humidity}%")
            
            return data
        else:
            print(f"请求失败，状态码: {response.status}")
            return None

# 示例
weather_data = get_weather("Beijing")
if weather_data:
    print("天气信息获取成功")
```

### 示例2：调用GitHub API

```python
import http.client
import json

def get_github_user(username):
    """调用GitHub API获取用户信息"""
    with http.client.HTTPSConnection("api.github.com") as conn:
        # 设置请求头
        headers = {
            "User-Agent": "Python-http.client/3.7",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # 构建请求URL
        url = f"/users/{username}"
        
        # 发送GET请求
        conn.request("GET", url, headers=headers)
        
        # 获取响应
        response = conn.getresponse()
        
        if response.status == 200:
            # 解析JSON响应
            user_data = json.loads(response.read().decode("utf-8"))
            
            # 提取用户信息
            print(f"用户名: {user_data['login']}")
            print(f"姓名: {user_data.get('name', '未知')}")
            print(f"公司: {user_data.get('company', '未知')}")
            print(f"位置: {user_data.get('location', '未知')}")
            print(f"邮箱: {user_data.get('email', '未知')}")
            print(f"博客: {user_data.get('blog', '未知')}")
            print(f"关注者: {user_data['followers']}")
            print(f"关注: {user_data['following']}")
            print(f"仓库数量: {user_data['public_repos']}")
            print(f"创建时间: {user_data['created_at']}")
            
            return user_data
        elif response.status == 404:
            print(f"用户 {username} 不存在")
            return None
        else:
            print(f"请求失败，状态码: {response.status}")
            return None

# 示例
user_data = get_github_user("octocat")
if user_data:
    print("GitHub用户信息获取成功")
```

### 示例3：创建REST API客户端

```python
import http.client
import json
import urllib.parse

class APIClient:
    def __init__(self, base_url, api_key=None, timeout=30):
        """初始化API客户端"""
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        
        # 解析base_url
        if base_url.startswith("https://"):
            self.host = base_url[8:]
            self.is_https = True
        elif base_url.startswith("http://"):
            self.host = base_url[7:]
            self.is_https = False
        else:
            self.host = base_url
            self.is_https = True
    
    def _get_connection(self):
        """获取HTTP连接"""
        if self.is_https:
            return http.client.HTTPSConnection(self.host, timeout=self.timeout)
        else:
            return http.client.HTTPConnection(self.host, timeout=self.timeout)
    
    def _build_headers(self, custom_headers=None):
        """构建请求头"""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        # 添加API密钥
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        # 添加自定义请求头
        if custom_headers:
            headers.update(custom_headers)
        
        return headers
    
    def get(self, path, params=None):
        """发送GET请求"""
        # 构建请求URL
        if params:
            path += "?" + urllib.parse.urlencode(params)
        
        with self._get_connection() as conn:
            # 发送请求
            conn.request("GET", path, headers=self._build_headers())
            
            # 获取响应
            response = conn.getresponse()
            
            # 解析响应
            return self._parse_response(response)
    
    def post(self, path, data=None):
        """发送POST请求"""
        with self._get_connection() as conn:
            # 转换请求数据
            body = json.dumps(data) if data else None
            
            # 发送请求
            conn.request("POST", path, body=body, headers=self._build_headers())
            
            # 获取响应
            response = conn.getresponse()
            
            # 解析响应
            return self._parse_response(response)
    
    def put(self, path, data=None):
        """发送PUT请求"""
        with self._get_connection() as conn:
            # 转换请求数据
            body = json.dumps(data) if data else None
            
            # 发送请求
            conn.request("PUT", path, body=body, headers=self._build_headers())
            
            # 获取响应
            response = conn.getresponse()
            
            # 解析响应
            return self._parse_response(response)
    
    def delete(self, path):
        """发送DELETE请求"""
        with self._get_connection() as conn:
            # 发送请求
            conn.request("DELETE", path, headers=self._build_headers())
            
            # 获取响应
            response = conn.getresponse()
            
            # 解析响应
            return self._parse_response(response)
    
    def _parse_response(self, response):
        """解析响应"""
        # 获取响应内容
        content = response.read().decode("utf-8")
        
        # 解析JSON响应
        try:
            data = json.loads(content)
        except json.JSONDecodeError:
            data = content
        
        return {
            "status": response.status,
            "reason": response.reason,
            "headers": dict(response.getheaders()),
            "data": data
        }

# 使用示例
if __name__ == "__main__":
    # 创建API客户端
    client = APIClient("https://jsonplaceholder.typicode.com")
    
    # 发送GET请求
    response = client.get("/users")
    print(f"GET请求状态码: {response['status']}")
    print(f"GET请求响应: {response['data'][:2]}")  # 只显示前两个用户
    
    # 发送POST请求
    new_user = {
        "name": "张三",
        "username": "zhangsan",
        "email": "zhangsan@example.com"
    }
    response = client.post("/users", data=new_user)
    print(f"\nPOST请求状态码: {response['status']}")
    print(f"POST请求响应: {response['data']}")
    
    # 发送PUT请求
    updated_user = {
        "name": "李四",
        "email": "lisi@example.com"
    }
    response = client.put("/users/1", data=updated_user)
    print(f"\nPUT请求状态码: {response['status']}")
    print(f"PUT请求响应: {response['data']}")
    
    # 发送DELETE请求
    response = client.delete("/users/1")
    print(f"\nDELETE请求状态码: {response['status']}")
    print(f"DELETE请求响应: {response['data']}")
```

## 最佳实践

1. **使用HTTPS**：优先使用HTTPS连接，提高通信安全性
2. **处理异常**：捕获并处理HTTPException、socket.timeout等异常
3. **设置超时**：设置合理的超时时间，避免无限等待
4. **关闭连接**：使用with语句自动关闭连接
5. **设置请求头**：根据API要求设置合适的请求头
6. **处理响应**：根据响应状态码处理不同情况
7. **解析JSON**：使用json.loads解析JSON响应
8. **避免硬编码**：从配置文件或环境变量读取API密钥等敏感信息
9. **限制请求频率**：遵守API的请求频率限制
10. **使用代理**：根据需要设置HTTP代理

## 与其他模块的关系

- **urllib.request**：提供更高级的HTTP请求API
- **requests**：第三方库，提供更简洁的HTTP请求API
- **http.server**：用于创建HTTP服务器
- **json**：用于解析JSON响应
- **urllib.parse**：用于解析和构建URL

## 总结

http.client模块是Python中用于实现HTTP客户端功能的标准库，支持连接HTTP服务器、发送各种HTTP请求、设置请求头、处理请求数据和接收响应。通过HTTPSConnection类，可以安全地连接HTTPS服务器。

在实际应用中，http.client模块可以用于调用REST API、访问Web服务、创建网络爬虫等。对于更复杂的HTTP请求需求，可以考虑使用requests等第三方库，它们提供了更简洁易用的API。