# collections.Counter模块 - Python标准库中的计数工具

"""
collections.Counter是Python标准库中collections模块提供的一个字典子类，
专门用于计数可哈希对象。它提供了多种便捷的方法来统计、合并和操作元素计数，
在数据分析、文本处理和算法实现中非常有用。

Counter对象本质上是一个字典，其中键是被计数的元素，值是该元素出现的次数。
它支持所有字典操作，并添加了额外的计数相关功能。
"""

# 1. 核心功能介绍

print("=== 1. 核心功能介绍 ===")
print("\ncollections.Counter模块提供了以下主要功能:")
print("1. 高效统计可哈希对象的出现频率")
print("2. 支持多种初始化方式（可迭代对象、映射、关键字参数）")
print("3. 提供便捷的计数操作方法（增加、减少、清除计数）")
print("4. 支持元素计数的排序、合并和数学运算")
print("5. 提供查找最常见元素的功能")
print("6. 可以与其他集合类型进行转换")

# 2. 基本操作

print("\n=== 2. 基本操作 ===")

# 导入Counter
from collections import Counter

print("\n2.1 创建Counter对象")
print("Counter可以通过多种方式初始化:")

# 从可迭代对象创建
counter1 = Counter('abracadabra')
print(f"从字符串创建: {counter1}")

counter2 = Counter([1, 2, 3, 1, 2, 1, 4, 5])
print(f"从列表创建: {counter2}")

counter3 = Counter({'a': 3, 'b': 2, 'c': 1})
print(f"从字典创建: {counter3}")

counter4 = Counter(a=3, b=2, c=1)
print(f"从关键字参数创建: {counter4}")

print("\n2.2 访问和修改计数")
print("可以像字典一样访问和修改Counter对象中的计数:")

# 创建一个Counter对象
c = Counter('banana')
print(f"初始Counter: {c}")

# 访问元素计数
print(f"'a'的计数: {c['a']}")
print(f"'b'的计数: {c['b']}")
print(f"不存在元素'x'的计数: {c['x']}")  # 不会抛出KeyError，而是返回0

# 修改元素计数
c['a'] += 1
print(f"增加'a'的计数后: {c}")

c['b'] -= 1
print(f"减少'b'的计数后: {c}")

c['x'] = 1  # 添加新元素
print(f"添加新元素'x'后: {c}")

print("\n2.3 检查元素是否存在")
print("可以使用in操作符检查元素是否存在:")

c = Counter('banana')
print(f"Counter: {c}")
print(f"'a'在Counter中: {'a' in c}")
print(f"'x'在Counter中: {'x' in c}")

# 注意：访问不存在的元素不会将其添加到Counter中
print(f"访问'x'后的Counter: {c}")

print("\n2.4 遍历Counter")
print("可以像遍历字典一样遍历Counter:")

c = Counter('banana')

# 遍历键
print("遍历键:")
for key in c:
    print(f"  {key}")

# 遍历值
print("遍历值:")
for value in c.values():
    print(f"  {value}")

# 遍历键值对
print("遍历键值对:")
for key, value in c.items():
    print(f"  {key}: {value}")

print("\n2.5 清空Counter")
print("使用clear()方法清空Counter中的所有元素:")

c = Counter('banana')
print(f"清空前: {c}")
c.clear()
print(f"清空后: {c}")

# 3. 高级用法

print("\n=== 3. 高级用法 ===")

print("\n3.1 most_common方法")
print("most_common()方法返回出现频率最高的n个元素及其计数:")

# 创建Counter对象
c = Counter('the quick brown fox jumps over the lazy dog')

# 获取出现频率最高的5个字符
print("频率最高的5个字符:")
for char, count in c.most_common(5):
    print(f"  '{char}': {count}")

# 获取所有元素（按频率降序排列）
print("所有元素按频率降序排列:")
for char, count in c.most_common():
    print(f"  '{char}': {count}")

print("\n3.2 elements方法")
print("elements()方法返回一个迭代器，包含所有元素，每个元素重复的次数等于其计数:")

c = Counter(a=3, b=2, c=1)

# 获取所有元素的迭代器
print("所有元素（不保证顺序）:")
elements = list(c.elements())
print(elements)

# 注意：计数小于等于0的元素不会被包含
c['c'] = 0
c['d'] = -1
print("移除计数为0和负数的元素后:")
elements = list(c.elements())
print(elements)

print("\n3.3 update方法")
print("update()方法用于更新Counter中的计数，可以接受多种输入格式:")

# 初始Counter
c = Counter(a=1, b=2)
print(f"初始Counter: {c}")

# 使用可迭代对象更新
c.update('abba')
print(f"使用字符串'update'更新后: {c}")

# 使用字典更新
c.update({'a': 1, 'c': 3})
print(f"使用字典更新后: {c}")

# 使用关键字参数更新
c.update(a=1, b=-2, d=4)
print(f"使用关键字参数更新后: {c}")

print("\n3.4 subtract方法")
print("subtract()方法用于减去指定的计数，可以接受多种输入格式:")

# 初始Counter
c = Counter(a=5, b=3, c=1)
print(f"初始Counter: {c}")

# 使用可迭代对象减去
c.subtract('abc')
print(f"使用字符串'abc'减去后: {c}")

# 使用字典减去
c.subtract({'a': 2, 'b': 1})
print(f"使用字典减去后: {c}")

# 使用关键字参数减去
c.subtract(a=1, c=-2)
print(f"使用关键字参数减去后: {c}")

print("\n3.5 数学运算")
print("Counter支持多种数学运算，包括加法、减法、交集和并集:")

c1 = Counter(a=3, b=1, c=2)
c2 = Counter(a=1, b=2, d=1)

print(f"c1: {c1}")
print(f"c2: {c2}")

# 加法：c1 + c2，对应元素计数相加
print(f"加法 c1 + c2: {c1 + c2}")

# 减法：c1 - c2，只保留计数为正的元素
print(f"减法 c1 - c2: {c1 - c2}")
print(f"减法 c2 - c1: {c2 - c1}")

# 交集：c1 & c2，取对应元素计数的最小值
print(f"交集 c1 & c2: {c1 & c2}")

# 并集：c1 | c2，取对应元素计数的最大值
print(f"并集 c1 | c2: {c1 | c2}")

print("\n3.6 集合操作")
print("Counter可以与集合进行类似的操作:")

c = Counter(a=3, b=2, c=1, d=0, e=-1)

# 获取所有正计数的元素（相当于集合的元素）
print(f"正计数元素: {list(c.elements())}")

# 转换为集合（只包含正计数的键）
print(f"转换为集合: {set(c)}")

# 获取所有键（包括计数为0或负的）
print(f"所有键: {list(c.keys())}")

print("\n3.7 计数器的复制")
print("Counter可以被复制，支持浅拷贝:")

c1 = Counter(a=3, b=2, c=1)

# 使用copy()方法复制
c2 = c1.copy()
c2['a'] = 5

print(f"原始Counter: {c1}")
print(f"复制后的Counter: {c2}")

# 使用dict构造函数创建新的Counter
c3 = Counter(c1)
c3['b'] = 4

print(f"使用Counter()构造函数复制: {c3}")

print("\n3.8 与其他数据类型的转换")
print("Counter可以与其他数据类型相互转换:")

c = Counter(a=3, b=2, c=1)

# 转换为字典
print(f"转换为字典: {dict(c)}")

# 转换为列表（只包含键）
print(f"转换为列表（键）: {list(c)}")

# 转换为集合
print(f"转换为集合: {set(c)}")

# 转换为元组列表（键值对）
print(f"转换为元组列表: {list(c.items())}")

# 从元组列表创建
c_from_items = Counter(dict([('a', 3), ('b', 2), ('c', 1)]))
print(f"从元组列表创建: {c_from_items}")

# 4. 实际应用场景

print("\n=== 4. 实际应用场景 ===")

print("\n4.1 文本分析和词频统计")
print("Counter最常见的用途之一是进行文本分析和词频统计:")

print("\n示例: 文本词频统计")

# 示例文本
text = """
Python is a high-level, interpreted, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms,
including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.
"""

# 预处理文本：转换为小写并分割成单词
def preprocess_text(text):
    # 转换为小写
    text = text.lower()
    
    # 移除标点符号
    import re
    text = re.sub(r'[.,;:"\'-]', ' ', text)
    
    # 分割成单词并过滤空字符串
    words = [word.strip() for word in text.split() if word.strip()]
    
    return words

# 预处理文本
words = preprocess_text(text)

# 使用Counter统计词频
word_counts = Counter(words)

# 显示最常见的10个单词
print("最常见的10个单词:")
for word, count in word_counts.most_common(10):
    print(f"  '{word}': {count}")

# 计算词汇丰富度（不同单词数量除以总单词数量）
vocabulary_size = len(word_counts)
total_words = sum(word_counts.values())
lexical_diversity = vocabulary_size / total_words

print(f"\n文本统计:")
print(f"  总单词数: {total_words}")
print(f"  不同单词数: {vocabulary_size}")
print(f"  词汇丰富度: {lexical_diversity:.4f}")

print("\n4.2 数据分析中的频率计算")
print("在数据分析中，Counter可以用来计算各种类别的频率:")

print("\n示例: 分析学生成绩分布")

# 示例：学生成绩数据
scores = [85, 92, 78, 90, 88, 76, 95, 82, 87, 91, 
          83, 89, 77, 94, 86, 93, 79, 84, 80, 96]

# 将分数转换为等级
def score_to_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# 计算等级分布
grades = [score_to_grade(score) for score in scores]
grade_counts = Counter(grades)

# 计算总人数
total_students = len(scores)

# 显示等级分布
print("学生成绩等级分布:")
for grade, count in sorted(grade_counts.items()):
    percentage = (count / total_students) * 100
    print(f"  等级 {grade}: {count} 人 ({percentage:.1f}%)")

print(f"\n平均分: {sum(scores) / total_students:.2f}")
print(f"最高分: {max(scores)}")
print(f"最低分: {min(scores)}")

print("\n4.3 重复元素检测和去重")
print("Counter可以用来检测和处理重复元素:")

print("\n示例: 检测列表中的重复元素")

# 示例列表
items = ['a', 'b', 'c', 'a', 'd', 'b', 'a', 'e', 'f', 'b', 'g']

# 使用Counter统计每个元素的出现次数
item_counts = Counter(items)

# 找出重复的元素（出现次数大于1的元素）
duplicates = [item for item, count in item_counts.items() if count > 1]
print(f"重复元素: {duplicates}")

# 统计每个重复元素的出现次数
print("重复元素统计:")
for item in duplicates:
    print(f"  '{item}': {item_counts[item]}次")

# 去重（保留顺序）
def deduplicate_preserve_order(seq):
    seen = set()
    return [x for x in seq if not (x in seen or seen.add(x))]

# 去重并保持原顺序
unique_items = deduplicate_preserve_order(items)
print(f"去重后的列表: {unique_items}")

print("\n4.4 投票和多数元素查找")
print("Counter可以用于实现投票系统和查找多数元素:")

print("\n示例: 找出多数元素（出现次数超过一半的元素）")

# 示例投票数据
votes = [1, 2, 1, 3, 1, 2, 1, 1, 3, 1, 1, 2, 1]

# 使用Counter统计投票
vote_counts = Counter(votes)

# 找出得票最多的元素
most_common = vote_counts.most_common(1)[0]
print(f"得票最多的元素: {most_common[0]}，得票: {most_common[1]}票")

# 检查是否有多数元素（得票超过总票数的一半）
total_votes = len(votes)
if most_common[1] > total_votes / 2:
    print(f"元素 {most_common[0]} 是多数元素，得票率: {(most_common[1] / total_votes) * 100:.1f}%")
else:
    print("没有多数元素（没有元素得票超过总票数的一半）")

# 模拟选举系统
print("\n模拟选举系统:")

candidates = ['Alice', 'Bob', 'Charlie', 'Diana']
election_votes = ['Alice', 'Bob', 'Charlie', 'Alice', 'Diana', 'Alice', 'Bob', 
                  'Alice', 'Charlie', 'Alice', 'Bob', 'Diana', 'Alice']

# 统计选举结果
election_results = Counter(election_votes)

print("选举结果:")
for candidate, votes_count in election_results.most_common():
    percentage = (votes_count / len(election_votes)) * 100
    print(f"  {candidate}: {votes_count}票 ({percentage:.1f}%)")

print("\n4.5 字符频率分析（用于简单加密破解）")
print("Counter可以用于进行简单的字符频率分析，这在加密学中有用:")

print("\n示例: 字符频率分析")

# 示例密文（实际上只是普通文本，用于演示）
ciphertext = "GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK."

# 统计字符频率（不区分大小写，忽略非字母字符）
import re

# 提取字母并转换为小写
letters = re.findall(r'[A-Z]', ciphertext)
letter_counts = Counter(letters)

# 计算总字母数
total_letters = len(letters)

print("字符频率分析:")
for letter, count in letter_counts.most_common():
    frequency = (count / total_letters) * 100
    print(f"  {letter}: {count}次 ({frequency:.1f}%)")

# 英文字母频率参考（真实数据的近似值）
english_frequencies = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 
    'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25,
    'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36,
    'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29,
    'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07
}

print("\n英文字母平均频率参考:")
for letter, freq in sorted(english_frequencies.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"  {letter}: {freq:.1f}%")

print("\n4.6 购物篮分析")
print("Counter可以用于进行简单的购物篮分析，找出经常一起购买的商品:")

print("\n示例: 简单购物篮分析")

# 示例购物篮数据（每个列表代表一个顾客购买的商品）
baskets = [
    ['牛奶', '面包', '黄油', '鸡蛋'],
    ['面包', '黄油', '果酱'],
    ['牛奶', '面包', '饼干'],
    ['牛奶', '鸡蛋', '饼干', '水果'],
    ['面包', '黄油', '果酱', '巧克力'],
    ['牛奶', '饼干', '水果'],
    ['面包', '黄油', '果酱'],
    ['牛奶', '面包', '黄油', '果酱', '巧克力']
]

# 统计每个商品的出现次数
product_counts = Counter()
for basket in baskets:
    product_counts.update(basket)

print("商品销售频率:")
for product, count in product_counts.most_common():
    percentage = (count / len(baskets)) * 100
    print(f"  {product}: {count}次 ({percentage:.1f}%)")

# 计算商品两两之间的共同出现频率
from itertools import combinations

# 统计商品对的共同出现次数
product_pairs = Counter()
for basket in baskets:
    # 生成所有可能的商品对
    pairs = combinations(sorted(basket), 2)
    product_pairs.update(pairs)

print("\n最常见的商品组合:")
for pair, count in product_pairs.most_common(5):
    percentage = (count / len(baskets)) * 100
    print(f"  {pair}: {count}次 ({percentage:.1f}%)")

print("\n4.7 日志分析")
print("Counter可以用于分析日志文件，统计不同类型的事件或错误:")

print("\n示例: 日志级别统计")

# 模拟日志条目
log_entries = [
    "2023-06-01 10:15:23 INFO User login successful: user123",
    "2023-06-01 10:16:45 WARNING Disk space is running low",
    "2023-06-01 10:17:30 ERROR Database connection failed",
    "2023-06-01 10:18:15 INFO User logout: user123",
    "2023-06-01 10:20:05 ERROR Failed to load configuration file",
    "2023-06-01 10:22:30 INFO User login successful: admin456",
    "2023-06-01 10:25:15 WARNING High CPU usage detected",
    "2023-06-01 10:30:45 ERROR Permission denied for user: guest789",
    "2023-06-01 10:35:20 INFO Backup process started",
    "2023-06-01 10:40:30 INFO Backup process completed successfully"
]

# 提取日志级别
log_levels = []
for entry in log_entries:
    # 假设日志级别是行中的第三个元素
    parts = entry.split()
    if len(parts) >= 3:
        log_levels.append(parts[2])

# 统计日志级别
level_counts = Counter(log_levels)

print("日志级别统计:")
for level, count in level_counts.most_common():
    percentage = (count / len(log_entries)) * 100
    print(f"  {level}: {count}次 ({percentage:.1f}%)")

# 提取错误消息
error_messages = []
for entry in log_entries:
    if "ERROR" in entry:
        # 提取ERROR后面的消息
        error_msg = entry.split("ERROR", 1)[1].strip()
        error_messages.append(error_msg)

# 统计错误消息
if error_messages:
    error_counts = Counter(error_messages)
    print("\n错误消息统计:")
    for error, count in error_counts.most_common():
        print(f"  {error}: {count}次")

# 5. 性能分析

print("\n=== 5. 性能分析 ===")

print("\n5.1 时间复杂度")
print("Counter的主要操作时间复杂度如下:")
print("  - 创建Counter: O(n)，其中n是输入数据的大小")
print("  - 访问元素计数: O(1) 平均情况")
print("  - 更新计数: O(n)，其中n是被更新数据的大小")
print("  - most_common(): O(n log n)，其中n是Counter中元素的数量")
print("  - elements(): O(n)，其中n是所有元素计数的总和")
print("  - 数学运算 (+, -, &, |): O(n + m)，其中n和m是两个Counter的大小")

print("\n5.2 与手动计数的性能比较")
print("使用Counter进行计数通常比手动实现更高效，原因如下:")
print("  - Counter是用C实现的（在CPython中），运行速度更快")
print("  - Counter针对计数操作进行了优化")
print("  - 使用Counter可以减少代码量，提高可读性和可维护性")

print("\n5.3 内存使用")
print("Counter的内存使用情况:")
print("  - 存储键值对：与普通字典类似，存储每个元素及其计数")
print("  - 对于稀疏数据（大部分元素计数为0或1），Counter的内存效率较高")
print("  - 对于密集数据，可以考虑使用其他数据结构如数组来节省内存")

print("\n5.4 最佳实践性能建议")
print("为了获得最佳性能，使用Counter时应注意以下几点:")
print("  - 对于单次计数操作，直接使用Counter比手动实现更高效")
print("  - 对于频繁更新的场景，考虑使用update()方法而不是重新创建Counter")
print("  - 当只需要前N个最常见元素时，使用most_common(N)而不是获取所有元素后排序")
print("  - 对于非常大的数据集，可以考虑使用流式处理或分块处理来减少内存使用")

# 6. 使用注意事项

print("\n=== 6. 使用注意事项 ===")

print("\n6.1 关于零和负计数")
print("Counter允许元素计数为零或负数，但有些操作会忽略这些元素:")

# 创建包含零和负计数的Counter
c = Counter(a=2, b=0, c=-1)

print(f"\nCounter: {c}")
print(f"elements()方法结果（只包含正计数元素）: {list(c.elements())}")
print(f"数学运算结果（忽略非正计数元素）: {c + Counter()}")
print(f"检查键是否存在（包含零和负计数元素）: {'b' in c}, {'c' in c}")

print("\n6.2 访问不存在的元素")
print("与普通字典不同，访问Counter中不存在的元素不会抛出KeyError，而是返回0:")

c = Counter(a=1, b=2)
print(f"\nCounter: {c}")
print(f"访问存在的元素'a': {c['a']}")
print(f"访问不存在的元素'x': {c['x']}")  # 返回0，不抛出KeyError

# 但使用get()方法的行为与普通字典相同
print(f"使用get()访问'a': {c.get('a')}")
print(f"使用get()访问'x': {c.get('x')}")  # 返回None
print(f"使用get()访问'x'并提供默认值: {c.get('x', -1)}")  # 返回-1

print("\n6.3 元素顺序")
print("注意：在Python 3.7之前，Counter不保证元素的顺序；Python 3.7及以后，")
print("Counter会保留插入顺序，但most_common()方法会按计数排序:")

c = Counter()
c['z'] = 1
c['a'] = 2
c['m'] = 3

print(f"\nCounter（保留插入顺序）: {c}")
print(f"most_common()（按计数排序）: {c.most_common()}")

print("\n6.4 可哈希性要求")
print("Counter的键必须是可哈希的，与字典相同:")

try:
    # 尝试使用列表作为键（列表不可哈希）
    c = Counter()
    c[[1, 2]] = 3
except TypeError as e:
    print(f"\n错误: 键必须是可哈希的: {e}")

# 可以使用元组作为键（元组是可哈希的，只要其包含的所有元素都是可哈希的）
c = Counter()
c[(1, 2)] = 3
print(f"使用元组作为键: {c}")

print("\n6.5 与其他字典子类的交互")
print("Counter可以与其他字典子类交互，但要注意默认行为:")

from collections import defaultdict

# 创建defaultdict和Counter
dd = defaultdict(int, {'a': 1, 'b': 2})
c = Counter({'b': 3, 'c': 4})

# 转换为普通字典后合并
merged = dict(dd)
merged.update(c)
print(f"\ndefaultdict: {dict(dd)}")
print(f"Counter: {c}")
print(f"合并后的字典: {merged}")

# 使用Counter的update方法
c2 = Counter(dd)  # 从defaultdict创建Counter
c2.update(c)
print(f"使用Counter.update()合并: {c2}")

print("\n6.6 序列化注意事项")
print("序列化Counter时需要注意，与普通字典类似:")

import json

# 创建Counter
c = Counter(a=3, b=2, c=1)

# 序列化为JSON
json_str = json.dumps(c)
print(f"\nJSON序列化: {json_str}")

# 反序列化为普通字典
restored = json.loads(json_str)
print(f"反序列化结果: {restored}")
print(f"类型: {type(restored).__name__}")

# 需要手动恢复为Counter
restored_counter = Counter(restored)
print(f"恢复为Counter: {restored_counter}")
print(f"类型: {type(restored_counter).__name__}")

# 7. 综合示例：文本分析系统

print("\n=== 7. 综合示例：文本分析系统 ===")

print("\n实现一个使用Counter的文本分析系统，支持词频统计、关键词提取、文本相似度比较等功能:")

from collections import Counter
import re
import string
from typing import Dict, List, Tuple, Set

class TextAnalyzer:
    """
    文本分析系统
    使用Counter实现文本统计、关键词提取和文本比较等功能
    """
    
    def __init__(self, stop_words: Set[str] = None):
        """
        初始化文本分析器
        
        Args:
            stop_words: 停用词集合，这些词将被排除在分析之外
        """
        # 默认停用词列表（英语常用停用词）
        self.default_stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'if', 'because', 'as',
            'what', 'when', 'where', 'how', 'who', 'which', 'this', 'that',
            'these', 'those', 'then', 'just', 'so', 'than', 'such', 'both',
            'through', 'about', 'for', 'is', 'of', 'to', 'in', 'by', 'on',
            'at', 'from', 'with', 'about', 'against', 'between', 'into',
            'through', 'during', 'before', 'after', 'above', 'below', 'to',
            'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under',
            'again', 'further', 'then', 'once', 'here', 'there', 'all', 'any',
            'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such',
            'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
            'very', 'can', 'will', 'just', 'should', 'now', 'i', 'you', 'he',
            'she', 'it', 'we', 'they', 'them', 'their', 'what', 'which', 'who',
            'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was',
            'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having',
            'do', 'does', 'did', 'doing'
        }
        
        # 使用提供的停用词或默认停用词
        self.stop_words = stop_words if stop_words is not None else self.default_stop_words
        
        # 标点符号集合
        self.punctuation = set(string.punctuation)
    
    def tokenize(self, text: str) -> List[str]:
        """
        将文本分词并进行预处理
        
        Args:
            text: 输入文本
            
        Returns:
            处理后的单词列表
        """
        # 转换为小写
        text = text.lower()
        
        # 移除标点符号（替换为空格）
        translator = str.maketrans(self.punctuation, ' ' * len(self.punctuation))
        text = text.translate(translator)
        
        # 移除多余的空格并分割成单词
        words = re.findall(r'\b\w+\b', text)
        
        # 过滤停用词和单字符单词
        filtered_words = [word for word in words 
                         if word not in self.stop_words and len(word) > 1]
        
        return filtered_words
    
    def count_words(self, text: str) -> Counter:
        """
        统计文本中每个单词的出现次数
        
        Args:
            text: 输入文本
            
        Returns:
            单词计数Counter对象
        """
        words = self.tokenize(text)
        return Counter(words)
    
    def extract_keywords(self, text: str, n: int = 10, use_tfidf: bool = False, 
                        reference_texts: List[str] = None) -> List[Tuple[str, float]]:
        """
        从文本中提取关键词
        
        Args:
            text: 输入文本
            n: 返回的关键词数量
            use_tfidf: 是否使用TF-IDF算法
            reference_texts: 用于TF-IDF计算的参考文本列表
            
        Returns:
            关键词及其权重的列表（按权重降序排列）
        """
        # 简单的词频方法
        if not use_tfidf or not reference_texts:
            word_counts = self.count_words(text)
            # 归一化权重
            total_words = sum(word_counts.values())
            keywords = [(word, count / total_words) 
                        for word, count in word_counts.most_common(n)]
            return keywords
        
        # TF-IDF方法
        else:
            # 计算TF (Term Frequency)
            word_counts = self.count_words(text)
            total_words = sum(word_counts.values())
            tf = {word: count / total_words for word, count in word_counts.items()}
            
            # 计算IDF (Inverse Document Frequency)
            # 计算每个词在多少篇参考文档中出现
            doc_count = Counter()
            for ref_text in reference_texts:
                ref_words = set(self.tokenize(ref_text))
                doc_count.update(ref_words)
            
            # 总文档数
            total_docs = len(reference_texts)
            
            # 计算IDF，使用平滑处理避免除零
            import math
            idf = {word: math.log(total_docs / (count + 1)) + 1 
                  for word, count in doc_count.items()}
            
            # 计算TF-IDF
            tfidf = {word: tf[word] * idf.get(word, math.log(total_docs + 1)) 
                    for word in tf}
            
            # 排序并返回前n个关键词
            sorted_keywords = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)
            return sorted_keywords[:n]
    
    def calculate_similarity(self, text1: str, text2: str, method: str = 'cosine') -> float:
        """
        计算两个文本之间的相似度
        
        Args:
            text1: 第一个文本
            text2: 第二个文本
            method: 相似度计算方法，支持'cosine'（余弦相似度）或'jaccard'（杰卡德相似度）
            
        Returns:
            相似度分数（0.0到1.0之间）
        """
        # 计算词频
        c1 = self.count_words(text1)
        c2 = self.count_words(text2)
        
        if method == 'jaccard':
            # 杰卡德相似度：交集大小除以并集大小
            intersection = sum((c1 & c2).values())
            union = sum((c1 | c2).values())
            return intersection / union if union > 0 else 0.0
        
        elif method == 'cosine':
            # 余弦相似度：两个向量的点积除以它们的范数乘积
            # 计算点积
            dot_product = sum(c1[word] * c2.get(word, 0) for word in c1)
            
            # 计算范数
            norm1 = sum(count ** 2 for count in c1.values()) ** 0.5
            norm2 = sum(count ** 2 for count in c2.values()) ** 0.5
            
            # 计算余弦相似度
            return dot_product / (norm1 * norm2) if norm1 > 0 and norm2 > 0 else 0.0
        
        else:
            raise ValueError(f"不支持的相似度计算方法: {method}")
    
    def generate_text_summary(self, text: str, n_sentences: int = 3) -> str:
        """
        生成文本摘要（基于句子中关键词的重要性）
        
        Args:
            text: 输入文本
            n_sentences: 返回的句子数量
            
        Returns:
            文本摘要
        """
        # 分割句子（简单实现）
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        if len(sentences) <= n_sentences:
            return text
        
        # 计算整个文本的词频
        word_counts = self.count_words(text)
        
        # 计算每个句子的分数
        sentence_scores = []
        for i, sentence in enumerate(sentences):
            # 计算句子中单词的平均重要性
            words = self.tokenize(sentence)
            if words:  # 确保句子不为空
                score = sum(word_counts.get(word, 0) for word in words) / len(words)
                sentence_scores.append((i, score, sentence))
        
        # 排序并选择前n个句子
        sentence_scores.sort(key=lambda x: x[1], reverse=True)
        top_sentences = sorted(sentence_scores[:n_sentences], key=lambda x: x[0])
        
        # 合并句子
        summary = ' '.join(sentence for _, _, sentence in top_sentences)
        
        return summary
    
    def analyze_sentiment(self, text: str) -> Dict[str, float]:
        """
        简单的情感分析（基于关键词匹配）
        
        Args:
            text: 输入文本
            
        Returns:
            情感分析结果，包含积极、消极和中性的分数
        """
        # 简单的情感词典（实际应用中应使用更复杂的词典）
        positive_words = {
            'good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic',
            'terrific', 'outstanding', 'superb', 'awesome', 'best', 'better',
            'positive', 'beautiful', 'love', 'like', 'enjoy', 'happy', 'joy',
            'exciting', 'excited', 'pleased', 'satisfied', 'success', 'successful'
        }
        
        negative_words = {
            'bad', 'poor', 'terrible', 'horrible', 'awful', 'worst', 'worse',
            'negative', 'ugly', 'hate', 'dislike', 'disappoint', 'sad', 'sorrow',
            'angry', 'upset', 'frustrated', 'annoyed', 'failure', 'fail', 'error',
            'mistake', 'problem', 'issue', 'difficult', 'hard', 'trouble'
        }
        
        # 分词
        words = self.tokenize(text)
        
        # 统计积极和消极词汇
        word_counter = Counter(words)
        positive_count = sum(word_counter.get(word, 0) for word in positive_words)
        negative_count = sum(word_counter.get(word, 0) for word in negative_words)
        
        # 计算情感分数
        total = max(1, positive_count + negative_count)  # 避免除零
        positive_score = positive_count / total
        negative_score = negative_count / total
        neutral_score = 1.0 - positive_score - negative_score
        
        return {
            'positive': positive_score,
            'negative': negative_score,
            'neutral': neutral_score
        }
    
    def find_ngrams(self, text: str, n: int = 2) -> Counter:
        """
        查找文本中的n-gram（连续的n个单词）
        
        Args:
            text: 输入文本
            n: n-gram的大小
            
        Returns:
            n-gram计数Counter对象
        """
        words = self.tokenize(text)
        if len(words) < n:
            return Counter()
        
        # 生成n-gram
        ngrams = zip(*[words[i:] for i in range(n)])
        ngram_strings = [' '.join(gram) for gram in ngrams]
        
        return Counter(ngram_strings)
    
    def text_statistics(self, text: str) -> Dict[str, any]:
        """
        计算文本的基本统计信息
        
        Args:
            text: 输入文本
            
        Returns:
            文本统计信息
        """
        # 原始文本统计
        num_chars = len(text)
        num_chars_no_spaces = len(text.replace(' ', ''))
        num_lines = text.count('\n') + 1
        num_paragraphs = len(re.split(r'\n\s*\n', text.strip())) if text.strip() else 0
        
        # 单词统计
        words = self.tokenize(text)
        unique_words = set(words)
        num_words = len(words)
        num_unique_words = len(unique_words)
        
        # 句子统计
        sentences = re.split(r'(?<=[.!?])\s+', text)
        num_sentences = len(sentences)
        
        # 词汇丰富度
        lexical_diversity = num_unique_words / num_words if num_words > 0 else 0.0
        
        # 平均词长
        avg_word_length = sum(len(word) for word in words) / num_words if num_words > 0 else 0.0
        
        # 平均句子长度（以单词数计）
        if num_sentences > 0:
            words_all = re.findall(r'\b\w+\b', text.lower())
            avg_sentence_length = len(words_all) / num_sentences
        else:
            avg_sentence_length = 0.0
        
        # 最常见的单词
        word_counts = Counter(words)
        most_common_words = word_counts.most_common(5)
        
        return {
            '字符数': num_chars,
            '不含空格字符数': num_chars_no_spaces,
            '行数': num_lines,
            '段落数': num_paragraphs,
            '单词总数': num_words,
            '不同单词数': num_unique_words,
            '句子数': num_sentences,
            '词汇丰富度': lexical_diversity,
            '平均词长': avg_word_length,
            '平均句子长度': avg_sentence_length,
            '最常见单词': most_common_words
        }

# 演示文本分析系统
print("\n演示文本分析系统:")

# 创建文本分析器实例
analyzer = TextAnalyzer()

# 示例文本
text1 = """
Python is a high-level, interpreted, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation.
Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms,
including structured (particularly procedural), object-oriented and functional programming.
It is often described as a "batteries included" language due to its comprehensive standard library.
"""

text2 = """
Python is widely used in web development, data science, artificial intelligence, scientific computing,
and many other fields. Its simplicity and readability make it an excellent choice for beginners,
while its powerful libraries and frameworks make it suitable for advanced developers as well.
Python's community is large and active, providing extensive documentation and support.
"""

print("1. 词频统计:")
word_counts = analyzer.count_words(text1)
print(f"前10个最常见的单词:")
for word, count in word_counts.most_common(10):
    print(f"  '{word}': {count}")

print("\n2. 关键词提取:")
keywords = analyzer.extract_keywords(text1, n=5)
print(f"提取的关键词:")
for word, weight in keywords:
    print(f"  '{word}': {weight:.4f}")

print("\n3. 文本相似度计算:")
similarity = analyzer.calculate_similarity(text1, text2, method='cosine')
print(f"文本1和文本2的余弦相似度: {similarity:.4f}")

jaccard_similarity = analyzer.calculate_similarity(text1, text2, method='jaccard')
print(f"文本1和文本2的杰卡德相似度: {jaccard_similarity:.4f}")

print("\n4. 文本摘要生成:")
summary = analyzer.generate_text_summary(text1, n_sentences=2)
print("生成的摘要:")
print(summary)

print("\n5. 情感分析:")
text_with_sentiment = "I love Python programming! It's amazing and powerful. However, sometimes it can be slow for certain tasks."
sentiment = analyzer.analyze_sentiment(text_with_sentiment)
print(f"情感分析结果:")
print(f"  积极: {sentiment['positive']:.4f}")
print(f"  消极: {sentiment['negative']:.4f}")
print(f"  中性: {sentiment['neutral']:.4f}")

print("\n6. n-gram分析:")
ngrams = analyzer.find_ngrams(text1, n=2)
print(f"最常见的10个2-gram:")
for ngram, count in ngrams.most_common(10):
    print(f"  '{ngram}': {count}")

print("\n7. 文本统计信息:")
stats = analyzer.text_statistics(text1)
for key, value in stats.items():
    if key == '最常见单词':
        print(f"  {key}:")
        for word, count in value:
            print(f"    '{word}': {count}")
    else:
        print(f"  {key}: {value}")

# 8. 总结

print("\n=== 8. 总结 ===")

print("\ncollections.Counter是Python标准库中collections模块提供的一个专门用于计数的字典子类，")
print("它提供了丰富的方法来高效地统计、合并和操作元素计数。")

print("\n主要功能:")
print("1. 高效统计可哈希对象的出现频率")
print("2. 提供便捷的计数操作方法（update、subtract等）")
print("3. 支持元素计数的排序、合并和数学运算")
print("4. 提供查找最常见元素的功能（most_common方法）")
print("5. 可以与其他集合类型进行转换")

print("\n优势:")
print("1. 简化代码，减少手动计数的样板代码")
print("2. 提高代码可读性和可维护性")
print("3. 针对计数操作进行了优化，性能优异")
print("4. 与Python的数据处理生态系统无缝集成")
print("5. 支持丰富的计数操作和数学运算")

print("\n常见用例:")
print("1. 文本分析和词频统计")
print("2. 数据分析中的频率计算和分布分析")
print("3. 重复元素检测和去重")
print("4. 投票系统和多数元素查找")
print("5. 字符频率分析和简单加密破解")
print("6. 购物篮分析和关联规则挖掘")
print("7. 日志分析和事件统计")

print("\n使用建议:")
print("1. 在需要计数功能时，优先考虑使用Counter而不是手动实现")
print("2. 对于单次计数操作，直接使用Counter构造函数")
print("3. 对于频繁更新的场景，使用update()和subtract()方法")
print("4. 使用most_common()方法获取最常见的元素，这比手动排序更高效")
print("5. 注意Counter允许零和负计数，但某些操作会忽略这些元素")
print("6. 访问不存在的元素不会抛出KeyError，而是返回0")

print("\ncollections.Counter是Python标准库中一个强大而灵活的工具，")
print("它在数据分析、文本处理、算法实现等领域有着广泛的应用。无论是简单的计数任务还是复杂的数据分析，")
print("Counter都能提供简洁高效的解决方案，帮助开发者编写更优雅、更高效的代码。")
