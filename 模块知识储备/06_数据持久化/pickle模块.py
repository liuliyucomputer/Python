# Python pickle模块详解

import pickle
import pickletools
import io
import gzip
import os

# 1. 模块概述
print("=== 1. pickle模块概述 ===")
print("pickle模块提供了Python对象的序列化和反序列化功能，允许将复杂的Python对象转换为字节流，以便存储或传输，然后再将字节流转换回原始对象。")
print("该模块的主要特点：")
print("- 支持几乎所有Python数据类型（包括自定义类）")
print("- 提供多种协议版本，支持不同版本的Python兼容性")
print("- 可以与文件对象和字节流一起使用")
print("- 提供压缩选项以减少存储大小")
print("- 支持自定义序列化和反序列化逻辑")
print()

# 2. 基本用法
print("=== 2. 基本用法 ===")

print("2.1 对象的序列化（pickling）：")
# 创建一个复杂的Python对象
complex_object = {
    'string': 'Hello, pickle!',
    'list': [1, 2, 3, 4, 5],
    'tuple': (10, 20, 30),
    'dict': {'a': 1, 'b': 2, 'c': 3},
    'int': 42,
    'float': 3.14159,
    'bool': True,
    'none': None
}

# 使用pickle.dumps()将对象序列化为字节流
pickled_data = pickle.dumps(complex_object)
print(f"  原始对象: {complex_object}")
print(f"  序列化后的字节流长度: {len(pickled_data)} 字节")
print(f"  序列化后的字节流类型: {type(pickled_data)}")

print()

print("2.2 对象的反序列化（unpickling）：")
# 使用pickle.loads()将字节流反序列化为对象
unpickled_object = pickle.loads(pickled_data)
print(f"  反序列化后的对象: {unpickled_object}")
print(f"  原始对象与反序列化对象是否相等: {complex_object == unpickled_object}")
print(f"  原始对象与反序列化对象是否是同一对象: {complex_object is unpickled_object}")

print()

print("2.3 与文件一起使用：")
# 使用pickle.dump()将对象序列化到文件
with open("pickle_test.pkl", "wb") as f:
    pickle.dump(complex_object, f)

print(f"  对象已序列化到文件: pickle_test.pkl")
print(f"  文件大小: {os.path.getsize('pickle_test.pkl')} 字节")

# 使用pickle.load()从文件中反序列化对象
with open("pickle_test.pkl", "rb") as f:
    loaded_object = pickle.load(f)

print(f"  从文件中反序列化的对象: {loaded_object}")
print(f"  与原始对象是否相等: {complex_object == loaded_object}")

# 清理测试文件
os.remove("pickle_test.pkl")

print()

# 3. 高级特性
print("=== 3. 高级特性 ===")

print("3.1 协议版本：")
print("   pickle模块支持多种协议版本，不同版本的协议提供不同的功能和兼容性：")
print(f"   - 协议0：ASCII协议，向后兼容（默认用于Python 2.x）")
print(f"   - 协议1：旧的二进制协议")
print(f"   - 协议2：Python 2.3引入的新二进制协议")
print(f"   - 协议3：Python 3.0引入的协议，不兼容Python 2.x")
print(f"   - 协议4：Python 3.4引入的协议，支持更大的对象")
print(f"   - 协议5：Python 3.8引入的协议，支持PEP 574定义的数据类型")

# 显示当前默认协议版本
print(f"   当前默认协议版本: {pickle.HIGHEST_PROTOCOL}")

# 使用不同协议版本序列化对象
for protocol in range(0, pickle.HIGHEST_PROTOCOL + 1):
    pickled_data = pickle.dumps(complex_object, protocol=protocol)
    print(f"   协议 {protocol}: 字节流长度 = {len(pickled_data)} 字节")

print()

print("3.2 压缩序列化数据：")
# 使用gzip模块压缩序列化数据
print(f"  未压缩的序列化数据长度: {len(pickle.dumps(complex_object))} 字节")

# 使用gzip压缩
with io.BytesIO() as buffer:
    with gzip.GzipFile(fileobj=buffer, mode='wb') as f:
        pickle.dump(complex_object, f)
    compressed_data = buffer.getvalue()

print(f"  gzip压缩后的序列化数据长度: {len(compressed_data)} 字节")
print(f"  压缩率: {round((len(pickle.dumps(complex_object)) - len(compressed_data)) / len(pickle.dumps(complex_object)) * 100, 2)}%")

# 解压缩并反序列化
with io.BytesIO(compressed_data) as buffer:
    with gzip.GzipFile(fileobj=buffer, mode='rb') as f:
        decompressed_object = pickle.load(f)

print(f"  解压缩并反序列化后的对象与原始对象是否相等: {complex_object == decompressed_object}")

print()

print("3.3 自定义类的序列化：")
# 定义一个自定义类
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, email='{self.email}')"
    
    def greet(self):
        return f"Hello, my name is {self.name} and I'm {self.age} years old."

# 创建自定义类的实例
person = Person("张三", 30, "zhangsan@example.com")
print(f"  原始自定义对象: {person}")
print(f"  调用对象方法: {person.greet()}")

# 序列化自定义类实例
pickled_person = pickle.dumps(person)
print(f"  序列化后的字节流长度: {len(pickled_person)} 字节")

# 反序列化自定义类实例
unpickled_person = pickle.loads(pickled_person)
print(f"  反序列化后的对象: {unpickled_person}")
print(f"  调用反序列化对象的方法: {unpickled_person.greet()}")
print(f"  反序列化对象的类型: {type(unpickled_person)}")

print()

# 4. 实用函数
print("=== 4. 实用函数 ===")

print("4.1 pickle.dumps() 和 pickle.loads()：")
print("   - pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None):")
print("     将对象序列化为字节流")
print("     参数：")
print("     - obj: 要序列化的对象")
print("     - protocol: 使用的协议版本，默认为pickle.HIGHEST_PROTOCOL")
print("     - fix_imports: 是否修复Python 2.x到Python 3.x的导入问题")
print("     - buffer_callback: 用于处理缓冲区的回调函数")

print("   ")

print("   - pickle.loads(data, /, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=None):")
print("     将字节流反序列化为对象")
print("     参数：")
print("     - data: 要反序列化的字节流")
print("     - fix_imports: 是否修复Python 2.x到Python 3.x的导入问题")
print("     - encoding: 反序列化时使用的编码")
print("     - errors: 编码错误处理方式")
print("     - buffers: 用于处理缓冲区的对象列表")

print()

print("4.2 pickle.dump() 和 pickle.load()：")
print("   - pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None):")
print("     将对象序列化到文件对象")
print("     参数：")
print("     - obj: 要序列化的对象")
print("     - file: 要写入的文件对象，必须以二进制模式打开")
print("     - protocol: 使用的协议版本")
print("     - fix_imports: 是否修复Python 2.x到Python 3.x的导入问题")
print("     - buffer_callback: 用于处理缓冲区的回调函数")

print("   ")

print("   - pickle.load(file, /, *, fix_imports=True, encoding='ASCII', errors='strict', buffers=None):")
print("     从文件对象中反序列化对象")
print("     参数：")
print("     - file: 要读取的文件对象，必须以二进制模式打开")
print("     - fix_imports: 是否修复Python 2.x到Python 3.x的导入问题")
print("     - encoding: 反序列化时使用的编码")
print("     - errors: 编码错误处理方式")
print("     - buffers: 用于处理缓冲区的对象列表")

print()

print("4.3 pickletools.dis()：")
print("   反汇编pickle数据，用于调试和分析")
print(f"  反汇编序列化数据示例：")
simple_object = {"a": 1, "b": 2, "c": 3}
simple_pickled = pickle.dumps(simple_object)

# 使用pickletools.dis()反汇编
print("   ")
pickletools.dis(simple_pickled)

print()

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")

print("5.1 保存和加载机器学习模型：")
# 注意：这里只是一个示例，实际使用中需要安装scikit-learn
print("  示例：")
print("  # 保存机器学习模型")
print("  import pickle")
print("  from sklearn.linear_model import LinearRegression")
print()
print("  # 创建和训练模型")
print("  model = LinearRegression()")
print("  model.fit(X_train, y_train)")
print()
print("  # 保存模型到文件")
print("  with open('linear_model.pkl', 'wb') as f:")
print("      pickle.dump(model, f)")
print()
print("  # 加载模型")
print("  with open('linear_model.pkl', 'rb') as f:")
print("      loaded_model = pickle.load(f)")
print()
print("  # 使用加载的模型进行预测")
print("  predictions = loaded_model.predict(X_test)")

print()

print("5.2 保存和加载游戏进度：")
class GameSave:
    def __init__(self, player_name, level, score, inventory, position):
        self.player_name = player_name
        self.level = level
        self.score = score
        self.inventory = inventory
        self.position = position
        self.timestamp = pickle.time()  # 保存时间戳
    
    def __repr__(self):
        return f"GameSave(player='{self.player_name}', level={self.level}, score={self.score})"

# 创建游戏存档
game_save = GameSave(
    player_name="勇者张三",
    level=10,
    score=15000,
    inventory=["剑", "盾", "药水", "金币(100)"],
    position=(100, 200)
)

print(f"  游戏存档: {game_save}")

# 保存游戏存档到文件
with open("game_save.pkl", "wb") as f:
    pickle.dump(game_save, f)

print(f"  游戏存档已保存到文件: game_save.pkl")

# 加载游戏存档
with open("game_save.pkl", "rb") as f:
    loaded_game_save = pickle.load(f)

print(f"  加载的游戏存档: {loaded_game_save}")
print(f"  存档位置: {loaded_game_save.position}")
print(f"  存档物品栏: {loaded_game_save.inventory}")

# 清理测试文件
os.remove("game_save.pkl")

print()

print("5.3 缓存计算结果：")
def expensive_calculation(n):
    """模拟耗时的计算"""
    print(f"  执行耗时计算: n = {n}")
    result = 0
    for i in range(n):
        result += i ** 2
    return result

# 创建缓存装饰器
import functools

def cache_with_pickle(func):
    """使用pickle缓存函数结果的装饰器"""
    cache_file = f"{func.__name__}_cache.pkl"
    
    # 尝试加载缓存
    try:
        with open(cache_file, "rb") as f:
            cache = pickle.load(f)
    except (FileNotFoundError, EOFError):
        cache = {}
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 创建缓存键
        key = (args, frozenset(kwargs.items()))
        
        # 检查缓存
        if key not in cache:
            # 执行函数并缓存结果
            cache[key] = func(*args, **kwargs)
            # 保存缓存到文件
            with open(cache_file, "wb") as f:
                pickle.dump(cache, f)
        
        return cache[key]
    
    return wrapper

# 应用缓存装饰器
@cache_with_pickle
def cached_expensive_calculation(n):
    return expensive_calculation(n)

# 第一次调用（会执行计算并缓存）
print("  第一次调用：")
result1 = cached_expensive_calculation(100000)
print(f"  计算结果: {result1}")

# 第二次调用（会使用缓存）
print("\n  第二次调用：")
result2 = cached_expensive_calculation(100000)
print(f"  计算结果: {result2}")

# 清理缓存文件
os.remove("cached_expensive_calculation_cache.pkl")

print()

print("5.4 序列化自定义类的高级示例：")
class Employee:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department
        self._salary = 0  # 私有属性
    
    def set_salary(self, salary):
        self._salary = salary
    
    def get_salary(self):
        return self._salary
    
    def __repr__(self):
        return f"Employee(name='{self.name}', id={self.id}, department='{self.department}')"
    
    # 自定义序列化方法
    def __getstate__(self):
        # 返回要序列化的属性字典
        state = self.__dict__.copy()
        # 可以在这里添加额外的处理
        return state
    
    # 自定义反序列化方法
    def __setstate__(self, state):
        # 恢复对象状态
        self.__dict__.update(state)
        # 可以在这里添加额外的初始化

# 创建Employee实例
employee = Employee("李四", 1001, "技术部")
employee.set_salary(5000)

print(f"  原始Employee对象: {employee}")
print(f"  员工工资: {employee.get_salary()}")

# 序列化
pickled_employee = pickle.dumps(employee)
print(f"  序列化后的字节流长度: {len(pickled_employee)} 字节")

# 反序列化
unpickled_employee = pickle.loads(pickled_employee)
print(f"  反序列化后的Employee对象: {unpickled_employee}")
print(f"  反序列化后的员工工资: {unpickled_employee.get_salary()}")

print()

# 6. 高级技巧
print("=== 6. 高级技巧 ===")

print("6.1 使用__getstate__和__setstate__自定义序列化：")
print("  如5.4示例所示，可以在自定义类中实现__getstate__和__setstate__方法来控制序列化和反序列化过程。")
print("  - __getstate__(): 返回要序列化的对象状态（通常是字典）")
print("  - __setstate__(state): 从state字典恢复对象状态")

print()

print("6.2 使用__reduce__方法自定义序列化：")
class CustomObject:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"CustomObject(value={self.value})")
    
    def __reduce__(self):
        # 返回一个元组，包含：
        # 1. 用于重建对象的函数
        # 2. 传递给该函数的参数
        return (recreate_custom_object, (self.value,))

def recreate_custom_object(value):
    """用于重建CustomObject的函数"""
    obj = CustomObject(value)
    # 可以在这里添加额外的初始化逻辑
    return obj

custom_obj = CustomObject(42)
pickled_custom = pickle.dumps(custom_obj)
unpickled_custom = pickle.loads(pickled_custom)

print(f"  自定义对象: {custom_obj}")
print(f"  反序列化后的自定义对象: {unpickled_custom}")

print()

print("6.3 使用pickle协议5的新特性：")
# 协议5支持PEP 574定义的数据类型，如内存视图

# 创建一个使用内存视图的对象
memory_view_obj = {
    "name": "内存视图示例",
    "data": memoryview(b"Hello, Pickle Protocol 5!\x00\x01\x02\x03")
}

# 使用协议5序列化
pickled_mv = pickle.dumps(memory_view_obj, protocol=5)
print(f"  使用协议5序列化内存视图对象的长度: {len(pickled_mv)} 字节")

# 反序列化
unpickled_mv = pickle.loads(pickled_mv)
print(f"  反序列化后的对象: {unpickled_mv}")
print(f"  内存视图数据: {bytes(unpickled_mv['data'])}")

print()

print("6.4 处理循环引用：")
# 创建循环引用
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"Node(value={self.value}, next={self.next.value if self.next else None})")

# 创建循环链表
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node1  # 创建循环引用

print(f"  循环链表节点1: {node1}")
print(f"  循环链表节点2: {node2}")
print(f"  循环链表节点3: {node3}")

# 序列化循环引用对象
pickled_node = pickle.dumps(node1)
print(f"  序列化循环引用对象的长度: {len(pickled_node)} 字节")

# 反序列化循环引用对象
unpickled_node = pickle.loads(pickled_node)
print(f"  反序列化后的节点1: {unpickled_node}")
print(f"  反序列化后的节点2: {unpickled_node.next}")
print(f"  反序列化后的节点3: {unpickled_node.next.next}")
print(f"  反序列化后是否仍然是循环引用: {unpickled_node.next.next.next is unpickled_node}")

print()

# 7. 最佳实践
print("=== 7. 最佳实践 ===")

print("1. 使用最新的协议版本：")
print("   # 使用最新的协议版本可以提高性能和兼容性")
print("   pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)")

print("\n2. 安全使用pickle：")
print("   # 不要反序列化来自不可信源的数据")
print("   # 反序列化不可信数据可能导致安全漏洞")

print("\n3. 处理文件操作异常：")
print("   # 序列化和反序列化时可能会遇到文件操作异常")
print("   try:")
print("       with open('data.pkl', 'wb') as f:")
print("           pickle.dump(obj, f)")
print("   except IOError as e:")
print("       print(f'文件操作错误: {e}')")

print("\n4. 考虑使用压缩：")
print("   # 对于大型对象，可以使用压缩减少存储空间")
print("   import gzip")
print("   with gzip.open('data.pkl.gz', 'wb') as f:")
print("       pickle.dump(obj, f)")

print("\n5. 文档化序列化格式：")
print("   # 记录序列化对象的结构和版本，以便将来可以正确反序列化")
print("   # 例如，可以在序列化数据中包含版本号")
print("   data = {")
print("       'version': '1.0',")
print("       'data': actual_data")
print("   }")
print("   pickle.dump(data, f)")

print("\n6. 测试序列化和反序列化：")
print("   # 确保序列化和反序列化能够正确工作")
print("   def test_pickling(obj):")
print("       pickled = pickle.dumps(obj)")
print("       unpickled = pickle.loads(pickled)")
print("       assert obj == unpickled, '序列化和反序列化后对象不相等'")
print("       return True")

print("\n7. 考虑使用替代方案：")
print("   # 对于简单数据，考虑使用JSON或其他更安全的格式")
print("   # JSON是人类可读的，并且比pickle更安全")
print("   import json")
print("   json.dumps(obj)  # 对于简单对象")

# 8. 常见错误和陷阱
print("=== 8. 常见错误和陷阱 ===")

print("1. 安全风险：")
print("   # 错误：反序列化来自不可信源的数据")
print("   with open('untrusted_data.pkl', 'rb') as f:")
print("       obj = pickle.load(f)  # 危险！")
print("   ")
print("   # 正确：只反序列化来自可信源的数据")
print("   # 或者使用更安全的格式，如JSON")

print("\n2. 版本兼容性：")
print("   # 错误：在Python 3.x中反序列化Python 2.x的pickle数据")
print("   # 可能会遇到编码问题")
print("   ")
print("   # 正确：使用fix_imports参数")
print("   pickle.load(f, fix_imports=True)")

print("\n3. 循环引用导致的内存泄漏：")
print("   # 错误：创建大量循环引用对象但不清理")
print("   # 可能导致内存泄漏")
print("   ")
print("   # 正确：定期清理不再使用的对象")
print("   import gc")
print("   gc.collect()  # 手动触发垃圾回收")

print("\n4. 无法序列化的对象：")
print("   # 错误：尝试序列化无法序列化的对象")
print("   import socket")
print("   s = socket.socket()")
print("   pickle.dumps(s)  # 抛出TypeError")
print("   ")
print("   # 正确：实现自定义序列化方法或跳过无法序列化的属性")
print("   class MyClass:")
print("       def __init__(self):")
print("           self.socket = socket.socket()")
print("           self.data = '可序列化的数据'")
print("       ")
print("       def __getstate__(self):")
print("           state = self.__dict__.copy()")
print("           del state['socket']  # 跳过无法序列化的属性")
print("           return state")

print("\n5. 文件模式错误：")
print("   # 错误：使用文本模式打开文件进行pickle操作")
print("   with open('data.pkl', 'w') as f:  # 错误的模式")
print("       pickle.dump(obj, f)")
print("   ")
print("   # 正确：使用二进制模式打开文件")
print("   with open('data.pkl', 'wb') as f:  # 正确的模式")
print("       pickle.dump(obj, f)")

print("\n6. 类定义变更：")
print("   # 错误：类定义变更后尝试反序列化旧的pickle数据")
print("   # 可能导致AttributeError或其他错误")
print("   ")
print("   # 正确：版本化你的数据结构")
print("   # 或者实现__setstate__方法来处理旧版本的数据")

# 9. 总结
print("=== 9. 总结 ===")
print("pickle模块是Python中强大的对象序列化和反序列化工具，允许将复杂的Python对象转换为字节流进行存储或传输。")
print()
print("主要功能：")
print("- 支持几乎所有Python数据类型的序列化和反序列化")
print("- 提供多种协议版本，支持不同版本的Python兼容性")
print("- 可以与文件对象和字节流一起使用")
print("- 支持自定义序列化和反序列化逻辑")
print("- 提供压缩选项以减少存储大小")
print()
print("优势：")
print("- 功能强大，支持复杂对象的序列化")
print("- 使用简单，API简洁易用")
print("- 性能良好，适用于大多数应用场景")
print("- 与Python标准库紧密集成")
print()
print("应用场景：")
print("- 保存和加载机器学习模型")
print("- 游戏进度的保存和加载")
print("- 缓存计算结果")
print("- 分布式计算中的数据传输")
print("- 对象的持久化存储")
print()
print("注意事项：")
print("- 不要反序列化来自不可信源的数据")
print("- 注意版本兼容性问题")
print("- 考虑使用压缩减少存储大小")
print("- 文档化序列化格式以便将来维护")

print("\n通过合理使用pickle模块，可以方便地实现Python对象的持久化和传输，提高应用程序的灵活性和可扩展性。")
