"""
此文件是Python模块的学习文档，包含Markdown格式和代码示例。
请使用文本编辑器或Markdown查看器打开以获得最佳阅读体验。
"""

# functools模块 - Python函数式编程工具集

## 1. 核心功能与概述

"functools"模块提供了用于高阶函数操作的工具,即那些作用于或返回其他函数的函数.它是Python函数式编程范式的重要组成部分,可以帮助开发者编写更加简洁,高效和可复用的代码.

### 主要功能:
- 函数装饰器:提供各种用于增强函数行为的装饰器
- 函数变换:支持函数的部分应用,柯里化等高级操作
- 函数组合:支持多个函数的组合使用
- 比较功能:提供通用的比较功能支持
- 缓存机制:实现函数结果缓存以提高性能

### 应用场景:
- 函数式编程范式
- 代码优化与性能提升
- API设计与扩展
- 数据处理与转换
- 装饰器模式实现

## 2. 基本使用方法

### 2.1 functools.wraps - 保留原函数元数据的装饰器

"wraps"装饰器用于在创建自定义装饰器时保留原始函数的元数据(如名称,文档字符串,参数签名等).

```python
import functools
import time

def timer(func):
    """计算函数执行时间的装饰器"""
    @functools.wraps(func)  # 保留原函数的元数据
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行耗时: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@timer
def fibonacci(n):
    """计算斐波那契数列的第n个数"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 调用被装饰的函数
result = fibonacci(10)
print(f"结果: {result}")

# 验证元数据是否被保留
print(f"函数名: {fibonacci.__name__}")
print(f"文档字符串: {fibonacci.__doc__}")

# 不使用wraps的对比
def bad_timer(func):
    """不使用wraps的装饰器"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数执行耗时: {end_time - start_time:.4f} 秒")
        return result
    return wrapper

@bad_timer
def bad_fibonacci(n):
    """计算斐波那契数列的第n个数(无wraps)"""
    if n <= 1:
        return n
    return bad_fibonacci(n-1) + bad_fibonacci(n-2)

print(f"\n不使用wraps的情况:")
print(f"函数名: {bad_fibonacci.__name__}")  # 输出'wrapper'而非'bad_fibonacci'
print(f"文档字符串: {bad_fibonacci.__doc__}")  # 输出None或wrapper的文档
```

### 2.2 functools.lru_cache - 函数结果缓存装饰器

"lru_cache"(Least Recently Used Cache)装饰器实现了LRU缓存机制,可以缓存函数调用的结果,避免重复计算,显著提高递归或重复调用函数的性能.

```python
import functools
import time

# 使用lru_cache装饰器优化斐波那契函数
@functools.lru_cache(maxsize=None)  # maxsize=None表示不限制缓存大小
def cached_fibonacci(n):
    """使用缓存优化的斐波那契数列计算"""
    if n <= 1:
        return n
    return cached_fibonacci(n-1) + cached_fibonacci(n-2)

# 测试性能提升
print("测试缓存版本与非缓存版本的性能对比:")

# 非缓存版本
def non_cached_fibonacci(n):
    if n <= 1:
        return n
    return non_cached_fibonacci(n-1) + non_cached_fibonacci(n-2)

# 测试非缓存版本
start = time.time()
result1 = non_cached_fibonacci(30)
end = time.time()
print(f"非缓存版本计算fibonacci(30): {end - start:.4f} 秒, 结果: {result1}")

# 测试缓存版本(首次调用)
start = time.time()
result2 = cached_fibonacci(30)
end = time.time()
print(f"缓存版本首次计算fibonacci(30): {end - start:.4f} 秒, 结果: {result2}")

# 测试缓存版本(再次调用,使用缓存)
start = time.time()
result3 = cached_fibonacci(30)
end = time.time()
print(f"缓存版本再次计算fibonacci(30): {end - start:.4f} 秒, 结果: {result3}")

# 查看缓存信息
print(f"\n缓存信息: {cached_fibonacci.cache_info()}")

# 清除缓存
cached_fibonacci.cache_clear()
print(f"清除缓存后: {cached_fibonacci.cache_info()}")

# 带参数的lru_cache
@functools.lru_cache(maxsize=128)  # 限制缓存最多保存128个结果
def limited_cache_func(n):
    """使用有限缓存的函数"""
    time.sleep(0.1)  # 模拟耗时操作
    return n * n

# 测试有限缓存
print("\n测试有限缓存:")
for i in range(200):
    limited_cache_func(i)

print(f"有限缓存信息: {limited_cache_func.cache_info()}")
```

### 2.3 functools.partial - 函数部分应用

"partial"函数用于创建一个新函数,该函数是原函数的一个部分应用版本,预先填充了部分参数.

```python
import functools

# 原始函数
def power(base, exponent):
    """计算base的exponent次方"""
    return base ** exponent

# 创建平方函数(固定指数为2)
square = functools.partial(power, exponent=2)

# 创建立方函数(固定指数为3)
cube = functools.partial(power, exponent=3)

# 创建以2为底的指数函数(固定底数为2)
power_of_two = functools.partial(power, 2)

# 测试部分应用后的函数
print(f"square(5) = {square(5)}")         # 输出: 25
print(f"cube(4) = {cube(4)}")           # 输出: 64
print(f"power_of_two(10) = {power_of_two(10)}")  # 输出: 1024

# 可以覆盖预设的参数
print(f"square(base=7, exponent=3) = {square(base=7, exponent=3)}")  # 输出: 343

# 在实际场景中的应用:将open函数配置为默认以UTF-8编码打开文件
open_utf8 = functools.partial(open, encoding='utf-8')

# 现在使用open_utf8打开文件时,默认使用UTF-8编码
# 例如:with open_utf8('example.txt', 'r') as f:

# 用于数据转换
def format_data(value, prefix="", suffix=""):
    """格式化数据,添加前缀和后缀"""
    return f"{prefix}{value}{suffix}"

# 创建特定格式的转换函数
format_currency = functools.partial(format_data, prefix="$", suffix=" USD")
format_percentage = functools.partial(format_data, suffix="%")
format_code = functools.partial(format_data, prefix="<code>", suffix="</code>")

# 测试格式化函数
print(f"\n格式化测试:")
print(f"金额: {format_currency(100)}")        # 输出: $100 USD
print(f"百分比: {format_percentage(75.5)}")  # 输出: 75.5%
print(f"代码: {format_code('print(1)')}")    # 输出: <code>print(1)</code>
```

### 2.4 functools.reduce - 归约函数

"reduce"函数将一个二元函数连续应用于一个序列的元素,从左到右累积计算结果.

```python
import functools

# 计算列表元素的和
numbers = [1, 2, 3, 4, 5]
sum_result = functools.reduce(lambda x, y: x + y, numbers)
print(f"列表元素之和: {sum_result}")  # 输出: 15

# 计算列表元素的乘积
product_result = functools.reduce(lambda x, y: x * y, numbers)
print(f"列表元素之积: {product_result}")  # 输出: 120

# 使用初始值
sum_with_initial = functools.reduce(lambda x, y: x + y, numbers, 10)
print(f"列表元素之和(初始值10): {sum_with_initial}")  # 输出: 25

# 处理空序列(必须提供初始值)
try:
    # 这会引发TypeError
    functools.reduce(lambda x, y: x + y, [])
except TypeError as e:
    print(f"错误: {e}")

# 提供初始值可以安全处理空序列
print(f"空序列之和(初始值0): {functools.reduce(lambda x, y: x + y, [], 0)}")

# 查找列表中的最大值
max_value = functools.reduce(lambda x, y: x if x > y else y, numbers)
print(f"列表最大值: {max_value}")  # 输出: 5

# 字符串连接
words = ['Python', 'is', 'awesome!']
sentence = functools.reduce(lambda x, y: f"{x} {y}", words)
print(f"连接后的句子: {sentence}")  # 输出: Python is awesome!

# 更复杂的例子:计算阶乘
def factorial(n):
    """计算n的阶乘"""
    if n < 0:
        raise ValueError("阶乘不能计算负数")
    return functools.reduce(lambda x, y: x * y, range(1, n+1), 1)

print(f"\n阶乘计算:")
for i in range(1, 11):
    print(f"{i}! = {factorial(i)}")
```

### 2.5 functools.total_ordering - 简化比较方法实现

"total_ordering"是一个类装饰器,它可以基于一个或几个已定义的比较方法(如"__eq__"和"__lt__")自动生成其余的比较方法.

```python
import functools

@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
    
    # 只需要定义__eq__和__lt__,其他比较方法会自动生成
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age
    
    def __lt__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age

# 创建Person实例
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p3 = Person("Charlie", 30)

# 测试自动生成的比较方法
print(f"p1 < p2: {p1 < p2}")    # 输出: False
print(f"p1 <= p2: {p1 <= p2}")  # 输出: False
print(f"p1 > p2: {p1 > p2}")    # 输出: True
print(f"p1 >= p2: {p1 >= p2}")  # 输出: True
print(f"p1 == p3: {p1 == p3}")  # 输出: True
print(f"p1 != p2: {p1 != p2}")  # 输出: True

# 排序测试
people = [p1, p2, p3]
people.sort()
print(f"\n排序后的人员列表: {people}")

# 不使用total_ordering的对比(需要手动实现所有比较方法)
class ManualPerson:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"ManualPerson(name='{self.name}', age={self.age})"
    
    def __eq__(self, other):
        if not isinstance(other, ManualPerson):
            return NotImplemented
        return self.age == other.age
    
    def __lt__(self, other):
        if not isinstance(other, ManualPerson):
            return NotImplemented
        return self.age < other.age
    
    # 需要手动实现其他比较方法
    def __le__(self, other):
        return self == other or self < other
    
    def __gt__(self, other):
        return not (self == other or self < other)
    
    def __ge__(self, other):
        return not self < other
    
    def __ne__(self, other):
        return not self == other
```

## 3. 高级用法

### 3.1 functools.singledispatch - 单分派泛型函数

"singledispatch"是Python 3.4引入的装饰器,用于创建泛型函数,它允许根据第一个参数的类型来选择不同的实现.

```python
import functools

@functools.singledispatch
def process_data(data):
    """处理数据的通用函数"""
    raise NotImplementedError(f"不支持的数据类型: {type(data).__name__}")

# 为整数类型注册实现
@process_data.register(int)
def _(data):
    print(f"处理整数: {data}, 平方结果: {data ** 2}")
    return data ** 2

# 为浮点数类型注册实现
@process_data.register(float)
def _(data):
    print(f"处理浮点数: {data:.2f}, 立方结果: {data ** 3:.2f}")
    return data ** 3

# 为字符串类型注册实现
@process_data.register(str)
def _(data):
    print(f"处理字符串: '{data}', 大写结果: '{data.upper()}'")
    return data.upper()

# 为列表类型注册实现
@process_data.register(list)
def _(data):
    print(f"处理列表: {data}, 元素和: {sum(data)}")
    return sum(data)

# 为多个类型注册同一个实现
@process_data.register(tuple)
@process_data.register(set)
def _(data):
    print(f"处理容器类型: {type(data).__name__} {data}, 转换为列表: {list(data)}")
    return list(data)

# 测试不同类型的数据处理
print("测试单分派泛型函数:")
process_data(5)          # 整数处理
process_data(3.14)       # 浮点数处理
process_data("hello")    # 字符串处理
process_data([1, 2, 3])  # 列表处理
process_data((4, 5, 6))  # 元组处理(使用容器类型实现)
process_data({7, 8, 9})  # 集合处理(使用容器类型实现)

# 尝试处理不支持的类型
try:
    process_data({'a': 1})
except NotImplementedError as e:
    print(f"错误: {e}")

# 检查已注册的类型
print(f"\n已注册的类型: {process_data.registry.keys()}")

# 在类中使用单分派
class DataProcessor:
    @functools.singledispatch
    def process(self, data):
        raise NotImplementedError(f"不支持的数据类型: {type(data).__name__}")
    
    @process.register(int)
    def _(self, data):
        return f"整数处理结果: {data * 10}"
    
    @process.register(str)
    def _(self, data):
        return f"字符串处理结果: {data * 2}"

# 测试类中的单分派
processor = DataProcessor()
print(f"\n类方法单分派测试:")
print(processor.process(123))
print(processor.process("abc"))
```

### 3.2 functools.update_wrapper - 手动更新函数包装器

"update_wrapper"函数是"wraps"装饰器的底层实现,用于手动更新包装函数,使其保留原始函数的元数据.

```python
import functools
import inspect

def log_calls(func):
    """记录函数调用的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        print(f"参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"返回值: {result}")
        return result
    
    # 手动使用update_wrapper更新包装函数的元数据
    functools.update_wrapper(
        wrapper,
        func,
        assigned=('__name__', '__module__', '__doc__'),  # 要复制的属性
        updated=('__dict__',)  # 要更新的属性
    )
    
    return wrapper

def example_function(x, y):
    """这是一个示例函数文档字符串"""
    return x + y

# 应用装饰器
wrapped_func = log_calls(example_function)

# 验证元数据是否被保留
print(f"函数名: {wrapped_func.__name__}")  # 应该输出'example_function'
print(f"文档字符串: {wrapped_func.__doc__}")  # 应该显示原始文档

# 检查函数签名
print(f"函数签名: {inspect.signature(wrapped_func)}")  # 应该显示(x, y)

# 测试函数调用
result = wrapped_func(3, 4)
print(f"最终结果: {result}")

# 自定义属性也会被更新
original_func = lambda x: x * 2
original_func.custom_attribute = "这是一个自定义属性"

wrapped_custom = log_calls(original_func)
print(f"\n自定义属性: {getattr(wrapped_custom, 'custom_attribute', '未找到')}")
```

### 3.3 functools.cmp_to_key - 将比较函数转换为键函数

"cmp_to_key"函数用于将传统的比较函数(返回-1, 0, 1的函数)转换为键函数,以便在排序等操作中使用.

```python
import functools

# 传统的比较函数
def compare_by_length(a, b):
    """按字符串长度比较"""
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    else:
        return 0  # 长度相同时按字典序比较

# 使用cmp_to_key转换为键函数
key_func = functools.cmp_to_key(compare_by_length)

# 测试排序
words = ['apple', 'banana', 'kiwi', 'strawberry', 'fig', 'watermelon']
sorted_by_length = sorted(words, key=key_func)
print(f"按长度排序: {sorted_by_length}")

# 直接在sorted中使用
another_sorted = sorted(words, key=functools.cmp_to_key(compare_by_length))
print(f"再次按长度排序: {another_sorted}")

# 更复杂的比较函数
def custom_sort(a, b):
    """自定义排序规则:先按首字母,再按长度"""
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        # 首字母相同时按长度排序
        return compare_by_length(a, b)

# 测试自定义排序
custom_sorted = sorted(words, key=functools.cmp_to_key(custom_sort))
print(f"\n自定义排序: {custom_sorted}")

# 在列表sort方法中使用
words_copy = words.copy()
words_copy.sort(key=functools.cmp_to_key(custom_sort))
print(f"列表原地排序: {words_copy}")

# 对于数值类型的特殊排序(例如,奇数排在偶数前面)
def odd_even_compare(a, b):
    """奇数排在偶数前面,同类型按大小排序"""
    a_is_odd = a % 2 == 1
    b_is_odd = b % 2 == 1
    
    if a_is_odd and not b_is_odd:
        return -1  # 奇数排在前面
    elif not a_is_odd and b_is_odd:
        return 1   # 偶数排在后面
    else:
        # 同类型按大小排序
        return a - b if a < b else 1 if a > b else 0

# 测试奇偶数排序
numbers = [1, 4, 3, 2, 5, 8, 7, 6]
odd_even_sorted = sorted(numbers, key=functools.cmp_to_key(odd_even_compare))
print(f"\n奇偶数排序: {odd_even_sorted}")
```

### 3.4 functools.lru_cache的高级配置

除了基本使用外,"lru_cache"还可以与其他装饰器结合使用,或者用于复杂对象的缓存.

```python
import functools
import time
from dataclasses import dataclass

# 1. 与其他装饰器结合使用
@timer  # 使用之前定义的timer装饰器
@functools.lru_cache(maxsize=128)
def complex_calculation(a, b, c):
    """一个复杂的计算函数,同时使用缓存和计时"""
    time.sleep(0.1)  # 模拟耗时计算
    return a * b + c

# 测试组合装饰器
print("\n测试组合装饰器:")
for _ in range(3):
    complex_calculation(10, 20, 30)

# 2. 缓存复杂对象
@dataclass
class Point:
    x: int
    y: int
    
    # 为了能在缓存中使用,需要实现__hash__方法
    def __hash__(self):
        return hash((self.x, self.y))

@functools.lru_cache(maxsize=None)
def distance_to_origin(point):
    """计算点到原点的距离"""
    print(f"计算点 {point} 到原点的距离")
    time.sleep(0.1)  # 模拟耗时计算
    return (point.x ** 2 + point.y ** 2) ** 0.5

# 测试复杂对象缓存
print("\n测试复杂对象缓存:")
p1 = Point(3, 4)
p2 = Point(3, 4)  # 与p1值相同的新对象

# 第一次调用,会计算
d1 = distance_to_origin(p1)
print(f"距离1: {d1}")

# 第二次调用相同的对象,应该使用缓存
d1_again = distance_to_origin(p1)
print(f"距离1(再次): {d1_again}")

# 调用值相同的不同对象,由于实现了__hash__,也应该使用缓存
d2 = distance_to_origin(p2)
print(f"距离2: {d2}")

# 检查缓存信息
print(f"缓存信息: {distance_to_origin.cache_info()}")

# 3. 使用typed参数
@functools.lru_cache(maxsize=None, typed=True)  # typed=True时,不同类型的相同值会被视为不同键
def typed_func(x):
    """演示typed参数的函数"""
    print(f"参数类型: {type(x).__name__}, 值: {x}")
    return x

# 测试typed参数
print("\n测试typed参数:")
print(typed_func(1))      # 整数1
print(typed_func(1.0))    # 浮点数1.0,typed=True时会重新计算
print(typed_func(True))   # 布尔值True,在Python中等同于1,但类型不同

print(f"缓存信息: {typed_func.cache_info()}")  # 应该有3个缓存条目

# 4. 缓存过期策略(自定义)
import threading
import time
from collections import OrderedDict

class TimedLRUCache:
    """带过期时间的LRU缓存"""
    def __init__(self, maxsize=128, ttl=300):
        self.maxsize = maxsize
        self.ttl = ttl  # 缓存过期时间(秒)
        self.cache = OrderedDict()
        self.lock = threading.RLock()  # 可重入锁保证线程安全
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            
            with self.lock:
                # 检查缓存是否存在且未过期
                if key in self.cache:
                    result, timestamp = self.cache[key]
                    if time.time() - timestamp < self.ttl:
                        # 缓存有效,移动到末尾(最近使用)
                        self.cache.move_to_end(key)
                        return result
                    else:
                        # 缓存已过期,删除
                        del self.cache[key]
                
                # 缓存不存在或已过期,计算结果
                result = func(*args, **kwargs)
                
                # 检查缓存大小
                if self.maxsize is not None and len(self.cache) >= self.maxsize:
                    # 删除最久未使用的缓存项(OrderedDict的第一项)
                    self.cache.popitem(last=False)
                
                # 存储结果和时间戳
                self.cache[key] = (result, time.time())
                
                return result
        
        # 添加缓存管理方法
        def clear():
            with self.lock:
                self.cache.clear()
        
        def info():
            with self.lock:
                return {
                    'hits': sum(1 for _, timestamp in self.cache.values() 
                              if time.time() - timestamp < self.ttl),
                    'misses': 0,  # 简化版,不统计misses
                    'maxsize': self.maxsize,
                    'currsize': len(self.cache)
                }
        
        wrapper.clear_cache = clear
        wrapper.cache_info = info
        
        return wrapper

# 测试带过期时间的缓存
@TimedLRUCache(maxsize=5, ttl=2)  # 缓存2秒过期
def timed_cached_func(x):
    """带过期时间的缓存函数"""
    print(f"计算 {x} 的值")
    time.sleep(0.1)  # 模拟耗时计算
    return x * x

print("\n测试带过期时间的缓存:")
# 第一次调用
timed_cached_func(1)
# 立即再次调用,应该使用缓存
timed_cached_func(1)

print("等待2秒让缓存过期...")
time.sleep(2)
# 缓存过期后调用,应该重新计算
timed_cached_func(1)

# 查看缓存信息
print(f"缓存信息: {timed_cached_func.cache_info()}")
```

### 3.5 functools.partialmethod - 部分应用方法

"partialmethod"类似于"partial",但它专门用于类方法的部分应用.

```python
import functools

class Calculator:
    def __init__(self, base=10):
        self.base = base
    
    def add(self, a, b):
        """加法运算"""
        return a + b
    
    def multiply(self, a, b):
        """乘法运算"""
        return a * b
    
    # 使用partialmethod创建部分应用的方法
    add_to_ten = functools.partialmethod(add, 10)  # 固定第一个参数为10
    multiply_by_base = functools.partialmethod(multiply, b=None)  # 固定第二个参数为None,将在调用时替换
    
    def multiply_by_base(self, a, b=None):
        """使用base作为第二个参数的乘法"""
        if b is None:
            b = self.base
        return a * b
    
    # 正确的partialmethod用法
    multiply_by_base = functools.partialmethod(multiply, b=None)

# 创建Calculator实例
calc = Calculator(base=20)

# 测试普通方法
print(f"calc.add(5, 3) = {calc.add(5, 3)}")  # 输出: 8
print(f"calc.multiply(4, 5) = {calc.multiply(4, 5)}")  # 输出: 20

# 测试partialmethod
print(f"calc.add_to_ten(5) = {calc.add_to_ten(5)}")  # 输出: 15 (10 + 5)

# 注意:上面的multiply_by_base定义有问题,我们重新定义一个正确的例子
class CorrectCalculator:
    def __init__(self, base=10):
        self.base = base
    
    def operation(self, op, a, b):
        """通用运算方法"""
        if op == 'add':
            return a + b
        elif op == 'subtract':
            return a - b
        elif op == 'multiply':
            return a * b
        elif op == 'divide':
            return a / b if b != 0 else float('inf')
        else:
            raise ValueError(f"不支持的操作: {op}")
    
    # 使用partialmethod预设操作类型
    add = functools.partialmethod(operation, 'add')
    subtract = functools.partialmethod(operation, 'subtract')
    multiply = functools.partialmethod(operation, 'multiply')
    divide = functools.partialmethod(operation, 'divide')

# 测试正确的partialmethod用法
correct_calc = CorrectCalculator()
print(f"\n正确的partialmethod用法:")
print(f"correct_calc.add(10, 5) = {correct_calc.add(10, 5)}")
print(f"correct_calc.subtract(10, 5) = {correct_calc.subtract(10, 5)}")
print(f"correct_calc.multiply(10, 5) = {correct_calc.multiply(10, 5)}")
print(f"correct_calc.divide(10, 5) = {correct_calc.divide(10, 5)}")

# 更复杂的例子:数据库操作封装
class Database:
    def execute(self, query_type, table, **kwargs):
        """执行数据库操作"""
        print(f"执行{query_type}操作到表'{table}'")
        print(f"参数: {kwargs}")
        # 实际的数据库操作代码...
        return f"{query_type}操作成功: {table}"
    
    # 使用partialmethod创建常用操作方法
    insert = functools.partialmethod(execute, 'INSERT')
    update = functools.partialmethod(execute, 'UPDATE')
    delete = functools.partialmethod(execute, 'DELETE')
    select = functools.partialmethod(execute, 'SELECT')

# 测试数据库操作
print("\n测试数据库操作封装:")
db = Database()
db.insert('users', name='Alice', age=30)
db.update('users', where='id=1', name='Bob')
db.select('users', where='age>25', limit=10)
```

## 4. 实际应用场景

### 4.1 函数式编程模式实现

functools模块是实现函数式编程模式的重要工具,下面展示几个常见的函数式编程模式.

```python
import functools

# 1. 函数组合
def compose(*functions):
    """组合多个函数,从右到左执行"""
    def composed_function(x):
        result = x
        for func in reversed(functions):
            result = func(result)
        return result
    return composed_function

# 测试函数组合
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def square(x):
    return x ** 2

# 创建组合函数: square(multiply_by_two(add_one(x)))
composed = compose(square, multiply_by_two, add_one)
print(f"函数组合测试: {composed(3)}")  # 输出: (3+1)*2)^2 = 64

# 2. 使用reduce实现函数组合
def compose_with_reduce(*functions):
    """使用reduce实现函数组合"""
    def composed_function(x):
        return functools.reduce(lambda result, func: func(result), functions, x)
    return composed_function

# 注意:这个版本是从左到右执行的
left_to_right_composed = compose_with_reduce(add_one, multiply_by_two, square)
print(f"从左到右的函数组合: {left_to_right_composed(3)}")  # 输出: ((3+1)^2)*2 = 32

# 3. 柯里化(Currying)
def curry(func):
    """将多参数函数转换为一系列单参数函数"""
    arg_count = func.__code__.co_argcount
    
    def curried(*args):
        if len(args) >= arg_count:
            # 如果参数足够,直接调用原函数
            return func(*args)
        else:
            # 否则返回一个新函数,等待接收更多参数
            def partial(*more_args):
                return curried(*(args + more_args))
            return partial
    
    return curried

# 测试柯里化
@curry
def add_three(a, b, c):
    return a + b + c

print(f"\n柯里化测试:")
print(f"add_three(1, 2, 3) = {add_three(1, 2, 3)}")       # 直接调用
print(f"add_three(1)(2, 3) = {add_three(1)(2, 3)}")     # 部分应用
print(f"add_three(1)(2)(3) = {add_three(1)(2)(3)}")     # 完全柯里化

# 4. 函子(Functor)模式
class Functor:
    """简单的函子实现"""
    def __init__(self, value):
        self.value = value
    
    def map(self, func):
        """将函数应用于值并返回新的函子"""
        return Functor(func(self.value))
    
    def __repr__(self):
        return f"Functor({self.value})"

# 测试函子
f = Functor(5)
f2 = f.map(lambda x: x * 2).map(lambda x: x + 3)
print(f"\n函子测试:")
print(f"初始: {f}")
print(f"应用函数后: {f2}")

# 5. 备忘录化(Memoization)优化递归
@functools.lru_cache(maxsize=None)
def memoized_factorial(n):
    """使用lru_cache优化的阶乘函数"""
    if n <= 1:
        return 1
    return n * memoized_factorial(n - 1)

# 测试备忘录化
print(f"\n备忘录化递归测试:")
for i in range(10):
    print(f"{i}! = {memoized_factorial(i)}")
```

### 4.2 API设计与参数验证

functools模块在API设计中可以用于参数验证,默认值处理和接口一致性维护.

```python
```python
"""  # 闭合未闭合的双三引号
import functools
import time
from collections import deque

# 1. 带缓存的数据转换管道
@functools.lru_cache(maxsize=1000)
def expensive_transformation(data):
    """模拟耗时的数据转换操作"""
    time.sleep(0.01)  # 模拟10ms的处理时间
    return data.upper() + "_PROCESSED"

@functools.lru_cache(maxsize=500)
def data_enrichment(data):
    """模拟数据富集操作"""
    time.sleep(0.005)  # 模拟5ms的处理时间
    return f"{data}_ENRICHED"

@functools.lru_cache(maxsize=1000)
def data_validation(data):
    """模拟数据验证操作"""
    time.sleep(0.003)  # 模拟3ms的处理时间
    return f"VALID_{data}" if len(data) > 10 else f"INVALID_{data}"

# 构建数据处理管道
def process_data_pipeline(raw_data):
    """完整的数据处理管道"""
    # 第一步:数据转换
    transformed = expensive_transformation(raw_data)
    # 第二步:数据富集
    enriched = data_enrichment(transformed)
    # 第三步:数据验证
    validated = data_validation(enriched)
    return validated

# 测试数据处理管道的性能
print("\n数据处理管道性能测试:")

# 生成测试数据
test_data = [f"data_item_{i}" for i in range(200)]

# 模拟重复数据(实际应用中很常见)
test_data.extend([f"data_item_{i}" for i in range(100)])

# 第一次运行(没有缓存)
start_time = time.time()
results1 = [process_data_pipeline(item) for item in test_data]
results1_time = time.time() - start_time
print(f"首次运行耗时: {(end_time - start_time) * 1000:.2f} ms")
print(f"处理了 {len(test_data)} 条数据")

# 第二次运行(有缓存)
start_time = time.time()
results2 = [process_data_pipeline(item) for item in test_data]
results2_time = time.time() - start_time
print(f"第二次运行耗时: {(end_time - start_time) * 1000:.2f} ms")
print(f"性能提升: {(results1_time - results2_time) / results1_time * 100:.2f}%")

# 查看缓存使用情况
print(f"\n缓存使用情况:")
print(f"expensive_transformation: {expensive_transformation.cache_info()}")
print(f"data_enrichment: {data_enrichment.cache_info()}")
print(f"data_validation: {data_validation.cache_info()}")

# 2. 并行数据处理管道
import threading
from concurrent.futures import ThreadPoolExecutor

# 定义管道处理函数
def parallel_processing_pipeline(items, num_workers=4):
    """并行数据处理管道"""
    # 创建结果队列
    results = []
    
    # 定义单个项目的处理函数
    def process_item(item):
        return process_data_pipeline(item)
    
    # 使用线程池并行处理
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        # 提交所有任务
        futures = [executor.submit(process_item, item) for item in items]
        # 收集结果
        results = [future.result() for future in futures]
    
    return results

# 测试并行处理性能
large_test_data = [f"large_data_item_{i}" for i in range(1000)]
large_test_data.extend([f"large_data_item_{i}" for i in range(500)])

print("\n并行处理性能测试:")

# 清除缓存
expensive_transformation.cache_clear()
data_enrichment.cache_clear()
data_validation.cache_clear()

# 串行处理
start_time = time.time()
serial_results = [process_data_pipeline(item) for item in large_test_data[:200]]
serial_time = time.time() - start_time
print(f"串行处理耗时: {serial_time * 1000:.2f} ms")

# 清除缓存
expensive_transformation.cache_clear()
data_enrichment.cache_clear()
data_validation.cache_clear()

# 并行处理
start_time = time.time()
parallel_results = parallel_processing_pipeline(large_test_data[:200], num_workers=4)
parallel_time = time.time() - start_time
print(f"4线程并行处理耗时: {parallel_time * 1000:.2f} ms")
print(f"并行处理加速比: {serial_time / parallel_time:.2f}x")

# 3. 响应式数据流处理
class DataProcessor:
    """响应式数据处理器"""
    def __init__(self):
        self.processors = deque()
    
    def add_processor(self, processor_func):
        """添加数据处理函数"""
        self.processors.append(processor_func)
        return self  # 支持链式调用
    
    def process(self, data):
        """处理数据"""
        result = data
        for processor in self.processors:
            result = processor(result)
        return result
    
    def process_batch(self, data_batch):
        """批量处理数据"""
        return [self.process(data) for data in data_batch]

# 创建响应式数据处理器
processor = DataProcessor()
processor.add_processor(expensive_transformation)
        .add_processor(data_enrichment)
        .add_processor(data_validation)

# 测试响应式处理
print("\n响应式数据处理测试:")
test_items = ["item1", "item2", "item3"]
results = processor.process_batch(test_items)
print(f"响应式处理结果: {results}")

# 4. 可配置的数据处理管道
class ConfigurablePipeline:
    """可配置的数据处理管道"""
    def __init__(self):
        self.steps = []
        self.cache_enabled = {}
    
    def add_step(self, name, func, use_cache=True, cache_size=128):
        """添加处理步骤"""
        if use_cache:
            # 创建带缓存的函数
            cached_func = functools.lru_cache(maxsize=cache_size)(func)
            self.steps.append((name, cached_func))
            self.cache_enabled[name] = True
        else:
            self.steps.append((name, func))
            self.cache_enabled[name] = False
        return self
    
    def process(self, data):
        """处理数据"""
        result = data
        step_results = {"input": data}
        
        for name, func in self.steps:
            result = func(result)
            step_results[name] = result
        
        step_results["output"] = result
        return step_results
    
    def clear_cache(self, step_name=None):
        """清除指定步骤或所有步骤的缓存"""
        if step_name:
            # 清除指定步骤的缓存
            for name, func in self.steps:
                if name == step_name and self.cache_enabled.get(name, False):
                    func.cache_clear()
                    print(f"已清除步骤 '{step_name}' 的缓存")
                    return
            print(f"未找到步骤 '{step_name}' 或该步骤未启用缓存")
        else:
            # 清除所有步骤的缓存
            for name, func in self.steps:
                if self.cache_enabled.get(name, False):
                    func.cache_clear()
                    print(f"已清除步骤 '{name}' 的缓存")

# 测试可配置管道
def transform_step(data):
    return data.upper()

def filter_step(data):
    return data if len(data) > 5 else None

def format_step(data):
    return f"PROCESSED: {data}" if data else "SKIPPED"

# 创建可配置管道
pipeline = ConfigurablePipeline()
pipeline.add_step("transform", transform_step, use_cache=True, cache_size=100)
        .add_step("filter", filter_step, use_cache=False)  # 过滤步骤不需要缓存
        .add_step("format", format_step, use_cache=True, cache_size=50)

# 测试可配置管道
print("\n可配置数据处理管道测试:")
test_data = ["short", "longer_text", "medium", "very_long_text_here"]

for item in test_data:
    result = pipeline.process(item)
    print(f"处理 '{item}':")
    for step, value in result.items():
        print(f"  {step}: {value}")

# 清除特定步骤的缓存
pipeline.clear_cache("transform")
"""

### 4.4 缓存策略与性能优化

functools.lru_cache是性能优化的强大工具,但需要根据实际场景选择合适的缓存策略.

"""python
import functools
import time
import random
import threading
from collections import Counter

# 1. 缓存策略选择指南
print("\n缓存策略选择指南:")

# 不同缓存大小对比
def test_cache_sizes():
    """测试不同缓存大小的性能影响"""
    sizes = [16, 32, 64, 128, 256, 512, 1024]
    results = {}
    
    # 测试数据:生成可能重复的数据
    def generate_test_data(size, duplication_factor=0.3):
        unique_items = int(size * (1 - duplication_factor))
        duplicated_items = size - unique_items
        data = [f"item_{i}" for i in range(unique_items)]
        # 添加重复项
        data.extend(random.choices(data, k=duplicated_items))
        random.shuffle(data)
        return data
    
    # 模拟计算密集型函数
    def expensive_operation(x):
        time.sleep(0.001)  # 模拟1ms的计算时间
        return sum(ord(c) for c in x) * 2.5
    
    # 测试不同缓存大小
    for maxsize in sizes:
        # 创建带指定缓存大小的函数
        @functools.lru_cache(maxsize=maxsize)
        def cached_operation(x):
            return expensive_operation(x)
        
        # 生成测试数据
        test_data = generate_test_data(2000)
        
        # 执行测试
        start_time = time.time()
        for item in test_data:
            cached_operation(item)
        end_time = time.time()
        
        # 记录结果
        cache_info = cached_operation.cache_info()
        hit_ratio = cache_info.hits / (cache_info.hits + cache_info.misses) if (cache_info.hits + cache_info.misses) > 0 else 0
        
        results[maxsize] = {
            "time": end_time - start_time,
            "hits": cache_info.hits,
            "misses": cache_info.misses,
            "hit_ratio": hit_ratio
        }
    
    # 打印结果
    print("不同缓存大小的性能对比:")
    print("{:<8} {:<12} {:<10} {:<10} {:<10}".format(
        "缓存大小", "执行时间(秒)", "缓存命中", "缓存未命中", "命中率(%)"
    ))
    for size in sizes:
        res = results[size]
        print("{:<8} {:<12.4f} {:<10} {:<10} {:<10.2f}".format(
            size, res["time"], res["hits"], res["misses"], res["hit_ratio"] * 100
        ))

# 运行缓存大小测试
test_cache_sizes()

# 2. 缓存键设计最佳实践
print("\n缓存键设计最佳实践:")

# 测试不同类型参数的缓存效果
@functools.lru_cache(maxsize=None)
def process_with_complex_args(a, b, items=None, options=None):
    """处理具有复杂参数的函数"""
    time.sleep(0.01)  # 模拟计算时间
    return f"处理结果: {a}, {b}, {items}, {options}"

# 正确使用不可变类型作为缓存键
print("使用元组代替列表作为缓存键:")
try:
    # 错误:列表是可变的,不能作为缓存键
    process_with_complex_args(1, 2, items=[1, 2, 3])
except TypeError as e:
    print(f"错误: {e}")

# 正确:使用元组(不可变)
result = process_with_complex_args(1, 2, items=(1, 2, 3))
print(f"成功调用: {result}")

# 正确:字典转换为frozenset
result = process_with_complex_args(1, 2, options=frozenset({"key": "value"}.items()))
print(f"使用frozenset作为参数: {result}")

# 3. 缓存失效策略
class CacheWithTimeout:
    """带超时机制的缓存装饰器"""
    def __init__(self, maxsize=128, timeout=300):
        self.maxsize = maxsize
        self.timeout = timeout  # 超时时间(秒)
        self._cache = {}
        self._expirations = {}
        self._lock = threading.RLock() if threading else None
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 创建缓存键
            key = (args, frozenset(kwargs.items())) if kwargs else args
            
            # 检查是否有锁
            if self._lock:
                with self._lock:
                    return self._get_or_compute(key, func, args, kwargs)
            else:
                return self._get_or_compute(key, func, args, kwargs)
        
        # 添加清除缓存方法
        def clear():
            if self._lock:
                with self._lock:
                    self._cache.clear()
                    self._expirations.clear()
            else:
                self._cache.clear()
                self._expirations.clear()
        
        wrapper.clear_cache = clear
        return wrapper
    
    def _get_or_compute(self, key, func, args, kwargs):
        # 检查缓存是否有效
        current_time = time.time()
        if key in self._cache:
            if current_time < self._expirations[key]:
                # 缓存有效
                return self._cache[key]
            else:
                # 缓存过期,删除
                del self._cache[key]
                del self._expirations[key]
        
        # 计算结果
        result = func(*args, **kwargs)
        
        # 管理缓存大小(简化的LRU逻辑)
        if len(self._cache) >= self.maxsize:
            # 删除最早的项目(简化版,实际应该使用OrderedDict)
            oldest_key = next(iter(self._cache.keys()))
            del self._cache[oldest_key]
            del self._expirations[oldest_key]
        
        # 存储结果
        self._cache[key] = result
        self._expirations[key] = current_time + self.timeout
        
        return result

# 测试带超时的缓存
@CacheWithTimeout(maxsize=10, timeout=2)  # 2秒后缓存过期
def time_sensitive_data(user_id):
    """模拟返回时间敏感的数据"""
    print(f"计算用户 {user_id} 的时间敏感数据")
    return {"user_id": user_id, "timestamp": time.time()}

print("\n带超时机制的缓存测试:")

# 第一次调用(计算结果)
print("首次调用:")
data1 = time_sensitive_data(1)
print(f"结果: {data1}")

# 立即再次调用(使用缓存)
print("\n立即再次调用(使用缓存):")
data2 = time_sensitive_data(1)
print(f"结果: {data2}")
print(f"是否相同: {data1 == data2}")

# 等待缓存过期
print("\n等待2秒让缓存过期...")
time.sleep(2)

# 缓存过期后调用(重新计算)
print("缓存过期后调用:")
data3 = time_sensitive_data(1)
print(f"结果: {data3}")
print(f"是否相同: {data1 == data3}")

# 4. 缓存性能监控
class MonitoredCache:
    """带性能监控的缓存装饰器"""
    def __init__(self, maxsize=128):
        self.maxsize = maxsize
        self.stats = {
            "hits": 0,
            "misses": 0,
            "calls": 0,
            "computation_time": 0,
            "total_time": 0
        }
    
    def __call__(self, func):
        # 创建LRU缓存
        cached_func = functools.lru_cache(maxsize=self.maxsize)(func)
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # 记录总时间
            start_time = time.time()
            
            # 执行调用
            result = cached_func(*args, **kwargs)
            
            # 更新总时间
            self.stats["total_time"] += time.time() - start_time
            self.stats["calls"] += 1
            
            # 获取缓存信息并更新统计
            cache_info = cached_func.cache_info()
            self.stats["hits"] = cache_info.hits
            self.stats["misses"] = cache_info.misses
            
            return result
        
        # 添加获取统计信息的方法
        def get_stats():
            hits = self.stats["hits"]
            misses = self.stats["misses"]
            total = hits + misses
            hit_ratio = hits / total if total > 0 else 0
            
            return {
                **self.stats,
                "hit_ratio": hit_ratio,
                "avg_time_per_call": self.stats["total_time"] / self.stats["calls"] if self.stats["calls"] > 0 else 0
            }
        
        # 添加清除缓存方法
        def clear_cache():
            cached_func.cache_clear()
            # 重置统计
            self.stats = {
                "hits": 0,
                "misses": 0,
                "calls": 0,
                "computation_time": 0,
                "total_time": 0
            }
        
        wrapper.get_stats = get_stats
        wrapper.clear_cache = clear_cache
        
        return wrapper

# 测试带监控的缓存
@MonitoredCache(maxsize=100)
def monitored_function(x):
    """被监控的函数"""
    time.sleep(0.01)  # 模拟计算时间
    return x * x

print("\n带性能监控的缓存测试:")

# 执行一些调用
test_values = [random.randint(1, 50) for _ in range(200)]
for val in test_values:
    monitored_function(val)

# 查看统计信息
stats = monitored_function.get_stats()
print(f"调用次数: {stats['calls']}")
print(f"缓存命中: {stats['hits']}")
print(f"缓存未命中: {stats['misses']}")
print(f"命中率: {stats['hit_ratio'] * 100:.2f}%")
print(f"平均调用时间: {stats['avg_time_per_call'] * 1000:.2f} ms")

# 5. 内存使用优化技巧
print("\n内存使用优化技巧:")

# 使用最大大小限制内存使用
@functools.lru_cache(maxsize=128)  # 限制缓存大小为128项
def memory_optimized_function(x):
    """内存优化的缓存函数"""
    # 生成一些可能占用内存的数据
    return [x] * 1000

# 使用typed参数避免不必要的缓存项
@functools.lru_cache(maxsize=100, typed=True)
def typed_optimized_function(x):
    """使用typed参数优化的函数"""
    time.sleep(0.01)
    return x

# 定期清理缓存的示例
def periodic_cache_cleanup(cached_func, interval=300):
    """定期清理缓存的函数"""
    def cleanup_task():
        while True:
            time.sleep(interval)
            print(f"定期清理缓存: {cached_func.__name__}")
            cached_func.cache_clear()
    
    # 在实际应用中,这里会启动一个后台线程
    # 这里只是示例,不实际启动线程
    print(f"设置了定期清理缓存,间隔: {interval}秒")

# 演示缓存清理设置
periodic_cache_cleanup(memory_optimized_function)
"""

## 5. 性能分析

### 5.1 时间与空间复杂度

| 功能 | 时间复杂度 | 空间复杂度 | 说明 |
|------|------------|------------|------|
| "wraps" | O(1) | O(1) | 仅复制函数元数据,常数时间和空间 |
| "lru_cache" | 平均 O(1),最坏 O(n) | O(maxsize) | 查找/插入平均常数时间,取决于缓存大小 |
| "partial" | O(1) | O(1) | 仅存储预设参数,常数空间 |
| "reduce" | O(n) | O(1) | 遍历序列一次,常数额外空间 |
| "total_ordering" | O(1) | O(1) | 仅生成额外方法,不影响运行时复杂度 |
| "singledispatch" | O(1) - O(m) | O(m) | m为已注册类型数量,查找复杂度取决于调度实现 |
| "cmp_to_key" | O(1) | O(1) | 仅创建键函数,不影响排序算法的复杂度 |

### 5.2 性能比较测试

"``python
import functools
import time
import random
from functools import lru_cache

# 测试配置
TEST_SIZES = [100, 1000, 10000]
REPEAT = 3

# 1. lru_cache vs 手动缓存实现
print("\nlru_cache vs 手动缓存实现性能比较:")

# 手动缓存实现
class ManualCache:
    def __init__(self, maxsize=128):
        self.cache = {}
        self.keys = []
        self.maxsize = maxsize
    
    def get(self, key, func, *args, **kwargs):
        if key in self.cache:
            return self.cache[key]
        
        result = func(*args, **kwargs)
        
        # 简单的LRU实现
        if len(self.keys) >= self.maxsize:
            oldest_key = self.keys.pop(0)
            del self.cache[oldest_key]
        
        self.cache[key] = result
        self.keys.append(key)
        return result

# 测试函数
def fib_manual(n, cache):
    if n <= 1:
        return n
    key = n
    return cache.get(key, lambda: fib_manual(n-1, cache) + fib_manual(n-2, cache))

@lru_cache(maxsize=None)
def fib_lru(n):
    if n <= 1:
        return n
    return fib_lru(n-1) + fib_lru(n-2)

# 运行比较
for size in [30, 35, 40]:
    print(f"\n计算fibonacci({size}):")
    
    # 测试lru_cache
    fib_lru.cache_clear()
    start = time.time()
    result_lru = fib_lru(size)
    lru_time = time.time() - start
    print(f"lru_cache: {lru_time*1000:.2f} ms, 结果: {result_lru}")
    
    # 测试手动缓存
    manual_cache = ManualCache()
    start = time.time()
    result_manual = fib_manual(size, manual_cache)
    manual_time = time.time() - start
    print(f"手动缓存: {manual_time*1000:.2f} ms, 结果: {result_manual}")
    
    # 计算性能比
    ratio = manual_time / lru_time if lru_time > 0 else 0
    print(f"lru_cache 比手动缓存快 {ratio:.2f}x")

# 2. reduce vs for循环性能比较
print("\nreduce vs for循环性能比较:")

for size in TEST_SIZES:
    # 生成测试数据
    data = [random.random() for _ in range(size)]
    
    print(f"\n数据大小: {size}")
    
    # 测试reduce
    total_reduce = 0
    for _ in range(REPEAT):
        start = time.time()
        result = functools.reduce(lambda x, y: x + y, data)
        total_reduce += time.time() - start
    avg_reduce = total_reduce / REPEAT
    print(f"reduce: {avg_reduce*1000:.2f} ms")
    
    # 测试for循环
    total_for = 0
    for _ in range(REPEAT):
        start = time.time()
        result = 0
        for item in data:
            result += item
        total_for += time.time() - start
    avg_for = total_for / REPEAT
    print(f"for循环: {avg_for*1000:.2f} ms")
    
    # 计算性能比
    ratio = avg_for / avg_reduce if avg_reduce > 0 else 0
    print(f"reduce 比 for循环快 {ratio:.2f}x")

# 3. partial vs lambda性能比较
print("\npartial vs lambda性能比较:")

# 原始函数
def power(base, exponent):
    return base ** exponent

for size in TEST_SIZES:
    # 生成测试数据
    bases = [random.random() for _ in range(size)]
    
    print(f"\n数据大小: {size}")
    
    # 测试partial
    square_partial = functools.partial(power, exponent=2)
    total_partial = 0
    for _ in range(REPEAT):
        start = time.time()
        results = [square_partial(base) for base in bases]
        total_partial += time.time() - start
    avg_partial = total_partial / REPEAT
    print(f"partial: {avg_partial*1000:.2f} ms")
    
    # 测试lambda
    square_lambda = lambda x: power(x, 2)
    total_lambda = 0
    for _ in range(REPEAT):
        start = time.time()
        results = [square_lambda(base) for base in bases]
        total_lambda += time.time() - start
    avg_lambda = total_lambda / REPEAT
    print(f"lambda: {avg_lambda*1000:.2f} ms")
    
    # 计算性能比
    ratio = avg_lambda / avg_partial if avg_partial > 0 else 0
    print(f"partial 比 lambda快 {ratio:.2f}x")

# 4. singledispatch vs 手动类型检查性能比较
print("\n singledispatch vs 手动类型检查性能比较:")

# 使用singledispatch
@functools.singledispatch
def process_value(value):
    return f"未知类型: {type(value).__name__}"

@process_value.register(int)
def _(value):
    return f"整数: {value}"

@process_value.register(float)
def _(value):
    return f"浮点数: {value}"

@process_value.register(str)
def _(value):
    return f"字符串: {value}"

@process_value.register(list)
def _(value):
    return f"列表: {len(value)} 个元素"

# 手动类型检查
def manual_process_value(value):
    if isinstance(value, int):
        return f"整数: {value}"
    elif isinstance(value, float):
        return f"浮点数: {value}"
    elif isinstance(value, str):
        return f"字符串: {value}"
    elif isinstance(value, list):
        return f"列表: {len(value)} 个元素"
    else:
        return f"未知类型: {type(value).__name__}"

# 生成测试数据
test_data = []
for _ in range(1000):
    test_data.extend([
        random.randint(1, 100),
        random.random() * 100,
        f"string_{random.randint(1, 100)}",
        [random.randint(1, 10) for _ in range(5)]
    ])

print(f"\n测试数据大小: {len(test_data)}")

# 测试singledispatch
total_sd = 0
for _ in range(REPEAT):
    start = time.time()
    results = [process_value(item) for item in test_data]
    total_sd += time.time() - start
avg_sd = total_sd / REPEAT
print(f"singledispatch: {avg_sd*1000:.2f} ms")

# 测试手动类型检查
total_manual = 0
for _ in range(REPEAT):
    start = time.time()
    results = [manual_process_value(item) for item in test_data]
    total_manual += time.time() - start
avg_manual = total_manual / REPEAT
print(f"手动类型检查: {avg_manual*1000:.2f} ms")

# 计算性能比
ratio = avg_manual / avg_sd if avg_sd > 0 else 0
print(f"singledispatch 比手动类型检查快 {ratio:.2f}x")
```

## 6. 使用注意事项

### 6.1 缓存使用的潜在问题

1. **内存消耗**:"lru_cache"会存储函数调用的结果,如果缓存大小设置过大或函数返回值过大,可能导致内存占用过高.
   
2. **不可哈希参数**:被缓存的函数参数必须是可哈希的(如整数,字符串,元组等),列表,字典等可变类型不能直接用作缓存键.

3. **状态变化函数**:对于依赖外部状态或有副作用的函数,缓存可能导致不一致的结果.

4. **缓存过期**:"lru_cache"本身没有内置的缓存过期机制,需要手动实现或使用第三方库.

5. **递归深度限制**:使用"lru_cache"优化递归函数时,仍需注意Python的递归深度限制.

### 6.2 避免常见错误

```python
import functools

# 错误示例1: 使用不可哈希的参数
@functools.lru_cache()
def process_list(items):
    return sum(items)

try:
    process_list([1, 2, 3])  # 错误:列表不可哈希
except TypeError as e:
    print(f"错误1: {e}")

# 正确做法: 转换为元组
@functools.lru_cache()
def process_tuple(items):
    return sum(items)

result = process_tuple((1, 2, 3))  # 正确
print(f"正确做法结果: {result}")

# 错误示例2: 缓存依赖外部状态的函数
counter = 0

@functools.lru_cache()
def get_counter():
    global counter
    counter += 1
    return counter

print(f"第一次调用: {get_counter()}")  # 返回1
print(f"第二次调用: {get_counter()}")  # 返回1(从缓存获取,计数器没有增加)

# 错误示例3: 缓存大对象导致内存问题
@functools.lru_cache(maxsize=None)
def generate_large_object(n):
    # 生成一个大列表
    return [i for i in range(n)]

# 调用几次后可能导致内存问题
# 正确做法:限制缓存大小或使用弱引用缓存

# 错误示例4: 不适当的缓存键设计
@functools.lru_cache()
def process_data(data_dict):
    # 即使内容相同,不同的字典实例也会被视为不同的键
    return sum(data_dict.values())

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2}  # 内容相同的不同实例

print(f"dict1结果: {process_data(dict1)}")  # 计算
print(f"dict2结果: {process_data(dict2)}")  # 再次计算,没有使用缓存

# 正确做法: 使用frozenset或其他可哈希的表示
@functools.lru_cache()
def process_data_fixed(data_items):
    return sum(value for _, value in data_items)

print(f"正确做法 - dict1: {process_data_fixed(frozenset(dict1.items()))}")
print(f"正确做法 - dict2: {process_data_fixed(frozenset(dict2.items()))}")  # 这次会使用缓存
```

### 6.3 线程安全考虑

虽然"lru_cache"本身是线程安全的,但在多线程环境中使用时仍需注意一些事项:

```python
import functools
import threading
import time

# 线程安全的缓存使用示例
@functools.lru_cache(maxsize=100)
def expensive_operation(x):
    """模拟昂贵的操作"""
    time.sleep(0.1)  # 模拟耗时操作
    return x * x

# 线程函数
def worker(values, results, index):
    """工作线程函数"""
    for i, value in enumerate(values):
        results[index + i] = expensive_operation(value)

# 多线程测试
def test_thread_safety():
    print("\n线程安全测试:")
    
    # 生成测试数据
    test_values = [i % 20 for i in range(100)]  # 故意包含重复值以测试缓存
    results = [None] * len(test_values)
    
    # 创建线程
    thread_count = 4
    values_per_thread = len(test_values) // thread_count
    threads = []
    
    start_time = time.time()
    
    # 启动线程
    for i in range(thread_count):
        start = i * values_per_thread
        end = start + values_per_thread if i < thread_count - 1 else len(test_values)
        thread_values = test_values[start:end]
        thread = threading.Thread(
            target=worker,
            args=(thread_values, results, start)
        )
        threads.append(thread)
        thread.start()
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()
    
    end_time = time.time()
    
    print(f"多线程执行时间: {(end_time - start_time) * 1000:.2f} ms")
    print(f"缓存信息: {expensive_operation.cache_info()}")
    
    # 验证结果正确性
    expected_results = [x * x for x in test_values]
    assert results == expected_results, "结果不正确!"
    print("结果验证通过!")

# 运行线程安全测试
test_thread_safety()

# 注意:虽然lru_cache是线程安全的,但在以下情况仍需额外注意:
# 1. 函数本身有副作用或修改共享状态
# 2. 需要精确控制缓存过期或清理时机
# 3. 缓存大小管理在高并发环境中可能不够精细
```

## 7. 总结与最佳实践

### 7.1 主要优势

1. **代码简洁性**:使用"functools"模块可以大幅减少样板代码,使代码更加简洁易读.

2. **性能优化**:"lru_cache"提供了简单而强大的缓存机制,可以显著提升重复计算的性能.

3. **函数式编程支持**:提供了丰富的函数式编程工具,如"reduce","partial"等,使函数式编程范式在Python中更加实用.

4. **装饰器增强**:"wraps","total_ordering"等工具使装饰器和类的定义更加规范和功能完善.

5. **类型分发**:"singledispatch"提供了一种优雅的方式来实现根据参数类型选择不同行为的多态函数.

### 7.2 最佳实践建议

1. **缓存策略**:
   - 对计算密集型,结果确定性的函数使用"lru_cache"
   - 根据实际数据分布选择合适的缓存大小
   - 避免缓存大对象或无限增长的缓存

2. **装饰器使用**:
   - 始终使用"wraps"装饰器来保留原函数的元数据
   - 合理组合多个装饰器,注意装饰顺序

3. **函数设计**:
   - 对于频繁调用的多参数函数,考虑使用"partial"创建更简单的接口
   - 对于需要根据参数类型有不同行为的函数,使用"singledispatch"代替复杂的条件判断

4. **性能监控**:
   - 定期检查缓存命中率,调整缓存大小
   - 监控内存使用,避免缓存导致内存泄漏

5. **线程安全**:
   - 在多线程环境中使用时,确保函数本身是线程安全的
   - 考虑使用适当的锁机制来保护共享状态

### 7.3 选择使用建议

| 场景 | 推荐工具 | 原因 |
|------|----------|------|
| 缓存计算结果 | "lru_cache" | 简单高效,内置LRU策略 |
| 装饰器创建 | "wraps" | 保留原函数元数据 |
| 函数参数固定 | "partial" | 创建简洁的函数变体 |
| 归约操作 | "reduce" | 函数式编程风格的归约 |
| 类比较方法 | "total_ordering" | 减少样板代码 |
| 类型分发 | "singledispatch" | 优雅实现基于类型的多态 |
| 比较函数转换 | "cmp_to_key" | 兼容传统比较函数 |

### 7.4 学习资源与进阶阅读

1. **官方文档**:[Python functools模块文档](https://docs.python.org/3/library/functools.html)
2. **函数式编程**:<Python函数式编程>(Steven F. Lott著)
3. **装饰器深入**:<流畅的Python>第9章(Luciano Ramalho著)
4. **性能优化**:<Python高性能编程>(Micha Gorelick & Ian Ozsvald著)

### 7.5 学习总结

"functools"模块是Python标准库中用于函数式编程的核心工具集,提供了从简单的函数装饰器到复杂的函数变换等多种功能.通过合理使用这些工具,可以编写出更加简洁,高效,可维护的代码.

在实际应用中,"lru_cache"常用于优化计算密集型函数的性能,"wraps"用于创建高质量的装饰器,"partial"用于函数接口的适配和简化,"reduce"用于数据聚合,"total_ordering"用于简化类的比较方法实现,而"singledispatch"则为Python带来了基于类型的函数多态能力.

通过本模块的学习,我们不仅掌握了这些工具的基本用法,还了解了如何在实际场景中组合使用它们来解决复杂问题,以及如何避免常见的陷阱和错误.这些知识将帮助我们在日常编程中更加得心应手地应用函数式编程思想,编写出更高质量的Python代码.","}}}
```
"""
'''
"
'
