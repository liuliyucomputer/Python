# collections.defaultdict模块 - Python标准库中的默认值字典

"""
collections.defaultdict是Python标准库中collections模块提供的一个字典子类，
它在普通字典的基础上添加了默认值机制。当访问一个不存在的键时，defaultdict会
自动创建该键并使用预定义的默认值，而不是抛出KeyError异常。

这在很多场景中非常有用，特别是当我们需要统计计数、分组或构建嵌套数据结构时，
可以避免大量的条件检查代码。
"""

# 1. 核心功能介绍

print("=== 1. 核心功能介绍 ===")
print("\ncollections.defaultdict模块提供了以下主要功能:")
print("1. 自动为不存在的键生成默认值，避免KeyError异常")
print("2. 支持所有标准字典操作（查找、插入、删除等）")
print("3. 可以使用各种可调用对象作为默认值工厂函数")
print("4. 在分组、计数和构建嵌套数据结构时特别有用")
print("5. 简化了需要初始化键的代码模式")

# 2. 基本操作

print("\n=== 2. 基本操作 ===")

# 导入defaultdict
from collections import defaultdict

print("\n2.1 创建defaultdict")
print("可以通过指定默认值工厂函数来创建defaultdict:")

# 使用int作为默认值工厂（默认值为0）
dd_int = defaultdict(int)
print(f"使用int作为默认值: {dd_int}")

# 使用list作为默认值工厂（默认值为[]）
dd_list = defaultdict(list)
print(f"使用list作为默认值: {dd_list}")

# 使用dict作为默认值工厂（默认值为{{}}）
dd_dict = defaultdict(dict)
print(f"使用dict作为默认值: {dd_dict}")

# 使用set作为默认值工厂（默认值为set()）
dd_set = defaultdict(set)
print(f"使用set作为默认值: {dd_set}")

# 使用自定义的默认值工厂函数
def default_value():
    return "默认值"

dd_custom = defaultdict(default_value)
print(f"使用自定义函数作为默认值: {dd_custom}")

# 使用lambda表达式作为默认值工厂
dd_lambda = defaultdict(lambda: "默认值")
print(f"使用lambda作为默认值: {dd_lambda}")

print("\n2.2 访问和修改元素")
print("defaultdict的一个主要特性是访问不存在的键时自动创建默认值:")

# 创建一个使用int作为默认值工厂的defaultdict
dd_int = defaultdict(int)
print(f"初始defaultdict: {dict(dd_int)}")

# 访问不存在的键
print(f"访问'count': {dd_int['count']}")
print(f"访问后defaultdict: {dict(dd_int)}")

# 增加计数
dd_int['count'] += 1
dd_int['count'] += 1
print(f"增加计数后: {dict(dd_int)}")

# 同时访问多个不存在的键
print(f"访问'another_count': {dd_int['another_count']}")
print(f"访问'third_count': {dd_int['third_count']}")
print(f"访问多个键后: {dict(dd_int)}")

print("\n2.3 使用列表作为默认值")
print("使用list作为默认值工厂非常适合构建分组数据:")

# 创建使用list作为默认值工厂的defaultdict
dd_list = defaultdict(list)

# 向不存在的键添加值
dd_list['fruits'].append('apple')
dd_list['fruits'].append('banana')
dd_list['vegetables'].append('carrot')
dd_list['vegetables'].append('broccoli')

print(f"分组结果: {dict(dd_list)}")
print(f"水果列表: {dd_list['fruits']}")
print(f"蔬菜列表: {dd_list['vegetables']}")

# 即使访问空列表也不会出错
print(f"空列表键: {dd_list['grains']}")
print(f"访问后defaultdict: {dict(dd_list)}")

print("\n2.4 使用集合作为默认值")
print("使用set作为默认值工厂可以自动去重:")

# 创建使用set作为默认值工厂的defaultdict
dd_set = defaultdict(set)

# 向不存在的键添加值
dd_set['colors'].add('red')
dd_set['colors'].add('blue')
dd_set['colors'].add('red')  # 重复值不会被添加
dd_set['shapes'].add('circle')
dd_set['shapes'].add('square')

print(f"去重结果: {dict(dd_set)}")
print(f"颜色集合: {dd_set['colors']}")
print(f"形状集合: {dd_set['shapes']}")

print("\n2.5 使用字典作为默认值")
print("使用dict作为默认值工厂可以轻松构建嵌套字典:")

# 创建使用dict作为默认值工厂的defaultdict
dd_dict = defaultdict(dict)

# 构建嵌套字典
dd_dict['user1']['name'] = 'Alice'
dd_dict['user1']['age'] = 30
dd_dict['user1']['city'] = 'New York'

dd_dict['user2']['name'] = 'Bob'
dd_dict['user2']['age'] = 25

print(f"嵌套字典: {dict(dd_dict)}")
print(f"用户1信息: {dd_dict['user1']}")
print(f"用户2信息: {dd_dict['user2']}")
print(f"用户2城市（不存在，将创建）: {dd_dict['user2'].get('city', 'N/A')}")

print("\n2.6 迭代和其他操作")
print("defaultdict支持所有标准字典的迭代和操作:")

# 创建defaultdict并添加一些数据
dd = defaultdict(int, {'a': 1, 'b': 2, 'c': 3})

# 迭代键
print("迭代键:")
for key in dd:
    print(f"  {key}")

# 迭代值
print("迭代值:")
for value in dd.values():
    print(f"  {value}")

# 迭代键值对
print("迭代键值对:")
for key, value in dd.items():
    print(f"  {key}: {value}")

# 检查键是否存在
print(f"'a'在defaultdict中: {'a' in dd}")
print(f"'d'在defaultdict中: {'d' in dd}")

# 获取所有键
print(f"所有键: {list(dd.keys())}")

# 获取所有值
print(f"所有值: {list(dd.values())}")

# 3. 高级用法

print("\n=== 3. 高级用法 ===")

print("\n3.1 自定义默认值工厂函数")
print("除了内置类型构造函数，还可以使用更复杂的自定义默认值工厂函数:")

# 使用生成递增ID的工厂函数
class IDGenerator:
    """简单的ID生成器类"""
    def __init__(self):
        self.id = 0
    
    def __call__(self):
        """使类实例可调用"""
        self.id += 1
        return self.id

# 创建ID生成器实例
id_gen = IDGenerator()

# 使用ID生成器作为默认值工厂
dd_id = defaultdict(id_gen)

# 每次访问不存在的键都会生成一个新的ID
print(f"访问'item1': {dd_id['item1']}")
print(f"访问'item2': {dd_id['item2']}")
print(f"访问'item3': {dd_id['item3']}")
print(f"defaultdict内容: {dict(dd_id)}")

print("\n3.2 使用defaultdict进行分组统计")
print("defaultdict非常适合对数据进行分组和统计:")

# 示例：按首字母分组单词
words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

# 使用defaultdict(list)按首字母分组
by_first_letter = defaultdict(list)
for word in words:
    by_first_letter[word[0]].append(word)

print("按首字母分组的单词:")
for letter, word_list in sorted(by_first_letter.items()):
    print(f"  {letter}: {word_list}")

# 示例：统计字符出现频率
text = "the quick brown fox jumps over the lazy dog"

# 使用defaultdict(int)统计字符频率
char_count = defaultdict(int)
for char in text:
    if char.isalpha():
        char_count[char.lower()] += 1

print("\n字符频率统计:")
for char, count in sorted(char_count.items()):
    print(f"  {char}: {count}")

print("\n3.3 构建嵌套的defaultdict")
print("可以创建多层嵌套的defaultdict来构建复杂的数据结构:")

# 示例：创建嵌套的defaultdict
def nested_dict():
    """创建一个默认值为dict的defaultdict"""
    return defaultdict(dict)

# 创建两级嵌套的defaultdict
two_level_nested = defaultdict(nested_dict)

# 填充数据
two_level_nested['users']['alice']['age'] = 30
two_level_nested['users']['alice']['city'] = 'New York'
two_level_nested['users']['bob']['age'] = 25
two_level_nested['users']['bob']['city'] = 'Boston'
two_level_nested['settings']['theme'] = 'dark'
two_level_nested['settings']['notifications'] = True

print("嵌套defaultdict结构:")
for category, items in two_level_nested.items():
    print(f"  {category}:")
    for key, value in items.items():
        print(f"    {key}: {value}")

# 示例：三级嵌套的defaultdict
def nested_list_dict():
    """创建一个默认值为list的defaultdict"""
    return defaultdict(list)

def three_level_nested_factory():
    """创建三级嵌套的defaultdict工厂"""
    return defaultdict(nested_list_dict)

# 创建三级嵌套的defaultdict
three_level_nested = defaultdict(three_level_nested_factory)

# 填充数据
three_level_nested['students']['math']['A'].append('Alice')
three_level_nested['students']['math']['B'].append('Bob')
three_level_nested['students']['math']['A'].append('Charlie')
three_level_nested['students']['english']['A'].append('Alice')
three_level_nested['students']['english']['C'].append('Bob')
three_level_nested['teachers']['math'].append('Mr. Smith')
three_level_nested['teachers']['english'].append('Ms. Johnson')

print("\n三级嵌套defaultdict结构:")
for level1, level2_items in three_level_nested.items():
    print(f"  {level1}:")
    for level2, level3_items in level2_items.items():
        print(f"    {level2}:")
        for level3, values in level3_items.items():
            print(f"      {level3}: {values}")

print("\n3.4 与其他集合类型的结合使用")
print("defaultdict可以与其他集合类型结合使用，实现更复杂的数据处理任务:")

# 示例：使用defaultdict和Counter结合进行词频统计
from collections import Counter

# 示例文本
documents = [
    "the quick brown fox jumps over the lazy dog",
    "python is a programming language",
    "the quick brown fox runs through the forest",
    "python programming is fun"
]

# 使用defaultdict(Counter)统计每个文档中的词频
document_word_counts = defaultdict(Counter)

for i, doc in enumerate(documents):
    words = doc.lower().split()
    document_word_counts[f"doc_{i+1}"] = Counter(words)

print("各文档词频统计:")
for doc_id, word_count in document_word_counts.items():
    print(f"  {doc_id}:")
    for word, count in sorted(word_count.items()):
        print(f"    {word}: {count}")

# 计算所有文档中单词的总出现次数
total_word_counts = Counter()
for word_count in document_word_counts.values():
    total_word_counts.update(word_count)

print("\n所有文档单词总出现次数:")
for word, count in total_word_counts.most_common(5):
    print(f"  {word}: {count}")

print("\n3.5 defaultdict的拷贝操作")
print("defaultdict支持复制操作，但需要注意默认值工厂函数的行为:")

# 创建一个defaultdict
dd1 = defaultdict(int)
dd1['a'] = 1
dd1['b'] = 2

# 使用copy()方法复制
dd2 = dd1.copy()
dd2['c'] = 3

print(f"原始defaultdict: {dict(dd1)}")
print(f"复制后的defaultdict: {dict(dd2)}")

# 检查复制后的defaultdict仍然保持默认值行为
print(f"访问dd2中不存在的键'd': {dd2['d']}")
print(f"复制后的defaultdict（访问后）: {dict(dd2)}")

# 使用dict构造函数创建普通字典
d3 = dict(dd1)
print(f"转换为普通字典: {d3}")

# 普通字典不再有默认值行为
try:
    print(d3['c'])
except KeyError:
    print("访问普通字典中不存在的键会抛出KeyError")

print("\n3.6 序列化defaultdict")
print("defaultdict可以被序列化，但在反序列化后需要手动恢复其默认值行为:")

import json

# 创建一个defaultdict
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
dd['vegetables'].append('carrot')

# 序列化为JSON
json_str = json.dumps(dd)
print(f"JSON序列化: {json_str}")

# 反序列化为普通字典
restored = json.loads(json_str)
print(f"反序列化结果（普通字典）: {restored}")
print(f"类型: {type(restored).__name__}")

# 手动恢复为defaultdict
restored_dd = defaultdict(list, restored)
print(f"恢复为defaultdict: {dict(restored_dd)}")
print(f"类型: {type(restored_dd).__name__}")

# 验证默认值行为
print(f"访问不存在的键'grains': {restored_dd['grains']}")

# 4. 实际应用场景

print("\n=== 4. 实际应用场景 ===")

print("\n4.1 词频统计")
print("defaultdict是进行文本词频统计的理想选择:")

print("\n示例: 使用defaultdict进行文本词频统计")

# 示例文本
text = """
Python is a programming language that lets you work more quickly and integrate your systems more effectively.
You can learn Python and see where it takes you.
Python is powerful and fast;
plays well with others;
runs everywhere;
is friendly & easy to learn;
is Open.
"""

# 使用defaultdict(int)统计词频
word_freq = defaultdict(int)

# 预处理文本并统计
for word in text.lower().split():
    # 移除标点符号
    word = ''.join(char for char in word if char.isalnum())
    if word:  # 避免空字符串
        word_freq[word] += 1

# 按频率排序并显示前10个单词
print("词频统计结果（前10个）:")
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
for word, freq in sorted_words[:10]:
    print(f"  {word}: {freq}")

print("\n4.2 分组数据处理")
print("在数据分析中，经常需要按某个属性对数据进行分组处理:")

print("\n示例: 按属性分组数据")

# 示例数据：学生信息
students = [
    {"name": "Alice", "age": 20, "major": "Computer Science", "GPA": 3.8},
    {"name": "Bob", "age": 21, "major": "Mathematics", "GPA": 3.5},
    {"name": "Charlie", "age": 19, "major": "Computer Science", "GPA": 4.0},
    {"name": "David", "age": 22, "major": "Physics", "GPA": 3.7},
    {"name": "Eve", "age": 20, "major": "Mathematics", "GPA": 3.9},
    {"name": "Frank", "age": 21, "major": "Computer Science", "GPA": 3.6},
    {"name": "Grace", "age": 19, "major": "Physics", "GPA": 3.8},
    {"name": "Henry", "age": 22, "major": "Mathematics", "GPA": 3.7}
]

# 按专业分组
by_major = defaultdict(list)
for student in students:
    by_major[student["major"]].append(student)

# 计算每个专业的平均GPA
major_gpa = defaultdict(float)
major_count = defaultdict(int)

for major, student_list in by_major.items():
    total_gpa = sum(student["GPA"] for student in student_list)
    count = len(student_list)
    major_gpa[major] = total_gpa / count
    major_count[major] = count

# 显示结果
print("按专业分组的统计信息:")
for major in sorted(by_major.keys()):
    print(f"  专业: {major}")
    print(f"    学生人数: {major_count[major]}")
    print(f"    平均GPA: {major_gpa[major]:.2f}")
    print(f"    学生列表: {[s['name'] for s in by_major[major]]}")
    print()

print("\n4.3 构建图数据结构")
print("在图论和网络分析中，defaultdict可以轻松构建图数据结构:")

print("\n示例: 使用defaultdict构建无向图")

class Graph:
    """
    简单的无向图实现
    """
    
    def __init__(self):
        """
        初始化图，使用defaultdict(list)存储邻接表
        """
        self.adj_list = defaultdict(list)
    
    def add_edge(self, u, v):
        """
        添加一条边（无向图，所以两个方向都添加）
        
        Args:
            u: 起始节点
            v: 终止节点
        """
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # 无向图的特点
    
    def add_node(self, node):
        """
        添加一个孤立节点
        
        Args:
            node: 节点
        """
        # 只需访问该节点，defaultdict会自动创建空列表
        _ = self.adj_list[node]
    
    def get_neighbors(self, node):
        """
        获取节点的所有邻居
        
        Args:
            node: 节点
        
        Returns:
            邻居节点列表
        """
        return self.adj_list[node]
    
    def get_nodes(self):
        """
        获取图中所有节点
        
        Returns:
            节点集合
        """
        return list(self.adj_list.keys())
    
    def __str__(self):
        """
        返回图的字符串表示
        """
        result = []
        for node, neighbors in self.adj_list.items():
            result.append(f"{node}: {neighbors}")
        return "\n".join(result)

# 创建一个简单的社交网络图
social_graph = Graph()

# 添加边（表示好友关系）
social_graph.add_edge("Alice", "Bob")
social_graph.add_edge("Alice", "Charlie")
social_graph.add_edge("Bob", "David")
social_graph.add_edge("Charlie", "David")
social_graph.add_edge("Charlie", "Eve")
social_graph.add_edge("David", "Eve")

# 显示图
print("社交网络图:")
print(social_graph)

# 查找特定人的朋友
print(f"\nAlice的朋友: {social_graph.get_neighbors('Alice')}")
print(f"David的朋友: {social_graph.get_neighbors('David')}")
print(f"所有节点: {social_graph.get_nodes()}")

print("\n4.4 文件系统路径统计")
print("defaultdict可以用于分析文件系统中的文件类型分布:")

print("\n示例: 文件类型统计")

import os
from collections import defaultdict

# 模拟文件路径列表（实际应用中可以使用os.walk遍历目录）
file_paths = [
    "/home/user/documents/report.pdf",
    "/home/user/documents/notes.txt",
    "/home/user/downloads/image.jpg",
    "/home/user/downloads/data.csv",
    "/home/user/downloads/archive.zip",
    "/home/user/projects/project1/main.py",
    "/home/user/projects/project1/utils.py",
    "/home/user/projects/project1/README.md",
    "/home/user/projects/project2/app.js",
    "/home/user/projects/project2/styles.css",
    "/home/user/projects/project2/index.html"
]

# 统计文件类型分布
file_type_count = defaultdict(int)
for file_path in file_paths:
    # 获取文件扩展名
    _, ext = os.path.splitext(file_path)
    # 移除扩展名前面的点，如果没有扩展名则为'无扩展名'
    ext = ext[1:] if ext else '无扩展名'
    file_type_count[ext] += 1

# 按文件类型统计目录分布
dir_by_file_type = defaultdict(set)
for file_path in file_paths:
    _, ext = os.path.splitext(file_path)
    ext = ext[1:] if ext else '无扩展名'
    # 获取目录路径
    dir_path = os.path.dirname(file_path)
    dir_by_file_type[ext].add(dir_path)

# 显示结果
print("文件类型统计:")
for ext, count in sorted(file_type_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {ext}: {count} 个文件")
    print(f"    出现在目录: {', '.join(sorted(dir_by_file_type[ext]))}")

print("\n4.5 日志分析")
print("defaultdict可以用于分析日志文件，统计不同级别的日志数量或错误类型:")

print("\n示例: 日志分析")

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

# 统计日志级别
log_levels = defaultdict(int)

# 统计错误信息
error_messages = defaultdict(int)

# 分析日志
for log in log_entries:
    # 提取日志级别（假设格式是固定的，日志级别在时间之后）
    parts = log.split()
    if len(parts) >= 3:
        level = parts[2]
        log_levels[level] += 1
        
        # 如果是错误日志，统计错误消息
        if level == "ERROR":
            error_msg = ' '.join(parts[3:])
            error_messages[error_msg] += 1

# 显示结果
print("日志级别统计:")
for level, count in sorted(log_levels.items()):
    print(f"  {level}: {count}")

print("\n错误消息统计:")
for error, count in error_messages.items():
    print(f"  {error}: {count}")

print("\n4.6 缓存实现")
print("defaultdict可以用于实现简单的缓存系统:")

print("\n示例: 简单的计算缓存")

from functools import wraps

# 创建一个缓存字典
cache = defaultdict(dict)

def memoize(func):
    """
    一个简单的缓存装饰器
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 创建缓存键
        key = (args, frozenset(kwargs.items()))
        
        # 检查缓存中是否已有结果
        if key not in cache[func.__name__]:
            # 如果没有，计算并缓存结果
            result = func(*args, **kwargs)
            cache[func.__name__][key] = result
        
        # 返回缓存的结果
        return cache[func.__name__][key]
    
    return wrapper

# 使用装饰器缓存计算结果
@memoize
def fibonacci(n):
    """
    计算斐波那契数列的第n个数（递归实现，仅用于演示缓存效果）
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 计算斐波那契数
print("计算斐波那契数列:")
for i in range(10):
    print(f"  fibonacci({i}) = {fibonacci(i)}")

# 显示缓存内容
print("\n缓存内容:")
print(f"fibonacci函数的缓存项数量: {len(cache['fibonacci'])}")
print("缓存项示例:")
count = 0
for key, value in cache['fibonacci'].items():
    if count < 3:  # 只显示前3个
        print(f"  {key}: {value}")
        count += 1

# 重新计算相同的值，应该使用缓存
print("\n再次计算相同的值（使用缓存）:")
for i in range(10):
    print(f"  fibonacci({i}) = {fibonacci(i)}")

print(f"\n缓存项数量（应该不变）: {len(cache['fibonacci'])}")

# 5. 性能分析

print("\n=== 5. 性能分析 ===")

print("\n5.1 时间复杂度")
print("defaultdict的主要操作时间复杂度与普通字典相同:")
print("  - 查找操作(get, []): O(1) 平均情况")
print("  - 插入操作(setitem): O(1) 平均情况")
print("  - 删除操作(del, pop): O(1) 平均情况")
print("  - 检查键是否存在(in 操作符): O(1) 平均情况")

print("\n5.2 与普通字典的性能比较")
print("与普通字典相比，defaultdict在以下方面可能有轻微的性能差异:")
print("  - 初始化: defaultdict需要存储默认值工厂函数，所以初始化可能略慢")
print("  - 访问不存在的键: defaultdict会自动创建默认值，这比普通字典抛出异常要慢，但避免了异常处理的开销")
print("  - 内存使用: defaultdict通常比普通字典使用略多的内存")
print("  - 正常操作: 在正常使用（访问已存在的键）时，性能与普通字典几乎相同")

print("\n5.3 最佳实践性能建议")
print("为了获得最佳性能，使用defaultdict时应注意以下几点:")
print("  - 选择合适的默认值工厂函数，尽量使用轻量级的函数（如内置类型构造函数）")
print("  - 避免在默认值工厂中执行复杂的计算")
print("  - 在不需要默认值功能的场景中，使用普通字典可能更高效")
print("  - 对于大量数据，考虑在使用defaultdict后转换为普通字典（dict(dd)）以节省内存")

# 6. 使用注意事项

print("\n=== 6. 使用注意事项 ===")

print("\n6.1 默认值工厂函数")
print("使用defaultdict时，需要注意默认值工厂函数的行为:")

# 示例：使用可变对象作为默认值
print("\n错误示例: 使用可变对象作为默认值工厂的返回值")

# 错误的做法 - 使用可变对象作为默认值工厂
# 这个例子中，所有不存在的键都会共享同一个列表实例
def get_default_list():
    return []  # 每次调用都返回新列表，这是正确的

# 正确的方式
dd_correct = defaultdict(get_default_list)
dd_correct['a'].append(1)
dd_correct['b'].append(2)
print(f"正确使用可变对象: {dict(dd_correct)}")

# 警告：默认值工厂函数不能有参数
try:
    # 这会导致错误，因为int()接受参数
    dd_error = defaultdict(lambda: int(10))
except TypeError as e:
    print(f"\n错误: 默认值工厂函数不能有参数: {e}")

print("\n6.2 避免不必要的键创建")
print("使用defaultdict时，访问不存在的键会自动创建该键，这可能导致意外的内存使用:")

# 示例：意外创建键
print("\n示例: 意外创建键")

dd = defaultdict(int)
print(f"初始defaultdict: {dict(dd)}")

# 检查键是否存在
print(f"'count' in dd: {'count' in dd}")
print(f"检查后defaultdict: {dict(dd)}")  # 'count' 不存在

# 访问不存在的键
value = dd['count']  # 自动创建'count'键
print(f"访问'count'后defaultdict: {dict(dd)}")  # 'count' 现在存在

# 使用get方法不会创建键
value = dd.get('another_count')
print(f"使用get访问后defaultdict: {dict(dd)}")  # 'another_count' 仍然不存在

print("\n6.3 序列化注意事项")
print("序列化defaultdict时需要注意，标准的序列化方法（如JSON）会丢失其默认值行为:")

# 示例：JSON序列化
import json

dd = defaultdict(list)
dd['fruits'].append('apple')
dd['vegetables'].append('carrot')

json_str = json.dumps(dd)
print(f"\nJSON序列化: {json_str}")

# 反序列化后是普通字典
restored = json.loads(json_str)
print(f"反序列化结果类型: {type(restored).__name__}")

# 需要手动恢复默认值行为
restored_dd = defaultdict(list, restored)
print(f"恢复为defaultdict: {dict(restored_dd)}")

print("\n6.4 与pickle模块一起使用")
print("当使用pickle模块序列化defaultdict时，需要确保默认值工厂函数是可pickle的:")

# 示例：pickle序列化
import pickle

try:
    # 自定义函数
    def my_factory():
        return "default"
    
    dd = defaultdict(my_factory)
    dd['key'] = 'value'
    
    # 序列化
    pickled = pickle.dumps(dd)
    # 反序列化
    unpickled = pickle.loads(pickled)
    
    print(f"\npickle序列化后: {dict(unpickled)}")
    print(f"默认值行为: {unpickled['new_key']}")
    
    # 注意：lambda函数通常不可pickle
    dd_lambda = defaultdict(lambda: "lambda default")
    try:
        pickle.dumps(dd_lambda)
    except Exception as e:
        print(f"\n错误: lambda函数通常不可pickle: {type(e).__name__}")
        
except Exception as e:
    print(f"\n序列化错误: {e}")

print("\n6.5 比较操作")
print("defaultdict的比较操作与普通字典相同，不考虑默认值工厂函数:")

# 示例：比较defaultdict和普通字典
dd = defaultdict(int, {'a': 1, 'b': 2})
d = {'a': 1, 'b': 2}

print(f"\ndefaultdict: {dict(dd)}")
print(f"普通字典: {d}")
print(f"比较结果: {dd == d}")  # 应该是True

# 不同的默认值工厂但相同的内容也会被认为是相等的
dd1 = defaultdict(int, {'a': 1})
dd2 = defaultdict(list, {'a': 1})
print(f"\ndd1默认值工厂: int, 内容: {dict(dd1)}")
print(f"dd2默认值工厂: list, 内容: {dict(dd2)}")
print(f"比较结果: {dd1 == dd2}")  # 应该是True

# 7. 综合示例：电商购物车系统

print("\n=== 7. 综合示例：电商购物车系统 ===")

print("\n实现一个使用defaultdict的电商购物车系统，支持商品添加、删除、更新数量、计算总价等功能:")

from collections import defaultdict
from datetime import datetime

class ShoppingCart:
    """
    电商购物车系统
    使用defaultdict实现商品管理、分类统计和价格计算
    """
    
    def __init__(self):
        """
        初始化购物车
        """
        # 使用defaultdict(int)存储商品及数量
        self.items = defaultdict(int)
        
        # 使用defaultdict(float)存储商品价格
        self.prices = defaultdict(float)
        
        # 使用defaultdict(str)存储商品名称
        self.names = defaultdict(str)
        
        # 使用defaultdict(list)按类别存储商品
        self.by_category = defaultdict(list)
        
        # 使用defaultdict(float)存储类别折扣
        self.category_discounts = defaultdict(float)
        
        # 购物车创建时间
        self.created_at = datetime.now()
        
        # 购物车最后更新时间
        self.updated_at = datetime.now()
    
    def add_item(self, item_id, name, price, quantity=1, category="general"):
        """
        添加商品到购物车
        
        Args:
            item_id: 商品ID
            name: 商品名称
            price: 商品价格
            quantity: 数量
            category: 商品类别
        """
        # 更新商品数量
        self.items[item_id] += quantity
        
        # 存储商品信息
        self.prices[item_id] = price
        self.names[item_id] = name
        
        # 如果商品还没有分配到类别，添加到类别列表
        if item_id not in self.by_category[category]:
            self.by_category[category].append(item_id)
        
        # 更新最后修改时间
        self.updated_at = datetime.now()
        
        return self.items[item_id]  # 返回更新后的数量
    
    def remove_item(self, item_id):
        """
        从购物车中移除商品
        
        Args:
            item_id: 商品ID
        
        Returns:
            True如果成功移除，False如果商品不在购物车中
        """
        if item_id in self.items:
            # 获取商品类别
            category = self._get_item_category(item_id)
            
            # 从类别列表中移除
            if category and item_id in self.by_category[category]:
                self.by_category[category].remove(item_id)
            
            # 删除商品信息
            del self.items[item_id]
            
            # 注意：我们保留价格和名称信息，以便将来可能的重新添加
            # 如果需要完全清理，可以取消下面两行的注释
            # del self.prices[item_id]
            # del self.names[item_id]
            
            # 更新最后修改时间
            self.updated_at = datetime.now()
            
            return True
        return False
    
    def update_quantity(self, item_id, quantity):
        """
        更新商品数量
        
        Args:
            item_id: 商品ID
            quantity: 新数量
        
        Returns:
            更新后的数量，如果商品不在购物车中返回None
        """
        if item_id in self.items:
            # 确保数量是正数
            if quantity <= 0:
                return self.remove_item(item_id)
            
            # 更新数量
            self.items[item_id] = quantity
            
            # 更新最后修改时间
            self.updated_at = datetime.now()
            
            return quantity
        return None
    
    def increase_quantity(self, item_id, amount=1):
        """
        增加商品数量
        
        Args:
            item_id: 商品ID
            amount: 增加的数量
        
        Returns:
            更新后的数量，如果商品不在购物车中返回None
        """
        if item_id in self.items:
            self.items[item_id] += amount
            
            # 更新最后修改时间
            self.updated_at = datetime.now()
            
            return self.items[item_id]
        return None
    
    def decrease_quantity(self, item_id, amount=1):
        """
        减少商品数量
        
        Args:
            item_id: 商品ID
            amount: 减少的数量
        
        Returns:
            更新后的数量，如果商品不在购物车中返回None，
            如果数量减至0或以下则移除商品并返回0
        """
        if item_id in self.items:
            self.items[item_id] -= amount
            
            # 如果数量小于等于0，移除商品
            if self.items[item_id] <= 0:
                self.remove_item(item_id)
                return 0
            
            # 更新最后修改时间
            self.updated_at = datetime.now()
            
            return self.items[item_id]
        return None
    
    def set_category_discount(self, category, discount):
        """
        设置类别折扣
        
        Args:
            category: 商品类别
            discount: 折扣比例（0.0到1.0之间）
        """
        # 确保折扣在有效范围内
        if 0.0 <= discount <= 1.0:
            self.category_discounts[category] = discount
            return True
        return False
    
    def calculate_subtotal(self):
        """
        计算购物车商品总价（不含折扣）
        
        Returns:
            商品总价
        """
        subtotal = 0.0
        for item_id, quantity in self.items.items():
            subtotal += self.prices[item_id] * quantity
        return subtotal
    
    def calculate_discount(self):
        """
        计算总折扣金额
        
        Returns:
            折扣金额
        """
        discount = 0.0
        for category, discount_rate in self.category_discounts.items():
            if discount_rate > 0:
                # 计算该类别的商品总价
                category_total = 0.0
                for item_id in self.by_category[category]:
                    if item_id in self.items:
                        category_total += self.prices[item_id] * self.items[item_id]
                
                # 计算该类别的折扣
                category_discount = category_total * discount_rate
                discount += category_discount
        return discount
    
    def calculate_total(self):
        """
        计算购物车最终总价（含折扣）
        
        Returns:
            最终总价
        """
        return max(0.0, self.calculate_subtotal() - self.calculate_discount())
    
    def get_items_by_category(self, category):
        """
        获取指定类别的所有商品
        
        Args:
            category: 商品类别
        
        Returns:
            商品列表
        """
        items = []
        for item_id in self.by_category[category]:
            if item_id in self.items:
                items.append({
                    'id': item_id,
                    'name': self.names[item_id],
                    'price': self.prices[item_id],
                    'quantity': self.items[item_id]
                })
        return items
    
    def get_category_summary(self):
        """
        获取每个类别的汇总信息
        
        Returns:
            类别汇总信息字典
        """
        summary = defaultdict(lambda: {'items': 0, 'quantity': 0, 'subtotal': 0.0, 'discount': 0.0, 'total': 0.0})
        
        # 计算每个类别的商品数量、总数量和总价
        for category, item_ids in self.by_category.items():
            for item_id in item_ids:
                if item_id in self.items:
                    price = self.prices[item_id]
                    quantity = self.items[item_id]
                    item_total = price * quantity
                    
                    summary[category]['items'] += 1
                    summary[category]['quantity'] += quantity
                    summary[category]['subtotal'] += item_total
        
        # 计算折扣和最终总价
        for category, info in summary.items():
            discount_rate = self.category_discounts.get(category, 0.0)
            info['discount'] = info['subtotal'] * discount_rate
            info['total'] = max(0.0, info['subtotal'] - info['discount'])
        
        return dict(summary)
    
    def is_empty(self):
        """
        检查购物车是否为空
        
        Returns:
            True如果购物车为空，否则False
        """
        return len(self.items) == 0
    
    def clear(self):
        """
        清空购物车
        """
        self.items.clear()
        # 保留价格、名称和类别映射信息，以便将来可能的重新添加
        # 如果需要完全清理，可以取消下面三行的注释
        # self.prices.clear()
        # self.names.clear()
        # self.by_category.clear()
        
        # 更新最后修改时间
        self.updated_at = datetime.now()
    
    def _get_item_category(self, item_id):
        """
        获取商品所属的类别
        
        Args:
            item_id: 商品ID
        
        Returns:
            商品类别，如果找不到返回None
        """
        for category, items in self.by_category.items():
            if item_id in items:
                return category
        return None
    
    def __str__(self):
        """
        返回购物车的字符串表示
        """
        lines = []
        lines.append("购物车内容:")
        
        if self.is_empty():
            lines.append("  购物车为空")
        else:
            # 按类别显示商品
            category_summary = self.get_category_summary()
            
            for category in sorted(self.by_category.keys()):
                if category in category_summary and category_summary[category]['items'] > 0:
                    lines.append(f"\n  类别: {category}")
                    lines.append(f"  {'-' * 60}")
                    lines.append(f"  {'商品名称':<20} {'单价':>10} {'数量':>8} {'小计':>12}")
                    lines.append(f"  {'-' * 60}")
                    
                    # 显示该类别的所有商品
                    for item_id in self.by_category[category]:
                        if item_id in self.items:
                            name = self.names[item_id]
                            price = self.prices[item_id]
                            quantity = self.items[item_id]
                            subtotal = price * quantity
                            lines.append(f"  {name:<20} {price:>10.2f} {quantity:>8} {subtotal:>12.2f}")
                    
                    # 显示类别汇总
                    cat_info = category_summary[category]
                    discount_rate = self.category_discounts.get(category, 0.0)
                    if discount_rate > 0:
                        lines.append(f"  {'-' * 60}")
                        lines.append(f"  {'类别小计':<20} {'':>10} {'':>8} {cat_info['subtotal']:>12.2f}")
                        lines.append(f"  {f'类别折扣 ({discount_rate*100:.0f}%)':<20} {'':>10} {'':>8} {-cat_info['discount']:>12.2f}")
                        lines.append(f"  {f'类别总价':<20} {'':>10} {'':>8} {cat_info['total']:>12.2f}")
            
            # 显示总计
            lines.append(f"\n  {'-' * 60}")
            lines.append(f"  {'购物车小计':<20} {'':>10} {'':>8} {self.calculate_subtotal():>12.2f}")
            
            total_discount = self.calculate_discount()
            if total_discount > 0:
                lines.append(f"  {'总折扣':<20} {'':>10} {'':>8} {-total_discount:>12.2f}")
                
            lines.append(f"  {'-' * 60}")
            lines.append(f"  {'应付总额':<20} {'':>10} {'':>8} {self.calculate_total():>12.2f}")
            
            # 显示其他信息
            lines.append(f"\n  商品种类数: {len(self.items)}")
            lines.append(f"  商品总数量: {sum(self.items.values())}")
            lines.append(f"  创建时间: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
            lines.append(f"  更新时间: {self.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
        
        return "\n".join(lines)

# 演示购物车系统
print("\n演示电商购物车系统:")

# 创建购物车
cart = ShoppingCart()
print("空购物车:")
print(cart)

# 添加商品
print("\n添加商品:")
cart.add_item("p001", "智能手机", 5999.00, 1, "electronics")
cart.add_item("p002", "笔记本电脑", 6999.00, 1, "electronics")
cart.add_item("p003", "蓝牙耳机", 899.00, 2, "electronics")
cart.add_item("p004", "T恤衫", 99.00, 3, "clothing")
cart.add_item("p005", "牛仔裤", 299.00, 1, "clothing")
cart.add_item("p006", "运动鞋", 499.00, 1, "clothing")
cart.add_item("p007", "咖啡杯", 49.00, 2, "household")

print("\n购物车内容:")
print(cart)

# 更新商品数量
print("\n更新商品数量:")
cart.update_quantity("p002", 2)
cart.decrease_quantity("p004", 1)
cart.increase_quantity("p003", 1)

print("\n更新后的购物车:")
print(cart)

# 设置类别折扣
print("\n设置类别折扣:")
cart.set_category_discount("electronics", 0.1)  # 电子产品9折
cart.set_category_discount("clothing", 0.15)  # 服装85折

print("\n应用折扣后的购物车:")
print(cart)

# 按类别查看商品
print("\n按类别查看商品:")
electronics_items = cart.get_items_by_category("electronics")
print("电子产品:")
for item in electronics_items:
    print(f"  {item['name']}: ¥{item['price']:.2f} x {item['quantity']}")

# 获取类别汇总
print("\n类别汇总:")
category_summary = cart.get_category_summary()
for category, info in category_summary.items():
    print(f"  {category}:")
    print(f"    商品种类: {info['items']}")
    print(f"    总数量: {info['quantity']}")
    print(f"    小计: ¥{info['subtotal']:.2f}")
    print(f"    折扣: ¥{info['discount']:.2f}")
    print(f"    总计: ¥{info['total']:.2f}")

# 移除商品
print("\n移除商品:")
cart.remove_item("p002")

print("\n移除后的购物车:")
print(cart)

# 清空购物车
print("\n清空购物车:")
cart.clear()

print("\n清空后的购物车:")
print(cart)

# 8. 总结

print("\n=== 8. 总结 ===")

print("\ncollections.defaultdict是Python标准库中collections模块提供的一个字典子类，")
print("它通过提供默认值机制，大大简化了许多常见的数据处理任务。")

print("\n主要功能:")
print("1. 自动为不存在的键生成默认值，避免KeyError异常")
print("2. 支持各种可调用对象作为默认值工厂函数")
print("3. 保持与普通字典完全兼容的接口")
print("4. 特别适合用于分组、计数和构建嵌套数据结构")

print("\n优势:")
print("1. 简化代码，减少条件检查和异常处理")
print("2. 提高代码可读性和可维护性")
print("3. 在需要为不存在的键提供默认值的场景中非常高效")
print("4. 与Python的数据处理生态系统无缝集成")

print("\n常见用例:")
print("1. 词频统计和文本分析")
print("2. 数据分组和分类统计")
print("3. 构建图和树等复杂数据结构")
print("4. 缓存实现和记忆化计算")
print("5. 日志分析和错误计数")
print("6. 购物车和订单系统等电商应用")

print("\n使用建议:")
print("1. 选择合适的默认值工厂函数，根据需要选择int、list、dict、set等")
print("2. 对于复杂的默认值，使用自定义的可调用对象或工厂函数")
print("3. 注意避免意外创建不需要的键，必要时使用get()方法")
print("4. 序列化时需要特殊处理，以保持默认值行为")
print("5. 在不需要默认值功能的场景中，普通字典可能是更好的选择")

print("\ncollections.defaultdict是Python标准库中一个强大而灵活的工具，")
print("它在简化代码的同时，提供了良好的性能和可维护性。无论是在简单的脚本还是复杂的应用程序中，")
print("defaultdict都能在各种数据处理场景中发挥重要作用，特别是在需要处理和组织大量数据时。")
