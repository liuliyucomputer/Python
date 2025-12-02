"""
# functools模块详解：Python函数式编程的核心工具

functools模块提供了一系列高阶函数（接收函数作为参数或返回函数的函数）和用于函数操作的工具，是Python实现函数式编程范式的核心模块之一。这些工具可以帮助开发者编写更简洁、更具声明式风格的代码。

## 1. 核心功能概览

functools模块主要提供以下几类功能：

1. **函数转换与包装**：如`lru_cache`、`wraps`、`singledispatch`等
2. **函数组合与操作**：如`reduce`、`partial`等
3. **比较工具**：如`cmp_to_key`
4. **泛函编程支持**：如`total_ordering`

## 2. 常用函数详解

### 2.1 functools.reduce - 函数归约

`reduce`函数对可迭代对象应用累积操作，从左到右依次将当前结果与下一个元素传给指定函数。

```python
from functools import reduce

# 计算列表元素的乘积
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"列表元素乘积: {product}")  # 输出: 120

# 使用初始值
result = reduce(lambda x, y: x + y, numbers, 100)  # 从100开始累加
print(f"带初始值的累加: {result}")  # 输出: 115
```

### 2.2 functools.partial - 函数参数冻结

`partial`函数用于创建一个新函数，该函数是原函数的部分参数被冻结后的版本，常用于简化函数调用。

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

# 创建平方函数（指数固定为2）
square = partial(power, exponent=2)

# 创建以2为底的幂函数（底数固定为2）
power_of_two = partial(power, 2)

print(square(5))  # 输出: 25
print(power_of_two(10))  # 输出: 1024
```

### 2.3 functools.lru_cache - 最近最少使用缓存

`lru_cache`是一个装饰器，用于缓存函数调用结果，避免重复计算，显著提高递归或重复调用函数的性能。

```python
from functools import lru_cache
import time

@lru_cache(maxsize=None)  # 无限制缓存

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 测试性能
start = time.time()
result = fibonacci(35)
end = time.time()
print(f"Fibonacci(35) = {result}")
print(f"计算时间: {end - start:.6f}秒")

# 再次调用，将使用缓存结果
start = time.time()
result = fibonacci(35)
end = time.time()
print(f"缓存后计算时间: {end - start:.6f}秒")

# 查看缓存统计信息
print(fibonacci.cache_info())
```

### 2.4 functools.wraps - 保留原函数元数据

`wraps`是一个装饰器工厂，用于在自定义装饰器中保留被装饰函数的元数据（如名称、文档字符串等）。

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用函数: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example_function(x, y):
    """这是示例函数的文档字符串"""
    return x + y

print(example_function.__name__)  # 输出: example_function
print(example_function.__doc__)   # 输出: 这是示例函数的文档字符串
```

### 2.5 functools.singledispatch - 单分派泛函数

`singledispatch`装饰器将一个普通函数转变为泛函数，可以根据第一个参数的类型执行不同的实现。

```python
from functools import singledispatch

@singledispatch
def format_value(value):
    """默认格式化函数"""
    return str(value)

@format_value.register(int)
def _(value):
    return f"整数: {value}"

@format_value.register(list)
def _(value):
    return f"列表（长度{len(value)}）: {value}"

@format_value.register(dict)
def _(value):
    return f"字典（{len(value)}个键值对）: {value}"

# 测试不同类型
print(format_value(42))        # 输出: 整数: 42
print(format_value([1, 2, 3]))  # 输出: 列表（长度3）: [1, 2, 3]
print(format_value({'a': 1, 'b': 2}))  # 输出: 字典（2个键值对）: {'a': 1, 'b': 2}
print(format_value("hello"))   # 输出: hello
```

### 2.6 functools.total_ordering - 自动生成比较方法

`total_ordering`装饰器用于自动生成类的比较方法（`__lt__`, `__le__`, `__gt__`, `__ge__`），只需定义其中的一部分即可。

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

# 创建对象并测试比较
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p3 = Person("Charlie", 30)

print(p1 > p2)   # True
print(p1 <= p3)  # True
print(p2 != p3)  # True
```

### 2.7 functools.cmp_to_key - 比较函数转换

`cmp_to_key`函数将旧式的比较函数（返回-1、0或1）转换为键函数，用于支持Python 3中的排序方法。

```python
from functools import cmp_to_key

# 旧式比较函数

def compare_lengths(a, b):
    """比较两个字符串的长度"""
    if len(a) < len(b):
        return -1
    elif len(a) > len(b):
        return 1
    return 0

strings = ["apple", "banana", "cherry", "date"]

# 使用cmp_to_key转换比较函数
strings_sorted = sorted(strings, key=cmp_to_key(compare_lengths))
print(strings_sorted)  # 输出: ['date', 'apple', 'cherry', 'banana']
```

### 2.8 functools.cache - 简单缓存装饰器

Python 3.9+中新增的`cache`装饰器是`lru_cache(maxsize=None)`的便捷版本，提供无限制的缓存。

```python
from functools import cache

@cache
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(10))  # 计算并缓存
print(factorial(10))  # 使用缓存结果
```

## 3. 高级应用示例

### 3.1 函数组合

使用`reduce`和`partial`实现函数组合，将多个函数串联起来执行。

```python
from functools import reduce, partial

def compose(*functions):
    """组合多个函数，从右到左执行"""
    return reduce(lambda f, g: lambda x: f(g(x)), functions)

# 示例函数
def add_one(x):
    return x + 1

def multiply_by_two(x):
    return x * 2

def square(x):
    return x ** 2

# 组合函数：先加1，再乘2，最后平方
transform = compose(square, multiply_by_two, add_one)

result = transform(3)  # ((3+1)*2)^2 = 64
print(result)
```

### 3.2 记忆化递归

结合`lru_cache`优化递归算法性能。

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def longest_common_subsequence(s1, s2):
    """计算两个字符串的最长公共子序列长度"""
    if not s1 or not s2:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + longest_common_subsequence(s1[:-1], s2[:-1])
    else:
        return max(longest_common_subsequence(s1[:-1], s2),
                  longest_common_subsequence(s1, s2[:-1]))

# 测试
str1 = "ABCDGH"
str2 = "AEDFHR"
print(longest_common_subsequence(str1, str2))  # 输出: 3 (ADH)
```

### 3.3 装饰器链

使用`wraps`创建可堆叠的装饰器。

```python
from functools import wraps
import time

def timing_decorator(func):
    """计算函数执行时间的装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.6f}秒")
        return result
    return wrapper

def logging_decorator(func):
    """记录函数调用的装饰器"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用 {func.__name__} 与参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} 返回: {result}")
        return result
    return wrapper

# 应用多个装饰器
@timing_decorator
@logging_decorator
def compute_complex(x, y):
    """一个复杂计算示例"""
    time.sleep(0.1)  # 模拟耗时操作
    return x ** y

compute_complex(2, 10)
```

## 4. 注意事项和最佳实践

1. **缓存使用建议**：
   - 对计算密集型函数使用`lru_cache`或`cache`
   - 为缓存设置合理的`maxsize`以避免内存过度使用
   - 仅缓存参数可哈希的函数调用

2. **装饰器设计原则**：
   - 始终使用`wraps`保留原函数元数据
   - 装饰器应透明地传递参数和返回值
   - 考虑装饰器的可组合性

3. **函数式编程风格**：
   - 使用`partial`简化重复参数模式
   - 结合`reduce`和其他高阶函数实现声明式代码
   - 利用`singledispatch`实现多态行为

4. **性能考量**：
   - 缓存虽好，但对简单函数可能引入额外开销
   - 递归函数优化时，确保基本情况正确实现

## 5. 总结

functools模块是Python实现函数式编程范式的强大工具集，它提供了多种高阶函数和装饰器，帮助开发者编写更简洁、高效、可维护的代码。通过合理使用functools中的工具，我们可以：

- 优化函数调用性能（缓存）
- 简化复杂函数（部分应用）
- 创建灵活的装饰器（元数据保留）
- 实现多态行为（单分派）
- 简化类实现（比较方法生成）

函数式编程强调不可变性、纯函数和组合，这些概念在现代Python开发中越来越受到重视，functools模块为实践这些理念提供了坚实的基础。