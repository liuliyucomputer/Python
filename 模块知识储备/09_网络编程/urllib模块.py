# urllib模块 - Python URL处理与网络请求

Python的`urllib`模块是一个包含多个子模块的包，提供了URL处理、打开URL、发送HTTP请求、处理错误等功能。本文档将详细介绍urllib模块的核心功能、使用方法、最佳实践以及实际应用案例。

## 1. 模块概述

`urllib`模块主要包含以下子模块：

- **urllib.request**: 用于打开URL和发送HTTP请求
- **urllib.error**: 包含urllib.request可能引发的异常
- **urllib.parse**: 用于解析URL
- **urllib.robotparser**: 用于解析robots.txt文件

## 2. urllib.request模块

`urllib.request`模块提供了打开URL的功能，可以用于访问Web资源。它支持各种协议，如HTTP、HTTPS、FTP等，并且提供了一些高级功能，如身份验证、代理支持等。

### 2.1 基本URL打开

#### 2.1.1 urlopen函数

`urlopen`函数是`urllib.request`模块中最基本的函数，用于打开URL并返回一个文件类对象。

```python
import urllib.request

# 基本用法
response = urllib.request.urlopen('https://www.example.com')

# 读取响应内容
data = response.read()
print(f"响应状态码: {response.status}")
print(f"响应原因: {response.reason}")
print(f"响应头: {response.getheaders()}")
print(f"内容长度: {len(data)} 字节")

# 读取部分内容（最多100字节）
partial_data = response.read(100)
print(f"部分内容: {partial_data}")

# 获取特定响应头
content_type = response.getheader('Content-Type')
print(f"Content-Type: {content_type}")
```

#### 2.1.2 Request对象

`Request`类用于创建更复杂的HTTP请求，可以设置请求头、请求方法、请求体等。

```python
import urllib.request

# 创建Request对象
req = urllib.request.Request(
    url='https://www.example.com',
    headers={'User-Agent': 'Mozilla/5.0'},
    method='GET'
)

# 发送请求
with urllib.request.urlopen(req) as response:
    data = response.read()
    print(f"状态码: {response.status}")
    print(f"内容长度: {len(data)} 字节")
```

### 2.2 发送POST请求

```python
import urllib.request
import urllib.parse

# 准备POST数据
post_data = {
    'username': 'testuser',
    'password': 'testpass'
}

# 编码数据
encoded_data = urllib.parse.urlencode(post_data).encode('utf-8')

# 创建Request对象
req = urllib.request.Request(
    url='https://httpbin.org/post',
    data=encoded_data,
    headers={'Content-Type': 'application/x-www-form-urlencoded'},
    method='POST'
)

# 发送请求
with urllib.request.urlopen(req) as response:
    data = response.read()
    print(f"状态码: {response.status}")
    print(f"响应内容: {data.decode('utf-8')}")
```

### 2.3 处理认证

```python
import urllib.request

# 创建密码管理器
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加用户名和密码
# 第一个参数是realm（通常为空字符串）
# 第二个参数是目标URL
# 第三和第四个参数是用户名和密码
password_mgr.add_password(None, 'https://httpbin.org/basic-auth/user/pass', 'user', 'pass')

# 创建认证处理器
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# 创建opener
opener = urllib.request.build_opener(handler)

# 使用opener发送请求
with opener.open('https://httpbin.org/basic-auth/user/pass') as response:
    data = response.read()
    print(f"状态码: {response.status}")
    print(f"响应内容: {data.decode('utf-8')}")

# 或者将opener设置为全局的
try:
    urllib.request.install_opener(opener)
    with urllib.request.urlopen('https://httpbin.org/basic-auth/user/pass') as response:
        data = response.read()
        print(f"使用全局opener - 状态码: {response.status}")
except Exception as e:
    print(f"错误: {e}")
finally:
    # 重置全局opener（可选）
    urllib.request.install_opener(urllib.request.build_opener())
```

### 2.4 使用代理

```python
import urllib.request

# 创建代理处理器
proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://proxy.example.com:8080',
    'https': 'https://proxy.example.com:8080'
})

# 或者使用有认证的代理
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'proxy.example.com:8080', 'proxyuser', 'proxypass')

# 创建opener
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

# 使用opener发送请求
try:
    with opener.open('https://www.example.com') as response:
        data = response.read()
        print(f"状态码: {response.status}")
        print(f"内容长度: {len(data)} 字节")
except Exception as e:
    print(f"代理错误: {e}")
```

### 2.5 处理Cookies

```python
import urllib.request
import http.cookiejar

# 创建CookieJar
cookie_jar = http.cookiejar.CookieJar()

# 创建Cookie处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)

# 创建opener
opener = urllib.request.build_opener(cookie_handler)

# 发送请求（自动处理Cookie）
with opener.open('https://www.example.com') as response:
    print("收到的Cookie:")
    for cookie in cookie_jar:
        print(f"  {cookie.name}={cookie.value}")

# 保存Cookie到文件
filename = 'cookies.txt'
cookie_jar.save(filename)
print(f"Cookie已保存到: {filename}")

# 从文件加载Cookie
new_cookie_jar = http.cookiejar.CookieJar()
new_cookie_jar.load(filename)
print("从文件加载的Cookie:")
for cookie in new_cookie_jar:
    print(f"  {cookie.name}={cookie.value}")
```

### 2.6 超时设置

```python
import urllib.request

try:
    # 设置超时为5秒
    with urllib.request.urlopen('https://www.example.com', timeout=5) as response:
        data = response.read()
        print(f"成功获取内容，长度: {len(data)} 字节")
except urllib.error.URLError as e:
    print(f"超时或URL错误: {e}")
except Exception as e:
    print(f"其他错误: {e}")
```

### 2.7 高级功能

#### 2.7.1 添加重试机制

```python
import urllib.request
import urllib.error
import time

def fetch_with_retry(url, max_retries=3, delay=1):
    """带重试机制的URL获取函数"""
    retries = 0
    while retries <= max_retries:
        try:
            with urllib.request.urlopen(url, timeout=10) as response:
                return response.read()
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            retries += 1
            if retries > max_retries:
                raise
            print(f"尝试 {retries}/{max_retries} 失败: {e}，{delay}秒后重试...")
            time.sleep(delay)
        except Exception as e:
            raise

# 使用示例
try:
    data = fetch_with_retry('https://www.example.com')
    print(f"成功获取内容，长度: {len(data)} 字节")
except Exception as e:
    print(f"所有重试都失败了: {e}")
```

#### 2.7.2 自定义用户代理

```python
import urllib.request

# 创建Request对象，设置自定义User-Agent
req = urllib.request.Request(
    url='https://httpbin.org/user-agent',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
)

with urllib.request.urlopen(req) as response:
    data = response.read()
    print(f"服务器收到的User-Agent: {data.decode('utf-8')}")
```

## 3. urllib.error模块

`urllib.error`模块包含了`urllib.request`可能引发的异常，主要有以下几种：

- **URLError**: 所有URL相关错误的基类
- **HTTPError**: 当HTTP请求返回错误状态码时引发
- **ContentTooShortError**: 当下载的数据少于预期时引发

### 3.1 错误处理示例

```python
import urllib.request
import urllib.error

def handle_errors():
    # 处理HTTPError
    try:
        response = urllib.request.urlopen('https://httpbin.org/status/404')
    except urllib.error.HTTPError as e:
        print(f"HTTP错误: {e.code} - {e.reason}")
        print(f"错误页面: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"其他错误: {e}")
    
    # 处理URLError（网络错误、主机不存在等）
    try:
        response = urllib.request.urlopen('https://nonexistent-domain-123456789.com')
    except urllib.error.URLError as e:
        print(f"URL错误: {e.reason}")
    except Exception as e:
        print(f"其他错误: {e}")
    
    # 综合错误处理
    try:
        response = urllib.request.urlopen('https://httpbin.org/delay/10', timeout=5)
    except urllib.error.HTTPError as e:
        print(f"HTTP错误: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL错误: {e.reason}")
    except Exception as e:
        print(f"未预期的错误: {e}")
    else:
        # 如果没有异常
        print(f"请求成功，状态码: {response.status}")
    finally:
        # 无论是否有异常都会执行
        print("错误处理示例结束")

if __name__ == "__main__":
    handle_errors()
```

## 4. urllib.parse模块

`urllib.parse`模块提供了URL解析和构建的功能，可以分解URL为各个组件，也可以将组件组合成URL。

### 4.1 URL解析函数

#### 4.1.1 urlparse函数

`urlparse`函数将URL字符串解析为组件。

```python
from urllib.parse import urlparse

url = 'https://user:pass@example.com:8080/path;param?query=value#fragment'

# 解析URL
parsed = urlparse(url)

print("URL组件:")
print(f"  scheme: {parsed.scheme}")     # 协议
print(f"  netloc: {parsed.netloc}")     # 网络位置（域名+端口）
print(f"  path: {parsed.path}")         # 路径
print(f"  params: {parsed.params}")     # 参数
print(f"  query: {parsed.query}")       # 查询字符串
print(f"  fragment: {parsed.fragment}") # 片段标识符
print(f"  username: {parsed.username}") # 用户名
print(f"  password: {parsed.password}") # 密码
print(f"  hostname: {parsed.hostname}") # 主机名
print(f"  port: {parsed.port}")         # 端口

# 重新组合URL
reconstructed = parsed.geturl()
print(f"\n重新组合的URL: {reconstructed}")
```

#### 4.1.2 urlsplit函数

`urlsplit`函数与`urlparse`类似，但不解析`params`部分，将其包含在`path`中。

```python
from urllib.parse import urlsplit

url = 'https://user:pass@example.com:8080/path;param?query=value#fragment'

# 解析URL
split = urlsplit(url)

print("URL组件 (urlsplit):")
print(f"  scheme: {split.scheme}")     # 协议
print(f"  netloc: {split.netloc}")     # 网络位置
print(f"  path: {split.path}")         # 路径（包含params）
print(f"  query: {split.query}")       # 查询字符串
print(f"  fragment: {split.fragment}") # 片段标识符

# 重新组合URL
reconstructed = split.geturl()
print(f"\n重新组合的URL: {reconstructed}")
```

#### 4.1.3 parse_qs和parse_qsl函数

这两个函数用于解析查询字符串。

```python
from urllib.parse import parse_qs, parse_qsl

query_string = 'name=John&age=30&city=New+York&hobby=reading&hobby=swimming'

# parse_qs返回字典，值是列表
parsed_dict = parse_qs(query_string)
print("parse_qs结果:")
for key, values in parsed_dict.items():
    print(f"  {key}: {values}")

# parse_qsl返回元组列表
parsed_list = parse_qsl(query_string)
print("\nparse_qsl结果:")
for key, value in parsed_list:
    print(f"  {key}: {value}")
```

### 4.2 URL构建函数

#### 4.2.1 urlunparse函数

`urlunparse`函数将组件组合成URL。

```python
from urllib.parse import urlunparse

# URL组件
scheme = 'https'
netloc = 'example.com'
path = '/path'
params = 'param=value'
query = 'key1=value1&key2=value2'
fragment = 'section1'

# 组合URL
url_components = (scheme, netloc, path, params, query, fragment)
url = urlunparse(url_components)

print(f"构建的URL: {url}")
```

#### 4.2.2 urlunsplit函数

`urlunsplit`函数与`urlunparse`类似，但不包含`params`组件。

```python
from urllib.parse import urlunsplit

# URL组件
scheme = 'https'
netloc = 'example.com'
path = '/path;param=value'
query = 'key1=value1&key2=value2'
fragment = 'section1'

# 组合URL
url_components = (scheme, netloc, path, query, fragment)
url = urlunsplit(url_components)

print(f"构建的URL: {url}")
```

#### 4.2.3 urlencode函数

`urlencode`函数将字典或元组列表编码为查询字符串。

```python
from urllib.parse import urlencode

# 字典形式
params_dict = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York',
    'interests': ['reading', 'swimming']
}

# 编码单个参数
query_string = urlencode(params_dict)
print(f"编码的查询字符串: {query_string}")

# 编码列表参数（需要特殊处理）
params_list = [
    ('name', 'John Doe'),
    ('age', 30),
    ('city', 'New York'),
    ('interest', 'reading'),
    ('interest', 'swimming')
]

query_string_multi = urlencode(params_list)
print(f"编码的多值查询字符串: {query_string_multi}")
```

### 4.3 URL引用和反引用

```python
from urllib.parse import quote, quote_plus, unquote, unquote_plus

# 原始字符串
original = 'Hello World! This is a test with spaces & symbols.'

# quote - 基本URL编码（不编码斜杠等某些字符）
quoted = quote(original)
print(f"quote结果: {quoted}")

# quote_plus - 更严格的编码（将空格编码为+）
quoted_plus = quote_plus(original)
print(f"quote_plus结果: {quoted_plus}")

# unquote - 解码
unquoted = unquote(quoted)
print(f"unquote结果: {unquoted}")

# unquote_plus - 解码（将+解码为空格）
unquoted_plus = unquote_plus(quoted_plus)
print(f"unquote_plus结果: {unquoted_plus}")

# 编码路径部分
path = '/path with spaces/and#symbols?query=value'
encoded_path = quote(path)
print(f"编码路径: {encoded_path}")
```

### 4.4 连接URL

```python
from urllib.parse import urljoin

# 基础URL
base_url = 'https://example.com/path/to/page.html'

# 相对URLs
relative_urls = [
    'next.html',
    '../previous.html',
    '/absolute/path.html',
    'https://another-site.com'
]

print("URL连接结果:")
for rel_url in relative_urls:
    joined = urljoin(base_url, rel_url)
    print(f"  {rel_url} -> {joined}")
```

## 5. urllib.robotparser模块

`urllib.robotparser`模块用于解析网站的robots.txt文件，检查哪些URL可以被抓取，哪些不可以。

### 5.1 基本用法

```python
import urllib.robotparser

def check_robot_rules():
    # 创建RobotFileParser对象
    rp = urllib.robotparser.RobotFileParser()
    
    # 设置robots.txt的URL
    rp.set_url('https://www.python.org/robots.txt')
    
    # 读取和解析robots.txt
    rp.read()
    
    # 检查是否允许抓取特定URL
    user_agent = 'mybot'
    
    urls_to_check = [
        'https://www.python.org/',
        'https://www.python.org/download/',
        'https://www.python.org/admin/',  # 可能被禁止
        'https://www.python.org/robots.txt'
    ]
    
    print(f"用户代理 '{user_agent}' 的抓取权限:")
    for url in urls_to_check:
        can_fetch = rp.can_fetch(user_agent, url)
        print(f"  {url}: {'允许' if can_fetch else '禁止'}")
    
    # 获取抓取延迟
    crawl_delay = rp.crawl_delay(user_agent)
    print(f"\n抓取延迟: {crawl_delay} 秒")
    
    # 获取请求率
    request_rate = rp.request_rate(user_agent)
    if request_rate:
        print(f"请求率: {request_rate.requests} 请求/{request_rate.seconds} 秒")
    else:
        print("没有指定请求率")

if __name__ == "__main__":
    check_robot_rules()
```

### 5.2 示例：带robots.txt检查的爬虫

```python
import urllib.request
import urllib.error
import urllib.parse
import urllib.robotparser
import time
from bs4 import BeautifulSoup  # 需要安装：pip install beautifulsoup4

def check_robots(url):
    """检查URL是否可以被抓取"""
    # 获取robots.txt的URL
    parsed_url = urllib.parse.urlparse(url)
    robots_url = urllib.parse.urljoin(f"{parsed_url.scheme}://{parsed_url.netloc}", '/robots.txt')
    
    # 创建并解析RobotFileParser
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    
    try:
        rp.read()
        user_agent = 'MyExampleBot/1.0'
        
        # 检查是否允许抓取
        if rp.can_fetch(user_agent, url):
            # 获取抓取延迟
            delay = rp.crawl_delay(user_agent)
            if delay:
                print(f"根据robots.txt，需要延迟 {delay} 秒")
                time.sleep(delay)
            return True
        else:
            print(f"根据robots.txt，禁止抓取: {url}")
            return False
    except Exception as e:
        print(f"无法解析robots.txt: {e}")
        # 如果无法解析robots.txt，默认不抓取
        return False

def simple_crawler(start_url, max_pages=5):
    """简单的爬虫，遵守robots.txt规则"""
    visited = set()
    to_visit = [start_url]
    crawled = 0
    
    while to_visit and crawled < max_pages:
        url = to_visit.pop(0)
        
        # 避免重复访问
        if url in visited:
            continue
        
        # 检查robots.txt
        if not check_robots(url):
            continue
        
        try:
            print(f"\n正在抓取: {url}")
            
            # 发送请求
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'MyExampleBot/1.0'}
            )
            
            with urllib.request.urlopen(req, timeout=10) as response:
                # 只处理HTML内容
                content_type = response.getheader('Content-Type', '')
                if 'text/html' not in content_type:
                    print(f"跳过非HTML内容: {content_type}")
                    visited.add(url)
                    continue
                
                # 读取内容
                html = response.read().decode('utf-8', errors='ignore')
                
                # 简单解析，提取链接
                soup = BeautifulSoup(html, 'html.parser')
                
                # 获取页面标题
                title = soup.title.string if soup.title else "无标题"
                print(f"页面标题: {title}")
                
                # 提取所有链接
                for link in soup.find_all('a'):
                    href = link.get('href')
                    if href:
                        # 解析相对链接
                        absolute_url = urllib.parse.urljoin(url, href)
                        
                        # 检查是否是同一网站的链接
                        parsed_start = urllib.parse.urlparse(start_url)
                        parsed_link = urllib.parse.urlparse(absolute_url)
                        
                        if parsed_link.netloc == parsed_start.netloc:
                            if absolute_url not in visited and absolute_url not in to_visit:
                                to_visit.append(absolute_url)
                
                # 标记为已访问
                visited.add(url)
                crawled += 1
                
                # 遵守爬虫礼仪，避免过快请求
                time.sleep(1)
                
        except urllib.error.HTTPError as e:
            print(f"HTTP错误: {e.code} - {e.reason}")
            visited.add(url)
        except urllib.error.URLError as e:
            print(f"URL错误: {e.reason}")
        except Exception as e:
            print(f"抓取错误: {e}")
    
    print(f"\n爬虫完成，共抓取了 {crawled} 个页面")
    print(f"已访问的URL: {len(visited)}")
    print(f"待访问的URL: {len(to_visit)}")

if __name__ == "__main__":
    # 示例：爬取Python文档网站
    simple_crawler('https://docs.python.org/3/', max_pages=3)
```

## 6. 实际应用示例

### 6.1 文件下载器

```python
import urllib.request
import urllib.error
import os
import time

def download_file(url, save_path=None, chunk_size=8192, show_progress=True):
    """
    下载文件并显示进度
    
    参数:
        url: 要下载的文件URL
        save_path: 保存路径，默认从URL提取文件名
        chunk_size: 下载块大小
        show_progress: 是否显示下载进度
    """
    # 如果没有指定保存路径，从URL提取文件名
    if save_path is None:
        filename = os.path.basename(urllib.parse.urlparse(url).path)
        if not filename:
            filename = 'downloaded_file'
        save_path = os.path.join(os.getcwd(), filename)
    
    try:
        # 发送请求获取文件信息
        with urllib.request.urlopen(url) as response:
            # 获取文件大小
            file_size = int(response.getheader('Content-Length', 0))
            print(f"开始下载: {url}")
            print(f"保存到: {save_path}")
            print(f"文件大小: {file_size:,} 字节")
            
            # 创建保存目录
            os.makedirs(os.path.dirname(os.path.abspath(save_path)), exist_ok=True)
            
            # 开始时间
            start_time = time.time()
            downloaded_size = 0
            
            # 写入文件
            with open(save_path, 'wb') as f:
                while True:
                    chunk = response.read(chunk_size)
                    if not chunk:
                        break
                    
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    
                    # 显示进度
                    if show_progress and file_size > 0:
                        percent = (downloaded_size / file_size) * 100
                        elapsed_time = time.time() - start_time
                        speed = downloaded_size / elapsed_time if elapsed_time > 0 else 0
                        
                        # 估计剩余时间
                        if speed > 0:
                            remaining_time = (file_size - downloaded_size) / speed
                            remaining_str = f"ETA: {remaining_time:.1f}s"
                        else:
                            remaining_str = "ETA: N/A"
                        
                        # 使用回车符覆盖当前行
                        print(f"\r下载进度: {percent:.1f}% ({downloaded_size:,}/{file_size:,} bytes) "
                              f"速度: {speed/1024:.1f} KB/s {remaining_str}", end='')
            
            # 完成下载
            elapsed_time = time.time() - start_time
            print(f"\n下载完成！耗时: {elapsed_time:.1f} 秒")
            print(f"平均速度: {file_size / elapsed_time / 1024:.1f} KB/s")
            
            return save_path
    
    except urllib.error.HTTPError as e:
        print(f"HTTP错误: {e.code} - {e.reason}")
        raise
    except urllib.error.URLError as e:
        print(f"URL错误: {e.reason}")
        raise
    except Exception as e:
        print(f"下载错误: {e}")
        raise

def batch_download(urls, directory=None):
    """
    批量下载文件
    
    参数:
        urls: URL列表
        directory: 保存目录
    """
    if directory is not None:
        os.makedirs(directory, exist_ok=True)
    
    results = {}
    
    for i, url in enumerate(urls, 1):
        print(f"\n=== 下载 {i}/{len(urls)} ===")
        try:
            save_path = os.path.join(directory, os.path.basename(urllib.parse.urlparse(url).path)) if directory else None
            path = download_file(url, save_path)
            results[url] = {'success': True, 'path': path}
        except Exception as e:
            results[url] = {'success': False, 'error': str(e)}
    
    # 打印汇总信息
    print("\n=== 下载汇总 ===")
    successful = sum(1 for r in results.values() if r['success'])
    print(f"成功: {successful}/{len(urls)}")
    
    if successful < len(urls):
        print("\n失败的下载:")
        for url, result in results.items():
            if not result['success']:
                print(f"  {url}: {result['error']}")
    
    return results

# 示例用法
if __name__ == "__main__":
    # 单个文件下载示例
    # download_file('https://www.example.com/sample.zip')
    
    # 批量下载示例
    sample_urls = [
        'https://www.example.com/file1.txt',
        'https://www.example.com/file2.txt',
        'https://httpbin.org/image/jpeg'  # 这个是有效的，可以下载测试
    ]
    batch_download(sample_urls, directory='downloads')
```

### 6.2 简单的API客户端

```python
import urllib.request
import urllib.parse
import urllib.error
import json

class SimpleAPIClient:
    def __init__(self, base_url, default_headers=None):
        """
        初始化API客户端
        
        参数:
            base_url: API基础URL
            default_headers: 默认请求头
        """
        self.base_url = base_url.rstrip('/')
        self.default_headers = default_headers or {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    
    def _build_url(self, endpoint, params=None):
        """构建完整的URL"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        # 添加查询参数
        if params:
            query_string = urllib.parse.urlencode(params)
            url = f"{url}?{query_string}"
        
        return url
    
    def _prepare_headers(self, custom_headers=None):
        """准备请求头"""
        headers = self.default_headers.copy()
        if custom_headers:
            headers.update(custom_headers)
        return headers
    
    def _parse_response(self, response):
        """解析响应"""
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
            'headers': dict(response.getheaders()),
            'data': data
        }
    
    def get(self, endpoint, params=None, headers=None):
        """发送GET请求"""
        url = self._build_url(endpoint, params)
        req_headers = self._prepare_headers(headers)
        
        req = urllib.request.Request(url, headers=req_headers, method='GET')
        
        try:
            with urllib.request.urlopen(req) as response:
                return self._parse_response(response)
        except urllib.error.HTTPError as e:
            # 返回错误响应
            error_response = self._parse_response(e)
            error_response['error'] = str(e)
            return error_response
        except urllib.error.URLError as e:
            raise Exception(f"网络错误: {e.reason}")
    
    def post(self, endpoint, data=None, json_data=None, headers=None):
        """发送POST请求"""
        url = self._build_url(endpoint)
        req_headers = self._prepare_headers(headers)
        body = None
        
        # 准备请求体
        if json_data is not None:
            body = json.dumps(json_data).encode('utf-8')
            req_headers['Content-Type'] = 'application/json'
        elif data is not None:
            if isinstance(data, dict):
                body = urllib.parse.urlencode(data).encode('utf-8')
                req_headers['Content-Type'] = 'application/x-www-form-urlencoded'
            else:
                body = str(data).encode('utf-8')
        
        req = urllib.request.Request(url, data=body, headers=req_headers, method='POST')
        
        try:
            with urllib.request.urlopen(req) as response:
                return self._parse_response(response)
        except urllib.error.HTTPError as e:
            error_response = self._parse_response(e)
            error_response['error'] = str(e)
            return error_response
        except urllib.error.URLError as e:
            raise Exception(f"网络错误: {e.reason}")
    
    def put(self, endpoint, data=None, json_data=None, headers=None):
        """发送PUT请求"""
        url = self._build_url(endpoint)
        req_headers = self._prepare_headers(headers)
        body = None
        
        # 准备请求体
        if json_data is not None:
            body = json.dumps(json_data).encode('utf-8')
            req_headers['Content-Type'] = 'application/json'
        elif data is not None:
            if isinstance(data, dict):
                body = urllib.parse.urlencode(data).encode('utf-8')
                req_headers['Content-Type'] = 'application/x-www-form-urlencoded'
            else:
                body = str(data).encode('utf-8')
        
        req = urllib.request.Request(url, data=body, headers=req_headers, method='PUT')
        
        try:
            with urllib.request.urlopen(req) as response:
                return self._parse_response(response)
        except urllib.error.HTTPError as e:
            error_response = self._parse_response(e)
            error_response['error'] = str(e)
            return error_response
        except urllib.error.URLError as e:
            raise Exception(f"网络错误: {e.reason}")
    
    def delete(self, endpoint, headers=None):
        """发送DELETE请求"""
        url = self._build_url(endpoint)
        req_headers = self._prepare_headers(headers)
        
        req = urllib.request.Request(url, headers=req_headers, method='DELETE')
        
        try:
            with urllib.request.urlopen(req) as response:
                return self._parse_response(response)
        except urllib.error.HTTPError as e:
            error_response = self._parse_response(e)
            error_response['error'] = str(e)
            return error_response
        except urllib.error.URLError as e:
            raise Exception(f"网络错误: {e.reason}")
    
    def set_auth(self, username, password):
        """设置基本认证"""
        import base64
        auth_string = f"{username}:{password}"
        encoded_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        self.default_headers['Authorization'] = f'Basic {encoded_auth}'
    
    def set_bearer_token(self, token):
        """设置Bearer令牌认证"""
        self.default_headers['Authorization'] = f'Bearer {token}'

# 示例用法
if __name__ == "__main__":
    # 创建API客户端
    client = SimpleAPIClient('https://jsonplaceholder.typicode.com')
    
    print("\n=== 测试GET请求 ===")
    # 发送GET请求
    response = client.get('posts/1')
    print(f"状态码: {response['status_code']}")
    print(f"数据: {response['data']}")
    
    print("\n=== 测试带参数的GET请求 ===")
    # 带参数的GET请求
    response = client.get('posts', params={'userId': 1})
    print(f"状态码: {response['status_code']}")
    if isinstance(response['data'], list):
        print(f"返回了 {len(response['data'])} 条记录")
    
    print("\n=== 测试POST请求 ===")
    # 发送POST请求
    post_data = {
        'title': '测试标题',
        'body': '测试内容',
        'userId': 1
    }
    response = client.post('posts', json_data=post_data)
    print(f"状态码: {response['status_code']}")
    print(f"创建的记录: {response['data']}")
```

### 6.3 网页内容抓取和解析

```python
import urllib.request
import urllib.error
import re
from bs4 import BeautifulSoup  # 需要安装：pip install beautifulsoup4

def fetch_webpage(url, user_agent=None):
    """获取网页内容"""
    headers = {}
    if user_agent:
        headers['User-Agent'] = user_agent
    else:
        headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    
    req = urllib.request.Request(url, headers=headers)
    
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            # 获取内容类型和编码
            content_type = response.getheader('Content-Type', '')
            charset = 'utf-8'  # 默认编码
            
            # 尝试从Content-Type头中提取编码
            charset_match = re.search(r'charset=([^;]+)', content_type)
            if charset_match:
                charset = charset_match.group(1)
            
            # 读取内容并解码
            html = response.read()
            try:
                return html.decode(charset)
            except UnicodeDecodeError:
                # 如果指定的编码失败，尝试使用utf-8
                return html.decode('utf-8', errors='replace')
    except urllib.error.HTTPError as e:
        print(f"HTTP错误: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"URL错误: {e.reason}")
        return None
    except Exception as e:
        print(f"抓取错误: {e}")
        return None

def extract_links(html, base_url):
    """从HTML中提取链接"""
    if not html:
        return []
    
    links = []
    
    # 使用正则表达式提取链接（简单方法）
    href_pattern = re.compile(r'href=["\'](.*?)["\']', re.IGNORECASE)
    matches = href_pattern.findall(html)
    
    for link in matches:
        # 过滤JavaScript链接和锚点
        if link.startswith('javascript:') or link.startswith('#'):
            continue
        
        # 构建绝对URL
        from urllib.parse import urljoin
        absolute_url = urljoin(base_url, link)
        links.append(absolute_url)
    
    return links

def extract_links_bs4(html, base_url):
    """使用BeautifulSoup从HTML中提取链接"""
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and not href.startswith(('javascript:', '#')):
            from urllib.parse import urljoin
            absolute_url = urljoin(base_url, href)
            links.append(absolute_url)
    
    return links

def extract_images(html, base_url):
    """使用BeautifulSoup从HTML中提取图片链接"""
    if not html:
        return []
    
    soup = BeautifulSoup(html, 'html.parser')
    images = []
    
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            from urllib.parse import urljoin
            absolute_url = urljoin(base_url, src)
            alt = img.get('alt', '无alt文本')
            images.append({
                'url': absolute_url,
                'alt': alt,
                'width': img.get('width'),
                'height': img.get('height')
            })
    
    return images

def extract_metadata(html):
    """提取网页元数据"""
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
    
    # 提取charset
    charset_meta = soup.find('meta', attrs={'charset': True})
    if charset_meta:
        metadata['charset'] = charset_meta.get('charset')
    else:
        charset_http_equiv = soup.find('meta', attrs={'http-equiv': 'Content-Type'})
        if charset_http_equiv and charset_http_equiv.get('content'):
            charset_match = re.search(r'charset=([^;]+)', charset_http_equiv.get('content'))
            if charset_match:
                metadata['charset'] = charset_match.group(1)
    
    # 提取视口设置
    viewport = soup.find('meta', attrs={'name': 'viewport'})
    if viewport and viewport.get('content'):
        metadata['viewport'] = viewport.get('content')
    
    return metadata

# 示例用法
if __name__ == "__main__":
    url = 'https://www.python.org/'
    
    print(f"正在抓取: {url}")
    html = fetch_webpage(url)
    
    if html:
        print("\n=== 提取的元数据 ===")
        metadata = extract_metadata(html)
        for key, value in metadata.items():
            print(f"{key}: {value}")
        
        print("\n=== 提取的图片 ===")
        images = extract_images(html, url)
        print(f"找到 {len(images)} 张图片")
        for i, img in enumerate(images[:5]):  # 只显示前5张
            print(f"  {i+1}. {img['url']} (alt: {img['alt']})")
        
        if len(images) > 5:
            print(f"  ... 还有 {len(images) - 5} 张图片")
        
        print("\n=== 提取的链接 ===")
        links = extract_links_bs4(html, url)
        print(f"找到 {len(links)} 个链接")
        for i, link in enumerate(links[:5]):  # 只显示前5个
            print(f"  {i+1}. {link}")
        
        if len(links) > 5:
            print(f"  ... 还有 {len(links) - 5} 个链接")
```

## 7. 安全考虑

### 7.1 安全最佳实践

1. **验证URL**: 始终验证和净化用户提供的URL，避免SSRF（服务器端请求伪造）攻击。

```python
def validate_url(url):
    """验证URL的基本安全检查"""
    from urllib.parse import urlparse
    
    parsed = urlparse(url)
    
    # 检查协议
    if parsed.scheme not in ('http', 'https'):
        return False
    
    # 检查主机名（防止访问内部网络）
    # 这是一个简单的示例，实际情况可能更复杂
    host = parsed.hostname
    if host:
        # 禁止访问内部地址
        internal_patterns = [
            r'^127\.',  # localhost
            r'^10\.',   # private IP
            r'^172\.(?:1[6-9]|2\d|3[01])\.',
            r'^192\.168\.',
            r'^localhost$',
            r'^0\.0\.0\.0$',
            r'^::1$'  # IPv6 localhost
        ]
        
        import re
        for pattern in internal_patterns:
            if re.match(pattern, host, re.IGNORECASE):
                return False
    
    return True

# 使用示例
user_url = input("请输入URL: ")
if validate_url(user_url):
    print("URL看起来安全，可以处理")
else:
    print("URL不安全，拒绝处理")
```

2. **设置超时**: 始终设置合理的超时，避免请求挂起。

3. **限制重定向**: 限制重定向次数，防止无限重定向攻击。

```python
import urllib.request
import urllib.error

def fetch_with_redirect_limit(url, max_redirects=5):
    """限制重定向次数的URL获取"""
    class RedirectLimiter(urllib.request.HTTPRedirectHandler):
        def __init__(self, max_redirects):
            self.max_redirects = max_redirects
            self.redirect_count = 0
        
        def http_error_302(self, req, fp, code, msg, headers):
            self.redirect_count += 1
            if self.redirect_count > self.max_redirects:
                raise urllib.error.URLError(f"重定向次数超过限制 ({self.max_redirects})")
            return super().http_error_302(req, fp, code, msg, headers)
        
        # 也处理其他重定向状态码
        http_error_301 = http_error_302
        http_error_303 = http_error_302
        http_error_307 = http_error_302
        http_error_308 = http_error_302
    
    # 创建自定义opener
    opener = urllib.request.build_opener(RedirectLimiter(max_redirects))
    
    try:
        with opener.open(url, timeout=10) as response:
            return response.read()
    except urllib.error.URLError as e:
        print(f"错误: {e}")
        raise

# 使用示例
try:
    data = fetch_with_redirect_limit('https://example.com', max_redirects=3)
    print(f"成功获取内容，长度: {len(data)} 字节")
except Exception as e:
    print(f"获取失败: {e}")
```

4. **验证SSL证书**: 确保验证SSL证书，避免中间人攻击。

```python
import urllib.request
import ssl

def fetch_with_ssl_validation(url):
    """带SSL验证的URL获取"""
    # 创建SSL上下文
    context = ssl.create_default_context()
    
    # 设置验证模式
    context.check_hostname = True
    context.verify_mode = ssl.CERT_REQUIRED
    
    # 创建HTTPS处理器
    https_handler = urllib.request.HTTPSHandler(context=context)
    
    # 创建opener
    opener = urllib.request.build_opener(https_handler)
    
    try:
        with opener.open(url, timeout=10) as response:
            return response.read()
    except urllib.error.URLError as e:
        print(f"SSL错误: {e}")
        raise

# 使用示例
try:
    data = fetch_with_ssl_validation('https://www.python.org')
    print(f"成功获取内容，长度: {len(data)} 字节")
except Exception as e:
    print(f"获取失败: {e}")
```

5. **限制请求大小**: 限制请求体大小，防止DoS攻击。

```python
def fetch_with_size_limit(url, max_size=10*1024*1024):  # 默认10MB
    """限制响应大小的URL获取"""
    response = urllib.request.urlopen(url, timeout=10)
    
    # 检查Content-Length头
    content_length = response.getheader('Content-Length')
    if content_length:
        try:
            if int(content_length) > max_size:
                response.close()
                raise Exception(f"响应大小 ({content_length} 字节) 超过限制 ({max_size} 字节)")
        except ValueError:
            pass  # Content-Length不是有效数字，继续处理
    
    # 读取内容时限制大小
    data = b''
    chunk_size = 8192
    
    while True:
        chunk = response.read(chunk_size)
        if not chunk:
            break
        
        if len(data) + len(chunk) > max_size:
            response.close()
            raise Exception(f"响应大小超过限制 ({max_size} 字节)")
        
        data += chunk
    
    return data

# 使用示例
try:
    data = fetch_with_size_limit('https://www.example.com', max_size=1024*1024)  # 限制为1MB
    print(f"成功获取内容，长度: {len(data)} 字节")
except Exception as e:
    print(f"获取失败: {e}")
```

## 8. 性能优化

### 8.1 连接复用

使用`HTTPConnection`的连接复用功能可以提高性能，尤其是在需要发送多个请求到同一服务器时。

```python
import http.client
import time

def reuse_connection_example():
    # 创建连接
    conn = http.client.HTTPSConnection('www.python.org')
    
    start_time = time.time()
    
    # 发送多个请求，复用同一个连接
    for i in range(5):
        conn.request('GET', f'/blog/?page={i+1}')
        response = conn.getresponse()
        # 读取响应内容（必须读取，否则连接不能重用）
        data = response.read()
        print(f"请求 {i+1}: 状态码 {response.status}, 内容长度 {len(data)} 字节")
    
    # 关闭连接
    conn.close()
    
    reuse_time = time.time() - start_time
    print(f"复用连接总耗时: {reuse_time:.2f} 秒")
    
    # 对比：每次都创建新连接
    start_time = time.time()
    
    for i in range(5):
        conn = http.client.HTTPSConnection('www.python.org')
        conn.request('GET', f'/blog/?page={i+1}')
        response = conn.getresponse()
        data = response.read()
        conn.close()
        print(f"新连接请求 {i+1}: 状态码 {response.status}, 内容长度 {len(data)} 字节")
    
    new_conn_time = time.time() - start_time
    print(f"新连接总耗时: {new_conn_time:.2f} 秒")
    
    print(f"性能提升: {(new_conn_time - reuse_time) / new_conn_time * 100:.1f}%")

# 使用示例
if __name__ == "__main__":
    reuse_connection_example()
```

### 8.2 多线程并发请求

对于需要发送大量请求的情况，可以使用多线程来提高效率。

```python
import urllib.request
import concurrent.futures
import time

def fetch_url(url):
    """获取单个URL的内容"""
    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()
            return url, response.status, len(data)
    except Exception as e:
        return url, None, str(e)

def concurrent_fetch(urls, max_workers=10):
    """并发获取多个URL"""
    results = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # 提交所有请求
        future_to_url = {executor.submit(fetch_url, url): url for url in urls}
        
        # 收集结果
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                url, status, result = future.result()
                results.append((url, status, result))
            except Exception as e:
                results.append((url, None, str(e)))
    
    return results

# 使用示例
if __name__ == "__main__":
    # 示例URL列表
    urls = [
        'https://www.python.org/',
        'https://docs.python.org/',
        'https://pypi.org/',
        'https://numpy.org/',
        'https://pandas.pydata.org/',
        'https://scikit-learn.org/',
        'https://matplotlib.org/',
        'https://flask.palletsprojects.com/',
        'https://django.org/',
        'https://requests.readthedocs.io/'
    ]
    
    print("\n=== 串行请求 ===")
    start_time = time.time()
    
    serial_results = []
    for url in urls:
        result = fetch_url(url)
        serial_results.append(result)
    
    serial_time = time.time() - start_time
    print(f"串行请求总耗时: {serial_time:.2f} 秒")
    
    print("\n=== 并发请求 ===")
    start_time = time.time()
    
    concurrent_results = concurrent_fetch(urls, max_workers=5)
    
    concurrent_time = time.time() - start_time
    print(f"并发请求总耗时: {concurrent_time:.2f} 秒")
    
    print(f"\n性能提升: {(serial_time - concurrent_time) / serial_time * 100:.1f}%")
    
    print("\n=== 请求结果 ===")
    for url, status, result in concurrent_results:
        if status:
            print(f"{url}: 状态码 {status}, 内容长度 {result} 字节")
        else:
            print(f"{url}: 失败 - {result}")
```

### 8.3 缓存响应

对于频繁访问的相同资源，可以实现缓存机制来提高性能。

```python
import urllib.request
import urllib.error
import hashlib
import os
import time

def get_cache_key(url):
    """为URL生成缓存键"""
    return hashlib.md5(url.encode('utf-8')).hexdigest()

def get_cached_response(url, cache_dir='.cache', max_age=3600):
    """获取缓存的响应，如果没有或过期则重新获取"""
    # 创建缓存目录
    os.makedirs(cache_dir, exist_ok=True)
    
    # 生成缓存文件名
    cache_key = get_cache_key(url)
    cache_file = os.path.join(cache_dir, cache_key)
    
    # 检查缓存是否存在且有效
    if os.path.exists(cache_file):
        cache_time = os.path.getmtime(cache_file)
        current_time = time.time()
        
        if current_time - cache_time < max_age:
            print(f"使用缓存: {url}")
            with open(cache_file, 'rb') as f:
                return f.read()
        else:
            print(f"缓存已过期，重新获取: {url}")
    
    # 获取新内容
    try:
        print(f"请求新内容: {url}")
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()
            
            # 保存到缓存
            with open(cache_file, 'wb') as f:
                f.write(data)
            
            return data
    except urllib.error.URLError as e:
        print(f"请求失败: {e}")
        # 如果请求失败，尝试返回过期的缓存
        if os.path.exists(cache_file):
            print(f"使用过期缓存: {url}")
            with open(cache_file, 'rb') as f:
                return f.read()
        raise

# 使用示例
if __name__ == "__main__":
    url = 'https://www.python.org/'
    
    # 第一次请求（缓存不存在）
    start_time = time.time()
    data1 = get_cached_response(url, max_age=60)
    time1 = time.time() - start_time
    print(f"第一次请求耗时: {time1:.2f} 秒")
    
    # 第二次请求（使用缓存）
    start_time = time.time()
    data2 = get_cached_response(url, max_age=60)
    time2 = time.time() - start_time
    print(f"第二次请求耗时: {time2:.2f} 秒")
    
    print(f"缓存提升: {(time1 - time2) / time1 * 100:.1f}%")
    print(f"内容相同: {data1 == data2}")
```

## 9. 常见问题与解决方案

### 9.1 URL相关问题

**问题**: URL编码错误
**解决方案**:
- 使用`urllib.parse.quote()`和`urllib.parse.quote_plus()`正确编码URL
- 特别注意中文字符和特殊字符的编码

**问题**: URL解析错误
**解决方案**:
- 使用`urllib.parse.urlparse()`或`urllib.parse.urlsplit()`正确解析URL
- 检查URL格式是否符合标准

### 9.2 请求相关问题

**问题**: 403 Forbidden错误
**解决方案**:
- 设置合适的User-Agent头
- 检查是否需要认证
- 查看网站robots.txt规则

**问题**: 404 Not Found错误
**解决方案**:
- 检查URL是否正确
- 确认资源是否存在
- 处理重定向

**问题**: 请求超时
**解决方案**:
- 设置合理的超时值
- 实现重试机制
- 检查网络连接

### 9.3 编码问题

**问题**: 中文显示乱码
**解决方案**:
- 从Content-Type头中提取正确的编码
- 使用正确的编码解码响应内容
- 对于未知编码，尝试常见的编码如utf-8、gbk等

**问题**: UnicodeDecodeError
**解决方案**:
- 使用errors参数，如`decode('utf-8', errors='replace')`
- 尝试多种编码直到成功

## 10. 总结

Python的`urllib`模块是一个功能强大的标准库，提供了URL处理和HTTP通信的核心功能。通过本文档的介绍，我们了解了`urllib`的各个子模块及其用法：

- **urllib.request**: 提供打开URL和发送HTTP请求的功能
- **urllib.error**: 处理URL请求可能出现的异常
- **urllib.parse**: 解析和构建URL
- **urllib.robotparser**: 解析robots.txt文件

`urllib`模块虽然功能强大，但在处理复杂的HTTP请求时可能会显得有些繁琐。对于更高级的HTTP客户端功能，推荐使用第三方库如`requests`，它提供了更简洁、更人性化的API。不过，作为Python标准库的一部分，`urllib`在许多场景下仍然是一个可靠的选择，特别是在不能安装第三方库的环境中。

在使用`urllib`时，我们应该遵循网络编程的最佳实践，如设置超时、处理异常、验证输入、遵守robots协议等，以确保代码的稳定性、安全性和效率。