#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
functools模块示例代码集合

本文件演示了Python functools模块中的各种函数式编程工具，
包括lru_cache、partial、reduce、total_ordering等。

作者: Python数据结构教程
日期: 2023-11-28
"""

import functools
import time
from pprint import pprint
import random


def example_lru_cache():
    """示例1: lru_cache - 缓存装饰器"""
    print("=== 示例1: lru_cache - 缓存装饰器 ===")
    
    # 基本用法
    print("基本用法:")
    
    @functools.lru_cache(maxsize=128)
    def fibonacci(n):
        """计算斐波那契数列的第n个数"""
        print(f"计算fibonacci({n})")
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    # 第一次调用，会计算所有子问题
    print("第一次调用fibonacci(6):")
    result = fibonacci(6)
    print(f"结果: {result}")
    print(f"缓存信息: {fibonacci.cache_info()}")
    
    # 第二次调用，直接从缓存获取
    print("\n第二次调用fibonacci(6):")
    result = fibonacci(6)
    print(f"结果: {result}")
    print(f"缓存信息: {fibonacci.cache_info()}")
    
    # 测试不同的maxsize
    print("\n测试不同的maxsize:")
    
    @functools.lru_cache(maxsize=3)
    def cached_function(x):
        print(f"执行cached_function({x})")
        return x * 2
    
    # 依次调用不同的参数
    for i in range(5):
        cached_function(i)
        print(f"调用{i}后缓存: {cached_function.cache_info()}")
    
    # 再次调用，观察缓存情况
    print("\n再次调用:")
    cached_function(0)  # 应该已被缓存淘汰
    print(f"缓存信息: {cached_function.cache_info()}")
    
    # 清除缓存
    print("\n清除缓存:")
    cached_function.cache_clear()
    print(f"清除后缓存: {cached_function.cache_info()}")
    
    # 实际应用：模拟耗时操作
    print("\n实际应用：模拟耗时操作")
    
    def simulate_expensive_operation(param1, param2):
        """模拟一个耗时的操作"""
        print(f"执行耗时操作: {param1}, {param2}")
        time.sleep(0.2)  # 模拟耗时
        return param1 + param2
    
    # 使用缓存版本
    cached_operation = functools.lru_cache(maxsize=None)(simulate_expensive_operation)
    
    # 测试性能
    print("\n测试性能:")
    
    # 第一次调用（无缓存）
    start = time.time()
    result1 = cached_operation(10, 20)
    time1 = time.time() - start
    print(f"第一次调用结果: {result1}, 耗时: {time1:.6f}秒")
    
    # 第二次调用（有缓存）
    start = time.time()
    result2 = cached_operation(10, 20)
    time2 = time.time() - start
    print(f"第二次调用结果: {result2}, 耗时: {time2:.6f}秒")
    
    print(f"加速比: {time1 / time2:.2f}倍")
    print()


def example_partial():
    """示例2: partial - 部分函数应用"""
    print("=== 示例2: partial - 部分函数应用 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 定义一个多参数函数
    def power(base, exponent):
        return base ** exponent
    
    # 创建部分应用函数
    square = functools.partial(power, exponent=2)  # 固定指数为2
    cube = functools.partial(power, exponent=3)    # 固定指数为3
    
    print(f"square(5) = {square(5)}")  # 5^2 = 25
    print(f"cube(5) = {cube(5)}")      # 5^3 = 125
    
    # 也可以固定第一个参数
    power_of_2 = functools.partial(power, 2)  # 固定底数为2
    print(f"power_of_2(10) = {power_of_2(10)}")  # 2^10 = 1024
    
    # 与map、filter等结合使用
    print("\n与map、filter等结合使用:")
    numbers = [1, 2, 3, 4, 5]
    
    # 计算所有数字的平方
    squares = list(map(square, numbers))
    print(f"原列表: {numbers}")
    print(f"平方结果: {squares}")
    
    # 计算所有数字的立方
    cubes = list(map(cube, numbers))
    print(f"立方结果: {cubes}")
    
    # 使用在字符串处理中
    print("\n字符串处理示例:")
    
    # 定义一个格式化函数
    def format_greeting(greeting, name, punctuation):
        return f"{greeting}, {name}{punctuation}"
    
    # 创建特定的问候语函数
    say_hello = functools.partial(format_greeting, "Hello")
    say_hi = functools.partial(format_greeting, "Hi")
    
    # 进一步特化
    say_hello_excited = functools.partial(say_hello, punctuation="!")
    say_hi_polite = functools.partial(say_hi, punctuation=".")
    
    print(f"say_hello('World', '!') = {say_hello('World', '!')}")
    print(f"say_hello_excited('Python') = {say_hello_excited('Python')}")
    print(f"say_hi_polite('User') = {say_hi_polite('User')}")
    
    # 实际应用：配置函数
    print("\n实际应用：配置函数")
    
    def log_message(level, message):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level.upper()}] {message}")
    
    # 创建不同级别的日志函数
    log_info = functools.partial(log_message, "INFO")
    log_error = functools.partial(log_message, "ERROR")
    log_debug = functools.partial(log_message, "DEBUG")
    
    # 使用这些日志函数
    log_info("应用程序启动")
    log_debug("初始化变量")
    log_error("发生错误")
    print()


def example_reduce():
    """示例3: reduce - 归约函数"""
    print("=== 示例3: reduce - 归约函数 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 计算列表所有元素的和
    numbers = [1, 2, 3, 4, 5]
    sum_result = functools.reduce(lambda x, y: x + y, numbers)
    print(f"列表: {numbers}")
    print(f"求和结果: {sum_result}")
    print(f"验证: {sum(numbers)}")
    
    # 计算列表所有元素的积
    product_result = functools.reduce(lambda x, y: x * y, numbers)
    print(f"求积结果: {product_result}")
    
    # 指定初始值
    print("\n指定初始值:")
    sum_with_initial = functools.reduce(lambda x, y: x + y, numbers, 100)
    print(f"初始值为100的求和: {sum_with_initial}")
    
    # 处理空列表（必须提供初始值）
    try:
        functools.reduce(lambda x, y: x + y, [])
    except TypeError as e:
        print(f"错误: {e}")
    
    # 提供初始值可以安全处理空列表
    result = functools.reduce(lambda x, y: x + y, [], 0)
    print(f"空列表求和 (有初始值): {result}")
    
    # 复杂操作示例
    print("\n复杂操作示例:")
    
    # 找出最大值
    max_result = functools.reduce(lambda x, y: x if x > y else y, numbers)
    print(f"最大值: {max_result}")
    print(f"验证: {max(numbers)}")
    
    # 连接字符串
    words = ["Hello", "World", "from", "Python"]
    sentence = functools.reduce(lambda x, y: x + " " + y, words)
    print(f"连接字符串: '{sentence}'")
    
    # 实际应用：数据处理
    print("\n实际应用：数据处理")
    
    # 模拟销售数据
    sales_data = [
        {"product": "A", "quantity": 10, "price": 5.0},
        {"product": "B", "quantity": 5, "price": 10.0},
        {"product": "A", "quantity": 3, "price": 5.0},
        {"product": "C", "quantity": 2, "price": 20.0}
    ]
    
    # 计算总销售额
    total_sales = functools.reduce(
        lambda total, item: total + (item["quantity"] * item["price"]),
        sales_data,
        0
    )
    
    print(f"销售数据: {sales_data}")
    print(f"总销售额: ${total_sales:.2f}")
    
    # 按产品分组并计算销售额
    product_sales = functools.reduce(
        lambda result, item: {
            **result,
            item["product"]: result.get(item["product"], 0) + (item["quantity"] * item["price"])
        },
        sales_data,
        {}
    )
    
    print(f"按产品销售额: {product_sales}")
    print()


def example_total_ordering():
    """示例4: total_ordering - 类比较方法装饰器"""
    print("=== 示例4: total_ordering - 类比较方法装饰器 ===")
    
    # 基本用法
    print("基本用法:")
    
    @functools.total_ordering
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person({self.name}, {self.age})"
        
        # 只需要实现 __eq__ 和一个其他比较方法
        def __eq__(self, other):
            if not isinstance(other, Person):
                return NotImplemented
            return self.age == other.age
        
        def __lt__(self, other):
            if not isinstance(other, Person):
                return NotImplemented
            return self.age < other.age
        
        # total_ordering会自动生成 __le__, __gt__, __ge__
    
    # 创建实例
    alice = Person("Alice", 25)
    bob = Person("Bob", 30)
    charlie = Person("Charlie", 25)
    
    print(f"alice: {alice}")
    print(f"bob: {bob}")
    print(f"charlie: {charlie}")
    
    # 测试比较操作
    print("\n比较操作测试:")
    print(f"alice == charlie: {alice == charlie}")  # True
    print(f"alice != bob: {alice != bob}")        # True
    print(f"alice < bob: {alice < bob}")          # True
    print(f"alice <= bob: {alice <= bob}")        # True
    print(f"bob > alice: {bob > alice}")          # True
    print(f"bob >= alice: {bob >= alice}")        # True
    print(f"alice <= charlie: {alice <= charlie}")  # True
    
    # 在排序中的应用
    print("\n排序应用:")
    people = [bob, alice, charlie]
    sorted_people = sorted(people)
    print(f"排序前: {people}")
    print(f"排序后: {sorted_people}")
    
    # 自定义数据类型
    print("\n自定义数据类型:")
    
    @functools.total_ordering
    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
        
        def __repr__(self):
            return f"Book('{self.title}', '{self.author}', {self.year})"
        
        def __eq__(self, other):
            if not isinstance(other, Book):
                return NotImplemented
            return (
                self.title == other.title and
                self.author == other.author and
                self.year == other.year
            )
        
        def __lt__(self, other):
            if not isinstance(other, Book):
                return NotImplemented
            # 先按年份排序，再按作者，最后按标题
            if self.year != other.year:
                return self.year < other.year
            if self.author != other.author:
                return self.author < other.author
            return self.title < other.title
    
    books = [
        Book("Python Cookbook", "David Beazley", 2013),
        Book("Fluent Python", "Luciano Ramalho", 2015),
        Book("Effective Python", "Brett Slatkin", 2015),
        Book("Python for Data Analysis", "Wes McKinney", 2012)
    ]
    
    sorted_books = sorted(books)
    print("排序后的书籍:")
    for book in sorted_books:
        print(f"  {book}")
    print()


def example_wraps():
    """示例5: wraps - 装饰器元数据保留"""
    print("=== 示例5: wraps - 装饰器元数据保留 ===")
    
    # 不使用wraps的装饰器
    print("不使用wraps的装饰器:")
    
    def simple_decorator(func):
        def wrapper(*args, **kwargs):
            """包装函数的文档字符串"""
            print(f"调用函数: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    # 使用wraps的装饰器
    def better_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """包装函数的文档字符串"""
            print(f"调用函数: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    # 定义测试函数
    @simple_decorator
    def function1(x):
        """函数1的文档字符串"""
        return x * 2
    
    @better_decorator
    def function2(x):
        """函数2的文档字符串"""
        return x * 2
    
    # 比较结果
    print("\n函数1 (不使用wraps):")
    print(f"  名称: {function1.__name__}")
    print(f"  文档: {function1.__doc__}")
    print(f"  模块: {function1.__module__}")
    
    print("\n函数2 (使用wraps):")
    print(f"  名称: {function2.__name__}")
    print(f"  文档: {function2.__doc__}")
    print(f"  模块: {function2.__module__}")
    
    # 调用测试
    print("\n调用测试:")
    print(f"function1(5) = {function1(5)}")
    print(f"function2(5) = {function2(5)}")
    
    # 实际应用：计时装饰器
    print("\n实际应用：计时装饰器")
    
    def timer_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{func.__name__} 执行耗时: {end_time - start_time:.6f}秒")
            return result
        return wrapper
    
    @timer_decorator
    def slow_function(n):
        """一个慢速函数，用于测试计时装饰器"""
        total = 0
        for i in range(n):
            total += i
        return total
    
    print(f"\n函数文档: {slow_function.__doc__}")
    result = slow_function(1000000)
    print(f"结果: {result}")
    print()


def example_cmp_to_key():
    """示例6: cmp_to_key - 将比较函数转换为排序键函数"""
    print("=== 示例6: cmp_to_key - 比较函数转换 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 自定义比较函数
    def compare_by_length(a, b):
        """按字符串长度比较"""
        if len(a) < len(b):
            return -1
        elif len(a) > len(b):
            return 1
        else:
            return 0
    
    # 测试列表
    words = ["apple", "banana", "kiwi", "strawberry", "fig"]
    print(f"原始列表: {words}")
    
    # 使用cmp_to_key排序
    sorted_by_length = sorted(words, key=functools.cmp_to_key(compare_by_length))
    print(f"按长度排序: {sorted_by_length}")
    
    # 逆序排序
    reverse_sorted = sorted(words, key=functools.cmp_to_key(compare_by_length), reverse=True)
    print(f"按长度逆序排序: {reverse_sorted}")
    
    # 复杂排序示例
    print("\n复杂排序示例:")
    
    # 人员数据
    people = [
        {"name": "Alice", "age": 25, "salary": 80000},
        {"name": "Bob", "age": 30, "salary": 75000},
        {"name": "Charlie", "age": 25, "salary": 90000},
        {"name": "David", "age": 35, "salary": 85000}
    ]
    
    # 自定义比较函数：先按年龄，再按薪资降序
    def compare_people(a, b):
        if a["age"] != b["age"]:
            return a["age"] - b["age"]  # 年龄升序
        else:
            return b["salary"] - a["salary"]  # 薪资降序
    
    sorted_people = sorted(people, key=functools.cmp_to_key(compare_people))
    print("按年龄升序，同年龄按薪资降序排序:")
    for person in sorted_people:
        print(f"  {person}")
    
    # 实际应用：自定义排序规则
    print("\n实际应用：自定义排序规则")
    
    # 文件名排序（自然排序）
    filenames = ["file1.txt", "file10.txt", "file2.txt", "file100.txt"]
    print(f"原始文件名: {filenames}")
    print(f"默认排序: {sorted(filenames)}")
    
    # 自然排序的比较函数
    def natural_sort_cmp(a, b):
        import re
        # 分割数字和非数字部分
        def split_filename(filename):
            return [int(text) if text.isdigit() else text.lower() 
                    for text in re.split(r'(\d+)', filename)]
        
        parts_a = split_filename(a)
        parts_b = split_filename(b)
        
        # 逐项比较
        for i in range(min(len(parts_a), len(parts_b))):
            if parts_a[i] != parts_b[i]:
                if isinstance(parts_a[i], int) and isinstance(parts_b[i], int):
                    return parts_a[i] - parts_b[i]
                else:
                    return -1 if parts_a[i] < parts_b[i] else 1
        
        # 如果前面的部分都相同，则较短的排在前面
        return len(parts_a) - len(parts_b)
    
    natural_sorted = sorted(filenames, key=functools.cmp_to_key(natural_sort_cmp))
    print(f"自然排序: {natural_sorted}")
    print()


def example_singledispatch():
    """示例7: singledispatch - 单分派泛函数"""
    print("=== 示例7: singledispatch - 单分派泛函数 ===")
    
    # 基本用法
    print("基本用法:")
    
    @functools.singledispatch
    def process_data(data):
        """处理数据的通用函数"""
        raise NotImplementedError(f"不支持的数据类型: {type(data).__name__}")
    
    # 为不同类型注册专门的处理函数
    @process_data.register(str)
    def _(data):
        """处理字符串类型"""
        print(f"处理字符串: '{data}' (长度: {len(data)})")
        return data.upper()
    
    @process_data.register(int)
    def _(data):
        """处理整数类型"""
        print(f"处理整数: {data}")
        return data * 2
    
    @process_data.register(list)
    def _(data):
        """处理列表类型"""
        print(f"处理列表: {data} (元素数: {len(data)})")
        return [x * 2 for x in data]
    
    @process_data.register(dict)
    def _(data):
        """处理字典类型"""
        print(f"处理字典: {data} (键值对: {len(data)})")
        return {k.upper(): v for k, v in data.items()}
    
    # 支持多种类型
    @process_data.register(float)
    @process_data.register(complex)
    def _(data):
        """处理浮点数和复数类型"""
        print(f"处理数值: {data} (类型: {type(data).__name__})")
        return data * 2
    
    # 测试不同类型
    print("\n测试不同数据类型:")
    
    result1 = process_data("hello")
    print(f"结果: {result1}")
    
    result2 = process_data(42)
    print(f"结果: {result2}")
    
    result3 = process_data([1, 2, 3])
    print(f"结果: {result3}")
    
    result4 = process_data({"a": 1, "b": 2})
    print(f"结果: {result4}")
    
    result5 = process_data(3.14)
    print(f"结果: {result5}")
    
    # 不支持的类型
    try:
        process_data(set([1, 2, 3]))
    except NotImplementedError as e:
        print(f"错误: {e}")
    
    # 获取函数的文档
    print("\n函数文档:")
    print(process_data.__doc__)
    
    # 实际应用：JSON序列化器
    print("\n实际应用：JSON序列化器")
    
    @functools.singledispatch
    def to_json(data):
        """将Python对象转换为JSON兼容格式"""
        raise TypeError(f"无法序列化类型: {type(data).__name__}")
    
    @to_json.register(str)
    @to_json.register(int)
    @to_json.register(float)
    @to_json.register(bool)
    @to_json.register(type(None))
    def _(data):
        """基本类型直接返回"""
        return data
    
    @to_json.register(list)
    @to_json.register(tuple)
    def _(data):
        """处理列表和元组"""
        return [to_json(item) for item in data]
    
    @to_json.register(dict)
    def _(data):
        """处理字典"""
        return {str(key): to_json(value) for key, value in data.items()}
    
    # 自定义类型
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    @to_json.register(Person)
    def _(data):
        """处理Person对象"""
        return {"name": data.name, "age": data.age, "type": "Person"}
    
    # 测试序列化
    test_data = {
        "name": "JSON测试",
        "numbers": [1, 2, 3.14],
        "person": Person("Alice", 25),
        "nested": {
            "active": True,
            "tags": ("test", "demo")
        }
    }
    
    import json
    json_result = json.dumps(to_json(test_data), ensure_ascii=False, indent=2)
    print("序列化结果:")
    print(json_result)
    print()


def example_lru_cache_advanced():
    """示例8: lru_cache高级用法"""
    print("=== 示例8: lru_cache高级用法 ===")
    
    # 使用typed参数
    print("使用typed参数:")
    
    @functools.lru_cache(maxsize=128, typed=True)
    def func_with_types(x, y):
        print(f"执行func_with_types({x}, {y})")
        return x + y
    
    # 相同值但不同类型会被视为不同的调用
    print("相同值不同类型:")
    func_with_types(1, 2)    # 整数
    func_with_types(1.0, 2)  # 浮点数和整数
    print(f"缓存信息: {func_with_types.cache_info()}")  # 应该有2次命中
    
    # 再次调用相同类型
    print("\n再次调用:")
    func_with_types(1, 2)    # 应该命中缓存
    func_with_types(1.0, 2)  # 应该命中缓存
    print(f"缓存信息: {func_with_types.cache_info()}")
    
    # 缓存不可哈希的参数
    print("\n处理不可哈希的参数:")
    
    def memoize_unhashable(func):
        """为接受不可哈希参数的函数提供缓存"""
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args):
            # 将不可哈希的参数转换为可哈希的表示
            key_parts = []
            for arg in args:
                try:
                    # 尝试直接使用参数作为键的一部分
                    hash(arg)
                    key_parts.append(arg)
                except TypeError:
                    # 对于不可哈希的类型，使用其字符串表示
                    if isinstance(arg, (list, tuple)):
                        key_parts.append(tuple(wrapper(*([x] if not isinstance(x, (list, tuple, dict, set)) else [x])[0]) for x in arg))
                    elif isinstance(arg, dict):
                        key_parts.append(tuple(sorted((k, wrapper(*([v] if not isinstance(v, (list, tuple, dict, set)) else [v])[0])) for k, v in arg.items())))
                    elif isinstance(arg, set):
                        key_parts.append(tuple(sorted(wrapper(*([x] if not isinstance(x, (list, tuple, dict, set)) else [x])[0]) for x in arg)))
                    else:
                        key_parts.append(repr(arg))
            
            key = tuple(key_parts)
            
            if key not in cache:
                cache[key] = func(*args)
            return cache[key]
        
        def clear_cache():
            cache.clear()
        
        wrapper.clear_cache = clear_cache
        return wrapper
    
    @memoize_unhashable
    def process_list(data):
        """处理列表的函数"""
        print(f"处理列表: {data}")
        return sum(data)
    
    # 测试
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]  # 内容相同但不同的列表对象
    
    print(f"首次调用process_list({list1}):")
    result1 = process_list(list1)
    print(f"结果: {result1}")
    
    print(f"\n调用相同内容的不同列表process_list({list2}):")
    result2 = process_list(list2)  # 应该使用缓存
    print(f"结果: {result2}")
    print()


def example_function_composition():
    """示例9: 函数组合"""
    print("=== 示例9: 函数组合 ===")
    
    # 基本的函数组合
    print("基本的函数组合:")
    
    def compose(f, g):
        """组合两个函数: (f ∘ g)(x) = f(g(x))"""
        @functools.wraps(g)
        def wrapper(*args, **kwargs):
            return f(g(*args, **kwargs))
        return wrapper
    
    # 测试函数
    def double(x):
        """将输入值翻倍"""
        return x * 2
    
    def increment(x):
        """将输入值加1"""
        return x + 1
    
    # 创建组合函数
    double_then_increment = compose(increment, double)  # 先翻倍再加1
    increment_then_double = compose(double, increment)  # 先加1再翻倍
    
    # 测试
    x = 5
    print(f"x = {x}")
    print(f"先翻倍再加1: {double_then_increment(x)}")  # 应该是 5*2+1 = 11
    print(f"先加1再翻倍: {increment_then_double(x)}")  # 应该是 (5+1)*2 = 12
    
    # 多函数组合
    print("\n多函数组合:")
    
    def compose_multiple(*functions):
        """组合多个函数"""
        def compose_two(f, g):
            @functools.wraps(g)
            def wrapper(*args, **kwargs):
                return f(g(*args, **kwargs))
            return wrapper
        
        # 从右到左组合函数
        return functools.reduce(compose_two, functions)
    
    # 测试函数
    def square(x):
        return x ** 2
    
    def add_ten(x):
        return x + 10
    
    # 创建多函数组合
    pipeline = compose_multiple(add_ten, square, double, increment)
    # 相当于 add_ten(square(double(increment(x))))
    
    result = pipeline(3)
    print(f"组合函数 pipeline(3): {result}")  # (3+1)*2^2+10 = 4*4+10 = 26
    
    # 验证
    manual_result = add_ten(square(double(increment(3))))
    print(f"手动计算结果: {manual_result}")
    print(f"结果一致: {result == manual_result}")
    
    # 实际应用：数据处理管道
    print("\n实际应用：数据处理管道")
    
    # 定义一系列数据处理函数
    def clean_text(text):
        """清理文本"""
        print("清理文本")
        return text.lower().strip().replace("!", "").replace(",", "")
    
    def tokenize(text):
        """分词"""
        print("分词处理")
        return text.split()
    
    def remove_stopwords(words):
        """移除停用词"""
        stopwords = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for"}
        print("移除停用词")
        return [word for word in words if word not in stopwords]
    
    def count_words(words):
        """计数"""
        from collections import Counter
        print("词频统计")
        return dict(Counter(words))
    
    # 创建数据处理管道
    text_processor = compose_multiple(
        count_words,
        remove_stopwords,
        tokenize,
        clean_text
    )
    
    # 测试
    text = "The quick brown fox jumps over the lazy dog! It was a sunny day."
    print(f"原始文本: '{text}'")
    word_counts = text_processor(text)
    print(f"处理结果: {word_counts}")
    print()


def example_practical_scenarios():
    """示例10: 实际应用场景"""
    print("=== 示例10: 实际应用场景 ===")
    
    # 1. 记忆化搜索（递归优化）
    print("1. 记忆化搜索（递归优化）:")
    
    @functools.lru_cache(maxsize=None)
    def longest_common_subsequence(text1, text2):
        """计算最长公共子序列的长度"""
        if not text1 or not text2:
            return 0
        if text1[0] == text2[0]:
            return 1 + longest_common_subsequence(text1[1:], text2[1:])
        else:
            return max(
                longest_common_subsequence(text1[1:], text2),
                longest_common_subsequence(text1, text2[1:])
            )
    
    # 测试
    s1 = "abcde"
    s2 = "ace"
    print(f"字符串1: '{s1}'")
    print(f"字符串2: '{s2}'")
    print(f"最长公共子序列长度: {longest_common_subsequence(s1, s2)}")
    print(f"缓存信息: {longest_common_subsequence.cache_info()}")
    
    # 2. 配置化的API客户端
    print("\n2. 配置化的API客户端:")
    
    class APIClient:
        def __init__(self, base_url, api_key):
            self.base_url = base_url
            self.api_key = api_key
        
        def _make_request(self, endpoint, method="GET", **kwargs):
            """发送API请求的内部方法"""
            print(f"发送{method}请求到 {self.base_url}/{endpoint}")
            print(f"参数: {kwargs}")
            print(f"使用API密钥: {self.api_key[:4]}...")
            # 实际项目中这里会使用requests库发送请求
            return {"success": True, "data": kwargs}
        
        # 创建特定端点的方法
        def get_users(self, **params):
            return self._make_request("users", "GET", **params)
        
        def get_posts(self, **params):
            return self._make_request("posts", "GET", **params)
    
    # 使用partial创建预配置的客户端
    create_client = functools.partial(APIClient, "https://api.example.com")
    
    # 创建不同的客户端实例
    client1 = create_client("api_key_1")
    client2 = create_client("api_key_2")
    
    # 使用客户端
    print("\n客户端1请求:")
    client1.get_users(page=1, limit=10)
    
    print("\n客户端2请求:")
    client2.get_posts(category="tech")
    
    # 3. 装饰器链
    print("\n3. 装饰器链:")
    
    def log_entry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] 进入函数: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    def log_exit(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"[LOG] 退出函数: {func.__name__}")
            return result
        return wrapper
    
    def validate_positive(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (int, float)) and arg < 0:
                    raise ValueError("参数必须为正数")
            for value in kwargs.values():
                if isinstance(value, (int, float)) and value < 0:
                    raise ValueError("参数必须为正数")
            return func(*args, **kwargs)
        return wrapper
    
    # 应用多个装饰器
    @log_entry
    @log_exit
    @validate_positive
    def calculate_area(radius):
        """计算圆的面积"""
        import math
        return math.pi * radius ** 2
    
    # 测试
    print("\n调用calculate_area(5):")
    try:
        area = calculate_area(5)
        print(f"面积: {area:.2f}")
    except ValueError as e:
        print(f"错误: {e}")
    
    print("\n调用calculate_area(-1):")
    try:
        area = calculate_area(-1)
        print(f"面积: {area:.2f}")
    except ValueError as e:
        print(f"错误: {e}")
    
    # 4. 延迟计算和惰性求值
    print("\n4. 延迟计算和惰性求值:")
    
    class LazyProperty:
        def __init__(self, func):
            self.func = func
            functools.update_wrapper(self, func)
        
        def __get__(self, instance, owner):
            if instance is None:
                return self
            # 计算一次后缓存结果
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
    
    class ExpensiveObject:
        def __init__(self):
            self.counter = 0
        
        @LazyProperty
        def expensive_calculation(self):
            """一个耗时的计算"""
            self.counter += 1
            print(f"执行耗时计算... (第{self.counter}次)")
            time.sleep(0.1)  # 模拟耗时
            return sum(i * i for i in range(10000))
    
    # 测试
    obj = ExpensiveObject()
    print("首次访问:")
    result1 = obj.expensive_calculation
    print(f"结果: {result1}")
    
    print("\n再次访问:")
    result2 = obj.expensive_calculation  # 应该使用缓存
    print(f"结果: {result2}")
    
    print(f"计算次数: {obj.counter}")
    print()


if __name__ == "__main__":
    print("Python functools 模块示例代码\n")
    
    # 运行所有示例
    example_lru_cache()
    example_partial()
    example_reduce()
    example_total_ordering()
    example_wraps()
    example_cmp_to_key()
    example_singledispatch()
    example_lru_cache_advanced()
    example_function_composition()
    example_practical_scenarios()
    
    print("所有示例执行完成！")
