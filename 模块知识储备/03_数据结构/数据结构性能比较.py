# Python数据结构性能比较

"""
本文件对Python中常用数据结构的性能特点进行详细比较，帮助开发者在实际应用中选择最合适的数据结构。
不同的数据结构在不同操作上有各自的优势和劣势，了解这些性能差异对于编写高效的Python代码至关重要。

主要比较的内容包括：
- 各种数据结构的时间复杂度
- 内存占用情况
- 适用场景分析
- 实际性能测试
- 选择建议
"""

import time
import random
import sys
from collections import deque, defaultdict, Counter, namedtuple

# 1. 常见数据结构的时间复杂度表

print("=== 常见数据结构的时间复杂度比较 ===")

"""
数据结构操作的时间复杂度（平均情况，除非特别说明）：

操作\数据结构 | 列表(list) | 字典(dict) | 集合(set) | 双端队列(deque) | 堆(heapq)
------------|-----------|-----------|----------|---------------|--------
索引访问     | O(1)      | O(1)      | N/A      | O(1)          | O(n)
添加元素     | O(1)      | O(1)      | O(1)     | O(1)          | O(log n)
删除元素     | O(n)      | O(1)      | O(1)     | O(1)          | O(log n)
查找元素     | O(n)      | O(1)      | O(1)     | O(n)          | O(n)
修改元素     | O(1)      | O(1)      | N/A      | O(1)          | O(log n)
排序         | O(n log n)| N/A       | N/A      | O(n log n)    | O(n log n)
获取最大/最小| O(n)      | O(n)      | O(n)     | O(n)          | O(1)
"""

# 格式化输出时间复杂度比较表
print("操作\数据结构 | 列表(list) | 字典(dict) | 集合(set) | 双端队列(deque) | 堆(heapq)")
print("------------|-----------|-----------|----------|---------------|--------")
print("索引访问     | O(1)      | O(1)      | N/A      | O(1)          | O(n)")
print("添加元素     | O(1)      | O(1)      | O(1)     | O(1)          | O(log n)")
print("删除元素     | O(n)      | O(1)      | O(1)     | O(1)          | O(log n)")
print("查找元素     | O(n)      | O(1)      | O(1)     | O(n)          | O(n)")
print("修改元素     | O(1)      | O(1)      | N/A      | O(1)          | O(log n)")
print("排序         | O(n log n)| N/A       | N/A      | O(n log n)    | O(n log n)")
print("获取最大/最小| O(n)      | O(n)      | O(n)     | O(n)          | O(1)")

# 2. 内存占用比较

print("\n=== 内存占用比较 ===")

# 定义不同大小的测试数据
sizes = [100, 1000, 10000]

for size in sizes:
    print(f"\n数据大小: {size} 个元素")
    
    # 创建相同内容的不同数据结构
    data = list(range(size))
    
    # 列表
    list_obj = list(data)
    list_memory = sys.getsizeof(list_obj)
    print(f"列表 (list): {list_memory} 字节")
    
    # 字典（键值对形式）
    dict_obj = {i: i for i in data}
    dict_memory = sys.getsizeof(dict_obj)
    print(f"字典 (dict): {dict_memory} 字节 ({dict_memory/list_memory:.2f}x 列表大小)")
    
    # 集合
    set_obj = set(data)
    set_memory = sys.getsizeof(set_obj)
    print(f"集合 (set): {set_memory} 字节 ({set_memory/list_memory:.2f}x 列表大小)")
    
    # 双端队列
    deque_obj = deque(data)
    deque_memory = sys.getsizeof(deque_obj)
    print(f"双端队列 (deque): {deque_memory} 字节 ({deque_memory/list_memory:.2f}x 列表大小)")
    
    # array模块的数组（如果数据是同类型的）
    try:
        import array
        array_obj = array.array('i', data)
        array_memory = sys.getsizeof(array_obj)
        print(f"数组 (array): {array_memory} 字节 ({array_memory/list_memory:.2f}x 列表大小)")
    except ImportError:
        pass
    
    # 清理内存
    del list_obj, dict_obj, set_obj, deque_obj
    if 'array_obj' in locals():
        del array_obj

# 3. 基本操作性能测试

print("\n=== 基本操作性能测试 ===")

def test_performance(operation_name, func, *args, **kwargs):
    """测试函数执行时间"""
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time, result

# 定义不同的测试大小
test_sizes = [1000, 10000, 100000]

# 3.1 添加元素性能测试
print("\n3.1 添加元素性能测试")

for size in test_sizes:
    print(f"\n添加 {size} 个元素:")
    
    # 列表 append
    lst = []
    time_taken, _ = test_performance("列表 append", 
                                   lambda: [lst.append(i) for i in range(size)])
    print(f"列表 append: {time_taken:.6f} 秒")
    
    # 字典添加
    d = {}
    time_taken, _ = test_performance("字典添加", 
                                   lambda: [d.update({i: i}) for i in range(size)])
    print(f"字典添加: {time_taken:.6f} 秒")
    
    # 集合添加
    s = set()
    time_taken, _ = test_performance("集合添加", 
                                   lambda: [s.add(i) for i in range(size)])
    print(f"集合添加: {time_taken:.6f} 秒")
    
    # 双端队列 append
    dq = deque()
    time_taken, _ = test_performance("双端队列 append", 
                                   lambda: [dq.append(i) for i in range(size)])
    print(f"双端队列 append: {time_taken:.6f} 秒")
    
    # 双端队列 appendleft
    dq = deque()
    time_taken, _ = test_performance("双端队列 appendleft", 
                                   lambda: [dq.appendleft(i) for i in range(size)])
    print(f"双端队列 appendleft: {time_taken:.6f} 秒")
    
    # heapq.heappush
    import heapq
    h = []
    time_taken, _ = test_performance("堆添加", 
                                   lambda: [heapq.heappush(h, i) for i in range(size)])
    print(f"堆添加: {time_taken:.6f} 秒")

# 3.2 查找元素性能测试
print("\n3.2 查找元素性能测试")

for size in test_sizes:
    print(f"\n在 {size} 个元素中查找:")
    
    # 创建测试数据
    data = list(range(size))
    random.shuffle(data)
    
    lst = data.copy()
    d = {i: i for i in data}
    s = set(data)
    
    # 要查找的值（选择一些随机值和不存在的值）
    to_find = [random.choice(data), size + 1]  # 一个存在的值，一个不存在的值
    
    for target in to_find:
        existence = "存在" if target in data else "不存在"
        print(f"\n查找{existence}的值: {target}")
        
        # 列表查找 (in 操作符)
        time_taken, found = test_performance("列表查找", lambda: target in lst)
        print(f"列表查找: {time_taken:.6f} 秒, 结果: {found}")
        
        # 字典查找键
        time_taken, found = test_performance("字典查找键", lambda: target in d)
        print(f"字典查找键: {time_taken:.6f} 秒, 结果: {found}")
        
        # 集合查找
        time_taken, found = test_performance("集合查找", lambda: target in s)
        print(f"集合查找: {time_taken:.6f} 秒, 结果: {found}")

# 3.3 删除元素性能测试
print("\n3.3 删除元素性能测试")

for size in test_sizes:
    print(f"\n删除 {size//10} 个元素 (从 {size} 个元素中):")
    
    # 生成要删除的索引/值
    to_remove = random.sample(range(size), size//10)
    
    # 列表删除 (按值)
    lst = list(range(size))
    time_taken, _ = test_performance("列表删除(按值)", 
                                   lambda: [lst.remove(v) for v in to_remove[:100]])  # 限制删除数量避免超时
    print(f"列表删除(按值): {time_taken:.6f} 秒")
    
    # 列表删除 (按索引，从末尾)
    lst = list(range(size))
    indices = sorted(random.sample(range(size), min(size//10, 100)), reverse=True)
    time_taken, _ = test_performance("列表删除(按索引，从末尾)", 
                                   lambda: [lst.pop(i) for i in indices])
    print(f"列表删除(按索引，从末尾): {time_taken:.6f} 秒")
    
    # 字典删除
    d = {i: i for i in range(size)}
    time_taken, _ = test_performance("字典删除", 
                                   lambda: [d.pop(k, None) for k in to_remove[:500]])  # 限制数量
    print(f"字典删除: {time_taken:.6f} 秒")
    
    # 集合删除
    s = set(range(size))
    time_taken, _ = test_performance("集合删除", 
                                   lambda: [s.remove(k) if k in s else None for k in to_remove[:500]])  # 限制数量
    print(f"集合删除: {time_taken:.6f} 秒")
    
    # 双端队列删除 (从两端)
    dq = deque(range(size))
    time_taken, _ = test_performance("双端队列删除(从两端)", 
                                   lambda: [dq.popleft() for _ in range(min(size//10, 1000))])
    print(f"双端队列删除(从左端): {time_taken:.6f} 秒")
    
    dq = deque(range(size))
    time_taken, _ = test_performance("双端队列删除(从右端)", 
                                   lambda: [dq.pop() for _ in range(min(size//10, 1000))])
    print(f"双端队列删除(从右端): {time_taken:.6f} 秒")

# 4. 实际应用场景性能比较

print("\n=== 实际应用场景性能比较 ===")

# 4.1 队列实现
print("\n4.1 队列实现比较")

for size in test_sizes:
    print(f"\n处理 {size} 个元素的队列操作:")
    
    # 使用列表实现队列
    def list_queue():
        q = []
        for i in range(size):
            q.append(i)  # 入队
        for _ in range(size):
            q.pop(0)  # 出队
    
    # 使用deque实现队列
    def deque_queue():
        q = deque()
        for i in range(size):
            q.append(i)  # 入队
        for _ in range(size):
            q.popleft()  # 出队
    
    # 测试性能
    list_time, _ = test_performance("列表队列", list_queue)
    print(f"列表队列: {list_time:.6f} 秒")
    
    deque_time, _ = test_performance("deque队列", deque_queue)
    print(f"deque队列: {deque_time:.6f} 秒")
    
    if list_time > deque_time:
        print(f"deque比列表快 {list_time/deque_time:.2f} 倍")
    else:
        print(f"列表比deque快 {deque_time/list_time:.2f} 倍")

# 4.2 栈实现
print("\n4.2 栈实现比较")

for size in test_sizes:
    print(f"\n处理 {size} 个元素的栈操作:")
    
    # 使用列表实现栈
    def list_stack():
        s = []
        for i in range(size):
            s.append(i)  # 入栈
        for _ in range(size):
            s.pop()  # 出栈
    
    # 使用deque实现栈
    def deque_stack():
        s = deque()
        for i in range(size):
            s.append(i)  # 入栈
        for _ in range(size):
            s.pop()  # 出栈
    
    # 测试性能
    list_time, _ = test_performance("列表栈", list_stack)
    print(f"列表栈: {list_time:.6f} 秒")
    
    deque_time, _ = test_performance("deque栈", deque_stack)
    print(f"deque栈: {deque_time:.6f} 秒")
    
    if list_time > deque_time:
        print(f"deque比列表快 {list_time/deque_time:.2f} 倍")
    else:
        print(f"列表比deque快 {deque_time/list_time:.2f} 倍")

# 4.3 词频统计
print("\n4.3 词频统计比较")

# 生成测试文本
def generate_test_text(size):
    """生成随机单词组成的测试文本"""
    words = [f"word{i}" for i in range(size//10)]  # 创建较少的不同单词以确保重复
    return [random.choice(words) for _ in range(size)]

for size in [1000, 10000, 100000]:
    print(f"\n统计 {size} 个单词的词频:")
    
    # 生成测试数据
    test_text = generate_test_text(size)
    
    # 使用字典手动统计
    def dict_count():
        counts = {}
        for word in test_text:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
    
    # 使用defaultdict统计
    def defaultdict_count():
        counts = defaultdict(int)
        for word in test_text:
            counts[word] += 1
        return counts
    
    # 使用Counter统计
    def counter_count():
        return Counter(test_text)
    
    # 测试性能
    dict_time, dict_result = test_performance("字典手动统计", dict_count)
    print(f"字典手动统计: {dict_time:.6f} 秒")
    
    defaultdict_time, defaultdict_result = test_performance("defaultdict统计", defaultdict_count)
    print(f"defaultdict统计: {defaultdict_time:.6f} 秒")
    
    counter_time, counter_result = test_performance("Counter统计", counter_count)
    print(f"Counter统计: {counter_time:.6f} 秒")
    
    # 比较效率
    best_method = min([(dict_time, "字典手动统计"), 
                      (defaultdict_time, "defaultdict统计"), 
                      (counter_time, "Counter统计")])
    print(f"最快的方法: {best_method[1]} ({best_method[0]:.6f} 秒)")

# 5. 各种数据结构的适用场景

print("\n=== 数据结构适用场景总结 ===")

# 列表(list)
print("\n5.1 列表(list)")
print("适用场景:")
print("- 需要按顺序存储和访问数据")
print("- 需要频繁访问元素（通过索引）")
print("- 需要在末尾添加或删除元素")
print("- 需要对数据进行排序或反转操作")
print("- 存储异构数据（不同类型的元素）")
print("不适用场景:")
print("- 需要频繁在中间或开头插入/删除元素")
print("- 需要频繁查找元素（特别是大列表）")
print("- 需要确保元素唯一性")

# 字典(dict)
print("\n5.2 字典(dict)")
print("适用场景:")
print("- 需要键值对映射关系")
print("- 需要通过键快速查找、添加、删除元素")
print("- 需要统计频率或计数")
print("- 需要缓存或记忆化结果")
print("- 需要表示对象属性或配置信息")
print("不适用场景:")
print("- 需要保持元素的插入顺序（Python 3.7+已支持，但不是设计初衷）")
print("- 需要基于索引访问元素")
print("- 需要对键进行排序或范围查询")

# 集合(set)
print("\n5.3 集合(set)")
print("适用场景:")
print("- 需要存储唯一元素")
print("- 需要快速判断元素是否存在")
print("- 需要进行数学集合操作（并集、交集、差集等）")
print("- 需要去重操作")
print("不适用场景:")
print("- 需要保持元素顺序")
print("- 需要重复元素")
print("- 需要键值对映射")
print("- 需要基于索引访问元素")

# 双端队列(deque)
print("\n5.4 双端队列(deque)")
print("适用场景:")
print("- 实现队列（FIFO）数据结构")
print("- 实现栈（LIFO）数据结构")
print("- 需要在两端频繁添加或删除元素")
print("- 滑动窗口算法")
print("- 广度优先搜索(BFS)")
print("不适用场景:")
print("- 需要基于索引随机访问元素")
print("- 需要在中间插入或删除元素")
print("- 需要对元素进行排序")

# 堆(heapq)
print("\n5.5 堆(heapq)")
print("适用场景:")
print("- 实现优先队列")
print("- 需要频繁获取最大/最小元素")
print("- 堆排序")
print("- 任务调度系统")
print("- 图算法（如Dijkstra算法）")
print("不适用场景:")
print("- 需要快速查找任意元素")
print("- 需要在中间插入元素")
print("- 需要维护元素的相对顺序")

# array数组
print("\n5.6 array数组")
print("适用场景:")
print("- 需要高效存储大量同类型数值数据")
print("- 需要节省内存空间")
print("- 需要与C语言代码交互")
print("- 处理二进制数据")
print("- 科学计算和数值处理")
print("不适用场景:")
print("- 需要存储不同类型的数据")
print("- 需要灵活的数据结构操作")
print("- 对于小型数据集，内存优势不明显")

# 6. 选择数据结构的决策树

print("\n=== 选择数据结构的决策树 ===")

print("1. 数据的组织方式：")
print("   ├── 需要键值对映射 → 字典(dict)")
print("   ├── 需要存储唯一元素 → 集合(set)")
print("   └── 需要线性序列：")
print("       ├── 需要频繁在两端操作 → 双端队列(deque)")
print("       ├── 需要频繁访问最大/最小元素 → 堆(heapq)")
print("       ├── 存储大量同类型数值 → array数组")
print("       └── 其他情况 → 列表(list)")

print("\n2. 操作性能需求：")
print("   ├── 频繁查找 → 字典(dict) 或 集合(set)")
print("   ├── 频繁在两端添加/删除 → 双端队列(deque)")
print("   ├── 频繁在末尾添加/删除 → 列表(list) 或 双端队列(deque)")
print("   ├── 频繁在中间插入/删除 → 考虑使用链表（Python标准库没有内置链表）")
print("   └── 频繁排序 → 列表(list) + sort()")

print("\n3. 内存使用考量：")
print("   ├── 内存受限且存储大量数值 → array数组")
print("   ├── 一般情况下 → 列表(list)")
print("   └── 需要键值对但内存紧张 → 考虑使用更紧凑的数据结构")

# 7. 综合应用示例

print("\n=== 综合应用示例 ===")

# 场景：日志分析系统
print("\n7.1 日志分析系统")

"""
假设我们需要构建一个简单的日志分析系统，具有以下功能：
- 统计不同级别的日志数量（INFO, WARNING, ERROR等）
- 统计最常出现的错误信息
- 记录日志的时间分布
- 快速查找特定时间段的日志
"""

class LogAnalyzer:
    def __init__(self):
        # 使用Counter统计日志级别
        self.level_counts = Counter()
        
        # 使用defaultdict存储错误信息和出现次数
        self.error_messages = defaultdict(int)
        
        # 使用deque存储最近的日志，便于快速添加和移除
        self.recent_logs = deque(maxlen=10000)
        
        # 使用字典存储按小时统计的日志数量
        self.hourly_logs = defaultdict(int)
        
        # 使用列表存储日志时间戳，用于二分查找
        self.timestamps = []
        self.logs_by_time = []
    
    def add_log(self, timestamp, level, message):
        # 更新日志级别计数
        self.level_counts[level]
        
        # 更新错误信息计数
        if level in ['ERROR', 'CRITICAL']:
            self.error_messages[message] += 1
        
        # 添加到最近日志队列
        self.recent_logs.append((timestamp, level, message))
        
        # 更新按小时统计
        hour_key = timestamp[:13]  # 假设timestamp格式为"2023-01-01 12:34:56"
        self.hourly_logs[hour_key] += 1
        
        # 添加到时间戳排序列表（用于二分查找）
        # 这里简化处理，实际应用中应该保持列表有序
        self.timestamps.append(timestamp)
        self.logs_by_time.append((timestamp, level, message))
    
    def get_level_stats(self):
        return self.level_counts
    
    def get_top_errors(self, n=10):
        return self.error_messages.most_common(n)
    
    def get_hourly_stats(self):
        return dict(self.hourly_logs)
    
    def find_logs_by_time_range(self, start_time, end_time):
        # 在实际应用中，应该使用bisect模块进行二分查找
        # 这里简化处理
        results = []
        for log in self.logs_by_time:
            if start_time <= log[0] <= end_time:
                results.append(log)
        return results

# 模拟日志数据生成和分析
print("模拟日志分析:")

analyzer = LogAnalyzer()
log_levels = ['INFO', 'WARNING', 'ERROR', 'CRITICAL', 'DEBUG']
error_messages = [
    "Database connection failed",
    "Network timeout",
    "Out of memory",
    "File not found",
    "Permission denied"
]

# 生成模拟日志
for i in range(1000):
    # 生成简单的时间戳
    hour = i // 100 + 10  # 10点到19点
    minute = (i % 100) // 6
    second = (i % 100) % 6 * 10
    timestamp = f"2023-01-01 {hour:02d}:{minute:02d}:{second:02d}"
    
    # 随机选择日志级别
    level = random.choice(log_levels)
    
    # 根据级别生成消息
    if level in ['ERROR', 'CRITICAL']:
        message = random.choice(error_messages)
    else:
        message = f"Normal operation {i}"
    
    analyzer.add_log(timestamp, level, message)

# 分析结果
print("\n日志级别统计:")
for level, count in analyzer.get_level_stats().items():
    print(f"{level}: {count}")

print("\n最常见的错误:")
for message, count in analyzer.get_top_errors(3):
    print(f"'{message}': {count} 次")

print("\n按小时统计:")
for hour, count in sorted(analyzer.get_hourly_stats().items()):
    print(f"{hour}:00: {count} 条")

# 8. 总结与最佳实践

print("\n=== 总结与最佳实践 ===")

print("1. 选择数据结构时，应优先考虑以下因素：")
print("   - 操作的频率和类型（查找、插入、删除等）")
print("   - 数据的大小和特性")
print("   - 内存使用限制")
print("   - 代码可读性和维护性")

print("\n2. 常见最佳实践：")
print("   - 使用列表存储有序数据，但避免频繁在中间插入/删除")
print("   - 使用字典进行快速查找和键值映射")
print("   - 使用集合确保元素唯一性和快速成员检查")
print("   - 使用deque实现队列和栈，避免使用列表的pop(0)")
print("   - 使用heapq实现优先队列和获取极值")
print("   - 使用array存储大量同类型数值以节省内存")

print("\n3. 性能优化建议：")
print("   - 对于频繁查找操作，考虑使用字典或集合代替列表")
print("   - 对于需要频繁修改的大列表，考虑使用其他数据结构")
print("   - 使用生成器和迭代器减少内存使用")
print("   - 避免在循环中进行昂贵的操作，如创建新的数据结构")
print("   - 对于特定领域的问题，考虑使用专门的库（如NumPy、pandas）")

print("\n4. 注意事项：")
print("   - Python的内置数据结构已经过高度优化，通常是性能和可用性的良好平衡")
print("   - 不要过早优化，先确保代码正确和可维护")
print("   - 使用性能分析工具（如cProfile）识别真正的性能瓶颈")
print("   - 考虑算法复杂度，有时候选择正确的算法比选择数据结构更重要")
print("   - 在实际应用中测试不同数据结构的性能，因为理论复杂度和实际性能可能有差异")

"""
本文件全面比较了Python中常见数据结构的性能特点、适用场景和实际应用。
理解这些数据结构的性能差异，对于编写高效、可靠的Python程序至关重要。
在实际开发中，应根据具体需求选择合适的数据结构，并在必要时进行性能测试和优化。

记住，没有放之四海而皆准的最佳数据结构，最好的选择取决于具体的应用场景和需求。
"""
