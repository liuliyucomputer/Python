# math模块 - 数学函数库
# 功能作用：提供数学常数和各种数学函数（如三角函数、对数函数等）的实现
# 使用情景：科学计算、数据分析、图形处理、金融计算等需要数学运算的场景
# 注意事项：math模块只处理实数，复数相关运算应使用cmath模块；函数参数和返回值通常是浮点数

import math

# 模块概述
"""
math模块提供了许多对浮点数进行数学运算的函数。它包括：

1. 数学常量：如π、e等
2. 基本数学函数：如绝对值、幂、平方根等
3. 三角函数：如sin、cos、tan等
4. 双曲函数：如sinh、cosh、tanh等
5. 对数和指数函数：如log、log10、exp等
6. 特殊函数：如gamma、erf等
7. 取整函数：如ceil、floor、trunc等

math模块中的函数通常比使用Python内置运算符实现的相同功能更快，因为它们是用C语言实现的。
所有函数都适用于浮点数，对于整数参数，它们会自动转换为浮点数再进行计算。
"""

# 1. 数学常量
print("=== 1. 数学常量 ===")

# 基本数学常量
def mathematical_constants():
    """数学常量示例"""
    print("Python math模块中的数学常量:")
    
    # π (圆周率)
    print(f"math.pi = {math.pi}")
    print(f"π的近似值: {math.pi:.15f}")
    print(f"2π = {2 * math.pi:.15f}")
    print(f"π/2 = {math.pi / 2:.15f}")
    print()
    
    # e (自然对数的底数)
    print(f"math.e = {math.e}")
    print(f"e的近似值: {math.e:.15f}")
    print()
    
    # 无穷大和NaN (非数字)
    print(f"math.inf = {math.inf}")  # 正无穷大
    print(f"-math.inf = {-math.inf}")  # 负无穷大
    print(f"math.nan = {math.nan}")  # 非数字
    print(f"math.isinf(math.inf) = {math.isinf(math.inf)}")  # 检查是否为无穷大
    print(f"math.isnan(math.nan) = {math.isnan(math.nan)}")  # 检查是否为NaN
    print(f"math.isnan(10) = {math.isnan(10)}")  # 检查非NaN值
    print()
    
    # τ (tau, 2π的别名)
    print(f"math.tau = {math.tau}")
    print(f"tau与2π的关系: {math.tau} == {2 * math.pi}")
    print(f"math.tau == 2 * math.pi: {math.tau == 2 * math.pi}")
    print()
    
    # φ (黄金比例，(1+√5)/2)
    print(f"math.sqrt(5) = {math.sqrt(5)}")
    phi = (1 + math.sqrt(5)) / 2
    print(f"黄金比例 φ = {(1 + math.sqrt(5)) / 2:.15f}")
    
# 运行数学常量示例
mathematical_constants()
print()

# 2. 基本数学函数
print("=== 2. 基本数学函数 ===")

def basic_math_functions():
    """基本数学函数示例"""
    print("基本数学函数:")
    
    # 绝对值
    print(f"math.fabs(-10) = {math.fabs(-10)}")  # 注意：返回浮点数
    print(f"abs(-10) = {abs(-10)}")  # 内置函数，返回整数
    print(f"math.fabs(-3.14) = {math.fabs(-3.14)}")
    print()
    
    # 幂和指数
    print(f"math.pow(2, 3) = {math.pow(2, 3)}")  # 2^3
    print(f"2 ** 3 = {2 ** 3}")  # Python运算符
    print(f"math.pow(2, 0.5) = {math.pow(2, 0.5)}")  # 2的平方根
    print(f"math.pow(10, -1) = {math.pow(10, -1)}")  # 10的-1次方
    print()
    
    # 平方根
    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"math.sqrt(2) = {math.sqrt(2):.15f}")
    print(f"math.isqrt(16) = {math.isqrt(16)}")  # 返回整数平方根
    print(f"math.isqrt(17) = {math.isqrt(17)}")  # 向下取整
    print()
    
    # 立方根
    print(f"math.cbrt(8) = {math.cbrt(8)}")  # 8的立方根
    print(f"math.cbrt(-27) = {math.cbrt(-27)}")  # -27的立方根
    print()
    
    # 超根（任意次根）
    def nth_root(x, n):
        """计算x的n次方根"""
        if n == 0:
            raise ValueError("根指数不能为零")
        if x < 0 and n % 2 == 0:
            raise ValueError("负数不能开偶次方根")
        return math.pow(x, 1/n)
    
    print(f"nth_root(16, 4) = {nth_root(16, 4)}")  # 16的4次方根
    print(f"nth_root(-32, 5) = {nth_root(-32, 5)}")  # -32的5次方根
    print()
    
    # 最大公约数(GCD)
    print(f"math.gcd(12, 18) = {math.gcd(12, 18)}")
    print(f"math.gcd(0, 5) = {math.gcd(0, 5)}")  # gcd(0, x) = x
    print(f"math.gcd(5, 0) = {math.gcd(5, 0)}")  # gcd(x, 0) = x
    print(f"math.gcd(-12, 18) = {math.gcd(-12, 18)}")  # 绝对值
    print()
    
    # 最小公倍数(LCM)
    def lcm(a, b):
        """计算最小公倍数"""
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // math.gcd(a, b)
    
    print(f"lcm(12, 18) = {lcm(12, 18)}")
    print(f"lcm(7, 13) = {lcm(7, 13)}")
    print(f"lcm(0, 5) = {lcm(0, 5)}")
    print()
    
    # 四舍五入
    print(f"math.ceil(4.2) = {math.ceil(4.2)}")  # 向上取整
    print(f"math.ceil(-4.2) = {math.ceil(-4.2)}")
    print(f"math.floor(4.8) = {math.floor(4.8)}")  # 向下取整
    print(f"math.floor(-4.8) = {math.floor(-4.8)}")
    print(f"math.trunc(4.8) = {math.trunc(4.8)}")  # 截断小数部分
    print(f"math.trunc(-4.8) = {math.trunc(-4.8)}")
    print(f"round(4.5) = {round(4.5)}")  # Python内置四舍五入
    print(f"round(5.5) = {round(5.5)}")  # 注意银行家舍入法

# 运行基本数学函数示例
basic_math_functions()
print()

# 3. 三角函数
print("=== 3. 三角函数 ===")

def trigonometric_functions():
    """三角函数示例"""
    print("三角函数示例:")
    
    # 角度转弧度
    def degrees_to_radians(degrees):
        """将角度转换为弧度"""
        return degrees * math.pi / 180
    
    # 弧度转角度
    def radians_to_degrees(radians):
        """将弧度转换为角度"""
        return radians * 180 / math.pi
    
    # 测试角度和弧度转换
    angles = [0, 30, 45, 60, 90, 180, 270, 360]
    print("角度转弧度:")
    for angle in angles:
        rad = degrees_to_radians(angle)
        print(f"{angle}度 = {rad:.10f}弧度")
    print()
    
    # 使用math模块的转换函数
    print("使用math模块函数转换:")
    print(f"math.radians(90) = {math.radians(90)}")
    print(f"math.degrees(math.pi/2) = {math.degrees(math.pi/2)}")
    print()
    
    # 基本三角函数
    print("基本三角函数值:")
    test_radians = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi]
    
    for rad in test_radians:
        deg = math.degrees(rad)
        print(f"角度: {deg}度, 弧度: {rad:.6f}")
        print(f"  sin({deg}°) = {math.sin(rad):.10f}")
        print(f"  cos({deg}°) = {math.cos(rad):.10f}")
        print(f"  tan({deg}°) = ", end="")
        try:
            print(f"{math.tan(rad):.10f}")
        except ValueError:
            print("未定义")
        print()
    
    # 反三角函数
    print("反三角函数:")
    test_values = [0, 0.5, math.sqrt(2)/2, math.sqrt(3)/2, 1, -1]
    
    for val in test_values:
        try:
            asin_val = math.asin(val)
            print(f"math.asin({val}) = {asin_val:.10f} 弧度 ({math.degrees(asin_val):.2f}度)")
        except ValueError:
            print(f"math.asin({val}) = 值域错误")
    print()
    
    for val in test_values:
        try:
            acos_val = math.acos(val)
            print(f"math.acos({val}) = {acos_val:.10f} 弧度 ({math.degrees(acos_val):.2f}度)")
        except ValueError:
            print(f"math.acos({val}) = 值域错误")
    print()
    
    test_values_tan = [-10, -1, 0, 1, 10]
    for val in test_values_tan:
        atan_val = math.atan(val)
        print(f"math.atan({val}) = {atan_val:.10f} 弧度 ({math.degrees(atan_val):.2f}度)")
    print()
    
    # math.atan2(y, x) 返回atan(y/x)，但可以确定象限
    print("math.atan2(y, x)函数:")
    points = [(1, 1), (1, -1), (-1, -1), (-1, 1), (0, 1), (1, 0)]
    
    for y, x in points:
        angle = math.atan2(y, x)
        print(f"math.atan2({y}, {x}) = {angle:.10f} 弧度 ({math.degrees(angle):.2f}度)")
    print()
    
    # 验证三角恒等式
    print("验证三角恒等式:")
    x = math.pi / 4  # 45度
    sin_sq_plus_cos_sq = math.sin(x)**2 + math.cos(x)**2
    print(f"sin²({math.degrees(x)}°) + cos²({math.degrees(x)}°) = {sin_sq_plus_cos_sq}")
    print(f"是否等于1? {abs(sin_sq_plus_cos_sq - 1) < 1e-10}")

# 运行三角函数示例
trigonometric_functions()
print()

# 4. 双曲函数
print("=== 4. 双曲函数 ===")

def hyperbolic_functions():
    """双曲函数示例"""
    print("双曲函数示例:")
    
    # 基本双曲函数
    print("基本双曲函数:")
    x_values = [-2, -1, 0, 1, 2]
    
    for x in x_values:
        print(f"x = {x}:")
        print(f"  sinh({x}) = {math.sinh(x):.10f}")
        print(f"  cosh({x}) = {math.cosh(x):.10f}")
        print(f"  tanh({x}) = {math.tanh(x):.10f}")
        print()
    
    # 反双曲函数
    print("反双曲函数:")
    for x in x_values:
        print(f"x = {x}:")
        try:
            print(f"  asinh({x}) = {math.asinh(x):.10f}")
        except ValueError:
            print(f"  asinh({x}) = 值域错误")
        
        try:
            print(f"  acosh({x}) = {math.acosh(x):.10f}")
        except ValueError:
            print(f"  acosh({x}) = 值域错误")
        
        try:
            print(f"  atanh({x}) = {math.atanh(x):.10f}")
        except ValueError:
            print(f"  atanh({x}) = 值域错误")
        print()
    
    # 验证双曲恒等式
    print("验证双曲恒等式:")
    x = 1.5
    cosh_sq_minus_sinh_sq = math.cosh(x)**2 - math.sinh(x)**2
    print(f"cosh²({x}) - sinh²({x}) = {cosh_sq_minus_sinh_sq}")
    print(f"是否等于1? {abs(cosh_sq_minus_sinh_sq - 1) < 1e-10}")

# 运行双曲函数示例
hyperbolic_functions()
print()

# 5. 对数和指数函数
print("=== 5. 对数和指数函数 ===")

def logarithmic_exponential_functions():
    """对数和指数函数示例"""
    print("对数和指数函数:")
    
    # 指数函数
    print("指数函数:")
    x_values = [-1, 0, 1, 2]
    
    for x in x_values:
        print(f"math.exp({x}) = {math.exp(x):.10f}")
    
    # math.e的幂
    print(f"math.exp(1) = {math.exp(1):.10f} (应该等于math.e = {math.e:.10f})")
    print(f"math.e ** 2 = {math.e ** 2:.10f}, math.exp(2) = {math.exp(2):.10f}")
    print()
    
    # 自然对数
    print("自然对数(以e为底):")
    x_values = [0.5, 1, math.e, 10]
    
    for x in x_values:
        try:
            print(f"math.log({x}) = {math.log(x):.10f}")
        except ValueError:
            print(f"math.log({x}) = 错误（参数必须为正数）")
    print()
    
    # 以10为底的对数
    print("以10为底的对数:")
    x_values = [0.1, 1, 10, 100, 1000]
    
    for x in x_values:
        try:
            print(f"math.log10({x}) = {math.log10(x):.10f}")
        except ValueError:
            print(f"math.log10({x}) = 错误")
    print()
    
    # 以2为底的对数
    print("以2为底的对数:")
    x_values = [0.5, 1, 2, 4, 8]
    
    for x in x_values:
        try:
            print(f"math.log2({x}) = {math.log2(x):.10f}")
        except ValueError:
            print(f"math.log2({x}) = 错误")
    print()
    
    # 任意底的对数
    print("任意底的对数:")
    def log_base(x, base):
        """计算以base为底的x的对数"""
        return math.log(x) / math.log(base)
    
    test_cases = [(8, 2), (100, 10), (16, 4), (27, 3)]
    
    for x, base in test_cases:
        result = log_base(x, base)
        print(f"log_{base}({x}) = {result:.10f}")
        # 验证结果
        verification = base ** result
        print(f"  验证: {base}^{result:.10f} = {verification:.10f} (应该接近{x})")
    print()
    
    # 对数加法公式验证
    print("对数加法公式验证:")
    a, b = 3, 4
    log_a_plus_log_b = math.log(a) + math.log(b)
    log_a_times_b = math.log(a * b)
    print(f"log({a}) + log({b}) = {log_a_plus_log_b:.10f}")
    print(f"log({a} * {b}) = {log_a_times_b:.10f}")
    print(f"两者相等? {abs(log_a_plus_log_b - log_a_times_b) < 1e-10}")

# 运行对数和指数函数示例
logarithmic_exponential_functions()
print()

# 6. 特殊函数
print("=== 6. 特殊函数 ===")

def special_functions():
    """特殊数学函数示例"""
    print("特殊数学函数:")
    
    # gamma函数
    print("Gamma函数:")
    x_values = [0.5, 1, 2, 3, 4, 5]
    
    for x in x_values:
        try:
            gamma_val = math.gamma(x)
            print(f"math.gamma({x}) = {gamma_val:.10f}")
            
            # 对于正整数n，gamma(n) = (n-1)!
            if x == int(x) and x > 0:
                factorial_val = math.factorial(int(x) - 1)
                print(f"  (验证: ({x}-1)! = {factorial_val})")
        except ValueError:
            print(f"math.gamma({x}) = 错误")
    print()
    
    # beta函数
    def beta(x, y):
        """Beta函数: B(x,y) = gamma(x) * gamma(y) / gamma(x+y)"""
        return math.gamma(x) * math.gamma(y) / math.gamma(x + y)
    
    print("Beta函数:")
    test_cases = [(0.5, 0.5), (1, 1), (2, 3)]
    
    for x, y in test_cases:
        try:
            beta_val = beta(x, y)
            print(f"B({x}, {y}) = {beta_val:.10f}")
        except ValueError:
            print(f"B({x}, {y}) = 错误")
    print()
    
    # 误差函数和互补误差函数
    print("误差函数和互补误差函数:")
    x_values = [-2, -1, 0, 1, 2]
    
    for x in x_values:
        erf_val = math.erf(x)
        erfc_val = math.erfc(x)
        print(f"x = {x}:")
        print(f"  math.erf({x}) = {erf_val:.10f}")
        print(f"  math.erfc({x}) = {erfc_val:.10f}")
        print(f"  erf + erfc = {erf_val + erfc_val:.10f} (应该等于1)")
        print()
    
    # 高斯误差函数的反函数
    print("高斯误差函数的反函数:")
    y_values = [-0.9, -0.5, 0, 0.5, 0.9]
    
    for y in y_values:
        try:
            erfinv_val = math.erfinv(y)
            print(f"math.erfinv({y}) = {erfinv_val:.10f}")
            # 验证
            erf_val = math.erf(erfinv_val)
            print(f"  验证: erf({erfinv_val:.10f}) = {erf_val:.10f} (应该接近{y})")
        except ValueError:
            print(f"math.erfinv({y}) = 错误")
    print()
    
    # 双曲误差函数的反函数
    print("双曲误差函数的反函数:")
    y_values = [-2, -1, 0, 1, 2]
    
    for y in y_values:
        try:
            erfcinv_val = math.erfcinv(y)
            print(f"math.erfcinv({y}) = {erfcinv_val:.10f}")
            # 验证
            erfc_val = math.erfc(erfcinv_val)
            print(f"  验证: erfc({erfcinv_val:.10f}) = {erfc_val:.10f} (应该接近{y})")
        except ValueError:
            print(f"math.erfcinv({y}) = 错误")

# 运行特殊函数示例
special_functions()
print()

# 7. 实际应用示例
print("=== 7. 实际应用示例 ===")

def practical_applications():
    """实际应用示例"""
    
    # 示例1: 计算圆的属性
    def circle_properties(radius):
        """计算圆的周长和面积"""
        if radius <= 0:
            raise ValueError("半径必须为正数")
        
        circumference = 2 * math.pi * radius
        area = math.pi * radius ** 2
        
        return {
            'radius': radius,
            'circumference': circumference,
            'area': area
        }
    
    print("示例1: 计算圆的属性")
    radius = 5
    props = circle_properties(radius)
    print(f"半径: {props['radius']}")
    print(f"周长: {props['circumference']:.10f}")
    print(f"面积: {props['area']:.10f}")
    print()
    
    # 示例2: 计算三角形的面积（海伦公式）
    def triangle_area(a, b, c):
        """使用海伦公式计算三角形的面积"""
        # 检查是否可以构成三角形
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("边长必须为正数")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("给定的边长无法构成三角形")
        
        # 计算半周长
        s = (a + b + c) / 2
        
        # 应用海伦公式: 面积 = √[s(s-a)(s-b)(s-c)]
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        return area
    
    print("示例2: 三角形面积计算")
    triangle_sides = [(3, 4, 5), (5, 5, 5), (7, 8, 9)]
    
    for a, b, c in triangle_sides:
        try:
            area = triangle_area(a, b, c)
            print(f"三角形边长 {a}, {b}, {c} 的面积: {area:.10f}")
        except ValueError as e:
            print(f"边长 {a}, {b}, {c}: {e}")
    print()
    
    # 示例3: 计算复利
    def compound_interest(principal, rate, years, compounded_annually=12):
        """计算复利
        
        Args:
            principal: 本金
            rate: 年利率（小数形式）
            years: 年数
            compounded_annually: 每年复利次数
            
        Returns:
            最终金额
        """
        amount = principal * math.pow(1 + rate / compounded_annually, 
                                     compounded_annually * years)
        return amount
    
    print("示例3: 复利计算")
    principal = 1000
    rate = 0.05  # 5%
    years = 10
    
    # 不同复利频率
    compounding_options = [1, 2, 4, 12, 365]
    compounding_names = ["年复利", "半年复利", "季度复利", "月复利", "日复利"]
    
    for freq, name in zip(compounding_options, compounding_names):
        amount = compound_interest(principal, rate, years, freq)
        interest = amount - principal
        print(f"{name} ({freq}次/年):")
        print(f"  最终金额: {amount:.2f}")
        print(f"  利息收入: {interest:.2f}")
    print()
    
    # 示例4: 求解二次方程
    def quadratic_equation(a, b, c):
        """求解二次方程 ax² + bx + c = 0"""
        if a == 0:
            raise ValueError("这不是二次方程（a=0）")
        
        # 计算判别式
        discriminant = b**2 - 4*a*c
        
        if discriminant < 0:
            # 无实根
            return None
        elif discriminant == 0:
            # 一个实根
            x = -b / (2*a)
            return (x,)
        else:
            # 两个实根
            sqrt_d = math.sqrt(discriminant)
            x1 = (-b + sqrt_d) / (2*a)
            x2 = (-b - sqrt_d) / (2*a)
            return (x1, x2)
    
    print("示例4: 求解二次方程")
    equations = [
        (1, -3, 2),      # 两个实根: 1, 2
        (1, -2, 1),      # 一个实根: 1
        (1, 0, 1),       # 无实根
        (2, 5, -3)       # 两个实根
    ]
    
    for a, b, c in equations:
        print(f"方程 {a}x² + {b}x + {c} = 0 的解:")
        try:
            roots = quadratic_equation(a, b, c)
            if roots is None:
                print("  无实根")
            elif len(roots) == 1:
                print(f"  一个实根: {roots[0]:.10f}")
            else:
                print(f"  两个实根: {roots[0]:.10f}, {roots[1]:.10f}")
        except ValueError as e:
            print(f"  {e}")
    print()
    
    # 示例5: 角度和距离计算
    def calculate_distance(point1, point2):
        """计算两点之间的欧几里得距离"""
        x1, y1 = point1
        x2, y2 = point2
        
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def calculate_angle(point1, point2):
        """计算两点之间的角度（相对于x轴）"""
        x1, y1 = point1
        x2, y2 = point2
        
        dx = x2 - x1
        dy = y2 - y1
        
        # 使用math.atan2确保角度在正确的象限
        angle_rad = math.atan2(dy, dx)
        angle_deg = math.degrees(angle_rad)
        
        return angle_rad, angle_deg
    
    print("示例5: 几何计算 - 距离和角度")
    points = [
        [(0, 0), (3, 4)],
        [(1, 1), (4, 5)],
        [(5, 5), (5, 0)],
        [(0, 0), (-1, -1)]
    ]
    
    for p1, p2 in points:
        distance = calculate_distance(p1, p2)
        angle_rad, angle_deg = calculate_angle(p1, p2)
        print(f"点{p1}到点{p2}:")
        print(f"  距离: {distance:.10f}")
        print(f"  角度: {angle_rad:.10f} 弧度 ({angle_deg:.2f}度)")

# 运行实际应用示例
practical_applications()
print()

# 8. 浮点数精度和舍入问题
print("=== 8. 浮点数精度和舍入问题 ===")

def floating_point_precision():
    """浮点数精度和舍入问题"""
    print("浮点数精度和舍入问题:")
    
    # 浮点数精度问题
    print("\n1. 浮点数精度问题:")
    print(f"0.1 + 0.2 = {0.1 + 0.2}")
    print(f"0.1 + 0.2 == 0.3? {0.1 + 0.2 == 0.3}")
    print(f"精确表示: {0.1 + 0.2:.20f}")
    print(f"0.3的精确表示: {0.3:.20f}")
    print()
    
    # 如何正确比较浮点数
    print("\n2. 正确比较浮点数:")
    def almost_equal(a, b, epsilon=1e-10):
        """检查两个浮点数是否几乎相等"""
        return abs(a - b) < epsilon
    
    print(f"almost_equal(0.1 + 0.2, 0.3) = {almost_equal(0.1 + 0.2, 0.3)}")
    print(f"almost_equal(0.1 + 0.2, 0.3, epsilon=1e-15) = {almost_equal(0.1 + 0.2, 0.3, epsilon=1e-15)}")
    print()
    
    # 使用math.isclose()
    print("\n3. 使用math.isclose()函数:")
    print(f"math.isclose(0.1 + 0.2, 0.3) = {math.isclose(0.1 + 0.2, 0.3)}")
    print(f"math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9, abs_tol=0.0) = {math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9, abs_tol=0.0)}")
    print()
    
    # 舍入模式
    print("\n4. 舍入模式:")
    x = 2.5
    print(f"x = {x}")
    print(f"round(x) = {round(x)}")  # 注意银行家舍入法
    print(f"math.ceil(x) = {math.ceil(x)}")
    print(f"math.floor(x) = {math.floor(x)}")
    print(f"math.trunc(x) = {math.trunc(x)}")
    print()
    
    x = 3.5
    print(f"x = {x}")
    print(f"round(x) = {round(x)}")  # 银行家舍入法
    print(f"math.ceil(x) = {math.ceil(x)}")
    print(f"math.floor(x) = {math.floor(x)}")
    print(f"math.trunc(x) = {math.trunc(x)}")
    print()
    
    # 格式化输出以控制精度
    print("\n5. 格式化输出以控制精度:")
    pi = math.pi
    print(f"pi = {pi}")
    print(f"pi 精确到2位小数: {pi:.2f}")
    print(f"pi 精确到5位小数: {pi:.5f}")
    print(f"pi 精确到10位小数: {pi:.10f}")
    print(f"pi 科学计数法: {pi:.3e}")

# 运行浮点数精度示例
floating_point_precision()
print()

# 9. 最佳实践和注意事项
print("=== 9. 最佳实践和注意事项 ===")

def best_practices():
    """math模块使用的最佳实践和注意事项"""
    
    print("math模块使用的最佳实践和注意事项:")
    
    # 1. 浮点数比较
    print("\n1. 浮点数比较:")
    print("   - 永远不要直接使用 == 比较浮点数")
    print("   - 使用math.isclose()或自定义epsilon比较")
    print("   - 对于金融计算，考虑使用decimal模块")
    
    # 2. 异常处理
    print("\n2. 异常处理:")
    print("   - 对数函数参数必须为正数")
    print("   - math.sqrt()的参数不能为负数")
    print("   - math.asin()和math.acos()的参数范围是[-1, 1]")
    print("   - 总是捕获可能的ValueError异常")
    
    # 3. 性能考虑
    print("\n3. 性能考虑:")
    print("   - math模块函数比Python实现的相同功能更快")
    print("   - 预先计算常用的常量值")
    print("   - 对于大量计算，考虑使用NumPy等库")
    
    # 4. 角度和弧度
    print("\n4. 角度和弧度:")
    print("   - math模块的三角函数使用弧度，不是角度")
    print("   - 始终使用math.radians()和math.degrees()进行转换")
    
    # 5. 复数运算
    print("\n5. 复数运算:")
    print("   - math模块只处理实数")
    print("   - 对于复数运算，使用cmath模块")
    
    # 6. 代码示例：健壮的数学函数
    print("\n6. 健壮的数学函数示例:")
    print("""
    def safe_sqrt(x, default=None):
        """安全的平方根计算"""
        try:
            return math.sqrt(x)
        except ValueError:
            if default is not None:
                return default
            raise ValueError(f"无法计算负数的平方根: {x}")
    
    def safe_log(x, base=None, default=None):
        """安全的对数计算"""
        try:
            if base is None:
                return math.log(x)
            else:
                return math.log(x) / math.log(base)
        except (ValueError, ZeroDivisionError):
            if default is not None:
                return default
            raise ValueError(f"无法计算log({x}){'' if base is None else f'以{base}为底'}")
    
    def robust_calculation(values, operation):
        """健壮的计算，处理异常值"""
        results = []
        errors = []
        
        for i, val in enumerate(values):
            try:
                if operation == 'sqrt':
                    results.append(math.sqrt(val))
                elif operation == 'log':
                    results.append(math.log(val))
                elif operation == 'exp':
                    results.append(math.exp(val))
                else:
                    raise ValueError(f"未知操作: {operation}")
            except Exception as e:
                results.append(None)
                errors.append((i, val, str(e)))
        
        return results, errors
    """)

# 运行最佳实践示例
best_practices()

# 总结
print("\n=== 总结 ===")
print("math模块是Python中进行数学计算的核心库，提供了丰富的数学函数和常量。")
print("主要功能和优势包括：")
print("1. 提供基本数学运算函数：幂、平方根、绝对值等")
print("2. 包含完整的三角函数和双曲函数")
print("3. 提供各种对数和指数函数")
print("4. 包含特殊数学函数如gamma函数、误差函数等")
print("5. 定义常用数学常量：pi、e等")
print("6. 提供浮点数比较和分类函数")
print()
print("在使用math模块时，需要注意浮点数精度问题、异常处理和性能优化。")
print("对于复杂的数学计算或大量数据处理，可以考虑结合NumPy等专门的科学计算库。")
print()
print("掌握math模块的使用对于科学计算、数据分析、图形处理等领域的Python编程至关重要。")

# 运行完整演示
if __name__ == "__main__":
    print("Python math模块演示\n")
    print("请参考源代码中的详细示例和说明")