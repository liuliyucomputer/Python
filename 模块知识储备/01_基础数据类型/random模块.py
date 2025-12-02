# random模块 - 随机数生成库
# 功能作用：提供各种随机数生成器和随机选择功能
# 使用情景：游戏开发、模拟实验、密码学（需谨慎使用）、数据分析采样、随机化算法等
# 注意事项：random模块生成的是伪随机数；默认情况下不适合用于安全敏感的应用；可通过seed()函数设置随机种子以复现结果

import random
import math
import time

# 模块概述
"""
random模块实现了各种分布的伪随机数生成器，提供了丰富的随机数相关功能：

1. 基本随机数生成：生成0到1之间的随机浮点数
2. 整数随机数：生成指定范围内的随机整数
3. 序列随机化：随机打乱序列或从序列中随机选择元素
4. 分布随机数：生成各种概率分布的随机数（均匀分布、正态分布等）
5. 随机种子管理：设置和获取随机种子以控制随机数生成

该模块中的函数适用于大多数常见的随机数生成需求，但请注意，它不适合用于加密目的。
对于加密安全的随机数生成，应使用secrets模块。
"""

# 1. 随机种子设置和管理
print("=== 1. 随机种子设置和管理 ===")

def seed_management():
    """随机种子设置和管理示例"""
    print("随机种子设置和管理:")
    
    # 默认随机数生成
    print("\n1. 默认随机数生成:")
    print(f"默认随机浮点数 (0-1): {random.random()}")
    print(f"默认随机整数 (1-10): {random.randint(1, 10)}")
    print()
    
    # 设置固定随机种子
    print("\n2. 设置固定随机种子:")
    print("设置随机种子为42后生成的随机数:")
    random.seed(42)
    print(f"随机浮点数 (0-1): {random.random()}")
    print(f"随机整数 (1-10): {random.randint(1, 10)}")
    print(f"随机浮点数 (0-1): {random.random()}")
    print()
    
    # 重置随机种子，再次生成相同序列
    print("\n3. 重置随机种子，生成相同序列:")
    random.seed(42)
    print(f"随机浮点数 (0-1): {random.random()}")  # 与上面相同
    print(f"随机整数 (1-10): {random.randint(1, 10)}")  # 与上面相同
    print(f"随机浮点数 (0-1): {random.random()}")  # 与上面相同
    print()
    
    # 使用时间作为随机种子
    print("\n4. 使用时间作为随机种子:")
    seed_time = int(time.time())
    print(f"当前时间戳: {seed_time}")
    random.seed(seed_time)
    print(f"以时间戳为种子的随机数: {random.random()}")
    print()
    
    # 使用不同类型的种子
    print("\n5. 使用不同类型的种子:")
    # 整数种子
    random.seed(12345)
    print(f"整数种子后的随机数: {random.random()}")
    
    # 字符串种子
    random.seed("hello world")
    print(f"字符串种子后的随机数: {random.random()}")
    
    # None种子（使用系统熵）
    random.seed(None)
    print(f"None种子后的随机数: {random.random()}")
    print()
    
    # 注意事项：设置随机种子的重要性
    print("\n6. 随机种子的重要性:")
    print("- 可重复性：使用相同的随机种子可以重现相同的随机序列")
    print("- 调试：在调试涉及随机数的代码时非常有用")
    print("- 科学实验：确保实验结果的可重复性")
    print("- 默认行为：不设置种子时，Python会使用系统时间和其他熵源")

# 运行随机种子示例
seed_management()
print()

# 2. 基本随机数函数
print("=== 2. 基本随机数函数 ===")

def basic_random_functions():
    """基本随机数函数示例"""
    print("基本随机数函数:")
    
    # random() - 生成[0.0, 1.0)范围内的随机浮点数
    print("\n1. random() - 生成[0.0, 1.0)范围内的随机浮点数:")
    for i in range(5):
        print(f"  随机浮点数 {i+1}: {random.random():.10f}")
    print()
    
    # 生成指定范围的随机浮点数
    def random_float(min_val, max_val):
        """生成[min_val, max_val)范围内的随机浮点数"""
        return min_val + (max_val - min_val) * random.random()
    
    print("\n2. 生成自定义范围的随机浮点数:")
    min_val, max_val = 5.0, 10.0
    for i in range(5):
        print(f"  随机浮点数 {i+1} ({min_val}到{max_val}): {random_float(min_val, max_val):.10f}")
    print()
    
    # randint(a, b) - 生成[a, b]范围内的随机整数，包含a和b
    print("\n3. randint(a, b) - 生成[a, b]范围内的随机整数:")
    a, b = 1, 10
    print(f"生成{10}个{[a, b]}范围内的随机整数:")
    for i in range(10):
        print(f"  {random.randint(a, b)}", end=" ")
    print("\n")
    
    # randrange(start, stop[, step]) - 从range(start, stop, step)中随机选择一个整数
    print("\n4. randrange(start, stop[, step]) - 从range中随机选择:")
    
    # 生成1-10的随机整数
    print("生成1-10的随机整数:")
    for i in range(5):
        print(f"  {random.randrange(1, 11)}", end=" ")
    print("\n")
    
    # 生成1-10的随机偶数
    print("生成1-10的随机偶数:")
    for i in range(5):
        print(f"  {random.randrange(2, 11, 2)}", end=" ")
    print("\n")
    
    # 生成1-10的随机奇数
    print("生成1-10的随机奇数:")
    for i in range(5):
        print(f"  {random.randrange(1, 10, 2)}", end=" ")
    print("\n")
    
    # uniform(a, b) - 生成[a, b]范围内的随机浮点数，具有均匀分布
    print("\n5. uniform(a, b) - 生成均匀分布的随机浮点数:")
    a, b = 2.5, 7.5
    print(f"生成5个{[a, b]}范围内的均匀分布随机浮点数:")
    for i in range(5):
        print(f"  {random.uniform(a, b):.10f}")
    print()
    
    # 对比random()和uniform()
    print("\n6. random()和uniform(0, 1)的对比:")
    random.seed(42)  # 设置相同种子
    r1 = random.random()
    
    random.seed(42)  # 重置种子
    r2 = random.uniform(0, 1)
    
    print(f"random(): {r1:.15f}")
    print(f"uniform(0, 1): {r2:.15f}")
    print(f"结果相同: {r1 == r2}")

# 运行基本随机数函数示例
basic_random_functions()
print()

# 3. 序列随机化和选择
print("=== 3. 序列随机化和选择 ===")

def sequence_operations():
    """序列随机化和选择示例"""
    print("序列随机化和选择:")
    
    # 准备示例数据
    numbers = list(range(1, 11))
    fruits = ['苹果', '香蕉', '橙子', '梨', '葡萄', '草莓']
    
    print(f"原始数字列表: {numbers}")
    print(f"原始水果列表: {fruits}")
    print()
    
    # choice(seq) - 从非空序列中随机选择一个元素
    print("\n1. choice(seq) - 随机选择一个元素:")
    print("随机选择一个数字:")
    for i in range(5):
        print(f"  {random.choice(numbers)}")
    
    print("\n随机选择一个水果:")
    for i in range(5):
        print(f"  {random.choice(fruits)}")
    print()
    
    # choices(population, weights=None, *, cum_weights=None, k=1) - 有放回地随机选择k个元素
    print("\n2. choices(population, weights=None, *, cum_weights=None, k=1) - 有放回随机选择:")
    
    # 等概率随机选择
    print("从水果列表中有放回地随机选择3个元素:")
    result = random.choices(fruits, k=3)
    print(f"  {result}")
    
    # 多次选择查看结果分布
    print("\n多次有放回选择的结果分布:")
    results = random.choices(fruits, k=1000)
    distribution = {}
    for fruit in fruits:
        distribution[fruit] = results.count(fruit)
    
    for fruit, count in distribution.items():
        print(f"  {fruit}: {count}次 ({count/10:.1f}%)")
    print()
    
    # 使用权重进行非等概率选择
    print("\n使用权重进行非等概率选择:")
    # 权重表示每个水果被选中的相对概率
    weights = [5, 3, 2, 1, 1, 1]  # 苹果被选中的概率是香蕉的5/3倍
    print(f"水果列表: {fruits}")
    print(f"对应权重: {weights}")
    
    weighted_results = random.choices(fruits, weights=weights, k=1000)
    weighted_distribution = {}
    for fruit in fruits:
        weighted_distribution[fruit] = weighted_results.count(fruit)
    
    print("\n加权选择的结果分布:")
    for fruit, count in weighted_distribution.items():
        print(f"  {fruit}: {count}次 ({count/10:.1f}%)")
    print()
    
    # shuffle(x) - 随机打乱序列，原地修改
    print("\n3. shuffle(x) - 随机打乱序列:")
    # 打乱数字列表
    numbers_copy = numbers.copy()
    print(f"打乱前: {numbers_copy}")
    random.shuffle(numbers_copy)
    print(f"打乱后: {numbers_copy}")
    
    # 打乱水果列表
    fruits_copy = fruits.copy()
    print(f"\n打乱前: {fruits_copy}")
    random.shuffle(fruits_copy)
    print(f"打乱后: {fruits_copy}")
    print()
    
    # sample(population, k) - 无放回地随机选择k个元素
    print("\n4. sample(population, k) - 无放回随机选择:")
    print(f"从{len(numbers)}个数字中无放回地随机选择5个:")
    sample_result = random.sample(numbers, k=5)
    print(f"  {sample_result}")
    
    print(f"\n从{len(fruits)}个水果中无放回地随机选择3个:")
    sample_result = random.sample(fruits, k=3)
    print(f"  {sample_result}")
    print()
    
    # 尝试从较小的序列中选择更多的元素（会引发错误）
    print("\n5. 无放回选择的限制:")
    try:
        # 尝试从5个元素中选择6个，这是不可能的
        print("尝试从水果列表中无放回地选择10个元素:")
        random.sample(fruits, k=10)
    except ValueError as e:
        print(f"  错误: {e}")
    print()
    
    # 实际应用：随机抽样
    print("\n6. 实际应用：数据分析中的随机抽样:")
    # 创建一个大数据集的示例
    large_dataset = list(range(1, 1001))  # 1000个元素
    
    # 随机抽取10%的数据作为样本
    sample_size = int(len(large_dataset) * 0.1)  # 100个样本
    random_sample = random.sample(large_dataset, k=sample_size)
    
    print(f"从{len(large_dataset)}个数据中随机抽取{sample_size}个样本")
    print(f"样本的最小值: {min(random_sample)}")
    print(f"样本的最大值: {max(random_sample)}")
    print(f"样本的前10个元素: {random_sample[:10]}")

# 运行序列随机化和选择示例
sequence_operations()
print()

# 4. 概率分布随机数
print("=== 4. 概率分布随机数 ===")

def probability_distributions():
    """概率分布随机数生成示例"""
    print("概率分布随机数生成:")
    
    # 均匀分布 (我们已经在前面介绍过uniform())
    print("\n1. 均匀分布:")
    print("uniform(a, b) 生成[a, b]区间内的均匀分布随机数")
    uniform_samples = [random.uniform(-1, 1) for _ in range(5)]
    print(f"均匀分布样本 (-1, 1): {[f'{x:.6f}' for x in uniform_samples]}")
    print()
    
    # 正态分布 (高斯分布)
    print("\n2. 正态分布 (高斯分布):")
    # gauss(mu, sigma) - 生成均值为mu，标准差为sigma的正态分布随机数
    mu, sigma = 0, 1  # 标准正态分布
    print(f"生成5个均值={mu}，标准差={sigma}的正态分布随机数:")
    for i in range(5):
        print(f"  {random.gauss(mu, sigma):.10f}")
    print()
    
    # 生成多个样本并计算统计量
    print("\n生成10000个标准正态分布样本并计算统计量:")
    gauss_samples = [random.gauss(mu, sigma) for _ in range(10000)]
    sample_mean = sum(gauss_samples) / len(gauss_samples)
    sample_var = sum((x - sample_mean) ** 2 for x in gauss_samples) / len(gauss_samples)
    sample_std = math.sqrt(sample_var)
    
    print(f"样本均值: {sample_mean:.6f} (理论值: {mu})")
    print(f"样本方差: {sample_var:.6f} (理论值: {sigma**2})")
    print(f"样本标准差: {sample_std:.6f} (理论值: {sigma})")
    print(f"样本最小值: {min(gauss_samples):.6f}")
    print(f"样本最大值: {max(gauss_samples):.6f}")
    print()
    
    # 对数正态分布
    print("\n3. 对数正态分布:")
    # lognormvariate(mu, sigma) - 生成对数正态分布随机数
    # 对数正态分布是指随机变量的自然对数服从正态分布
    log_mu, log_sigma = 0, 0.5
    print(f"生成5个对数正态分布随机数 (mu={log_mu}, sigma={log_sigma}):")
    for i in range(5):
        print(f"  {random.lognormvariate(log_mu, log_sigma):.10f}")
    print()
    
    # 指数分布
    print("\n4. 指数分布:")
    # expovariate(lambd) - 生成指数分布随机数
    # lambd是1.0除以期望间隔时间
    lambd = 0.5  # 平均间隔时间为2
    print(f"生成5个指数分布随机数 (λ={lambd}):")
    for i in range(5):
        print(f"  {random.expovariate(lambd):.10f}")
    print()
    
    # 生成多个样本并计算期望
    exp_samples = [random.expovariate(lambd) for _ in range(10000)]
    exp_mean = sum(exp_samples) / len(exp_samples)
    theoretical_mean = 1.0 / lambd
    print(f"指数分布样本均值: {exp_mean:.6f} (理论值: {theoretical_mean:.6f})")
    print()
    
    # 贝塔分布
    print("\n5. 贝塔分布:")
    # betavariate(alpha, beta) - 生成贝塔分布随机数
    # 贝塔分布的参数alpha和beta必须大于0
    alpha, beta = 2, 5
    print(f"生成5个贝塔分布随机数 (α={alpha}, β={beta}):")
    for i in range(5):
        print(f"  {random.betavariate(alpha, beta):.10f}")
    print()
    
    # 伽马分布
    print("\n6. 伽马分布:")
    # gammavariate(alpha, beta) - 生成伽马分布随机数
    # 伽马分布的参数alpha和beta必须大于0
    gamma_alpha, gamma_beta = 2, 2
    print(f"生成5个伽马分布随机数 (α={gamma_alpha}, β={gamma_beta}):")
    for i in range(5):
        print(f"  {random.gammavariate(gamma_alpha, gamma_beta):.10f}")
    print()
    
    # 三角形分布
    print("\n7. 三角形分布:")
    # triangular(low, high, mode) - 生成三角形分布随机数
    low, high, mode = 0, 10, 5
    print(f"生成5个三角形分布随机数 (low={low}, high={high}, mode={mode}):")
    for i in range(5):
        print(f"  {random.triangular(low, high, mode):.10f}")
    print()
    
    # 帕累托分布
    print("\n8. 帕累托分布:")
    # paretovariate(alpha) - 生成帕累托分布随机数
    # 帕累托分布的参数alpha必须大于0
    pareto_alpha = 2.5
    print(f"生成5个帕累托分布随机数 (α={pareto_alpha}):")
    for i in range(5):
        print(f"  {random.paretovariate(pareto_alpha):.10f}")
    print()
    
    # 威布尔分布
    print("\n9. 威布尔分布:")
    # weibullvariate(alpha, beta) - 生成威布尔分布随机数
    # 威布尔分布的参数alpha和beta必须大于0
    weibull_alpha, weibull_beta = 1, 1
    print(f"生成5个威布尔分布随机数 (α={weibull_alpha}, β={weibull_beta}):")
    for i in range(5):
        print(f"  {random.weibullvariate(weibull_alpha, weibull_beta):.10f}")

# 运行概率分布随机数示例
probability_distributions()
print()

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")

def practical_applications():
    """实际应用示例"""
    print("实际应用示例:")
    
    # 示例1: 简单的随机密码生成器
    def generate_password(length=12, use_uppercase=True, use_lowercase=True, 
                         use_digits=True, use_special=True):
        """生成随机密码
        
        Args:
            length: 密码长度
            use_uppercase: 是否使用大写字母
            use_lowercase: 是否使用小写字母
            use_digits: 是否使用数字
            use_special: 是否使用特殊字符
            
        Returns:
            生成的随机密码
        """
        # 定义字符集
        chars = ''
        if use_uppercase:
            chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if use_lowercase:
            chars += 'abcdefghijklmnopqrstuvwxyz'
        if use_digits:
            chars += '0123456789'
        if use_special:
            chars += '!@#$%^&*()-_=+[]{}|;:,.<>?/\'
        
        if not chars:
            raise ValueError("至少需要选择一种字符类型")
        
        # 生成密码
        password = ''.join(random.choice(chars) for _ in range(length))
        
        return password
    
    print("示例1: 随机密码生成器")
    print("生成默认密码 (12位，包含所有字符类型):")
    for _ in range(3):
        print(f"  {generate_password()}")
    
    print("\n生成8位纯数字密码:")
    for _ in range(3):
        print(f"  {generate_password(length=8, use_uppercase=False, use_lowercase=False, use_special=False)}")
    
    print("\n生成16位字母数字密码 (不包含特殊字符):")
    for _ in range(3):
        print(f"  {generate_password(length=16, use_special=False)}")
    print()
    
    # 示例2: 蒙特卡洛方法计算π
    def estimate_pi(n_iterations=10000):
        """使用蒙特卡洛方法估算π的值
        
        原理：在正方形中随机生成点，计算落在1/4圆内的点的比例
        π/4 ≈ 圆内点数/总点数
        
        Args:
            n_iterations: 生成的随机点数量
            
        Returns:
            π的估算值
        """
        inside_circle = 0
        
        for _ in range(n_iterations):
            # 生成[0, 1)范围内的随机点 (x, y)
            x = random.random()
            y = random.random()
            
            # 检查点是否在1/4圆内 (x² + y² <= 1)
            if x**2 + y**2 <= 1:
                inside_circle += 1
        
        # 估算π
        pi_estimate = 4 * inside_circle / n_iterations
        
        return pi_estimate
    
    print("示例2: 蒙特卡洛方法计算π")
    print(f"理论值 π = {math.pi:.10f}")
    
    # 使用不同数量的迭代计算π
    for n in [1000, 10000, 100000]:
        start_time = time.time()
        pi_estimate = estimate_pi(n)
        elapsed_time = time.time() - start_time
        
        error = abs(pi_estimate - math.pi) / math.pi * 100
        print(f"使用{n:,}次迭代估算π: {pi_estimate:.10f}")
        print(f"  误差: {error:.6f}%")
        print(f"  耗时: {elapsed_time:.6f}秒")
    print()
    
    # 示例3: 随机采样和数据分割
    def split_dataset(data, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
        """将数据集随机分割为训练集、验证集和测试集
        
        Args:
            data: 完整数据集
            train_ratio: 训练集比例
            val_ratio: 验证集比例
            test_ratio: 测试集比例
            
        Returns:
            (train_data, val_data, test_data) 元组
        """
        # 验证比例和为1
        if not math.isclose(train_ratio + val_ratio + test_ratio, 1.0):
            raise ValueError("比例和必须等于1.0")
        
        # 复制数据并打乱顺序
        data_copy = data.copy()
        random.shuffle(data_copy)
        
        # 计算分割点
        n = len(data_copy)
        train_size = int(n * train_ratio)
        val_size = int(n * val_ratio)
        
        # 分割数据
        train_data = data_copy[:train_size]
        val_data = data_copy[train_size:train_size+val_size]
        test_data = data_copy[train_size+val_size:]
        
        return train_data, val_data, test_data
    
    print("示例3: 数据集随机分割")
    # 创建一个示例数据集
    sample_dataset = list(range(1, 101))  # 100个样本
    print(f"原始数据集大小: {len(sample_dataset)}")
    
    # 分割数据集
    train, val, test = split_dataset(sample_dataset)
    
    print(f"训练集大小: {len(train)} ({len(train)/len(sample_dataset)*100:.1f}%)")
    print(f"验证集大小: {len(val)} ({len(val)/len(sample_dataset)*100:.1f}%)")
    print(f"测试集大小: {len(test)} ({len(test)/len(sample_dataset)*100:.1f}%)")
    print(f"训练集前10个元素: {train[:10]}")
    print()
    
    # 示例4: 蒙特卡洛模拟 - 掷骰子
    def simulate_dice_rolls(n_simulations=10000, n_dice=2):
        """模拟掷骰子并分析结果分布
        
        Args:
            n_simulations: 模拟次数
            n_dice: 骰子数量
            
        Returns:
            结果频率分布字典
        """
        # 初始化结果计数器
        results = {}
        min_result = n_dice
        max_result = n_dice * 6
        
        for i in range(min_result, max_result + 1):
            results[i] = 0
        
        # 进行模拟
        for _ in range(n_simulations):
            # 掷骰子并计算总和
            total = sum(random.randint(1, 6) for _ in range(n_dice))
            results[total] += 1
        
        # 计算频率
        frequencies = {}
        for result, count in results.items():
            frequencies[result] = count / n_simulations
        
        return frequencies
    
    print("示例4: 蒙特卡洛模拟 - 掷骰子")
    # 模拟掷两个骰子
    n_simulations = 100000
    print(f"模拟掷两个骰子{',':,}次的结果分布:")
    dice_frequencies = simulate_dice_rolls(n_simulations)
    
    for result in sorted(dice_frequencies.keys()):
        frequency = dice_frequencies[result]
        count = int(frequency * n_simulations)
        print(f"  点数{result}: {count:,}次 ({frequency*100:.2f}%)", end="")
        # 绘制简单的频率条形图
        bar_length = int(frequency * 1000)
        print(" #" * bar_length)
    print()
    
    # 示例5: 随机漫步模拟
    def random_walk(n_steps=1000, step_size=1):
        """模拟一维随机漫步
        
        Args:
            n_steps: 步数
            step_size: 步长
            
        Returns:
            (路径位置列表, 最终位置)
        """
        position = 0
        positions = [position]  # 记录每一步的位置
        
        for _ in range(n_steps):
            # 随机选择方向 (-1 或 1)
            direction = random.choice([-1, 1])
            # 更新位置
            position += direction * step_size
            positions.append(position)
        
        return positions, position
    
    print("示例5: 随机漫步模拟")
    n_walks = 5
    n_steps = 100
    
    print(f"模拟{n_walks}次{',':,}步的一维随机漫步:")
    final_positions = []
    
    for i in range(n_walks):
        path, final_pos = random_walk(n_steps)
        final_positions.append(final_pos)
        print(f"  漫步{i+1}: 起始位置=0, 最终位置={final_pos}, 最大距离={max(abs(p) for p in path)}")
    
    avg_final_pos = sum(final_positions) / n_walks
    print(f"\n平均最终位置: {avg_final_pos:.2f}")
    print(f"理论上，随机漫步的平均位置应该接近0")

# 运行实际应用示例
practical_applications()
print()

# 6. 随机数生成器高级用法
print("=== 6. 随机数生成器高级用法 ===")

def advanced_usage():
    """随机数生成器高级用法"""
    print("随机数生成器高级用法:")
    
    # 创建独立的随机数生成器实例
    print("\n1. 创建独立的随机数生成器实例:")
    # 默认的随机数生成器是模块级别的
    print("使用默认随机数生成器:")
    random.seed(42)  # 设置默认生成器的种子
    print(f"  随机数1: {random.random()}")
    print(f"  随机数2: {random.random()}")
    
    # 创建新的随机数生成器实例
    print("\n创建并使用独立的随机数生成器:")
    rng1 = random.Random(42)  # 使用相同的种子
    print(f"  随机数1: {rng1.random()}")
    print(f"  随机数2: {rng1.random()}")
    
    # 创建第二个独立的随机数生成器
    print("\n创建第二个独立的随机数生成器:")
    rng2 = random.Random(42)  # 也使用相同的种子
    print(f"  随机数1: {rng2.random()}")
    print(f"  随机数2: {rng2.random()}")
    
    # 两个生成器生成的序列相同，因为使用了相同的种子
    print("\n注意: 两个生成器生成的序列是相同的，因为它们使用了相同的种子")
    print()
    
    # 使用不同种子创建多个独立的生成器
    print("\n2. 使用不同种子创建多个独立的生成器:")
    rng_a = random.Random(123)
    rng_b = random.Random(456)
    
    print("生成5对随机数:")
    for i in range(5):
        print(f"  rng_a: {rng_a.random():.8f}, rng_b: {rng_b.random():.8f}")
    print()
    
    # 不同的随机数生成器算法
    print("\n3. 不同的随机数生成器算法:")
    print("Python的random模块使用Mersenne Twister作为默认的随机数生成算法")
    print("这是一个周期非常长(2^19937-1)的伪随机数生成器")
    print("但请注意，它不适合加密目的")
    print()
    
    # 关于加密安全性的注意事项
    print("\n4. 加密安全的随机数生成:")
    print("对于需要加密安全的应用，请使用Python的secrets模块")
    print("secrets模块提供了适合加密和安全敏感操作的随机数生成函数")
    print()
    print("示例 - 使用secrets模块生成安全的随机数:")
    print("""
    import secrets
    
    # 生成安全的随机整数
    secure_number = secrets.randbelow(100)  # 0到99之间的安全随机整数
    
    # 生成安全的随机字节
    secure_bytes = secrets.token_bytes(16)  # 16字节的随机数据
    
    # 生成安全的十六进制字符串
    secure_hex = secrets.token_hex(16)  # 32字符的十六进制字符串
    
    # 生成安全的URL安全文本字符串
    secure_urlsafe = secrets.token_urlsafe(16)  # URL安全的随机字符串
    """)
    print()
    
    # 自定义随机数生成器
    print("\n5. 自定义随机数生成器:")
    print("可以通过继承Random类来自定义随机数生成器:")
    print("""
    class CustomRandom(random.Random):
        """自定义随机数生成器"""
        def __init__(self, x=0):
            super().__init__(x)
        
        def custom_random_method(self, param):
            """添加自定义的随机方法"""
            # 实现自定义的随机逻辑
            pass
    
    # 使用自定义生成器
    custom_rng = CustomRandom()
    """)
    print()
    
    # 设置和获取state
    print("\n6. 设置和获取随机数生成器的状态:")
    # 获取当前状态
    rng = random.Random(42)
    state = rng.getstate()
    
    # 生成一些随机数
    print("生成一些随机数:")
    for i in range(3):
        print(f"  {rng.random():.8f}")
    
    # 恢复状态
    rng.setstate(state)
    print("\n恢复状态后再生成随机数:")
    for i in range(3):
        print(f"  {rng.random():.8f}")
    
    print("\n注意: 恢复状态后生成的随机数与之前相同")
    print("这在需要保存随机数生成进度时很有用")

# 运行高级用法示例
advanced_usage()
print()

# 7. 最佳实践和注意事项
print("=== 7. 最佳实践和注意事项 ===")

def best_practices():
    """random模块使用的最佳实践和注意事项"""
    
    print("random模块使用的最佳实践和注意事项:")
    
    # 1. 随机数质量和安全性
    print("\n1. 随机数质量和安全性:")
    print("   - random模块生成的是伪随机数，不是真随机数")
    print("   - 对于加密安全的应用，应使用secrets模块而不是random模块")
    print("   - 不要在密码学应用中使用random模块")
    
    # 2. 种子设置
    print("\n2. 种子设置:")
    print("   - 为了可重复性，特别是在科学模拟中，应该设置固定的随机种子")
    print("   - 在生产环境中，通常不需要手动设置种子，让Python使用系统熵")
    print("   - 避免使用可预测的值作为种子")
    
    # 3. 性能考虑
    print("\n3. 性能考虑:")
    print("   - 对于大量随机数生成，考虑使用NumPy的随机数生成器，它更快")
    print("   - 避免在循环中重复创建Random实例")
    print("   - 对于多线程环境，考虑为每个线程使用独立的随机数生成器实例")
    
    # 4. 多线程和多进程注意事项
    print("\n4. 多线程和多进程注意事项:")
    print("   - 模块级别的随机数生成器不是线程安全的")
    print("   - 在多线程程序中，应使用threading.local()来为每个线程创建独立的生成器")
    print("   - 在多进程程序中，每个进程会有自己的随机数生成器状态")
    
    # 5. 分布选择
    print("\n5. 选择合适的分布:")
    print("   - 均匀分布: 适用于所有结果等概率的情况")
    print("   - 正态分布: 适用于许多自然现象建模")
    print("   - 指数分布: 适用于间隔时间建模")
    print("   - 对数正态分布: 适用于右偏数据建模")
    print("   - 根据实际问题选择合适的概率分布")
    
    # 6. 序列操作的注意事项
    print("\n6. 序列操作的注意事项:")
    print("   - shuffle()会原地修改序列，返回None")
    print("   - sample()不会修改原序列")
    print("   - sample()的k参数不能大于序列长度")
    print("   - 对于非常大的序列，考虑使用迭代器而不是一次性加载所有元素")
    
    # 7. 避免常见错误
    print("\n7. 避免常见错误:")
    print("   - 不要将random()的结果直接用作整数概率（使用randint()或randrange()）")
    print("   - 不要在循环中重复调用seed()，这会导致生成重复的随机数序列")
    print("   - 不要假设随机数序列中的模式或规律")
    print("   - 避免使用浮点数比较来检查随机数生成的准确性")
    
    # 8. 代码示例：线程安全的随机数生成器
    print("\n8. 示例：线程安全的随机数生成器:")
    print("""
    import threading
    import random
    
    # 创建线程本地存储
    local_random = threading.local()
    
    def get_thread_random():
        """获取当前线程的随机数生成器实例"""
        if not hasattr(local_random, 'rng'):
            # 为每个线程创建独立的随机数生成器
            # 使用线程ID作为种子的一部分，增加随机性
            seed = (threading.get_ident() + hash(random.random())) & 0xFFFFFFFF
            local_random.rng = random.Random(seed)
        return local_random.rng
    
    # 在多线程环境中使用
    def worker():
        """工作线程函数"""
        rng = get_thread_random()
        # 使用线程本地的随机数生成器
        print(f"线程 {threading.get_ident()} 生成的随机数: {rng.random()}")
    """)
    
    # 9. 代码示例：生成加权随机选择
    print("\n9. 示例：高级加权随机选择:")
    print("""
    def weighted_random_choice(items, weights):
        """根据权重随机选择项目
        
        Args:
            items: 项目列表
            weights: 权重列表，与项目一一对应
            
        Returns:
            随机选中的项目
        """
        if len(items) != len(weights):
            raise ValueError("项目和权重数量必须一致")
        
        # 计算累计权重
        total = 0
        cum_weights = []
        for w in weights:
            total += w
            cum_weights.append(total)
        
        # 生成随机数
        r = random.uniform(0, total)
        
        # 找到对应的项目
        for i, cw in enumerate(cum_weights):
            if r < cw:
                return items[i]
        
        # 防止浮点数精度问题导致的错误
        return items[-1]
    
    # 使用示例
    # items = ['A', 'B', 'C']
    # weights = [5, 3, 2]  # A的权重是5，B是3，C是2
    # choice = weighted_random_choice(items, weights)
    """)

# 运行最佳实践示例
best_practices()

# 总结
print("\n=== 总结 ===")
print("random模块是Python中用于生成随机数和实现随机化算法的核心库。")
print("主要功能和优势包括：")
print("1. 提供多种随机数生成函数：基本随机数、整数随机数、序列随机选择等")
print("2. 支持多种概率分布：均匀分布、正态分布、指数分布等")
print("3. 提供随机种子管理功能，确保实验可重复性")
print("4. 包含丰富的序列随机化操作：打乱、抽样等")
print("5. 可创建独立的随机数生成器实例，支持多线程应用")
print()
print("在使用random模块时，需要注意其伪随机性本质，不要将其用于安全敏感的应用。")
print("对于需要加密安全的随机数生成，应使用secrets模块。")
print()
print("random模块广泛应用于游戏开发、模拟实验、数据分析采样、随机化算法等领域，")
print("是Python编程中处理随机性的重要工具。")

# 运行完整演示
if __name__ == "__main__":
    print("Python random模块演示\n")
    print("请参考源代码中的详细示例和说明")