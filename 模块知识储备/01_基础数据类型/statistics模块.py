# statistics模块 - 统计计算库
# 功能作用：提供用于计算数值数据统计量的函数，如均值、中位数、标准差等
# 使用情景：数据分析、科学计算、金融统计、质量控制等需要统计分析的场景
# 注意事项：statistics模块主要处理数值数据，非数值数据会引发TypeError；对于空序列通常会引发StatisticsError

import statistics
import math
from collections import Counter

# 模块概述
"""
statistics模块提供了用于计算数值数据的数学统计量的函数。它包括：

1. 集中趋势度量：如均值、中位数、众数等
2. 离散度度量：如标准差、方差、范围等
3. 分布函数：如正态分布等
4. 相关性函数：如线性回归等

该模块设计用于处理现实世界中的数据，包括处理NaN值、空值和异常值的合理行为。
它同时支持整数、浮点数和Decimal等数值类型的输入。
"""

# 1. 集中趋势度量
print("=== 1. 集中趋势度量 ===")

def central_tendency():
    """集中趋势度量函数示例"""
    print("集中趋势度量函数:")
    
    # 测试数据
    data = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
    print(f"测试数据: {data}")
    print()
    
    # 算术平均值 (mean)
    print("算术平均值:")
    mean_val = statistics.mean(data)
    print(f"statistics.mean(data) = {mean_val}")
    
    # 手动计算验证
    manual_mean = sum(data) / len(data)
    print(f"手动计算: sum(data)/len(data) = {manual_mean}")
    print(f"结果一致: {mean_val == manual_mean}")
    print()
    
    # 中位数 (median)
    print("中位数:")
    median_val = statistics.median(data)
    print(f"statistics.median(data) = {median_val}")
    
    # 对于奇数个元素的数据集
    odd_data = [1, 2, 3, 4, 5]
    odd_median = statistics.median(odd_data)
    print(f"奇数个元素数据集 {odd_data} 的中位数: {odd_median}")
    
    # 对于偶数个元素的数据集
    even_data = [1, 2, 3, 4]
    even_median = statistics.median(even_data)
    print(f"偶数个元素数据集 {even_data} 的中位数: {even_median}")
    print()
    
    # 中位数的变种
    print("中位数的变种:")
    # median_low - 对于偶数个元素，返回较小的中间值
    print(f"statistics.median_low(data) = {statistics.median_low(data)}")
    print(f"statistics.median_low({even_data}) = {statistics.median_low(even_data)}")
    
    # median_high - 对于偶数个元素，返回较大的中间值
    print(f"statistics.median_high(data) = {statistics.median_high(data)}")
    print(f"statistics.median_high({even_data}) = {statistics.median_high(even_data)}")
    print()
    
    # 众数 (mode)
    print("众数:")
    # 简单数据集的众数
    mode_val = statistics.mode(data)
    print(f"statistics.mode(data) = {mode_val}")
    
    # 多众数数据集
    multimodal_data = [1, 2, 2, 3, 3, 4]
    try:
        print(f"多众数数据集 {multimodal_data} 的众数:")
        print(f"statistics.mode(multimodal_data) = {statistics.mode(multimodal_data)}")
    except statistics.StatisticsError as e:
        print(f"错误: {e}")
    
    # 使用multimode获取所有众数
    print(f"statistics.multimode(multimodal_data) = {statistics.multimode(multimodal_data)}")
    print(f"statistics.multimode(data) = {statistics.multimode(data)}")
    print()
    
    # 几何平均值 (geometric mean)
    print("几何平均值:")
    # 几何平均值只适用于正数
    positive_data = [2, 4, 8]
    geometric_mean_val = statistics.geometric_mean(positive_data)
    print(f"statistics.geometric_mean({positive_data}) = {geometric_mean_val}")
    
    # 手动计算验证: (2*4*8)^(1/3) = 64^(1/3) = 4
    product = 1
    for num in positive_data:
        product *= num
    manual_geo_mean = product ** (1/len(positive_data))
    print(f"手动计算: product^(1/n) = {manual_geo_mean}")
    print(f"结果一致: {abs(geometric_mean_val - manual_geo_mean) < 1e-10}")
    print()
    
    # 调和平均值 (harmonic mean)
    print("调和平均值:")
    # 调和平均值只适用于正数
    harmonic_mean_val = statistics.harmonic_mean(positive_data)
    print(f"statistics.harmonic_mean({positive_data}) = {harmonic_mean_val}")
    
    # 手动计算验证: n / (1/2 + 1/4 + 1/8)
    manual_harmonic_mean = len(positive_data) / sum(1/num for num in positive_data)
    print(f"手动计算: n / sum(1/x) = {manual_harmonic_mean}")
    print(f"结果一致: {abs(harmonic_mean_val - manual_harmonic_mean) < 1e-10}")

# 运行集中趋势度量示例
central_tendency()
print()

# 2. 离散度度量
print("=== 2. 离散度度量 ===")

def dispersion_measures():
    """离散度度量函数示例"""
    print("离散度度量函数:")
    
    # 测试数据
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    print(f"测试数据: {data}")
    print()
    
    # 数据范围 (range)
    print("数据范围:")
    # statistics模块没有直接提供range函数，但可以轻松计算
    data_range = max(data) - min(data)
    print(f"数据范围 = max(data) - min(data) = {data_range}")
    print()
    
    # 样本方差 (variance)
    print("样本方差:")
    variance_val = statistics.variance(data)
    print(f"statistics.variance(data) = {variance_val}")
    
    # 手动计算验证: 样本方差 = Σ(x_i - mean)^2 / (n-1)
    mean_val = sum(data) / len(data)
    squared_diffs = [(x - mean_val) ** 2 for x in data]
    manual_variance = sum(squared_diffs) / (len(data) - 1) if len(data) > 1 else 0
    print(f"手动计算: sum((x-mean)^2)/(n-1) = {manual_variance}")
    print(f"结果一致: {abs(variance_val - manual_variance) < 1e-10}")
    print()
    
    # 总体方差 (pvariance)
    print("总体方差:")
    pvariance_val = statistics.pvariance(data)
    print(f"statistics.pvariance(data) = {pvariance_val}")
    
    # 手动计算验证: 总体方差 = Σ(x_i - mean)^2 / n
    manual_pvariance = sum(squared_diffs) / len(data)
    print(f"手动计算: sum((x-mean)^2)/n = {manual_pvariance}")
    print(f"结果一致: {abs(pvariance_val - manual_pvariance) < 1e-10}")
    print()
    
    # 样本标准差 (stdev)
    print("样本标准差:")
    stdev_val = statistics.stdev(data)
    print(f"statistics.stdev(data) = {stdev_val}")
    
    # 手动计算验证: 样本标准差 = sqrt(样本方差)
    manual_stdev = math.sqrt(manual_variance)
    print(f"手动计算: sqrt(样本方差) = {manual_stdev}")
    print(f"结果一致: {abs(stdev_val - manual_stdev) < 1e-10}")
    print()
    
    # 总体标准差 (pstdev)
    print("总体标准差:")
    pstdev_val = statistics.pstdev(data)
    print(f"statistics.pstdev(data) = {pstdev_val}")
    
    # 手动计算验证: 总体标准差 = sqrt(总体方差)
    manual_pstdev = math.sqrt(manual_pvariance)
    print(f"手动计算: sqrt(总体方差) = {manual_pstdev}")
    print(f"结果一致: {abs(pstdev_val - manual_pstdev) < 1e-10}")
    print()
    
    # 四分位数和四分位距
    print("四分位数和四分位距:")
    # statistics模块没有直接提供四分位数函数，但可以通过以下方式计算
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # 计算四分位数
    def quartile(data, q):
        """计算第q四分位数 (q can be 1, 2, 3)"""
        n = len(data)
        if n == 0:
            raise statistics.StatisticsError("无法计算空数据的四分位数")
        
        # 排序数据
        sorted_data = sorted(data)
        
        # 计算位置
        pos = (n - 1) * q / 4.0
        
        # 线性插值
        lower = int(pos)
        upper = lower + 1 if lower < n - 1 else lower
        weight = pos - lower
        
        return sorted_data[lower] * (1 - weight) + sorted_data[upper] * weight
    
    q1 = quartile(data, 1)  # 第一四分位数
    q2 = quartile(data, 2)  # 第二四分位数（中位数）
    q3 = quartile(data, 3)  # 第三四分位数
    iqr = q3 - q1          # 四分位距
    
    print(f"第一四分位数 (Q1): {q1}")
    print(f"第二四分位数 (Q2): {q2} (与中位数相同: {statistics.median(data)})")
    print(f"第三四分位数 (Q3): {q3}")
    print(f"四分位距 (IQR): {iqr}")

# 运行离散度度量示例
dispersion_measures()
print()

# 3. 分布函数和数据特性
print("=== 3. 分布函数和数据特性 ===")

def distribution_functions():
    """分布函数和数据特性函数示例"""
    print("分布函数和数据特性:")
    
    # 测试数据
    normal_data = [1.2, 1.5, 1.8, 2.1, 2.3, 2.5, 2.7, 2.9, 3.1, 3.3]
    skewed_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]  # 右偏数据
    print(f"正态分布数据: {normal_data}")
    print(f"右偏数据: {skewed_data}")
    print()
    
    # 正态性检验（偏度和峰度）
    print("正态性检验:")
    
    # 计算偏度 (skewness)
    # statistics模块提供了skew函数，但实现简单版本以展示计算过程
    def skewness(data):
        """计算数据的偏度"""
        n = len(data)
        if n < 3:
            raise statistics.StatisticsError("偏度计算至少需要3个数据点")
        
        mean_val = sum(data) / n
        variance_val = sum((x - mean_val) ** 2 for x in data) / n
        std_dev = math.sqrt(variance_val)
        
        if std_dev == 0:
            return 0  # 所有数据相同，偏度为0
        
        # 计算三阶中心矩
        third_moment = sum((x - mean_val) ** 3 for x in data) / n
        
        # 计算偏度
        skew = third_moment / (std_dev ** 3)
        
        # Fisher's 无偏估计调整
        # 对于样本数据，应用调整因子
        skew *= math.sqrt(n * (n - 1)) / (n - 2)
        
        return skew
    
    # 计算峰度 (kurtosis)
    def kurtosis(data):
        """计算数据的峰度"""
        n = len(data)
        if n < 4:
            raise statistics.StatisticsError("峰度计算至少需要4个数据点")
        
        mean_val = sum(data) / n
        variance_val = sum((x - mean_val) ** 2 for x in data) / n
        std_dev = math.sqrt(variance_val)
        
        if std_dev == 0:
            return 0  # 所有数据相同，峰度为0
        
        # 计算四阶中心矩
        fourth_moment = sum((x - mean_val) ** 4 for x in data) / n
        
        # 计算峰度 (超额峰度)
        kurt = fourth_moment / (std_dev ** 4) - 3  # 减去3使其对正态分布为0
        
        # Fisher's 无偏估计调整
        # 对于样本数据，应用调整因子
        adjustment = (n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))
        adjustment *= (n * n - 1) / (n * n)
        kurt = kurt * adjustment + 3 * (n - 1) ** 2 / ((n - 2) * (n - 3)) - 3
        
        return kurt
    
    # 计算和显示偏度
    try:
        # 注意：Python 3.8+ 才有statistics.skew函数
        print(f"正态数据的偏度（近似）: {skewness(normal_data):.6f}")
        print(f"右偏数据的偏度（近似）: {skewness(skewed_data):.6f}")
    except Exception as e:
        print(f"偏度计算错误: {e}")
    
    # 计算和显示峰度
    try:
        # 注意：Python 3.8+ 才有statistics.kurtosis函数
        print(f"正态数据的峰度（近似）: {kurtosis(normal_data):.6f}")
        print(f"右偏数据的峰度（近似）: {kurtosis(skewed_data):.6f}")
    except Exception as e:
        print(f"峰度计算错误: {e}")
    print()
    
    # 数据特性分析
    print("数据特性分析:")
    
    # 计算异常值（使用IQR方法）
    def find_outliers_iqr(data):
        """使用IQR方法识别异常值"""
        sorted_data = sorted(data)
        n = len(sorted_data)
        
        # 计算四分位数
        q1_pos = (n - 1) * 0.25
        q1_lower = int(q1_pos)
        q1_upper = q1_lower + 1 if q1_lower < n - 1 else q1_lower
        q1 = sorted_data[q1_lower] * (1 - (q1_pos - q1_lower)) + sorted_data[q1_upper] * (q1_pos - q1_lower)
        
        q3_pos = (n - 1) * 0.75
        q3_lower = int(q3_pos)
        q3_upper = q3_lower + 1 if q3_lower < n - 1 else q3_lower
        q3 = sorted_data[q3_lower] * (1 - (q3_pos - q3_lower)) + sorted_data[q3_upper] * (q3_pos - q3_lower)
        
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        
        outliers = [x for x in data if x < lower_bound or x > upper_bound]
        
        return {
            'Q1': q1,
            'Q3': q3,
            'IQR': iqr,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'outliers': outliers
        }
    
    # 分析正态数据
    normal_outliers = find_outliers_iqr(normal_data)
    print("正态数据异常值分析:")
    print(f"  Q1 = {normal_outliers['Q1']:.2f}")
    print(f"  Q3 = {normal_outliers['Q3']:.2f}")
    print(f"  IQR = {normal_outliers['IQR']:.2f}")
    print(f"  下限 = {normal_outliers['lower_bound']:.2f}")
    print(f"  上限 = {normal_outliers['upper_bound']:.2f}")
    print(f"  异常值 = {normal_outliers['outliers']}")
    print()
    
    # 分析偏斜数据
    skewed_outliers = find_outliers_iqr(skewed_data)
    print("右偏数据异常值分析:")
    print(f"  Q1 = {skewed_outliers['Q1']:.2f}")
    print(f"  Q3 = {skewed_outliers['Q3']:.2f}")
    print(f"  IQR = {skewed_outliers['IQR']:.2f}")
    print(f"  下限 = {skewed_outliers['lower_bound']:.2f}")
    print(f"  上限 = {skewed_outliers['upper_bound']:.2f}")
    print(f"  异常值 = {skewed_outliers['outliers']}")
    print()
    
    # 频率分布
    print("频率分布:")
    
    # 创建一个稍微简单的数据用于演示
    frequency_data = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5]
    
    # 使用Counter计算频率
    frequency_counter = Counter(frequency_data)
    
    print(f"数据: {frequency_data}")
    print("频率分布:")
    for value, count in sorted(frequency_counter.items()):
        print(f"  值 {value}: 出现 {count} 次, 频率 {count/len(frequency_data):.2%}")

# 运行分布函数示例
distribution_functions()
print()

# 4. 相关性和回归
print("=== 4. 相关性和回归 ===")

def correlation_regression():
    """相关性和回归函数示例"""
    print("相关性和回归:")
    
    # 示例数据集 (X和Y有正相关关系)
    x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_data = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    # 负相关关系数据集
    x_neg_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_neg_data = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # 无相关关系数据集
    x_uncorr_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_uncorr_data = [5, 3, 8, 1, 10, 2, 7, 4, 9, 6]
    
    print(f"正相关数据集 - X: {x_data}, Y: {y_data}")
    print(f"负相关数据集 - X: {x_neg_data}, Y: {y_neg_data}")
    print(f"无相关数据集 - X: {x_uncorr_data}, Y: {y_uncorr_data}")
    print()
    
    # 计算皮尔逊相关系数
    def pearson_correlation(x, y):
        """计算皮尔逊相关系数"""
        n = len(x)
        if n != len(y):
            raise ValueError("两个数据集长度必须相同")
        if n < 2:
            raise ValueError("相关系数计算至少需要2对数据")
        
        # 计算均值
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        # 计算协方差
        covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        
        # 计算标准差
        std_x = math.sqrt(sum((xi - mean_x) ** 2 for xi in x) / n)
        std_y = math.sqrt(sum((yi - mean_y) ** 2 for yi in y) / n)
        
        if std_x == 0 or std_y == 0:
            return 0  # 无变化的数据，相关系数为0
        
        # 计算皮尔逊相关系数
        correlation = covariance / (n * std_x * std_y) * n  # 修正计算
        
        # 确保结果在-1到1之间
        return max(-1, min(1, correlation))
    
    # 计算正相关系数
    corr_pos = pearson_correlation(x_data, y_data)
    print(f"正相关数据集的皮尔逊相关系数: {corr_pos:.6f}")
    
    # 计算负相关系数
    corr_neg = pearson_correlation(x_neg_data, y_neg_data)
    print(f"负相关数据集的皮尔逊相关系数: {corr_neg:.6f}")
    
    # 计算无相关系数
    corr_uncorr = pearson_correlation(x_uncorr_data, y_uncorr_data)
    print(f"无相关数据集的皮尔逊相关系数: {corr_uncorr:.6f}")
    print()
    
    # 简单线性回归
    def linear_regression(x, y):
        """计算简单线性回归系数 (y = a + bx)"""
        n = len(x)
        if n != len(y):
            raise ValueError("两个数据集长度必须相同")
        if n < 2:
            raise ValueError("回归分析至少需要2对数据")
        
        # 计算均值
        mean_x = sum(x) / n
        mean_y = sum(y) / n
        
        # 计算斜率 (b)
        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = sum((xi - mean_x) ** 2 for xi in x)
        
        if denominator == 0:
            raise ValueError("X值必须有变化才能计算回归")
        
        b = numerator / denominator
        
        # 计算截距 (a)
        a = mean_y - b * mean_x
        
        # 计算决定系数 R²
        # 总平方和
        total_sum_squares = sum((yi - mean_y) ** 2 for yi in y)
        
        # 回归平方和
        regression_sum_squares = sum((a + b * xi - mean_y) ** 2 for xi in x)
        
        # 残差平方和
        residual_sum_squares = sum((yi - (a + b * xi)) ** 2 for xi, yi in zip(x, y))
        
        # 决定系数
        r_squared = 1 - (residual_sum_squares / total_sum_squares)
        if r_squared < 0:  # 处理浮点误差
            r_squared = 0
        
        return {
            'slope': b,           # 斜率
            'intercept': a,       # 截距
            'r_squared': r_squared, # 决定系数
            'correlation': corr_pos if corr_pos != 0 else pearson_correlation(x, y)  # 相关系数
        }
    
    # 对正相关数据进行回归分析
    regression_result = linear_regression(x_data, y_data)
    print("正相关数据的线性回归分析:")
    print(f"  回归方程: y = {regression_result['intercept']:.6f} + {regression_result['slope']:.6f} * x")
    print(f"  决定系数 R²: {regression_result['r_squared']:.6f}")
    print(f"  相关系数: {regression_result['correlation']:.6f}")
    print()
    
    # 使用回归模型进行预测
    def predict_y(x, slope, intercept):
        """使用回归模型预测y值"""
        return intercept + slope * x
    
    # 预测几个值
    print("使用回归模型进行预测:")
    for x in [0, 12, 15, 20]:
        y_pred = predict_y(x, regression_result['slope'], regression_result['intercept'])
        print(f"  当x = {x}时, 预测的y值 = {y_pred:.2f}")
    print()
    
    # 注意事项：外推的风险
    print("注意事项: 线性回归只在用于数据范围内的预测时最可靠。")
    print("过度外推（预测超出观测数据范围的值）可能导致不准确的结果。")

# 运行相关性和回归示例
correlation_regression()
print()

# 5. 实际应用示例
print("=== 5. 实际应用示例 ===")

def practical_applications():
    """实际应用示例"""
    print("实际应用示例:")
    
    # 示例1: 学生成绩分析
    def analyze_scores(scores):
        """分析学生成绩"""
        if not scores:
            return "没有成绩数据可分析"
        
        # 基本统计
        mean_score = statistics.mean(scores)
        median_score = statistics.median(scores)
        mode_scores = statistics.multimode(scores)
        min_score = min(scores)
        max_score = max(scores)
        score_range = max_score - min_score
        std_dev = statistics.stdev(scores)
        
        # 计算分位数
        sorted_scores = sorted(scores)
        n = len(sorted_scores)
        q1_pos = (n - 1) * 0.25
        q1 = sorted_scores[int(q1_pos)] * (1 - (q1_pos - int(q1_pos))) + sorted_scores[min(int(q1_pos) + 1, n - 1)] * (q1_pos - int(q1_pos))
        q3_pos = (n - 1) * 0.75
        q3 = sorted_scores[int(q3_pos)] * (1 - (q3_pos - int(q3_pos))) + sorted_scores[min(int(q3_pos) + 1, n - 1)] * (q3_pos - int(q3_pos))
        iqr = q3 - q1
        
        # 计算成绩分布
        grade_distribution = {
            'A': sum(1 for s in scores if s >= 90),
            'B': sum(1 for s in scores if 80 <= s < 90),
            'C': sum(1 for s in scores if 70 <= s < 80),
            'D': sum(1 for s in scores if 60 <= s < 70),
            'F': sum(1 for s in scores if s < 60)
        }
        
        return {
            'count': n,
            'mean': mean_score,
            'median': median_score,
            'mode': mode_scores,
            'min': min_score,
            'max': max_score,
            'range': score_range,
            'std_dev': std_dev,
            'Q1': q1,
            'Q3': q3,
            'IQR': iqr,
            'grades': grade_distribution
        }
    
    print("示例1: 学生成绩分析")
    student_scores = [85, 92, 78, 90, 88, 95, 75, 80, 82, 93, 87, 79, 81, 89, 91, 55, 100]
    score_analysis = analyze_scores(student_scores)
    
    print(f"学生人数: {score_analysis['count']}")
    print(f"平均分: {score_analysis['mean']:.2f}")
    print(f"中位数: {score_analysis['median']}")
    print(f"众数: {score_analysis['mode']}")
    print(f"最高分: {score_analysis['max']}")
    print(f"最低分: {score_analysis['min']}")
    print(f"分数范围: {score_analysis['range']}")
    print(f"标准差: {score_analysis['std_dev']:.2f}")
    print(f"第一四分位数 (Q1): {score_analysis['Q1']:.2f}")
    print(f"第三四分位数 (Q3): {score_analysis['Q3']:.2f}")
    print(f"四分位距 (IQR): {score_analysis['IQR']:.2f}")
    print("成绩分布:")
    for grade, count in score_analysis['grades'].items():
        print(f"  {grade}: {count} 人 ({count/score_analysis['count']:.1%})")
    print()
    
    # 示例2: 股票收益率分析
    def analyze_stock_returns(returns):
        """分析股票收益率"""
        if not returns:
            return "没有收益率数据可分析"
        
        # 基本统计
        mean_return = statistics.mean(returns)
        median_return = statistics.median(returns)
        std_dev = statistics.stdev(returns)
        min_return = min(returns)
        max_return = max(returns)
        
        # 计算额外的金融指标
        # 平均绝对偏差
        abs_devs = [abs(r - mean_return) for r in returns]
        mean_abs_dev = sum(abs_devs) / len(abs_devs)
        
        # 夏普比率 (假设无风险利率为0.01)
        risk_free_rate = 0.01
        sharpe_ratio = (mean_return - risk_free_rate / 252) / std_dev if std_dev != 0 else 0
        
        # 偏度 (近似)
        n = len(returns)
        skewness = sum((r - mean_return) ** 3 for r in returns) / (n * std_dev ** 3) if std_dev != 0 else 0
        
        # 峰度 (近似)
        kurtosis = sum((r - mean_return) ** 4 for r in returns) / (n * std_dev ** 4) - 3 if std_dev != 0 else 0
        
        # 最大回撤 (简化计算)
        cumulative = [100]
        for r in returns:
            cumulative.append(cumulative[-1] * (1 + r))
        
        max_dd = 0
        peak = cumulative[0]
        for val in cumulative:
            if val > peak:
                peak = val
            dd = (peak - val) / peak
            if dd > max_dd:
                max_dd = dd
        
        return {
            'mean_daily_return': mean_return,
            'annualized_return': mean_return * 252,
            'median_return': median_return,
            'std_dev': std_dev,
            'annualized_volatility': std_dev * math.sqrt(252),
            'min_return': min_return,
            'max_return': max_return,
            'mean_abs_dev': mean_abs_dev,
            'sharpe_ratio': sharpe_ratio * math.sqrt(252),  # 年化夏普比率
            'skewness': skewness,
            'kurtosis': kurtosis,
            'max_drawdown': max_dd
        }
    
    print("示例2: 股票收益率分析")
    # 模拟股票日收益率数据 (百分比形式)
    import random
    random.seed(42)  # 设置随机种子以获得可重复的结果
    daily_returns = [random.gauss(0.04/252, 0.2/math.sqrt(252)) for _ in range(252)]  # 年化4%收益率，20%波动率
    
    stock_analysis = analyze_stock_returns(daily_returns)
    
    print(f"平均日收益率: {stock_analysis['mean_daily_return']*100:.6f}%")
    print(f"年化收益率: {stock_analysis['annualized_return']*100:.2f}%")
    print(f"中位数日收益率: {stock_analysis['median_return']*100:.6f}%")
    print(f"日收益率标准差: {stock_analysis['std_dev']*100:.6f}%")
    print(f"年化波动率: {stock_analysis['annualized_volatility']*100:.2f}%")
    print(f"最大单日涨幅: {stock_analysis['max_return']*100:.2f}%")
    print(f"最大单日跌幅: {stock_analysis['min_return']*100:.2f}%")
    print(f"平均绝对偏差: {stock_analysis['mean_abs_dev']*100:.6f}%")
    print(f"年化夏普比率: {stock_analysis['sharpe_ratio']:.2f}")
    print(f"收益率偏度: {stock_analysis['skewness']:.6f}")
    print(f"收益率峰度: {stock_analysis['kurtosis']:.6f}")
    print(f"最大回撤: {stock_analysis['max_drawdown']*100:.2f}%")
    print()
    
    # 示例3: A/B测试结果分析
    def analyze_ab_test(control_data, treatment_data):
        """分析A/B测试结果"""
        if not control_data or not treatment_data:
            return "数据不足，无法进行A/B测试分析"
        
        # 基本统计
        control_mean = statistics.mean(control_data)
        treatment_mean = statistics.mean(treatment_data)
        
        control_std = statistics.stdev(control_data)
        treatment_std = statistics.stdev(treatment_data)
        
        control_n = len(control_data)
        treatment_n = len(treatment_data)
        
        # 计算均值差
        mean_diff = treatment_mean - control_mean
        
        # 计算差异百分比
        percent_change = (mean_diff / control_mean) * 100 if control_mean != 0 else float('inf')
        
        # 计算标准误
        pooled_std_error = math.sqrt(
            (control_std**2 / control_n) + (treatment_std**2 / treatment_n)
        )
        
        # 计算t统计量
        t_statistic = mean_diff / pooled_std_error if pooled_std_error != 0 else 0
        
        # 注意: 真实的p值计算需要更复杂的统计库
        # 这里提供一个简化的p值估计（仅供演示）
        # 对于双侧检验，|t| > 1.96 对应p < 0.05（近似）
        p_value_estimate = "< 0.05" if abs(t_statistic) > 1.96 else ">= 0.05"
        
        return {
            'control_mean': control_mean,
            'treatment_mean': treatment_mean,
            'mean_difference': mean_diff,
            'percent_change': percent_change,
            'control_std': control_std,
            'treatment_std': treatment_std,
            'control_n': control_n,
            'treatment_n': treatment_n,
            't_statistic': t_statistic,
            'p_value_estimate': p_value_estimate,
            'statistically_significant': abs(t_statistic) > 1.96
        }
    
    print("示例3: A/B测试结果分析")
    # 模拟A/B测试数据 (例如，网站点击转化率)
    # 控制组 - 旧版本网站
    control_conversion = [0.12, 0.11, 0.13, 0.12, 0.14, 0.11, 0.12, 0.13, 0.10, 0.12]
    
    # 实验组 - 新版本网站
    treatment_conversion = [0.14, 0.15, 0.13, 0.14, 0.16, 0.15, 0.14, 0.13, 0.15, 0.14]
    
    ab_result = analyze_ab_test(control_conversion, treatment_conversion)
    
    print(f"控制组平均转化率: {ab_result['control_mean']*100:.2f}%")
    print(f"实验组平均转化率: {ab_result['treatment_mean']*100:.2f}%")
    print(f"转化率差异: {ab_result['mean_difference']*100:.2f}%")
    print(f"提升百分比: {ab_result['percent_change']:.2f}%")
    print(f"控制组标准差: {ab_result['control_std']*100:.2f}%")
    print(f"实验组标准差: {ab_result['treatment_std']*100:.2f}%")
    print(f"控制组样本量: {ab_result['control_n']}")
    print(f"实验组样本量: {ab_result['treatment_n']}")
    print(f"t统计量: {ab_result['t_statistic']:.4f}")
    print(f"p值估计: {ab_result['p_value_estimate']}")
    print(f"结果是否统计显著: {'是' if ab_result['statistically_significant'] else '否'}")
    print(f"结论: {'新版本显著提高了转化率' if ab_result['statistically_significant'] else '未观察到新版本对转化率的显著影响'}")

# 运行实际应用示例
practical_applications()
print()

# 6. 错误处理和边缘情况
print("=== 6. 错误处理和边缘情况 ===")

def error_handling():
    """错误处理和边缘情况处理"""
    print("错误处理和边缘情况处理:")
    
    # 空数据集处理
    print("\n1. 空数据集处理:")
    empty_data = []
    
    functions_to_test = [
        statistics.mean,
        statistics.median,
        statistics.mode,
        statistics.stdev,
        statistics.variance
    ]
    
    for func in functions_to_test:
        try:
            result = func(empty_data)
            print(f"{func.__name__}([]) = {result}")
        except statistics.StatisticsError as e:
            print(f"{func.__name__}([]) 引发错误: {e}")
        except Exception as e:
            print(f"{func.__name__}([]) 引发意外错误: {e}")
    print()
    
    # 单元素数据集处理
    print("\n2. 单元素数据集处理:")
    single_element = [42]
    
    for func in functions_to_test:
        try:
            result = func(single_element)
            print(f"{func.__name__}([42]) = {result}")
        except statistics.StatisticsError as e:
            print(f"{func.__name__}([42]) 引发错误: {e}")
        except Exception as e:
            print(f"{func.__name__}([42]) 引发意外错误: {e}")
    print()
    
    # 非数值数据处理
    print("\n3. 非数值数据处理:")
    mixed_data = [1, 2, 3, "four", 5]
    
    for func in functions_to_test:
        try:
            result = func(mixed_data)
            print(f"{func.__name__}([1, 2, 3, 'four', 5]) = {result}")
        except TypeError as e:
            print(f"{func.__name__}([1, 2, 3, 'four', 5]) 引发类型错误: {e}")
        except Exception as e:
            print(f"{func.__name__}([1, 2, 3, 'four', 5]) 引发意外错误: {e}")
    print()
    
    # NaN值处理
    print("\n4. NaN值处理:")
    import math
    data_with_nan = [1, 2, float('nan'), 4, 5]
    
    for func in functions_to_test:
        try:
            result = func(data_with_nan)
            print(f"{func.__name__}(含NaN数据) = {result}")
        except statistics.StatisticsError as e:
            print(f"{func.__name__}(含NaN数据) 引发统计错误: {e}")
        except Exception as e:
            print(f"{func.__name__}(含NaN数据) 引发意外错误: {e}")
    print()
    
    # 健壮的统计计算函数示例
    print("\n5. 健壮的统计计算函数示例:")
    print("""
    def safe_stat_calculation(data, function, default=None, remove_nan=True):
        """安全的统计计算函数
        
        Args:
            data: 数据序列
            function: 要应用的统计函数
            default: 出错时返回的默认值
            remove_nan: 是否移除NaN值
            
        Returns:
            统计函数的结果或默认值
        """
        try:
            # 复制数据以避免修改原始数据
            processed_data = list(data)
            
            # 移除NaN值
            if remove_nan:
                processed_data = [x for x in processed_data if not (isinstance(x, float) and math.isnan(x))]
            
            # 检查数据是否为空
            if not processed_data:
                if default is not None:
                    return default
                raise statistics.StatisticsError("处理后的数据为空")
            
            # 检查是否所有元素都是数值
            for x in processed_data:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"非数值元素: {x}")
            
            # 应用统计函数
            return function(processed_data)
        except Exception as e:
            if default is not None:
                return default
            raise
    
    # 使用示例
    mixed_data = [1, 2, 3, None, 5, float('nan')]
    
    safe_mean = safe_stat_calculation(mixed_data, statistics.mean)
    safe_median = safe_stat_calculation(mixed_data, statistics.median)
    safe_stdev = safe_stat_calculation(mixed_data, statistics.stdev)
    """)

# 运行错误处理示例
error_handling()
print()

# 7. 最佳实践和注意事项
print("=== 7. 最佳实践和注意事项 ===")

def best_practices():
    """statistics模块使用的最佳实践和注意事项"""
    
    print("statistics模块使用的最佳实践和注意事项:")
    
    # 数据准备
    print("\n1. 数据准备:")
    print("   - 始终检查数据质量，包括缺失值、异常值和数据类型")
    print("   - 在计算统计量前清洗和预处理数据")
    print("   - 对于大型数据集，考虑使用NumPy或pandas以提高性能")
    
    # 选择适当的统计量
    print("\n2. 选择适当的统计量:")
    print("   - 对于对称分布的数据，使用均值作为集中趋势的度量")
    print("   - 对于偏斜分布或含有异常值的数据，使用中位数更稳健")
    print("   - 使用众数来描述类别数据的集中趋势")
    print("   - 始终结合多个统计量来全面描述数据")
    
    # 理解样本和总体统计量
    print("\n3. 理解样本和总体统计量:")
    print("   - 使用statistics.variance()和statistics.stdev()计算样本统计量")
    print("   - 使用statistics.pvariance()和statistics.pstdev()计算总体统计量")
    print("   - 对于样本数据，默认使用样本统计量(分母为n-1)以获得无偏估计")
    
    # 处理异常值
    print("\n4. 处理异常值:")
    print("   - 在分析前识别和评估异常值")
    print("   - 使用箱线图或IQR方法检测异常值")
    print("   - 考虑异常值是数据错误还是真实的极端值")
    print("   - 对于异常值敏感的统计量(如均值)，考虑使用稳健的替代方法")
    
    # 相关性和因果关系
    print("\n5. 相关性和因果关系:")
    print("   - 相关性不等于因果关系")
    print("   - 即使两个变量高度相关，也不能直接推断它们之间存在因果关系")
    print("   - 使用回归分析时，考虑其他可能的解释变量")
    
    # 避免过度解释
    print("\n6. 避免过度解释:")
    print("   - 考虑样本大小对统计显著性的影响")
    print("   - 对于小样本，统计结果可能不够可靠")
    print("   - 始终报告效应大小，不仅仅是统计显著性")
    
    # 选择合适的工具
    print("\n7. 选择合适的工具:")
    print("   - statistics模块适用于简单的统计分析")
    print("   - 对于复杂的统计分析，考虑使用SciPy、statsmodels等专门的统计库")
    print("   - 对于数据处理和可视化，pandas和matplotlib是很好的选择")
    print("   - 对于机器学习任务，scikit-learn提供了更全面的功能")
    
    # 示例代码：高效统计分析函数
    print("\n8. 示例：高效的统计分析函数:")
    print("""
    def comprehensive_stats(data, remove_outliers=False, outlier_threshold=1.5):
        """提供全面的统计摘要，支持异常值处理
        
        Args:
            data: 数值数据序列
            remove_outliers: 是否移除异常值
            outlier_threshold: IQR倍数，用于定义异常值
            
        Returns:
            包含各种统计量的字典
        """
        # 转换为浮点数列表并移除非数值
        clean_data = []
        for item in data:
            try:
                num = float(item)
                if not math.isnan(num):
                    clean_data.append(num)
            except (ValueError, TypeError):
                pass
        
        if not clean_data:
            raise ValueError("没有有效数据进行统计分析")
        
        # 处理异常值
        if remove_outliers:
            sorted_data = sorted(clean_data)
            n = len(sorted_data)
            
            # 计算四分位数
            q1_idx = int(n * 0.25)
            q3_idx = int(n * 0.75)
            q1 = sorted_data[q1_idx]
            q3 = sorted_data[q3_idx]
            iqr = q3 - q1
            
            # 定义异常值边界
            lower_bound = q1 - outlier_threshold * iqr
            upper_bound = q3 + outlier_threshold * iqr
            
            # 过滤异常值
            clean_data = [x for x in clean_data if lower_bound <= x <= upper_bound]
            
            if not clean_data:
                raise ValueError("移除异常值后没有数据")
        
        # 计算基本统计量
        n = len(clean_data)
        mean_val = statistics.mean(clean_data)
        median_val = statistics.median(clean_data)
        mode_val = statistics.multimode(clean_data)
        min_val = min(clean_data)
        max_val = max(clean_data)
        
        # 计算离散度统计量
        if n > 1:
            variance_val = statistics.variance(clean_data)
            std_dev_val = statistics.stdev(clean_data)
            
            # 计算四分位数
            sorted_data = sorted(clean_data)
            q1_idx = int(n * 0.25)
            q3_idx = int(n * 0.75)
            q1 = sorted_data[q1_idx]
            q3 = sorted_data[q3_idx]
            iqr_val = q3 - q1
        else:
            variance_val = std_dev_val = iqr_val = 0
            q1 = q3 = mean_val
        
        # 返回综合统计结果
        return {
            'count': n,
            'mean': mean_val,
            'median': median_val,
            'mode': mode_val,
            'min': min_val,
            'max': max_val,
            'range': max_val - min_val,
            'variance': variance_val,
            'std_dev': std_dev_val,
            'Q1': q1,
            'Q3': q3,
            'IQR': iqr_val,
            'outliers_removed': remove_outliers
        }
    """)

# 运行最佳实践示例
best_practices()

# 总结
print("\n=== 总结 ===")
print("statistics模块是Python标准库中用于统计计算的重要工具，提供了丰富的统计函数。")
print("主要功能和优势包括：")
print("1. 提供各种集中趋势度量：均值、中位数、众数、几何均值和调和均值")
print("2. 提供离散度度量：方差、标准差、四分位数等")
print("3. 包含相关性和回归分析功能")
print("4. 提供对异常值和边缘情况的合理处理")
print("5. 支持各种数值类型（整数、浮点数、Decimal等）")
print()
print("在使用statistics模块时，应注意数据质量、选择适当的统计量、理解样本和总体的区别，并避免统计陷阱。")
print("对于复杂的统计分析需求，可以结合SciPy、statsmodels、pandas等专业库。")
print()
print("掌握statistics模块的使用对于数据分析、科学研究、金融计算等领域的Python编程非常有价值。")

# 运行完整演示
if __name__ == "__main__":
    print("Python statistics模块演示\n")
    print("请参考源代码中的详细示例和说明")