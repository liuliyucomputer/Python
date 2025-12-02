# Python bisect模块详解

# 1. bisect模块概述
print("=== 1. bisect模块概述 ===")
print("bisect模块提供了用于维护有序列表的二分查找算法实现。")
print("它允许在保持列表排序的同时，高效地插入和查找元素。")
print("bisect模块中的函数基于二分查找原理，时间复杂度为O(log n)。")
print("这个模块特别适用于需要频繁查找和插入操作的有序数据集。")
print()

# 2. 核心函数
print("=== 2. 核心函数 ===")

def bisect_basic_functions():
    """展示bisect模块的基本函数"""
    import bisect
    
    # 创建一个有序列表
    sorted_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"有序列表: {sorted_list}")
    
    print("\n1. bisect.bisect_left(a, x, lo=0, hi=len(a)):")
    print("   查找x应该插入到有序列表a中的位置，使得插入后列表仍保持有序")
    print("   如果x已经存在，返回其左侧第一个出现的位置")
    
    # 查找已存在元素的插入位置
    pos1 = bisect.bisect_left(sorted_list, 50)
    print(f"   bisect_left(sorted_list, 50) = {pos1}")
    
    # 查找不存在元素的插入位置
    pos2 = bisect.bisect_left(sorted_list, 35)
    print(f"   bisect_left(sorted_list, 35) = {pos2}")
    
    # 查找边界情况
    pos3 = bisect.bisect_left(sorted_list, 0)
    pos4 = bisect.bisect_left(sorted_list, 110)
    print(f"   bisect_left(sorted_list, 0) = {pos3}")
    print(f"   bisect_left(sorted_list, 110) = {pos4}")
    
    print("\n2. bisect.bisect_right(a, x, lo=0, hi=len(a)):")
    print("   查找x应该插入到有序列表a中的位置，使得插入后列表仍保持有序")
    print("   如果x已经存在，返回其右侧的位置")
    
    # 查找已存在元素的插入位置
    pos1 = bisect.bisect_right(sorted_list, 50)
    print(f"   bisect_right(sorted_list, 50) = {pos1}")
    
    # 查找不存在元素的插入位置
    pos2 = bisect.bisect_right(sorted_list, 35)
    print(f"   bisect_right(sorted_list, 35) = {pos2}")
    
    # 查找边界情况
    pos3 = bisect.bisect_right(sorted_list, 0)
    pos4 = bisect.bisect_right(sorted_list, 110)
    print(f"   bisect_right(sorted_list, 0) = {pos3}")
    print(f"   bisect_right(sorted_list, 110) = {pos4}")
    
    print("\n3. bisect.bisect(a, x, lo=0, hi=len(a)):")
    print("   bisect_right的别名，行为完全相同")
    
    # 验证bisect和bisect_right的等价性
    pos_bisect = bisect.bisect(sorted_list, 50)
    pos_right = bisect.bisect_right(sorted_list, 50)
    print(f"   bisect(sorted_list, 50) = {pos_bisect}")
    print(f"   bisect_right(sorted_list, 50) = {pos_right}")
    print(f"   是否等价: {pos_bisect == pos_right}")
    
    print("\n4. bisect.insort_left(a, x, lo=0, hi=len(a)):")
    print("   在保持列表排序的前提下，将x插入到适当的位置")
    print("   如果x已经存在，插入到左侧第一个出现的位置之前")
    
    # 创建副本进行测试
    test_list = sorted_list.copy()
    bisect.insort_left(test_list, 35)
    print(f"   插入35后: {test_list}")
    
    # 插入已存在的元素
    test_list = sorted_list.copy()
    bisect.insort_left(test_list, 50)
    print(f"   插入已存在的50后: {test_list}")
    
    print("\n5. bisect.insort_right(a, x, lo=0, hi=len(a)):")
    print("   在保持列表排序的前提下，将x插入到适当的位置")
    print("   如果x已经存在，插入到右侧的位置")
    
    # 创建副本进行测试
    test_list = sorted_list.copy()
    bisect.insort_right(test_list, 35)
    print(f"   插入35后: {test_list}")
    
    # 插入已存在的元素
    test_list = sorted_list.copy()
    bisect.insort_right(test_list, 50)
    print(f"   插入已存在的50后: {test_list}")
    
    print("\n6. bisect.insort(a, x, lo=0, hi=len(a)):")
    print("   insort_right的别名，行为完全相同")
    
    # 验证insort和insort_right的等价性
    test_list1 = sorted_list.copy()
    test_list2 = sorted_list.copy()
    bisect.insort(test_list1, 50)
    bisect.insort_right(test_list2, 50)
    print(f"   insort后的列表: {test_list1}")
    print(f"   insort_right后的列表: {test_list2}")
    print(f"   是否等价: {test_list1 == test_list2}")

bisect_basic_functions()
print()

# 3. 参数说明
print("=== 3. 参数说明 ===")

def bisect_parameters():
    """详细说明bisect模块函数的参数"""
    print("bisect模块函数的通用参数:")
    print("\n1. a: 有序列表")
    print("   - 必须是预先排序好的列表")
    print("   - 列表必须是按照升序排序的")
    print("   - 如果列表不是有序的，bisect函数将返回不正确的结果")
    
    print("\n2. x: 要查找或插入的值")
    print("   - 可以是任何可比较的对象")
    print("   - 与列表中的元素必须是可比较的类型")
    
    print("\n3. lo: 搜索的起始索引（可选）")
    print("   - 默认为0，表示从列表的开始位置搜索")
    print("   - 可以限制搜索范围以提高效率")
    
    print("\n4. hi: 搜索的结束索引（可选）")
    print("   - 默认为列表的长度，表示搜索到列表末尾")
    print("   - 注意：hi是排他的，不包括该索引位置的元素")
    
    # 演示lo和hi参数的使用
    import bisect
    
    extended_list = list(range(0, 100, 10))  # 创建0, 10, 20, ..., 90
    print(f"\n演示列表: {extended_list}")
    
    # 使用lo和hi参数限制搜索范围
    pos1 = bisect.bisect_left(extended_list, 35)  # 搜索整个列表
    pos2 = bisect.bisect_left(extended_list, 35, lo=2, hi=5)  # 只搜索索引2到4的范围
    
    print(f"在整个列表中查找35的位置: {pos1}")
    print(f"在索引2到4的范围内查找35的位置: {pos2}")
    print(f"索引2到4的子列表: {extended_list[2:5]}")
    
    # 演示lo和hi参数在insort中的使用
    test_list = extended_list.copy()
    bisect.insort_left(test_list, 35, lo=2, hi=5)
    print(f"在索引2到4的范围内插入35后的列表: {test_list}")
    
    # 错误使用示例（不演示，但解释）
    print("\n错误使用示例:")
    print("1. 使用未排序的列表:")
    print("   - 如果使用未排序的列表，bisect函数将返回不可预测的结果")
    print("   - 必须确保在使用bisect函数前列表已经排序")
    
    print("\n2. 使用不兼容的类型:")
    print("   - 如果尝试将不可比较的类型与列表元素比较，会引发TypeError")
    print("   - 例如：尝试在整数列表中查找字符串")
    
    print("\n3. 无效的lo和hi参数:")
    print("   - lo应该大于等于0，否则会被截断为0")
    print("   - hi应该小于等于列表长度，否则会被截断为列表长度")
    print("   - 如果lo >= hi，函数行为可能不正确")

bisect_parameters()
print()

# 4. 实际应用示例
print("=== 4. 实际应用示例 ===")

def bisect_practical_examples():
    """bisect模块的实际应用示例"""
    import bisect
    
    print("\n示例1: 成绩评级")
    def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
        """根据分数确定等级"""
        # 使用bisect_right查找分数应该插入的位置
        # 这实际上对应于分数所在的区间
        i = bisect.bisect_right(breakpoints, score)
        # 返回对应的等级
        return grades[i]
    
    # 测试不同分数
    scores = [55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
    print("分数及对应的等级:")
    for score in scores:
        print(f"   {score} -> {grade(score)}")
    
    print("\n示例2: 频率统计")
    def count_ranges(data, ranges):
        """统计数据在各个区间内的频率"""
        # 确保数据已排序
        data.sort()
        # 确保区间边界已排序
        ranges.sort()
        
        counts = []
        prev = 0
        
        # 统计每个区间内的元素数量
        for r in ranges:
            # 找到大于等于prev且小于r的元素数量
            # 即bisect_right(data, r-1) - bisect_left(data, prev)
            # 简化为bisect_left(data, r) - bisect_left(data, prev)
            count = bisect.bisect_left(data, r) - prev
            counts.append(count)
            prev = bisect.bisect_left(data, r)
        
        # 添加最后一个区间的计数
        counts.append(len(data) - prev)
        
        # 返回区间及其对应的计数
        result = []
        start = data[0] if data else 0
        for i, r in enumerate(ranges):
            result.append(f"[{start}, {r})")
            start = r
        result.append(f"[{start}, ∞)")
        
        return list(zip(result, counts))
    
    # 测试数据
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    ranges = [10, 20]
    
    print("数据在各个区间内的频率:")
    for interval, count in count_ranges(data, ranges):
        print(f"   {interval}: {count}")
    
    print("\n示例3: 维护已排序的数据流")
    class SortedCollection:
        """使用bisect模块维护一个有序集合"""
        def __init__(self):
            self.data = []
        
        def add(self, item):
            """添加元素并保持有序"""
            bisect.insort(self.data, item)
        
        def remove(self, item):
            """删除元素"""
            pos = bisect.bisect_left(self.data, item)
            if pos < len(self.data) and self.data[pos] == item:
                del self.data[pos]
                return True
            return False
        
        def contains(self, item):
            """检查元素是否存在"""
            pos = bisect.bisect_left(self.data, item)
            return pos < len(self.data) and self.data[pos] == item
        
        def find_ge(self, item):
            """查找大于等于item的最小元素"""
            pos = bisect.bisect_left(self.data, item)
            if pos < len(self.data):
                return self.data[pos]
            return None
        
        def find_le(self, item):
            """查找小于等于item的最大元素"""
            pos = bisect.bisect_right(self.data, item)
            if pos > 0:
                return self.data[pos-1]
            return None
        
        def __len__(self):
            return len(self.data)
        
        def __str__(self):
            return str(self.data)
    
    # 测试SortedCollection
    print("SortedCollection类的测试:")
    sorted_collection = SortedCollection()
    
    # 添加元素
    for item in [5, 2, 7, 3, 9, 1, 8, 4, 6]:
        sorted_collection.add(item)
    print(f"添加元素后: {sorted_collection}")
    
    # 检查元素是否存在
    print(f"是否包含7: {sorted_collection.contains(7)}")
    print(f"是否包含10: {sorted_collection.contains(10)}")
    
    # 查找元素
    print(f"大于等于5的最小元素: {sorted_collection.find_ge(5)}")
    print(f"小于等于5的最大元素: {sorted_collection.find_le(5)}")
    print(f"大于等于10的最小元素: {sorted_collection.find_ge(10)}")
    print(f"小于等于0的最大元素: {sorted_collection.find_le(0)}")
    
    # 删除元素
    print(f"删除3: {sorted_collection.remove(3)}")
    print(f"删除后: {sorted_collection}")
    print(f"尝试删除不存在的元素10: {sorted_collection.remove(10)}")
    
    print("\n示例4: 使用自定义比较逻辑")
    def bisect_with_key(a, x, key_func):
        """使用自定义键函数的二分查找"""
        # 创建键值列表
        keys = [key_func(item) for item in a]
        # 使用bisect_left查找位置
        pos = bisect.bisect_left(keys, x)
        return pos
    
    def insort_with_key(a, x, key_func):
        """使用自定义键函数的插入"""
        # 查找插入位置
        pos = bisect_with_key(a, key_func(x), key_func)
        # 插入元素
        a.insert(pos, x)
        return pos
    
    # 测试自定义键函数
    print("使用自定义键函数的二分查找:")
    
    # 定义一些自定义对象
    data = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 35},
        {'name': 'David', 'age': 40},
        {'name': 'Eve', 'age': 45}
    ]
    
    # 键函数 - 使用age字段
    def get_age(item):
        return item['age']
    
    # 查找age=35的位置
    pos = bisect_with_key(data, 35, get_age)
    print(f"age=35的位置: {pos}")
    print(f"对应的数据: {data[pos]}")
    
    # 查找age=37的位置
    pos = bisect_with_key(data, 37, get_age)
    print(f"age=37的位置: {pos}")
    
    # 插入一个新元素
    new_person = {'name': 'Frank', 'age': 37}
    pos = insort_with_key(data, new_person, get_age)
    print(f"插入后的列表:")
    for person in data:
        print(f"   {person}")

bisect_practical_examples()
print()

# 5. 高级应用示例
print("=== 5. 高级应用示例 ===")

def bisect_advanced_examples():
    """bisect模块的高级应用示例"""
    import bisect
    
    print("\n示例1: 二分查找算法的实现")
    def binary_search(arr, x):
        """使用bisect实现二分查找"""
        # 使用bisect_left找到插入位置
        pos = bisect.bisect_left(arr, x)
        
        # 检查元素是否存在
        if pos < len(arr) and arr[pos] == x:
            return pos  # 返回找到的索引
        return -1  # 元素不存在
    
    # 测试二分查找
    test_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"测试数组: {test_arr}")
    print(f"查找40: 索引 = {binary_search(test_arr, 40)}")
    print(f"查找45: 索引 = {binary_search(test_arr, 45)}")
    print(f"查找10: 索引 = {binary_search(test_arr, 10)}")
    print(f"查找100: 索引 = {binary_search(test_arr, 100)}")
    print(f"查找0: 索引 = {binary_search(test_arr, 0)}")
    print(f"查找110: 索引 = {binary_search(test_arr, 110)}")
    
    print("\n示例2: 寻找最接近的值")
    def find_nearest(arr, x):
        """在有序数组中找到最接近x的值"""
        # 找到插入位置
        pos = bisect.bisect_left(arr, x)
        
        # 边界情况处理
        if pos == 0:
            return arr[0]
        if pos == len(arr):
            return arr[-1]
        
        # 比较左右两个元素，返回更接近的一个
        left = arr[pos - 1]
        right = arr[pos]
        
        if (x - left) <= (right - x):
            return left
        else:
            return right
    
    # 测试寻找最接近的值
    print(f"测试数组: {test_arr}")
    print(f"最接近42的值: {find_nearest(test_arr, 42)}")
    print(f"最接近35的值: {find_nearest(test_arr, 35)}")
    print(f"最接近5的值: {find_nearest(test_arr, 5)}")
    print(f"最接近105的值: {find_nearest(test_arr, 105)}")
    
    print("\n示例3: 范围查询")
    def range_query(arr, low, high):
        """查询有序数组中介于[low, high)之间的所有元素"""
        # 找到low应该插入的位置（即第一个>=low的元素）
        left_pos = bisect.bisect_left(arr, low)
        
        # 找到high应该插入的位置（即第一个>=high的元素）
        right_pos = bisect.bisect_left(arr, high)
        
        # 返回区间[left_pos, right_pos)内的所有元素
        return arr[left_pos:right_pos]
    
    # 测试范围查询
    extended_arr = list(range(5, 100, 5))  # [5, 10, 15, ..., 95]
    print(f"扩展测试数组: {extended_arr}")
    print(f"范围[20, 50)内的元素: {range_query(extended_arr, 20, 50)}")
    print(f"范围[5, 10)内的元素: {range_query(extended_arr, 5, 10)}")
    print(f"范围[95, 100)内的元素: {range_query(extended_arr, 95, 100)}")
    print(f"范围[0, 5)内的元素: {range_query(extended_arr, 0, 5)}")
    print(f"范围[100, 200)内的元素: {range_query(extended_arr, 100, 200)}")
    
    print("\n示例4: 前缀和与二分查找的结合")
    def weighted_random_selection(weights):
        """根据权重进行随机选择"""
        import random
        
        # 计算前缀和数组
        prefix_sums = []
        current_sum = 0
        for w in weights:
            current_sum += w
            prefix_sums.append(current_sum)
        
        # 生成随机数
        r = random.random() * current_sum
        
        # 使用bisect_left找到对应的索引
        index = bisect.bisect_left(prefix_sums, r)
        return index
    
    # 测试带权重的随机选择
    weights = [1, 2, 3, 4]  # 权重分别为1, 2, 3, 4
    print(f"权重数组: {weights}")
    
    # 进行多次随机选择，统计结果
    results = [0] * len(weights)
    iterations = 10000
    
    for _ in range(iterations):
        idx = weighted_random_selection(weights)
        results[idx] += 1
    
    print(f"{iterations}次随机选择的结果:")
    for i, count in enumerate(results):
        probability = count / iterations * 100
        expected = weights[i] / sum(weights) * 100
        print(f"   索引{i}: 出现{count}次 ({probability:.1f}%), 期望概率: {expected:.1f}%")
    
    print("\n示例5: 使用bisect实现的缓存替换策略")
    class LRUCache:
        """使用bisect模块实现的LRU (Least Recently Used) 缓存"""
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = {}
            self.usage_order = []  # 存储最近使用的键的时间戳和键
            self.timestamp = 0
        
        def get(self, key):
            """获取键对应的值"""
            if key in self.cache:
                # 更新使用时间
                self._update_usage(key)
                return self.cache[key]
            return None
        
        def put(self, key, value):
            """存储键值对"""
            if key not in self.cache and len(self.cache) >= self.capacity:
                # 需要淘汰最久未使用的键
                self._evict_oldest()
            
            # 存储值
            self.cache[key] = value
            # 更新使用时间
            self._update_usage(key)
        
        def _update_usage(self, key):
            """更新键的使用时间"""
            # 增加时间戳
            self.timestamp += 1
            
            # 移除旧的使用记录
            for i, (ts, k) in enumerate(self.usage_order):
                if k == key:
                    del self.usage_order[i]
                    break
            
            # 使用bisect插入新记录（按时间戳升序）
            # 由于我们使用的是bisect.insort，它会自动找到正确位置
            bisect.insort(self.usage_order, (self.timestamp, key))
        
        def _evict_oldest(self):
            """淘汰最久未使用的键"""
            if self.usage_order:
                # 移除最早使用的键（索引0）
                oldest_key = self.usage_order[0][1]
                del self.usage_order[0]
                del self.cache[oldest_key]
        
        def __str__(self):
            """返回缓存的字符串表示"""
            return str(self.cache)
    
    # 测试LRU缓存
    print("LRU缓存测试:")
    lru = LRUCache(3)  # 容量为3的缓存
    
    lru.put(1, "一")
    lru.put(2, "二")
    lru.put(3, "三")
    print(f"缓存初始状态: {lru}")
    
    # 访问键1，应该更新其使用时间
    print(f"获取键1: {lru.get(1)}")
    
    # 添加新键4，应该淘汰键2（最久未使用）
    lru.put(4, "四")
    print(f"添加键4后: {lru}")
    print(f"尝试获取已淘汰的键2: {lru.get(2)}")
    
    # 访问键3，然后添加键5，应该淘汰键1
    print(f"获取键3: {lru.get(3)}")
    lru.put(5, "五")
    print(f"添加键5后: {lru}")
    print(f"尝试获取已淘汰的键1: {lru.get(1)}")

bisect_advanced_examples()
print()

# 6. 性能分析
print("=== 6. 性能分析 ===")

def bisect_performance_analysis():
    """bisect模块的性能分析"""
    import bisect
    import time
    import random
    
    print("1. 时间复杂度分析:")
    print("   - bisect_left和bisect_right函数: O(log n)")
    print("   - insort_left和insort_right函数: O(n)")
    print("     (因为插入操作需要移动元素，这部分是线性的)")
    print()
    
    print("2. 性能测试:")
    
    # 测试不同大小的数据集
    sizes = [1000, 10000, 100000, 1000000]
    
    for size in sizes:
        print(f"\n数据集大小: {size:,}")
        
        # 创建有序列表
        sorted_list = list(range(size))
        
        # 测试bisect_left性能
        start_time = time.time()
        for _ in range(10000):
            # 随机查找一个值
            target = random.randint(-1000, size + 1000)
            bisect.bisect_left(sorted_list, target)
        end_time = time.time()
        print(f"   bisect_left (10,000次操作): {end_time - start_time:.6f} 秒")
        
        # 测试insort_left性能（使用较小的数据集以避免测试时间过长）
        if size <= 100000:
            test_list = list(range(size))
            start_time = time.time()
            for _ in range(1000):
                # 随机插入一个值
                value = random.randint(-1000, size + 1000)
                bisect.insort_left(test_list, value)
            end_time = time.time()
            print(f"   insort_left (1,000次操作): {end_time - start_time:.6f} 秒")
        else:
            print(f"   insort_left: 数据集过大，跳过测试")
    
    print("\n3. 性能优化建议:")
    print("   - 对于频繁的插入操作，如果可能，预先对数据排序并一次性创建列表")
    print("   - 使用lo和hi参数限制搜索范围，特别是在大型列表中")
    print("   - 对于自定义对象的排序，可以考虑使用key函数预处理并缓存键值")
    print("   - 对于非常大的数据集或频繁的插入操作，考虑使用更高效的数据结构")
    print("   - 在Python 3.10+中，可以使用内置的bisect模块与functools.cmp_to_key结合使用自定义比较器")

bisect_performance_analysis()
print()

# 7. 注意事项和常见问题
print("=== 7. 注意事项和常见问题 ===")

def bisect_caveats():
    """bisect模块的注意事项和常见问题"""
    import bisect
    
    print("1. 列表必须有序:")
    print("   - bisect模块的所有函数都假设列表是按照升序排序的")
    print("   - 如果列表未排序，函数将返回不正确的结果")
    print("   - 始终确保在使用bisect函数之前列表已经排序")
    
    # 示例：使用未排序列表的错误
    print("\n示例：使用未排序列表的错误:")
    unsorted_list = [30, 10, 50, 20, 40]
    print(f"未排序列表: {unsorted_list}")
    # 错误地使用bisect
    pos = bisect.bisect_left(unsorted_list, 25)
    print(f"查找25的位置: {pos} (结果错误)")
    # 正确的做法
    sorted_list = sorted(unsorted_list)
    print(f"排序后的列表: {sorted_list}")
    pos = bisect.bisect_left(sorted_list, 25)
    print(f"查找25的位置: {pos} (结果正确)")
    
    print("\n2. 可比较性:")
    print("   - 要查找或插入的值必须与列表中的元素类型兼容")
    print("   - 如果尝试比较不可比较的类型，将引发TypeError")
    
    # 示例：不可比较的类型
    print("\n示例：不可比较的类型:")
    try:
        mixed_list = [1, 2, 3, 4, 5]
        # 尝试比较整数和字符串
        pos = bisect.bisect_left(mixed_list, "3")
    except TypeError as e:
        print(f"引发TypeError: {e}")
    
    print("\n3. 相等元素的处理:")
    print("   - bisect_left在相等元素的左侧插入")
    print("   - bisect_right在相等元素的右侧插入")
    print("   - 选择哪种取决于具体的应用需求")
    
    # 示例：相等元素的处理
    print("\n示例：相等元素的处理:")
    list_with_duplicates = [10, 20, 20, 30, 40]
    print(f"包含重复元素的列表: {list_with_duplicates}")
    
    pos_left = bisect.bisect_left(list_with_duplicates, 20)
    pos_right = bisect.bisect_right(list_with_duplicates, 20)
    
    print(f"bisect_left查找20的位置: {pos_left}")
    print(f"bisect_right查找20的位置: {pos_right}")
    print(f"等于20的元素个数: {pos_right - pos_left}")
    
    print("\n4. 内存效率:")
    print("   - bisect.insort函数需要移动列表元素，对于大型列表可能效率较低")
    print("   - 如果需要频繁插入，考虑使用collections.deque或其他数据结构")
    
    print("\n5. 边界条件:")
    print("   - 处理空列表时不会引发异常")
    print("   - 查找超出范围的值会返回0或列表长度")
    
    # 示例：边界条件
    print("\n示例：边界条件:")
    empty_list = []
    print(f"空列表查找10: {bisect.bisect_left(empty_list, 10)}")
    
    single_element = [50]
    print(f"单元素列表 [50] 查找40: {bisect.bisect_left(single_element, 40)}")
    print(f"单元素列表 [50] 查找60: {bisect.bisect_left(single_element, 60)}")
    
    print("\n6. 自定义排序:")
    print("   - bisect模块本身不支持直接使用key函数")
    print("   - 对于自定义排序，需要手动创建键值列表或使用其他方法")
    
    print("\n7. 线程安全性:")
    print("   - bisect模块的函数不是线程安全的")
    print("   - 在多线程环境中使用时，需要自己加锁保护共享列表")

bisect_caveats()
print()

# 8. 输入输出示例
print("=== 8. 输入输出示例 ===")

def bisect_io_examples():
    """bisect模块的输入输出示例"""
    print("\n示例1: 基本的bisect操作")
    print("输入:")
    print("    import bisect")
    print("    sorted_list = [10, 20, 30, 40, 50]")
    print("    ")
    print("    # 查找元素位置")
    print("    print(f'bisect_left查找30: {bisect.bisect_left(sorted_list, 30)}')")
    print("    print(f'bisect_right查找30: {bisect.bisect_right(sorted_list, 30)}')")
    print("    print(f'bisect查找30: {bisect.bisect(sorted_list, 30)}')")
    print("    ")
    print("    # 查找不存在的元素位置")
    print("    print(f'bisect_left查找35: {bisect.bisect_left(sorted_list, 35)}')")
    print("输出:")
    print("    bisect_left查找30: 2")
    print("    bisect_right查找30: 3")
    print("    bisect查找30: 3")
    print("    bisect_left查找35: 3")
    
    print("\n示例2: 基本的insort操作")
    print("输入:")
    print("    import bisect")
    print("    sorted_list = [10, 20, 30, 40, 50]")
    print("    ")
    print("    # 插入元素")
    print("    bisect.insort_left(sorted_list, 35)")
    print("    print(f'插入35后: {sorted_list}')")
    print("    ")
    print("    # 插入已存在的元素")
    print("    bisect.insort_left(sorted_list, 30)")
    print("    print(f'插入30后: {sorted_list}')")
    print("    ")
    print("    # 使用insort")
    print("    bisect.insort(sorted_list, 25)")
    print("    print(f'插入25后: {sorted_list}')")
    print("输出:")
    print("    插入35后: [10, 20, 30, 35, 40, 50]")
    print("    插入30后: [10, 20, 30, 30, 35, 40, 50]")
    print("    插入25后: [10, 20, 25, 30, 30, 35, 40, 50]")
    
    print("\n示例3: 使用lo和hi参数")
    print("输入:")
    print("    import bisect")
    print("    extended_list = list(range(0, 100, 10))  # [0, 10, 20, ..., 90]")
    print("    print(f'扩展列表: {extended_list}')")
    print("    ")
    print("    # 限制搜索范围")
    print("    print(f'在索引2到5范围内查找35: {bisect.bisect_left(extended_list, 35, lo=2, hi=5)}')")
    print("    print(f'在索引2到5范围内插入35:')")
    print("    test_list = extended_list.copy()")
    print("    bisect.insort_left(test_list, 35, lo=2, hi=5)")
    print("    print(f'插入后: {test_list}')")
    print("输出:")
    print("    扩展列表: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]")
    print("    在索引2到5范围内查找35: 3")
    print("    在索引2到5范围内插入35:")
    print("    插入后: [0, 10, 20, 30, 35, 40, 50, 60, 70, 80, 90]")
    
    print("\n示例4: 实现自定义的二分查找")
    print("输入:")
    print("    import bisect")
    print("    ")
    print("    def binary_search(arr, x):")
    print("        pos = bisect.bisect_left(arr, x)")
    print("        if pos < len(arr) and arr[pos] == x:")
    print("            return pos")
    print("        return -1")
    print("    ")
    print("    test_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]")
    print("    print(f'查找40: {binary_search(test_arr, 40)}')")
    print("    print(f'查找45: {binary_search(test_arr, 45)}')")
    print("输出:")
    print("    查找40: 3")
    print("    查找45: -1")

bisect_io_examples()
print()

# 9. 总结和完整导入指南
print("=== 9. 总结和完整导入指南 ===")

def bisect_summary():
    """bisect模块总结和导入指南"""
    print("bisect模块提供了基于二分查找算法的函数，用于维护有序列表。\n")
    
    # 核心功能
    print("核心功能:")
    print("- 提供O(log n)时间复杂度的二分查找算法")
    print("- 支持在保持列表排序的同时插入新元素")
    print("- 适用于需要频繁查找和插入操作的有序数据集")
    print("- 是实现各种高级数据结构和算法的基础")
    
    # 主要函数
    print("\n主要函数:")
    print("1. bisect.bisect_left(a, x, lo=0, hi=len(a))")
    print("   在有序列表a中查找x的插入位置，保证插入后列表仍有序")
    print("   如果x已存在，返回其第一次出现的位置")
    
    print("\n2. bisect.bisect_right(a, x, lo=0, hi=len(a))")
    print("   在有序列表a中查找x的插入位置，保证插入后列表仍有序")
    print("   如果x已存在，返回其最后一次出现的位置之后")
    
    print("\n3. bisect.bisect(a, x, lo=0, hi=len(a))")
    print("   bisect_right的别名")
    
    print("\n4. bisect.insort_left(a, x, lo=0, hi=len(a))")
    print("   在保持列表排序的前提下插入x")
    print("   如果x已存在，插入到第一次出现的位置之前")
    
    print("\n5. bisect.insort_right(a, x, lo=0, hi=len(a))")
    print("   在保持列表排序的前提下插入x")
    print("   如果x已存在，插入到最后一次出现的位置之后")
    
    print("\n6. bisect.insort(a, x, lo=0, hi=len(a))")
    print("   insort_right的别名")
    
    # 导入指南
    print("\n导入指南:")
    print("\n1. 导入整个模块:")
    print("   import bisect")
    print("   ")
    print("   使用方式:")
    print("   sorted_list = [10, 20, 30, 40, 50]")
    print("   position = bisect.bisect_left(sorted_list, 35)")
    print("   bisect.insort(sorted_list, 35)")
    
    print("\n2. 从模块中导入特定函数:")
    print("   from bisect import bisect_left, bisect_right, insort")
    print("   ")
    print("   使用方式:")
    print("   sorted_list = [10, 20, 30, 40, 50]")
    print("   position = bisect_left(sorted_list, 35)")
    print("   insort(sorted_list, 35)")
    
    print("\n3. 导入所有函数:")
    print("   from bisect import *")
    print("   ")
    print("   注意: 这种方式可能会与其他模块的函数名冲突，不推荐在复杂程序中使用")
    
    # 最佳实践
    print("\n最佳实践:")
    print("1. 始终确保列表是有序的，最好是升序排序")
    print("2. 根据需要选择合适的函数:")
    print("   - 仅需查找位置: bisect_left 或 bisect_right")
    print("   - 需要插入元素: insort_left 或 insort_right")
    print("3. 对于大数据集，使用lo和hi参数限制搜索范围以提高效率")
    print("4. 对于自定义对象，考虑使用额外的键值列表或自定义比较逻辑")
    print("5. 对于频繁的插入操作，评估是否有更适合的数据结构")
    
    # 版本兼容性
    print("\n版本兼容性:")
    print("- bisect模块在Python 2和Python 3中都可用")
    print("- 函数接口在Python 2和Python 3中基本相同")
    print("- Python 3中没有特别的更新或弃用")
    
    # 最终建议
    print("\n最终建议:")
    print("- bisect模块是实现有序数据管理的轻量级解决方案")
    print("- 对于简单的应用场景，直接使用bisect模块即可")
    print("- 对于复杂的应用场景，考虑基于bisect模块构建自定义数据结构")
    print("- 在处理大量数据时，注意性能优化和内存使用")

bisect_summary()

print("\n至此，bisect模块的全部功能已详细介绍完毕。")
