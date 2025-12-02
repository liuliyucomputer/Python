# decimal模块 - 十进制浮点数运算
# 功能作用：提供高精度的十进制浮点数运算支持
# 使用情景：金融计算、税务计算、需要精确小数表示的科学计算、避免浮点数精度问题
# 注意事项：比浮点数计算慢；需要显式导入并创建Decimal对象；可以设置不同精度和舍入模式；避免与浮点数直接混合运算

import decimal
from decimal import Decimal
import math

# 模块概述
"""
decimal模块为十进制浮点数运算提供了高精度支持，主要特点包括：

1. 精确表示：Decimal类型可以精确表示十进制小数，不会像float类型那样产生精度误差
2. 可配置精度：可以根据需要设置任意精度的运算
3. 可配置舍入模式：提供多种舍入规则，如ROUND_HALF_UP（四舍五入）、ROUND_UP（向上舍入）等
4. 丰富的数学函数：提供大量数学运算和查询函数
5. 金融计算支持：特别适合需要精确小数计算的金融和税务应用

decimal模块定义了Decimal类型和Context类型，前者用于表示十进制数，后者用于控制运算环境（如精度、舍入模式等）。
"""

# 1. 基本使用
print("=== 1. 基本使用 ===")

def basic_usage():
    """decimal模块的基本使用示例"""
    print("decimal模块的基本使用:")
    
    # 创建Decimal对象
    print("\n1. 创建Decimal对象:")
    
    # 从整数创建
    d1 = Decimal(10)
    print(f"从整数创建: Decimal(10) = {d1}")
    
    # 从字符串创建（推荐方式）
    d2 = Decimal('0.1')
    print(f"从字符串创建: Decimal('0.1') = {d2}")
    
    # 从浮点数创建（不推荐，因为浮点数本身可能有精度问题）
    d3 = Decimal(0.1)
    print(f"从浮点数创建: Decimal(0.1) = {d3}")
    print(f"注意: 从浮点数创建时保留了浮点数的精度问题")
    
    # 从元组创建
    # 元组格式: (符号位(0=正, 1=负), 数字元组, 指数)
    d4 = Decimal((1, (3, 1, 4), -2))  # 表示 -314 * 10^-2 = -3.14
    print(f"从元组创建: Decimal((1, (3, 1, 4), -2)) = {d4}")
    
    # 使用常量
    print(f"Decimal('Infinity') = {Decimal('Infinity')}")
    print(f"Decimal('-Infinity') = {Decimal('-Infinity')}")
    print(f"Decimal('NaN') = {Decimal('NaN')}")  # Not a Number
    print(f"Decimal('0') = {Decimal('0')}")
    print(f"Decimal('1E+3') = {Decimal('1E+3')}")  # 科学计数法
    print()
    
    # 浮点数vs十进制：精度对比
    print("\n2. 浮点数vs十进制：精度对比:")
    
    # 浮点数计算中的精度问题
    print("浮点数计算:")
    a_float = 0.1 + 0.1 + 0.1
    b_float = 0.3
    print(f"0.1 + 0.1 + 0.1 = {a_float}")
    print(f"0.3 = {b_float}")
    print(f"(0.1 + 0.1 + 0.1) == 0.3: {a_float == b_float}")
    print()
    
    # 十进制计算中的精确表示
    print("十进制计算:")
    a_decimal = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
    b_decimal = Decimal('0.3')
    print(f"Decimal('0.1') + Decimal('0.1') + Decimal('0.1') = {a_decimal}")
    print(f"Decimal('0.3') = {b_decimal}")
    print(f"(Decimal('0.1') + Decimal('0.1') + Decimal('0.1')) == Decimal('0.3'): {a_decimal == b_decimal}")
    print()
    
    # 基本算术运算
    print("\n3. 基本算术运算:")
    x = Decimal('10.5')
    y = Decimal('3.2')
    
    print(f"x = {x}, y = {y}")
    print(f"x + y = {x + y}")
    print(f"x - y = {x - y}")
    print(f"x * y = {x * y}")
    print(f"x / y = {x / y}")
    print(f"x // y = {x // y}")  # 整除
    print(f"x % y = {x % y}")   # 取模
    print(f"x ** y = {x ** y}") # 幂运算
    print(f"-x = {-x}")        # 取负
    print(f"+x = {+x}")        # 取正
    print(f"abs(x) = {abs(x)}")  # 绝对值
    print()
    
    # 比较运算
    print("\n4. 比较运算:")
    print(f"x == y: {x == y}")
    print(f"x != y: {x != y}")
    print(f"x > y: {x > y}")
    print(f"x >= y: {x >= y}")
    print(f"x < y: {x < y}")
    print(f"x <= y: {x <= y}")
    print()
    
    # 类型转换
    print("\n5. 类型转换:")
    d = Decimal('123.45')
    print(f"原始Decimal: {d}")
    print(f"转换为整数: {int(d)}")        # 截断小数部分
    print(f"转换为浮点数: {float(d)}")    # 可能会丢失精度
    print(f"转换为字符串: {str(d)}")
    print(f"转换为元组: {tuple(d)}")      # (符号位, 数字元组, 指数)
    print(f"转换为元组的示例: {tuple(d)}")
    print()
    
    # 金融计算示例
    print("\n6. 金融计算示例:")
    # 计算利息
    principal = Decimal('1000.00')  # 本金
    rate = Decimal('0.05')         # 年利率5%
    time = Decimal('2.5')          # 2.5年
    
    interest = principal * rate * time
    total = principal + interest
    
    print(f"本金: ${principal}")
    print(f"年利率: {rate * 100}%")
    print(f"时间: {time}年")
    print(f"利息: ${interest}")
    print(f"总额: ${total}")
    
    # 格式化输出为货币格式
    print(f"\n格式化输出:")
    print(f"利息: ${interest:.2f}")
    print(f"总额: ${total:.2f}")

# 运行基本使用示例
basic_usage()
print()

# 2. 上下文管理
print("=== 2. 上下文管理 ===")

def context_management():
    """decimal模块的上下文管理示例"""
    print("decimal模块的上下文管理:")
    
    # 获取全局上下文
    print("\n1. 获取全局上下文:")
    global_context = decimal.getcontext()
    print(f"全局上下文: {global_context}")
    print(f"当前精度: {global_context.prec}")
    print(f"当前舍入模式: {global_context.rounding}")
    print()
    
    # 修改全局上下文
    print("\n2. 修改全局上下文:")
    # 保存原始设置
    original_prec = global_context.prec
    original_rounding = global_context.rounding
    
    # 修改精度和舍入模式
    global_context.prec = 28
    global_context.rounding = decimal.ROUND_HALF_UP  # 四舍五入
    
    print(f"修改后的精度: {global_context.prec}")
    print(f"修改后的舍入模式: {global_context.rounding}")
    print()
    
    # 精度对计算结果的影响
    print("\n3. 精度对计算结果的影响:")
    
    # 重置上下文
    decimal.getcontext().prec = 28
    d1 = Decimal('1') / Decimal('3')
    print(f"精度28位: 1/3 = {d1}")
    
    decimal.getcontext().prec = 10
    d2 = Decimal('1') / Decimal('3')
    print(f"精度10位: 1/3 = {d2}")
    
    decimal.getcontext().prec = 5
    d3 = Decimal('1') / Decimal('3')
    print(f"精度5位: 1/3 = {d3}")
    print()
    
    # 舍入模式
    print("\n4. 舍入模式:")
    
    # 可用的舍入模式
    rounding_modes = {
        'ROUND_CEILING': decimal.ROUND_CEILING,  # 向正无穷方向舍入
        'ROUND_FLOOR': decimal.ROUND_FLOOR,      # 向负无穷方向舍入
        'ROUND_DOWN': decimal.ROUND_DOWN,        # 向零方向舍入
        'ROUND_UP': decimal.ROUND_UP,            # 向远离零的方向舍入
        'ROUND_HALF_UP': decimal.ROUND_HALF_UP,  # 四舍五入
        'ROUND_HALF_DOWN': decimal.ROUND_HALF_DOWN,  # 五舍六入
        'ROUND_HALF_EVEN': decimal.ROUND_HALF_EVEN   # 银行家舍入法
    }
    
    # 测试不同舍入模式
    test_value = Decimal('2.5')
    print(f"测试值: {test_value}")
    
    for name, mode in rounding_modes.items():
        decimal.getcontext().rounding = mode
        rounded = +test_value  # 使用一元+运算符触发舍入
        print(f"{name}: {rounded}")
    print()
    
    # 使用localcontext创建临时上下文
    print("\n5. 使用localcontext创建临时上下文:")
    
    # 全局上下文
    print(f"全局精度: {decimal.getcontext().prec}")
    
    # 临时上下文
    with decimal.localcontext() as ctx:
        ctx.prec = 5
        ctx.rounding = decimal.ROUND_HALF_UP
        temp_result = Decimal('1') / Decimal('3')
        print(f"临时上下文(精度5)中的计算结果: {temp_result}")
    
    # 全局上下文不受影响
    global_result = Decimal('1') / Decimal('3')
    print(f"临时上下文结束后(全局精度)的计算结果: {global_result}")
    print()
    
    # 陷阱设置
    print("\n6. 陷阱设置:")
    print("decimal模块可以设置陷阱来捕获各种异常条件")
    print("常见陷阱:")
    print("- InvalidOperation: 无效操作")
    print("- DivisionByZero: 除以零")
    print("- Overflow: 溢出")
    print("- Underflow: 下溢")
    print("- Inexact: 不精确结果")
    print("- Rounded: 结果被舍入")
    
    # 设置陷阱示例
    print("\n设置除以零陷阱:")
    with decimal.localcontext() as ctx:
        # 默认情况下，除以零返回Infinity
        print(f"默认行为: Decimal('1') / Decimal('0') = {Decimal('1') / Decimal('0')}")
        
        # 设置除以零陷阱
        ctx.traps[decimal.DivisionByZero] = True
        try:
            result = Decimal('1') / Decimal('0')
            print(f"结果: {result}")
        except decimal.DivisionByZero:
            print("触发异常: 除以零")
    print()
    
    # 恢复原始上下文设置
    global_context.prec = original_prec
    global_context.rounding = original_rounding
    print(f"已恢复全局上下文的原始设置")

# 运行上下文管理示例
context_management()
print()

# 3. 数学函数
print("=== 3. 数学函数 ===")

def mathematical_functions():
    """decimal模块提供的数学函数示例"""
    print("decimal模块提供的数学函数:")
    
    # 平方根
    print("\n1. 平方根 (sqrt):")
    print(f"sqrt(2) = {Decimal('2').sqrt()}")
    print(f"sqrt(9) = {Decimal('9').sqrt()}")
    print(f"sqrt(0) = {Decimal('0').sqrt()}")
    
    # 精确计算平方根
    print("\n使用高精度计算sqrt(2):")
    with decimal.localcontext() as ctx:
        ctx.prec = 50
        print(f"精度50位: sqrt(2) = {Decimal('2').sqrt()}")
    print()
    
    # 比较函数
    print("\n2. 比较函数:")
    a = Decimal('10.5')
    b = Decimal('3.2')
    print(f"a = {a}, b = {b}")
    print(f"a.compare(b) = {a.compare(b)}")    # 1表示a > b, 0表示a = b, -1表示a < b
    print(f"a.compare_total(b) = {a.compare_total(b)}")  # 考虑所有位，包括精度
    print(f"a.compare_total_mag(b) = {a.compare_total_mag(b)}")  # 只比较绝对值
    print(f"a.copysign(b) = {a.copysign(b)}")  # 复制符号
    print()
    
    # 转换和格式化
    print("\n3. 转换和格式化:")
    d = Decimal('123.456')
    print(f"原始值: {d}")
    print(f"规范化: {d.normalize()}")  # 移除末尾的零
    print(f"工程计数法: {d.normalize().to_eng_string()}")
    print(f"指数为0: {d.quantize(Decimal('1.'))}")  # 调整到指定的指数
    print(f"两位小数: {d.quantize(Decimal('0.00'))}")
    print(f"科学计数法: {d.to_eng_string()}")
    print()
    
    # 逻辑运算
    print("\n4. 逻辑运算:")
    print(f"is_zero(): {Decimal('0').is_zero()}")
    print(f"is_positive(): {Decimal('5').is_positive()}")
    print(f"is_negative(): {Decimal('-5').is_negative()}")
    print(f"is_nan(): {Decimal('NaN').is_nan()}")
    print(f"is_infinite(): {Decimal('Infinity').is_infinite()}")
    print(f"is_finite(): {Decimal('5').is_finite()}")
    print(f"is_snan(): {Decimal('sNaN').is_snan()}")  # 信号NaN
    print()
    
    # 调整函数
    print("\n5. 调整函数:")
    print(f"调整到两位小数 (ROUND_HALF_UP): {Decimal('1.234').quantize(Decimal('0.00'), rounding=decimal.ROUND_HALF_UP)}")
    print(f"调整到两位小数 (ROUND_DOWN): {Decimal('1.239').quantize(Decimal('0.00'), rounding=decimal.ROUND_DOWN)}")
    print(f"调整到整数: {Decimal('1.999').to_integral_value()}")
    print(f"向上取整: {Decimal('1.1').to_integral_value(rounding=decimal.ROUND_CEILING)}")
    print(f"向下取整: {Decimal('1.9').to_integral_value(rounding=decimal.ROUND_FLOOR)}")
    print()
    
    # 其他数学函数
    print("\n6. 其他数学函数:")
    print(f"abs(): {abs(Decimal('-10.5'))}")
    print(f"exp(): {Decimal('1').exp()}")  # 自然指数
    print(f"ln(): {Decimal('2.71828').ln()}")  # 自然对数
    print(f"log10(): {Decimal('100').log10()}")  # 以10为底的对数
    print(f"logb(): {Decimal('1000').logb()}")  # 自然对数的整数部分
    print(f"max(): {max(Decimal('5'), Decimal('10'), Decimal('7'))}")
    print(f"min(): {min(Decimal('5'), Decimal('10'), Decimal('7'))}")
    print(f"power(): {Decimal('2').__pow__(Decimal('10'))}")  # 幂运算
    print(f"power(余数): {Decimal('10').__pow__(Decimal('3'), Decimal('7'))}")  # 带余数的幂运算
    print()
    
    # 高精度数学计算
    print("\n7. 高精度数学计算:")
    with decimal.localcontext() as ctx:
        ctx.prec = 100  # 设置高精度
        pi = Decimal('0')
        k = 0
        
        # 使用莱布尼茨公式计算π
        # π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
        for i in range(100):
            term = Decimal('1') / Decimal(2 * i + 1)
            if i % 2 == 0:
                pi += term
            else:
                pi -= term
        
        pi *= Decimal('4')
        print(f"使用100项莱布尼茨公式计算的π (精度100位):")
        print(pi)
        
        # 与Python的math.pi比较
        print(f"\nPython的math.pi: {math.pi}")

# 运行数学函数示例
mathematical_functions()
print()

# 4. 实际应用示例
print("=== 4. 实际应用示例 ===")

def practical_applications():
    """decimal模块的实际应用示例"""
    print("decimal模块的实际应用示例:")
    
    # 示例1: 金融计算 - 复利计算
    def compound_interest(principal, rate, years, compounding_periods=12):
        """计算复利
        
        Args:
            principal: 本金
            rate: 年利率
            years: 年数
            compounding_periods: 每年复利次数
            
        Returns:
            最终金额
        """
        # 转换为Decimal类型
        p = Decimal(str(principal))
        r = Decimal(str(rate))
        n = Decimal(str(compounding_periods))
        t = Decimal(str(years))
        
        # 复利公式: A = P * (1 + r/n)^(n*t)
        amount = p * (1 + r / n) ** (n * t)
        
        return amount
    
    print("\n示例1: 金融计算 - 复利计算")
    principal = 10000
    annual_rate = 0.05  # 5%
    years = 10
    
    # 每年复利
    annual_compound = compound_interest(principal, annual_rate, years, 1)
    print(f"本金: ${principal}")
    print(f"年利率: {annual_rate * 100}%")
    print(f"时间: {years}年")
    print(f"\n最终金额:")
    print(f"每年复利: ${annual_compound:.2f}")
    
    # 每半年复利
    semi_annual_compound = compound_interest(principal, annual_rate, years, 2)
    print(f"每半年复利: ${semi_annual_compound:.2f}")
    
    # 每季度复利
    quarterly_compound = compound_interest(principal, annual_rate, years, 4)
    print(f"每季度复利: ${quarterly_compound:.2f}")
    
    # 每月复利
    monthly_compound = compound_interest(principal, annual_rate, years, 12)
    print(f"每月复利: ${monthly_compound:.2f}")
    
    # 每日复利
    daily_compound = compound_interest(principal, annual_rate, years, 365)
    print(f"每日复利: ${daily_compound:.2f}")
    print()
    
    # 示例2: 税务计算
    def calculate_tax(income, tax_brackets):
        """计算累进税率
        
        Args:
            income: 收入
            tax_brackets: 税率表，格式为[(上限, 税率), ...]
            
        Returns:
            应纳税额
        """
        income_decimal = Decimal(str(income))
        tax = Decimal('0')
        previous_bracket = Decimal('0')
        
        for bracket_limit, rate in tax_brackets:
            bracket_limit_decimal = Decimal(str(bracket_limit))
            rate_decimal = Decimal(str(rate))
            
            if income_decimal <= previous_bracket:
                break
            
            # 计算当前税级的应纳税所得额
            taxable_amount = min(income_decimal, bracket_limit_decimal) - previous_bracket
            tax += taxable_amount * rate_decimal
            previous_bracket = bracket_limit_decimal
        
        return tax
    
    print("\n示例2: 税务计算 - 累进税率")
    # 简化的税率表
    # 0-10000: 0%
    # 10000-30000: 10%
    # 30000-70000: 20%
    # 70000-150000: 30%
    # 150000以上: 40%
    tax_brackets = [
        (10000, 0.00),
        (30000, 0.10),
        (70000, 0.20),
        (150000, 0.30),
        (float('inf'), 0.40)
    ]
    
    # 测试不同收入水平
    test_incomes = [5000, 20000, 50000, 100000, 200000]
    
    print("税率表:")
    print("0-10000: 0%")
    print("10000-30000: 10%")
    print("30000-70000: 20%")
    print("70000-150000: 30%")
    print("150000以上: 40%")
    print()
    
    print("不同收入水平的应纳税额:")
    for income in test_incomes:
        tax = calculate_tax(income, tax_brackets)
        effective_rate = tax / Decimal(str(income)) if income > 0 else Decimal('0')
        print(f"收入${income:,.2f}: 税额${tax:,.2f}, 实际税率{effective_rate*100:.2f}%")
    print()
    
    # 示例3: 货币转换和格式化
    def format_currency(amount, currency_code='USD', locale='en_US'):
        """格式化货币
        
        Args:
            amount: 金额
            currency_code: 货币代码
            locale: 区域设置
            
        Returns:
            格式化后的货币字符串
        """
        # 转换为Decimal
        amount_decimal = Decimal(str(amount))
        
        # 确保有两位小数
        rounded_amount = amount_decimal.quantize(Decimal('0.01'))
        
        # 简单的货币符号映射
        currency_symbols = {
            'USD': '$',
            'EUR': '€',
            'GBP': '£',
            'JPY': '¥',
            'CNY': '¥',
            'CAD': 'C$',
            'AUD': 'A$'
        }
        
        symbol = currency_symbols.get(currency_code, currency_code)
        
        # 格式化输出
        # 注意：实际应用中可以使用locale模块进行更复杂的本地化
        parts = str(rounded_amount).split('.')
        integer_part = parts[0]
        decimal_part = parts[1] if len(parts) > 1 else '00'
        
        # 添加千位分隔符
        formatted_integer = ''
        for i, digit in enumerate(reversed(integer_part)):
            if i > 0 and i % 3 == 0:
                formatted_integer = ',' + formatted_integer
            formatted_integer = digit + formatted_integer
        
        # 处理负数
        if formatted_integer.startswith('-'):
            return f"-{symbol}{formatted_integer[1:]}.{decimal_part}"
        else:
            return f"{symbol}{formatted_integer}.{decimal_part}"
    
    print("\n示例3: 货币转换和格式化")
    amounts = [1234.56, -789.12, 0.00, 999999.99]
    currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CNY']
    
    print("不同货币格式:")
    for amount in amounts:
        print(f"\n原始金额: {amount}")
        for currency in currencies:
            formatted = format_currency(amount, currency)
            print(f"  {currency}: {formatted}")
    print()
    
    # 示例4: 高精度科学计算
    def high_precision_calculation():
        """高精度科学计算示例"""
        print("高精度计算1/7 + 1/13:")
        
        # 使用浮点数
        float_result = 1/7 + 1/13
        print(f"浮点数结果: {float_result}")
        print(f"浮点数十六进制表示: {float_result.hex()}")
        
        # 使用Decimal (默认精度)
        default_decimal = Decimal('1')/Decimal('7') + Decimal('1')/Decimal('13')
        print(f"\nDecimal默认精度结果: {default_decimal}")
        
        # 使用高精度Decimal
        with decimal.localcontext() as ctx:
            ctx.prec = 50
            high_precision_decimal = Decimal('1')/Decimal('7') + Decimal('1')/Decimal('13')
            print(f"\nDecimal高精度结果 (50位): {high_precision_decimal}")
        
        # 验证结果
        exact_result = Decimal('20')/Decimal('91')  # 1/7 + 1/13 = 20/91
        print(f"\n精确结果 (20/91): {exact_result}")
        print(f"验证: {default_decimal == exact_result}")
    
    print("\n示例4: 高精度科学计算")
    high_precision_calculation()
    print()
    
    # 示例5: 自定义货币类
    class Money:
        """简单的货币类，使用Decimal进行精确计算"""
        def __init__(self, amount, currency='USD'):
            self.amount = Decimal(str(amount))
            self.currency = currency
        
        def __add__(self, other):
            if isinstance(other, Money):
                if self.currency != other.currency:
                    raise ValueError("不能相加不同货币")
                return Money(self.amount + other.amount, self.currency)
            return Money(self.amount + Decimal(str(other)), self.currency)
        
        def __sub__(self, other):
            if isinstance(other, Money):
                if self.currency != other.currency:
                    raise ValueError("不能相减不同货币")
                return Money(self.amount - other.amount, self.currency)
            return Money(self.amount - Decimal(str(other)), self.currency)
        
        def __mul__(self, other):
            return Money(self.amount * Decimal(str(other)), self.currency)
        
        def __truediv__(self, other):
            return Money(self.amount / Decimal(str(other)), self.currency)
        
        def __repr__(self):
            # 格式化显示两位小数
            return f"{self.currency} {self.amount.quantize(Decimal('0.01'))}"
        
        def format(self):
            """格式化货币显示"""
            return format_currency(self.amount, self.currency)
    
    print("\n示例5: 自定义货币类")
    # 创建货币对象
    price = Money(19.99)
    tax_rate = 0.08
    
    print(f"商品价格: {price.format()}")
    
    # 计算税费
    tax = price * tax_rate
    print(f"税费 (8%): {tax.format()}")
    
    # 计算总价
    total = price + tax
    print(f"总价: {total.format()}")
    
    # 计算折扣价格 (15%折扣)
    discount = price * 0.15
    discounted_price = price - discount
    print(f"折扣 (15%): {discount.format()}")
    print(f"折扣后价格: {discounted_price.format()}")

# 运行实际应用示例
practical_applications()
print()

# 5. 高级用法
print("=== 5. 高级用法 ===")

def advanced_usage():
    """decimal模块的高级用法"""
    print("decimal模块的高级用法:")
    
    # 使用DecimalTuple
    print("\n1. 使用DecimalTuple:")
    # DecimalTuple是Decimal内部表示的底层结构
    # 格式: DecimalTuple(sign, digits, exponent)
    # sign: 0表示正数, 1表示负数
    # digits: 数字元组
    # exponent: 指数
    
    # 手动创建DecimalTuple
    from decimal import DecimalTuple
    dt = DecimalTuple(sign=0, digits=(1, 2, 3, 4), exponent=-2)
    d = Decimal(dt)
    print(f"DecimalTuple(0, (1, 2, 3, 4), -2) = {d}")  # 1234 * 10^-2 = 12.34
    
    # 将Decimal转换为DecimalTuple
    d2 = Decimal('56.78')
    dt2 = d2.as_tuple()
    print(f"Decimal('56.78').as_tuple() = {dt2}")
    print(f"符号: {dt2.sign}, 数字: {dt2.digits}, 指数: {dt2.exponent}")
    print()
    
    # 设置精度和舍入模式的最佳实践
    print("\n2. 设置精度和舍入模式的最佳实践:")
    print("为不同类型的计算设置合适的上下文:")
    
    # 金融计算上下文
    financial_ctx = decimal.Context(prec=28, rounding=decimal.ROUND_HALF_UP)
    print(f"金融计算上下文: 精度={financial_ctx.prec}, 舍入模式={financial_ctx.rounding}")
    
    # 科学计算上下文
    scientific_ctx = decimal.Context(prec=50, rounding=decimal.ROUND_HALF_EVEN)
    print(f"科学计算上下文: 精度={scientific_ctx.prec}, 舍入模式={scientific_ctx.rounding}")
    
    # 税务计算上下文
    tax_ctx = decimal.Context(prec=38, rounding=decimal.ROUND_HALF_UP)
    print(f"税务计算上下文: 精度={tax_ctx.prec}, 舍入模式={tax_ctx.rounding}")
    print()
    
    # 使用预设上下文
    print("\n3. 使用预设上下文:")
    print("decimal模块提供了几个预设上下文:")
    
    # 获取预设上下文
    basic_ctx = decimal.BasicContext
    extended_ctx = decimal.ExtendedContext
    default_ctx = decimal.DefaultContext
    
    print(f"BasicContext: 精度={basic_ctx.prec}, 舍入模式={basic_ctx.rounding}")
    print(f"ExtendedContext: 精度={extended_ctx.prec}, 舍入模式={extended_ctx.rounding}")
    print(f"DefaultContext: 精度={default_ctx.prec}, 舍入模式={default_ctx.rounding}")
    print()
    
    # 异常处理
    print("\n4. 异常处理:")
    print("decimal模块定义了以下异常:")
    print("- DecimalException: 所有decimal异常的基类")
    print("- Clamped: 指数被限制到允许的范围内")
    print("- Inexact: 结果无法精确表示")
    print("- Rounded: 结果被舍入")
    print("- Subnormal: 结果是一个非常小的数")
    print("- Underflow: 结果小于最小可表示的正数")
    print("- Overflow: 结果溢出")
    print("- DivisionByZero: 除以零")
    print("- InvalidOperation: 无效操作")
    
    # 异常处理示例
    print("\n处理InvalidOperation异常:")
    try:
        # 无效操作：计算负数的平方根
        result = Decimal('-1').sqrt()
    except decimal.InvalidOperation:
        print("捕获到InvalidOperation异常: 无法计算负数的平方根")
    print()
    
    # 陷阱和标志
    print("\n5. 陷阱和标志:")
    print("decimal模块允许设置陷阱(traps)和标志(flags)来控制异常行为:")
    
    # 使用标志检测条件
    with decimal.localcontext() as ctx:
        # 清除所有标志
        ctx.clear_flags()
        
        # 执行可能导致舍入的操作
        result = Decimal('1') / Decimal('3')
        
        # 检查标志
        print(f"Inexact标志: {ctx.flags[decimal.Inexact]}")
        print(f"Rounded标志: {ctx.flags[decimal.Rounded]}")
        print(f"Overflow标志: {ctx.flags[decimal.Overflow]}")
    print()
    
    # 创建自定义上下文
    print("\n6. 创建自定义上下文:")
    # 创建用于金融计算的上下文
    financial_context = decimal.Context(
        prec=28,
        rounding=decimal.ROUND_HALF_UP,
        traps=[
            decimal.DivisionByZero,
            decimal.InvalidOperation,
            decimal.Overflow
        ],
        flags=[
            decimal.Clamped,
            decimal.Inexact,
            decimal.Rounded
        ]
    )
    
    print(f"自定义金融计算上下文:")
    print(f"  精度: {financial_context.prec}")
    print(f"  舍入模式: {financial_context.rounding}")
    print(f"  陷阱: {[trap.__name__ for trap in financial_context.traps if financial_context.traps[trap]]}")
    print(f"  标志: {[flag.__name__ for flag in financial_context.flags if financial_context.flags[flag]]}")

# 运行高级用法示例
advanced_usage()
print()

# 6. 最佳实践和注意事项
print("=== 6. 最佳实践和注意事项 ===")

def best_practices():
    """decimal模块使用的最佳实践和注意事项"""
    print("decimal模块使用的最佳实践和注意事项:")
    
    # 1. 从字符串创建Decimal对象
    print("\n1. 从字符串创建Decimal对象:")
    print("   - 最佳实践: 始终从字符串创建Decimal对象，避免从浮点数创建")
    print("   - 原因: 浮点数本身可能有精度问题，会被Decimal保留")
    
    # 演示问题
    print("   - 示例:")
    print(f"     从浮点数创建: Decimal(0.1) = {Decimal(0.1)}")
    print(f"     从字符串创建: Decimal('0.1') = {Decimal('0.1')}")
    print()
    
    # 2. 避免混合使用浮点数和Decimal
    print("\n2. 避免混合使用浮点数和Decimal:")
    print("   - 最佳实践: 同一计算中应统一使用Decimal类型")
    print("   - 原因: 混合使用会导致精度问题，并且会触发隐式转换")
    
    print("   - 错误示例:")
    d = Decimal('10.0')
    f = 0.1
    print(f"     Decimal('10.0') + 0.1 = {d + f}")  # 会触发警告
    
    print("   - 正确示例:")
    d = Decimal('10.0')
    d2 = Decimal('0.1')
    print(f"     Decimal('10.0') + Decimal('0.1') = {d + d2}")
    print()
    
    # 3. 正确设置精度和舍入模式
    print("\n3. 正确设置精度和舍入模式:")
    print("   - 最佳实践: 根据计算类型设置合适的精度和舍入模式")
    print("   - 常用场景:")
    print("     - 金融计算: 精度28, 舍入模式ROUND_HALF_UP")
    print("     - 科学计算: 精度根据需要, 舍入模式ROUND_HALF_EVEN")
    print("     - 税务计算: 精度38, 舍入模式ROUND_HALF_UP")
    print()
    
    # 4. 使用quantize方法进行精度控制
    print("\n4. 使用quantize方法进行精度控制:")
    print("   - 最佳实践: 使用quantize方法明确控制结果的小数位数")
    print("   - 示例:")
    d = Decimal('123.456789')
    print(f"     原始值: {d}")
    print(f"     两位小数: {d.quantize(Decimal('0.00'))}")
    print(f"     零位小数: {d.quantize(Decimal('1'))}")
    print(f"     三位小数: {d.quantize(Decimal('0.000'))}")
    print()
    
    # 5. 使用localcontext进行临时设置
    print("\n5. 使用localcontext进行临时设置:")
    print("   - 最佳实践: 使用localcontext()上下文管理器临时修改计算上下文")
    print("   - 好处: 避免全局设置影响其他代码，自动恢复原始设置")
    print()
    
    # 6. 处理NaN和Infinity
    print("\n6. 处理NaN和Infinity:")
    print("   - 最佳实践: 在可能产生特殊值的计算中检查结果")
    print("   - 注意事项:")
    print("     - NaN不等于任何值，包括它自己")
    print("     - 应使用is_nan()和is_infinite()方法检测特殊值")
    print()
    
    # 7. 性能考虑
    print("\n7. 性能考虑:")
    print("   - 注意事项: Decimal运算比浮点数运算慢")
    print("   - 建议:")
    print("     - 在不需要高精度的场景中，使用浮点数")
    print("     - 在需要高精度的场景中（如金融计算），使用Decimal")
    print("     - 避免在性能关键路径上频繁创建Decimal对象")
    print()
    
    # 8. 序列化和反序列化
    print("\n8. 序列化和反序列化:")
    print("   - 最佳实践: 序列化时转换为字符串，反序列化时从字符串创建")
    print("   - JSON序列化示例:")
    print("""
    import json
    from decimal import Decimal
    
    class DecimalJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Decimal):
                return str(obj)
            return super().default(obj)
    
    class DecimalJSONDecoder(json.JSONDecoder):
        def decode(self, s):
            result = super().decode(s)
            return self._convert_decimals(result)
        
        def _convert_decimals(self, obj):
            if isinstance(obj, str):
                try:
                    # 尝试转换为Decimal
                    return Decimal(obj)
                except:
                    return obj
            elif isinstance(obj, dict):
                return {k: self._convert_decimals(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [self._convert_decimals(item) for item in obj]
            else:
                return obj
    """)
    print()
    
    # 9. 常见陷阱
    print("\n9. 常见陷阱:")
    print("   - 陷阱1: 从浮点数创建Decimal，继承了浮点数的精度问题")
    print("   - 陷阱2: 忽略精度设置，导致结果精度不足")
    print("   - 陷阱3: 忘记使用quantize进行结果舍入")
    print("   - 陷阱4: 混合使用不同精度或舍入模式的上下文")
    print("   - 陷阱5: 没有处理可能的异常情况（如除以零）")
    print()
    
    # 10. 代码示例：高性能Decimal使用模式
    print("\n10. 示例：高性能Decimal使用模式:")
    print("""
    # 预创建常用的Decimal常量
    ONE = Decimal('1')
    TEN = Decimal('10')
    HUNDRED = Decimal('100')
    ZERO = Decimal('0')
    TWO_PLACES = Decimal('0.01')
    
    # 在计算中重用这些常量
    def calculate_percentage(value, percent):
        """计算百分比，结果保留两位小数"""
        value_dec = Decimal(str(value))
        percent_dec = Decimal(str(percent))
        # 使用预创建的常量
        result = (value_dec * percent_dec) / HUNDRED
        # 明确设置精度
        return result.quantize(TWO_PLACES)
    """)

# 运行最佳实践示例
best_practices()

# 总结
print("\n=== 总结 ===")
print("decimal模块提供了高精度的十进制浮点数运算，是Python中处理金融计算和需要精确小数表示的重要工具。")
print("主要功能和优势包括：")
print("1. 精确表示十进制小数，避免浮点数精度问题")
print("2. 可配置的精度和舍入模式，适应不同场景需求")
print("3. 丰富的数学函数和转换方法")
print("4. 上下文管理系统，支持全局和局部设置")
print("5. 完整的异常处理机制")
print()
print("在使用decimal模块时，需要注意性能开销，并遵循最佳实践，特别是从字符串创建Decimal对象、")
print("适当设置精度和舍入模式、使用quantize控制小数位数等。")
print()
print("decimal模块广泛应用于金融、税务、科学计算等领域，")
print("是需要高精度计算时的首选工具。")

# 运行完整演示
if __name__ == "__main__":
    print("Python decimal模块演示\n")
    print("请参考源代码中的详细示例和说明")