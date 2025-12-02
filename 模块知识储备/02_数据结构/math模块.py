# Python math模块详解

# 1. math模块概述
print("=== 1. math模块概述 ===")
print("math模块提供了各种数学函数，包括三角函数、对数函数、指数函数等。")
print("这些函数适用于浮点数运算，提供了高精度的数学计算能力。")
print("math模块中的函数不支持复数运算，如果需要复数运算，应使用cmath模块。")
print()

# 2. 常量
print("=== 2. math模块中的常量 ===")
def math_constants():
    """展示math模块中定义的数学常量"""
    import math
    
    print(f"math.pi = {math.pi}")  # π = 3.141592653589793
    print(f"math.e = {math.e}")    # 自然对数的底，e = 2.718281828459045
    print(f"math.tau = {math.tau}")  # τ = 2π = 6.283185307179586
    print(f"math.inf = {math.inf}")  # 正无穷大
    print(f"math.nan = {math.nan}")  # 非数字(Not a Number)
    print(f"-math.inf = {-math.inf}")  # 负无穷大
    
    # 验证无穷大和NaN的特性
    print(f"\n无穷大特性:")
    print(f"math.isinf(math.inf) = {math.isinf(math.inf)}")
    print(f"math.isinf(-math.inf) = {math.isinf(-math.inf)}")
    print(f"math.isinf(10) = {math.isinf(10)}")
    
    print(f"\nNaN特性:")
    print(f"math.isnan(math.nan) = {math.isnan(math.nan)}")
    print(f"math.isnan(10) = {math.isnan(10)}")
    print(f"math.nan == math.nan = {math.nan == math.nan}")  # NaN不等于任何值，包括自身

math_constants()
print()

# 3. 基本运算函数
print("=== 3. 基本运算函数 ===")
def math_basic_operations():
    """展示基本的数学运算函数"""
    import math
    
    # 绝对值
    print(f"math.fabs(-10.5) = {math.fabs(-10.5)}")  # 返回浮点数绝对值
    print(f"abs(-10.5) = {abs(-10.5)}")  # Python内置的abs可以处理整数和浮点数
    
    # 取整函数
    print(f"\n取整函数:")
    x = 3.7
    print(f"x = {x}")
    print(f"math.ceil(x) = {math.ceil(x)}")  # 向上取整
    print(f"math.floor(x) = {math.floor(x)}")  # 向下取整
    print(f"math.trunc(x) = {math.trunc(x)}")  # 截断小数部分
    print(f"int(x) = {int(x)}")  # Python内置的int转换
    
    # 幂函数
    print(f"\n幂函数:")
    print(f"math.pow(2, 3) = {math.pow(2, 3)}")  # 2^3 = 8.0
    print(f"2 ** 3 = {2 ** 3}")  # Python内置的幂运算符
    print(f"math.pow(2, 0.5) = {math.pow(2, 0.5)}")  # 2的平方根
    
    # 平方根
    print(f"\n平方根:")
    print(f"math.sqrt(16) = {math.sqrt(16)}")  # 16的平方根 = 4.0
    print(f"math.isqrt(16) = {math.isqrt(16)}")  # 整数平方根，返回整数4
    
    # 立方根
    print(f"\n立方根:")
    print(f"math.pow(8, 1/3) = {math.pow(8, 1/3)}")  # 8的立方根
    print(f"math.cbrt(8) = {math.cbrt(8)}")  # 立方根函数(Python 3.10+)
    
    # 余数
    print(f"\n余数:")
    print(f"math.fmod(7, 3) = {math.fmod(7, 3)}")  # 浮点数余数
    print(f"7 % 3 = {7 % 3}")  # Python内置的余数运算符
    
    # 分解
    print(f"\n分解:")
    print(f"math.modf(3.7) = {math.modf(3.7)}")  # 返回(小数部分, 整数部分)
    
    # 精确计算
    print(f"\n精确计算:")
    print(f"math.fsum([0.1, 0.2, 0.3]) = {math.fsum([0.1, 0.2, 0.3])}")  # 精确求和
    print(f"0.1 + 0.2 + 0.3 = {0.1 + 0.2 + 0.3}")  # 浮点数舍入误差

math_basic_operations()
print()

# 4. 三角函数
print("=== 4. 三角函数 ===")
def math_trigonometric():
    """展示三角函数"""
    import math
    
    # 角度与弧度转换
    degrees = 45
    radians = math.radians(degrees)
    print(f"{degrees}度 = {radians}弧度")
    print(f"{radians}弧度 = {math.degrees(radians)}度")
    
    # 基本三角函数
    print(f"\n基本三角函数:")
    x = math.pi / 4  # 45度
    print(f"sin(π/4) = {math.sin(x)}")
    print(f"cos(π/4) = {math.cos(x)}")
    print(f"tan(π/4) = {math.tan(x)}")
    
    # 反三角函数
    print(f"\n反三角函数:")
    print(f"asin(0.5) = {math.asin(0.5)} 弧度 = {math.degrees(math.asin(0.5))} 度")
    print(f"acos(0.5) = {math.acos(0.5)} 弧度 = {math.degrees(math.acos(0.5))} 度")
    print(f"atan(1) = {math.atan(1)} 弧度 = {math.degrees(math.atan(1))} 度")
    print(f"atan2(1, 1) = {math.atan2(1, 1)} 弧度 = {math.degrees(math.atan2(1, 1))} 度")  # 更精确的反正切
    
    # 双曲函数
    print(f"\n双曲函数:")
    x = 1.0
    print(f"sinh(1) = {math.sinh(x)}")
    print(f"cosh(1) = {math.cosh(x)}")
    print(f"tanh(1) = {math.tanh(x)}")
    
    # 反双曲函数
    print(f"\n反双曲函数:")
    print(f"asinh(1) = {math.asinh(1)}")
    print(f"acosh(2) = {math.acosh(2)}")
    print(f"atanh(0.5) = {math.atanh(0.5)}")

math_trigonometric()
print()

# 5. 对数函数
print("=== 5. 对数函数 ===")
def math_logarithmic():
    """展示对数函数"""
    import math
    
    # 自然对数
    print(f"ln(e) = {math.log(math.e)}")
    print(f"ln(1) = {math.log(1)}")
    print(f"ln(10) = {math.log(10)}")
    
    # 以10为底的对数
    print(f"\nlog10(10) = {math.log10(10)}")
    print(f"log10(100) = {math.log10(100)}")
    print(f"log10(0.1) = {math.log10(0.1)}")
    
    # 以2为底的对数
    print(f"\nlog2(2) = {math.log2(2)}")
    print(f"log2(8) = {math.log2(8)}")
    print(f"log2(0.5) = {math.log2(0.5)}")
    
    # 任意底数的对数
    print(f"\nlog(16, 2) = {math.log(16, 2)}")  # 以2为底16的对数
    print(f"log(81, 3) = {math.log(81, 3)}")  # 以3为底81的对数
    
    # 自然对数的变体
    print(f"\nlog1p(0) = {math.log1p(0)}")  # log(1+x)，精确计算接近0的值
    print(f"log1p(1) = {math.log1p(1)}")
    
    # 指数函数变体
    print(f"\nexp(1) = {math.exp(1)}")  # e^1
    print(f"exp(0) = {math.exp(0)}")  # e^0
    print(f"expm1(0) = {math.expm1(0)}")  # exp(x) - 1，精确计算接近0的值
    print(f"expm1(1) = {math.expm1(1)}")

math_logarithmic()
print()

# 6. 特殊函数
print("=== 6. 特殊函数 ===")
def math_special_functions():
    """展示特殊数学函数"""
    import math
    
    # 阶乘
    print(f"5! = {math.factorial(5)}")
    print(f"0! = {math.factorial(0)}")
    
    # gamma函数
    print(f"\ngamma(5) = {math.gamma(5)}")  # gamma(n) = (n-1)!
    print(f"gamma(0.5) = {math.gamma(0.5)}")  # √π
    
    # 误差函数
    print(f"\nerf(0) = {math.erf(0)}")
    print(f"erf(1) = {math.erf(1)}")
    print(f"erfc(0) = {math.erfc(0)}")  # 1 - erf(x)
    
    # 贝塞尔函数
    print(f"\nj0(0) = {math.j0(0)}")  # 0阶贝塞尔函数
    print(f"j1(0) = {math.j1(0)}")  # 1阶贝塞尔函数
    print(f"y0(1) = {math.y0(1)}")  # 0阶第二类贝塞尔函数
    print(f"y1(1) = {math.y1(1)}")  # 1阶第二类贝塞尔函数
    
    # 海维赛德阶跃函数
    print(f"\nheaviside(0, 0.5) = {math.heaviside(0, 0.5)}")  # x=0时返回0.5
    print(f"heaviside(1, 0.5) = {math.heaviside(1, 0.5)}")  # x>0时返回1
    print(f"heaviside(-1, 0.5) = {math.heaviside(-1, 0.5)}")  # x<0时返回0

math_special_functions()
print()

# 7. 实用工具函数
print("=== 7. 实用工具函数 ===")
def math_utilities():
    """展示实用工具函数"""
    import math
    
    # 最大公约数
    print(f"gcd(42, 56) = {math.gcd(42, 56)}")
    
    # 最小公倍数
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b) if a and b else 0
    
    print(f"lcm(12, 18) = {lcm(12, 18)}")
    print(f"math.lcm(12, 18) = {math.lcm(12, 18)}")  # Python 3.9+
    
    # 度分秒转换
    print(f"\ndms(0.75)度 = {math.degrees(math.radians(0.75))}度")
    
    # 检查浮点数关系
    print(f"\n浮点数关系检查:")
    print(f"isclose(1.0, 1.0000001) = {math.isclose(1.0, 1.0000001)}")
    print(f"isclose(1.0, 1.1) = {math.isclose(1.0, 1.1)}")
    
    # 符号函数
    print(f"\n符号函数:")
    print(f"copysign(1, 5) = {math.copysign(1, 5)}")  # 复制符号
    print(f"copysign(1, -5) = {math.copysign(1, -5)}")
    print(f"signbit(-5) = {math.signbit(-5)}")  # 检查符号位
    print(f"signbit(5) = {math.signbit(5)}")
    
    # 距离计算
    print(f"\n距离计算:")
    def distance(p1, p2):
        return math.hypot(p2[0] - p1[0], p2[1] - p1[1])
    
    p1 = (1, 2)
    p2 = (4, 6)
    print(f"两点{str(p1)}和{str(p2)}之间的距离: {distance(p1, p2)}")

math_utilities()
print()

# 8. 高级应用示例
print("=== 8. 高级应用示例 ===")
def math_advanced_examples():
    """展示math模块的高级应用示例"""
    import math
    
    print("1. 计算圆的周长和面积:")
    def circle_properties(radius):
        circumference = 2 * math.pi * radius
        area = math.pi * radius ** 2
        return circumference, area
    
    radius = 5
    circumference, area = circle_properties(radius)
    print(f"半径为{radius}的圆:")
    print(f"  周长: {circumference:.2f}")
    print(f"  面积: {area:.2f}")
    
    print("\n2. 计算三角形的面积(海伦公式):")
    def triangle_area(a, b, c):
        # 检查三角形是否有效
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("无效的三角形边长")
        
        # 半周长
        s = (a + b + c) / 2
        # 海伦公式
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
    try:
        a, b, c = 3, 4, 5
        area = triangle_area(a, b, c)
        print(f"边长为{a}, {b}, {c}的三角形面积: {area:.2f}")
    except ValueError as e:
        print(f"错误: {e}")
    
    print("\n3. 计算向量的长度和方向:")
    def vector_properties(x, y):
        # 向量长度
        length = math.hypot(x, y)
        # 向量方向(弧度)
        direction = math.atan2(y, x)
        # 转换为角度
        direction_deg = math.degrees(direction)
        return length, direction, direction_deg
    
    x, y = 3, 4
    length, direction, direction_deg = vector_properties(x, y)
    print(f"向量({x}, {y}):")
    print(f"  长度: {length:.2f}")
    print(f"  方向: {direction:.4f} 弧度 = {direction_deg:.2f} 度")
    
    print("\n4. 计算复利:")
    def compound_interest(principal, rate, years, compounds_per_year):
        # 复利公式: A = P(1 + r/n)^(nt)
        amount = principal * math.pow(1 + rate / compounds_per_year, compounds_per_year * years)
        interest = amount - principal
        return amount, interest
    
    principal = 1000  # 本金
    rate = 0.05  # 年利率
    years = 10  # 年数
    compounds_per_year = 12  # 每年复利次数
    
    amount, interest = compound_interest(principal, rate, years, compounds_per_year)
    print(f"本金: {principal}, 年利率: {rate:.1%}, 年数: {years}, 每年复利: {compounds_per_year}次")
    print(f"  最终金额: {amount:.2f}")
    print(f"  利息收入: {interest:.2f}")
    
    print("\n5. 使用黄金分割法查找函数最小值:")
    def golden_section_search(f, a, b, tol=1e-6):
        # 黄金比例
        gr = (math.sqrt(5) + 1) / 2
        
        # 初始内部点
        c = b - (b - a) / gr
        d = a + (b - a) / gr
        
        # 计算函数值
        fc = f(c)
        fd = f(d)
        
        # 迭代查找最小值
        while abs(b - a) > tol:
            if fc < fd:
                b = d
                d = c
                fd = fc
                c = b - (b - a) / gr
                fc = f(c)
            else:
                a = c
                c = d
                fc = fd
                d = a + (b - a) / gr
                fd = f(d)
        
        return (a + b) / 2
    
    # 测试函数: f(x) = x^2
    f = lambda x: x**2
    min_x = golden_section_search(f, -2, 2)
    print(f"函数f(x) = x^2在区间[-2, 2]内的最小值点: x = {min_x:.6f}")
    print(f"最小值: f({min_x:.6f}) = {f(min_x):.6f}")

math_advanced_examples()
print()

# 9. 性能优化和注意事项
print("=== 9. 性能优化和注意事项 ===")
def math_performance_tips():
    """math模块的性能优化和注意事项"""
    print("1. 浮点数精度问题:")
    print("   - 浮点数计算存在精度限制，可能导致舍入误差")
    print("   - 使用math.isclose()而不是直接比较浮点数是否相等")
    print("   - 对于需要高精度计算的场景，考虑使用decimal模块")
    
    print("\n2. 计算效率:")
    print("   - math模块中的函数通常是用C实现的，比Python内置函数更快")
    print("   - 对于重复计算的常量值，应预先计算并缓存")
    print("   - 对于向量运算，考虑使用numpy库获得更好的性能")
    
    print("\n3. 异常处理:")
    print("   - 数学函数可能抛出ValueError或OverflowError等异常")
    print("   - 如math.log(0)、math.sqrt(-1)、math.gamma(-1)等会抛出错误")
    print("   - 在使用这些函数时应当进行适当的异常处理")
    
    print("\n4. 特殊值处理:")
    print("   - 了解如何处理math.inf和math.nan等特殊值")
    print("   - 使用math.isinf()和math.isnan()检查这些特殊值")
    print("   - 注意NaN不等于任何值，包括它自己")
    
    print("\n5. 复数计算:")
    print("   - math模块只支持实数运算")
    print("   - 对于复数计算，应使用cmath模块")
    
    print("\n6. Python版本差异:")
    print("   - 一些函数是在较新版本中添加的，如math.lcm()(Python 3.9+)")
    print("   - math.isqrt()(Python 3.8+)")
    print("   - math.cbrt()(Python 3.10+)")
    print("   - 在编写需要跨版本兼容的代码时要注意")

math_performance_tips()
print()

# 10. 输入输出示例
print("=== 10. 输入输出示例 ===")

def math_io_examples():
    """math模块的输入输出示例"""
    print("\n示例1: 基本数学运算")
    print("输入:")
    print("    import math")
    print("    print(f'π的近似值: {math.pi:.10f}')")
    print("    print(f'e的近似值: {math.e:.10f}')")
    print("    print(f'2的平方根: {math.sqrt(2):.10f}')")
    print("    print(f'10的自然对数: {math.log(10):.10f}')")
    print("    print(f'10的以10为底的对数: {math.log10(10):.10f}')")
    print("输出:")
    print("    π的近似值: 3.1415926536")
    print("    e的近似值: 2.7182818285")
    print("    2的平方根: 1.4142135624")
    print("    10的自然对数: 2.3025850930")
    print("    10的以10为底的对数: 1.0000000000")
    
    print("\n示例2: 三角函数计算")
    print("输入:")
    print("    import math")
    print("    angle_deg = 30")
    print("    angle_rad = math.radians(angle_deg)")
    print("    print(f'{angle_deg}度的正弦值: {math.sin(angle_rad):.10f}')")
    print("    print(f'{angle_deg}度的余弦值: {math.cos(angle_rad):.10f}')")
    print("    print(f'{angle_deg}度的正切值: {math.tan(angle_rad):.10f}')")
    print("    # 反三角函数示例")
    print("    sin_value = 0.5")
    print("    angle_rad = math.asin(sin_value)")
    print("    print(f'反正弦({sin_value}) = {math.degrees(angle_rad):.2f}度')")
    print("输出:")
    print("    30度的正弦值: 0.5000000000")
    print("    30度的余弦值: 0.8660254038")
    print("    30度的正切值: 0.5773502692")
    print("    反正弦(0.5) = 30.00度")
    
    print("\n示例3: 取整和余数运算")
    print("输入:")
    print("    import math")
    print("    x = 3.7")
    print("    print(f'x = {x}')")
    print("    print(f'向上取整: {math.ceil(x)}')")
    print("    print(f'向下取整: {math.floor(x)}')")
    print("    print(f'截断小数: {math.trunc(x)}')")
    print("    print(f'小数部分和整数部分: {math.modf(x)}')")
    print("    print(f'7除以3的浮点数余数: {math.fmod(7, 3)}')")
    print("输出:")
    print("    x = 3.7")
    print("    向上取整: 4")
    print("    向下取整: 3")
    print("    截断小数: 3")
    print("    小数部分和整数部分: (0.7, 3.0)")
    print("    7除以3的浮点数余数: 1.0")
    
    print("\n示例4: 精确计算")
    print("输入:")
    print("    import math")
    print("    values = [0.1, 0.2, 0.3]")
    print("    print(f'直接求和: {values[0] + values[1] + values[2]}')")
    print("    print(f'math.fsum求和: {math.fsum(values)}')")
    print("输出:")
    print("    直接求和: 0.6000000000000001")
    print("    math.fsum求和: 0.6")
    
    print("\n示例5: 检查浮点数关系")
    print("输入:")
    print("    import math")
    print("    a = 0.1 + 0.2")
    print("    b = 0.3")
    print("    print(f'a = {a}, b = {b}')")
    print("    print(f'a == b: {a == b}')")
    print("    print(f'math.isclose(a, b): {math.isclose(a, b)}')")
    print("    # 自定义容差")
    print("    print(f'math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0): {math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0)}')")
    print("输出:")
    print("    a = 0.30000000000000004, b = 0.3")
    print("    a == b: False")
    print("    math.isclose(a, b): True")
    print("    math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0): True")

math_io_examples()
print()

# 11. 总结和完整导入指南
print("=== 11. 总结和完整导入指南 ===")

def math_summary():
    """math模块总结和导入指南"""
    print("math模块是Python标准库中提供数学计算功能的模块，包含了各种基本和高级数学函数。\n")
    
    # 主要功能分类
    print("主要功能分类:")
    print("1. 数学常量: pi, e, tau, inf, nan")
    print("2. 基本运算: fabs, ceil, floor, trunc, pow, sqrt, isqrt, cbrt, fmod, modf, fsum")
    print("3. 三角函数: sin, cos, tan, asin, acos, atan, atan2, radians, degrees")
    print("4. 双曲函数: sinh, cosh, tanh, asinh, acosh, atanh")
    print("5. 对数函数: log, log10, log2, log1p, exp, expm1")
    print("6. 特殊函数: factorial, gamma, erf, erfc, j0, j1, y0, y1, heaviside")
    print("7. 实用工具: gcd, lcm, isclose, copysign, signbit, hypot\n")
    
    # 导入指南
    print("导入指南:")
    print("\n1. 导入整个模块:")
    print("   import math")
    print("   print(math.pi)")
    print("   print(math.sqrt(16))")
    
    print("\n2. 导入特定函数:")
    print("   from math import pi, sqrt, sin, cos")
    print("   print(pi)")
    print("   print(sqrt(16))")
    
    print("\n3. 导入并重命名:")
    print("   from math import pi as PI, sqrt as square_root")
    print("   print(PI)")
    print("   print(square_root(16))")
    
    # 版本兼容性
    print("\n版本兼容性:")
    print("- math模块在Python 2和Python 3中都可用，但有些函数是在较新版本中添加的")
    print("- Python 3.8新增函数: isqrt()")
    print("- Python 3.9新增函数: lcm(), gcd()参数允许0")
    print("- Python 3.10新增函数: cbrt()")
    print("- 对于需要在多个Python版本间兼容的代码，应检查函数是否可用或提供替代实现\n")
    
    # 最终建议
    print("最终建议:")
    print("- 对于浮点数计算，使用math模块中的函数获得更高的精度和性能")
    print("- 始终注意浮点数精度问题，避免直接比较浮点数是否相等")
    print("- 对于特殊值如inf和nan，使用专门的函数进行检测")
    print("- 对于复数运算，使用cmath模块而不是math模块")
    print("- 在性能关键的应用中，考虑预先计算和缓存常用的值")
    print("- 对于科学计算和向量运算，考虑使用numpy等专业库\n")
    
    print("math模块是Python中进行数学计算的基础工具，熟练掌握其功能可以让您的数值计算代码更加准确和高效。")

math_summary()

print("\n至此，math模块的全部功能已详细介绍完毕。")
