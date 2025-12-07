# Python cmath模块详解

import cmath

# 1. 模块概述
print("=== 1. cmath模块概述 ===")
print("cmath模块提供了复数运算的函数和常量，功能与math模块类似，但适用于复数。")
print("该模块包含以下主要功能类别：")
print("- 复数常量（如虚数单位j）")
print("- 复数的基本运算（绝对值、共轭等）")
print("- 复数的三角函数")
print("- 复数的对数和指数函数")
print("- 复数的平方根和幂运算")
print("- 复数的相位和极坐标转换")
print()

# 2. 复数常量
print("=== 2. 复数常量 ===")
print(f"cmath.pi = {cmath.pi}")       # 圆周率 π
print(f"cmath.e = {cmath.e}")         # 自然对数的底数 e
print(f"cmath.tau = {cmath.tau}")     # 2π
print(f"cmath.inf = {cmath.inf}")     # 正无穷大
print(f"cmath.infj = {cmath.infj}")   # 复无穷大
print(f"cmath.nan = {cmath.nan}")     # 非数字
print(f"cmath.nanj = {cmath.nanj}")   # 复非数字
print()

# 3. 复数的创建和表示
print("=== 3. 复数的创建和表示 ===")

# 创建复数的几种方式
z1 = complex(3, 4)          # 使用实部和虚部创建
z2 = 3 + 4j                 # 直接使用虚数单位j
z3 = complex('3+4j')        # 从字符串创建

print(f"z1 = complex(3, 4) = {z1}")
print(f"z2 = 3 + 4j = {z2}")
print(f"z3 = complex('3+4j') = {z3}")

# 获取实部和虚部
print(f"z1的实部: {z1.real}")
print(f"z1的虚部: {z1.imag}")

# 共轭复数
print(f"z1的共轭复数: {cmath.conj(z1)}")
print(f"z1的共轭复数(内置): {z1.conjugate()}")
print()

# 4. 复数的基本运算
print("=== 4. 复数的基本运算 ===")

z1 = 3 + 4j
z2 = 1 + 2j

# 加法
print(f"z1 + z2 = {z1 + z2}")

# 减法
print(f"z1 - z2 = {z1 - z2}")

# 乘法
print(f"z1 * z2 = {z1 * z2}")

# 除法
print(f"z1 / z2 = {z1 / z2}")

# 幂运算
print(f"z1 ** z2 = {z1 ** z2}")
print(f"cmath.pow(z1, z2) = {cmath.pow(z1, z2)}")

# 绝对值（模）
print(f"z1的绝对值: {abs(z1)}")
print(f"cmath.abs(z1): {cmath.abs(z1)}")
print()

# 5. 复数的三角函数
print("=== 5. 复数的三角函数 ===")

z = 1 + 1j

# 正弦、余弦、正切
print(f"cmath.sin(z) = {cmath.sin(z)}")
print(f"cmath.cos(z) = {cmath.cos(z)}")
print(f"cmath.tan(z) = {cmath.tan(z)}")

# 反正弦、反余弦、反正切
print(f"cmath.asin(z) = {cmath.asin(z)}")
print(f"cmath.acos(z) = {cmath.acos(z)}")
print(f"cmath.atan(z) = {cmath.atan(z)}")

# 双曲函数
print(f"cmath.sinh(z) = {cmath.sinh(z)}")
print(f"cmath.cosh(z) = {cmath.cosh(z)}")
print(f"cmath.tanh(z) = {cmath.tanh(z)}")

# 反双曲函数
print(f"cmath.asinh(z) = {cmath.asinh(z)}")
print(f"cmath.acosh(z) = {cmath.acosh(z)}")
print(f"cmath.atanh(z) = {cmath.atanh(z)}")
print()

# 6. 复数的对数和指数函数
print("=== 6. 复数的对数和指数函数 ===")

z = 1 + 1j

# 指数函数
print(f"cmath.exp(z) = {cmath.exp(z)}")
print(f"cmath.expm1(z) = {cmath.expm1(z)}")  # e^z - 1（小z值更精确）

# 对数函数
print(f"cmath.log(z) = {cmath.log(z)}")                 # 自然对数
print(f"cmath.log(z, 10) = {cmath.log(z, 10)}")         # 以10为底的对数
print(f"cmath.log10(z) = {cmath.log10(z)}")             # 以10为底的对数
print(f"cmath.log2(z) = {cmath.log2(z)}")               # 以2为底的对数
print(f"cmath.log1p(z) = {cmath.log1p(z)}")             # log(1+z)（小z值更精确）
print()

# 7. 复数的平方根和其他根
print("=== 7. 复数的平方根和其他根 ===")

z = 1 + 0j

# 平方根
print(f"cmath.sqrt(z) = {cmath.sqrt(z)}")
print(f"z ** 0.5 = {z ** 0.5}")

# 立方根
print(f"cmath.exp(cmath.log(z)/3) = {cmath.exp(cmath.log(z)/3)}")  # 计算立方根的一种方式
print(f"z ** (1/3) = {z ** (1/3)}")

# 注意：复数有多个根
z = -1 + 0j
print(f"\n-1的平方根:")
print(f"cmath.sqrt(z) = {cmath.sqrt(z)}")  # 返回主根
print(f"另一个根: {-cmath.sqrt(z)}")
print()

# 8. 复数的相位和极坐标转换
print("=== 8. 复数的相位和极坐标转换 ===")

z = 3 + 4j

# 相位角（弧度）
print(f"cmath.phase(z) = {cmath.phase(z)}")
print(f"相位角（度）: {cmath.degrees(cmath.phase(z)):.2f}°")

# 极坐标转换
r = abs(z)
theta = cmath.phase(z)
print(f"z的极坐标表示: r={r}, θ={theta:.4f}弧度")

# 从极坐标转换回直角坐标
z_new = cmath.rect(r, theta)
print(f"从极坐标转换回直角坐标: {z_new}")

# 使用math.atan2计算相位角
print(f"使用math.atan2计算相位角: {math.atan2(z.imag, z.real)}")
print()

# 9. 复数的分类函数
print("=== 9. 复数的分类函数 ===")

# 判断是否为无穷大
print(f"cmath.isinf(cmath.inf) = {cmath.isinf(cmath.inf)}")
print(f"cmath.isinf(cmath.infj) = {cmath.isinf(cmath.infj)}")
print(f"cmath.isinf(3+4j) = {cmath.isinf(3+4j)}")

# 判断是否为非数字
print(f"cmath.isnan(cmath.nan) = {cmath.isnan(cmath.nan)}")
print(f"cmath.isnan(cmath.nanj) = {cmath.isnan(cmath.nanj)}")
print(f"cmath.isnan(3+4j) = {cmath.isnan(3+4j)}")

# 判断是否为有限数
print(f"cmath.isfinite(3+4j) = {cmath.isfinite(3+4j)}")
print(f"cmath.isfinite(cmath.inf) = {cmath.isfinite(cmath.inf)}")
print()

# 10. 特殊函数
print("=== 10. 特殊函数 ===")

z = 1 + 1j

# 伽马函数
print(f"cmath.gamma(z) = {cmath.gamma(z)}")

# 不完全伽马函数
print(f"cmath.lgamma(z) = {cmath.lgamma(z)}")

# 误差函数
print(f"cmath.erf(z) = {cmath.erf(z)}")
print(f"cmath.erfc(z) = {cmath.erfc(z)}")
print()

# 11. 综合示例
print("=== 11. 综合示例 ===")

# 示例1：求解复数方程 z^2 + 2z + 5 = 0
def solve_complex_quadratic(a, b, c):
    """解复数二次方程 ax² + bx + c = 0"""
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return (root1, root2)

a, b, c = 1, 2, 5  # 方程: z² + 2z + 5 = 0
roots = solve_complex_quadratic(a, b, c)
print(f"复数二次方程 {a}z² + {b}z + {c} = 0 的解:")
print(f"z1 = {roots[0]}")
print(f"z2 = {roots[1]}")

# 验证解
print(f"\n验证解:")
print(f"a*z1² + b*z1 + c = {a*roots[0]**2 + b*roots[0] + c}")
print(f"a*z2² + b*z2 + c = {a*roots[1]**2 + b*roots[1] + c}")

# 示例2：复数的指数和对数运算
def complex_exponential_and_logarithm():
    """演示复数的指数和对数运算"""
    # 欧拉公式：e^(iθ) = cosθ + i sinθ
    theta = math.pi / 2
    z = cmath.exp(1j * theta)
    print(f"\n欧拉公式演示:")
    print(f"e^(iπ/2) = {z}")
    print(f"cos(π/2) + i sin(π/2) = {math.cos(theta) + 1j*math.sin(theta)}")
    
    # 计算复数的自然对数
    z = 1 + 0j
    print(f"\nln(1) = {cmath.log(z)}")
    
    z = -1 + 0j
    print(f"ln(-1) = {cmath.log(z)}")
    
    z = 1j
    print(f"ln(1j) = {cmath.log(z)}")

complex_exponential_and_logarithm()

# 示例3：复数的三角函数恒等式
def complex_trigonometric_identities():
    """验证复数的三角函数恒等式"""
    z = 1 + 1j
    
    # sin²(z) + cos²(z) = 1
    result = cmath.sin(z)**2 + cmath.cos(z)**2
    print(f"\n三角函数恒等式验证:")
    print(f"sin²(z) + cos²(z) = {result}")
    print(f"是否等于1: {cmath.isclose(result, 1+0j)}")
    
    # sinh(z) = -i sin(iz)
    lhs = cmath.sinh(z)
    rhs = -1j * cmath.sin(1j * z)
    print(f"\nsinh(z) = -i sin(iz):")
    print(f"左边: {lhs}")
    print(f"右边: {rhs}")
    print(f"是否相等: {cmath.isclose(lhs, rhs)}")

complex_trigonometric_identities()

# 12. 与math模块的比较
print("\n=== 12. 与math模块的比较 ===")
print("cmath模块与math模块的功能相似，但有以下主要区别：")
print("1. cmath模块支持复数运算，而math模块只支持实数运算")
print("2. cmath模块提供了处理复数特有的函数（如phase、rect等）")
print("3. cmath模块的函数可以接受复数参数，也可以接受实数参数")
print("4. math模块在遇到复数参数时会抛出TypeError，而cmath不会")

# 示例比较
print(f"\n示例比较:")
try:
    print(f"math.sqrt(-1) = {math.sqrt(-1)}")
except Exception as e:
    print(f"math.sqrt(-1) 抛出异常: {e}")
    
print(f"cmath.sqrt(-1) = {cmath.sqrt(-1)}")

# 13. 最佳实践
print("\n=== 13. 最佳实践 ===")
print("1. 使用cmath模块进行复数运算，而不是手动实现")
print("2. 注意复数的多值性（如平方根有两个值）")
print("3. 使用cmath.isclose()来比较复数是否接近")
print("4. 对于极坐标表示，使用cmath.phase()和cmath.rect()")
print("5. 注意无穷大和非数字的处理")

# 示例：比较复数
z1 = 0.1 + 0.2j
z2 = 0.3 + 0.0j
print(f"\n示例：比较复数")
print(f"z1 = {z1}")
print(f"z2 = {z2}")
print(f"直接比较 z1 == z2: {z1 == z2}")
print(f"使用cmath.isclose(z1, z2): {cmath.isclose(z1, z2, rel_tol=1e-9)}")

# 14. 应用场景
print("\n=== 14. 应用场景 ===")
print("cmath模块在以下场景中特别有用：")
print("1. 信号处理和傅里叶变换")
print("2. 控制系统分析")
print("3. 量子力学和物理模拟")
print("4. 电气工程（交流电路分析）")
print("5. 复变函数计算")
print("6. 数值分析和科学计算")

# 15. 总结
print("\n=== 15. cmath模块总结 ===")
print("cmath模块提供了全面的复数运算功能，是Python中处理复数的标准库。")
print("主要特点：")
print("- 功能全面：涵盖了复数的基本运算到高级函数")
print("- 与math模块接口一致：易于学习和使用")
print("- 支持极坐标和直角坐标表示之间的转换")
print("- 提供了复数特有的分类函数")
print()
print("使用cmath模块可以方便地进行各种复数运算，避免了手动实现的复杂性和潜在错误。")
print("对于需要处理复数的科学计算和工程应用，cmath模块是不可或缺的工具。")
