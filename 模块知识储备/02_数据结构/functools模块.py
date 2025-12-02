# Python functools模块详解

# 1. functools模块概述
print("=== 1. functools模块概述 ===")
print("functools模块提供了高阶函数相关的工具，主要用于处理或扩展函数对象。")
print("该模块特别关注于函数式编程风格的支持，提供了各种用于函数操作的装饰器和实用函数。")
print("functools模块的核心功能包括：函数缓存、函数装饰器、部分应用、减少可调用对象等。")
print("该模块在需要优化、扩展或修改函数行为时特别有用。")
print()

# 2. functools模块核心函数
print("=== 2. functools模块核心函数 ===")

def functools_core_functions():
    """展示functools模块中的核心函数"""
    import functools
    import time
    
    print("1. functools.cache(user_function=None, /):")
    print("   为函数提供简单的内存缓存，缓存无参数函数或参数可哈希的函数调用结果")
    print("   这是在Python 3.9中新增的装饰器，相当于lru_cache(maxsize=None)")
    
    @functools.cache
    def fibonacci(n):
        """计算斐波那契数列（使用缓存优化）"""
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("   示例: 计算斐波那契数列的第30项")
    start_time = time.time()
    result = fibonacci(30)
    first_time = time.time() - start_time
    print(f"   第一次计算结果: {result}")
    print(f"   第一次计算耗时: {first_time:.6f} 秒")
    
    # 再次调用，应该从缓存中获取
    start_time = time.time()
    result = fibonacci(30)
    second_time = time.time() - start_time
    print(f"   第二次计算结果: {result}")
    print(f"   第二次计算耗时: {second_time:.6f} 秒")
    print(f"   缓存提升: {first_time / second_time:.2f} 倍")
    
    print("\n2. functools.lru_cache(maxsize=128, typed=False):")
    print("   实现最近最少使用（LRU）缓存，限制缓存大小以避免内存过度使用")
    print("   maxsize参数控制缓存的最大条目数，typed参数控制是否区分不同类型的相同值")
    
    @functools.lru_cache(maxsize=10)
    def expensive_calculation(x, y):
        """模拟耗时计算"""
        time.sleep(0.1)  # 模拟耗时操作
        return x * y
    
    print("   示例: 使用LRU缓存进行耗时计算")
    # 第一次调用，会执行计算
    start_time = time.time()
    result1 = expensive_calculation(10, 20)
    first_time = time.time() - start_time
    print(f"   第一次计算结果: {result1}")
    print(f"   第一次计算耗时: {first_time:.6f} 秒")
    
    # 第二次调用相同参数，从缓存获取
    start_time = time.time()
    result2 = expensive_calculation(10, 20)
    second_time = time.time() - start_time
    print(f"   第二次计算结果: {result2}")
    print(f"   第二次计算耗时: {second_time:.6f} 秒")
    
    # 测试typed参数
    print("   \n测试typed参数:")
    print("   默认情况下，lru_cache不区分不同类型的相同值:")
    
    @functools.lru_cache()
    def same_value_diff_types(x):
        return f"值: {x}, 类型: {type(x).__name__}"
    
    print(f"   same_value_diff_types(5): {same_value_diff_types(5)}")
    print(f"   same_value_diff_types(5.0): {same_value_diff_types(5.0)}")
    print(f"   缓存统计: {same_value_diff_types.cache_info()}")
    
    # 使用typed=True
    @functools.lru_cache(typed=True)
    def typed_function(x):
        return f"值: {x}, 类型: {type(x).__name__}"
    
    print(f"   \n使用typed=True:")
    print(f"   typed_function(5): {typed_function(5)}")
    print(f"   typed_function(5.0): {typed_function(5.0)}")
    print(f"   缓存统计: {typed_function.cache_info()}")
    
    print("\n3. functools.reduce(function, iterable[, initializer]):")
    print("   将一个二元函数连续应用于iterable的元素，从左到右，累积结果")
    print("   如果提供了initializer，则作为第一个参数，iterable的元素作为后续参数")
    
    # 基本用法：计算列表元素的总和
    numbers = [1, 2, 3, 4, 5]
    sum_result = functools.reduce(lambda x, y: x + y, numbers)
    print(f"   示例1: 计算列表元素的总和 {numbers}")
    print(f"   结果: {sum_result}")
    
    # 使用initializer
    sum_with_initializer = functools.reduce(lambda x, y: x + y, numbers, 10)
    print(f"   示例2: 计算列表元素的总和，初始值为10")
    print(f"   结果: {sum_with_initializer}")
    
    # 计算列表元素的乘积
    product_result = functools.reduce(lambda x, y: x * y, numbers)
    print(f"   示例3: 计算列表元素的乘积")
    print(f"   结果: {product_result}")
    
    # 查找列表中的最大值
    max_result = functools.reduce(lambda x, y: x if x > y else y, numbers)
    print(f"   示例4: 查找列表中的最大值")
    print(f"   结果: {max_result}")
    
    print("\n4. functools.partial(func, /, *args, **keywords):")
    print("   创建一个新的函数，该函数是func的部分应用版本")
    print("   预设了部分参数，调用新函数时只需提供剩余的参数")
    
    # 基本用法：预设乘法函数的一个参数
    multiply = lambda x, y: x * y
    double = functools.partial(multiply, 2)  # 预设第一个参数为2
    triple = functools.partial(multiply, 3)  # 预设第一个参数为3
    
    print(f"   示例1: 创建double和triple函数")
    print(f"   double(5) = {double(5)}")
    print(f"   triple(5) = {triple(5)}")
    
    # 预设关键字参数
    format_number = lambda value, prefix="", suffix="": f"{prefix}{value}{suffix}"
    format_currency = functools.partial(format_number, prefix="$", suffix=" USD")
    
    print(f"   \n示例2: 创建格式化货币的函数")
    print(f"   format_currency(100) = '{format_currency(100)}'")
    print(f"   format_currency(200, suffix=' EUR') = '{format_currency(200, suffix=' EUR')}'")
    
    # 实际应用：预设日志级别
    def log(level, message):
        print(f"[{level.upper()}] {message}")
    
    info = functools.partial(log, "INFO")
    error = functools.partial(log, "ERROR")
    warning = functools.partial(log, "WARNING")
    
    print(f"   \n示例3: 创建日志级别函数")
    info("这是一条信息日志")
    warning("这是一条警告日志")
    error("这是一条错误日志")
    
    print("\n5. functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):")
    print("   更新wrapper函数，使其看起来像wrapped函数")
    print("   复制元数据（如名称、文档字符串、模块名等）")
    
    def original_function(x):
        """这是原始函数的文档字符串"""
        return x * 2
    
    # 不使用update_wrapper
    def bad_decorator(func):
        def wrapper(*args, **kwargs):
            print("装饰器逻辑执行")
            return func(*args, **kwargs)
        return wrapper
    
    # 使用update_wrapper
    def good_decorator(func):
        def wrapper(*args, **kwargs):
            print("装饰器逻辑执行")
            return func(*args, **kwargs)
        # 更新wrapper以保留原始函数的元数据
        functools.update_wrapper(wrapper, func)
        return wrapper
    
    bad_wrapped = bad_decorator(original_function)
    good_wrapped = good_decorator(original_function)
    
    print("   示例: 比较使用和不使用update_wrapper的装饰器")
    print("   原始函数:")
    print(f"     __name__: {original_function.__name__}")
    print(f"     __doc__: {original_function.__doc__}")
    print(f"     调用结果: {original_function(5)}")
    
    print("   \n不使用update_wrapper的装饰器:")
    print(f"     __name__: {bad_wrapped.__name__}")
    print(f"     __doc__: {bad_wrapped.__doc__}")
    print(f"     调用结果: {bad_wrapped(5)}")
    
    print("   \n使用update_wrapper的装饰器:")
    print(f"     __name__: {good_wrapped.__name__}")
    print(f"     __doc__: {good_wrapped.__doc__}")
    print(f"     调用结果: {good_wrapped(5)}")
    
    print("\n6. functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES):")
    print("   这是update_wrapper的装饰器版本，更方便使用")
    print("   自动将wrapper函数的元数据更新为wrapped函数的元数据")
    
    @functools.wraps(original_function)
    def better_decorator(func):
        def wrapper(*args, **kwargs):
            """这是装饰器的文档字符串"""
            print("使用wraps的装饰器逻辑执行")
            return func(*args, **kwargs)
        return wrapper
    
    # 应用装饰器
    wrapped_with_wraps = better_decorator(original_function)
    
    print("   示例: 使用wraps装饰器")
    print(f"   __name__: {wrapped_with_wraps.__name__}")
    print(f"   __doc__: {wrapped_with_wraps.__doc__}")
    print(f"   调用结果: {wrapped_with_wraps(5)}")
    
    # 更典型的装饰器用法
    def log_execution(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"执行函数: {func.__name__}")
            result = func(*args, **kwargs)
            print(f"函数 {func.__name__} 执行完成")
            return result
        return wrapper
    
    @log_execution
    def example_function(n):
        """示例函数：计算斐波那契数"""
        if n < 2:
            return n
        return example_function(n-1) + example_function(n-2)
    
    print("   \n典型装饰器用法:")
    print(f"   函数名称: {example_function.__name__}")
    print(f"   函数文档: {example_function.__doc__}")
    print(f"   调用example_function(3):")
    example_function(3)
    
    print("\n7. functools.total_ordering(cls):")
    print("   为类自动生成比较方法，只需要定义__eq__和一个排序方法（如__lt__, __le__, __gt__, __ge__之一）")
    print("   这简化了为类实现全序关系的工作")
    
    @functools.total_ordering
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __eq__(self, other):
            if not isinstance(other, Person):
                return NotImplemented
            return self.age == other.age
        
        def __lt__(self, other):
            if not isinstance(other, Person):
                return NotImplemented
            return self.age < other.age
        
        def __repr__(self):
            return f"Person(name='{self.name}', age={self.age})"
    
    # 创建Person对象
    alice = Person("Alice", 25)
    bob = Person("Bob", 30)
    charlie = Person("Charlie", 25)
    
    print("   示例: 使用total_ordering装饰类")
    print(f"   alice = {alice}")
    print(f"   bob = {bob}")
    print(f"   charlie = {charlie}")
    
    print("   \n比较操作:")
    print(f"   alice == charlie: {alice == charlie}")
    print(f"   alice != bob: {alice != bob}")
    print(f"   alice < bob: {alice < bob}")
    print(f"   alice <= bob: {alice <= bob}")
    print(f"   bob > charlie: {bob > charlie}")
    print(f"   bob >= alice: {bob >= alice}")
    
    # 排序Person对象列表
    people = [bob, alice, charlie]
    people.sort()
    print(f"   \n排序后的人员列表: {people}")
    
    print("\n8. functools.singledispatch(func):")
    print("   为函数创建单分派泛型函数，根据第一个参数的类型选择不同的实现")
    print("   这是Python中实现函数重载的一种方式")
    
    @functools.singledispatch
    def process_data(data):
        """处理数据的通用函数"""
        print(f"处理通用数据: {data}")
    
    @process_data.register(int)
    def _(data):
        """处理整数数据"""
        print(f"处理整数: {data}, 平方: {data ** 2}")
    
    @process_data.register(str)
    def _(data):
        """处理字符串数据"""
        print(f"处理字符串: '{data}', 长度: {len(data)}")
    
    @process_data.register(list)
    def _(data):
        """处理列表数据"""
        print(f"处理列表: {data}, 总和: {sum(data) if all(isinstance(x, (int, float)) for x in data) else '无法计算'}")
    
    # 还可以注册多个类型
    @process_data.register(tuple)
    @process_data.register(set)
    def _(data):
        """处理元组和集合数据"""
        print(f"处理{type(data).__name__}: {data}, 元素数量: {len(data)}")
    
    print("   示例: 使用singledispatch创建泛型函数")
    process_data(42)
    process_data("hello")
    process_data([1, 2, 3, 4, 5])
    process_data((1, 2, 3))
    process_data({1, 2, 3, 4})
    process_data(3.14)  # 使用默认实现
    
    print("   \n查看泛型函数的注册类型:")
    print(f"   注册的类型: {list(process_data.registry.keys())}")
    print(f"   默认实现: {process_data.registry[object]}")
    
    print("\n9. functools.cmp_to_key(func):")
    print("   将旧式的比较函数转换为key函数，用于sorted()、list.sort()等函数")
    print("   比较函数应该返回负数、零或正数，表示第一个参数小于、等于或大于第二个参数")
    
    # 定义一个旧式比较函数
    def compare_length(a, b):
        """根据字符串长度比较"""
        return len(a) - len(b)
    
    # 字符串列表
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    
    # 使用cmp_to_key转换比较函数
    sorted_by_length = sorted(words, key=functools.cmp_to_key(compare_length))
    
    print("   示例: 使用cmp_to_key排序")
    print(f"   原始列表: {words}")
    print(f"   按长度排序: {sorted_by_length}")
    
    # 更复杂的比较函数
    def compare_person(a, b):
        """先按年龄比较，年龄相同则按名字比较"""
        if a.age != b.age:
            return a.age - b.age
        return (a.name > b.name) - (a.name < b.name)  # 等同于字符串比较
    
    # 创建Person对象列表
    people = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 30),
        Person("David", 25)
    ]
    
    # 使用cmp_to_key排序
    sorted_people = sorted(people, key=functools.cmp_to_key(compare_person))
    
    print("   \n示例: 复杂对象排序")
    print(f"   排序后的人员列表:")
    for person in sorted_people:
        print(f"     {person}")

functools_core_functions()
print()

# 3. 高级应用示例
print("=== 3. 高级应用示例 ===")

def functools_advanced_examples():
    """functools模块的高级应用示例"""
    import functools
    import time
    
    print("示例1: 创建自定义缓存装饰器")
    def custom_cache_decorator():
        """创建一个可以清除缓存的装饰器"""
        
        def decorator(func):
            # 使用字典存储缓存
            cache = {}
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 创建缓存键
                key = (args, frozenset(kwargs.items()))
                
                # 检查缓存
                if key not in cache:
                    cache[key] = func(*args, **kwargs)
                    print(f"缓存miss，计算结果: {cache[key]}")
                else:
                    print(f"缓存hit，使用缓存结果: {cache[key]}")
                
                return cache[key]
            
            # 添加清除缓存的方法
            def clear_cache():
                nonlocal cache
                size = len(cache)
                cache.clear()
                print(f"缓存已清除，共{size}个条目")
            
            # 将清除缓存方法附加到包装函数
            wrapper.clear_cache = clear_cache
            
            # 添加获取缓存统计的方法
            def cache_info():
                return len(cache)
            
            wrapper.cache_info = cache_info
            
            return wrapper
        
        return decorator
    
    # 测试自定义缓存装饰器
    @custom_cache_decorator()
    def fibonacci(n):
        """计算斐波那契数列"""
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    print("   使用自定义缓存装饰器:")
    print("   计算fibonacci(5):")
    result = fibonacci(5)
    print(f"   结果: {result}")
    print(f"   缓存条目数: {fibonacci.cache_info()}")
    
    print("   \n再次计算fibonacci(5):")
    result = fibonacci(5)
    
    print("   \n清除缓存:")
    fibonacci.clear_cache()
    
    print("   \n清除后再次计算fibonacci(5):")
    result = fibonacci(5)
    
    print("\n示例2: 创建带有超时机制的缓存装饰器")
    def timed_cache(max_age_seconds):
        """创建一个具有超时机制的缓存装饰器"""
        def decorator(func):
            # 使用字典存储缓存，值为(结果, 时间戳)对
            cache = {}
            
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 创建缓存键
                key = (args, frozenset(kwargs.items()))
                current_time = time.time()
                
                # 检查缓存是否存在且未过期
                if key in cache:
                    result, timestamp = cache[key]
                    if current_time - timestamp < max_age_seconds:
                        print(f"缓存命中，结果: {result}")
                        return result
                    else:
                        print("缓存已过期，重新计算")
                
                # 计算新结果
                result = func(*args, **kwargs)
                cache[key] = (result, current_time)
                print(f"缓存未命中，计算结果: {result}")
                
                return result
            
            return wrapper
        
        return decorator
    
    # 测试带超时的缓存装饰器
    @timed_cache(max_age_seconds=2)  # 缓存2秒后过期
    def get_current_price(product_id):
        """模拟获取产品当前价格"""
        print(f"查询数据库获取产品{product_id}的价格")
        # 模拟数据库查询延迟
        time.sleep(0.5)
        return 100 + product_id * 10  # 示例价格
    
    print("   使用带超时的缓存装饰器:")
    print("   第一次查询产品1的价格:")
    price1 = get_current_price(1)
    
    print("   \n立即再次查询产品1的价格:")
    price1 = get_current_price(1)
    
    print("   \n等待3秒后再次查询产品1的价格:")
    time.sleep(3)
    price1 = get_current_price(1)
    
    print("\n示例3: 使用partial实现函数适配器")
    def function_adapter_example():
        """使用partial创建函数适配器"""
        
        # 假设这是一个库函数，接口固定
        def library_function(a, b, c, callback=None):
            """一个库函数，参数顺序固定"""
            result = a + b + c
            if callback:
                return callback(result)
            return result
        
        # 但我们有一个现有函数，参数顺序或数量不匹配
        def my_callback(value, prefix="Result: "):
            """我们的回调函数"""
            return f"{prefix}{value}"
        
        # 使用partial创建适配器
        adapted_callback = functools.partial(my_callback, prefix="计算结果: ")
        
        print("   使用partial创建函数适配器:")
        result = library_function(1, 2, 3, callback=adapted_callback)
        print(f"   库函数调用结果: {result}")
        
        # 另一个例子：适配具有不同参数顺序的函数
        def add_three_numbers(x, y, z):
            return x + y + z
        
        # 创建一个适配器，使参数顺序变为z, x, y
        def adapter(func):
            @functools.wraps(func)
            def wrapper(z, x, y):
                return func(x, y, z)
            return wrapper
        
        adapted_add = adapter(add_three_numbers)
        print("   \n使用装饰器适配参数顺序:")
        print(f"   原始函数 add_three_numbers(1, 2, 3) = {add_three_numbers(1, 2, 3)}")
        print(f"   适配函数 adapted_add(3, 1, 2) = {adapted_add(3, 1, 2)}")
    
    function_adapter_example()
    
    print("\n示例4: 使用singledispatch实现多态")
    def singledispatch_polymorphism():
        """使用singledispatch实现更复杂的多态行为"""
        
        @functools.singledispatch
        def format_data(data):
            """格式化数据的通用函数"""
            return str(data)
        
        @format_data.register(list)
        def _(data):
            """格式化列表数据"""
            return "[" + ", ".join(format_data(item) for item in data) + "]"
        
        @format_data.register(dict)
        def _(data):
            """格式化字典数据"""
            items = [f"{format_data(k)}: {format_data(v)}" for k, v in data.items()]
            return "{" + ", ".join(items) + "}"
        
        @format_data.register(int)
        def _(data):
            """格式化整数数据"""
            return f"整数({data})"
        
        @format_data.register(str)
        def _(data):
            """格式化字符串数据"""
            return f'字符串("{data}")'
        
        # 测试嵌套数据结构的格式化
        complex_data = {
            "name": "John",
            "age": 30,
            "skills": ["Python", "JavaScript", "Java"],
            "address": {
                "city": "New York",
                "zipcode": 10001
            }
        }
        
        print("   使用singledispatch格式化复杂数据结构:")
        formatted = format_data(complex_data)
        print(f"   格式化结果: {formatted}")
        
        # 动态注册新类型
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age
        
        # 动态注册Person类型的格式化方法
        @format_data.register(Person)
        def _(data):
            return f"Person(name='{data.name}', age={data.age})"
        
        # 测试新注册的类型
        person = Person("Alice", 25)
        print(f"   \n格式化Person对象: {format_data(person)}")
    
    singledispatch_polymorphism()
    
    print("\n示例5: 实现记忆化递归函数")
    def memoized_recursion():
        """使用functools.cache实现高效的递归函数"""
        
        print("   比较普通递归和记忆化递归的性能:")
        
        # 普通递归计算斐波那契数
        def fib_normal(n):
            if n < 2:
                return n
            return fib_normal(n-1) + fib_normal(n-2)
        
        # 使用cache装饰的递归函数
        @functools.cache
        def fib_memoized(n):
            if n < 2:
                return n
            return fib_memoized(n-1) + fib_memoized(n-2)
        
        # 测试性能
        n = 35  # 计算较大的斐波那契数以显示差异
        
        print(f"   计算斐波那契数F({n}):")
        
        # 测试普通递归
        print("   普通递归:")
        start_time = time.time()
        # 注意：这可能会非常慢，对于大n可能无法在合理时间内完成
        # 这里使用较小的n值进行演示
        try:
            if n > 30:  # 避免程序运行时间过长
                raise ValueError("n too large for normal recursion")
            result_normal = fib_normal(n)
            normal_time = time.time() - start_time
            print(f"     结果: {result_normal}")
            print(f"     耗时: {normal_time:.6f} 秒")
        except ValueError as e:
            print(f"     {e}，跳过测试")
        
        # 测试记忆化递归
        print("   记忆化递归:")
        start_time = time.time()
        result_memoized = fib_memoized(n)
        memoized_time = time.time() - start_time
        print(f"     结果: {result_memoized}")
        print(f"     耗时: {memoized_time:.6f} 秒")
        
        # 显示缓存统计
        print(f"     缓存信息: {fib_memoized.cache_info()}")
        
        # 清除缓存后再次测试
        print("   清除缓存后再次计算:")
        fib_memoized.cache_clear()
        start_time = time.time()
        result_memoized = fib_memoized(n)
        memoized_time2 = time.time() - start_time
        print(f"     结果: {result_memoized}")
        print(f"     耗时: {memoized_time2:.6f} 秒")
    
    memoized_recursion()

functools_advanced_examples()
print()

# 4. 性能考虑
print("=== 4. 性能考虑 ===")

def functools_performance_considerations():
    """functools模块的性能考虑"""
    import functools
    import time
    import random
    
    print("1. 缓存装饰器的性能影响:")
    print("   - 对于计算密集型函数，使用cache或lru_cache可以显著提高性能")
    print("   - 但对于简单函数，缓存的开销可能超过计算本身")
    print("   - cache和lru_cache使用字典存储结果，查找速度为O(1)")
    print("   - lru_cache的maxsize参数会影响内存使用，适当设置可以平衡性能和内存占用")
    
    print("\n2. 缓存装饰器性能测试:")
    # 定义不同复杂度的函数进行测试
    
    # 简单函数
    def simple_function(x):
        return x * 2
    
    # 中等复杂度函数
    def medium_function(x):
        result = 0
        for i in range(x):
            result += i
        return result
    
    # 复杂函数
    def complex_function(x):
        result = 0
        for i in range(x):
            result += sum(j for j in range(i))
        return result
    
    # 使用lru_cache装饰
    cached_simple = functools.lru_cache()(simple_function)
    cached_medium = functools.lru_cache()(medium_function)
    cached_complex = functools.lru_cache()(complex_function)
    
    # 测试参数
    simple_param = 1000
    medium_param = 1000
    complex_param = 100
    num_calls = 1000
    
    # 测试简单函数
    print(f"   \n测试简单函数 (参数: {simple_param}, 调用次数: {num_calls}):")
    
    # 非缓存版本
    start_time = time.time()
    for _ in range(num_calls):
        simple_function(simple_param)
    simple_time = time.time() - start_time
    print(f"     非缓存版本耗时: {simple_time:.6f} 秒")
    
    # 缓存版本（第一次调用，无缓存）
    start_time = time.time()
    cached_simple(simple_param)  # 第一次调用，填充缓存
    first_cache_time = time.time() - start_time
    print(f"     缓存版本第一次调用耗时: {first_cache_time:.6f} 秒")
    
    # 缓存版本（后续调用，有缓存）
    start_time = time.time()
    for _ in range(num_calls - 1):
        cached_simple(simple_param)
    cached_time = time.time() - start_time
    total_cached_time = first_cache_time + cached_time
    print(f"     缓存版本后续{num_calls-1}次调用耗时: {cached_time:.6f} 秒")
    print(f"     缓存版本总耗时: {total_cached_time:.6f} 秒")
    print(f"     速度比: {simple_time / total_cached_time:.2f}x")
    
    # 测试中等复杂度函数
    print(f"   \n测试中等复杂度函数 (参数: {medium_param}, 调用次数: {num_calls}):")
    
    # 非缓存版本
    start_time = time.time()
    for _ in range(num_calls):
        medium_function(medium_param)
    medium_time = time.time() - start_time
    print(f"     非缓存版本耗时: {medium_time:.6f} 秒")
    
    # 缓存版本（第一次调用，无缓存）
    start_time = time.time()
    cached_medium(medium_param)  # 第一次调用，填充缓存
    first_cache_time = time.time() - start_time
    print(f"     缓存版本第一次调用耗时: {first_cache_time:.6f} 秒")
    
    # 缓存版本（后续调用，有缓存）
    start_time = time.time()
    for _ in range(num_calls - 1):
        cached_medium(medium_param)
    cached_time = time.time() - start_time
    total_cached_time = first_cache_time + cached_time
    print(f"     缓存版本后续{num_calls-1}次调用耗时: {cached_time:.6f} 秒")
    print(f"     缓存版本总耗时: {total_cached_time:.6f} 秒")
    print(f"     速度比: {medium_time / total_cached_time:.2f}x")
    
    # 测试复杂函数
    print(f"   \n测试复杂函数 (参数: {complex_param}, 调用次数: {num_calls}):")
    
    # 非缓存版本
    start_time = time.time()
    for _ in range(num_calls):
        complex_function(complex_param)
    complex_time = time.time() - start_time
    print(f"     非缓存版本耗时: {complex_time:.6f} 秒")
    
    # 缓存版本（第一次调用，无缓存）
    start_time = time.time()
    cached_complex(complex_param)  # 第一次调用，填充缓存
    first_cache_time = time.time() - start_time
    print(f"     缓存版本第一次调用耗时: {first_cache_time:.6f} 秒")
    
    # 缓存版本（后续调用，有缓存）
    start_time = time.time()
    for _ in range(num_calls - 1):
        cached_complex(complex_param)
    cached_time = time.time() - start_time
    total_cached_time = first_cache_time + cached_time
    print(f"     缓存版本后续{num_calls-1}次调用耗时: {cached_time:.6f} 秒")
    print(f"     缓存版本总耗时: {total_cached_time:.6f} 秒")
    print(f"     速度比: {complex_time / total_cached_time:.2f}x")
    
    print("\n3. maxsize参数对lru_cache性能的影响:")
    print("   - maxsize=None 提供无限缓存，查找速度最快，但可能导致内存使用过多")
    print("   - maxsize=2^n 设置为2的幂可以获得最佳性能")
    print("   - 较小的maxsize会导致更多的缓存未命中，但内存使用更少")
    
    # 测试不同maxsize设置的性能
    print("   \n测试不同maxsize设置的性能:")
    
    # 定义要测试的maxsize值
    maxsizes = [None, 32, 128, 512, 2048]
    test_params = list(range(1000))  # 使用1000个不同的参数
    
    for maxsize in maxsizes:
        # 创建具有不同maxsize的缓存函数
        @functools.lru_cache(maxsize=maxsize)
        def cached_func(x):
            return x * x
        
        # 预热缓存
        for i in range(min(100, maxsize if maxsize is not None else 100)):
            cached_func(i)
        
        # 随机访问，混合命中和未命中
        random.shuffle(test_params)
        
        start_time = time.time()
        for i in test_params:
            cached_func(i)
        end_time = time.time()
        
        print(f"     maxsize={maxsize}: 耗时 {end_time - start_time:.6f} 秒, 缓存统计: {cached_func.cache_info()}")
    
    print("\n4. 装饰器对函数调用的影响:")
    print("   - 装饰器会引入额外的函数调用开销")
    print("   - wraps装饰器通过保留原始函数的元数据来提高可维护性")
    print("   - 对于性能关键路径，应权衡装饰器的便利性和性能开销")
    
    print("\n5. partial的性能考虑:")
    print("   - partial创建的新函数比直接调用原始函数稍慢")
    print("   - 但对于大多数用例，性能差异可以忽略不计")
    print("   - partial比手动创建包装函数更高效，因为它是在C级别实现的")
    
    # 测试partial的性能
    print("   \n测试partial的性能:")
    
    # 定义原始函数
    def add(a, b, c):
        return a + b + c
    
    # 使用partial
    add_five = functools.partial(add, 5)
    
    # 手动创建包装函数
    def manual_add_five(b, c):
        return add(5, b, c)
    
    # 测试调用性能
    iterations = 1000000
    
    # 测试原始函数
    start_time = time.time()
    for i in range(iterations):
        add(5, i, i+1)
    original_time = time.time() - start_time
    
    # 测试partial
    start_time = time.time()
    for i in range(iterations):
        add_five(i, i+1)
    partial_time = time.time() - start_time
    
    # 测试手动包装函数
    start_time = time.time()
    for i in range(iterations):
        manual_add_five(i, i+1)
    manual_time = time.time() - start_time
    
    print(f"     原始函数: {original_time:.6f} 秒")
    print(f"     partial包装: {partial_time:.6f} 秒 ({partial_time/original_time:.2f}x 慢)")
    print(f"     手动包装: {manual_time:.6f} 秒 ({manual_time/original_time:.2f}x 慢)")

functools_performance_considerations()
print()

# 5. 注意事项和常见问题
print("=== 5. 注意事项和常见问题 ===")

def functools_caveats_and_faq():
    """functools模块的注意事项和常见问题"""
    import functools
    import time
    
    print("1. 缓存装饰器的注意事项:")
    print("   - 缓存的键必须是可哈希的，因为它们存储在字典中")
    print("   - 避免对具有可变参数或副作用的函数使用缓存")
    print("   - 注意内存使用，无限缓存可能导致内存泄漏")
    print("   - 缓存不会自动失效，除非显式调用clear_cache()")
    
    # 示例：缓存可变参数会导致的问题
    print("   \n示例: 缓存可变参数导致的问题:")
    
    @functools.lru_cache()
    def process_list(items):
        """处理列表（错误用法：缓存可变参数）"""
        print(f"处理列表: {items}")
        return sum(items)
    
    try:
        # 列表是不可哈希的，会引发TypeError
        result = process_list([1, 2, 3])
        print(f"结果: {result}")
    except TypeError as e:
        print(f"错误: {e}")
    
    # 正确的做法：将可变参数转换为元组或其他可哈希类型
    @functools.lru_cache()
    def process_tuple(items):
        """处理元组（正确用法：缓存可哈希参数）"""
        print(f"处理元组: {items}")
        return sum(items)
    
    # 元组是可哈希的，可以被缓存
    result1 = process_tuple((1, 2, 3))
    print(f"\n使用元组参数:")
    print(f"结果1: {result1}")
    
    # 再次调用相同参数，应该从缓存中获取
    result2 = process_tuple((1, 2, 3))
    print(f"结果2: {result2} (来自缓存)")
    
    print("\n2. 装饰器使用的常见问题:")
    print("   - 不使用wraps装饰器会丢失原始函数的元数据")
    print("   - 多个装饰器应用时，顺序很重要")
    print("   - 装饰器本身定义在类内部时需要特殊处理")
    
    # 示例：多个装饰器的顺序
    print("   \n示例: 多个装饰器的应用顺序:")
    
    def decorator1(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("装饰器1：调用前")
            result = func(*args, **kwargs)
            print("装饰器1：调用后")
            return result
        return wrapper
    
    def decorator2(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("装饰器2：调用前")
            result = func(*args, **kwargs)
            print("装饰器2：调用后")
            return result
        return wrapper
    
    @decorator1
    @decorator2
    def example_function():
        print("执行原始函数")
        return "完成"
    
    print("装饰器应用顺序为：@decorator1 -> @decorator2 时的执行顺序:")
    result = example_function()
    print(f"结果: {result}")
    
    print("\n3. partial函数的注意事项:")
    print("   - partial创建的函数不能直接作为被装饰函数使用functools.wraps")
    print("   - partial预设的参数是在创建时求值的，而不是在调用时")
    
    # 示例：partial参数在创建时求值
    print("   \n示例: partial参数在创建时求值:")
    
    # 定义一个函数，记录调用时间
    def log_with_timestamp(message, timestamp=None):
        if timestamp is None:
            timestamp = time.time()
        return f"[{timestamp:.2f}] {message}"
    
    # 使用当前时间创建partial
    now = time.time()
    log_now = functools.partial(log_with_timestamp, timestamp=now)
    
    # 等待一段时间后调用
    time.sleep(1)
    print(f"立即创建的partial (1秒后调用): {log_now('消息1')}")
    
    # 再等待一段时间后再次调用
    time.sleep(1)
    print(f"相同partial (再过1秒后调用): {log_now('消息2')}")
    
    # 对比：每次调用都使用当前时间
    print(f"直接调用函数: {log_with_timestamp('消息3')}")
    time.sleep(1)
    print(f"直接调用函数 (1秒后): {log_with_timestamp('消息4')}")
    
    print("\n4. reduce函数的使用场景:")
    print("   - reduce适用于需要累积计算的场景")
    print("   - 但对于简单操作，Python内置的sum()、max()、min()等函数通常更高效更清晰")
    print("   - 对于复杂累积操作，考虑使用生成器表达式或列表推导式结合内置函数")
    
    # 示例：reduce与内置函数的比较
    numbers = list(range(1, 101))  # 1到100的数字
    
    print("   \n示例: reduce与内置函数的比较:")
    
    # 使用reduce计算总和
    start_time = time.time()
    sum_with_reduce = functools.reduce(lambda x, y: x + y, numbers)
    reduce_time = time.time() - start_time
    
    # 使用内置sum函数
    start_time = time.time()
    sum_with_builtin = sum(numbers)
    builtin_time = time.time() - start_time
    
    print(f"   使用reduce计算1-100的和: {sum_with_reduce}, 耗时: {reduce_time:.6f} 秒")
    print(f"   使用sum()计算1-100的和: {sum_with_builtin}, 耗时: {builtin_time:.6f} 秒")
    print(f"   内置sum()函数比reduce快约 {reduce_time/builtin_time:.2f} 倍")
    
    print("\n5. singledispatch的限制:")
    print("   - singledispatch只根据第一个参数的类型进行分派")
    print("   - 不支持基于多个参数类型的分派")
    print("   - 无法直接替换为函数重载（如其他语言中的实现）")
    
    # 示例：singledispatch的限制
    print("   \n示例: singledispatch只根据第一个参数类型分派:")
    
    @functools.singledispatch
    def mixed_types(a, b):
        print(f"默认实现: a={a}, b={b}")
        return a, b
    
    @mixed_types.register(int)
    def _(a, b):
        print(f"a是整数: a={a}, b={b}")
        return a * b
    
    @mixed_types.register(str)
    def _(a, b):
        print(f"a是字符串: a={a}, b={b}")
        return a + str(b)
    
    print("   调用mixed_types(10, 'hello'):")
    mixed_types(10, "hello")  # 使用int版本，因为第一个参数是int
    
    print("   \n调用mixed_types('hello', 10):")
    mixed_types("hello", 10)  # 使用str版本，因为第一个参数是str
    
    print("\n6. total_ordering的注意事项:")
    print("   - 必须至少实现__eq__和一个排序方法(__lt__, __le__, __gt__, __ge__之一)")
    print("   - 如果同时实现多个排序方法，应该确保它们之间的一致性")
    print("   - total_ordering装饰的类可能比手动实现所有比较方法稍慢")
    
    print("\n7. 常见问题解答 (FAQ):")
    print("   Q1: cache和lru_cache有什么区别？")
    print("   A1: cache是Python 3.9新增的，相当于lru_cache(maxsize=None)，提供无限缓存。")
    print("       lru_cache可以设置maxsize限制缓存大小，当缓存满时会移除最久未使用的条目。")
    
    print("   \nQ2: 如何选择合适的maxsize值？")
    print("   A2: 对于大多数用例，默认值128是一个很好的起点。")
    print("       如果函数调用非常频繁且参数组合有限，可以设置更大的值。")
    print("       如果内存是关键考虑因素，可以设置较小的值。")
    print("       对于性能最优，设置为2的幂次方值。")
    
    print("   \nQ3: 可以缓存带有副作用的函数吗？")
    print("   A3: 不建议缓存带有副作用的函数，因为缓存会跳过函数执行，导致副作用不发生。")
    print("       副作用包括修改全局状态、执行I/O操作、改变传入的可变参数等。")
    
    print("   \nQ4: wraps装饰器具体复制了哪些元数据？")
    print("   A4: wraps默认复制以下属性：__module__、__name__、__qualname__、__doc__、__annotations__。")
    print("       还会更新__dict__中的属性，并复制自定义属性。")
    
    print("   \nQ5: singledispatch和multipledispatch有什么区别？")
    print("   A5: singledispatch是标准库的一部分，只根据第一个参数的类型分派。")
    print("       multipledispatch是第三方库，可以根据多个参数的类型进行分派。")
    
    print("   \nQ6: 如何清除lru_cache或cache的缓存？")
    print("   A6: 可以调用装饰函数的cache_clear()方法来清除缓存。")
    print("       例如：@functools.lru_cache()装饰的函数func可以通过func.cache_clear()清除缓存。")
    
    print("   \nQ7: 什么情况下应该使用reduce而不是列表推导式？")
    print("   A7: 当操作需要累积前一次计算的结果作为输入时，reduce更合适。")
    print("       对于简单的映射或过滤操作，列表推导式通常更清晰。")
    print("       对于内置函数能处理的操作（如sum、max、min），优先使用内置函数。")
    
    print("   \nQ8: partial和闭包有什么区别？")
    print("   A8: partial是一个内置工具，可以预设函数的部分参数。")
    print("       闭包是一种函数式编程概念，允许函数访问其定义范围之外的变量。")
    print("       partial通常比手动创建闭包更高效，因为它是在C级别实现的。")
    print("       partial更适合简单的参数预设，而闭包可以实现更复杂的逻辑。")

functools_caveats_and_faq()
print()

# 6. 输入输出示例
print("=== 6. 输入输出示例 ===")

def functools_examples():
    """functools模块的输入输出示例"""
    import functools
    
    print("示例1: 使用lru_cache优化递归函数")
    print("输入:")
    print("""
    @functools.lru_cache()
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    # 第一次调用
    result1 = fibonacci(10)
    print(f"fibonacci(10) = {result1}")
    print(f"缓存信息: {fibonacci.cache_info()}")
    
    # 再次调用，从缓存获取
    result2 = fibonacci(10)
    print(f"再次调用 fibonacci(10) = {result2}")
    print(f"缓存信息: {fibonacci.cache_info()}")
    """)
    
    print("输出:")
    print("""
    fibonacci(10) = 55
    缓存信息: CacheInfo(hits=8, misses=11, maxsize=128, currsize=11)
    再次调用 fibonacci(10) = 55
    缓存信息: CacheInfo(hits=9, misses=11, maxsize=128, currsize=11)
    """)
    print()
    
    print("示例2: 使用partial预设函数参数")
    print("输入:")
    print("""
    # 定义一个格式化日期的函数
    def format_date(year, month, day, format_str="%Y-%m-%d"):
        return f"{year}{format_str[4]}{month:02d}{format_str[7]}{day:02d}"
    
    # 创建预设年份的函数
    format_2023_date = functools.partial(format_date, 2023)
    
    # 创建预设年份和格式的函数
    format_2023_jp_date = functools.partial(format_date, 2023, format_str="%Y/%m/%d")
    
    print(f"format_2023_date(6, 15) = '{format_2023_date(6, 15)}'")
    print(f"format_2023_jp_date(6, 15) = '{format_2023_jp_date(6, 15)}'")
    """)
    
    print("输出:")
    print("""
    format_2023_date(6, 15) = '2023-06-15'
    format_2023_jp_date(6, 15) = '2023/06/15'
    """)
    print()
    
    print("示例3: 使用total_ordering实现类的比较方法")
    print("输入:")
    print("""
    @functools.total_ordering
    class Book:
        def __init__(self, title, author, year):
            self.title = title
            self.author = author
            self.year = year
        
        def __eq__(self, other):
            if not isinstance(other, Book):
                return NotImplemented
            return self.year == other.year
        
        def __lt__(self, other):
            if not isinstance(other, Book):
                return NotImplemented
            return self.year < other.year
        
        def __repr__(self):
            return f"Book('{self.title}', '{self.author}', {self.year})"
    
    # 创建Book对象
    book1 = Book("Python Basics", "John Smith", 2020)
    book2 = Book("Advanced Python", "Jane Doe", 2022)
    book3 = Book("Python Cookbook", "John Smith", 2022)
    
    # 测试比较操作
    print(f"book1 < book2: {book1 < book2}")
    print(f"book2 > book1: {book2 > book1}")
    print(f"book2 == book3: {book2 == book3}")
    print(f"book2 <= book3: {book2 <= book3}")
    
    # 测试排序
    books = [book2, book1, book3]
    books.sort()
    print(f"排序后的列表: {books}")
    """)
    
    print("输出:")
    print("""
    book1 < book2: True
    book2 > book1: True
    book2 == book3: True
    book2 <= book3: True
    排序后的列表: [Book('Python Basics', 'John Smith', 2020), Book('Advanced Python', 'Jane Doe', 2022), Book('Python Cookbook', 'John Smith', 2022)]
    """)
    print()
    
    print("示例4: 使用singledispatch实现泛型函数")
    print("输入:")
    print("""
    @functools.singledispatch
    def format_value(value):
        """格式化值的通用函数"""
        return str(value)
    
    @format_value.register(int)
    def _(value):
        """格式化整数: 添加千位分隔符"""
        return f"{value:,}"
    
    @format_value.register(float)
    def _(value):
        """格式化浮点数: 保留两位小数"""
        return f"{value:.2f}"
    
    @format_value.register(str)
    def _(value):
        """格式化字符串: 添加引号"""
        return f'"{value}"'
    
    @format_value.register(list)
    def _(value):
        """格式化列表: 格式化每个元素"""
        formatted = [format_value(item) for item in value]
        return f"[{', '.join(formatted)}]"
    
    # 测试不同类型的值
    print(f"整数: {format_value(1000000)}")
    print(f"浮点数: {format_value(3.14159)}")
    print(f"字符串: {format_value('hello')}")
    print(f"列表: {format_value([1000, 3.14, 'world'])}")
    print(f"布尔值: {format_value(True)}")  # 使用默认实现
    """)
    
    print("输出:")
    print("""
    整数: 1,000,000
    浮点数: 3.14
    字符串: "hello"
    列表: [1,000, 3.14, "world"]
    布尔值: True
    """)
    print()
    
    print("示例5: 使用wraps保留函数元数据")
    print("输入:")
    print("""
    def with_wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """这是wrapper的文档"""
            print(f"调用函数: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    def without_wraps(func):
        def wrapper(*args, **kwargs):
            """这是wrapper的文档"""
            print(f"调用函数: {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    
    def original_func(x):
        """原始函数的文档字符串"""
        return x * 2
    
    wrapped_with = with_wraps(original_func)
    wrapped_without = without_wraps(original_func)
    
    print("使用wraps的装饰器:")
    print(f"  __name__: {wrapped_with.__name__}")
    print(f"  __doc__: {wrapped_with.__doc__}")
    
    print("\n不使用wraps的装饰器:")
    print(f"  __name__: {wrapped_without.__name__}")
    print(f"  __doc__: {wrapped_without.__doc__}")
    """)
    
    print("输出:")
    print("""
    使用wraps的装饰器:
      __name__: original_func
      __doc__: 原始函数的文档字符串

    不使用wraps的装饰器:
      __name__: wrapper
      __doc__: 这是wrapper的文档
    """)

functools_examples()
print()

# 7. 总结和完整导入指南
print("=== 7. 总结和完整导入指南 ===")

def functools_summary():
    """functools模块总结和导入指南"""
    print("7.1 模块总结:")
    print("   functools模块提供了一系列用于函数操作和扩展的工具，主要功能包括：")
    print("   - 函数缓存：通过cache、lru_cache装饰器提高性能")
    print("   - 函数装饰器工具：wraps、update_wrapper保留函数元数据")
    print("   - 部分应用：partial预设函数参数")
    print("   - 累积计算：reduce连续应用二元函数")
    print("   - 类辅助：total_ordering自动生成比较方法")
    print("   - 泛型函数：singledispatch根据类型分派函数实现")
    print("   - 兼容性工具：cmp_to_key用于转换比较函数")
    print()
    
    print("7.2 完整导入指南:")
    print("   1. 导入整个模块:")
    print("      import functools")
    print("      ")
    print("   2. 导入特定函数:")
    print("      from functools import cache, lru_cache, reduce, partial")
    print("      from functools import wraps, update_wrapper, total_ordering")
    print("      from functools import singledispatch, cmp_to_key")
    print("      ")
    print("   3. 常用导入组合:")
    print("      # 函数缓存常用导入")
    print("      from functools import lru_cache, cache")
    print("      ")
    print("      # 装饰器开发常用导入")
    print("      from functools import wraps, update_wrapper")
    print("      ")
    print("      # 函数式编程常用导入")
    print("      from functools import reduce, partial")
    print()
    
    print("7.3 版本兼容性:")
    print("   - cache装饰器是Python 3.9新增的")
    print("   - singledispatch是Python 3.4新增的")
    print("   - lru_cache的typed参数是Python 3.3新增的")
    print("   - 在Python 2.x中，functools模块的功能有所不同，建议查阅对应版本的文档")
    print()
    
    print("7.4 最佳实践:")
    print("   1. 对于需要多次计算相同参数的函数，优先使用lru_cache或cache装饰器")
    print("   2. 开发装饰器时，始终使用wraps装饰器保留原始函数的元数据")
    print("   3. 需要预设函数部分参数时，使用partial而不是手动创建包装函数")
    print("   4. 为类实现比较方法时，使用total_ordering减少样板代码")
    print("   5. 需要根据参数类型提供不同实现时，考虑使用singledispatch")
    print("   6. 对于简单的累积操作，优先使用内置函数而不是reduce")
    print("   7. 使用缓存时，注意键的可哈希性和内存使用")

functools_summary()
print()

# 运行总结
print("=== 运行总结 ===")
print("本文件详细介绍了Python的functools模块，涵盖了其核心功能、高级应用、性能考虑和注意事项。")
print("通过实际的代码示例和输入输出展示，帮助您理解如何有效地使用这个强大的模块。")
print("functools模块是函数式编程风格的重要支持，能够帮助您编写更简洁、高效的代码。")
print("在实际应用中，根据具体需求选择合适的函数，将大大提升代码的质量和性能。")