# concurrent.futures模块详解

concurrent.futures模块是Python标准库中用于异步执行可调用对象的高级接口。它提供了一个统一的API来管理线程池和进程池，简化了并发编程的复杂性。

## 模块概述

concurrent.futures模块主要提供以下功能：

- 线程池执行器（ThreadPoolExecutor）：用于多线程编程
- 进程池执行器（ProcessPoolExecutor）：用于多进程编程
- 异步任务提交和结果获取
- 任务取消和超时处理
- 任务完成通知
- 异常处理

## 基本概念

在使用concurrent.futures模块之前，需要了解几个基本概念：

1. **执行器（Executor）**: 管理和重用线程或进程的抽象类
2. **线程池执行器（ThreadPoolExecutor）**: 管理线程池的执行器
3. **进程池执行器（ProcessPoolExecutor）**: 管理进程池的执行器
4. **未来对象（Future）**: 表示异步执行的结果
5. **任务（Task）**: 提交给执行器的可调用对象
6. **工作线程/进程（Worker）**: 执行任务的线程或进程

## 基本用法

### 线程池执行器（ThreadPoolExecutor）

```python
import concurrent.futures
import time
import threading

def task(n):
    """简单任务函数"""
    print(f"任务 {n} 开始执行，线程ID: {threading.current_thread().name}")
    time.sleep(1)
    print(f"任务 {n} 执行完毕，线程ID: {threading.current_thread().name}")
    return n * n

# 创建线程池执行器，最多使用3个线程
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务并获取Future对象
    futures = [executor.submit(task, i) for i in range(10)]
    
    # 遍历Future对象获取结果
    for future in concurrent.futures.as_completed(futures):
        try:
            # 获取任务结果
            result = future.result()
            print(f"任务结果: {result}")
        except Exception as e:
            print(f"任务异常: {e}")

print("所有任务执行完毕")
```

### 进程池执行器（ProcessPoolExecutor）

```python
import concurrent.futures
import time
import os

def task(n):
    """简单任务函数"""
    print(f"任务 {n} 开始执行，进程ID: {os.getpid()}")
    time.sleep(1)
    print(f"任务 {n} 执行完毕，进程ID: {os.getpid()}")
    return n * n

# 创建进程池执行器，最多使用3个进程
with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    # 提交任务并获取Future对象
    futures = [executor.submit(task, i) for i in range(10)]
    
    # 遍历Future对象获取结果
    for future in concurrent.futures.as_completed(futures):
        try:
            # 获取任务结果
            result = future.result()
            print(f"任务结果: {result}")
        except Exception as e:
            print(f"任务异常: {e}")

print("所有任务执行完毕")
```

### 使用map方法

```python
import concurrent.futures
import time

def task(n):
    """简单任务函数"""
    print(f"任务 {n} 开始执行")
    time.sleep(1)
    print(f"任务 {n} 执行完毕")
    return n * n

# 使用线程池的map方法
print("=== 使用ThreadPoolExecutor.map ===")
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # map方法返回的结果顺序与输入顺序相同
    results = executor.map(task, range(10))
    
    # 遍历结果
    for result in results:
        print(f"任务结果: {result}")

# 使用进程池的map方法
print("\n=== 使用ProcessPoolExecutor.map ===")
with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    # map方法返回的结果顺序与输入顺序相同
    results = executor.map(task, range(10))
    
    # 遍历结果
    for result in results:
        print(f"任务结果: {result}")

print("所有任务执行完毕")
```

### 使用submit和result方法

```python
import concurrent.futures
import time

def task(n):
    """简单任务函数"""
    print(f"任务 {n} 开始执行")
    time.sleep(1)
    print(f"任务 {n} 执行完毕")
    return n * n

# 使用线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交单个任务
    future = executor.submit(task, 5)
    
    print("等待任务完成...")
    
    # 获取任务结果，会阻塞直到任务完成
    result = future.result()
    
    print(f"任务结果: {result}")

print("所有任务执行完毕")
```

## 高级用法

### 任务取消

```python
import concurrent.futures
import time

def task(n):
    """长时间运行的任务函数"""
    print(f"任务 {n} 开始执行")
    time.sleep(5)
    print(f"任务 {n} 执行完毕")
    return n * n

# 使用线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    future = executor.submit(task, 5)
    
    print("等待1秒后尝试取消任务...")
    time.sleep(1)
    
    # 尝试取消任务
    if future.cancel():
        print("任务已成功取消")
    else:
        print("任务取消失败，可能已经开始执行")
        
        # 等待任务完成并获取结果
        result = future.result()
        print(f"任务结果: {result}")

print("所有任务执行完毕")
```

### 超时处理

```python
import concurrent.futures
import time

def task(n):
    """长时间运行的任务函数"""
    print(f"任务 {n} 开始执行")
    time.sleep(5)
    print(f"任务 {n} 执行完毕")
    return n * n

# 使用线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    future = executor.submit(task, 5)
    
    print("等待3秒获取结果...")
    
    try:
        # 尝试获取任务结果，最多等待3秒
        result = future.result(timeout=3)
        print(f"任务结果: {result}")
    except concurrent.futures.TimeoutError:
        print("获取结果超时")
        
        # 尝试取消任务
        if future.cancel():
            print("任务已成功取消")
        else:
            print("任务取消失败，可能已经开始执行")

print("所有任务执行完毕")
```

### 异常处理

```python
import concurrent.futures
import time

def task(n):
    """可能抛出异常的任务函数"""
    print(f"任务 {n} 开始执行")
    time.sleep(1)
    
    if n % 2 == 0:
        # 偶数任务抛出异常
        raise ValueError(f"任务 {n} 是偶数，抛出异常")
    
    print(f"任务 {n} 执行完毕")
    return n * n

# 使用线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 提交任务
    futures = [executor.submit(task, i) for i in range(10)]
    
    # 遍历Future对象获取结果
    for future in concurrent.futures.as_completed(futures):
        try:
            # 获取任务结果
            result = future.result()
            print(f"任务结果: {result}")
        except Exception as e:
            print(f"任务异常: {e}")

print("所有任务执行完毕")
```

### 带参数的任务

```python
import concurrent.futures
import time

def task(n, delay):
    """带参数的任务函数"""
    print(f"任务 {n} 开始执行，延迟 {delay} 秒")
    time.sleep(delay)
    print(f"任务 {n} 执行完毕")
    return n * delay

# 使用线程池
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    # 方法1: 使用submit传递多个参数
    future1 = executor.submit(task, 5, 2)
    print(f"任务1结果: {future1.result()}")
    
    # 方法2: 使用map和zip传递多个参数
    numbers = [1, 2, 3, 4, 5]
    delays = [0.5, 1, 1.5, 2, 2.5]
    
    results = executor.map(task, numbers, delays)
    for i, result in enumerate(results):
        print(f"任务{i+2}结果: {result}")

print("所有任务执行完毕")
```

### 多参数任务与starmap

```python
import concurrent.futures
import time

def task(a, b, c):
    """多参数任务函数"""
    print(f"任务 {a}-{b}-{c} 开始执行")
    time.sleep(1)
    print(f"任务 {a}-{b}-{c} 执行完毕")
    return a + b + c

# 准备参数
parameters = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]

# 使用进程池的starmap方法
with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
    # starmap可以处理多参数任务
    results = executor.starmap(task, parameters)
    
    for i, result in enumerate(results):
        print(f"任务{i+1}结果: {result}")

print("所有任务执行完毕")
```

## 实际应用示例

### 示例1：多线程下载文件

```python
import concurrent.futures
import requests
import time
import os

def download_file(url, save_path):
    """下载文件"""
    print(f"开始下载: {url}")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # 确保保存目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # 写入文件
        with open(save_path, 'wb') as f:
            f.write(response.content)
        
        print(f"下载完成: {url}")
        return True
    except Exception as e:
        print(f"下载失败: {url}, 错误: {e}")
        return False

# 文件下载列表
download_list = [
    ('https://example.com/file1.txt', 'downloads/file1.txt'),
    ('https://example.com/file2.txt', 'downloads/file2.txt'),
    ('https://example.com/file3.txt', 'downloads/file3.txt'),
    ('https://example.com/file4.txt', 'downloads/file4.txt'),
    ('https://example.com/file5.txt', 'downloads/file5.txt')
]

# 记录开始时间
start_time = time.time()

# 使用线程池下载文件
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # 提交任务
    results = executor.map(lambda x: download_file(x[0], x[1]), download_list)
    
    # 统计结果
    successful = sum(results)
    failed = len(download_list) - successful

# 记录结束时间
end_time = time.time()

print("=" * 50)
print("下载完成")
print(f"总文件数: {len(download_list)}")
print(f"成功: {successful}")
print(f"失败: {failed}")
print(f"总耗时: {end_time - start_time:.2f}秒")
```

### 示例2：多进程图像处理

```python
import concurrent.futures
import os
import time
from PIL import Image, ImageFilter

def process_image(image_path, output_dir):
    """处理图像"""
    filename = os.path.basename(image_path)
    base_name, ext = os.path.splitext(filename)
    
    try:
        # 打开图像
        with Image.open(image_path) as img:
            # 应用模糊滤镜
            blurred_img = img.filter(ImageFilter.GaussianBlur(radius=5))
            blurred_path = os.path.join(output_dir, f"{base_name}_blurred{ext}")
            blurred_img.save(blurred_path)
            
            # 应用锐化滤镜
            sharpened_img = img.filter(ImageFilter.SHARPEN)
            sharpened_path = os.path.join(output_dir, f"{base_name}_sharpened{ext}")
            sharpened_img.save(sharpened_path)
            
            # 转换为灰度图
            gray_img = img.convert('L')
            gray_path = os.path.join(output_dir, f"{base_name}_gray{ext}")
            gray_img.save(gray_path)
        
        print(f"处理完成: {filename}")
        return True
    except Exception as e:
        print(f"处理失败: {filename}, 错误: {e}")
        return False

# 图像目录和输出目录
input_dir = 'images'
output_dir = 'processed_images'

# 获取所有图像文件
image_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir)
               if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

if not image_files:
    print("没有找到图像文件")
    exit(0)

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 记录开始时间
start_time = time.time()

# 使用进程池处理图像
with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    # 准备任务参数
    tasks = [(img_file, output_dir) for img_file in image_files]
    # 执行任务
    results = executor.starmap(process_image, tasks)

# 记录结束时间
end_time = time.time()

# 统计结果
successful = sum(results)
failed = len(results) - successful

print("=" * 50)
print("图像处理完成")
print(f"总图像数: {len(image_files)}")
print(f"成功: {successful}")
print(f"失败: {failed}")
print(f"总耗时: {end_time - start_time:.2f}秒")
```

### 示例3：多线程网络爬虫

```python
import concurrent.futures
import requests
import time
from bs4 import BeautifulSoup

def crawl_url(url):
    """爬取URL内容"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No Title'
        
        # 获取链接数量
        links = soup.find_all('a')
        link_count = len(links)
        
        print(f"URL: {url}")
        print(f"Title: {title}")
        print(f"Status Code: {response.status_code}")
        print(f"Link Count: {link_count}")
        print("=" * 50)
        
        return {
            'url': url,
            'title': title,
            'status_code': response.status_code,
            'link_count': link_count,
            'success': True
        }
    except Exception as e:
        print(f"爬取失败: {url}, 错误: {e}")
        print("=" * 50)
        
        return {
            'url': url,
            'success': False,
            'error': str(e)
        }

# 待爬取的URL列表
urls = [
    'https://www.python.org',
    'https://www.github.com',
    'https://www.stackoverflow.com',
    'https://www.reddit.com',
    'https://www.quora.com',
    'https://www.wikipedia.org',
    'https://www.cnn.com',
    'https://www.bbc.com',
    'https://www.nytimes.com',
    'https://www.washingtonpost.com'
]

# 记录开始时间
start_time = time.time()

# 使用线程池爬取URL
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # 提交任务
    futures = [executor.submit(crawl_url, url) for url in urls]
    
    # 获取结果
    results = [future.result() for future in concurrent.futures.as_completed(futures)]

# 记录结束时间
end_time = time.time()

# 统计结果
successful = [r for r in results if r['success']]
failed = [r for r in results if not r['success']]

print("爬取完成")
print(f"总URL数: {len(urls)}")
print(f"成功: {len(successful)}")
print(f"失败: {len(failed)}")
print(f"总耗时: {end_time - start_time:.2f}秒")

# 输出成功爬取的URL标题和链接数
print("\n成功爬取的URL:")
for r in successful:
    print(f"- {r['title']} ({r['url']}): {r['link_count']}个链接")
```

## 最佳实践

1. **选择合适的执行器**：
   - I/O密集型任务：使用ThreadPoolExecutor
   - CPU密集型任务：使用ProcessPoolExecutor

2. **合理设置工作线程/进程数**：
   - ThreadPoolExecutor：线程数可以大于CPU核心数，一般为CPU核心数的2-4倍
   - ProcessPoolExecutor：进程数不超过CPU核心数

3. **使用上下文管理器**：使用with语句自动管理执行器的生命周期

4. **异常处理**：在任务函数中添加异常处理，或在获取结果时捕获异常

5. **避免共享状态**：多线程环境下避免使用全局变量，多进程环境下使用进程间通信

6. **超时处理**：使用timeout参数避免任务无限期等待

7. **取消不必要的任务**：对于已提交但不再需要的任务，使用cancel()方法取消

8. **使用as_completed()**：对于需要尽快处理结果的场景，使用as_completed()遍历Future对象

9. **使用map()**：对于需要顺序处理结果的场景，使用map()方法

10. **监控任务进度**：可以通过Future对象的done()方法监控任务进度

## 与其他模块的关系

- **threading模块**：ThreadPoolExecutor基于threading模块实现
- **multiprocessing模块**：ProcessPoolExecutor基于multiprocessing模块实现
- **asyncio模块**：用于异步编程，可以与concurrent.futures结合使用
- **queue模块**：ThreadPoolExecutor和ProcessPoolExecutor内部使用queue模块实现任务队列

## 总结

concurrent.futures模块提供了高级接口来管理线程池和进程池，简化了并发编程的复杂性。它的主要特点包括：

1. 统一的API：无论是线程池还是进程池，都使用相同的接口
2. 异步任务处理：支持异步提交任务和获取结果
3. 异常处理：提供了统一的异常处理机制
4. 超时处理：支持设置任务超时
5. 任务取消：支持取消未开始执行的任务

concurrent.futures模块适用于各种并发编程场景，包括：

1. I/O密集型任务：如网络请求、文件操作等
2. CPU密集型任务：如数据处理、图像处理等
3. 批量任务处理：如批量下载、批量处理等

通过使用concurrent.futures模块，可以大大简化并发编程的复杂性，提高程序的性能和响应速度。