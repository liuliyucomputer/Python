# collections.OrderedDict模块 - Python标准库中的有序字典

"""
collections.OrderedDict是Python标准库中提供的一个字典子类，它保持键值对的插入顺序。

在Python 3.7之前，普通字典不保证保持插入顺序，因此OrderedDict在需要维护键值对顺序的场景中非常有用。
即使在Python 3.7+中普通字典已经保证了插入顺序，OrderedDict仍然提供了一些额外的功能，
如move_to_end()方法，可以高效地移动元素到字典的开头或末尾。
"""

# 1. 核心功能介绍

print("=== 1. 核心功能介绍 ===")
print("\ncollections.OrderedDict模块提供了以下主要功能:")
print("1. 保持键值对的插入顺序")
print("2. 支持所有标准字典操作（查找、插入、删除等）")
print("3. 提供额外的方法来操作元素顺序")
print("4. 迭代时按照插入顺序返回键值对")
print("5. 支持反向迭代")
print("6. 比较操作（==, !=）考虑键值对的顺序")

# 2. 基本操作

print("\n=== 2. 基本操作 ===")

# 导入OrderedDict
from collections import OrderedDict

print("\n2.1 创建OrderedDict")
print("可以通过多种方式创建OrderedDict:")

# 基本方式创建空的OrderedDict
od1 = OrderedDict()
print(f"空的OrderedDict: {od1}")

# 从键值对创建
od2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"从列表创建: {od2}")

# 通过关键字参数创建（注意：在Python 3.6+中，关键字参数的顺序也会被保留）
od3 = OrderedDict(a=1, b=2, c=3)
print(f"通过关键字参数创建: {od3}")

# 从普通字典创建（在Python 3.7+中，普通字典也保留插入顺序）
normal_dict = {'x': 10, 'y': 20, 'z': 30}
od4 = OrderedDict(normal_dict)
print(f"从普通字典创建: {od4}")

print("\n2.2 添加和更新元素")
print("添加和更新元素的操作与普通字典类似:")

# 创建OrderedDict
od = OrderedDict()

# 逐个添加元素
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(f"添加元素后: {od}")

# 更新现有元素
od['b'] = 20
print(f"更新元素后: {od}")

# 使用update方法批量添加/更新
od.update({'d': 4, 'e': 5, 'a': 10})
print(f"使用update后: {od}")

# 使用元组列表更新
od.update([('f', 6), ('g', 7)])
print(f"使用元组列表update后: {od}")

print("\n2.3 访问元素")
print("访问元素的方式与普通字典相同:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 通过键访问值
print(f"a的值: {od['a']}")
print(f"b的值: {od['b']}")

# 使用get方法访问（与字典相同）
print(f"c的值: {od.get('c')}")
print(f"不存在的键: {od.get('d', 'default')}")

# 检查键是否存在
print(f"'a'在OrderedDict中: {'a' in od}")
print(f"'d'在OrderedDict中: {'d' in od}")

print("\n2.4 删除元素")
print("可以通过多种方式删除OrderedDict中的元素:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(f"原始OrderedDict: {od}")

# 使用del语句删除
if 'b' in od:
    del od['b']
print(f"删除'b'后: {od}")

# 使用pop方法删除并返回值
value = od.pop('c')
print(f"使用pop删除'c'，返回值: {value}")
print(f"删除后: {od}")

# 使用popitem方法删除并返回最后添加的键值对
item = od.popitem()
print(f"使用popitem删除，返回: {item}")
print(f"删除后: {od}")

# 使用popitem(last=False)删除并返回第一个添加的键值对
item = od.popitem(last=False)
print(f"使用popitem(last=False)删除，返回: {item}")
print(f"删除后: {od}")

# 清空OrderedDict
od.clear()
print(f"清空后: {od}")

print("\n2.5 迭代操作")
print("OrderedDict的迭代操作会按照插入顺序返回键值对:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# 迭代键
print("迭代键:")
for key in od:
    print(f"  {key}")

# 使用keys()方法迭代键
print("使用keys()方法迭代键:")
for key in od.keys():
    print(f"  {key}")

# 迭代值
print("迭代值:")
for value in od.values():
    print(f"  {value}")

# 迭代键值对
print("迭代键值对:")
for key, value in od.items():
    print(f"  {key}: {value}")

# 反向迭代（Python 3.8+）
print("反向迭代:")
for key in reversed(od):
    print(f"  {key}")

# 3. 高级用法

print("\n=== 3. 高级用法 ===")

print("\n3.1 移动元素到末尾")
print("使用move_to_end()方法可以将元素移动到OrderedDict的末尾:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(f"原始OrderedDict: {od}")

# 将'b'移动到末尾
od.move_to_end('b')
print(f"将'b'移动到末尾: {od}")

# 将'a'移动到末尾
od.move_to_end('a')
print(f"将'a'移动到末尾: {od}")

print("\n3.2 移动元素到开头")
print("使用move_to_end(last=False)可以将元素移动到OrderedDict的开头:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(f"原始OrderedDict: {od}")

# 将'd'移动到开头
od.move_to_end('d', last=False)
print(f"将'd'移动到开头: {od}")

# 将'c'移动到开头
od.move_to_end('c', last=False)
print(f"将'c'移动到开头: {od}")

print("\n3.3 顺序敏感的比较")
print("OrderedDict的比较操作（==, !=）会考虑键值对的顺序:")

# 创建具有相同键值但顺序不同的OrderedDict
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# 比较OrderedDict与OrderedDict
print(f"od1 == od2: {od1 == od2}")  # 应该是False，因为顺序不同

# 创建具有相同键值和顺序的OrderedDict
od3 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"od1 == od3: {od1 == od3}")  # 应该是True，因为顺序相同

# 与普通字典比较（在Python 3.7+中，普通字典也保留插入顺序）
d = {'a': 1, 'b': 2, 'c': 3}
print(f"od1 == d: {od1 == d}")  # 在Python 3.7+中是True，因为普通字典也保留顺序

print("\n3.4 反转顺序")
print("可以创建一个顺序反转的新OrderedDict:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(f"原始OrderedDict: {od}")

# 创建反转顺序的新OrderedDict
reversed_od = OrderedDict(reversed(list(od.items())))
print(f"反转顺序后: {reversed_od}")

# 另一种反转方式：使用reversed()
reversed_od2 = OrderedDict()
for key in reversed(od):
    reversed_od2[key] = od[key]
print(f"使用reversed()反转后: {reversed_od2}")

print("\n3.5 排序OrderedDict")
print("可以根据键或值对OrderedDict进行排序:")

# 创建一个未排序的OrderedDict
od = OrderedDict([('c', 3), ('a', 1), ('d', 4), ('b', 2)])
print(f"未排序的OrderedDict: {od}")

# 按键排序
od_sorted_by_key = OrderedDict(sorted(od.items()))
print(f"按键排序后: {od_sorted_by_key}")

# 按值排序
od_sorted_by_value = OrderedDict(sorted(od.items(), key=lambda x: x[1]))
print(f"按值排序后: {od_sorted_by_value}")

# 按键的长度排序（假设键是字符串）
od_str = OrderedDict([('apple', 5), ('banana', 3), ('cherry', 7), ('date', 2)])
od_sorted_by_key_length = OrderedDict(sorted(od_str.items(), key=lambda x: len(x[0])))
print(f"按键长度排序后: {od_sorted_by_key_length}")

print("\n3.6 有序字典的复制")
print("OrderedDict可以通过多种方式进行复制:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 使用copy()方法
od_copy1 = od.copy()
print(f"使用copy()复制: {od_copy1}")

# 创建新的OrderedDict
od_copy2 = OrderedDict(od)
print(f"创建新的OrderedDict: {od_copy2}")

# 使用dict.copy()（会变成普通字典）
d_copy = dict.copy(od)
print(f"使用dict.copy()复制（普通字典）: {d_copy}")
print(f"类型: {type(d_copy).__name__}")

print("\n3.7 与其他数据结构的转换")
print("OrderedDict可以与其他数据结构进行转换:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 转换为列表（元组列表）
list_items = list(od.items())
print(f"转换为元组列表: {list_items}")

# 转换为普通字典
normal_dict = dict(od)
print(f"转换为普通字典: {normal_dict}")

# 转换为集合（只能转换键或值）
keys_set = set(od.keys())
values_set = set(od.values())
print(f"键集合: {keys_set}")
print(f"值集合: {values_set}")

# JSON序列化和反序列化
import json

# 序列化
json_str = json.dumps(od)
print(f"JSON序列化: {json_str}")

# 反序列化（注意：在Python 3.7+中，普通字典也保留顺序）
restored_dict = json.loads(json_str)
restored_od = OrderedDict(restored_dict)
print(f"JSON反序列化为OrderedDict: {restored_od}")

# 4. 实际应用场景

print("\n=== 4. 实际应用场景 ===")

print("\n4.1 LRU缓存实现")
print("OrderedDict非常适合实现LRU（最近最少使用）缓存:")

print("\n示例: 使用OrderedDict实现LRU缓存")

class LRUCache:
    """
    使用OrderedDict实现的LRU缓存
    """
    
    def __init__(self, capacity):
        """
        初始化LRU缓存
        
        Args:
            capacity: 缓存容量
        """
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        """
        获取缓存中的值
        
        Args:
            key: 缓存键
        
        Returns:
            缓存的值，如果键不存在返回None
        """
        if key not in self.cache:
            return None
        
        # 将访问的元素移到末尾（表示最近使用）
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        """
        添加或更新缓存
        
        Args:
            key: 缓存键
            value: 缓存值
        """
        # 如果键已存在，先删除
        if key in self.cache:
            del self.cache[key]
        # 如果缓存已满，删除最久未使用的元素（开头）
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        
        # 添加新元素到末尾（最近使用）
        self.cache[key] = value
    
    def __str__(self):
        """
        返回缓存的字符串表示
        """
        return str(self.cache)

# 测试LRU缓存
cache = LRUCache(3)

# 添加元素
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)
print(f"初始缓存: {cache}")

# 访问元素，会将其移到末尾
print(f"获取'a': {cache.get('a')}")
print(f"访问后缓存: {cache}")

# 添加新元素，超出容量，会删除最久未使用的元素（'b'）
cache.put('d', 4)
print(f"添加'd'后缓存: {cache}")

# 更新已存在的元素
cache.put('c', 30)
print(f"更新'c'后缓存: {cache}")

print("\n4.2 保持配置项顺序")
print("在处理配置文件时，OrderedDict可以保持配置项的顺序:")

print("\n示例: 配置管理")

# 模拟配置文件解析
class ConfigParser:
    """
    简单的配置解析器，保持配置项的顺序
    """
    
    def __init__(self):
        """
        初始化配置解析器
        """
        self.sections = OrderedDict()
    
    def add_section(self, section_name):
        """
        添加配置节
        
        Args:
            section_name: 配置节名称
        """
        if section_name not in self.sections:
            self.sections[section_name] = OrderedDict()
    
    def set(self, section_name, option, value):
        """
        设置配置项
        
        Args:
            section_name: 配置节名称
            option: 配置项名称
            value: 配置项值
        """
        if section_name not in self.sections:
            self.add_section(section_name)
        self.sections[section_name][option] = value
    
    def get(self, section_name, option, default=None):
        """
        获取配置项
        
        Args:
            section_name: 配置节名称
            option: 配置项名称
            default: 默认值
        
        Returns:
            配置项值或默认值
        """
        if section_name in self.sections:
            return self.sections[section_name].get(option, default)
        return default
    
    def __str__(self):
        """
        返回配置的字符串表示
        """
        result = []
        for section, options in self.sections.items():
            result.append(f"[{section}]")
            for option, value in options.items():
                result.append(f"{option} = {value}")
            result.append("")
        return "\n".join(result)

# 测试配置解析器
config = ConfigParser()

# 添加配置节和配置项
config.add_section("database")
config.set("database", "host", "localhost")
config.set("database", "port", "5432")
config.set("database", "user", "postgres")
config.set("database", "password", "secret")

config.add_section("server")
config.set("server", "host", "0.0.0.0")
config.set("server", "port", "8000")
config.set("server", "debug", "false")

print(f"配置内容:\n{config}")
print(f"数据库主机: {config.get('database', 'host')}")
print(f"服务器端口: {config.get('server', 'port')}")

print("\n4.3 任务调度器")
print("在任务调度器中，可以使用OrderedDict来管理任务的执行顺序:")

print("\n示例: 简单的任务调度器")

class TaskScheduler:
    """
    简单的任务调度器，使用OrderedDict管理任务执行顺序
    """
    
    def __init__(self):
        """
        初始化任务调度器
        """
        self.tasks = OrderedDict()
    
    def add_task(self, task_id, task_func, *args, **kwargs):
        """
        添加任务
        
        Args:
            task_id: 任务ID
            task_func: 任务函数
            *args, **kwargs: 任务函数参数
        """
        self.tasks[task_id] = (task_func, args, kwargs)
    
    def remove_task(self, task_id):
        """
        移除任务
        
        Args:
            task_id: 任务ID
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
    
    def move_task_to_front(self, task_id):
        """
        将任务移到队列前面
        
        Args:
            task_id: 任务ID
        """
        if task_id in self.tasks:
            # 保存任务
            task_func, args, kwargs = self.tasks.pop(task_id)
            # 创建新的OrderedDict，将任务放在前面
            new_tasks = OrderedDict()
            new_tasks[task_id] = (task_func, args, kwargs)
            # 添加其他任务
            new_tasks.update(self.tasks)
            self.tasks = new_tasks
    
    def move_task_to_end(self, task_id):
        """
        将任务移到队列末尾
        
        Args:
            task_id: 任务ID
        """
        if task_id in self.tasks:
            # 保存任务
            task_func, args, kwargs = self.tasks.pop(task_id)
            # 重新添加，会自动放到末尾
            self.tasks[task_id] = (task_func, args, kwargs)
    
    def execute_all(self):
        """
        执行所有任务
        """
        results = OrderedDict()
        for task_id, (task_func, args, kwargs) in self.tasks.items():
            try:
                result = task_func(*args, **kwargs)
                results[task_id] = result
            except Exception as e:
                results[task_id] = f"Error: {str(e)}"
        return results
    
    def __str__(self):
        """
        返回任务列表的字符串表示
        """
        return str(list(self.tasks.keys()))

# 测试任务调度器

def task1():
    return "Task 1 executed"

def task2(param):
    return f"Task 2 executed with param: {param}"

def task3(a, b):
    return f"Task 3 executed with a={a}, b={b}"

# 创建任务调度器
scheduler = TaskScheduler()

# 添加任务
scheduler.add_task("task1", task1)
scheduler.add_task("task2", task2, "hello")
scheduler.add_task("task3", task3, 10, 20)

print(f"任务列表: {scheduler}")

# 调整任务顺序
scheduler.move_task_to_front("task3")
print(f"调整顺序后: {scheduler}")

scheduler.move_task_to_end("task1")
print(f"再次调整后: {scheduler}")

# 执行所有任务
results = scheduler.execute_all()
print(f"执行结果: {results}")

print("\n4.4 历史记录和撤销操作")
print("OrderedDict可以用于实现操作历史记录和撤销功能:")

print("\n示例: 简单的编辑器历史记录")

class EditorHistory:
    """
    简单的编辑器历史记录，支持撤销和重做操作
    """
    
    def __init__(self):
        """
        初始化历史记录
        """
        self.history = OrderedDict()  # 存储所有操作
        self.current_state = -1       # 当前状态索引
        self.history_id = 0           # 操作ID计数器
    
    def add_operation(self, operation_type, content):
        """
        添加操作到历史记录
        
        Args:
            operation_type: 操作类型
            content: 操作内容
        """
        # 如果当前不在历史记录的末尾，删除当前状态之后的所有操作
        if self.current_state >= 0 and self.history_id > self.current_state + 1:
            # 获取当前状态之后的操作ID
            ids_to_remove = []
            for op_id in self.history:
                if op_id > self.current_state:
                    ids_to_remove.append(op_id)
            # 删除这些操作
            for op_id in ids_to_remove:
                del self.history[op_id]
        
        # 添加新操作
        self.history[self.history_id] = (operation_type, content)
        self.current_state = self.history_id
        self.history_id += 1
    
    def undo(self):
        """
        撤销操作
        
        Returns:
            被撤销的操作，如果没有可撤销的操作返回None
        """
        if self.current_state < 0:
            return None
        
        operation = self.history[self.current_state]
        self.current_state -= 1
        return operation
    
    def redo(self):
        """
        重做操作
        
        Returns:
            被重做的操作，如果没有可重做的操作返回None
        """
        if self.current_state >= self.history_id - 1:
            return None
        
        self.current_state += 1
        return self.history[self.current_state]
    
    def get_current_state(self):
        """
        获取当前状态
        
        Returns:
            当前状态的操作，如果没有状态返回None
        """
        if self.current_state < 0:
            return None
        return self.history[self.current_state]
    
    def __str__(self):
        """
        返回历史记录的字符串表示
        """
        result = []
        for op_id, (op_type, content) in self.history.items():
            marker = "->" if op_id == self.current_state else "  "
            result.append(f"{marker} {op_id}: {op_type} - {content}")
        return "\n".join(result)

# 测试编辑器历史记录
editor = EditorHistory()

# 添加操作
editor.add_operation("insert", "Hello")
editor.add_operation("insert", "World")
editor.add_operation("delete", "World")
editor.add_operation("insert", "Python")

print(f"历史记录:\n{editor}")

# 撤销操作
print(f"\n撤销操作: {editor.undo()}")
print(f"历史记录:\n{editor}")

print(f"撤销操作: {editor.undo()}")
print(f"历史记录:\n{editor}")

# 重做操作
print(f"\n重做操作: {editor.redo()}")
print(f"历史记录:\n{editor}")

# 添加新操作，会清除重做历史
editor.add_operation("replace", "Python Programming")
print(f"\n添加新操作后:\n{editor}")

print(f"尝试重做: {editor.redo()}")  # 应该返回None，因为重做历史已被清除

print("\n4.5 优先级队列")
print("OrderedDict可以用于实现简单的优先级队列:")

print("\n示例: 优先级任务队列")

class PriorityQueue:
    """
    简单的优先级队列，优先级高的任务先执行
    """
    
    def __init__(self):
        """
        初始化优先级队列
        """
        # 使用OrderedDict存储每个优先级的任务队列
        # 键为优先级（整数，数字越小优先级越高）
        self.queues = OrderedDict()
        self.task_counter = 0  # 用于生成唯一的任务ID
    
    def add_task(self, task, priority=0):
        """
        添加任务到队列
        
        Args:
            task: 任务内容
            priority: 优先级（默认0，数字越小优先级越高）
        
        Returns:
            任务ID
        """
        # 确保优先级是整数
        priority = int(priority)
        
        # 如果该优先级不存在，创建一个新的OrderedDict作为任务队列
        if priority not in self.queues:
            self.queues[priority] = OrderedDict()
            # 重新排序优先级（从小到大）
            self.queues = OrderedDict(sorted(self.queues.items()))
        
        # 生成唯一的任务ID
        task_id = f"task_{self.task_counter}"
        self.task_counter += 1
        
        # 添加任务
        self.queues[priority][task_id] = task
        return task_id
    
    def get_task(self):
        """
        获取优先级最高的任务
        
        Returns:
            任务内容，如果队列为空返回None
        """
        for priority, tasks in self.queues.items():
            if tasks:  # 如果该优先级有任务
                # 获取第一个任务（最早添加的）
                task_id, task = next(iter(tasks.items()))
                # 移除该任务
                del self.queues[priority][task_id]
                # 如果该优先级的任务队列为空，移除该优先级
                if not self.queues[priority]:
                    del self.queues[priority]
                return task
        return None
    
    def is_empty(self):
        """
        检查队列是否为空
        
        Returns:
            如果队列为空返回True，否则返回False
        """
        return len(self.queues) == 0
    
    def get_size(self):
        """
        获取队列中的任务总数
        
        Returns:
            任务总数
        """
        return sum(len(tasks) for tasks in self.queues.values())
    
    def __str__(self):
        """
        返回队列的字符串表示
        """
        result = []
        for priority, tasks in self.queues.items():
            result.append(f"Priority {priority}:")
            for task_id, task in tasks.items():
                result.append(f"  {task_id}: {task}")
        return "\n".join(result)

# 测试优先级队列
queue = PriorityQueue()

# 添加不同优先级的任务
queue.add_task("普通任务1")
queue.add_task("重要任务1", priority=-1)
queue.add_task("紧急任务1", priority=-2)
queue.add_task("普通任务2")
queue.add_task("重要任务2", priority=-1)
queue.add_task("紧急任务2", priority=-2)

print(f"优先级队列:\n{queue}")
print(f"队列大小: {queue.get_size()}")

# 按优先级获取任务
print("\n按优先级获取任务:")
while not queue.is_empty():
    task = queue.get_task()
    print(f"  执行任务: {task}")

print(f"\n队列为空: {queue.is_empty()}")

# 5. 性能分析

print("\n=== 5. 性能分析 ===")

print("\n5.1 时间复杂度")
print("OrderedDict的主要操作时间复杂度:")
print("  - 查找操作(get, []): O(1)")
print("  - 插入操作(setitem): O(1)")
print("  - 删除操作(del, pop, popitem): O(1)")
print("  - move_to_end操作: O(1)")
print("  - 迭代操作: O(n)")

print("\n5.2 与普通字典的性能比较")
print("在Python 3.7之前，普通字典不保证顺序，而OrderedDict保证顺序但性能略低。")
print("在Python 3.7及以后，普通字典也保证插入顺序，但OrderedDict仍然有以下性能差异:")
print("  - 内存消耗：OrderedDict通常比普通字典使用更多的内存，因为需要维护额外的链表结构")
print("  - 操作速度：对于基本操作，普通字典和OrderedDict性能相近，但在某些场景下普通字典略快")
print("  - 特殊操作：OrderedDict提供了move_to_end()等额外方法，这些操作在普通字典中需要重建才能实现")

print("\n5.3 选择建议")
print("根据不同的需求选择合适的数据结构:")
print("  - 如果只需要保持插入顺序，且使用Python 3.7+，普通字典通常是更好的选择")
print("  - 如果需要频繁地调整元素顺序（如移动到开头/末尾），OrderedDict更高效")
print("  - 如果需要顺序敏感的比较操作，OrderedDict会考虑顺序，而普通字典不会")
print("  - 如果需要最大的内存效率，普通字典通常更优")

# 6. 使用注意事项

print("\n=== 6. 使用注意事项 ===")

print("\n6.1 顺序的定义")
print("OrderedDict维护的是插入顺序，而不是键的排序:")

od = OrderedDict()
od['c'] = 3
od['a'] = 1
od['b'] = 2
print(f"插入顺序: {od}")  # 不会按字母顺序排序

print("\n6.2 更新已存在键的值")
print("更新已存在键的值不会改变该键的顺序:")

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"更新前: {od}")

# 更新已存在的键
od['b'] = 20
print(f"更新'b'后: {od}")  # 'b'的位置不变

print("\n6.3 Python版本差异")
print("关于OrderedDict在不同Python版本中的行为差异:")
print("  - Python 3.1到3.6：OrderedDict保证插入顺序，但普通字典不保证")
print("  - Python 3.7+：普通字典也保证插入顺序，但OrderedDict仍然提供额外功能")
print("  - Python 3.8+：OrderedDict支持反向迭代（使用reversed()函数）")

print("\n6.4 内存使用")
print("OrderedDict通常比普通字典使用更多的内存，因为它需要维护额外的数据结构来跟踪顺序:")
print("  - 如果内存使用是关键考虑因素，在Python 3.7+中可以考虑使用普通字典")
print("  - 对于大型数据集，这种内存差异可能会更加明显")

print("\n6.5 序列化和反序列化")
print("在序列化和反序列化OrderedDict时需要注意:")
print("  - JSON序列化会将OrderedDict转换为普通字典，可能会丢失顺序信息（在Python 3.7之前）")
print("  - 在反序列化时，需要显式将结果转换回OrderedDict以恢复其特殊方法")

# 示例：序列化和反序列化
import json

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 序列化
json_str = json.dumps(od)
print(f"JSON序列化: {json_str}")

# 反序列化
restored = json.loads(json_str)
print(f"普通反序列化类型: {type(restored).__name__}")

# 反序列化为OrderedDict
restored_od = OrderedDict(restored)
print(f"转换为OrderedDict: {restored_od}")
print(f"类型: {type(restored_od).__name__}")

print("\n6.6 与比较操作符的行为")
print("OrderedDict的比较操作符（==, !=）会考虑键值对的顺序，而普通字典（在Python 3.7+中）不会:")

od1 = OrderedDict([('a', 1), ('b', 2)])
od2 = OrderedDict([('b', 2), ('a', 1)])
d = {'b': 2, 'a': 1}

print(f"od1 == od2: {od1 == od2}")  # False，因为顺序不同
print(f"od1 == d: {od1 == d}")      # 在Python 3.7+中是True，因为普通字典也保留顺序

# 7. 综合示例：网页爬虫的URL管理器

print("\n=== 7. 综合示例：网页爬虫的URL管理器 ===")

print("\n实现一个使用OrderedDict的URL管理器，用于管理网页爬虫的URL队列，支持优先级、去重和URL状态追踪:")

from collections import OrderedDict
from urllib.parse import urlparse, urljoin
import time

class URLManager:
    """
    网页爬虫的URL管理器
    使用OrderedDict实现URL的优先级管理、去重和状态追踪
    """
    
    # URL状态常量
    STATUS_NEW = 0       # 新发现的URL
    STATUS_FETCHING = 1  # 正在抓取的URL
    STATUS_FETCHED = 2   # 已抓取的URL
    STATUS_ERROR = 3     # 抓取错误的URL
    
    def __init__(self, max_urls=10000):
        """
        初始化URL管理器
        
        Args:
            max_urls: 最大URL数量限制
        """
        # 使用OrderedDict存储URL优先级队列
        # 键为优先级（数字越小优先级越高）
        self.url_queues = OrderedDict()
        
        # 存储URL的状态信息
        self.url_status = {}
        
        # 存储URL的其他信息
        self.url_info = {}
        
        # 最大URL数量限制
        self.max_urls = max_urls
        
        # URL计数器
        self.total_urls = 0
    
    def add_url(self, url, priority=0, **info):
        """
        添加URL到管理器
        
        Args:
            url: 要添加的URL
            priority: 优先级（默认0，数字越小优先级越高）
            **info: URL的附加信息
        
        Returns:
            如果URL成功添加返回True，如果已存在或超出限制返回False
        """
        # 规范化URL
        url = self._normalize_url(url)
        
        # 检查URL是否已存在
        if url in self.url_status:
            return False
        
        # 检查是否超出最大数量限制
        if self.total_urls >= self.max_urls:
            return False
        
        # 确保优先级是整数
        priority = int(priority)
        
        # 如果该优先级不存在，创建一个新的OrderedDict
        if priority not in self.url_queues:
            self.url_queues[priority] = OrderedDict()
            # 重新排序优先级（从小到大）
            self.url_queues = OrderedDict(sorted(self.url_queues.items()))
        
        # 添加URL到对应优先级的队列
        self.url_queues[priority][url] = None
        
        # 设置URL状态
        self.url_status[url] = self.STATUS_NEW
        
        # 设置URL附加信息
        self.url_info[url] = {
            'added_time': time.time(),
            'priority': priority,
            **info
        }
        
        # 更新计数器
        self.total_urls += 1
        
        return True
    
    def add_urls(self, urls, priority=0, **info):
        """
        批量添加URL
        
        Args:
            urls: URL列表
            priority: 优先级
            **info: URL的附加信息
        
        Returns:
            添加成功的URL数量
        """
        added_count = 0
        for url in urls:
            if self.add_url(url, priority, **info):
                added_count += 1
        return added_count
    
    def get_next_url(self):
        """
        获取下一个待抓取的URL（按优先级）
        
        Returns:
            下一个URL，如果没有则返回None
        """
        for priority, url_queue in self.url_queues.items():
            if url_queue:
                # 获取第一个URL
                url = next(iter(url_queue.keys()))
                
                # 从队列中移除
                del self.url_queues[priority][url]
                
                # 如果队列为空，删除该优先级
                if not self.url_queues[priority]:
                    del self.url_queues[priority]
                
                # 更新URL状态为正在抓取
                self.url_status[url] = self.STATUS_FETCHING
                self.url_info[url]['fetch_start_time'] = time.time()
                
                return url
        
        return None
    
    def mark_fetched(self, url, status_code=200, content_length=None, **info):
        """
        标记URL为已抓取
        
        Args:
            url: URL
            status_code: HTTP状态码
            content_length: 内容长度
            **info: 其他抓取信息
        """
        url = self._normalize_url(url)
        if url in self.url_status:
            self.url_status[url] = self.STATUS_FETCHED
            self.url_info[url].update({
                'fetch_end_time': time.time(),
                'status_code': status_code,
                'content_length': content_length,
                **info
            })
    
    def mark_error(self, url, error=None, **info):
        """
        标记URL为抓取错误
        
        Args:
            url: URL
            error: 错误信息
            **info: 其他信息
        """
        url = self._normalize_url(url)
        if url in self.url_status:
            self.url_status[url] = self.STATUS_ERROR
            self.url_info[url].update({
                'fetch_end_time': time.time(),
                'error': error,
                **info
            })
    
    def retry_url(self, url, new_priority=None):
        """
        重试抓取失败的URL
        
        Args:
            url: URL
            new_priority: 新的优先级（可选）
        
        Returns:
            如果成功重试返回True，否则返回False
        """
        url = self._normalize_url(url)
        if url in self.url_status and self.url_status[url] == self.STATUS_ERROR:
            # 获取原始优先级
            priority = self.url_info[url]['priority']
            if new_priority is not None:
                priority = new_priority
            
            # 获取URL信息
            info = self.url_info[url].copy()
            
            # 增加重试次数
            info['retry_count'] = info.get('retry_count', 0) + 1
            
            # 从当前状态中移除
            del self.url_status[url]
            del self.url_info[url]
            self.total_urls -= 1
            
            # 重新添加
            return self.add_url(url, priority, **info)
        
        return False
    
    def update_priority(self, url, new_priority):
        """
        更新URL的优先级
        
        Args:
            url: URL
            new_priority: 新的优先级
        
        Returns:
            如果成功更新返回True，否则返回False
        """
        url = self._normalize_url(url)
        if url in self.url_status and self.url_status[url] == self.STATUS_NEW:
            # 获取URL信息
            info = self.url_info[url].copy()
            
            # 从当前队列中移除（需要查找所在的优先级队列）
            removed = False
            for priority, url_queue in self.url_queues.items():
                if url in url_queue:
                    del self.url_queues[priority][url]
                    # 如果队列为空，删除该优先级
                    if not self.url_queues[priority]:
                        del self.url_queues[priority]
                    removed = True
                    break
            
            if removed:
                # 更新优先级
                info['priority'] = new_priority
                
                # 重新添加到新优先级队列
                if new_priority not in self.url_queues:
                    self.url_queues[new_priority] = OrderedDict()
                    # 重新排序优先级
                    self.url_queues = OrderedDict(sorted(self.url_queues.items()))
                
                self.url_queues[new_priority][url] = None
                self.url_info[url] = info
                
                return True
        
        return False
    
    def get_status_count(self):
        """
        获取各状态URL的数量
        
        Returns:
            包含各状态URL数量的字典
        """
        counts = {
            'new': 0,
            'fetching': 0,
            'fetched': 0,
            'error': 0
        }
        
        for status in self.url_status.values():
            if status == self.STATUS_NEW:
                counts['new'] += 1
            elif status == self.STATUS_FETCHING:
                counts['fetching'] += 1
            elif status == self.STATUS_FETCHED:
                counts['fetched'] += 1
            elif status == self.STATUS_ERROR:
                counts['error'] += 1
        
        return counts
    
    def get_url_info(self, url):
        """
        获取URL的详细信息
        
        Args:
            url: URL
        
        Returns:
            URL信息字典，如果URL不存在返回None
        """
        url = self._normalize_url(url)
        return self.url_info.get(url)
    
    def has_pending_urls(self):
        """
        检查是否有待处理的URL
        
        Returns:
            如果有待处理的URL返回True，否则返回False
        """
        return any(len(queue) > 0 for queue in self.url_queues.values())
    
    def get_pending_count(self):
        """
        获取待处理的URL数量
        
        Returns:
            待处理的URL数量
        """
        return sum(len(queue) for queue in self.url_queues.values())
    
    def _normalize_url(self, url):
        """
        规范化URL
        
        Args:
            url: 原始URL
        
        Returns:
            规范化后的URL
        """
        # 这里可以添加更复杂的URL规范化逻辑
        # 例如：处理相对路径、移除冗余参数等
        return url.strip()
    
    def __str__(self):
        """
        返回URL管理器的字符串表示
        """
        counts = self.get_status_count()
        return (
            f"URL Manager:\n"  
            f"  总URL数: {self.total_urls}\n"  
            f"  待抓取: {counts['new']}\n"  
            f"  抓取中: {counts['fetching']}\n"  
            f"  已抓取: {counts['fetched']}\n"  
            f"  抓取失败: {counts['error']}\n"  
            f"  优先级队列: {len(self.url_queues)}"
        )

# 演示URL管理器
print("\n演示网页爬虫的URL管理器:")

# 创建URL管理器
url_manager = URLManager()

# 添加不同优先级的URL
url_manager.add_url("https://example.com", priority=-2, source="seed")
url_manager.add_url("https://example.com/page1", priority=-1, source="homepage")
url_manager.add_url("https://example.com/page2", source="homepage")
url_manager.add_url("https://example.com/page3", priority=1, source="page1")
url_manager.add_url("https://example.com/page4", priority=-1, source="page1")

# 尝试添加重复URL
result = url_manager.add_url("https://example.com")
print(f"添加重复URL的结果: {result}")

# 显示URL管理器状态
print(f"\nURL管理器状态:\n{url_manager}")

# 获取下一个URL（应该按优先级顺序）
print("\n按优先级获取URL:")
while url_manager.has_pending_urls():
    url = url_manager.get_next_url()
    info = url_manager.get_url_info(url)
    print(f"  获取URL: {url}")
    print(f"    优先级: {info['priority']}")
    print(f"    来源: {info['source']}")
    
    # 模拟抓取
    if "page3" in url:
        # 模拟抓取失败
        url_manager.mark_error(url, error="Connection timeout")
        print(f"    状态: 抓取失败")
    else:
        # 模拟抓取成功
        url_manager.mark_fetched(url, status_code=200, content_length=1024)
        print(f"    状态: 抓取成功")

# 显示URL管理器状态
print(f"\nURL管理器状态（抓取后）:\n{url_manager}")

# 重试失败的URL
print("\n重试失败的URL:")
result = url_manager.retry_url("https://example.com/page3", new_priority=-1)
print(f"重试结果: {result}")

# 再次获取URL
url = url_manager.get_next_url()
print(f"获取重试的URL: {url}")
url_manager.mark_fetched(url, status_code=200, content_length=2048)

# 显示最终状态
print(f"\nURL管理器最终状态:\n{url_manager}")

# 8. 总结

print("\n=== 8. 总结 ===")

print("\ncollections.OrderedDict是Python标准库中提供的一个字典子类，它保持键值对的插入顺序。")

print("\n主要功能:")
print("1. 保持键值对的插入顺序")
print("2. 支持所有标准字典操作")
print("3. 提供move_to_end()等额外方法来操作元素顺序")
print("4. 支持顺序敏感的比较操作")
print("5. 支持反向迭代（Python 3.8+）")

print("\n优势:")
print("1. 提供明确的键值对顺序保证，无论Python版本如何")
print("2. 可以高效地调整元素顺序，而不需要重建整个字典")
print("3. 顺序敏感的比较操作可以检测顺序差异")
print("4. 在需要维护插入顺序的场景中提供了可靠的行为")

print("\n限制:")
print("1. 通常比普通字典使用更多的内存")
print("2. 在某些操作上可能比普通字典稍慢")
print("3. 在Python 3.7+中，普通字典已经提供了插入顺序保证，减少了OrderedDict的部分使用场景")

print("\n应用场景:")
print("1. 实现LRU缓存和其他需要频繁调整顺序的数据结构")
print("2. 配置管理，需要保持配置项的顺序")
print("3. 任务调度器，按照添加顺序或优先级执行任务")
print("4. 历史记录和撤销/重做功能")
print("5. 优先级队列，根据优先级和插入顺序处理元素")
print("6. 需要顺序敏感比较的场景")

print("\n使用建议:")
print("1. 在Python 3.7+中，如果只需要保持插入顺序，普通字典通常是更好的选择")
print("2. 如果需要频繁地调整元素顺序或需要顺序敏感的比较，仍然建议使用OrderedDict")
print("3. 对于LRU缓存等需要移动元素到开头或末尾的场景，OrderedDict的move_to_end()方法非常高效")
print("4. 在处理大型数据集时，需要注意OrderedDict的额外内存消耗")

print("\ncollections.OrderedDict在Python标准库中扮演着重要的角色，特别是在需要维护键值对顺序的场景中。")
print("虽然在Python 3.7+中普通字典已经提供了插入顺序保证，但OrderedDict仍然是实现复杂数据结构")
print("和算法的强大工具，特别是在需要高效地操作元素顺序的场景中。")
