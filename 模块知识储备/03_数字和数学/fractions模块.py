# Python fractions模块详解

import fractions
from fractions import Fraction
import math

# 1. 模块概述
print("=== 1. fractions模块概述 ===")
print("fractions模块提供了分数运算的支持，用于需要精确分数表示的场景。")
print("该模块的主要特点：")
print("- 精确的分数表示，避免浮点数精度问题")
print("- 支持分数的创建、运算和转换")
print("- 可与整数、浮点数和字符串互操作")
print("- 支持比较和数学运算")
print()

# 2. Fraction对象的创建
print("=== 2. Fraction对象的创建 ===")

# 从整数创建
print(f"Fraction(10) = {Fraction(10)}")

# 从两个整数创建（分子和分母）
print(f"Fraction(1, 2) = {Fraction(1, 2)}")
print(f"Fraction(3, 6) = {Fraction(3, 6)}")  # 自动约分

# 从字符串创建
print(f"Fraction('1/2') = {Fraction('1/2')}")
print(f"Fraction('2.5') = {Fraction('2.5')}")
print(f"Fraction('3.14') = {Fraction('3.14')}")
print(f"Fraction('0.3333333333') = {Fraction('0.3333333333')}")

# 从浮点数创建
print(f"Fraction(0.5) = {Fraction(0.5)}")
print(f"Fraction(0.1) = {Fraction(0.1)}")  # 浮点数精度导致的问题
print(f"Fraction(0.3) = {Fraction(0.3)}")

# 使用Fraction.from_float
print(f"Fraction.from_float(0.1) = {Fraction.from_float(0.1)}")

# 使用Fraction.from_decimal
from decimal import Decimal
print(f"Fraction.from_decimal(Decimal('0.1')) = {Fraction.from_decimal(Decimal('0.1'))}")

# 负分数
print(f"Fraction(-1, 2) = {Fraction(-1, 2)}")
print(f"Fraction(1, -2) = {Fraction(1, -2)}")  # 符号自动移到分子
print()

# 3. 基本属性
print("=== 3. 基本属性 ===")

# 创建Fraction对象
frac = Fraction(3, 6)
print(f"Fraction(3, 6) = {frac}")

# 分子
print(f"frac.numerator = {frac.numerator}")

# 分母
print(f"frac.denominator = {frac.denominator}")

# 检查是否为整数
print(f"frac.is_integer() = {frac.is_integer()}")

# 转换为浮点数
print(f"float(frac) = {float(frac)}")

# 转换为字符串
print(f"str(frac) = {str(frac)}")

# 转换为元组
print(f"tuple(frac) = {tuple(frac)}")
print()

# 4. 基本算术运算
print("=== 4. 基本算术运算 ===")

# 创建Fraction对象
a = Fraction(1, 2)
b = Fraction(1, 3)

# 加法
print(f"a + b = {a + b}")

# 减法
print(f"a - b = {a - b}")

# 乘法
print(f"a * b = {a * b}")

# 除法
print(f"a / b = {a / b}")

# 整数除法
print(f"a // b = {a // b}")

# 取模
print(f"a % b = {a % b}")

# 幂运算
print(f"a ** 2 = {a ** 2}")
print(f"a ** Fraction(1, 2) = {a ** Fraction(1, 2)}")  # 平方根
print()

# 5. 比较运算
print("=== 5. 比较运算 ===")

# 创建Fraction对象
a = Fraction(1, 2)
b = Fraction(2, 4)
c = Fraction(1, 3)

# 相等比较
print(f"a == b: {a == b}")  # True，因为约分后相等
print(f"a == c: {a == c}")  # False

# 大小比较
print(f"a < c: {a < c}")    # False
print(f"a > c: {a > c}")    # True
print(f"a <= b: {a <= b}")  # True
print(f"a >= c: {a >= c}")  # True

# 与其他类型比较
print(f"a == 0.5: {a == 0.5}")  # True
print(f"a > 0: {a > 0}")        # True
print(f"a < 1: {a < 1}")        # True
print()

# 6. 数学函数
print("=== 6. 数学函数 ===")

# 创建Fraction对象
frac = Fraction(1, 2)

# 绝对值
print(f"abs(frac) = {abs(frac)}")

# 负号
print(f"-frac = {-frac}")

# 截断
print(f"math.trunc(frac) = {math.trunc(frac)}")

# 四舍五入
print(f"round(frac) = {round(frac)}")
print(f"round(frac, 1) = {round(frac, 1)}")

# 最大公约数 (gcd)
print(f"math.gcd(frac.numerator, frac.denominator) = {math.gcd(frac.numerator, frac.denominator)}")

# 转换为浮点数并使用数学函数
print(f"math.sqrt(float(frac)) = {math.sqrt(float(frac))}")
print(f"math.sin(float(frac)) = {math.sin(float(frac))}")
print(f"math.cos(float(frac)) = {math.cos(float(frac))}")
print(f"math.tan(float(frac)) = {math.tan(float(frac))}")
print()

# 7. 格式化输出
print("=== 7. 格式化输出 ===")

# 创建Fraction对象
frac = Fraction(3, 4)

# 基本格式化
print(f"基本格式: {frac}")

# 使用format方法
print(f"format(frac) = {format(frac)}")

# 转换为浮点数后格式化
print(f"浮点数格式: {float(frac):.2f}")
print(f"百分比格式: {float(frac):.1%}")

# 使用字符串格式化
print(f"字符串格式化: {frac} = {float(frac):.2f}")
print()

# 8. 特殊值
print("=== 8. 特殊值 ===")

# 零
print(f"Fraction(0, 1) = {Fraction(0, 1)}")
print(f"Fraction(0) = {Fraction(0)}")

# 一
print(f"Fraction(1, 1) = {Fraction(1, 1)}")
print(f"Fraction(1) = {Fraction(1)}")

# 无穷大（不支持）
try:
    print(f"Fraction('Infinity') = {Fraction('Infinity')}")
except ValueError as e:
    print(f"不支持无穷大: {e}")

# 非数字（不支持）
try:
    print(f"Fraction('NaN') = {Fraction('NaN')}")
except ValueError as e:
    print(f"不支持NaN: {e}")
print()

# 9. 实际应用示例
print("=== 9. 实际应用示例 ===")

# 示例1：分数加减乘除
print("分数计算示例:")
num1 = Fraction('1/3')
num2 = Fraction('1/6')
num3 = Fraction('2/5')

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num3} = {num1 * num3}")
print(f"{num1} / {num3} = {num1 / num3}")

# 示例2：精确的百分比计算
print("\n百分比计算示例:")
total = 125
part = 30
percentage = Fraction(part, total) * 100
print(f"{part}/{total} = {percentage}%")
print(f"百分比（浮点数）: {float(percentage):.2f}%")

# 示例3：食谱配料调整
print("\n食谱配料调整示例:")
original_servings = 4
new_servings = 6
scaling_factor = Fraction(new_servings, original_servings)

# 原始配料
original_ingredients = {
    '面粉': Fraction('2 1/2'),  # 2.5杯
    '糖': Fraction('3/4'),       # 0.75杯
    '鸡蛋': 2,
    '牛奶': Fraction('1 1/3')   # 1.333杯
}

# 调整后的配料
adjusted_ingredients = {}
for ingredient, amount in original_ingredients.items():
    if isinstance(amount, Fraction):
        adjusted_ingredients[ingredient] = amount * scaling_factor
    else:
        adjusted_ingredients[ingredient] = amount * scaling_factor

print(f"原始份量: {original_servings}人")
print(f"新份量: {new_servings}人")
print(f"调整系数: {scaling_factor}")
print("\n调整后的配料:")
for ingredient, amount in adjusted_ingredients.items():
    if isinstance(amount, Fraction):
        if amount.denominator == 1:
            print(f"- {ingredient}: {amount.numerator}杯")
        else:
            print(f"- {ingredient}: {amount}杯")
    else:
        print(f"- {ingredient}: {amount}个")

# 示例4：分数序列生成
print("\n分数序列生成示例:")
# 生成1/1, 1/2, 1/3, ..., 1/10
unit_fractions = [Fraction(1, i) for i in range(1, 11)]
print("单位分数序列:", unit_fractions)

# 生成调和级数的前10项和
harmonic_sum = sum(unit_fractions)
print(f"调和级数前10项和: {harmonic_sum} = {float(harmonic_sum):.5f}")
print()

# 10. 与其他数值类型的交互
print("=== 10. 与其他数值类型的交互 ===")

# 与整数交互
print(f"Fraction(1, 2) + 1 = {Fraction(1, 2) + 1}")
print(f"Fraction(3, 2) * 2 = {Fraction(3, 2) * 2}")

# 与浮点数交互
print(f"Fraction(1, 2) + 0.5 = {Fraction(1, 2) + 0.5}")
print(f"type(Fraction(1, 2) + 0.5) = {type(Fraction(1, 2) + 0.5)}")

# 与decimal模块交互
from decimal import Decimal
print(f"Fraction(1, 3) + Decimal('0.1') = {Fraction(1, 3) + Decimal('0.1')}")
print(f"type(Fraction(1, 3) + Decimal('0.1')) = {type(Fraction(1, 3) + Decimal('0.1'))}")

# 混合运算
result = Fraction(1, 2) + 0.5 * 3
print(f"Fraction(1, 2) + 0.5 * 3 = {result}")
print(f"type(result) = {type(result)}")
print()

# 11. 性能比较
print("=== 11. 性能比较 ===")

import time

def test_performance():
    """测试分数运算与浮点数运算的性能"""
    
    n = 1000000
    
    # 测试浮点数运算
    start = time.time()
    total_float = 0.0
    for i in range(1, n+1):
        total_float += 1.0 / i
    time_float = time.time() - start
    
    # 测试分数运算
    start = time.time()
    total_fraction = Fraction(0)
    for i in range(1, n+1):
        total_fraction += Fraction(1, i)
    time_fraction = time.time() - start
    
    print(f"浮点数运算时间: {time_float:.4f}秒")
    print(f"分数运算时间: {time_fraction:.4f}秒")
    print(f"分数运算比浮点数慢{time_fraction/time_float:.2f}倍")
    print(f"浮点数结果: {total_float:.15f}")
    print(f"分数结果: {total_fraction}")
    print(f"分数转浮点数: {float(total_fraction):.15f}")

# 运行性能测试（只运行10000次以节省时间）
print("简化性能测试（10000次迭代）:")
test_performance()
print()

# 12. 最佳实践
print("=== 12. 最佳实践 ===")

print("1. 从字符串创建Fraction以避免浮点数精度问题:")
print(f"Fraction('0.1') + Fraction('0.2') = {Fraction('0.1') + Fraction('0.2')}")
print(f"Fraction(0.1) + Fraction(0.2) = {Fraction(0.1) + Fraction(0.2)}")

print("\n2. 使用约分后的分数进行比较:")
print(f"Fraction(2, 4) == Fraction(1, 2): {Fraction(2, 4) == Fraction(1, 2)}")

print("\n3. 对于大量计算，考虑使用浮点数以提高性能:")
print("分数运算精度高但速度慢，浮点数运算速度快但精度有限")

print("\n4. 利用分数的精确性处理财务和测量计算:")
print("例如：1/3美元 = 33.333...美分，使用Fraction可精确表示")

print("\n5. 使用分母为1的分数表示整数:")
print(f"Fraction(5, 1) = {Fraction(5, 1)}")
print(f"Fraction(5) = {Fraction(5)}")
print()

# 13. 分数模块与小数模块的比较
print("=== 13. 分数模块与小数模块的比较 ===")

print("| 特性 | fractions模块 | decimal模块 |")
print("|------|--------------|------------|")
print("| 表示方式 | 精确分数（分子/分母） | 高精度十进制数 |")
print("| 精度 | 无限精度 | 可配置精度（默认28位） |")
print("| 适用场景 | 分数运算、精确比例 | 金融计算、货币处理 |")
print("| 性能 | 较慢 | 中等 |")
print("| 内存占用 | 较高 | 中等 |")
print("| 特殊值支持 | 不支持无穷大和NaN | 支持无穷大和NaN |")
print("| 与整数互操作 | 优秀 | 优秀 |")
print("| 格式化输出 | 有限 | 丰富 |")
print()

# 14. 总结
print("=== 14. fractions模块总结 ===")
print("fractions模块提供了精确的分数运算功能，适用于需要精确比例表示的场景。")
print("主要优势：")
print("- 精确表示分数，避免浮点数的精度问题")
print("- 自动约分和符号处理")
print("- 支持与整数、浮点数和字符串的互操作")
print("- 完整的算术和比较运算支持")
print()
print("主要劣势：")
print("- 比浮点数运算慢")
print("- 内存占用较大")
print("- 不支持无穷大和NaN")
print()
print("使用建议：")
print("- 在需要精确分数表示的场景（如数学计算、比例调整）中使用")
print("- 从字符串创建Fraction对象以避免浮点数精度问题")
print("- 对于性能要求高的大量计算，考虑使用浮点数")
print("- 结合decimal模块处理复杂的数值计算需求")
