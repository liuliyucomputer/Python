# dataclasses模块 - 数据类定义工具
# 功能作用：自动为类生成特殊方法，如__init__(), __repr__(), __eq__()等，简化数据类的创建
# 使用情景：需要大量数据存储类、配置类、数据传输对象等场景
# 注意事项：需要Python 3.7+版本；装饰器参数如frozen、slots等会影响类行为；需要注意默认值的可变性问题

import dataclasses
import typing
from typing import List, Dict, Set, Tuple, Optional, Union, Any
import inspect
import sys

# 模块概述
"""
dataclasses模块是Python 3.7中引入的标准库，为数据类提供了简洁的语法和自动生成特殊方法的功能。
数据类是主要用于存储数据的类，通常具有大量属性和默认的特殊方法实现。

使用@dataclass装饰器，我们可以自动生成以下特殊方法：
- __init__()：初始化方法
- __repr__()：字符串表示方法
- __eq__()：相等性比较方法
- __lt__(), __le__(), __gt__(), __ge__()：排序方法（当order=True时）
- __hash__()：哈希方法（当frozen=True或exkwonly=True时）

此外，dataclasses模块还提供了一些辅助函数来操作数据类，如字段访问、类转换等。

主要功能类别：
1. 数据类装饰器和参数
2. 字段定义和默认值
3. 特殊方法自动生成
4. 数据类辅助函数
5. 高级特性（冻结类、继承、类型提示等）
"""

# 1. 基本数据类创建
print("=== 1. 基本数据类创建 ===")

def basic_dataclasses():
    """演示基本数据类的创建和使用"""
    print("使用@dataclass装饰器可以轻松创建数据类：\n")
    
    # 1. 基本数据类定义
    print("1. 基本数据类定义")
    print("   - 使用@dataclass装饰器标记类")
    print("   - 在类体中定义类变量，指定类型注解")
    print("   - 装饰器会自动生成__init__、__repr__和__eq__方法")
    
    # 示例：基本数据类
    print("\n   示例：基本数据类定义和使用")
    
    @dataclasses.dataclass
    class Point:
        x: float
        y: float
        z: float = 0.0  # 带默认值的字段
    
    # 创建实例
    p1 = Point(1.0, 2.0)
    p2 = Point(3.0, 4.0, 5.0)
    
    # 打印实例（自动使用__repr__）
    print(f"     p1 = {p1}")
    print(f"     p2 = {p2}")
    
    # 访问字段
    print(f"     p1.x = {p1.x}, p1.y = {p1.y}, p1.z = {p1.z}")
    
    # 相等性比较（自动使用__eq__）
    p3 = Point(1.0, 2.0)
    print(f"     p1 == p3: {p1 == p3}")
    print(f"     p1 == p2: {p1 == p2}")
    
    # 2. 手动定义vs数据类
    print("\n2. 手动定义类vs数据类比较")
    
    # 手动定义的类
    class ManualPoint:
        def __init__(self, x: float, y: float, z: float = 0.0):
            self.x = x
            self.y = y
            self.z = z
        
        def __repr__(self) -> str:
            return f"ManualPoint(x={self.x}, y={self.y}, z={self.z})"
        
        def __eq__(self, other) -> bool:
            if not isinstance(other, ManualPoint):
                return NotImplemented
            return (
                self.x == other.x and
                self.y == other.y and
                self.z == other.z
            )
    
    print("   手动定义的类需要编写__init__、__repr__、__eq__等方法")
    print("   数据类通过装饰器自动生成这些方法，代码更简洁")
    
    # 3. 数据类的默认行为
    print("\n3. 数据类的默认行为")
    print("   - 自动生成__init__方法，参数顺序与字段定义顺序相同")
    print("   - 自动生成__repr__方法，显示类名和所有字段名及其值")
    print("   - 自动生成__eq__方法，比较所有字段是否相等")
    print("   - 注意：默认不会生成排序方法和哈希方法")
    
    # 示例：验证默认行为
    m1 = ManualPoint(1.0, 2.0)
    m2 = ManualPoint(1.0, 2.0)
    
    print("\n   比较手动类和数据类的行为：")
    print(f"     手动类 - m1: {m1}")
    print(f"     手动类 - m1 == m2: {m1 == m2}")
    print(f"     数据类 - p1: {p1}")
    print(f"     数据类 - p1 == p3: {p1 == p3}")
    
    # 验证默认没有生成__lt__等排序方法
    try:
        p1 < p2
    except TypeError as e:
        print(f"     验证排序方法：{e}")

# 运行基本数据类创建演示
basic_dataclasses()
print()

# 2. 装饰器参数
print("=== 2. 装饰器参数 ===")

def decorator_parameters():
    """演示dataclass装饰器的各种参数"""
    print("@dataclass装饰器支持多个参数，可以控制生成的方法和类行为：\n")
    
    # 1. init参数
    print("1. init参数")
    print("   - 控制是否生成__init__方法")
    print("   - 默认为True")
    print("   - 设为False时，需要手动定义__init__方法")
    
    # 示例：init=False
    print("\n   示例：init=False")
    
    @dataclasses.dataclass(init=False)
    class NoInitClass:
        x: int
        y: int
        
        def __init__(self, x: int):
            self.x = x
            self.y = x * 2  # 自定义初始化逻辑
    
    no_init = NoInitClass(5)
    print(f"     NoInitClass(5) = {no_init}")
    
    # 2. repr参数
    print("\n2. repr参数")
    print("   - 控制是否生成__repr__方法")
    print("   - 默认为True")
    print("   - 设为False时，使用默认的对象表示")
    
    # 示例：repr=False
    print("\n   示例：repr=False")
    
    @dataclasses.dataclass(repr=False)
    class NoReprClass:
        x: int
        y: int
    
    no_repr = NoReprClass(10, 20)
    print(f"     NoReprClass(10, 20) = {no_repr}")
    
    # 3. eq参数
    print("\n3. eq参数")
    print("   - 控制是否生成__eq__方法")
    print("   - 默认为True")
    print("   - 设为False时，使用默认的对象标识比较（is）")
    
    # 示例：eq=False
    print("\n   示例：eq=False")
    
    @dataclasses.dataclass(eq=False)
    class NoEqClass:
        x: int
        y: int
    
    eq1 = NoEqClass(1, 2)
    eq2 = NoEqClass(1, 2)
    print(f"     eq1 = {eq1}")
    print(f"     eq2 = {eq2}")
    print(f"     eq1 == eq2: {eq1 == eq2}  # 使用对象标识比较")
    print(f"     eq1 is eq2: {eq1 is eq2}")
    
    # 4. order参数
    print("\n4. order参数")
    print("   - 控制是否生成排序方法（__lt__, __le__, __gt__, __ge__）")
    print("   - 默认为False")
    print("   - 排序基于字段的定义顺序，逐个比较")
    
    # 示例：order=True
    print("\n   示例：order=True")
    
    @dataclasses.dataclass(order=True)
    class OrderedClass:
        name: str
        age: int
    
    person1 = OrderedClass("Alice", 25)
    person2 = OrderedClass("Bob", 30)
    person3 = OrderedClass("Alice", 30)
    
    print(f"     person1 = {person1}")
    print(f"     person2 = {person2}")
    print(f"     person3 = {person3}")
    print(f"     person1 < person2: {person1 < person2}")  # 先比较name
    print(f"     person1 < person3: {person1 < person3}")  # name相同，比较age
    print(f"     person2 > person3: {person2 > person3}")
    
    # 排序列表
    people = [person2, person3, person1]
    people.sort()  # 使用生成的__lt__方法排序
    print(f"     排序后的列表: {people}")
    
    # 5. unsafe_hash参数
    print("\n5. unsafe_hash参数")
    print("   - 控制是否生成__hash__方法")
    print("   - 默认为None，根据eq和frozen参数自动决定")
    print("   - 设为True时，强制生成__hash__方法（即使类可变）")
    print("   - 设为False时，不生成__hash__方法，实例不能用作字典键或添加到集合中")
    
    # 示例：unsafe_hash=True
    print("\n   示例：unsafe_hash=True")
    
    @dataclasses.dataclass(unsafe_hash=True)
    class HashableClass:
        x: int
        y: int
    
    hash1 = HashableClass(1, 2)
    print(f"     hash1的哈希值: {hash(hash1)}")
    
    # 用作字典键
    d = {hash1: "value"}
    print(f"     字典查找: {d[hash1]}")
    
    # 6. frozen参数
    print("\n6. frozen参数")
    print("   - 创建不可变（冻结）的数据类")
    print("   - 默认为False")
    print("   - 设置为True时，实例创建后不能修改字段值")
    print("   - 自动生成__hash__方法，使实例可哈希（可用于字典键和集合）")
    
    # 示例：frozen=True
    print("\n   示例：frozen=True")
    
    @dataclasses.dataclass(frozen=True)
    class FrozenPoint:
        x: float
        y: float
    
    fp = FrozenPoint(1.0, 2.0)
    print(f"     fp = {fp}")
    print(f"     fp的哈希值: {hash(fp)}")
    
    # 尝试修改字段值会抛出异常
    try:
        fp.x = 3.0
    except dataclasses.FrozenInstanceError as e:
        print(f"     尝试修改冻结类字段: {e}")
    
    # 用作字典键
    frozen_dict = {fp: "frozen point"}
    print(f"     冻结类实例用作字典键: {frozen_dict[fp]}")
    
    # 7. slots参数（Python 3.10+）
    print("\n7. slots参数")
    print("   - 为数据类生成__slots__属性")
    print("   - 默认为False")
    print("   - 设为True时，类将使用__slots__而不是__dict__")
    print("   - 可以减少内存使用并提高属性访问速度")
    print("   - 注意：仅在Python 3.10及以上版本可用")
    
    # 尝试使用slots参数
    try:
        @dataclasses.dataclass(slots=True)
        class SlotsClass:
            x: int
            y: int
        
        sc = SlotsClass(5, 10)
        print(f"     sc = {sc}")
        print(f"     sc是否有__slots__: {'__slots__' in dir(SlotsClass)}")
        
        # 尝试添加动态属性会失败
        try:
            sc.z = 15
        except AttributeError as e:
            print(f"     尝试添加动态属性: {e}")
            
    except TypeError as e:
        print(f"     当前Python版本小于3.10，slots参数不可用: {e}")

# 运行装饰器参数演示
decorator_parameters()
print()

# 3. 字段定义和默认值
print("=== 3. 字段定义和默认值 ===")

def field_definition():
    """演示数据类字段的定义和默认值设置"""
    print("数据类的字段定义支持多种选项，可以控制默认值、默认工厂等行为：\n")
    
    # 1. 基本字段定义
    print("1. 基本字段定义")
    print("   - 字段定义使用类型注解语法: name: type")
    print("   - 可以设置默认值: name: type = default_value")
    print("   - 带默认值的字段必须放在不带默认值的字段后面")
    
    # 2. field函数
    print("\n2. dataclasses.field函数")
    print("   - 提供更精细的字段控制选项")
    print("   - 主要参数：")
    print("     * default: 默认值")
    print("     * default_factory: 默认值工厂函数")
    print("     * init: 是否包含在__init__参数中")
    print("     * repr: 是否在__repr__中包含")
    print("     * compare: 是否在比较方法中包含")
    print("     * hash: 是否在哈希计算中包含")
    print("     * metadata: 存储附加信息的字典")
    
    # 示例：使用field函数
    print("\n   示例：使用field函数定义字段")
    
    @dataclasses.dataclass
    class FieldExample:
        # 普通字段
        name: str
        # 带默认值的字段
        value: int = 0
        # 使用field函数的字段
        tags: List[str] = dataclasses.field(default_factory=list)
        # 不在__init__中的字段
        created_at: float = dataclasses.field(default_factory=time.time, init=False)
        # 不在__repr__中的字段
        secret: str = dataclasses.field(default="", repr=False)
        # 不在比较中的字段
        temp_id: int = dataclasses.field(default=0, compare=False)
        # 带元数据的字段
        config: Dict[str, Any] = dataclasses.field(
            default_factory=dict,
            metadata={"description": "Configuration settings"}
        )
    
    # 创建实例
    example = FieldExample(name="test", secret="hidden", temp_id=123)
    
    # 访问字段
    print(f"     example = {example}")  # secret不在输出中
    print(f"     example.secret = {example.secret}")  # 但可以访问
    print(f"     example.created_at = {example.created_at}")  # 自动设置的字段
    
    # 比较测试
    example2 = FieldExample(name="test", secret="different", temp_id=456)
    print(f"     example == example2: {example == example2}")  # temp_id不参与比较
    
    # 获取字段元数据
    field_config = dataclasses.fields(example)[-1]  # 获取最后一个字段
    print(f"     config字段元数据: {field_config.metadata}")
    
    # 3. 默认值的可变性问题
    print("\n3. 默认值的可变性问题")
    print("   - 对于可变类型（如列表、字典等），不要直接使用它们作为默认值")
    print("   - 应使用default_factory来创建可变类型的默认值")
    
    # 示例：错误的默认值用法
    print("\n   示例：错误的默认值用法")
    
    @dataclasses.dataclass
    class BadDefault:
        items: List[int] = []  # 危险！所有实例共享同一个列表
    
    # 创建两个实例
    b1 = BadDefault()
    b2 = BadDefault()
    
    # 向第一个实例添加元素
    b1.items.append(1)
    
    # 查看两个实例的items
    print(f"     b1.items = {b1.items}")
    print(f"     b2.items = {b2.items}  # 注意：b2也被修改了！")
    
    # 示例：正确的默认值用法
    print("\n   示例：正确的默认值用法")
    
    @dataclasses.dataclass
    class GoodDefault:
        items: List[int] = dataclasses.field(default_factory=list)  # 每个实例有自己的列表
    
    # 创建两个实例
    g1 = GoodDefault()
    g2 = GoodDefault()
    
    # 向第一个实例添加元素
    g1.items.append(1)
    
    # 查看两个实例的items
    print(f"     g1.items = {g1.items}")
    print(f"     g2.items = {g2.items}  # 正确：g2没有被修改")
    
    # 4. 类型注解和默认值组合
    print("\n4. 类型注解和默认值组合")
    print("   - 使用typing模块的类型注解")
    print("   - 处理复杂类型的默认值")
    
    # 示例：复杂类型注解
    print("\n   示例：复杂类型注解")
    
    @dataclasses.dataclass
    class ComplexTypes:
        # 可选类型
        name: Optional[str] = None
        # 联合类型
        value: Union[int, float] = 0
        # 嵌套类型
        coordinates: List[Tuple[float, float]] = dataclasses.field(default_factory=list)
        # 字典类型
        properties: Dict[str, Any] = dataclasses.field(default_factory=dict)
    
    # 创建实例
    complex_obj = ComplexTypes(
        value=3.14,
        coordinates=[(1.0, 2.0), (3.0, 4.0)],
        properties={"color": "red", "size": "medium"}
    )
    
    print(f"     complex_obj = {complex_obj}")

# 运行字段定义和默认值演示
field_definition()
print()

# 4. 数据类辅助函数
print("=== 4. 数据类辅助函数 ===")

def helper_functions():
    """演示dataclasses模块提供的辅助函数"""
    print("dataclasses模块提供了多个辅助函数，用于获取数据类信息和操作数据类：\n")
    
    # 定义一个用于演示的基本数据类
    @dataclasses.dataclass
    class Person:
        name: str
        age: int
        email: Optional[str] = None
    
    # 创建一个实例
    person = Person("Alice", 30, "alice@example.com")
    
    # 1. fields函数
    print("1. dataclasses.fields")
    print("   - 返回数据类的所有字段的Field对象列表")
    print("   - 每个Field对象包含字段名、类型、默认值等信息")
    
    print("\n   示例：使用fields函数获取字段信息")
    
    fields = dataclasses.fields(person)
    print("   Person类的字段信息：")
    for field in fields:
        print(f"     字段名: {field.name}")
        print(f"       类型: {field.type}")
        print(f"       默认值: {field.default if field.default != dataclasses.MISSING else '没有默认值'}")
        print(f"       是否在__init__中: {field.init}")
        print(f"       是否在__repr__中: {field.repr}")
        print(f"       是否在比较中: {field.compare}")
    
    # 2. asdict函数
    print("\n2. dataclasses.asdict")
    print("   - 将数据类实例转换为字典")
    print("   - 递归转换嵌套的数据类和集合类型")
    
    print("\n   示例：使用asdict函数转换为字典")
    person_dict = dataclasses.asdict(person)
    print(f"     person_dict = {person_dict}")
    
    # 3. astuple函数
    print("\n3. dataclasses.astuple")
    print("   - 将数据类实例转换为元组")
    print("   - 递归转换嵌套的数据类和集合类型")
    
    print("\n   示例：使用astuple函数转换为元组")
    person_tuple = dataclasses.astuple(person)
    print(f"     person_tuple = {person_tuple}")
    
    # 4. make_dataclass函数
    print("\n4. dataclasses.make_dataclass")
    print("   - 动态创建数据类")
    print("   - 可以在运行时根据需要创建类")
    
    print("\n   示例：使用make_dataclass动态创建数据类")
    
    # 动态创建数据类
    Car = dataclasses.make_dataclass(
        'Car',  # 类名
        [       # 字段列表
            ('brand', str),
            ('model', str),
            ('year', int),
            ('price', float, dataclasses.field(default=0.0))
        ],
        namespace={'start_engine': lambda self: f"Starting {self.brand} {self.model}"}  # 添加方法
    )
    
    # 创建实例
    car = Car('Toyota', 'Corolla', 2020, 25000.0)
    print(f"     car = {car}")
    print(f"     调用方法: {car.start_engine()}")
    
    # 5. is_dataclass函数
    print("\n5. dataclasses.is_dataclass")
    print("   - 判断一个对象或类是否是数据类")
    print("   - 对于实例，返回True如果实例的类是数据类")
    print("   - 对于类，返回True如果是数据类")
    
    print("\n   示例：使用is_dataclass函数判断数据类")
    
    print(f"     Person是数据类: {dataclasses.is_dataclass(Person)}")
    print(f"     person实例是数据类实例: {dataclasses.is_dataclass(person)}")
    print(f"     Car是数据类: {dataclasses.is_dataclass(Car)}")
    print(f"     car实例是数据类实例: {dataclasses.is_dataclass(car)}")
    print(f"     list是数据类: {dataclasses.is_dataclass(list)}")
    print(f"     [1, 2, 3]是数据类实例: {dataclasses.is_dataclass([1, 2, 3])}")
    
    # 6. replace函数
    print("\n6. dataclasses.replace")
    print("   - 创建数据类实例的副本，替换指定字段的值")
    print("   - 类似于命名元组的_replace方法")
    print("   - 对于冻结数据类，这是修改字段值的唯一方法")
    
    print("\n   示例：使用replace函数创建修改副本")
    
    # 创建普通数据类的修改副本
    new_person = dataclasses.replace(person, age=31, email="alice.new@example.com")
    print(f"     原始person: {person}")
    print(f"     修改后副本: {new_person}")
    
    # 创建冻结数据类
    @dataclasses.dataclass(frozen=True)
    class FrozenPerson:
        name: str
        age: int
    
    frozen_person = FrozenPerson("Bob", 25)
    
    # 使用replace修改冻结数据类
    new_frozen = dataclasses.replace(frozen_person, age=26)
    print(f"     原始冻结实例: {frozen_person}")
    print(f"     修改后冻结副本: {new_frozen}")
    
    # 7. fields函数的metadata访问
    print("\n7. 访问字段元数据")
    print("   - 通过fields函数获取字段，然后访问metadata属性")
    
    # 定义带元数据的数据类
    @dataclasses.dataclass
    class WithMetadata:
        name: str = dataclasses.field(metadata={"description": "名称"})
        value: int = dataclasses.field(metadata={"description": "数值", "range": "0-100"})
    
    print("\n   示例：访问字段元数据")
    
    for field in dataclasses.fields(WithMetadata):
        print(f"     字段 {field.name} 的元数据: {field.metadata}")

# 导入time模块用于演示
def import_time_if_needed():
    try:
        global time
        import time
    except ImportError:
        pass

# 运行数据类辅助函数演示
import_time_if_needed()
helper_functions()
print()

# 5. 高级特性
print("=== 5. 高级特性 ===")

def advanced_features():
    """演示dataclasses模块的高级特性"""
    print("dataclasses模块支持多种高级特性，如继承、自定义方法等：\n")
    
    # 1. 数据类继承
    print("1. 数据类继承")
    print("   - 数据类可以像普通类一样继承")
    print("   - 子类会继承父类的所有字段")
    print("   - 需要注意初始化顺序和默认值")
    
    print("\n   示例：数据类继承")
    
    @dataclasses.dataclass
    class Base:
        value1: int
        value2: str = "default"
    
    @dataclasses.dataclass
    class Derived(Base):
        value3: float
        value4: bool = False
    
    # 创建子类实例
    derived = Derived(10, "test", 3.14)
    print(f"     derived = {derived}")
    
    # 检查字段顺序
    print("     字段顺序：")
    for field in dataclasses.fields(derived):
        print(f"       {field.name}")
    
    # 2. 自定义特殊方法
    print("\n2. 自定义特殊方法")
    print("   - 可以在数据类中重写自动生成的特殊方法")
    print("   - 自定义方法会覆盖自动生成的方法")
    
    print("\n   示例：自定义特殊方法")
    
    @dataclasses.dataclass
    class CustomMethods:
        value: int
        
        # 自定义__add__方法
        def __add__(self, other):
            if isinstance(other, CustomMethods):
                return CustomMethods(self.value + other.value)
            elif isinstance(other, int):
                return CustomMethods(self.value + other)
            return NotImplemented
        
        # 自定义__repr__方法
        def __repr__(self):
            return f"Custom(value={self.value})"
    
    c1 = CustomMethods(5)
    c2 = CustomMethods(10)
    
    print(f"     c1 = {c1}")  # 使用自定义的__repr__
    print(f"     c1 + c2 = {c1 + c2}")  # 使用自定义的__add__
    print(f"     c1 + 3 = {c1 + 3}")  # 使用自定义的__add__
    
    # 3. Init-only字段（Python 3.8+）
    print("\n3. Init-only字段")
    print("   - 仅在__init__方法中使用的字段，不会成为实例属性")
    print("   - 使用field(init=True, repr=False, compare=False, hash=False)")
    print("   - 在Python 3.8+中，可以使用typing.InitVar类型")
    
    # 尝试使用InitVar
    try:
        from typing import InitVar
        
        @dataclasses.dataclass
        class WithInitVar:
            name: str
            # Init-only字段
            compute_size: InitVar[bool] = False
            size: int = 0
            
            def __post_init__(self, compute_size):
                if compute_size:
                    self.size = len(self.name)
        
        print("\n   示例：使用InitVar")
        
        w1 = WithInitVar("test", compute_size=True)
        w2 = WithInitVar("example", compute_size=False)
        
        print(f"     w1 = {w1}")
        print(f"     w2 = {w2}")
        
        # 验证compute_size不是实例属性
        print(f"     compute_size是实例属性: {'compute_size' in dir(w1)}")
        
    except ImportError:
        print("\n   当前Python版本小于3.8，InitVar不可用")
    
    # 4. __post_init__方法
    print("\n4. __post_init__方法")
    print("   - 初始化后自动调用的方法")
    print("   - 用于执行额外的初始化逻辑")
    print("   - 可以使用InitVar字段的值")
    
    print("\n   示例：使用__post_init__方法")
    
    @dataclasses.dataclass
    class WithPostInit:
        first_name: str
        last_name: str
        full_name: str = dataclasses.field(init=False)  # 不参与初始化
        
        def __post_init__(self):
            # 计算full_name
            self.full_name = f"{self.first_name} {self.last_name}"
    
    person = WithPostInit("John", "Doe")
    print(f"     person = {person}")
    
    # 5. 数据类与属性装饰器结合
    print("\n5. 数据类与属性装饰器结合")
    print("   - 在数据类中可以使用@property装饰器定义属性")
    print("   - 可以实现只读属性、计算属性等")
    
    print("\n   示例：数据类与属性装饰器结合")
    
    @dataclasses.dataclass
    class WithProperties:
        base_price: float
        tax_rate: float = 0.1
        
        @property
        def tax_amount(self):
            """计算税额"""
            return self.base_price * self.tax_rate
        
        @property
        def total_price(self):
            """计算总价"""
            return self.base_price + self.tax_amount
    
    product = WithProperties(100.0)
    print(f"     产品基础价格: {product.base_price}")
    print(f"     税率: {product.tax_rate}")
    print(f"     税额: {product.tax_amount}")
    print(f"     总价: {product.total_price}")
    
    # 6. 嵌套数据类
    print("\n6. 嵌套数据类")
    print("   - 数据类的字段可以是另一个数据类的实例")
    print("   - asdict和astuple函数会递归转换嵌套数据类")
    
    print("\n   示例：嵌套数据类")
    
    @dataclasses.dataclass
    class Address:
        street: str
        city: str
        country: str
    
    @dataclasses.dataclass
    class Contact:
        name: str
        address: Address  # 嵌套数据类字段
        emails: List[str] = dataclasses.field(default_factory=list)
    
    # 创建实例
    address = Address("123 Main St", "Any City", "Any Country")
    contact = Contact("Alice", address, ["alice@example.com", "alice.work@example.com"])
    
    print(f"     contact = {contact}")
    
    # 使用asdict转换
    contact_dict = dataclasses.asdict(contact)
    print(f"     contact_dict = {contact_dict}")
    
    # 7. 协议和抽象基类
    print("\n7. 协议和抽象基类")
    print("   - 数据类可以实现协议或继承抽象基类")
    print("   - 可以结合typing模块的Protocol或abc模块使用")
    
    try:
        from typing import Protocol
        
        # 定义协议
        class Printable(Protocol):
            def print_info(self) -> None:
                ...
        
        @dataclasses.dataclass
        class Document(Printable):
            title: str
            content: str
            
            def print_info(self) -> None:
                print(f"文档: {self.title}, 长度: {len(self.content)}字符")
        
        print("\n   示例：数据类实现协议")
        
        doc = Document("示例文档", "这是文档内容...")
        doc.print_info()
        
    except ImportError:
        print("\n   当前Python版本小于3.8，Protocol不可用")

# 运行高级特性演示
advanced_features()
print()

# 6. 实际应用示例
print("=== 6. 实际应用示例 ===")

def practical_applications():
    """演示dataclasses在实际应用中的使用"""
    print("dataclasses在实际编程中的应用场景：\n")
    
    # 示例1: 配置管理
    print("示例1: 配置管理")
    
    @dataclasses.dataclass
    class DatabaseConfig:
        host: str = "localhost"
        port: int = 5432
        username: str = "admin"
        password: str = dataclasses.field(repr=False)  # 不在repr中显示密码
        database: str = "default_db"
        pool_size: int = 10
        timeout: int = 30
    
    print("   数据库配置类：")
    config = DatabaseConfig(
        host="db.example.com",
        username="app_user",
        password="secret123",
        database="production_db"
    )
    print(f"     {config}")
    
    # 示例2: 数据传输对象(DTO)
    print("\n示例2: 数据传输对象(DTO)")
    
    @dataclasses.dataclass
    class UserDTO:
        id: int
        username: str
        email: str
        first_name: Optional[str] = None
        last_name: Optional[str] = None
        created_at: str = dataclasses.field(init=False)  # 服务器端设置
    
    print("   用户数据传输对象：")
    # 模拟从客户端接收的数据
    user_data = UserDTO(
        id=1,
        username="john_doe",
        email="john@example.com",
        first_name="John",
        last_name="Doe"
    )
    # 服务器端设置创建时间
    user_data.created_at = "2023-01-01T10:00:00Z"
    
    print(f"     {user_data}")
    
    # 转换为字典用于JSON序列化
    user_dict = dataclasses.asdict(user_data)
    print(f"     JSON序列化格式: {user_dict}")
    
    # 示例3: 不可变数据模型
    print("\n示例3: 不可变数据模型")
    
    @dataclasses.dataclass(frozen=True)
    class Point2D:
        x: float
        y: float
        
        def distance_to(self, other: 'Point2D') -> float:
            """计算到另一个点的距离"""
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        
        def __add__(self, other: 'Point2D') -> 'Point2D':
            """点的加法运算"""
            return Point2D(self.x + other.x, self.y + other.y)
    
    print("   不可变的二维点类：")
    p1 = Point2D(1.0, 2.0)
    p2 = Point2D(3.0, 4.0)
    
    print(f"     p1 = {p1}")
    print(f"     p2 = {p2}")
    print(f"     p1到p2的距离: {p1.distance_to(p2):.2f}")
    print(f"     p1 + p2 = {p1 + p2}")
    
    # 用作字典键
    point_dict = {p1: "first point", p2: "second point"}
    print(f"     字典查找: {point_dict[p1]}")
    
    # 示例4: 记录型数据
    print("\n示例4: 记录型数据")
    
    @dataclasses.dataclass
    class LogEntry:
        timestamp: float = dataclasses.field(default_factory=time.time)
        level: str
        message: str
        source: str = "application"
        metadata: Dict[str, Any] = dataclasses.field(default_factory=dict)
    
    print("   日志条目类：")
    
    # 创建日志条目
    error_log = LogEntry(
        level="ERROR",
        message="Database connection failed",
        source="db_service",
        metadata={"connection_id": "12345", "attempts": 3}
    )
    
    info_log = LogEntry(
        level="INFO",
        message="Application started successfully"
    )
    
    print(f"     错误日志: {error_log}")
    print(f"     信息日志: {info_log}")
    
    # 示例5: 配置验证
    print("\n示例5: 配置验证")
    
    @dataclasses.dataclass
    class AppConfig:
        app_name: str
        debug: bool = False
        max_connections: int = 100
        
        def __post_init__(self):
            # 验证配置
            if not self.app_name:
                raise ValueError("应用名称不能为空")
            
            if self.max_connections <= 0:
                raise ValueError("最大连接数必须大于0")
            
            # 日志配置验证结果
            print(f"     配置验证: 应用名称='{self.app_name}', 调试模式={self.debug}, 最大连接数={self.max_connections}")
    
    print("   应用配置类（带验证）：")
    
    try:
        # 有效配置
        valid_config = AppConfig("MyApp", debug=True, max_connections=50)
        print(f"     有效配置: {valid_config}")
        
        # 无效配置
        invalid_config = AppConfig("", max_connections=-1)
    except ValueError as e:
        print(f"     配置验证失败: {e}")
    
    # 示例6: 单元测试数据
    print("\n示例6: 单元测试数据")
    
    @dataclasses.dataclass
    class TestCase:
        name: str
        input_data: Any
        expected_output: Any
        description: str = ""
    
    print("   测试用例类：")
    
    # 定义测试用例
    test_cases = [
        TestCase(
            name="加法测试-正数",
            input_data=(1, 2),
            expected_output=3,
            description="测试两个正数相加"
        ),
        TestCase(
            name="加法测试-零",
            input_data=(5, 0),
            expected_output=5,
            description="测试与零相加"
        ),
        TestCase(
            name="加法测试-负数",
            input_data=(-1, -1),
            expected_output=-2,
            description="测试两个负数相加"
        )
    ]
    
    # 运行测试（模拟）
    print("   运行测试用例：")
    for tc in test_cases:
        # 模拟测试执行
        actual_output = tc.input_data[0] + tc.input_data[1]  # 简单加法
        passed = actual_output == tc.expected_output
        
        print(f"     测试: {tc.name}")
        print(f"       描述: {tc.description}")
        print(f"       输入: {tc.input_data}")
        print(f"       期望输出: {tc.expected_output}")
        print(f"       实际输出: {actual_output}")
        print(f"       结果: {'通过' if passed else '失败'}")

# 运行实际应用示例
practical_applications()
print()

# 7. 性能优化和最佳实践
print("=== 7. 性能优化和最佳实践 ===")

def performance_and_best_practices():
    """dataclasses的性能优化和最佳实践"""
    print("dataclasses模块的性能优化和最佳实践：\n")
    
    # 性能考虑
    print("1. 性能考虑")
    print("   - 数据类比手动编写的等效类稍慢，因为装饰器生成的代码可能不如手写代码优化")
    print("   - 但在大多数应用场景中，性能差异可以忽略不计")
    print("   - 对于性能关键路径，可以考虑手动优化或使用slots参数（Python 3.10+）")
    
    # 最佳实践
    print("\n2. 最佳实践")
    print("   - 使用类型注解提供字段类型信息")
    print("   - 对于可变类型的默认值，始终使用default_factory而不是直接赋值")
    print("   - 使用frozen=True创建不可变数据类，增加代码安全性")
    print("   - 使用__post_init__进行额外的初始化和验证")
    print("   - 使用metadata存储字段的附加信息，如验证规则、文档等")
    print("   - 对于配置类，使用dataclasses.replace创建变体，保持原始配置不变")
    print("   - 对于简单的数据结构，数据类比命名元组更灵活，特别是需要继承或自定义方法时")
    
    # 常见陷阱
    print("\n3. 常见陷阱")
    print("   - 可变默认值问题：使用可变对象作为默认值会导致所有实例共享该对象")
    print("   - 字段顺序问题：带默认值的字段必须放在不带默认值的字段后面")
    print("   - 继承问题：当父类不是数据类时，子类的初始化可能需要特殊处理")
    print("   - 类型提示不是强制的：dataclasses不强制执行类型注解，可以使用mypy等工具进行类型检查")
    print("   - 性能问题：在极端性能场景下，数据类可能不如手动优化的类高效")
    
    # 代码示例：最佳实践演示
    print("\n   示例：数据类最佳实践")
    
    @dataclasses.dataclass(frozen=True)
    class Config:
        """配置类 - 演示最佳实践"""
        # 使用类型注解
        app_name: str
        version: str
        debug: bool = False
        
        # 使用default_factory处理可变类型
        endpoints: List[str] = dataclasses.field(default_factory=list)
        
        # 使用metadata添加文档
        max_retries: int = dataclasses.field(
            default=3,
            metadata={"description": "最大重试次数", "range": "0-10"}
        )
        
        # 使用__post_init__进行验证
        def __post_init__(self):
            # 在冻结类中，需要使用特殊方式设置字段
            if not self.app_name:
                raise ValueError("应用名称不能为空")
            
            if not isinstance(self.version, str) or not self.version:
                raise ValueError("版本必须是非空字符串")
    
    try:
        # 创建有效配置
        config = Config(
            app_name="BestPracticeApp",
            version="1.0.0",
            endpoints=["/api/v1", "/api/v2"]
        )
        print(f"     有效配置: {config}")
        
        # 创建配置变体
        dev_config = dataclasses.replace(config, debug=True, max_retries=5)
        print(f"     开发配置变体: {dev_config}")
        
        # 验证原始配置未被修改
        print(f"     原始配置未变: {config}")
        
    except ValueError as e:
        print(f"     配置错误: {e}")
    
    # 版本兼容性
    print("\n4. 版本兼容性")
    print(f"当前Python版本: {sys.version}")
    print("- dataclasses模块在Python 3.7中引入")
    print("- Python 3.8新增InitVar类型")
    print("- Python 3.9改进了类型注解支持")
    print("- Python 3.10新增slots参数")
    
    # 向后兼容方案
    print("\n5. 向后兼容方案")
    print("   - 对于Python 3.6及以下版本，可以使用第三方库dataclasses")
    print("   - 安装命令: pip install dataclasses")
    print("   - 然后使用条件导入：")
    print("     try:")
    print("         from dataclasses import dataclass")
    print("     except ImportError:")
    print("         from dataclasses import dataclass  # 从第三方库导入")

# 运行性能优化和最佳实践演示
performance_and_best_practices()
print()

# 8. 总结和完整导入指南
print("=== 8. 总结和完整导入指南 ===")

def dataclasses_summary():
    """dataclasses模块的总结和完整导入指南"""
    print("dataclasses模块总结：\n")
    
    # 功能总结
    print("功能总结：")
    print("1. 数据类装饰器：@dataclass - 自动生成特殊方法")
    print("2. 字段定义：支持类型注解、默认值、默认工厂等")
    print("3. 特殊方法：自动生成__init__, __repr__, __eq__等")
    print("4. 辅助函数：fields, asdict, astuple, replace等")
    print("5. 高级特性：继承、嵌套、不可变类、协议实现等")
    print("\n")
    
    # 完整导入指南
    print("完整导入指南：")
    print("""
# 基本导入
from dataclasses import dataclass, field

# 完整导入
from dataclasses import (
    # 装饰器
    dataclass,
    # 字段定义
    field,
    # 辅助函数
    fields,
    asdict,
    astuple,
    make_dataclass,
    is_dataclass,
    replace,
    # 常量
    MISSING,
    # 异常
    FrozenInstanceError
)

# 类型注解导入
from typing import (
    List, Dict, Set, Tuple, Optional, Union, Any, TypeVar, Generic, Protocol,
    # Python 3.8+
    InitVar
)

# 向后兼容的导入方式
try:
    from dataclasses import dataclass
except ImportError:
    from dataclasses import dataclass  # 从第三方库导入

# 获取Python版本信息
import sys
PY38 = sys.version_info >= (3, 8)
PY310 = sys.version_info >= (3, 10)

# 条件使用特性
def create_config_class():
    if PY310:
        # 使用slots参数（Python 3.10+）
        @dataclass(slots=True)
        class Config:
            name: str
            value: str
    else:
        @dataclass
        class Config:
            name: str
            value: str
    return Config
""")

# 运行总结
dataclasses_summary()

print("\n=== 9. 总结 ===")
print("dataclasses模块为Python中的数据类定义提供了强大而简洁的语法。")
print("通过自动生成常用的特殊方法，dataclasses大大减少了模板代码，提高了开发效率。")
print("数据类特别适合需要存储和传递数据的场景，如配置管理、数据传输对象、测试数据等。")
print("掌握dataclasses模块的各种特性和最佳实践，可以帮助你编写更清晰、更安全、更可维护的代码。")
print("记住，虽然dataclasses提供了便利，但也需要注意其局限性和性能考虑。")
print("在适当的场景中使用数据类，可以显著提升代码质量和开发效率。")

# 清理演示过程中创建的大型对象
# 这里主要是为了代码完整性，在实际脚本执行中通常不需要显式清理
if 'large_list' in locals():
    del large_list