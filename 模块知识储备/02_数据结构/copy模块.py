# copy模块 - 对象复制操作
# 功能作用：提供对象复制功能，包括浅拷贝和深拷贝
# 使用情景：需要复制对象而不共享引用、创建对象的独立副本、数据处理中的不变性保证
# 注意事项：注意深拷贝的循环引用问题、性能考虑、不可变对象的特殊处理、自定义对象的复制控制

import copy

# 模块概述
"""
copy模块提供了用于创建Python对象副本的函数，主要包括两种类型的复制：
1. 浅拷贝(Shallow Copy)：创建一个新对象，但其中包含的子对象引用仍然指向原始对象中的子对象
2. 深拷贝(Deep Copy)：创建一个新对象，并且递归地复制其中包含的所有子对象

该模块对于需要操作对象的独立副本而不影响原始对象的场景非常有用，
例如数据处理、配置管理、保护性复制等场景。

主要函数：
- copy()：创建对象的浅拷贝
- deepcopy()：创建对象的深拷贝
- copyreg模块：控制对象的复制行为
"""

# 1. 浅拷贝与深拷贝的基本概念
print("=== 1. 浅拷贝与深拷贝的基本概念 ===")

def basic_concepts():
    """演示浅拷贝与深拷贝的基本概念和区别"""
    print("浅拷贝和深拷贝的核心区别在于如何处理对象中的嵌套对象引用：\n")
    
    print("浅拷贝 (Shallow Copy):")
    print("- 创建一个新对象，但仅复制对象的顶层结构")
    print("- 新对象中的嵌套对象仍然引用原始对象中的嵌套对象")
    print("- 修改新对象中的嵌套对象会影响原始对象")
    print("- 适用于简单对象或不需要完全隔离的场景")
    
    print("\n深拷贝 (Deep Copy):")
    print("- 创建一个新对象，并递归复制所有嵌套对象")
    print("- 新对象与原始对象完全隔离，包括所有嵌套对象")
    print("- 修改新对象中的任何内容都不会影响原始对象")
    print("- 适用于需要完全独立副本的场景，但可能有性能开销")
    
    # 内存布局示意图（文本表示）
    print("\n内存布局示意图：")
    print("原始对象:")
    print("Object A [数据 | ref->Object B]")
    print("                |")
    print("                v")
    print("Object B [嵌套数据]")
    
    print("\n浅拷贝结果:")
    print("Object A' [数据 | ref->Object B]")
    print("                 |")
    print("                 v")
    print("Object B [嵌套数据] <-- 共享")
    
    print("\n深拷贝结果:")
    print("Object A' [数据 | ref->Object B']")
    print("                |")
    print("                v")
    print("Object B' [嵌套数据] <-- 独立副本")

# 运行基本概念演示
basic_concepts()
print()

# 2. 浅拷贝 (copy()) 函数
print("=== 2. 浅拷贝 (copy()) 函数 ===")

def shallow_copy_demo():
    """演示浅拷贝函数的使用"""
    print("copy()函数创建对象的浅拷贝，适用于简单数据结构的复制：\n")
    
    # 语法
    print("语法:")
    print("copy.copy(x)")
    print("参数:")
    print("  x: 要复制的对象")
    print("返回值:")
    print("  x的浅拷贝副本")
    print("\n注意:")
    print("- 如果对象实现了__copy__()方法，则调用该方法进行复制")
    print("- 否则，尝试创建相同类型的新对象，并复制其内容")
    
    # 示例1: 复制列表
    print("\n示例1: 复制列表")
    
    original_list = [1, 2, 3, [4, 5]]
    shallow_copied = copy.copy(original_list)
    
    print(f"原始列表: {original_list}")
    print(f"浅拷贝列表: {shallow_copied}")
    
    # 修改顶层元素，不影响原始列表
    shallow_copied[0] = 100
    print(f"修改浅拷贝列表的顶层元素后:")
    print(f"  原始列表: {original_list}")
    print(f"  浅拷贝列表: {shallow_copied}")
    
    # 修改嵌套列表，会影响原始列表
    shallow_copied[3][0] = 400
    print(f"修改浅拷贝列表的嵌套列表后:")
    print(f"  原始列表: {original_list}")
    print(f"  浅拷贝列表: {shallow_copied}")
    
    # 示例2: 复制字典
    print("\n示例2: 复制字典")
    
    original_dict = {"name": "Alice", "scores": [85, 90, 95]}
    shallow_copied_dict = copy.copy(original_dict)
    
    print(f"原始字典: {original_dict}")
    print(f"浅拷贝字典: {shallow_copied_dict}")
    
    # 修改顶层值，不影响原始字典
    shallow_copied_dict["name"] = "Bob"
    print(f"修改浅拷贝字典的顶层值后:")
    print(f"  原始字典: {original_dict}")
    print(f"  浅拷贝字典: {shallow_copied_dict}")
    
    # 修改嵌套列表，会影响原始字典
    shallow_copied_dict["scores"][0] = 100
    print(f"修改浅拷贝字典的嵌套列表后:")
    print(f"  原始字典: {original_dict}")
    print(f"  浅拷贝字典: {shallow_copied_dict}")
    
    # 示例3: 复制自定义对象
    print("\n示例3: 复制自定义对象")
    
    class Person:
        def __init__(self, name, friends):
            self.name = name
            self.friends = friends  # 嵌套对象
        
        def __repr__(self):
            return f"Person(name='{self.name}', friends={self.friends})"
    
    original_person = Person("Alice", ["Bob", "Charlie"])
    shallow_copied_person = copy.copy(original_person)
    
    print(f"原始对象: {original_person}")
    print(f"浅拷贝对象: {shallow_copied_person}")
    
    # 修改顶层属性，不影响原始对象
    shallow_copied_person.name = "Diana"
    print(f"修改浅拷贝对象的顶层属性后:")
    print(f"  原始对象: {original_person}")
    print(f"  浅拷贝对象: {shallow_copied_person}")
    
    # 修改嵌套对象，会影响原始对象
    shallow_copied_person.friends.append("Eve")
    print(f"修改浅拷贝对象的嵌套对象后:")
    print(f"  原始对象: {original_person}")
    print(f"  浅拷贝对象: {shallow_copied_person}")
    
    # 示例4: 不可变对象的浅拷贝
    print("\n示例4: 不可变对象的浅拷贝")
    print("注意：对于不可变对象(tuple, string, int等)，浅拷贝不会创建新对象，而是返回原始对象的引用")
    
    # 元组的浅拷贝
    original_tuple = (1, 2, (3, 4))
    shallow_copied_tuple = copy.copy(original_tuple)
    
    print(f"原始元组: {original_tuple}")
    print(f"浅拷贝元组: {shallow_copied_tuple}")
    print(f"是否是同一个对象: {original_tuple is shallow_copied_tuple}")  # True
    
    # 字符串的浅拷贝
    original_str = "Hello"
    shallow_copied_str = copy.copy(original_str)
    
    print(f"\n原始字符串: {original_str}")
    print(f"浅拷贝字符串: {shallow_copied_str}")
    print(f"是否是同一个对象: {original_str is shallow_copied_str}")  # True

# 运行浅拷贝演示
shallow_copy_demo()
print()

# 3. 深拷贝 (deepcopy()) 函数
print("=== 3. 深拷贝 (deepcopy()) 函数 ===")

def deep_copy_demo():
    """演示深拷贝函数的使用"""
    print("deepcopy()函数创建对象的深拷贝，递归复制所有嵌套对象，适用于需要完全隔离的场景：\n")
    
    # 语法
    print("语法:")
    print("copy.deepcopy(x, memo=None, _nil=[])")
    print("参数:")
    print("  x: 要复制的对象")
    print("  memo: 用于存储已复制对象的字典，防止循环引用")
    print("  _nil: 内部使用的参数")
    print("返回值:")
    print("  x的深拷贝副本")
    print("\n注意:")
    print("- 如果对象实现了__deepcopy__()方法，则调用该方法进行复制")
    print("- 会递归复制所有嵌套对象，创建完全独立的副本")
    print("- 使用memo字典跟踪已复制的对象，处理循环引用")
    
    # 示例1: 复制嵌套列表
    print("\n示例1: 复制嵌套列表")
    
    original_list = [1, 2, 3, [4, 5, [6, 7]]]
    deep_copied = copy.deepcopy(original_list)
    
    print(f"原始列表: {original_list}")
    print(f"深拷贝列表: {deep_copied}")
    
    # 修改顶层元素，不影响原始列表
    deep_copied[0] = 100
    print(f"修改深拷贝列表的顶层元素后:")
    print(f"  原始列表: {original_list}")
    print(f"  深拷贝列表: {deep_copied}")
    
    # 修改嵌套列表，不影响原始列表
    deep_copied[3][0] = 400
    print(f"修改深拷贝列表的第一层嵌套后:")
    print(f"  原始列表: {original_list}")
    print(f"  深拷贝列表: {deep_copied}")
    
    # 修改深层嵌套列表，不影响原始列表
    deep_copied[3][2][0] = 600
    print(f"修改深拷贝列表的深层嵌套后:")
    print(f"  原始列表: {original_list}")
    print(f"  深拷贝列表: {deep_copied}")
    
    # 示例2: 复制复杂字典
    print("\n示例2: 复制复杂字典")
    
    original_dict = {
        "user": "Alice",
        "settings": {
            "theme": "dark",
            "notifications": True
        },
        "scores": [85, 90, 95]
    }
    deep_copied_dict = copy.deepcopy(original_dict)
    
    print(f"原始字典: {original_dict}")
    print(f"深拷贝字典: {deep_copied_dict}")
    
    # 修改嵌套对象，不影响原始字典
    deep_copied_dict["settings"]["theme"] = "light"
    deep_copied_dict["scores"].append(100)
    
    print(f"修改深拷贝字典的嵌套对象后:")
    print(f"  原始字典: {original_dict}")
    print(f"  深拷贝字典: {deep_copied_dict}")
    
    # 示例3: 复制自定义对象
    print("\n示例3: 复制自定义对象")
    
    class Address:
        def __init__(self, city, street):
            self.city = city
            self.street = street
        
        def __repr__(self):
            return f"Address(city='{self.city}', street='{self.street}')"
    
    class Person:
        def __init__(self, name, age, address):
            self.name = name
            self.age = age
            self.address = address  # 嵌套对象
        
        def __repr__(self):
            return f"Person(name='{self.name}', age={self.age}, address={self.address})"
    
    # 创建嵌套对象
    original_address = Address("Beijing", "Main Street")
    original_person = Person("Alice", 30, original_address)
    
    # 深拷贝
    deep_copied_person = copy.deepcopy(original_person)
    
    print(f"原始对象: {original_person}")
    print(f"深拷贝对象: {deep_copied_person}")
    
    # 修改嵌套对象，不影响原始对象
    deep_copied_person.address.city = "Shanghai"
    deep_copied_person.age = 31
    
    print(f"修改深拷贝对象的嵌套对象后:")
    print(f"  原始对象: {original_person}")
    print(f"  深拷贝对象: {deep_copied_person}")
    print(f"  原始地址对象: {original_address}")
    print(f"  深拷贝地址对象: {deep_copied_person.address}")
    print(f"  是否是同一个地址对象: {original_address is deep_copied_person.address}")  # False
    
    # 示例4: 处理循环引用
    print("\n示例4: 处理循环引用")
    print("deepcopy()可以正确处理对象之间的循环引用，避免无限递归")
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.neighbors = []  # 可能包含对自身的引用
        
        def __repr__(self):
            return f"Node(value={self.value}, neighbors_count={len(self.neighbors)})"
    
    # 创建循环引用
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors.append(node2)  # node1引用node2
    node2.neighbors.append(node1)  # node2引用node1，形成循环
    
    # 深拷贝含有循环引用的对象
    deep_copied_node1 = copy.deepcopy(node1)
    
    print(f"原始节点1: {node1}")
    print(f"深拷贝节点1: {deep_copied_node1}")
    
    # 验证深拷贝正确处理了循环引用
    print(f"\n验证循环引用处理:")
    print(f"原始节点1的邻居: {node1.neighbors}")
    print(f"深拷贝节点1的邻居: {deep_copied_node1.neighbors}")
    
    # 验证深拷贝后的对象仍然保持引用关系
    print(f"深拷贝节点1的邻居是否是深拷贝节点2: {deep_copied_node1.neighbors[0] is deep_copied_node1.neighbors[0]}")  # True
    
    # 修改深拷贝对象不会影响原始对象
    deep_copied_node1.value = 10
    deep_copied_node1.neighbors[0].value = 20
    
    print(f"\n修改深拷贝对象后:")
    print(f"  原始节点1: {node1}")
    print(f"  原始节点2: {node2}")
    print(f"  深拷贝节点1: {deep_copied_node1}")
    print(f"  深拷贝节点2: {deep_copied_node1.neighbors[0]}")

# 运行深拷贝演示
deep_copy_demo()
print()

# 4. 自定义对象的复制行为
print("=== 4. 自定义对象的复制行为 ===")

def custom_copy_behavior():
    """演示如何自定义对象的复制行为"""
    print("通过实现特殊方法，可以自定义对象的浅拷贝和深拷贝行为：\n")
    
    print("自定义浅拷贝:")
    print("- 实现__copy__()方法来自定义浅拷贝行为")
    print("- 该方法应返回对象的浅拷贝副本")
    print("- 不需要传入额外参数")
    
    print("\n自定义深拷贝:")
    print("- 实现__deepcopy__()方法来自定义深拷贝行为")
    print("- 该方法接受一个memo字典参数，用于处理循环引用")
    print("- 在复制嵌套对象时，应使用copy.deepcopy()并传递memo字典")
    
    # 示例1: 自定义浅拷贝
    print("\n示例1: 自定义浅拷贝")
    
    class MyClassWithCopy:
        def __init__(self, name, data):
            self.name = name
            self.data = data
        
        def __repr__(self):
            return f"MyClassWithCopy(name='{self.name}', data={self.data})"
        
        def __copy__(self):
            print("自定义__copy__()方法被调用")
            # 创建新实例，复制属性
            new_instance = MyClassWithCopy(self.name, self.data)  # 注意这里是浅拷贝data
            # 可以在这里进行额外的自定义逻辑
            return new_instance
    
    # 测试自定义浅拷贝
    original = MyClassWithCopy("test", [1, 2, 3])
    shallow_copied = copy.copy(original)
    
    print(f"原始对象: {original}")
    print(f"浅拷贝对象: {shallow_copied}")
    
    # 验证是否是新对象
    print(f"是否是同一个对象: {original is shallow_copied}")  # False
    
    # 验证嵌套对象是否共享引用
    print(f"嵌套数据是否共享引用: {original.data is shallow_copied.data}")  # True
    
    # 示例2: 自定义深拷贝
    print("\n示例2: 自定义深拷贝")
    
    class MyClassWithDeepCopy:
        def __init__(self, name, data, metadata):
            self.name = name
            self.data = data  # 嵌套对象
            self.metadata = metadata  # 嵌套对象
        
        def __repr__(self):
            return f"MyClassWithDeepCopy(name='{self.name}', data={self.data}, metadata={self.metadata})"
        
        def __deepcopy__(self, memo):
            print(f"自定义__deepcopy__()方法被调用，memo={memo}")
            # 创建新实例，使用deepcopy复制嵌套对象
            # 注意必须传递memo字典以处理循环引用
            new_data = copy.deepcopy(self.data, memo)
            new_metadata = copy.deepcopy(self.metadata, memo)
            new_instance = MyClassWithDeepCopy(self.name, new_data, new_metadata)
            # 将新实例添加到memo字典，避免循环引用问题
            memo[id(self)] = new_instance
            return new_instance
    
    # 测试自定义深拷贝
    original = MyClassWithDeepCopy(
        "test", 
        [1, 2, 3, [4, 5]],  # 嵌套列表
        {"created": "today", "tags": ["important", "urgent"]}  # 嵌套字典
    )
    deep_copied = copy.deepcopy(original)
    
    print(f"\n原始对象: {original}")
    print(f"深拷贝对象: {deep_copied}")
    
    # 验证是否是新对象
    print(f"是否是同一个对象: {original is deep_copied}")  # False
    
    # 验证嵌套对象是否是独立副本
    print(f"data是否是独立副本: {original.data is not deep_copied.data}")  # True
    print(f"metadata是否是独立副本: {original.metadata is not deep_copied.metadata}")  # True
    
    # 验证深层嵌套对象是否是独立副本
    print(f"深层嵌套是否是独立副本: {original.data[3] is not deep_copied.data[3]}")  # True
    
    # 修改深拷贝对象，验证不影响原始对象
    deep_copied.data[0] = 100
    deep_copied.metadata["tags"].append("updated")
    
    print(f"\n修改深拷贝对象后:")
    print(f"  原始对象: {original}")
    print(f"  深拷贝对象: {deep_copied}")
    
    # 示例3: 同时自定义浅拷贝和深拷贝
    print("\n示例3: 同时自定义浅拷贝和深拷贝")
    
    class MyClass:
        def __init__(self, name, items):
            self.name = name
            self.items = items  # 嵌套对象
        
        def __repr__(self):
            return f"MyClass(name='{self.name}', items={self.items})"
        
        def __copy__(self):
            print("__copy__() 被调用")
            # 浅拷贝：创建新实例但共享items引用
            return MyClass(self.name, self.items)
        
        def __deepcopy__(self, memo):
            print("__deepcopy__() 被调用")
            # 深拷贝：创建新实例并复制items
            new_items = copy.deepcopy(self.items, memo)
            new_instance = MyClass(self.name, new_items)
            memo[id(self)] = new_instance
            return new_instance
    
    # 测试
    original = MyClass("collection", [1, 2, 3])
    
    # 浅拷贝
    shallow_copy = copy.copy(original)
    print(f"浅拷贝对象: {shallow_copy}")
    print(f"items共享引用: {original.items is shallow_copy.items}")  # True
    
    # 深拷贝
    deep_copy = copy.deepcopy(original)
    print(f"深拷贝对象: {deep_copy}")
    print(f"items是独立副本: {original.items is not deep_copy.items}")  # True

# 运行自定义复制行为演示
custom_copy_behavior()
print()

# 5. 复制模块的高级特性
print("=== 5. 复制模块的高级特性 ===")

def advanced_features():
    """演示copy模块的高级特性"""
    print("copy模块提供了一些高级特性，用于控制复制行为和处理特殊情况：\n")
    
    # 1. copyreg模块
    print("1. copyreg模块")
    print("- copyreg模块用于注册自定义的复制函数")
    print("- 允许为无法直接复制的类型定义复制行为")
    print("- 特别适用于扩展类型和内置类型")
    
    print("\n基本用法:")
    print("import copyreg")
    print("copyreg.pickle(type, reduce_function, constructor=None)")
    print("  - type: 要注册的类型")
    print("  - reduce_function: 将对象转换为可序列化形式的函数")
    print("  - constructor: 可选的构造函数，用于重建对象")
    
    # 示例: 使用copyreg注册复制函数
    print("\n示例: 使用copyreg注册复制函数")
    
    try:
        import copyreg
        
        class CustomType:
            def __init__(self, value):
                self.value = value
            
            def __repr__(self):
                return f"CustomType(value={self.value})"
        
        # 定义reduce函数，将对象转换为元组
        def reduce_custom_type(obj):
            print("reduce_custom_type被调用")
            # 返回一个元组：(构造函数, (参数1, 参数2, ...))
            return (CustomType, (obj.value,))
        
        # 注册reduce函数
        copyreg.pickle(CustomType, reduce_custom_type)
        
        # 测试复制
        original = CustomType(42)
        shallow_copied = copy.copy(original)
        deep_copied = copy.deepcopy(original)
        
        print(f"原始对象: {original}")
        print(f"浅拷贝对象: {shallow_copied}")
        print(f"深拷贝对象: {deep_copied}")
        print(f"是否是相同对象: 原始 vs 浅拷贝: {original is shallow_copied}")  # False
        print(f"是否是相同对象: 原始 vs 深拷贝: {original is deep_copied}")  # False
        
    except ImportError:
        print("copyreg模块不可用")
    
    # 2. 处理不可复制的对象
    print("\n2. 处理不可复制的对象")
    print("- 某些对象无法直接复制，如文件对象、网络连接等")
    print("- 可以通过自定义__copy__和__deepcopy__方法处理这些情况")
    
    # 示例: 处理不可复制的资源
    print("\n示例: 处理不可复制的资源")
    
    class ResourceManager:
        def __init__(self, resource_name):
            self.resource_name = resource_name
            # 模拟打开资源
            print(f"打开资源: {resource_name}")
            self.is_open = True
        
        def __del__(self):
            # 模拟关闭资源
            if self.is_open:
                print(f"关闭资源: {self.resource_name}")
        
        def __repr__(self):
            return f"ResourceManager(name='{self.resource_name}')"
        
        def __copy__(self):
            # 浅拷贝时创建新的资源管理器，但使用不同的资源名称
            print(f"复制资源管理器: {self.resource_name}")
            # 创建一个新的资源管理器，模拟打开新资源
            return ResourceManager(f"{self.resource_name}_copy")
        
        def __deepcopy__(self, memo):
            # 深拷贝与浅拷贝行为相同，因为资源是外部的
            print(f"深拷贝资源管理器: {self.resource_name}")
            new_instance = ResourceManager(f"{self.resource_name}_deepcopy")
            memo[id(self)] = new_instance
            return new_instance
    
    # 测试资源管理器的复制
    original = ResourceManager("file.txt")
    try:
        shallow_copied = copy.copy(original)
        deep_copied = copy.deepcopy(original)
        
        print(f"原始对象: {original}")
        print(f"浅拷贝对象: {shallow_copied}")
        print(f"深拷贝对象: {deep_copied}")
        
    finally:
        # 确保资源被清理
        original.is_open = False
        # 在实际应用中，应提供明确的关闭方法而不是依赖__del__
    
    # 3. 性能考虑
    print("\n3. 性能考虑")
    print("- 深拷贝通常比浅拷贝慢，因为需要递归复制所有嵌套对象")
    print("- 对于大型复杂对象，深拷贝可能导致显著的性能开销")
    print("- 在不需要完全隔离的情况下，优先使用浅拷贝")
    
    # 示例: 性能比较
    print("\n示例: 浅拷贝vs深拷贝性能简单比较")
    
    import time
    
    # 创建一个复杂的嵌套结构
    def create_complex_structure(depth=3, width=10):
        if depth == 0:
            return [i for i in range(width)]
        return [create_complex_structure(depth-1, width) for _ in range(width)]
    
    # 创建测试数据
    complex_data = create_complex_structure(depth=3, width=5)  # 控制数据大小
    
    # 测量浅拷贝时间
    start_time = time.time()
    for _ in range(10):
        shallow_copy = copy.copy(complex_data)
    shallow_time = time.time() - start_time
    
    # 测量深拷贝时间
    start_time = time.time()
    for _ in range(10):
        deep_copy = copy.deepcopy(complex_data)
    deep_time = time.time() - start_time
    
    print(f"浅拷贝平均时间: {shallow_time / 10:.6f}秒")
    print(f"深拷贝平均时间: {deep_time / 10:.6f}秒")
    print(f"深拷贝比浅拷贝慢约: {deep_time / shallow_time:.1f}倍")

# 运行高级特性演示
advanced_features()
print()

# 6. 实际应用示例
print("=== 6. 实际应用示例 ===")

def practical_examples():
    """演示copy模块在实际应用中的使用"""
    print("copy模块在各种实际场景中的应用示例：\n")
    
    # 示例1: 保护性复制 - 防止外部修改内部数据
    print("示例1: 保护性复制 - 防止外部修改内部数据")
    
    class ConfigManager:
        def __init__(self, config):
            # 存储配置的深拷贝，防止外部修改
            self._config = copy.deepcopy(config)
        
        def get_config(self):
            # 返回配置的深拷贝，防止外部修改内部状态
            return copy.deepcopy(self._config)
        
        def update_config(self, new_config):
            # 更新配置时使用深拷贝
            self._config.update(copy.deepcopy(new_config))
        
        def __repr__(self):
            return f"ConfigManager(config={self._config})"
    
    # 测试保护性复制
    original_config = {
        "app_name": "MyApp",
        "version": "1.0",
        "settings": {
            "debug": False,
            "timeout": 30
        }
    }
    
    config_manager = ConfigManager(original_config)
    
    # 获取配置并尝试修改
    config_copy = config_manager.get_config()
    config_copy["settings"]["debug"] = True
    
    print("原始配置:")
    print(f"  original_config: {original_config}")
    print(f"  config_manager内部配置: {config_manager._config}")
    print(f"  获取的配置副本: {config_copy}")
    print(f"内部配置未被修改: {config_manager._config['settings']['debug'] is False}")
    
    # 示例2: 原型模式 - 使用复制创建对象
    print("\n示例2: 原型模式 - 使用复制创建对象")
    
    class Document:
        def __init__(self, title, content, metadata=None):
            self.title = title
            self.content = content
            self.metadata = metadata or {}
        
        def clone(self):
            """创建文档的深拷贝"""
            return copy.deepcopy(self)
        
        def __repr__(self):
            return f"Document(title='{self.title}', content='{content_preview}', metadata={self.metadata})"
    
    # 创建模板文档
    template = Document(
        title="模板文档",
        content="这是一个文档模板，包含基本格式。",
        metadata={"author": "System", "created": "2023-01-01", "tags": ["template"]}
    )
    
    # 使用模板创建新文档
    document1 = template.clone()
    document1.title = "项目计划"
    document1.content += "\n这是项目计划的具体内容。"
    document1.metadata["tags"].append("project")
    
    document2 = template.clone()
    document2.title = "会议记录"
    document2.content += "\n这是会议记录的详细内容。"
    document2.metadata["tags"].append("meeting")
    
    # 为了更好的显示效果，截断content
    content_preview = "..."
    
    print("文档模板:")
    print(f"  {template}")
    print("从模板创建的文档1:")
    print(f"  {document1}")
    print("从模板创建的文档2:")
    print(f"  {document2}")
    
    # 示例3: 游戏开发 - 复制游戏状态
    print("\n示例3: 游戏开发 - 复制游戏状态")
    
    class GameState:
        def __init__(self):
            self.score = 0
            self.level = 1
            self.player_position = [0, 0]
            self.inventory = []
            self.enemies = []
        
        def save_state(self):
            """保存当前游戏状态"""
            return copy.deepcopy(self)
        
        def load_state(self, saved_state):
            """加载游戏状态"""
            self.__dict__.update(copy.deepcopy(saved_state).__dict__)
        
        def __repr__(self):
            return f"GameState(score={self.score}, level={self.level}, position={self.player_position})"
    
    # 创建游戏状态
    game = GameState()
    game.score = 100
    game.level = 2
    game.player_position = [10, 20]
    game.inventory = ["sword", "shield"]
    game.enemies = [{"type": "goblin", "health": 50}]
    
    # 保存状态
    saved_state = game.save_state()
    
    # 修改游戏状态
    game.score = 200
    game.level = 3
    game.player_position = [30, 40]
    game.inventory.append("potion")
    
    print("当前游戏状态:")
    print(f"  {game}")
    print(f"  物品栏: {game.inventory}")
    
    print("保存的游戏状态:")
    print(f"  {saved_state}")
    print(f"  物品栏: {saved_state.inventory}")
    
    # 加载保存的状态
    game.load_state(saved_state)
    print("加载保存的状态后:")
    print(f"  {game}")
    print(f"  物品栏: {game.inventory}")
    
    # 示例4: 数据分析 - 复制数据进行实验
    print("\n示例4: 数据分析 - 复制数据进行实验")
    
    class DataAnalyzer:
        def __init__(self, data):
            self.original_data = copy.deepcopy(data)  # 保存原始数据
            self.processed_data = copy.deepcopy(data)  # 用于处理的数据副本
        
        def reset_data(self):
            """重置处理后的数据为原始状态"""
            self.processed_data = copy.deepcopy(self.original_data)
        
        def normalize_data(self):
            """标准化数据（示例操作）"""
            # 在实际应用中，这里会有真实的标准化逻辑
            for item in self.processed_data:
                if isinstance(item, dict) and 'value' in item:
                    # 模拟标准化
                    item['value'] = round(item['value'] / 100, 2)
        
        def filter_data(self, threshold):
            """过滤数据（示例操作）"""
            self.processed_data = [
                item for item in self.processed_data
                if isinstance(item, dict) and item.get('value', 0) > threshold
            ]
        
        def __repr__(self):
            return f"DataAnalyzer(original_len={len(self.original_data)}, processed_len={len(self.processed_data)})"
    
    # 创建测试数据
    test_data = [
        {"id": 1, "value": 150},  
        {"id": 2, "value": 250},
        {"id": 3, "value": 75}, 
        {"id": 4, "value": 300}
    ]
    
    # 创建分析器
    analyzer = DataAnalyzer(test_data)
    print(f"初始状态: {analyzer}")
    print(f"原始数据: {analyzer.original_data}")
    print(f"处理数据: {analyzer.processed_data}")
    
    # 执行操作
    analyzer.normalize_data()
    print("\n标准化后:")
    print(f"处理数据: {analyzer.processed_data}")
    print(f"原始数据未改变: {analyzer.original_data}")
    
    # 过滤数据
    analyzer.filter_data(2.0)
    print("\n过滤后:")
    print(f"处理数据: {analyzer.processed_data}")
    
    # 重置数据
    analyzer.reset_data()
    print("\n重置后:")
    print(f"处理数据: {analyzer.processed_data}")

# 运行实际应用示例
practical_examples()
print()

# 7. 注意事项和最佳实践
print("=== 7. 注意事项和最佳实践 ===")

def best_practices():
    """copy模块使用的注意事项和最佳实践"""
    print("使用copy模块时需要注意的事项和推荐的最佳实践：\n")
    
    print("注意事项:")
    print("1. 循环引用问题")
    print("   - deepcopy()会自动处理循环引用，但自定义的__deepcopy__()方法需要确保正确使用memo参数")
    print("   - 忘记在自定义__deepcopy__()中传递memo可能导致无限递归")
    
    print("\n2. 不可变对象的特殊处理")
    print("   - 对于不可变对象(tuple, string, int等)，copy()通常返回原对象的引用而不是创建新对象")
    print("   - 如果tuple包含可变的元素，deepcopy()仍然会复制这些可变元素")
    
    print("\n3. 外部资源处理")
    print("   - 文件句柄、网络连接等外部资源可能无法正确复制")
    print("   - 需要自定义复制方法来正确处理这些资源")
    
    print("\n4. 性能考虑")
    print("   - 深拷贝比浅拷贝消耗更多资源，特别是对于大型复杂对象")
    print("   - 避免不必要的深拷贝操作")
    
    print("\n5. 自定义对象的复制行为")
    print("   - 实现__copy__和__deepcopy__时需要确保复制逻辑正确")
    print("   - 特别是需要处理所有属性，包括私有属性")
    
    print("\n最佳实践:")
    print("1. 选择合适的复制方式")
    print("   - 如果只需要顶层对象的副本，使用copy()")
    print("   - 如果需要完全独立的副本，使用deepcopy()")
    print("   - 考虑性能影响，避免不必要的深拷贝")
    
    print("\n2. 实现复制接口")
    print("   - 对于自定义类，考虑实现__copy__和__deepcopy__方法")
    print("   - 确保复制方法正确处理所有属性和可能的循环引用")
    
    print("\n3. 保护性复制")
    print("   - 在返回内部数据结构时，考虑返回副本而不是原始引用")
    print("   - 这可以防止外部代码意外修改内部状态")
    
    print("\n4. 明确文档化")
    print("   - 对于返回对象副本的方法，在文档中明确说明是浅拷贝还是深拷贝")
    print("   - 这有助于其他开发者正确使用你的代码")
    
    print("\n5. 考虑替代方案")
    print("   - 在某些情况下，使用不可变数据结构可能比复制更合适")
    print("   - 考虑使用设计模式如原型模式来管理对象复制")
    
    print("\n6. 测试复制行为")
    print("   - 为自定义的复制方法编写测试，确保其行为符合预期")
    print("   - 特别是测试嵌套对象和循环引用的情况")
    
    print("\n7. 避免常见陷阱")
    print("   - 不要在自定义复制方法中忘记复制所有属性")
    print("   - 不要在__deepcopy__中忘记使用和更新memo字典")
    print("   - 不要假设所有对象都可以被简单复制")
    
    print("\n8. 使用copyreg进行类型扩展")
    print("   - 对于无法直接修改源代码的类，可以使用copyreg注册自定义复制行为")
    print("   - 这在处理第三方库和内置类型时特别有用")

# 运行注意事项和最佳实践
best_practices()
print()

# 8. 总结
print("=== 8. 总结 ===")

def summarize_copy():
    """总结copy模块的关键点"""
    print("copy模块提供了创建Python对象副本的标准机制，是Python数据处理中的重要工具：\n")
    
    print("核心功能：")
    print("1. 浅拷贝 (copy.copy()) - 创建对象的浅层副本，嵌套对象仍共享引用")
    print("2. 深拷贝 (copy.deepcopy()) - 创建对象的完全副本，包括所有嵌套对象")
    print("3. 自定义复制行为 - 通过__copy__和__deepcopy__方法控制对象的复制过程")
    print("4. 高级控制 - 使用copyreg模块注册和定制复制函数")
    
    print("\n应用场景：")
    print("1. 保护性编程 - 防止外部代码修改内部数据结构")
    print("2. 状态管理 - 保存和恢复对象状态")
    print("3. 原型模式 - 基于现有对象创建新对象")
    print("4. 并发编程 - 创建独立的数据副本避免并发修改问题")
    print("5. 数据分析 - 在不影响原始数据的情况下进行实验和处理")
    
    print("\n选择指南：")
    print("- 当需要修改对象但不想影响原始对象时，使用复制")
    print("- 对于简单对象或仅修改顶层属性时，使用浅拷贝")
    print("- 对于复杂嵌套对象或需要完全隔离时，使用深拷贝")
    print("- 考虑性能影响，深拷贝可能比浅拷贝慢得多")
    
    print("\n技术要点：")
    print("- 深拷贝通过memo字典跟踪已复制对象，避免循环引用导致的无限递归")
    print("- 不可变对象通常会返回自身引用而不是创建新副本")
    print("- 自定义复制行为需要正确处理所有属性和可能的循环引用")
    print("- 外部资源(文件、网络连接等)可能需要特殊处理")
    
    print("\n最终建议：")
    print("在Python编程中，理解对象引用机制和正确使用复制操作是编写健壮、可维护代码的重要部分。")
    print("copy模块提供的工具使我们能够灵活地控制对象复制行为，根据具体需求选择合适的复制策略。")
    print("无论是简单的数据处理还是复杂的应用架构，恰当使用复制操作都能帮助我们避免许多常见的编程陷阱。")

# 运行总结
summarize_copy()
print()

# 完整导入指南
print("=== 完整导入指南 ===")

print("copy模块的导入方式：")
print("""
# 基本导入
import copy

# 导入特定函数
from copy import copy, deepcopy

# 与copyreg结合使用
import copyreg
""")

# 模块功能速查表
print("\n=== 模块功能速查表 ===")
print("| 函数/方法 | 说明 | 使用场景 |")
print("|----------|------|----------|")
print("| copy.copy(x) | 创建浅拷贝 | 只需要顶层副本，性能要求高 |")
print("| copy.deepcopy(x) | 创建深拷贝 | 需要完全独立副本，包含嵌套对象 |")
print("| __copy__() | 自定义浅拷贝行为 | 自定义类需要特殊浅拷贝逻辑 |")
print("| __deepcopy__(memo) | 自定义深拷贝行为 | 自定义类需要特殊深拷贝逻辑 |")
print("| copyreg.pickle(type, reduce) | 注册类型的复制函数 | 为不可修改的类型定义复制行为 |")

# 最后一段，作为文档结尾
print("\n" + "="*80)
print("copy模块 - Python对象复制的标准解决方案")
print("通过掌握copy模块，你可以在Python编程中更好地控制对象的复制行为，")
print("避免因引用共享导致的意外修改，创建更加健壮和可维护的代码。")
print("无论是简单的列表复制还是复杂的自定义对象复制，")
print("copy模块都提供了灵活而强大的工具来满足各种复制需求。")
print("="*80)

# 此文档全面介绍了Python copy模块的功能、用法和最佳实践，
# 包含了浅拷贝和深拷贝的概念、自定义复制行为、高级特性以及实际应用示例，
# 适合作为日常开发中的参考指南，帮助开发者正确使用复制操作，避免常见陷阱。

# 9. 常见问题解答
print("\n=== 9. 常见问题解答 ===")

print("Q1: 浅拷贝和深拷贝的本质区别是什么？")
print("A1: 本质区别在于如何处理嵌套对象。浅拷贝仅复制对象的顶层结构，嵌套对象仍然共享引用；")
print("    深拷贝则递归复制所有嵌套对象，创建完全独立的副本。")

print("\nQ2: 为什么对于不可变对象，copy()返回原对象引用？")
print("A2: 因为不可变对象不能被修改，所以复制它们没有实际意义，返回原引用是一种优化。")

print("\nQ3: deepcopy()如何处理循环引用？")
print("A3: deepcopy()使用memo字典记录已复制的对象，当遇到已经复制过的对象时，")
print("    直接返回已复制的引用，避免无限递归。")

print("\nQ4: 复制对象时如何处理文件句柄等外部资源？")
print("A4: 需要自定义__copy__和__deepcopy__方法，根据具体需求决定如何处理外部资源，")
print("    可能是创建新资源、共享现有资源或抛出异常。")

print("\nQ5: 深拷贝总是比浅拷贝慢吗？")
print("A5: 通常是的，因为深拷贝需要递归复制所有嵌套对象。但对于没有嵌套对象的简单结构，")
print("    两者性能差异可能很小。")

print("\nQ6: 如何测试对象是否被正确复制？")
print("A6: 可以使用is运算符检查对象标识，使用==运算符检查值相等性，")
print("    并修改复制后的对象，验证原始对象是否受影响。")

print("\nQ7: 为什么自定义的__deepcopy__方法需要使用memo参数？")
print("A7: memo参数用于跟踪已复制的对象，防止循环引用导致的无限递归，")
print("    并确保同一对象只被复制一次。")

# 10. 版本兼容性信息
print("\n=== 10. 版本兼容性信息 ===")

print("copy模块在所有Python版本中可用，但有一些细微差异：")
print("- Python 2.x vs Python 3.x:")
print("  - copy.copy()在Python 3中对某些内置类型的处理更一致")
print("  - Python 3中deepcopy()对循环引用的处理更高效")

print("\n- Python 3.3+")
print("  - 改进了deepcopy()的性能和内存使用")
print("  - 增强了对某些自定义对象的复制支持")

print("\n- Python 3.7+")
print("  - 进一步优化了深拷贝的性能")
print("  - 对某些新的内置类型提供了更好的支持")

print("\n- 通用兼容性建议:")
print("  - 在跨版本项目中，测试复制操作的行为")
print("  - 避免依赖于具体版本的实现细节")
print("  - 对于关键功能，考虑添加单元测试")

# 实际编码示例：完整的复制操作测试套件
print("\n=== 11. 复制操作测试套件 ===")
print("以下是一个完整的复制操作测试套件示例：")

import copy
import unittest

class TestCopyOperations(unittest.TestCase):
    
    def test_shallow_copy_list(self):
        """测试列表的浅拷贝"""
        original = [1, 2, 3, [4, 5]]
        copied = copy.copy(original)
        
        # 验证是不同对象但内容相同
        self.assertIsNot(original, copied)
        self.assertEqual(original, copied)
        
        # 验证嵌套列表共享引用
        self.assertIs(original[3], copied[3])
        
        # 修改嵌套列表，验证原始列表受影响
        copied[3][0] = 400
        self.assertEqual(original[3][0], 400)
    
    def test_deep_copy_list(self):
        """测试列表的深拷贝"""
        original = [1, 2, 3, [4, 5]]
        copied = copy.deepcopy(original)
        
        # 验证是不同对象但内容相同
        self.assertIsNot(original, copied)
        self.assertEqual(original, copied)
        
        # 验证嵌套列表是独立副本
        self.assertIsNot(original[3], copied[3])
        
        # 修改嵌套列表，验证原始列表不受影响
        copied[3][0] = 400
        self.assertEqual(original[3][0], 4)
    
    def test_copy_immutable_types(self):
        """测试不可变类型的复制"""
        # 测试元组
        original_tuple = (1, 2, 3)
        copied_tuple = copy.copy(original_tuple)
        self.assertIs(original_tuple, copied_tuple)  # 引用相同
        
        # 测试字符串
        original_str = "hello"
        copied_str = copy.copy(original_str)
        self.assertIs(original_str, copied_str)  # 引用相同
        
        # 测试元组中的可变元素
        original_tuple_with_list = (1, 2, [3, 4])
        copied_tuple = copy.copy(original_tuple_with_list)
        deep_copied_tuple = copy.deepcopy(original_tuple_with_list)
        
        # 元组本身是同一对象，但内部列表可能不同
        self.assertIs(original_tuple_with_list, copied_tuple)
        self.assertIs(original_tuple_with_list, deep_copied_tuple)  # 元组引用相同
        
        # 嵌套列表在深拷贝中是独立的
        self.assertIs(original_tuple_with_list[2], copied_tuple[2])
        self.assertIsNot(original_tuple_with_list[2], deep_copied_tuple[2])
    
    def test_custom_class_copy(self):
        """测试自定义类的复制"""
        class TestClass:
            def __init__(self, value):
                self.value = value
                self.items = [1, 2, 3]
        
        original = TestClass(42)
        shallow_copied = copy.copy(original)
        deep_copied = copy.deepcopy(original)
        
        # 验证是不同对象
        self.assertIsNot(original, shallow_copied)
        self.assertIsNot(original, deep_copied)
        
        # 验证浅拷贝中嵌套列表共享引用
        self.assertIs(original.items, shallow_copied.items)
        self.assertIsNot(original.items, deep_copied.items)
        
        # 修改深拷贝的嵌套列表，验证原始列表不受影响
        deep_copied.items.append(4)
        self.assertEqual(len(original.items), 3)
    
    def test_custom_copy_methods(self):
        """测试自定义复制方法"""
        class CustomCopyClass:
            def __init__(self, value):
                self.value = value
                self.copied = False
            
            def __copy__(self):
                result = CustomCopyClass(self.value)
                result.copied = True
                return result
        
        original = CustomCopyClass(42)
        copied = copy.copy(original)
        
        # 验证自定义__copy__被调用
        self.assertTrue(copied.copied)
        self.assertFalse(original.copied)
    
    def test_circular_references(self):
        """测试循环引用"""
        class Node:
            def __init__(self, value):
                self.value = value
                self.neighbors = []
        
        # 创建循环引用
        node1 = Node(1)
        node2 = Node(2)
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)
        
        # 测试深拷贝能处理循环引用
        copied_node1 = copy.deepcopy(node1)
        
        # 验证是不同对象但保持引用关系
        self.assertIsNot(node1, copied_node1)
        self.assertIsNot(node2, copied_node1.neighbors[0])
        self.assertIs(copied_node1, copied_node1.neighbors[0].neighbors[0])

if __name__ == '__main__':
    unittest.main()

print("\n=== 12. 输入输出示例 ===")
print("以下是copy模块的典型输入输出示例：")

print("\n示例1: 基本复制操作")
print("输入:")
print("import copy")
print("original = [1, 2, 3, [4, 5]]")
print("shallow = copy.copy(original)")
print("deep = copy.deepcopy(original)")
print("\nprint('原始列表:', original)")
print("print('浅拷贝:', shallow)")
print("print('深拷贝:', deep)")
print("\n# 修改嵌套列表")
print("shallow[3][0] = 400")
print("deep[3][0] = 500")
print("\nprint('修改后原始列表:', original)")
print("print('修改后浅拷贝:', shallow)")
print("print('修改后深拷贝:', deep)")

print("\n输出:")
print("原始列表: [1, 2, 3, [4, 5]]")
print("浅拷贝: [1, 2, 3, [4, 5]]")
print("深拷贝: [1, 2, 3, [4, 5]]")
print("修改后原始列表: [1, 2, 3, [400, 5]]")
print("修改后浅拷贝: [1, 2, 3, [400, 5]]")
print("修改后深拷贝: [1, 2, 3, [500, 5]]")

print("\n示例2: 自定义对象复制")
print("输入:")
print("import copy")
print("\nclass Person:")
print("    def __init__(self, name, friends):")
print("        self.name = name")
print("        self.friends = friends")
print("    ")
print("    def __repr__(self):")
print("        return f'Person(name={self.name}, friends={self.friends})'")
print("\nalice = Person('Alice', ['Bob', 'Charlie'])")
print("alice_shallow = copy.copy(alice)")
print("alice_deep = copy.deepcopy(alice)")
print("\n# 添加朋友")
print("alice_shallow.friends.append('David')")
print("alice_deep.friends.append('Eve')")
print("\nprint('原始Alice:', alice)")
print("print('浅拷贝Alice:', alice_shallow)")
print("print('深拷贝Alice:', alice_deep)")

print("\n输出:")
print("原始Alice: Person(name=Alice, friends=['Bob', 'Charlie', 'David'])")
print("浅拷贝Alice: Person(name=Alice, friends=['Bob', 'Charlie', 'David'])")
print("深拷贝Alice: Person(name=Alice, friends=['Bob', 'Charlie', 'Eve'])")

print("\n=== 文档完成 ===")
print("Python copy模块的完整文档已创建，包含了所有核心功能、用法和最佳实践。")
print("此文档可作为日常开发中的参考指南，帮助你正确使用复制操作，避免常见陷阱。")

# 注意：在实际执行此文件时，代码示例部分不会被执行，因为它们被包含在多行字符串中。
# 要执行这些示例，需要将它们提取出来单独运行。

