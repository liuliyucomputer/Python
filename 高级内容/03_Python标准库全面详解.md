# Python标准库全面详解

## 1. 集合数据类型扩展 (collections)

### 1.1 collections模块核心数据结构
**[标识: STD-COLLECTIONS-001]**

collections模块提供了许多扩展的集合数据类型，这些类型比Python内置的list、dict、set和tuple更加灵活和强大。

```python
# collections模块核心数据结构示例

from collections import (
    namedtuple, deque, ChainMap, Counter, OrderedDict,
    defaultdict, UserDict, UserList, UserString
)
import time

# 1. namedtuple - 命名元组
print("=== 1. namedtuple ===")

# 定义一个命名元组类
Point = namedtuple('Point', ['x', 'y', 'z'])

# 创建命名元组实例
p1 = Point(1, 2, 3)
p2 = Point(x=4, y=5, z=6)

print(f"p1: {p1}")
print(f"p1.x: {p1.x}, p1.y: {p1.y}, p1.z: {p1.z}")
print(f"p1[0]: {p1[0]}, p1[1]: {p1[1]}")  # 支持索引访问

# 解包操作
x, y, z = p2
print(f"解包: x={x}, y={y}, z={z}")

# 命名元组是不可变的
# p1.x = 10  # 会抛出AttributeError

# 转换为字典
p1_dict = p1._asdict()
print(f"转换为字典: {p1_dict}")

# 替换字段值（返回新实例）
p1_updated = p1._replace(x=10)
print(f"替换后的p1: {p1_updated}")
print(f"原p1保持不变: {p1}")

# 2. deque - 双端队列
print("\n=== 2. deque ===")

# 创建双端队列
dq = deque([1, 2, 3, 4])
print(f"初始deque: {dq}")

# 在两端添加元素
dq.append(5)  # 右端添加
print(f"append后: {dq}")

dq.appendleft(0)  # 左端添加
print(f"appendleft后: {dq}")

# 在两端移除元素
right_val = dq.pop()  # 右端移除
print(f"pop后: {dq}, 移除的值: {right_val}")

left_val = dq.popleft()  # 左端移除
print(f"popleft后: {dq}, 移除的值: {left_val}")

# 扩展队列
dq.extend([6, 7, 8])  # 右端扩展
print(f"extend后: {dq}")

dq.extendleft([-1, -2, -3])  # 左端扩展，注意顺序
print(f"extendleft后: {dq}")

# 旋转
dq.rotate(1)  # 向右旋转1位
print(f"向右旋转1位: {dq}")

dq.rotate(-2)  # 向左旋转2位
print(f"向左旋转2位: {dq}")

# 限制最大长度
dq = deque(maxlen=5)
dq.extend([1, 2, 3, 4, 5])
print(f"限制长度的deque: {dq}")
dq.append(6)  # 添加新元素会自动移除最左侧元素
print(f"添加新元素后: {dq}")  # 注意1被移除了

# 性能对比：deque vs list 用于首尾操作
print("\n=== deque vs list 性能对比 ===")

# 创建大列表和大deque
large_list = list(range(1000000))
large_deque = deque(range(1000000))

# 测量列表左侧插入时间
start = time.time()
for _ in range(1000):
    large_list.insert(0, -1)
list_time = time.time() - start
print(f"列表左侧插入1000次时间: {list_time:.6f}秒")

# 测量deque左侧插入时间
start = time.time()
for _ in range(1000):
    large_deque.appendleft(-1)
deque_time = time.time() - start
print(f"deque左侧插入1000次时间: {deque_time:.6f}秒")
print(f"性能提升: {list_time / deque_time:.2f}倍")

# 3. Counter - 计数器
print("\n=== 3. Counter ===")

# 从可迭代对象创建计数器
counter = Counter('abracadabra')
print(f"字符计数: {counter}")

# 从字典创建计数器
counter2 = Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
print(f"字典创建计数器: {counter2}")

# 访问计数
print(f"'a'出现次数: {counter['a']}")
print(f"'z'出现次数: {counter['z']}")  # 不存在的键返回0

# 更新计数
counter.update('aaaaazzz')
print(f"更新后的计数: {counter}")

# 减少计数
counter.subtract('aaa')
print(f"减少后的计数: {counter}")

# 获取最常见的元素
print(f"最常见的3个元素: {counter.most_common(3)}")

# 计数器算术运算
counter3 = Counter('abcabc')
counter4 = Counter('abx')
print(f"counter3: {counter3}")
print(f"counter4: {counter4}")
print(f"counter3 + counter4: {counter3 + counter4}")
print(f"counter3 - counter4: {counter3 - counter4}")  # 只保留正数计数
print(f"counter3 & counter4: {counter3 & counter4}")  # 交集：最小值
print(f"counter3 | counter4: {counter3 | counter4}")  # 并集：最大值

# 4. defaultdict - 默认字典
print("\n=== 4. defaultdict ===")

# 创建默认值为list的defaultdict
word_list = [
    'apple', 'banana', 'cherry', 'date',
    'elderberry', 'fig', 'grape', 'kiwi'
]

# 使用普通dict统计首字母
normal_dict = {}
for word in word_list:
    first_letter = word[0]
    if first_letter not in normal_dict:
        normal_dict[first_letter] = []
    normal_dict[first_letter].append(word)
print(f"普通dict统计: {normal_dict}")

# 使用defaultdict统计首字母
def_dict = defaultdict(list)
for word in word_list:
    first_letter = word[0]
    def_dict[first_letter].append(word)
print(f"defaultdict统计: {dict(def_dict)}")  # 转换为普通dict以便打印

# 使用int作为默认工厂（计数）
letter_counts = defaultdict(int)
for word in word_list:
    for letter in word:
        letter_counts[letter] += 1
print(f"字母计数: {dict(letter_counts)}")

# 使用set作为默认工厂（去重集合）
letter_sets = defaultdict(set)
for word in word_list:
    for letter in word:
        letter_sets[word].add(letter)
print(f"单词字母集合: {dict(letter_sets)}")

# 使用lambda作为默认工厂
custom_default = defaultdict(lambda: 'Not Present')
custom_default['a'] = 'Present'
print(f"存在的键: {custom_default['a']}")
print(f"不存在的键: {custom_default['x']}")

# 5. OrderedDict - 有序字典
print("\n=== 5. OrderedDict ===")

# 创建OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
print(f"OrderedDict: {od}")

# 注意：Python 3.7+中，普通dict也保持插入顺序，但OrderedDict有额外功能

# 移动键到末尾
od.move_to_end('a')
print(f"移动'a'到末尾: {od}")

# 移动键到开头
od.move_to_end('d', last=False)
print(f"移动'd'到开头: {od}")

# 反向迭代
print(f"反向迭代: {list(reversed(od))}")

# 比较两个OrderedDict的顺序
od1 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od2 = OrderedDict([('b', 2), ('a', 1), ('c', 3)])
print(f"od1 == od2: {od1 == od2}")  # 顺序不同，所以不相等
print(f"dict(od1) == dict(od2): {dict(od1) == dict(od2)}")  # 普通dict只比较键值对

# 6. ChainMap - 链式映射
print("\n=== 6. ChainMap ===")

# 创建多个字典
config_default = {'debug': False, 'log_level': 'INFO', 'timeout': 30}
config_user = {'log_level': 'DEBUG', 'timeout': 60}
config_session = {'debug': True}

# 创建ChainMap
config = ChainMap(config_session, config_user, config_default)
print(f"ChainMap: {config}")

# 查找键（按顺序查找，找到第一个就返回）
print(f"debug值: {config['debug']}")  # 从config_session中获取
print(f"log_level值: {config['log_level']}")  # 从config_user中获取
print(f"timeout值: {config['timeout']}")  # 从config_user中获取

# 修改ChainMap中的值（只修改第一个映射中的值）
config['timeout'] = 120
print(f"修改后的timeout: {config['timeout']}")
print(f"config_user中的timeout: {config_user['timeout']}")  # 已被修改

# 新增键（只添加到第一个映射中）
config['max_retries'] = 5
print(f"config_session: {config_session}")  # 已添加新键

# 获取所有映射的列表
print(f"所有映射: {config.maps}")

# 反转查找顺序
reversed_config = config.new_child()
print(f"反转后的ChainMap: {reversed_config}")

# 7. 用户自定义容器类
print("\n=== 7. 用户自定义容器类 ===")

# UserDict - 字典的包装器
class CustomDict(UserDict):
    def __getitem__(self, key):
        print(f"获取键: {key}")
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        print(f"设置键: {key} = {value}")
        super().__setitem__(key, value)

custom_dict = CustomDict({'a': 1, 'b': 2})
custom_dict['c'] = 3
print(f"自定义字典: {custom_dict}")
print(f"访问键'a': {custom_dict['a']}")

# UserList - 列表的包装器
class CustomList(UserList):
    def append(self, item):
        print(f"添加项: {item}")
        super().append(item)
    
    def __getitem__(self, index):
        print(f"获取索引: {index}")
        return super().__getitem__(index)

custom_list = CustomList([1, 2, 3])
custom_list.append(4)
print(f"自定义列表: {custom_list}")
print(f"访问索引0: {custom_list[0]}")

# UserString - 字符串的包装器
class CustomString(UserString):
    def upper(self):
        print("调用upper方法")
        return super().upper()
    
    def append(self, s):
        """添加自定义方法"""
        self.data += s

custom_string = CustomString("Hello")
print(f"原始字符串: {custom_string}")
print(f"大写字符串: {custom_string.upper()}")
custom_string.append(" World")
print(f"追加后字符串: {custom_string}")
```

### 1.2 collections应用场景与最佳实践
**[标识: STD-COLLECTIONS-002]**

collections模块提供的扩展数据结构在各种实际场景中都能发挥重要作用，下面展示一些典型应用场景和最佳实践。

```python
# collections模块应用场景与最佳实践

from collections import (
    namedtuple, deque, Counter, defaultdict, OrderedDict,
    ChainMap, UserDict, UserList
)
import heapq

# 1. 数据建模与结构化数据处理
print("=== 1. 数据建模与结构化数据处理 ===")

# 使用namedtuple建模数据记录
Employee = namedtuple('Employee', ['id', 'name', 'department', 'salary'])

# 创建员工记录
employees = [
    Employee(1, 'Alice', 'Engineering', 100000),
    Employee(2, 'Bob', 'Marketing', 85000),
    Employee(3, 'Charlie', 'Engineering', 120000),
    Employee(4, 'Diana', 'Sales', 95000),
    Employee(5, 'Ethan', 'Engineering', 90000)
]

# 按部门分组员工
dept_employees = defaultdict(list)
for emp in employees:
    dept_employees[emp.department].append(emp)

# 显示每个部门的员工
for dept, emp_list in dept_employees.items():
    print(f"\n部门: {dept}")
    for emp in emp_list:
        print(f"  - {emp.name}, 薪资: ${emp.salary:,}")

# 计算每个部门的平均薪资
for dept, emp_list in dept_employees.items():
    avg_salary = sum(emp.salary for emp in emp_list) / len(emp_list)
    print(f"{dept}部门平均薪资: ${avg_salary:,.2f}")

# 2. 高效的缓存实现
print("\n=== 2. 高效的缓存实现 ===")

# 使用OrderedDict实现LRU（最近最少使用）缓存
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        super().__init__()
    
    def __getitem__(self, key):
        # 访问项目时，将其移到末尾（最近使用）
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value
    
    def __setitem__(self, key, value):
        # 如果键已存在，先移动到末尾
        if key in self:
            self.move_to_end(key)
        # 如果超出容量，删除最不常使用的项目（开头）
        elif len(self) >= self.capacity:
            self.popitem(last=False)
        # 设置新值
        super().__setitem__(key, value)

# 测试LRU缓存
cache = LRUCache(3)

# 添加项目
cache['a'] = 1
cache['b'] = 2
cache['c'] = 3
print(f"初始缓存: {dict(cache)}")

# 访问'a'，它会移到末尾
print(f"访问'a': {cache['a']}")
print(f"缓存状态: {dict(cache)}")

# 添加新项目'd'，会淘汰'b'
cache['d'] = 4
print(f"添加'd'后: {dict(cache)}")  # 'b'被淘汰

# 再次访问'c'，它会移到末尾
print(f"访问'c': {cache['c']}")
print(f"缓存状态: {dict(cache)}")

# 3. 文本处理与分析
print("\n=== 3. 文本处理与分析 ===")

# 示例文本
text = """Python is a high-level, interpreted, general-purpose programming language. 
Its design philosophy emphasizes code readability with the use of significant indentation. 
Python is dynamically-typed and garbage-collected. 
It supports multiple programming paradigms, including structured, object-oriented and functional programming."""

# 使用Counter进行词频分析
# 预处理文本
import re
words = re.findall(r'\b\w+\b', text.lower())

# 计算词频
word_counts = Counter(words)

print("文本词频分析:")
print(f"总单词数: {len(words)}")
print(f"不同单词数: {len(word_counts)}")
print("\n最常见的10个单词:")
for word, count in word_counts.most_common(10):
    print(f"  - '{word}': {count}次")

# 找出长度大于5的单词
long_words = [word for word in words if len(word) > 5]
long_word_counts = Counter(long_words)
print("\n长度大于5的单词计数:")
for word, count in long_word_counts.most_common(5):
    print(f"  - '{word}': {count}次")

# 4. 图算法实现
print("\n=== 4. 图算法实现 ===")

# 使用defaultdict表示图的邻接表
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # 无向图
    
    def bfs(self, start):
        """广度优先搜索"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()
    
    def dfs(self, start):
        """深度优先搜索"""
        visited = set()
        self._dfs_recursive(start, visited)
        print()
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

# 创建图并添加边
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

print("广度优先搜索 (从节点0开始):")
g.bfs(0)

print("深度优先搜索 (从节点0开始):")
g.dfs(0)

# 5. 配置管理
print("\n=== 5. 配置管理 ===")

# 使用ChainMap管理多层配置
def create_config():
    # 默认配置
    default_config = {
        'database': {
            'host': 'localhost',
            'port': 5432,
            'timeout': 30
        },
        'logging': {
            'level': 'INFO',
            'file': 'app.log'
        },
        'app': {
            'debug': False,
            'max_connections': 10
        }
    }
    
    # 环境特定配置（例如生产环境）
    env_config = {
        'database': {
            'host': 'db.example.com',
            'timeout': 60
        },
        'app': {
            'max_connections': 100
        }
    }
    
    # 用户配置
    user_config = {
        'logging': {
            'level': 'DEBUG'
        },
        'app': {
            'debug': True
        }
    }
    
    # 创建配置字典的ChainMap
    from collections import ChainMap
    
    # 注意：这里我们只对顶级键使用ChainMap
    # 对于嵌套字典，我们需要递归地应用ChainMap或使用特殊处理
    config = {}
    
    for key in set(default_config) | set(env_config) | set(user_config):
        # 获取所有层级中该键的值
        dicts = []
        if key in user_config:
            dicts.append(user_config[key])
        if key in env_config:
            dicts.append(env_config[key])
        if key in default_config:
            dicts.append(default_config[key])
        
        # 如果值是字典，递归创建ChainMap
        if all(isinstance(d, dict) for d in dicts):
            config[key] = ChainMap(*dicts)
        # 否则使用第一个非None值
        else:
            config[key] = next((d for d in dicts if d is not None), None)
    
    return ChainMap(config)

# 创建和使用配置
config = create_config()
print("配置示例:")
print(f"数据库主机: {config['database']['host']}")
print(f"数据库端口: {config['database']['port']}")
print(f"日志级别: {config['logging']['level']}")
print(f"调试模式: {config['app']['debug']}")
print(f"最大连接数: {config['app']['max_connections']}")

# 6. 优先级队列实现
print("\n=== 6. 优先级队列实现 ===")

# 使用heapq和Counter实现任务优先级队列
class PriorityQueue:
    def __init__(self):
        self.heap = []  # 存储(优先级, 计数, 任务)
        self.counter = Counter()  # 用于确保同优先级任务的FIFO顺序
    
    def push(self, priority, task):
        """添加任务到队列，优先级数字越小越优先"""
        count = self.counter[priority]
        self.counter[priority] += 1
        heapq.heappush(self.heap, (priority, count, task))
    
    def pop(self):
        """移除并返回优先级最高的任务"""
        if self.heap:
            return heapq.heappop(self.heap)[2]
        raise IndexError("Priority queue is empty")
    
    def is_empty(self):
        """检查队列是否为空"""
        return len(self.heap) == 0

# 测试优先级队列
queue = PriorityQueue()

# 添加任务（优先级：1=最高，5=最低）
queue.push(3, "普通任务1")
queue.push(1, "紧急任务1")
queue.push(5, "低优先级任务1")
queue.push(1, "紧急任务2")
queue.push(3, "普通任务2")

print("按优先级顺序处理任务:")
while not queue.is_empty():
    task = queue.pop()
    print(f"  - {task}")

# 7. 自定义集合类的最佳实践
print("\n=== 7. 自定义集合类的最佳实践 ===")

# 继承UserDict创建高级字典类
class EnhancedDict(UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def get_nested(self, keys, default=None):
        """获取嵌套键的值"""
        d = self.data
        for key in keys:
            if not isinstance(d, dict) or key not in d:
                return default
            d = d[key]
        return d
    
    def set_nested(self, keys, value):
        """设置嵌套键的值"""
        d = self.data
        for key in keys[:-1]:
            if key not in d or not isinstance(d[key], dict):
                d[key] = {}
            d = d[key]
        d[keys[-1]] = value
    
    def flatten(self, parent_key='', sep='.'):
        """将嵌套字典展平"""
        items = []
        for k, v in self.data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(EnhancedDict(v).flatten(new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return EnhancedDict(items)

# 测试增强字典
nested_dict = EnhancedDict({
    'database': {
        'primary': {
            'host': 'db1.example.com',
            'port': 5432
        },
        'replica': {
            'host': 'db2.example.com',
            'port': 5432
        }
    },
    'api': {
        'version': 'v2',
        'timeout': 30
    }
})

# 获取嵌套值
print("获取嵌套值:")
print(f"主数据库主机: {nested_dict.get_nested(['database', 'primary', 'host'])}")
print(f"不存在的键: {nested_dict.get_nested(['database', 'secondary', 'host'], 'not found')}")

# 设置嵌套值
nested_dict.set_nested(['database', 'primary', 'user'], 'admin')
print(f"设置后的用户: {nested_dict.get_nested(['database', 'primary', 'user'])}")

# 展平字典
flattened = nested_dict.flatten()
print("\n展平后的字典:")
for key, value in flattened.items():
    print(f"  - {key}: {value}")
```

## 2. 迭代器与生成器工具 (itertools)

### 2.1 itertools模块核心函数
**[标识: STD-ITERTOOLS-001]**

itertools模块提供了一系列用于高效循环的迭代器函数，这些函数可以帮助我们创建各种复杂的迭代模式。

```python
# itertools模块核心函数示例

import itertools
import operator
from itertools import (
    count, cycle, repeat,
    chain, zip_longest, product, permutations, combinations, combinations_with_replacement,
    groupby, filterfalse, dropwhile, takewhile, accumulate,
    starmap, tee
)

# 1. 无限迭代器
print("=== 1. 无限迭代器 ===")

# count - 从start开始，步长为step的无限序列
print("count(10, 2)的前5个元素:")
for i, num in enumerate(count(10, 2)):
    print(f"  {num}")
    if i >= 4:  # 只显示前5个
        break

# cycle - 无限循环迭代序列
print("\ncycle(['A', 'B', 'C'])的前7个元素:")
for i, item in enumerate(itertools.cycle(['A', 'B', 'C'])):
    print(f"  {item}")
    if i >= 6:  # 只显示前7个
        break

# repeat - 重复元素
print("\nrepeat(5, 3)的所有元素:")
for item in repeat(5, 3):
    print(f"  {item}")

print("\nrepeat('hello')的前4个元素:")
for i, item in enumerate(repeat('hello')):
    print(f"  {item}")
    if i >= 3:  # 只显示前4个
        break

# 2. 迭代器组合函数
print("\n=== 2. 迭代器组合函数 ===")

# chain - 链接多个迭代器
iter1 = [1, 2, 3]
iter2 = ['a', 'b', 'c']
iter3 = (4, 5, 6)

print("chain多个迭代器:")
for item in chain(iter1, iter2, iter3):
    print(f"  {item}")

# chain.from_iterable - 从可迭代对象中链接迭代器
nested_iter = [[1, 2], ['a', 'b'], (3, 4)]
print("\nchain.from_iterable链接嵌套迭代器:")
for item in chain.from_iterable(nested_iter):
    print(f"  {item}")

# zip_longest - 类似于zip，但会以fillvalue填充较短迭代器
print("\nzip_longest([1, 2, 3], ['a', 'b'], fillvalue=None):")
for item in zip_longest([1, 2, 3], ['a', 'b'], fillvalue=None):
    print(f"  {item}")

# product - 笛卡尔积
print("\nproduct([1, 2], ['a', 'b']):")
for item in product([1, 2], ['a', 'b']):
    print(f"  {item}")

print("\nproduct([1, 2], repeat=3):")
for item in product([1, 2], repeat=3):
    print(f"  {item}")

# permutations - 排列
print("\npermutations(['a', 'b', 'c'], 2):")
for item in permutations(['a', 'b', 'c'], 2):
    print(f"  {item}")

# combinations - 组合（不考虑顺序，元素不重复）
print("\ncombinations(['a', 'b', 'c', 'd'], 2):")
for item in combinations(['a', 'b', 'c', 'd'], 2):
    print(f"  {item}")

# combinations_with_replacement - 允许重复元素的组合
print("\ncombinations_with_replacement([1, 2, 3], 2):")
for item in combinations_with_replacement([1, 2, 3], 2):
    print(f"  {item}")

# 3. 迭代器过滤函数
print("\n=== 3. 迭代器过滤函数 ===")

# filterfalse - 返回不满足条件的元素
print("filterfalse(lambda x: x % 2 == 0, range(10)):")
for item in filterfalse(lambda x: x % 2 == 0, range(10)):
    print(f"  {item}")

# dropwhile - 丢弃满足条件的元素，直到遇到第一个不满足条件的元素
print("\ndropwhile(lambda x: x < 5, range(10)):")
for item in dropwhile(lambda x: x < 5, range(10)):
    print(f"  {item}")

# takewhile - 获取满足条件的元素，直到遇到第一个不满足条件的元素
print("\ntakewhile(lambda x: x < 5, range(10)):")
for item in takewhile(lambda x: x < 5, range(10)):
    print(f"  {item}")

# compress - 根据选择器过滤元素
print("\ncompress('ABCDEF', [1, 0, 1, 0, 1, 1]):")
for item in itertools.compress('ABCDEF', [1, 0, 1, 0, 1, 1]):
    print(f"  {item}")

# islice - 切片迭代器
print("\nislice(range(20), 5, 15, 2):")
for item in itertools.islice(range(20), 5, 15, 2):
    print(f"  {item}")

# 4. 迭代器映射与归约函数
print("\n=== 4. 迭代器映射与归约函数 ===")

# accumulate - 累积结果
print("accumulate([1, 2, 3, 4, 5]):")
for item in accumulate([1, 2, 3, 4, 5]):
    print(f"  {item}")

print("\naccumulate([1, 2, 3, 4, 5], operator.mul):")
for item in accumulate([1, 2, 3, 4, 5], operator.mul):
    print(f"  {item}")

print("\naccumulate([5, 2, 6, 4, 3], max):")
for item in accumulate([5, 2, 6, 4, 3], max):
    print(f"  {item}")

# starmap - 类似于map，但将迭代器中的元素作为参数解包
print("\nstarmap(operator.pow, [(2, 3), (3, 2), (4, 2)]):")
for item in starmap(operator.pow, [(2, 3), (3, 2), (4, 2)]):
    print(f"  {item}")

# 5. 分组与其他函数
print("\n=== 5. 分组与其他函数 ===")

# groupby - 根据键函数分组
print("按长度分组字符串:")
words = ['apple', 'bat', 'bar', 'atom', 'book']
# 注意：使用groupby前通常需要排序
for key, group in groupby(sorted(words, key=len), key=len):
    print(f"  长度 {key}: {list(group)}")

# 按首字母分组
print("\n按首字母分组字符串:")
for key, group in groupby(sorted(words), key=lambda x: x[0]):
    print(f"  首字母 '{key}': {list(group)}")

# tee - 创建迭代器的多个副本
print("\ntee创建迭代器的多个副本:")
original = iter([1, 2, 3, 4, 5])
copy1, copy2, copy3 = tee(original, 3)

print(f"副本1: {list(copy1)}")
print(f"副本2: {list(copy2)}")
print(f"副本3: {list(copy3)}")
print(f"原迭代器已被消耗: {list(original)}")  # 应该为空
```

### 2.2 itertools应用场景与高级用法
**[标识: STD-ITERTOOLS-002]**

itertools模块在许多高级编程场景中都能发挥重要作用，下面展示一些典型的应用场景和高级用法。

```python
# itertools模块应用场景与高级用法

import itertools
import operator
from itertools import (
    count, cycle, repeat,
    chain, zip_longest, product, permutations, combinations,
    groupby, filterfalse, dropwhile, takewhile, accumulate,
    starmap, tee
)
import heapq

# 1. 数据处理与转换
print("=== 1. 数据处理与转换 ===")

# 示例数据 - 销售记录
sales_records = [
    {'product': 'A', 'region': 'North', 'quarter': 1, 'sales': 100},
    {'product': 'A', 'region': 'South', 'quarter': 1, 'sales': 150},
    {'product': 'A', 'region': 'East', 'quarter': 1, 'sales': 120},
    {'product': 'A', 'region': 'West', 'quarter': 1, 'sales': 90},
    {'product': 'B', 'region': 'North', 'quarter': 1, 'sales': 200},
    {'product': 'B', 'region': 'South', 'quarter': 1, 'sales': 180},
    {'product': 'B', 'region': 'East', 'quarter': 1, 'sales': 210},
    {'product': 'B', 'region': 'West', 'quarter': 1, 'sales': 170},
    # 第二季度数据
    {'product': 'A', 'region': 'North', 'quarter': 2, 'sales': 110},
    {'product': 'A', 'region': 'South', 'quarter': 2, 'sales': 155},
    {'product': 'A', 'region': 'East', 'quarter': 2, 'sales': 125},
    {'product': 'A', 'region': 'West', 'quarter': 2, 'sales': 95},
    {'product': 'B', 'region': 'North', 'quarter': 2, 'sales': 205},
    {'product': 'B', 'region': 'South', 'quarter': 2, 'sales': 185},
    {'product': 'B', 'region': 'East', 'quarter': 2, 'sales': 215},
    {'product': 'B', 'region': 'West', 'quarter': 2, 'sales': 175},
]

# 使用groupby按产品分组并计算总销售额
print("按产品分组计算总销售额:")
for product, group in groupby(sorted(sales_records, key=lambda x: x['product']),
                              key=lambda x: x['product']):
    product_sales = list(group)
    total_sales = sum(record['sales'] for record in product_sales)
    print(f"  产品 {product}: 总销售额 = {total_sales}")

# 计算每个季度每个产品的总销售额
print("\n按季度和产品分组计算总销售额:")
key_func = lambda x: (x['quarter'], x['product'])
for (quarter, product), group in groupby(sorted(sales_records, key=key_func), key=key_func):
    quarter_sales = sum(record['sales'] for record in group)
    print(f"  季度 {quarter}, 产品 {product}: 总销售额 = {quarter_sales}")

# 查找销售额最高的前3个记录
print("\n销售额最高的前3个记录:")
top_sales = heapq.nlargest(3, sales_records, key=lambda x: x['sales'])
for record in top_sales:
    print(f"  {record}")

# 2. 高效的数据生成
print("\n=== 2. 高效的数据生成 ===")

# 生成所有可能的IP地址组合（简化示例）
def generate_ip_addresses():
    octets = range(256)
    # 生成所有可能的IP地址组合
    for ip_parts in product(octets, repeat=4):
        yield '.'.join(map(str, ip_parts))

# 显示前5个和后5个IP地址
print("前5个IP地址:")
ip_gen = generate_ip_addresses()
for _ in range(5):
    print(f"  {next(ip_gen)}")

# 生成日期组合
def generate_date_combinations():
    years = range(2020, 2025)
    months = range(1, 13)
    days = range(1, 32)  # 简化处理，实际应用中需要考虑每月天数
    
    for year, month, day in product(years, months, days):
        yield f"{year}-{month:02d}-{day:02d}"

print("\n2023年1月的前10个日期:")
date_gen = generate_date_combinations()
# 跳过到2023-01-01
for date in date_gen:
    if date.startswith("2023-01"):
        print(f"  {date}")
        # 再打印9个
        for _ in range(9):
            print(f"  {next(date_gen)}")
        break

# 3. 高级算法实现
print("\n=== 3. 高级算法实现 ===")

# 使用itertools实现排列组合算法
print("生成['A', 'B', 'C', 'D']的所有3个元素的排列:")
perms = permutations(['A', 'B', 'C', 'D'], 3)
for i, perm in enumerate(perms, 1):
    print(f"  {i}. {perm}")
    if i >= 8:  # 只显示前8个
        break

# 使用itertools实现子集生成
def generate_subsets(items):
    """生成所有子集"""
    # 对于每个可能的长度，生成所有组合
    for r in range(len(items) + 1):
        for subset in combinations(items, r):
            yield subset

print("\n生成['a', 'b', 'c']的所有子集:")
for subset in generate_subsets(['a', 'b', 'c']):
    print(f"  {subset}")

# 使用itertools实现笛卡尔积求解问题
print("\n求解简单的组合优化问题:")
print("找出三个数字x, y, z，使得 x^2 + y^2 = z^2 且 x, y, z < 20")

# 生成所有可能的三元组
for x, y, z in product(range(1, 20), repeat=3):
    if x*x + y*y == z*z:
        print(f"  {x}^2 + {y}^2 = {z}^2 ({x*x} + {y*y} = {z*z})")

# 4. 流式数据处理
print("\n=== 4. 流式数据处理 ===")

# 模拟无限数据流
def infinite_data_stream():
    """模拟传感器数据流"""
    for i in count(1):
        # 模拟传感器读数（带有一些噪声）
        reading = {
            'timestamp': i,
            'value': 100 + (i % 10) + (i // 20) * 2
        }
        yield reading

# 处理数据流中的异常值
def process_data_stream(stream, threshold=110, window_size=5):
    """处理数据流，检测并报告异常值"""
    # 使用islice获取窗口数据
    window = list(itertools.islice(stream, window_size))
    
    while window:
        # 计算窗口平均值
        avg_value = sum(item['value'] for item in window) / window_size
        
        # 检测当前窗口中的异常值
        for item in window:
            if abs(item['value'] - avg_value) > threshold:
                print(f"检测到异常值: 时间戳={item['timestamp']}, 值={item['value']}, "
                      f"窗口平均值={avg_value:.2f}")
        
        # 获取下一个元素并更新窗口
        try:
            next_item = next(stream)
            window = window[1:] + [next_item]
        except StopIteration:
            break

# 模拟处理数据流（限制为20个数据点）
print("处理数据流并检测异常值:")
limited_stream = itertools.islice(infinite_data_stream(), 20)
process_data_stream(limited_stream, threshold=5)  # 降低阈值以便演示

# 5. 内存高效的数据处理
print("\n=== 5. 内存高效的数据处理 ===")

# 生成大文件中的特定行（不一次性加载整个文件）
def find_lines_with_pattern(file_path, pattern):
    """查找文件中包含指定模式的行"""
    with open(file_path, 'r') as f:
        # 使用filterfalse过滤不匹配的行
        matching_lines = filterfalse(lambda line: pattern not in line, f)
        for line in matching_lines:
            yield line.strip()

# 由于我们没有实际文件，这里模拟一个文件生成器
def mock_file_generator():
    """模拟文件内容生成器"""
    for i in range(100):
        if i % 7 == 0:
            yield f"这是包含模式的行 {i}\n"
        else:
            yield f"这是普通行 {i}\n"

# 使用模拟文件生成器演示
print("查找包含模式的行:")
matching_lines = filterfalse(lambda line: "模式" not in line, mock_file_generator())
for line in matching_lines:
    print(f"  {line.strip()}")

# 使用itertools处理大型数据集
print("\n使用accumulate计算大型数据集的累积和:")
# 模拟大型数据集（生成器表达式）
large_dataset = (i % 100 for i in range(1000000))

# 只计算前10个累积值进行演示
limited_accumulate = itertools.islice(accumulate(large_dataset), 10)
print(list(limited_accumulate))

# 6. 迭代器模式的高级应用
print("\n=== 6. 迭代器模式的高级应用 ===")

# 使用tee创建多个独立的迭代器
def process_in_parallel(data_stream):
    """并行处理数据流的不同方面"""
    # 创建数据的三个副本
    stream1, stream2, stream3 = tee(data_stream, 3)
    
    # 处理方式1: 计算总和
    total = sum(item['value'] for item in stream1)
    
    # 处理方式2: 找出最大值及其位置
    max_item = max(stream2, key=lambda x: x['value'], default=None)
    
    # 处理方式3: 计算平均值
    values = list(item['value'] for item in stream3)
    avg = sum(values) / len(values) if values else 0
    
    return {
        'total': total,
        'max': max_item,
        'average': avg,
        'count': len(values)
    }

# 创建测试数据流
test_data = [
    {'id': 1, 'value': 10},
    {'id': 2, 'value': 20},
    {'id': 3, 'value': 15},
    {'id': 4, 'value': 30},
    {'id': 5, 'value': 25}
]

# 处理数据
results = process_in_parallel(test_data)
print(f"数据处理结果:")
print(f"  总数: {results['total']}")
print(f"  最大值: {results['max']}")
print(f"  平均值: {results['average']}")
print(f"  计数: {results['count']}")

# 使用itertools实现惰性计算管道
def data_pipeline(data):
    """创建数据处理管道"""
    # 步骤1: 过滤出值大于15的项目
    filtered = filter(lambda x: x['value'] > 15, data)
    
    # 步骤2: 转换数据格式
    transformed = map(lambda x: {'id': x['id'], 'value': x['value'] * 2, 'tag': 'processed'}, filtered)
    
    # 步骤3: 排序
    sorted_data = sorted(transformed, key=lambda x: x['value'], reverse=True)
    
    # 步骤4: 限制结果数量
    limited = itertools.islice(sorted_data, 3)
    
    return limited

# 执行管道并显示结果
print("\n执行数据处理管道:")
for item in data_pipeline(test_data):
    print(f"  {item}")
```

## 3. 函数式编程工具 (functools)

### 3.1 functools模块核心函数
**[标识: STD-FUNCTOOLS-001]**

functools模块提供了一系列用于高阶函数的工具，包括函数式编程中的常用操作，如部分应用、柯里化、缓存和函数组合等。

```python
# functools模块核心函数示例

import functools
import time
from functools import (
    partial, reduce, lru_cache, wraps, singledispatch,
    cached_property, total_ordering
)

# 1. partial - 部分应用函数
print("=== 1. partial - 部分应用函数 ===")

# 定义一个多参数函数
def power(base, exponent):
    return base ** exponent

# 创建一个固定指数为2的平方函数
square = partial(power, exponent=2)
print(f"square(5) = {square(5)}")
print(f"square(10) = {square(10)}")

# 创建一个固定底数为2的指数函数
two_power = partial(power, 2)
print(f"two_power(3) = {two_power(3)}")
print(f"two_power(10) = {two_power(10)}")

# 使用partial处理多参数函数
def greet(greeting, name, punctuation):
    return f"{greeting}, {name}{punctuation}"

# 创建固定问候语的函数
say_hello = partial(greet, "Hello")
say_hi = partial(greet, "Hi")

# 进一步固定标点符号
say_hello_excited = partial(say_hello, punctuation="!")
say_hi_polite = partial(say_hi, punctuation=".")

print(f"say_hello_excited('World') = {say_hello_excited('World')}")
print(f"say_hi_polite('Python') = {say_hi_polite('Python')}")

# partial在回调函数中的应用
def process_data(data, callback=None):
    result = sum(data)
    if callback:
        callback(result)
    return result

# 使用partial创建特定的回调
log_result = partial(print, "处理结果:")
save_result = partial(lambda label, value: print(f"{label}: {value}"), "保存结果")

print("\n使用不同回调处理数据:")
process_data([1, 2, 3, 4, 5], log_result)
process_data([10, 20, 30], save_result)

# 2. reduce - 归约函数
print("\n=== 2. reduce - 归约函数 ===")

# 计算列表的和
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"reduce计算和: {sum_result}")
print(f"内置sum函数: {sum(numbers)}")  # 对于求和，内置sum更高效

# 计算列表的乘积
product_result = reduce(lambda x, y: x * y, numbers)
print(f"reduce计算乘积: {product_result}")

# 使用初始值
product_with_initial = reduce(lambda x, y: x * y, [], 1)  # 空列表需要初始值
print(f"空列表乘积(有初始值): {product_with_initial}")

# 使用operator模块函数提高可读性
import operator
max_result = reduce(operator.max, numbers)
min_result = reduce(operator.min, numbers)
print(f"使用operator.max: {max_result}")
print(f"使用operator.min: {min_result}")

# 实现自定义连接函数
words = ['Python', 'is', 'awesome']
joined = reduce(lambda x, y: f"{x} {y}", words)
print(f"自定义连接: '{joined}'")

# 3. lru_cache - 最近最少使用缓存
print("\n=== 3. lru_cache - 缓存装饰器 ===")

# 定义一个耗时的函数
@lru_cache(maxsize=32)
def fibonacci(n):
    """计算斐波那契数列"""
    print(f"计算fibonacci({n})")
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 首次调用，会计算所有中间值
print("首次计算fibonacci(10):")
result1 = fibonacci(10)
print(f"结果: {result1}")

# 再次调用，将使用缓存结果
print("\n再次计算fibonacci(10)（应使用缓存）:")
result2 = fibonacci(10)
print(f"结果: {result2}")

# 查看缓存信息
print(f"\n缓存统计: {fibonacci.cache_info()}")

# 清除缓存
print("\n清除缓存后重新计算:")
fibonacci.cache_clear()
result3 = fibonacci(10)
print(f"结果: {result3}")

# 带参数的耗时函数
@lru_cache(maxsize=None)  # 无限制缓存
def slow_operation(x, y):
    """模拟耗时操作"""
    print(f"执行slow_operation({x}, {y})")
    time.sleep(0.2)  # 模拟耗时操作
    return x + y

# 测试缓存性能
print("\n测试缓存性能:")

# 首次调用
start = time.time()
slow_operation(1, 2)
first_time = time.time() - start
print(f"首次调用时间: {first_time:.4f}秒")

# 缓存调用
start = time.time()
slow_operation(1, 2)
second_time = time.time() - start
print(f"缓存调用时间: {second_time:.4f}秒")
print(f"性能提升: {first_time / second_time:.2f}倍")

# 4. wraps - 保留原函数元数据
print("\n=== 4. wraps - 保留原函数元数据 ===")

# 不使用wraps的装饰器
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        """wrapper函数的文档字符串"""
        print(f"调用{func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 使用wraps的装饰器
def better_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper函数的文档字符串"""
        print(f"调用{func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# 定义测试函数
@simple_decorator
def function1(x):
    """函数1的文档字符串"""
    return x * 2

@better_decorator
def function2(x):
    """函数2的文档字符串"""
    return x * 3

# 比较两个装饰器的效果
print("不使用wraps的装饰器:")
print(f"函数名: {function1.__name__}")
print(f"文档字符串: {function1.__doc__}")
print(f"模块名: {function1.__module__}")

print("\n使用wraps的装饰器:")
print(f"函数名: {function2.__name__}")
print(f"文档字符串: {function2.__doc__}")
print(f"模块名: {function2.__module__}")

# 5. singledispatch - 单分派泛型函数
print("\n=== 5. singledispatch - 单分派泛型函数 ===")

@singledispatch
def process_data(data):
    """处理数据的通用函数"""
    print(f"处理通用数据: {data}")
    return str(data)

# 为不同类型注册专门的处理函数
@process_data.register(int)
def _(data):
    """处理整数数据"""
    print(f"处理整数: {data}")
    return f"整数: {data}"

@process_data.register(list)
def _(data):
    """处理列表数据"""
    print(f"处理列表: {data}")
    return f"列表（{len(data)}个元素）: {data}"

@process_data.register(dict)
def _(data):
    """处理字典数据"""
    print(f"处理字典: {data}")
    return f"字典（{len(data)}个键）: {data}"

# 可以同时注册多个类型
@process_data.register(tuple)
@process_data.register(set)
def _(data):
    """处理元组或集合数据"""
    print(f"处理{type(data).__name__}: {data}")
    return f"{type(data).__name__}（{len(data)}个元素）: {data}"

# 测试不同类型的处理
print("测试单分派泛型函数:")
process_data(42)
process_data([1, 2, 3, 4, 5])
process_data({'a': 1, 'b': 2, 'c': 3})
process_data((1, 2, 3))
process_data({1, 2, 3, 4})
process_data("字符串")  # 使用默认处理函数

# 6. cached_property - 缓存属性
print("\n=== 6. cached_property - 缓存属性 ===")

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    @property
    def expensive_calculation(self):
        """每次访问都会重新计算的属性"""
        print("执行昂贵计算...")
        time.sleep(0.5)  # 模拟耗时计算
        return sum(self.data) / len(self.data) if self.data else 0
    
    @cached_property
    def cached_calculation(self):
        """结果会被缓存的属性"""
        print("执行缓存计算...")
        time.sleep(0.5)  # 模拟耗时计算
        return sum(self.data) / len(self.data) if self.data else 0

# 创建处理器实例
processor = DataProcessor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 测试普通属性（每次都计算）
print("测试普通属性:")
start = time.time()
result1 = processor.expensive_calculation
first_time = time.time() - start
print(f"第一次访问: {result1}, 耗时: {first_time:.4f}秒")

start = time.time()
result2 = processor.expensive_calculation
second_time = time.time() - start
print(f"第二次访问: {result2}, 耗时: {second_time:.4f}秒")

# 测试缓存属性（只计算一次）
print("\n测试缓存属性:")
start = time.time()
result3 = processor.cached_calculation
first_time = time.time() - start
print(f"第一次访问: {result3}, 耗时: {first_time:.4f}秒")

start = time.time()
result4 = processor.cached_calculation
second_time = time.time() - start
print(f"第二次访问: {result4}, 耗时: {second_time:.4f}秒")
print(f"性能提升: {first_time / second_time:.2f}倍")

# 7. total_ordering - 简化比较方法实现
print("\n=== 7. total_ordering - 简化比较方法实现 ===")

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        """等于比较"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age
    
    def __lt__(self, other):
        """小于比较 - total_ordering会基于此自动生成其他比较方法"""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age < other.age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

# 创建Person实例
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)
p3 = Person("Charlie", 30)
p4 = Person("David", 35)

# 测试各种比较操作
print("测试Person类的比较操作:")
print(f"{p1} == {p2}: {p1 == p2}")
print(f"{p1} == {p3}: {p1 == p3}")
print(f"{p1} < {p2}: {p1 < p2}")
print(f"{p1} <= {p3}: {p1 <= p3}")
print(f"{p1} > {p2}: {p1 > p2}")
print(f"{p1} >= {p4}: {p1 >= p4}")

# 测试排序
people = [p1, p2, p3, p4]
sorted_people = sorted(people)
print(f"\n按年龄排序的人员列表: {sorted_people}")
```

### 3.2 functools应用场景与函数式编程实践
**[标识: STD-FUNCTOOLS-002]**

functools模块在函数式编程风格的Python代码中有广泛的应用，下面展示一些典型的应用场景和函数式编程最佳实践。

```python
# functools应用场景与函数式编程实践

import functools
import operator
from functools import (
    partial, reduce, lru_cache, wraps, singledispatch,
    cached_property, total_ordering
)
import time
from itertools import chain

# 1. 函数组合与管道模式
print("=== 1. 函数组合与管道模式 ===")

# 定义函数组合操作符
def compose(*funcs):
    """组合多个函数，从右到左执行"""
    def composed_function(x):
        result = x
        # 从右到左依次应用函数
        for func in reversed(funcs):
            result = func(result)
        return result
    return composed_function

# 定义一系列转换函数
def add_one(x): return x + 1
def multiply_by_two(x): return x * 2
def square(x): return x ** 2

# 使用函数组合创建新函数
transform = compose(square, multiply_by_two, add_one)
print(f"转换函数: square(multiply_by_two(add_one(x)))")
print(f"transform(3) = {transform(3)}")  # ((3+1)*2)^2 = 64
print(f"transform(5) = {transform(5)}")  # ((5+1)*2)^2 = 144

# 使用partial和compose创建可配置的处理管道
def process_data_pipeline(data, transformations):
    """应用一系列转换到数据"""
    pipeline = compose(*transformations)
    return pipeline(data)

# 定义数据处理函数
def filter_positive(numbers):
    return [n for n in numbers if n > 0]

def convert_to_strings(numbers):
    return [f"Item: {n}" for n in numbers]

def join_with_commas(strings):
    return ", ".join(strings)

# 创建数据处理管道
numbers_pipeline = [filter_positive, convert_to_strings, join_with_commas]

# 应用管道到数据
data = [-5, 10, -3, 8, 0, 15]
result = process_data_pipeline(data, numbers_pipeline)
print(f"\n数据处理管道结果: '{result}'")

# 2. 数据验证与转换
print("\n=== 2. 数据验证与转换 ===")

# 使用装饰器进行数据验证
def validate_input(*validators):
    """验证输入参数的装饰器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # 验证位置参数
            for i, (arg, validator) in enumerate(zip(args, validators)):
                if not validator(arg):
                    raise ValueError(f"参数 {i} 验证失败: {arg}")
            # 执行原函数
            return func(*args, **kwargs)
        return wrapper
    return decorator

# 定义验证器
is_positive = lambda x: isinstance(x, int) and x > 0
is_non_empty_str = lambda x: isinstance(x, str) and len(x.strip()) > 0
is_valid_email = lambda x: isinstance(x, str) and '@' in x and '.' in x.split('@')[1]

# 使用验证器装饰函数
@validate_input(is_positive, is_non_empty_str, is_valid_email)
def register_user(user_id, username, email):
    """注册新用户"""
    print(f"注册用户: ID={user_id}, 用户名='{username}', 邮箱='{email}'")
    return {"user_id": user_id, "username": username, "email": email}

# 测试验证
print("测试数据验证:")
try:
    register_user(1, "alice", "alice@example.com")
    print("✓ 验证通过")
except ValueError as e:
    print(f"✗ 验证失败: {e}")

try:
    register_user(-1, "bob", "bob@example.com")
    print("✓ 验证通过")
except ValueError as e:
    print(f"✗ 验证失败: {e}")

try:
    register_user(2, "", "charlie@example.com")
    print("✓ 验证通过")
except ValueError as e:
    print(f"✗ 验证失败: {e}")

# 3. 记忆化与性能优化
print("\n=== 3. 记忆化与性能优化 ===")

# 递归函数的记忆化优化
@lru_cache(maxsize=None)
def calculate_path_cost(start, end, graph):
    """计算图中两点之间的最短路径成本"""
    print(f"计算路径: {start} -> {end}")
    
    # 基本情况：起点和终点相同
    if start == end:
        return 0
    
    # 找到所有可能的下一个节点
    if start not in graph or not graph[start]:
        return float('inf')  # 不可达
    
    # 计算到每个邻居的路径成本
    min_cost = float('inf')
    for neighbor, cost in graph[start].items():
        # 递归计算到终点的成本
        path_cost = cost + calculate_path_cost(neighbor, end, graph)
        min_cost = min(min_cost, path_cost)
    
    return min_cost

# 示例图（邻接表表示）
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'C': 2, 'D': 6},
    'C': {'D': 7, 'E': 4},
    'D': {'E': 2},
    'E': {}
}

# 计算路径成本
print("计算最短路径成本:")
cost1 = calculate_path_cost('A', 'E', graph)
print(f"A到E的最短路径成本: {cost1}")

# 再次计算相同路径（将使用缓存）
cost2 = calculate_path_cost('A', 'E', graph)
print(f"再次计算（使用缓存）: {cost2}")

# 查看缓存信息
print(f"\n缓存统计: {calculate_path_cost.cache_info()}")

# 4. 适配器模式与接口兼容
print("\n=== 4. 适配器模式与接口兼容 ===")

# 使用functools.wraps创建函数适配器
def api_adapter(func):
    """适配旧API到新接口"""
    @wraps(func)
    def wrapper(data=None, options=None):
        # 适配不同的参数格式
        if isinstance(data, dict) and 'items' in data:
            # 新API格式: {'items': [...], 'config': {...}}
            items = data['items']
            config = data.get('config', {})
        else:
            # 旧API格式: 直接传入items和options
            items = data
            config = options or {}
        
        # 调用原始函数并返回结果
        return func(items, config)
    return wrapper

# 原始函数
def process_items(items, config):
    """处理项目列表"""
    print(f"处理 {len(items)} 个项目，配置: {config}")
    result = [item * config.get('multiplier', 1) for item in items]
    return result

# 适配后的函数
adapted_process_items = api_adapter(process_items)

# 使用旧API格式调用
print("使用旧API格式:")
result1 = adapted_process_items([1, 2, 3], {'multiplier': 2})
print(f"结果: {result1}")

# 使用新API格式调用
print("\n使用新API格式:")
result2 = adapted_process_items({'items': [4, 5, 6], 'config': {'multiplier': 3}})
print(f"结果: {result2}")

# 5. 命令行参数处理
print("\n=== 5. 命令行参数处理 ===")

# 使用partial创建特定的命令处理器
def process_command(command, *args, **kwargs):
    """处理命令"""
    print(f"执行命令: {command}")
    print(f"参数: {args}")
    print(f"选项: {kwargs}")
    return f"命令 {command} 执行完成"

# 创建特定命令的处理函数
create_user = partial(process_command, "create_user")
delete_user = partial(process_command, "delete_user")
list_users = partial(process_command, "list_users")

# 执行特定命令
print("执行特定命令:")
create_user("alice", admin=True)
delete_user("bob")
list_users(active_only=True)

# 6. 延迟计算与惰性求值
print("\n=== 6. 延迟计算与惰性求值 ===")

class LazyEvaluation:
    def __init__(self, func):
        self.func = func
        self._value = None
        self._evaluated = False
    
    def __call__(self):
        if not self._evaluated:
            self._value = self.func()
            self._evaluated = True
        return self._value
    
    def reset(self):
        """重置计算状态，下次调用将重新计算"""
        self._value = None
        self._evaluated = False

# 创建惰性计算对象
def expensive_computation():
    print("执行昂贵计算...")
    time.sleep(1)  # 模拟耗时操作
    return sum(i * i for i in range(10000))

# 包装为惰性计算
lazy_result = LazyEvaluation(expensive_computation)

# 首次访问会执行计算
print("首次访问惰性计算结果:")
start = time.time()
result1 = lazy_result()
first_time = time.time() - start
print(f"结果: {result1}, 耗时: {first_time:.4f}秒")

# 再次访问会使用缓存的结果
print("\n再次访问惰性计算结果:")
start = time.time()
result2 = lazy_result()
second_time = time.time() - start
print(f"结果: {result2}, 耗时: {second_time:.4f}秒")
print(f"性能提升: {first_time / second_time:.2f}倍")

# 重置后会重新计算
print("\n重置后再次访问:")
lazy_result.reset()
start = time.time()
result3 = lazy_result()
reset_time = time.time() - start
print(f"结果: {result3}, 耗时: {reset_time:.4f}秒")

# 7. 上下文管理器与资源管理
print("\n=== 7. 上下文管理器与资源管理 ===")

# 使用functools.wraps创建自定义上下文管理器
def timer_context(label):
    """计时上下文管理器"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{label}] 开始执行...")
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = time.time()
                print(f"[{label}] 执行完成，耗时: {(end_time - start_time):.4f}秒")
        return wrapper
    return decorator

# 使用上下文管理器装饰函数
@timer_context("数据处理")
def process_large_data(data):
    """处理大量数据"""
    time.sleep(0.5)  # 模拟处理时间
    return sum(data) / len(data) if data else 0

# 执行带计时的函数
print("执行带计时的函数:")
result = process_large_data(list(range(100000)))
print(f"计算结果: {result}")

# 8. 高阶函数实践
print("\n=== 8. 高阶函数实践 ===")

# 创建数据转换管道
def create_pipeline(*steps):
    """创建数据转换管道"""
    def pipeline(data):
        result = data
        for step in steps:
            result = step(result)
        return result
    return pipeline

# 定义转换步骤
def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def double_values(numbers):
    return [n * 2 for n in numbers]

def sum_values(numbers):
    return sum(numbers)

# 创建并使用管道
data_pipeline = create_pipeline(filter_even, double_values, sum_values)

# 测试管道
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = data_pipeline(data)
print(f"数据管道结果: {result}")

# 使用functools.reduce实现fold操作
def foldl(func, iterable, initializer=None):
    """左折叠操作"""
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('foldl() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = func(accum_value, x)
    return accum_value

# 使用左折叠实现自定义聚合
def aggregate_data(data, key_func, agg_func):
    """按键聚合数据并应用聚合函数"""
    # 按键分组
    groups = {}
    for item in data:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    
    # 对每个组应用聚合函数
    return {key: agg_func(items) for key, items in groups.items()}

# 测试数据
students = [
    {'name': 'Alice', 'class': 'A', 'score': 90},
    {'name': 'Bob', 'class': 'B', 'score': 85},
    {'name': 'Charlie', 'class': 'A', 'score': 95},
    {'name': 'David', 'class': 'B', 'score': 80},
    {'name': 'Eve', 'class': 'A', 'score': 88}
]

# 按班级计算平均分
avg_scores = aggregate_data(
    students,
    key_func=lambda s: s['class'],
    agg_func=lambda items: sum(s['score'] for s in items) / len(items)
)

print(f"\n各班平均分数:")
for class_name, avg_score in avg_scores.items():
    print(f"班级 {class_name}: {avg_score:.2f}")
