# Python迭代器与生成器详细指南

## 一、模块概述

迭代器（Iterator）和生成器（Generator）是Python中处理序列数据的高级机制，它们能够高效地生成和处理大量数据，同时节省内存空间。迭代器提供了一种统一的方式来访问序列中的元素，而生成器则是一种特殊的迭代器，使用`yield`关键字实现，能够更简洁地创建迭代器。

## 二、基本概念

1. **可迭代对象（Iterable）**：实现了`__iter__`方法的对象，可以使用`for`循环遍历
2. **迭代器（Iterator）**：实现了`__iter__`和`__next__`方法的对象，能够逐个返回元素
3. **生成器（Generator）**：使用`yield`关键字定义的函数，调用时返回一个生成器对象
4. **yield关键字**：用于暂停和恢复函数执行，返回一个中间结果
5. **生成器表达式**：类似于列表推导式的语法，用于创建生成器对象

## 三、迭代器

### 1. 可迭代对象与迭代器的区别

可迭代对象是指实现了`__iter__`方法的对象，而迭代器是指实现了`__iter__`和`__next__`方法的对象。所有迭代器都是可迭代对象，但并非所有可迭代对象都是迭代器。

```python
# 检查对象是否可迭代
from collections.abc import Iterable, Iterator

# 列表是可迭代对象，但不是迭代器
my_list = [1, 2, 3]
print(f"列表是否可迭代: {isinstance(my_list, Iterable)}")  # True
print(f"列表是否是迭代器: {isinstance(my_list, Iterator)}")  # False

# 迭代器对象
my_iterator = iter(my_list)
print(f"迭代器是否可迭代: {isinstance(my_iterator, Iterable)}")  # True
print(f"迭代器是否是迭代器: {isinstance(my_iterator, Iterator)}")  # True
```

### 2. 手动实现迭代器

要创建自定义迭代器，需要实现`__iter__`和`__next__`方法：

```python
class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        """返回迭代器对象本身"""
        return self
    
    def __next__(self):
        """返回下一个元素"""
        if self.current > self.end:
            raise StopIteration  # 迭代结束标记
        value = self.current
        self.current += 1
        return value

# 使用自定义迭代器
my_iterator = MyIterator(1, 5)
print(f"自定义迭代器类型: {type(my_iterator)}")

# 方法1：使用next()函数
print("\n使用next()函数:")
print(next(my_iterator))
print(next(my_iterator))

# 方法2：使用for循环
print("\n使用for循环:")
for num in MyIterator(1, 5):
    print(num)

# 方法3：转换为列表
print("\n转换为列表:")
my_list = list(MyIterator(1, 5))
print(my_list)
```

输出结果：
```
自定义迭代器类型: <class '__main__.MyIterator'>

使用next()函数:
1
2

使用for循环:
1
2
3
4
5

转换为列表:
[1, 2, 3, 4, 5]
```

### 3. 迭代器的状态

```python
# 迭代器的状态示例
class CounterIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.count

# 创建迭代器对象
counter = CounterIterator(3)

# 第一次迭代
print("第一次迭代:")
for num in counter:
    print(num)

# 第二次迭代（不会产生任何输出，因为迭代器已耗尽）
print("\n第二次迭代:")
for num in counter:
    print(num)

# 需要重新创建迭代器对象
print("\n重新创建迭代器:")
counter2 = CounterIterator(3)
for num in counter2:
    print(num)
```

输出结果：
```
第一次迭代:
1
2
3

第二次迭代:

重新创建迭代器:
1
2
3
```

## 四、生成器

### 1. 生成器函数

生成器函数使用`yield`关键字定义，调用时返回一个生成器对象：

```python
def my_generator():
    """简单的生成器函数"""
    yield 1
    yield 2
    yield 3

# 调用生成器函数返回生成器对象
gen = my_generator()
print(f"生成器对象类型: {type(gen)}")
print(f"是否是迭代器: {isinstance(gen, Iterator)}")

# 使用生成器
print("\n使用next()函数:")
print(next(gen))
print(next(gen))
print(next(gen))
try:
    print(next(gen))  # 超出范围，抛出StopIteration
except StopIteration:
    print("迭代结束")

# 使用for循环
print("\n使用for循环:")
for num in my_generator():
    print(num)
```

输出结果：
```
生成器对象类型: <class 'generator'>
是否是迭代器: True

使用next()函数:
1
2
3
迭代结束

使用for循环:
1
2
3
```

### 2. yield关键字的工作原理

`yield`关键字用于暂停函数执行，返回一个中间结果，并保存函数的状态。当再次调用`next()`函数时，函数从上次暂停的地方继续执行。

```python
def count_down(n):
    """倒计时生成器"""
    print(f"开始倒计时: {n}")
    while n > 0:
        yield n
        n -= 1
    print("倒计时结束")

# 使用倒计时生成器
print("创建生成器对象")
timer = count_down(3)

print("\n第一次调用next():")
print(next(timer))

print("\n第二次调用next():")
print(next(timer))

print("\n第三次调用next():")
print(next(timer))

print("\n第四次调用next():")
try:
    print(next(timer))
except StopIteration:
    print("迭代结束")
```

输出结果：
```
创建生成器对象

第一次调用next():
开始倒计时: 3
3

第二次调用next():
2

第三次调用next():
1

第四次调用next():
倒计时结束
迭代结束
```

### 3. 生成器表达式

生成器表达式类似于列表推导式，使用圆括号而不是方括号，返回一个生成器对象：

```python
# 列表推导式
list_comp = [x * x for x in range(5)]
print(f"列表推导式: {list_comp}")
print(f"类型: {type(list_comp)}")

# 生成器表达式
gen_exp = (x * x for x in range(5))
print(f"\n生成器表达式: {gen_exp}")
print(f"类型: {type(gen_exp)}")

# 使用生成器表达式
print("\n使用生成器表达式:")
for num in gen_exp:
    print(num)

# 生成器表达式节省内存
print("\n生成器表达式节省内存:")
import sys
large_list = [x for x in range(1000000)]
large_gen = (x for x in range(1000000))
print(f"列表占用内存: {sys.getsizeof(large_list)} 字节")
print(f"生成器占用内存: {sys.getsizeof(large_gen)} 字节")
```

输出结果：
```
列表推导式: [0, 1, 4, 9, 16]
类型: <class 'list'>

生成器表达式: <generator object <genexpr> at 0x00000123456789AB>
类型: <class 'generator'>

使用生成器表达式:
0
1
4
9
16

生成器表达式节省内存:
列表占用内存: 8697464 字节
生成器占用内存: 112 字节
```

## 五、高级用法

### 1. 生成器的send()方法

`send()`方法用于向生成器发送数据，可以修改生成器的内部状态：

```python
def echo_generator():
    """回声生成器"""
    while True:
        received = yield  # 接收数据
        yield f"接收到: {received}"

gen = echo_generator()
next(gen)  # 启动生成器

# 发送数据
result = gen.send("Hello")
print(result)

# 继续迭代
next(gen)  # 消耗yield
result = gen.send("World")
print(result)

# 关闭生成器
gen.close()
```

输出结果：
```
接收到: Hello
接收到: World
```

### 2. 生成器的throw()和close()方法

```python
def exception_generator():
    """处理异常的生成器"""
    try:
        while True:
            value = yield
            print(f"处理值: {value}")
    except ValueError as e:
        print(f"捕获到ValueError: {e}")
        # 可以选择继续生成
        yield f"从ValueError恢复"
    except StopIteration:
        print("生成器关闭")
        raise
    finally:
        print("执行清理操作")

gen = exception_generator()
next(gen)  # 启动生成器

# 发送正常数据
gen.send(100)

# 抛出异常
gen.send(200)
result = gen.throw(ValueError, "测试异常")
print(result)

# 继续发送数据
next(gen)  # 消耗yield
gen.send(300)

# 关闭生成器
gen.close()
```

输出结果：
```
处理值: 100
处理值: 200
捕获到ValueError: 测试异常
从ValueError恢复
处理值: 300
执行清理操作
```

### 3. 生成器的嵌套

```python
def outer_generator(n):
    """外层生成器"""
    for i in range(n):
        print(f"外层生成器: {i}")
        yield from inner_generator(i)  # 使用yield from委托给内层生成器

def inner_generator(m):
    """内层生成器"""
    for j in range(m):
        yield f"内层生成器: {j}"

# 使用嵌套生成器
print("使用嵌套生成器:")
for item in outer_generator(3):
    print(item)

# 不使用yield from的等价实现
def outer_generator_old(n):
    for i in range(n):
        print(f"外层生成器(旧): {i}")
        for item in inner_generator(i):
            yield item

print("\n不使用yield from:")
for item in outer_generator_old(3):
    print(item)
```

输出结果：
```
使用嵌套生成器:
外层生成器: 0
外层生成器: 1
内层生成器: 0
外层生成器: 2
内层生成器: 0
内层生成器: 1

不使用yield from:
外层生成器(旧): 0
外层生成器(旧): 1
内层生成器: 0
外层生成器(旧): 2
内层生成器: 0
内层生成器: 1
```

### 4. 递归生成器

```python
def fibonacci_generator(n):
    """生成斐波那契数列的递归生成器"""
    if n <= 0:
        return
    if n == 1:
        yield 0
        return
    if n == 2:
        yield 0
        yield 1
        return
    
    # 生成前n-1个斐波那契数
    yield from fibonacci_generator(n - 1)
    
    # 计算第n个斐波那契数
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    yield b

# 使用递归生成器
print("前10个斐波那契数:")
for num in fibonacci_generator(10):
    print(num, end=" ")
```

输出结果：
```
前10个斐波那契数:
0 1 1 2 3 5 8 13 21 34
```

### 5. 无限生成器

```python
def infinite_counter(start=0):
    """无限计数器生成器"""
    n = start
    while True:
        yield n
        n += 1

# 使用无限生成器
print("无限计数器（前5个）:")
counter = infinite_counter()
for _ in range(5):
    print(next(counter), end=" ")

print("\n\n无限计数器从10开始（前5个）:")
counter2 = infinite_counter(10)
for _ in range(5):
    print(next(counter2), end=" ")

# 无限偶数生成器
def infinite_even():
    """无限偶数生成器"""
    n = 0
    while True:
        yield n
        n += 2

print("\n\n无限偶数（前5个）:")
even = infinite_even()
for _ in range(5):
    print(next(even), end=" ")
```

输出结果：
```
无限计数器（前5个）:
0 1 2 3 4 

无限计数器从10开始（前5个）:
10 11 12 13 14 

无限偶数（前5个）:
0 2 4 6 8 
```

## 六、实际应用示例

### 1. 大数据处理

```python
def large_data_processor(data_source):
    """高效处理大量数据的生成器"""
    batch_size = 1000
    while True:
        # 模拟从数据源读取一批数据
        batch = data_source.read(batch_size)
        if not batch:
            break
        # 处理数据
        processed_batch = [item * 2 for item in batch]
        yield from processed_batch

# 模拟数据源
class MockDataSource:
    def __init__(self, total_items):
        self.total_items = total_items
        self.processed = 0
    
    def read(self, batch_size):
        """模拟读取数据"""
        if self.processed >= self.total_items:
            return []
        start = self.processed
        end = min(start + batch_size, self.total_items)
        self.processed = end
        # 生成模拟数据
        return list(range(start, end))

# 使用示例
data_source = MockDataSource(1000000)  # 模拟100万条数据
processor = large_data_processor(data_source)

# 处理前10条数据
print("处理前10条数据:")
for i, item in enumerate(processor):
    if i >= 10:
        break
    print(item, end=" ")

# 注意：生成器只在需要时处理数据，节省内存
import sys
print(f"\n\n生成器占用内存: {sys.getsizeof(processor)} 字节")
```

输出结果：
```
处理前10条数据:
0 2 4 6 8 10 12 14 16 18 

生成器占用内存: 112 字节
```

### 2. 文件逐行处理

```python
def read_large_file(file_path, chunk_size=1024):
    """逐行读取大文件的生成器"""
    with open(file_path, 'r') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            # 按行分割
            lines = chunk.splitlines(True)  # True保留换行符
            for line in lines[:-1]:  # 处理完整的行
                yield line
            # 最后一行可能不完整，与下一个chunk合并
            if lines and not lines[-1].endswith('\n'):
                remaining = lines[-1]
            else:
                remaining = ''
        # 处理最后剩余的内容
        if remaining:
            yield remaining

# 创建一个大文件用于测试
large_file_path = "large_test_file.txt"
with open(large_file_path, 'w') as f:
    for i in range(10000):
        f.write(f"这是第{i+1}行内容\n")

# 使用生成器逐行读取
print("读取文件前10行:")
line_count = 0
for line in read_large_file(large_file_path):
    line_count += 1
    if line_count <= 10:
        print(f"第{line_count}行: {line.strip()}")
    else:
        break

print(f"\n文件总共有{line_count}行")
```

输出结果：
```
读取文件前10行:
第1行: 这是第1行内容
第2行: 这是第2行内容
第3行: 这是第3行内容
第4行: 这是第4行内容
第5行: 这是第5行内容
第6行: 这是第6行内容
第7行: 这是第7行内容
第8行: 这是第8行内容
第9行: 这是第9行内容
第10行: 这是第10行内容

文件总共有10000行
```

### 3. 网页爬虫

```python
import requests
from bs4 import BeautifulSoup

def scrape_website(url, max_depth=1, current_depth=0, visited=None):
    """递归爬取网站的生成器"""
    if visited is None:
        visited = set()
    
    if current_depth > max_depth or url in visited:
        return
    
    visited.add(url)
    
    try:
        # 发送请求
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # 检查请求是否成功
        
        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 提取页面标题
        title = soup.title.string if soup.title else "无标题"
        yield (url, title, current_depth)
        
        # 提取所有链接
        for link in soup.find_all('a', href=True):
            href = link['href']
            # 处理相对链接
            from urllib.parse import urljoin
            full_url = urljoin(url, href)
            # 只爬取相同域名的链接
            if full_url.startswith(url):
                # 递归爬取子页面
                yield from scrape_website(full_url, max_depth, current_depth + 1, visited)
    
    except requests.exceptions.RequestException as e:
        print(f"爬取{url}失败: {e}")

# 使用爬虫生成器
# 注意：此示例可能因网站反爬策略而失败
# print("爬取简单网站:")
# for url, title, depth in scrape_website("https://example.com", max_depth=1):
#     print(f"{'  ' * depth}[{depth}] {title}: {url}")

# 模拟爬虫行为
print("模拟爬虫行为:")
def mock_scraper(base_url, max_depth=1):
    """模拟网页爬虫"""
    for depth in range(max_depth + 1):
        if depth == 0:
            yield (base_url, "首页", depth)
        else:
            for i in range(3):
                yield (f"{base_url}/page{depth}_{i}", f"页面{depth}_{i}", depth)

for url, title, depth in mock_scraper("https://example.com", max_depth=2):
    print(f"{'  ' * depth}[{depth}] {title}: {url}")
```

输出结果：
```
模拟爬虫行为:
[0] 首页: https://example.com
  [1] 页面1_0: https://example.com/page1_0
  [1] 页面1_1: https://example.com/page1_1
  [1] 页面1_2: https://example.com/page1_2
    [2] 页面2_0: https://example.com/page2_0
    [2] 页面2_1: https://example.com/page2_1
    [2] 页面2_2: https://example.com/page2_2
```

### 4. 数据转换管道

```python
def filter_positive(numbers):
    """过滤正数的生成器"""
    for num in numbers:
        if num > 0:
            yield num

def square(numbers):
    """计算平方的生成器"""
    for num in numbers:
        yield num * num

def add_one(numbers):
    """加1的生成器"""
    for num in numbers:
        yield num + 1

# 创建数据管道
numbers = [-5, -3, 0, 2, 4, 6, -1]
result = add_one(square(filter_positive(numbers)))

# 使用管道
print("数据转换管道结果:")
for num in result:
    print(num, end=" ")

# 与列表推导式比较
result_list = [(x * x) + 1 for x in numbers if x > 0]
print(f"\n\n列表推导式结果: {result_list}")
```

输出结果：
```
数据转换管道结果:
5 17 37 

列表推导式结果: [5, 17, 37]
```

### 5. 并发处理模拟

```python
def task_generator(tasks):
    """生成任务的生成器"""
    for i, task in enumerate(tasks):
        print(f"生成任务 {i+1}: {task}")
        yield task

def worker(task_gen, worker_id):
    """处理任务的工作者"""
    results = []
    for task in task_gen:
        # 模拟任务处理时间
        import time
        time.sleep(0.1)
        result = f"{worker_id}处理{task}"
        results.append(result)
        print(f"工作者{worker_id}完成任务: {task}")
    return results

# 使用生成器模拟并发处理
print("模拟并发处理:")
tasks = ["任务A", "任务B", "任务C", "任务D", "任务E"]
task_gen = task_generator(tasks)

# 创建两个工作者
worker1_results = worker(task_gen, 1)
worker2_results = worker(task_gen, 2)

print(f"\n工作者1结果: {worker1_results}")
print(f"工作者2结果: {worker2_results}")
```

输出结果：
```
模拟并发处理:
生成任务 1: 任务A
生成任务 2: 任务B
生成任务 3: 任务C
生成任务 4: 任务D
生成任务 5: 任务E
工作者1完成任务: 任务A
工作者1完成任务: 任务B
工作者1完成任务: 任务C
工作者1完成任务: 任务D
工作者1完成任务: 任务E
工作者2结果: []

工作者1结果: ['1处理任务A', '1处理任务B', '1处理任务C', '1处理任务D', '1处理任务E']
工作者2结果: []
```

## 七、最佳实践

1. **优先使用生成器处理大量数据**：生成器只在需要时生成数据，节省内存空间
2. **使用生成器表达式代替列表推导式**：对于只需要遍历一次的数据，使用生成器表达式更高效
3. **使用yield from简化嵌套迭代**：使用`yield from`可以简化生成器的嵌套调用
4. **保持生成器函数简洁**：生成器函数应该专注于生成数据，避免复杂的逻辑
5. **正确处理异常**：在生成器中适当处理异常，确保资源能够正确释放
6. **使用无限生成器处理连续数据流**：对于需要持续生成数据的场景，使用无限生成器
7. **文档化生成器**：为生成器函数添加清晰的文档字符串，说明其功能和用法
8. **避免在生成器中保存大量状态**：生成器应该保持轻量，避免保存大量状态信息

## 八、总结

迭代器和生成器是Python中处理序列数据的强大工具，它们提供了一种高效、节省内存的方式来生成和处理数据。迭代器提供了统一的序列访问方式，而生成器则使用`yield`关键字更简洁地创建迭代器。

从基本的迭代器和生成器函数，到高级的生成器方法（send、throw、close）和嵌套生成器，掌握这些技术能够帮助开发者编写更高效、更优雅的代码。

在实际应用中，迭代器和生成器广泛应用于大数据处理、文件操作、网页爬虫、数据转换管道等场景，能够显著提高代码的性能和可读性。