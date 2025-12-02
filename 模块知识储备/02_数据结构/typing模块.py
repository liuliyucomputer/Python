# typing模块 - 类型注解和泛型支持
# 功能作用：提供类型注解支持，用于静态类型检查，增强代码可读性和IDE支持
# 使用情景：大型项目开发、库开发、需要静态类型检查的代码、提高代码文档性
# 注意事项：Python 3.5+引入，3.9+有所简化；类型注解不会影响运行时行为；某些特性在不同Python版本中有差异

import sys
import typing
from typing import *  # 演示星号导入，但实际开发中建议显式导入需要的类型

# 模块概述
"""
typing模块是Python 3.5中引入的标准库，提供了用于类型注解的工具。
类型注解允许开发者显式声明变量、函数参数和返回值的类型，提高代码的可读性和可维护性。

虽然Python是动态类型语言，但类型注解可以与静态类型检查工具（如mypy）配合使用，
在开发阶段捕获类型错误，同时也能为IDE提供更好的代码补全和提示功能。

主要功能类别：
1. 基本类型注解
2. 复合类型和容器类型
3. 泛型类型
4. 特殊类型构造器
5. 可调用对象类型
6. 协议和抽象基类
7. 类型别名和变量
"""

# 1. 基本类型注解
print("=== 1. 基本类型注解 ===")

def basic_type_annotations():
    """演示基本的类型注解用法"""
    print("Python中的基本类型注解用于声明变量、参数和返回值的预期类型：\n")
    
    # 1. 变量类型注解
    print("1. 变量类型注解")
    print("   - 使用冒号(:)后跟类型来注解变量")
    print("   - 语法：变量名: 类型")
    print("   - 注意：类型注解不会强制类型检查，只是提供提示")
    
    # 示例：基本变量类型注解
    print("\n   示例：变量类型注解")
    
    # 基本类型
    integer_var: int = 10
    float_var: float = 3.14
    string_var: str = "Hello, Python!"
    boolean_var: bool = True
    none_var: None = None
    
    print(f"     整数: {integer_var!r} (类型: int)")
    print(f"     浮点数: {float_var!r} (类型: float)")
    print(f"     字符串: {string_var!r} (类型: str)")
    print(f"     布尔值: {boolean_var!r} (类型: bool)")
    print(f"     None值: {none_var!r} (类型: None)")
    
    # 2. 函数参数和返回值类型注解
    print("\n2. 函数参数和返回值类型注解")
    print("   - 使用冒号(:)后跟类型来注解参数")
    print("   - 使用->后跟类型来注解返回值")
    print("   - 语法：def 函数名(参数名: 类型, ...) -> 返回类型:")
    
    # 示例：函数类型注解
    print("\n   示例：函数类型注解")
    
    def greet(name: str) -> str:
        """向指定名称的人打招呼"""
        return f"Hello, {name}!"
    
    def add_numbers(a: int, b: int) -> int:
        """计算两个整数的和"""
        return a + b
    
    def calculate_area(radius: float) -> float:
        """计算圆的面积"""
        import math
        return math.pi * radius ** 2
    
    # 调用函数
    print(f"     greet('Alice'): {greet('Alice')}")
    print(f"     add_numbers(5, 3): {add_numbers(5, 3)}")
    print(f"     calculate_area(2.5): {calculate_area(2.5):.2f}")
    
    # 3. 无返回值函数
    print("\n3. 无返回值函数")
    print("   - 使用None或NoReturn注解无返回值函数")
    print("   - None: 函数不返回任何值（隐式返回None）")
    print("   - NoReturn: 函数永远不会正常返回（如抛出异常或无限循环）")
    
    # 示例：无返回值函数
    print("\n   示例：无返回值函数")
    
    def log_message(message: str) -> None:
        """打印日志消息，无返回值"""
        print(f"[LOG] {message}")
    
    try:
        from typing import NoReturn
        
        def raise_error() -> NoReturn:
            """抛出异常，永远不会正常返回"""
            raise ValueError("This function never returns")
        
        print("     NoReturn注解导入成功")
    except ImportError:
        print("     当前Python版本中NoReturn可能不可用")
    
    # 调用无返回值函数
    log_message("This is a test message")
    
    # 4. 类型注解的运行时行为
    print("\n4. 类型注解的运行时行为")
    print("   - 类型注解在运行时不会进行类型检查")
    print("   - 可以通过__annotations__属性访问函数和模块的类型注解")
    
    # 示例：类型注解不会强制类型
    print("\n   示例：类型注解不会强制类型检查")
    
    # 尽管有类型注解，Python仍然允许传入不同类型的值
    result = add_numbers("5", "3")  # 类型不匹配，但Python不会报错
    print(f"     add_numbers('5', '3'): {result}  # 字符串拼接而不是整数相加")
    
    # 访问__annotations__属性
    print(f"     add_numbers的注解: {add_numbers.__annotations__}")
    
    # 5. 注释中的类型提示（Python 3.5之前的替代方案）
    print("\n5. 注释中的类型提示")
    print("   - 在Python 3.5之前，常用注释来表示类型")
    print("   - 现代IDE仍然可以识别这种格式")
    
    # 示例：注释中的类型提示
    print("\n   示例：注释中的类型提示")
    
    def legacy_function(x, y):
        # type: (int, int) -> int
        """使用注释表示类型的函数"""
        return x + y
    
    print(f"     legacy_function(10, 20): {legacy_function(10, 20)}")

# 运行基本类型注解演示
basic_type_annotations()
print()

# 2. 复合类型和容器类型
print("=== 2. 复合类型和容器类型 ===")

def container_types():
    """演示复合类型和容器类型的注解"""
    print("typing模块提供了多种复合类型和容器类型，用于注解列表、字典、集合等复杂数据结构：\n")
    
    # 1. 列表类型
    print("1. 列表类型 (List)")
    print("   - 用于注解列表类型，可以指定列表中元素的类型")
    print("   - 语法：List[元素类型]")
    print("   - Python 3.9+中可以直接使用内置的list[元素类型]")
    
    # 示例：列表类型注解
    print("\n   示例：列表类型注解")
    
    from typing import List
    
    # 整数列表
    numbers: List[int] = [1, 2, 3, 4, 5]
    # 字符串列表
    names: List[str] = ["Alice", "Bob", "Charlie"]
    # 浮点数列表
    scores: List[float] = [85.5, 90.0, 78.5]
    # 列表的列表
    matrix: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    print(f"     整数列表: {numbers}")
    print(f"     字符串列表: {names}")
    print(f"     浮点数列表: {scores}")
    print(f"     嵌套列表: {matrix}")
    
    # 2. 字典类型
    print("\n2. 字典类型 (Dict)")
    print("   - 用于注解字典类型，可以指定键和值的类型")
    print("   - 语法：Dict[键类型, 值类型]")
    print("   - Python 3.9+中可以直接使用内置的dict[键类型, 值类型]")
    
    # 示例：字典类型注解
    print("\n   示例：字典类型注解")
    
    from typing import Dict
    
    # 字符串键，整数值
    user_ages: Dict[str, int] = {"Alice": 30, "Bob": 25, "Charlie": 35}
    # 整数键，字符串值
    id_to_name: Dict[int, str] = {1: "Alice", 2: "Bob", 3: "Charlie"}
    # 嵌套字典
    student_grades: Dict[str, Dict[str, float]] = {
        "Alice": {"Math": 90.5, "English": 85.0},
        "Bob": {"Math": 82.5, "English": 95.0}
    }
    
    print(f"     用户年龄字典: {user_ages}")
    print(f"     ID到名称的映射: {id_to_name}")
    print(f"     学生成绩嵌套字典: {student_grades}")
    
    # 3. 集合类型
    print("\n3. 集合类型 (Set)")
    print("   - 用于注解集合类型，可以指定集合中元素的类型")
    print("   - 语法：Set[元素类型]")
    print("   - Python 3.9+中可以直接使用内置的set[元素类型]")
    
    # 示例：集合类型注解
    print("\n   示例：集合类型注解")
    
    from typing import Set
    
    # 整数集合
    unique_numbers: Set[int] = {1, 2, 3, 4, 5}
    # 字符串集合
    unique_names: Set[str] = {"Alice", "Bob", "Charlie"}
    # 浮点数集合
    unique_scores: Set[float] = {85.5, 90.0, 78.5}
    
    print(f"     整数集合: {unique_numbers}")
    print(f"     字符串集合: {unique_names}")
    print(f"     浮点数集合: {unique_scores}")
    
    # 4. 元组类型
    print("\n4. 元组类型 (Tuple)")
    print("   - 用于注解元组类型，有两种主要形式：")
    print("     * 固定长度和类型的元组: Tuple[类型1, 类型2, ...]")
    print("     * 可变长度但元素类型相同的元组: Tuple[元素类型, ...]")
    print("   - Python 3.9+中可以直接使用内置的tuple[...]语法")
    
    # 示例：元组类型注解
    print("\n   示例：元组类型注解")
    
    from typing import Tuple
    
    # 固定长度和类型的元组（常用于返回多个值）
    point: Tuple[float, float] = (3.5, 4.2)
    person: Tuple[str, int, bool] = ("Alice", 30, True)
    
    # 可变长度但元素类型相同的元组
    coordinates: Tuple[float, ...] = (1.0, 2.0, 3.0)
    numbers_tuple: Tuple[int, ...] = (1, 2, 3, 4, 5)
    
    print(f"     二维点元组: {point}")
    print(f"     人员信息元组: {person}")
    print(f"     可变长度浮点数元组: {coordinates}")
    print(f"     可变长度整数元组: {numbers_tuple}")
    
    # 5. 可迭代类型
    print("\n5. 可迭代类型 (Iterable)")
    print("   - 用于注解任何可迭代的对象")
    print("   - 语法：Iterable[元素类型]")
    
    # 示例：可迭代类型注解
    print("\n   示例：可迭代类型注解")
    
    from typing import Iterable
    
    def process_items(items: Iterable[int]) -> List[int]:
        """处理可迭代对象中的整数，返回平方后的列表"""
        return [x ** 2 for x in items]
    
    # 可以传入列表
    result1 = process_items([1, 2, 3, 4, 5])
    # 可以传入元组
    result2 = process_items((10, 20, 30))
    # 可以传入集合
    result3 = process_items({5, 10, 15})
    
    print(f"     处理列表结果: {result1}")
    print(f"     处理元组结果: {result2}")
    print(f"     处理集合结果: {result3}")
    
    # 6. 序列类型
    print("\n6. 序列类型 (Sequence)")
    print("   - 用于注解有序的可索引序列（如列表、元组、字符串等）")
    print("   - 语法：Sequence[元素类型]")
    
    # 示例：序列类型注解
    print("\n   示例：序列类型注解")
    
    from typing import Sequence
    
    def get_first_element(seq: Sequence[int]) -> int:
        """获取序列的第一个元素"""
        return seq[0]
    
    print(f"     列表的第一个元素: {get_first_element([1, 2, 3])}")
    print(f"     元组的第一个元素: {get_first_element((10, 20, 30))}")
    
    # 7. 映射类型
    print("\n7. 映射类型 (Mapping)")
    print("   - 用于注解映射对象（如字典、defaultdict等）")
    print("   - 语法：Mapping[键类型, 值类型]")
    
    # 示例：映射类型注解
    print("\n   示例：映射类型注解")
    
    from typing import Mapping
    
    def get_value_by_key(mapping: Mapping[str, int], key: str) -> int:
        """根据键从映射中获取值"""
        return mapping.get(key, 0)
    
    print(f"     从字典获取值: {get_value_by_key({'a': 1, 'b': 2, 'c': 3}, 'b')}")

# 运行复合类型和容器类型演示
container_types()
print()

# 3. 泛型类型
print("=== 3. 泛型类型 ===")

def generic_types():
    """演示泛型类型的使用"""
    print("泛型类型允许创建可以适用于多种数据类型的函数、类和数据结构：\n")
    
    # 1. 类型变量 (TypeVar)
    print("1. 类型变量 (TypeVar)")
    print("   - 用于创建通用的类型变量，可用于定义泛型函数和类")
    print("   - 可以限制类型变量的上限类型")
    print("   - 可以指定协变和逆变")
    
    # 示例：类型变量和泛型函数
    print("\n   示例：类型变量和泛型函数")
    
    from typing import TypeVar, List
    
    # 创建无约束的类型变量
    T = TypeVar('T')
    
    # 创建有约束的类型变量
    Numeric = TypeVar('Numeric', int, float)
    
    # 泛型函数示例
    def first_element(items: List[T]) -> T:
        """返回列表的第一个元素，保留元素类型"""
        return items[0] if items else None
    
    # 泛型函数，限制为数值类型
    def add(a: Numeric, b: Numeric) -> Numeric:
        """添加两个数值，返回相同类型的结果"""
        return a + b
    
    # 测试泛型函数
    print(f"     从整数列表获取第一个元素: {first_element([1, 2, 3])}")
    print(f"     从字符串列表获取第一个元素: {first_element(['a', 'b', 'c'])}")
    print(f"     添加整数: {add(5, 3)}")
    print(f"     添加浮点数: {add(5.5, 3.3)}")
    
    # 2. 泛型类
    print("\n2. 泛型类")
    print("   - 使用Generic基类创建泛型类")
    print("   - 可以接受多个类型变量")
    
    # 示例：泛型类
    print("\n   示例：泛型类")
    
    from typing import Generic
    
    # 创建一个简单的泛型容器类
    class Box(Generic[T]):
        def __init__(self, value: T):
            self.value = value
        
        def get_value(self) -> T:
            return self.value
        
        def set_value(self, value: T) -> None:
            self.value = value
    
    # 使用不同类型实例化泛型类
    int_box = Box[int](10)
    string_box = Box[str]("Hello")
    float_box = Box[float](3.14)
    
    print(f"     整数盒子: {int_box.get_value()}")
    print(f"     字符串盒子: {string_box.get_value()}")
    print(f"     浮点数盒子: {float_box.get_value()}")
    
    # 修改盒子中的值
    int_box.set_value(20)
    print(f"     修改后的整数盒子: {int_box.get_value()}")
    
    # 3. 多类型变量泛型
    print("\n3. 多类型变量泛型")
    print("   - 泛型类可以使用多个类型变量")
    print("   - 适用于需要多种类型参数的数据结构")
    
    # 示例：多类型变量泛型
    print("\n   示例：多类型变量泛型")
    
    K = TypeVar('K')
    V = TypeVar('V')
    
    class Pair(Generic[K, V]):
        def __init__(self, key: K, value: V):
            self.key = key
            self.value = value
        
        def get_pair(self) -> Tuple[K, V]:
            return (self.key, self.value)
    
    # 创建不同类型的Pair实例
    int_string_pair = Pair[int, str](1, "one")
    string_float_pair = Pair[str, float]("pi", 3.14)
    
    print(f"     整数-字符串对: {int_string_pair.get_pair()}")
    print(f"     字符串-浮点数对: {string_float_pair.get_pair()}")
    
    # 4. 泛型容器类型
    print("\n4. 泛型容器类型")
    print("   - typing模块提供了常用的泛型容器类型")
    print("   - 如Dict, List, Set, Tuple等都是泛型类型")
    
    # 示例：泛型容器类型
    print("\n   示例：泛型容器类型的实际应用")
    
    def filter_list(items: List[T], predicate) -> List[T]:
        """使用谓词函数过滤列表"""
        return [item for item in items if predicate(item)]
    
    def map_list(items: List[T], transform) -> List:
        """使用转换函数映射列表"""
        return [transform(item) for item in items]
    
    # 过滤和映射整数列表
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = filter_list(numbers, lambda x: x % 2 == 0)
    squared_numbers = map_list(numbers, lambda x: x ** 2)
    
    print(f"     原始列表: {numbers}")
    print(f"     偶数列表: {even_numbers}")
    print(f"     平方列表: {squared_numbers}")
    
    # 5. 协变和逆变
    print("\n5. 协变和逆变")
    print("   - 控制泛型类型的继承关系")
    print("   - 协变(Covariant): 使用+TypeVar")
    print("   - 逆变(Contravariant): 使用-TypeVar")
    print("   - 不变(Invariant): 默认行为")
    
    # 示例：协变和逆变
    print("\n   示例：协变和逆变")
    
    try:
        # 协变示例
        T_co = TypeVar('T_co', covariant=True)
        
        class Producer(Generic[T_co]):
            def produce(self) -> T_co:
                # 实现省略
                pass
        
        # 逆变示例
        T_contra = TypeVar('T_contra', contravariant=True)
        
        class Consumer(Generic[T_contra]):
            def consume(self, value: T_contra) -> None:
                # 实现省略
                pass
        
        print("     协变和逆变类型变量定义成功")
    except TypeError as e:
        print(f"     协变/逆变定义错误: {e}")

# 运行泛型类型演示
generic_types()
print()

# 4. 特殊类型构造器
print("=== 4. 特殊类型构造器 ===")

def special_type_constructors():
    """演示特殊类型构造器"""
    print("typing模块提供了多种特殊类型构造器，用于处理复杂的类型注解场景：\n")
    
    # 1. Optional类型
    print("1. Optional类型")
    print("   - 用于注解可能为None的值")
    print("   - 等价于Union[Type, None]")
    print("   - 语法：Optional[类型]")
    
    # 示例：Optional类型
    print("\n   示例：Optional类型")
    
    from typing import Optional
    
    def find_user(user_id: int) -> Optional[str]:
        """根据ID查找用户，如果找到返回用户名，否则返回None"""
        users = {1: "Alice", 2: "Bob", 3: "Charlie"}
        return users.get(user_id)
    
    print(f"     查找用户ID=2: {find_user(2)}")
    print(f"     查找用户ID=999: {find_user(999)}")
    
    # 2. Union类型
    print("\n2. Union类型")
    print("   - 用于注解可能是多种类型之一的值")
    print("   - 语法：Union[类型1, 类型2, ...]")
    print("   - Python 3.10+中可以使用|操作符：类型1 | 类型2 | ...")
    
    # 示例：Union类型
    print("\n   示例：Union类型")
    
    from typing import Union
    
    def process_value(value: Union[int, float, str]) -> int:
        """处理可能是整数、浮点数或字符串的值"""
        if isinstance(value, (int, float)):
            return int(value)
        elif isinstance(value, str):
            return int(float(value))  # 尝试将字符串转换为数字
        raise TypeError("Unsupported type")
    
    print(f"     处理整数: {process_value(42)}")
    print(f"     处理浮点数: {process_value(3.14)}")
    print(f"     处理字符串: {process_value('100')}")
    
    # 3. Any类型
    print("\n3. Any类型")
    print("   - 表示任何类型的值")
    print("   - 使用Any会禁用类型检查")
    print("   - 谨慎使用，尽量使用更具体的类型")
    
    # 示例：Any类型
    print("\n   示例：Any类型")
    
    from typing import Any
    
    def process_any(value: Any) -> Any:
        """处理任何类型的值"""
        print(f"     处理值: {value}, 类型: {type(value).__name__}")
        return value
    
    process_any(42)
    process_any("Hello")
    process_any([1, 2, 3])
    process_any({"key": "value"})
    
    # 4. NoReturn类型
    print("\n4. NoReturn类型")
    print("   - 用于注解永远不会正常返回的函数")
    print("   - 如抛出异常或进入无限循环的函数")
    
    # 示例：NoReturn类型
    print("\n   示例：NoReturn类型")
    
    try:
        from typing import NoReturn
        
        def exit_program() -> NoReturn:
            """退出程序，永远不会返回"""
            print("     程序即将退出...")
            # 注意：在实际演示中不执行退出
            # exit(0)
            raise SystemExit("模拟退出")
        
        def infinite_loop() -> NoReturn:
            """无限循环，永远不会返回"""
            print("     进入无限循环...")
            # 注意：在实际演示中不执行无限循环
            # while True:
            #     pass
            raise RuntimeError("模拟无限循环")
        
        # 尝试调用
        try:
            exit_program()
        except SystemExit:
            print("     捕获到SystemExit异常")
        
    except ImportError:
        print("     当前Python版本中NoReturn可能不可用")
    except Exception as e:
        print(f"     捕获到异常: {e}")
    
    # 5. Callable类型
    print("\n5. Callable类型")
    print("   - 用于注解可调用对象（如函数、方法）")
    print("   - 语法：Callable[[参数类型1, 参数类型2, ...], 返回类型]")
    print("   - 对于可变参数，使用Ellipsis: Callable[..., 返回类型]")
    
    # 示例：Callable类型
    print("\n   示例：Callable类型")
    
    from typing import Callable
    
    def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:
        """应用函数到两个整数"""
        return func(a, b)
    
    def add(a: int, b: int) -> int:
        return a + b
    
    def multiply(a: int, b: int) -> int:
        return a * b
    
    print(f"     加法应用: {apply_function(add, 5, 3)}")
    print(f"     乘法应用: {apply_function(multiply, 5, 3)}")
    
    # 使用lambda表达式
    print(f"     Lambda应用: {apply_function(lambda x, y: x - y, 10, 4)}")
    
    # 6. Literal类型（Python 3.8+）
    print("\n6. Literal类型")
    print("   - 用于注解只能是特定字面量值的类型")
    print("   - Python 3.8中引入")
    print("   - 语法：Literal[值1, 值2, ...]")
    
    # 示例：Literal类型
    print("\n   示例：Literal类型")
    
    try:
        from typing import Literal
        
        def set_mode(mode: Literal["read", "write", "append"]) -> None:
            """设置文件模式"""
            print(f"     设置文件模式为: {mode}")
        
        # 有效调用
        set_mode("read")
        set_mode("write")
        
        # 以下调用在静态类型检查时会报错，但Python运行时允许
        # set_mode("invalid")  # 静态类型检查会报错
        
        # 用于枚举-like行为
        def get_color(code: Literal["R", "G", "B"]) -> str:
            colors = {"R": "Red", "G": "Green", "B": "Blue"}
            return colors[code]
        
        print(f"     颜色代码'R'对应: {get_color('R')}")
        print(f"     颜色代码'G'对应: {get_color('G')}")
        
    except ImportError:
        print("     当前Python版本小于3.8，Literal类型不可用")
    
    # 7. Final类型和Final变量（Python 3.8+）
    print("\n7. Final类型和Final变量")
    print("   - 用于注解不可变的变量或不可被继承的类")
    print("   - Python 3.8中引入")
    print("   - 注意：Final只是一个提示，Python运行时不会强制不可变性")
    
    # 示例：Final类型
    print("\n   示例：Final类型")
    
    try:
        from typing import Final
        
        # Final变量
        PI: Final = 3.14159
        print(f"     Final常量PI: {PI}")
        
        # 在静态类型检查时，以下行应该报错，但Python运行时允许修改
        # PI = 3.14  # 静态类型检查会报错
        
        # Final类
        class Base:
            pass
        
        class Derived(Base):  # 这是允许的
            pass
        
        # 以下在Python 3.11+中可用
        # @final
        # class FinalClass:
        #     pass
        
        # class DerivedFromFinal(FinalClass):  # 静态类型检查会报错
        #     pass
        
    except ImportError:
        print("     当前Python版本小于3.8，Final类型不可用")

# 运行特殊类型构造器演示
special_type_constructors()
print()

# 5. 可调用对象类型
print("=== 5. 可调用对象类型 ===")

def callable_types():
    """演示可调用对象的类型注解"""
    print("可调用对象（如函数、方法、类等）可以使用Callable类型进行注解：\n")
    
    # 1. 基本的Callable注解
    print("1. 基本的Callable注解")
    print("   - 用于注解接受特定参数并返回特定类型的可调用对象")
    print("   - 语法：Callable[[参数类型1, 参数类型2, ...], 返回类型]")
    
    # 示例：基本的Callable注解
    print("\n   示例：基本的Callable注解")
    
    from typing import Callable
    
    def execute_operation(
        operation: Callable[[int, int], int],
        a: int,
        b: int
    ) -> int:
        """执行操作并返回结果"""
        return operation(a, b)
    
    # 定义一些操作函数
    def addition(x: int, y: int) -> int:
        return x + y
    
    def subtraction(x: int, y: int) -> int:
        return x - y
    
    def multiplication(x: int, y: int) -> int:
        return x * y
    
    # 执行操作
    print(f"     5 + 3 = {execute_operation(addition, 5, 3)}")
    print(f"     5 - 3 = {execute_operation(subtraction, 5, 3)}")
    print(f"     5 * 3 = {execute_operation(multiplication, 5, 3)}")
    print(f"     5 / 3 = {execute_operation(lambda x, y: x // y, 5, 3)}")
    
    # 2. 可变参数的Callable注解
    print("\n2. 可变参数的Callable注解")
    print("   - 用于注解接受可变数量参数的可调用对象")
    print("   - 使用...表示任意参数")
    print("   - 语法：Callable[..., 返回类型]")
    
    # 示例：可变参数的Callable注解
    print("\n   示例：可变参数的Callable注解")
    
    def execute_any(operation: Callable[..., Any], *args, **kwargs) -> Any:
        """执行任意操作并返回结果"""
        return operation(*args, **kwargs)
    
    # 测试不同的可调用对象
    print(f"     字符串格式化: {execute_any('Hello, {}!'.format, 'Python')}")
    print(f"     列表排序: {execute_any(sorted, [3, 1, 4, 2])}")
    print(f"     数学运算: {execute_any(lambda x, y, z: x + y * z, 1, 2, 3)}")
    
    # 3. 带默认参数的Callable注解
    print("\n3. 带默认参数的Callable注解")
    print("   - 类型注解不直接支持默认参数的表示")
    print("   - 可以使用文档字符串或注释说明")
    
    # 示例：带默认参数的Callable注解
    print("\n   示例：带默认参数的Callable注解")
    
    def process_with_defaults(
        processor: Callable[[List[int], Optional[int]], List[int]],
        items: List[int]
    ) -> List[int]:
        """使用带默认参数的处理器处理列表"""
        return processor(items)
    
    def filter_above_threshold(items: List[int], threshold: int = 0) -> List[int]:
        """过滤出大于阈值的元素，默认为0"""
        return [item for item in items if item > threshold]
    
    # 处理数据
    numbers = [-5, -2, 0, 3, 7, 10]
    print(f"     原始列表: {numbers}")
    print(f"     默认过滤: {process_with_defaults(filter_above_threshold, numbers)}")
    print(f"     阈值5过滤: {process_with_defaults(lambda items: filter_above_threshold(items, 5), numbers)}")
    
    # 4. 函数装饰器的类型注解
    print("\n4. 函数装饰器的类型注解")
    print("   - 装饰器本身可以使用Callable类型进行注解")
    print("   - 保留原始函数的签名")
    
    # 示例：函数装饰器的类型注解
    print("\n   示例：函数装饰器的类型注解")
    
    from typing import cast
    
    def log_execution(
        func: Callable[..., R]
    ) -> Callable[..., R]:
        """记录函数执行的装饰器"""
        def wrapper(*args: Any, **kwargs: Any) -> R:
            print(f"     执行函数: {func.__name__}")
            print(f"       参数: args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"       结果: {result}")
            return result
        return cast(Callable[..., R], wrapper)
    
    # 测试装饰器
    @log_execution
    def add_numbers(a: int, b: int) -> int:
        """添加两个数字"""
        return a + b
    
    result = add_numbers(10, 20)
    print(f"     最终结果: {result}")

# 运行可调用对象类型演示
callable_types()
print()

# 6. 协议和抽象基类
print("=== 6. 协议和抽象基类 ===")

def protocols_and_abc():
    """演示协议和抽象基类"""
    print("typing模块提供了协议和抽象基类，用于定义接口和进行鸭子类型检查：\n")
    
    # 1. 协议 (Protocol)
    print("1. 协议 (Protocol)")
    print("   - 用于定义隐式接口")
    print("   - 基于鸭子类型：只要实现了协议中定义的方法，就被视为符合协议")
    print("   - Python 3.8中引入，在之前版本可以使用typing_extensions库")
    
    # 示例：协议定义和使用
    print("\n   示例：协议定义和使用")
    
    try:
        from typing import Protocol
        
        # 定义一个协议
        class Printable(Protocol):
            def print_info(self) -> None:
                """打印对象信息"""
                ...
        
        # 实现协议的类
        class Person:
            def __init__(self, name: str, age: int):
                self.name = name
                self.age = age
            
            def print_info(self) -> None:
                print(f"     人员信息: 姓名={self.name}, 年龄={self.age}")
        
        class Product:
            def __init__(self, name: str, price: float):
                self.name = name
                self.price = price
            
            def print_info(self) -> None:
                print(f"     产品信息: 名称={self.name}, 价格={self.price}")
        
        # 函数接受任何实现了Printable协议的对象
        def print_details(obj: Printable) -> None:
            obj.print_info()
        
        # 测试
        person = Person("Alice", 30)
        product = Product("Laptop", 999.99)
        
        print("     使用协议接受不同类型的对象:")
        print_details(person)
        print_details(product)
        
        # 验证是否符合协议
        print(f"     Person类是否符合Printable协议: {isinstance(person, Printable)}")
        print(f"     Product类是否符合Printable协议: {isinstance(product, Printable)}")
        
    except ImportError:
        print("     当前Python版本小于3.8，Protocol不可用")
    except TypeError as e:
        print(f"     协议相关错误: {e}")
    
    # 2. 抽象基类 (ABC)
    print("\n2. 抽象基类 (ABC)")
    print("   - 用于定义显式接口")
    print("   - 使用@abstractmethod装饰器标记必须实现的方法")
    print("   - 不能直接实例化抽象基类")
    print("   - 继承抽象基类的子类必须实现所有抽象方法")
    
    # 示例：抽象基类定义和使用
    print("\n   示例：抽象基类定义和使用")
    
    from abc import ABC, abstractmethod
    
    class Shape(ABC):
        @abstractmethod
        def area(self) -> float:
            """计算形状的面积"""
            pass
        
        @abstractmethod
        def perimeter(self) -> float:
            """计算形状的周长"""
            pass
    
    # 实现抽象基类
    class Rectangle(Shape):
        def __init__(self, width: float, height: float):
            self.width = width
            self.height = height
        
        def area(self) -> float:
            return self.width * self.height
        
        def perimeter(self) -> float:
            return 2 * (self.width + self.height)
    
    class Circle(Shape):
        def __init__(self, radius: float):
            self.radius = radius
        
        def area(self) -> float:
            import math
            return math.pi * self.radius ** 2
        
        def perimeter(self) -> float:
            import math
            return 2 * math.pi * self.radius
    
    # 测试
    rectangle = Rectangle(5, 3)
    circle = Circle(4)
    
    print("     矩形:")
    print(f"       面积: {rectangle.area():.2f}")
    print(f"       周长: {rectangle.perimeter():.2f}")
    
    print("     圆形:")
    print(f"       面积: {circle.area():.2f}")
    print(f"       周长: {circle.perimeter():.2f}")
    
    # 验证是否是实例
    print(f"     rectangle是否是Shape实例: {isinstance(rectangle, Shape)}")
    print(f"     circle是否是Shape实例: {isinstance(circle, Shape)}")
    
    # 尝试直接实例化抽象基类会引发错误
    try:
        shape = Shape()
    except TypeError as e:
        print(f"     尝试实例化抽象基类: {e}")
    
    # 3. 抽象基类和泛型结合
    print("\n3. 抽象基类和泛型结合")
    print("   - 可以创建泛型抽象基类")
    print("   - 结合了抽象基类的接口强制和泛型的类型灵活性")
    
    # 示例：泛型抽象基类
    print("\n   示例：泛型抽象基类")
    
    T = TypeVar('T')
    
    class Storage(ABC, Generic[T]):
        @abstractmethod
        def add(self, item: T) -> None:
            """添加项目到存储"""
            pass
        
        @abstractmethod
        def get(self) -> T:
            """从存储中获取项目"""
            pass
        
        @abstractmethod
        def is_empty(self) -> bool:
            """检查存储是否为空"""
            pass
    
    # 实现泛型抽象基类
    class Stack(Storage[T]):
        def __init__(self):
            self._items: List[T] = []
        
        def add(self, item: T) -> None:
            self._items.append(item)
        
        def get(self) -> T:
            if self.is_empty():
                raise IndexError("Stack is empty")
            return self._items.pop()
        
        def is_empty(self) -> bool:
            return len(self._items) == 0
    
    # 测试整数栈
    int_stack = Stack[int]()
    int_stack.add(1)
    int_stack.add(2)
    int_stack.add(3)
    
    print("     整数栈:")
    while not int_stack.is_empty():
        print(f"       弹出: {int_stack.get()}")
    
    # 测试字符串栈
    str_stack = Stack[str]()
    str_stack.add("a")
    str_stack.add("b")
    str_stack.add("c")
    
    print("     字符串栈:")
    while not str_stack.is_empty():
        print(f"       弹出: {str_stack.get()}")

# 运行协议和抽象基类演示
protocols_and_abc()
print()

# 7. 类型别名和变量
print("=== 7. 类型别名和变量 ===")

def type_aliases_and_variables():
    """演示类型别名和类型变量"""
    print("类型别名和类型变量可以简化复杂的类型注解，提高代码可读性：\n")
    
    # 1. 类型别名
    print("1. 类型别名")
    print("   - 为复杂类型创建别名，简化注解")
    print("   - 使用赋值语句定义：类型别名 = 类型")
    
    # 示例：类型别名
    print("\n   示例：类型别名")
    
    # 简单类型别名
    UserID = int
    Username = str
    
    # 复合类型别名
    Coordinate = Tuple[float, float]
    Point3D = Tuple[float, float, float]
    
    # 嵌套类型别名
    UserData = Dict[str, Any]
    Matrix = List[List[float]]
    
    # 使用类型别名
    def get_user_by_id(user_id: UserID) -> Optional[UserData]:
        """根据用户ID获取用户数据"""
        users = {
            1: {"name": "Alice", "age": 30},
            2: {"name": "Bob", "age": 25}
        }
        return users.get(user_id)
    
    def calculate_distance(p1: Coordinate, p2: Coordinate) -> float:
        """计算两个坐标点之间的距离"""
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
    
    # 测试
    user = get_user_by_id(1)
    distance = calculate_distance((1.0, 2.0), (4.0, 6.0))
    
    print(f"     用户数据: {user}")
    print(f"     两点距离: {distance:.2f}")
    
    # 2. NewType
    print("\n2. NewType")
    print("   - 创建类型的子类型，用于静态类型检查")
    print("   - 运行时实际上仍然是原始类型，但静态类型检查器会视为不同类型")
    print("   - 语法：新类型名 = NewType('新类型名', 基础类型)")
    
    # 示例：NewType
    print("\n   示例：NewType")
    
    try:
        from typing import NewType
        
        # 创建新类型
        UserID = NewType('UserID', int)
        Email = NewType('Email', str)
        Temperature = NewType('Temperature', float)
        
        # 创建新类型的值
        user_id = UserID(123)
        email = Email("user@example.com")
        temp_celsius = Temperature(25.5)
        
        # 函数注解
        def send_email(user_id: UserID, email: Email) -> None:
            print(f"     发送邮件到用户ID {user_id}，邮箱 {email}")
        
        def convert_to_fahrenheit(celsius: Temperature) -> float:
            return (celsius * 9/5) + 32
        
        # 测试
        send_email(user_id, email)
        fahrenheit = convert_to_fahrenheit(temp_celsius)
        print(f"     {temp_celsius}°C = {fahrenheit:.1f}°F")
        
        # 运行时行为
        print(f"     UserID运行时类型: {type(user_id).__name__}")
        print(f"     Email运行时类型: {type(email).__name__}")
        print(f"     Temperature运行时类型: {type(temp_celsius).__name__}")
        
        # 类型转换
        print(f"     UserID(123) == 123: {UserID(123) == 123}")
        
    except ImportError:
        print("     当前Python版本可能不支持NewType")
    
    # 3. 类型变量的约束
    print("\n3. 类型变量的约束")
    print("   - 可以限制类型变量只能是特定类型或其子类")
    print("   - 使用bound参数指定上界类型")
    
    # 示例：带约束的类型变量
    print("\n   示例：带约束的类型变量")
    
    # 创建带约束的类型变量
    Numeric = TypeVar('Numeric', bound=Union[int, float])
    
    def get_average(numbers: List[Numeric]) -> Numeric:
        """计算平均值，保留原始数值类型"""
        if not numbers:
            return 0  # 可能需要根据情况调整
        return sum(numbers) / len(numbers)
    
    # 测试整数列表
    int_average = get_average([1, 2, 3, 4, 5])
    print(f"     整数列表平均值: {int_average}, 类型: {type(int_average).__name__}")
    
    # 测试浮点数列表
    float_average = get_average([1.5, 2.5, 3.5])
    print(f"     浮点数列表平均值: {float_average}, 类型: {type(float_average).__name__}")
    
    # 4. 类型变量的协变和逆变
    print("\n4. 类型变量的协变和逆变")
    print("   - 控制泛型类型之间的继承关系")
    print("   - 协变(+)：如果A是B的子类，那么Generic[A]是Generic[B]的子类")
    print("   - 逆变(-)：如果A是B的子类，那么Generic[B]是Generic[A]的子类")
    
    # 示例：协变和逆变
    print("\n   示例：协变和逆变的简化演示")
    
    try:
        # 协变类型变量
        T_co = TypeVar('T_co', covariant=True)
        
        class Producer(Generic[T_co]):
            def produce(self) -> T_co:
                # 实际实现中会返回T_co类型的值
                return None
        
        # 逆变类型变量
        T_contra = TypeVar('T_contra', contravariant=True)
        
        class Consumer(Generic[T_contra]):
            def consume(self, value: T_contra) -> None:
                # 实际实现中会消费T_contra类型的值
                pass
        
        # 在静态类型检查的世界中，以下关系成立：
        # - 如果Cat是Animal的子类
        # - 那么Producer[Cat]是Producer[Animal]的子类型（协变）
        # - Consumer[Animal]是Consumer[Cat]的子类型（逆变）
        
        print("     协变和逆变类型变量定义成功")
        print("     注意：协变和逆变主要影响静态类型检查，运行时没有效果")
        
    except Exception as e:
        print(f"     协变/逆变示例错误: {e}")

# 运行类型别名和变量演示
type_aliases_and_variables()
print()

# 8. 实际应用示例
print("=== 8. 实际应用示例 ===")

def practical_applications():
    """演示typing模块在实际应用中的使用"""
    print("typing模块在实际编程中的应用场景：\n")
    
    # 示例1: REST API 响应处理
    print("示例1: REST API 响应处理")
    
    # 定义响应类型
    class APIResponse(Generic[T]):
        def __init__(self, data: T, success: bool, message: Optional[str] = None):
            self.data = data
            self.success = success
            self.message = message
        
        def __repr__(self) -> str:
            return f"APIResponse(success={self.success}, data={self.data!r}, message={self.message!r})"
    
    # 定义用户数据类型
    UserData = Dict[str, Union[str, int, bool]]
    UserList = List[UserData]
    
    # 模拟API函数
    def get_users() -> APIResponse[UserList]:
        """获取用户列表API"""
        # 模拟API调用
        users = [
            {"id": 1, "name": "Alice", "active": True},
            {"id": 2, "name": "Bob", "active": False}
        ]
        return APIResponse(data=users, success=True)
    
    def get_user(user_id: int) -> APIResponse[Optional[UserData]]:
        """获取单个用户API"""
        # 模拟API调用
        users = {1: {"id": 1, "name": "Alice", "active": True}}
        user = users.get(user_id)
        if user:
            return APIResponse(data=user, success=True)
        else:
            return APIResponse(data=None, success=False, message=f"User {user_id} not found")
    
    # 测试API响应
    users_response = get_users()
    print(f"     用户列表响应: {users_response}")
    
    user1_response = get_user(1)
    print(f"     用户ID=1响应: {user1_response}")
    
    user2_response = get_user(999)
    print(f"     用户ID=999响应: {user2_response}")
    
    # 示例2: 数据验证器
    print("\n示例2: 数据验证器")
    
    # 定义验证器类型
    Validator = Callable[[Any], bool]
    ValidationResult = Tuple[bool, Optional[str]]
    
    # 创建验证器函数
    def create_length_validator(min_length: int, max_length: int) -> Validator:
        """创建长度验证器"""
        def validate(value: str) -> bool:
            return min_length <= len(value) <= max_length
        return validate
    
    def create_range_validator(min_val: Numeric, max_val: Numeric) -> Validator:
        """创建范围验证器"""
        def validate(value: Numeric) -> bool:
            return min_val <= value <= max_val
        return validate
    
    # 验证函数
    def validate_data(
        value: Any,
        validators: List[Validator],
        error_messages: List[str]
    ) -> ValidationResult:
        """使用多个验证器验证数据"""
        for i, validator in enumerate(validators):
            if not validator(value):
                return False, error_messages[i]
        return True, None
    
    # 测试验证器
    username = "john_doe"
    age = 20
    
    # 验证用户名
    username_validators = [
        lambda x: isinstance(x, str),
        create_length_validator(3, 20),
        lambda x: all(c.isalnum() or c == '_' for c in x)
    ]
    
    username_errors = [
        "用户名必须是字符串",
        "用户名长度必须在3-20个字符之间",
        "用户名只能包含字母、数字和下划线"
    ]
    
    # 验证年龄
    age_validators = [
        lambda x: isinstance(x, int),
        create_range_validator(18, 120)
    ]
    
    age_errors = [
        "年龄必须是整数",
        "年龄必须在18-120之间"
    ]
    
    # 执行验证
    username_valid, username_error = validate_data(username, username_validators, username_errors)
    age_valid, age_error = validate_data(age, age_validators, age_errors)
    
    print("     数据验证结果:")
    print(f"       用户名验证: {'通过' if username_valid else '失败'}")
    if not username_valid:
        print(f"         错误: {username_error}")
    
    print(f"       年龄验证: {'通过' if age_valid else '失败'}")
    if not age_valid:
        print(f"         错误: {age_error}")
    
    # 示例3: 通用数据转换
    print("\n示例3: 通用数据转换")
    
    # 定义转换函数类型
    Converter = Callable[[T], U]
    
    # 通用转换函数
    def convert_items(items: List[T], converter: Converter[T, U]) -> List[U]:
        """将转换函数应用到列表中的每个项目"""
        return [converter(item) for item in items]
    
    # 示例转换
    # 整数转字符串
    numbers = [1, 2, 3, 4, 5]
    str_numbers = convert_items(numbers, str)
    print(f"     整数转字符串: {str_numbers}")
    
    # 字符串转整数
    str_values = ["10", "20", "30"]
    int_values = convert_items(str_values, int)
    print(f"     字符串转整数: {int_values}")
    
    # 字符串转大写
    words = ["hello", "world", "python"]
    upper_words = convert_items(words, str.upper)
    print(f"     字符串转大写: {upper_words}")
    
    # 复杂转换：提取字典中的字段
    users = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 25}
    ]
    names = convert_items(users, lambda user: user["name"])
    print(f"     提取用户名: {names}")
    
    # 示例4: 缓存装饰器
    print("\n示例4: 通用缓存装饰器")
    
    # 通用LRU缓存装饰器
    def lru_cache(maxsize: Optional[int] = None):
        def decorator(func: Callable[..., R]) -> Callable[..., R]:
            cache = {}
            
            def wrapper(*args: Any, **kwargs: Any) -> R:
                # 构建缓存键
                key = (args, tuple(sorted(kwargs.items())))
                
                # 检查缓存
                if key not in cache:
                    # 如果缓存已满，删除最早的项（简单实现）
                    if maxsize is not None and len(cache) >= maxsize:
                        cache.pop(next(iter(cache)))
                    # 计算结果并缓存
                    cache[key] = func(*args, **kwargs)
                    print(f"     缓存未命中: {func.__name__}{args}, kwargs={kwargs}")
                else:
                    print(f"     缓存命中: {func.__name__}{args}, kwargs={kwargs}")
                
                return cache[key]
            
            return cast(Callable[..., R], wrapper)
        
        return decorator
    
    # 测试缓存装饰器
    @lru_cache(maxsize=3)
    def compute_expensive(x: int, y: int) -> int:
        """模拟昂贵的计算"""
        print(f"     执行昂贵计算: {x} * {y}")
        return x * y
    
    # 测试缓存行为
    print("     测试缓存装饰器:")
    print(f"     结果1: {compute_expensive(10, 20)}")
    print(f"     结果2: {compute_expensive(10, 20)}  # 应该从缓存返回")
    print(f"     结果3: {compute_expensive(20, 30)}")
    print(f"     结果4: {compute_expensive(30, 40)}")
    print(f"     结果5: {compute_expensive(40, 50)}  # 此时应该替换最早的缓存项")
    print(f"     结果6: {compute_expensive(10, 20)}  # 可能需要重新计算")

# 运行实际应用示例
practical_applications()
print()

# 9. 版本兼容性和最佳实践
print("=== 9. 版本兼容性和最佳实践 ===")

def version_compatibility_and_best_practices():
    """typing模块的版本兼容性和最佳实践"""
    print("typing模块在不同Python版本中的变化和使用最佳实践：\n")
    
    # Python版本检查
    print(f"当前Python版本: {sys.version}")
    
    # 版本兼容性
    print("\n版本兼容性：")
    print("- Python 3.5: 引入typing模块，包含基本的类型注解功能")
    print("- Python 3.6: 增加了变量注解语法")
    print("- Python 3.7: 优化性能，添加__future__.annotations")
    print("- Python 3.8: 引入Literal, Final, Protocol等新类型")
    print("- Python 3.9: 支持内置泛型类型(list[int], dict[str, int]等)")
    print("- Python 3.10: 支持联合类型运算符(int | str)和更严格的类型检查")
    
    # 向后兼容方案
    print("\n向后兼容方案：")
    print("1. 使用__future__.annotations")
    print("   - 延迟评估类型注解，允许在类型注解中使用尚未定义的类型")
    print("   - 在Python 3.7+中可用")
    
    print("\n   示例：使用__future__.annotations")
    print("""
   from __future__ import annotations
   
   def func(x: List[int]) -> List[int]:
       # 这里可以使用List而不需要在模块顶部导入
       from typing import List
       return x
   """)
    
    print("\n2. 使用条件导入")
    print("   - 为不同Python版本提供不同的导入方案")
    
    print("\n   示例：条件导入")
    print("""
   # 类型导入
   try:
       from typing import Literal, Final, Protocol
   except ImportError:
       # Python 3.8以下版本的兼容处理
       from typing_extensions import Literal, Final, Protocol
   """)
    
    print("\n3. 使用typing_extensions库")
    print("   - 为旧版本Python提供最新的typing功能")
    print("   - 安装: pip install typing_extensions")
    
    print("\n最佳实践：")
    print("1. 显式导入所需类型")
    print("   - 避免使用from typing import *")
    print("   - 只导入实际使用的类型")
    
    print("\n   推荐写法：")
    print("""
   from typing import List, Dict, Optional, Union
   """)
    
    print("\n2. 使用合适的类型粒度")
    print("   - 不要过度使用Any，尽量使用具体类型")
    print("   - 复杂数据结构使用TypedDict或数据类")
    
    print("\n3. 使用类型别名简化复杂注解")
    print("   - 为常用的复杂类型创建有意义的别名")
    
    print("\n4. 考虑性能影响")
    print("   - 使用__future__.annotations延迟类型评估")
    print("   - Python 3.9+中使用内置泛型类型(list[int]代替List[int])")
    
    print("\n5. 配合静态类型检查工具")
    print("   - 使用mypy等工具验证类型注解")
    print("   - 在CI/CD流程中添加类型检查")
    
    print("\n6. 文档字符串与类型注解结合")
    print("   - 类型注解声明参数和返回值类型")
    print("   - 文档字符串解释参数用途和返回值含义")
    
    print("\n7. 避免循环导入")
    print("   - 使用字符串字面量类型注解或__future__.annotations避免循环引用")
    
    print("\n   示例：避免循环导入")
    print("""
   from __future__ import annotations
   
   # 在ModuleA中
   def process_user(user: 'User') -> None:  # 使用字符串字面量
       pass
   
   # 之后可以导入
   from module_b import User
   """)

# 运行版本兼容性和最佳实践
version_compatibility_and_best_practices()
print()

# 10. 总结
print("=== 10. 总结 ===")

def summarize_typing():
    """总结typing模块的关键点"""
    print("typing模块是Python标准库中的重要组件，为Python代码提供了类型注解支持：\n")
    
    print("核心优势：")
    print("1. 提高代码可读性 - 明确变量、参数和返回值的预期类型")
    print("2. 增强IDE支持 - 更好的代码补全、错误提示和重构功能")
    print("3. 静态类型检查 - 与mypy等工具配合，在开发阶段捕获类型错误")
    print("4. 改进文档 - 类型注解作为代码自文档化的一部分")
    print("5. 更好的维护性 - 大型代码库和团队协作中尤为重要")
    
    print("\n主要组件：")
    print("1. 基本类型 - int, float, str, bool, None等")
    print("2. 容器类型 - List, Dict, Set, Tuple等")
    print("3. 特殊类型 - Optional, Union, Any, NoReturn等")
    print("4. 泛型支持 - TypeVar, Generic等")
    print("5. 可调用类型 - Callable")
    print("6. 协议和抽象基类 - Protocol, ABC")
    print("7. 类型别名和变量 - 自定义类型别名, NewType")
    
    print("\n使用建议：")
    print("1. 从简单开始 - 逐步引入类型注解，不必一步到位")
    print("2. 关注关键接口 - 优先为公共API和复杂函数添加类型注解")
    print("3. 利用工具 - 使用mypy等静态类型检查工具")
    print("4. 保持一致 - 团队内部统一类型注解风格")
    print("5. 版本兼容 - 考虑项目的Python版本要求，必要时使用兼容方案")
    
    print("\n常见误区：")
    print("1. 认为类型注解会影响Python的动态特性 - 它们只是提示，不影响运行时行为")
    print("2. 过度使用Any - 应尽量使用更具体的类型")
    print("3. 忽略版本兼容性 - 不同Python版本的typing功能有所差异")
    print("4. 忘记类型注解只是辅助工具 - 良好的设计和测试仍然是关键")

# 运行总结
summarize_typing()
print()

# 完整导入指南
print("=== 完整导入指南 ===")

print("typing模块常用类型的导入方式：")
print("""
# 基本类型导入
from typing import (
    # 基础类型注解
    Any, Optional, Union, NoReturn,
    
    # 容器类型
    List, Dict, Set, Tuple,
    Iterable, Sequence, Mapping, MutableMapping,
    
    # 泛型支持
    TypeVar, Generic, GenericAlias,
    
    # 可调用类型
    Callable, 
    
    # 其他实用工具
    cast, final, Type, ClassVar,
    
    # Python 3.8+ 特性
    Literal, Final, Protocol,
    
    # 类型转换
    get_type_hints, get_origin, get_args
)

# Python 3.9+ 中的替代写法
# 容器类型可以直接使用内置类型
list[int]     # 替代 List[int]
dict[str, int] # 替代 Dict[str, int]
set[int]      # 替代 Set[int]
tuple[int, ...] # 替代 Tuple[int, ...]

# Python 3.10+ 中的联合类型
int | str     # 替代 Union[int, str]
""")

print("\n=== 模块兼容性信息 ===")
print("typing模块在不同Python版本中的可用性：")

compatibility = {
    "Python 3.5": ["List", "Dict", "Set", "Tuple", "Any", "Optional", "Union", 
                  "Callable", "TypeVar", "Generic", "cast"],
    "Python 3.6": ["变量注解语法"],
    "Python 3.7": ["__future__.annotations", "get_type_hints改进"],
    "Python 3.8": ["Literal", "Final", "Protocol", "TypedDict"],
    "Python 3.9": ["内置泛型类型(list[int], dict[str, int]等)"],
    "Python 3.10": ["联合类型运算符(int | str)", "match语句中的类型检查"],
    "Python 3.11": ["Self类型", "类型参数默认值"]
}

for version, features in compatibility.items():
    print(f"\n{version} 新增/改进：")
    for feature in features:
        print(f"- {feature}")

print("\n对于旧版本Python，可以使用typing_extensions库获取较新版本的功能。")

# 最后一段，作为文档结尾
print("\n" + "="*80)
print("typing模块 - 提升Python代码质量的重要工具")
print("通过合理使用类型注解，可以显著提高代码的可读性、可维护性和可靠性。")
print("虽然Python仍然保持其动态类型的灵活性，但类型注解为静态分析和工具支持打开了大门。")
print("无论是小型脚本还是大型项目，typing模块都能为你的Python代码提供额外的安全保障和开发体验提升。")
print("="*80)

# 此文档包含了typing模块的全面介绍、详细用法和最佳实践，适合作为日常参考。
# 文档涵盖了从基础类型注解到高级泛型编程的各个方面，
# 并提供了丰富的代码示例来帮助理解各个概念的实际应用。