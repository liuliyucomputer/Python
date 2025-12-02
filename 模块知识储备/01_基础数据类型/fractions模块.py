# fractions模块 - 分数运算
# 功能作用：提供分数数据类型和分数运算功能
# 使用情景：需要精确分数表示和运算的场景、有理数计算、避免浮点数精度问题、数学计算
# 注意事项：比浮点数计算慢；对于非常大的分数可能会消耗较多内存；可以与整数、浮点数、字符串等类型相互转换

import fractions
from fractions import Fraction
import math
import decimal

# 模块概述
"""
fractions模块提供了表示有理数的支持，主要通过Fraction类实现。Fraction类允许进行精确的分数运算，避免了浮点数计算中的精度问题。

主要特点：
1. 精确表示分数，分子和分母都是整数
2. 自动进行分数约分
3. 支持所有基本算术运算
4. 可以与整数、浮点数、字符串等类型相互转换
5. 提供丰富的数学运算方法

fractions模块特别适用于需要精确分数计算的场景，如数学计算、财务计算等需要避免浮点数精度问题的应用。
"""

# 1. 基本使用
print("=== 1. 基本使用 ===")

def basic_usage():
    """fractions模块的基本使用示例"""
    print("fractions模块的基本使用:")
    
    # 创建Fraction对象
    print("\n1. 创建Fraction对象:")
    
    # 使用分子和分母创建
    f1 = Fraction(1, 2)
    print(f"使用分子和分母: Fraction(1, 2) = {f1}")
    
    # 使用单个整数创建（分母默认为1）
    f2 = Fraction(5)
    print(f"使用单个整数: Fraction(5) = {f2}")
    
    # 使用字符串创建
    f3 = Fraction('3/4')
    print(f"使用字符串: Fraction('3/4') = {f3}")
    
    # 使用浮点数创建
    f4 = Fraction(0.5)
    print(f"使用浮点数: Fraction(0.5) = {f4}")
    
    # 使用Decimal对象创建
    from decimal import Decimal
    f5 = Fraction(Decimal('0.75'))
    print(f"使用Decimal: Fraction(Decimal('0.75')) = {f5}")
    
    # 使用其他分数创建（复制）
    f6 = Fraction(f1)
    print(f"使用其他分数: Fraction(Fraction(1, 2)) = {f6}")
    print()
    
    # 自动约分
    print("\n2. 自动约分:")
    f7 = Fraction(2, 4)  # 会自动约分为1/2
    print(f"Fraction(2, 4) = {f7}")
    
    f8 = Fraction(12, 18)  # 会自动约分为2/3
    print(f"Fraction(12, 18) = {f8}")
    
    f9 = Fraction(-3, 6)  # 会自动约分为-1/2，并将负号放在分子
    print(f"Fraction(-3, 6) = {f9}")
    print()
    
    # 基本属性
    print("\n3. Fraction的基本属性:")
    f = Fraction(3, 4)
    print(f"Fraction(3, 4)的属性:")
    print(f"  分子 (numerator): {f.numerator}")
    print(f"  分母 (denominator): {f.denominator}")
    print(f"  字符串表示: {str(f)}")
    print(f"  浮点数表示: {float(f)}")
    print(f"  整数部分: {f.numerator // f.denominator}")
    print(f"  小数部分: {Fraction(f.numerator % f.denominator, f.denominator)}")
    print()
    
    # 基本算术运算
    print("\n4. 基本算术运算:")
    a = Fraction(1, 2)
    b = Fraction(1, 4)
    
    print(f"a = {a}, b = {b}")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a // b = {a // b}")  # 整除
    print(f"a % b = {a % b}")   # 取模
    print(f"a ** b = {a ** b}")  # 幂运算
    print(f"-a = {-a}")        # 取负
    print(f"+a = {+a}")        # 取正
    print(f"abs(a) = {abs(a)}")  # 绝对值
    print()
    
    # 比较运算
    print("\n5. 比较运算:")
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")
    print(f"a > b: {a > b}")
    print(f"a >= b: {a >= b}")
    print(f"a < b: {a < b}")
    print(f"a <= b: {a <= b}")
    print()
    
    # 与其他数字类型的运算
    print("\n6. 与其他数字类型的运算:")
    frac = Fraction(1, 2)
    
    print(f"Fraction(1, 2) + 1 = {frac + 1}")
    print(f"Fraction(1, 2) + 0.5 = {frac + 0.5}")
    print(f"Fraction(1, 2) + '1/4' = {frac + Fraction('1/4')}")
    
    # 混合类型的运算结果类型
    print(f"\n混合类型的运算结果类型:")
    print(f"type(Fraction(1, 2) + 1) = {type(frac + 1)}")
    print(f"type(Fraction(1, 2) + 0.5) = {type(frac + 0.5)}")
    print(f"type(Fraction(1, 2) + Fraction(1, 4)) = {type(frac + Fraction(1, 4))}")
    print()
    
    # 浮点数vs分数：精度对比
    print("\n7. 浮点数vs分数：精度对比:")
    
    # 浮点数计算中的精度问题
    print("浮点数计算:")
    a_float = 0.1 + 0.1 + 0.1
    b_float = 0.3
    print(f"0.1 + 0.1 + 0.1 = {a_float}")
    print(f"0.3 = {b_float}")
    print(f"(0.1 + 0.1 + 0.1) == 0.3: {a_float == b_float}")
    print()
    
    # 分数计算中的精确表示
    print("分数计算:")
    a_frac = Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10)
    b_frac = Fraction(3, 10)
    print(f"Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) = {a_frac}")
    print(f"Fraction(3, 10) = {b_frac}")
    print(f"(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10)) == Fraction(3, 10): {a_frac == b_frac}")

# 运行基本使用示例
basic_usage()
print()

# 2. 高级创建方法
print("=== 2. 高级创建方法 ===")

def advanced_creation():
    """Fraction的高级创建方法示例"""
    print("Fraction的高级创建方法:")
    
    # 从浮点数创建的精度控制
    print("\n1. 从浮点数创建的精度控制:")
    print("当从浮点数创建Fraction时，会尝试找到最接近的有理数表示:")
    
    # 精确可表示的浮点数
    print("\n精确可表示的浮点数:")
    print(f"Fraction(0.5) = {Fraction(0.5)}")  # 1/2
    print(f"Fraction(0.25) = {Fraction(0.25)}")  # 1/4
    print(f"Fraction(0.125) = {Fraction(0.125)}")  # 1/8
    print()
    
    # 不精确表示的浮点数
    print("\n不精确表示的浮点数:")
    print(f"Fraction(0.1) = {Fraction(0.1)}")  # 会显示实际存储的精确值
    print(f"Fraction(0.1).limit_denominator() = {Fraction(0.1).limit_denominator()}")  # 限制分母，找到近似值
    print(f"Fraction(0.333) = {Fraction(0.333)}")
    print(f"Fraction(0.333).limit_denominator(100) = {Fraction(0.333).limit_denominator(100)}")  # 限制分母不超过100
    print()
    
    # limit_denominator方法
    print("\n2. limit_denominator方法:")
    print("limit_denominator(max_denominator=1000000) 返回最接近的分数，其中分母不超过max_denominator")
    
    f = Fraction('0.333333333333')
    print(f"原始分数: {f}")
    
    print("\n使用不同的max_denominator:")
    print(f"max_denominator=10: {f.limit_denominator(10)}")
    print(f"max_denominator=100: {f.limit_denominator(100)}")
    print(f"max_denominator=1000: {f.limit_denominator(1000)}")
    print(f"max_denominator=10000: {f.limit_denominator(10000)}")
    print()
    
    # 实际应用：浮点数近似
    print("\n3. 实际应用：浮点数近似:")
    pi_float = 3.141592653589793
    print(f"π的浮点数表示: {pi_float}")
    
    # 使用不同的精度近似π
    print("\nπ的分数近似:")
    print(f"近似为22/7: {Fraction(pi_float).limit_denominator(100)}")
    print(f"更精确的近似: {Fraction(pi_float).limit_denominator(1000000)}")
    print(f"实际值: {Fraction(pi_float)}")
    print()
    
    # from_float方法
    print("\n4. from_float方法:")
    print("Fraction.from_float(x) 是创建Fraction对象的类方法，等价于Fraction(x)")
    print(f"Fraction.from_float(0.5) = {Fraction.from_float(0.5)}")
    print(f"Fraction.from_float(0.1) = {Fraction.from_float(0.1)}")
    print()
    
    # from_decimal方法
    print("\n5. from_decimal方法:")
    print("Fraction.from_decimal(x) 从Decimal对象创建Fraction")
    from decimal import Decimal
    
    d = Decimal('0.1')
    print(f"Decimal('0.1') = {d}")
    print(f"Fraction.from_decimal(d) = {Fraction.from_decimal(d)}")
    
    # 也可以直接将Decimal作为参数传给Fraction构造函数
    print(f"Fraction(d) = {Fraction(d)}")
    print()
    
    # 使用字符串创建的高级格式
    print("\n6. 使用字符串创建的高级格式:")
    print("Fraction可以解析多种字符串格式:")
    
    formats = [
        '3/4',        # 分数形式
        '1.5',        # 小数形式
        '-2.5',       # 负小数
        '1 1/2',      # 带整数部分的分数
        ' 22/7 ',     # 带空格的分数
        '3e-1',       # 科学计数法
        '1/2 + 1/3'   # 表达式 (注意：这不会被计算，会抛出异常)
    ]
    
    for fmt in formats:
        try:
            f = Fraction(fmt)
            print(f"Fraction('{fmt}') = {f}")
        except ValueError as e:
            print(f"Fraction('{fmt}') 解析失败: {e}")
    print()
    
    # 创建极大的分数
    print("\n7. 创建极大的分数:")
    # 创建一个极大的分数
    big_fraction = Fraction(10**100, 3)
    print(f"Fraction(10**100, 3) 的分子位数: {len(str(big_fraction.numerator))}")
    print(f"Fraction(10**100, 3) 的分母: {big_fraction.denominator}")
    
    # 计算结果（但可能不会显示完整结果）
    try:
        result = big_fraction * 3
        print(f"Fraction(10**100, 3) * 3 = {result}")
    except Exception as e:
        print(f"计算大分数时出错: {e}")

# 运行高级创建方法示例
advanced_creation()
print()

# 3. 数学函数和方法
print("=== 3. 数学函数和方法 ===")

def mathematical_functions():
    """Fraction支持的数学函数和方法示例"""
    print("Fraction支持的数学函数和方法:")
    
    # 标准数学函数
    print("\n1. 标准数学函数:")
    f = Fraction(1, 2)
    
    print(f"f = {f}")
    print(f"abs(f) = {abs(f)}")
    print(f"round(f, 1) = {round(f, 1)}")
    print(f"math.floor(f) = {math.floor(f)}")
    print(f"math.ceil(f) = {math.ceil(f)}")
    
    # 注意：math.sqrt等函数会将Fraction转换为浮点数
    print(f"math.sqrt(f) = {math.sqrt(f)}")
    print(f"type(math.sqrt(f)) = {type(math.sqrt(f))}")
    print()
    
    # 转换方法
    print("\n2. 转换方法:")
    f = Fraction(3, 4)
    
    print(f"f = {f}")
    print(f"float(f) = {float(f)}")
    print(f"str(f) = {str(f)}")
    print(f"repr(f) = {repr(f)}")
    print(f"int(f) = {int(f)}")  # 截断小数部分
    print()
    
    # 分数操作方法
    print("\n3. 分数操作方法:")
    f = Fraction(5, 6)
    
    print(f"f = {f}")
    print(f"f.numerator = {f.numerator}")
    print(f"f.denominator = {f.denominator}")
    
    # 四舍五入到最接近的1/10
    tenth = Fraction(1, 10)
    rounded = round(f / tenth) * tenth
    print(f"四舍五入到最接近的1/10: {rounded}")
    print()
    
    # 比较方法
    print("\n4. 比较方法:")
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    
    print(f"a = {a}, b = {b}")
    print(f"a.__eq__(b) = {a.__eq__(b)}")  # 等于
    print(f"a.__ne__(b) = {a.__ne__(b)}")  # 不等于
    print(f"a.__lt__(b) = {a.__lt__(b)}")  # 小于
    print(f"a.__le__(b) = {a.__le__(b)}")  # 小于等于
    print(f"a.__gt__(b) = {a.__gt__(b)}")  # 大于
    print(f"a.__ge__(b) = {a.__ge__(b)}")  # 大于等于
    print()
    
    # 幂运算
    print("\n5. 幂运算:")
    f = Fraction(2, 3)
    print(f"f = {f}")
    print(f"f ** 2 = {f ** 2}")
    print(f"f ** 3 = {f ** 3}")
    print(f"f ** 0.5 = {f ** 0.5}")  # 结果是浮点数
    print(f"f ** Fraction(1, 2) = {f ** Fraction(1, 2)}")  # 精确的平方根分数表示
    print()
    
    # 最大公约数和最小公倍数
    print("\n6. 最大公约数和最小公倍数:")
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    
    # 计算分母的最小公倍数
    def lcm(a, b):
        """计算最小公倍数"""
        return a * b // math.gcd(a, b)
    
    # 计算两个分数的最小公分母
    def least_common_denominator(f1, f2):
        """计算两个分数的最小公分母"""
        return lcm(f1.denominator, f2.denominator)
    
    # 计算两个分数的公共分母形式
    def common_denominator_form(f1, f2):
        """将两个分数转换为公共分母形式"""
        lcd = least_common_denominator(f1, f2)
        f1_common = Fraction(f1.numerator * (lcd // f1.denominator), lcd)
        f2_common = Fraction(f2.numerator * (lcd // f2.denominator), lcd)
        return f1_common, f2_common
    
    print(f"a = {a}, b = {b}")
    print(f"最小公分母: {least_common_denominator(a, b)}")
    
    a_common, b_common = common_denominator_form(a, b)
    print(f"公共分母形式: {a_common} 和 {b_common}")

# 运行数学函数和方法示例
mathematical_functions()
print()

# 4. 实际应用示例
print("=== 4. 实际应用示例 ===")

def practical_applications():
    """fractions模块的实际应用示例"""
    print("fractions模块的实际应用示例:")
    
    # 示例1: 精确的厨房测量转换
    def convert_measurement(amount, from_unit, to_unit):
        """转换厨房测量单位
        
        Args:
            amount: 数量
            from_unit: 原单位
            to_unit: 目标单位
            
        Returns:
            转换后的数量（Fraction对象）
        """
        # 定义单位转换关系（转换为茶匙）
        conversions = {
            'teaspoon': Fraction(1, 1),
            'tablespoon': Fraction(3, 1),
            'cup': Fraction(48, 1),
            'fluid_ounce': Fraction(6, 1),
            'milliliter': Fraction(1, 5),  # 近似值
            'liter': Fraction(202, 1),     # 近似值
            'pinch': Fraction(1, 16),
            'dash': Fraction(1, 8)
        }
        
        # 验证单位是否支持
        if from_unit not in conversions or to_unit not in conversions:
            raise ValueError(f"不支持的单位: {from_unit} 或 {to_unit}")
        
        # 转换为茶匙
        amount_in_teaspoons = Fraction(amount) * conversions[from_unit]
        
        # 转换为目标单位
        result = amount_in_teaspoons / conversions[to_unit]
        
        return result
    
    print("\n示例1: 精确的厨房测量转换")
    # 定义一些常见的转换
    conversions = [
        (1, 'tablespoon', 'teaspoon'),
        (1, 'cup', 'tablespoon'),
        (1, 'teaspoon', 'cup'),
        (1, 'fluid_ounce', 'teaspoon'),
        (1, 'pinch', 'teaspoon'),
        (Fraction(1, 2), 'cup', 'tablespoon')
    ]
    
    print("厨房测量转换:")
    for amount, from_unit, to_unit in conversions:
        result = convert_measurement(amount, from_unit, to_unit)
        print(f"{amount} {from_unit} = {result} {to_unit}")
    print()
    
    # 示例2: 分数精确计算 - 分摊账单
    def split_bill(total_amount, num_people):
        """精确计算每个人应该支付的金额
        
        Args:
            total_amount: 总金额（字符串格式，避免浮点数精度问题）
            num_people: 人数
            
        Returns:
            每人应付金额（Fraction对象）
        """
        # 使用字符串创建Fraction以保持精确性
        total = Fraction(total_amount)
        people = Fraction(num_people)
        
        # 计算每人应付金额
        per_person = total / people
        
        return per_person
    
    print("\n示例2: 分数精确计算 - 分摊账单")
    # 测试不同的账单金额和人数
    bills = [
        ('100', 3),       # 100元3人分摊
        ('75.50', 2),     # 75.50元2人分摊
        ('123.33', 4),    # 123.33元4人分摊
        ('50.01', 3)      # 50.01元3人分摊（测试精确性）
    ]
    
    print("账单分摊计算:")
    for amount_str, people in bills:
        per_person = split_bill(amount_str, people)
        # 转换为浮点数显示（实际应用中仍应保持Fraction进行计算）
        per_person_float = float(per_person)
        
        # 验证总和
        total_calculated = per_person * people
        
        print(f"总金额: ${amount_str}, {people}人分摊")
        print(f"每人应付: ${per_person_float:.2f} (精确值: {per_person})")
        print(f"验证总和: ${float(total_calculated):.2f} (是否等于原始金额: {total_calculated == Fraction(amount_str)})")
        print()
    print()
    
    # 示例3: 精确的百分比计算
    def calculate_percentage(value, percent):
        """精确计算百分比
        
        Args:
            value: 原始值
            percent: 百分比值（如10表示10%）
            
        Returns:
            计算结果（Fraction对象）
        """
        value_frac = Fraction(value)
        percent_frac = Fraction(percent)
        
        # 计算百分比
        result = value_frac * percent_frac / Fraction(100)
        
        return result
    
    print("\n示例3: 精确的百分比计算")
    # 测试不同的百分比计算
    calculations = [
        (100, 10),    # 100的10%
        (100, 33.33), # 100的33.33%
        (50, 25),     # 50的25%
        (75.5, 15.75) # 75.5的15.75%
    ]
    
    print("百分比计算:")
    for value, percent in calculations:
        result = calculate_percentage(value, percent)
        result_float = float(result)
        
        # 验证计算结果
        manual_check = float(value) * float(percent) / 100
        
        print(f"{value}的{percent}% = {result_float:.4f} (精确值: {result})")
        print(f"浮点数计算结果: {manual_check:.4f}")
        print(f"差异: {abs(result_float - manual_check):.10f}")
        print()
    print()
    
    # 示例4: 数学问题求解
    def solve_math_problem():
        """使用分数解决数学问题"""
        print("数学问题求解示例:")
        
        # 问题1: 解方程 1/3 + 1/4 = x
        print("\n问题1: 解方程 1/3 + 1/4 = x")
        x = Fraction(1, 3) + Fraction(1, 4)
        print(f"x = {x} = {float(x)}")
        
        # 问题2: 计算 2/3 ÷ 4/5
        print("\n问题2: 计算 2/3 ÷ 4/5")
        result = Fraction(2, 3) / Fraction(4, 5)
        print(f"结果 = {result} = {float(result)}")
        
        # 问题3: 计算等差数列 1/2, 1/3, 1/6, 0, ... 的公差
        print("\n问题3: 计算等差数列 1/2, 1/3, 1/6, 0, ... 的公差")
        a1 = Fraction(1, 2)
        a2 = Fraction(1, 3)
        a3 = Fraction(1, 6)
        a4 = Fraction(0, 1)
        
        d1 = a2 - a1
        d2 = a3 - a2
        d3 = a4 - a3
        
        print(f"公差1 = {d1}")
        print(f"公差2 = {d2}")
        print(f"公差3 = {d3}")
        print(f"公差是否一致: {d1 == d2 == d3}")
        
        # 问题4: 计算复利问题（这里简化为使用分数计算）
        print("\n问题4: 计算复利问题")
        principal = Fraction(1000, 1)  # 本金1000
        rate = Fraction(10, 100)       # 年利率10%
        years = Fraction(2, 1)         # 2年
        
        # 复利公式: A = P * (1 + r)^t
        amount = principal * (1 + rate) ** years
        interest = amount - principal
        
        print(f"本金: {principal}")
        print(f"年利率: {rate * 100}%")
        print(f"时间: {years}年")
        print(f"最终金额: {amount} = {float(amount)}")
        print(f"利息: {interest} = {float(interest)}")
    
    print("\n示例4: 数学问题求解")
    solve_math_problem()
    print()
    
    # 示例5: 自定义分数计算工具
    class FractionCalculator:
        """简单的分数计算器"""
        def __init__(self):
            self.history = []
        
        def add(self, a, b):
            """加法"""
            result = Fraction(a) + Fraction(b)
            self.history.append(f"{a} + {b} = {result}")
            return result
        
        def subtract(self, a, b):
            """减法"""
            result = Fraction(a) - Fraction(b)
            self.history.append(f"{a} - {b} = {result}")
            return result
        
        def multiply(self, a, b):
            """乘法"""
            result = Fraction(a) * Fraction(b)
            self.history.append(f"{a} * {b} = {result}")
            return result
        
        def divide(self, a, b):
            """除法"""
            result = Fraction(a) / Fraction(b)
            self.history.append(f"{a} / {b} = {result}")
            return result
        
        def power(self, a, b):
            """幂运算"""
            result = Fraction(a) ** Fraction(b)
            self.history.append(f"{a} ** {b} = {result}")
            return result
        
        def get_history(self):
            """获取计算历史"""
            return self.history
        
        def clear_history(self):
            """清除计算历史"""
            self.history = []
    
    print("\n示例5: 自定义分数计算工具")
    calc = FractionCalculator()
    
    # 执行一些计算
    print("执行计算:")
    print(f"1/2 + 1/3 = {calc.add('1/2', '1/3')}")
    print(f"3/4 - 1/8 = {calc.subtract('3/4', '1/8')}")
    print(f"2/3 * 3/5 = {calc.multiply('2/3', '3/5')}")
    print(f"5/6 / 7/8 = {calc.divide('5/6', '7/8')}")
    print(f"(1/2) ** 2 = {calc.power('1/2', 2)}")
    
    # 显示历史记录
    print("\n计算历史:")
    for i, entry in enumerate(calc.get_history(), 1):
        print(f"{i}. {entry}")

# 运行实际应用示例
practical_applications()
print()

# 5. 与其他模块的交互
print("=== 5. 与其他模块的交互 ===")

def module_interactions():
    """fractions模块与其他模块的交互示例"""
    print("fractions模块与其他模块的交互:")
    
    # 与math模块的交互
    print("\n1. 与math模块的交互:")
    import math
    
    f = Fraction(1, 2)
    print(f"f = {f}")
    
    # math模块函数对Fraction的处理
    print(f"math.sqrt(f) = {math.sqrt(f)}")
    print(f"math.sin(f) = {math.sin(f)}")
    print(f"math.cos(f) = {math.cos(f)}")
    print(f"math.exp(f) = {math.exp(f)}")
    print(f"math.log(f) = {math.log(f)}")
    
    # 注意：math模块的函数通常会将Fraction转换为float
    print(f"type(math.sqrt(f)) = {type(math.sqrt(f))}")
    print()
    
    # 与decimal模块的交互
    print("\n2. 与decimal模块的交互:")
    from decimal import Decimal, getcontext
    
    # 设置decimal上下文
    getcontext().prec = 28
    
    # Fraction转换为Decimal
    f = Fraction(1, 3)
    d = Decimal(f)
    print(f"Fraction(1, 3) = {f}")
    print(f"转换为Decimal = {d}")
    
    # Decimal转换为Fraction
    d2 = Decimal('0.1')
    f2 = Fraction(d2)
    print(f"Decimal('0.1') = {d2}")
    print(f"转换为Fraction = {f2}")
    
    # 精度对比
    print(f"\n精度对比:")
    f3 = Fraction(1, 7)
    d3 = Decimal(f3)
    float3 = float(f3)
    
    print(f"Fraction(1, 7) = {f3}")
    print(f"Decimal表示 = {d3}")
    print(f"float表示 = {float3}")
    print()
    
    # 与random模块的交互
    print("\n3. 与random模块的交互:")
    import random
    
    # 生成随机分数
    print("生成随机分数:")
    for i in range(5):
        # 生成1-10之间的随机分子和分母
        numerator = random.randint(1, 10)
        denominator = random.randint(1, 10)
        f = Fraction(numerator, denominator)
        print(f"  {f}")
    print()
    
    # 与statistics模块的交互
    print("\n4. 与statistics模块的交互:")
    import statistics
    
    # 计算分数列表的统计量
   分数列表 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4), Fraction(1, 5), Fraction(1, 6)]
    print(f"分数列表: {分数列表}")
    
    # 计算均值
    mean = statistics.mean(分数列表)
    print(f"均值: {mean} = {float(mean)}")
    
    # 计算中位数
    median = statistics.median(分数列表)
    print(f"中位数: {median} = {float(median)}")
    
    # 计算众数（如果有）
    try:
        mode = statistics.mode(分数列表)
        print(f"众数: {mode}")
    except statistics.StatisticsError:
        print("没有众数（所有元素出现次数相同）")
    
    # 计算标准差
    stdev = statistics.stdev(分数列表)
    print(f"标准差: {stdev}")
    print()
    
    # 与NumPy的交互（如果可用）
    print("\n5. 与NumPy的交互:")
    try:
        import numpy as np
        
        # Fraction转换为NumPy数组
       分数 = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)]
        np_array = np.array(分数, dtype=np.float64)
        print(f"分数列表: {分数}")
        print(f"NumPy数组: {np_array}")
        
        # NumPy数组操作
        print(f"NumPy数组平均值: {np.mean(np_array)}")
        print(f"NumPy数组总和: {np.sum(np_array)}")
    except ImportError:
        print("NumPy模块未安装，无法进行交互演示")

# 运行与其他模块的交互示例
module_interactions()
print()

# 6. 最佳实践和注意事项
print("=== 6. 最佳实践和注意事项 ===")

def best_practices():
    """fractions模块使用的最佳实践和注意事项"""
    print("fractions模块使用的最佳实践和注意事项:")
    
    # 1. 创建Fraction对象的最佳方式
    print("\n1. 创建Fraction对象的最佳方式:")
    print("   - 推荐: 从字符串或整数对创建Fraction")
    print("   - 避免: 从浮点数直接创建Fraction（除非必要）")
    print("   - 原因: 浮点数可能有精度问题，会影响Fraction的精确性")
    
    print("   - 示例:")
    print(f"     字符串创建: Fraction('0.1') = {Fraction('0.1')}")
    print(f"     浮点数创建: Fraction(0.1) = {Fraction(0.1)}")  # 包含浮点数精度问题
    print()
    
    # 2. 避免过度使用Fraction
    print("\n2. 避免过度使用Fraction:")
    print("   - 注意事项: Fraction运算比浮点数运算慢")
    print("   - 建议:")
    print("     - 只在需要精确分数表示的场景使用Fraction")
    print("     - 对于性能敏感的应用，考虑使用其他数据类型")
    print()
    
    # 3. 处理大数
    print("\n3. 处理大数:")
    print("   - 注意事项: 非常大的分数可能会消耗大量内存")
    print("   - 建议:")
    print("     - 对于大数运算，考虑使用limit_denominator方法限制分母大小")
    print("     - 使用浮点数进行近似计算（如果精度要求允许）")
    print()
    
    # 4. 序列化和存储
    print("\n4. 序列化和存储:")
    print("   - 最佳实践: 存储分数的分子和分母，而不是字符串表示")
    print("   - 原因: 更容易重建精确的分数对象")
    print("   - JSON序列化示例:")
    print("""
    import json
    from fractions import Fraction
    
    class FractionJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Fraction):
                return {
                    "__fraction__": True,
                    "numerator": obj.numerator,
                    "denominator": obj.denominator
                }
            return super().default(obj)
    
    def fraction_json_decoder(dct):
        if "__fraction__" in dct:
            return Fraction(dct["numerator"], dct["denominator"])
        return dct
    
    # 使用示例
    # f = Fraction(1, 2)
    # json_str = json.dumps(f, cls=FractionJSONEncoder)
    # decoded_f = json.loads(json_str, object_hook=fraction_json_decoder)
    """)
    print()
    
    # 5. 错误处理
    print("\n5. 错误处理:")
    print("   - 最佳实践: 捕获并处理可能的异常")
    print("   - 常见异常:")
    print("     - ZeroDivisionError: 分母为零")
    print("     - ValueError: 无效的字符串格式")
    print("     - TypeError: 无效的参数类型")
    
    print("   - 示例:")
    print("""
    def safe_fraction(numerator, denominator=None):
        """安全地创建Fraction对象"""
        try:
            if denominator is None:
                return Fraction(numerator)
            else:
                return Fraction(numerator, denominator)
        except ZeroDivisionError:
            print("错误: 分母不能为零")
            return None
        except ValueError as e:
            print(f"错误: {e}")
            return None
        except TypeError:
            print("错误: 参数类型无效")
            return None
    """)
    print()
    
    # 6. 性能优化
    print("\n6. 性能优化:")
    print("   - 预创建常用分数对象")
    print("   - 避免重复创建相同的Fraction对象")
    print("   - 对于不需要精确表示的操作，考虑在最后才转换为Fraction")
    
    print("   - 示例:")
    print("""
    # 预创建常用分数
    ONE = Fraction(1, 1)
    HALF = Fraction(1, 2)
    THIRD = Fraction(1, 3)
    QUARTER = Fraction(1, 4)
    
    # 重用这些对象
    def calculate_discount(price, discount_rate):
        """计算折扣价格"""
        # 如果discount_rate是常见值，使用预创建的分数
        discount_fractions = {
            0.25: QUARTER,
            0.5: HALF,
            0.333: THIRD
        }
        
        if discount_rate in discount_fractions:
            discount = discount_fractions[discount_rate]
        else:
            discount = Fraction(discount_rate)
        
        return price * (ONE - discount)
    """)
    print()
    
    # 7. 与浮点数的转换时机
    print("\n7. 与浮点数的转换时机:")
    print("   - 最佳实践: 尽可能晚地将Fraction转换为浮点数")
    print("   - 原因: 保留计算过程中的精度，只在最终输出时转换为浮点数")
    print("   - 注意事项: 当需要与浮点数API交互时，转换是必要的")
    print()
    
    # 8. 混合精度计算
    print("\n8. 混合精度计算:")
    print("   - 注意事项: 混合使用Fraction和浮点数会导致Fraction被转换为浮点数")
    print("   - 建议: 尽量在同一计算中保持相同的数据类型")
    
    print("   - 示例:")
    f = Fraction(1, 2)
    fl = 0.5
    print(f"Fraction(1, 2) + 0.5 = {f + fl}")
    print(f"type(Fraction(1, 2) + 0.5) = {type(f + fl)}")  # 结果是float
    print(f"Fraction(1, 2) + Fraction(1, 2) = {f + Fraction(1, 2)}")
    print(f"type(Fraction(1, 2) + Fraction(1, 2)) = {type(f + Fraction(1, 2))}")  # 结果是Fraction

# 运行最佳实践示例
best_practices()

# 总结
print("\n=== 总结 ===")
print("fractions模块为Python提供了精确的分数运算支持，是处理有理数的重要工具。")
print("主要功能和优势包括：")
print("1. 精确表示分数，避免浮点数精度问题")
print("2. 自动约分，保持分数的最简形式")
print("3. 支持所有基本算术运算和比较运算")
print("4. 可以与整数、浮点数、字符串、Decimal等类型相互转换")
print("5. 提供limit_denominator等方法用于浮点数近似")
print()
print("在使用fractions模块时，需要注意性能开销，并遵循最佳实践，特别是从字符串创建Fraction对象、")
print("避免不必要的类型转换、合理处理大数运算等。")
print()
print("fractions模块广泛应用于需要精确分数计算的场景，如数学计算、金融计算、科学计算等，")
print("是Python中处理有理数的理想选择。")

# 运行完整演示
if __name__ == "__main__":
    print("Python fractions模块演示\n")
    print("请参考源代码中的详细示例和说明")