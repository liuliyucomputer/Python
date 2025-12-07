# Python random模块详解

import random
import string

# 1. 模块概述
print("=== 1. random模块概述 ===")
print("random模块提供了生成随机数和随机选择的功能，用于模拟、游戏、密码学等场景。")
print("该模块的主要特点：")
print("- 伪随机数生成器（PRNG）")
print("- 丰富的随机数分布支持")
print("- 随机选择和打乱功能")
print("- 可种子化以重现结果")
print()

# 2. 随机数生成器的种子设置
print("=== 2. 随机数生成器的种子设置 ===")

# 设置种子（使用相同种子可重现相同的随机序列）
random.seed(42)
print("设置种子为42后生成的随机数序列：")
for i in range(5):
    print(f"  random() = {random.random()}")

# 重新设置种子并再次生成
random.seed(42)
print("\n再次设置种子为42后生成的随机数序列（相同）：")
for i in range(5):
    print(f"  random() = {random.random()}")

# 使用系统时间作为种子（默认行为）
random.seed()  # 不传递参数使用系统时间
print("\n使用系统时间作为种子后生成的随机数：")
print(f"  random() = {random.random()}")

# 使用其他类型的种子
random.seed("hello")
print(f"\n使用字符串'hello'作为种子：")
print(f"  random() = {random.random()}")

random.seed(b"bytes")
print(f"\n使用字节串b'bytes'作为种子：")
print(f"  random() = {random.random()}")
print()

# 3. 基本随机数函数
print("=== 3. 基本随机数函数 ===")

# random(): 生成0.0到1.0之间的浮点数
print(f"random.random() = {random.random()}")

# uniform(a, b): 生成a到b之间的浮点数
print(f"random.uniform(1, 10) = {random.uniform(1, 10)}")
print(f"random.uniform(10, 1) = {random.uniform(10, 1)}")  # a > b时仍能正常工作

# randint(a, b): 生成a到b之间的整数（包括a和b）
print(f"random.randint(1, 10) = {random.randint(1, 10)}")

# randrange(start, stop[, step]): 生成指定范围内的整数
print(f"random.randrange(1, 10) = {random.randrange(1, 10)}")  # 1到9之间的整数
print(f"random.randrange(1, 10, 2) = {random.randrange(1, 10, 2)}")  # 1到9之间的奇数
print(f"random.randrange(10) = {random.randrange(10)}")  # 0到9之间的整数

# getrandbits(k): 生成k位的随机整数
print(f"random.getrandbits(10) = {random.getrandbits(10)}")
print(f"random.getrandbits(32) = {random.getrandbits(32)}")
print()

# 4. 随机选择和打乱
print("=== 4. 随机选择和打乱 ===")

# choice(seq): 从序列中随机选择一个元素
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"random.choice({fruits}) = {random.choice(fruits)}")

# choices(seq, weights=None, *, cum_weights=None, k=1): 从序列中随机选择k个元素（有放回）
print(f"random.choices({fruits}, k=3) = {random.choices(fruits, k=3)}")

# 带权重的随机选择
weights = [5, 1, 1, 1, 1]  # apple被选中的概率是其他水果的5倍
print(f"random.choices({fruits}, weights={weights}, k=10) = {random.choices(fruits, weights=weights, k=10)}")

# sample(seq, k): 从序列中随机选择k个元素（无放回）
print(f"random.sample({fruits}, k=3) = {random.sample(fruits, k=3)}")

# shuffle(seq): 打乱序列（原地修改）
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(f"原始序列: {cards}")
random.shuffle(cards)
print(f"打乱后: {cards}")
print()

# 5. 分布随机数
print("=== 5. 分布随机数 ===")

# 正态分布（高斯分布）
print(f"随机.normalvariate(mean=0, stddev=1) = {random.normalvariate(0, 1)}")

# 对数正态分布
print(f"random.lognormvariate(mu=0, sigma=1) = {random.lognormvariate(0, 1)}")

# 指数分布
print(f"random.expovariate(lambd=1) = {random.expovariate(1)}")

# 伽马分布
print(f"random.gammavariate(alpha=2, beta=3) = {random.gammavariate(2, 3)}")

# 贝塔分布
print(f"random.betavariate(alpha=2, beta=5) = {random.betavariate(2, 5)}")

# 帕累托分布
print(f"random.paretovariate(alpha=1) = {random.paretovariate(1)}")

# 威布尔分布
print(f"random.weibullvariate(alpha=1, beta=2) = {random.weibullvariate(1, 2)}")

# 三角形分布
print(f"random.triangular(low=0, high=10, mode=5) = {random.triangular(0, 10, 5)}")

# 均匀分布（与uniform函数相同）
print(f"random.uniform(0, 10) = {random.uniform(0, 10)}")
print()

# 6. 实际应用示例
print("=== 6. 实际应用示例 ===")

# 示例1：生成随机密码
def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """生成随机密码"""
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("至少需要选择一种字符类型")
    
    # 确保密码包含至少一种选中类型的字符
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    
    # 填充剩余长度
    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choices(characters, k=remaining_length))
    
    # 打乱密码
    random.shuffle(password)
    return ''.join(password)

# 生成密码
print("生成随机密码：")
print(f"- 长度12，包含所有字符类型: {generate_password()}")
print(f"- 长度16，只包含字母和数字: {generate_password(16, use_symbols=False)}")
print(f"- 长度8，只包含小写字母: {generate_password(8, use_uppercase=False, use_digits=False, use_symbols=False)}")

# 示例2：模拟骰子掷骰
def roll_dice(num_dice=1, num_sides=6):
    """模拟掷骰子"""
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results, sum(results)

print("\n模拟骰子掷骰：")
for i in range(5):
    rolls, total = roll_dice(2)
    print(f"  掷2个6面骰子: {rolls} -> 总和: {total}")

# 示例3：生成随机电话号码
def generate_phone_number(country_code='+1', area_code=None):
    """生成随机电话号码"""
    if area_code is None:
        area_code = random.randint(200, 999)  # 有效的美国区号范围
    
    # 中间3位和最后4位
    exchange_code = random.randint(200, 999)
    line_number = random.randint(1000, 9999)
    
    return f"{country_code} {area_code}-{exchange_code}-{line_number}"

print("\n生成随机电话号码：")
for _ in range(3):
    print(f"  {generate_phone_number()}")

# 示例4：随机生成IP地址
def generate_ip_address():
    """生成随机IP地址"""
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))

print("\n生成随机IP地址：")
for _ in range(3):
    print(f"  {generate_ip_address()}")
print()

# 7. 随机数生成器对象
print("=== 7. 随机数生成器对象 ===")

# 创建独立的随机数生成器
rng1 = random.Random(42)
rng2 = random.Random(42)

print("两个使用相同种子的独立随机数生成器：")
for _ in range(3):
    print(f"  rng1: {rng1.random()}, rng2: {rng2.random()}")

# 独立生成器的好处：不影响全局随机数序列
print("\n使用全局生成器和独立生成器：")
random.seed(100)
rng = random.Random(100)

print(f"全局生成器: {random.random()}")
print(f"独立生成器: {rng.random()}")
print(f"再次使用全局生成器: {random.random()}")
print(f"再次使用独立生成器: {rng.random()}")
print()

# 8. 加密安全的随机数
print("=== 8. 加密安全的随机数 ===")

# random模块的随机数不适合加密用途
print("注意：random模块的随机数生成器不适合加密或安全敏感的应用！")
print("对于加密用途，请使用secrets模块：")

# 展示secrets模块的基本用法
import secrets

print(f"secrets.randbelow(100) = {secrets.randbelow(100)}")  # 生成0到99之间的随机整数
print(f"secrets.randbits(16) = {secrets.randbits(16)}")      # 生成16位随机整数
print(f"secrets.choice({fruits}) = {secrets.choice(fruits)}")  # 从序列中随机选择元素

# 生成加密安全的随机密码
secure_password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(16))
print(f"secrets生成的安全密码: {secure_password}")
print()

# 9. 性能考虑
print("=== 9. 性能考虑 ===")

import time

def test_performance():
    """测试随机数生成性能"""
    n = 1000000
    
    # 测试random.random()
    start = time.time()
    for _ in range(n):
        random.random()
    time_random = time.time() - start
    
    # 测试random.randint()
    start = time.time()
    for _ in range(n):
        random.randint(1, 100)
    time_randint = time.time() - start
    
    # 测试random.choice()
    start = time.time()
    for _ in range(n):
        random.choice(fruits)
    time_choice = time.time() - start
    
    # 测试random.shuffle()
    start = time.time()
    for _ in range(n // 100):  # 减少迭代次数以节省时间
        temp = fruits.copy()
        random.shuffle(temp)
    time_shuffle = time.time() - start
    
    print(f"random.random(): {time_random:.4f}秒/{n}次")
    print(f"random.randint(): {time_randint:.4f}秒/{n}次")
    print(f"random.choice(): {time_choice:.4f}秒/{n}次")
    print(f"random.shuffle(): {time_shuffle:.4f}秒/{n//100}次")

print("简化性能测试（100000次迭代）:")
test_performance()
print()

# 10. 最佳实践
print("=== 10. 最佳实践 ===")

print("1. 为了可重现性，在测试时设置固定种子：")
print("   random.seed(42)  # 确保测试结果可重现")

print("\n2. 对于加密或安全敏感的应用，使用secrets模块：")
print("   import secrets")
print("   secure_token = secrets.token_hex(16)")

print("\n3. 避免在循环中多次调用random()生成大范围随机数：")
print("   # 不推荐：")
print("   for i in range(1000):")
print("       x = random.randint(0, 1000000)")
print("   # 可以接受，但secrets更安全")

print("\n4. 对于大量随机数生成，考虑使用numpy.random：")
print("   import numpy as np")
print("   random_numbers = np.random.rand(1000000)")

print("\n5. 使用sample()而不是shuffle()来获取序列的随机子集：")
print("   # 获取列表的3个随机元素")
print("   random.sample(my_list, 3)")

print("\n6. 使用choices()进行有放回的随机选择：")
print("   # 随机选择5个元素，允许重复")
print("   random.choices(my_list, k=5)")
print()

# 11. 常见错误和陷阱
print("=== 11. 常见错误和陷阱 ===")

print("1. 忘记random()返回的是[0.0, 1.0)区间的浮点数：")
print("   # 错误：想要1-10的整数")
print("   x = random.random() * 10  # 返回0.0-10.0的浮点数")
print("   # 正确：")
print("   x = random.randint(1, 10)  # 返回1-10的整数")

print("\n2. 误用randrange()和randint()的参数范围：")
print("   random.randrange(1, 10)  # 返回1-9的整数")
print("   random.randint(1, 10)    # 返回1-10的整数")

print("\n3. 对不可变序列使用shuffle()：")
print("   # 错误：字符串是不可变的")
print("   s = 'hello'")
print("   random.shuffle(s)  # 会抛出TypeError")
print("   # 正确：")
print("   s_list = list(s)")
print("   random.shuffle(s_list)")
print("   s_shuffled = ''.join(s_list)")

print("\n4. 使用random模块进行加密：")
print("   # 错误：random模块的随机数不够安全")
print("   secure_token = ''.join(random.choice(string.hexdigits) for _ in range(32))")
print("   # 正确：")
print("   import secrets")
print("   secure_token = secrets.token_hex(16)")

print("\n5. 假设random.choices()返回的是无放回的样本：")
print("   # random.choices()是有放回的")
print("   sample = random.choices(range(5), k=3)  # 可能包含重复值")
print("   # random.sample()是无放回的")
print("   sample = random.sample(range(5), k=3)    # 不包含重复值")
print()

# 12. 总结
print("=== 12. random模块总结 ===")
print("random模块提供了丰富的随机数生成功能，适用于各种非安全敏感的应用场景。")
print("主要功能包括：")
print("- 基本随机数生成（random(), uniform(), randint()等）")
print("- 随机选择和打乱（choice(), sample(), shuffle()等）")
print("- 多种概率分布支持（normalvariate(), expovariate()等）")
print("- 可配置的种子和独立的随机数生成器")
print()
print("使用建议：")
print("- 在需要可重现结果的场景中设置固定种子")
print("- 对于加密或安全敏感的应用，使用secrets模块")
print("- 根据具体需求选择合适的随机数函数")
print("- 对于高性能需求，考虑使用numpy.random")
print("- 注意区分有放回和无放回的随机选择")
