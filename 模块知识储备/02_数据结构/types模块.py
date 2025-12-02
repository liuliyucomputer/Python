# Python types模块详解

# 1. types模块概述
print("=== 1. types模块概述 ===")
print("types模块提供了Python内置类型的类型对象和其他与类型相关的实用函数。")
print("该模块主要用于以下场景：")
print("- 检查对象的具体类型（比使用isinstance更精确）")
print("- 创建自定义类型和函数")
print("- 动态修改和检查函数属性")
print("- 类型元编程和高级类型操作")
print("types模块是Python标准库的一部分，提供了对Python内部类型系统的访问。")
print()

# 2. types模块中的类型对象
print("=== 2. types模块中的类型对象 ===")

def types_type_objects():
    """展示types模块中的主要类型对象"""
    import types
    import inspect
    
    print("1. 基本类型对象")
    print("   types模块提供了Python内置类型的类型对象，可以用于精确的类型检查")
    
    # 基本类型对象示例
    print("   \n常用类型对象:")
    
    # 函数类型
    def example_function():
        pass
    
    # 方法类型
    class ExampleClass:
        def example_method(self):
            pass
    
    # 创建实例和方法
    obj = ExampleClass()
    
    # 生成器函数
    def example_generator():
        yield 1
    
    # 定义异步函数和异步生成器函数
    async def async_func():
        pass
    
    async def async_gen():
        yield
    
    # 检查类型
    print(f"   函数类型: {isinstance(example_function, types.FunctionType)}")
    print(f"   方法类型: {isinstance(obj.example_method, types.MethodType)}")
    print(f"   生成器类型: {isinstance(example_generator(), types.GeneratorType)}")
    print(f"   协程类型: {isinstance(async_func(), types.CoroutineType)}")
    print(f"   异步生成器类型: {isinstance(async_gen(), types.AsyncGeneratorType)}")
    print(f"   模块类型: {isinstance(types, types.ModuleType)}")
    print(f"   类型类型: {isinstance(int, types.TypeType)}")
    print(f"   内置函数类型: {isinstance(len, types.BuiltinFunctionType)}")
    
    print("\n2. 其他重要类型对象")
    print("   types模块还提供了许多其他类型对象，用于更精细的类型检查")
    
    # 特殊方法类型
    class WithSpecialMethods:
        def __call__(self):
            pass
        
        def __getitem__(self, key):
            pass
    
    # Lambda函数
    lambda_func = lambda x: x * 2
    
    # 检查更多类型
    print(f"   Lambda函数类型: {isinstance(lambda_func, types.LambdaType)}")  # 注意：在Python 3中，lambda也是FunctionType
    print(f"   代码对象类型: {isinstance(example_function.__code__, types.CodeType)}")
    print(f"   帧对象类型: {isinstance(inspect.currentframe(), types.FrameType)}")
    print(f"   追踪对象类型: {isinstance(inspect.currentframe().f_trace, types.TracebackType)}")
    print(f"   映射代理类型: {isinstance(type.__dict__, types.MappingProxyType)}")
    
    # 某些类型可能只在特定Python版本中可用
    try:
        print(f"   准备好的对象类型: {hasattr(types, 'ReadyType')}")
    except AttributeError:
        print("   准备好的对象类型: 不可用（Python版本不支持）")
    
    print("\n3. 使用类型对象进行精确类型检查")
    print("   使用types模块可以区分不同类型的可调用对象")
    
    # 定义各种可调用对象
    def regular_function():
        """普通函数"""
        pass
    
    lambda_func = lambda x: x
    
    class MyClass:
        @staticmethod
        def static_method():
            pass
        
        @classmethod
        def class_method(cls):
            pass
        
        def instance_method(self):
            pass
    
    # 创建实例
    my_instance = MyClass()
    
    # 检查各种方法的类型
    print("   \n可调用对象类型检查:")
    print(f"   普通函数: {type(regular_function)}")
    print(f"   Lambda函数: {type(lambda_func)}")
    print(f"   实例方法: {type(my_instance.instance_method)}")
    print(f"   静态方法: {type(MyClass.static_method)}")
    print(f"   类方法: {type(MyClass.class_method)}")
    print(f"   内置函数: {type(len)}")
    
    # 使用isinstance和types对象进行比较
    print("   \nisinstance检查:")
    print(f"   regular_function是FunctionType: {isinstance(regular_function, types.FunctionType)}")
    print(f"   lambda_func是FunctionType: {isinstance(lambda_func, types.FunctionType)}")
    print(f"   my_instance.instance_method是MethodType: {isinstance(my_instance.instance_method, types.MethodType)}")
    print(f"   MyClass.static_method是FunctionType: {isinstance(MyClass.static_method, types.FunctionType)}")
    print(f"   len是BuiltinFunctionType: {isinstance(len, types.BuiltinFunctionType)}")
    
    print("\n4. 类型对象的实际应用")
    print("   在需要区分不同类型的可调用对象时特别有用")
    
    # 定义一个函数，根据可调用对象的类型执行不同操作
    def process_callable(callable_obj):
        """根据可调用对象的类型执行不同的处理"""
        if isinstance(callable_obj, types.FunctionType):
            return f"普通函数: {callable_obj.__name__}"
        elif isinstance(callable_obj, types.MethodType):
            return f"方法: {callable_obj.__name__}"
        elif isinstance(callable_obj, types.BuiltinFunctionType):
            return f"内置函数: {callable_obj.__name__}"
        else:
            return f"其他可调用类型: {type(callable_obj).__name__}"
    
    # 测试各种可调用对象
    results = [
        process_callable(regular_function),
        process_callable(lambda_func),
        process_callable(my_instance.instance_method),
        process_callable(MyClass.static_method),
        process_callable(len)
    ]
    
    print("   \n可调用对象处理结果:")
    for result in results:
        print(f"   {result}")
    
    print("\n5. 类型对象的属性")
    print("   类型对象本身也有一些有用的属性")
    
    # 检查函数类型对象的属性
    func_type_attrs = dir(types.FunctionType)
    print(f"   FunctionType对象的主要属性: {[attr for attr in func_type_attrs if not attr.startswith('__')][:5]}...")
    
    # 检查代码对象的属性
    code_obj = regular_function.__code__
    print("   \n代码对象的重要属性:")
    print(f"   co_name: {code_obj.co_name}")  # 函数名
    print(f"   co_argcount: {code_obj.co_argcount}")  # 参数数量
    print(f"   co_filename: {code_obj.co_filename}")  # 文件名
    print(f"   co_firstlineno: {code_obj.co_firstlineno}")  # 起始行号
    print(f"   co_consts: {code_obj.co_consts}")  # 常量
    print(f"   co_varnames: {code_obj.co_varnames}")  # 变量名

# 运行类型对象演示
types_type_objects()
print()

# 3. 创建自定义类型和函数
print("=== 3. 创建自定义类型和函数 ===")

def create_custom_types():
    """展示如何使用types模块创建自定义类型和函数"""
    import types
    import functools
    
    print("1. 动态创建函数")
    print("   使用types.FunctionType可以动态创建函数对象")
    
    # 定义一个简单的函数作为模板
    def template_function(x, y):
        return x + y
    
    # 获取模板函数的代码对象
    code_obj = template_function.__code__
    
    # 创建一个新的函数对象
    # 参数: code, globals, name=None, argdefs=None, closure=None
    new_func = types.FunctionType(
        code_obj,
        globals(),
        name="dynamic_add_function",  # 可以重命名函数
        argdefs=None,
        closure=None
    )
    
    # 测试新创建的函数
    print(f"   原始函数名: {template_function.__name__}")
    print(f"   动态创建的函数名: {new_func.__name__}")
    print(f"   template_function(5, 3) = {template_function(5, 3)}")
    print(f"   new_func(5, 3) = {new_func(5, 3)}")
    
    print("\n2. 创建自定义方法")
    print("   使用types.MethodType可以将函数绑定为对象的方法")
    
    # 定义一个类
    class Calculator:
        def __init__(self, base=0):
            self.base = base
    
    # 定义一个独立函数
    def add_to_base(self, value):
        return self.base + value
    
    # 创建实例
    calc = Calculator(10)
    
    # 将函数绑定为实例方法
    calc.add = types.MethodType(add_to_base, calc)
    
    # 测试绑定的方法
    print(f"   calc.base = {calc.base}")
    print(f"   calc.add(5) = {calc.add(5)}")
    
    # 也可以绑定为类方法
    @classmethod
    def class_add(cls, a, b):
        return a + b
    
    # 绑定到类
    Calculator.class_add = class_add
    print(f"   Calculator.class_add(10, 20) = {Calculator.class_add(10, 20)}")
    
    print("\n3. 创建自定义模块")
    print("   使用types.ModuleType可以动态创建模块")
    
    # 创建一个新模块
    my_module = types.ModuleType("custom_module")
    
    # 向模块添加属性和函数
    my_module.__doc__ = "这是一个动态创建的模块"
    my_module.VERSION = "1.0.0"
    
    # 添加函数到模块
    def greeting(name):
        return f"Hello, {name}!"
    
    my_module.greeting = greeting
    
    # 测试模块功能
    print(f"   模块名称: {my_module.__name__}")
    print(f"   模块文档: {my_module.__doc__}")
    print(f"   模块版本: {my_module.VERSION}")
    print(f"   模块函数调用: {my_module.greeting('Alice')}")
    
    print("\n4. 创建带有闭包的函数")
    print("   可以创建带有闭包的函数，捕获外部变量")
    
    # 定义一个创建函数的函数（闭包）
    def make_multiplier(factor):
        def multiplier(x):
            return x * factor
        return multiplier
    
    # 创建一个乘法函数
    double = make_multiplier(2)
    triple = make_multiplier(3)
    
    # 检查闭包
    print(f"   double(5) = {double(5)}")
    print(f"   triple(5) = {triple(5)}")
    print(f"   double函数有闭包: {double.__closure__ is not None}")
    if double.__closure__:
        print(f"   闭包变量值: {double.__closure__[0].cell_contents}")
    
    print("\n5. 创建自定义代码对象")
    print("   高级用法：使用compile创建代码对象，然后创建函数")
    
    # 使用compile创建代码对象
    code_source = "def dynamic_function(a, b):\n    return a * b"
    code_object = compile(code_source, '<string>', 'exec')
    
    # 创建一个局部命名空间
    local_namespace = {}
    
    # 执行代码对象来定义函数
    exec(code_object, globals(), local_namespace)
    
    # 获取定义的函数
    dynamic_func = local_namespace['dynamic_function']
    
    # 测试函数
    print(f"   动态定义的函数: {dynamic_func(4, 5)}")
    print(f"   函数类型: {type(dynamic_func)}")
    
    print("\n6. 动态修改函数属性")
    print("   使用types模块相关功能可以动态修改函数的属性")
    
    # 定义一个函数
    def example_function(x):
        return x * x
    
    # 修改函数名称
    example_function.__name__ = "squared_function"
    
    # 添加文档字符串
    example_function.__doc__ = "计算输入值的平方"
    
    # 添加自定义属性
    example_function.version = "1.0"
    example_function.author = "Python Programmer"
    
    # 测试修改后的函数
    print(f"   修改后的函数名: {example_function.__name__}")
    print(f"   函数文档: {example_function.__doc__}")
    print(f"   函数版本: {example_function.version}")
    print(f"   函数作者: {example_function.author}")
    print(f"   函数调用: {example_function(7)}")
    
    print("\n7. 创建自定义装饰器")
    print("   使用types模块可以创建更灵活的装饰器")
    
    def log_calls(func):
        """记录函数调用的装饰器"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"调用 {func.__name__} 与参数: {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} 返回: {result}")
            return result
        return wrapper
    
    # 应用装饰器
    @log_calls
    def add(a, b):
        return a + b
    
    # 测试装饰后的函数
    print(f"   调用装饰后的函数:")
    result = add(3, 4)
    print(f"   结果: {result}")
    
    # 检查装饰器是否保留了原始函数的元数据
    print(f"   装饰后函数名: {add.__name__}")
    
    print("\n8. 动态创建类型")
    print("   使用types.new_class可以动态创建新的类型")
    
    # 使用types.new_class动态创建类（Python 3.3+）
    try:
        # 定义类主体
        class_body = {
            '__init__': lambda self, x: setattr(self, 'value', x),
            'get_value': lambda self: self.value,
            '__str__': lambda self: f"MyDynamicClass({self.value})"
        }
        
        # 创建动态类
        MyDynamicClass = types.new_class(
            'MyDynamicClass',  # 类名
            (),  # 基类
            {},  # 关键字参数
            lambda ns: ns.update(class_body)  # 类主体更新函数
        )
        
        # 创建实例并测试
        instance = MyDynamicClass(42)
        print(f"   动态创建的类: {instance}")
        print(f"   实例方法调用: {instance.get_value()}")
        print(f"   实例类型: {type(instance)}")
        
    except AttributeError:
        print("   types.new_class在当前Python版本中不可用（需要Python 3.3+）")
        # 替代方法：使用type()函数创建类
        MyDynamicClass = type(
            'MyDynamicClass',  # 类名
            (),  # 基类
            {
                '__init__': lambda self, x: setattr(self, 'value', x),
                'get_value': lambda self: self.value,
                '__str__': lambda self: f"MyDynamicClass({self.value})"
            }  # 类字典
        )
        
        instance = MyDynamicClass(42)
        print(f"   使用type()替代方法创建的类: {instance}")
        print(f"   实例方法调用: {instance.get_value()}")

# 运行自定义类型创建演示
create_custom_types()
print()

# 4. 类型检查和验证
print("=== 4. 类型检查和验证 ===")

def type_checking():
    """展示如何使用types模块进行高级类型检查和验证"""
    import types
    import inspect
    
    print("1. 精确的类型区分")
    print("   使用types模块可以区分不同种类的可调用对象")
    
    # 定义各种类型的可调用对象
    def regular_function():
        """普通函数"""
        pass
    
    lambda_func = lambda x: x * 2
    
    class MyClass:
        def instance_method(self):
            pass
        
        @staticmethod
        def static_method():
            pass
        
        @classmethod
        def class_method(cls):
            pass
    
    # 创建实例
    obj = MyClass()
    
    # 创建一个装饰器来检查参数类型
    def check_callable_type(func):
        """检查可调用对象的具体类型"""
        if isinstance(func, types.FunctionType):
            if func.__name__ == '<lambda>':
                return "Lambda函数"
            return "普通函数"
        elif isinstance(func, types.MethodType):
            return "实例方法"
        elif isinstance(func, types.BuiltinFunctionType):
            return "内置函数"
        elif isinstance(func, types.BuiltinMethodType):
            return "内置方法"
        else:
            return f"其他类型: {type(func).__name__}"
    
    # 测试各种可调用对象的类型
    callables_to_check = [
        regular_function,
        lambda_func,
        obj.instance_method,
        MyClass.static_method,
        MyClass.class_method,
        len,
        str.upper
    ]
    
    print("   \n可调用对象类型检查结果:")
    for callable_obj in callables_to_check:
        if hasattr(callable_obj, '__name__'):
            name = callable_obj.__name__
        else:
            name = str(callable_obj)
        print(f"   {name}: {check_callable_type(callable_obj)}")
    
    print("\n2. 函数签名检查")
    print("   使用inspect模块和types模块可以检查函数的签名和参数")
    
    def complex_function(a, b=10, *args, **kwargs):
        """一个带有各种参数类型的复杂函数"""
        return a + b + sum(args)
    
    # 获取函数签名
    signature = inspect.signature(complex_function)
    
    # 分析函数对象
    print(f"   函数名: {complex_function.__name__}")
    print(f"   函数文档: {complex_function.__doc__}")
    print(f"   函数签名: {signature}")
    print(f"   函数参数数量: {complex_function.__code__.co_argcount}")
    print(f"   函数参数名称: {complex_function.__code__.co_varnames[:complex_function.__code__.co_argcount]}")
    print(f"   函数是否有*args: {complex_function.__code__.co_flags & inspect.CO_VARARGS != 0}")
    print(f"   函数是否有**kwargs: {complex_function.__code__.co_flags & inspect.CO_VARKEYWORDS != 0}")
    
    print("\n3. 创建类型验证装饰器")
    print("   使用类型检查来创建参数验证装饰器")
    
    def validate_types(**type_checks):
        """验证函数参数类型的装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 获取函数参数
                arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
                
                # 验证位置参数
                for i, (name, value) in enumerate(zip(arg_names, args)):
                    if name in type_checks and not isinstance(value, type_checks[name]):
                        raise TypeError(f"参数 '{name}' 应该是 {type_checks[name].__name__} 类型，而不是 {type(value).__name__}")
                
                # 验证关键字参数
                for name, value in kwargs.items():
                    if name in type_checks and not isinstance(value, type_checks[name]):
                        raise TypeError(f"参数 '{name}' 应该是 {type_checks[name].__name__} 类型，而不是 {type(value).__name__}")
                
                # 调用原始函数
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    # 应用类型验证装饰器
    @validate_types(a=int, b=(int, float))
    def add_numbers(a, b=0):
        return a + b
    
    # 测试有效和无效的调用
    print(f"   有效的调用: add_numbers(5, 3.5) = {add_numbers(5, 3.5)}")
    
    try:
        add_numbers("5", 3)
    except TypeError as e:
        print(f"   无效的调用被捕获: {e}")
    
    print("\n4. 动态类型检查")
    print("   在运行时动态检查对象的类型和属性")
    
    # 定义一个类型检查函数
    def check_object_type(obj):
        """检查对象的类型和关键属性"""
        print(f"   对象: {obj}")
        print(f"   类型: {type(obj)}")
        print(f"   是函数: {isinstance(obj, types.FunctionType)}")
        print(f"   是方法: {isinstance(obj, types.MethodType)}")
        print(f"   是模块: {isinstance(obj, types.ModuleType)}")
        print(f"   是实例方法: {hasattr(obj, '__self__')}")
        
        if hasattr(obj, '__name__'):
            print(f"   名称: {obj.__name__}")
        
        if hasattr(obj, '__code__'):
            print(f"   代码对象: {obj.__code__}")
            print(f"   参数数量: {obj.__code__.co_argcount}")
    
    # 测试不同类型的对象
    print("   \n检查普通函数:")
    check_object_type(regular_function)
    
    print("   \n检查实例方法:")
    check_object_type(obj.instance_method)
    
    print("   \n检查模块:")
    check_object_type(types)
    
    print("\n5. 检查生成器和迭代器类型")
    print("   使用types模块检查生成器和迭代器的具体类型")
    
    # 定义一个生成器函数
    def my_generator():
        for i in range(3):
            yield i
    
    # 创建一个迭代器
    my_iterator = iter([1, 2, 3])
    
    # 创建一个生成器对象
    gen_obj = my_generator()
    
    # 检查类型
    print(f"   生成器函数类型: {type(my_generator)}")
    print(f"   生成器对象类型: {type(gen_obj)}")
    print(f"   是生成器类型: {isinstance(gen_obj, types.GeneratorType)}")
    print(f"   迭代器类型: {type(my_iterator)}")
    print(f"   是迭代器: {isinstance(my_iterator, collections.abc.Iterator)}")
    print(f"   列表是可迭代的: {isinstance([], collections.abc.Iterable)}")
    print(f"   列表不是迭代器: {isinstance([], collections.abc.Iterator)}")
    
    print("\n6. 检查特殊方法的存在性")
    print("   检查对象是否实现了特定的特殊方法")
    
    # 定义具有不同特殊方法的类
    class BasicClass:
        pass
    
    class CallableClass:
        def __call__(self):
            return "Called!"
    
    class ContainerClass:
        def __init__(self):
            self.items = []
        
        def __getitem__(self, index):
            return self.items[index]
        
        def __len__(self):
            return len(self.items)
    
    # 检查特殊方法
    def check_special_methods(obj):
        """检查对象是否实现了常见的特殊方法"""
        methods_to_check = ['__call__', '__getitem__', '__len__', '__iter__', '__next__']
        print(f"   检查 {type(obj).__name__} 的特殊方法:")
        for method in methods_to_check:
            if hasattr(obj, method):
                print(f"     ✓ 实现了 {method}")
            else:
                print(f"     ✗ 未实现 {method}")
    
    # 测试不同的类
    print("   \n")
    check_special_methods(BasicClass())
    print("   \n")
    check_special_methods(CallableClass())
    print("   \n")
    check_special_methods(ContainerClass())
    
    # 测试可调用性
    callable_obj = CallableClass()
    print(f"   callable_obj() = {callable_obj()}")

# 导入需要的模块
import functools
import collections.abc

# 运行类型检查演示
type_checking()
print()

# 5. 高级应用示例
print("=== 5. 高级应用示例 ===")

def advanced_examples():
    """types模块的高级应用示例"""
    import types
    import inspect
    import functools
    import sys
    import gc
    
    print("1. 动态代码注入")
    print("   使用types模块动态修改和扩展代码功能")
    
    # 定义一个简单的类
    class Person:
        def __init__(self, name):
            self.name = name
        
        def greet(self):
            return f"Hello, my name is {self.name}"
    
    # 动态添加新方法
    def say_hello(self, other_name):
        return f"Hello {other_name}, I'm {self.name}"
    
    # 将新方法绑定到类
    Person.say_hello = say_hello
    
    # 创建实例并测试
    person = Person("Alice")
    print(f"   原始方法: {person.greet()}")
    print(f"   动态添加的方法: {person.say_hello('Bob')}")
    
    print("\n2. 函数包装与元编程")
    print("   使用types模块创建函数包装器和代理")
    
    # 创建一个函数包装器类
    class FunctionWrapper:
        def __init__(self, func):
            self.original_func = func
            # 复制原始函数的元数据
            functools.update_wrapper(self, func)
        
        def __call__(self, *args, **kwargs):
            print(f"调用被包装的函数: {self.original_func.__name__}")
            result = self.original_func(*args, **kwargs)
            print(f"函数返回: {result}")
            return result
        
        def __get__(self, instance, owner):
            """支持将包装器用作方法"""
            if instance is None:
                return self
            return types.MethodType(self, instance)
    
    # 应用包装器
    @FunctionWrapper
    def add(a, b):
        return a + b
    
    # 测试函数包装器
    print(f"   函数包装器调用: {add(3, 4)}")
    
    # 在类中使用
    class Calculator:
        @FunctionWrapper
        def multiply(self, a, b):
            return a * b
    
    calc = Calculator()
    print(f"   方法包装器调用: {calc.multiply(5, 6)}")
    
    print("\n3. 模块猴子补丁")
    print("   使用types模块修改现有模块的功能")
    
    # 假设我们想要修改math模块的sqrt函数
    import math
    
    # 保存原始函数
    original_sqrt = math.sqrt
    
    # 定义替代函数
    def patched_sqrt(x):
        print(f"计算平方根: {x}")
        result = original_sqrt(x)
        return result
    
    # 替换模块中的函数
    math.sqrt = patched_sqrt
    
    # 测试补丁后的函数
    print(f"   补丁后的sqrt(16) = {math.sqrt(16)}")
    
    # 恢复原始函数
    math.sqrt = original_sqrt
    
    print("\n4. 动态代码分析器")
    print("   使用types和inspect模块创建代码分析器")
    
    # 创建一个简单的代码分析器
    def analyze_function(func):
        """分析函数并返回详细信息"""
        if not isinstance(func, types.FunctionType):
            return "不是一个函数对象"
        
        result = {
            'name': func.__name__,
            'docstring': func.__doc__,
            'module': func.__module__,
            'file': inspect.getfile(func),
            'line_number': inspect.getsourcelines(func)[1],
            'args': inspect.signature(func).parameters,
            'arg_count': func.__code__.co_argcount,
            'varargs': bool(func.__code__.co_flags & inspect.CO_VARARGS),
            'varkw': bool(func.__code__.co_flags & inspect.CO_VARKEYWORDS),
            'local_variables': func.__code__.co_varnames,
            'constants': func.__code__.co_consts
        }
        
        return result
    
    # 分析一个函数
    def example_analyze(a, b=10, *args, **kwargs):
        """这是一个示例函数，用于演示代码分析。"""
        c = a + b
        d = sum(args)
        return c + d
    
    # 获取分析结果
    analysis = analyze_function(example_analyze)
    
    # 打印分析结果
    print(f"   函数分析结果:")
    print(f"   函数名: {analysis['name']}")
    print(f"   文档字符串: {analysis['docstring']}")
    print(f"   参数数量: {analysis['arg_count']}")
    print(f"   是否有*args: {analysis['varargs']}")
    print(f"   是否有**kwargs: {analysis['varkw']}")
    print(f"   局部变量: {analysis['local_variables']}")
    print(f"   常量: {analysis['constants']}")
    
    print("\n5. 动态类型注册系统")
    print("   使用types模块创建动态类型注册和查找系统")
    
    # 创建一个类型注册系统
    class TypeRegistry:
        def __init__(self):
            self._registry = {}
        
        def register(self, name, type_obj):
            """注册一个类型"""
            self._registry[name] = type_obj
            return type_obj
        
        def get(self, name):
            """获取注册的类型"""
            return self._registry.get(name)
        
        def list_types(self):
            """列出所有注册的类型"""
            return list(self._registry.keys())
    
    # 创建注册表实例
    registry = TypeRegistry()
    
    # 注册一些类型
    registry.register('int_list', list)
    registry.register('string_dict', dict)
    registry.register('custom_type', Person)
    
    # 动态创建并注册一个类型
    @registry.register('dynamic_type')
    class DynamicType:
        def __init__(self, value):
            self.value = value
        
        def __str__(self):
            return f"DynamicType({self.value})"
    
    # 测试类型注册系统
    print(f"   注册的类型: {registry.list_types()}")
    
    # 使用注册的类型
    int_list_type = registry.get('int_list')
    my_list = int_list_type([1, 2, 3])
    print(f"   使用注册类型创建: {my_list} (类型: {type(my_list).__name__})")
    
    dynamic_type = registry.get('dynamic_type')
    my_dynamic = dynamic_type(42)
    print(f"   动态类型实例: {my_dynamic}")
    
    print("\n6. 函数依赖注入容器")
    print("   使用types模块创建简单的依赖注入系统")
    
    # 创建一个简单的依赖注入容器
    class DependencyContainer:
        def __init__(self):
            self._dependencies = {}
        
        def register(self, name, dependency):
            """注册一个依赖"""
            self._dependencies[name] = dependency
        
        def inject(self, func):
            """注入依赖到函数参数"""
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 获取函数签名
                sig = inspect.signature(func)
                params = sig.parameters
                
                # 注入依赖
                for name, param in params.items():
                    if name in self._dependencies and name not in kwargs:
                        kwargs[name] = self._dependencies[name]
                
                # 调用函数
                return func(*args, **kwargs)
            return wrapper
    
    # 创建容器实例
    container = DependencyContainer()
    
    # 注册一些依赖
    class Logger:
        def log(self, message):
            return f"[LOG] {message}"
    
    class Database:
        def query(self, sql):
            return f"执行SQL: {sql}"
    
    container.register('logger', Logger())
    container.register('db', Database())
    
    # 使用依赖注入
    @container.inject
    def process_data(data, logger, db):
        logger_msg = logger.log(f"处理数据: {data}")
        db_msg = db.query(f"SELECT * FROM table WHERE data = '{data}'")
        return f"{logger_msg}\n{db_msg}"
    
    # 测试依赖注入
    result = process_data("test_data")
    print(f"   依赖注入结果:\n   {result}")
    
    print("\n7. 动态代理和装饰器工厂")
    print("   使用types模块创建动态代理和装饰器工厂")
    
    # 创建一个装饰器工厂
    def create_decorator(prefix="[DEBUG]"):
        """创建一个带有自定义前缀的日志装饰器"""
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                print(f"{prefix} 调用 {func.__name__} 与参数: {args}, {kwargs}")
                result = func(*args, **kwargs)
                print(f"{prefix} {func.__name__} 返回: {result}")
                return result
            return wrapper
        return decorator
    
    # 创建特定的装饰器
    info_decorator = create_decorator("[INFO]")
    error_decorator = create_decorator("[ERROR]")
    
    # 应用不同的装饰器
    @info_decorator
    def calculate_sum(a, b):
        return a + b
    
    @error_decorator
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "除数不能为零"
    
    # 测试装饰器
    print(f"   测试INFO装饰器:")
    calculate_sum(10, 20)
    
    print(f"   测试ERROR装饰器:")
    divide(10, 2)
    divide(10, 0)
    
    print("\n8. 运行时函数监控")
    print("   使用types模块监控函数调用和性能")
    
    # 创建一个性能监控装饰器
    import time
    
    class FunctionMonitor:
        def __init__(self):
            self.stats = {}
        
        def monitor(self, func):
            """监控函数的调用次数、执行时间等"""
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                # 初始化函数统计信息
                if func.__name__ not in self.stats:
                    self.stats[func.__name__] = {
                        'calls': 0,
                        'total_time': 0,
                        'min_time': float('inf'),
                        'max_time': 0
                    }
                
                # 记录开始时间
                start_time = time.time()
                
                # 调用函数
                try:
                    result = func(*args, **kwargs)
                    return result
                finally:
                    # 计算执行时间
                    exec_time = time.time() - start_time
                    
                    # 更新统计信息
                    stats = self.stats[func.__name__]
                    stats['calls'] += 1
                    stats['total_time'] += exec_time
                    stats['min_time'] = min(stats['min_time'], exec_time)
                    stats['max_time'] = max(stats['max_time'], exec_time)
            
            return wrapper
        
        def get_stats(self):
            """获取所有函数的统计信息"""
            return self.stats
        
        def print_stats(self):
            """打印统计信息"""
            print("   函数监控统计:")
            for func_name, stats in self.stats.items():
                avg_time = stats['total_time'] / stats['calls'] if stats['calls'] > 0 else 0
                print(f"   {func_name}:")
                print(f"     调用次数: {stats['calls']}")
                print(f"     总执行时间: {stats['total_time']:.6f} 秒")
                print(f"     平均执行时间: {avg_time:.6f} 秒")
                print(f"     最小执行时间: {stats['min_time']:.6f} 秒")
                print(f"     最大执行时间: {stats['max_time']:.6f} 秒")
    
    # 创建监控器实例
    monitor = FunctionMonitor()
    
    # 监控一些函数
    @monitor.monitor
    def slow_function():
        """模拟一个耗时操作"""
        time.sleep(0.01)  # 模拟工作负载
        return "完成"
    
    @monitor.monitor
    def fast_function():
        """模拟一个快速操作"""
        return sum(range(1000))
    
    # 调用函数多次
    for _ in range(5):
        slow_function()
        fast_function()
    
    # 打印统计信息
    monitor.print_stats()

# 运行高级应用示例
advanced_examples()
print()

# 6. 性能优化和注意事项
print("=== 6. 性能优化和注意事项 ===")

def performance_considerations():
    """types模块使用的性能优化和注意事项"""
    import time
    
    print("1. 类型检查性能对比")
    print("   比较不同类型检查方法的性能")
    
    # 测试对象
    def test_func():
        pass
    
    # 导入需要的模块
    import types
    
    # 性能测试函数
    def time_check(check_func, iterations=1000000):
        """测量函数执行时间"""
        start_time = time.time()
        for _ in range(iterations):
            check_func()
        end_time = time.time()
        return end_time - start_time
    
    # 测试不同的类型检查方法
    isinstance_time = time_check(lambda: isinstance(test_func, types.FunctionType))
    type_time = time_check(lambda: type(test_func) is types.FunctionType)
    name_time = time_check(lambda: test_func.__class__.__name__ == 'function')
    
    print(f"   isinstance检查: {isinstance_time:.6f} 秒")
    print(f"   type() 比较: {type_time:.6f} 秒")
    print(f"   __class__.__name__ 比较: {name_time:.6f} 秒")
    
    print("\n2. 函数创建性能")
    print("   动态创建函数与直接定义函数的性能对比")
    
    # 测试动态函数创建
    def dynamic_function_creation():
        # 定义一个模板函数
        def template(x, y):
            return x + y
        
        # 获取代码对象
        code_obj = template.__code__
        
        # 创建新函数
        return types.FunctionType(code_obj, globals())
    
    # 测量动态函数创建时间
    creation_time = time_check(dynamic_function_creation, 10000)
    print(f"   动态创建10,000个函数: {creation_time:.6f} 秒")
    print(f"   平均每个函数创建时间: {(creation_time / 10000) * 1000000:.2f} 微秒")
    
    print("\n3. 装饰器性能影响")
    print("   测量装饰器对函数性能的影响")
    
    # 普通函数
    def normal_function(x):
        return x * x
    
    # 带装饰器的函数
    import functools
    
    def simple_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    @simple_decorator
    def decorated_function(x):
        return x * x
    
    # 测量性能
    normal_time = time_check(lambda: normal_function(5))
    decorated_time = time_check(lambda: decorated_function(5))
    
    overhead = ((decorated_time - normal_time) / normal_time) * 100
    print(f"   普通函数: {normal_time:.6f} 秒")
    print(f"   装饰函数: {decorated_time:.6f} 秒")
    print(f"   性能开销: {overhead:.2f}%")
    
    print("\n4. 注意事项")
    print("   使用types模块时的重要注意事项")
    
    print("   1. 版本兼容性")
    print("      - types模块中的某些属性和函数在不同Python版本间可能有所不同")
    print("      - 例如，types.ClassType在Python 3中已被移除，types.LambdaType已被合并到types.FunctionType")
    print("      - 建议使用hasattr()检查属性是否存在，或使用try-except块处理可能的AttributeError")
    
    print("   \n2. 元编程的复杂性")
    print("      - 过度使用元编程和动态类型操作会使代码难以理解和维护")
    print("      - 应该优先考虑清晰性和可读性，仅在必要时使用高级元编程技术")
    print("      - 务必为元编程代码编写充分的文档和测试")
    
    print("   \n3. 性能考虑")
    print("      - 动态创建函数、方法和类型比静态定义要慢")
    print("      - 频繁的类型检查（如在循环中）可能会影响性能")
    print("      - 对于性能关键路径，考虑缓存类型检查结果或使用其他优化技术")
    
    print("   \n4. 调试困难")
    print("      - 动态生成的代码可能缺乏有用的堆栈跟踪信息")
    print("      - 使用动态类型操作时，错误可能更难追踪")
    print("      - 建议添加详细的日志记录以帮助调试")
    
    print("   \n5. 安全考虑")
    print("      - 使用exec()或eval()创建动态代码时要格外小心，避免执行不可信的代码")
    print("      - 模块猴子补丁可能导致意外的副作用，尤其是在多线程环境中")
    print("      - 避免修改内置模块或类型的行为，这可能会影响系统的其他部分")
    
    print("   \n6. 内存管理")
    print("      - 动态创建的函数和类型不会自动清理，可能导致内存泄漏")
    print("      - 特别是当它们形成循环引用时，可能需要显式的垃圾回收")
    print("      - 使用weakref模块处理可能的循环引用问题")
    
    print("   \n7. 最佳实践")
    print("      - 仅在必要时使用types模块进行高级类型操作")
    print("      - 优先使用isinstance()进行类型检查，而不是直接比较类型对象")
    print("      - 使用functools.wraps保留装饰函数的元数据")
    print("      - 为动态生成的代码提供清晰的文档和适当的名称")
    print("      - 在生产环境中避免过度使用元编程技术")
    
    print("   \n8. 常见陷阱")
    print("      - 混淆函数、方法和其他可调用对象的类型")
    print("      - 忽略闭包变量的作用域问题")
    print("      - 忘记在动态创建的函数中正确设置全局命名空间")
    print("      - 过度使用装饰器导致的性能下降")
    print("      - 在不同Python版本间使用不兼容的类型属性")

# 导入需要的模块
import types

# 运行性能优化和注意事项
performance_considerations()
print()

# 7. 输入输出示例
print("=== 7. 输入输出示例 ===")

def types_io_examples():
    """types模块的输入输出示例"""
    import types
    
    print("示例1: 基本类型检查")
    print("输入:")
    print("  import types")
    print("  ")
    print("  def my_function():")
    print("      pass")
    print("  ")
    print("  class MyClass:")
    print("      def my_method(self):")
    print("          pass")
    print("  ")
    print("  obj = MyClass()")
    print("  print(isinstance(my_function, types.FunctionType))")
    print("  print(isinstance(obj.my_method, types.MethodType))")
    print("  print(isinstance(len, types.BuiltinFunctionType))")
    print("  print(isinstance(MyClass, types.TypeType))")
    
    print("\n输出:")
    print("  True")
    print("  True")
    print("  True")
    print("  True")
    
    print("\n示例2: 动态创建函数")
    print("输入:")
    print("  import types")
    print("  ")
    print("  # 定义一个模板函数")
    print("  def template(x, y):")
    print("      return x * y")
    print("  ")
    print("  # 获取代码对象")
    print("  code_obj = template.__code__")
    print("  ")
    print("  # 创建新函数")
    print("  multiply = types.FunctionType(code_obj, globals(), name='multiply')")
    print("  ")
    print("  # 测试新函数")
    print("  print(multiply.__name__)")
    print("  print(multiply(5, 3))")
    
    print("\n输出:")
    print("  multiply")
    print("  15")
    
    print("\n示例3: 动态添加方法到类")
    print("输入:")
    print("  import types")
    print("  ")
    print("  class Calculator:")
    print("      def __init__(self, value=0):")
    print("          self.value = value")
    print("  ")
    print("  # 定义一个独立函数")
    print("  def add(self, x):")
    print("      self.value += x")
    print("      return self.value")
    print("  ")
    print("  # 将函数绑定为实例方法")
    print("  calc = Calculator(10)")
    print("  calc.add = types.MethodType(add, calc)")
    print("  ")
    print("  # 测试绑定的方法")
    print("  print(calc.add(5))")
    print("  print(calc.add(7))")
    
    print("\n输出:")
    print("  15")
    print("  22")
    
    print("\n示例4: 动态创建模块")
    print("输入:")
    print("  import types")
    print("  ")
    print("  # 创建一个新模块")
    print("  my_module = types.ModuleType('mymath')")
    print("  ")
    print("  # 添加函数和属性")
    print("  my_module.__doc__ = '自定义数学模块'")
    print("  my_module.PI = 3.14159")
    print("  ")
    print("  def add(a, b):")
    print("      return a + b")
    print("  ")
    print("  def subtract(a, b):")
    print("      return a - b")
    print("  ")
    print("  # 将函数添加到模块")
    print("  my_module.add = add")
    print("  my_module.subtract = subtract")
    print("  ")
    print("  # 使用模块")
    print("  print(my_module.__name__)")
    print("  print(my_module.PI)")
    print("  print(my_module.add(10, 5))")
    print("  print(my_module.subtract(10, 5))")
    
    print("\n输出:")
    print("  mymath")
    print("  3.14159")
    print("  15")
    print("  5")
    
    print("\n示例5: 检查生成器和迭代器类型")
    print("输入:")
    print("  import types")
    print("  import collections.abc")
    print("  ")
    print("  # 定义生成器函数")
    print("  def my_generator():")
    print("      for i in range(3):")
    print("          yield i")
    print("  ")
    print("  # 创建生成器对象")
    print("  gen = my_generator()")
    print("  ")
    print("  # 创建迭代器")
    print("  it = iter([1, 2, 3])")
    print("  ")
    print("  # 检查类型")
    print("  print(isinstance(gen, types.GeneratorType))")
    print("  print(isinstance(gen, collections.abc.Iterator))")
    print("  print(isinstance(it, collections.abc.Iterator))")
    print("  print(isinstance([], collections.abc.Iterable))")
    print("  print(isinstance([], collections.abc.Iterator))")
    
    print("\n输出:")
    print("  True")
    print("  True")
    print("  True")
    print("  True")
    print("  False")

# 运行输入输出示例
types_io_examples()
print()

# 8. 总结和导入指南
print("=== 8. 总结和导入指南 ===")

def types_summary():
    """types模块总结和导入指南"""
    
    print("1. types模块核心功能总结")
    print("   - 提供了Python内置类型的类型对象，用于精确的类型检查")
    print("   - 支持动态创建和修改函数、方法、模块和类型")
    print("   - 提供了访问Python内部类型系统的能力")
    print("   - 支持高级元编程和类型操作")
    print("   - 可以区分不同类型的可调用对象（函数、方法、内置函数等）")
    
    print("\n2. 常见使用场景")
    print("   - 需要精确区分函数、方法和其他可调用对象时")
    print("   - 动态扩展现有类或模块的功能")
    print("   - 创建自定义类型系统或框架")
    print("   - 实现高级装饰器和代理模式")
    print("   - 进行代码分析和检查")
    print("   - 开发元编程工具和框架")
    
    print("\n3. 完整导入指南")
    print("   基本导入:")
    print("   ```python")
    print("   import types")
    print("   ```")
    
    print("\n   特定函数或类型导入:")
    print("   ```python")
    print("   from types import FunctionType, MethodType, GeneratorType")
    print("   from types import ModuleType, CodeType, FrameType")
    print("   ```")
    
    print("\n   常用导入组合:")
    print("   ```python")
    print("   # 用于类型检查")
    print("   import types")
    print("   import inspect")
    print("   ")
    print("   # 用于元编程")
    print("   import types")
    print("   import functools")
    print("   import inspect")
    print("   ")
    print("   # 用于类型系统和接口检查")
    print("   import types")
    print("   import collections.abc")
    print("   ```")
    
    print("\n4. 版本兼容性")
    print("   - types模块在Python 2.x和3.x中都可用，但具体内容有所不同")
    print("   - Python 3中移除了一些Python 2中的类型，如ClassType")
    print("   - Python 3中LambdaType与FunctionType合并")
    print("   - Python 3.3+引入了types.new_class()用于动态创建类")
    print("   - Python 3.5+引入了更多协程相关的类型")
    
    print("\n5. 最佳实践")
    print("   - 优先使用isinstance()进行类型检查，而不是直接比较类型对象")
    print("   - 仅在必要时使用types模块进行高级类型操作")
    print("   - 使用functools.wraps保留装饰函数的元数据")
    print("   - 避免过度使用元编程，以保持代码的可读性和可维护性")
    print("   - 在生产环境中谨慎使用动态类型修改和猴子补丁")
    print("   - 为元编程代码编写充分的文档和测试")
    print("   - 注意版本兼容性问题，避免使用在不同Python版本中行为不一致的功能")
    
    print("\n6. 相关模块")
    print("   - inspect: 提供更高级的检查活动对象的功能")
    print("   - functools: 提供高阶函数和可调用对象的操作工具")
    print("   - collections.abc: 提供抽象基类，用于接口和类型检查")
    print("   - weakref: 用于处理可能的循环引用问题")
    print("   - importlib: 用于动态导入模块")
    
    print("\n7. 运行本模块")
    print("   本模块包含了types模块的全面介绍和示例代码，")
    print("   可以直接运行查看所有示例的输出。每个部分都有详细的解释和示例，")
    print("   涵盖了从基本使用到高级应用的各个方面。")

# 运行总结
import collections.abc  # 导入需要的模块
types_summary()
print("\n=== types模块文档完成 ===")