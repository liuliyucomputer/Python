# Python装饰器高级应用

## 1. 装饰器基础回顾

装饰器是Python中的一种强大工具，允许我们在不修改原始函数代码的情况下，增强或修改函数的行为。

### 基本装饰器结构

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # 在调用原函数前执行的代码
        print("函数调用前")
        result = func(*args, **kwargs)
        # 在调用原函数后执行的代码
        print("函数调用后")
        return result
    return wrapper

@decorator
def say_hello(name):
    print(f"你好，{name}！")
    
# 等同于 say_hello = decorator(say_hello)
```

## 2. 带参数的装饰器

有时我们需要创建可以接收参数的装饰器，这需要额外一层嵌套函数。

```python
def repeat(n=1):
    """一个可以接收参数的装饰器，用于重复执行函数n次"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"你好，{name}！"

print(greet("张三"))  # 将输出 ["你好，张三！", "你好，张三！", "你好，张三！"]
```

## 3. 类装饰器

装饰器不仅可以是函数，还可以是类。

```python
class CountCalls:
    """统计函数调用次数的类装饰器"""
    def __init__(self, func):
        self.func = func
        self.count = 0
        
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"函数 {self.func.__name__} 已被调用 {self.count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi!")
    
say_hi()  # 输出: 函数 say_hi 已被调用 1 次 / Hi!
say_hi()  # 输出: 函数 say_hi 已被调用 2 次 / Hi!
```

## 4. 保留函数元数据

当使用装饰器时，被装饰函数的元数据（如名称、文档字符串等）会丢失，这可能导致调试困难。Python的`functools.wraps`装饰器可以解决这个问题：

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # 保留被装饰函数的元数据
    def wrapper(*args, **kwargs):
        """包装函数的文档"""
        print("调用前")
        result = func(*args, **kwargs)
        print("调用后")
        return result
    return wrapper

@my_decorator
def example():
    """这是原函数的文档字符串"""
    pass

print(example.__name__)  # 输出 'example' 而不是 'wrapper'
print(example.__doc__)   # 输出 '这是原函数的文档字符串'
```

## 5. 高级应用场景

### 5.1 执行时间测量

```python
import time
from functools import wraps

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"函数 {func.__name__} 执行时间: {end_time - start_time:.6f} 秒")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """一个故意执行缓慢的函数"""
    time.sleep(1)
    
slow_function()  # 输出: 函数 slow_function 执行时间: 1.000123 秒
```

### 5.2 缓存装饰器（记忆化）

```python
def memoize(func):
    """缓存函数结果的装饰器"""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    """计算斐波那契数列第n项"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 测试性能
import time
start = time.time()
result = fibonacci(35)
end = time.time()
print(f"fibonacci(35) = {result}, 耗时: {end - start:.6f} 秒")
# 如果没有缓存，计算 fibonacci(35) 将需要很长时间
```

### 5.3 参数验证装饰器

```python
def validate_types(*types):
    """验证函数参数类型的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 检查位置参数类型
            for arg, expected_type in zip(args, types):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"参数 {arg} 应该是 {expected_type} 类型，但得到了 {type(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(int, int)
def add_numbers(a, b):
    return a + b

print(add_numbers(1, 2))  # 输出: 3
# print(add_numbers("1", 2))  # 引发 TypeError
```

### 5.4 重试装饰器

```python
import time
import random
from functools import wraps

def retry(max_attempts=3, delay=1):
    """在函数失败时自动重试的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        raise
                    print(f"尝试 {attempts} 失败: {str(e)}. 将在 {delay} 秒后重试...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=5, delay=0.5)
def unstable_function():
    """一个不稳定的函数，有时会失败"""
    if random.random() < 0.7:  # 70% 的几率失败
        raise ValueError("随机错误！")
    return "成功执行！"

print(unstable_function())  # 可能会输出几次错误消息，然后成功，或者最终失败
```

### 5.5 装饰器堆叠

装饰器可以堆叠使用，从而组合多种功能：

```python
@timing_decorator
@memoize
def complex_calculation(n):
    """一个复杂计算函数"""
    time.sleep(0.1)  # 模拟复杂计算
    return n ** 2

# 第一次调用会测量时间
result1 = complex_calculation(10)
# 第二次调用会使用缓存，几乎没有延迟
result2 = complex_calculation(10)
```

## 6. 装饰器设计模式

### 6.1 注册模式

装饰器可以用来实现注册模式，常用于插件系统或命令分发：

```python
# 简单的命令分发系统
commands = {}

def register_command(name):
    """注册一个命令处理函数"""
    def decorator(func):
        commands[name] = func
        return func
    return decorator

@register_command("hello")
def hello_command(args):
    return f"Hello, {args[0] if args else 'World'}!"

@register_command("add")
def add_command(args):
    return sum(int(x) for x in args)

# 命令分发器
def dispatch_command(command_line):
    tokens = command_line.split()
    if not tokens:
        return "请输入命令"
    
    command = tokens[0]
    args = tokens[1:]
    
    if command in commands:
        return commands[command](args)
    else:
        return f"未知命令: {command}"

# 测试
print(dispatch_command("hello"))  # 输出: Hello, World!
print(dispatch_command("hello 张三"))  # 输出: Hello, 张三!
print(dispatch_command("add 1 2 3 4"))  # 输出: 10
print(dispatch_command("unknown"))  # 输出: 未知命令: unknown
```

### 6.2 上下文提供者模式

```python
class ContextProvider:
    """为函数执行提供上下文环境的装饰器类"""
    def __init__(self, **context):
        self.context = context
        
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 合并上下文和传入的关键字参数
            kwargs.update(self.context)
            return func(*args, **kwargs)
        return wrapper

# 使用示例
@ContextProvider(database="users_db", logger=print)
def process_user(user_id, database=None, logger=None):
    logger(f"正在处理用户 {user_id}")
    # 使用数据库做一些操作
    logger(f"使用 {database} 数据库")
    return f"用户 {user_id} 处理完成"

print(process_user(123))
```

## 7. 实际项目中的装饰器应用

### 7.1 Web框架中的路由装饰器

Flask和其他Web框架广泛使用装饰器进行URL路由：

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "首页"

@app.route("/user/<username>")
def show_user_profile(username):
    return f"用户: {username}"

# 如果此脚本作为主程序运行
if __name__ == "__main__":
    app.run(debug=True)
```

### 7.2 权限控制装饰器

```python
def require_permission(permission):
    """检查用户是否有特定权限的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if permission not in user.permissions:
                raise PermissionError(f"用户 {user.username} 没有 {permission} 权限")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

# 模拟用户类
class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

# 使用装饰器控制权限
@require_permission("admin")
def delete_user(current_user, user_id):
    print(f"{current_user.username} 删除了用户 {user_id}")
    return True

# 测试
admin = User("admin", ["admin", "edit", "view"])
normal_user = User("user1", ["edit", "view"])

delete_user(admin, 123)  # 正常执行
try:
    delete_user(normal_user, 123)  # 引发 PermissionError
except PermissionError as e:
    print(e)
```

### 7.3 API速率限制装饰器

```python
import time
from collections import defaultdict
from functools import wraps

class RateLimiter:
    """API速率限制装饰器"""
    def __init__(self, max_calls=15, period=60):
        self.max_calls = max_calls
        self.period = period
        self.call_history = defaultdict(list)
        
    def __call__(self, func):
        @wraps(func)
        def wrapper(user_id, *args, **kwargs):
            # 清理过期的调用记录
            now = time.time()
            self.call_history[user_id] = [
                timestamp for timestamp in self.call_history[user_id]
                if now - timestamp < self.period
            ]
            
            # 检查是否超过速率限制
            if len(self.call_history[user_id]) >= self.max_calls:
                raise Exception(f"API速率限制: 用户 {user_id} 在 {self.period} 秒内超过了 {self.max_calls} 次调用限制")
                
            # 记录本次调用
            self.call_history[user_id].append(now)
            
            return func(user_id, *args, **kwargs)
        return wrapper

# 使用示例
@RateLimiter(max_calls=3, period=10)
def api_endpoint(user_id, query):
    return f"API响应: 用户={user_id}, 查询={query}"

# 测试
try:
    for i in range(5):
        print(f"调用 {i+1}: {api_endpoint(42, 'test')}")
        time.sleep(2)
except Exception as e:
    print(e)
```

## 8. 装饰器的最佳实践

1. **保持简单**: 装饰器应该遵循单一职责原则，专注于一种功能
2. **使用`functools.wraps`**: 总是使用`wraps`保留被装饰函数的元数据
3. **提供文档**: 为装饰器提供清晰的文档字符串，解释其功能和用法
4. **错误处理**: 妥善处理装饰器中可能出现的异常
5. **避免副作用**: 装饰器不应该对外部状态产生意外的副作用
6. **组合优于继承**: 通过组合多个装饰器而不是复杂的继承来实现功能
7. **性能考虑**: 记住装饰器会在每次函数调用时执行，所以保持高效

## 9. 练习题

### 基础练习
1. 创建一个装饰器，记录函数的调用次数和参数
2. 编写一个装饰器，打印函数的输入参数和返回值

### 进阶练习
1. 实现一个缓存装饰器，能够缓存任意函数的结果，并设置过期时间
2. 创建一个装饰器，用于限制函数执行时间，超时则抛出异常

### 高级挑战
实现一个完整的装饰器库，包含以下功能：
- 重试机制
- 速率限制
- 超时控制
- 参数验证
- 结果缓存
- 异步支持

## 10. 解决方案示例

### 基础练习解答

```python
# 1. 记录函数调用次数和参数
def log_calls(func):
    calls = []
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        calls.append({"args": args, "kwargs": kwargs})
        print(f"函数 {func.__name__} 已被调用 {len(calls)} 次")
        print(f"最新调用参数: args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    
    # 添加一个属性来访问调用历史
    wrapper.calls = calls
    return wrapper

@log_calls
def greet(name, greeting="你好"):
    return f"{greeting}, {name}!"

print(greet("张三"))
print(greet("李四", greeting="您好"))
print(f"调用历史: {greet.calls}")

# 2. 打印函数的输入和输出
def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"调用: {func.__name__}(args={args}, kwargs={kwargs})")
        result = func(*args, **kwargs)
        print(f"返回: {result}")
        return result
    return wrapper

@trace
def add(a, b):
    return a + b

add(3, 4)
```
