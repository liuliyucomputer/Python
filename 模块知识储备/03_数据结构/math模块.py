# math模块 - Python标准库中的数学函数库

'''
math模块提供了用于数学运算的各种函数，包括三角函数、对数函数、指数函数等，
这些函数大多是对C语言标准数学库函数的封装，性能优良且精度高。
'''

import math
from typing import Union, List, Tuple, Optional, Callable

# 核心功能介绍
print("=== math模块核心功能 ===")
print("math模块提供了以下核心功能：")
print("1. 基本数学运算 - 如求幂、平方根、绝对值等")
print("2. 三角函数 - 正弦、余弦、正切及其反函数")
print("3. 双曲函数 - 双曲正弦、双曲余弦、双曲正切等")
print("4. 指数和对数函数 - 自然对数、常用对数、指数函数等")
print("5. 特殊常量 - 如π、e等")
print("6. 浮点运算函数 - 如取整、余数、阶乘等")
print("7. 角度转换 - 弧度和角度之间的转换")

# 1. 数学常量
def show_math_constants():
    """展示math模块中的常量"""
    print("\n=== 1. 数学常量 ===")
    
    # 圆周率 π
    print(f"π (math.pi): {math.pi}")  # 圆周率
    
    # 自然对数的底数 e
    print(f"e (math.e): {math.e}")  # 自然对数的底数
    
    # 正无穷
    print(f"正无穷 (math.inf): {math.inf}")  # 正无穷大
    
    # 负无穷
    print(f"负无穷 (-math.inf): {-math.inf}")  # 负无穷大
    
    # 非数字
    print(f"非数字 (math.nan): {math.nan}")  # 非数字
    print(f"验证nan不等于自身: {math.nan != math.nan}")  # NaN不等于任何值，包括它自己
    
    # 验证无穷
    print(f"验证无穷: {math.isinf(math.inf)}")
    print(f"验证非数字: {math.isnan(math.nan)}")
    
    # 无穷常量的一些运算特性
    print(f"\n无穷常量的运算特性:")
    print(f"inf + 1 = {math.inf + 1}")
    print(f"inf * 0 = {math.inf * 0}")  # 结果是nan
    print(f"inf / inf = {math.inf / math.inf}")  # 结果是nan
    print(f"1 / 0 = {1 / 0 if 0 else None}")  # 在Python中，1/0会抛出ZeroDivisionError
    print(f"1 / 0.0 = {1 / 0.0}")  # 但1/0.0会得到inf
    
    # 使用这些常量的实际例子
    print("\n使用数学常量的例子:")
    # 计算圆的面积
    radius = 5
    area = math.pi * radius ** 2
    print(f"半径为{radius}的圆的面积: {area:.2f}")
    
    # 使用自然对数的底数
    x = 2
    result = math.e ** x
    print(f"e的{ x }次方: {result:.2f}")
    print(f"使用math.exp({x}): {math.exp(x):.2f}")  # math.exp更高效且精确

# 2. 基本数学函数
def show_basic_math_functions():
    """展示基本数学函数"""
    print("\n=== 2. 基本数学函数 ===")
    
    # 2.1 求幂和平方根
    print("\n2.1 求幂和平方根")
    
    # 求x的y次方
    x, y = 2, 3
    print(f"pow({x}, {y}) = {math.pow(x, y)}")  # 与x**y相似，但返回浮点数
    print(f"{x} ** {y} = {x ** y}")  # Python内置运算符
    
    # 计算平方根
    num = 16
    print(f"sqrt({num}) = {math.sqrt(num)}")
    print(f"{num} ** 0.5 = {num ** 0.5}")  # 等效但math.sqrt更高效
    
    # 计算立方根
    cube = 27
    print(f"{cube}的立方根: {cube ** (1/3):.6f}")
    
    # 2.2 绝对值
    print("\n2.2 绝对值")
    
    neg_num = -10
    print(f"abs({neg_num}) = {abs(neg_num)}")  # Python内置函数
    print(f"fabs({neg_num}) = {math.fabs(neg_num)}")  # math.fabs总是返回浮点数
    
    # 处理复数（注意math.fabs不能处理复数）
    # 对于复数，应使用内置的abs函数
    try:
        complex_num = 3 + 4j
        print(f"abs({complex_num}) = {abs(complex_num)}")
        # math.fabs(complex_num)  # 这会抛出TypeError
    except TypeError:
        print("math.fabs()不能处理复数")
    
    # 2.3 取整函数
    print("\n2.3 取整函数")
    
    float_num = 3.7
    print(f"原始浮点数: {float_num}")
    print(f"ceil({float_num}) = {math.ceil(float_num)}")  # 向上取整
    print(f"floor({float_num}) = {math.floor(float_num)}")  # 向下取整
    print(f"trunc({float_num}) = {math.trunc(float_num)}")  # 截断小数部分，向零取整
    print(f"int({float_num}) = {int(float_num)}")  # Python内置函数，截断小数部分
    print(f"round({float_num}) = {round(float_num)}")  # 四舍五入
    
    # 测试负数
    neg_float = -3.7
    print(f"\n原始负浮点数: {neg_float}")
    print(f"ceil({neg_float}) = {math.ceil(neg_float)}")
    print(f"floor({neg_float}) = {math.floor(neg_float)}")
    print(f"trunc({neg_float}) = {math.trunc(neg_float)}")
    print(f"int({neg_float}) = {int(neg_float)}")
    print(f"round({neg_float}) = {round(neg_float)}")
    
    # 2.4 余数和模运算
    print("\n2.4 余数和模运算")
    
    a, b = 10, 3
    print(f"{a} / {b} = {a / b}")  # 除法
    print(f"{a} // {b} = {a // b}")  # 整除
    print(f"{a} % {b} = {a % b}")  # 取余运算符
    print(f"fmod({a}, {b}) = {math.fmod(a, b)}")  # math.fmod函数
    
    # 处理负数的模运算（注意%和fmod的区别）
    a, b = -10, 3
    print(f"\n负数的模运算:")
    print(f"{a} % {b} = {a % b}")
    print(f"fmod({a}, {b}) = {math.fmod(a, b)}")
    
    # 2.5 阶乘和组合数
    print("\n2.5 阶乘和组合数")
    
    n = 5
    print(f"factorial({n}) = {math.factorial(n)}")  # 阶乘
    
    # 计算组合数 C(n, k) = n!/(k!(n-k)!)
    def combinations(n, k):
        if k < 0 or k > n:
            return 0
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
    
    n, k = 10, 3
    print(f"C({n}, {k}) = {combinations(n, k)}")
    
    # 2.6 最大公约数和最小公倍数
    print("\n2.6 最大公约数和最小公倍数")
    
    x, y = 48, 36
    # 最大公约数（GCD）
    print(f"gcd({x}, {y}) = {math.gcd(x, y)}")  # Python 3.5+ 才有math.gcd
    
    # 计算最小公倍数（LCM）
    def lcm(x, y):
        return abs(x * y) // math.gcd(x, y)
    
    print(f"lcm({x}, {y}) = {lcm(x, y)}")
    
    # 2.7 浮点数分解
    print("\n2.7 浮点数分解")
    
    float_value = 123.456
    # 将浮点数分解为尾数和指数（科学记数法）
    mantissa, exponent = math.frexp(float_value)
    print(f"frexp({float_value}) = ({mantissa}, {exponent})")
    print(f"验证: {mantissa} * 2 ** {exponent} = {mantissa * (2 ** exponent)}")
    
    # 构造浮点数
    constructed = math.ldexp(mantissa, exponent)
    print(f"ldexp({mantissa}, {exponent}) = {constructed}")
    
    # 2.8 比较浮点数
    print("\n2.8 比较浮点数")
    
    a, b = 0.1 + 0.2, 0.3
    print(f"a = 0.1 + 0.2 = {a}")
    print(f"b = 0.3 = {b}")
    print(f"a == b: {a == b}")  # 由于浮点数精度问题，可能不相等
    
    # 使用近似相等来比较浮点数
    epsilon = 1e-10
    print(f"近似相等 (|a - b| < {epsilon}): {abs(a - b) < epsilon}")

# 3. 三角函数
def show_trigonometric_functions():
    """展示三角函数"""
    print("\n=== 3. 三角函数 ===")
    print("注意：math模块中的三角函数接受的是弧度值")
    
    # 3.1 基本三角函数
    print("\n3.1 基本三角函数")
    
    # 定义一些常见角度的弧度值
    angles_rad = [0, math.pi/6, math.pi/4, math.pi/3, math.pi/2, math.pi]
    
    print("角度(度)  角度(弧度)     sin      cos      tan")
    print("-" * 60)
    
    for angle_rad in angles_rad:
        angle_deg = math.degrees(angle_rad)  # 转换为度数
        sin_val = math.sin(angle_rad)
        cos_val = math.cos(angle_rad)
        try:
            tan_val = math.tan(angle_rad)
        except ZeroDivisionError:
            tan_val = "inf"
        
        print(f"{angle_deg:9.1f} {angle_rad:12.6f} {sin_val:8.6f} {cos_val:8.6f} {tan_val}")
    
    # 3.2 反三角函数
    print("\n3.2 反三角函数")
    
    # 反三角函数示例
    values = [0, 0.5, math.sqrt(2)/2, math.sqrt(3)/2, 1]
    
    print("值         asin(弧度)   asin(度)    acos(弧度)   acos(度)    atan(弧度)   atan(度)")
    print("-" * 80)
    
    for val in values:
        asin_val = math.asin(val)
        acos_val = math.acos(val)
        atan_val = math.atan(val)
        
        print(f"{val:8.6f} {asin_val:11.6f} {math.degrees(asin_val):10.2f} "
              f"{acos_val:12.6f} {math.degrees(acos_val):10.2f} "
              f"{atan_val:12.6f} {math.degrees(atan_val):10.2f}")
    
    # atan2函数 - 给定x和y坐标，返回反正切值
    print("\n3.3 atan2函数")
    
    # 不同象限的点
    points = [(1, 1), (-1, 1), (-1, -1), (1, -1), (0, 1), (1, 0), (0, -1), (-1, 0)]
    
    print("点(x, y)   atan2(y, x)(弧度)  atan2(y, x)(度)")
    print("-" * 50)
    
    for x, y in points:
        angle_rad = math.atan2(y, x)
        angle_deg = math.degrees(angle_rad)
        print(f"({x}, {y})     {angle_rad:16.6f} {angle_deg:13.2f}")
    
    # 3.4 角度和弧度的转换
    print("\n3.4 角度和弧度的转换")
    
    # 一些常见角度
    degrees = [0, 30, 45, 60, 90, 180, 270, 360]
    
    print("角度(度)  弧度值")
    print("-" * 20)
    
    for deg in degrees:
        rad = math.radians(deg)
        print(f"{deg:9d} {rad:10.6f}")
    
    # 3.5 实际应用示例：计算三角形面积
    print("\n3.5 实际应用示例：计算三角形面积")
    
    # 使用余弦定理计算三角形面积
    def triangle_area(a, b, c):
        """使用海伦公式计算三角形面积，其中a, b, c是三角形的三边长"""
        # 检查三边是否能构成三角形
        if a + b <= c or a + c <= b or b + c <= a:
            return "无法构成三角形"
        
        # 海伦公式: s = (a + b + c) / 2, area = sqrt(s(s-a)(s-b)(s-c))
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area
    
    # 使用角度和边长计算三角形面积
    def triangle_area_angle(a, b, angle_deg):
        """已知两边和夹角，计算三角形面积"""
        angle_rad = math.radians(angle_deg)
        # 公式: 面积 = (1/2) * a * b * sin(C)
        area = 0.5 * a * b * math.sin(angle_rad)
        return area
    
    # 测试
    print("使用海伦公式:")
    print(f"边长为3, 4, 5的三角形面积: {triangle_area(3, 4, 5):.2f}")
    print(f"边长为5, 5, 5的等边三角形面积: {triangle_area(5, 5, 5):.2f}")
    print(f"边长为1, 1, 3的三角形: {triangle_area(1, 1, 3)}")
    
    print("\n使用两边和夹角:")
    print(f"边长为5和6，夹角为60度的三角形面积: {triangle_area_angle(5, 6, 60):.2f}")
    print(f"边长为2和3，夹角为90度的三角形面积: {triangle_area_angle(2, 3, 90):.2f}")

# 4. 双曲函数
def show_hyperbolic_functions():
    """展示双曲函数"""
    print("\n=== 4. 双曲函数 ===")
    
    # 4.1 基本双曲函数
    print("\n4.1 基本双曲函数")
    
    # 一些测试值
    x_values = [0, 0.5, 1.0, 2.0, -0.5, -1.0]
    
    print("x值       sinh(x)      cosh(x)      tanh(x)")
    print("-" * 50)
    
    for x in x_values:
        sinh_val = math.sinh(x)
        cosh_val = math.cosh(x)
        tanh_val = math.tanh(x)
        
        print(f"{x:8.2f} {sinh_val:11.6f} {cosh_val:11.6f} {tanh_val:11.6f}")
    
    # 4.2 反双曲函数
    print("\n4.2 反双曲函数")
    
    # 对于反双曲正弦，可以接受任何实数
    # 对于反双曲余弦，参数必须大于等于1
    # 对于反双曲正切，参数必须在(-1, 1)之间
    
    # 测试反双曲正弦
    print("反双曲正弦:")
    for x in x_values:
        asinh_val = math.asinh(x)
        print(f"asinh({x:6.2f}) = {asinh_val:10.6f}")
    
    # 测试反双曲余弦
    print("\n反双曲余弦:")
    cosh_x_values = [1.0, 1.5, 2.0]
    for x in cosh_x_values:
        acosh_val = math.acosh(x)
        print(f"acosh({x:6.2f}) = {acosh_val:10.6f}")
    
    # 测试反双曲正切
    print("\n反双曲正切:")
    tanh_x_values = [-0.8, -0.5, 0.0, 0.5, 0.8]
    for x in tanh_x_values:
        atanh_val = math.atanh(x)
        print(f"atanh({x:6.2f}) = {atanh_val:10.6f}")
    
    # 4.3 双曲函数的恒等式
    print("\n4.3 双曲函数的恒等式")
    
    # 验证双曲函数的基本恒等式
    x = 1.0
    print(f"对于x = {x}:")
    print(f"cosh²(x) - sinh²(x) = {math.cosh(x)**2 - math.sinh(x)**2:.10f}")  # 应该等于1
    print(f"1 - tanh²(x) = {1 - math.tanh(x)**2:.10f}")  # 应该等于1/cosh²(x)
    print(f"1/cosh²(x) = {1/(math.cosh(x)**2):.10f}")
    
    # 4.4 实际应用示例
    print("\n4.4 实际应用示例：悬链线")
    
    # 悬链线方程: y = a * cosh(x/a)
    def catenary(x, a=1):
        """计算悬链线在点x处的y坐标"""
        return a * math.cosh(x/a)
    
    # 计算一些点的悬链线
    a = 2  # 参数a
    print(f"悬链线 y = {a} * cosh(x/{a}):")
    print("x值       y值")
    print("-" * 20)
    
    for x in range(-5, 6):
        y = catenary(x, a)
        print(f"{x:5d} {y:10.4f}")

# 5. 指数和对数函数
def show_exponential_logarithmic_functions():
    """展示指数和对数函数"""
    print("\n=== 5. 指数和对数函数 ===")
    
    # 5.1 指数函数
    print("\n5.1 指数函数")
    
    # math.exp(x) 计算 e^x
    x_values = [0, 1, 2, -1, -2, 0.5]
    
    print("x值       exp(x)       e^x (计算值)")
    print("-" * 50)
    
    for x in x_values:
        exp_val = math.exp(x)
        calc_val = math.e ** x  # 也可以通过e的幂计算，但math.exp更高效
        print(f"{x:8.2f} {exp_val:11.6f} {calc_val:16.6f}")
    
    # 5.2 对数函数
    print("\n5.2 对数函数")
    
    # 自然对数 (底为e)
    print("自然对数 (ln):")
    log_values = [1, math.e, math.e**2, 0.5, 2]
    
    for x in log_values:
        ln_val = math.log(x)
        print(f"ln({x:8.6f}) = {ln_val:10.6f}")
    
    # 常用对数 (底为10)
    print("\n常用对数 (log10):")
    for x in [1, 10, 100, 0.1, 2, 5]:
        log10_val = math.log10(x)
        print(f"log10({x:8.6f}) = {log10_val:10.6f}")
    
    # 以任意底的对数
    print("\n以任意底的对数:")
    # math.log(x, base) 计算以base为底的x的对数
    print(f"log2(8) = {math.log(8, 2):.6f}")
    print(f"log3(81) = {math.log(81, 3):.6f}")
    print(f"log5(125) = {math.log(125, 5):.6f}")
    
    # Python 3.3+ 新增的快速对数函数
    if hasattr(math, 'log2') and hasattr(math, 'log1p'):
        print("\nPython 3.3+ 新增对数函数:")
        print(f"log2(8) = {math.log2(8):.6f}")  # 专门用于计算2为底的对数，更高效
        print(f"log1p(0.5) = {math.log1p(0.5):.6f}")  # 计算log(1+x)，对于小x更精确
        print(f"等价于 log(1.5) = {math.log(1.5):.6f}")
    
    # 5.3 幂函数的其他形式
    print("\n5.3 幂函数的其他形式")
    
    # math.pow(x, y) 计算x的y次方
    # 注意：math.pow总是返回浮点数，而**运算符可能返回整数
    print("x^y 使用math.pow和**运算符:")
    test_cases = [(2, 3), (2, 0.5), (-2, 3), (2, -1)]
    
    for x, y in test_cases:
        pow_val = math.pow(x, y)
        op_val = x ** y
        print(f"{x}^{y}: math.pow={pow_val:10.6f}, **={op_val:10.6f}")
    
    # 5.4 实际应用示例：复利计算
    print("\n5.4 实际应用示例：复利计算")
    
    # 复利公式: A = P(1 + r/n)^(nt)
    # 其中：A = 最终金额, P = 本金, r = 年利率, n = 每年复利次数, t = 年数
    def compound_interest(principal, rate, compound_freq, years):
        """计算复利"""
        amount = principal * math.pow((1 + rate / compound_freq), compound_freq * years)
        return amount
    
    # 测试
    principal = 10000  # 本金10000元
    rate = 0.05  # 年利率5%
    years = 10  # 10年
    
    print(f"本金: {principal}元, 年利率: {rate*100}%, 时间: {years}年")
    print("复利频率    最终金额")
    print("-" * 30)
    
    compound_freqs = [1, 2, 4, 12, 365, float('inf')]  # 每年、每半年、每季度、每月、每天、连续复利
    freq_names = ['年复利', '半年复利', '季度复利', '月复利', '日复利', '连续复利']
    
    for freq, name in zip(compound_freqs, freq_names):
        if freq == float('inf'):
            # 连续复利公式: A = P * e^(rt)
            amount = principal * math.exp(rate * years)
        else:
            amount = compound_interest(principal, rate, freq, years)
        print(f"{name:10s} {amount:10.2f}元")
    
    # 计算总收益
    simple_interest = principal * (1 + rate * years)  # 单利
    final_amount = compound_interest(principal, rate, 12, years)  # 月复利
    
    print(f"\n单利收益: {simple_interest - principal:.2f}元")
    print(f"月复利收益: {final_amount - principal:.2f}元")
    print(f"复利比单利多赚: {(final_amount - simple_interest):.2f}元")

# 6. 特殊函数
def show_special_functions():
    """展示一些特殊函数"""
    print("\n=== 6. 特殊函数 ===")
    
    # 6.1 gamma函数和相关函数
    if hasattr(math, 'gamma'):
        print("\n6.1 Gamma函数和相关函数 (Python 3.2+)")
        
        # gamma函数
        print("Gamma函数:")
        for x in [0.5, 1, 2, 3, 4, 5]:
            gamma_val = math.gamma(x)
            print(f"gamma({x}) = {gamma_val:10.6f}")
        
        # 注意：gamma(n) = (n-1)! 对于正整数n
        print("\n验证gamma(n) = (n-1)! 对于正整数n:")
        for n in range(1, 6):
            gamma_val = math.gamma(n)
            factorial_val = math.factorial(n-1)
            print(f"gamma({n}) = {gamma_val:10.6f}, (n-1)! = {factorial_val:10.6f}")
        
        # lgamma函数 - gamma函数的自然对数
        print("\nlgamma函数 (gamma函数的自然对数):")
        for x in [0.5, 1, 2, 5]:
            lgamma_val = math.lgamma(x)
            gamma_val = math.gamma(x)
            print(f"lgamma({x}) = {lgamma_val:10.6f}, ln(gamma({x})) = {math.log(gamma_val):10.6f}")
    
    # 6.2 误差函数
    if hasattr(math, 'erf'):
        print("\n6.2 误差函数 (Python 3.2+)")
        
        # erf函数 - 高斯误差函数
        print("误差函数erf:")
        x_values = [-3, -2, -1, 0, 1, 2, 3]
        for x in x_values:
            erf_val = math.erf(x)
            print(f"erf({x}) = {erf_val:10.6f}")
        
        # erfc函数 - 互补误差函数
        print("\n互补误差函数erfc:")
        for x in x_values[:3]:  # 只测试几个值
            erfc_val = math.erfc(x)
            erf_val = math.erf(x)
            print(f"erfc({x}) = {erfc_val:10.6f}, 1-erf({x}) = {1-erf_val:10.6f}")
    
    # 6.3 高斯函数相关计算
    print("\n6.3 高斯函数相关计算")
    
    def normal_pdf(x, mu=0, sigma=1):
        """计算正态分布的概率密度函数值"""
        return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
    
    def normal_cdf(x, mu=0, sigma=1):
        """计算正态分布的累积分布函数值（近似）"""
        # 使用误差函数计算
        if hasattr(math, 'erf'):
            return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))
        else:
            # 没有erf函数时返回一个提示
            return "需要math.erf函数(Python 3.2+)"
    
    # 计算标准正态分布的一些值
    print("标准正态分布N(0,1)的概率密度函数:")
    x_values = [-2, -1, 0, 1, 2]
    
    for x in x_values:
        pdf_val = normal_pdf(x)
        print(f"x = {x}, pdf = {pdf_val:10.6f}")
    
    print("\n标准正态分布N(0,1)的累积分布函数:")
    for x in x_values:
        cdf_val = normal_cdf(x)
        print(f"x = {x}, cdf = {cdf_val}")

# 7. 实际应用场景
def show_practical_applications():
    """展示math模块在实际场景中的应用"""
    print("\n=== 7. 实际应用场景 ===")
    
    # 7.1 几何计算
    print("\n7.1 几何计算")
    
    # 计算两点之间的距离
    def distance(x1, y1, x2, y2):
        """计算两点(x1,y1)和(x2,y2)之间的距离"""
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # 计算点到直线的距离
    def point_to_line_distance(px, py, x1, y1, x2, y2):
        """计算点(px,py)到直线(x1,y1)-(x2,y2)的距离"""
        # 直线方程: ax + by + c = 0
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        
        # 距离公式: |ax + by + c| / sqrt(a^2 + b^2)
        return abs(a * px + b * py + c) / math.sqrt(a**2 + b**2)
    
    # 测试
    print("两点之间的距离:")
    print(f"(0,0) 到 (3,4) 的距离: {distance(0, 0, 3, 4)}")
    print(f"(1,2) 到 (4,6) 的距离: {distance(1, 2, 4, 6)}")
    
    print("\n点到直线的距离:")
    print(f"点(0,0) 到直线(1,0)-(0,1)的距离: {point_to_line_distance(0, 0, 1, 0, 0, 1):.6f}")
    print(f"点(2,2) 到直线(0,0)-(3,4)的距离: {point_to_line_distance(2, 2, 0, 0, 3, 4):.6f}")
    
    # 7.2 物理计算
    print("\n7.2 物理计算")
    
    # 计算自由落体运动的距离
    def free_fall_distance(time, initial_velocity=0, gravity=9.8):
        """计算自由落体的距离".
        s = v0 * t + 0.5 * g * t^2
        """
        return initial_velocity * time + 0.5 * gravity * time**2
    
    # 计算抛体运动的轨迹
    def projectile_motion(v_initial, angle_deg, time, gravity=9.8):
        """计算抛体在给定时间的位置".
        初始速度v0，发射角度angle(度)
        """
        angle_rad = math.radians(angle_deg)
        vx = v_initial * math.cos(angle_rad)
        vy = v_initial * math.sin(angle_rad)
        
        x = vx * time
        y = vy * time - 0.5 * gravity * time**2
        
        return (x, y)
    
    # 测试
    print("自由落体距离:")
    print(f"1秒后: {free_fall_distance(1):.2f}米")
    print(f"2秒后: {free_fall_distance(2):.2f}米")
    print(f"5秒后: {free_fall_distance(5):.2f}米")
    
    print("\n抛体运动轨迹:")
    v0 = 50  # 初始速度50m/s
    angle = 45  # 发射角度45度
    
    print(f"初始速度: {v0}m/s, 发射角度: {angle}度")
    print("时间(s)   x位置(m)   y位置(m)")
    print("-" * 35)
    
    for t in [0, 1, 2, 3, 4, 5, 6]:
        x, y = projectile_motion(v0, angle, t)
        if y >= 0:  # 只显示y>=0的点（落地前）
            print(f"{t:8.1f} {x:10.2f} {y:10.2f}")
        else:
            print(f"{t:8.1f} {x:10.2f}  (已落地)")
    
    # 7.3 数据分析和统计
    print("\n7.3 数据分析和统计")
    
    # 计算样本标准差
    def sample_std_dev(data):
        """计算样本标准差"""
        n = len(data)
        if n < 2:
            return 0
        
        mean = sum(data) / n
        variance = sum((x - mean)**2 for x in data) / (n - 1)
        return math.sqrt(variance)
    
    # 计算相关系数
    def correlation(x_data, y_data):
        """计算两个数据集的皮尔逊相关系数"""
        n = len(x_data)
        if n != len(y_data) or n < 2:
            return None
        
        # 计算平均值
        mean_x = sum(x_data) / n
        mean_y = sum(y_data) / n
        
        # 计算协方差和标准差
        covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(x_data, y_data)) / n
        std_x = math.sqrt(sum((x - mean_x)**2 for x in x_data) / n)
        std_y = math.sqrt(sum((y - mean_y)**2 for y in y_data) / n)
        
        # 计算相关系数
        if std_x * std_y == 0:
            return 0
        return covariance / (std_x * std_y)
    
    # 测试数据
    temperatures = [20, 22, 25, 24, 23, 21, 20, 19, 18, 20]
    ice_cream_sales = [150, 165, 200, 190, 180, 160, 155, 140, 130, 155]
    
    print("温度数据:", temperatures)
    print("冰淇淋销量:", ice_cream_sales)
    
    # 计算标准差
    temp_std = sample_std_dev(temperatures)
    sales_std = sample_std_dev(ice_cream_sales)
    
    print(f"\n温度标准差: {temp_std:.2f}")
    print(f"销量标准差: {sales_std:.2f}")
    
    # 计算相关系数
    corr = correlation(temperatures, ice_cream_sales)
    print(f"\n温度和冰淇淋销量的相关系数: {corr:.4f}")
    print(f"相关强度: {'强正相关' if corr > 0.7 else '中等正相关' if corr > 0.3 else '弱正相关' if corr > 0 else '无相关' if corr == 0 else '弱负相关' if corr > -0.3 else '中等负相关' if corr > -0.7 else '强负相关'}")
    
    # 7.4 图像处理中的应用
    print("\n7.4 图像处理中的应用")
    
    # 计算图像旋转后的坐标
    def rotate_point(x, y, angle_deg, center_x=0, center_y=0):
        """将点(x,y)绕中心点(center_x, center_y)旋转angle_deg度后的新坐标"""
        angle_rad = math.radians(angle_deg)
        
        # 平移到原点
        x_translated = x - center_x
        y_translated = y - center_y
        
        # 旋转
        x_rotated = x_translated * math.cos(angle_rad) - y_translated * math.sin(angle_rad)
        y_rotated = x_translated * math.sin(angle_rad) + y_translated * math.cos(angle_rad)
        
        # 平移回原中心点
        x_new = x_rotated + center_x
        y_new = y_rotated + center_y
        
        return (x_new, y_new)
    
    # 测试
    print("点旋转示例:")
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]  # 一个正方形的四个顶点
    center = (0.5, 0.5)  # 中心点
    angles = [90, 180, 270, 45]  # 旋转角度
    
    for angle in angles:
        print(f"\n旋转{angle}度后的坐标:")
        for x, y in points:
            x_new, y_new = rotate_point(x, y, angle, center[0], center[1])
            print(f"({x:.1f}, {y:.1f}) -> ({x_new:.4f}, {y_new:.4f})")

# 8. 性能考虑
def show_performance_considerations():
    """展示math模块的性能考虑因素"""
    print("\n=== 8. 性能考虑 ===")
    print("math模块中的函数是对C语言标准库的封装，性能通常非常好")
    
    import time
    
    # 比较math函数和等效的Python表达式的性能
    print("\n比较math函数和Python表达式的性能:")
    
    # 测试math.sqrt vs **0.5
    iterations = 1000000
    
    print(f"\n执行{iterations}次平方根计算:")
    
    # math.sqrt
    start_time = time.time()
    for i in range(iterations):
        math.sqrt(i)
    sqrt_time = time.time() - start_time
    print(f"math.sqrt: {sqrt_time:.6f}秒")
    
    # **0.5
    start_time = time.time()
    for i in range(iterations):
        i ** 0.5
    pow_time = time.time() - start_time
    print(f"**0.5: {pow_time:.6f}秒")
    print(f"math.sqrt比**0.5快约{pow_time/sqrt_time:.2f}倍")
    
    # 测试math.exp vs math.e ** x
    print(f"\n执行{iterations}次指数计算:")
    
    # math.exp
    start_time = time.time()
    for i in range(iterations):
        math.exp(i / 1000)
    exp_time = time.time() - start_time
    print(f"math.exp: {exp_time:.6f}秒")
    
    # math.e ** x
    start_time = time.time()
    for i in range(iterations):
        math.e ** (i / 1000)
    e_pow_time = time.time() - start_time
    print(f"math.e ** x: {e_pow_time:.6f}秒")
    print(f"math.exp比math.e ** x快约{e_pow_time/exp_time:.2f}倍")
    
    # 性能优化建议
    print("\n性能优化建议:")
    print("1. 优先使用math模块的函数，而不是等效的Python表达式")
    print("2. 对于重复计算的结果，考虑缓存")
    print("3. 在循环中避免重复计算相同的数学函数")
    print("4. 对于需要多次调用的函数，可以将函数引用存储在局部变量中")
    print("5. 对于非常大的数值计算，考虑使用NumPy等专门的数值计算库")

# 9. 使用注意事项
def usage_notes():
    print("\n=== 9. 使用注意事项 ===")
    print("1. 所有三角函数都使用弧度作为输入，使用math.radians()可以将角度转换为弧度")
    print("2. math模块中的函数通常只接受浮点数作为参数，对于整数会自动转换")
    print("3. math模块不支持复数运算，复数运算应该使用cmath模块")
    print("4. 浮点数计算存在精度问题，比较浮点数时应使用近似相等")
    print("5. 除以零或对负数开平方会抛出ValueError异常")
    print("6. math.factorial()只接受非负整数，且返回整数")
    print("7. math.gcd()只接受非负整数，且返回的是它们的最大公约数的绝对值")
    print("8. math.log()的参数必须大于0")
    print("9. 某些函数（如math.gamma()、math.erf()等）只在Python 3.2+版本中可用")
    print("10. 在处理大量数值计算时，考虑使用专门的数值计算库，如NumPy")

# 10. 综合示例
def comprehensive_example():
    """综合示例：使用math模块实现一个简单的物理模拟系统"""
    print("\n=== 10. 综合示例：物理模拟系统 ===")
    
    class Vector2D:
        """二维向量类"""
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y
        
        def __add__(self, other):
            if isinstance(other, Vector2D):
                return Vector2D(self.x + other.x, self.y + other.y)
            return Vector2D(self.x + other, self.y + other)
        
        def __sub__(self, other):
            if isinstance(other, Vector2D):
                return Vector2D(self.x - other.x, self.y - other.y)
            return Vector2D(self.x - other, self.y - other)
        
        def __mul__(self, scalar):
            return Vector2D(self.x * scalar, self.y * scalar)
        
        def magnitude(self):
            """返回向量的模长"""
            return math.sqrt(self.x**2 + self.y**2)
        
        def normalize(self):
            """返回标准化的向量"""
            mag = self.magnitude()
            if mag == 0:
                return Vector2D(0, 0)
            return Vector2D(self.x / mag, self.y / mag)
        
        def angle(self):
            """返回向量与x轴的夹角（弧度）"""
            return math.atan2(self.y, self.x)
        
        def angle_deg(self):
            """返回向量与x轴的夹角（度）"""
            return math.degrees(self.angle())
        
        def __repr__(self):
            return f"Vector2D({self.x:.2f}, {self.y:.2f})"
    
    class Particle:
        """粒子类，用于物理模拟"""
        def __init__(self, position, velocity, mass=1.0, radius=1.0):
            self.position = position  # Vector2D
            self.velocity = velocity  # Vector2D
            self.mass = mass
            self.radius = radius
            self.acceleration = Vector2D(0, 0)
        
        def apply_force(self, force):
            """应用力到粒子（F = ma）"""
            self.acceleration = force * (1.0 / self.mass)
        
        def update(self, dt):
            """更新粒子状态"""
            # 更新速度
            self.velocity = self.velocity + self.acceleration * dt
            # 更新位置
            self.position = self.position + self.velocity * dt
        
        def __repr__(self):
            return (f"Particle(pos={self.position}, vel={self.velocity}, "
                    f"mass={self.mass}, radius={self.radius})")
    
    class PhysicsSimulator:
        """简单的物理模拟器"""
        def __init__(self, gravity=9.8):
            self.particles = []
            self.gravity = gravity
            self.damping = 0.99  # 阻尼系数，模拟空气阻力
        
        def add_particle(self, particle):
            """添加粒子到模拟器"""
            self.particles.append(particle)
        
        def simulate(self, dt, steps=1):
            """模拟物理过程"""
            for _ in range(steps):
                for particle in self.particles:
                    # 应用重力
                    gravity_force = Vector2D(0, -particle.mass * self.gravity)
                    particle.apply_force(gravity_force)
                    
                    # 更新粒子
                    particle.update(dt)
                    
                    # 应用阻尼
                    particle.velocity = particle.velocity * self.damping
                    
                    # 边界碰撞检测（简单的地面碰撞）
                    if particle.position.y - particle.radius < 0:
                        particle.position.y = particle.radius
                        particle.velocity.y = -particle.velocity.y * 0.8  # 反弹，损失20%能量
        
        def get_state(self):
            """获取所有粒子的当前状态"""
            return [(p.position.x, p.position.y, p.velocity.x, p.velocity.y) for p in self.particles]
    
    # 使用示例：模拟抛体运动
    print("\n模拟抛体运动:")
    
    # 创建模拟器
    simulator = PhysicsSimulator(gravity=9.8)
    
    # 创建一个抛体
    angle_deg = 45
    angle_rad = math.radians(angle_deg)
    initial_velocity = 50
    
    # 计算初始速度分量
    vx = initial_velocity * math.cos(angle_rad)
    vy = initial_velocity * math.sin(angle_rad)
    
    # 创建粒子
    projectile = Particle(
        position=Vector2D(0, 10),  # 初始位置
        velocity=Vector2D(vx, vy),  # 初始速度
        mass=1.0,  # 质量
        radius=0.5  # 半径
    )
    
    simulator.add_particle(projectile)
    
    # 运行模拟
    dt = 0.1  # 时间步长
    total_time = 0
    
    print("时间(s)    X位置(m)    Y位置(m)    X速度(m/s)    Y速度(m/s)")
    print("-" * 60)
    
    # 打印初始状态
    state = simulator.get_state()[0]
    print(f"{total_time:8.1f} {state[0]:11.2f} {state[1]:11.2f} {state[2]:13.2f} {state[3]:13.2f}")
    
    # 运行模拟并打印结果
    while state[1] >= 0.5:  # 直到落地
        simulator.simulate(dt)
        total_time += dt
        state = simulator.get_state()[0]
        print(f"{total_time:8.1f} {state[0]:11.2f} {state[1]:11.2f} {state[2]:13.2f} {state[3]:13.2f}")
    
    print(f"\n抛体飞行时间: {total_time:.2f}秒")
    print(f"抛体飞行距离: {state[0]:.2f}米")
    
    # 理论最大射程 (无空气阻力)
    theoretical_range = (initial_velocity**2 * math.sin(2 * angle_rad)) / 9.8
    print(f"理论最大射程 (无空气阻力): {theoretical_range:.2f}米")
    print(f"实际射程 (有空气阻力): {state[0]:.2f}米")
    print(f"射程差异: {theoretical_range - state[0]:.2f}米")
    
    # 示例2：模拟多个粒子的运动
    print("\n模拟多个粒子的运动:")
    
    multi_simulator = PhysicsSimulator(gravity=9.8)
    
    # 创建多个粒子，不同的初始角度和速度
    angles = [30, 45, 60]  # 发射角度
    velocities = [40, 50, 60]  # 初始速度
    
    for angle_deg, velocity in zip(angles, velocities):
        angle_rad = math.radians(angle_deg)
        vx = velocity * math.cos(angle_rad)
        vy = velocity * math.sin(angle_rad)
        
        particle = Particle(
            position=Vector2D(0, 10),
            velocity=Vector2D(vx, vy),
            mass=1.0,
            radius=0.5
        )
        multi_simulator.add_particle(particle)
    
    # 运行模拟一段时间
    dt = 0.1
    total_time = 0
    steps = 20
    
    print(f"\n模拟{steps * dt}秒后的粒子状态:")
    print("粒子索引    X位置(m)    Y位置(m)    X速度(m/s)    Y速度(m/s)")
    print("-" * 65)
    
    # 运行模拟
    multi_simulator.simulate(dt, steps)
    
    # 打印最终状态
    states = multi_simulator.get_state()
    for i, state in enumerate(states):
        print(f"{i:10d} {state[0]:11.2f} {state[1]:11.2f} {state[2]:13.2f} {state[3]:13.2f}")
    
    print("\n物理模拟系统演示完成！")

# 执行所有示例
if __name__ == "__main__":
    print("math模块 - Python标准库中的数学函数库\n")
    
    # 执行各个示例
    show_math_constants()
    show_basic_math_functions()
    show_trigonometric_functions()
    show_hyperbolic_functions()
    show_exponential_logarithmic_functions()
    show_special_functions()
    show_practical_applications()
    show_performance_considerations()
    usage_notes()
    comprehensive_example()
    
    print("\n=== 结束 ===")
    print("math模块提供了丰富的数学函数，适用于各种科学计算、工程应用和数据分析场景。")
    print("它包含了基本数学运算、三角函数、双曲函数、指数和对数函数等多种功能。")
    print("使用math模块中的函数通常比使用等效的Python表达式性能更好。")
    print("在进行精确计算或性能关键的应用时，应优先考虑使用math模块。")
    print("对于复数运算，应使用cmath模块；对于大规模数组计算，应考虑NumPy等库。")
    print("了解math模块的功能和使用方法，可以帮助你更高效地完成各种数学计算任务。")
","}}}