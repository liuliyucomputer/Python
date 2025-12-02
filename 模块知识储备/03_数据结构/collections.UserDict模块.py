# collections.UserDict模块 - Python中的字典基类

"""
本文件详细介绍Python标准库中collections.UserDict模块的功能、用法和应用场景。
collections.UserDict是一个字典的包装类，为自定义字典行为提供了一个更方便的基类。

主要内容包括：
- UserDict的核心功能和特性
- 基本使用方法
- 自定义字典行为的实现
- 与继承dict的对比
- 实际应用场景和示例
- 高级用法和最佳实践
"""

from collections import UserDict
import copy

# 1. UserDict的核心功能和特性

print("=== 1. UserDict的核心功能和特性 ===")
print("collections.UserDict是Python collections模块中提供的一个字典包装类，为自定义字典行为提供了更方便的基类：")
print("- 提供了一个围绕字典的包装器，包含一个真实的内部字典(self.data)")
print("- 与直接继承dict相比，UserDict提供了更统一的接口和更好的实现一致性")
print("- 重写__getitem__, __setitem__, __delitem__等方法时更加直观，不会遇到dict子类的一些陷阱")
print("- 所有字典的标准方法都已实现，用户只需重写需要自定义的方法")
print("- 内部使用self.data字典存储实际数据，便于操作")
print("- 适用于创建自定义字典类型，添加新功能或修改现有功能")
print("- 支持所有字典操作，包括键值对的增删改查、迭代、长度获取等")

# 2. 基本使用方法

print("\n=== 2. UserDict的基本使用方法 ===")

## 2.1 创建UserDict对象
print("\n2.1 创建UserDict对象")

# 方法1：创建空的UserDict
empty_dict = UserDict()
print(f"创建空的UserDict: {empty_dict}")

# 方法2：通过字典创建UserDict
regular_dict = {"a": 1, "b": 2, "c": 3}
user_dict1 = UserDict(regular_dict)
print(f"通过字典创建UserDict: {user_dict1}")

# 方法3：通过键值对参数创建UserDict
user_dict2 = UserDict(a=1, b=2, c=3)
print(f"通过键值对参数创建UserDict: {user_dict2}")

# 方法4：通过可迭代对象创建UserDict
items = [("a", 1), ("b", 2), ("c", 3)]
user_dict3 = UserDict(items)
print(f"通过可迭代对象创建UserDict: {user_dict3}")

## 2.2 基本字典操作
print("\n2.2 基本字典操作")

# 创建一个UserDict实例
ud = UserDict({"a": 1, "b": 2})
print(f"初始UserDict: {ud}")

# 添加键值对
ud["c"] = 3
print(f"添加键值对后: {ud}")

# 更新键值对
ud["a"] = 10
print(f"更新键值对后: {ud}")

# 获取值
print(f"获取'a'的值: {ud['a']}")
print(f"使用get()获取'd'的值: {ud.get('d', 'default')}")

# 检查键是否存在
print(f"键'b'是否存在: {'b' in ud}")
print(f"键'd'是否存在: {'d' in ud}")

# 删除键值对
del ud["b"]
print(f"删除键'b'后: {ud}")

# 获取所有键
print(f"所有键: {list(ud.keys())}")

# 获取所有值
print(f"所有值: {list(ud.values())}")

# 获取所有键值对
print(f"所有键值对: {list(ud.items())}")

# 获取字典长度
print(f"字典长度: {len(ud)}")

# 清空字典
ud.clear()
print(f"清空后: {ud}")

## 2.3 访问内部data字典
print("\n2.3 访问内部data字典")

# UserDict内部使用self.data存储实际数据
ud = UserDict({"a": 1, "b": 2})
print(f"UserDict对象: {ud}")
print(f"内部data字典: {ud.data}")

# 可以直接操作data字典
ud.data["c"] = 3
print(f"通过data添加键值对后: {ud}")

# 类型检查
print(f"UserDict类型: {type(ud)}")
print(f"内部data字典类型: {type(ud.data)}")
print(f"普通字典类型: {type({})}")

# 3. 自定义字典行为

print("\n=== 3. 自定义字典行为 ===")

## 3.1 重写基本方法
print("\n3.1 重写基本方法")

class CaseInsensitiveDict(UserDict):
    """大小写不敏感的字典"""
    
    def __getitem__(self, key):
        # 将键转换为小写后再查找
        if isinstance(key, str):
            key = key.lower()
        return self.data[key]
    
    def __setitem__(self, key, value):
        # 将键转换为小写后再存储
        if isinstance(key, str):
            key = key.lower()
        self.data[key] = value
    
    def __delitem__(self, key):
        # 将键转换为小写后再删除
        if isinstance(key, str):
            key = key.lower()
        del self.data[key]
    
    def __contains__(self, key):
        # 将键转换为小写后再检查
        if isinstance(key, str):
            key = key.lower()
        return key in self.data

# 测试大小写不敏感的字典
print("测试大小写不敏感的字典:")
ci_dict = CaseInsensitiveDict()

# 添加键值对
ci_dict["Name"] = "John"
ci_dict["age"] = 30

# 使用不同大小写访问
print(f"ci_dict['Name'] = {ci_dict['Name']}")
print(f"ci_dict['name'] = {ci_dict['name']}")
print(f"ci_dict['NAME'] = {ci_dict['NAME']}")

# 检查键是否存在
print(f"'Name' in ci_dict: {'Name' in ci_dict}")
print(f"'name' in ci_dict: {'name' in ci_dict}")

# 修改值
ci_dict["NAME"] = "Jane"
print(f"修改后 ci_dict['name'] = {ci_dict['name']}")

# 删除键
# del ci_dict["Age"]  # 这会抛出KeyError，因为我们没有添加'Age'键
del ci_dict["age"]
print(f"删除'age'后: {ci_dict}")

## 3.2 重写字典方法
print("\n3.2 重写字典方法")

class LoggingDict(UserDict):
    """记录所有操作的字典"""
    
    def __init__(self, *args, **kwargs):
        print(f"初始化LoggingDict: args={args}, kwargs={kwargs}")
        super().__init__(*args, **kwargs)
    
    def __getitem__(self, key):
        print(f"获取键 '{key}' 的值")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print(f"设置键 '{key}' 的值为 {value}")
        super().__setitem__(key, value)
    
    def __delitem__(self, key):
        print(f"删除键 '{key}'")
        super().__delitem__(key)
    
    def update(self, *args, **kwargs):
        print(f"更新字典: args={args}, kwargs={kwargs}")
        super().update(*args, **kwargs)
    
    def get(self, key, default=None):
        print(f"使用get获取键 '{key}' 的值，默认值为 {default}")
        return super().get(key, default)

# 测试日志字典
print("测试日志字典:")
log_dict = LoggingDict(a=1, b=2)
print(f"初始字典: {log_dict}")

# 获取值
value = log_dict["a"]
print(f"获取的值: {value}")

# 设置值
log_dict["c"] = 3

# 使用get方法
value = log_dict.get("d", 0)
print(f"get方法返回: {value}")

# 更新字典
log_dict.update({"d": 4}, e=5)

# 删除键
del log_dict["b"]

print(f"最终字典: {log_dict}")

## 3.3 添加新功能
print("\n3.3 添加新功能")

class DefaultValueDict(UserDict):
    """支持默认值的字典"""
    
    def __init__(self, default_factory=None, *args, **kwargs):
        self.default_factory = default_factory
        super().__init__(*args, **kwargs)
    
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except KeyError:
            if self.default_factory is None:
                raise
            # 创建默认值
            default_value = self.default_factory()
            self[key] = default_value
            return default_value
    
    def set_default_factory(self, factory):
        """设置默认值工厂函数"""
        self.default_factory = factory
    
    def increment(self, key, amount=1):
        """增加指定键的值"""
        self[key] = self.get(key, 0) + amount
    
    def append(self, key, value):
        """向列表类型的值添加元素"""
        if key not in self:
            self[key] = []
        elif not isinstance(self[key], list):
            raise TypeError(f"键 '{key}' 的值不是列表类型")
        self[key].append(value)

# 测试带默认值的字典
print("测试带默认值的字典:")
# 创建一个默认值为0的字典
def_dict = DefaultValueDict(int)

# 访问不存在的键
def_dict["count"] += 1
def_dict["count"] += 1
print(f"count值: {def_dict['count']}")

# 使用increment方法
def_dict.increment("counter")
def_dict.increment("counter", 5)
print(f"counter值: {def_dict['counter']}")

# 创建一个默认值为列表的字典
list_dict = DefaultValueDict(list)

# 使用append方法
list_dict.append("items", 1)
list_dict.append("items", 2)
list_dict.append("items", 3)
print(f"items列表: {list_dict['items']}")

# 设置新的默认工厂函数
list_dict.set_default_factory(str)
list_dict["text"] += "Hello"
list_dict["text"] += " World"
print(f"text值: {list_dict['text']}")

## 3.4 创建不可变字典
print("\n3.4 创建不可变字典")

class ImmutableDict(UserDict):
    """不可变字典"""
    
    def __init__(self, *args, **kwargs):
        # 初始化字典
        super().__init__(*args, **kwargs)
        # 标记为已冻结
        self._frozen = True
    
    def _check_frozen(self):
        """检查字典是否已冻结"""
        if self._frozen:
            raise TypeError("不可变字典不允许修改")
    
    def __setitem__(self, key, value):
        self._check_frozen()
        super().__setitem__(key, value)
    
    def __delitem__(self, key):
        self._check_frozen()
        super().__delitem__(key)
    
    def update(self, *args, **kwargs):
        self._check_frozen()
        super().update(*args, **kwargs)
    
    def clear(self):
        self._check_frozen()
        super().clear()
    
    def pop(self, key, *args):
        self._check_frozen()
        return super().pop(key, *args)
    
    def popitem(self):
        self._check_frozen()
        return super().popitem()
    
    def setdefault(self, key, default=None):
        self._check_frozen()
        return super().setdefault(key, default)
    
    def copy(self):
        """返回一个可变的副本"""
        # 创建普通字典的副本
        return dict(self.data)
    
    @classmethod
    def fromkeys(cls, iterable, value=None):
        """从可迭代对象创建不可变字典"""
        # 先创建普通字典
        d = dict.fromkeys(iterable, value)
        # 再转换为不可变字典
        return cls(d)

# 测试不可变字典
print("测试不可变字典:")
try:
    # 创建不可变字典
    imm_dict = ImmutableDict(a=1, b=2, c=3)
    print(f"不可变字典: {imm_dict}")
    
    # 尝试修改
    print("尝试修改不可变字典...")
    imm_dict["a"] = 10
except TypeError as e:
    print(f"错误: {e}")

# 获取值仍然可以
try:
    print(f"获取'a'的值: {imm_dict['a']}")
except TypeError as e:
    print(f"错误: {e}")

# 创建副本
print("创建可变副本:")
mutable_copy = imm_dict.copy()
print(f"副本类型: {type(mutable_copy)}")
print(f"副本内容: {mutable_copy}")

# 修改副本
mutable_copy["a"] = 10
print(f"修改后副本: {mutable_copy}")
print(f"原字典保持不变: {imm_dict}")

# 从可迭代对象创建
print("从可迭代对象创建不可变字典:")
keys = ["x", "y", "z"]
new_imm_dict = ImmutableDict.fromkeys(keys, 0)
print(f"新不可变字典: {new_imm_dict}")

# 4. 与直接继承dict的对比

print("\n=== 4. 与直接继承dict的对比 ===")

## 4.1 直接继承dict的问题
print("\n4.1 直接继承dict的问题")

class DirectDict(dict):
    """直接继承dict的字典"""
    
    def __getitem__(self, key):
        print(f"DirectDict.__getitem__ called with key: {key}")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print(f"DirectDict.__setitem__ called with key: {key}, value: {value}")
        super().__setitem__(key, value)

class UserDictSubclass(UserDict):
    """继承UserDict的字典"""
    
    def __getitem__(self, key):
        print(f"UserDictSubclass.__getitem__ called with key: {key}")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print(f"UserDictSubclass.__setitem__ called with key: {key}, value: {value}")
        super().__setitem__(key, value)

# 测试直接继承dict的问题
print("测试直接继承dict的问题:")
dd = DirectDict()

# 使用__setitem__方法设置值
dd["a"] = 1  # 这里会调用我们重写的__setitem__

# 使用update方法更新值
print("使用update方法:")
dd.update({"b": 2})  # 这里不会调用我们重写的__setitem__，而是直接调用dict的update方法

# 测试UserDict子类
print("\n测试UserDict子类:")
ud = UserDictSubclass()

# 使用__setitem__方法设置值nud["a"] = 1  # 这里会调用我们重写的__setitem__

# 使用update方法更新值
print("使用update方法:")
ud.update({"b": 2})  # 这里会调用我们重写的__setitem__

## 4.2 对比总结
print("\n4.2 对比总结")

print("直接继承dict vs 继承UserDict的对比:")
print("1. 方法调用一致性:")
print("   - dict子类: 某些方法如update()可能绕过重写的__setitem__")
print("   - UserDict: 所有修改数据的方法都通过重写的__setitem__进行，保证一致性")

print("\n2. 内部数据存储:")
print("   - dict子类: 数据直接存储在实例本身")
print("   - UserDict: 数据存储在self.data属性中，便于操作和自定义")

print("\n3. 实现复杂度:")
print("   - dict子类: 需要注意覆盖所有可能绕过自定义方法的内置操作")
print("   - UserDict: 实现更简单，只需重写需要自定义的方法")

print("\n4. 继承体系:")
print("   - dict子类: 直接继承自内置dict类型")
print("   - UserDict: 继承自MutableMapping抽象基类，实现更完整的映射接口")

print("\n5. 初始化行为:")
print("   - dict子类: 初始化行为可能需要特别处理")
print("   - UserDict: 初始化行为更直观，通过self.data管理")

# 5. 实际应用场景

print("\n=== 5. 实际应用场景 ===")

## 5.1 自定义验证字典
print("\n5.1 自定义验证字典")

class ValidatedDict(UserDict):
    """带验证功能的字典"""
    
    def __init__(self, validators=None, *args, **kwargs):
        self.validators = validators or {}
        super().__init__(*args, **kwargs)
    
    def __setitem__(self, key, value):
        # 验证值
        if key in self.validators:
            validator = self.validators[key]
            if isinstance(validator, type):
                # 如果验证器是类型，检查值类型
                if not isinstance(value, validator):
                    raise TypeError(f"键 '{key}' 的值必须是 {validator.__name__} 类型")
            elif callable(validator):
                # 如果验证器是函数，调用函数验证
                if not validator(value):
                    raise ValueError(f"键 '{key}' 的值 '{value}' 不满足验证条件")
            else:
                raise TypeError(f"键 '{key}' 的验证器必须是类型或可调用对象")
        
        # 验证通过，设置值
        super().__setitem__(key, value)
    
    def update(self, *args, **kwargs):
        # 先创建临时字典存储要更新的值
        temp_dict = dict(*args, **kwargs)
        
        # 验证所有值
        for key, value in temp_dict.items():
            self.__setitem__(key, value)
    
    def add_validator(self, key, validator):
        """添加验证器"""
        self.validators[key] = validator
        # 对已存在的值进行验证
        if key in self:
            self.__setitem__(key, self[key])
    
    def remove_validator(self, key):
        """移除验证器"""
        if key in self.validators:
            del self.validators[key]

# 测试验证字典
print("测试验证字典:")

# 创建验证器
def is_positive(value):
    return isinstance(value, int) and value > 0

def is_not_empty(value):
    return isinstance(value, str) and value.strip() != ""

# 创建带验证器的字典
validators = {
    "age": is_positive,
    "name": is_not_empty,
    "scores": list,
    "active": bool
}

valid_dict = ValidatedDict(validators)

try:
    # 添加有效的值
    valid_dict["name"] = "Alice"
    valid_dict["age"] = 25
    valid_dict["scores"] = [85, 90, 95]
    valid_dict["active"] = True
    print(f"验证通过的字典: {valid_dict}")
    
    # 尝试添加无效的值
    print("尝试添加无效的年龄...")
    valid_dict["age"] = -5
except ValueError as e:
    print(f"验证错误: {e}")

try:
    print("尝试添加空名字...")
    valid_dict["name"] = "   "
except ValueError as e:
    print(f"验证错误: {e}")

try:
    print("尝试添加错误类型的分数...")
    valid_dict["scores"] = "not a list"
except TypeError as e:
    print(f"验证错误: {e}")

# 测试update方法
print("\n测试update方法:")
try:
    valid_dict.update({"age": 30, "new_key": "value"})
    print(f"更新后的字典: {valid_dict}")
    
    print("尝试更新无效值...")
    valid_dict.update({"age": -10})
except ValueError as e:
    print(f"验证错误: {e}")

# 测试添加/移除验证器
print("\n测试添加/移除验证器:")

# 添加新验证器
valid_dict.add_validator("new_key", is_not_empty)
print("添加新验证器后，'new_key'已验证通过")

try:
    valid_dict["new_key"] = ""
    print("错误：空值应该被拒绝")
except ValueError as e:
    print(f"验证错误: {e}")

# 移除验证器
valid_dict.remove_validator("new_key")
valid_dict["new_key"] = ""
print(f"移除验证器后，可以设置空值: {valid_dict['new_key']}")

## 5.2 有序属性字典
print("\n5.2 有序属性字典")

class AttrDict(UserDict):
    """支持属性访问的字典"""
    
    def __getattr__(self, name):
        """通过属性访问获取值"""
        try:
            return self[name]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def __setattr__(self, name, value):
        """通过属性访问设置值"""
        # 特殊处理内部属性
        if name == "data":
            super().__setattr__(name, value)
        else:
            self[name] = value
    
    def __delattr__(self, name):
        """通过属性访问删除值"""
        try:
            del self[name]
        except KeyError:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    
    def __dir__(self):
        """返回所有属性和键"""
        return super().__dir__() + list(self.keys())

# 测试属性字典
print("测试属性字典:")
attr_dict = AttrDict()

# 通过字典方式设置值
attr_dict["name"] = "Bob"
attr_dict["age"] = 28

# 通过属性方式访问值
print(f"通过属性访问name: {attr_dict.name}")
print(f"通过属性访问age: {attr_dict.age}")

# 通过属性方式设置值
attr_dict.email = "bob@example.com"
print(f"通过属性设置email: {attr_dict['email']}")

# 通过属性方式删除值
del attr_dict.age
print(f"删除age后: {attr_dict}")

# 尝试访问不存在的属性
try:
    print(attr_dict.address)
except AttributeError as e:
    print(f"错误: {e}")

# 嵌套属性字典
class NestedAttrDict(AttrDict):
    """支持嵌套属性访问的字典"""
    
    def __getitem__(self, key):
        value = super().__getitem__(key)
        # 如果值是字典，转换为NestedAttrDict
        if isinstance(value, dict) and not isinstance(value, NestedAttrDict):
            value = NestedAttrDict(value)
            self[key] = value
        return value
    
    def __setitem__(self, key, value):
        # 如果值是字典，转换为NestedAttrDict
        if isinstance(value, dict) and not isinstance(value, NestedAttrDict):
            value = NestedAttrDict(value)
        super().__setitem__(key, value)

# 测试嵌套属性字典
print("\n测试嵌套属性字典:")
nested_dict = NestedAttrDict()

# 设置嵌套值
nested_dict.user = {"name": "Charlie", "age": 35}
nested_dict.user.contact = {"email": "charlie@example.com", "phone": "123-456-7890"}

# 通过嵌套属性访问
print(f"嵌套属性访问: {nested_dict.user.name}")
print(f"更深层嵌套: {nested_dict.user.contact.email}")

# 修改嵌套值
nested_dict.user.age = 36
print(f"修改嵌套值后: {nested_dict.user.age}")

## 5.3 缓存字典
print("\n5.3 缓存字典")

class LRUCache(UserDict):
    """最近最少使用缓存字典"""
    
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.order = []  # 记录访问顺序
        super().__init__()
    
    def __getitem__(self, key):
        # 获取值
        value = super().__getitem__(key)
        # 更新访问顺序
        if key in self.order:
            self.order.remove(key)
        self.order.append(key)
        return value
    
    def __setitem__(self, key, value):
        # 如果键已存在，先删除旧的访问记录
        if key in self:
            self.order.remove(key)
        # 如果缓存已满，删除最久未使用的项
        elif len(self) >= self.max_size:
            oldest_key = self.order.pop(0)
            del self[oldest_key]
        # 设置新值
        super().__setitem__(key, value)
        # 添加到访问顺序末尾
        self.order.append(key)
    
    def __delitem__(self, key):
        # 删除值
        super().__delitem__(key)
        # 从访问顺序中移除
        if key in self.order:
            self.order.remove(key)
    
    def clear(self):
        # 清空缓存
        super().clear()
        self.order.clear()
    
    def get(self, key, default=None):
        try:
            return self[key]  # 使用__getitem__以更新访问顺序
        except KeyError:
            return default
    
    def get_lru_stats(self):
        """获取缓存统计信息"""
        return {
            "size": len(self),
            "max_size": self.max_size,
            "hit_ratio": "N/A"  # 可以扩展实现命中率计算
        }

# 测试LRU缓存
print("测试LRU缓存:")

# 创建一个最大容量为3的缓存
cache = LRUCache(max_size=3)

# 添加项
cache["a"] = 1
cache["b"] = 2
cache["c"] = 3
print(f"初始缓存: {cache}")
print(f"访问顺序: {cache.order}")

# 访问已有项，会更新访问顺序
value = cache["a"]
print(f"访问'a'后: {cache.order}")

# 添加新项，会淘汰最久未使用的项('b')
cache["d"] = 4
print(f"添加'd'后，缓存: {cache}")
print(f"访问顺序: {cache.order}")

# 验证'b'已被淘汰
print(f"'b'是否在缓存中: {'b' in cache}")

# 获取统计信息
stats = cache.get_lru_stats()
print(f"缓存统计: {stats}")

## 5.4 配置管理字典
print("\n5.4 配置管理字典")

class ConfigDict(UserDict):
    """配置管理字典"""
    
    def __init__(self, defaults=None, required_keys=None, *args, **kwargs):
        self.defaults = defaults or {}
        self.required_keys = required_keys or set()
        # 先加载默认值
        super().__init__(self.defaults)
        # 再更新提供的值
        self.update(*args, **kwargs)
        # 验证必需的键
        self._validate_required_keys()
    
    def _validate_required_keys(self):
        """验证所有必需的键是否存在"""
        missing_keys = [key for key in self.required_keys if key not in self]
        if missing_keys:
            raise KeyError(f"缺少必需的配置键: {missing_keys}")
    
    def __setitem__(self, key, value):
        # 设置值
        super().__setitem__(key, value)
        # 如果是必需的键，重新验证
        if key in self.required_keys:
            self._validate_required_keys()
    
    def update(self, *args, **kwargs):
        # 确保提供的参数是字典
        if args:
            if len(args) > 1:
                raise TypeError("update方法只接受一个位置参数")
            other = dict(args[0])
        else:
            other = {}
        other.update(kwargs)
        
        # 对于每个键值对调用__setitem__，以触发验证
        for key, value in other.items():
            self[key] = value
    
    def load_from_file(self, file_path):
        """从文件加载配置"""
        # 这里只是一个示例实现，实际应用中可以根据文件格式使用不同的解析方法
        import json
        try:
            with open(file_path, 'r') as f:
                config = json.load(f)
            self.update(config)
            return True
        except Exception as e:
            print(f"从文件加载配置失败: {e}")
            return False
    
    def save_to_file(self, file_path):
        """保存配置到文件"""
        import json
        try:
            with open(file_path, 'w') as f:
                json.dump(dict(self), f, indent=2)
            return True
        except Exception as e:
            print(f"保存配置到文件失败: {e}")
            return False
    
    def get_nested(self, keys, default=None):
        """获取嵌套配置值"""
        current = self
        for key in keys:
            if not isinstance(current, dict) or key not in current:
                return default
            current = current[key]
        return current
    
    def set_nested(self, keys, value):
        """设置嵌套配置值"""
        current = self
        # 遍历除最后一个键以外的所有键
        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]
        # 设置最后一个键的值
        current[keys[-1]] = value

# 测试配置管理字典
print("测试配置管理字典:")

# 定义默认值和必需键
defaults = {
    "server": {
        "host": "localhost",
        "port": 8000
    },
    "database": {
        "type": "sqlite",
        "timeout": 30
    },
    "logging": {
        "level": "INFO",
        "file": None
    }
}

required_keys = {"server", "database"}

# 创建配置字典
config = ConfigDict(defaults, required_keys)
print(f"初始配置: {json.dumps(dict(config), indent=2)}")

# 更新配置
config["database"]["type"] = "postgres"
config.set_nested(["logging", "level"], "DEBUG")
print(f"\n更新后配置:")
print(f"数据库类型: {config['database']['type']}")
print(f"日志级别: {config.get_nested(['logging', 'level'])}")

# 测试嵌套访问
port = config.get_nested(["server", "port"])
print(f"服务器端口: {port}")

# 尝试获取不存在的嵌套键
max_connections = config.get_nested(["database", "max_connections"], 10)
print(f"最大连接数: {max_connections}")

# 测试必需键验证
try:
    # 创建一个缺少必需键的配置字典
    invalid_config = ConfigDict({}, required_keys)
except KeyError as e:
    print(f"\n验证错误: {e}")

# 6. 高级用法

print("\n=== 6. 高级用法 ===")

## 6.1 深度复制
print("\n6.1 深度复制")

class DeepCopyDict(UserDict):
    """支持深度复制的字典"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def __getitem__(self, key):
        return copy.deepcopy(super().__getitem__(key))
    
    def __setitem__(self, key, value):
        super().__setitem__(key, copy.deepcopy(value))
    
    def update(self, *args, **kwargs):
        # 深度复制所有更新值
        if args:
            if len(args) > 1:
                raise TypeError("update方法只接受一个位置参数")
            other = copy.deepcopy(dict(args[0]))
        else:
            other = {}
        other.update(kwargs)
        # 对每个键值对进行深度复制
        for key, value in other.items():
            self[key] = value
    
    def copy(self):
        """返回一个深度复制"""
        return copy.deepcopy(self)

# 测试深度复制字典
print("测试深度复制字典:")

# 创建一个包含嵌套列表的字典
original = {"a": 1, "b": [1, 2, 3], "c": {"x": 1, "y": 2}}
deep_dict = DeepCopyDict(original)

# 修改原始值
original["b"].append(4)
original["c"]["z"] = 3

# 验证深度字典不受影响
print(f"原始字典: {original}")
print(f"深度复制字典: {deep_dict}")

# 修改从深度字典获取的值
value = deep_dict["b"]
value.append(10)
print(f"修改获取的值后，深度字典中的值: {deep_dict['b']}")

# 设置新值
deep_dict["d"] = {"m": 1, "n": 2}
print(f"设置新值后: {deep_dict}")

# 6.2 持久化字典
print("\n6.2 持久化字典")

class PersistentDict(UserDict):
    """自动持久化到文件的字典"""
    
    def __init__(self, file_path, *args, **kwargs):
        self.file_path = file_path
        # 尝试从文件加载数据
        self._load()
        # 更新数据
        self.update(*args, **kwargs)
        # 保存到文件
        self._save()
    
    def _load(self):
        """从文件加载数据"""
        import os
        if os.path.exists(self.file_path):
            try:
                import json
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                self.data = data
            except Exception as e:
                print(f"从文件加载数据失败: {e}")
                self.data = {}
        else:
            self.data = {}
    
    def _save(self):
        """保存数据到文件"""
        try:
            import json
            # 确保目录存在
            import os
            os.makedirs(os.path.dirname(os.path.abspath(self.file_path)), exist_ok=True)
            # 保存到文件
            with open(self.file_path, 'w') as f:
                json.dump(self.data, f, indent=2)
            return True
        except Exception as e:
            print(f"保存数据到文件失败: {e}")
            return False
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save()
    
    def __delitem__(self, key):
        super().__delitem__(key)
        self._save()
    
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._save()
    
    def clear(self):
        super().clear()
        self._save()
    
    def pop(self, key, *args):
        value = super().pop(key, *args)
        self._save()
        return value
    
    def popitem(self):
        item = super().popitem()
        self._save()
        return item
    
    def setdefault(self, key, default=None):
        # 检查键是否存在
        if key not in self:
            self[key] = default
            self._save()
            return default
        return self[key]

# 测试持久化字典
print("测试持久化字典:")

# 创建一个临时文件路径（实际应用中应使用真实路径）
temp_file = "temp_config.json"

# 创建持久化字典并添加数据
persistent_dict = PersistentDict(temp_file, name="Test", value=100)
print(f"初始持久化字典: {persistent_dict}")

# 更新数据
persistent_dict["value"] = 200
persistent_dict["new_key"] = "new_value"
print(f"更新后持久化字典: {persistent_dict}")

# 创建新实例，应该能从文件加载数据
print("\n创建新实例，从文件加载数据:")
new_instance = PersistentDict(temp_file)
print(f"新实例: {new_instance}")

# 测试删除
print("\n测试删除:")
del new_instance["new_key"]
print(f"删除后: {new_instance}")

# 清理临时文件
import os
if os.path.exists(temp_file):
    os.remove(temp_file)
    print(f"\n临时文件已清理")

# 6.3 带回调的字典
print("\n6.3 带回调的字典")

class ObservableDict(UserDict):
    """带回调的可观察字典"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 回调函数字典
        self._callbacks = {
            "set": [],    # 设置值的回调
            "delete": [], # 删除值的回调
            "clear": [],  # 清空字典的回调
            "update": []  # 更新字典的回调
        }
    
    def add_callback(self, event_type, callback):
        """添加回调函数
        
        Args:
            event_type: 事件类型，可选值：'set', 'delete', 'clear', 'update'
            callback: 回调函数，接收字典实例和相关参数
        """
        if event_type in self._callbacks:
            if callable(callback):
                self._callbacks[event_type].append(callback)
            else:
                raise TypeError("回调必须是可调用对象")
        else:
            raise ValueError(f"不支持的事件类型: {event_type}")
    
    def remove_callback(self, event_type, callback):
        """移除回调函数"""
        if event_type in self._callbacks:
            if callback in self._callbacks[event_type]:
                self._callbacks[event_type].remove(callback)
    
    def _notify_callbacks(self, event_type, *args, **kwargs):
        """通知所有相关回调"""
        for callback in self._callbacks.get(event_type, []):
            try:
                callback(self, *args, **kwargs)
            except Exception as e:
                print(f"回调函数执行失败: {e}")
    
    def __setitem__(self, key, value):
        old_value = self.get(key)
        super().__setitem__(key, value)
        self._notify_callbacks("set", key, value, old_value)
    
    def __delitem__(self, key):
        if key in self:
            old_value = self[key]
            super().__delitem__(key)
            self._notify_callbacks("delete", key, old_value)
    
    def clear(self):
        old_data = dict(self.data)
        super().clear()
        self._notify_callbacks("clear", old_data)
    
    def update(self, *args, **kwargs):
        old_data = dict(self.data)
        super().update(*args, **kwargs)
        # 确定更新的数据
        updated_data = dict(*args, **kwargs)
        self._notify_callbacks("update", updated_data, old_data)

# 测试可观察字典
print("测试可观察字典:")

# 创建回调函数
def on_set_callback(d, key, new_value, old_value):
    if old_value is None:
        print(f"回调: 添加键 '{key}' = {new_value}")
    else:
        print(f"回调: 更新键 '{key}': {old_value} -> {new_value}")

def on_delete_callback(d, key, old_value):
    print(f"回调: 删除键 '{key}' = {old_value}")

def on_clear_callback(d, old_data):
    print(f"回调: 清空字典，原数据: {old_data}")

# 创建可观察字典并添加回调
obs_dict = ObservableDict(a=1, b=2)
obs_dict.add_callback("set", on_set_callback)
obs_dict.add_callback("delete", on_delete_callback)
obs_dict.add_callback("clear", on_clear_callback)

# 测试设置值
print("\n测试设置值:")
obs_dict["a"] = 10  # 更新现有键
obs_dict["c"] = 3  # 添加新键

# 测试删除值
print("\n测试删除值:")
del obs_dict["b"]

# 测试更新
print("\n测试更新:")
obs_dict.update({"d": 4, "e": 5})

# 测试清空
print("\n测试清空:")
obs_dict.clear()

# 测试移除回调
print("\n测试移除回调后:")
obs_dict.remove_callback("set", on_set_callback)
obs_dict["a"] = 1  # 不会触发回调
print(f"字典当前状态: {obs_dict}")

# 7. 使用注意事项和最佳实践

print("\n=== 7. 使用注意事项和最佳实践 ===")

print("\n7.1 注意事项")
print("1. 重写方法时注意完整性: 确保重写的方法与原始接口保持一致")
print("2. 性能考虑: 某些自定义功能可能会影响字典的性能，特别是在大数据量场景下")
print("3. 继承体系: 了解UserDict在Python集合继承体系中的位置")
print("4. 序列化: 自定义字典在序列化和反序列化时可能需要特殊处理")
print("5. 线程安全: UserDict本身不是线程安全的，多线程环境需要额外同步机制")
print("6. 内存使用: 某些高级功能可能会增加内存消耗")
print("7. 兼容性: 确保自定义字典与期望使用标准字典的代码兼容")

print("\n7.2 最佳实践")
print("1. 只重写必要的方法: 只重写需要自定义行为的方法，其他方法使用父类实现")
print("2. 使用super()调用父类方法: 确保正确调用父类方法，保持继承链完整")
print("3. 文档化自定义行为: 清晰记录自定义字典的特殊行为和用法")
print("4. 考虑抽象基类: 在需要定义接口时，考虑使用collections.abc中的抽象基类")
print("5. 测试边界情况: 全面测试空字典、重复键、特殊键等边界情况")
print("6. 性能优化: 对性能关键路径进行优化，避免不必要的操作")
print("7. 复用现有实现: 尽量复用Python标准库中的现有实现")
            return False
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._save()
    
    def __delitem__(self, key):
        super().__delitem__(key)
        self._save()
    
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._save()
    
    def clear(self):
        super().clear()
        self._save()
    
    def pop(self, key, *args):
        value = super().pop(key, *args)
        self._save()
        return value
    
    def popitem(self):
        item = super().popitem()
        self._save()
        return item
    
    def setdefault(self, key, default=None):
        # 检查键是否存在
        if key not in self:
            self[key] = default
            self._save()
            return default
        return self[key]

# 测试持久化字典
print("测试持久化字典:")

# 创建一个临时文件路径（实际应用中应使用真实路径）
temp_file = "temp_config.json"

# 创建持久化字典并添加数据
persistent_dict = PersistentDict(temp_file, name="Test", value=100)
print(f"初始持久化字典: {persistent_dict}")

# 更新数据
persistent_dict["value"] = 200
persistent_dict["new_key"] = "new_value"
print(f"更新后持久化字典: {persistent_dict}")

# 创建新实例，应该能从文件加载数据
print("\n创建新实例，从文件加载数据:")
new_instance = PersistentDict(temp_file)
print(f"新实例: {new_instance}")

# 测试删除
print("\n测试删除:")
del new_instance["new_key"]
print(f"删除后: {new_instance}")

# 清理临时文件
import os
if os.path.exists(temp_file):
    os.remove(temp_file)
    print(f"\n临时文件已清理")

## 6.3 带回调的字典
print("\n6.3 带回调的字典")

class ObservableDict(UserDict):
    """带回调的可观察字典"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 回调函数字典
        self._callbacks = {
            "set": [],    # 设置值的回调
            "delete": [], # 删除值的回调
            "clear": [],  # 清空字典的回调
            "update": []  # 更新字典的回调
        }
    
    def add_callback(self, event_type, callback):
        """添加回调函数
        
        Args:
            event_type: 事件类型，可选值：'set', 'delete', 'clear', 'update'
            callback: 回调函数，接收字典实例和相关参数
        """
        if event_type in self._callbacks:
            if callable(callback):
                self._callbacks[event_type].append(callback)
            else:
                raise TypeError("回调必须是可调用对象")
        else:
            raise ValueError(f"不支持的事件类型: {event_type}")
    
    def remove_callback(self, event_type, callback):
        """移除回调函数"""
        if event_type in self._callbacks:
            if callback in self._callbacks[event_type]:
                self._callbacks[event_type].remove(callback)
    
    def _notify_callbacks(self, event_type, *args, **kwargs):
        """通知所有相关回调"""
        for callback in self._callbacks.get(event_type, []):
            try:
                callback(self, *args, **kwargs)
            except Exception as e:
                print(f"回调函数执行失败: {e}")
    
    def __setitem__(self, key, value):
        old_value = self.get(key)
        super().__setitem__(key, value)
        self._notify_callbacks("set", key, value, old_value)
    
    def __delitem__(self, key):
        if key in self:
            old_value = self[key]
            super().__delitem__(key)
            self._notify_callbacks("delete", key, old_value)
    
    def clear(self):
        old_data = dict(self.data)
        super().clear()
        self._notify_callbacks("clear", old_data)
    
    def update(self, *args, **kwargs):
        old_data = dict(self.data)
        super().update(*args, **kwargs)
        # 确定更新的数据
        updated_data = dict(*args, **kwargs)
        self._notify_callbacks("update", updated_data, old_data)

# 测试可观察字典
print("测试可观察字典:")

# 创建回调函数
def on_set_callback(d, key, new_value, old_value):
    if old_value is None:
        print(f"回调: 添加键 '{key}' = {new_value}")
    else:
        print(f"回调: 更新键 '{key}': {old_value} -> {new_value}")

def on_delete_callback(d, key, old_value):
    print(f"回调: 删除键 '{key}' = {old_value}")

def on_clear_callback(d, old_data):
    print(f"回调: 清空字典，原数据: {old_data}")

# 创建可观察字典并添加回调
obs_dict = ObservableDict(a=1, b=2)
obs_dict.add_callback("set", on_set_callback)
obs_dict.add_callback("delete", on_delete_callback)
obs_dict.add_callback("clear", on_clear_callback)

# 测试设置值
print("\n测试设置值:")
obs_dict["a"] = 10  # 更新现有键
obs_dict["c"] = 3  # 添加新键

# 测试删除值
print("\n测试删除值:")
del obs_dict["b"]

# 测试更新
print("\n测试更新:")
obs_dict.update({"d": 4, "e": 5})

# 测试清空
print("\n测试清空:")
obs_dict.clear()

# 测试移除回调
print("\n测试移除回调后:")
obs_dict.remove_callback("set", on_set_callback)
obs_dict["a"] = 1  # 不会触发回调
print(f"字典当前状态: {obs_dict}")

# 7. 使用注意事项和最佳实践

print("\n=== 7. 使用注意事项和最佳实践 ===")

print("\n7.1 注意事项")
print("1. 重写方法时注意完整性: 确保重写的方法与原始接口保持一致")
print("2. 性能考虑: 某些自定义功能可能会影响字典的性能，特别是在大数据量场景下")
print("3. 继承体系: 了解UserDict在Python集合继承体系中的位置")
print("4. 序列化: 自定义字典在序列化和反序列化时可能需要特殊处理")
print("5. 线程安全: UserDict本身不是线程安全的，多线程环境需要额外同步机制")
print("6. 内存使用: 某些高级功能可能会增加内存消耗")
print("7. 兼容性: 确保自定义字典与期望使用标准字典的代码兼容")

print("\n7.2 最佳实践")
print("1. 只重写必要的方法: 只重写需要自定义行为的方法，其他方法使用父类实现")
print("2. 使用super()调用父类方法: 确保正确调用父类方法，保持继承链完整")
print("3. 文档化自定义行为: 清晰记录自定义字典的特殊行为和用法")
print("4. 考虑抽象基类: 在需要定义接口时，考虑使用collections.abc中的抽象基类")
print("5. 测试边界情况: 全面测试空字典、重复键、特殊键等边界情况")
print("6. 性能优化: 对性能关键路径进行优化，避免不必要的操作")
print("7. 复用现有实现: 尽量复用Python标准库中的现有实现")

# 8. 综合示例：JSON配置管理系统

print("\n=== 8. 综合示例：JSON配置管理系统 ===")

class JSONConfigManager:
    """JSON配置管理系统"""
    
    class ConfigDict(UserDict):
        """配置字典，支持嵌套访问和类型验证"""
        
        def __init__(self, parent_manager=None, path=None, *args, **kwargs):
            self.parent_manager = parent_manager
            self.path = path or []
            super().__init__(*args, **kwargs)
        
        def __getitem__(self, key):
            value = super().__getitem__(key)
            # 如果值是字典，返回ConfigDict子实例
            if isinstance(value, dict) and not isinstance(value, JSONConfigManager.ConfigDict):
                new_path = self.path + [key]
                value = JSONConfigManager.ConfigDict(self.parent_manager, new_path, value)
                self[key] = value  # 更新为ConfigDict实例
            return value
        
        def __setitem__(self, key, value):
            # 如果值是字典，转换为ConfigDict
            if isinstance(value, dict) and not isinstance(value, JSONConfigManager.ConfigDict):
                new_path = self.path + [key]
                value = JSONConfigManager.ConfigDict(self.parent_manager, new_path, value)
            super().__setitem__(key, value)
            # 通知父管理器配置已更改
            if self.parent_manager:
                self.parent_manager._on_config_changed()
        
        def __delitem__(self, key):
            super().__delitem__(key)
            # 通知父管理器配置已更改
            if self.parent_manager:
                self.parent_manager._on_config_changed()
        
        def update(self, *args, **kwargs):
            # 确保所有字典值都转换为ConfigDict
            other = dict(*args, **kwargs)
            for k, v in other.items():
                if isinstance(v, dict) and not isinstance(v, JSONConfigManager.ConfigDict):
                    new_path = self.path + [k]
                    other[k] = JSONConfigManager.ConfigDict(self.parent_manager, new_path, v)
            super().update(other)
            # 通知父管理器配置已更改
            if self.parent_manager:
                self.parent_manager._on_config_changed()
        
        def clear(self):
            super().clear()
            # 通知父管理器配置已更改
            if self.parent_manager:
                self.parent_manager._on_config_changed()
        
        def get_nested(self, keys, default=None):
            """获取嵌套配置值"""
            current = self
            for key in keys:
                if not isinstance(current, dict) or key not in current:
                    return default
                current = current[key]
            return current
        
        def set_nested(self, keys, value):
            """设置嵌套配置值"""
            current = self
            # 遍历除最后一个键以外的所有键
            for key in keys[:-1]:
                if key not in current or not isinstance(current[key], dict):
                    new_path = self.path + keys[:keys.index(key)+1]
                    current[key] = JSONConfigManager.ConfigDict(self.parent_manager, new_path, {})
                current = current[key]
            # 设置最后一个键的值
            current[keys[-1]] = value
            # 通知父管理器配置已更改
            if self.parent_manager:
                self.parent_manager._on_config_changed()
    
    def __init__(self, config_file=None, auto_save=True):
        self.config_file = config_file
        self.auto_save = auto_save
        self._modified = False
        # 创建配置字典
        self.config = self.ConfigDict(self, [])
        # 如果提供了配置文件，加载配置
        if config_file:
            self.load()
    
    def _on_config_changed(self):
        """配置更改回调"""
        self._modified = True
        if self.auto_save and self.config_file:
            self.save()
    
    def load(self, file_path=None):
        """从文件加载配置"""
        file_path = file_path or self.config_file
        if not file_path:
            raise ValueError("未提供配置文件路径")
        
        try:
            import json
            import os
            
            # 检查文件是否存在
            if not os.path.exists(file_path):
                # 如果文件不存在，创建空配置
                self.config = self.ConfigDict(self, [])
                self.save(file_path)
  
# 8. 综合示例：JSON配置管理系统

print("\n=== 8. 综合示例：JSON配置管理系统 ===")

# 创建一个增强的配置管理字典
class ConfigDict(UserDict):
    """
    配置管理字典，支持自动保存、验证、默认值等功能
    """
    
    def __init__(self, config_file=None, defaults=None, *args, **kwargs):
        """
        初始化配置字典
        
        Args:
            config_file: 配置文件路径
            defaults: 默认配置字典
        """
        # 先加载默认配置
        if defaults:
            super().__init__(defaults)
        else:
            super().__init__()
        
        # 加载用户配置
        self.update(*args, **kwargs)
        
        self.config_file = config_file
        self._validators = {}
        
        # 如果提供了配置文件路径，尝试加载
        if self.config_file:
            self._load_from_file()
    
    def set_validator(self, key, validator_func):
        """
        设置键的验证器函数
        
        Args:
            key: 要验证的键
            validator_func: 验证函数，返回True表示验证通过
        """
        self._validators[key] = validator_func
    
    def _validate(self, key, value):
        """
        验证值是否符合要求
        """
        if key in self._validators:
            if not self._validators[key](value):
                raise ValueError(f"验证失败: 键 '{key}' 的值 '{value}' 不符合要求")
    
    def _load_from_file(self):
        """
        从JSON文件加载配置
        """
        if not self.config_file:
            return
        
        try:
            import os
            if os.path.exists(self.config_file):
                import json
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    file_config = json.load(f)
                    self.update(file_config)
                    print(f"已从 {self.config_file} 加载配置")
        except Exception as e:
            print(f"从文件加载配置失败: {e}")
    
    def save(self):
        """
        保存配置到JSON文件
        """
        if not self.config_file:
            raise ValueError("未设置配置文件路径")
        
        try:
            import os
            # 确保目录存在
            os.makedirs(os.path.dirname(os.path.abspath(self.config_file)), exist_ok=True)
            
            import json
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
            print(f"配置已保存到 {self.config_file}")
            return True
        except Exception as e:
            print(f"保存配置失败: {e}")
            return False
    
    def __setitem__(self, key, value):
        """
        设置配置项，同时进行验证
        """
        self._validate(key, value)
        super().__setitem__(key, value)
        # 自动保存（可选）
        # self.save()
    
    def update(self, *args, **kwargs):
        """
        更新配置，对每个键值对进行验证
        """
        # 创建临时字典来保存更新内容
        update_dict = dict(*args, **kwargs)
        
        # 先验证所有值
        for key, value in update_dict.items():
            self._validate(key, value)
        
        # 验证通过后再更新
        super().update(update_dict)
    
    def get_int(self, key, default=0):
        """
        获取整数值配置
        """
        try:
            value = self.get(key, default)
            return int(value)
        except (ValueError, TypeError):
            return default
    
    def get_float(self, key, default=0.0):
        """
        获取浮点数值配置
        """
        try:
            value = self.get(key, default)
            return float(value)
        except (ValueError, TypeError):
            return default
    
    def get_bool(self, key, default=False):
        """
        获取布尔值配置，支持多种格式
        """
        value = self.get(key, default)
        if isinstance(value, bool):
            return value
        if isinstance(value, str):
            return value.lower() in ('true', 'yes', '1', 'y', 't')
        if isinstance(value, (int, float)):
            return value != 0
        return bool(value)
    
    def get_list(self, key, default=None):
        """
        获取列表类型配置
        """
        if default is None:
            default = []
        value = self.get(key, default)
        if isinstance(value, str):
            # 尝试解析逗号分隔的字符串
            if ',' in value:
                return [item.strip() for item in value.split(',')]
        if isinstance(value, list):
            return value
        return [value]

# 演示配置管理系统的使用
print("\n演示配置管理系统:")

# 创建临时配置文件路径
import tempfile
config_file = os.path.join(tempfile.gettempdir(), "app_config.json")

# 定义默认配置
default_config = {
    "app_name": "ConfigManager",
    "debug": False,
    "log_level": "INFO",
    "max_connections": 100,
    "timeout": 30.0,
    "allowed_hosts": ["localhost", "127.0.0.1"]
}

# 创建配置管理器
config = ConfigDict(
    config_file=config_file,
    defaults=default_config
)

# 设置验证器
config.set_validator("max_connections", lambda x: isinstance(x, int) and x > 0)
config.set_validator("timeout", lambda x: isinstance(x, (int, float)) and x >= 0)
config.set_validator("log_level", lambda x: x.upper() in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

# 使用配置
print(f"\n应用名称: {config['app_name']}")
print(f"调试模式: {config.get_bool('debug')}")
print(f"日志级别: {config['log_level']}")
print(f"最大连接数: {config.get_int('max_connections')}")
print(f"超时时间: {config.get_float('timeout')}")
print(f"允许的主机: {config.get_list('allowed_hosts')}")

# 更新配置
print("\n更新配置:")
config.update({
    "debug": True,
    "log_level": "DEBUG",
    "max_connections": 200,
    "timeout": 60.0
})

# 保存配置
print("\n保存配置:")
config.save()

# 尝试设置无效值
print("\n尝试设置无效值:")
try:
    config["max_connections"] = -1  # 应该验证失败
    print("验证错误：应该抛出异常但没有")
except ValueError as e:
    print(f"正确捕获验证错误: {e}")

# 尝试更新多个配置，其中一个无效
try:
    config.update({
        "timeout": -10,  # 无效
        "app_name": "NewApp"
    })
    print("验证错误：应该抛出异常但没有")
except ValueError as e:
    print(f"正确捕获验证错误: {e}")

# 加载配置到新实例
print("\n加载保存的配置到新实例:")
new_config = ConfigDict(config_file=config_file)
print(f"新实例中的配置: {dict(new_config)}")

# 清理临时文件
import os
if os.path.exists(config_file):
    os.remove(config_file)
    print(f"\n临时配置文件已清理: {config_file}")

# 9. 总结

print("\n=== 9. 总结 ===")
print("\ncollections.UserDict为Python开发者提供了一个灵活、强大的自定义字典行为的基类。")
print("\n主要优势:")
print("1. 提供了比直接继承dict更简洁的自定义字典行为的方式")
print("2. 内部使用data属性存储实际数据，避免了许多与直接继承dict相关的陷阱")
print("3. 允许开发者轻松重写特定方法，实现所需的自定义行为")
print("4. 完全兼容标准字典接口，可作为字典的直接替代品使用")
print("5. 简化了复杂功能的实现，如类型验证、数据转换、持久化等")

print("\n适用场景:")
print("1. 需要对字典操作添加额外功能，如验证、日志记录或回调")
print("2. 实现特殊行为的字典，如大小写不敏感、有序字典或默认值字典")
print("3. 创建用于特定领域的专业字典类，如配置管理、缓存或数据验证")
print("4. 需要在字典操作中添加业务逻辑的场景")
print("5. 教学和学习Python面向对象编程和继承机制")

print("\n在实际开发中，UserDict是扩展和自定义字典功能的理想选择，")
print("它提供了良好的平衡点，既保持了字典的基本功能和性能，又提供了足够的灵活性来实现复杂的自定义行为。")

print("\n通过合理利用UserDict，开发者可以创建出既符合业务需求又保持代码清晰可维护的自定义数据结构。")
            
            # 加载JSON文件
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 更新配置
            self.config = self.ConfigDict(self, [], data)
            self._modified = False
            return True
        except Exception as e:
            print(f"加载配置文件失败: {e}")
            return False
    
    def save(self, file_path=None):
        """保存配置到文件"""
        file_path = file_path or self.config_file
        if not file_path:
            raise ValueError("未提供配置文件路径")
        
        try:
            import json
            import os
            
            # 确保目录存在
            os.makedirs(os.path.dirname(os.path.abspath(file_path)), exist_ok=True)
            
            # 递归转换ConfigDict为普通字典
            def convert_to_dict(data):
                if isinstance(data, JSONConfigManager.ConfigDict):
                    return {k: convert_to_dict(v) for k, v in data.items()}
                elif isinstance(data, dict):
                    return {k: convert_to_dict(v) for k, v in data.items()}
                elif isinstance(data, list):
                    return [convert_to_dict(v) for v in data]
                else:
                    return data
            
            # 转换配置数据
            config_data = convert_to_dict(self.config)
            
            # 保存到文件
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, ensure_ascii=False, indent=2)
            
            self._modified = False
            return True
        except Exception as e:
            print(f"保存配置文件失败: {e}")
            return False
    
    def get(self, key, default=None):
        """获取配置项"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """设置配置项"""
        self.config[key] = value
    
    def has(self, key):
        """检查配置项是否存在"""
        return key in self.config
    
    def remove(self, key):
        """移除配置项"""
        if key in self.config:
            del self.config[key]
            return True
        return False
    
    def get_nested(self, keys, default=None):
        """获取嵌套配置项"""
        return self.config.get_nested(keys, default)
    
    def set_nested(self, keys, value):
        """设置嵌套配置项"""
        self.config.set_nested(keys, value)
    
    def validate(self, schema):
        """验证配置是否符合schema"""
        # 简单的schema验证实现
        def validate_schema(data, schema, path=""):
            errors = []
            
            # 检查必需的键
            for key, key_schema in schema.items():
                full_path = f"{path}.{key}" if path else key
                
                if "required" in key_schema and key_schema["required"] and key not in data:
                    errors.append(f"缺少必需配置项: {full_path}")
                elif key in data:
                    # 检查类型
                    if "type" in key_schema:
                        expected_type = key_schema["type"]
                        actual_type = type(data[key]).__name__
                        if actual_type != expected_type:
                            errors.append(f"配置项 {full_path} 类型错误: 期望 {expected_type}, 得到 {actual_type}")
                    
                    # 检查值范围
                    if "min" in key_schema and data[key] < key_schema["min"]:
                        errors.append(f"配置项 {full_path} 值小于最小值 {key_schema['min']}")
                    if "max" in key_schema and data[key] > key_schema["max"]:
                        errors.append(f"配置项 {full_path} 值大于最大值 {key_schema['max']}")
                    
                    # 检查选项
                    if "options" in key_schema and data[key] not in key_schema["options"]:
                        errors.append(f"配置项 {full_path} 值不在允许的选项中: {key_schema['options']}")
                    
                    # 递归验证嵌套对象
                    if "schema" in key_schema and isinstance(data[key], dict):
                        nested_errors = validate_schema(data[key], key_schema["schema"], full_path)
                        errors.extend(nested_errors)
            
            return errors
        
        errors = validate_schema(self.config, schema)
        return errors
    
    def export(self):
        """导出配置为普通字典"""
        # 递归转换ConfigDict为普通字典
        def convert_to_dict(data):
            if isinstance(data, JSONConfigManager.ConfigDict):
                return {k: convert_to_dict(v) for k, v in data.items()}
            elif isinstance(data, dict):
                return {k: convert_to_dict(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [convert_to_dict(v) for v in data]
            else:
                return data
        
        return convert_to_dict(self.config)
    
    def import_config(self, data):
        """从字典导入配置"""
        self.config = self.ConfigDict(self, [], data)
        self._modified = True
        if self.auto_save and self.config_file:
            self.save()
    
    def merge(self, data):
        """合并配置"""
        # 递归合并配置
        def merge_dict(dest, src):
            for k, v in src.items():
                if k in dest and isinstance(dest[k], dict) and isinstance(v, dict):
                    merge_dict(dest[k], v)
                else:
                    if isinstance(v, dict):
                        # 转换为ConfigDict
                        path = []  # 这里简化了，实际应该跟踪路径
                        dest[k] = JSONConfigManager.ConfigDict(self, path, v)
                    else:
                        dest[k] = v
        
        merge_dict(self.config, data)
        self._modified = True
        if self.auto_save and self.config_file:
            self.save()
    
    def reset(self):
        """重置配置"""
        self.config = self.ConfigDict(self, [])
        self._modified = True
        if self.auto_save and self.config_file:
            self.save()
    
    def is_modified(self):
        """检查配置是否已修改"""
        return self._modified

# 测试JSON配置管理系统
print("测试JSON配置管理系统:")

# 创建临时文件路径
temp_config_file = "temp_app_config.json"

# 创建配置管理器
config_manager = JSONConfigManager(temp_config_file, auto_save=True)

# 设置基本配置
print("设置基本配置:")
config_manager.set("app_name", "TestApp")
config_manager.set("version", "1.0.0")
config_manager.set("debug", True)

# 设置嵌套配置
print("\n设置嵌套配置:")
config_manager.set_nested(["database", "host"], "localhost")
config_manager.set_nested(["database", "port"], 5432)
config_manager.set_nested(["database", "credentials", "username"], "admin")
config_manager.set_nested(["database", "credentials", "password"], "secure_password")

# 设置服务器配置
server_config = {
    "host": "0.0.0.0",
    "port": 8080,
    "ssl": {
        "enabled": False,
        "cert_file": None,
        "key_file": None
    },
    "max_connections": 100
}
config_manager.set("server", server_config)

# 获取配置
print("\n获取配置:")
print(f"应用名称: {config_manager.get('app_name')}")
print(f"数据库主机: {config_manager.get_nested(['database', 'host'])}")
print(f"SSL是否启用: {config_manager.get_nested(['server', 'ssl', 'enabled'])}")

# 测试验证
print("\n测试配置验证:")
schema = {
    "app_name": {"type": "str", "required": True},
    "version": {"type": "str", "required": True},
    "debug": {"type": "bool"},
    "database": {
        "type": "dict",
        "required": True,
        "schema": {
            "host": {"type": "str", "required": True},
            "port": {"type": "int", "min": 1, "max": 65535},
            "credentials": {
                "type": "dict",
                "required": True,
                "schema": {
                    "username": {"type": "str", "required": True},
                    "password": {"type": "str", "required": True}
                }
            }
        }
    },
    "server": {
        "type": "dict",
        "schema": {
            "host": {"type": "str"},
            "port": {"type": "int", "min": 1, "max": 65535},
            "ssl": {
                "type": "dict",
                "schema": {
                    "enabled": {"type": "bool"}
                }
            }
        }
    }
}

# 验证配置
validation_errors = config_manager.validate(schema)
if validation_errors:
    print("验证错误:")
    for error in validation_errors:
        print(f"  - {error}")
else:
    print("配置验证通过")

# 修改一些配置
print("\n修改配置:")
config_manager.set("debug", False)
config_manager.set_nested(["server", "port"], 8000)

# 导出配置
print("\n导出配置:")
exported_config = config_manager.export()
print(f"配置是否修改: {config_manager.is_modified()}")

# 重新加载配置
print("\n重新加载配置:")
config_manager.load()
print(f"应用名称: {config_manager.get('app_name')}")
print(f"调试模式: {config_manager.get('debug')}")
print(f"服务器端口: {config_manager.get_nested(['server', 'port'])}")

# 测试合并配置
print("\n测试合并配置:")
new_config = {
    "features": {
        "api": True,
        "web": True,
        "cli": False
    },
    "server": {
        "max_connections": 200,
        "timeout": 30
    }
}

config_manager.merge(new_config)
print(f"API功能是否启用: {config_manager.get_nested(['features', 'api'])}")
print(f"服务器最大连接数: {config_manager.get_nested(['server', 'max_connections'])}")
print(f"服务器超时设置: {config_manager.get_nested(['server', 'timeout'])}")

# 清理临时文件
import os
if os.path.exists(temp_config_file):
    os.remove(temp_config_file)
    print(f"\n临时配置文件已清理")

# 9. 总结

print("\n=== 9. 总结 ===")
print("collections.UserDict是Python中用于自定义字典行为的强大工具：")
print("- 提供了一个围绕字典的包装类，包含一个真实的内部字典(self.data)")
print("- 与直接继承dict相比，提供了更统一的接口和更好的实现一致性")
print("- 重写__getitem__, __setitem__, __delitem__等方法时更加直观，不会遇到dict子类的一些陷阱")
print("- 适用于创建自定义字典类型，添加新功能或修改现有功能")

print("\nUserDict特别适合以下应用场景：")
print("- 创建带验证功能的配置字典")
print("- 实现大小写不敏感的字典")
print("- 开发缓存系统，如LRU缓存")
print("- 构建支持属性访问的字典")
print("- 创建持久化字典，自动保存到文件")
print("- 实现可观察字典，支持事件回调")
print("- 开发配置管理系统")

print("\n使用UserDict时，我们需要注意以下几点：")
print("- 合理使用内部的self.data字典进行操作")
print("- 确保重写的方法与原始接口保持一致")
print("- 考虑性能影响，避免在高频路径中做过多额外操作")
print("- 注意线程安全问题，必要时添加同步机制")

print("\n总之，collections.UserDict为我们提供了一种灵活、强大的方式来扩展Python字典的功能，")
print("使我们能够创建满足特定需求的自定义字典类型。通过本文件的学习，")
print("我们已经掌握了UserDict的各种用法和最佳实践，可以在实际开发中灵活运用。")

"""
collections.UserDict模块为Python开发者提供了一个方便的基类，用于创建自定义的字典类型。
与直接继承内置的dict类相比，UserDict提供了更好的一致性和更少的陷阱，使自定义字典行为变得更加简单。

在本文件中，我们全面介绍了UserDict的基本用法、自定义方法的实现、与直接继承dict的对比，
以及各种实际应用场景。我们还开发了几个实用的自定义字典类，如大小写不敏感字典、
带验证功能的字典、LRU缓存等，展示了UserDict的强大功能。

通过综合示例，我们构建了一个完整的JSON配置管理系统，结合了UserDict的各种特性，
实现了配置的加载、保存、验证、嵌套访问等功能。这展示了UserDict在实际项目中的应用价值。

无论是简单的字典扩展，还是复杂的配置管理系统，UserDict都是Python开发者工具箱中的重要组件，
