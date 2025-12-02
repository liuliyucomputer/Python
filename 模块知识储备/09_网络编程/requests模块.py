# requests模块 - Python HTTP客户端的优雅之选

Python的`requests`模块是一个功能强大且优雅的HTTP客户端库，它建立在Python的urllib3库之上，提供了更加人性化和简洁的API。本文档将详细介绍requests模块的核心功能、使用方法、高级特性以及实际应用案例。

> 注意：requests不是Python标准库，需要单独安装：`pip install requests`

## 1. 模块概述

requests模块提供了以下主要功能：

- 发送HTTP/HTTPS请求（GET、POST、PUT、DELETE等）
- 处理Cookies和会话管理
- 支持文件上传和下载
- 提供简单的身份验证机制
- 自动处理URL编码和重定向
- 优雅的响应内容处理（JSON、二进制数据等）
- 灵活的请求头设置和自定义配置

## 2. 基本请求

### 2.1 发送GET请求

```python
import requests

# 基本GET请求
response = requests.get('https://httpbin.org/get')

# 查看响应状态码
print(f"状态码: {response.status_code}")

# 查看响应内容（字符串形式）
print(f"响应内容: {response.text}")

# 查看响应内容（二进制形式）
print(f"响应内容（二进制）: {response.content[:100]}...")  # 只显示前100个字节

# 查看响应头
print(f"响应头: {dict(response.headers)}")

# 检查请求是否成功
if response.ok:
    print("请求成功")
else:
    print("请求失败")
```

### 2.2 发送带参数的GET请求

```python
import requests

# 方法1：直接在URL中添加参数
response1 = requests.get('https://httpbin.org/get?name=张三&age=25')
print("响应URL:", response1.url)
print("响应内容:", response1.text)

# 方法2：使用params参数（推荐）
payload = {'name': '张三', 'age': 25, 'hobbies': ['reading', 'swimming']}
response2 = requests.get('https://httpbin.org/get', params=payload)
print("\n响应URL:", response2.url)
print("响应内容:", response2.text)
```

### 2.3 发送POST请求

```python
import requests

# 方法1：表单数据（application/x-www-form-urlencoded）
payload = {'username': 'testuser', 'password': 'testpass', 'remember': True}
response1 = requests.post('https://httpbin.org/post', data=payload)
print("表单数据响应:", response1.text)

# 方法2：JSON数据（application/json）
import json
json_payload = {'name': 'John', 'age': 30, 'city': 'New York'}

# 方式1：手动转换为JSON字符串
response2 = requests.post('https://httpbin.org/post', 
                          data=json.dumps(json_payload),
                          headers={'Content-Type': 'application/json'})

# 方式2：使用json参数（推荐，自动处理Content-Type头）
response3 = requests.post('https://httpbin.org/post', json=json_payload)

print("\nJSON数据响应:", response3.text)
print("Content-Type:", response3.headers.get('Content-Type'))
```

### 2.4 其他HTTP方法

```python
import requests

# PUT请求
put_response = requests.put('https://httpbin.org/put', json={'key': 'value'})
print("PUT请求状态码:", put_response.status_code)

# DELETE请求
delete_response = requests.delete('https://httpbin.org/delete')
print("DELETE请求状态码:", delete_response.status_code)

# PATCH请求
patch_response = requests.patch('https://httpbin.org/patch', json={'partial': 'update'})
print("PATCH请求状态码:", patch_response.status_code)

# HEAD请求（只获取响应头，不获取响应体）
head_response = requests.head('https://httpbin.org/get')
print("\nHEAD请求响应头:", dict(head_response.headers))
print("响应体长度:", len(head_response.content))  # 应为0

# OPTIONS请求（获取服务器支持的HTTP方法）
options_response = requests.options('https://httpbin.org/')
print("\n允许的HTTP方法:", options_response.headers.get('Allow'))
```

## 3. 定制请求

### 3.1 设置请求头

```python
import requests

# 创建自定义请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://www.example.com',
    'X-Custom-Header': 'CustomValue'
}

# 发送带自定义请求头的请求
response = requests.get('https://httpbin.org/headers', headers=headers)

print("请求头:", dict(response.json()['headers']))
```

### 3.2 设置超时

```python
import requests
import time

def test_timeout():
    # 设置超时（秒）
    try:
        # 设置总超时
        response = requests.get('https://httpbin.org/delay/3', timeout=2)
        print("请求成功")
    except requests.exceptions.Timeout:
        print("请求超时")
    
    # 分别设置连接超时和读取超时
    try:
        # 第一个参数是连接超时，第二个是读取超时
        response = requests.get('https://httpbin.org/delay/3', timeout=(1, 2))
        print("请求成功")
    except requests.exceptions.Timeout as e:
        print(f"请求超时: {e}")
    
    # 不设置超时（不推荐）
    # response = requests.get('https://httpbin.org/delay/3')  # 可能会一直等待

if __name__ == "__main__":
    test_timeout()
```

### 3.3 设置代理

```python
import requests

def test_proxies():
    # 基本代理设置
    proxies = {
        'http': 'http://proxy.example.com:8080',
        'https': 'https://proxy.example.com:8080'
    }
    
    try:
        # 使用代理发送请求
        # 注意：这个示例中的代理地址是虚构的，需要替换为实际的代理服务器地址
        # response = requests.get('https://httpbin.org/ip', proxies=proxies)
        # print("代理IP:", response.text)
        print("代理配置示例: 请替换为实际的代理服务器地址")
    except Exception as e:
        print(f"代理错误: {e}")
    
    # 带认证的代理
    proxies_with_auth = {
        'http': 'http://user:pass@proxy.example.com:8080',
        'https': 'https://user:pass@proxy.example.com:8080'
    }
    
    # 也可以使用HTTPProxyAuth类
    from requests.auth import HTTPProxyAuth
    auth = HTTPProxyAuth('user', 'pass')
    # response = requests.get('https://httpbin.org/ip', proxies=proxies, auth=auth)
    
    # SOCKS代理（需要安装：pip install requests[socks]）
    try:
        socks_proxies = {
            'http': 'socks5://user:pass@proxy.example.com:1080',
            'https': 'socks5://user:pass@proxy.example.com:1080'
        }
        print("SOCKS代理配置示例")
    except Exception as e:
        print(f"SOCKS代理错误: {e}")

if __name__ == "__main__":
    test_proxies()
```

### 3.4 禁用SSL验证

```python
import requests

def test_ssl_verification():
    # 默认情况下，requests会验证SSL证书
    try:
        # 这个URL使用的是自签名证书，默认会失败
        # response = requests.get('https://expired.badssl.com/')
        print("默认情况下会验证SSL证书")
    except requests.exceptions.SSLError as e:
        print(f"SSL验证错误: {e}")
    
    # 禁用SSL验证（不推荐在生产环境中使用）
    try:
        # response = requests.get('https://expired.badssl.com/', verify=False)
        print("禁用SSL验证示例")
    except Exception as e:
        print(f"错误: {e}")
    
    # 提供自定义CA证书
    # ca_cert = '/path/to/cert.pem'
    # response = requests.get('https://example.com', verify=ca_cert)
    
    # 指定客户端证书
    # client_cert = ('/path/to/client.cert', '/path/to/client.key')
    # response = requests.get('https://example.com', cert=client_cert)

if __name__ == "__main__":
    test_ssl_verification()
```

### 3.5 流式请求

```python
import requests

def stream_request():
    # 流式获取大文件
    url = 'https://httpbin.org/stream/20'  # 返回20行JSON数据
    
    print("流式处理响应:")
    with requests.get(url, stream=True) as response:
        # 逐行处理响应内容
        for line in response.iter_lines():
            if line:
                print(f"接收到数据: {line.decode('utf-8')}")
    
    # 分块处理大文件下载
    print("\n分块处理下载:")
    url = 'https://httpbin.org/bytes/1000'  # 返回1000字节的随机数据
    
    chunk_size = 128
    with requests.get(url, stream=True) as response:
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                downloaded_size += len(chunk)
                # 这里可以处理每个数据块，比如写入文件
                # with open('download.bin', 'ab') as f:
                #     f.write(chunk)
                
                # 显示进度
                if total_size > 0:
                    percent = (downloaded_size / total_size) * 100
                    print(f"下载进度: {percent:.1f}% ({downloaded_size}/{total_size} bytes)", end='\r')
        
        print()  # 换行

if __name__ == "__main__":
    stream_request()
```

## 4. 会话管理

### 4.1 创建和使用会话

```python
import requests

def use_session():
    # 创建一个会话
    session = requests.Session()
    
    # 设置会话级别的请求头
    session.headers.update({'User-Agent': 'MySessionAgent/1.0'})
    
    # 通过会话发送请求
    # 第一次请求，登录或获取Cookie
    login_data = {'username': 'testuser', 'password': 'testpass'}
    response1 = session.post('https://httpbin.org/cookies/set?sessioncookie=123456')
    print("第一次请求的Cookie:", dict(session.cookies))
    
    # 第二次请求，Cookie会自动附加
    response2 = session.get('https://httpbin.org/cookies')
    print("\n服务器收到的Cookie:", response2.text)
    
    # 手动设置Cookie
    session.cookies.set('custom_cookie', 'custom_value', domain='httpbin.org')
    response3 = session.get('https://httpbin.org/cookies')
    print("\n设置自定义Cookie后的结果:", response3.text)
    
    # 设置会话级别的代理
    session.proxies.update({
        # 'http': 'http://proxy.example.com:8080',
        # 'https': 'https://proxy.example.com:8080'
    })
    
    # 会话级别的认证
    # session.auth = ('username', 'password')
    
    # 关闭会话
    session.close()

if __name__ == "__main__":
    use_session()
```

### 4.2 使用上下文管理器

```python
import requests

def session_context_manager():
    # 使用上下文管理器自动关闭会话
    with requests.Session() as session:
        # 设置会话属性
        session.headers.update({'Custom-Header': 'CustomValue'})
        
        # 发送请求
        response = session.get('https://httpbin.org/headers')
        print("请求头:", response.json()['headers'].get('Custom-Header'))
        
        # 会话会在with块结束后自动关闭
    
    # 会话已关闭，无法再使用
    # 下面的代码会引发异常
    # try:
    #     session.get('https://httpbin.org/get')
    # except Exception as e:
    #     print(f"会话已关闭: {e}")

if __name__ == "__main__":
    session_context_manager()
```

### 4.3 持久化Cookie

```python
import requests
from http.cookiejar import LWPCookieJar

def persist_cookies():
    # 创建会话
    session = requests.Session()
    
    # 创建CookieJar并绑定到会话
    cookie_jar = LWPCookieJar('cookies.txt')
    session.cookies = cookie_jar
    
    try:
        # 尝试加载已保存的Cookie
        cookie_jar.load(ignore_discard=True)
        print("已加载保存的Cookie")
    except FileNotFoundError:
        print("没有找到Cookie文件，将创建新的")
    
    # 发送请求，更新Cookie
    response = session.get('https://httpbin.org/cookies/set?user=admin&token=12345')
    print("当前Cookie:", dict(session.cookies))
    
    # 保存Cookie到文件
    cookie_jar.save(ignore_discard=True)
    print("Cookie已保存到cookies.txt")
    
    # 下次使用时，可以加载这些Cookie
    # cookie_jar.load(ignore_discard=True)
    
    session.close()

if __name__ == "__main__":
    persist_cookies()
```

## 5. 身份验证

### 5.1 HTTP基本认证

```python
import requests
from requests.auth import HTTPBasicAuth

def test_basic_auth():
    # 方法1：直接在URL中提供凭据（不推荐）
    # response = requests.get('https://user:pass@httpbin.org/basic-auth/user/pass')
    
    # 方法2：使用auth参数
    response = requests.get('https://httpbin.org/basic-auth/user/pass', 
                           auth=('user', 'pass'))
    
    # 方法3：使用HTTPBasicAuth类（功能与方法2相同，但更明确）
    auth = HTTPBasicAuth('user', 'pass')
    response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=auth)
    
    print("认证结果:", response.json())
    
    # 失败的认证
    try:
        wrong_response = requests.get('https://httpbin.org/basic-auth/user/pass',
                                    auth=('wronguser', 'wrongpass'))
        wrong_response.raise_for_status()  # 引发HTTPError
    except requests.exceptions.HTTPError as e:
        print(f"认证失败: {e}")

if __name__ == "__main__":
    test_basic_auth()
```

### 5.2 HTTP摘要认证

```python
import requests
from requests.auth import HTTPDigestAuth

def test_digest_auth():
    # 使用HTTPDigestAuth进行摘要认证
    auth = HTTPDigestAuth('user', 'pass')
    response = requests.get('https://httpbin.org/digest-auth/auth/user/pass', auth=auth)
    
    print("摘要认证结果:", response.json())
    
    # 失败的认证
    try:
        wrong_response = requests.get('https://httpbin.org/digest-auth/auth/user/pass',
                                    auth=HTTPDigestAuth('wronguser', 'wrongpass'))
        wrong_response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"认证失败: {e}")

if __name__ == "__main__":
    test_digest_auth()
```

### 5.3 OAuth认证

```python
import requests

def test_oauth():
    # 方法1：在请求头中设置Bearer令牌
    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
    }
    # response = requests.get('https://api.example.com/resource', headers=headers)
    print("OAuth Bearer令牌认证示例")
    
    # 方法2：使用requests-oauthlib库（需要安装：pip install requests-oauthlib）
    try:
        from requests_oauthlib import OAuth1
        
        # OAuth 1.0认证
        auth = OAuth1(
            'YOUR_APP_KEY',
            'YOUR_APP_SECRET',
            'USER_OAUTH_TOKEN',
            'USER_OAUTH_TOKEN_SECRET'
        )
        # response = requests.get('https://api.twitter.com/1.1/account/verify_credentials.json', auth=auth)
        print("OAuth 1.0认证示例")
        
        # OAuth 2.0认证
        from requests_oauthlib import OAuth2Session
        
        # 创建OAuth2会话
        oauth2_session = OAuth2Session('YOUR_CLIENT_ID', token={'access_token': 'YOUR_ACCESS_TOKEN'})
        # response = oauth2_session.get('https://api.example.com/resource')
        print("OAuth 2.0认证示例")
    except ImportError:
        print("请安装requests-oauthlib库以使用OAuth功能: pip install requests-oauthlib")

if __name__ == "__main__":
    test_oauth()
```

### 5.4 自定义认证

```python
import requests
from requests.auth import AuthBase

class CustomAuth(AuthBase):
    """自定义认证类"""
    def __init__(self, token):
        self.token = token
    
    def __call__(self, r):
        # 修改请求对象
        r.headers['X-Custom-Auth'] = self.token
        return r

def test_custom_auth():
    # 使用自定义认证
    auth = CustomAuth('my-custom-token-12345')
    response = requests.get('https://httpbin.org/headers', auth=auth)
    
    # 检查认证头是否被正确添加
    headers = response.json()['headers']
    print("自定义认证头:", headers.get('X-Custom-Auth'))
    print("所有响应头:", headers)

if __name__ == "__main__":
    test_custom_auth()
```

## 6. 文件上传和下载

### 6.1 上传文件

```python
import requests
import io

def upload_file():
    # 方法1：上传本地文件
    # with open('example.txt', 'rb') as f:
    #     response = requests.post('https://httpbin.org/post', files={'file': f})
    # print(response.text)
    print("本地文件上传示例")
    
    # 方法2：上传内存中的文件
    # 创建内存中的文件对象
    file_content = "这是文件内容".encode('utf-8')
    file_obj = io.BytesIO(file_content)
    
    # 上传文件（指定文件名）
    response = requests.post('https://httpbin.org/post',
                           files={'file': ('example.txt', file_obj, 'text/plain')})
    
    print("\n内存文件上传结果:")
    # 解析响应中的文件内容
    try:
        files = response.json().get('files', {})
        if files:
            print(f"上传的文件名: {list(files.keys())[0]}")
    except ValueError:
        print(response.text)
    
    # 方法3：上传多个文件
    # file1 = open('file1.txt', 'rb')
    # file2 = open('file2.txt', 'rb')
    # response = requests.post('https://httpbin.org/post',
    #                         files=[('files', file1), ('files', file2)])
    # file1.close()
    # file2.close()
    
    # 方法4：上传文件并发送其他数据
    # response = requests.post('https://httpbin.org/post',
    #                         files={'file': open('example.txt', 'rb')},
    #                         data={'name': '张三', 'age': '25'})

if __name__ == "__main__":
    upload_file()
```

### 6.2 下载文件

```python
import requests
import os

def download_file():
    # 下载小文件（一次性加载到内存）
    url = 'https://httpbin.org/image/jpeg'  # 示例JPEG图片
    response = requests.get(url)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 保存文件
        filename = 'downloaded_image.jpg'
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"小文件下载完成: {filename}, 大小: {len(response.content)} 字节")
    
    # 下载大文件（分块下载）
    url = 'https://httpbin.org/bytes/1000000'  # 1MB的随机数据
    filename = 'large_file.bin'
    
    # 确保目录存在
    os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
    
    # 发送流式请求
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # 如果状态码不是200，引发异常
        
        # 获取文件大小
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        
        # 分块写入文件
        chunk_size = 8192  # 8KB
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:  # 过滤掉保持连接的空块
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    
                    # 显示下载进度
                    if total_size > 0:
                        percent = (downloaded_size / total_size) * 100
                        print(f"下载进度: {percent:.1f}% ({downloaded_size}/{total_size} bytes)", end='\r')
        
        print()  # 换行
        print(f"大文件下载完成: {filename}, 大小: {os.path.getsize(filename)} 字节")

if __name__ == "__main__":
    download_file()
```

## 7. 错误处理

### 7.1 捕获异常

```python
import requests

def handle_errors():
    # HTTP错误处理
    try:
        # 请求一个不存在的资源
        response = requests.get('https://httpbin.org/status/404')
        # 如果状态码不是200，引发HTTPError
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP错误: {e}")
    
    # 连接错误处理
    try:
        # 连接到不存在的域名
        response = requests.get('https://nonexistent-domain-123456789.com', timeout=3)
    except requests.exceptions.ConnectionError as e:
        print(f"连接错误: {e}")
    
    # 超时错误处理
    try:
        # 请求一个会延迟响应的URL，但设置较短的超时
        response = requests.get('https://httpbin.org/delay/3', timeout=1)
    except requests.exceptions.Timeout as e:
        print(f"超时错误: {e}")
    
    # URL错误处理
    try:
        # 无效的URL
        response = requests.get('http:///invalid-url')
    except requests.exceptions.InvalidURL as e:
        print(f"无效URL错误: {e}")
    
    # 通用异常处理
    try:
        response = requests.get('https://httpbin.org/get')
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")
    except ValueError as e:
        print(f"JSON解析错误: {e}")
    else:
        print("请求成功!")
        return data
    finally:
        print("错误处理示例完成")

if __name__ == "__main__":
    handle_errors()
```

### 7.2 重试机制

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def setup_retry_session(total_retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 503, 504)):
    """创建带有重试机制的会话"""
    # 创建重试策略
    retry_strategy = Retry(
        total=total_retries,  # 最大重试次数
        backoff_factor=backoff_factor,  # 重试间隔时间因子
        status_forcelist=status_forcelist,  # 触发重试的HTTP状态码
        allowed_methods=["HEAD", "GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],  # 允许重试的HTTP方法
    )
    
    # 创建适配器
    adapter = HTTPAdapter(max_retries=retry_strategy)
    
    # 创建会话
    session = requests.Session()
    
    # 挂载适配器到会话
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    return session

def test_retry_mechanism():
    # 创建带有重试机制的会话
    session = setup_retry_session(total_retries=3, backoff_factor=0.5)
    
    try:
        # 发送请求（这里使用模拟的503错误URL）
        # response = session.get('https://httpbin.org/status/503', timeout=3)
        # 为了演示，我们使用正常URL
        response = session.get('https://httpbin.org/get', timeout=3)
        response.raise_for_status()
        print("请求成功!")
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    test_retry_mechanism()
```

## 8. 高级特性

### 8.1 JSON处理

```python
import requests

def handle_json():
    # 发送JSON数据
    payload = {'name': '张三', 'age': 25, 'city': '北京'}
    response = requests.post('https://httpbin.org/post', json=payload)
    
    # 自动解析JSON响应
    if response.status_code == 200:
        try:
            # 方法1：使用.json()方法
            data = response.json()
            print("JSON响应:", data)
            print("解析的URL:", data.get('url'))
            
            # 访问嵌套的JSON数据
            if 'json' in data:
                json_data = data['json']
                print(f"发送的名称: {json_data.get('name')}")
                print(f"发送的年龄: {json_data.get('age')}")
        except ValueError as e:
            print(f"JSON解析错误: {e}")
    
    # 处理不同的JSON数据类型
    complex_payload = {
        'string': 'text',
        'number': 42,
        'float': 3.14,
        'boolean': True,
        'null': None,
        'array': [1, 2, 3],
        'object': {'key': 'value'}
    }
    
    response = requests.post('https://httpbin.org/post', json=complex_payload)
    if response.status_code == 200:
        data = response.json()
        print("\n复杂JSON响应:")
        for key, value in data.get('json', {}).items():
            print(f"{key}: {value} (类型: {type(value).__name__})")

if __name__ == "__main__":
    handle_json()
```

### 8.2 重定向处理

```python
import requests

def handle_redirects():
    # 默认情况下，requests会自动处理重定向
    response = requests.get('https://httpbin.org/redirect/3')
    print("最终URL:", response.url)
    print("状态码:", response.status_code)
    print("重定向历史:")
    for resp in response.history:
        print(f"  - {resp.status_code}: {resp.url}")
    
    # 禁用重定向
    response_no_redirect = requests.get('https://httpbin.org/redirect/1', allow_redirects=False)
    print("\n禁用重定向后:")
    print("状态码:", response_no_redirect.status_code)  # 应该是302
    print("Location头:", response_no_redirect.headers.get('Location'))
    
    # 限制重定向次数
    session = requests.Session()
    session.max_redirects = 2  # 最多允许2次重定向
    
    try:
        response_limited = session.get('https://httpbin.org/redirect/3')
    except requests.exceptions.TooManyRedirects as e:
        print(f"\n重定向次数过多: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    handle_redirects()
```

### 8.3 自定义请求钩子

```python
import requests
from requests import Response

def log_request(req, *args, **kwargs):
    """请求前的日志钩子"""
    print(f"\n发送请求: {req.method} {req.url}")
    print(f"请求头: {dict(req.headers)}")
    if hasattr(req, 'body') and req.body:
        print(f"请求体: {req.body[:100]}..." if len(req.body) > 100 else f"请求体: {req.body}")

def log_response(resp, *args, **kwargs):
    """响应后的日志钩子"""
    print(f"\n收到响应: {resp.status_code} {resp.reason}")
    print(f"响应URL: {resp.url}")
    print(f"响应头: {dict(resp.headers)}")
    # 注意：不要在生产环境中记录大型响应体

def test_request_hooks():
    # 创建会话
    session = requests.Session()
    
    # 添加请求钩子
    session.hooks['pre_request'] = [log_request]
    session.hooks['response'] = [log_response]
    
    try:
        # 发送请求
        response = session.get('https://httpbin.org/get')
        print(f"\n最终状态: {response.status_code}")
    finally:
        session.close()

def test_custom_hook():
    def check_status_hook(response: Response, *args, **kwargs):
        """检查响应状态码并记录"""
        if 400 <= response.status_code < 500:
            print(f"客户端错误: {response.status_code} {response.reason}")
        elif 500 <= response.status_code < 600:
            print(f"服务器错误: {response.status_code} {response.reason}")
    
    # 使用单次请求的钩子
    response = requests.get(
        'https://httpbin.org/status/404',
        hooks={'response': [check_status_hook]}
    )

if __name__ == "__main__":
    test_request_hooks()
    print("\n" + "="*50 + "\n")
    test_custom_hook()
```

### 8.4 会话事件钩子

```python
import requests
from requests import Session

def setup_event_hooks():
    # 创建会话
    session = Session()
    
    # 添加请求前钩子
    def before_request(session, request):
        print(f"即将发送请求: {request.method} {request.url}")
        return request
    
    # 添加响应后钩子
    def after_response(session, response, **kwargs):
        print(f"收到响应: {response.status_code} {response.url}")
        # 可以在这里处理响应，比如记录日志、解析数据等
        return response
    
    # 注册钩子
    session.hooks['pre_request'] = [before_request]
    session.hooks['response'] = [after_response]
    
    # 发送请求
    response = session.get('https://httpbin.org/get')
    print(f"最终状态码: {response.status_code}")
    
    # 清理
    session.close()

if __name__ == "__main__":
    setup_event_hooks()
```

## 9. 性能优化

### 9.1 连接池管理

```python
import requests
from requests.adapters import HTTPAdapter
import time

def optimize_connection_pool():
    # 创建会话并配置连接池
    session = requests.Session()
    
    # 创建适配器，设置连接池大小
    adapter = HTTPAdapter(
        pool_connections=20,  # 连接池中的连接数
        pool_maxsize=20,      # 连接池的最大大小
        max_retries=3,        # 最大重试次数
        pool_block=False      # 是否在连接池满时阻塞
    )
    
    # 挂载适配器
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    # 发送多个请求，测试连接复用
    urls = ['https://httpbin.org/get' for _ in range(10)]
    
    start_time = time.time()
    responses = []
    
    for url in urls:
        response = session.get(url, timeout=5)
        responses.append(response)
    
    end_time = time.time()
    
    print(f"使用连接池处理 {len(urls)} 个请求耗时: {end_time - start_time:.2f} 秒")
    print(f"平均每个请求耗时: {(end_time - start_time) / len(urls):.4f} 秒")
    
    # 对比：不使用会话（每次创建新连接）
    start_time = time.time()
    
    for url in urls:
        response = requests.get(url, timeout=5)
    
    end_time = time.time()
    
    print(f"\n不使用连接池处理 {len(urls)} 个请求耗时: {end_time - start_time:.2f} 秒")
    print(f"平均每个请求耗时: {(end_time - start_time) / len(urls):.4f} 秒")
    
    # 清理
    session.close()

if __name__ == "__main__":
    optimize_connection_pool()
```

### 9.2 并发请求

```python
import requests
import concurrent.futures
import time

def fetch_url(url, session=None, timeout=5):
    """获取单个URL的内容"""
    try:
        if session:
            response = session.get(url, timeout=timeout)
        else:
            response = requests.get(url, timeout=timeout)
        return url, response.status_code, len(response.content)
    except Exception as e:
        return url, None, str(e)

def concurrent_requests(urls, max_workers=10, use_session=False):
    """并发发送多个请求"""
    results = []
    
    if use_session:
        # 使用会话
        with requests.Session() as session:
            adapter = requests.adapters.HTTPAdapter(
                pool_connections=max_workers,
                pool_maxsize=max_workers
            )
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
                # 提交任务
                future_to_url = {executor.submit(fetch_url, url, session): url for url in urls}
                
                # 获取结果
                for future in concurrent.futures.as_completed(future_to_url):
                    results.append(future.result())
    else:
        # 不使用会话
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {executor.submit(fetch_url, url): url for url in urls}
            
            for future in concurrent.futures.as_completed(future_to_url):
                results.append(future.result())
    
    return results

def test_concurrent_performance():
    # 创建URL列表
    urls = ['https://httpbin.org/get' for _ in range(20)]
    
    # 测试串行请求
    start_time = time.time()
    serial_results = []
    
    for url in urls:
        result = fetch_url(url)
        serial_results.append(result)
    
    serial_time = time.time() - start_time
    print(f"串行请求耗时: {serial_time:.2f} 秒")
    
    # 测试并发请求（不使用会话）
    start_time = time.time()
    concurrent_results1 = concurrent_requests(urls, max_workers=5, use_session=False)
    concurrent_time1 = time.time() - start_time
    print(f"\n并发请求（不使用会话）耗时: {concurrent_time1:.2f} 秒")
    print(f"性能提升: {(serial_time - concurrent_time1) / serial_time * 100:.1f}%")
    
    # 测试并发请求（使用会话）
    start_time = time.time()
    concurrent_results2 = concurrent_requests(urls, max_workers=5, use_session=True)
    concurrent_time2 = time.time() - start_time
    print(f"\n并发请求（使用会话）耗时: {concurrent_time2:.2f} 秒")
    print(f"性能提升: {(serial_time - concurrent_time2) / serial_time * 100:.1f}%")
    
    # 显示结果统计
    success_count1 = sum(1 for _, status, _ in concurrent_results1 if status is not None)
    success_count2 = sum(1 for _, status, _ in concurrent_results2 if status is not None)
    
    print(f"\n不使用会话 - 成功请求: {success_count1}/{len(urls)}")
    print(f"使用会话 - 成功请求: {success_count2}/{len(urls)}")

if __name__ == "__main__":
    test_concurrent_performance()
```

### 9.3 响应缓存

```python
import requests
import os
import hashlib
import time
from datetime import datetime, timedelta

def get_cache_key(url):
    """生成URL的缓存键"""
    return hashlib.md5(url.encode('utf-8')).hexdigest()

def cache_response(url, response_content, cache_dir='.cache', expiration_hours=1):
    """缓存响应内容"""
    # 确保缓存目录存在
    os.makedirs(cache_dir, exist_ok=True)
    
    # 生成缓存文件名
    cache_key = get_cache_key(url)
    cache_file = os.path.join(cache_dir, cache_key)
    
    # 存储响应内容和过期时间
    expiration_time = datetime.now() + timedelta(hours=expiration_hours)
    cache_data = {
        'content': response_content,
        'expiration': expiration_time.isoformat()
    }
    
    # 写入缓存文件（以二进制形式）
    with open(cache_file, 'wb') as f:
        import pickle
        pickle.dump(cache_data, f)
    
    return cache_file

def get_cached_response(url, cache_dir='.cache'):
    """获取缓存的响应"""
    cache_key = get_cache_key(url)
    cache_file = os.path.join(cache_dir, cache_key)
    
    if not os.path.exists(cache_file):
        return None
    
    try:
        # 读取缓存文件
        with open(cache_file, 'rb') as f:
            import pickle
            cache_data = pickle.load(f)
        
        # 检查是否过期
        expiration_time = datetime.fromisoformat(cache_data['expiration'])
        if datetime.now() > expiration_time:
            # 删除过期缓存
            os.remove(cache_file)
            return None
        
        return cache_data['content']
    except Exception as e:
        print(f"读取缓存失败: {e}")
        return None

def requests_with_cache(url, cache_dir='.cache', expiration_hours=1, **kwargs):
    """带缓存的请求函数"""
    # 尝试从缓存获取
    cached_content = get_cached_response(url, cache_dir)
    if cached_content is not None:
        print(f"从缓存获取: {url}")
        # 创建一个模拟的Response对象
        from requests.models import Response
        response = Response()
        response._content = cached_content
        response.status_code = 200
        response.url = url
        return response
    
    # 缓存未命中，发送实际请求
    print(f"发送请求: {url}")
    response = requests.get(url, **kwargs)
    
    # 缓存响应
    if response.status_code == 200:
        cache_response(url, response.content, cache_dir, expiration_hours)
    
    return response

def test_caching_performance():
    # 测试URL
    url = 'https://httpbin.org/get'
    
    # 第一次请求（无缓存）
    start_time = time.time()
    response1 = requests_with_cache(url)
    time1 = time.time() - start_time
    print(f"第一次请求耗时: {time1:.2f} 秒")
    
    # 第二次请求（使用缓存）
    start_time = time.time()
    response2 = requests_with_cache(url)
    time2 = time.time() - start_time
    print(f"\n第二次请求耗时: {time2:.2f} 秒")
    
    # 计算性能提升
    print(f"\n缓存性能提升: {(time1 - time2) / time1 * 100:.1f}%")
    
    # 验证内容是否相同
    content_same = response1.content == response2.content
    print(f"缓存内容是否相同: {content_same}")

if __name__ == "__main__":
    test_caching_performance()
```

## 10. 实际应用示例

### 10.1 REST API客户端

```python
import requests
import json

class RESTClient:
    """简单的REST API客户端"""
    
    def __init__(self, base_url, auth=None, timeout=30):
        """
        初始化客户端
        
        参数:
            base_url: API基础URL
            auth: 认证信息
            timeout: 请求超时时间
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.auth = auth
        self.timeout = timeout
        
        # 设置默认请求头
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        # 配置连接池
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=10,
            pool_maxsize=10,
            max_retries=3
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
    
    def _build_url(self, endpoint):
        """构建完整的URL"""
        return f"{self.base_url}/{endpoint.lstrip('/')}"
    
    def _handle_response(self, response):
        """处理API响应"""
        try:
            # 尝试解析JSON响应
            data = response.json()
        except ValueError:
            # 非JSON响应
            data = response.text
        
        # 检查状态码
        if not response.ok:
            error_msg = f"API错误: {response.status_code} {response.reason}"
            if isinstance(data, dict) and 'error' in data:
                error_msg += f" - {data['error']}"
            raise requests.exceptions.HTTPError(error_msg, response=response)
        
        return data
    
    def get(self, endpoint, params=None, **kwargs):
        """发送GET请求"""
        url = self._build_url(endpoint)
        response = self.session.get(url, params=params, timeout=self.timeout, **kwargs)
        return self._handle_response(response)
    
    def post(self, endpoint, data=None, json_data=None, **kwargs):
        """发送POST请求"""
        url = self._build_url(endpoint)
        
        # 优先使用json_data
        if json_data is not None:
            response = self.session.post(url, json=json_data, timeout=self.timeout, **kwargs)
        else:
            response = self.session.post(url, data=data, timeout=self.timeout, **kwargs)
        
        return self._handle_response(response)
    
    def put(self, endpoint, data=None, json_data=None, **kwargs):
        """发送PUT请求"""
        url = self._build_url(endpoint)
        
        if json_data is not None:
            response = self.session.put(url, json=json_data, timeout=self.timeout, **kwargs)
        else:
            response = self.session.put(url, data=data, timeout=self.timeout, **kwargs)
        
        return self._handle_response(response)
    
    def delete(self, endpoint, **kwargs):
        """发送DELETE请求"""
        url = self._build_url(endpoint)
        response = self.session.delete(url, timeout=self.timeout, **kwargs)
        return self._handle_response(response)
    
    def patch(self, endpoint, data=None, json_data=None, **kwargs):
        """发送PATCH请求"""
        url = self._build_url(endpoint)
        
        if json_data is not None:
            response = self.session.patch(url, json=json_data, timeout=self.timeout, **kwargs)
        else:
            response = self.session.patch(url, data=data, timeout=self.timeout, **kwargs)
        
        return self._handle_response(response)
    
    def set_auth(self, auth):
        """设置认证信息"""
        self.session.auth = auth
    
    def set_header(self, name, value):
        """设置请求头"""
        self.session.headers[name] = value
    
    def close(self):
        """关闭会话"""
        self.session.close()
    
    def __enter__(self):
        """支持上下文管理器"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器时关闭会话"""
        self.close()

# 使用示例
def test_rest_client():
    # 使用上下文管理器创建客户端
    with RESTClient('https://jsonplaceholder.typicode.com') as client:
        try:
            # 获取资源
            print("\n=== 获取单个帖子 ===")
            post = client.get('posts/1')
            print(f"标题: {post.get('title')}")
            print(f"内容: {post.get('body')[:100]}...")
            
            # 获取资源列表
            print("\n=== 获取帖子列表 ===")
            posts = client.get('posts', params={'userId': 1})
            print(f"找到 {len(posts)} 个帖子")
            
            # 创建资源
            print("\n=== 创建新帖子 ===")
            new_post = client.post('posts', json_data={
                'title': '测试帖子',
                'body': '这是测试内容',
                'userId': 1
            })
            print(f"创建的帖子ID: {new_post.get('id')}")
            
            # 更新资源
            print("\n=== 更新帖子 ===")
            updated_post = client.put('posts/1', json_data={
                'id': 1,
                'title': '更新的标题',
                'body': '更新的内容',
                'userId': 1
            })
            print(f"更新后的标题: {updated_post.get('title')}")
            
            # 部分更新
            print("\n=== 部分更新帖子 ===")
            patched_post = client.patch('posts/1', json_data={
                'title': '部分更新的标题'
            })
            print(f"部分更新后的标题: {patched_post.get('title')}")
            
        except Exception as e:
            print(f"API请求失败: {e}")

if __name__ == "__main__":
    test_rest_client()
```

### 10.2 文件下载器

```python
import requests
import os
import time
from tqdm import tqdm  # 需要安装: pip install tqdm

def download_file_with_progress(url, save_path=None, chunk_size=8192, show_progress=True):
    """
    下载文件并显示进度条
    
    参数:
        url: 要下载的文件URL
        save_path: 保存路径，默认使用URL中的文件名
        chunk_size: 下载块大小
        show_progress: 是否显示进度条
    
    返回:
        下载的文件路径
    """
    # 如果没有指定保存路径，从URL提取文件名
    if save_path is None:
        filename = os.path.basename(url)
        if not filename:
            filename = 'downloaded_file'
        save_path = os.path.join(os.getcwd(), filename)
    
    # 确保目录存在
    os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
    
    try:
        # 发送请求获取文件信息
        with requests.get(url, stream=True, timeout=30) as response:
            response.raise_for_status()  # 检查状态码
            
            # 获取文件大小
            total_size = int(response.headers.get('content-length', 0))
            
            print(f"开始下载: {url}")
            print(f"保存到: {save_path}")
            if total_size > 0:
                print(f"文件大小: {total_size / (1024*1024):.2f} MB")
            
            # 开始时间
            start_time = time.time()
            
            # 创建进度条
            if show_progress and total_size > 0:
                pbar = tqdm(total=total_size, unit='B', unit_scale=True, desc=os.path.basename(save_path))
            
            # 写入文件
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:  # 过滤掉保持连接的空块
                        f.write(chunk)
                        
                        # 更新进度条
                        if show_progress and total_size > 0:
                            pbar.update(len(chunk))
            
            # 关闭进度条
            if show_progress and total_size > 0:
                pbar.close()
            
            # 计算下载时间和速度
            elapsed_time = time.time() - start_time
            file_size = os.path.getsize(save_path)
            download_speed = file_size / elapsed_time if elapsed_time > 0 else 0
            
            print(f"下载完成!")
            print(f"实际文件大小: {file_size / (1024*1024):.2f} MB")
            print(f"下载时间: {elapsed_time:.2f} 秒")
            print(f"下载速度: {download_speed / (1024*1024):.2f} MB/s")
            
            return save_path
            
    except requests.exceptions.RequestException as e:
        print(f"下载失败: {e}")
        # 如果下载失败，删除部分文件
        if os.path.exists(save_path):
            os.remove(save_path)
        raise

def batch_download(urls, directory=None, max_workers=5):
    """
    批量下载文件
    
    参数:
        urls: URL列表或字典 {url: filename}
        directory: 保存目录
        max_workers: 最大并发数
    """
    # 确保目录存在
    if directory:
        os.makedirs(directory, exist_ok=True)
    
    # 处理URL输入
    download_tasks = []
    if isinstance(urls, dict):
        for url, filename in urls.items():
            if directory:
                save_path = os.path.join(directory, filename)
            else:
                save_path = filename
            download_tasks.append((url, save_path))
    else:
        for url in urls:
            if directory:
                filename = os.path.basename(url)
                if not filename:
                    filename = f'downloaded_{len(download_tasks)}.bin'
                save_path = os.path.join(directory, filename)
            else:
                save_path = None
            download_tasks.append((url, save_path))
    
    # 并发下载
    import concurrent.futures
    results = {}
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交任务
        future_to_url = {}
        for url, save_path in download_tasks:
            future = executor.submit(download_file_with_progress, url, save_path, show_progress=False)
            future_to_url[future] = url
        
        # 获取结果
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                save_path = future.result()
                results[url] = {'success': True, 'path': save_path}
                print(f"\nURL: {url} 下载成功")
            except Exception as e:
                results[url] = {'success': False, 'error': str(e)}
                print(f"\nURL: {url} 下载失败: {e}")
    
    # 打印汇总信息
    print("\n=== 下载汇总 ===")
    total = len(results)
    success = sum(1 for r in results.values() if r['success'])
    failed = total - success
    
    print(f"总任务: {total}")
    print(f"成功: {success}")
    print(f"失败: {failed}")
    
    if failed > 0:
        print("\n失败的下载:")
        for url, result in results.items():
            if not result['success']:
                print(f"  - {url}: {result['error']}")
    
    return results

# 使用示例
def test_file_downloader():
    # 单个文件下载
    print("\n=== 测试单个文件下载 ===")
    # 这是一个示例图片URL，实际使用时请替换为有效的URL
    image_url = 'https://httpbin.org/image/jpeg'
    try:
        save_path = download_file_with_progress(image_url, save_path='example_image.jpg')
        print(f"文件保存到: {save_path}")
    except Exception as e:
        print(f"下载失败: {e}")
    
    # 批量下载
    print("\n=== 测试批量下载 ===")
    test_urls = {
        'https://httpbin.org/image/jpeg': 'image1.jpg',
        'https://httpbin.org/image/png': 'image2.png',
        'https://httpbin.org/bytes/100000': 'data.bin'
    }
    
    batch_download(test_urls, directory='downloads', max_workers=2)

if __name__ == "__main__":
    test_file_downloader()
```

### 10.3 简易网页爬虫

```python
import requests
from bs4 import BeautifulSoup  # 需要安装: pip install beautifulsoup4
import urllib.parse
import time
import os
from urllib.robotparser import RobotFileParser

class SimpleWebCrawler:
    """简易网页爬虫"""
    
    def __init__(self, user_agent='SimpleCrawler/1.0', respect_robots=True,
                 max_retries=3, timeout=10, delay=1):
        """
        初始化爬虫
        
        参数:
            user_agent: 用户代理
            respect_robots: 是否遵守robots.txt规则
            max_retries: 最大重试次数
            timeout: 请求超时时间
            delay: 请求间隔时间（秒）
        """
        self.user_agent = user_agent
        self.respect_robots = respect_robots
        self.max_retries = max_retries
        self.timeout = timeout
        self.delay = delay
        
        # 创建会话
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': user_agent})
        
        # 配置连接池和重试
        from requests.adapters import HTTPAdapter
        from urllib3.util.retry import Retry
        
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=0.3,
            status_forcelist=(500, 502, 503, 504)
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy, 
                             pool_connections=10, 
                             pool_maxsize=10)
        
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        
        # 存储已访问的URL
        self.visited_urls = set()
        
        # 存储robots.txt解析器
        self.robots_parsers = {}
    
    def _get_robots_parser(self, base_url):
        """获取指定网站的robots.txt解析器"""
        if base_url not in self.robots_parsers:
            robots_url = urllib.parse.urljoin(base_url, '/robots.txt')
            parser = RobotFileParser()
            
            try:
                response = self.session.get(robots_url, timeout=self.timeout)
                if response.status_code == 200:
                    parser.parse(response.text.splitlines())
            except Exception as e:
                print(f"无法获取robots.txt: {e}")
                # 如果无法获取robots.txt，默认允许抓取
            
            self.robots_parsers[base_url] = parser
        
        return self.robots_parsers[base_url]
    
    def _is_allowed_by_robots(self, url):
        """检查URL是否被robots.txt允许抓取"""
        if not self.respect_robots:
            return True
        
        parsed_url = urllib.parse.urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        parser = self._get_robots_parser(base_url)
        return parser.can_fetch(self.user_agent, url)
    
    def fetch_page(self, url):
        """获取页面内容"""
        if url in self.visited_urls:
            return None
        
        # 检查robots.txt
        if not self._is_allowed_by_robots(url):
            print(f"根据robots.txt，禁止抓取: {url}")
            return None
        
        # 添加到已访问列表
        self.visited_urls.add(url)
        
        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            
            # 检查内容类型
            content_type = response.headers.get('Content-Type', '')
            if 'text/html' not in content_type:
                print(f"跳过非HTML内容: {content_type} - {url}")
                return None
            
            # 等待一段时间再发送下一个请求
            time.sleep(self.delay)
            
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"获取页面失败: {e} - {url}")
            return None
    
    def extract_links(self, html, base_url):
        """从HTML中提取链接"""
        if not html:
            return []
        
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            
            # 过滤掉JavaScript链接和锚点
            if href.startswith('javascript:') or href.startswith('#'):
                continue
            
            # 构建绝对URL
            absolute_url = urllib.parse.urljoin(base_url, href)
            
            # 只保留相同域名的链接
            base_domain = urllib.parse.urlparse(base_url).netloc
            link_domain = urllib.parse.urlparse(absolute_url).netloc
            
            if base_domain == link_domain:
                links.append(absolute_url)
        
        return links
    
    def extract_metadata(self, html):
        """提取页面元数据"""
        if not html:
            return {}
        
        soup = BeautifulSoup(html, 'html.parser')
        metadata = {}
        
        # 提取标题
        title = soup.title
        if title:
            metadata['title'] = title.string.strip()
        
        # 提取描述
        description = soup.find('meta', attrs={'name': 'description'})
        if description and description.get('content'):
            metadata['description'] = description.get('content')
        
        # 提取keywords
        keywords = soup.find('meta', attrs={'name': 'keywords'})
        if keywords and keywords.get('content'):
            metadata['keywords'] = keywords.get('content').split(',')
        
        return metadata
    
    def crawl(self, start_url, max_pages=10, save_dir=None):
        """
        开始爬取
        
        参数:
            start_url: 起始URL
            max_pages: 最大爬取页面数
            save_dir: 保存目录
        """
        # 确保保存目录存在
        if save_dir:
            os.makedirs(save_dir, exist_ok=True)
        
        # 待爬取的URL队列
        to_crawl = [start_url]
        crawled_count = 0
        results = []
        
        print(f"开始爬取，起始URL: {start_url}")
        print(f"最大爬取页面数: {max_pages}")
        
        while to_crawl and crawled_count < max_pages:
            url = to_crawl.pop(0)
            
            # 获取页面
            html = self.fetch_page(url)
            if not html:
                continue
            
            # 提取元数据
            metadata = self.extract_metadata(html)
            print(f"\n爬取: {url}")
            print(f"标题: {metadata.get('title', '无标题')}")
            
            # 提取链接
            links = self.extract_links(html, url)
            print(f"发现 {len(links)} 个链接")
            
            # 添加新的链接到队列
            for link in links:
                if link not in self.visited_urls and link not in to_crawl:
                    to_crawl.append(link)
            
            # 保存页面内容（如果指定了保存目录）
            if save_dir:
                # 生成安全的文件名
                filename = urllib.parse.quote(url, safe='')[:250] + '.html'
                filepath = os.path.join(save_dir, filename)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)
                
                print(f"已保存到: {filename}")
            
            # 记录结果
            result = {
                'url': url,
                'metadata': metadata,
                'links_count': len(links)
            }
            results.append(result)
            
            crawled_count += 1
            print(f"已爬取 {crawled_count}/{max_pages} 页面")
        
        print(f"\n爬取完成! 共爬取 {crawled_count} 个页面")
        return results
    
    def close(self):
        """关闭会话"""
        self.session.close()
    
    def __enter__(self):
        """支持上下文管理器"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器时关闭会话"""
        self.close()

# 使用示例
def test_web_crawler():
    # 使用上下文管理器创建爬虫
    with SimpleWebCrawler(
        user_agent='TestCrawler/1.0 (+https://example.com/crawler)',
        respect_robots=True,
        delay=2
    ) as crawler:
        # 爬取示例网站（实际使用时请替换为合法的网站）
        # 注意：爬取网站时请遵守网站的robots.txt规则和使用条款
        print("简易网页爬虫示例")
        print("注意：以下代码仅用于演示，实际爬取时请确保遵守相关网站的规定")
        
        # 以下是示例代码框架，实际使用时请替换为合法的URL
        # results = crawler.crawl(
        #     start_url='https://example.com',
        #     max_pages=5,
        #     save_dir='crawled_pages'
        # )
        
        # 打印结果统计
        # print("\n=== 爬取结果统计 ===")
        # for i, result in enumerate(results, 1):
        #     print(f"\n页面 {i}:")
        #     print(f"URL: {result['url']}")
        #     print(f"标题: {result['metadata'].get('title', '无标题')}")
        #     print(f"发现链接数: {result['links_count']}")

if __name__ == "__main__":
    test_web_crawler()

## 11. 安全考虑

### 11.1 避免常见安全问题

```python
import requests

def security_best_practices():
    # 1. 验证SSL证书（默认已启用）
    # 永远不要在生产环境中使用verify=False
    # 错误示例: response = requests.get('https://example.com', verify=False)
    
    # 正确做法: 使用系统CA证书或指定自定义CA证书
    # response = requests.get('https://example.com', verify='/path/to/cert.pem')
    
    # 2. 避免在URL中暴露敏感信息
    # 错误示例: 
    # url = 'https://api.example.com/data?api_key=abc123xyz456'
    
    # 正确做法: 使用请求头或请求体传递敏感信息
    headers = {
        'Authorization': 'Bearer abc123xyz456'
    }
    # response = requests.get('https://api.example.com/data', headers=headers)
    
    # 3. 限制请求超时
    # 错误示例: 没有设置超时
    # response = requests.get('https://example.com')  # 可能会一直等待
    
    # 正确做法: 设置合理的超时
    # response = requests.get('https://example.com', timeout=10)
    
    # 4. 避免存储敏感信息
    # 错误示例: 硬编码密码或令牌
    # auth = ('admin', 'password123')
    
    # 正确做法: 从环境变量或配置文件中读取
    import os
    # username = os.environ.get('API_USERNAME')
    # password = os.environ.get('API_PASSWORD')
    # auth = (username, password)
    
    # 5. 验证响应内容
    # 始终验证接收到的数据，不要盲目信任
    # response = requests.get('https://api.example.com/data')
    # if response.status_code == 200:
    #     try:
    #         data = response.json()
    #         # 验证数据结构
    #         if 'key' in data and isinstance(data['key'], str):
    #             # 处理数据
    #             pass
    #     except (ValueError, KeyError):
    #         print("无效的响应数据")
    
    print("安全最佳实践示例")

if __name__ == "__main__":
    security_best_practices()
```

### 11.2 处理敏感数据

```python
import requests
import os
from dotenv import load_dotenv  # 需要安装: pip install python-dotenv

def handle_sensitive_data():
    # 1. 从环境变量加载敏感信息
    # 创建.env文件（不提交到版本控制）并添加：
    # API_KEY=your_actual_api_key
    # API_SECRET=your_actual_api_secret
    
    # 加载环境变量
    load_dotenv()
    
    # 获取敏感信息
    api_key = os.getenv('API_KEY')
    api_secret = os.getenv('API_SECRET')
    
    # 如果环境变量不存在，使用默认值或抛出异常
    if not api_key or not api_secret:
        print("警告: 未找到API密钥，请设置环境变量")
        # 可以使用占位符值用于演示
        api_key = 'demo_api_key'
        api_secret = 'demo_api_secret'
    
    # 2. 使用安全的认证方式
    # 方法1: 使用请求头
    headers = {
        'X-API-Key': api_key,
        'X-API-Secret': api_secret
    }
    # response = requests.get('https://api.example.com/secure-endpoint', headers=headers)
    
    # 方法2: 使用认证对象
    # from requests.auth import HTTPBasicAuth
    # auth = HTTPBasicAuth(api_key, api_secret)
    # response = requests.get('https://api.example.com/secure-endpoint', auth=auth)
    
    # 3. 加密敏感数据
    # 如果需要在请求体中发送敏感数据，可以考虑加密
    # 这里是一个简化的示例，实际应用中应使用强加密算法
    # import base64
    # sensitive_data = 'secret information'
    # encoded_data = base64.b64encode(sensitive_data.encode('utf-8')).decode('utf-8')
    # response = requests.post('https://api.example.com/secure-endpoint', 
    #                         json={'data': encoded_data})
    
    print("敏感数据处理示例")

if __name__ == "__main__":
    handle_sensitive_data()
```

## 12. 最佳实践

### 12.1 一般最佳实践

1. **使用会话（Session）**：对于多个相关请求，始终使用`requests.Session()`来重用连接和保留Cookie。

2. **设置超时**：始终为请求设置超时，避免无限期等待。

3. **处理异常**：使用try-except捕获可能的请求异常，确保程序稳定性。

4. **验证SSL证书**：在生产环境中，永远不要禁用SSL验证。

5. **使用上下文管理器**：使用`with`语句管理会话和文件，确保资源正确释放。

6. **检查状态码**：使用`response.raise_for_status()`或检查`response.ok`来验证请求是否成功。

7. **尊重robots.txt**：编写爬虫时，遵守网站的robots.txt规则。

8. **设置适当的用户代理**：提供有意义的用户代理，以便网站管理员能够联系到你。

9. **实现速率限制**：添加请求延迟，避免对服务器造成压力。

10. **使用连接池**：配置连接池参数，优化大量请求的性能。

### 12.2 代码组织最佳实践

```python
# 1. 将API调用封装到类或函数中
import requests
import json

class APIClient:
    """API客户端基类"""
    def __init__(self, base_url, api_key=None, timeout=30):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.session = requests.Session()
        self._setup_session()
    
    def _setup_session(self):
        """配置会话参数"""
        # 设置默认请求头
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
        
        # 如果有API密钥，添加到请求头
        if self.api_key:
            self.session.headers['Authorization'] = f'Bearer {self.api_key}'
        
        # 配置连接池
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=20,
            pool_maxsize=20,
            max_retries=3
        )
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
    
    def _build_url(self, endpoint):
        """构建完整URL"""
        return f"{self.base_url}/{endpoint.lstrip('/')}"
    
    def get(self, endpoint, params=None):
        """发送GET请求"""
        url = self._build_url(endpoint)
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"GET请求失败: {e}")
            return None
    
    def post(self, endpoint, data=None):
        """发送POST请求"""
        url = self._build_url(endpoint)
        try:
            response = self.session.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"POST请求失败: {e}")
            return None
    
    def close(self):
        """关闭会话"""
        self.session.close()
    
    def __enter__(self):
        """支持上下文管理器"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文管理器"""
        self.close()

# 2. 使用配置文件管理环境
import os
from configparser import ConfigParser

def load_config():
    """加载配置"""
    config = ConfigParser()
    # 尝试加载配置文件
    config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
    if os.path.exists(config_path):
        config.read(config_path)
    
    # 获取配置值，优先使用环境变量
    api_config = {
        'base_url': os.environ.get('API_BASE_URL', config.get('api', 'base_url', fallback='https://api.example.com')),
        'api_key': os.environ.get('API_KEY', config.get('api', 'api_key', fallback='')),
        'timeout': int(os.environ.get('API_TIMEOUT', config.get('api', 'timeout', fallback='30')))
    }
    
    return api_config

# 3. 使用日志记录
import logging

def setup_logging():
    """设置日志"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("requests.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

# 4. 重试装饰器
def retry_on_failure(max_retries=3, delay=1, exceptions=(requests.exceptions.RequestException,)):
    """请求重试装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            last_exception = None
            
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    retries += 1
                    print(f"请求失败，{retries}/{max_retries} 次重试，错误: {e}")
                    if retries < max_retries:
                        print(f"{delay}秒后重试...")
                        import time
                        time.sleep(delay)
            
            raise last_exception
        
        return wrapper
    
    return decorator

@retry_on_failure(max_retries=3, delay=2)
def fetch_data_with_retry(url):
    """带重试机制的数据获取函数"""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
```

## 13. 与其他HTTP客户端的比较

| 特性 | requests | urllib | http.client | aiohttp | httpx |
|------|----------|--------|------------|---------|-------|
| 是否标准库 | 否 | 是 | 是 | 否 | 否 |
| API简洁度 | ★★★★★ | ★★ | ★☆ | ★★★★ | ★★★★★ |
| 异步支持 | 否 | 否 | 否 | 是 | 是 |
| 会话管理 | 是 | 部分 | 否 | 是 | 是 |
| 文件上传 | 简单 | 复杂 | 复杂 | 简单 | 简单 |
| JSON支持 | 内置 | 需手动 | 需手动 | 内置 | 内置 |
| 重定向处理 | 自动 | 需手动 | 需手动 | 自动 | 自动 |
| 连接池 | 内置 | 部分 | 否 | 内置 | 内置 |
| 性能（同步） | 良好 | 良好 | 良好 | - | 良好 |
| 性能（异步） | - | - | - | 优秀 | 优秀 |

## 14. 总结

requests模块是Python生态系统中最流行的HTTP客户端库，它以其简洁优雅的API和强大的功能赢得了广泛的使用。通过本文档的学习，我们已经掌握了requests模块的核心功能，包括：

- 发送各种HTTP请求（GET、POST、PUT、DELETE等）
- 定制请求（请求头、超时、代理等）
- 会话管理和Cookie处理
- 身份验证（基本认证、摘要认证、OAuth等）
- 文件上传和下载
- 错误处理和重试机制
- 高级特性（JSON处理、重定向处理、请求钩子等）
- 性能优化（连接池、并发请求、响应缓存等）
- 安全最佳实践

requests模块适用于各种HTTP交互场景，从简单的API调用到复杂的网络爬虫，都能胜任。通过遵循文档中的最佳实践，您可以编写高效、可靠、安全的HTTP客户端代码。

如果您需要异步HTTP请求功能，可以考虑使用aiohttp或httpx库，它们提供了类似requests的API，但支持异步IO操作，适合高并发场景。

最后，无论使用哪种HTTP客户端库，都应该尊重目标服务器的使用条款和robots.txt规则，避免对服务器造成不必要的负担。
