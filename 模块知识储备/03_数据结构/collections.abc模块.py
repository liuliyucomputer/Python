# collections.abc模块 - Python中的抽象基类集合

"""
collections.abc模块提供了一系列抽象基类，这些类定义了Python中各种集合类型的标准接口和行为。
这些抽象基类可以用于类型检查，也可以作为自定义集合类型的基类，确保实现了必要的方法。

在Python 3.3之前，这些抽象基类直接位于collections模块中；从Python 3.3开始，
它们被移到了专门的collections.abc子模块中，但为了向后兼容，collections模块仍然保留了这些类的引用。
"""

# 1. 核心功能介绍

print("=== 1. 核心功能介绍 ===")
print("\ncollections.abc模块提供了以下主要功能:")
print("1. 定义各种集合类型的标准接口和最小方法集")
print("2. 提供混入(mixin)方法，实现基于核心方法的派生功能")
print("3. 支持运行时类型检查，验证对象是否满足特定集合接口")
print("4. 作为自定义集合类型的基类，简化实现过程")
print("5. 明确区分不同类型集合的行为预期")

# 2. 主要抽象基类分类

print("\n=== 2. 主要抽象基类分类 ===")

print("\n2.1 容器类(Container)抽象基类")
print("容器类抽象基类定义了对象是否包含特定元素的接口:")

print("  - Container: 所有容器的基类，定义`__contains__`方法")
print("    用于支持`in`操作符检查元素是否存在于容器中")

print("\n2.2 迭代器类(Iterator)抽象基类")
print("迭代器类抽象基类定义了对象的迭代行为:")

print("  - Iterable: 可迭代对象，定义`__iter__`方法")
print("    返回一个迭代器对象")
print("  - Iterator: 迭代器，继承自Iterable，定义`__next__`方法")
print("    用于逐个访问元素并在迭代结束时引发StopIteration异常")

print("\n2.3 序列类(Sequence)抽象基类")
print("序列类抽象基类定义了有序、可索引集合的接口:")

print("  - Reversible: 可反转序列，定义`__reversed__`方法")
print("    返回一个反向迭代器")
print("  - Collection: 集合的基类，继承自Container、Iterable和Sized")
print("    结合了容器、可迭代和可测量大小的特性")
print("  - Sequence: 序列，继承自Reversible和Collection")
print("    定义了序列的基本接口，如`__getitem__`、`__contains__`等")
print("  - MutableSequence: 可变序列，继承自Sequence")
print("    添加了修改序列的方法，如`__setitem__`、`__delitem__`等")

print("\n2.4 映射类(Mapping)抽象基类")
print("映射类抽象基类定义了键值对集合的接口:")

print("  - Mapping: 映射，继承自Collection")
print("    定义了只读映射的基本接口，如`__getitem__`、`keys`等")
print("  - MappingView: 映射视图的基类")
print("    提供映射键、值或项的视图")
print("  - KeysView: 键视图，继承自MappingView和Set")
print("    提供对映射键集合的视图")
print("  - ValuesView: 值视图，继承自MappingView和Collection")
print("    提供对映射值集合的视图")
print("  - ItemsView: 项视图，继承自MappingView和Set")
print("    提供对映射(键,值)对集合的视图")
print("  - MutableMapping: 可变映射，继承自Mapping")
print("    添加了修改映射的方法，如`__setitem__`、`__delitem__`等")

print("\n2.5 集合类(Set)抽象基类")
print("集合类抽象基类定义了无序列表集合的接口:")

print("  - Set: 集合，继承自Collection")
print("    定义了只读集合的基本接口，如`__contains__`、`__and__`等")
print("  - MutableSet: 可变集合，继承自Set")
print("    添加了修改集合的方法，如`add`、`remove`等")

print("\n2.6 可调用类(Callable)抽象基类")
print("可调用类抽象基类定义了可调用对象的接口:")

print("  - Callable: 可调用对象，定义`__call__`方法")
print("    用于支持像函数一样调用对象")

print("\n2.7 数字类(Number)抽象基类")
print("数字类抽象基类定义了数值类型的接口:")

print("  - Hashable: 可哈希对象的基类，定义`__hash__`方法")
print("    用于支持对象作为字典键或集合元素")
print("  - Number: 数字的基类")
print("    是所有数值类型的抽象基类")
print("  - Complex: 复数的抽象基类")
print("    定义了复数的基本操作")
print("  - Real: 实数的抽象基类，继承自Complex")
print("    定义了实数的基本操作")
print("  - Rational: 有理数的抽象基类，继承自Real")
print("    定义了有理数的基本操作")
print("  - Integral: 整数的抽象基类，继承自Rational")
print("    定义了整数的基本操作")

# 3. 基本使用方法

print("\n=== 3. 基本使用方法 ===")

# 导入必要的模块
from collections.abc import (
    Container, Iterable, Iterator, Reversible,
    Collection, Sequence, MutableSequence,
    Mapping, MutableMapping, Set, MutableSet,
    MappingView, KeysView, ValuesView, ItemsView,
    Callable, Hashable
)

print("\n3.1 使用抽象基类进行类型检查")
print("可以使用isinstance()函数检查对象是否满足特定的接口:")

# 检查内置类型
print("内置类型的类型检查:")
print(f"列表是Sequence吗? {isinstance([1, 2, 3], Sequence)}")
print(f"元组是Sequence吗? {isinstance((1, 2, 3), Sequence)}")
print(f"字符串是Sequence吗? {isinstance('abc', Sequence)}")
print(f"字典是Mapping吗? {isinstance({'a': 1}, Mapping)}")
print(f"集合是Set吗? {isinstance({1, 2, 3}, Set)}")
print(f"函数是Callable吗? {isinstance(lambda x: x, Callable)}")
print(f"整数是Hashable吗? {isinstance(42, Hashable)}")

# 注意区分可变和不可变类型
print("\n区分可变和不可变类型:")
print(f"列表是MutableSequence吗? {isinstance([1, 2, 3], MutableSequence)}")
print(f"元组是MutableSequence吗? {isinstance((1, 2, 3), MutableSequence)}")  # 元组是不可变的
print(f"字典是MutableMapping吗? {isinstance({'a': 1}, MutableMapping)}")
print(f"集合是MutableSet吗? {isinstance({1, 2, 3}, MutableSet)}")
print(f"frozenset是MutableSet吗? {isinstance(frozenset({1, 2, 3}), MutableSet)}")  # frozenset是不可变的

print("\n3.2 检查自定义类")
print("检查自定义类是否满足特定接口:")

# 一个自定义类，实现了__contains__方法
class CustomContainer:
    def __init__(self, items):
        self.items = items
    
    def __contains__(self, item):
        return item in self.items

# 一个自定义类，实现了__iter__方法
class CustomIterable:
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        return iter(self.items)

# 一个自定义类，实现了__iter__和__next__方法
class CustomIterator:
    def __init__(self, items):
        self.items = items
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.items):
            value = self.items[self.index]
            self.index += 1
            return value
        raise StopIteration

# 检查这些自定义类
container = CustomContainer([1, 2, 3])
iterable = CustomIterable([1, 2, 3])
iterator = CustomIterator([1, 2, 3])

print(f"CustomContainer是Container吗? {isinstance(container, Container)}")
print(f"CustomIterable是Iterable吗? {isinstance(iterable, Iterable)}")
print(f"CustomIterator是Iterator吗? {isinstance(iterator, Iterator)}")
print(f"CustomIterator是Iterable吗? {isinstance(iterator, Iterable)}")  # Iterator继承自Iterable

print("\n3.3 使用抽象基类作为自定义类的基类")
print("可以将抽象基类作为自定义类的基类，确保实现了必要的方法:")

try:
    # 尝试创建一个继承自Sequence但没有实现必要方法的类
    class BrokenSequence(Sequence):
        pass
    
    # 尝试实例化这个类会引发TypeError
    broken = BrokenSequence()
except TypeError as e:
    print(f"错误: 没有实现必要方法时无法实例化: {e}")

# 创建一个正确实现了Sequence接口的类
class MySequence(Sequence):
    def __init__(self, data):
        self.data = data
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __len__(self):
        return len(self.data)

# 实例化并使用这个类
my_seq = MySequence([1, 2, 3, 4, 5])
print(f"MySequence的长度: {len(my_seq)}")
print(f"MySequence[0]: {my_seq[0]}")
print(f"MySequence[1:3]: {my_seq[1:3]}")
print(f"3在MySequence中吗? {3 in my_seq}")
print(f"MySequence是Sequence吗? {isinstance(my_seq, Sequence)}")

# 即使我们没有实现__contains__方法，也可以使用in操作符
# 这是因为Sequence抽象基类提供了默认实现
print("\n3.4 使用抽象基类提供的混入方法")
print("抽象基类提供了许多基于核心方法的默认实现:")

# 查看MySequence自动获得了哪些方法
print(f"MySequence有__contains__方法: {'__contains__' in dir(my_seq)}")
print(f"MySequence有__iter__方法: {'__iter__' in dir(my_seq)}")
print(f"MySequence有__reversed__方法: {'__reversed__' in dir(my_seq)}")
print(f"MySequence有index方法: {'index' in dir(my_seq)}")
print(f"MySequence有count方法: {'count' in dir(my_seq)}")

# 演示这些方法
print(f"\n使用混入方法:")
print(f"'__iter__'的结果: {list(my_seq)}")
print(f"'__reversed__'的结果: {list(reversed(my_seq))}")
print(f"'index'方法结果: {my_seq.index(3)}")
print(f"'count'方法结果: {my_seq.count(2)}")

# 4. 实现自定义集合类

print("\n=== 4. 实现自定义集合类 ===")

print("\n4.1 实现自定义序列类")
print("通过继承MutableSequence实现自定义可变序列:")

class MyList(MutableSequence):
    """自定义列表类，继承自MutableSequence"""
    
    def __init__(self, data=None):
        """初始化，可选地从现有数据创建"""
        self._data = list(data) if data is not None else []
    
    def __getitem__(self, index):
        """获取指定索引的元素"""
        return self._data[index]
    
    def __setitem__(self, index, value):
        """设置指定索引的元素"""
        self._data[index] = value
    
    def __delitem__(self, index):
        """删除指定索引的元素"""
        del self._data[index]
    
    def __len__(self):
        """获取列表长度"""
        return len(self._data)
    
    def insert(self, index, value):
        """在指定索引插入元素"""
        self._data.insert(index, value)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        return f"MyList({self._data})"

# 测试自定义列表类
print("测试自定义列表类:")
my_list = MyList([1, 2, 3])
print(f"初始列表: {my_list}")

# 测试序列操作
my_list.append(4)  # 混入方法，基于insert实现
print(f"添加元素后: {my_list}")

my_list.extend([5, 6])  # 混入方法
print(f"扩展列表后: {my_list}")

my_list.remove(3)  # 混入方法
print(f"移除元素后: {my_list}")

popped = my_list.pop()  # 混入方法
print(f"弹出元素: {popped}")
print(f"弹出后列表: {my_list}")

# 测试继承关系
print(f"\n继承关系:")
print(f"MyList是MutableSequence吗? {isinstance(my_list, MutableSequence)}")
print(f"MyList是Sequence吗? {isinstance(my_list, Sequence)}")
print(f"MyList是Collection吗? {isinstance(my_list, Collection)}")
print(f"MyList是Iterable吗? {isinstance(my_list, Iterable)}")
print(f"MyList是Container吗? {isinstance(my_list, Container)}")

print("\n4.2 实现自定义映射类")
print("通过继承MutableMapping实现自定义可变映射:")

class MyDict(MutableMapping):
    """自定义字典类，继承自MutableMapping"""
    
    def __init__(self, data=None):
        """初始化，可选地从现有数据创建"""
        self._data = dict(data) if data is not None else {}
    
    def __getitem__(self, key):
        """获取指定键的值"""
        if key not in self._data:
            raise KeyError(key)
        return self._data[key]
    
    def __setitem__(self, key, value):
        """设置指定键的值"""
        self._data[key] = value
    
    def __delitem__(self, key):
        """删除指定键的值"""
        if key not in self._data:
            raise KeyError(key)
        del self._data[key]
    
    def __iter__(self):
        """返回键的迭代器"""
        return iter(self._data)
    
    def __len__(self):
        """获取字典长度"""
        return len(self._data)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        return f"MyDict({self._data})"

# 测试自定义字典类
print("测试自定义字典类:")
my_dict = MyDict({"a": 1, "b": 2})
print(f"初始字典: {my_dict}")

# 测试映射操作
my_dict["c"] = 3  # 基本操作
print(f"添加键值对后: {my_dict}")

my_dict.update({"d": 4, "e": 5})  # 混入方法
print(f"更新字典后: {my_dict}")

popped = my_dict.pop("b")  # 混入方法
print(f"弹出值: {popped}")
print(f"弹出后字典: {my_dict}")

# 测试视图方法
print(f"\n字典视图:")
print(f"键视图: {my_dict.keys()}")
print(f"值视图: {my_dict.values()}")
print(f"项视图: {my_dict.items()}")

# 测试继承关系
print(f"\n继承关系:")
print(f"MyDict是MutableMapping吗? {isinstance(my_dict, MutableMapping)}")
print(f"MyDict是Mapping吗? {isinstance(my_dict, Mapping)}")
print(f"MyDict是Collection吗? {isinstance(my_dict, Collection)}")

print("\n4.3 实现自定义集合类")
print("通过继承MutableSet实现自定义可变集合:")

class MySet(MutableSet):
    """自定义集合类，继承自MutableSet"""
    
    def __init__(self, data=None):
        """初始化，可选地从现有数据创建"""
        self._data = set(data) if data is not None else set()
    
    def __contains__(self, item):
        """检查元素是否在集合中"""
        return item in self._data
    
    def __iter__(self):
        """返回集合元素的迭代器"""
        return iter(self._data)
    
    def __len__(self):
        """获取集合长度"""
        return len(self._data)
    
    def add(self, value):
        """向集合添加元素"""
        self._data.add(value)
    
    def discard(self, value):
        """从集合中移除元素，如果元素不存在则不执行任何操作"""
        self._data.discard(value)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        return f"MySet({self._data})"

# 测试自定义集合类
print("测试自定义集合类:")
my_set = MySet([1, 2, 3])
print(f"初始集合: {my_set}")

# 测试集合操作
my_set.add(4)  # 基本操作
print(f"添加元素后: {my_set}")

my_set.update([5, 6])  # 混入方法
print(f"更新集合后: {my_set}")

my_set.remove(3)  # 混入方法，基于discard实现，但元素不存在时会引发KeyError
print(f"移除元素后: {my_set}")

# 测试集合运算符
other_set = MySet([4, 5, 7, 8])
print(f"\n集合运算:")
print(f"并集: {my_set | other_set}")  # 混入方法
print(f"交集: {my_set & other_set}")  # 混入方法
print(f"差集: {my_set - other_set}")  # 混入方法
print(f"对称差: {my_set ^ other_set}")  # 混入方法

# 测试继承关系
print(f"\n继承关系:")
print(f"MySet是MutableSet吗? {isinstance(my_set, MutableSet)}")
print(f"MySet是Set吗? {isinstance(my_set, Set)}")
print(f"MySet是Collection吗? {isinstance(my_set, Collection)}")

# 5. 实际应用场景

print("\n=== 5. 实际应用场景 ===")

print("\n5.1 类型检查和接口验证")
print("在编写通用代码时，使用collections.abc进行类型检查，确保对象满足预期接口:")

print("示例: 通用函数，接受任何序列类型")

# 一个通用函数，处理任何实现了Sequence接口的对象
def process_sequence(seq):
    """处理序列对象，无论其具体实现类型"""
    # 检查参数是否满足Sequence接口
    if not isinstance(seq, Sequence):
        raise TypeError("Expected a Sequence type")
    
    # 可以安全地使用Sequence接口定义的方法
    print(f"序列长度: {len(seq)}")
    print(f"第一个元素: {seq[0]}")
    print(f"最后一个元素: {seq[-1]}")
    
    # 如果序列可反转
    if isinstance(seq, Reversible):
        print(f"反向序列: {list(reversed(seq))}")
    
    # 计算元素总和（假设元素支持加法）
    try:
        total = sum(seq)
        print(f"元素总和: {total}")
    except TypeError:
        print("元素不支持加法操作")

# 测试不同类型的序列
print("\n测试列表:")
process_sequence([1, 2, 3, 4, 5])

print("\n测试元组:")
process_sequence((1, 2, 3, 4, 5))

print("\n测试字符串:")
process_sequence("hello")

print("\n测试自定义序列:")
process_sequence(MySequence([1, 2, 3, 4, 5]))

print("\n5.2 创建自定义数据结构")
print("通过继承抽象基类，可以轻松创建具有特定行为的数据结构:")

print("示例: 实现一个有序字典，维护插入顺序")

# 注意：Python 3.7+中，普通字典也保留插入顺序
# 这里为了演示，实现一个简单的有序字典
class OrderedDict2(MutableMapping):
    """简单的有序字典实现"""
    
    def __init__(self, data=None):
        """初始化有序字典"""
        # 使用列表保存键的顺序
        self._keys = []
        # 使用字典存储键值对
        self._values = {}
        
        # 从现有数据初始化
        if data is not None:
            self.update(data)
    
    def __getitem__(self, key):
        """获取指定键的值"""
        return self._values[key]
    
    def __setitem__(self, key, value):
        """设置指定键的值，并维护顺序"""
        if key not in self._values:
            self._keys.append(key)
        self._values[key] = value
    
    def __delitem__(self, key):
        """删除指定键的值，并维护顺序"""
        del self._values[key]
        self._keys.remove(key)
    
    def __iter__(self):
        """返回键的迭代器，保持插入顺序"""
        return iter(self._keys)
    
    def __len__(self):
        """获取字典长度"""
        return len(self._values)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        items = [f"{repr(k)}: {repr(v)}" for k, v in self.items()]
        return f"OrderedDict2({{{', '.join(items)}}})"

# 测试有序字典
print("\n测试有序字典:")
od = OrderedDict2()
od["c"] = 3
od["a"] = 1
od["b"] = 2

print(f"有序字典: {od}")
print(f"迭代顺序: {list(od.keys())}")
print(f"项视图: {list(od.items())}")

# 修改现有键的值
od["a"] = 10
print(f"修改后: {od}")  # 顺序不变

# 删除键
od.pop("b")
print(f"删除后: {od}")

print("\n5.3 实现缓存系统")
print("使用抽象基类实现自定义缓存系统:")

print("示例: 实现一个LRU缓存(最近最少使用缓存)")

class LRUCache(MutableMapping):
    """简单的LRU缓存实现"""
    
    def __init__(self, capacity=128):
        """初始化LRU缓存
        
        Args:
            capacity: 缓存最大容量
        """
        self.capacity = capacity
        self._cache = {}  # 存储键值对
        self._access_order = []  # 存储访问顺序
    
    def __getitem__(self, key):
        """获取值并更新访问顺序"""
        if key not in self._cache:
            raise KeyError(key)
        
        # 更新访问顺序
        self._access_order.remove(key)
        self._access_order.append(key)
        
        return self._cache[key]
    
    def __setitem__(self, key, value):
        """设置值并维护缓存大小"""
        # 如果键已存在，更新值和访问顺序
        if key in self._cache:
            self._access_order.remove(key)
        # 如果达到容量且是新键，删除最久未使用的项
        elif len(self._cache) >= self.capacity:
            oldest_key = self._access_order.pop(0)
            del self._cache[oldest_key]
        
        # 添加/更新值和访问顺序
        self._cache[key] = value
        self._access_order.append(key)
    
    def __delitem__(self, key):
        """删除键值对"""
        if key not in self._cache:
            raise KeyError(key)
        
        del self._cache[key]
        self._access_order.remove(key)
    
    def __iter__(self):
        """返回键的迭代器"""
        return iter(self._cache)
    
    def __len__(self):
        """获取缓存大小"""
        return len(self._cache)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        return f"LRUCache({self._cache})"
    
    def clear(self):
        """清空缓存"""
        self._cache.clear()
        self._access_order.clear()

# 测试LRU缓存
print("\n测试LRU缓存:")
cache = LRUCache(capacity=3)

# 添加元素
print("添加元素:")
cache["a"] = 1
cache["b"] = 2
cache["c"] = 3
print(f"缓存内容: {cache}")

# 访问元素，更新访问顺序
print("\n访问元素'a':")
print(f"获取'a': {cache['a']}")

# 添加新元素，超过容量，应该删除最久未使用的元素'b'
print("\n添加新元素'd':")
cache["d"] = 4
print(f"缓存内容: {cache}")  # 应该不包含'b'

try:
    # 尝试访问已被淘汰的键
    print(f"获取'b': {cache['b']}")
except KeyError:
    print("键'b'已被淘汰出缓存")

print("\n5.4 实现特殊集合类型")
print("通过继承Set或MutableSet实现特殊的集合类型:")

print("示例: 实现一个有序集合，保持元素的插入顺序")

class OrderedSet(MutableSet):
    """简单的有序集合实现"""
    
    def __init__(self, data=None):
        """初始化有序集合"""
        # 使用字典同时实现集合和顺序维护（键为元素，值无意义）
        self._data = {}
        
        # 从现有数据初始化
        if data is not None:
            for item in data:
                self.add(item)
    
    def __contains__(self, item):
        """检查元素是否在集合中"""
        return item in self._data
    
    def __iter__(self):
        """返回元素的迭代器，保持插入顺序"""
        return iter(self._data)
    
    def __len__(self):
        """获取集合大小"""
        return len(self._data)
    
    def add(self, value):
        """向集合添加元素"""
        self._data[value] = None  # 值设为None，只关心键的存在性
    
    def discard(self, value):
        """从集合中移除元素"""
        if value in self._data:
            del self._data[value]
    
    def __repr__(self):
        """返回对象的字符串表示"""
        items = [repr(item) for item in self._data]
        return f"OrderedSet({{{', '.join(items)}}})"

# 测试有序集合
print("\n测试有序集合:")
os = OrderedSet([3, 1, 2, 1, 3])
print(f"有序集合: {os}")
print(f"迭代顺序: {list(os)}")

# 添加元素
os.add(4)
print(f"添加后: {os}")

# 移除元素
os.remove(2)  # 使用继承的remove方法
print(f"移除后: {os}")

# 集合操作
os2 = OrderedSet([1, 4, 5, 6])
print(f"\n集合运算:")
print(f"并集: {os | os2}")
print(f"交集: {os & os2}")
print(f"差集: {os - os2}")

print("\n5.5 实现自定义迭代器")
print("通过实现Iterator接口创建自定义迭代器:")

print("示例: 实现一个无限序列迭代器")

class FibonacciIterator(Iterator):
    """生成斐波那契数列的迭代器"""
    
    def __init__(self, limit=None):
        """初始化迭代器
        
        Args:
            limit: 生成的最大项数，None表示无限生成
        """
        self.a, self.b = 0, 1  # 斐波那契数列的前两个数
        self.count = 0
        self.limit = limit
    
    def __next__(self):
        """返回下一个斐波那契数"""
        # 检查是否达到限制
        if self.limit is not None and self.count >= self.limit:
            raise StopIteration
        
        # 保存当前值用于返回
        current = self.a
        
        # 计算下一个斐波那契数
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        
        return current

# 测试斐波那契迭代器
print("\n测试有限斐波那契迭代器:")
fib_limited = FibonacciIterator(10)
print(f"前10个斐波那契数: {list(fib_limited)}")

print("\n测试无限斐波那契迭代器:")
fib_infinite = FibonacciIterator()

# 只取前15个数
print(f"前15个斐波那契数: ")
for i, num in enumerate(fib_infinite):
    print(f"  {i+1}: {num}")
    if i >= 14:  # 已经取了15个数
        break

print("\n5.6 类型提示和接口定义")
print("在类型提示系统中使用collections.abc定义接口:")

print("示例: 使用collections.abc进行函数参数类型注解")

# 虽然Python不会强制类型检查，但这提供了清晰的接口文档和IDE支持
def summarize_collection(items: Collection) -> dict:
    """返回集合的摘要信息
    
    Args:
        items: 任何实现了Collection接口的对象
        
    Returns:
        包含集合摘要信息的字典
    """
    summary = {
        "length": len(items),
        "type": type(items).__name__
    }
    
    # 尝试获取一些样本
    try:
        # 将items转换为列表，最多取5个样本
        item_list = list(items)
        summary["sample"] = item_list[:5] if len(item_list) > 0 else None
    except:
        summary["sample"] = "无法获取样本"
    
    return summary

# 测试不同类型的集合
print("\n测试不同类型集合的摘要:")

print("列表:")
print(summarize_collection([1, 2, 3, 4, 5, 6, 7]))

print("\n集合:")
print(summarize_collection({1, 2, 3, 4, 5, 6, 7}))

print("\n字典:")
print(summarize_collection({"a": 1, "b": 2, "c": 3}))

print("\n字符串:")
print(summarize_collection("hello world"))

# 6. 性能分析

print("\n=== 6. 性能分析 ===")

print("\n6.1 抽象基类的开销")
print("使用抽象基类时的性能考虑:")
print("  - 类型检查开销: isinstance()检查是相对快速的操作，但频繁使用仍会带来开销")
print("  - 混入方法的性能: 抽象基类提供的混入方法通常是通用实现，可能不是最优的")
print("  - 多继承复杂性: 复杂的抽象基类层次结构可能导致方法解析顺序(MRO)查找开销增加")

print("\n6.2 与直接实现的比较")
print("直接实现所有方法与使用抽象基类的性能比较:")
print("  - 对于关键性能路径，直接实现所有必要方法可能比依赖混入方法更快")
print("  - 对于非关键路径，混入方法提供的便利性和代码复用优势通常超过性能损失")
print("  - 继承自抽象基类的主要优势是代码的正确性和可维护性，而不是纯粹的性能")

print("\n6.3 内存使用")
print("使用抽象基类时的内存考虑:")
print("  - 抽象基类增加了类层次结构的复杂性，可能导致额外的内存使用")
print("  - 对于大量实例的场景，这种额外开销可能变得显著")
print("  - 在内存受限环境中，可能需要权衡接口保证和内存使用")

print("\n6.4 最佳实践性能建议")
print("为了获得最佳性能，使用collections.abc时应注意以下几点:")
print("  - 在性能关键的代码中，考虑直接实现必要的方法而不是依赖混入方法")
print("  - 使用 isinstance() 进行类型检查时，优先检查最具体的抽象基类，避免不必要的层次结构遍历")
print("  - 在定义自定义集合类时，只继承必要的抽象基类")
print("  - 考虑使用__slots__来减少内存使用，特别是对于将有大量实例的类")

# 7. 使用注意事项

print("\n=== 7. 使用注意事项 ===")

print("\n7.1 抽象基类的版本兼容性")
print("注意collections.abc在不同Python版本中的位置:")

print("  - Python 3.3+: 抽象基类位于collections.abc模块中")
print("  - Python 2.7 和 Python 3.0-3.2: 抽象基类直接位于collections模块中")
print("  - 为了向后兼容，collections模块在Python 3.3+中仍然保留了这些类的引用，但建议直接使用collections.abc")

print("\n7.2 方法实现要求")
print("实现抽象基类时，必须提供所有必要的抽象方法:")

print("  - Sequence需要实现: __getitem__, __len__")
print("  - MutableSequence需要额外实现: __setitem__, __delitem__, insert")
print("  - Mapping需要实现: __getitem__, __iter__, __len__")
print("  - MutableMapping需要额外实现: __setitem__, __delitem__")
print("  - Set需要实现: __contains__, __iter__, __len__")
print("  - MutableSet需要额外实现: add, discard")

print("\n7.3 避免过度使用类型检查")
print("在Python中，通常更倾向于"鸭子类型"而不是严格的类型检查:")

print("  - 考虑使用try-except块处理可能的接口不匹配，而不是使用isinstance()进行预检查")
print("  - 类型检查更适合用于API边界或文档目的，而不是内部代码")
print("  - 在性能关键路径中，过度的类型检查可能导致不必要的开销")

print("\n7.4 正确处理抽象基类的继承关系")
print("理解抽象基类之间的继承关系:")

print("  - MutableXXX继承自XXX（例如，MutableSequence继承自Sequence）")
print("  - 检查更具体的抽象基类（如MutableSequence）比检查更通用的基类（如Sequence）更有意义")
print("  - 避免创建与现有抽象基类接口冲突的自定义接口")

print("\n7.5 与具体类型的交互")
print("注意与Python内置类型和第三方库类型的交互:")

print("  - Python 3.7+中的普通字典保持插入顺序，但其行为可能与OrderedDict的某些特定方法不同")
print("  - 某些第三方库可能实现了collections.abc接口，但有额外的限制或行为")
print("  - 在混合使用不同实现时，始终测试边界情况")

# 8. 综合示例：实现一个完整的数据容器库

print("\n=== 8. 综合示例：实现一个完整的数据容器库 ===")

print("\n实现一个包含多种数据结构的微型容器库，所有容器都实现了适当的collections.abc接口:")

# 导入必要的模块
from collections.abc import Sequence, MutableSequence, Mapping, MutableMapping, Set, MutableSet
from abc import ABCMeta, abstractmethod
import copy

class ImmutableContainer(metaclass=ABCMeta):
    """不可变容器的基类，提供基本的复制功能"""
    
    def copy(self):
        """创建容器的浅拷贝"""
        return copy.copy(self)
    
    def deepcopy(self):
        """创建容器的深拷贝"""
        return copy.deepcopy(self)

class ImmutableList(ImmutableContainer, Sequence):
    """不可变列表实现"""
    
    def __init__(self, data=None):
        """初始化不可变列表
        
        Args:
            data: 初始数据，可以是任何可迭代对象
        """
        self._data = tuple(data) if data is not None else tuple()
    
    def __getitem__(self, index):
        """获取指定索引的元素"""
        return self._data[index]
    
    def __len__(self):
        """获取列表长度"""
        return len(self._data)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        return f"ImmutableList({self._data})"
    
    def __eq__(self, other):
        """比较两个列表是否相等"""
        if isinstance(other, Sequence):
            return list(self) == list(other)
        return False

class UniqueList(MutableSequence):
    """不允许重复元素的可变列表"""
    
    def __init__(self, data=None):
        """初始化唯一列表
        
        Args:
            data: 初始数据，重复元素将被忽略
        """
        self._data = []
        self._set = set()
        
        if data is not None:
            for item in data:
                self.append(item)
    
    def __getitem__(self, index):
        """获取指定索引的元素"""
        return self._data[index]
    
    def __setitem__(self, index, value):
        """设置指定索引的元素，如果值已存在则抛出异常"""
        if value in self._set and value != self._data[index]:
            raise ValueError(f"值 '{value}' 已存在于列表中")
        
        # 移除旧值，添加新值
        old_value = self._data[index]
        self._set.remove(old_value)
        self._data[index] = value
        self._set.add(value)
    
    def __delitem__(self, index):
        """删除指定索引的元素"""
        value = self._data[index]
        del self._data[index]
        self._set.remove(value)
    
    def __len__(self):
        """获取列表长度"""
        return len(self._data)
    
    def insert(self, index, value):
        """在指定索引插入元素，如果值已存在则忽略"""
        if value not in self._set:
            self._data.insert(index, value)
            self._set.add(value)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        return f"UniqueList({self._data})"

class ReadOnlyDict(ImmutableContainer, Mapping):
    """只读字典实现"""
    
    def __init__(self, data=None):
        """初始化只读字典
        
        Args:
            data: 初始数据，可以是任何映射或键值对序列
        """
        self._data = dict(data) if data is not None else {}
    
    def __getitem__(self, key):
        """获取指定键的值"""
        return self._data[key]
    
    def __iter__(self):
        """返回键的迭代器"""
        return iter(self._data)
    
    def __len__(self):
        """获取字典长度"""
        return len(self._data)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        return f"ReadOnlyDict({self._data})"
    
    def __eq__(self, other):
        """比较两个字典是否相等"""
        if isinstance(other, Mapping):
            return dict(self) == dict(other)
        return False

class CaseInsensitiveDict(MutableMapping):
    """大小写不敏感的字典实现"""
    
    def __init__(self, data=None):
        """初始化大小写不敏感字典
        
        Args:
            data: 初始数据，可以是任何映射或键值对序列
        """
        self._data = {}  # 存储小写键到值的映射
        self._keys = {}  # 存储小写键到原始键的映射
        
        if data is not None:
            self.update(data)
    
    def _normalize_key(self, key):
        """将键转换为小写（如果可能）"""
        if isinstance(key, str):
            return key.lower()
        return key
    
    def __getitem__(self, key):
        """获取指定键的值，不区分大小写"""
        norm_key = self._normalize_key(key)
        return self._data[norm_key]
    
    def __setitem__(self, key, value):
        """设置指定键的值，不区分大小写"""
        norm_key = self._normalize_key(key)
        self._data[norm_key] = value
        self._keys[norm_key] = key
    
    def __delitem__(self, key):
        """删除指定键的值，不区分大小写"""
        norm_key = self._normalize_key(key)
        del self._data[norm_key]
        del self._keys[norm_key]
    
    def __iter__(self):
        """返回原始键的迭代器"""
        return iter(self._keys.values())
    
    def __len__(self):
        """获取字典长度"""
        return len(self._data)
    
    def __repr__(self):
        """返回对象的字符串表示"""
        items = [f"{repr(self._keys[norm_key])}: {repr(value)}"
                for norm_key, value in self._data.items()]
        return f"CaseInsensitiveDict({{{', '.join(items)}}})"

class OrderedSet2(MutableSet):
    """保持元素插入顺序的可变集合"""
    
    def __init__(self, data=None):
        """初始化有序集合
        
        Args:
            data: 初始数据
        """
        self._data = {}  # 使用字典实现，键为元素，值无意义
        
        if data is not None:
            for item in data:
                self.add(item)
    
    def __contains__(self, item):
        """检查元素是否在集合中"""
        return item in self._data
    
    def __iter__(self):
        """返回元素的迭代器，保持插入顺序"""
        return iter(self._data)
    
    def __len__(self):
        """获取集合长度"""
        return len(self._data)
    
    def add(self, value):
        """向集合添加元素"""
        self._data[value] = None
    
    def discard(self, value):
        """从集合中移除元素"""
        if value in self._data:
            del self._data[value]
    
    def __repr__(self):
        """返回对象的字符串表示"""
        items = [repr(item) for item in self._data]
        return f"OrderedSet2({{{', '.join(items)}}})"

# 测试容器库
print("\n测试不可变列表:")
im_list = ImmutableList([1, 2, 3, 4, 5])
print(f"创建: {im_list}")
print(f"访问: {im_list[2]}")
print(f"长度: {len(im_list)}")

# 创建副本
im_list_copy = im_list.copy()
print(f"副本: {im_list_copy}")
print(f"是否为同一对象: {im_list is im_list_copy}")

print("\n测试唯一列表:")
ul = UniqueList([1, 2, 2, 3, 4, 4, 5])
print(f"创建（自动去重）: {ul}")

# 尝试添加重复元素
ul.append(6)
ul.append(3)  # 重复，将被忽略
print(f"添加元素后: {ul}")

try:
    # 尝试设置重复元素
    ul[0] = 2
except ValueError as e:
    print(f"预期的错误: {e}")

print("\n测试只读字典:")
ro_dict = ReadOnlyDict({"a": 1, "b": 2, "c": 3})
print(f"创建: {ro_dict}")
print(f"访问: {ro_dict['b']}")
print(f"长度: {len(ro_dict)}")

# 创建副本
ro_dict_copy = ro_dict.copy()
print(f"副本: {ro_dict_copy}")

print("\n测试大小写不敏感字典:")
ci_dict = CaseInsensitiveDict({"Name": "John", "AGE": 30, "city": "New York"})
print(f"创建: {ci_dict}")
print(f"访问'name': {ci_dict['name']}")  # 小写
print(f"访问'AGE': {ci_dict['AGE']}")  # 大写
print(f"访问'City': {ci_dict['City']}")  # 首字母大写

# 添加新键
ci_dict["country"] = "USA"
print(f"添加后: {ci_dict}")

# 覆盖现有键（不区分大小写）
ci_dict["CITY"] = "Boston"
print(f"覆盖后: {ci_dict}")

print("\n测试有序集合:")
os2 = OrderedSet2([3, 1, 2, 1, 3])
print(f"创建（自动去重并保持顺序）: {os2}")

# 添加元素
os2.add(4)
os2.add(2)  # 重复，将被忽略
print(f"添加后: {os2}")

# 移除元素
os2.remove(1)
print(f"移除后: {os2}")

# 集合运算
os2_2 = OrderedSet2([2, 4, 5, 6])
print(f"\n集合运算:")
print(f"并集: {os2 | os2_2}")
print(f"交集: {os2 & os2_2}")
print(f"差集: {os2 - os2_2}")

print("\n类型检查:")
print(f"ImmutableList是Sequence吗? {isinstance(im_list, Sequence)}")
print(f"UniqueList是MutableSequence吗? {isinstance(ul, MutableSequence)}")
print(f"ReadOnlyDict是Mapping吗? {isinstance(ro_dict, Mapping)}")
print(f"CaseInsensitiveDict是MutableMapping吗? {isinstance(ci_dict, MutableMapping)}")
print(f"OrderedSet2是MutableSet吗? {isinstance(os2, MutableSet)}")

# 9. 总结

print("\n=== 9. 总结 ===")

print("\ncollections.abc模块提供了一系列强大的抽象基类，它们定义了Python中各种集合类型的标准接口和行为。")

print("\n主要优势:")
print("1. 定义标准接口：为各种集合类型提供了明确的接口定义")
print("2. 代码复用：通过混入方法提供了基于核心方法的派生功能")
print("3. 类型检查：支持使用isinstance()进行运行时类型检查")
print("4. 接口验证：确保自定义集合类型实现了必要的方法")
print("5. 文档化：使代码的意图和接口更加清晰")

print("\n主要用途:")
print("1. 类型检查和接口验证：确保函数接收的对象满足预期接口")
print("2. 创建自定义集合类型：通过继承抽象基类简化实现")
print("3. API设计：定义清晰的接口，提高代码的可维护性")
print("4. 类型提示：在类型注解系统中使用抽象基类定义接口")
print("5. 代码文档：通过类型系统提供额外的代码文档")

print("\n最佳实践:")
print("1. 优先使用Python内置集合类型，只在需要特殊行为时创建自定义类型")
print("2. 实现自定义集合类型时，继承适当的抽象基类确保接口一致性")
print("3. 对于性能关键路径，考虑直接实现所有必要方法而不是依赖混入方法")
print("4. 在Python 3.3+中，直接从collections.abc模块导入抽象基类")
print("5. 在类型检查时，优先检查最具体的抽象基类")
print("6. 避免过度使用类型检查，Python通常更适合"鸭子类型"方法")
print("7. 为自定义集合类提供有用的文档字符串，说明其行为和特殊属性")

print("\ncollections.abc模块是Python类型系统的重要组成部分，它通过提供标准接口定义，")
print("帮助开发者创建更一致、更可维护的代码。无论是进行类型检查、创建自定义集合类型，")
print("还是设计API，collections.abc都提供了强大而灵活的工具，使得Python代码更加健壮和可读。")
