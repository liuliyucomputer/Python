# cmath模块 - 复数数学函数
# 功能作用：提供用于处理复数的数学函数
# 使用情景：需要对复数进行数学运算，如复数平方根、对数、三角函数等
# 注意事项：cmath模块专门用于复数，而math模块仅适用于实数

import cmath
import math

# 模块概述
"""
cmath模块提供了各种用于复数的数学函数，包括：
- 基本函数（如幂、对数、平方根）
- 三角函数和双曲函数
- 复数的特殊操作
- 数学常量（与math模块类似，但适用于复数）

cmath模块与math模块的主要区别是：
- cmath模块处理复数，math模块处理实数
- cmath模块的函数可以接受复数参数并返回复数结果
- 对于可以接受实数的情况，cmath模块也能处理，但总是返回复数结果
"""

# 1. 复数的基本表示和操作
print("=== 复数的基本表示和操作 ===")

# 创建复数
z1 = complex(1, 2)  # 1 + 2j
z2 = 3 + 4j         # 直接使用j或J表示虚数单位
print(f"z1 = {z1}")
print(f"z2 = {z2}")

# 复数属性
print(f"z1的实部: {z1.real}")
print(f"z1的虚部: {z1.imag}")
print(f"z1的共轭复数: {z1.conjugate()}")

# 复数运算
print(f"z1 + z2 = {z1 + z2}")  # 加法
print(f"z1 - z2 = {z1 - z2}")  # 减法
print(f"z1 * z2 = {z1 * z2}")  # 乘法
print(f"z1 / z2 = {z1 / z2}")  # 除法
print(f"z1 ** z2 = {z1 ** z2}")  # 幂运算
print()

# 2. cmath模块的常量
print("=== cmath模块的常量 ===")
print(f"π (pi): {cmath.pi}")        # 圆周率
print(f"e: {cmath.e}")            # 自然对数的底
print(f"1j: {cmath.sqrt(-1)}")     # 虚数单位
print(f"正无穷大: {cmath.inf}")    # 复数正无穷大
print(f"负无穷大: {cmath.infj}")   # 复数虚部无穷大
print(f"NaN: {cmath.nan}")        # 非数字
print()

# 3. 基本复数函数
def demonstrate_basic_functions():
    """演示基本复数函数"""
    print("=== 基本复数函数 ===")
    
    z = 1 + 1j
    print(f"z = {z}")
    
    # 绝对值（模）
    print(f"abs(z) = {abs(z)}")                    # 内置函数
    print(f"cmath.polar(z) = {cmath.polar(z)}")      # 转换为极坐标形式 (r, phi)
    
    # 极坐标转直角坐标
    r, phi = 2, cmath.pi/4  # 半径2，角度45度
    print(f"cmath.rect({r}, {phi}) = {cmath.rect(r, phi)}")
    
    # 平方根
    print(f"cmath.sqrt(z) = {cmath.sqrt(z)}")        # 复数平方根
    print(f"cmath.sqrt(-1) = {cmath.sqrt(-1)}")      # 负数的平方根
    
    # 对数
    print(f"cmath.log(z) = {cmath.log(z)}")          # 自然对数
    print(f"cmath.log10(z) = {cmath.log10(z)}")      # 以10为底的对数
    print(f"cmath.log(-1) = {cmath.log(-1)}")        # 负数的对数
    
    # 指数
    print(f"cmath.exp(z) = {cmath.exp(z)}")          # e的z次方
    print()

# 4. 复数三角函数
def demonstrate_trigonometric():
    """演示复数三角函数"""
    print("=== 复数三角函数 ===")
    
    z = 1 + 1j
    print(f"z = {z}")
    
    # 基本三角函数
    print(f"cmath.sin(z) = {cmath.sin(z)}")        # 正弦
    print(f"cmath.cos(z) = {cmath.cos(z)}")        # 余弦
    print(f"cmath.tan(z) = {cmath.tan(z)}")        # 正切
    
    # 反三角函数
    print(f"cmath.asin(0.5) = {cmath.asin(0.5)}")  # 反正弦
    print(f"cmath.acos(0.5) = {cmath.acos(0.5)}")  # 反余弦
    print(f"cmath.atan(1) = {cmath.atan(1)}")      # 反正切
    
    # 双曲函数
    print(f"cmath.sinh(z) = {cmath.sinh(z)}")      # 双曲正弦
    print(f"cmath.cosh(z) = {cmath.cosh(z)}")      # 双曲余弦
    print(f"cmath.tanh(z) = {cmath.tanh(z)}")      # 双曲正切
    
    # 反双曲函数
    print(f"cmath.asinh(z) = {cmath.asinh(z)}")    # 反双曲正弦
    print(f"cmath.acosh(1+z) = {cmath.acosh(1+z)}")  # 反双曲余弦
    print(f"cmath.atanh(0.5) = {cmath.atanh(0.5)}")  # 反双曲正切
    print()

# 5. 复数分类函数
def demonstrate_classification():
    """演示复数分类函数"""
    print("=== 复数分类函数 ===")
    
    test_values = [
        1.0 + 0j,        # 实数
        0.0 + 1j,        # 纯虚数
        1.0 + 1j,        # 一般复数
        float('inf') + 0j,  # 实部无穷大
        0.0 + float('inf')*1j,  # 虚部无穷大
        float('nan') + 0j,  # 实部为NaN
        0.0 + float('nan')*1j,  # 虚部为NaN
    ]
    
    for z in test_values:
        print(f"z = {z}")
        print(f"  isfinite: {cmath.isfinite(z)}")  # 是否为有限数
        print(f"  isinf: {cmath.isinf(z)}")      # 是否为无穷大
        print(f"  isnan: {cmath.isnan(z)}")      # 是否为NaN
        
        # 检查是否为实数
        if z.imag == 0:
            print(f"  是实数")
        elif z.real == 0:
            print(f"  是纯虚数")
        else:
            print(f"  是一般复数")
        print()

# 6. 实际应用示例
def complex_roots(a, b, c):
    """求解二次方程 ax² + bx + c = 0 的复数根"""
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

def complex_polar_form(z):
    """将复数转换为极坐标形式并返回格式化的字符串"""
    r, phi = cmath.polar(z)
    # 将弧度转换为度数便于阅读
    degrees = math.degrees(phi)
    return f"{r:.4f} * e^({phi:.4f}j) 或 {r:.4f} ∠ {degrees:.2f}°"

def demonstrate_applications():
    """演示实际应用"""
    print("=== 实际应用示例 ===")
    
    # 1. 求解二次方程的复数根
    print("二次方程 x² + x + 1 = 0 的根:")
    root1, root2 = complex_roots(1, 1, 1)
    print(f"根1: {root1}")
    print(f"根2: {root2}")
    
    # 2. 将复数转换为极坐标形式
    z = 1 + 1j
    print(f"\n复数 {z} 的极坐标形式:")
    print(complex_polar_form(z))
    
    # 3. 计算复数的指数函数
    print(f"\n复数 {z} 的指数函数:")
    exp_z = cmath.exp(z)
    print(f"e^({z}) = {exp_z}")
    print(f"极坐标形式: {complex_polar_form(exp_z)}")
    
    # 4. 复数的三角恒等式验证
    print("\n验证欧拉公式 e^(πj) + 1 = 0:")
    euler = cmath.exp(cmath.pi * 1j) + 1
    print(f"e^(πj) + 1 = {euler}")
    print(f"近似为: {euler.real:.10f} + {euler.imag:.10f}j")
    print()

# 7. cmath与math模块的比较
def compare_math_cmath():
    """比较math和cmath模块"""
    print("=== math与cmath模块比较 ===")
    
    # 对实数的处理
    x = 2.0
    print(f"实数 x = {x}")
    print(f"math.sqrt(x) = {math.sqrt(x)}, 类型: {type(math.sqrt(x)).__name__}")
    print(f"cmath.sqrt(x) = {cmath.sqrt(x)}, 类型: {type(cmath.sqrt(x)).__name__}")
    
    # 对负数的处理
    x = -1.0
    print(f"\n负数 x = {x}")
    try:
        math_result = math.sqrt(x)
    except ValueError as e:
        math_result = f"错误: {e}"
    print(f"math.sqrt(x) = {math_result}")
    
    cmath_result = cmath.sqrt(x)
    print(f"cmath.sqrt(x) = {cmath_result}")
    
    # 对复数的处理
    z = 1 + 1j
    print(f"\n复数 z = {z}")
    try:
        math_result = math.sqrt(z)
    except TypeError as e:
        math_result = f"错误: {e}"
    print(f"math.sqrt(z) = {math_result}")
    
    cmath_result = cmath.sqrt(z)
    print(f"cmath.sqrt(z) = {cmath_result}")
    print()

# 8. 注意事项和最佳实践
"""
1. **选择适当的模块**：
   - 处理实数时优先使用math模块
   - 处理复数或需要处理负数平方根等操作时使用cmath模块

2. **精度问题**：
   - 与math模块一样，cmath模块的浮点数计算也会有精度限制
   - 比较复数时应分别比较实部和虚部，且使用近似比较

3. **类型转换**：
   - cmath模块的函数总是返回复数类型，即使结果在数学上是实数
   - 需要实数结果时，可以取返回值的.real属性

4. **特殊值处理**：
   - 对于无穷大、NaN等特殊值，cmath提供了isfinite(), isinf(), isnan()函数进行检测
   - 这些函数比直接比较更可靠

5. **性能考虑**：
   - 对于大量的复数计算，考虑使用专门的科学计算库如NumPy
   - NumPy提供了更高效的向量化复数运算
"""

def demonstrate_best_practices():
    """演示最佳实践"""
    print("=== 最佳实践示例 ===")
    
    # 安全地比较复数
    z1 = 1.0 + 2.0j
    z2 = 1.0 + 2.0000000001j
    
    # 直接比较
    print(f"z1 = {z1}")
    print(f"z2 = {z2}")
    print(f"直接比较 z1 == z2: {z1 == z2}")
    
    # 近似比较
    tolerance = 1e-9
    approx_equal = (abs(z1.real - z2.real) < tolerance and 
                   abs(z1.imag - z2.imag) < tolerance)
    print(f"近似比较 (容差={tolerance}): {approx_equal}")
    
    # 处理可能返回复数的情况
    x = -4
    sqrt_x = cmath.sqrt(x)
    print(f"\nsqrt({x}) = {sqrt_x}")
    
    # 从复数中提取实数结果（当知道结果应为实数时）
    y = 4
    sqrt_y = cmath.sqrt(y)
    print(f"\nsqrt({y}) = {sqrt_y}")
    if abs(sqrt_y.imag) < tolerance:
        print(f"实数结果: {sqrt_y.real}")
    
    # 检查特殊值
    inf_complex = complex(float('inf'), 0)
    nan_complex = complex(float('nan'), 0)
    print(f"\n检查无穷大: cmath.isfinite({inf_complex}) = {cmath.isfinite(inf_complex)}")
    print(f"检查NaN: cmath.isnan({nan_complex}) = {cmath.isnan(nan_complex)}")
    print()

# 运行演示代码
if __name__ == "__main__":
    print("Python cmath模块演示\n")
    
    demonstrate_basic_functions()
    demonstrate_trigonometric()
    demonstrate_classification()
    demonstrate_applications()
    compare_math_cmath()
    demonstrate_best_practices()
    
    print("演示完成！")