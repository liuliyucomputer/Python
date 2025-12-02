# Python statistics模块详解

# 1. statistics模块概述
print("=== 1. statistics模块概述 ===")
print("statistics模块提供了计算数值数据统计量的函数。")
print("这些函数计算数学统计量，如平均值、中位数、方差、标准差等。")
print("该模块适用于数据分析、科学计算和统计建模等场景。")
print("statistics模块在Python 3.4版本中首次引入。")
print()

# 2. 集中趋势测量函数
print("=== 2. 集中趋势测量函数 ===")
def statistics_central_tendency():
    """展示集中趋势测量函数"""
    import statistics
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"数据: {data}")
    
    # 算术平均值
    print(f"\n算术平均值:")
    print(f"statistics.mean(data) = {statistics.mean(data)}")
    
    # 中位数
    print(f"\n中位数:")
    print(f"statistics.median(data) = {statistics.median(data)}")  # 数据个数为偶数，返回中间两个数的平均值
    
    # 中位数的两种变体
    print(f"\n中位数变体:")
    # median_low返回排序后中间位置左边的数
    print(f"statistics.median_low(data) = {statistics.median_low(data)}")
    # median_high返回排序后中间位置右边的数
    print(f"statistics.median_high(data) = {statistics.median_high(data)}")
    
    # 众数
    print(f"\n众数:")
    data_with_mode = [1, 2, 2, 3, 3, 3, 4]
    print(f"有众数的数据: {data_with_mode}")
    print(f"statistics.mode(data_with_mode) = {statistics.mode(data_with_mode)}")
    
    # 众数(支持多个众数)
    print(f"\n多众数:")
    data_with_multimode = [1, 1, 2, 2, 3]
    print(f"多众数数据: {data_with_multimode}")
    print(f"statistics.multimode(data_with_multimode) = {statistics.multimode(data_with_multimode)}")
    
    # 几何平均值
    print(f"\n几何平均值:")
    positive_data = [2, 8]
    print(f"正实数数据: {positive_data}")
    print(f"statistics.geometric_mean(positive_data) = {statistics.geometric_mean(positive_data)}")
    
    # 调和平均值
    print(f"\n调和平均值:")
    positive_data = [2, 4, 8]
    print(f"正实数数据: {positive_data}")
    print(f"statistics.harmonic_mean(positive_data) = {statistics.harmonic_mean(positive_data)}")

statistics_central_tendency()
print()

# 3. 离散度测量函数
print("=== 3. 离散度测量函数 ===")
def statistics_dispersion():
    """展示离散度测量函数"""
    import statistics
    
    data = [2, 4, 6, 8, 10]
    print(f"数据: {data}")
    
    # 方差
    print(f"\n方差:")
    # 总体方差
    print(f"statistics.pvariance(data) = {statistics.pvariance(data)}")
    # 样本方差
    print(f"statistics.variance(data) = {statistics.variance(data)}")
    
    # 标准差
    print(f"\n标准差:")
    # 总体标准差
    print(f"statistics.pstdev(data) = {statistics.pstdev(data)}")
    # 样本标准差
    print(f"statistics.stdev(data) = {statistics.stdev(data)}")
    
    # 范围(range函数是Python内置的，不是statistics模块的)
    print(f"\n数据范围:")
    print(f"max(data) - min(data) = {max(data) - min(data)}")
    
    # 四分位数
    print(f"\n四分位数:")
    data_extended = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"扩展数据: {data_extended}")
    # 计算四分位数
    q1 = statistics.quantiles(data_extended, n=4)[0]  # 第一四分位数
    q2 = statistics.quantiles(data_extended, n=4)[1]  # 第二四分位数(中位数)
    q3 = statistics.quantiles(data_extended, n=4)[2]  # 第三四分位数
    iqr = q3 - q1  # 四分位距
    print(f"第一四分位数(Q1): {q1}")
    print(f"第二四分位数(Q2): {q2}")
    print(f"第三四分位数(Q3): {q3}")
    print(f"四分位距(IQR): {iqr}")
    
    # 更多分位数
    print(f"\n更多分位数:")
    # 计算百分位数
    deciles = statistics.quantiles(data_extended, n=10)  # 十分位数
    print(f"十分位数: {deciles}")
    
    # 中位数绝对偏差
    print(f"\n中位数绝对偏差:")
    print(f"statistics.median_abs_deviation(data) = {statistics.median_abs_deviation(data)}")
    print(f"statistics.median_abs_deviation(data, scale=1) = {statistics.median_abs_deviation(data, scale=1)}")

statistics_dispersion()
print()

# 4. 分布函数
print("=== 4. 分布函数 ===")
def statistics_distributions():
    """展示分布相关函数"""
    import statistics
    import random
    
    # 正态分布检验
    print(f"正态分布检验:")
    # 生成正态分布样本
    normal_data = [random.gauss(0, 1) for _ in range(1000)]
    print(f"正态分布样本前10个: {normal_data[:10]}")
    print(f"偏度(应接近0): {statistics.skew(normal_data):.4f}")
    print(f"峰度(应接近0): {statistics.kurtosis(normal_data):.4f}")
    
    # 偏度
    print(f"\n偏度计算:")
    # 右偏数据
    right_skewed = [1, 2, 3, 4, 100]
    print(f"右偏数据: {right_skewed}")
    print(f"右偏数据偏度: {statistics.skew(right_skewed):.4f} (正值)")
    
    # 左偏数据
    left_skewed = [1, 96, 97, 98, 99, 100]
    print(f"左偏数据: {left_skewed}")
    print(f"左偏数据偏度: {statistics.skew(left_skewed):.4f} (负值)")
    
    # 峰度
    print(f"\n峰度计算:")
    # 高峰度数据
    high_kurtosis = [0, 0, 0, 0, 1, 2, 3, 4, 5, 10, 10, 10, 10]
    print(f"高峰度数据前10个: {high_kurtosis[:10]}...")
    print(f"高峰度数据峰度: {statistics.kurtosis(high_kurtosis):.4f}")
    
    # 低峰度数据
    low_kurtosis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"低峰度数据: {low_kurtosis}")
    print(f"低峰度数据峰度: {statistics.kurtosis(low_kurtosis):.4f}")

statistics_distributions()
print()

# 5. 相关函数
print("=== 5. 相关函数 ===")
def statistics_correlation():
    """展示相关函数"""
    import statistics
    import random
    
    # 生成相关数据
    x = [i for i in range(20)]
    # y与x正相关
    y_positive = [i + random.uniform(-2, 2) for i in x]
    # y与x负相关
    y_negative = [-i + random.uniform(-2, 2) for i in x]
    
    print(f"正相关数据:")
    print(f"x: {x[:10]}...")
    print(f"y: {y_positive[:10]}...")
    # 计算协方差
    covariance_pos = statistics.covariance(x, y_positive)
    print(f"协方差: {covariance_pos:.4f}")
    
    print(f"\n负相关数据:")
    print(f"x: {x[:10]}...")
    print(f"y: {y_negative[:10]}...")
    # 计算协方差
    covariance_neg = statistics.covariance(x, y_negative)
    print(f"协方差: {covariance_neg:.4f}")
    
    # 计算皮尔逊相关系数
    print(f"\n皮尔逊相关系数计算:")
    try:
        # 注意：statistics模块中没有直接计算相关系数的函数
        # 我们可以使用协方差和标准差计算皮尔逊相关系数
        def pearson_correlation(x, y):
            cov = statistics.covariance(x, y)
            std_x = statistics.stdev(x)
            std_y = statistics.stdev(y)
            return cov / (std_x * std_y)
        
        corr_pos = pearson_correlation(x, y_positive)
        corr_neg = pearson_correlation(x, y_negative)
        
        print(f"正相关数据的皮尔逊相关系数: {corr_pos:.4f}")
        print(f"负相关数据的皮尔逊相关系数: {corr_neg:.4f}")
    except Exception as e:
        print(f"计算相关系数时出错: {e}")

statistics_correlation()
print()

# 6. 异常处理
print("=== 6. 异常处理 ===")
def statistics_exceptions():
    """展示statistics模块中的异常处理"""
    import statistics
    
    print(f"常见异常示例:")
    
    # 空数据集
    print(f"\n1. 空数据集:")
    try:
        statistics.mean([])
    except statistics.StatisticsError as e:
        print(f"异常: {type(e).__name__}: {e}")
    
    # 计算几何平均值时包含非正数
    print(f"\n2. 非正数数据(几何平均值):")
    try:
        statistics.geometric_mean([-1, 2, 3])
    except statistics.StatisticsError as e:
        print(f"异常: {type(e).__name__}: {e}")
    
    # 计算调和平均值时包含非正数或零
    print(f"\n3. 零或非正数数据(调和平均值):")
    try:
        statistics.harmonic_mean([0, 1, 2])
    except statistics.StatisticsError as e:
        print(f"异常: {type(e).__name__}: {e}")
    
    # 计算四分位数时数据不足
    print(f"\n4. 数据不足(四分位数):")
    try:
        statistics.quantiles([1, 2])
    except statistics.StatisticsError as e:
        print(f"异常: {type(e).__name__}: {e}")
    
    # 协方差计算时两个序列长度不匹配
    print(f"\n5. 序列长度不匹配(协方差):")
    try:
        statistics.covariance([1, 2, 3], [4, 5])
    except statistics.StatisticsError as e:
        print(f"异常: {type(e).__name__}: {e}")

statistics_exceptions()
print()

# 7. 高级应用示例
print("=== 7. 高级应用示例 ===")
def statistics_advanced_examples():
    """展示statistics模块的高级应用示例"""
    import statistics
    import random
    
    print("1. 数据描述性统计分析:")
    def descriptive_stats(data):
        """计算数据的描述性统计量"""
        stats = {}
        stats['count'] = len(data)
        stats['mean'] = statistics.mean(data)
        stats['median'] = statistics.median(data)
        stats['mode'] = statistics.mode(data)
        stats['min'] = min(data)
        stats['max'] = max(data)
        stats['range'] = max(data) - min(data)
        stats['stdev'] = statistics.stdev(data)
        stats['variance'] = statistics.variance(data)
        
        # 计算四分位数
        if len(data) >= 4:
            quartiles = statistics.quantiles(data, n=4)
            stats['q1'] = quartiles[0]
            stats['q3'] = quartiles[2]
            stats['iqr'] = quartiles[2] - quartiles[0]
        
        return stats
    
    # 生成模拟数据
    random.seed(42)  # 设置随机种子以获得可重复结果
    sample_data = [random.gauss(50, 10) for _ in range(100)]
    
    # 计算描述性统计量
    stats = descriptive_stats(sample_data)
    
    # 打印结果
    print(f"样本数据统计量:")
    for key, value in stats.items():
        print(f"  {key}: {value:.4f}")
    
    print("\n2. 检测异常值(使用IQR方法):")
    def detect_outliers_iqr(data, threshold=1.5):
        """使用IQR方法检测异常值"""
        if len(data) < 4:
            return [], [], []
        
        q1, q3 = statistics.quantiles(data, n=4)[0], statistics.quantiles(data, n=4)[2]
        iqr = q3 - q1
        
        lower_bound = q1 - threshold * iqr
        upper_bound = q3 + threshold * iqr
        
        outliers = [x for x in data if x < lower_bound or x > upper_bound]
        lower_outliers = [x for x in data if x < lower_bound]
        upper_outliers = [x for x in data if x > upper_bound]
        
        return outliers, lower_outliers, upper_outliers
    
    # 添加一些异常值
    sample_with_outliers = sample_data.copy()
    sample_with_outliers.extend([10, 20, 90, 100])  # 添加异常值
    
    outliers, lower_outliers, upper_outliers = detect_outliers_iqr(sample_with_outliers)
    
    print(f"检测到的异常值个数: {len(outliers)}")
    print(f"下界异常值: {lower_outliers}")
    print(f"上界异常值: {upper_outliers}")
    
    print("\n3. 数据分布特征分析:")
    def distribution_analysis(data):
        """分析数据分布特征"""
        analysis = {}
        analysis['skewness'] = statistics.skew(data)
        analysis['kurtosis'] = statistics.kurtosis(data)
        
        # 判断偏度类型
        if abs(analysis['skewness']) < 0.5:
            analysis['skewness_type'] = "近似对称"
        elif analysis['skewness'] > 0:
            analysis['skewness_type'] = "右偏(正偏)"
        else:
            analysis['skewness_type'] = "左偏(负偏)"
        
        # 判断峰度类型
        if abs(analysis['kurtosis']) < 0.5:
            analysis['kurtosis_type'] = "近似正态峰度"
        elif analysis['kurtosis'] > 0:
            analysis['kurtosis_type'] = "尖峰"
        else:
            analysis['kurtosis_type'] = "平峰"
        
        return analysis
    
    # 分析正态分布数据
    normal_data = [random.gauss(0, 1) for _ in range(1000)]
    normal_analysis = distribution_analysis(normal_data)
    
    print(f"正态分布数据特征:")
    for key, value in normal_analysis.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")
    
    # 分析右偏数据
    right_skewed_data = [random.expovariate(0.5) for _ in range(1000)]
    skewed_analysis = distribution_analysis(right_skewed_data)
    
    print(f"\n右偏数据特征:")
    for key, value in skewed_analysis.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.4f}")
        else:
            print(f"  {key}: {value}")

statistics_advanced_examples()
print()

# 8. 性能优化和注意事项
print("=== 8. 性能优化和注意事项 ===")
def statistics_performance_tips():
    """statistics模块的性能优化和注意事项"""
    print("1. 数据准备:")
    print("   - 确保数据是数值类型，statistics模块主要处理数值数据")
    print("   - 对于大型数据集，可以预先过滤无效值和异常值")
    print("   - 对于重复计算，考虑缓存结果而不是重复调用函数")
    
    print("\n2. 函数选择:")
    print("   - 根据需要选择合适的集中趋势测量函数(mean, median, mode等)")
    print("   - 对于有偏数据，median通常比mean更适合作为中心位置的度量")
    print("   - 对于存在异常值的数据集，使用median_abs_deviation可能比标准差更稳健")
    print("   - 对于总体数据使用pvariance/pstdev，对于样本数据使用variance/stdev")
    
    print("\n3. 性能考虑:")
    print("   - 对于非常大的数据集，statistics模块可能不是最高效的选择")
    print("   - 对于性能关键的应用，考虑使用numpy或pandas等库")
    print("   - 多次计算不同统计量时，可以先排序数据以提高效率")
    
    print("\n4. 异常处理:")
    print("   - 始终处理StatisticsError异常，特别是在处理用户输入或可能为空的数据集时")
    print("   - 注意几何平均值和调和平均值只适用于正实数数据")
    print("   - 协方差和相关系数计算要求两个序列长度相同")
    
    print("\n5. 版本兼容性:")
    print("   - statistics模块在Python 3.4及以上版本可用")
    print("   - 一些函数在较新版本中添加，如:")
    print("     - multimode()在Python 3.8中添加")
    print("     - quantiles()在Python 3.8中添加")
    print("     - median_abs_deviation()在Python 3.8中添加")
    print("     - covariance()在Python 3.10中添加")
    print("     - correlation()在Python 3.10中添加")
    print("   - 对于需要在多个Python版本间兼容的代码，应检查函数是否可用")

statistics_performance_tips()
print()

# 9. 输入输出示例
print("=== 9. 输入输出示例 ===")

def statistics_io_examples():
    """statistics模块的输入输出示例"""
    print("\n示例1: 基本统计量计算")
    print("输入:")
    print("    import statistics")
    print("    data = [2.5, 3.7, 1.2, 4.8, 5.6, 2.9, 3.1]")
    print("    print(f'平均值: {statistics.mean(data)}')")
    print("    print(f'中位数: {statistics.median(data)}')")
    print("    print(f'样本标准差: {statistics.stdev(data)}')")
    print("    print(f'样本方差: {statistics.variance(data)}')")
    print("输出:")
    print("    平均值: 3.4")
    print("    中位数: 3.1")
    print("    样本标准差: 1.4988888162869175")
    print("    样本方差: 2.246190476190476")
    
    print("\n示例2: 众数计算")
    print("输入:")
    print("    import statistics")
    print("    # 单众数数据")
    print("    data1 = [1, 2, 3, 2, 1, 2, 4]")
    print("    print(f'单众数: {statistics.mode(data1)}')")
    print("    # 多众数数据")
    print("    data2 = [1, 2, 3, 2, 1, 4]")
    print("    print(f'多众数: {statistics.multimode(data2)}')")
    print("输出:")
    print("    单众数: 2")
    print("    多众数: [1, 2]")
    
    print("\n示例3: 中位数变体")
    print("输入:")
    print("    import statistics")
    print("    # 偶数个元素")
    print("    even_data = [1, 2, 3, 4, 5, 6]")
    print("    print(f'中位数: {statistics.median(even_data)}')")
    print("    print(f'低中位数: {statistics.median_low(even_data)}')")
    print("    print(f'高中位数: {statistics.median_high(even_data)}')")
    print("输出:")
    print("    中位数: 3.5")
    print("    低中位数: 3")
    print("    高中位数: 4")
    
    print("\n示例4: 百分位数计算")
    print("输入:")
    print("    import statistics")
    print("    data = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
    print("    # 计算四分位数")
    print("    quartiles = statistics.quantiles(data, n=4)")
    print("    print(f'四分位数: {quartiles}')")
    print("    # 计算百分位数(例如25%和75%)")
    print("    q1 = statistics.quantiles(data, n=4)[0]")
    print("    q3 = statistics.quantiles(data, n=4)[2]")
    print("    print(f'25%分位数: {q1}')")
    print("    print(f'75%分位数: {q3}')")
    print("输出:")
    print("    四分位数: [3.0, 5.5, 8.0]")
    print("    25%分位数: 3.0")
    print("    75%分位数: 8.0")
    
    print("\n示例5: 几何平均值和调和平均值")
    print("输入:")
    print("    import statistics")
    print("    data = [2, 4, 8]")
    print("    print(f'算术平均值: {statistics.mean(data)}')")
    print("    print(f'几何平均值: {statistics.geometric_mean(data)}')")
    print("    print(f'调和平均值: {statistics.harmonic_mean(data)}')")
    print("输出:")
    print("    算术平均值: 4.666666666666667")
    print("    几何平均值: 4.0")
    print("    调和平均值: 3.4285714285714284")

statistics_io_examples()
print()

# 10. 总结和完整导入指南
print("=== 10. 总结和完整导入指南 ===")

def statistics_summary():
    """statistics模块总结和导入指南"""
    print("statistics模块是Python标准库中用于统计计算的模块，提供了计算各种统计量的函数。\n")
    
    # 主要功能分类
    print("主要功能分类:")
    print("1. 集中趋势测量:")
    print("   - mean(): 算术平均值")
    print("   - median(): 中位数")
    print("   - median_low(): 低中位数")
    print("   - median_high(): 高中位数")
    print("   - mode(): 单众数")
    print("   - multimode(): 多众数")
    print("   - geometric_mean(): 几何平均值")
    print("   - harmonic_mean(): 调和平均值")
    
    print("\n2. 离散度测量:")
    print("   - variance(): 样本方差")
    print("   - pvariance(): 总体方差")
    print("   - stdev(): 样本标准差")
    print("   - pstdev(): 总体标准差")
    print("   - quantiles(): 分位数")
    print("   - median_abs_deviation(): 中位数绝对偏差")
    
    print("\n3. 分布特征:")
    print("   - skew(): 偏度")
    print("   - kurtosis(): 峰度")
    
    print("\n4. 关联性测量:")
    print("   - covariance(): 协方差(Python 3.10+)")
    print("   - correlation(): 相关系数(Python 3.10+)")
    
    # 导入指南
    print("\n导入指南:")
    print("\n1. 导入整个模块:")
    print("   import statistics")
    print("   avg = statistics.mean([1, 2, 3, 4, 5])")
    
    print("\n2. 导入特定函数:")
    print("   from statistics import mean, median, stdev")
    print("   avg = mean([1, 2, 3, 4, 5])")
    
    print("\n3. 导入所有函数:")
    print("   from statistics import *")
    print("   avg = mean([1, 2, 3, 4, 5])")
    
    # 版本兼容性
    print("\n版本兼容性:")
    print("- statistics模块在Python 3.4及以上版本可用")
    print("- 新增函数:")
    print("  * multimode(): Python 3.8+")
    print("  * quantiles(): Python 3.8+")
    print("  * median_abs_deviation(): Python 3.8+")
    print("  * covariance(): Python 3.10+")
    print("  * correlation(): Python 3.10+")
    print("- 对于Python 3.4之前的版本，需要使用第三方库如numpy或pandas")
    
    # 最终建议
    print("\n最终建议:")
    print("- statistics模块适用于简单的统计分析和计算")
    print("- 对于复杂的数据分析，考虑使用专业库如numpy、scipy和pandas")
    print("- 始终注意数据质量，处理缺失值和异常值")
    print("- 选择合适的统计量来描述数据特征")
    print("- 在使用统计结果时，考虑数据的分布特性")
    print("- 对于需要在多个Python版本间兼容的代码，注意版本差异")

statistics_summary()

print("\n至此，statistics模块的全部功能已详细介绍完毕。")
