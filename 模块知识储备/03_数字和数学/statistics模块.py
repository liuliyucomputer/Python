# Python statistics模块详解

import statistics
import math
import random

# 1. 模块概述
print("=== 1. statistics模块概述 ===")
print("statistics模块提供了基本的统计计算功能，用于数据分析和统计建模。")
print("该模块的主要特点：")
print("- 集中趋势度量（均值、中位数、众数等）")
print("- 离散程度度量（方差、标准差、极差等）")
print("- 分布形状度量（偏度、峰度）")
print("- 相关性度量（协方差、相关系数）")
print("- 支持多种数值类型（整数、浮点数）")
print()

# 2. 集中趋势度量
print("=== 2. 集中趋势度量 ===")

# 创建数据集
data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
print(f"数据集: {data}")

# 算术平均数
print(f"statistics.mean(data) = {statistics.mean(data)}")

# 中位数
print(f"statistics.median(data) = {statistics.median(data)}")

# 低中位数（当数据个数为偶数时，取较小的中间值）
print(f"statistics.median_low(data) = {statistics.median_low(data)}")

# 高中位数（当数据个数为偶数时，取较大的中间值）
print(f"statistics.median_high(data) = {statistics.median_high(data)}")

# 中位数分组（用于分组数据）
data_grouped = [1, 2, 3, 4, 5, 6]
print(f"statistics.median_grouped(data_grouped) = {statistics.median_grouped(data_grouped)}")
print(f"statistics.median_grouped(data_grouped, interval=2) = {statistics.median_grouped(data_grouped, interval=2)}")

# 众数（返回出现频率最高的元素）
data_mode = [1, 2, 3, 3, 4, 4, 4, 5, 5]
print(f"众数数据集: {data_mode}")
print(f"statistics.mode(data_mode) = {statistics.mode(data_mode)}")

# 多模式（返回所有出现频率最高的元素）
data_multimode = [1, 1, 2, 2, 3, 4, 5]
print(f"多模式数据集: {data_multimode}")
print(f"statistics.multimode(data_multimode) = {statistics.multimode(data_multimode)}")

# 几何平均数（用于比例数据）
data_geo = [2, 8, 4]
print(f"几何平均数数据集: {data_geo}")
print(f"statistics.geometric_mean(data_geo) = {statistics.geometric_mean(data_geo)}")

# 调和平均数（用于速率数据）
data_harmonic = [2, 4, 8]
print(f"调和平均数数据集: {data_harmonic}")
print(f"statistics.harmonic_mean(data_harmonic) = {statistics.harmonic_mean(data_harmonic)}")
print()

# 3. 离散程度度量
print("=== 3. 离散程度度量 ===")

# 数据集
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"数据集: {data}")

# 极差（最大值 - 最小值）
print(f"statistics.pstdev(data)计算的是总体标准差，这里用max-min计算极差: {max(data) - min(data)}")

# 方差
print(f"statistics.variance(data) = {statistics.variance(data)}")  # 样本方差

# 总体方差
print(f"statistics.pvariance(data) = {statistics.pvariance(data)}")  # 总体方差

# 标准差
print(f"statistics.stdev(data) = {statistics.stdev(data)}")  # 样本标准差

# 总体标准差
print(f"statistics.pstdev(data) = {statistics.pstdev(data)}")  # 总体标准差

# 四分位数
from statistics import quantiles
try:
    quartiles = quantiles(data, n=4)
    print(f"四分位数 (n=4): {quartiles}")
    
    # 百分位数
    percentiles = quantiles(data, n=100)
    print(f"第25、50、75百分位数: {percentiles[24]}, {percentiles[49]}, {percentiles[74]}")
except AttributeError:
    print("注意: 当前Python版本可能不支持statistics.quantiles函数")

# 四分位距
if 'quantiles' in dir(statistics):
    q1, q2, q3 = quantiles(data, n=4)
    iqr = q3 - q1
    print(f"四分位距 (IQR): {iqr}")
print()

# 4. 分布形状度量
print("=== 4. 分布形状度量 ===")

# 创建正态分布数据集
normal_data = [random.normalvariate(0, 1) for _ in range(1000)]
print(f"正态分布数据集示例: {normal_data[:10]}...")

# 偏度（skewness）
print(f"statistics.skew(normal_data) = {statistics.skew(normal_data)}")

# 峰度（kurtosis）
print(f"statistics.kurtosis(normal_data) = {statistics.kurtosis(normal_data)}")

# 正偏态数据
positive_skew_data = [random.lognormvariate(0, 0.5) for _ in range(1000)]
print(f"正偏态数据的偏度: {statistics.skew(positive_skew_data)}")

# 负偏态数据
negative_skew_data = [-x for x in positive_skew_data]
print(f"负偏态数据的偏度: {statistics.skew(negative_skew_data)}")
print()

# 5. 相关性度量
print("=== 5. 相关性度量 ===")

# 创建相关数据集
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [2, 4, 5, 7, 8, 10, 11, 13, 14, 16]
print(f"x数据集: {x}")
print(f"y数据集: {y}")

# 协方差
print(f"statistics.covariance(x, y) = {statistics.covariance(x, y)}")

# 皮尔逊相关系数
print(f"statistics.correlation(x, y) = {statistics.correlation(x, y)}")

# 计算相关系数的手动方法（用于验证）
def manual_correlation(x, y):
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    # 计算协方差
    covariance = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)) / (n - 1)
    
    # 计算标准差
    std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) / (n - 1))
    std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y) / (n - 1))
    
    # 计算相关系数
    correlation = covariance / (std_x * std_y)
    return correlation

print(f"手动计算的相关系数: {manual_correlation(x, y)}")
print()

# 6. 数据验证和处理
print("=== 6. 数据验证和处理 ===")

# 空数据集处理
try:
    statistics.mean([])
except statistics.StatisticsError as e:
    print(f"空数据集错误: {e}")

# 单元素数据集
print(f"单元素数据集的均值: {statistics.mean([5])}")
print(f"单元素数据集的中位数: {statistics.median([5])}")
print(f"单元素数据集的众数: {statistics.mode([5])}")

# 异常值处理
data_with_outlier = [1, 2, 3, 4, 5, 100]
print(f"包含异常值的数据集: {data_with_outlier}")
print(f"均值（受异常值影响大）: {statistics.mean(data_with_outlier)}")
print(f"中位数（受异常值影响小）: {statistics.median(data_with_outlier)}")

# 混合数据类型
try:
    mixed_data = [1, 2, '3', 4, 5]
    statistics.mean(mixed_data)
except TypeError as e:
    print(f"混合数据类型错误: {e}")
print()

# 7. 实际应用示例
print("=== 7. 实际应用示例 ===")

# 示例1：学生成绩分析
def analyze_student_scores(scores):
    """分析学生成绩"""
    if not scores:
        raise ValueError("成绩数据集不能为空")
    
    analysis = {}
    analysis['最高分'] = max(scores)
    analysis['最低分'] = min(scores)
    analysis['平均分'] = statistics.mean(scores)
    analysis['中位数'] = statistics.median(scores)
    analysis['标准差'] = statistics.stdev(scores)
    analysis['方差'] = statistics.variance(scores)
    
    # 计算及格率和优秀率
    pass_count = sum(1 for score in scores if score >= 60)
    excellent_count = sum(1 for score in scores if score >= 90)
    analysis['及格率'] = pass_count / len(scores) * 100
    analysis['优秀率'] = excellent_count / len(scores) * 100
    
    return analysis

# 学生成绩数据
scores = [85, 92, 78, 90, 88, 76, 95, 89, 82, 91, 79, 87, 93, 84, 80]
print("学生成绩分析:")
score_analysis = analyze_student_scores(scores)
for key, value in score_analysis.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

# 示例2：销售数据分析
def analyze_sales_data(sales):
    """分析销售数据"""
    if not sales:
        raise ValueError("销售数据集不能为空")
    
    analysis = {}
    analysis['总销售额'] = sum(sales)
    analysis['平均销售额'] = statistics.mean(sales)
    analysis['中位数销售额'] = statistics.median(sales)
    analysis['销售额标准差'] = statistics.stdev(sales)
    analysis['最高销售额'] = max(sales)
    analysis['最低销售额'] = min(sales)
    analysis['销售天数'] = len(sales)
    
    # 计算每日销售额与均值的偏差
    mean_sales = analysis['平均销售额']
    analysis['偏差总和'] = sum(s - mean_sales for s in sales)
    analysis['平均偏差'] = statistics.mean([abs(s - mean_sales) for s in sales])
    
    return analysis

# 销售数据
sales_data = [12500, 13200, 11800, 14500, 12900, 13700, 12200, 15100, 13500, 12800]
print("\n销售数据分析:")
sales_analysis = analyze_sales_data(sales_data)
for key, value in sales_analysis.items():
    if isinstance(value, float):
        print(f"  {key}: {value:.2f}")
    else:
        print(f"  {key}: {value}")

# 示例3：相关性分析
print("\n相关性分析示例:")
# 广告支出与销售额
ad_spend = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
sales = [15000, 28000, 40000, 52000, 65000, 78000, 89000, 102000, 115000, 128000]

print(f"广告支出: {ad_spend}")
print(f"销售额: {sales}")
print(f"协方差: {statistics.covariance(ad_spend, sales):.2f}")
print(f"相关系数: {statistics.correlation(ad_spend, sales):.4f}")

# 解释相关性
correlation = statistics.correlation(ad_spend, sales)
if correlation > 0.9:
    print("广告支出与销售额之间存在极强的正相关关系")
elif correlation > 0.7:
    print("广告支出与销售额之间存在强正相关关系")
elif correlation > 0.5:
    print("广告支出与销售额之间存在中等正相关关系")
else:
    print("广告支出与销售额之间的相关关系较弱")
print()

# 8. 与其他统计库的比较
print("=== 8. 与其他统计库的比较 ===")

print("| 特性 | statistics模块 | NumPy | SciPy | pandas |")
print("|------|--------------|-------|-------|--------|")
print("| 功能范围 | 基础统计 | 高级数学和统计 | 科学计算和统计 | 数据分析和统计 |")
print("| 性能 | 较慢 | 很快 | 很快 | 很快 |")
print("| 易用性 | 高 | 中 | 中 | 中 |")
print("| 内存占用 | 低 | 中 | 中 | 高 |")
print("| 数据类型支持 | 列表、元组 | NumPy数组 | NumPy数组 | DataFrame、Series |")
print("| 依赖 | 无 | 无（C扩展） | NumPy | NumPy等 |")
print()

# 9. 性能考虑
print("=== 9. 性能考虑 ===")

import time

def test_performance():
    """测试statistics模块的性能"""
    
    # 生成大型数据集
    large_data = [random.random() for _ in range(100000)]
    
    # 测试均值计算
    start = time.time()
    mean = statistics.mean(large_data)
    time_mean = time.time() - start
    print(f"计算均值 (100,000个元素): {time_mean:.4f}秒")
    
    # 测试中位数计算
    start = time.time()
    median = statistics.median(large_data)
    time_median = time.time() - start
    print(f"计算中位数 (100,000个元素): {time_median:.4f}秒")
    
    # 测试标准差计算
    start = time.time()
    std = statistics.stdev(large_data)
    time_std = time.time() - start
    print(f"计算标准差 (100,000个元素): {time_std:.4f}秒")

print("性能测试（100,000个随机数）:")
test_performance()

print("\n性能建议:")
print("- 对于小型数据集（小于10,000个元素），statistics模块足够快")
print("- 对于大型数据集，考虑使用NumPy等高性能库")
print("- 避免在循环中重复计算统计量")
print("- 预计算常用统计量并缓存结果")
print()

# 10. 最佳实践
print("=== 10. 最佳实践 ===")

print("1. 选择合适的集中趋势度量:")
print("   - 当数据对称分布时，使用均值")
print("   - 当数据存在异常值时，使用中位数")
print("   - 当需要了解最常见值时，使用众数")
print("   - 当数据是比例或增长率时，使用几何平均数")
print("   - 当数据是速率时，使用调和平均数")

print("\n2. 正确理解方差和标准差:")
print("   - 方差的单位是数据单位的平方")
print("   - 标准差的单位与数据单位相同，更易解释")
print("   - 使用样本标准差（stdev）分析样本数据")
print("   - 使用总体标准差（pstdev）分析总体数据")

print("\n3. 注意相关性与因果关系:")
print("   - 相关系数仅表示两个变量之间的线性关系强度")
print("   - 相关性不等于因果关系")
print("   - 高相关系数可能是由第三个变量引起的")

print("\n4. 处理缺失值:")
print("   - statistics模块不支持缺失值（NaN）")
print("   - 在计算统计量前，应删除或填充缺失值")
print("   - 对于大型数据集，可以使用pandas处理缺失值")

print("\n5. 验证数据质量:")
print("   - 检查数据类型是否一致")
print("   - 识别并处理异常值")
print("   - 确保数据集不为空")
print()

# 11. 常见错误和陷阱
print("=== 11. 常见错误和陷阱 ===")

print("1. 对非数值数据使用统计函数:")
print("   # 错误:")
print("   data = ['a', 'b', 'c', 1, 2]")
print("   statistics.mean(data)  # 会抛出TypeError")
print("   # 正确:")
print("   data = [1, 2, 3, 4, 5]")
print("   statistics.mean(data)")

print("\n2. 混淆样本标准差和总体标准差:")
print("   # 样本数据（部分数据）")
print("   sample_data = [1, 2, 3, 4, 5]")
print("   sample_std = statistics.stdev(sample_data)")
print("   # 总体数据（全部数据）")
print("   population_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print("   population_std = statistics.pstdev(population_data)")

print("\n3. 误用众数函数:")
print("   # 数据集: [1, 2, 3, 4, 5]")
print("   # 每个元素出现频率相同")
print("   # statistics.mode()在Python 3.8+中会抛出StatisticsError")
print("   # 使用statistics.multimode()获取所有众数")

print("\n4. 忽略数据分布:")
print("   # 偏态分布的数据")
print("   skewed_data = [1, 2, 3, 4, 5, 100]")
print("   # 均值受异常值影响大")
print("   mean = statistics.mean(skewed_data)")
print("   # 中位数更能反映数据的集中趋势")
print("   median = statistics.median(skewed_data)")

print("\n5. 过度解读相关性:")
print("   # 相关系数高并不意味着因果关系")
print("   # 例如：冰淇淋销量和游泳溺水人数正相关")
print("   # 但这是由于夏季气温升高导致的")
print()

# 12. 总结
print("=== 12. statistics模块总结 ===")
print("statistics模块提供了基本的统计计算功能，适用于简单的数据分析和统计建模。")
print("主要优势：")
print("- 易用性高，API简单直观")
print("- 无外部依赖，属于Python标准库")
print("- 支持多种统计度量")
print("- 提供详细的文档和示例")
print()
print("主要劣势：")
print("- 性能较慢，不适合大型数据集")
print("- 功能有限，不支持高级统计分析")
print("- 不支持缺失值处理")
print("- 不支持复杂的数据结构")
print()
print("使用建议：")
print("- 用于简单的数据分析和教学目的")
print("- 对于复杂的统计分析，使用NumPy、SciPy或pandas")
print("- 结合可视化库（如matplotlib）进行数据探索")
print("- 在生产环境中，根据数据规模选择合适的统计库")
