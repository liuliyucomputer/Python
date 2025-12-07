# Python装饰器详细指南

## 一、模块概述

装饰器（Decorator）是Python中一种强大的函数式编程工具，它允许在不修改原函数代码的情况下扩展或修改函数的行为。装饰器本质上是一个返回函数的函数，它接受一个函数作为参数，并返回一个新的函数。装饰器广泛应用于日志记录、性能测试、权限验证、缓存等场景。

## 二、基本概念

1. **装饰器函数**：接受一个函数作为参数，并返回一个新的函数
2. **被装饰函数**：被装饰器修改或扩展的函数
3. **装饰器语法**：使用`@装饰器名`的语法糖来应用装饰器
4. **闭包**：装饰器内部通常使用闭包来保存被装饰函数的引用
5. **函数对象**：在Python中，函数是第一类对象，可以作为参数传递、作为返回值返回、赋值给变量等

## 三、基本用法

### 1. 简单装饰器

```python
# 定义一个简单的装饰器

def my_decorator(func):
    def wrapper():
        print("装饰器添加的功能 - 执行前")
        func()
        print("装饰器添加的功能 - 执行后")
    return wrapper

# 使用装饰器

@my_decorator
def say_hello():
    print("Hello, World!")

# 调用被装饰的函数
say_hello()
```

输出结果：
```
装饰器添加的功能 - 执行前
Hello, World!
装饰器添加的功能 - 执行后
```

### 2. 带参数的被装饰函数

```python
# 装饰带参数的函数
def my_decorator(func):
    def wrapper(name):
        print("装饰器添加的功能 - 执行前")
        func(name)
        print("装饰器添加的功能 - 执行后")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

输出结果：
```
装饰器添加的功能 - 执行前
Hello, Alice!
装饰器添加的功能 - 执行后
```

### 3. 带任意参数的被装饰函数

```python
# 装饰带任意参数的函数
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("装饰器添加的功能 - 执行前")
        result = func(*args, **kwargs)
        print("装饰器添加的功能 - 执行后")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

@my_decorator
def greet(name, message="Hello"):
    return f"{message}, {name}!"

result1 = add(3, 5)
print(f"Add result: {result1}")

result2 = greet("Bob", message="Hi")
print(f"Greet result: {result2}")
```

输出结果：
```
装饰器添加的功能 - 执行前
装饰器添加的功能 - 执行后
Add result: 8
装饰器添加的功能 - 执行前
装饰器添加的功能 - 执行后
Greet result: Hi, Bob!
```

### 4. 保留原函数信息

默认情况下，装饰器返回的新函数会丢失原函数的名称、文档字符串等信息，使用`functools.wraps`可以保留这些信息：

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """装饰器的包装函数"""
        print("装饰器添加的功能 - 执行前")
        result = func(*args, **kwargs)
        print("装饰器添加的功能 - 执行后")
        return result
    return wrapper

@my_decorator
def say_hello():
    """这是一个打招呼的函数"""
    print("Hello, World!")

print(f"函数名称: {say_hello.__name__}")
print(f"函数文档: {say_hello.__doc__}")
```

输出结果：
```
函数名称: say_hello
函数文档: 这是一个打招呼的函数
```

## 四、高级用法

### 1. 带参数的装饰器

装饰器本身也可以接受参数，需要额外一层函数来处理：

```python
import functools

def repeat(num_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def say_hello():
    print("Hello!")

@repeat(num_times=2)
def greet(name):
    return f"Hello, {name}!"

say_hello()
result = greet("Alice")
print(result)
```

输出结果：
```
Hello!
Hello!
Hello!
Hello, Alice!
Hello, Alice!
```

### 2. 多个装饰器

一个函数可以应用多个装饰器，装饰器的应用顺序是从上到下（从外到内）：

```python
import functools

def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("装饰器1 - 执行前")
        result = func(*args, **kwargs)
        print("装饰器1 - 执行后")
        return result
    return wrapper

def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("装饰器2 - 执行前")
        result = func(*args, **kwargs)
        print("装饰器2 - 执行后")
        return result
    return wrapper

# 应用多个装饰器
@decorator1
@decorator2
def say_hello():
    print("Hello, World!")

say_hello()
```

输出结果：
```
装饰器1 - 执行前
装饰器2 - 执行前
Hello, World!
装饰器2 - 执行后
装饰器1 - 执行后
```

### 3. 类装饰器

使用类作为装饰器，需要实现`__call__`方法：

```python
import functools

class MyDecorator:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)
    
    def __call__(self, *args, **kwargs):
        print("类装饰器添加的功能 - 执行前")
        result = self.func(*args, **kwargs)
        print("类装饰器添加的功能 - 执行后")
        return result

@MyDecorator
def say_hello():
    """这是一个打招呼的函数"""
    print("Hello, World!")

print(f"函数名称: {say_hello.__name__}")
print(f"函数文档: {say_hello.__doc__}")
say_hello()
```

输出结果：
```
函数名称: say_hello
函数文档: 这是一个打招呼的函数
类装饰器添加的功能 - 执行前
Hello, World!
类装饰器添加的功能 - 执行后
```

### 4. 带参数的类装饰器

类装饰器也可以接受参数，需要额外一层`__init__`方法处理：

```python
import functools

class Repeat:
    def __init__(self, num_times):
        self.num_times = num_times
    
    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeat(num_times=3)
def say_hello():
    print("Hello!")

say_hello()
```

输出结果：
```
Hello!
Hello!
Hello!
```

### 5. 装饰器应用于类方法

```python
import functools

def method_decorator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"方法装饰器 - 执行 {func.__name__} 前")
        result = func(self, *args, **kwargs)
        print(f"方法装饰器 - 执行 {func.__name__} 后")
        return result
    return wrapper

class MyClass:
    @method_decorator
    def my_method(self, name):
        print(f"Hello, {name} from MyClass!")
        return f"Greeted {name}"

obj = MyClass()
result = obj.my_method("Alice")
print(f"结果: {result}")
```

输出结果：
```
方法装饰器 - 执行 my_method 前
Hello, Alice from MyClass!
方法装饰器 - 执行 my_method 后
结果: Greeted Alice
```

### 6. 装饰器应用于类

```python
import functools

def class_decorator(cls):
    # 保存原始的 __init__ 方法
    original_init = cls.__init__
    
    # 定义新的 __init__ 方法
    def new_init(self, *args, **kwargs):
        print(f"类装饰器 - 初始化 {cls.__name__} 前")
        original_init(self, *args, **kwargs)
        print(f"类装饰器 - 初始化 {cls.__name__} 后")
    
    # 替换类的 __init__ 方法
    cls.__init__ = new_init
    
    # 添加新的方法
    def new_method(self):
        print(f"类装饰器添加的新方法 - {self.name}")
    
    cls.new_method = new_method
    return cls

@class_decorator
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, I'm {self.name}, {self.age} years old.")

# 创建对象
person = Person("Bob", 30)
person.greet()
person.new_method()
```

输出结果：
```
类装饰器 - 初始化 Person 前
类装饰器 - 初始化 Person 后
Hello, I'm Bob, 30 years old.
类装饰器添加的新方法 - Bob
```

## 五、实际应用示例

### 1. 日志记录装饰器

```python
import functools
import datetime


def log_decorator(func):
    """记录函数调用日志的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 记录开始时间
        start_time = datetime.datetime.now()
        
        # 记录函数信息
        print(f"[{start_time}] 函数 {func.__name__} 开始执行")
        print(f"  参数: args={args}, kwargs={kwargs}")
        
        try:
            # 执行函数
            result = func(*args, **kwargs)
            # 记录结果
            print(f"  结果: {result}")
            return result
        except Exception as e:
            # 记录异常
            print(f"  异常: {type(e).__name__}: {e}")
            raise
        finally:
            # 记录结束时间
            end_time = datetime.datetime.now()
            execution_time = end_time - start_time
            print(f"[{end_time}] 函数 {func.__name__} 执行结束，耗时 {execution_time.total_seconds():.4f} 秒")
    return wrapper


@log_decorator
def add(a, b):
    """两个数相加"""
    return a + b


@log_decorator
def divide(a, b):
    """两个数相除"""
    return a / b


# 使用示例
add(3, 5)
divide(10, 2)
try:
    divide(10, 0)
except Exception:
    pass
```

输出结果：
```
[2025-12-06 17:01:15.123456] 函数 add 开始执行
  参数: args=(3, 5), kwargs={}
  结果: 8
[2025-12-06 17:01:15.123460] 函数 add 执行结束，耗时 0.0000 秒
[2025-12-06 17:01:15.123462] 函数 divide 开始执行
  参数: args=(10, 2), kwargs={}
  结果: 5.0
[2025-12-06 17:01:15.123465] 函数 divide 执行结束，耗时 0.0000 秒
[2025-12-06 17:01:15.123467] 函数 divide 开始执行
  参数: args=(10, 0), kwargs={}
  异常: ZeroDivisionError: division by zero
[2025-12-06 17:01:15.123480] 函数 divide 执行结束，耗时 0.0000 秒
```

### 2. 性能测试装饰器

```python
import functools
import time
import random


def performance_decorator(func):
    """测试函数性能的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行耗时: {execution_time:.4f} 秒")
        return result
    return wrapper


@performance_decorator
def slow_function():
    """模拟一个缓慢的函数"""
    time.sleep(random.uniform(0.1, 0.5))
    return "完成"


@performance_decorator
def fast_function():
    """模拟一个快速的函数"""
    return "完成"


# 使用示例
for i in range(3):
    slow_function()
    fast_function()
```

输出结果：
```
函数 slow_function 执行耗时: 0.3456 秒
函数 fast_function 执行耗时: 0.0000 秒
函数 slow_function 执行耗时: 0.1234 秒
函数 fast_function 执行耗时: 0.0000 秒
函数 slow_function 执行耗时: 0.4567 秒
函数 fast_function 执行耗时: 0.0000 秒
```

### 3. 缓存装饰器

```python
import functools
import time


def cache_decorator(func):
    """缓存函数结果的装饰器"""
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 创建缓存键
        cache_key = str(args) + str(sorted(kwargs.items()))
        
        if cache_key in cache:
            print(f"从缓存中获取 {func.__name__}{args} 的结果")
            return cache[cache_key]
        else:
            print(f"计算 {func.__name__}{args} 的结果")
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return result
    return wrapper


@cache_decorator
def expensive_calculation(n):
    """模拟一个昂贵的计算"""
    time.sleep(1)  # 模拟耗时操作
    return n * n


# 使用示例
print(expensive_calculation(5))
print(expensive_calculation(5))  # 从缓存获取
print(expensive_calculation(10))
print(expensive_calculation(10))  # 从缓存获取

# Python内置的缓存装饰器
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    """计算斐波那契数"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print("\n使用lru_cache:")
start_time = time.time()
print(fibonacci(30))
end_time = time.time()
print(f"计算fibonacci(30)耗时: {end_time - start_time:.4f} 秒")

start_time = time.time()
print(fibonacci(30))  # 从缓存获取
end_time = time.time()
print(f"再次计算fibonacci(30)耗时: {end_time - start_time:.4f} 秒")
```

输出结果：
```
计算 expensive_calculation(5) 的结果
25
从缓存中获取 expensive_calculation(5) 的结果
25
计算 expensive_calculation(10) 的结果
100
从缓存中获取 expensive_calculation(10) 的结果
100

使用lru_cache:
832040
计算fibonacci(30)耗时: 0.0001 秒
832040
再次计算fibonacci(30)耗时: 0.0000 秒
```

### 4. 权限验证装饰器

```python
import functools


# 模拟用户角色
current_user = {"name": "admin", "role": "admin"}


def requires_permission(required_role):
    """权限验证装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            user_role = current_user.get("role")
            if user_role == required_role or user_role == "admin":
                print(f"用户 {current_user['name']} 有权限执行 {func.__name__}")
                return func(*args, **kwargs)
            else:
                print(f"用户 {current_user['name']} 没有权限执行 {func.__name__}")
                raise PermissionError(f"需要 {required_role} 权限")
        return wrapper
    return decorator


@requires_permission("user")
def view_data():
    """查看数据"""
    return "数据内容"


@requires_permission("editor")
def edit_data():
    """编辑数据"""
    return "数据已更新"


@requires_permission("admin")
def delete_data():
    """删除数据"""
    return "数据已删除"


# 使用示例
print(view_data())
print(edit_data())
print(delete_data())

# 切换用户
current_user["role"] = "user"
print("\n切换到普通用户:")
print(view_data())
try:
    print(edit_data())
except PermissionError:
    pass
try:
    print(delete_data())
except PermissionError:
    pass
```

输出结果：
```
用户 admin 有权限执行 view_data
数据内容
用户 admin 有权限执行 edit_data
数据已更新
用户 admin 有权限执行 delete_data
数据已删除

切换到普通用户:
用户 admin 有权限执行 view_data
数据内容
用户 admin 没有权限执行 edit_data
用户 admin 没有权限执行 delete_data
```

### 5. 重试装饰器

```python
import functools
import time
import random


def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """重试装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            current_delay = delay
            
            while attempts < max_attempts:
                try:
                    attempts += 1
                    print(f"尝试执行 {func.__name__}，第 {attempts} 次")
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempts == max_attempts:
                        print(f"执行 {func.__name__} 失败，已达到最大重试次数")
                        raise
                    else:
                        print(f"执行 {func.__name__} 失败，{type(e).__name__}: {e}")
                        print(f"{current_delay} 秒后重试...")
                        time.sleep(current_delay)
                        current_delay *= backoff  # 指数退避
        return wrapper
    return decorator


@retry(max_attempts=3, delay=0.1, exceptions=(ValueError,))
def unreliable_function():
    """模拟一个不可靠的函数"""
    if random.random() > 0.5:
        raise ValueError("随机错误")
    return "成功"


# 使用示例
try:
    result = unreliable_function()
    print(f"结果: {result}")
except Exception as e:
    print(f"最终失败: {e}")
```

输出结果：
```
尝试执行 unreliable_function，第 1 次
执行 unreliable_function 失败，ValueError: 随机错误
0.1 秒后重试...
尝试执行 unreliable_function，第 2 次
执行 unreliable_function 失败，ValueError: 随机错误
0.2 秒后重试...
尝试执行 unreliable_function，第 3 次
结果: 成功
```

## 六、最佳实践

1. **使用functools.wraps**：保留被装饰函数的元信息，如名称、文档字符串等
2. **保持装饰器简单**：装饰器应该专注于单一功能，避免过于复杂
3. **使用参数化装饰器**：通过参数化装饰器提高灵活性
4. **处理异常**：在装饰器中适当处理异常，避免掩盖被装饰函数的异常
5. **考虑性能**：对于频繁调用的函数，避免在装饰器中添加过多的性能开销
6. **测试装饰器**：确保装饰器在各种情况下都能正常工作
7. **文档化装饰器**：为装饰器添加清晰的文档字符串，说明其功能和用法
8. **避免过度使用**：不要为了使用装饰器而使用装饰器，确保装饰器确实带来了好处

## 七、总结

装饰器是Python中一种强大的编程工具，它允许在不修改原函数代码的情况下扩展或修改函数的行为。装饰器广泛应用于日志记录、性能测试、权限验证、缓存等场景。

从简单的装饰器到带参数的装饰器、类装饰器，再到实际应用中的各种装饰器模式，掌握装饰器的使用可以使代码更加简洁、灵活和可维护。

通过学习和实践装饰器，开发者可以提高Python编程水平，编写更优雅、更高效的代码。