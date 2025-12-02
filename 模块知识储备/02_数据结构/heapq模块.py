# Python heapq模块详解

# 1. heapq模块概述
print("=== 1. heapq模块概述 ===")
print("heapq模块实现了堆队列算法（优先队列算法），提供了堆操作的相关功能。")
print("该模块主要用于以下场景：")
print("- 实现优先队列，快速获取最小或最大元素")
print("- 高效排序和选择算法")
print("- 图算法中的优先队列实现（如Dijkstra算法）")
print("- 数据流中的Top N元素处理")
print("heapq模块实现的是最小堆（min-heap），堆顶元素始终是最小的元素。")
print()

# 2. heapq模块核心函数
print("=== 2. heapq模块核心函数 ===")

def heapq_core_functions():
    """展示heapq模块的核心函数"""
    import heapq
    import random
    
    print("1. 堆的基本操作")
    print("   heapq模块提供了创建和操作堆的基本函数")
    
    # 创建一个空列表作为堆
    heap = []
    
    # 使用heappush添加元素
    print("   使用heappush添加元素:")
    data = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"   原始数据: {data}")
    
    for item in data:
        heapq.heappush(heap, item)
        print(f"   添加 {item} 后的堆: {heap}")
    
    # 使用heappop弹出最小元素
    print("   \n使用heappop弹出最小元素:")
    while heap:
        smallest = heapq.heappop(heap)
        print(f"   弹出最小元素: {smallest}, 剩余堆: {heap}")
    
    print("\n2. heapify函数 - 将列表转换为堆")
    print("   直接将现有列表原地转换为堆结构，时间复杂度O(n)")
    
    # 创建一个未排序的列表
    data = [7, 1, 3, 5, 2, 8, 4, 6]
    print(f"   原始列表: {data}")
    
    # 原地转换为堆
    heapq.heapify(data)
    print(f"   转换后的堆: {data}")
    
    # 验证堆属性
    print(f"   堆顶元素（最小值）: {data[0]}")
    
    print("\n3. heappushpop函数 - 先推入再弹出")
    print("   结合了heappush和heappop的操作，比单独调用更高效")
    
    # 创建一个堆
    heap = [1, 3, 5, 7, 9]
    print(f"   原始堆: {heap}")
    
    # 使用heappushpop
    result = heapq.heappushpop(heap, 4)
    print(f"   推入4后弹出的结果: {result}")
    print(f"   操作后的堆: {heap}")
    
    # 与单独调用对比
    heap2 = [1, 3, 5, 7, 9]
    heapq.heappush(heap2, 4)
    result2 = heapq.heappop(heap2)
    print(f"   单独调用的结果: {result2}")
    print(f"   操作后的堆2: {heap2}")
    
    print("\n4. heapreplace函数 - 先弹出再推入")
    print("   先弹出最小元素，然后推入新元素，保持堆大小不变")
    
    # 创建一个堆
    heap = [1, 3, 5, 7, 9]
    print(f"   原始堆: {heap}")
    
    # 使用heapreplace
    result = heapq.heapreplace(heap, 6)
    print(f"   替换后弹出的结果: {result}")
    print(f"   操作后的堆: {heap}")
    
    print("\n5. nlargest和nsmallest函数")
    print("   获取可迭代对象中最大或最小的n个元素")
    
    # 测试数据
    data = [random.randint(1, 100) for _ in range(10)]
    print(f"   测试数据: {data}")
    
    # 获取最大的3个元素
    largest = heapq.nlargest(3, data)
    print(f"   最大的3个元素: {largest}")
    
    # 获取最小的3个元素
    smallest = heapq.nsmallest(3, data)
    print(f"   最小的3个元素: {smallest}")
    
    # 使用key参数
    people = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20},
        {'name': 'David', 'age': 35},
        {'name': 'Eve', 'age': 28}
    ]
    
    # 按年龄排序获取最年轻的2个人
    youngest = heapq.nsmallest(2, people, key=lambda x: x['age'])
    print(f"   最年轻的2个人: {[p['name'] for p in youngest]}")
    
    # 按年龄排序获取最年长的2个人
    oldest = heapq.nlargest(2, people, key=lambda x: x['age'])
    print(f"   最年长的2个人: {[p['name'] for p in oldest]}")
    
    print("\n6. 堆的性质验证")
    print("   验证堆的重要性质：对于索引i，其父节点索引为(i-1)//2，左子节点为2*i+1，右子节点为2*i+2")
    
    # 创建一个堆
    heap = []
    for i in range(10):
        heapq.heappush(heap, i)
    
    print(f"   堆结构: {heap}")
    
    # 验证堆性质
    is_valid = True
    for i in range(1, len(heap)):
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            is_valid = False
            break
    
    print(f"   堆性质验证: {'通过' if is_valid else '失败'}")
    
    # 显示堆的层次结构
    print("   \n堆的层次结构:")
    level = 0
    while 2 ** level - 1 < len(heap):
        start = 2 ** level - 1
        end = min(2 ** (level + 1) - 1, len(heap))
        print(f"   第{level}层: {heap[start:end]}")
        level += 1

# 运行核心函数演示
heapq_core_functions()
print()

# 3. 优先队列实现
print("=== 3. 优先队列实现 ===")

def priority_queue_implementation():
    """使用heapq实现优先队列"""
    import heapq
    
    print("1. 基本优先队列")
    print("   使用(优先级, 计数器, 任务)元组实现稳定的优先队列")
    
    # 基本优先队列类
    class PriorityQueue:
        def __init__(self):
            self._queue = []  # 存储堆元素
            self._index = 0   # 计数器，用于保持同优先级元素的FIFO顺序
        
        def push(self, item, priority=0):
            """添加元素到队列，默认优先级为0（数字越小优先级越高）"""
            # 注意：使用负优先级可以让数字越大优先级越高
            heapq.heappush(self._queue, (priority, self._index, item))
            self._index += 1
        
        def pop(self):
            """移除并返回优先级最高的元素"""
            if not self._queue:
                raise IndexError("优先队列为空")
            return heapq.heappop(self._queue)[-1]  # 返回任务部分
        
        def peek(self):
            """查看优先级最高的元素但不移除"""
            if not self._queue:
                return None
            return self._queue[0][-1]
        
        def empty(self):
            """检查队列是否为空"""
            return len(self._queue) == 0
        
        def size(self):
            """返回队列大小"""
            return len(self._queue)
    
    # 测试基本优先队列
    pq = PriorityQueue()
    
    # 添加任务
    pq.push('普通任务', 3)
    pq.push('重要任务', 1)
    pq.push('紧急任务', 0)
    pq.push('次要任务', 5)
    pq.push('中等任务', 2)
    
    print(f"   队列大小: {pq.size()}")
    print(f"   队列首元素: {pq.peek()}")
    
    print("   \n按优先级处理任务:")
    while not pq.empty():
        task = pq.pop()
        print(f"   处理任务: {task}")
    
    print("\n2. 最大优先队列")
    print("   通过使用负优先级实现最大堆行为")
    
    class MaxPriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0
        
        def push(self, item, priority=0):
            """添加元素，数字越大优先级越高"""
            heapq.heappush(self._queue, (-priority, self._index, item))  # 使用负优先级
            self._index += 1
        
        def pop(self):
            """移除并返回优先级最高的元素"""
            if not self._queue:
                raise IndexError("优先队列为空")
            return heapq.heappop(self._queue)[-1]
        
        def empty(self):
            return len(self._queue) == 0
    
    # 测试最大优先队列
    max_pq = MaxPriorityQueue()
    
    # 添加任务（优先级数字越大越重要）
    max_pq.push('普通任务', 1)
    max_pq.push('重要任务', 3)
    max_pq.push('紧急任务', 5)
    max_pq.push('次要任务', 0)
    
    print("   按优先级处理任务（数字越大越优先）:")
    while not max_pq.empty():
        task = max_pq.pop()
        print(f"   处理任务: {task}")
    
    print("\n3. 带截止时间的优先队列")
    print("   结合时间和优先级的高级优先队列")
    
    import time
    
    class DeadlinePriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0
        
        def push(self, item, priority=0, deadline=None):
            """添加带截止时间的任务
            
            Args:
                item: 任务项
                priority: 优先级（数字越小优先级越高）
                deadline: 截止时间戳，None表示无截止时间
            """
            # 如果没有截止时间，使用一个很大的值
            if deadline is None:
                deadline = float('inf')
            
            # (截止时间, 优先级, 索引, 任务)
            heapq.heappush(self._queue, (deadline, priority, self._index, item))
            self._index += 1
        
        def pop(self):
            """移除并返回最紧急的任务（先按截止时间，再按优先级）"""
            if not self._queue:
                raise IndexError("优先队列为空")
            return heapq.heappop(self._queue)[-1]
        
        def get_overdue_tasks(self, current_time=None):
            """获取已过期的任务列表"""
            if current_time is None:
                current_time = time.time()
            
            overdue = []
            valid_queue = []
            
            # 分离过期和有效任务
            for task in self._queue:
                if task[0] < current_time:
                    overdue.append(task[-1])
                else:
                    valid_queue.append(task)
            
            # 重建堆
            self._queue = valid_queue
            heapq.heapify(self._queue)
            
            return overdue
        
        def empty(self):
            return len(self._queue) == 0
    
    # 模拟时间
    current_time = 100
    
    # 测试截止时间优先队列
    deadline_pq = DeadlinePriorityQueue()
    
    # 添加任务
    deadline_pq.push('紧急任务1', 0, current_time + 5)    # 5秒后截止
    deadline_pq.push('普通任务', 2, current_time + 30)     # 30秒后截止
    deadline_pq.push('紧急任务2', 0, current_time + 10)   # 10秒后截止
    deadline_pq.push('已过期任务', 1, current_time - 5)   # 已过期
    
    # 获取过期任务
    overdue = deadline_pq.get_overdue_tasks(current_time)
    print(f"   当前时间: {current_time}")
    print(f"   过期任务: {overdue}")
    
    print("   \n处理剩余任务:")
    while not deadline_pq.empty():
        task = deadline_pq.pop()
        print(f"   处理任务: {task}")
    
    print("\n4. 优先队列的应用场景")
    print("   - 任务调度系统")
    print("   - 事件驱动模拟")
    print("   - 网络数据包处理")
    print("   - 资源分配系统")
    print("   - 图算法（如Dijkstra最短路径算法）")
    print("   - 多线程任务优先级处理")

# 运行优先队列实现演示
priority_queue_implementation()
print()

# 4. 堆排序实现
print("=== 4. 堆排序实现 ===")

def heap_sort_implementation():
    """使用heapq模块实现堆排序"""
    import heapq
    import random
    import time
    
    print("1. 基本堆排序实现")
    print("   使用heappush和heappop实现稳定的排序算法")
    
    def heap_sort(arr):
        """堆排序算法实现"""
        heap = []
        # 构建堆
        for item in arr:
            heapq.heappush(heap, item)
        
        # 提取排序后的元素
        sorted_arr = []
        while heap:
            sorted_arr.append(heapq.heappop(heap))
        
        return sorted_arr
    
    # 测试堆排序
    test_data = [random.randint(1, 1000) for _ in range(20)]
    print(f"   原始数据: {test_data[:10]}...")
    
    sorted_data = heap_sort(test_data)
    print(f"   排序后: {sorted_data[:10]}...")
    
    # 验证排序正确性
    is_sorted = all(sorted_data[i] <= sorted_data[i+1] for i in range(len(sorted_data)-1))
    print(f"   排序验证: {'成功' if is_sorted else '失败'}")
    
    print("\n2. 原地堆排序")
    print("   不使用额外空间的堆排序实现")
    
    def in_place_heap_sort(arr):
        """原地堆排序实现"""
        # 先将列表转换为最大堆
        # 从最后一个非叶子节点开始，自底向上调整
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            _heapify_max(arr, n, i)
        
        # 逐个提取最大元素并放到数组末尾
        for i in range(n - 1, 0, -1):
            # 将当前堆顶（最大值）与末尾元素交换
            arr[i], arr[0] = arr[0], arr[i]
            # 对剩余的元素重新调整为最大堆
            _heapify_max(arr, i, 0)
    
    def _heapify_max(arr, heap_size, root_index):
        """将以root_index为根的子树调整为最大堆"""
        largest = root_index
        left_child = 2 * root_index + 1
        right_child = 2 * root_index + 2
        
        # 如果左子节点存在且大于根节点
        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child
        
        # 如果右子节点存在且大于目前的最大值
        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child
        
        # 如果最大值不是根节点
        if largest != root_index:
            # 交换根节点与最大值
            arr[root_index], arr[largest] = arr[largest], arr[root_index]
            # 递归调整受影响的子树
            _heapify_max(arr, heap_size, largest)
    
    # 测试原地堆排序
    test_data = [random.randint(1, 1000) for _ in range(20)]
    print(f"   原始数据: {test_data[:10]}...")
    
    in_place_heap_sort(test_data)
    print(f"   排序后: {test_data[:10]}...")
    
    # 验证排序正确性
    is_sorted = all(test_data[i] <= test_data[i+1] for i in range(len(test_data)-1))
    print(f"   排序验证: {'成功' if is_sorted else '失败'}")
    
    print("\n3. 堆排序性能分析")
    print("   比较堆排序与Python内置排序的性能")
    
    # 生成较大的测试数据
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        print(f"   \n处理 {size} 个元素:")
        
        # 生成随机数据
        data = [random.randint(1, 100000) for _ in range(size)]
        
        # 测试堆排序性能
        data_copy1 = data.copy()
        start_time = time.time()
        heap_sort_result = heap_sort(data_copy1)
        heap_sort_time = time.time() - start_time
        
        # 测试Python内置排序性能
        data_copy2 = data.copy()
        start_time = time.time()
        data_copy2.sort()
        builtin_sort_time = time.time() - start_time
        
        # 验证两种方法结果一致
        results_match = heap_sort_result == data_copy2
        
        print(f"   堆排序耗时: {heap_sort_time:.6f} 秒")
        print(f"   内置排序耗时: {builtin_sort_time:.6f} 秒")
        print(f"   结果一致性: {'一致' if results_match else '不一致'}")
    
    print("\n4. 堆排序的优缺点")
    print("   优点:")
    print("   - 高效的时间复杂度：平均、最坏和最好情况均为O(n log n)")
    print("   - 适用于大数据集和流式数据处理")
    print("   - 可以实现优先级队列功能")
    print("   - 原地堆排序的空间复杂度为O(1)")
    print("   ")
    print("   缺点:")
    print("   - 不是稳定排序算法（相等元素的相对顺序可能改变）")
    print("   - 缓存局部性较差，对现代处理器不太友好")
    print("   - 对于小规模数据，性能可能不如插入排序等简单算法")
    print("   - Python内置排序已经过高度优化，通常比手动实现的堆排序更快")
    
    print("\n5. 堆排序的适用场景")
    print("   - 需要稳定的O(n log n)性能保证")
    print("   - 需要同时进行排序和优先级队列操作")
    print("   - 内存空间有限，需要原地排序")
    print("   - 处理流式数据，需要维护部分排序结果")
    print("   - 实现自定义排序逻辑的场景")

# 运行堆排序实现演示
heap_sort_implementation()
print()

# 5. 高级应用示例
print("=== 5. 高级应用示例 ===")

def heapq_advanced_examples():
    """heapq模块的高级应用示例"""
    import heapq
    import random
    import time
    
    print("1. 合并多个有序序列")
    print("   使用heapq.merge高效合并多个已排序的序列")
    
    # 生成多个有序序列
    def generate_sorted_sequences(num_sequences=3, seq_length=5, max_value=100):
        sequences = []
        for _ in range(num_sequences):
            # 生成随机数据并排序
            seq = sorted(random.sample(range(max_value), seq_length))
            sequences.append(seq)
        return sequences
    
    # 获取测试数据
    sequences = generate_sorted_sequences(4, 6, 200)
    
    # 打印输入序列
    print("   输入有序序列:")
    for i, seq in enumerate(sequences):
        print(f"   序列{i+1}: {seq}")
    
    # 使用heapq.merge合并序列
    merged = list(heapq.merge(*sequences))
    
    print(f"   \n合并结果: {merged}")
    
    # 验证结果是否有序
    is_sorted = all(merged[i] <= merged[i+1] for i in range(len(merged)-1))
    print(f"   合并验证: {'成功' if is_sorted else '失败'}")
    
    print("\n2. 寻找数组中的第k大元素")
    print("   使用heapq高效查找第k大元素")
    
    def find_kth_largest(arr, k):
        """找到数组中第k大的元素"""
        # 使用最小堆，保持堆大小为k
        min_heap = []
        
        for num in arr:
            # 如果堆大小小于k，直接添加
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            # 如果当前元素大于堆顶，替换堆顶
            elif num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        
        # 堆顶即为第k大元素
        return min_heap[0]
    
    # 测试数据
    arr = [random.randint(1, 1000) for _ in range(30)]
    k = 5
    
    print(f"   数组样本: {arr[:10]}...")
    print(f"   寻找第{k}大元素")
    
    # 使用我们的方法
    result1 = find_kth_largest(arr, k)
    
    # 使用排序验证
    sorted_arr = sorted(arr, reverse=True)
    result2 = sorted_arr[k-1]
    
    print(f"   使用堆方法结果: {result1}")
    print(f"   使用排序验证: {result2}")
    print(f"   结果验证: {'正确' if result1 == result2 else '错误'}")
    
    print("\n3. 实现Top K频繁元素统计")
    print("   统计数组中出现频率最高的k个元素")
    
    def top_k_frequent_elements(nums, k):
        """找出数组中出现频率最高的k个元素"""
        # 统计频率
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        # 使用最小堆，按频率排序
        min_heap = []
        
        for num, freq in frequency_map.items():
            # 如果堆大小小于k，直接添加
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            # 如果当前元素频率大于堆顶，替换堆顶
            elif freq > min_heap[0][0]:
                heapq.heapreplace(min_heap, (freq, num))
        
        # 提取结果（频率从高到低）
        return [item[1] for item in sorted(min_heap, reverse=True)]
    
    # 生成测试数据（有些元素会重复）
    def generate_test_data(size=100, unique_count=20):
        base = list(range(1, unique_count + 1))
        # 确保某些元素更频繁出现
        data = []
        for i in range(unique_count):
            # 元素越小，出现频率越高
            count = (unique_count - i) * 2
            data.extend([base[i]] * count)
        # 随机打乱
        random.shuffle(data)
        # 截取指定大小
        return data[:size]
    
    # 测试
    nums = generate_test_data(100, 15)
    k = 3
    
    print(f"   数据样本: {nums[:20]}...")
    print(f"   寻找出现频率最高的{k}个元素")
    
    result = top_k_frequent_elements(nums, k)
    print(f"   结果: {result}")
    
    # 验证结果
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    
    print("   频率验证:")
    for num in result:
        print(f"   元素 {num}: 出现 {frequency_map[num]} 次")
    
    print("\n4. 实现Dijkstra最短路径算法")
    print("   使用优先队列高效实现图算法")
    
    def dijkstra(graph, start):
        """使用Dijkstra算法计算从起点到所有其他节点的最短路径"""
        # 初始化距离字典，所有节点距离设为无穷大
        distances = {node: float('infinity') for node in graph}
        distances[start] = 0
        
        # 使用优先队列（距离，节点）
        priority_queue = [(0, start)]
        
        # 已访问的节点
        visited = set()
        
        while priority_queue:
            # 获取当前距离最小的节点
            current_distance, current_node = heapq.heappop(priority_queue)
            
            # 如果节点已访问或当前距离大于已知距离，跳过
            if current_node in visited or current_distance > distances[current_node]:
                continue
            
            # 标记节点为已访问
            visited.add(current_node)
            
            # 更新相邻节点的距离
            for neighbor, weight in graph[current_node].items():
                distance = current_distance + weight
                
                # 如果找到更短的路径
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances
    
    # 创建一个测试图
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 5, 'D': 10},
        'C': {'A': 2, 'B': 5, 'D': 3},
        'D': {'B': 10, 'C': 3, 'E': 11},
        'E': {'D': 11}
    }
    
    print("   测试图结构:")
    for node, neighbors in graph.items():
        print(f"   {node} -> {neighbors}")
    
    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)
    
    print(f"   \n从节点 {start_node} 到各节点的最短路径:")
    for node, distance in shortest_paths.items():
        print(f"   到 {node}: 距离 = {distance}")
    
    print("\n5. 滑动窗口最大值")
    print("   使用堆实现滑动窗口最大值问题")
    
    def max_sliding_window(nums, k):
        """计算滑动窗口中的最大值"""
        result = []
        # 使用最大堆（通过负数值实现）
        max_heap = []
        
        for i, num in enumerate(nums):
            # 添加元素到堆，存储(-值, 索引)以实现最大堆
            heapq.heappush(max_heap, (-num, i))
            
            # 当堆大小至少为k时
            if i >= k - 1:
                # 移除不在当前窗口内的元素
                while max_heap[0][1] <= i - k:
                    heapq.heappop(max_heap)
                
                # 堆顶就是当前窗口的最大值
                result.append(-max_heap[0][0])
        
        return result
    
    # 测试数据
    nums = [random.randint(1, 100) for _ in range(20)]
    k = 3
    
    print(f"   数组: {nums}")
    print(f"   滑动窗口大小: {k}")
    
    result = max_sliding_window(nums, k)
    print(f"   滑动窗口最大值: {result}")
    
    # 验证结果
    print("   验证:")
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        manual_max = max(window)
        print(f"   窗口 {i}: {window} -> 最大值 = {manual_max}")
    
    print("\n6. 多阶段任务调度")
    print("   结合堆和贪心算法实现任务调度")
    
    def schedule_tasks(tasks, max_time_slots):
        """调度任务，每个任务有优先级和处理时间"""
        # 按优先级排序任务
        sorted_tasks = sorted(tasks, key=lambda x: x[0])  # 优先级升序
        
        # 当前时间
        current_time = 0
        # 进行中的任务堆（完成时间, 任务名）
        ongoing_tasks = []
        # 完成的任务
        completed_tasks = []
        
        # 任务索引
        task_index = 0
        
        while task_index < len(tasks) or ongoing_tasks:
            # 添加当前时间可用的所有高优先级任务
            while task_index < len(tasks) and sorted_tasks[task_index][0] <= current_time:
                priority, duration, task_name = sorted_tasks[task_index]
                # 计算完成时间
                completion_time = current_time + duration
                # 添加到进行中任务堆
                heapq.heappush(ongoing_tasks, (completion_time, task_name, duration))
                task_index += 1
            
            # 如果没有进行中的任务，直接跳到下一个任务的开始时间
            if not ongoing_tasks and task_index < len(tasks):
                current_time = sorted_tasks[task_index][0]
                continue
            
            # 处理完成时间最早的任务
            if ongoing_tasks:
                completion_time, task_name, duration = heapq.heappop(ongoing_tasks)
                current_time = completion_time
                completed_tasks.append((task_name, current_time - duration, current_time))
        
        return completed_tasks
    
    # 创建测试任务
    tasks = [
        (0, 3, '任务A'),  # (优先级, 持续时间, 任务名)
        (1, 2, '任务B'),
        (2, 4, '任务C'),
        (3, 1, '任务D'),
        (4, 5, '任务E')
    ]
    
    max_time_slots = 2  # 最多同时处理2个任务
    
    print("   任务列表:")
    for priority, duration, name in tasks:
        print(f"   {name}: 优先级={priority}, 持续时间={duration}")
    
    schedule = schedule_tasks(tasks, max_time_slots)
    
    print("   \n任务调度结果:")
    for name, start, end in schedule:
        print(f"   {name}: 开始时间={start}, 结束时间={end}")
    
    print("\n7. 堆在数据流处理中的应用")
    print("   使用堆维护动态数据流的统计信息")
    
    class DataStreamStatistics:
        def __init__(self):
            self.min_heap = []  # 存储较大的一半元素
            self.max_heap = []  # 存储较小的一半元素（使用负数值）
            self.count = 0
        
        def add_number(self, num):
            """添加一个新数字到数据流"""
            # 策略：保持 max_heap 中的元素数量等于或比 min_heap 多一个
            # max_heap 存储的是负值，以模拟最大堆
            
            # 先添加到合适的堆
            if not self.max_heap or num <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)  # 较小的一半
            else:
                heapq.heappush(self.min_heap, num)    # 较大的一半
            
            # 重新平衡两个堆
            if len(self.max_heap) > len(self.min_heap) + 1:
                # max_heap 太大，移动一个到 min_heap
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            elif len(self.min_heap) > len(self.max_heap):
                # min_heap 太大，移动一个到 max_heap
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            
            self.count += 1
        
        def get_median(self):
            """获取当前数据流的中位数"""
            if not self.max_heap:
                raise ValueError("数据流为空")
            
            if len(self.max_heap) > len(self.min_heap):
                # 奇数个元素，max_heap 多一个
                return -self.max_heap[0]
            else:
                # 偶数个元素，取两个堆顶的平均值
                return (-self.max_heap[0] + self.min_heap[0]) / 2
        
        def get_percentile(self, p):
            """获取p百分位数（近似值）"""
            if not 0 <= p <= 100:
                raise ValueError("百分位数必须在0到100之间")
            
            if not self.max_heap:
                raise ValueError("数据流为空")
            
            # 计算百分位数的位置
            index = int(self.count * p / 100)
            
            # 合并两个堆并排序来获取精确值（实际应用中可以优化）
            all_values = sorted(-x for x in self.max_heap) + sorted(self.min_heap)
            
            return all_values[index]
    
    # 测试数据流统计
    stats = DataStreamStatistics()
    
    # 添加随机数据
    data_stream = [random.randint(1, 1000) for _ in range(20)]
    
    print("   数据流: ", data_stream)
    
    # 逐个添加数据并计算中位数
    print("   \n动态计算中位数:")
    for i, num in enumerate(data_stream):
        stats.add_number(num)
        median = stats.get_median()
        percentile_50 = stats.get_percentile(50)
        print(f"   添加 {num} 后，中位数: {median}, 50百分位: {percentile_50}")
    
    # 计算最终的各种统计量
    print("   \n最终统计:")
    print(f"   数据数量: {stats.count}")
    print(f"   中位数: {stats.get_median()}")
    print(f"   25百分位: {stats.get_percentile(25)}")
    print(f"   75百分位: {stats.get_percentile(75)}")
    print(f"   90百分位: {stats.get_percentile(90)}")

# 运行高级应用示例
heapq_advanced_examples()
print()

# 6. 性能优化和注意事项
print("=== 6. 性能优化和注意事项 ===")

def heapq_performance_and_notes():
    """heapq模块的性能优化和注意事项"""
    import heapq
    import random
    import time
    import sys
    
    print("1. heapq性能特点")
    print("   - heappush和heappop操作的时间复杂度为O(log n)")
    print("   - heapify的时间复杂度为O(n)，比逐个插入更高效")
    print("   - nlargest和nsmallest在n较小的情况下效率高，当n接近数据大小m时，排序更高效")
    print()
    
    # 性能对比测试
    print("2. 性能对比测试")
    
    # 测试不同大小的数据
    sizes = [100, 1000, 10000]
    
    for size in sizes:
        print(f"   \n数据大小: {size}")
        data = [random.randint(1, 100000) for _ in range(size)]
        
        # 测试heapify vs 逐个heappush
        print("   heapify vs 逐个heappush:")
        
        # heapify
        data_copy1 = data.copy()
        start_time = time.time()
        heapq.heapify(data_copy1)
        heapify_time = time.time() - start_time
        
        # 逐个heappush
        data_copy2 = []
        start_time = time.time()
        for item in data:
            heapq.heappush(data_copy2, item)
        heappush_time = time.time() - start_time
        
        print(f"   heapify耗时: {heapify_time:.6f}秒")
        print(f"   逐个heappush耗时: {heappush_time:.6f}秒")
        print(f"   heapify速度提升: {(heappush_time / heapify_time):.2f}倍")
        
        # 测试nlargest vs 排序后切片
        print("   nlargest vs 排序后切片:")
        
        # 测试不同的k值
        k_values = [10, size//2, size-10]
        
        for k in k_values:
            k = min(k, size)  # 确保k不大于size
            
            # nlargest
            start_time = time.time()
            result1 = heapq.nlargest(k, data)
            nlargest_time = time.time() - start_time
            
            # 排序后切片
            start_time = time.time()
            result2 = sorted(data, reverse=True)[:k]
            sort_time = time.time() - start_time
            
            print(f"   k={k}:")
            print(f"     nlargest耗时: {nlargest_time:.6f}秒")
            print(f"     排序耗时: {sort_time:.6f}秒")
            
            # 确定哪种方法更快
            if nlargest_time < sort_time:
                print(f"     nlargest快{(sort_time / nlargest_time):.2f}倍")
            else:
                print(f"     排序快{(nlargest_time / sort_time):.2f}倍")
    
    print("\n3. 内存使用注意事项")
    
    # 测试内存使用
    def get_memory_usage(obj):
        """估算对象的内存使用量"""
        return sys.getsizeof(obj)
    
    print("   堆数据结构的内存占用:")
    
    # 创建不同大小的堆
    heap_sizes = [1000, 10000, 100000]
    
    for size in heap_sizes:
        heap = []
        for i in range(size):
            heapq.heappush(heap, i)
        
        memory = get_memory_usage(heap)
        print(f"   大小为{size}的堆: {memory}字节 ({memory/size:.2f}字节/元素)")
    
    print("\n4. 常见性能陷阱和优化建议")
    print("   陷阱1: 对已排序数据使用heappush逐个添加")
    print("   解决: 对已排序数据，使用heapify更高效")
    
    print("   \n陷阱2: 当n接近数据大小m时使用nlargest/mnsmallest")
    print("   解决: 当n > m/2时，使用排序然后切片的方式更高效")
    
    print("   \n陷阱3: 频繁的heappush和heappop操作没有批处理")
    print("   解决: 尽可能批量处理数据，减少堆操作次数")
    
    print("   \n陷阱4: 堆中存储复杂对象导致比较操作缓慢")
    print("   解决: 只在堆中存储必要的键值和索引，而不是整个对象")
    
    print("   \n陷阱5: 不适当的堆大小管理")
    print("   解决: 对于固定大小的优先队列，使用heapreplace或heappushpop避免堆过大")
    
    print("\n5. 多线程环境中的注意事项")
    print("   - heapq模块不是线程安全的")
    print("   - 在多线程环境中使用时，需要加锁保护")
    print("   - 可以使用threading.RLock来保护堆操作")
    print("   - 考虑使用queue.PriorityQueue作为线程安全的替代方案")
    
    print("\n6. 堆操作的最佳实践")
    print("   - 优先使用heapify而不是逐个heappush")
    print("   - 对于大n值，考虑直接排序而不是使用nlargest/nsmallest")
    print("   - 使用元组(优先级, 索引, 数据)来保证同优先级元素的稳定排序")
    print("   - 对于自定义比较，考虑使用包装器类或自定义键")
    print("   - 在处理大数据集时，考虑内存使用并实现批量处理")
    print("   - 对于需要最大堆的场景，可以通过取负值来实现")
    print("   - 对于固定大小的Top-N问题，维护一个大小为N的堆")

# 运行性能优化和注意事项
heapq_performance_and_notes()
print()

# 7. 输入输出示例
print("=== 7. 输入输出示例 ===")

def heapq_io_examples():
    """heapq模块的输入输出示例"""
    import heapq
    
    print("1. 基本堆操作示例")
    print("   输入:")
    print("   import heapq")
    print("   heap = []")
    print("   # 添加元素")
    print("   for i in [5, 3, 8, 1, 2]:")
    print("       heapq.heappush(heap, i)")
    print("   print('堆:', heap)")
    print("   # 弹出最小元素")
    print("   while heap:")
    print("       print('弹出:', heapq.heappop(heap))")
    print("   ")
    print("   输出:")
    
    # 执行上述代码
    heap = []
    for i in [5, 3, 8, 1, 2]:
        heapq.heappush(heap, i)
    print("   堆: [1, 2, 8, 5, 3]")  # 这是实际输出的堆结构
    
    print_heap = heap.copy()
    while print_heap:
        print(f"   弹出: {heapq.heappop(print_heap)}")
    
    print("\n2. 使用heapify示例")
    print("   输入:")
    print("   import heapq")
    print("   data = [5, 3, 8, 1, 2]")
    print("   heapq.heapify(data)")
    print("   print('堆:', data)")
    print("   ")
    print("   输出:")
    
    data = [5, 3, 8, 1, 2]
    heapq.heapify(data)
    print(f"   堆: {data}")
    
    print("\n3. nlargest和nsmallest示例")
    print("   输入:")
    print("   import heapq")
    print("   data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]")
    print("   largest = heapq.nlargest(3, data)")
    print("   smallest = heapq.nsmallest(3, data)")
    print("   print('最大的3个元素:', largest)")
    print("   print('最小的3个元素:', smallest)")
    print("   ")
    print("   输出:")
    
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    largest = heapq.nlargest(3, data)
    smallest = heapq.nsmallest(3, data)
    print(f"   最大的3个元素: {largest}")
    print(f"   最小的3个元素: {smallest}")
    
    print("\n4. 自定义对象排序示例")
    print("   输入:")
    print("   import heapq")
    print("   class Person:")
    print("       def __init__(self, name, age):")
    print("           self.name = name")
    print("           self.age = age")
    print("       def __repr__(self):")
    print("           return f'Person({self.name}, {self.age})'")
    print("   ")
    print("   people = [")
    print("       Person('Alice', 25),")
    print("       Person('Bob', 30),")
    print("       Person('Charlie', 20),")
    print("       Person('David', 35)")
    print("   ]")
    print("   ")
    print("   # 方法1：使用元组")
    print("   heap = []")
    print("   for person in people:")
    print("       heapq.heappush(heap, (person.age, person.name, person))")
    print("   ")
    print("   # 方法2：使用key参数")
    print("   youngest = heapq.nsmallest(2, people, key=lambda x: x.age)")
    print("   print('最年轻的2个人:', youngest)")
    print("   ")
    print("   输出:")
    
    # 定义Person类
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __repr__(self):
            return f'Person({self.name}, {self.age})'
    
    people = [
        Person('Alice', 25),
        Person('Bob', 30),
        Person('Charlie', 20),
        Person('David', 35)
    ]
    
    youngest = heapq.nsmallest(2, people, key=lambda x: x.age)
    print(f"   最年轻的2个人: {youngest}")
    
    print("\n5. 优先队列完整示例")
    print("   输入:")
    print("   import heapq")
    print("   class PriorityQueue:")
    print("       def __init__(self):")
    print("           self._queue = []")
    print("           self._index = 0")
    print("       ")
    print("       def push(self, item, priority=0):")
    print("           heapq.heappush(self._queue, (priority, self._index, item))")
    print("           self._index += 1")
    print("       ")
    print("       def pop(self):")
    print("           return heapq.heappop(self._queue)[-1]")
    print("   ")
    print("   # 使用优先队列")
    print("   pq = PriorityQueue()")
    print("   pq.push('编写报告', 3)")
    print("   pq.push('参加会议', 1)")
    print("   pq.push('紧急任务', 0)")
    print("   ")
    print("   print('按优先级处理任务:')")
    print("   while True:")
    print("       try:")
    print("           task = pq.pop()")
    print("           print(f'- {task}')")
    print("       except IndexError:")
    print("           break")
    print("   ")
    print("   输出:")
    print("   按优先级处理任务:")
    print("   - 紧急任务")
    print("   - 参加会议")
    print("   - 编写报告")

# 运行输入输出示例
heapq_io_examples()
print()

# 8. 总结和导入指南
print("=== 8. 总结和导入指南 ===")

def heapq_summary():
    """heapq模块总结和导入指南"""
    print("1. heapq模块核心功能总结")
    print("   - 提供堆队列算法的高效实现，主要是最小堆")
    print("   - 支持基本堆操作：heappush、heappop、heapify")
    print("   - 提供高级操作：heappushpop、heapreplace、nlargest、nsmallest")
    print("   - 适用于优先队列、排序算法和图算法等场景")
    print()
    
    print("2. heapq模块使用场景")
    print("   - 任务调度系统中的优先级处理")
    print("   - 寻找Top N元素或第K大/小元素")
    print("   - 实现高效的排序算法（堆排序）")
    print("   - 图算法中的最短路径计算（Dijkstra算法）")
    print("   - 数据流的统计分析和动态维护")
    print("   - 合并多个有序序列")
    print()
    
    print("3. 完整导入指南")
    print("   基本导入:")
    print("   import heapq")
    print()
    
    print("   特定函数导入:")
    print("   from heapq import heappush, heappop, heapify, nlargest, nsmallest")
    print()
    
    print("   常用导入组合:")
    print("   from heapq import (")
    print("       heappush, heappop, heapify,       # 基本操作")
    print("       heappushpop, heapreplace,         # 组合操作")
    print("       nlargest, nsmallest               # 选择操作")
    print("   )")
    print()
    
    print("4. 版本兼容性")
    print("   - heapq模块在Python 2.3及以上版本中可用")
    print("   - 所有核心函数在Python 3.x版本中保持稳定")
    print("   - Python 3.7+中，nlargest和nsmallest函数在性能上有所优化")
    print()
    
    print("5. 最佳实践和建议")
    print("   - 对于已知数据，优先使用heapify而不是逐个heappush")
    print("   - 使用元组(优先级, 索引, 数据)来保证同优先级元素的FIFO顺序")
    print("   - 对于需要最大堆的场景，可以通过存储负值来实现")
    print("   - 当n接近数据大小时，考虑使用排序而不是nlargest/nsmallest")
    print("   - 在多线程环境中，记得加锁保护堆操作")
    print("   - 对于自定义对象的排序，使用合适的键或比较方法")
    print("   - 实现优先队列时，考虑使用专门的类来封装堆操作")
    print()
    
    print("6. 相关模块和扩展")
    print("   - queue.PriorityQueue: 线程安全的优先队列实现")
    print("   - collections.defaultdict: 结合使用可实现更复杂的优先级逻辑")
    print("   - operator模块: 与heapq配合实现高级排序和比较")
    print("   - concurrent.futures: 在并发环境中结合堆使用")
    print()
    
    print("7. 关键性能考虑")
    print("   - 堆操作的时间复杂度: O(log n)")
    print("   - heapify的时间复杂度: O(n)")
    print("   - nlargest/nsmallest的时间复杂度: O(m log n)，其中m是数据量")
    print("   - 空间复杂度: O(n)，需要存储堆中的所有元素")
    print()
    
    print("8. 运行此文件的完整指南")
    print("   - 确保您的环境中安装了Python 3.6或更高版本")
    print("   - 直接运行此Python文件: python heapq模块.py")
    print("   - 查看输出以了解heapq模块的各种功能和用例")
    print("   - 可以修改示例代码以测试不同的场景和参数")
    print()
    
    print("heapq模块是Python标准库中处理优先队列和堆排序的强大工具，通过本指南的学习，")
    print("您应该能够掌握其核心功能并在实际项目中灵活应用。")

# 运行总结
try:
    heapq_summary()
except Exception as e:
    print(f"运行总结时出错: {e}")

print("\n=== heapq模块学习完成 ===")
print("通过本文件，您已学习了Python heapq模块的完整功能和最佳实践。")
print("继续学习其他Python标准库模块，提升您的编程技能！")
