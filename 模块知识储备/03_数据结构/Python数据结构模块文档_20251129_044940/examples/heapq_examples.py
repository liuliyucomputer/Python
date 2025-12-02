#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
heapq模块示例代码集合

本文件演示了Python heapq模块的各种实用功能，
包括堆操作、优先队列实现、Top-K问题解决等。

作者: Python数据结构教程
日期: 2023-11-28
"""

import heapq
import random
import time
from pprint import pprint


def example_basic_heap_operations():
    """示例1: 基本堆操作"""
    print("=== 示例1: 基本堆操作 ===")
    
    # 创建一个空列表作为堆
    heap = []
    
    # 插入元素（堆化）
    print("插入元素: 10, 5, 3, 8, 7")
    heapq.heappush(heap, 10)
    heapq.heappush(heap, 5)
    heapq.heappush(heap, 3)
    heapq.heappush(heap, 8)
    heapq.heappush(heap, 7)
    
    print(f"堆的内容: {heap}")  # 注意：堆是一个特殊的列表结构，而不是有序列表
    print(f"堆的最小元素: {heap[0]}")
    
    # 弹出最小元素
    print("\n依次弹出最小元素:")
    while heap:
        smallest = heapq.heappop(heap)
        print(f"弹出: {smallest}, 剩余堆: {heap}")
    
    # 从现有列表创建堆（原地堆化）
    print("\n从现有列表创建堆:")
    data = [10, 5, 3, 8, 7]
    print(f"原始数据: {data}")
    heapq.heapify(data)
    print(f"堆化后: {data}")
    print()


def example_max_heap():
    """示例2: 最大堆的实现"""
    print("=== 示例2: 最大堆的实现 ===")
    
    # 方法1: 使用负数实现最大堆
    print("方法1: 使用负数实现最大堆")
    data = [10, 5, 3, 8, 7]
    max_heap = [-x for x in data]  # 存储负数
    heapq.heapify(max_heap)
    
    print(f"最大堆（存储负数）: {max_heap}")
    print(f"最大元素: {-max_heap[0]}")  # 取相反数得到最大值
    
    # 弹出最大元素
    print("\n依次弹出最大元素:")
    while max_heap:
        largest = -heapq.heappop(max_heap)  # 取相反数
        print(f"弹出: {largest}")
    
    # 方法2: 使用自定义比较器（通过包装元素）
    print("\n方法2: 使用自定义包装类实现最大堆")
    
    class MaxHeapElement:
        def __init__(self, value):
            self.value = value
        def __lt__(self, other):
            # 重写小于运算符，实现最大堆
            return self.value > other.value
        def __repr__(self):
            return str(self.value)
    
    max_heap = [MaxHeapElement(x) for x in data]
    heapq.heapify(max_heap)
    
    print(f"最大堆（自定义类）: {max_heap}")
    print(f"最大元素: {max_heap[0].value}")
    
    print("\n依次弹出最大元素:")
    while max_heap:
        largest = heapq.heappop(max_heap).value
        print(f"弹出: {largest}")
    print()


def example_priority_queue():
    """示例3: 优先队列实现"""
    print("=== 示例3: 优先队列实现 ===")
    
    # 简单的优先队列实现
    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0  # 用于在优先级相同时保持插入顺序
        
        def push(self, item, priority):
            # 使用负优先级来实现最大堆
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1
        
        def pop(self):
            if self._queue:
                return heapq.heappop(self._queue)[-1]
            raise IndexError("队列为空")
        
        def is_empty(self):
            return len(self._queue) == 0
        
        def size(self):
            return len(self._queue)
        
        def peek(self):
            """查看最高优先级的元素但不移除"""
            if self._queue:
                return self._queue[0][-1]
            return None
    
    # 测试优先队列
    pq = PriorityQueue()
    
    # 添加任务
    pq.push("编写报告", 3)
    pq.push("回复邮件", 1)
    pq.push("参加会议", 2)
    pq.push("紧急修复", 5)
    pq.push("整理文档", 2)
    
    print(f"队列大小: {pq.size()}")
    print(f"最高优先级任务: {pq.peek()}")
    
    # 按优先级处理任务
    print("\n按优先级处理任务:")
    while not pq.is_empty():
        task = pq.pop()
        print(f"处理: {task}")
    print()


def example_top_k():
    """示例4: Top-K问题解决"""
    print("=== 示例4: Top-K问题解决 ===")
    
    # 生成大量随机数据
    data = [random.randint(1, 10000) for _ in range(1000)]
    print(f"生成了{len(data)}个随机数")
    
    # 方法1: 排序后取前K个
    k = 10
    print(f"\n方法1: 获取最大的{k}个数（排序法）")
    
    start = time.time()
    sorted_data = sorted(data, reverse=True)
    top_k_sorted = sorted_data[:k]
    sort_time = time.time() - start
    
    print(f"最大的{k}个数: {sorted(top_k_sorted, reverse=True)}")
    print(f"排序法耗时: {sort_time:.6f}秒")
    
    # 方法2: 使用heapq.nlargest
    print(f"\n方法2: 获取最大的{k}个数（heapq.nlargest）")
    
    start = time.time()
    top_k_heapq = heapq.nlargest(k, data)
    heapq_time = time.time() - start
    
    print(f"最大的{k}个数: {sorted(top_k_heapq, reverse=True)}")
    print(f"heapq.nlargest耗时: {heapq_time:.6f}秒")
    
    # 方法3: 手动维护一个大小为K的小顶堆
    print(f"\n方法3: 获取最大的{k}个数（手动维护小顶堆）")
    
    start = time.time()
    min_heap = []
    
    # 先将前K个元素加入堆
    for i in range(min(k, len(data))):
        heapq.heappush(min_heap, data[i])
    
    # 遍历剩余元素
    for i in range(k, len(data)):
        if data[i] > min_heap[0]:  # 如果当前元素大于堆顶（最小值）
            heapq.heappushpop(min_heap, data[i])  # 弹出堆顶，加入新元素
    
    manual_time = time.time() - start
    top_k_manual = sorted(min_heap, reverse=True)
    
    print(f"最大的{k}个数: {top_k_manual}")
    print(f"手动堆化耗时: {manual_time:.6f}秒")
    
    # 验证结果
    print(f"\n结果验证: {sorted(top_k_sorted) == sorted(top_k_heapq) == sorted(min_heap)}")
    
    # 获取最小的K个数
    print(f"\n获取最小的{k}个数:")
    bottom_k = heapq.nsmallest(k, data)
    print(f"最小的{k}个数: {sorted(bottom_k)}")
    print()


def example_merge_sorted_lists():
    """示例5: 合并多个有序列表"""
    print("=== 示例5: 合并多个有序列表 ===")
    
    # 创建几个有序列表
    list1 = [1, 4, 7, 10]
    list2 = [2, 5, 8, 11]
    list3 = [3, 6, 9, 12]
    
    print(f"列表1: {list1}")
    print(f"列表2: {list2}")
    print(f"列表3: {list3}")
    
    # 使用heapq.merge合并
    merged = list(heapq.merge(list1, list2, list3))
    print(f"\n合并结果: {merged}")
    
    # 应用：归并排序
    print("\n应用: 归并排序实现")
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        # 分割数组
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        
        # 合并两个有序数组
        return list(heapq.merge(left, right))
    
    # 测试归并排序
    test_arr = [5, 2, 9, 1, 5, 6]
    sorted_arr = merge_sort(test_arr)
    print(f"原数组: {test_arr}")
    print(f"排序后: {sorted_arr}")
    print()


def example_task_scheduling():
    """示例6: 任务调度系统"""
    print("=== 示例6: 任务调度系统 ===")
    
    class Task:
        def __init__(self, name, priority, due_time):
            self.name = name
            self.priority = priority  # 数值越小，优先级越高
            self.due_time = due_time  # 截止时间戳
        
        def __lt__(self, other):
            # 首先按优先级排序，相同优先级按截止时间排序
            if self.priority != other.priority:
                return self.priority < other.priority
            return self.due_time < other.due_time
        
        def __repr__(self):
            return f"Task({self.name}, priority={self.priority}, due={self.due_time:.1f})"
    
    class TaskScheduler:
        def __init__(self):
            self._tasks = []
        
        def add_task(self, task):
            heapq.heappush(self._tasks, task)
        
        def get_next_task(self):
            if self._tasks:
                return heapq.heappop(self._tasks)
            return None
        
        def has_tasks(self):
            return len(self._tasks) > 0
        
        def task_count(self):
            return len(self._tasks)
    
    # 创建调度器
    scheduler = TaskScheduler()
    
    # 创建任务（模拟当前时间为100）
    current_time = 100
    tasks = [
        Task("紧急修复", 1, current_time + 5),
        Task("周报", 3, current_time + 60),
        Task("客户会议", 2, current_time + 15),
        Task("代码审查", 2, current_time + 30),
        Task("系统更新", 1, current_time + 10)
    ]
    
    # 添加任务到调度器
    for task in tasks:
        scheduler.add_task(task)
    
    print(f"调度器中有{scheduler.task_count()}个任务")
    print("\n任务执行顺序:")
    
    # 执行任务
    while scheduler.has_tasks():
        next_task = scheduler.get_next_task()
        # 计算剩余时间
        time_remaining = next_task.due_time - current_time
        print(f"执行: {next_task}, 剩余时间: {time_remaining:.1f}秒")
        # 模拟任务执行
        current_time += 2  # 假设每个任务需要2秒执行
    print()


def example_event_simulator():
    """示例7: 事件模拟器"""
    print("=== 示例7: 事件模拟器 ===")
    
    class Event:
        def __init__(self, event_time, event_type, data=None):
            self.event_time = event_time
            self.event_type = event_type
            self.data = data
        
        def __lt__(self, other):
            return self.event_time < other.event_time
        
        def __repr__(self):
            return f"Event(time={self.event_time:.2f}, type={self.event_type}, data={self.data})"
    
    class EventSimulator:
        def __init__(self):
            self._event_queue = []
            self._current_time = 0.0
        
        def schedule_event(self, delay, event_type, data=None):
            """安排一个事件在指定延迟后发生"""
            event_time = self._current_time + delay
            event = Event(event_time, event_type, data)
            heapq.heappush(self._event_queue, event)
            return event
        
        def run(self):
            """运行模拟器"""
            print(f"开始模拟，初始时间: {self._current_time:.2f}")
            
            while self._event_queue:
                # 获取下一个事件
                next_event = heapq.heappop(self._event_queue)
                # 更新当前时间
                self._current_time = next_event.event_time
                # 处理事件
                self._process_event(next_event)
            
            print(f"模拟结束，最终时间: {self._current_time:.2f}")
        
        def _process_event(self, event):
            """处理单个事件"""
            print(f"时间 {event.event_time:.2f}: 处理 {event.event_type} 事件, 数据: {event.data}")
            
            # 根据事件类型生成新事件
            if event.event_type == "customer_arrival":
                # 客户到达，安排服务事件
                service_time = random.uniform(1.0, 3.0)  # 服务时间1-3秒
                self.schedule_event(service_time, "service_completed", event.data)
                # 安排下一个客户到达
                next_arrival = random.expovariate(1/5)  # 指数分布，平均间隔5秒
                self.schedule_event(next_arrival, "customer_arrival", f"客户{random.randint(100, 999)}")
    
    # 创建模拟器
    simulator = EventSimulator()
    
    # 安排初始事件
    simulator.schedule_event(0, "customer_arrival", "客户001")
    simulator.schedule_event(20, "simulation_end", None)  # 20秒后结束模拟
    
    # 运行模拟
    simulator.run()
    print()


def example_median_maintenance():
    """示例8: 中位数维护"""
    print("=== 示例8: 中位数维护 ===")
    
    # 使用两个堆来维护中位数
    # max_heap存储较小的一半元素（使用负数实现最大堆）
    # min_heap存储较大的一半元素
    max_heap = []  # 存储较小的一半元素
    min_heap = []  # 存储较大的一半元素
    medians = []  # 存储每次添加元素后的中位数
    
    # 测试数据
    test_data = [12, 4, 5, 3, 8, 7]
    print(f"输入数据: {test_data}")
    
    for num in test_data:
        # 策略：保持 max_heap.size() >= min_heap.size()
        # 所有元素先加入max_heap，然后将max_heap的最大元素移到min_heap
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)  # 注意取负数
        else:
            heapq.heappush(min_heap, num)
        
        # 平衡两个堆的大小
        if len(max_heap) > len(min_heap) + 1:
            # max_heap太大，移动最大元素到min_heap
            largest = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, largest)
        elif len(min_heap) > len(max_heap):
            # min_heap太大，移动最小元素到max_heap
            smallest = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -smallest)
        
        # 计算中位数
        if len(max_heap) > len(min_heap):
            median = -max_heap[0]  # max_heap多一个元素，中位数就是max_heap的最大值
        else:
            median = (-max_heap[0] + min_heap[0]) / 2  # 两个堆大小相等，取平均值
        
        medians.append(median)
        
        # 打印当前状态
        current_max_heap = [-x for x in max_heap]  # 转回正数显示
        print(f"添加 {num} 后:")
        print(f"  较小一半: {sorted(current_max_heap)}")
        print(f"  较大一半: {sorted(min_heap)}")
        print(f"  当前中位数: {median}")
    
    print(f"\n所有中位数: {medians}")
    print()


def example_performance_comparison():
    """示例9: 性能比较"""
    print("=== 示例9: 性能比较 ===")
    
    # 生成大数据集
    n = 1000000
    data = [random.randint(1, 1000000) for _ in range(n)]
    k = 100
    
    # 测试1: 排序 vs heapq.nlargest
    print(f"测试1: 排序 vs heapq.nlargest (n={n}, k={k})")
    
    # 排序方法
    start = time.time()
    sorted_data = sorted(data, reverse=True)
    top_k_sorted = sorted_data[:k]
    sort_time = time.time() - start
    print(f"  排序法: {sort_time:.6f}秒")
    
    # heapq.nlargest方法
    start = time.time()
    top_k_heapq = heapq.nlargest(k, data)
    heapq_time = time.time() - start
    print(f"  heapq.nlargest: {heapq_time:.6f}秒")
    
    # 当k远小于n时，heapq应该更高效
    print(f"  heapq加速比: {sort_time / heapq_time:.2f}倍")
    
    # 测试2: 堆插入 vs 列表排序插入
    print(f"\n测试2: 堆插入 vs 列表排序插入")
    
    # 堆插入
    start = time.time()
    heap = []
    for num in data[:10000]:  # 使用较小的子集进行测试
        heapq.heappush(heap, num)
    heap_time = time.time() - start
    print(f"  堆插入10,000个元素: {heap_time:.6f}秒")
    
    # 列表排序插入（保持列表有序）
    start = time.time()
    sorted_list = []
    for num in data[:10000]:
        # 找到插入位置（二分查找）
        import bisect
        bisect.insort(sorted_list, num)
    list_time = time.time() - start
    print(f"  列表排序插入10,000个元素: {list_time:.6f}秒")
    print(f"  堆插入加速比: {list_time / heap_time:.2f}倍")
    print()


def example_huffman_coding():
    """示例10: 哈夫曼编码实现"""
    print("=== 示例10: 哈夫曼编码实现 ===")
    
    class Node:
        def __init__(self, char, freq):
            self.char = char  # 字符，None表示内部节点
            self.freq = freq  # 频率
            self.left = None  # 左子节点
            self.right = None  # 右子节点
        
        def __lt__(self, other):
            # 按频率排序
            return self.freq < other.freq
        
        def __repr__(self):
            return f"Node({self.char}, {self.freq})"
    
    def build_huffman_tree(text):
        """构建哈夫曼树"""
        # 计算字符频率
        from collections import Counter
        freq_counter = Counter(text)
        
        # 创建叶节点堆
        priority_queue = []
        for char, freq in freq_counter.items():
            heapq.heappush(priority_queue, Node(char, freq))
        
        # 构建哈夫曼树
        while len(priority_queue) > 1:
            # 取出两个频率最小的节点
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)
            
            # 创建新的内部节点，频率为两个子节点之和
            internal = Node(None, left.freq + right.freq)
            internal.left = left
            internal.right = right
            
            # 将内部节点加入堆
            heapq.heappush(priority_queue, internal)
        
        # 返回根节点
        return heapq.heappop(priority_queue) if priority_queue else None
    
    def generate_codes(node, current_code="", codes={}):
        """生成哈夫曼编码"""
        if node is None:
            return
        
        # 如果是叶节点，保存编码
        if node.char is not None:
            codes[node.char] = current_code if current_code else "0"  # 处理单个字符的情况
            return
        
        # 递归处理左右子树
        generate_codes(node.left, current_code + "0", codes)
        generate_codes(node.right, current_code + "1", codes)
        
        return codes
    
    def huffman_encode(text, codes):
        """使用哈夫曼编码压缩文本"""
        return "".join(codes[char] for char in text)
    
    def huffman_decode(encoded, root):
        """解码哈夫曼编码"""
        if not root:
            return ""
        
        result = []
        current = root
        
        for bit in encoded:
            # 0表示左，1表示右
            if bit == "0":
                current = current.left
            else:
                current = current.right
            
            # 如果到达叶节点
            if current.char is not None:
                result.append(current.char)
                current = root  # 重置到根节点
        
        return "".join(result)
    
    # 测试哈夫曼编码
    test_text = "this is an example for huffman encoding"
    print(f"原始文本: {test_text}")
    print(f"原始长度: {len(test_text) * 8} 位")  # 假设每个字符8位
    
    # 构建哈夫曼树
    huffman_tree = build_huffman_tree(test_text)
    
    # 生成编码
    codes = generate_codes(huffman_tree)
    print(f"\n哈夫曼编码表:")
    for char, code in sorted(codes.items()):
        print(f"  '{char}': {code}")
    
    # 编码文本
    encoded = huffman_encode(test_text, codes)
    print(f"\n编码结果: {encoded}")
    print(f"编码长度: {len(encoded)} 位")
    
    # 计算压缩率
    compression_ratio = (len(test_text) * 8) / len(encoded)
    print(f"压缩率: {compression_ratio:.2f}倍")
    
    # 解码验证
    decoded = huffman_decode(encoded, huffman_tree)
    print(f"\n解码结果: {decoded}")
    print(f"解码正确: {test_text == decoded}")


if __name__ == "__main__":
    print("Python heapq 模块示例代码\n")
    
    # 运行所有示例
    example_basic_heap_operations()
    example_max_heap()
    example_priority_queue()
    example_top_k()
    example_merge_sorted_lists()
    example_task_scheduling()
    example_event_simulator()  # 模拟事件，输出可能有所不同
    example_median_maintenance()
    
    # 性能测试（可选，可能需要一些时间）
    # example_performance_comparison()
    
    # 高级应用示例
    example_huffman_coding()
    
    print("\n所有示例执行完成！")
