# collections.abc模块 - 容器抽象基类
# 功能作用：提供各种容器类型的抽象基类，定义接口规范和共享功能
# 使用情景：创建自定义容器类、类型检查、协议验证、接口定义
# 注意事项：从Python 3.3开始，抽象基类从collections移至collections.abc子模块；实现抽象方法时必须严格遵循接口规范；可以使用register()方法将具体类注册为抽象基类的虚拟子类

import collections.abc
from abc import abstractmethod, ABC
import inspect
from typing import Any, Callable, Generator, Iterator, List, Mapping, MutableMapping, Sequence, Set, Tuple, Type, Union

# 模块概述
"""
collections.abc模块定义了一系列抽象基类(ABC)，这些类用于表示Python中各种容器类型的接口规范。

抽象基类的主要作用：

1. **接口定义**：规定了特定类型的容器应该实现哪些方法
2. **类型检查**：提供了更精确的isinstance()和issubclass()检查
3. **混入功能**：为具体实现提供共享方法
4. **代码清晰**：明确表达类的设计意图和行为

该模块中的抽象基类分为几个主要类别：

1. **容器基类**：提供__contains__方法的实现
2. **迭代器基类**：提供__iter__和__next__方法的接口
3. **序列基类**：如Sequence, MutableSequence
4. **映射基类**：如Mapping, MutableMapping
5. **集合基类**：如Set, MutableSet
6. **可调用基类**：如Callable
7. **其他特殊基类**：如Hashable, Sized, Iterable

collections.abc模块适用于需要定义或扩展容器类型、实现协议、进行精确类型检查等场景。
"""

# 1. 基本抽象基类
print("=== 1. 基本抽象基类 ===")

def basic_abc_classes():
    """演示collections.abc中的基本抽象基类"""
    print("collections.abc中的基本抽象基类定义了容器的核心接口：\n")
    
    # 1. Container - 可包含元素的容器
    print("1. collections.abc.Container")
    print("   - 提供__contains__方法的接口")
    print("   - 用于实现'item in container'操作")
    print("   - 要求实现: __contains__(self, item)")
    
    # 检查内置类型是否为Container的实例
    container_examples = [
        ("list", [1, 2, 3]),
        ("tuple", (1, 2, 3)),
        ("set", {1, 2, 3}),
        ("dict", {1: "a", 2: "b"}),
        ("str", "abc"),
        ("generator", (x for x in range(3))),
    ]
    
    print("   内置类型是否为Container实例：")
    for name, example in container_examples:
        is_container = isinstance(example, collections.abc.Container)
        print(f"     {name:10}: {'是' if is_container else '否'} {'(可使用in操作符)' if is_container else ''}")
    
    # 2. Sized - 可获取大小的容器
    print("\n2. collections.abc.Sized")
    print("   - 提供__len__方法的接口")
    print("   - 用于实现'len(container)'操作")
    print("   - 要求实现: __len__(self)")
    
    # 检查内置类型是否为Sized的实例
    sized_examples = [
        ("list", [1, 2, 3]),
        ("tuple", (1, 2, 3)),
        ("set", {1, 2, 3}),
        ("dict", {1: "a", 2: "b"}),
        ("str", "abc"),
        ("range", range(5)),
        ("generator", (x for x in range(3))),
    ]
    
    print("   内置类型是否为Sized实例：")
    for name, example in sized_examples:
        is_sized = isinstance(example, collections.abc.Sized)
        print(f"     {name:10}: {'是' if is_sized else '否'} {'(可使用len()函数)' if is_sized else ''}")
    
    # 3. Iterable - 可迭代的对象
    print("\n3. collections.abc.Iterable")
    print("   - 提供__iter__方法的接口")
    print("   - 用于实现迭代功能")
    print("   - 要求实现: __iter__(self)")
    print("   - 返回: 一个迭代器")
    
    # 检查内置类型是否为Iterable的实例
    iterable_examples = [
        ("list", [1, 2, 3]),
        ("tuple", (1, 2, 3)),
        ("set", {1, 2, 3}),
        ("dict", {1: "a", 2: "b"}),
        ("str", "abc"),
        ("range", range(5)),
        ("generator", (x for x in range(3))),
        ("file-like", open("temp.txt", "w")) if __name__ == "__main__" else ("file-like", "文件对象"),
    ]
    
    print("   内置类型是否为Iterable实例：")
    for name, example in iterable_examples:
        if name == "file-like" and isinstance(example, str):
            print(f"     {name:10}: 是 (文件对象可迭代)")
            continue
            
        is_iterable = isinstance(example, collections.abc.Iterable)
        print(f"     {name:10}: {'是' if is_iterable else '否'} {'(可在for循环中使用)' if is_iterable else ''}")
    
    # 如果创建了临时文件，关闭它
    if iterable_examples and iterable_examples[-1][0] == "file-like" and not isinstance(iterable_examples[-1][1], str):
        iterable_examples[-1][1].close()
        import os
        os.remove("temp.txt")
    
    # 4. Iterator - 迭代器
    print("\n4. collections.abc.Iterator")
    print("   - 继承自Iterable，提供__next__方法的接口")
    print("   - 代表一个迭代器对象")
    print("   - 要求实现: __next__(self)")
    print("   - 返回: 下一个元素，如果迭代结束则抛出StopIteration异常")
    
    # 检查内置类型是否为Iterator的实例
    iterator_examples = [
        ("list iterator", iter([1, 2, 3])),
        ("tuple iterator", iter((1, 2, 3))),
        ("set iterator", iter({1, 2, 3})),
        ("dict iterator", iter({1: "a", 2: "b"})),
        ("string iterator", iter("abc")),
        ("range iterator", iter(range(5))),
        ("generator", (x for x in range(3))),
    ]
    
    print("   内置类型是否为Iterator实例：")
    for name, example in iterator_examples:
        is_iterator = isinstance(example, collections.abc.Iterator)
        print(f"     {name:15}: {'是' if is_iterator else '否'} {'(可使用next()函数)' if is_iterator else ''}")
    
    print("\n   Iterable和Iterator的区别:")
    print("     - Iterable: 可被迭代的对象，通过iter()获取迭代器")
    print("     - Iterator: 迭代器本身，可通过next()获取下一个元素")
    print("     - 所有Iterator都是Iterable，但不是所有Iterable都是Iterator")
    
    # 5. Hashable - 可哈希对象
    print("\n5. collections.abc.Hashable")
    print("   - 提供__hash__方法的接口")
    print("   - 用于实现可哈希的对象")
    print("   - 可哈希对象可以作为字典键或加入集合")
    print("   - 要求实现: __hash__(self)")
    
    # 检查内置类型是否为Hashable的实例
    hashable_examples = [
        ("int", 42),
        ("float", 3.14),
        ("str", "abc"),
        ("tuple", (1, 2, 3)),
        ("list", [1, 2, 3]),
        ("set", {1, 2, 3}),
        ("dict", {1: "a", 2: "b"}),
    ]
    
    print("   内置类型是否为Hashable实例：")
    for name, example in hashable_examples:
        try:
            # 尝试获取哈希值
            hash_value = hash(example)
            is_hashable = isinstance(example, collections.abc.Hashable)
            print(f"     {name:10}: {'是' if is_hashable else '否'} {'(哈希值:' + str(hash_value)[:8] + '...)' if is_hashable else ''}")
        except TypeError:
            print(f"     {name:10}: 否 (不可哈希)")

# 运行基本抽象基类演示
basic_abc_classes()
print()

# 2. 序列抽象基类
print("=== 2. 序列抽象基类 ===")

def sequence_abc_classes():
    """演示collections.abc中的序列抽象基类"""
    print("collections.abc中的序列抽象基类用于定义有序集合的接口：\n")
    
    # 1. Sequence - 不可变序列
    print("1. collections.abc.Sequence")
    print("   - 继承自Sized, Iterable, Container")
    print("   - 定义了不可变序列的接口")
    print("   - 要求实现:")
    print("     * __getitem__(self, index)")
    print("     * __len__(self)")
    print("   - 自动提供:")
    print("     * __contains__ (通过__getitem__和__len__实现)")
    print("     * __iter__ (通过__getitem__实现)")
    print("     * __reversed__ (通过__getitem__和__len__实现)")
    print("     * index (通过__getitem__和__len__实现)")
    print("     * count (通过__getitem__和__len__实现)")
    
    # 检查内置类型是否为Sequence的实例
    sequence_examples = [
        ("list", [1, 2, 3]),
        ("tuple", (1, 2, 3)),
        ("str", "abc"),
        ("range", range(5)),
        ("set", {1, 2, 3}),
        ("dict", {1: "a", 2: "b"}),
    ]
    
    print("   内置类型是否为Sequence实例：")
    for name, example in sequence_examples:
        is_sequence = isinstance(example, collections.abc.Sequence)
        print(f"     {name:10}: {'是' if is_sequence else '否'} {'(支持索引访问)' if is_sequence else ''}")
    
    # 2. MutableSequence - 可变序列
    print("\n2. collections.abc.MutableSequence")
    print("   - 继承自Sequence")
    print("   - 定义了可变序列的接口")
    print("   - 要求实现Sequence的所有方法，以及:")
    print("     * __setitem__(self, index, value)")
    print("     * __delitem__(self, index)")
    print("     * insert(self, index, value)")
    print("   - 自动提供:")
    print("     * append")
    print("     * clear")
    print("     * extend")
    print("     * pop")
    print("     * remove")
    print("     * reverse")
    print("     * __iadd__")
    
    # 检查内置类型是否为MutableSequence的实例
    mutable_sequence_examples = [
        ("list", [1, 2, 3]),
        ("tuple", (1, 2, 3)),
        ("str", "abc"),
        ("range", range(5)),
    ]
    
    print("   内置类型是否为MutableSequence实例：")
    for name, example in mutable_sequence_examples:
        is_mutable = isinstance(example, collections.abc.MutableSequence)
        print(f"     {name:10}: {'是' if is_mutable else '否'} {'(支持元素修改)' if is_mutable else ''}")
    
    # 3. 自定义序列实现示例
    print("\n3. 自定义序列实现示例")
    print("   实现一个简单的不可变序列：")
    
    class CustomSequence(collections.abc.Sequence):
        """自定义不可变序列示例"""
        def __init__(self, data):
            self._data = list(data)  # 存储为内部列表
        
        def __getitem__(self, index):
            return self._data[index]
        
        def __len__(self):
            return len(self._data)
    
    # 创建并测试自定义序列
    custom_seq = CustomSequence([1, 2, 3, 4, 5])
    
    print("   测试自定义序列:")
    print(f"     长度: {len(custom_seq)}")
    print(f"     索引访问: {custom_seq[2]}")
    print(f"     切片访问: {custom_seq[1:4]}")
    print(f"     成员检查: {'3' in custom_seq if isinstance(custom_seq[0], str) else 3 in custom_seq}")
    print(f"     迭代测试: {list(custom_seq)}")
    print(f"     索引方法: {custom_seq.index(3) if 3 in custom_seq else custom_seq.index('3')}")
    print(f"     计数方法: {custom_seq.count(1)}")
    
    print("\n   实现一个简单的可变序列：")
    
    class CustomMutableSequence(collections.abc.MutableSequence):
        """自定义可变序列示例"""
        def __init__(self, data):
            self._data = list(data)
        
        def __getitem__(self, index):
            return self._data[index]
        
        def __setitem__(self, index, value):
            self._data[index] = value
        
        def __delitem__(self, index):
            del self._data[index]
        
        def __len__(self):
            return len(self._data)
        
        def insert(self, index, value):
            self._data.insert(index, value)
    
    # 创建并测试自定义可变序列
    custom_mutable = CustomMutableSequence([1, 2, 3, 4, 5])
    
    print("   测试自定义可变序列:")
    print(f"     修改前: {list(custom_mutable)}")
    custom_mutable[2] = 99  # 修改元素
    print(f"     修改后: {list(custom_mutable)}")
    custom_mutable.append(6)  # 测试自动提供的append方法
    print(f"     append后: {list(custom_mutable)}")
    custom_mutable.extend([7, 8])  # 测试自动提供的extend方法
    print(f"     extend后: {list(custom_mutable)}")
    popped = custom_mutable.pop(1)  # 测试自动提供的pop方法
    print(f"     pop(1)后: {list(custom_mutable)}, 弹出值: {popped}")
    custom_mutable.remove(4)  # 测试自动提供的remove方法
    print(f"     remove(4)后: {list(custom_mutable)}")

# 运行序列抽象基类演示
sequence_abc_classes()
print()

# 3. 映射抽象基类
print("=== 3. 映射抽象基类 ===")

def mapping_abc_classes():
    """演示collections.abc中的映射抽象基类"""
    print("collections.abc中的映射抽象基类用于定义键值对集合的接口：\n")
    
    # 1. Mapping - 不可变映射
    print("1. collections.abc.Mapping")
    print("   - 继承自Sized, Iterable, Container")
    print("   - 定义了不可变映射的接口")
    print("   - 要求实现:")
    print("     * __getitem__(self, key)")
    print("     * __iter__(self)")
    print("     * __len__(self)")
    print("   - 自动提供:")
    print("     * __contains__")
    print("     * keys")
    print("     * items")
    print("     * values")
    print("     * get")
    print("     * __eq__, __ne__")
    
    # 检查内置类型是否为Mapping的实例
    mapping_examples = [
        ("dict", {1: "a", 2: "b", 3: "c"}),
        ("set", {1, 2, 3}),
        ("list", [1, 2, 3]),
        ("tuple", (1, 2, 3)),
        ("frozenset", frozenset([1, 2, 3])),
    ]
    
    print("   内置类型是否为Mapping实例：")
    for name, example in mapping_examples:
        is_mapping = isinstance(example, collections.abc.Mapping)
        print(f"     {name:10}: {'是' if is_mapping else '否'} {'(支持键值访问)' if is_mapping else ''}")
    
    # 2. MutableMapping - 可变映射
    print("\n2. collections.abc.MutableMapping")
    print("   - 继承自Mapping")
    print("   - 定义了可变映射的接口")
    print("   - 要求实现Mapping的所有方法，以及:")
    print("     * __setitem__(self, key, value)")
    print("     * __delitem__(self, key)")
    print("   - 自动提供:")
    print("     * pop")
    print("     * popitem")
    print("     * clear")
    print("     * update")
    print("     * setdefault")
    
    # 检查内置类型是否为MutableMapping的实例
    mutable_mapping_examples = [
        ("dict", {1: "a", 2: "b", 3: "c"}),
    ]
    
    print("   内置类型是否为MutableMapping实例：")
    for name, example in mutable_mapping_examples:
        is_mutable = isinstance(example, collections.abc.MutableMapping)
        print(f"     {name:10}: {'是' if is_mutable else '否'} {'(支持键值修改)' if is_mutable else ''}")
    
    # 3. 自定义映射实现示例
    print("\n3. 自定义映射实现示例")
    print("   实现一个简单的不可变映射：")
    
    class CustomMapping(collections.abc.Mapping):
        """自定义不可变映射示例"""
        def __init__(self, data):
            self._data = dict(data)  # 内部存储为字典
        
        def __getitem__(self, key):
            if key not in self._data:
                raise KeyError(key)
            return self._data[key]
        
        def __iter__(self):
            return iter(self._data)
        
        def __len__(self):
            return len(self._data)
    
    # 创建并测试自定义映射
    custom_map = CustomMapping({1: "one", 2: "two", 3: "three"})
    
    print("   测试自定义映射:")
    print(f"     长度: {len(custom_map)}")
    print(f"     键访问: {custom_map[2]}")
    print(f"     成员检查: {2 in custom_map}")
    print(f"     迭代键: {list(iter(custom_map))}")
    print(f"     keys(): {list(custom_map.keys())}")
    print(f"     values(): {list(custom_map.values())}")
    print(f"     items(): {list(custom_map.items())}")
    print(f"     get()方法: {custom_map.get(4, 'not found')}")
    
    print("\n   实现一个简单的可变映射：")
    
    class CustomMutableMapping(collections.abc.MutableMapping):
        """自定义可变映射示例"""
        def __init__(self, data=None):
            self._data = dict(data or {})  # 内部存储为字典
        
        def __getitem__(self, key):
            if key not in self._data:
                raise KeyError(key)
            return self._data[key]
        
        def __setitem__(self, key, value):
            self._data[key] = value
        
        def __delitem__(self, key):
            if key not in self._data:
                raise KeyError(key)
            del self._data[key]
        
        def __iter__(self):
            return iter(self._data)
        
        def __len__(self):
            return len(self._data)
    
    # 创建并测试自定义可变映射
    custom_mutable_map = CustomMutableMapping({1: "one", 2: "two"})
    
    print("   测试自定义可变映射:")
    print(f"     初始状态: {dict(custom_mutable_map)}")
    custom_mutable_map[3] = "three"  # 添加键值对
    print(f"     添加后: {dict(custom_mutable_map)}")
    custom_mutable_map[1] = "ONE"  # 修改键值对
    print(f"     修改后: {dict(custom_mutable_map)}")
    custom_mutable_map.update({4: "four", 5: "five"})  # 使用自动提供的update方法
    print(f"     update后: {dict(custom_mutable_map)}")
    popped_value = custom_mutable_map.pop(2)  # 使用自动提供的pop方法
    print(f"     pop(2)后: {dict(custom_mutable_map)}, 弹出值: {popped_value}")
    del custom_mutable_map[3]  # 删除键值对
    print(f"     del后: {dict(custom_mutable_map)}")

# 运行映射抽象基类演示
mapping_abc_classes()
print()

# 4. 集合抽象基类
print("=== 4. 集合抽象基类 ===")

def set_abc_classes():
    """演示collections.abc中的集合抽象基类"""
    print("collections.abc中的集合抽象基类用于定义集合类型的接口：\n")
    
    # 1. Set - 不可变集合
    print("1. collections.abc.Set")
    print("   - 继承自Sized, Iterable, Container")
    print("   - 定义了不可变集合的接口")
    print("   - 要求实现:")
    print("     * __contains__(self, value)")
    print("     * __iter__(self)")
    print("     * __len__(self)")
    print("   - 自动提供:")
    print("     * isdisjoint")
    print("     * issubset")
    print("     * issuperset")
    print("     * __and__ (交集)")
    print("     * __or__ (并集)")
    print("     * __sub__ (差集)")
    print("     * __xor__ (对称差)")
    
    # 检查内置类型是否为Set的实例
    set_examples = [
        ("set", {1, 2, 3}),
        ("frozenset", frozenset([1, 2, 3])),
        ("list", [1, 2, 3]),
        ("tuple", (1, 2, 3)),
        ("dict", {1: "a", 2: "b", 3: "c"}),
    ]
    
    print("   内置类型是否为Set实例：")
    for name, example in set_examples:
        is_set = isinstance(example, collections.abc.Set)
        print(f"     {name:10}: {'是' if is_set else '否'} {'(集合类型)' if is_set else ''}")
    
    # 2. MutableSet - 可变集合
    print("\n2. collections.abc.MutableSet")
    print("   - 继承自Set")
    print("   - 定义了可变集合的接口")
    print("   - 要求实现Set的所有方法，以及:")
    print("     * add(self, value)")
    print("     * discard(self, value)")
    print("   - 自动提供:")
    print("     * clear")
    print("     * pop")
    print("     * remove")
    print("     * __ior__")
    print("     * __iand__")
    print("     * __ixor__")
    print("     * __isub__")
    
    # 检查内置类型是否为MutableSet的实例
    mutable_set_examples = [
        ("set", {1, 2, 3}),
        ("frozenset", frozenset([1, 2, 3])),
    ]
    
    print("   内置类型是否为MutableSet实例：")
    for name, example in mutable_set_examples:
        is_mutable = isinstance(example, collections.abc.MutableSet)
        print(f"     {name:10}: {'是' if is_mutable else '否'} {'(可变集合)' if is_mutable else ''}")
    
    # 3. 自定义集合实现示例
    print("\n3. 自定义集合实现示例")
    print("   实现一个简单的不可变集合：")
    
    class CustomSet(collections.abc.Set):
        """自定义不可变集合示例"""
        def __init__(self, elements):
            # 使用frozenset存储元素，确保不可变性
            self._elements = frozenset(elements)
        
        def __contains__(self, value):
            return value in self._elements
        
        def __iter__(self):
            return iter(self._elements)
        
        def __len__(self):
            return len(self._elements)
    
    # 创建并测试自定义集合
    custom_set = CustomSet([1, 2, 3, 2, 1])  # 注意重复元素
    
    print("   测试自定义集合:")
    print(f"     长度: {len(custom_set)}")
    print(f"     成员检查: {2 in custom_set}")
    print(f"     迭代测试: {list(custom_set)}")
    
    # 创建另一个集合进行集合操作测试
    custom_set2 = CustomSet([3, 4, 5])
    
    # 测试集合操作
    print(f"     交集: {set(custom_set & custom_set2)}")
    print(f"     并集: {set(custom_set | custom_set2)}")
    print(f"     差集: {set(custom_set - custom_set2)}")
    print(f"     对称差: {set(custom_set ^ custom_set2)}")
    print(f"     子集检查: {custom_set <= custom_set2}")
    print(f"     超集检查: {custom_set >= custom_set2}")
    
    print("\n   实现一个简单的可变集合：")
    
    class CustomMutableSet(collections.abc.MutableSet):
        """自定义可变集合示例"""
        def __init__(self, elements=None):
            # 使用set存储元素
            self._elements = set(elements or [])
        
        def __contains__(self, value):
            return value in self._elements
        
        def __iter__(self):
            return iter(self._elements)
        
        def __len__(self):
            return len(self._elements)
        
        def add(self, value):
            self._elements.add(value)
        
        def discard(self, value):
            self._elements.discard(value)
    
    # 创建并测试自定义可变集合
    custom_mutable_set = CustomMutableSet([1, 2, 3])
    
    print("   测试自定义可变集合:")
    print(f"     初始状态: {set(custom_mutable_set)}")
    custom_mutable_set.add(4)  # 添加元素
    print(f"     add(4)后: {set(custom_mutable_set)}")
    custom_mutable_set.discard(2)  # 删除元素
    print(f"     discard(2)后: {set(custom_mutable_set)}")
    custom_mutable_set.discard(999)  # 删除不存在的元素，不应报错
    print(f"     discard(不存在)后: {set(custom_mutable_set)}")
    
    # 测试自动提供的方法
    try:
        custom_mutable_set.remove(1)  # 使用自动提供的remove方法
        print(f"     remove(1)后: {set(custom_mutable_set)}")
    except KeyError as e:
        print(f"     remove不存在的元素: {e}")
    
    # 清空集合
    custom_mutable_set.clear()  # 使用自动提供的clear方法
    print(f"     clear()后: {set(custom_mutable_set)}")

# 运行集合抽象基类演示
set_abc_classes()
print()

# 5. 其他抽象基类
print("=== 5. 其他抽象基类 ===")

def other_abc_classes():
    """演示collections.abc中的其他抽象基类"""
    print("collections.abc中的其他抽象基类提供了更多特殊类型的接口：\n")
    
    # 1. Callable - 可调用对象
    print("1. collections.abc.Callable")
    print("   - 表示可调用的对象，如函数、方法、类等")
    print("   - 提供__call__方法的接口")
    print("   - 要求实现: __call__(self, *args, **kwargs)")
    
    # 检查各种可调用对象
    callable_examples = [
        ("函数", lambda x: x*2),
        ("内置函数", len),
        ("类", type),
        ("类实例(带__call__)", type("CallableClass", (), {"__call__": lambda self: None})()),
        ("列表", [1, 2, 3]),
        ("字典", {1: "a"}),
    ]
    
    print("   各种对象是否为Callable实例：")
    for name, example in callable_examples:
        is_callable = isinstance(example, collections.abc.Callable)
        print(f"     {name:15}: {'是' if is_callable else '否'} {'(可调用)' if is_callable else ''}")
    
    # 2. Awaitable - 可等待对象（协程相关）
    print("\n2. collections.abc.Awaitable")
    print("   - 表示可被await表达式等待的对象")
    print("   - 主要用于异步编程")
    print("   - 要求实现: __await__(self)")
    
    # 3. Coroutine - 协程对象
    print("\n3. collections.abc.Coroutine")
    print("   - 继承自Awaitable")
    print("   - 表示协程对象")
    print("   - 要求实现Awaitable的所有方法，以及:")
    print("     * send(self, value)")
    print("     * throw(self, typ, val=None, tb=None)")
    print("     * close(self)")
    
    # 4. AsyncIterable - 异步可迭代对象
    print("\n4. collections.abc.AsyncIterable")
    print("   - 表示支持异步迭代的对象")
    print("   - 要求实现: __aiter__(self)")
    print("   - 返回: 一个异步迭代器")
    
    # 5. AsyncIterator - 异步迭代器
    print("\n5. collections.abc.AsyncIterator")
    print("   - 继承自AsyncIterable")
    print("   - 表示异步迭代器对象")
    print("   - 要求实现: __anext__(self)")
    print("   - 返回: 一个awaitable对象")
    
    # 6. AsyncGenerator - 异步生成器
    print("\n6. collections.abc.AsyncGenerator")
    print("   - 继承自AsyncIterator")
    print("   - 表示异步生成器对象")
    print("   - 要求实现AsyncIterator的所有方法，以及:")
    print("     * asend(self, value)")
    print("     * athrow(self, typ, val=None, tb=None)")
    print("     * aclose(self)")
    
    # 7. 自定义可调用对象示例
    print("\n7. 自定义可调用对象示例")
    print("   实现一个简单的可调用类：")
    
    class Multiplier(collections.abc.Callable):
        """一个简单的乘法器类"""
        def __init__(self, factor):
            self.factor = factor
        
        def __call__(self, x):
            return x * self.factor
    
    # 创建并测试可调用对象
    doubler = Multiplier(2)  # 乘以2
    tripler = Multiplier(3)  # 乘以3
    
    print("   测试可调用类:")
    print(f"     doubler(5) = {doubler(5)}")
    print(f"     tripler(5) = {tripler(5)}")
    print(f"     是否为Callable: {isinstance(doubler, collections.abc.Callable)}")

# 运行其他抽象基类演示
other_abc_classes()
print()

# 6. 抽象基类的高级用法
print("=== 6. 抽象基类的高级用法 ===")

def advanced_abc_usage():
    """演示collections.abc中抽象基类的高级用法"""
    print("抽象基类的高级用法包括虚拟子类注册、抽象方法检查等：\n")
    
    # 1. 虚拟子类注册
    print("1. 虚拟子类注册")
    print("   - 使用register()方法将一个类注册为抽象基类的虚拟子类")
    print("   - 虚拟子类不需要继承自抽象基类")
    print("   - isinstance()和issubclass()将返回True")
    
    # 定义一个普通类
    class RegularClass:
        """一个普通类，不继承自任何抽象基类"""
        def __init__(self, data):
            self.data = list(data)
        
        def __getitem__(self, index):
            return self.data[index]
        
        def __len__(self):
            return len(self.data)
    
    # 检查是否为Sequence的实例或子类
    print("   注册前:")
    print(f"     isinstance(RegularClass([1,2,3]), collections.abc.Sequence): {isinstance(RegularClass([1,2,3]), collections.abc.Sequence)}")
    print(f"     issubclass(RegularClass, collections.abc.Sequence): {issubclass(RegularClass, collections.abc.Sequence)}")
    
    # 注册为虚拟子类
    collections.abc.Sequence.register(RegularClass)
    
    print("   注册后:")
    print(f"     isinstance(RegularClass([1,2,3]), collections.abc.Sequence): {isinstance(RegularClass([1,2,3]), collections.abc.Sequence)}")
    print(f"     issubclass(RegularClass, collections.abc.Sequence): {issubclass(RegularClass, collections.abc.Sequence)}")
    
    # 2. 装饰器形式注册
    print("\n2. 装饰器形式注册")
    print("   - 使用@abstractmethod装饰器定义抽象方法")
    print("   - 使用@register装饰器注册虚拟子类")
    
    # 定义一个自定义抽象基类
    class MyABC(ABC):
        @abstractmethod
        def do_something(self):
            pass
    
    # 使用装饰器注册虚拟子类
    @MyABC.register
    class ConcreteClass:
        def do_something(self):
            return "I did something!"
    
    print("   测试装饰器注册:")
    print(f"     issubclass(ConcreteClass, MyABC): {issubclass(ConcreteClass, MyABC)}")
    print(f"     isinstance(ConcreteClass(), MyABC): {isinstance(ConcreteClass(), MyABC)}")
    
    # 3. 抽象方法检查
    print("\n3. 抽象方法检查")
    print("   - 抽象基类确保子类实现了所有必需的抽象方法")
    print("   - 尝试实例化未实现所有抽象方法的子类会引发TypeError")
    
    class MyAbstractClass(ABC):
        @abstractmethod
        def required_method(self):
            pass
        
        def optional_method(self):
            """可选方法，提供默认实现"""
            return "Default implementation"
    
    # 尝试定义一个未实现抽象方法的子类
    class IncompleteImplementation(MyAbstractClass):
        # 没有实现required_method
        pass
    
    # 定义一个完整实现的子类
    class CompleteImplementation(MyAbstractClass):
        def required_method(self):
            return "Implemented!"
    
    print("   测试抽象方法实现检查:")
    try:
        instance = IncompleteImplementation()
        print("     错误: 应该无法实例化不完整的实现")
    except TypeError as e:
        print(f"     正确: {str(e)}")
    
    try:
        instance = CompleteImplementation()
        print(f"     正确: 可以实例化完整的实现")
        print(f"     调用必需方法: {instance.required_method()}")
        print(f"     调用可选方法: {instance.optional_method()}")
    except TypeError as e:
        print(f"     错误: {str(e)}")
    
    # 4. 子类化内置集合类型 vs 使用抽象基类
    print("\n4. 子类化内置集合类型 vs 使用抽象基类")
    print("   示例: 实现一个带计数器的列表")
    
    # 方式1: 子类化内置list
    class CountingList(list):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._access_count = 0
        
        def __getitem__(self, index):
            self._access_count += 1
            return super().__getitem__(index)
        
        def get_access_count(self):
            return self._access_count
    
    # 方式2: 使用MutableSequence抽象基类
    class CountingSequence(collections.abc.MutableSequence):
        def __init__(self, data=None):
            self._data = list(data or [])
            self._access_count = 0
        
        def __getitem__(self, index):
            self._access_count += 1
            return self._data[index]
        
        def __setitem__(self, index, value):
            self._data[index] = value
        
        def __delitem__(self, index):
            del self._data[index]
        
        def __len__(self):
            return len(self._data)
        
        def insert(self, index, value):
            self._data.insert(index, value)
        
        def get_access_count(self):
            return self._access_count
    
    # 测试两种实现
    print("   测试CountingList (内置list子类):")
    clist = CountingList([1, 2, 3, 4, 5])
    print(f"     初始列表: {clist}")
    print(f"     访问clist[2]: {clist[2]}")
    print(f"     访问计数: {clist.get_access_count()}")
    print(f"     是否为list实例: {isinstance(clist, list)}")
    print(f"     是否为MutableSequence实例: {isinstance(clist, collections.abc.MutableSequence)}")
    
    print("\n   测试CountingSequence (MutableSequence实现):")
    cseq = CountingSequence([1, 2, 3, 4, 5])
    print(f"     初始列表: {list(cseq)}")
    print(f"     访问cseq[2]: {cseq[2]}")
    print(f"     访问计数: {cseq.get_access_count()}")
    print(f"     是否为list实例: {isinstance(cseq, list)}")
    print(f"     是否为MutableSequence实例: {isinstance(cseq, collections.abc.MutableSequence)}")
    
    print("\n   比较:")
    print("     - 子类化内置类型: 更简单，但可能会继承一些不需要的行为")
    print("     - 使用抽象基类: 更严格，需要实现所有必需方法，但行为更可控")
    print("     - 抽象基类提供了更清晰的接口规范和文档")
    
    # 5. 协议实现检查
    print("\n5. 协议实现检查")
    print("   - 使用collections.abc检查对象是否实现了特定协议")
    print("   - 例如，检查对象是否可迭代、可哈希、是否支持索引等")
    
    # 定义一些测试对象
    test_objects = {
        "列表": [1, 2, 3],
        "元组": (1, 2, 3),
        "集合": {1, 2, 3},
        "字典": {1: "a", 2: "b"},
        "字符串": "abc",
        "生成器": (x for x in range(3)),
        "迭代器": iter([1, 2, 3]),
    }
    
    # 定义要检查的协议
    protocols = [
        ("可迭代", collections.abc.Iterable),
        ("迭代器", collections.abc.Iterator),
        ("序列", collections.abc.Sequence),
        ("可变序列", collections.abc.MutableSequence),
        ("映射", collections.abc.Mapping),
        ("集合", collections.abc.Set),
        ("可哈希", collections.abc.Hashable),
    ]
    
    print("   测试各种对象实现的协议:")
    for name, obj in test_objects.items():
        implemented = []
        for proto_name, proto_class in protocols:
            try:
                if isinstance(obj, proto_class):
                    implemented.append(proto_name)
            except (TypeError, NotImplementedError):
                pass
        
        if implemented:
            print(f"     {name:10}: {'、'.join(implemented)}")
        else:
            print(f"     {name:10}: 无")

# 运行抽象基类高级用法演示
advanced_abc_usage()
print()

# 7. 实际应用示例
print("=== 7. 实际应用示例 ===")

def practical_applications():
    """演示collections.abc的实际应用"""
    print("collections.abc在实际编程中的应用场景：\n")
    
    # 示例1: 类型检查和接口验证
    print("示例1: 类型检查和接口验证")
    print("   - 使用collections.abc进行更精确的类型检查")
    print("   - 验证对象是否实现了必要的接口")
    
    def process_items(items):
        """处理可迭代的项目集合"""
        # 检查items是否可迭代
        if not isinstance(items, collections.abc.Iterable):
            raise TypeError("items参数必须是可迭代的")
        
        # 检查是否需要转换为列表（例如，如果是生成器）
        if isinstance(items, collections.abc.Generator) or isinstance(items, collections.abc.Iterator):
            print("   注意: 输入是迭代器，将转换为列表")
            items = list(items)
        
        # 处理items
        print(f"   处理{len(items) if isinstance(items, collections.abc.Sized) else '未知数量'}个项目")
        return [item * 2 for item in items]
    
    print("   测试类型检查函数:")
    
    try:
        result1 = process_items([1, 2, 3, 4])
        print(f"     列表输入: {result1}")
    except TypeError as e:
        print(f"     错误: {e}")
    
    try:
        result2 = process_items((x for x in range(4)))
        print(f"     生成器输入: {result2}")
    except TypeError as e:
        print(f"     错误: {e}")
    
    try:
        result3 = process_items("abcd")
        print(f"     字符串输入: {result3}")
    except TypeError as e:
        print(f"     错误: {e}")
    
    try:
        result4 = process_items(42)  # 不是可迭代的
        print(f"     整数输入: {result4}")
    except TypeError as e:
        print(f"     错误: {e}")
    
    # 示例2: 创建自定义容器
    print("\n示例2: 创建自定义容器")
    print("   - 使用collections.abc创建功能丰富的自定义容器类")
    
    class SortedList(collections.abc.MutableSequence):
        """一个自动排序的列表实现"""
        def __init__(self, data=None, key=None, reverse=False):
            self._data = sorted(data or [], key=key, reverse=reverse)
            self._key = key
            self._reverse = reverse
        
        def __getitem__(self, index):
            return self._data[index]
        
        def __setitem__(self, index, value):
            del self._data[index]
            self.insert(index, value)  # 使用我们的insert方法保持排序
        
        def __delitem__(self, index):
            del self._data[index]
        
        def __len__(self):
            return len(self._data)
        
        def insert(self, index, value):
            # 找到正确的插入位置以保持排序
            if self._key:
                key_value = self._key(value)
                # 二分查找插入位置
                import bisect
                if self._reverse:
                    # 对于降序排序，需要反转比较
                    index = bisect.bisect_right([-self._key(x) for x in self._data], -key_value)
                else:
                    index = bisect.bisect_right([self._key(x) for x in self._data], key_value)
            else:
                # 简单值的二分查找
                import bisect
                index = bisect.bisect_right(self._data, value)
                
            # 插入到正确位置
            self._data.insert(index, value)
    
    print("   测试SortedList类:")
    
    # 创建一个基本排序列表
    sl = SortedList([5, 2, 8, 1, 9])
    print(f"     基本排序列表: {list(sl)}")
    
    # 添加元素
    sl.append(6)
    print(f"     append(6)后: {list(sl)}")
    
    # 插入元素
    sl.insert(0, 7)  # 即使指定了索引，也会自动排序
    print(f"     insert(0, 7)后: {list(sl)}")
    
    # 使用自定义键函数
    sl2 = SortedList(["apple", "Banana", "cherry", "date"], key=str.lower)
    print(f"     按小写排序: {list(sl2)}")
    
    # 降序排序
    sl3 = SortedList([5, 2, 8, 1, 9], reverse=True)
    print(f"     降序排序: {list(sl3)}")
    
    # 示例3: 实现缓存装饰器
    print("\n示例3: 实现缓存装饰器")
    print("   - 使用MutableMapping实现一个自定义缓存类")
    
    class LRUCache(collections.abc.MutableMapping):
        """简单的LRU (最近最少使用) 缓存实现"""
        def __init__(self, capacity):
            self._capacity = capacity
            self._cache = {}  # 存储键值对
            self._order = []  # 存储访问顺序
        
        def _update_access(self, key):
            """更新键的访问顺序"""
            if key in self._order:
                self._order.remove(key)
            self._order.append(key)
            
            # 如果超出容量，删除最久未使用的项
            if len(self._cache) > self._capacity:
                oldest_key = self._order.pop(0)
                del self._cache[oldest_key]
        
        def __getitem__(self, key):
            value = self._cache[key]
            self._update_access(key)
            return value
        
        def __setitem__(self, key, value):
            self._cache[key] = value
            self._update_access(key)
        
        def __delitem__(self, key):
            del self._cache[key]
            if key in self._order:
                self._order.remove(key)
        
        def __iter__(self):
            return iter(self._cache)
        
        def __len__(self):
            return len(self._cache)
        
        def get_stats(self):
            """获取缓存统计信息"""
            return {
                "size": len(self._cache),
                "capacity": self._capacity,
                "access_order": list(self._order)
            }
    
    # 创建缓存装饰器
    def lru_cache(maxsize=128):
        """LRU缓存装饰器"""
        def decorator(func):
            cache = LRUCache(maxsize)
            
            def wrapper(*args, **kwargs):
                # 创建缓存键
                key = (args, frozenset(kwargs.items())) if kwargs else args
                
                # 检查缓存
                try:
                    return cache[key]
                except KeyError:
                    # 缓存未命中，调用函数
                    result = func(*args, **kwargs)
                    cache[key] = result
                    return result
            
            # 添加获取缓存统计信息的方法
            wrapper.get_cache_stats = cache.get_stats
            
            return wrapper
        return decorator
    
    print("   测试LRU缓存装饰器:")
    
    @lru_cache(maxsize=3)
    def fibonacci(n):
        """计算斐波那契数列"""
        print(f"   计算fibonacci({n})")
        if n <= 1:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
    # 测试缓存效果
    print("   首次计算:")
    result1 = fibonacci(5)
    print(f"     fibonacci(5) = {result1}")
    print(f"     缓存状态: {fibonacci.get_cache_stats()}")
    
    print("   再次计算相同值 (应该使用缓存):")
    result2 = fibonacci(5)
    print(f"     fibonacci(5) = {result2}")
    
    print("   计算新值，超出缓存大小:")
    result3 = fibonacci(6)
    print(f"     fibonacci(6) = {result3}")
    print(f"     缓存状态: {fibonacci.get_cache_stats()}")

# 运行实际应用示例
practical_applications()
print()

# 8. 总结和完整导入指南
print("=== 8. 总结和完整导入指南 ===")

def abc_summary():
    """collections.abc模块的总结"""
    print("collections.abc模块总结：\n")
    
    # 功能总结
    print("功能总结：")
    print("1. 提供容器类型的抽象基类")
    print("2. 定义接口规范和行为约束")
    print("3. 提供类型检查和接口验证功能")
    print("4. 通过混入方法减少重复代码")
    print("5. 支持虚拟子类注册\n")
    
    # 主要抽象基类分类
    print("主要抽象基类分类：")
    print("1. 基本接口:")
    print("   - Container: 支持 'in' 操作符 (__contains__)")
    print("   - Sized: 支持 len() 函数 (__len__)")
    print("   - Iterable: 支持迭代 (__iter__)")
    print("   - Iterator: 支持 next() 函数 (__next__)")
    print("   - Hashable: 支持哈希操作 (__hash__)")
    print("   - Callable: 支持调用操作 (__call__)")
    print("\n2. 序列:")
    print("   - Sequence: 不可变序列 (如tuple, str, range)")
    print("   - MutableSequence: 可变序列 (如list)")
    print("\n3. 映射:")
    print("   - Mapping: 不可变映射")
    print("   - MutableMapping: 可变映射 (如dict)")
    print("\n4. 集合:")
    print("   - Set: 不可变集合 (如frozenset)")
    print("   - MutableSet: 可变集合 (如set)")
    print("\n5. 异步编程:")
    print("   - Awaitable: 可等待对象")
    print("   - Coroutine: 协程对象")
    print("   - AsyncIterable: 异步可迭代对象")
    print("   - AsyncIterator: 异步迭代器")
    print("   - AsyncGenerator: 异步生成器")
    
    # 版本兼容性
    print("\n版本兼容性：")
    print(f"当前Python版本: {sys.version}")
    print("- Python 2.6: collections模块中添加了抽象基类")
    print("- Python 3.3: 抽象基类移至collections.abc子模块")
    print("- Python 3.4: 添加了异步相关的抽象基类")
    print("- Python 3.7: 增强了虚拟子类的行为")
    print("\n注意: 在Python 3.3之前，抽象基类直接在collections模块中定义，")
    print("可以通过`from collections import Sequence, Mapping`等方式导入。")
    print("在Python 3.3及以后版本，应使用`from collections.abc import ...`。")

# 运行总结
abc_summary()

print("\n=== 9. 完整导入和使用指南 ===")
print("collections.abc模块的导入方式：")
print("""
# 导入整个模块
import collections.abc

# 导入常用的抽象基类
from collections.abc import (
    # 基本接口
    Container, Sized, Iterable, Iterator, Hashable, Callable,
    # 序列
    Sequence, MutableSequence,
    # 映射
    Mapping, MutableMapping,
    # 集合
    Set, MutableSet,
    # 异步编程（Python 3.4+）
    Awaitable, Coroutine, AsyncIterable, AsyncIterator, AsyncGenerator
)

# 向后兼容的导入方式（对于Python 3.3之前的版本）
try:
    from collections.abc import Sequence
except ImportError:
    from collections import Sequence
""")

print("\n使用collections.abc的最佳实践：")
print("1. 使用抽象基类进行类型检查，而非具体实现类")
print("   - 推荐: isinstance(obj, collections.abc.Sequence)")
print("   - 不推荐: isinstance(obj, list)")
print("2. 创建自定义容器时，实现相应的抽象基类接口")
print("3. 使用虚拟子类注册扩展现有类型")
print("4. 理解抽象基类的继承层次结构")
print("5. 使用抽象基类定义接口契约")
print("6. 利用混入方法减少重复代码")

print("\n总结：collections.abc模块提供了Python容器类型的标准化接口，")
print("通过使用这些抽象基类，可以创建更健壮、更具互操作性的代码，")
print("同时使代码更清晰、更易于理解和维护。正确使用抽象基类，")
print("可以实现更好的接口分离、更精确的类型检查，以及更灵活的组件设计。")
print("在Python编程中，尤其是在设计需要与标准库无缝集成的自定义数据结构时，")
print("collections.abc是一个不可或缺的工具。")