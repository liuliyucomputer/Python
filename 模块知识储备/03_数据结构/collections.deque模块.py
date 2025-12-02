# collections.deque模块 - Python标准库中的双端队列

"""
 collections.deque是Python标准库中提供的双端队列数据结构实现。
双端队列是一种可以在两端进行快速添加和删除操作的线性数据结构，
其特点是在队列的两端执行添加和删除操作的时间复杂度均为O(1)。

相比普通的Python列表，deque在头部进行操作时具有显著的性能优势，
因为列表在头部操作需要移动所有元素，时间复杂度为O(n)。
"""

# 1. 核心功能介绍

print("=== 1. 核心功能介绍 ===")
print("\ncollections.deque模块提供了以下主要功能:")
print("1. 双端队列数据结构的高效实现")
print("2. 支持从队列的两端快速添加和删除元素")
print("3. 可以设置最大长度，实现固定大小的队列")
print("4. 支持队列旋转和扩展操作")
print("5. 提供高效的内存使用和操作性能")

# 2. 基本操作

print("\n=== 2. 基本操作 ===")

# 导入deque
from collections import deque

print("\n2.1 创建deque对象")
print("可以通过多种方式创建deque对象:")

# 从列表创建
d1 = deque([1, 2, 3, 4, 5])
print(f"从列表创建: {d1}")

# 从字符串创建
d2 = deque('python')
print(f"从字符串创建: {d2}")

# 从生成器创建
d3 = deque(range(1, 6))
print(f"从生成器创建: {d3}")

# 创建空的deque
d4 = deque()
print(f"创建空deque: {d4}")

# 创建指定最大长度的deque
d5 = deque(maxlen=3)
print(f"创建最大长度为3的deque: {d5}")

print("\n2.2 基本的添加和删除操作")
print("deque支持从两端添加和删除元素:")

# 创建一个deque
d = deque([1, 2, 3])
print(f"原始deque: {d}")

# 从右端添加元素（append）
d.append(4)
print(f"append(4)后: {d}")

# 从左端添加元素（appendleft）
d.appendleft(0)
print(f"appendleft(0)后: {d}")

# 从右端删除元素（pop）
last_item = d.pop()
print(f"pop()删除了: {last_item}, 剩余: {d}")

# 从左端删除元素（popleft）
first_item = d.popleft()
print(f"popleft()删除了: {first_item}, 剩余: {d}")

print("\n2.3 批量操作")
print("deque支持从两端批量添加元素:")

# 创建一个deque
d = deque([1, 2, 3])
print(f"原始deque: {d}")

# 从右端批量添加元素（extend）
d.extend([4, 5, 6])
print(f"extend([4, 5, 6])后: {d}")

# 从左端批量添加元素（extendleft）
d.extendleft([0, -1, -2])
print(f"extendleft([0, -1, -2])后: {d}")
print("注意: extendleft添加的元素顺序是反转的，因为每个新元素都添加到最左端")

print("\n2.4 固定大小的deque")
print("可以创建具有最大长度限制的deque，当达到限制时，新元素会导致旧元素被移除:")

# 创建最大长度为3的deque
d = deque(maxlen=3)
print(f"创建最大长度为3的deque: {d}")

# 添加元素直到达到最大长度
d.append(1)
d.append(2)
d.append(3)
print(f"添加三个元素后: {d}")

# 继续添加元素，最旧的元素会被自动移除
d.append(4)
print(f"再添加一个元素后（最旧的1被移除）: {d}")

# 从左端添加，最右端的元素会被移除
d.appendleft(0)
print(f"从左端添加0后（最右端的4被移除）: {d}")

print("\n2.5 队列旋转")
print("deque可以进行旋转操作，将元素从一端移动到另一端:")

# 创建一个deque
d = deque([1, 2, 3, 4, 5])
print(f"原始deque: {d}")

# 向右旋转1位（正数表示向右旋转）
d.rotate(1)
print(f"rotate(1)后: {d}")  # 向右旋转一位，最后一个元素移到开头

# 向右旋转2位
d.rotate(2)
print(f"再rotate(2)后: {d}")

# 向左旋转3位（负数表示向左旋转）
d.rotate(-3)
print(f"rotate(-3)后: {d}")  # 向左旋转三位，前三个元素移到末尾

print("\n2.6 其他基本操作")

# 创建一个deque
d = deque([1, 2, 3, 2, 1])
print(f"原始deque: {d}")

# 获取deque的长度
print(f"deque长度: {len(d)}")

# 检查元素是否在deque中
print(f"3在deque中: {3 in d}")
print(f"5在deque中: {5 in d}")

# 统计元素出现次数
print(f"元素2出现次数: {d.count(2)}")

# 反转deque
d.reverse()
print(f"反转后: {d}")

# 清空deque
d.clear()
print(f"清空后: {d}")

# 3. 高级用法

print("\n=== 3. 高级用法 ===")

print("\n3.1 作为栈使用")
print("deque可以高效地用作栈（后进先出，LIFO）:")

stack = deque()

# 入栈操作
stack.append(1)
stack.append(2)
stack.append(3)
print(f"入栈三次后: {stack}")

# 出栈操作
while stack:
    item = stack.pop()
    print(f"出栈: {item}")

print("栈为空: {}".format(not stack))

print("\n3.2 作为队列使用")
print("deque可以高效地用作队列（先进先出，FIFO）:")

queue = deque()

# 入队操作
queue.append(1)
queue.append(2)
queue.append(3)
print(f"入队三次后: {queue}")

# 出队操作
while queue:
    item = queue.popleft()
    print(f"出队: {item}")

print("队列为空: {}".format(not queue))

print("\n3.3 作为双端队列使用")
print("deque的主要优势是可以在两端高效操作:")

dq = deque([3, 4, 5])
print(f"初始队列: {dq}")

# 从左端添加
dq.appendleft(2)
dq.appendleft(1)
print(f"左端添加后: {dq}")

# 从右端添加
dq.append(6)
dq.append(7)
print(f"右端添加后: {dq}")

# 从左端删除
left_item = dq.popleft()
print(f"左端删除: {left_item}, 剩余: {dq}")

# 从右端删除
right_item = dq.pop()
print(f"右端删除: {right_item}, 剩余: {dq}")

print("\n3.4 实现滑动窗口")
print("使用固定大小的deque可以轻松实现滑动窗口算法:")

def sliding_window_max(nums, window_size):
    """
    使用deque实现滑动窗口最大值算法
    
    Args:
        nums: 输入数组
        window_size: 窗口大小
    
    Returns:
        每个窗口的最大值组成的列表
    """
    from collections import deque
    
    result = []
    # 存储索引而不是值，这样可以判断元素是否在当前窗口中
    dq = deque()
    
    for i, num in enumerate(nums):
        # 移除所有小于当前元素的值，因为它们不可能是窗口最大值
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        # 添加当前元素的索引
        dq.append(i)
        
        # 移除不在当前窗口内的元素（即索引超出范围）
        if dq[0] <= i - window_size:
            dq.popleft()
        
        # 当窗口完全形成后，记录最大值（队列头部的元素）
        if i >= window_size - 1:
            result.append(nums[dq[0]])
    
    return result

# 测试滑动窗口最大值算法
nums = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3
print(f"输入数组: {nums}")
print(f"窗口大小: {window_size}")
print(f"滑动窗口最大值: {sliding_window_max(nums, window_size)}")

print("\n3.5 实现回文检查器")
print("使用deque可以高效地实现回文检查器:")

def is_palindrome(text):
    """
    使用deque检查字符串是否为回文
    
    Args:
        text: 要检查的字符串
    
    Returns:
        如果是回文返回True，否则返回False
    """
    # 过滤掉非字母数字字符并转换为小写
    filtered_chars = [char.lower() for char in text if char.isalnum()]
    
    # 创建字符deque
    dq = deque(filtered_chars)
    
    # 从两端比较字符
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True

# 测试回文检查器
test_strings = ["A man, a plan, a canal: Panama", "race a car", "Was it a car or a cat I saw?", "Python"]
for s in test_strings:
    print(f'"{s}" 是回文: {is_palindrome(s)}')

print("\n3.6 实现最近最少使用(LRU)缓存")
print("使用deque可以实现简单的LRU缓存:")

class LRUCache:
    """
    使用deque和字典实现的LRU缓存
    """
    
    def __init__(self, capacity):
        """
        初始化LRU缓存
        
        Args:
            capacity: 缓存的最大容量
        """
        self.capacity = capacity
        self.cache = {}
        self.order = deque()
    
    def get(self, key):
        """
        获取键对应的值
        
        Args:
            key: 要查找的键
        
        Returns:
            如果键存在返回对应的值，否则返回-1
        """
        if key not in self.cache:
            return -1
        
        # 更新访问顺序
        self.order.remove(key)  # 注意：这是O(n)操作，实际LRU实现通常使用双向链表优化
        self.order.append(key)
        
        return self.cache[key]
    
    def put(self, key, value):
        """
        向缓存中添加或更新键值对
        
        Args:
            key: 键
            value: 值
        """
        # 如果键已存在，先移除旧的访问记录
        if key in self.cache:
            self.order.remove(key)
        # 如果缓存已满，移除最久未使用的元素
        elif len(self.cache) >= self.capacity:
            oldest_key = self.order.popleft()
            del self.cache[oldest_key]
        
        # 添加新的键值对和访问记录
        self.cache[key] = value
        self.order.append(key)
    
    def __str__(self):
        """
        返回缓存的字符串表示
        """
        return str({k: self.cache[k] for k in self.order})

# 测试LRU缓存
print("\n测试LRU缓存:")
lru = LRUCache(3)
lru.put(1, "一")
lru.put(2, "二")
lru.put(3, "三")
print(f"初始缓存: {lru}")

lru.get(1)  # 访问1，它应该移到最近使用
print(f"访问1后: {lru}")

lru.put(4, "四")  # 添加4，应该移除最久未使用的2
print(f"添加4后（移除最久未使用的2）: {lru}")

lru.put(3, "三_更新")  # 更新3的值
print(f"更新3后: {lru}")

# 4. 实际应用场景

print("\n=== 4. 实际应用场景 ===")

print("\n4.1 任务调度队列")
print("在需要按顺序处理任务的场景中，deque可以用作高效的任务队列。")
print("例如：处理用户请求、批量处理数据等。")

print("\n4.2 缓存实现")
print("可以使用deque实现各种缓存策略，如LRU（最近最少使用）缓存。")
print("固定大小的deque非常适合实现有限容量的缓存。")

print("\n4.3 历史记录管理")
print("在需要维护最近操作历史的应用中，可以使用固定大小的deque。")
print("例如：浏览历史、命令历史等。")

print("\n4.4 滑动窗口算法")
print("deque是实现滑动窗口算法的理想数据结构，常用于:")
print("  - 最大值/最小值滑动窗口")
print("  - 子数组/子串问题")
print("  - 时间窗口统计等")

print("\n4.5 广度优先搜索(BFS)")
print("在图算法中，特别是广度优先搜索中，deque常被用作队列来管理搜索顺序。")

print("\n4.6 生产者-消费者模式")
print("在多线程编程中，deque可以用作生产者和消费者之间的安全通信渠道。")
print("虽然deque本身不是线程安全的，但可以通过锁机制或使用queue模块来实现线程安全。")

print("\n4.7 文本处理")
print("在文本处理中，deque可以用于:")
print("  - 回文检测")
print("  - 括号匹配")
print("  - 编辑距离计算等")

# 5. 性能分析

print("\n=== 5. 性能分析 ===")

print("\n5.1 时间复杂度")
print("deque的主要操作时间复杂度:")
print("  - append/pop (右端): O(1)")
print("  - appendleft/popleft (左端): O(1)")
print("  - extend/extendleft: O(k)，其中k是添加的元素数量")
print("  - rotate: O(k)，其中k是旋转的位数")
print("  - len(): O(1)")
print("  - in操作符: O(n)")
print("  - count: O(n)")
print("  - remove: O(n)")

print("\n5.2 与list的性能比较")
print("与Python的内置列表相比:")
print("  - deque在两端操作（appendleft/popleft）时性能显著优于list，时间复杂度为O(1) vs O(n)")
print("  - list在随机访问（通过索引）时性能更好")
print("  - deque的内存使用通常比list更高效，尤其是对于频繁的两端操作")

print("\n5.3 内存效率")
print("deque使用了双端链表的变体实现，相比纯链表有更好的内存局部性。")
print("对于大型数据集，deque通常比手动实现的双链表更节省内存。")

# 6. 使用注意事项

print("\n=== 6. 使用注意事项 ===")

print("\n6.1 线程安全性")
print("deque本身不是线程安全的。在多线程环境中，需要使用锁或其他同步机制来保护deque的访问。")
print("对于线程安全的队列，可以考虑使用queue模块中的Queue类。")

print("\n6.2 索引访问效率")
print("虽然deque支持通过索引访问元素，但这不是其主要设计目标，效率不如list高。")
print("对于需要频繁随机访问的场景，list可能是更好的选择。")

print("\n6.3 remove和index方法的效率")
print("deque的remove()和index()方法需要线性时间O(n)，对于大型deque可能性能较差。")
print("如果需要频繁进行这些操作，可能需要考虑使用其他数据结构或算法。")

print("\n6.4 maxlen属性的不可变性")
print("deque的maxlen属性在创建后不能被修改。如果需要更改最大长度，必须创建一个新的deque。")

print("\n6.5 自定义对象的处理")
print("与其他Python容器一样，deque可以存储任意类型的对象，但要注意对象间的比较和排序。")
print("在需要进行比较操作的场景中，确保自定义对象实现了适当的比较方法。")

# 7. 综合示例：多任务调度器

print("\n=== 7. 综合示例：多任务调度器 ===")

print("\n实现一个使用deque的简单多任务调度器，支持任务的添加、执行和优先级管理:")

from collections import deque
import time
import threading

class Task:
    """
    表示一个可执行的任务
    """
    
    def __init__(self, task_id, name, priority=0, callback=None):
        """
        初始化任务
        
        Args:
            task_id: 任务ID
            name: 任务名称
            priority: 任务优先级，数字越小优先级越高
            callback: 任务完成后的回调函数
        """
        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.callback = callback
        self.created_at = time.time()
    
    def __lt__(self, other):
        """
        任务优先级比较
        """
        return self.priority < other.priority
    
    def execute(self):
        """
        执行任务
        """
        print(f"执行任务: {self.name} (ID: {self.task_id}, 优先级: {self.priority})")
        # 模拟任务执行时间
        time.sleep(0.1)
        print(f"任务完成: {self.name}")
        
        # 执行回调
        if self.callback:
            self.callback(self)

class TaskScheduler:
    """
    任务调度器
    使用deque管理待执行的任务队列
    """
    
    def __init__(self):
        """
        初始化任务调度器
        """
        # 不同优先级的任务队列
        self.high_priority_queue = deque()  # 高优先级任务
        self.normal_queue = deque()         # 普通优先级任务
        self.low_priority_queue = deque()   # 低优先级任务
        
        # 历史任务队列（使用固定大小的deque）
        self.history = deque(maxlen=100)
        
        # 锁，用于多线程环境
        self.lock = threading.Lock()
        
        # 调度器运行状态
        self.running = False
        self.worker_thread = None
    
    def add_task(self, task):
        """
        添加任务到调度器
        
        Args:
            task: Task对象
        """
        with self.lock:
            # 根据优先级添加到不同队列
            if task.priority <= 0:
                self.high_priority_queue.append(task)
            elif task.priority <= 10:
                self.normal_queue.append(task)
            else:
                self.low_priority_queue.append(task)
            
            print(f"添加任务: {task.name} (ID: {task.task_id}, 优先级: {task.priority})")
    
    def get_next_task(self):
        """
        获取下一个要执行的任务（按优先级顺序）
        
        Returns:
            下一个要执行的Task对象，如果没有任务则返回None
        """
        with self.lock:
            # 按优先级顺序检查队列
            if self.high_priority_queue:
                return self.high_priority_queue.popleft()
            elif self.normal_queue:
                return self.normal_queue.popleft()
            elif self.low_priority_queue:
                return self.low_priority_queue.popleft()
            return None
    
    def execute_next(self):
        """
        执行下一个任务
        
        Returns:
            如果有任务被执行返回True，否则返回False
        """
        task = self.get_next_task()
        if task:
            # 执行任务
            task.execute()
            
            # 添加到历史记录
            with self.lock:
                self.history.append(task)
            
            return True
        return False
    
    def start(self):
        """
        启动调度器
        """
        with self.lock:
            if self.running:
                print("调度器已经在运行中")
                return
            
            self.running = True
            print("启动任务调度器")
        
        # 创建并启动工作线程
        self.worker_thread = threading.Thread(target=self._worker)
        self.worker_thread.daemon = True
        self.worker_thread.start()
    
    def stop(self):
        """
        停止调度器
        """
        with self.lock:
            if not self.running:
                print("调度器未运行")
                return
            
            self.running = False
            print("停止任务调度器")
        
        # 等待工作线程结束
        if self.worker_thread:
            self.worker_thread.join(timeout=1.0)
    
    def _worker(self):
        """
        工作线程函数，不断检查和执行任务
        """
        while self.running:
            # 尝试执行下一个任务
            if not self.execute_next():
                # 如果没有任务，短暂休眠避免CPU使用率过高
                time.sleep(0.01)
    
    def get_queue_sizes(self):
        """
        获取各队列的大小
        
        Returns:
            包含各队列大小的字典
        """
        with self.lock:
            return {
                "high_priority": len(self.high_priority_queue),
                "normal": len(self.normal_queue),
                "low_priority": len(self.low_priority_queue),
                "history": len(self.history)
            }
    
    def get_recent_history(self, n=10):
        """
        获取最近执行的n个任务
        
        Args:
            n: 要返回的任务数量
        
        Returns:
            最近执行的任务列表
        """
        with self.lock:
            # 由于history是按执行顺序存储的，需要反转来获取最近的任务
            recent = list(self.history)[-n:]
            return recent[::-1]

# 演示多任务调度器
print("\n演示多任务调度器:")

# 创建任务调度器
scheduler = TaskScheduler()

# 定义任务完成回调
def task_callback(task):
    print(f"回调: 任务 '{task.name}' (ID: {task.task_id}) 已完成")

# 创建任务
tasks = [
    Task(1, "系统更新", priority=-5, callback=task_callback),
    Task(2, "数据库备份", priority=3, callback=task_callback),
    Task(3, "日志清理", priority=15, callback=task_callback),
    Task(4, "用户数据同步", priority=2, callback=task_callback),
    Task(5, "安全扫描", priority=-3, callback=task_callback),
    Task(6, "生成报表", priority=5, callback=task_callback),
    Task(7, "缓存刷新", priority=1, callback=task_callback),
    Task(8, "发送邮件通知", priority=8, callback=task_callback)
]

# 添加任务到调度器
print("\n添加任务:")
for task in tasks:
    scheduler.add_task(task)

# 打印队列状态
print("\n初始队列状态:")
sizes = scheduler.get_queue_sizes()
print(f"高优先级队列: {sizes['high_priority']} 个任务")
print(f"普通优先级队列: {sizes['normal']} 个任务")
print(f"低优先级队列: {sizes['low_priority']} 个任务")

# 执行单个任务
print("\n执行单个任务:")
scheduler.execute_next()

# 启动调度器
print("\n启动调度器:")
scheduler.start()

# 等待一段时间让任务执行
print("\n等待任务执行...")
time.sleep(2)

# 再添加一些新任务
print("\n添加更多任务:")
scheduler.add_task(Task(9, "紧急修复", priority=-10, callback=task_callback))
scheduler.add_task(Task(10, "性能监控", priority=0, callback=task_callback))

# 等待更多任务执行
time.sleep(1)

# 停止调度器
print("\n停止调度器:")
scheduler.stop()

# 打印队列最终状态
print("\n最终队列状态:")
sizes = scheduler.get_queue_sizes()
print(f"高优先级队列: {sizes['high_priority']} 个任务")
print(f"普通优先级队列: {sizes['normal']} 个任务")
print(f"低优先级队列: {sizes['low_priority']} 个任务")
print(f"历史任务: {sizes['history']} 个任务")

# 打印最近的历史任务
print("\n最近的历史任务:")
recent_tasks = scheduler.get_recent_history(5)
for i, task in enumerate(recent_tasks, 1):
    print(f"  {i}. {task.name} (ID: {task.task_id}, 优先级: {task.priority})")

# 8. 总结

print("\n=== 8. 总结 ===")

print("\ncollections.deque是Python标准库中提供的高效双端队列实现，它支持在两端进行快速添加和删除操作。")

print("\n主要功能:")
print("1. 提供O(1)时间复杂度的两端添加和删除操作")
print("2. 支持设置最大长度，实现固定大小的队列")
print("3. 提供旋转操作，便于元素位置调整")
print("4. 支持批量添加元素")
print("5. 提供高效的内存使用和操作性能")

print("\n优势:")
print("1. 两端操作的时间复杂度为O(1)，远优于list的O(n)")
print("2. 固定大小的deque自动维护最近的元素，适合实现历史记录和缓存")
print("3. 内存使用比手动实现的双链表更高效")
print("4. 可以作为栈、队列和双端队列使用，用途广泛")
print("5. 与Python的迭代器和生成器完美配合")

print("\n应用场景:")
print("1. 任务调度系统，管理待执行的任务队列")
print("2. 实现LRU等缓存策略")
print("3. 维护操作历史记录")
print("4. 实现滑动窗口算法")
print("5. 广度优先搜索(BFS)算法")
print("6. 生产者-消费者模式的通信渠道")
print("7. 文本处理和字符串操作")

print("\n使用建议:")
print("1. 对于需要频繁在两端操作的场景，优先选择deque而不是list")
print("2. 对于需要固定大小的队列或历史记录，使用maxlen参数创建deque")
print("3. 在多线程环境中使用时，记得添加适当的同步机制")
print("4. 对于需要频繁随机访问的场景，考虑使用list而不是deque")
print("5. 结合其他数据结构和算法，可以实现更复杂的功能")

print("\n通过合理使用collections.deque，可以在Python中高效地实现各种需要频繁在两端操作数据的应用场景，")
print("特别是在性能要求较高的情况下，deque提供的O(1)时间复杂度操作是非常有价值的。")
