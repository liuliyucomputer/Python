# Python decimal模块详解

import decimal
from decimal import Decimal, getcontext, setcontext

# 1. 模块概述
print("=== 1. decimal模块概述 ===")
print("decimal模块提供了十进制浮点数运算，用于需要高精度计算的场景，如金融计算。")
print("该模块的主要特点：")
print("- 高精度十进制浮点数表示")
print("- 可配置的精度和舍入模式")
print("- 精确的十进制算术运算")
print("- 货币计算支持")
print("- 与二进制浮点数的转换")
print()

# 2. Decimal对象的创建
print("=== 2. Decimal对象的创建 ===")

# 从整数创建
print(f"Decimal(10) = {Decimal(10)}")

# 从字符串创建（推荐方式，避免精度损失）
print(f"Decimal('10.5') = {Decimal('10.5')}")

# 从浮点数创建（可能有精度问题）
print(f"Decimal(10.5) = {Decimal(10.5)}")
print(f"Decimal(0.1) = {Decimal(0.1)}")
print(f"Decimal('0.1') = {Decimal('0.1')}")

# 从元组创建
print(f"Decimal((0, (3, 1, 4), -2)) = {Decimal((0, (3, 1, 4), -2))}")  # 0.314

# 使用常量
print(f"Decimal.from_float(0.1) = {Decimal.from_float(0.1)}")
print(f"Decimal.from_float(math.pi) = {Decimal.from_float(math.pi)}")
print()

# 3. 上下文设置
print("=== 3. 上下文设置 ===")

# 获取当前上下文
ctx = getcontext()
print(f"当前上下文: {ctx}")

# 查看当前精度
print(f"当前精度: {ctx.prec}")

# 查看当前舍入模式
print(f"当前舍入模式: {ctx.rounding}")

# 设置精度
ctx.prec = 28
print(f"设置精度为28: {ctx.prec}")

# 设置舍入模式
print(f"可用的舍入模式:")
for attr in dir(decimal):
    if attr.startswith('ROUND_'):
        print(f"- {attr}: {getattr(decimal, attr)}")

# 设置舍入模式为ROUND_HALF_UP（四舍五入）
ctx.rounding = decimal.ROUND_HALF_UP
print(f"设置舍入模式为ROUND_HALF_UP: {ctx.rounding}")
print()

# 4. 基本算术运算
print("=== 4. 基本算术运算 ===")

# 创建Decimal对象
a = Decimal('10.5')
b = Decimal('3.2')

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

# 平方根
print(f"a.sqrt() = {a.sqrt()}")
print()

# 5. 精度和舍入
print("=== 5. 精度和舍入 ===")

# 重置上下文
setcontext(decimal.Context(prec=10, rounding=decimal.ROUND_HALF_UP))
ctx = getcontext()
print(f"上下文重置: 精度={ctx.prec}, 舍入模式={ctx.rounding}")

# 演示精度限制
x = Decimal('1') / Decimal('3')
print(f"1/3 （精度10）: {x}")

# 更改精度
ctx.prec = 20
x = Decimal('1') / Decimal('3')
print(f"1/3 （精度20）: {x}")

# 演示不同舍入模式的效果
setcontext(decimal.Context(prec=2))
values = [Decimal('2.35'), Decimal('2.45'), Decimal('-2.35'), Decimal('-2.45')]

print(f"\n不同舍入模式对数值的影响（精度=2）:")
for rounding_mode in [decimal.ROUND_DOWN, decimal.ROUND_UP, decimal.ROUND_CEILING, 
                     decimal.ROUND_FLOOR, decimal.ROUND_HALF_UP, decimal.ROUND_HALF_DOWN, 
                     decimal.ROUND_HALF_EVEN, decimal.ROUND_05UP]:
    ctx.rounding = rounding_mode
    results = [f"{ctx.create_decimal(value).quantize(Decimal('1.0'))}" for value in values]
    print(f"{rounding_mode:<25} -> {', '.join(results)}")

# 重置上下文到默认设置
setcontext(decimal.Context())
print()

# 6. 货币计算示例
print("=== 6. 货币计算示例 ===")

# 设置适合货币计算的上下文
money_ctx = decimal.Context(prec=28, rounding=decimal.ROUND_HALF_UP)
setcontext(money_ctx)

# 价格和数量
price = Decimal('19.99')
quantity = Decimal('3')
discount = Decimal('0.10')
tax_rate = Decimal('0.08')

# 计算小计
subtotal = price * quantity
print(f"单价: ${price}")
print(f"数量: {quantity}")
print(f"小计: ${subtotal}")

# 计算折扣
discount_amount = subtotal * discount
print(f"折扣率: {discount * 100}%")
print(f"折扣金额: ${discount_amount}")

# 计算折扣后金额
discounted_total = subtotal - discount_amount
print(f"折扣后金额: ${discounted_total}")

# 计算税费
tax = discounted_total * tax_rate
print(f"税率: {tax_rate * 100}%")
print(f"税费: ${tax}")

# 计算总金额
total = discounted_total + tax
print(f"总金额: ${total}")

# 精确格式化
print(f"\n格式化输出:")
print(f"总金额: ${total.quantize(Decimal('0.00'))}")
print()

# 7. 与其他数值类型的转换
print("=== 7. 与其他数值类型的转换 ===")

# Decimal转整数
x = Decimal('10.99')
print(f"Decimal('10.99')转整数: {int(x)}")

# Decimal转浮点数
print(f"Decimal('10.99')转浮点数: {float(x)}")

# 浮点数转Decimal（精确方法）
f = 0.1
print(f"浮点数0.1转Decimal: {Decimal.from_float(f)}")
print(f"浮点数0.1的精确表示: {repr(f)}")

# 字符串转Decimal
print(f"字符串'123.456'转Decimal: {Decimal('123.456')}")

# 列表转Decimal列表
float_list = [1.1, 2.2, 3.3]
decimal_list = [Decimal.from_float(f) for f in float_list]
print(f"浮点数列表{float_list}转Decimal列表: {decimal_list}")
print()

# 8. 比较运算
print("=== 8. 比较运算 ===")

# 创建Decimal对象
x = Decimal('10.5')
y = Decimal('10.50')
z = Decimal('10.6')

# 相等比较
print(f"x == y: {x == y}")  # True，因为值相等
print(f"x == z: {x == z}")  # False

# 大小比较
print(f"x < z: {x < z}")    # True
print(f"x > z: {x > z}")    # False
print(f"x <= y: {x <= y}")  # True
print(f"x >= z: {x >= z}")  # False

# 与其他类型比较
print(f"x == 10.5: {x == 10.5}")  # True
print(f"x > 10: {x > 10}")        # True
print()

# 9. 特殊值和常量
print("=== 9. 特殊值和常量 ===")

# 零
print(f"Decimal('0') = {Decimal('0')}")
print(f"Decimal('-0') = {Decimal('-0')}")

# 无穷大
print(f"Decimal('Infinity') = {Decimal('Infinity')}")
print(f"Decimal('-Infinity') = {Decimal('-Infinity')}")

# 非数字
print(f"Decimal('NaN') = {Decimal('NaN')}")

# 检查特殊值
x = Decimal('Infinity')
y = Decimal('NaN')
print(f"\n检查特殊值:")
print(f"x.is_infinite(): {x.is_infinite()}")
print(f"x.is_finite(): {x.is_finite()}")
print(f"y.is_nan(): {y.is_nan()}")
print(f"Decimal('0').is_zero(): {Decimal('0').is_zero()}")
print(f"Decimal('-0').is_signed(): {Decimal('-0').is_signed()}")
print()

# 10. 数学函数
print("=== 10. 数学函数 ===")

x = Decimal('2')
y = Decimal('8')

# 平方根
print(f"y.sqrt() = {y.sqrt()}")

# 自然对数
print(f"y.ln() = {y.ln()}")

# 常用对数
print(f"y.log10() = {y.log10()}")

# 指数函数
print(f"x.exp() = {x.exp()}")

# 幂函数
print(f"x.pow(y) = {x.pow(y)}")

# 整数根
print(f"y.root(3) = {y.root(3)}")  # 立方根
print()

# 11. 格式化输出
print("=== 11. 格式化输出 ===")

# 创建Decimal对象
x = Decimal('1234.56789')

# 基本格式化
print(f"基本格式: {x}")

# 使用format方法
print(f"format(x, '.2f'): {format(x, '.2f')}")  # 保留两位小数
print(f"format(x, ',.2f'): {format(x, ',.2f')}")  # 添加千位分隔符
print(f"format(x, '+.2f'): {format(x, '+.2f')}")  # 显示正负号

# 使用字符串格式化
print(f"字符串格式化: ${x:.2f}")

# 科学计数法
print(f"科学计数法: {format(x, '.2e')}")

# 工程计数法
print(f"工程计数法: {format(x, '.2E')}")

# 百分比格式
print(f"百分比格式: {format(x * Decimal('0.01'), '.2%')}")
print()

# 12. 货币计算最佳实践
print("=== 12. 货币计算最佳实践 ===")

# 1. 始终从字符串创建Decimal对象
print("1. 推荐从字符串创建:")
print(f"Decimal('0.1') + Decimal('0.2') = {Decimal('0.1') + Decimal('0.2')}")
print(f"Decimal(0.1) + Decimal(0.2) = {Decimal(0.1) + Decimal(0.2)}")

# 2. 使用quantize方法进行舍入
print("\n2. 使用quantize方法进行舍入:")
price = Decimal('19.99')
tax_rate = Decimal('0.0825')
tax = price * tax_rate
print(f"税额（未舍入）: {tax}")
print(f"税额（舍入到分）: {tax.quantize(Decimal('0.00'), rounding=decimal.ROUND_HALF_UP)}")

# 3. 使用固定精度
print("\n3. 使用固定精度:")
setcontext(decimal.Context(prec=28, rounding=decimal.ROUND_HALF_UP))

# 4. 避免使用浮点数
print("\n4. 避免使用浮点数:")
try:
    total = Decimal(0.1) + Decimal(0.2)
    print(f"使用浮点数创建的结果: {total}")
except Exception as e:
    print(f"错误: {e}")

# 13. 性能比较
print("\n=== 13. 性能比较 ===")
import time

def test_performance():
    """测试Decimal与float的性能比较"""
    
    # 生成测试数据
    n = 1000000
    
    # 测试float运算
    start = time.time()
    total = 0.0
    for i in range(n):
        total += 0.1
    time_float = time.time() - start
    
    # 测试Decimal运算
    start = time.time()
    total_decimal = Decimal('0')
    for i in range(n):
        total_decimal += Decimal('0.1')
    time_decimal = time.time() - start
    
    print(f"float运算时间: {time_float:.4f}秒")
    print(f"Decimal运算时间: {time_decimal:.4f}秒")
    print(f"Decimal比float慢{time_decimal/time_float:.2f}倍")

# 运行性能测试
test_performance()

# 14. 实际应用示例
print("\n=== 14. 实际应用示例 ===")

# 示例1：复利计算
def compound_interest(principal, rate, years, compounded_annually):
    """计算复利
    
    Args:
        principal: 本金
        rate: 年利率
        years: 年数
        compounded_annually: 每年复利次数
        
    Returns:
        最终金额
    """
    principal = Decimal(str(principal))
    rate = Decimal(str(rate))
    
    amount = principal * (1 + rate / compounded_annually) ** (compounded_annually * years)
    return amount.quantize(Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)

# 计算复利
principal = 10000
rate = 0.05
years = 10
compounded_annually = 12  # 每月复利

final_amount = compound_interest(principal, rate, years, compounded_annually)
print(f"\n复利计算示例:")
print(f"本金: ${principal}")
print(f"年利率: {rate * 100}%")
print(f"年数: {years}")
print(f"每年复利次数: {compounded_annually}")
print(f"最终金额: ${final_amount}")

# 示例2：汇率转换
def convert_currency(amount, exchange_rate, fee_rate=0.005):
    """货币转换
    
    Args:
        amount: 金额
        exchange_rate: 汇率
        fee_rate: 手续费率
        
    Returns:
        转换后的金额（扣除手续费）
    """
    amount = Decimal(str(amount))
    exchange_rate = Decimal(str(exchange_rate))
    fee_rate = Decimal(str(fee_rate))
    
    converted = amount * exchange_rate
    fee = converted * fee_rate
    final_amount = converted - fee
    
    return final_amount.quantize(Decimal('0.01'), rounding=decimal.ROUND_HALF_UP)

# 货币转换
usd_amount = 1000
exchange_rate = 6.5  # 1 USD = 6.5 CNY
fee_rate = 0.005     # 0.5%手续费

rmb_amount = convert_currency(usd_amount, exchange_rate, fee_rate)
print(f"\n货币转换示例:")
print(f"美元金额: ${usd_amount}")
print(f"汇率: 1 USD = {exchange_rate} CNY")
print(f"手续费率: {fee_rate * 100}%")
print(f"人民币金额: ¥{rmb_amount}")

# 15. 与浮点数的比较
print("\n=== 15. 与浮点数的比较 ===")

# 创建数值
x_decimal = Decimal('0.1') + Decimal('0.2')
x_float = 0.1 + 0.2

print(f"Decimal('0.1') + Decimal('0.2') = {x_decimal}")
print(f"0.1 + 0.2 = {x_float}")
print(f"x_decimal == Decimal('0.3'): {x_decimal == Decimal('0.3')}")
print(f"x_float == 0.3: {x_float == 0.3}")
print(f"x_decimal == x_float: {x_decimal == x_float}")

# 16. 总结
print("\n=== 16. decimal模块总结 ===")
print("decimal模块提供了高精度的十进制浮点数运算，适用于需要精确计算的场景。")
print("主要优势：")
print("- 精确表示十进制数，避免二进制浮点数的精度问题")
print("- 可配置的精度和舍入模式")
print("- 全面的数学函数支持")
print("- 适合金融计算和货币处理")
print()
print("主要劣势：")
print("- 比浮点数运算慢")
print("- 内存占用更大")
print("- 语法稍复杂")
print()
print("使用建议：")
print("- 在需要高精度的场景（如金融、货币计算）中使用")
print("- 始终从字符串创建Decimal对象")
print("- 使用quantize方法进行精确舍入")
print("- 对于性能要求高的科学计算，考虑使用numpy")
