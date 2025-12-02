# numbers模块 - 数值抽象基类
# 功能作用：定义数值类型的抽象基类，提供数值操作的接口规范
# 使用情景：创建自定义数值类型、类型检查、确保数值操作一致性
# 注意事项：不直接提供具体实现；主要用于类型判断和接口定义；比具体数值类型（如int、float）更抽象

import numbers
from numbers import Number, Integral, Rational, Real, Complex
import math
from fractions import Fraction
from decimal import Decimal

# 模块概述
"""
numbers模块定义了数值类型的抽象基类(ABCs)，为数值操作提供了统一的接口规范。
这些抽象基类允许我们：
1. 检查一个对象是否属于某种数值类型（如：是否为整数、是否为实数）
2. 创建符合数值接口的自定义数值类型
3. 编写通用的数值处理函数，适用于多种数值类型

核心抽象基类层次结构：
- Number (所有数值类型的基类)
  ├── Complex (复数类型)
  │   ├── Real (实数类型)
  │   │   ├── Rational (有理数类型)
  │   │   │   └── Integral (整数类型)
  │   │   └── ...
  │   └── ...
  └── ...
"""

# 1. 基本使用 - 类型检查
print("=== 1. 基本使用 - 类型检查 ===")

def type_checking_demo():
    """numbers模块的类型检查功能示例"""
    print("数值类型检查示例:")
    
    # 定义各种数值
    values = [
        42,               # int
        3.14,             # float
        2 + 3j,           # complex
        Fraction(1, 2),   # fractions.Fraction
        Decimal('0.1'),   # decimal.Decimal
        "42",              # str (非数值类型)
        [1, 2, 3]         # list (非数值类型)
    ]
    
    # 检查每个值的类型
    for value in values:
        value_type = type(value).__name__
        print(f"\n值: {value} (类型: {value_type})")
        print(f"  是否为Number: {isinstance(value, Number)}")
        print(f"  是否为Integral: {isinstance(value, Integral)}")
        print(f"  是否为Rational: {isinstance(value, Rational)}")
        print(f"  是否为Real: {isinstance(value, Real)}")
        print(f"  是否为Complex: {isinstance(value, Complex)}")

# 运行类型检查示例
type_checking_demo()
print()

# 2. 抽象基类详解
print("=== 2. 抽象基类详解 ===")

def abstract_base_classes_demo():
    """numbers模块中抽象基类的详细说明"""
    print("numbers模块核心抽象基类:\n")
    
    # Number类
    print("1. Number类:")
    print("   - 所有数值类型的顶层抽象基类")
    print("   - 定义了所有数值类型共有的基本操作接口")
    print("   - 主要方法: +, -, *, /, abs(), conjugate(), etc.\n")
    
    # Complex类
    print("2. Complex类:")
    print("   - 复数类型的抽象基类")
    print("   - 要求实现的属性和方法:")
    print("     - real: 实部")
    print("     - imag: 虚部")
    print("     - conjugate(): 返回共轭复数")
    print("     - __complex__(): 转换为complex类型\n")
    
    # Real类
    print("3. Real类:")
    print("   - 实数类型的抽象基类，继承自Complex")
    print("   - 要求实现的属性和方法:")
    print("     - is_integer(): 判断是否为整数")
    print("     - __float__(): 转换为float类型")
    print("     - 比较操作: <, <=, >, >=, ==, etc.\n")
    
    # Rational类
    print("4. Rational类:")
    print("   - 有理数类型的抽象基类，继承自Real")
    print("   - 要求实现的属性:")
    print("     - numerator: 分子")
    print("     - denominator: 分母（正整数）\n")
    
    # Integral类
    print("5. Integral类:")
    print("   - 整数类型的抽象基类，继承自Rational")
    print("   - 要求实现的方法:")
    print("     - __int__(): 转换为int类型")
    print("     - bit_length(): 返回二进制表示的长度")
    print("     - to_bytes(): 转换为字节序列")
    print("     - from_bytes(): 从字节序列创建整数\n")
    
    # 类型检查示例
    print("类型检查实际应用:\n")
    def process_numeric_value(value):
        """根据数值类型处理值"""
        if isinstance(value, Integral):
            print(f"处理整数: {value}")
            # 整数特定操作
            print(f"  二进制表示: {bin(value)}")
            print(f"  绝对值: {abs(value)}")
        elif isinstance(value, Rational):
            print(f"处理有理数: {value} (分数表示: {value.numerator}/{value.denominator})")
            # 有理数特定操作
            print(f"  简化分数: {value}")
            print(f"  小数表示: {float(value):.4f}")
        elif isinstance(value, Real):
            print(f"处理实数: {value}")
            # 实数特定操作
            print(f"  四舍五入: {round(value, 2)}")
            print(f"  平方根: {math.sqrt(value):.4f}")
        elif isinstance(value, Complex):
            print(f"处理复数: {value}")
            # 复数特定操作
            print(f"  实部: {value.real}, 虚部: {value.imag}")
            print(f"  共轭复数: {value.conjugate()}")
        elif isinstance(value, Number):
            print(f"处理通用数值: {value}")
        else:
            raise TypeError(f"不支持的数值类型: {type(value)}")
    
    # 测试不同数值类型
    test_values = [
        42,                  # int
        Fraction(3, 4),      # Fraction
        3.14159,             # float
        2 + 3j,              # complex
        Decimal('123.456')   # Decimal
    ]
    
    print("不同数值类型的处理结果:\n")
    for value in test_values:
        process_numeric_value(value)
        print()

# 运行抽象基类演示
abstract_base_classes_demo()
print()

# 3. 创建自定义数值类型
print("=== 3. 创建自定义数值类型 ===")

def custom_numeric_type_demo():
    """演示如何创建符合numbers抽象基类的自定义数值类型"""
    print("创建自定义分数类型示例:\n")
    
    from abc import ABC, abstractmethod
    
    class CustomFraction(Number, ABC):
        """自定义分数类型，实现Rational接口"""
        def __init__(self, numerator, denominator=1):
            # 确保分母为正
            if denominator == 0:
                raise ValueError("分母不能为零")
            if denominator < 0:
                numerator = -numerator
                denominator = -denominator
            
            # 简化分数
            common_divisor = math.gcd(abs(numerator), denominator)
            self._numerator = numerator // common_divisor
            self._denominator = denominator // common_divisor
        
        @property
        def numerator(self):
            "分子"
            return self._numerator
        
        @property
        def denominator(self):
            "分母"
            return self._denominator
        
        @property
        def real(self):
            "实部"
            return float(self)
        
        @property
        def imag(self):
            "虚部（为0，因为是实数）"
            return 0.0
        
        def conjugate(self):
            "返回共轭复数（自身）"
            return self
        
        def __complex__(self):
            "转换为complex类型"
            return complex(float(self))
        
        def __float__(self):
            "转换为float类型"
            return self.numerator / self.denominator
        
        def __int__(self):
            "转换为int类型（截断小数部分）"
            return self.numerator // self.denominator
        
        def __round__(self, ndigits=None):
            "四舍五入"
            return round(float(self), ndigits)
        
        def is_integer(self):
            "判断是否为整数"
            return self.denominator == 1
        
        def __add__(self, other):
            "加法"
            if isinstance(other, CustomFraction):
                return CustomFraction(
                    self.numerator * other.denominator + other.numerator * self.denominator,
                    self.denominator * other.denominator
                )
            elif isinstance(other, Integral):
                return CustomFraction(self.numerator + other * self.denominator, self.denominator)
            elif isinstance(other, Rational):
                return CustomFraction(
                    self.numerator * other.denominator + other.numerator * self.denominator,
                    self.denominator * other.denominator
                )
            elif isinstance(other, Real):
                return float(self) + other
            elif isinstance(other, Complex):
                return complex(float(self)) + other
            else:
                return NotImplemented
        
        def __sub__(self, other):
            "减法"
            if isinstance(other, CustomFraction):
                return CustomFraction(
                    self.numerator * other.denominator - other.numerator * self.denominator,
                    self.denominator * other.denominator
                )
            elif isinstance(other, Integral):
                return CustomFraction(self.numerator - other * self.denominator, self.denominator)
            elif isinstance(other, Rational):
                return CustomFraction(
                    self.numerator * other.denominator - other.numerator * self.denominator,
                    self.denominator * other.denominator
                )
            elif isinstance(other, Real):
                return float(self) - other
            elif isinstance(other, Complex):
                return complex(float(self)) - other
            else:
                return NotImplemented
        
        def __mul__(self, other):
            "乘法"
            if isinstance(other, CustomFraction):
                return CustomFraction(
                    self.numerator * other.numerator,
                    self.denominator * other.denominator
                )
            elif isinstance(other, Integral):
                return CustomFraction(self.numerator * other, self.denominator)
            elif isinstance(other, Rational):
                return CustomFraction(
                    self.numerator * other.numerator,
                    self.denominator * other.denominator
                )
            elif isinstance(other, Real):
                return float(self) * other
            elif isinstance(other, Complex):
                return complex(float(self)) * other
            else:
                return NotImplemented
        
        def __truediv__(self, other):
            "除法"
            if isinstance(other, CustomFraction):
                return CustomFraction(
                    self.numerator * other.denominator,
                    self.denominator * other.numerator
                )
            elif isinstance(other, Integral):
                return CustomFraction(self.numerator, self.denominator * other)
            elif isinstance(other, Rational):
                return CustomFraction(
                    self.numerator * other.denominator,
                    self.denominator * other.numerator
                )
            elif isinstance(other, Real):
                return float(self) / other
            elif isinstance(other, Complex):
                return complex(float(self)) / other
            else:
                return NotImplemented
        
        def __repr__(self):
            "字符串表示"
            return f"CustomFraction({self.numerator}, {self.denominator})"
        
        def __str__(self):
            "友好字符串表示"
            if self.denominator == 1:
                return f"{self.numerator}"
            return f"{self.numerator}/{self.denominator}"
    
    # 使用自定义分数类型
    print("使用自定义分数类型:\n")
    a = CustomFraction(1, 2)
    b = CustomFraction(1, 3)
    
    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a + 2 = {a + 2}")
    print(f"a * 3.14 = {a * 3.14:.4f}")
    print(f"a是否为整数: {a.is_integer()}")
    print(f"a的分子: {a.numerator}, 分母: {a.denominator}")
    print(f"a的float表示: {float(a):.4f}")
    
    # 验证类型检查
    print(f"\n验证类型检查:\n")
    print(f"isinstance(a, Number): {isinstance(a, Number)}")
    print(f"isinstance(a, Rational): {isinstance(a, Rational)}")
    print(f"isinstance(a, Real): {isinstance(a, Real)}")

# 运行自定义数值类型演示
custom_numeric_type_demo()
print()

# 4. 实际应用示例
print("=== 4. 实际应用示例 ===")

def practical_applications():
    """numbers模块的实际应用场景"""
    print("numbers模块的实际应用场景:\n")
    
    # 应用1: 通用数值处理函数
    print("应用1: 通用数值处理函数\n")
    def numeric_processor(value):
        """处理各种类型的数值，确保兼容性"""
        # 检查输入是否为数值类型
        if not isinstance(value, Number):
            raise TypeError(f"输入必须是数值类型，而不是{type(value).__name__}")
        
        # 根据数值类型执行不同操作
        result = {}
        
        if isinstance(value, Integral):
            result["类型"] = "整数"
            result["二进制表示"] = bin(value)
            result["八进制表示"] = oct(value)
            result["十六进制表示"] = hex(value)
            result["是否为偶数"] = value % 2 == 0
        elif isinstance(value, Rational):
            result["类型"] = "有理数"
            result["分数表示"] = f"{value.numerator}/{value.denominator}"
            result["小数表示"] = float(value)
            result["简化形式"] = value
        elif isinstance(value, Real):
            result["类型"] = "实数"
            result["四舍五入(2位)"] = round(value, 2)
            result["绝对值"] = abs(value)
            result["是否为正数"] = value > 0
        elif isinstance(value, Complex):
            result["类型"] = "复数"
            result["实部"] = value.real
            result["虚部"] = value.imag
            result["模"] = abs(value)
            result["辐角"] = math.atan2(value.imag, value.real)
        
        # 所有数值类型通用操作
        result["值"] = value
        result["加10"] = value + 10
        result["乘以2"] = value * 2
        
        return result
    
    # 测试通用数值处理函数
    test_values = [
        42,                  # int
        Fraction(5, 3),      # Fraction
        3.14159,             # float
        2 + 3j               # complex
    ]
    
    for value in test_values:
        print(f"处理{type(value).__name__}类型值: {value}")
        processed = numeric_processor(value)
        for key, val in processed.items():
            print(f"  {key}: {val}")
        print()
    
    # 应用2: 创建数值类型装饰器
    print("应用2: 创建数值类型装饰器\n")
    def accept_numeric_types(*allowed_types):
        """装饰器：限制函数只接受指定的数值类型"""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # 检查位置参数
                for i, arg in enumerate(args):
                    if not any(isinstance(arg, numeric_type) for numeric_type in allowed_types):
                        raise TypeError(f"参数{i}必须是{allowed_types}类型之一，而不是{type(arg).__name__}")
                
                # 检查关键字参数
                for name, arg in kwargs.items():
                    if not any(isinstance(arg, numeric_type) for numeric_type in allowed_types):
                        raise TypeError(f"参数{name}必须是{allowed_types}类型之一，而不是{type(arg).__name__}")
                
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    # 使用装饰器
    @accept_numeric_types(Real)
    def calculate_circle_area(radius):
        "计算圆的面积"
        return math.pi * radius ** 2
    
    @accept_numeric_types(Integral)
    def factorial(n):
        "计算阶乘"
        if n < 0:
            raise ValueError("阶乘仅定义非负整数")
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    
    # 测试装饰器
    print("测试数值类型装饰器:\n")
    try:
        print(f"半径为2的圆面积: {calculate_circle_area(2):.4f}")
        print(f"半径为2.5的圆面积: {calculate_circle_area(2.5):.4f}")
        print(f"半径为Fraction(3,2)的圆面积: {calculate_circle_area(Fraction(3,2)):.4f}")
        print(f"5的阶乘: {factorial(5)}")
        
        # 这行会抛出错误
        print(f"错误测试: {calculate_circle_area('2')}")
    except TypeError as e:
        print(f"捕获到预期错误: {e}")
    except Exception as e:
        print(f"捕获到意外错误: {e}")

# 运行实际应用示例
practical_applications()
print()

# 5. 最佳实践和注意事项
print("=== 5. 最佳实践和注意事项 ===")

def best_practices():
    """使用numbers模块的最佳实践和注意事项"""
    print("使用numbers模块的最佳实践:\n")
    
    # 1. 类型检查的最佳实践
    print("1. 类型检查最佳实践:")
    print("   - 优先使用isinstance(value, Number)而非type(value) in (int, float, ...)")
    print("   - 示例:\n")
    print("     # 推荐写法")
    print("     if isinstance(value, Number):\n        # 处理数值类型\n")
    print("     # 不推荐写法")
    print("     if type(value) in (int, float, complex):\n        # 处理数值类型 (遗漏了Fraction, Decimal等)\n")
    
    # 2. 避免过度抽象
    print("\n2. 避免过度抽象:")
    print("   - numbers模块主要用于类型检查，而非日常数值操作")
    print("   - 直接使用具体数值类型(int, float, Fraction等)进行计算")
    print("   - 仅在需要通用数值处理时使用numbers模块的抽象基类\n")
    
    # 3. 性能考虑
    print("3. 性能考虑:")
    print("   - 抽象基类检查比具体类型检查稍慢")
    print("   - 在性能关键路径中，考虑使用具体类型检查")
    print("   - 对于频繁调用的函数，缓存类型检查结果\n")
    
    # 4. 扩展数值类型
    print("4. 扩展数值类型:")
    print("   - 当创建自定义数值类型时，应继承numbers模块的抽象基类")
    print("   - 实现所有抽象方法和属性，确保兼容性")
    print("   - 优先考虑组合而非继承现有数值类型\n")
    
    # 5. 与其他模块的配合
    print("5. 与其他模块的配合:")
    print("   - 与fractions模块: 用于精确分数运算")
    print("   - 与decimal模块: 用于高精度十进制运算")
    print("   - 与math模块: 用于数学函数")
    print("   - 与numpy模块: 用于数值数组运算\n")
    
    # 6. 常见陷阱
    print("6. 常见陷阱:")
    print("   - 不要尝试实例化numbers模块中的抽象基类")
    print("   - 注意: isinstance(True, Integral) 返回True，因为bool是int的子类")
    print("   - 示例:\n")
    print("     print(isinstance(True, Integral))  # 输出: True")
    print("     print(isinstance(False, Integral)) # 输出: True\n")
    print("   - 解决方法: 先检查是否为bool类型\n")
    print("     def is_real_number(value):\n         return isinstance(value, Real) and not isinstance(value, bool)\n")
    print("     print(is_real_number(True))  # 输出: False")
    print("     print(is_real_number(42))    # 输出: True")

# 运行最佳实践示例
best_practices()

# 6. 总结
print("\n=== 总结 ===")
print("numbers模块为Python数值类型提供了统一的抽象接口，主要用于:\n")
print("1. 类型检查 - 判断一个对象是否属于某种数值类型")
print("2. 接口定义 - 为自定义数值类型提供标准接口规范")
print("3. 通用编程 - 编写适用于多种数值类型的通用函数\n")
print("核心优势在于抽象和接口标准化，而非提供具体实现。在实际数值计算中，")
print("通常会结合使用具体数值类型(如int, float, Fraction, Decimal)和numbers模块的抽象基类，")
print("以实现既精确又灵活的数值处理。\n")
print("使用建议: 当需要编写能够处理多种数值类型的通用代码时，numbers模块是理想的选择；")
print("对于简单的数值计算，直接使用具体数值类型即可。")

# 运行完整演示
if __name__ == "__main__":
    print("Python numbers模块完整演示\n")
    print("请参考源代码中的详细示例和说明")