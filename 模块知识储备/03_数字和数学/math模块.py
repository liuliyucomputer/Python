# Python math模块详解

import math

# 1. 模块概述
print("=== 1. math模块概述 ===")
print("math模块提供了基本的数学函数和常量，用于实数运算。")
print("该模块包含以下主要功能类别：")
print("- 数学常量（如π、e等）")
print("- 基本数学运算（平方根、绝对值、幂运算等）")
print("- 三角函数（正弦、余弦、正切等）")
print("- 对数和指数函数")
print("- 角度转换")
print("- 特殊函数（伽马函数、贝塞尔函数等）")
print()

# 2. 数学常量
print("=== 2. 数学常量 ===")
print(f"math.pi = {math.pi}")       # 圆周率 π
print(f"math.e = {math.e}")         # 自然对数的底数 e
print(f"math.tau = {math.tau}")     # 2π
print(f"math.inf = {math.inf}")     # 正无穷大
print(f"math.nan = {math.nan}")     # 非数字
print(f"math.hypot(3, 4) = {math.hypot(3, 4)}")  # 勾股定理
print()

# 3. 基础数学运算
print("=== 3. 基础数学运算 ===")

# 绝对值
print(f"math.fabs(-5.5) = {math.fabs(-5.5)}")  # 返回浮点数的绝对值
print(f"abs(-5) = {abs(-5)}")                   # 内置abs函数

# 幂运算
print(f"math.pow(2, 3) = {math.pow(2, 3)}")     # 2^3，返回浮点数
print(f"2 ** 3 = {2 ** 3}")                     # 内置幂运算

# 平方根
print(f"math.sqrt(16) = {math.sqrt(16)}")       # 平方根

# 向上取整
print(f"math.ceil(3.14) = {math.ceil(3.14)}")   # 向上取整

# 向下取整
print(f"math.floor(3.99) = {math.floor(3.99)}") # 向下取整

# 截断取整
print(f"math.trunc(3.99) = {math.trunc(3.99)}") # 截断小数部分

# 取模运算
print(f"math.fmod(10, 3) = {math.fmod(10, 3)}") # 浮点数模运算
print(f"10 % 3 = {10 % 3}")                     # 内置模运算

# 最大公约数
print(f"math.gcd(48, 18) = {math.gcd(48, 18)}") # 最大公约数

# 最小公倍数
print(f"math.lcm(4, 6) = {math.lcm(4, 6)}")     # 最小公倍数

# 阶乘
print(f"math.factorial(5) = {math.factorial(5)}") # 阶乘
print()

# 4. 三角函数
print("=== 4. 三角函数 ===")
print("注意：所有三角函数默认使用弧度制")

# 正弦、余弦、正切
print(f"math.sin(math.pi/2) = {math.sin(math.pi/2)}")   # 正弦
print(f"math.cos(math.pi) = {math.cos(math.pi)}")       # 余弦
print(f"math.tan(math.pi/4) = {math.tan(math.pi/4)}")   # 正切

# 反正弦、反余弦、反正切
print(f"math.asin(1) = {math.asin(1)}")                 # 反正弦
print(f"math.acos(0) = {math.acos(0)}")                 # 反余弦
print(f"math.atan(1) = {math.atan(1)}")                 # 反正切
print(f"math.atan2(1, 1) = {math.atan2(1, 1)}")         # 四象限反正切

# 双曲函数
print(f"math.sinh(math.pi/2) = {math.sinh(math.pi/2)}") # 双曲正弦
print(f"math.cosh(math.pi/2) = {math.cosh(math.pi/2)}") # 双曲余弦
print(f"math.tanh(math.pi/2) = {math.tanh(math.pi/2)}") # 双曲正切

# 反双曲函数
print(f"math.asinh(1) = {math.asinh(1)}")               # 反双曲正弦
print(f"math.acosh(1) = {math.acosh(1)}")               # 反双曲余弦
print(f"math.atanh(0.5) = {math.atanh(0.5)}")           # 反双曲正切
print()

# 5. 角度转换
print("=== 5. 角度转换 ===")

# 度转弧度
print(f"math.radians(180) = {math.radians(180)}")       # 180度转弧度

# 弧度转度
print(f"math.degrees(math.pi) = {math.degrees(math.pi)}") # π弧度转度
print()

# 6. 对数和指数函数
print("=== 6. 对数和指数函数 ===")

# 指数函数
print(f"math.exp(1) = {math.exp(1)}")                   # e^x
print(f"math.expm1(0.1) = {math.expm1(0.1)}")           # e^x - 1（小x值更精确）

# 对数函数
print(f"math.log(math.e) = {math.log(math.e)}")         # 自然对数
print(f"math.log(100, 10) = {math.log(100, 10)}")       # 以10为底的对数
print(f"math.log10(100) = {math.log10(100)}")           # 以10为底的对数
print(f"math.log2(8) = {math.log2(8)}")                 # 以2为底的对数
print(f"math.log1p(0.1) = {math.log1p(0.1)}")           # log(1+x)（小x值更精确）
print()

# 7. 特殊函数
print("=== 7. 特殊函数 ===")

# 伽马函数
print(f"math.gamma(5) = {math.gamma(5)}")               # 伽马函数 Γ(x)

# 不完全伽马函数
print(f"math.lgamma(5) = {math.lgamma(5)}")             # 伽马函数的自然对数

# 误差函数
print(f"math.erf(0) = {math.erf(0)}")                   # 误差函数
print(f"math.erfc(0) = {math.erfc(0)}")                 # 互补误差函数

# 贝塞尔函数（Python 3.6+）
if hasattr(math, 'gamma'):
    print(f"math.gamma(3) = {math.gamma(3)}")

# 8. 数值分类函数
print("=== 8. 数值分类函数 ===")

# 判断是否为无穷大
print(f"math.isinf(math.inf) = {math.isinf(math.inf)}")
print(f"math.isinf(100) = {math.isinf(100)}")

# 判断是否为非数字
print(f"math.isnan(math.nan) = {math.isnan(math.nan)}")
print(f"math.isnan(100) = {math.isnan(100)}")

# 判断是否为有限数
print(f"math.isfinite(100) = {math.isfinite(100)}")
print(f"math.isfinite(math.inf) = {math.isfinite(math.inf)}")
print()

# 9. 综合示例
print("=== 9. 综合示例 ===")

# 示例1：计算圆的面积和周长
def calculate_circle(radius):
    """计算圆的面积和周长"""
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

radius = 5
area, circumference = calculate_circle(radius)
print(f"圆的半径: {radius}")
print(f"圆的面积: {area:.2f}")
print(f"圆的周长: {circumference:.2f}")

# 示例2：计算三角形的面积（海伦公式）
def calculate_triangle_area(a, b, c):
    """使用海伦公式计算三角形面积"""
    s = (a + b + c) / 2  # 半周长
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

a, b, c = 3, 4, 5  # 直角三角形
area = calculate_triangle_area(a, b, c)
print(f"\n三角形边长: {a}, {b}, {c}")
print(f"三角形面积: {area:.2f}")

# 示例3：解二次方程 ax² + bx + c = 0
def solve_quadratic(a, b, c):
    """解二次方程"""
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None  # 无实数解
    elif discriminant == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (x1, x2)

a, b, c = 1, -5, 6  # 方程: x² - 5x + 6 = 0
roots = solve_quadratic(a, b, c)
print(f"\n二次方程 {a}x² + {b}x + {c} = 0 的解:")
if roots is None:
    print("无实数解")
elif len(roots) == 1:
    print(f"唯一解: x = {roots[0]}")
else:
    print(f"两个解: x1 = {roots[0]}, x2 = {roots[1]}")

# 示例4：计算两点之间的距离
def calculate_distance(x1, y1, x2, y2):
    """计算平面上两点之间的距离"""
    return math.hypot(x2 - x1, y2 - y1)

x1, y1 = 0, 0
x2, y2 = 3, 4
distance = calculate_distance(x1, y1, x2, y2)
print(f"\n点({x1}, {y1})到点({x2}, {y2})的距离: {distance}")

# 示例5：将极坐标转换为直角坐标
def polar_to_cartesian(r, theta):
    """将极坐标(r, theta)转换为直角坐标(x, y)"""
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

r, theta = 5, math.pi/4  # 半径5，角度45度
x, y = polar_to_cartesian(r, theta)
print(f"\n极坐标(r={r}, theta={math.degrees(theta):.1f}°)转换为直角坐标:")
print(f"x = {x:.2f}, y = {y:.2f}")

# 10. 最佳实践
print("\n=== 10. 最佳实践 ===")
print("1. 使用math模块的函数而不是自定义实现，因为它们通常经过优化且更精确")
print("2. 注意三角函数使用弧度制，如果有角度需要先转换")
print("3. 对于小数值，使用math.expm1()和math.log1p()可以获得更高的精度")
print("4. 避免直接比较浮点数是否相等，因为存在精度问题")
print("5. 使用math.isclose()来比较浮点数是否接近")
print("6. 对于高精度需求，考虑使用decimal模块")

# 示例：比较浮点数
x = 0.1 + 0.2
print(f"\n示例：0.1 + 0.2 = {x}")
print(f"直接比较 x == 0.3: {x == 0.3}")
print(f"使用math.isclose(x, 0.3): {math.isclose(x, 0.3)}")

# 11. 性能比较
print("\n=== 11. 性能比较 ===")
import time

def test_performance():
    """测试math模块函数的性能"""
    import random
    
    # 生成测试数据
    data = [random.random() for _ in range(1000000)]
    
    # 测试math.sqrt与**0.5
    start = time.time()
    result1 = [math.sqrt(x) for x in data]
    time1 = time.time() - start
    
    start = time.time()
    result2 = [x ** 0.5 for x in data]
    time2 = time.time() - start
    
    print(f"math.sqrt: {time1:.4f}秒")
    print(f"**0.5: {time2:.4f}秒")
    print(f"math.sqrt比**0.5快{time2/time1:.2f}倍")

# 运行性能测试
test_performance()

# 12. 总结
print("\n=== 12. math模块总结 ===")
print("math模块提供了全面的数学函数和常量，适用于各种数值计算场景。")
print("主要优势：")
print("- 性能优化：底层使用C实现，执行速度快")
print("- 精度高：提供了多种精确计算函数")
print("- 功能全面：涵盖了基本数学运算到高级特殊函数")
print()
print("使用math模块可以避免重复造轮子，提高代码的可读性和性能。")
print("对于需要处理复数的场景，应使用cmath模块；对于需要高精度的场景，应使用decimal模块。")
print()
print("math模块是Python数值计算的基础工具，建议熟练掌握其常用函数的使用方法。")
