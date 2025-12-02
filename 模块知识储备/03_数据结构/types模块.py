# types模块 - Python标准库中的类型创建与检查

'''
types模块提供了用于动态创建类型和检查类型的函数和类，
允许程序员在运行时创建新的类型和检查对象的类型信息。
它包含了内置类型的引用、函数类型、生成器类型等各种类型定义。
'''

import types
import inspect
from typing import Any, Callable, List, Dict, Tuple, Set, Optional, Union, TypeVar, Generic, Type

# 核心功能介绍
print("=== types模块核心功能 ===")
print("types模块提供了以下核心功能：")
print("1. 提供内置类型的引用，用于类型检查")
print("2. 允许动态创建新的函数、方法和类型")
print("3. 提供对生成器、协程等特殊类型的支持")
print("4. 允许检查对象的底层类型信息")
print("5. 支持动态代码执行和元编程")
print("6. 提供函数签名和参数检查功能")

# 1. 内置类型引用
def show_builtin_types():
    """展示types模块中的内置类型引用"""
    print("\n=== 1. 内置类型引用 ===")
    print("types模块提供了内置类型的引用，可以用于精确的类型检查")
    
    # 1.1 基本类型引用
    print("\n1.1 基本类型引用")
    
    # 创建不同类型的对象
    obj_types = [
        (100, "整数"),
        (3.14, "浮点数"),
        ("hello", "字符串"),
        ([1, 2, 3], "列表"),
        ((1, 2, 3), "元组"),
        ({1, 2, 3}, "集合"),
        ({"a": 1}, "字典"),
        (lambda x: x, "函数"),
        (type(1), "类型对象")
    ]
    
    print("对象类型引用检查:")
    for obj, desc in obj_types:
        # 使用type()获取类型
        obj_type = type(obj)
        print(f"  {desc}的类型: {obj_type}")
        
        # 某些特殊类型的检查
        if isinstance(obj, list):
            print(f"    是否为列表类型: {obj_type is list}")
            print(f"    使用types模块: {obj_type is types.ListType}")
        elif isinstance(obj, dict):
            print(f"    是否为字典类型: {obj_type is dict}")
            print(f"    使用types模块: {obj_type is types.DictType}")
        elif isinstance(obj, tuple):
            print(f"    是否为元组类型: {obj_type is tuple}")
            print(f"    使用types模块: {obj_type is types.TupleType}")
        elif callable(obj):
            print(f"    是否为函数类型: {obj_type is types.FunctionType}")
    
    # 1.2 特殊类型引用
    print("\n1.2 特殊类型引用")
    
    # 定义一些特殊类型的对象
    def regular_func(x, y):
        return x + y
    
    class MyClass:
        def method(self, x):
            return x * 2
        
        @staticmethod
        def static_method(x):
            return x * 3
        
        @classmethod
        def class_method(cls, x):
            return x * 4
    
    # 实例化类
    instance = MyClass()
    
    # 生成器函数
    def gen_func():
        yield 1
        yield 2
    
    generator = gen_func()
    
    # 协程函数 (Python 3.5+)
    async def coro_func():
        await asyncio.sleep(0.1) if 'asyncio' in globals() else None
        return "coroutine result"
    
    # 特殊类型检查
    special_types = [
        (regular_func, "普通函数", types.FunctionType),
        (instance.method, "实例方法", types.MethodType),
        (MyClass.static_method, "静态方法", types.FunctionType),  # 静态方法实际上是普通函数
        (MyClass.class_method, "类方法", types.MethodType),
        (generator, "生成器", types.GeneratorType),
        (coro_func(), "协程", types.CoroutineType if hasattr(types, 'CoroutineType') else type(coro_func()))
    ]
    
    print("特殊类型引用检查:")
    for obj, desc, expected_type in special_types:
        obj_type = type(obj)
        print(f"  {desc}的类型: {obj_type}")
        try:
            print(f"    是否匹配: {obj_type is expected_type}")
        except TypeError:
            print(f"    类型比较出错，可能是Python版本差异")
    
    # 1.3 检查对象是否为特定类型
    print("\n1.3 检查对象是否为特定类型")
    
    test_objects = [1, "string", [1, 2], {"a": 1}, lambda x: x]
    
    print("使用types模块进行类型检查:")
    for obj in test_objects:
        print(f"  {obj!r}:")
        if isinstance(obj, int):
            print(f"    是整数类型")
        if isinstance(obj, str):
            print(f"    是字符串类型")
        if isinstance(obj, list):
            print(f"    是列表类型")
        if isinstance(obj, dict):
            print(f"    是字典类型")
        if isinstance(obj, types.FunctionType):
            print(f"    是函数类型")

# 2. 动态创建函数
def show_dynamic_function_creation():
    """展示如何使用types模块动态创建函数"""
    print("\n=== 2. 动态创建函数 ===")
    print("types模块允许在运行时动态创建函数对象")
    
    # 2.1 使用types.FunctionType创建函数
    print("\n2.1 使用types.FunctionType创建函数")
    
    # 定义函数的代码
    def add_impl(a, b):
        return a + b
    
    # 获取函数的代码对象
    add_code = add_impl.__code__
    
    # 获取函数的全局命名空间
    add_globals = add_impl.__globals__
    
    # 创建新的函数
    dynamic_add = types.FunctionType(
        add_code,           # 代码对象
        add_globals,        # 全局命名空间
        name="dynamic_add", # 函数名
        argdefs=(),         # 默认参数
        closure=None        # 闭包
    )
    
    # 测试动态创建的函数
    result = dynamic_add(5, 3)
    print(f"动态创建的函数dynamic_add(5, 3) = {result}")
    print(f"函数名称: {dynamic_add.__name__}")
    print(f"函数签名: {inspect.signature(dynamic_add)}")
    
    # 2.2 使用exec和compile动态创建函数
    print("\n2.2 使用exec和compile动态创建函数")
    
    # 定义函数的代码字符串
    func_code_str = """
def multiply(x, y):
    """乘法函数"""
    return x * y
"""
    
    # 创建一个命名空间
    local_namespace = {}
    
    # 编译并执行代码
    exec(func_code_str, globals(), local_namespace)
    
    # 获取动态创建的函数
    dynamic_multiply = local_namespace["multiply"]
    
    # 测试函数
    result = dynamic_multiply(4, 7)
    print(f"动态创建的函数multiply(4, 7) = {result}")
    print(f"函数文档: {dynamic_multiply.__doc__}")
    print(f"函数签名: {inspect.signature(dynamic_multiply)}")
    
    # 2.3 创建带有默认参数的函数
    print("\n2.3 创建带有默认参数的函数")
    
    # 定义带默认参数的函数实现
    def greet_impl(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    # 获取函数组件
    greet_code = greet_impl.__code__
    greet_globals = greet_impl.__globals__
    
    # 获取默认参数
    greet_defaults = greet_impl.__defaults__
    print(f"原始函数默认参数: {greet_defaults}")
    
    # 创建新函数，修改默认参数
    dynamic_greet = types.FunctionType(
        greet_code,
        greet_globals,
        name="dynamic_greet",
        argdefs=("Hi",),  # 修改默认参数为"Hi"
        closure=None
    )
    
    # 测试函数
    print(f"dynamic_greet('Alice') = {dynamic_greet('Alice')}")
    print(f"dynamic_greet('Bob', 'Welcome') = {dynamic_greet('Bob', 'Welcome')}")
    print(f"新函数默认参数: {dynamic_greet.__defaults__}")
    
    # 2.4 创建带有闭包的函数
    print("\n2.4 创建带有闭包的函数")
    
    # 这部分比较复杂，需要创建cell对象
    # 一个更简单的方法是使用functools.partial
    try:
        import functools
        
        # 创建一个带闭包效果的函数
        def make_adder(x):
            def adder(y):
                return x + y
            return adder
        
        # 使用functools.partial
        add_five = functools.partial(lambda x, y: x + y, 5)
        
        print(f"add_five(3) = {add_five(3)}")
        print(f"add_five(10) = {add_five(10)}")
        
        # 检查是否是偏函数
        print(f"是否是偏函数: {isinstance(add_five, functools.partial)}")
    except ImportError:
        print("functools模块不可用")

# 3. 动态创建方法
def show_dynamic_method_creation():
    """展示如何使用types模块动态创建方法"""
    print("\n=== 3. 动态创建方法 ===")
    print("types模块允许将函数绑定到类或实例，创建方法")
    
    # 3.1 动态创建实例方法
    print("\n3.1 动态创建实例方法")
    
    # 定义一个类
    class Person:
        def __init__(self, name):
            self.name = name
    
    # 定义一个普通函数
    def say_hello(self):
        return f"Hello, my name is {self.name}"
    
    # 创建实例
    person = Person("Alice")
    
    # 将函数绑定为实例方法
    person.say_hello = types.MethodType(say_hello, person)
    
    # 测试动态添加的方法
    print(f"调用动态添加的实例方法: {person.say_hello()}")
    
    # 3.2 动态添加类方法
    print("\n3.2 动态添加类方法")
    
    # 定义一个类函数
    def get_class_name(cls):
        return cls.__name__
    
    # 将函数绑定为类方法
    Person.get_class_name = classmethod(get_class_name)
    
    # 测试类方法
    print(f"调用类方法: {Person.get_class_name()}")
    print(f"通过实例调用类方法: {person.get_class_name()}")
    
    # 3.3 动态添加静态方法
    print("\n3.3 动态添加静态方法")
    
    # 定义一个静态函数
    def welcome_message():
        return "Welcome to the Person class!"
    
    # 将函数绑定为静态方法
    Person.welcome_message = staticmethod(welcome_message)
    
    # 测试静态方法
    print(f"调用静态方法: {Person.welcome_message()}")
    print(f"通过实例调用静态方法: {person.welcome_message()}")
    
    # 3.4 动态替换已存在的方法
    print("\n3.4 动态替换已存在的方法")
    
    # 定义新的初始化方法
    def new_init(self, name, age):
        self.name = name
        self.age = age
    
    # 替换类的__init__方法
    Person.__init__ = new_init
    
    # 创建新实例
    older_person = Person("Bob", 30)
    
    # 验证新方法是否生效
    print(f"新实例的属性 - 名称: {older_person.name}, 年龄: {older_person.age}")
    
    # 注意：旧实例不会受到影响
    try:
        print(f"旧实例是否有age属性: {'age' in vars(person)}")
    except AttributeError:
        print("旧实例没有age属性")

# 4. 检查函数和方法
def show_function_inspection():
    """展示如何使用types模块检查函数和方法"""
    print("\n=== 4. 检查函数和方法 ===")
    print("types模块提供了检查函数和方法类型的工具")
    
    # 定义测试函数和类
    def regular_function(x, y=10):
        """这是一个普通函数"""
        return x + y
    
    class TestClass:
        def instance_method(self, x):
            """这是一个实例方法"""
            return x * 2
        
        @staticmethod
        def static_method(x):
            """这是一个静态方法"""
            return x * 3
        
        @classmethod
        def class_method(cls, x):
            """这是一个类方法"""
            return x * 4
    
    # 创建实例
    test_instance = TestClass()
    
    # 4.1 检查对象是否为函数或方法
    print("\n4.1 检查对象是否为函数或方法")
    
    objects_to_check = [
        (regular_function, "普通函数"),
        (test_instance.instance_method, "实例方法"),
        (TestClass.static_method, "静态方法"),
        (TestClass.class_method, "类方法"),
        (123, "整数"),
        ("string", "字符串")
    ]
    
    print("类型检查结果:")
    for obj, desc in objects_to_check:
        print(f"  {desc}:")
        print(f"    是否可调用: {callable(obj)}")
        print(f"    是否为普通函数: {isinstance(obj, types.FunctionType)}")
        print(f"    是否为方法: {isinstance(obj, types.MethodType)}")
        
        # 如果是函数或方法，显示更多信息
        if callable(obj):
            try:
                print(f"    函数名: {obj.__name__}")
                print(f"    文档字符串: {obj.__doc__}")
                print(f"    签名: {inspect.signature(obj)}")
            except (AttributeError, TypeError):
                print(f"    无法获取更多信息")
    
    # 4.2 检查函数参数
    print("\n4.2 检查函数参数")
    
    # 获取函数签名
    sig = inspect.signature(regular_function)
    print(f"函数regular_function的签名: {sig}")
    
    # 获取参数信息
    print("参数信息:")
    for param_name, param in sig.parameters.items():
        print(f"  {param_name}:")
        print(f"    默认值: {param.default if param.default is not inspect.Parameter.empty else '无'}")
        print(f"    参数类型: {param.kind}")
    
    # 4.3 获取函数源码
    print("\n4.3 获取函数源码")
    
    try:
        source = inspect.getsource(regular_function)
        print(f"函数源码:\n{source}")
    except (IOError, TypeError):
        print("无法获取源码，可能是在交互环境中定义的函数")
    
    # 4.4 检查函数模块
    print("\n4.4 检查函数模块")
    
    print(f"函数regular_function的模块: {regular_function.__module__}")
    
    # 4.5 检查生成器和协程
    print("\n4.5 检查生成器和协程")
    
    # 定义生成器函数
    def gen_example():
        yield 1
        yield 2
    
    # 创建生成器
    gen = gen_example()
    
    print(f"生成器类型检查:")
    print(f"  是否为生成器: {isinstance(gen, types.GeneratorType)}")
    print(f"  是否为迭代器: {isinstance(gen, types.IteratorType) if hasattr(types, 'IteratorType') else 'N/A'}")
    
    # 尝试创建并检查协程
    try:
        async def coro_example():
            await asyncio.sleep(0.1) if 'asyncio' in globals() else None
            return "coroutine"
        
        coro = coro_example()
        
        print(f"\n协程类型检查:")
        if hasattr(types, 'CoroutineType'):
            print(f"  是否为协程: {isinstance(coro, types.CoroutineType)}")
        else:
            print(f"  协程类型: {type(coro)}")
            
except (SyntaxError, NameError):
        print("\n无法创建协程，可能是Python版本过低")

# 5. 动态创建类型
def show_dynamic_type_creation():
    """展示如何动态创建类型"""
    print("\n=== 5. 动态创建类型 ===")
    print("Python允许在运行时动态创建新的类型")
    
    # 5.1 使用type()函数创建类
    print("\n5.1 使用type()函数创建类")
    
    # 定义类的属性和方法
    def init_method(self, name, age):
        self.name = name
        self.age = age
    
    def get_info(self):
        return f"{self.name}, {self.age} years old"
    
    # 动态创建类
    DynamicPerson = type(
        "DynamicPerson",  # 类名
        (object,),        # 基类元组
        {                 # 类字典
            "__init__": init_method,
            "get_info": get_info,
            "species": "Human",  # 类属性
        }
    )
    
    # 创建实例并测试
    person = DynamicPerson("Charlie", 25)
    print(f"动态创建的类名: {DynamicPerson.__name__}")
    print(f"实例信息: {person.get_info()}")
    print(f"类属性: {DynamicPerson.species}")
    
    # 5.2 创建带有继承的类
    print("\n5.2 创建带有继承的类")
    
    # 创建一个基类
    class Employee:
        def __init__(self, employee_id):
            self.employee_id = employee_id
        
        def get_id(self):
            return self.employee_id
    
    # 定义子类的方法
    def manager_init(self, employee_id, department):
        Employee.__init__(self, employee_id)  # 调用父类初始化
        self.department = department
    
    def manager_get_info(self):
        return f"Manager ID: {self.get_id()}, Department: {self.department}"
    
    # 动态创建子类
    DynamicManager = type(
        "DynamicManager",  # 类名
        (Employee,),       # 继承自Employee
        {
            "__init__": manager_init,
            "get_info": manager_get_info,
        }
    )
    
    # 创建实例并测试
    manager = DynamicManager(1001, "Engineering")
    print(f"子类实例信息: {manager.get_info()}")
    print(f"是否是Employee的实例: {isinstance(manager, Employee)}")
    
    # 5.3 使用types.new_class创建类
    print("\n5.3 使用types.new_class创建类")
    
    try:
        # 使用types.new_class创建类
        def class_body(ns):
            ns["__init__"] = lambda self, name: setattr(self, "name", name)
            ns["greet"] = lambda self: f"Hello, {self.name}!"
            ns["class_attr"] = "This is a class attribute"
        
        # 创建新类
        NewClass = types.new_class(
            "NewClass",    # 类名
            (object,),     # 基类
            exec_body=class_body  # 类体执行函数
        )
        
        # 测试新类
        obj = NewClass("David")
        print(f"使用types.new_class创建的类名: {NewClass.__name__}")
        print(f"实例方法调用: {obj.greet()}")
        print(f"类属性: {NewClass.class_attr}")
    except AttributeError:
        print("types.new_class在当前Python版本中不可用")
    
    # 5.4 动态添加描述符
    print("\n5.4 动态添加描述符")
    
    # 定义一个描述符类
    class PropertyDescriptor:
        def __init__(self, name):
            self.name = f"_{name}"
        
        def __get__(self, instance, owner):
            if instance is None:
                return self
            return getattr(instance, self.name, None)
        
        def __set__(self, instance, value):
            # 添加一些验证
            if not isinstance(value, (int, float)):
                raise TypeError("Value must be a number")
            setattr(instance, self.name, value)
    
    # 动态创建一个带描述符的类
    class DynamicClass:
        pass
    
    # 动态添加描述符
    DynamicClass.value = PropertyDescriptor("value")
    
    # 测试描述符
    obj = DynamicClass()
    try:
        obj.value = 42
        print(f"描述符设置的值: {obj.value}")
        
        # 尝试设置错误类型
        obj.value = "not a number"
    except TypeError as e:
        print(f"预期的TypeError: {e}")

# 6. 实际应用场景
def show_practical_applications():
    """展示types模块在实际场景中的应用"""
    print("\n=== 6. 实际应用场景 ===")
    
    # 6.1 实现插件系统
    print("\n6.1 实现插件系统")
    
    # 简单的插件系统实现
    class PluginSystem:
        def __init__(self):
            self.plugins = {}
        
        def register_plugin(self, name, plugin_func):
            """注册插件"""
            if not callable(plugin_func):
                raise TypeError(f"Plugin '{name}' must be callable")
            self.plugins[name] = plugin_func
            print(f"Plugin '{name}' registered")
        
        def execute_plugin(self, name, *args, **kwargs):
            """执行插件"""
            if name not in self.plugins:
                raise KeyError(f"Plugin '{name}' not found")
            return self.plugins[name](*args, **kwargs)
    
    # 创建插件系统实例
    plugin_system = PluginSystem()
    
    # 定义一些插件函数
    def greeting_plugin(name):
        return f"Hello, {name}!"
    
    def sum_plugin(*args):
        return sum(args)
    
    # 注册插件
    plugin_system.register_plugin("greeting", greeting_plugin)
    plugin_system.register_plugin("sum", sum_plugin)
    
    # 执行插件
    print(f"执行greeting插件: {plugin_system.execute_plugin('greeting', 'Alice')}")
    print(f"执行sum插件: {plugin_system.execute_plugin('sum', 1, 2, 3, 4, 5)}")
    
    # 6.2 类型检查装饰器
    print("\n6.2 类型检查装饰器")
    
    def type_check(**type_hints):
        """类型检查装饰器"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # 检查位置参数
                arg_names = list(inspect.signature(func).parameters.keys())
                for i, arg_name in enumerate(arg_names[:len(args)]):
                    if arg_name in type_hints:
                        expected_type = type_hints[arg_name]
                        if not isinstance(args[i], expected_type):
                            raise TypeError(f"Expected {expected_type} for parameter '{arg_name}', got {type(args[i])}")
                
                # 检查关键字参数
                for arg_name, arg_value in kwargs.items():
                    if arg_name in type_hints:
                        expected_type = type_hints[arg_name]
                        if not isinstance(arg_value, expected_type):
                            raise TypeError(f"Expected {expected_type} for parameter '{arg_name}', got {type(arg_value)}")
                
                # 执行原函数
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    # 使用类型检查装饰器
    @type_check(a=int, b=int)
    def add_numbers(a, b):
        return a + b
    
    # 测试装饰器
    print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")
    
    try:
        add_numbers("5", 3)
    except TypeError as e:
        print(f"类型检查异常: {e}")
    
    # 6.3 动态代理
    print("\n6.3 动态代理")
    
    class DynamicProxy:
        def __init__(self, target):
            self._target = target
        
        def __getattr__(self, name):
            # 获取目标对象的属性
            target_attr = getattr(self._target, name)
            
            # 如果是方法，返回一个包装后的方法
            if callable(target_attr):
                def wrapper(*args, **kwargs):
                    print(f"Calling method '{name}' on {self._target}")
                    print(f"Arguments: {args}, {kwargs}")
                    result = target_attr(*args, **kwargs)
                    print(f"Result: {result}")
                    return result
                return wrapper
            
            # 否则直接返回属性值
            return target_attr
    
    # 定义一个目标类
    class Calculator:
        def add(self, a, b):
            return a + b
        
        def subtract(self, a, b):
            return a - b
    
    # 创建代理
    calculator = Calculator()
    proxy = DynamicProxy(calculator)
    
    # 使用代理
    print(f"\n使用代理调用方法:")
    result = proxy.add(10, 5)
    print(f"最终结果: {result}")
    
    # 6.4 动态API客户端
    print("\n6.4 动态API客户端")
    
    # 模拟HTTP请求库
    class MockRequests:
        @staticmethod
        def get(url, **kwargs):
            print(f"GET request to {url}")
            print(f"Params: {kwargs}")
            return MockResponse({"data": f"Response from {url}"})
        
        @staticmethod
        def post(url, **kwargs):
            print(f"POST request to {url}")
            print(f"Data: {kwargs.get('data', {})}")
            return MockResponse({"status": "success", "data": kwargs.get('data', {})})
    
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data
        
        def json(self):
            return self.json_data
    
    # 动态API客户端
    class DynamicAPIClient:
        def __init__(self, base_url):
            self.base_url = base_url
            self.requests = MockRequests()
        
        def __getattr__(self, name):
            def api_method(**kwargs):
                # 构建URL
                endpoint = name.replace('_', '/')
                url = f"{self.base_url}/{endpoint}"
                
                # 根据HTTP方法调用相应的请求函数
                method = kwargs.pop('method', 'get').lower()
                if method == 'get':
                    return self.requests.get(url, **kwargs)
                elif method == 'post':
                    return self.requests.post(url, **kwargs)
                else:
                    raise ValueError(f"Unsupported HTTP method: {method}")
            return api_method
    
    # 使用动态API客户端
    client = DynamicAPIClient("https://api.example.com")
    
    # 调用动态生成的方法
    print("\n调用GET接口:")
    response = client.users(method='get', params={"page": 1})
    print(f"Response JSON: {response.json()}")
    
    print("\n调用POST接口:")
    response = client.create_user(method='post', data={"name": "John", "email": "john@example.com"})
    print(f"Response JSON: {response.json()}")

# 7. 使用注意事项
def usage_notes():
    print("\n=== 7. 使用注意事项 ===")
    print("1. 版本兼容性：不同Python版本之间，types模块的API可能有所差异")
    print("2. 性能考虑：动态创建函数和类型比静态定义性能稍差")
    print("3. 调试困难：动态生成的代码可能更难调试和维护")
    print("4. 命名空间：动态创建的对象需要注意命名空间的管理")
    print("5. 类型检查：使用types模块进行精确类型检查，而不是简单的isinstance()")
    print("6. 安全性：动态执行代码时需要注意安全问题，避免执行不可信代码")
    print("7. 闭包处理：创建带闭包的函数时需要特别注意cell对象的处理")
    print("8. 文档生成：动态创建的对象可能难以自动生成文档")
    print("9. IDE支持：IDE可能无法很好地支持动态生成的代码的自动补全")
    print("10. 异常处理：动态代码可能产生难以预测的异常，需要完善的错误处理")

# 8. 综合示例
def comprehensive_example():
    """综合示例：使用types模块实现一个简单的ORM框架"""
    print("\n=== 8. 综合示例：简易ORM框架 ===")
    
    # 定义一个基础的Model类
    class Model:
        _registry = {}
        
        def __init_subclass__(cls, **kwargs):
            super().__init_subclass__(**kwargs)
            # 注册模型
            if hasattr(cls, '__tablename__'):
                cls._registry[cls.__tablename__] = cls
        
        def __init__(self, **kwargs):
            # 设置属性
            for key, value in kwargs.items():
                setattr(self, key, value)
        
        def save(self):
            # 模拟保存操作
            fields = []
            values = []
            for key, value in vars(self).items():
                fields.append(key)
                values.append(value)
            print(f"Saving {self.__class__.__name__} to {self.__class__.__tablename__}:")
            print(f"  Fields: {fields}")
            print(f"  Values: {values}")
            return True
    
    # 动态创建字段描述符
    class Field:
        def __init__(self, field_type, default=None, primary_key=False):
            self.field_type = field_type
            self.default = default
            self.primary_key = primary_key
            self.name = None
        
        def __set_name__(self, owner, name):
            self.name = name
        
        def __get__(self, instance, owner):
            if instance is None:
                return self
            return getattr(instance, f"_{self.name}", self.default)
        
        def __set__(self, instance, value):
            # 简单的类型检查
            if value is not None and not isinstance(value, self.field_type):
                try:
                    value = self.field_type(value)
                except (TypeError, ValueError):
                    raise TypeError(f"Field '{self.name}' must be of type {self.field_type.__name__}")
            setattr(instance, f"_{self.name}", value)
    
    # 动态创建模型的函数
    def create_model(name, tablename, fields):
        """动态创建ORM模型"""
        # 创建模型字典
        model_dict = {
            '__tablename__': tablename,
        }
        
        # 添加字段
        for field_name, field_params in fields.items():
            field_type = field_params.get('type', str)
            default = field_params.get('default', None)
            primary_key = field_params.get('primary_key', False)
            model_dict[field_name] = Field(field_type, default, primary_key)
        
        # 动态创建模型类
        model_class = type(name, (Model,), model_dict)
        return model_class
    
    # 创建数据库会话管理
    class Session:
        def __init__(self):
            self.objects = []
        
        def add(self, obj):
            self.objects.append(obj)
            return obj
        
        def commit(self):
            results = []
            for obj in self.objects:
                results.append(obj.save())
            self.objects.clear()
            return all(results)
    
    # 使用示例
    print("\n创建动态模型:")
    
    # 动态创建User模型
    User = create_model(
        "User",
        "users",
        {
            "id": {"type": int, "primary_key": True},
            "username": {"type": str},
            "email": {"type": str},
            "age": {"type": int, "default": 0},
            "is_active": {"type": bool, "default": True}
        }
    )
    
    # 动态创建Post模型
    Post = create_model(
        "Post",
        "posts",
        {
            "id": {"type": int, "primary_key": True},
            "title": {"type": str},
            "content": {"type": str},
            "user_id": {"type": int},
            "created_at": {"type": str}
        }
    )
    
    print(f"动态创建的模型: {User.__name__}, {Post.__name__}")
    print(f"User表名: {User.__tablename__}")
    print(f"Post表名: {Post.__tablename__}")
    
    # 创建会话
    session = Session()
    
    # 创建和保存对象
    print("\n创建和保存对象:")
    
    # 创建用户对象
    user1 = User(id=1, username="alice", email="alice@example.com", age=30)
    user2 = User(id=2, username="bob", email="bob@example.com")
    
    # 创建文章对象
    post1 = Post(id=1, title="First Post", content="Hello World", user_id=1, created_at="2023-05-01")
    post2 = Post(id=2, title="Second Post", content="Python is awesome", user_id=1, created_at="2023-05-02")
    
    # 添加到会话
    session.add(user1)
    session.add(user2)
    session.add(post1)
    session.add(post2)
    
    # 提交会话
    print("\n提交会话:")
    result = session.commit()
    print(f"提交结果: {result}")
    
    # 测试类型检查
    print("\n测试字段类型检查:")
    try:
        invalid_user = User(id="not_an_int", username="charlie", email="charlie@example.com")
    except TypeError as e:
        print(f"预期的类型错误: {e}")
    
    print("\nORM框架示例完成！")

# 执行所有示例
if __name__ == "__main__":
    print("types模块 - Python标准库中的类型创建与检查\n")
    
    # 执行各个示例
    show_builtin_types()
    show_dynamic_function_creation()
    show_dynamic_method_creation()
    show_function_inspection()
    show_dynamic_type_creation()
    show_practical_applications()
    usage_notes()
    comprehensive_example()
    
    print("\n=== 结束 ===")
    print("types模块是Python进行元编程的强大工具，允许在运行时动态创建和检查类型。")
    print("它提供了对内置类型的引用，支持动态创建函数、方法和类，")
    print("使得Python程序可以更加灵活地适应不同的需求。")
    print("在框架开发、插件系统、动态代理等场景中，types模块非常有用。")
    print("但需要注意，过度使用动态类型可能会使代码更难理解和维护，")
    print("在实际开发中应该权衡灵活性和可维护性。")
","}}}