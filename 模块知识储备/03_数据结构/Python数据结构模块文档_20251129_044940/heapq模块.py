"""
此文件是Python模块的学习文档，包含Markdown格式和代码示例。
请使用文本编辑器或Markdown查看器打开以获得最佳阅读体验。
"""

# heapq模块 - Python堆队列算法实现

## 1. 核心功能与概述

"heapq"模块实现了堆队列算法(也称为优先队列算法).堆是一种特殊的树形数据结构,它满足堆属性:父节点的值总是小于或等于(对于最小堆)或大于或等于(对于最大堆)其子节点的值.Python的"heapq"模块默认实现的是最小堆.

### 主要功能:
- 创建和管理堆结构
- 实现优先队列操作
- 高效地获取最小元素
- 支持堆排序
- 合并多个有序序列

### 应用场景:
- 优先队列实现
- 堆排序算法
- 任务调度系统
- 图算法(如Dijkstra算法)
- 数据流中的top-k问题
- 内存受限的排序操作

## 2. 基本使用方法

### 2.1 创建堆

Python的"heapq"模块不提供单独的堆类,而是通过函数来操作普通的列表,使其满足堆属性.

```python
import heapq

# 方法1:使用heapify将现有列表转换为堆
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5]
heapq.heapify(nums)  # 将列表原地转换为堆
print(f"转换后的堆: {nums}")  # 输出: [1, 1, 2, 6, 5, 9, 4, 3, 5]

# 方法2:使用heappush逐个添加元素
heap = []
for num in [3, 1, 4, 1, 5]:
    heapq.heappush(heap, num)
print(f"添加元素后的堆: {heap}")  # 输出: [1, 1, 4, 3, 5]
```

### 2.2 访问和移除堆元素

```python
import heapq

# 创建一个堆
heap = [1, 1, 2, 6, 5, 9, 4, 3, 5]  # 已经是堆结构

# 获取最小元素但不移除
min_val = heap[0]
print(f"最小元素: {min_val}")  # 输出: 1

# 移除并返回最小元素
pop_val = heapq.heappop(heap)
print(f"弹出的最小元素: {pop_val}")  # 输出: 1
print(f"弹出后的堆: {heap}")  # 输出: [1, 3, 2, 5, 5, 9, 4, 6]

# 添加元素后立即弹出最小元素
# 这比先heappush再heappop更高效
replace_val = heapq.heappushpop(heap, 0)
print(f"替换后的弹出值: {replace_val}")  # 输出: 0
print(f"操作后的堆: {heap}")  # 堆结构保持不变

# 先弹出最小元素,再添加新元素
# 如果新元素可能是最小的,这比heappushpop更高效
smallest = heapq.heapreplace(heap, -1)
print(f"替换前的最小元素: {smallest}")  # 输出: 1
print(f"最终堆: {heap}")  # 堆结构保持不变
```

### 2.3 获取n个最大/最小元素

```python
import heapq

# 测试数据
scores = [50, 75, 90, 65, 80, 95, 60, 85]

# 获取3个最小元素
smallest_3 = heapq.nsmallest(3, scores)
print(f"三个最小分数: {smallest_3}")  # 输出: [50, 60, 65]

# 获取3个最大元素
largest_3 = heapq.nlargest(3, scores)
print(f"三个最大分数: {largest_3}")  # 输出: [95, 90, 85]

# 可以指定key参数进行复杂对象排序
students = [
    {"name": "Alice", "score": 90},
    {"name": "Bob", "score": 85},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 80}
]

# 获取2个成绩最高的学生
top_students = heapq.nlargest(2, students, key=lambda x: x["score"])
print(f"成绩最高的两名学生: {top_students}")

# 获取2个成绩最低的学生
bottom_students = heapq.nsmallest(2, students, key=lambda x: x["score"])
print(f"成绩最低的两名学生: {bottom_students}")
```

### 2.4 合并多个有序序列

```python
import heapq

# 两个有序列表
list1 = [1, 4, 7, 10]
list2 = [2, 5, 8, 11]
list3 = [3, 6, 9, 12]

# 合并为一个有序列表
merged = list(heapq.merge(list1, list2, list3))
print(f"合并后的有序列表: {merged}")
# 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# 注意:输入列表必须是已排序的
unsorted_list = [10, 2, 8, 5]
# 以下将产生错误的结果,因为unsorted_list未排序
wrong_merge = list(heapq.merge(list1, unsorted_list))
print(f"错误合并结果: {wrong_merge}")

# 正确的做法是先排序
unsorted_list.sort()
correct_merge = list(heapq.merge(list1, unsorted_list))
print(f"正确合并结果: {correct_merge}")

# heapq.merge是惰性的,适合处理大文件
# 示例:合并多个已排序文件
def merge_sorted_files(file_paths, output_path):
    # 打开所有文件
    files = [open(path, 'r') for path in file_paths]
    
    try:
        # 使用生成器读取每一行并转换为整数
        def file_to_gen(file_obj):
            for line in file_obj:
                yield int(line.strip())
        
        # 创建所有文件的生成器
        file_generators = [file_to_gen(f) for f in files]
        
        # 合并并写入输出文件
        with open(output_path, 'w') as out_file:
            for num in heapq.merge(*file_generators):
                out_file.write(f"{num}\n")
    finally:
        # 确保所有文件都被关闭
        for f in files:
            f.close()
```

## 3. 高级用法

### 3.1 自定义比较器与优先级

由于Python的"heapq"只支持最小堆,但我们可以通过一些技巧实现最大堆或自定义优先级.

```python
import heapq

# 方法1:使用负号实现最大堆
nums = [3, 1, 4, 1, 5, 9]
max_heap = [-num for num in nums]  # 存储负数
heapq.heapify(max_heap)

# 获取最大元素
max_num = -heapq.heappop(max_heap)
print(f"最大元素: {max_num}")  # 输出: 9

# 方法2:使用元组自定义优先级
# 元组比较时会先比较第一个元素,再比较第二个
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # 用于同优先级元素的稳定排序
    
    def push(self, item, priority):
        # 低优先级数字表示高优先级任务
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]
    
    def is_empty(self):
        return len(self._queue) == 0

# 测试自定义优先队列
pq = PriorityQueue()
pq.push("write code", 1)    # 低优先级
pq.push("debug code", 3)   # 高优先级
pq.push("fix bug", 2)      # 中优先级
pq.push("test code", 3)    # 高优先级

# 按优先级弹出任务
while not pq.is_empty():
    print(f"处理任务: {pq.pop()}")
# 输出顺序应该是:debug code, test code, fix bug, write code
```

### 3.2 实现堆排序

```python
import heapq

def heapsort(iterable):
    """使用heapq实现堆排序"""
    h = []
    # 构建堆
    for value in iterable:
        heapq.heappush(h, value)
    # 依次弹出最小元素,得到排序后的列表
    return [heapq.heappop(h) for _ in range(len(h))]

# 测试堆排序
unsorted = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = heapsort(unsorted)
print(f"排序前: {unsorted}")
print(f"排序后: {sorted_list}")

# 与Python内置排序比较
python_sorted = sorted(unsorted)
print(f"是否与内置排序一致: {sorted_list == python_sorted}")

# 注意:对于小数据集,Python内置的sorted函数通常更快
# heapq实现的堆排序主要用于理解算法或特殊场景
```

### 3.3 多线程安全的优先队列

在多线程环境中使用堆时,需要添加适当的锁机制以确保线程安全.

```python
import heapq
import threading
import time
import random
from queue import Empty

class ThreadSafePriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        self._lock = threading.Lock()
    
    def put(self, item, priority):
        """添加元素到队列"""
        with self._lock:
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1
    
    def get(self, block=True, timeout=None):
        """从队列中获取元素"""
        if block:
            # 如果需要阻塞等待,使用条件变量
            end_time = time.time() + (timeout or 0)
            while True:
                with self._lock:
                    if self._queue:
                        return heapq.heappop(self._queue)[-1]
                
                remaining = end_time - time.time() if timeout else None
                if remaining is not None and remaining <= 0:
                    raise Empty("队列为空且超时")
                time.sleep(0.01)  # 短暂睡眠避免CPU占用过高
        else:
            # 非阻塞模式
            with self._lock:
                if self._queue:
                    return heapq.heappop(self._queue)[-1]
                else:
                    raise Empty("队列为空")
    
    def qsize(self):
        """返回队列大小"""
        with self._lock:
            return len(self._queue)
    
    def empty(self):
        """检查队列是否为空"""
        return self.qsize() == 0

# 测试多线程优先队列
def producer(queue, count):
    """生产者:添加任务到队列"""
    for i in range(count):
        priority = random.randint(1, 5)
        task = f"Task-{i} (Priority-{priority})"
        queue.put(task, priority)
        print(f"生产者添加: {task}")
        time.sleep(random.uniform(0.01, 0.1))

def consumer(queue, name, count):
    """消费者:从队列中获取任务"""
    tasks_processed = 0
    while tasks_processed < count:
        try:
            task = queue.get(block=True, timeout=1.0)
            print(f"消费者{name}处理: {task}")
            tasks_processed += 1
            # 模拟处理时间
            time.sleep(random.uniform(0.05, 0.2))
        except Empty:
            print(f"消费者{name}等待超时")
            continue

# 运行多线程测试
print("\n多线程安全优先队列测试:")
thread_queue = ThreadSafePriorityQueue()

# 创建生产者和消费者线程
producer_thread = threading.Thread(target=producer, args=(thread_queue, 10))
consumer1_thread = threading.Thread(target=consumer, args=(thread_queue, "A", 5))
consumer2_thread = threading.Thread(target=consumer, args=(thread_queue, "B", 5))

# 启动线程
producer_thread.start()
consumer1_thread.start()
consumer2_thread.start()

# 等待所有线程完成
producer_thread.join()
consumer1_thread.join()
consumer2_thread.join()

print("\n所有任务处理完成")
```

### 3.4 使用heapq实现优先级队列的各种变体

#### 3.4.1 带过期时间的优先队列

```python
import heapq
import time

class TimedPriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority, expiry=None):
        """添加元素,可选择设置过期时间"""
        # 计算过期时间戳
        expiry_time = time.time() + expiry if expiry is not None else float('inf')
        heapq.heappush(self._queue, (-priority, expiry_time, self._index, item))
        self._index += 1
    
    def pop(self, now=None):
        """获取未过期的最高优先级元素"""
        if now is None:
            now = time.time()
        
        # 移除所有过期元素
        while self._queue and self._queue[0][1] < now:
            heapq.heappop(self._queue)
        
        # 返回最高优先级的未过期元素
        if self._queue:
            return heapq.heappop(self._queue)[-1]
        return None
    
    def clean_expired(self, now=None):
        """清理所有过期元素"""
        if now is None:
            now = time.time()
        
        while self._queue and self._queue[0][1] < now:
            heapq.heappop(self._queue)
    
    def is_empty(self):
        """检查队列是否为空(考虑过期元素)"""
        self.clean_expired()
        return len(self._queue) == 0

# 测试带过期时间的优先队列
print("\n带过期时间的优先队列测试:")
timed_queue = TimedPriorityQueue()

# 添加任务,有些设置过期时间
timed_queue.push("紧急任务1", priority=5)
timed_queue.push("限时任务1", priority=4, expiry=2)  # 2秒后过期
timed_queue.push("普通任务1", priority=3)
timed_queue.push("限时任务2", priority=5, expiry=1)  # 1秒后过期

# 立即获取一个任务
print(f"立即获取: {timed_queue.pop()}")

# 等待1.5秒后再获取
print("等待1.5秒...")
time.sleep(1.5)
print(f"1.5秒后获取: {timed_queue.pop()}")

# 再等待1秒后获取
print("再等待1秒...")
time.sleep(1)
print(f"2.5秒后获取: {timed_queue.pop()}")
print(f"队列是否为空: {timed_queue.is_empty()}")
```

#### 3.4.2 可更新优先级的优先队列

```python
import heapq

class UpdatablePriorityQueue:
    def __init__(self):
        self._queue = []  # 堆
        self._index = 0   # 用于稳定排序
        self._entry_finder = {}  # 映射项目到其在堆中的条目
        self._REMOVED = object()  # 标记已移除项目的哨兵值
    
    def add(self, item, priority=0):
        """添加或更新项目的优先级"""
        if item in self._entry_finder:
            self.remove(item)
        entry = (-priority, self._index, item)
        self._index += 1
        self._entry_finder[item] = entry
        heapq.heappush(self._queue, entry)
    
    def remove(self, item):
        """标记项目为已移除"""
        entry = self._entry_finder.pop(item)
        entry[-1] = self._REMOVED
    
    def pop(self):
        """获取优先级最高的未移除项目"""
        while self._queue:
            priority, count, item = heapq.heappop(self._queue)
            if item is not self._REMOVED:
                del self._entry_finder[item]
                return item
        raise KeyError("优先队列为空")
    
    def is_empty(self):
        """检查队列是否为空"""
        return not self._entry_finder

# 测试可更新优先级的队列
print("\n可更新优先级的队列测试:")
updatable_queue = UpdatablePriorityQueue()

# 添加初始任务
updatable_queue.add("任务A", priority=3)
updatable_queue.add("任务B", priority=2)
updatable_queue.add("任务C", priority=5)

# 更新任务优先级
print("更新任务B的优先级...")
updatable_queue.add("任务B", priority=6)  # 提高优先级

# 逐个弹出任务
while not updatable_queue.is_empty():
    task = updatable_queue.pop()
    print(f"处理任务: {task}")
```

## 4. 实际应用场景

### 4.1 任务调度系统

堆可以用来实现高效的任务调度系统,根据任务优先级进行调度.

```python
import heapq
import time
import threading
from datetime import datetime

class TaskScheduler:
    def __init__(self):
        self._tasks = []  # 任务堆
        self._lock = threading.Lock()
        self._stop_event = threading.Event()
        self._scheduler_thread = None
    
    def schedule(self, task_id, func, priority=0, delay=0):
        """调度任务"""
        # 计算执行时间
        execution_time = time.time() + delay
        with self._lock:
            heapq.heappush(self._tasks, (execution_time, priority, task_id, func))
        return task_id
    
    def cancel(self, task_id):
        """取消任务"""
        # 注意:为简化,这里不实现任务取消
        # 实际应用中,需要标记任务为已取消或使用上面的UpdatablePriorityQueue
        pass
    
    def start(self):
        """启动调度器"""
        if self._scheduler_thread and self._scheduler_thread.is_alive():
            return
        
        self._stop_event.clear()
        self._scheduler_thread = threading.Thread(target=self._run_scheduler)
        self._scheduler_thread.daemon = True
        self._scheduler_thread.start()
    
    def stop(self):
        """停止调度器"""
        self._stop_event.set()
        if self._scheduler_thread:
            self._scheduler_thread.join(timeout=1.0)
    
    def _run_scheduler(self):
        """调度器的主循环"""
        while not self._stop_event.is_set():
            now = time.time()
            next_task_time = None
            
            with self._lock:
                # 查找所有已到执行时间的任务
                while self._tasks and self._tasks[0][0] <= now:
                    _, _, task_id, func = heapq.heappop(self._tasks)
                    # 在锁外执行任务,避免阻塞其他调度操作
                    self._execute_task(task_id, func)
                
                # 计算下次需要被唤醒的时间
                if self._tasks:
                    next_task_time = self._tasks[0][0]
            
            # 休眠直到下一个任务或被停止
            if next_task_time:
                sleep_time = max(0, next_task_time - time.time())
                self._stop_event.wait(timeout=sleep_time)
            else:
                # 队列为空时,等待一段时间后再检查
                self._stop_event.wait(timeout=0.1)
    
    def _execute_task(self, task_id, func):
        """执行任务"""
        try:
            print(f"[{datetime.now().strftime('%H:%M:%S.%f')}] 执行任务 {task_id}")
            func()
        except Exception as e:
            print(f"执行任务 {task_id} 时出错: {e}")

# 测试任务调度器
def example_task(name):
    print(f"  运行任务: {name}")

# 创建并启动调度器
scheduler = TaskScheduler()
scheduler.start()

print("调度任务示例:")

# 调度一些任务
scheduler.schedule("T1", lambda: example_task("T1 - 立即执行"), priority=1)
scheduler.schedule("T2", lambda: example_task("T2 - 延迟1秒"), priority=2, delay=1.0)
scheduler.schedule("T3", lambda: example_task("T3 - 延迟0.5秒"), priority=3, delay=0.5)
scheduler.schedule("T4", lambda: example_task("T4 - 延迟2秒"), priority=1, delay=2.0)

# 等待所有任务执行完成
time.sleep(3)

# 停止调度器
scheduler.stop()
print("调度器已停止")
```

### 4.2 Dijkstra最短路径算法

堆是实现Dijkstra最短路径算法的关键数据结构,它可以高效地选择当前距离最短的节点.

```python
import heapq

def dijkstra(graph, start):
    """使用Dijkstra算法查找从start到所有节点的最短路径"""
    # 初始化距离字典,所有节点的距离初始化为无穷大
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # 起点到自身的距离为0
    
    # 初始化路径字典
    previous_nodes = {node: None for node in graph}
    
    # 使用优先队列,存储(距离, 节点)元组
    priority_queue = [(0, start)]
    
    while priority_queue:
        # 获取当前距离最小的节点
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 如果当前距离大于已知距离,跳过(处理重复条目)
        if current_distance > distances[current_node]:
            continue
        
        # 遍历所有邻居节点
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 如果找到更短的路径,更新距离和前驱节点
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    """根据前驱节点重构从start到end的最短路径"""
    path = []
    current = end
    
    # 如果不可达,返回空路径
    if previous_nodes[end] is None:
        return path
    
    # 从终点回溯到起点
    while current:
        path.append(current)
        current = previous_nodes[current]
    
    # 反转路径,使其从起点到终点
    path.reverse()
    return path

# 测试Dijkstra算法
# 定义图的邻接表表示
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 3, 'B': 2, 'D': 3, 'E': 6},
    'D': {'B': 1, 'C': 3, 'E': 4, 'F': 5},
    'E': {'C': 6, 'D': 4, 'F': 2},
    'F': {'D': 5, 'E': 2}
}

# 运行算法
start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

print(f"从节点 {start_node} 到各节点的最短距离:")
for node, distance in distances.items():
    print(f"到 {node}: {distance}")

print("\n最短路径详情:")
for end_node in graph:
    if end_node != start_node:
        path = reconstruct_path(previous_nodes, start_node, end_node)
        if path:
            print(f"{start_node} -> {end_node}: {' -> '.join(path)} (距离: {distances[end_node]})")
        else:
            print(f"{start_node} -> {end_node}: 不可达")
```

### 4.3 实时数据分析中的Top-K问题

在数据流中找出频率最高的K个元素,这在日志分析,网络监控等场景中非常常见.

```python
import heapq
import random
from collections import Counter

class TopKProcessor:
    def __init__(self, k):
        self.k = k
        self.min_heap = []  # 存储(k+1)个最高频率的元素
        self.counter = Counter()  # 用于计数
    
    def process_item(self, item):
        """处理单个元素"""
        # 更新计数
        self.counter[item] += 1
        count = self.counter[item]
        
        # 更新最小堆
        # 方法1:使用负计数实现最小堆(推荐)
        # 这样可以快速获取当前最小频率的元素
        entry = (count, item)  # 注意这里不使用负号
        
        # 检查元素是否已在堆中
        # 为了简化,我们直接添加,后续处理重复
        # 实际应用中可以使用类似于UpdatablePriorityQueue的实现
        heapq.heappush(self.min_heap, entry)
        
        # 保持堆的大小不超过k
        while len(self.min_heap) > self.k:
            # 弹出最小频率的元素
            min_count, min_item = heapq.heappop(self.min_heap)
            # 注意:由于可能存在重复条目,我们需要确保弹出的是实际最小的
            if self.counter[min_item] > min_count:
                # 这是一个过时的条目,继续弹出
                continue
            break
    
    def get_top_k(self):
        """获取频率最高的k个元素"""
        # 清理过时条目并重建堆
        # 收集所有有效的(count, item)对
        valid_entries = []
        seen = set()
        
        for count, item in self.min_heap:
            if self.counter[item] >= count and item not in seen:
                valid_entries.append((-self.counter[item], item))  # 使用负号实现最大堆
                seen.add(item)
        
        # 重建堆以获取正确的顺序
        heapq.heapify(valid_entries)
        
        # 获取Top K元素
        top_k = []
        while valid_entries and len(top_k) < self.k:
            neg_count, item = heapq.heappop(valid_entries)
            top_k.append((item, -neg_count))
        
        return top_k

# 测试TopK处理器
def generate_data_stream(size=1000, unique_items=50):
    """生成模拟数据流,某些元素出现频率更高"""
    # 创建不均匀分布的概率
    weights = [random.randint(1, 10) for _ in range(unique_items)]
    total_weight = sum(weights)
    probabilities = [w / total_weight for w in weights]
    
    items = [f"item_{i}" for i in range(unique_items)]
    
    # 根据权重生成数据
    stream = []
    for _ in range(size):
        # 基于概率选择元素
        r = random.random()
        cumulative = 0
        for i, prob in enumerate(probabilities):
            cumulative += prob
            if r <= cumulative:
                stream.append(items[i])
                break
    
    return stream

# 生成测试数据流
data_stream = generate_data_stream(size=10000, unique_items=100)

# 初始化TopK处理器
k = 10
top_k_processor = TopKProcessor(k)

# 处理数据流
for i, item in enumerate(data_stream):
    top_k_processor.process_item(item)
    
    # 每处理1000个元素输出一次当前Top K
    if (i + 1) % 1000 == 0:
        current_top_k = top_k_processor.get_top_k()
        print(f"处理了 {i + 1} 个元素后的Top {k}:")
        for j, (item, count) in enumerate(current_top_k, 1):
            print(f"  {j}. {item}: {count} 次")
        print()

# 使用Counter计算实际的Top K进行比较
print("使用Counter计算的实际Top K:")
full_counter = Counter(data_stream)
actual_top_k = full_counter.most_common(k)
for j, (item, count) in enumerate(actual_top_k, 1):
    print(f"  {j}. {item}: {count} 次")
```

### 4.4 实现内存高效的外部排序

当处理超出内存容量的大型数据集时,外部排序是一种常用技术,堆可以用于合并多个已排序的子文件.

```python
import heapq
import os
import tempfile
import random

def external_sort(input_file, output_file, chunk_size=10000):
    """对大文件进行外部排序
    
    Args:
        input_file: 输入文件路径
        output_file: 输出文件路径
        chunk_size: 每个内存块的大小(行数)
    """
    temp_files = []
    
    try:
        # 第一阶段:将大文件分割成多个已排序的小文件
        print(f"开始分割文件 {input_file}...")
        
        with open(input_file, 'r') as f:
            chunk_number = 0
            while True:
                # 读取一块数据到内存
                lines = []
                for _ in range(chunk_size):
                    line = f.readline()
                    if not line:
                        break
                    lines.append(line.strip())
                
                if not lines:
                    break  # 文件读取完毕
                
                # 对内存中的数据进行排序
                lines.sort()
                
                # 将排序后的数据写入临时文件
                fd, temp_path = tempfile.mkstemp(suffix='.txt', prefix=f'sorted_chunk_{chunk_number}_')
                temp_files.append(temp_path)
                
                with os.fdopen(fd, 'w') as temp:
                    for line in lines:
                        temp.write(f"{line}\n")
                
                chunk_number += 1
                print(f"  已创建临时文件 {chunk_number}/{chunk_number}: {temp_path}")
        
        print(f"分割完成,创建了 {len(temp_files)} 个临时文件")
        
        # 第二阶段:使用堆合并所有排序好的临时文件
        print(f"开始合并临时文件到 {output_file}...")
        
        # 打开所有临时文件
        file_handlers = [open(temp_file, 'r') for temp_file in temp_files]
        
        # 使用heapq.merge合并多个有序文件
        with open(output_file, 'w') as out:
            # heapq.merge要求输入序列是已排序的
            # 文件对象作为迭代器,每次返回一行
            for line in heapq.merge(*file_handlers):
                out.write(line)
        
        print("合并完成")
        
    finally:
        # 清理临时文件
        for file_handler in file_handlers:
            try:
                file_handler.close()
            except:
                pass
        
        for temp_file in temp_files:
            try:
                os.unlink(temp_file)
            except:
                pass
        
        print(f"已清理 {len(temp_files)} 个临时文件")

# 生成测试数据
def generate_test_file(file_path, lines=100000, line_length=20):
    """生成随机测试数据文件"""
    print(f"生成测试文件 {file_path},包含 {lines} 行数据...")
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    
    with open(file_path, 'w') as f:
        for _ in range(lines):
            # 生成随机字符串
            line = ''.join(random.choice(chars) for _ in range(line_length))
            f.write(f"{line}\n")
    
    print(f"测试文件生成完成,大小约为 {os.path.getsize(file_path) / 1024:.2f} KB")

# 验证排序结果
def verify_sort_result(sorted_file):
    """验证排序结果是否正确"""
    print(f"验证排序结果 {sorted_file}...")
    
    is_sorted = True
    prev_line = None
    error_count = 0
    
    with open(sorted_file, 'r') as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if prev_line is not None and line < prev_line:
                is_sorted = False
                error_count += 1
                if error_count <= 5:  # 只显示前5个错误
                    print(f"  错误在第 {i} 行: '{prev_line}' > '{line}'")
            prev_line = line
    
    if is_sorted:
        print("验证通过,文件已正确排序")
    else:
        print(f"验证失败,发现 {error_count} 处顺序错误")
    
    return is_sorted

# 主程序
test_input = 'test_input.txt'
test_output = 'sorted_output.txt'

# 生成测试数据
generate_test_file(test_input, lines=50000, line_length=30)

# 执行外部排序
external_sort(test_input, test_output, chunk_size=10000)

# 验证结果
verify_sort_result(test_output)

# 清理测试文件
os.unlink(test_input)
os.unlink(test_output)
print("测试完成,已清理测试文件")
```

### 4.5 优先级任务执行系统

在实际应用中,我们经常需要按照优先级执行任务,特别是在资源有限的情况下.

```python
import heapq
import threading
import time
import random

class PriorityTaskExecutor:
    def __init__(self, num_workers=4):
        self._task_queue = []  # 任务堆
        self._lock = threading.Lock()
        self._condition = threading.Condition(self._lock)
        self._workers = []
        self._num_workers = num_workers
        self._stop_event = threading.Event()
        self._task_counter = 0
    
    def start(self):
        """启动工作线程"""
        if self._workers:
            return  # 已经启动
        
        self._stop_event.clear()
        
        # 创建并启动工作线程
        for i in range(self._num_workers):
            worker = threading.Thread(target=self._worker_thread, args=(i,))
            worker.daemon = True  # 设为守护线程,主线程结束时自动退出
            worker.start()
            self._workers.append(worker)
        
        print(f"启动了 {self._num_workers} 个工作线程")
    
    def stop(self, wait=True):
        """停止工作线程"""
        with self._lock:
            self._stop_event.set()
            self._condition.notify_all()  # 通知所有等待的工作线程
        
        if wait and self._workers:
            for worker in self._workers:
                worker.join()
            self._workers = []
        
        print("执行器已停止")
    
    def submit(self, task_func, priority=0, *args, **kwargs):
        """提交任务到队列"""
        with self._lock:
            if self._stop_event.is_set():
                raise RuntimeError("执行器已停止,不能提交新任务")
            
            # 为了任务的稳定排序,使用递增的计数器
            self._task_counter += 1
            # 注意:优先级使用负数,因为heapq是最小堆
            task = (-priority, self._task_counter, task_func, args, kwargs)
            heapq.heappush(self._task_queue, task)
            
            # 通知一个工作线程有新任务
            self._condition.notify()
            
            return self._task_counter
    
    def _worker_thread(self, worker_id):
        """工作线程的主循环"""
        print(f"工作线程 {worker_id} 已启动")
        
        while not self._stop_event.is_set():
            task_func = None
            args = ()
            kwargs = {}
            
            with self._lock:
                # 如果队列为空,等待新任务或停止信号
                while len(self._task_queue) == 0 and not self._stop_event.is_set():
                    self._condition.wait()
                
                # 检查是否收到停止信号
                if self._stop_event.is_set():
                    break
                
                # 获取一个任务
                _, _, task_func, args, kwargs = heapq.heappop(self._task_queue)
            
            # 在锁外执行任务
            try:
                print(f"工作线程 {worker_id} 开始执行任务")
                task_func(*args, **kwargs)
                print(f"工作线程 {worker_id} 完成任务")
            except Exception as e:
                print(f"工作线程 {worker_id} 执行任务时出错: {e}")
    
    def task_count(self):
        """获取队列中的任务数量"""
        with self._lock:
            return len(self._task_queue)

# 模拟任务函数
def example_task(task_id, sleep_time):
    """示例任务:休眠指定时间"""
    print(f"  任务 {task_id} 开始执行,将休眠 {sleep_time:.2f} 秒")
    time.sleep(sleep_time)
    print(f"  任务 {task_id} 执行完成")

# 测试优先级任务执行器
print("\n优先级任务执行器测试:")

executor = PriorityTaskExecutor(num_workers=3)
executor.start()

# 提交不同优先级的任务
print("\n提交任务:")
for i in range(1, 11):
    # 随机生成优先级 (1-5,数字越大优先级越高)
    priority = random.randint(1, 5)
    # 随机生成任务执行时间
    sleep_time = random.uniform(0.2, 1.0)
    
    task_id = executor.submit(
        example_task, 
        priority=priority,
        task_id=f"T{i}(优先级{priority})",
        sleep_time=sleep_time
    )
    
    print(f"  提交任务 {task_id}: T{i}, 优先级 {priority}, 执行时间约 {sleep_time:.2f} 秒")
    time.sleep(0.1)  # 短暂延迟,便于观察

# 等待任务执行完成
while executor.task_count() > 0:
    print(f"\n队列中剩余任务数: {executor.task_count()}")
    time.sleep(1)

# 再等待一小段时间确保最后一个任务完成
time.sleep(1)

# 停止执行器
executor.stop()
print("测试完成")
```

### 4.6 实现模拟退火算法

堆可以用于在模拟退火等优化算法中高效地管理候选解.

```python
import heapq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

class SimulatedAnnealing:
    def __init__(self, objective_func, initial_state, temperature_schedule, 
                 neighbor_func, max_iterations=1000):
        self.objective_func = objective_func  # 目标函数
        self.current_state = initial_state    # 当前状态
        self.temperature_schedule = temperature_schedule  # 温度调度函数
        self.neighbor_func = neighbor_func    # 邻居生成函数
        self.max_iterations = max_iterations  # 最大迭代次数
        
        # 初始化
        self.current_energy = objective_func(initial_state)
        self.best_state = np.copy(initial_state)
        self.best_energy = self.current_energy
        self.energy_history = [self.current_energy]
        self.temperature_history = []
        self.acceptance_history = []
    
    def run(self):
        """运行模拟退火算法"""
        print("开始模拟退火算法...")
        start_time = time.time()
        
        accepted_count = 0
        
        for i in range(self.max_iterations):
            # 获取当前温度
            temperature = self.temperature_schedule(i, self.max_iterations)
            self.temperature_history.append(temperature)
            
            # 生成邻居状态
            new_state = self.neighbor_func(self.current_state)
            new_energy = self.objective_func(new_state)
            
            # 计算能量差
            energy_diff = new_energy - self.current_energy
            
            # 决定是否接受新状态
            accept = False
            if energy_diff < 0:
                # 如果新状态更好,直接接受
                accept = True
            else:
                # 否则,以一定概率接受
                acceptance_probability = np.exp(-energy_diff / temperature)
                accept = np.random.random() < acceptance_probability
            
            if accept:
                self.current_state = new_state
                self.current_energy = new_energy
                accepted_count += 1
                
                # 更新全局最优解
                if self.current_energy < self.best_energy:
                    self.best_state = np.copy(self.current_state)
                    self.best_energy = self.current_energy
                    print(f"迭代 {i}: 找到更优解,能量值 = {self.best_energy:.4f}")
            
            # 记录历史
            self.energy_history.append(self.current_energy)
            self.acceptance_history.append(accepted_count / (i + 1))
            
            # 每100次迭代打印一次进度
            if (i + 1) % 100 == 0:
                print(f"迭代 {i+1}/{self.max_iterations}, 温度 = {temperature:.6f}, "
                      f"当前能量 = {self.current_energy:.4f}, 最优能量 = {self.best_energy:.4f}")
        
        end_time = time.time()
        print(f"模拟退火算法完成,耗时 {end_time - start_time:.2f} 秒")
        print(f"最终最优解能量值: {self.best_energy:.4f}")
        
        return self.best_state, self.best_energy

# 示例:求解旅行商问题 (TSP)
def tsp_objective(cities, route):
    """TSP目标函数:计算路径总距离"""
    total_distance = 0
    for i in range(len(route) - 1):
        # 计算两个城市之间的欧几里得距离
        total_distance += np.linalg.norm(cities[route[i]] - cities[route[i+1]])
    # 加上回到起点的距离
    total_distance += np.linalg.norm(cities[route[-1]] - cities[route[0]])
    return total_distance

def tsp_neighbor(route):
    """TSP邻居生成函数:随机交换两个城市的位置"""
    new_route = route.copy()
    # 随机选择两个不同的索引
    i, j = np.random.choice(len(route), size=2, replace=False)
    # 交换位置
    new_route[i], new_route[j] = new_route[j], new_route[i]
    return new_route

def geometric_cooling(iteration, max_iterations, initial_temp=100.0, cooling_rate=0.95):
    """几何冷却调度"""
    return initial_temp * (cooling_rate ** iteration)

def solve_tsp_example():
    """求解TSP示例"""
    # 生成随机城市坐标
    np.random.seed(42)  # 设置随机种子以确保结果可重现
    n_cities = 30
    cities = np.random.rand(n_cities, 2) * 100
    
    # 初始路径:随机排列城市
    initial_route = np.arange(n_cities)
    np.random.shuffle(initial_route)
    
    # 定义目标函数(使用部分应用来固定城市坐标)
    objective_func = lambda route: tsp_objective(cities, route)
    
    # 运行模拟退火算法
    sa = SimulatedAnnealing(
        objective_func=objective_func,
        initial_state=initial_route,
        temperature_schedule=geometric_cooling,
        neighbor_func=tsp_neighbor,
        max_iterations=5000
    )
    
    best_route, best_energy = sa.run()
    
    # 打印结果
    print(f"\n旅行商问题求解结果:")
    print(f"城市数量: {n_cities}")
    print(f"最短路径长度: {best_energy:.2f}")
    print(f"最优路径: {best_route}")
    
    # 可视化结果
    visualize_tsp_result(cities, best_route)
    
    # 可视化能量历史
    visualize_energy_history(sa.energy_history, sa.temperature_history)

def visualize_tsp_result(cities, route):
    """可视化TSP结果"""
    # 这部分需要matplotlib,如果环境中没有安装,可以注释掉
    try:
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(10, 8))
        
        # 绘制城市
        plt.scatter(cities[:, 0], cities[:, 1], c='red', s=50, label='城市')
        
        # 绘制路径
        route_cities = cities[route]
        plt.plot(route_cities[:, 0], route_cities[:, 1], 'b-', label='路径')
        
        # 绘制回到起点的连接
        plt.plot([route_cities[-1, 0], route_cities[0, 0]], 
                 [route_cities[-1, 1], route_cities[0, 1]], 'b-')
        
        # 标记起点
        plt.scatter(cities[route[0], 0], cities[route[0], 1], c='green', s=100, label='起点')
        
        plt.title(f'旅行商问题最优路径 (城市数: {len(cities)})')
        plt.xlabel('X坐标')
        plt.ylabel('Y坐标')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        
        # 注意:在非交互式环境中,可以保存图片而不是显示
        # plt.savefig('tsp_solution.png')
        # print("解决方案已保存为 'tsp_solution.png'")
        
    except ImportError:
        print("未安装matplotlib,跳过可视化")

def visualize_energy_history(energy_history, temperature_history):
    """可视化能量历史"""
    try:
        import matplotlib.pyplot as plt
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # 能量历史
        ax1.plot(energy_history)
        ax1.set_title('能量历史')
        ax1.set_xlabel('迭代次数')
        ax1.set_ylabel('能量值')
        ax1.grid(True)
        
        # 温度历史
        ax2.plot(temperature_history)
        ax2.set_title('温度历史')
        ax2.set_xlabel('迭代次数')
        ax2.set_ylabel('温度')
        ax2.set_yscale('log')  # 使用对数刻度更清晰
        ax2.grid(True)
        
        plt.tight_layout()
        
        # 注意:在非交互式环境中,可以保存图片
        # plt.savefig('sa_history.png')
        # print("历史记录已保存为 'sa_history.png'")
        
    except ImportError:
        print("未安装matplotlib,跳过历史记录可视化")

# 运行TSP示例
# 注意:由于可视化部分需要matplotlib,在实际运行时可能需要安装:pip install matplotlib
solve_tsp_example()
```

### 4.7 网络流量分析与异常检测

在网络流量分析中,我们可以使用堆来识别异常流量模式,例如检测DDoS攻击.

```python
import heapq
import time
import random
from collections import defaultdict, deque

class NetworkTrafficAnalyzer:
    def __init__(self, window_size=60, threshold_multiplier=3):
        self.window_size = window_size  # 时间窗口大小(秒)
        self.threshold_multiplier = threshold_multiplier  # 阈值倍数
        self.traffic_data = defaultdict(lambda: deque(maxlen=window_size))  # IP -> 流量记录
        self.ip_count_heap = []  # 用于存储IP流量计数的堆
        self.ip_last_update = {}  # 记录每个IP的最后更新时间
    
    def add_traffic(self, ip_address, timestamp=None, bytes_count=1):
        """添加流量数据"""
        if timestamp is None:
            timestamp = time.time()
        
        # 添加到时间序列数据
        self.traffic_data[ip_address].append((timestamp, bytes_count))
        
        # 更新最后更新时间
        self.ip_last_update[ip_address] = timestamp
    
    def _get_current_traffic_rate(self, ip_address):
        """获取指定IP的当前流量速率(字节/秒)"""
        if ip_address not in self.traffic_data or not self.traffic_data[ip_address]:
            return 0
        
        # 计算时间窗口内的总流量
        total_bytes = sum(bytes_count for _, bytes_count in self.traffic_data[ip_address])
        
        # 计算实际的时间窗口大小(可能小于window_size)
        timestamps = [t for t, _ in self.traffic_data[ip_address]]
        time_diff = max(1, timestamps[-1] - timestamps[0] + 1)  # 避免除零错误
        
        return total_bytes / time_diff
    
    def update_heap(self):
        """更新IP流量计数堆"""
        current_time = time.time()
        updated_heap = []
        
        # 收集所有活跃IP的当前流量速率
        for ip_address in list(self.traffic_data.keys()):
            # 清理长时间未更新的IP
            if current_time - self.ip_last_update.get(ip_address, 0) > self.window_size * 2:
                del self.traffic_data[ip_address]
                if ip_address in self.ip_last_update:
                    del self.ip_last_update[ip_address]
                continue
            
            # 获取当前流量速率
            rate = self._get_current_traffic_rate(ip_address)
            # 使用负速率,因为heapq是最小堆
            heapq.heappush(updated_heap, (-rate, ip_address))
        
        self.ip_count_heap = updated_heap
    
    def get_top_traffic_ips(self, n=10):
        """获取流量最高的n个IP"""
        self.update_heap()
        
        top_ips = []
        for i in range(min(n, len(self.ip_count_heap))):
            neg_rate, ip = heapq.heappop(self.ip_count_heap)
            top_ips.append((ip, -neg_rate))
        
        # 恢复堆(可选)
        for ip, rate in top_ips:
            heapq.heappush(self.ip_count_heap, (-rate, ip))
        
        return top_ips
    
    def detect_anomalies(self):
        """检测流量异常"""
        self.update_heap()
        
        # 计算平均流量速率和标准差
        rates = [-neg_rate for neg_rate, _ in self.ip_count_heap]
        if not rates:
            return []
        
        avg_rate = sum(rates) / len(rates)
        if len(rates) > 1:
            variance = sum((r - avg_rate) ** 2 for r in rates) / (len(rates) - 1)
            std_dev = variance ** 0.5
        else:
            std_dev = 0
        
        # 计算异常阈值
        threshold = avg_rate + self.threshold_multiplier * std_dev
        
        # 检测异常IP
        anomalies = []
        for neg_rate, ip in self.ip_count_heap:
            rate = -neg_rate
            if rate > threshold:
                anomalies.append((ip, rate, threshold))
        
        return anomalies
    
    def clean_old_data(self):
        """清理过期数据"""
        current_time = time.time()
        cutoff_time = current_time - self.window_size
        
        for ip_address in list(self.traffic_data.keys()):
            # 移除过期的流量记录
            while self.traffic_data[ip_address] and self.traffic_data[ip_address][0][0] < cutoff_time:
                self.traffic_data[ip_address].popleft()
            
            # 如果没有数据了,移除该IP
            if not self.traffic_data[ip_address]:
                del self.traffic_data[ip_address]
                if ip_address in self.ip_last_update:
                    del self.ip_last_update[ip_address]

# 模拟网络流量
def generate_network_traffic(analyzer, duration=60, base_ips=100, attack_ips=5):
    """生成模拟网络流量,包含一些异常流量(模拟DDoS攻击)"""
    print(f"开始生成网络流量,持续 {duration} 秒...")
    
    # 生成正常IP列表
    normal_ips = [f"192.168.1.{i}" for i in range(1, base_ips + 1)]
    
    # 生成攻击IP列表
    attack_ips_list = [f"10.0.0.{i}" for i in range(1, attack_ips + 1)]
    
    # 记录起始时间
    start_time = time.time()
    
    # 模拟流量
    while time.time() - start_time < duration:
        current_time = time.time()
        
        # 生成正常流量
        for _ in range(random.randint(10, 20)):  # 每次迭代生成10-20个正常流量
            ip = random.choice(normal_ips)
            # 正常流量较小
            bytes_count = random.randint(100, 1000)
            analyzer.add_traffic(ip, current_time, bytes_count)
        
        # 模拟DDoS攻击(只在部分时间发生)
        if random.random() < 0.3:  # 30%的概率发生攻击
            for ip in attack_ips_list:
                # 攻击流量很大
                bytes_count = random.randint(10000, 50000)
                analyzer.add_traffic(ip, current_time, bytes_count)
        
        # 清理旧数据
        analyzer.clean_old_data()
        
        # 短暂休眠以减少CPU使用
        time.sleep(0.01)
    
    print("网络流量模拟完成")

# 分析网络流量
def analyze_traffic():
    """分析网络流量并检测异常"""
    # 创建流量分析器
    analyzer = NetworkTrafficAnalyzer(window_size=30, threshold_multiplier=3)
    
    # 生成模拟流量
    generate_network_traffic(analyzer, duration=30, base_ips=50, attack_ips=3)
    
    # 分析结果
    print("\n===== 网络流量分析结果 =====")
    
    # 获取流量最高的10个IP
    top_ips = analyzer.get_top_traffic_ips(n=10)
    print(f"\n流量最高的10个IP:")
    for i, (ip, rate) in enumerate(top_ips, 1):
        print(f"  {i}. {ip}: {rate:.2f} B/s")
    
    # 检测异常
    anomalies = analyzer.detect_anomalies()
    print(f"\n检测到 {len(anomalies)} 个流量异常:")
    for ip, rate, threshold in anomalies:
        print(f"  {ip}: {rate:.2f} B/s (阈值: {threshold:.2f} B/s)")
        if ip.startswith("10.0.0."):
            print(f"    警告: 该IP可能参与了DDoS攻击!")

# 运行网络流量分析
analyze_traffic()
```

## 5. 性能分析

### 5.1 时间复杂度分析

| 操作 | 时间复杂度 | 空间复杂度 | 描述 |
|------|-----------|-----------|------|
| heapify | O(n) | O(1) | 将列表转换为堆 |
| heappush | O(log n) | O(1) | 添加元素到堆 |
| heappop | O(log n) | O(1) | 移除并返回最小元素 |
| heappushpop | O(log n) | O(1) | 添加后弹出最小元素(比单独操作更高效) |
| heapreplace | O(log n) | O(1) | 弹出最小元素后添加新元素 |
| nsmallest | O(n log k) | O(k) | 获取k个最小元素 |
| nlargest | O(n log k) | O(k) | 获取k个最大元素 |
| merge | O(n log m) | O(m) | 合并m个有序序列,总长度为n |

**性能比较**: 
- 对于"nsmallest"/"nlargest",当k较小时(k << n),使用堆实现更高效
- 当k接近n时,直接排序然后切片更高效:"sorted(iterable)[:n]"或"sorted(iterable)[-n:]"

### 5.2 性能比较测试

```python
```python
"""  # 闭合未闭合的双三引号
# 示例:处理大型数据集时的内存优化
import heapq
import itertools

def find_top_k_large_data(file_path, k=10, chunk_size=10000):
    """从大文件中找出前k个最大的数,避免一次性加载全部数据到内存"""
    # 用于存储当前top k的最小堆
    min_heap = []
    
    with open(file_path, 'r') as f:
        # 分块处理数据
        while True:
            # 读取一块数据
            lines = list(itertools.islice(f, chunk_size))
            if not lines:
                break
            
            # 转换为数字并处理
            numbers = [int(line.strip()) for line in lines]
            
            # 更新top k
            for num in numbers:
                if len(min_heap) < k:
                    heapq.heappush(min_heap, num)
                elif num > min_heap[0]:
                    # 如果当前数字比堆顶大,替换堆顶
                    heapq.heappushpop(min_heap, num)
    
    # 转换为降序排列的列表返回
    return sorted(min_heap, reverse=True)
"""

### 6.2 避免常见错误

"""python
import heapq

# 错误示例1:直接对普通列表使用堆操作
numbers = [3, 1, 4, 1, 5, 9]
# 这会出错,因为numbers不是一个堆
# print(heapq.heappop(numbers))  # 结果可能不是1

# 正确做法:先使用heapify
heapq.heapify(numbers)
print(heapq.heappop(numbers))  # 正确输出1

# 错误示例2:假设堆是完全有序的
heap = [1, 3, 2, 6, 5, 9, 4]
print(heap)  # 输出: [1, 3, 2, 6, 5, 9, 4]
# 注意:堆只保证最小元素在堆顶,其他元素不一定有序

# 错误示例3:使用heapq.merge处理未排序的列表
unsorted1 = [5, 2, 8]
unsorted2 = [3, 1, 9]
# 这会产生错误的结果
wrong_result = list(heapq.merge(unsorted1, unsorted2))
print(f"错误结果: {wrong_result}")  # 可能不是正确排序的

# 正确做法:先排序
unsorted1.sort()
unsorted2.sort()
correct_result = list(heapq.merge(unsorted1, unsorted2))
print(f"正确结果: {correct_result}")

# 错误示例4:在多线程环境中不使用锁
# 参考前面的ThreadSafePriorityQueue示例,确保线程安全

# 错误示例5:忽略了堆元素的比较规则
# 堆中的元素需要支持比较操作,特别是自定义对象
class CustomObject:
    def __init__(self, value):
        self.value = value

# 这会引发TypeError
# heap = [CustomObject(3), CustomObject(1)]
# heapq.heapify(heap)

# 正确做法:实现__lt__方法或使用元组
class ComparableObject:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value

# 现在可以正常工作
heap = [ComparableObject(3), ComparableObject(1)]
heapq.heapify(heap)
print(f"最小值: {heapq.heappop(heap).value}")  # 输出1
"""

### 6.3 堆的稳定性考虑

"``python
import heapq

# 堆排序是不稳定的排序算法
# 示例:具有相同优先级的元素可能会改变相对顺序

# 创建具有相同优先级但不同内容的元素
items = [(3, 'apple'), (1, 'banana'), (3, 'cherry'), (1, 'date'), (2, 'elderberry')]

# 使用heapq排序
heapq.heapify(items)
sorted_items = []
while items:
    sorted_items.append(heapq.heappop(items))

print(f"排序后: {sorted_items}")
# 注意:相同优先级的元素(如(1, 'banana')和(1, 'date'))的相对顺序可能会改变

# 解决方案:使用稳定的优先级队列实现
class StablePriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # 递增的索引,用于稳定排序
    
    def push(self, item, priority):
        # 优先级使用负数(对于最小堆),然后是索引(保证稳定性)
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

# 测试稳定的优先队列
stable_queue = StablePriorityQueue()
for priority, item in [(3, 'apple'), (1, 'banana'), (3, 'cherry'), (1, 'date'), (2, 'elderberry')]:
    stable_queue.push(item, priority)

stable_results = []
while stable_queue._queue:
    stable_results.append(stable_queue.pop())

print(f"稳定队列结果: {stable_results}")
# 相同优先级的元素会保持它们被插入的顺序
```

## 5. 使用注意事项

在使用 `heapq` 模块时，有几个重要的注意事项需要牢记，以避免常见的陷阱和性能问题。

### 5.1 堆的特性与限制

- **最小堆性质**：Python的`heapq`默认实现的是最小堆，这意味着堆顶元素始终是最小的。如果需要最大堆，可以通过取负数或使用自定义比较器来实现。
- **零索引**：与许多堆实现不同，Python的堆使用的是零索引，这意味着对于位置`i`的元素，其左子节点位于`2*i+1`，右子节点位于`2*i+2`。
- **非完全排序**：堆只保证堆顶元素是最小的，并不保证整个列表是有序的。如果需要有序序列，需要依次弹出元素。

### 5.2 性能考虑

- **初始化开销**：使用`heapify()`将现有列表转换为堆的时间复杂度是O(n)，而逐个插入元素的时间复杂度是O(n log n)，因此在处理已有数据时，`heapify()`通常更高效。
- **内存占用**：堆操作是在原列表上进行的，不会创建新的数据结构，因此内存效率较高。
- **大堆处理**：对于非常大的堆，需要注意内存使用和缓存效率问题。在处理大数据集时，考虑使用外部排序或流式处理。

### 5.3 线程安全

- `heapq`模块本身不是线程安全的。在多线程环境中，如果多个线程同时访问同一个堆，需要使用锁机制来确保线程安全。
- 可以参考前面提到的`ThreadSafePriorityQueue`类，它提供了线程安全的优先队列实现。

### 5.4 数据一致性

- **自定义对象**：当使用自定义对象作为堆元素时，必须确保这些对象实现了适当的比较方法（如`__lt__`），否则可能导致意外的行为或`TypeError`异常。
- **不可变数据**：为了避免意外修改堆元素的值导致堆属性被破坏，最好使用不可变数据类型或将自定义对象的关键属性设计为只读。

### 5.5 实用建议

- **避免直接访问**：不要直接通过索引访问或修改堆中的元素（除了堆顶元素），这可能会破坏堆的性质。
- **有序序列合并**：在使用`merge()`函数时，确保输入的序列已经排序，否则结果可能不符合预期。
- **优先级表示**：对于需要复杂优先级逻辑的场景，考虑使用元组(优先级, 计数器, 值)的形式来避免元素不可比较的问题。

## 6. 总结与最佳实践

### 7.1 heapq模块的主要优势

1. **高效的优先队列实现**:基于堆的优先队列操作复杂度为O(log n),比线性搜索更高效
2. **内存效率**:直接操作Python列表,无需额外的数据结构
3. **丰富的功能集**:支持创建堆,添加/删除元素,获取极值,合并有序序列等
4. **与Python生态系统集成**:可以与其他Python特性无缝配合
5. **惰性计算支持**:merge函数支持惰性计算,适合处理大数据集

### 7.2 最佳实践建议

1. **选择合适的操作函数**
   - 使用"heapify"初始化堆,而不是多次调用"heappush"
   - 使用"heappushpop"和"heapreplace"代替分开的操作
   - 根据k值大小选择"nsmallest"/"nlargest"或直接排序

2. **处理自定义对象**
   - 确保自定义对象实现了比较方法("__lt__"等)
   - 或者使用元组包装,将比较键放在元组的第一位

3. **内存管理**
   - 对于大文件处理,使用"merge"的惰性特性或分块处理
   - 考虑使用生成器表达式减少内存占用

4. **线程安全**
   - 在多线程环境中使用时,确保添加适当的锁机制
   - 考虑使用已有的线程安全队列实现

5. **性能优化**
   - 避免在堆操作中进行昂贵的计算
   - 对于频繁访问的堆,考虑使用更专用的数据结构

### 7.3 学习资源与进阶阅读

- [Python官方文档 - heapq模块](https://docs.python.org/3/library/heapq.html)
- <算法导论>(Introduction to Algorithms)第6章:堆排序和优先队列
- <Python Cookbook>第4版第1部分:数据结构与算法
- [Real Python - Python's heapq Module: Using Heaps and Priority Queues](https://realpython.com/python-heapq-module/)

### 7.4 学习总结

heapq模块提供了高效的堆操作实现,是Python中处理优先队列,堆排序和相关算法的重要工具.通过掌握heapq的基本操作和高级用法,开发者可以实现各种复杂的数据处理和算法需求,从简单的任务调度到复杂的图算法.

在实际应用中,需要根据具体场景选择合适的方法,并注意内存使用和线程安全等问题.对于性能关键的应用,可以结合其他优化技术,如使用更专用的数据结构或算法变体,以获得更好的性能.

总的来说,heapq模块是Python标准库中一个功能强大且易于使用的工具,值得每个Python开发者深入学习和掌握.
```
"""
'''
"
'
