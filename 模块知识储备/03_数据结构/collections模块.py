"""
此文件是Python模块的学习文档，包含Markdown格式和代码示例。
请使用文本编辑器或Markdown查看器打开以获得最佳阅读体验。
"""

# Python collections模块详解

## 1. 核心功能与概述

"collections"模块提供了Python内置容器类型(dict, list, set, tuple)的替代实现,这些特殊容器类型具有额外的功能和优化.该模块主要包含以下几个重要的数据结构:

1. **namedtuple**: 创建命名元组子类的工厂函数
2. **deque**: 双端队列,支持从两端高效添加和删除元素
3. **ChainMap**: 多个字典的集合,可以作为一个单独的映射查看和操作
4. **Counter**: 用于计数可哈希对象的字典子类
5. **OrderedDict**: 保持插入顺序的字典子类
6. **defaultdict**: 带有默认值的字典子类
7. **UserDict, UserList, UserTuple**: 用于自定义容器类的基类

这些数据结构在各种场景中提供了比内置容器更高效或更方便的功能,特别是在数据处理,算法实现和性能优化方面.

## 2. 基本使用方法

### 2.1 namedtuple - 命名元组

"namedtuple"创建一个具有命名字段的元组子类,既保持了元组的不可变性,又提供了通过名称访问元素的能力,增强了代码的可读性.

```python
from collections import namedtuple

# 创建一个命名元组类
Point = namedtuple('Point', ['x', 'y', 'z'])

# 创建命名元组实例
p1 = Point(1, 2, 3)
p2 = Point(x=4, y=5, z=6)

# 通过索引访问元素
print(f"p1[0] = {p1[0]}")  # 输出: 1

# 通过名称访问元素
print(f"p1.x = {p1.x}")   # 输出: 1
print(f"p1.y = {p1.y}")   # 输出: 2
print(f"p1.z = {p1.z}")   # 输出: 3

# 转换为字典
print(f"p1._asdict() = {p1._asdict()}")  # 输出: {'x': 1, 'y': 2, 'z': 3}

# 替换字段值(创建新实例)
p3 = p1._replace(y=10)
print(f"p3 = {p3}")       # 输出: Point(x=1, y=10, z=3)
print(f"p1 = {p1}")       # 输出: Point(x=1, y=2, z=3)  # 原实例不变

# 使用字段名列表创建命名元组
fields = ['name', 'age', 'city']
Person = namedtuple('Person', fields)
person = Person('Alice', 30, 'New York')
print(f"person = {person}")  # 输出: Person(name='Alice', age=30, city='New York')

# 使用字符串分隔符创建命名元组
Car = namedtuple('Car', 'brand model year')
car = Car('Toyota', 'Corolla', 2022)
print(f"car = {car}")    # 输出: Car(brand='Toyota', model='Corolla', year=2022)
```

### 2.2 deque - 双端队列

"deque"(double-ended queue)是一种双端队列数据结构,支持从两端高效地添加和删除元素,时间复杂度为O(1).它是列表的一个很好的替代方案,特别是在需要频繁从列表头部操作元素的场景中.

```python
from collections import deque

# 创建一个双端队列
dq = deque([1, 2, 3, 4, 5])
print(f"初始deque: {dq}")  # 输出: deque([1, 2, 3, 4, 5])

# 从右侧添加元素
dq.append(6)
print(f"右侧添加6后: {dq}")  # 输出: deque([1, 2, 3, 4, 5, 6])

# 从左侧添加元素
dq.appendleft(0)
print(f"左侧添加0后: {dq}")  # 输出: deque([0, 1, 2, 3, 4, 5, 6])

# 从右侧删除元素
right_element = dq.pop()
print(f"右侧删除元素: {right_element}")  # 输出: 6
print(f"删除后deque: {dq}")  # 输出: deque([0, 1, 2, 3, 4, 5])

# 从左侧删除元素
left_element = dq.popleft()
print(f"左侧删除元素: {left_element}")  # 输出: 0
print(f"删除后deque: {dq}")  # 输出: deque([1, 2, 3, 4, 5])

# 扩展右侧
dq.extend([6, 7, 8])
print(f"右侧扩展[6, 7, 8]后: {dq}")  # 输出: deque([1, 2, 3, 4, 5, 6, 7, 8])

# 扩展左侧
dq.extendleft([-1, 0])
print(f"左侧扩展[-1, 0]后: {dq}")  # 输出: deque([0, -1, 1, 2, 3, 4, 5, 6, 7, 8])

# 旋转(正数向右,负数向左)
dq.rotate(1)
print(f"向右旋转1位后: {dq}")  # 输出: deque([8, 0, -1, 1, 2, 3, 4, 5, 6, 7])

dq.rotate(-2)
print(f"向左旋转2位后: {dq}")  # 输出: deque([-1, 1, 2, 3, 4, 5, 6, 7, 8, 0])

# 限制最大长度
dq_limited = deque(maxlen=3)
dq_limited.extend([1, 2, 3])
print(f"限制长度为3的deque: {dq_limited}")  # 输出: deque([1, 2, 3], maxlen=3)
dq_limited.append(4)
print(f"添加4后: {dq_limited}")  # 输出: deque([2, 3, 4], maxlen=3) - 自动移除最左侧元素
```

### 2.3 defaultdict - 默认字典

"defaultdict"是字典的一个子类,它为不存在的键提供默认值,避免了手动检查键是否存在的需要.

```python
from collections import defaultdict

# 创建一个默认值为0的defaultdict
counter = defaultdict(int)
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# 统计单词频率
for word in words:
    counter[word] += 1

print(f"单词频率统计: {dict(counter)}")
# 输出: {'apple': 3, 'banana': 2, 'orange': 1}

# 创建一个默认值为空列表的defaultdict
word_by_first_letter = defaultdict(list)

# 按首字母分组单词
for word in words:
    word_by_first_letter[word[0]].append(word)

print(f"按首字母分组: {dict(word_by_first_letter)}")
# 输出: {'a': ['apple', 'apple', 'apple'], 'b': ['banana', 'banana'], 'o': ['orange']}

# 创建一个默认值为set的defaultdict
word_by_length = defaultdict(set)

# 按长度分组单词
for word in words:
    word_by_length[len(word)].add(word)

print(f"按长度分组: {dict(word_by_length)}")
# 输出: {5: {'apple'}, 6: {'banana'}, 6: {'orange'}} - 注意set自动去重

# 使用自定义默认值函数
def default_value():
    return {"count": 0, "total": 0}

stats = defaultdict(default_value)

# 更新统计信息
stats["apple"]["count"] += 1
stats["apple"]["total"] += 100
stats["banana"]["count"] += 1
stats["banana"]["total"] += 150

print(f"自定义默认值统计: {dict(stats)}")
```

### 2.4 Counter - 计数器

"Counter"是字典的一个子类,用于计数可哈希对象.它提供了多种方便的方法来处理计数数据.

```python
from collections import Counter

# 创建计数器
word_counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(f"单词计数: {word_counts}")  # 输出: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 创建空计数器
empty_counter = Counter()
print(f"空计数器: {empty_counter}")  # 输出: Counter()

# 从字典创建计数器
dict_counter = Counter({'a': 3, 'b': 2, 'c': 1})
print(f"从字典创建: {dict_counter}")  # 输出: Counter({'a': 3, 'b': 2, 'c': 1})

# 从关键字参数创建计数器
keyword_counter = Counter(a=3, b=2, c=1)
print(f"从关键字参数创建: {keyword_counter}")  # 输出: Counter({'a': 3, 'b': 2, 'c': 1})

# 获取最常见的元素
print(f"最常见的2个元素: {word_counts.most_common(2)}")  # 输出: [('apple', 3), ('banana', 2)]

# 计数器运算
counter1 = Counter(a=3, b=2, c=1)
counter2 = Counter(a=1, b=2, d=3)

# 加法 - 合并计数
print(f"加法: {counter1 + counter2}")  # 输出: Counter({'a': 4, 'b': 4, 'c': 1, 'd': 3})

# 减法 - 保留正计数
print(f"减法: {counter1 - counter2}")  # 输出: Counter({'a': 2, 'c': 1})

# 交集 - 取最小值
print(f"交集: {counter1 & counter2}")  # 输出: Counter({'b': 2, 'a': 1})

# 并集 - 取最大值
print(f"并集: {counter1 | counter2}")  # 输出: Counter({'a': 3, 'b': 2, 'd': 3, 'c': 1})

# 元素迭代
print(f"元素迭代: {list(word_counts.elements())}")
# 输出: ['apple', 'apple', 'apple', 'banana', 'banana', 'orange']

# 清空计数器
word_counts.clear()
print(f"清空后: {word_counts}")  # 输出: Counter()
```

### 2.5 OrderedDict - 有序字典

"OrderedDict"是字典的一个子类,它保持了键值对的插入顺序.在Python 3.7及以上版本中,普通字典也保持插入顺序,但"OrderedDict"提供了一些额外的方法来处理顺序.

```python
from collections import OrderedDict

# 创建有序字典
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4

print(f"有序字典: {ordered_dict}")  # 输出: OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# 重新插入已存在的键会将其移动到末尾
ordered_dict['a'] = 10
print(f"重新插入'a'后: {ordered_dict}")  # 输出: OrderedDict([('b', 2), ('c', 3), ('d', 4), ('a', 10)])

# 移动到末尾
ordered_dict.move_to_end('b')
print(f"将'b'移动到末尾后: {ordered_dict}")  # 输出: OrderedDict([('c', 3), ('d', 4), ('a', 10), ('b', 2)])

# 移动到开头
ordered_dict.move_to_end('d', last=False)
print(f"将'd'移动到开头后: {ordered_dict}")  # 输出: OrderedDict([('d', 4), ('c', 3), ('a', 10), ('b', 2)])

# 反转顺序
ordered_dict = OrderedDict(reversed(list(ordered_dict.items())))
print(f"反转顺序后: {ordered_dict}")  # 输出: OrderedDict([('b', 2), ('a', 10), ('c', 3), ('d', 4)])

# 等式比较考虑顺序
dict1 = OrderedDict([('a', 1), ('b', 2)])
dict2 = OrderedDict([('b', 2), ('a', 1)])
print(f"dict1 == dict2: {dict1 == dict2}")  # 输出: False - 顺序不同

# 与普通字典比较不考虑顺序
normal_dict = {'a': 1, 'b': 2}
print(f"dict1 == normal_dict: {dict1 == normal_dict}")  # 输出: True - 值相同
```

### 2.6 ChainMap - 链映射

"ChainMap"是多个字典的集合,可以将多个字典视为一个单一的映射.查找时会按照字典在链中的顺序依次查找,直到找到键或遍历完所有字典.

```python
from collections import ChainMap

# 创建几个字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 20, 'c': 3}
dict3 = {'c': 30, 'd': 4}

# 创建ChainMap
chain = ChainMap(dict1, dict2, dict3)

print(f"ChainMap: {chain}")  # 输出: ChainMap({'a': 1, 'b': 2}, {'b': 20, 'c': 3}, {'c': 30, 'd': 4})

# 查找键(从第一个字典开始)
print(f"chain['a'] = {chain['a']}")  # 输出: 1
print(f"chain['b'] = {chain['b']}")  # 输出: 2 (来自dict1)
print(f"chain['c'] = {chain['c']}")  # 输出: 3 (来自dict2)
print(f"chain['d'] = {chain['d']}")  # 输出: 4 (来自dict3)

# 修改会影响第一个字典
chain['b'] = 200
print(f"修改后chain['b'] = {chain['b']}")  # 输出: 200
print(f"修改后dict1 = {dict1}")  # 输出: {'a': 1, 'b': 200}

# 添加新键值对会添加到第一个字典
chain['e'] = 5
print(f"添加'e'后chain = {chain}")
print(f"添加'e'后dict1 = {dict1}")  # 输出: {'a': 1, 'b': 200, 'e': 5}

# 获取所有映射
print(f"所有映射: {chain.maps}")

# 获取键,值,项
print(f"所有键: {list(chain.keys())}")
print(f"所有值: {list(chain.values())}")
print(f"所有项: {list(chain.items())}")

# 重新排序
chain = chain.new_child({'f': 6, 'g': 7})  # 在前面添加新字典
print(f"添加新字典后: {chain}")

# 反向查找
for key in ['a', 'b', 'c', 'd', 'e']:
    for i, mapping in enumerate(chain.maps):
        if key in mapping:
            print(f"键'{key}'在第{i+1}个字典中: {mapping[key]}")
            break
```

## 3. 高级用法

### 3.1 namedtuple的高级应用

"namedtuple"可以与其他数据结构结合使用,实现更复杂的数据模型.

```python
from collections import namedtuple

# 嵌套namedtuple
Point = namedtuple('Point', 'x y')
Rectangle = namedtuple('Rectangle', 'top_left bottom_right')

# 创建一个矩形
tl = Point(0, 10)
br = Point(10, 0)
rect = Rectangle(tl, br)

print(f"矩形: {rect}")
print(f"矩形左上角x坐标: {rect.top_left.x}")
print(f"矩形宽度: {rect.bottom_right.x - rect.top_left.x}")
print(f"矩形高度: {rect.top_left.y - rect.bottom_right.y}")

# 使用namedtuple作为字典键
try:
    # 创建字典,使用Point作为键
    point_dict = {}
    point_dict[Point(1, 2)] = "A点"
    point_dict[Point(3, 4)] = "B点"
    
    print(f"\n点字典: {point_dict}")
    print(f"查找Point(1, 2): {point_dict.get(Point(1, 2))}")
    
except Exception as e:
    print(f"\nnamedtuple作为字典键出错: {e}")

# 自定义namedtuple的__repr__方法
try:
    class CustomPoint(namedtuple('CustomPoint', 'x y')):
        def __repr__(self):
            return f"点({self.x}, {self.y})"
    
    cp = CustomPoint(5, 7)
    print(f"\n自定义表示: {cp}")
    
except Exception as e:
    print(f"\n自定义namedtuple表示出错: {e}")

# 为namedtuple添加方法
try:
    Point3D = namedtuple('Point3D', 'x y z')
    
    # 动态添加方法
    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    
    # 添加方法到类
    Point3D.distance_to_origin = distance_to_origin
    
    p3d = Point3D(3, 4, 5)
    print(f"\n点到原点距离: {p3d.distance_to_origin():.2f}")
    
except Exception as e:
    print(f"\n为namedtuple添加方法出错: {e}")
```

### 3.2 deque的高级应用

"deque"可以用于实现多种高级数据结构和算法.

```python
from collections import deque
import itertools

# 使用deque实现滑动窗口
def sliding_window(iterable, size):
    # 创建窗口
    window = deque(maxlen=size)
    
    # 填充初始窗口
    for _ in range(size):
        try:
            window.append(next(iterable))
        except StopIteration:
            break
    
    # 如果窗口已满,生成第一个结果
    if len(window) == size:
        yield tuple(window)
    
    # 滑动窗口
    for item in iterable:
        window.append(item)
        yield tuple(window)

# 测试滑动窗口
numbers = [1, 2, 3, 4, 5, 6, 7]
print("3元素滑动窗口:")
for window in sliding_window(iter(numbers), 3):
    print(window)

# 使用deque实现队列
try:
    class Queue:
        def __init__(self):
            self._deque = deque()
        
        def enqueue(self, item):
            """入队"""
            self._deque.append(item)
        
        def dequeue(self):
            """出队"""
            if not self.is_empty():
                return self._deque.popleft()
            raise IndexError("队列为空")
        
        def peek(self):
            """查看队首元素"""
            if not self.is_empty():
                return self._deque[0]
            raise IndexError("队列为空")
        
        def is_empty(self):
            """检查队列是否为空"""
            return len(self._deque) == 0
        
        def size(self):
            """获取队列大小"""
            return len(self._deque)
    
    # 测试队列
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    print(f"\n队列大小: {q.size()}")
    print(f"队首元素: {q.peek()}")
    print(f"出队: {q.dequeue()}")
    print(f"出队: {q.dequeue()}")
    print(f"队列是否为空: {q.is_empty()}")
    print(f"出队: {q.dequeue()}")
    print(f"队列是否为空: {q.is_empty()}")
    
except Exception as e:
    print(f"\n队列实现出错: {e}")

# 使用deque实现栈
try:
    class Stack:
        def __init__(self):
            self._deque = deque()
        
        def push(self, item):
            """入栈"""
            self._deque.append(item)
        
        def pop(self):
            """出栈"""
            if not self.is_empty():
                return self._deque.pop()
            raise IndexError("栈为空")
        
        def peek(self):
            """查看栈顶元素"""
            if not self.is_empty():
                return self._deque[-1]
            raise IndexError("栈为空")
        
        def is_empty(self):
            """检查栈是否为空"""
            return len(self._deque) == 0
        
        def size(self):
            """获取栈大小"""
            return len(self._deque)
    
    # 测试栈
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    print(f"\n栈大小: {s.size()}")
    print(f"栈顶元素: {s.peek()}")
    print(f"出栈: {s.pop()}")
    print(f"出栈: {s.pop()}")
    print(f"栈是否为空: {s.is_empty()}")
    print(f"出栈: {s.pop()}")
    print(f"栈是否为空: {s.is_empty()}")
    
except Exception as e:
    print(f"\n栈实现出错: {e}")

# 使用deque实现双向队列
try:
    class Deque:
        def __init__(self):
            self._deque = deque()
        
        def add_front(self, item):
            """从前端添加元素"""
            self._deque.appendleft(item)
        
        def add_rear(self, item):
            """从后端添加元素"""
            self._deque.append(item)
        
        def remove_front(self):
            """从前端移除元素"""
            if not self.is_empty():
                return self._deque.popleft()
            raise IndexError("双端队列为空")
        
        def remove_rear(self):
            """从后端移除元素"""
            if not self.is_empty():
                return self._deque.pop()
            raise IndexError("双端队列为空")
        
        def is_empty(self):
            """检查双端队列是否为空"""
            return len(self._deque) == 0
        
        def size(self):
            """获取双端队列大小"""
            return len(self._deque)
    
    # 测试双端队列
    dq = Deque()
    dq.add_rear(1)
    dq.add_rear(2)
    dq.add_front(0)
    
    print(f"\n双端队列大小: {dq.size()}")
    print(f"从前端移除: {dq.remove_front()}")
    print(f"从后端移除: {dq.remove_rear()}")
    print(f"从前端移除: {dq.remove_front()}")
    print(f"双端队列是否为空: {dq.is_empty()}")
    
except Exception as e:
    print(f"\n双端队列实现出错: {e}")
```

### 3.3 defaultdict的高级应用

"defaultdict"可以与复杂的数据结构和函数结合,实现更强大的数据处理功能.

```python
from collections import defaultdict
import json

# 使用defaultdict实现树结构
try:
    def tree():
        """创建一个嵌套的defaultdict,用于表示树结构"""
        return defaultdict(tree)
    
    # 创建树
    file_tree = tree()
    
    # 构建文件系统结构
    file_tree['home']['user']['documents']['report.txt'] = 'file'
    file_tree['home']['user']['pictures']['vacation']['beach.jpg'] = 'file'
    file_tree['home']['user']['pictures']['family.jpg'] = 'file'
    file_tree['etc']['config']['settings.json'] = 'file'
    
    # 打印树结构
    def print_tree(node, prefix=""):
        for key, value in node.items():
            if isinstance(value, dict):
                print(f"{prefix}{key}/")
                print_tree(value, prefix + "  ")
            else:
                print(f"{prefix}{key}")
    
    print("文件系统树结构:")
    print_tree(file_tree)
    
except Exception as e:
    print(f"树结构实现出错: {e}")

# 使用defaultdict实现图结构
try:
    class Graph:
        def __init__(self):
            self._adjacency_list = defaultdict(list)
        
        def add_edge(self, from_node, to_node):
            """添加边"""
            self._adjacency_list[from_node].append(to_node)
        
        def get_neighbors(self, node):
            """获取节点的邻居"""
            return self._adjacency_list[node]
        
        def bfs(self, start_node):
            """广度优先搜索"""
            visited = set()
            queue = [start_node]
            visited.add(start_node)
            
            while queue:
                current = queue.pop(0)
                yield current
                
                for neighbor in self._adjacency_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
    
    # 创建图
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(4, 7)
    
    print("\n图的广度优先搜索:")
    bfs_result = list(g.bfs(1))
    print(bfs_result)
    
except Exception as e:
    print(f"\n图结构实现出错: {e}")

# 使用defaultdict进行复杂数据聚合
try:
    # 示例数据 - 销售记录
    sales_data = [
        {"region": "North", "product": "A", "quantity": 10, "price": 20},
        {"region": "North", "product": "B", "quantity": 5, "price": 30},
        {"region": "South", "product": "A", "quantity": 8, "price": 20},
        {"region": "South", "product": "C", "quantity": 12, "price": 15},
        {"region": "East", "product": "B", "quantity": 3, "price": 30},
        {"region": "East", "product": "A", "quantity": 7, "price": 20}
    ]
    
    # 使用defaultdict按区域和产品聚合
    sales_by_region_product = defaultdict(lambda: defaultdict(int))
    total_sales_by_region = defaultdict(int)
    
    for sale in sales_data:
        region = sale["region"]
        product = sale["product"]
        amount = sale["quantity"] * sale["price"]
        
        sales_by_region_product[region][product] += amount
        total_sales_by_region[region] += amount
    
    # 打印结果
    print("\n按区域和产品的销售总额:")
    for region, products in sales_by_region_product.items():
        print(f"区域: {region}")
        for product, amount in products.items():
            print(f"  产品 {product}: ¥{amount}")
        print(f"  区域总额: ¥{total_sales_by_region[region]}")
    
except Exception as e:
    print(f"\n复杂数据聚合出错: {e}")
```

### 3.4 Counter的高级应用

"Counter"可以用于高级文本处理,数据分析和统计计算.

```python
from collections import Counter
import re

# 文本分析 - 词频统计
try:
    text = """
    Python is a high-level, interpreted, general-purpose programming language.
    Its design philosophy emphasizes code readability with the use of significant indentation.
    Python is dynamically typed and garbage-collected.
    It supports multiple programming paradigms, including structured, object-oriented and functional programming.
    """
    
    # 移除标点符号并转换为小写
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    words = cleaned_text.split()
    
    # 计算词频
    word_counter = Counter(words)
    
    # 打印最常见的10个单词
    print("文本中最常见的10个单词:")
    for word, count in word_counter.most_common(10):
        print(f"{word}: {count}")
    
    # 计算单词总数
    total_words = sum(word_counter.values())
    print(f"\n总单词数: {total_words}")
    
    # 计算唯一单词数
    unique_words = len(word_counter)
    print(f"唯一单词数: {unique_words}")
    
except Exception as e:
    print(f"文本分析出错: {e}")

# 查找列表中的重复元素
def find_duplicates(lst):
    counter = Counter(lst)
    return [item for item, count in counter.items() if count > 1]

# 测试查找重复元素
numbers = [1, 2, 3, 4, 5, 2, 7, 8, 3, 10, 5]
duplicates = find_duplicates(numbers)
print(f"\n列表中的重复元素: {duplicates}")

# 计算两个列表的交集,并集和差集
def list_operations(list1, list2):
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    # 交集
    intersection = list((counter1 & counter2).elements())
    
    # 并集
    union = list((counter1 | counter2).elements())
    
    # 差集 (list1 - list2)
    difference = list((counter1 - counter2).elements())
    
    return intersection, union, difference

# 测试列表操作
list1 = [1, 2, 2, 3, 4, 4, 4]
list2 = [2, 2, 3, 5, 6]
intersection, union, difference = list_operations(list1, list2)

print(f"\n列表1: {list1}")
print(f"列表2: {list2}")
print(f"交集: {intersection}")
print(f"并集: {union}")
print(f"差集 (list1 - list2): {difference}")

# 字符频率分析
try:
    # 示例: 简单的密码强度分析(基于字符类型频率)
    def analyze_password_strength(password):
        # 定义字符类型
        uppercase = re.findall(r'[A-Z]', password)
        lowercase = re.findall(r'[a-z]', password)
        digits = re.findall(r'[0-9]', password)
        special = re.findall(r'[^A-Za-z0-9]', password)
        
        # 计算各类字符的频率
        char_types = {
            'uppercase': len(uppercase),
            'lowercase': len(lowercase),
            'digits': len(digits),
            'special': len(special)
        }
        
        # 计算密码强度分数
        score = 0
        if len(password) >= 8:
            score += 1
        if char_types['uppercase'] > 0:
            score += 1
        if char_types['lowercase'] > 0:
            score += 1
        if char_types['digits'] > 0:
            score += 1
        if char_types['special'] > 0:
            score += 1
        
        return {
            'length': len(password),
            'char_types': char_types,
            'strength_score': score,
            'strength': ['Very Weak', 'Weak', 'Medium', 'Strong', 'Very Strong', 'Excellent'][min(score, 5)]
        }
    
    # 测试密码强度分析
    passwords = ['password', 'Password123', 'P@ssw0rd!', 'a', 'Ab1!']
    
    print("\n密码强度分析:")
    for password in passwords:
        result = analyze_password_strength(password)
        print(f"密码: '{password}'")
        print(f"  长度: {result['length']}")
        print(f"  字符类型: {result['char_types']}")
        print(f"  强度分数: {result['strength_score']}/5")
        print(f"  强度评级: {result['strength']}")
    
except Exception as e:
    print(f"\n密码强度分析出错: {e}")
```

### 3.5 OrderedDict和ChainMap的高级应用

结合"OrderedDict"和"ChainMap"可以实现一些高级的数据管理模式.

```python
from collections import OrderedDict, ChainMap
import json

# 使用OrderedDict实现LRU缓存
try:
    class LRUCache:
        def __init__(self, capacity):
            self._capacity = capacity
            self._cache = OrderedDict()
        
        def get(self, key):
            """获取键值,如果存在则将其移到最近使用"""
            if key not in self._cache:
                return None
            
            # 将访问的项移到末尾(最近使用)
            self._cache.move_to_end(key)
            return self._cache[key]
        
        def put(self, key, value):
            """添加或更新键值对"""
            # 如果键已存在,先删除(会在后面重新添加到末尾)
            if key in self._cache:
                del self._cache[key]
            # 如果缓存已满,删除最久未使用的项(开头的项)
            elif len(self._cache) >= self._capacity:
                self._cache.popitem(last=False)
            
            # 添加新项到末尾(最近使用)
            self._cache[key] = value
        
        def __str__(self):
            return str(dict(self._cache))
    
    # 测试LRU缓存
    cache = LRUCache(3)
    cache.put(1, 'one')
    cache.put(2, 'two')
    cache.put(3, 'three')
    
    print(f"初始缓存: {cache}")
    
    # 访问已存在的项
    print(f"获取键1: {cache.get(1)}")
    print(f"访问后的缓存: {cache}")
    
    # 添加新项,超出容量
    cache.put(4, 'four')
    print(f"添加键4后的缓存: {cache}")  # 键2应该被移除
    
    # 验证键2已被移除
    print(f"获取键2: {cache.get(2)}")
    
except Exception as e:
    print(f"LRU缓存实现出错: {e}")

# 使用ChainMap实现配置管理
try:
    class ConfigManager:
        def __init__(self):
            # 创建默认配置
            self._defaults = {
                'debug': False,
                'log_level': 'INFO',
                'timeout': 30,
                'max_retries': 3
            }
            
            # 创建用户配置
            self._user_config = {}
            
            # 创建环境特定配置
            self._env_config = {}
            
            # 创建ChainMap,优先级为:环境配置 > 用户配置 > 默认配置
            self._config = ChainMap(self._env_config, self._user_config, self._defaults)
        
        def set_user_config(self, user_config):
            """设置用户配置"""
            self._user_config.clear()
            self._user_config.update(user_config)
        
        def set_env_config(self, env_config):
            """设置环境特定配置"""
            self._env_config.clear()
            self._env_config.update(env_config)
        
        def get(self, key, default=None):
            """获取配置值"""
            return self._config.get(key, default)
        
        def __getitem__(self, key):
            """使用下标访问配置"""
            return self._config[key]
        
        def __contains__(self, key):
            """检查键是否存在"""
            return key in self._config
        
        def get_all_configs(self):
            """获取所有配置及其来源"""
            return {
                'environment': dict(self._env_config),
                'user': dict(self._user_config),
                'defaults': dict(self._defaults),
                'effective': dict(self._config)
            }
    
    # 测试配置管理器
    config_manager = ConfigManager()
    
    # 获取默认配置
    print("\n默认配置:")
    print(f"调试模式: {config_manager['debug']}")
    print(f"日志级别: {config_manager['log_level']}")
    print(f"超时时间: {config_manager['timeout']}")
    
    # 设置用户配置
    config_manager.set_user_config({
        'debug': True,
        'timeout': 60,
        'api_key': 'user123'
    })
    
    print("\n设置用户配置后:")
    print(f"调试模式: {config_manager['debug']}")  # 应该为True
    print(f"超时时间: {config_manager['timeout']}")  # 应该为60
    print(f"日志级别: {config_manager['log_level']}")  # 应该保持默认值
    print(f"API密钥: {config_manager['api_key']}")  # 新添加的配置
    
    # 设置环境配置
    config_manager.set_env_config({
        'log_level': 'DEBUG',
        'timeout': 120,
        'env': 'production'
    })
    
    print("\n设置环境配置后:")
    print(f"调试模式: {config_manager['debug']}")  # 应该保持用户配置值
    print(f"日志级别: {config_manager['log_level']}")  # 应该为DEBUG
    print(f"超时时间: {config_manager['timeout']}")  # 应该为120
    print(f"环境: {config_manager['env']}")  # 环境特定配置
    
    # 打印所有配置
    all_configs = config_manager.get_all_configs()
    print("\n所有配置详情:")
    for config_type, config in all_configs.items():
        print(f"\n{config_type.capitalize()}:")
        for key, value in config.items():
            print(f"  {key}: {value}")
    
except Exception as e:
    print(f"\n配置管理器实现出错: {e}")
```

## 4. 实际应用场景

### 4.1 数据处理与分析

"collections"模块中的数据结构在数据处理和分析任务中非常有用,可以高效地处理和转换数据.

```python
from collections import defaultdict, Counter, namedtuple
import json

# 示例:销售数据分析
try:
    # 创建销售记录的命名元组
    Sale = namedtuple('Sale', ['date', 'product_id', 'quantity', 'price', 'region', 'customer_id'])
    
    # 模拟销售数据
    sales = [
        Sale('2023-01-01', 'P001', 2, 100, 'North', 'C001'),
        Sale('2023-01-02', 'P002', 1, 200, 'South', 'C002'),
        Sale('2023-01-03', 'P001', 3, 100, 'East', 'C003'),
        Sale('2023-01-04', 'P003', 2, 150, 'West', 'C004'),
        Sale('2023-01-05', 'P002', 1, 200, 'North', 'C005'),
        Sale('2023-01-06', 'P001', 1, 100, 'South', 'C006'),
        Sale('2023-01-07', 'P003', 3, 150, 'East', 'C007'),
        Sale('2023-01-08', 'P002', 2, 200, 'West', 'C008'),
        Sale('2023-01-09', 'P001', 2, 100, 'North', 'C009'),
        Sale('2023-01-10', 'P003', 1, 150, 'South', 'C010')
    ]
    
    # 1. 按产品ID统计销售总量和总收入
    product_stats = defaultdict(lambda: {'total_quantity': 0, 'total_revenue': 0})
    
    for sale in sales:
        product_stats[sale.product_id]['total_quantity'] += sale.quantity
        product_stats[sale.product_id]['total_revenue'] += sale.quantity * sale.price
    
    print("按产品统计:")
    for product_id, stats in product_stats.items():
        print(f"产品 {product_id}: 总销量 = {stats['total_quantity']}, 总收入 = ¥{stats['total_revenue']}")
    
    # 2. 按区域统计销售情况
    region_stats = defaultdict(lambda: {'total_sales': 0, 'total_revenue': 0, 'products': set()})
    
    for sale in sales:
        region_stats[sale.region]['total_sales'] += 1
        region_stats[sale.region]['total_revenue'] += sale.quantity * sale.price
        region_stats[sale.region]['products'].add(sale.product_id)
    
    print("\n按区域统计:")
    for region, stats in region_stats.items():
        print(f"区域 {region}: 销售次数 = {stats['total_sales']}, 总收入 = ¥{stats['total_revenue']}, 销售产品数 = {len(stats['products'])}")
    
    # 3. 查找最畅销的产品
    product_counter = Counter(sale.product_id for sale in sales)
    top_product = product_counter.most_common(1)[0]
    print(f"\n最畅销产品: {top_product[0]} (销售次数: {top_product[1]})")
    
    # 4. 分析客户购买行为
    customer_stats = defaultdict(lambda: {'total_spent': 0, 'products': set(), 'purchases': 0})
    
    for sale in sales:
        customer_stats[sale.customer_id]['total_spent'] += sale.quantity * sale.price
        customer_stats[sale.customer_id]['products'].add(sale.product_id)
        customer_stats[sale.customer_id]['purchases'] += 1
    
    # 找出消费最多的客户
    top_customer = max(customer_stats.items(), key=lambda x: x[1]['total_spent'])
    print(f"\n消费最多的客户: {top_customer[0]}")
    print(f"  总消费: ¥{top_customer[1]['total_spent']}")
    print(f"  购买产品数: {len(top_customer[1]['products'])}")
    print(f"  购买次数: {top_customer[1]['purchases']}")
    
except Exception as e:
    print(f"销售数据分析出错: {e}")

# 示例:文本数据分析
try:
    # 模拟社交媒体帖子数据
    posts = [
        {"id": 1, "text": "I love Python programming!", "likes": 100, "tags": ["python", "programming"]},
        {"id": 2, "text": "Data science is amazing", "likes": 85, "tags": ["data", "science"]},
        {"id": 3, "text": "Python for data analysis", "likes": 120, "tags": ["python", "data", "analysis"]},
        {"id": 4, "text": "Machine learning basics", "likes": 95, "tags": ["machine", "learning"]},
        {"id": 5, "text": "Programming tips and tricks", "likes": 75, "tags": ["programming", "tips"]}
    ]
    
    # 1. 统计标签出现频率
    tag_counter = Counter()
    for post in posts:
        tag_counter.update(post["tags"])
    
    print("\n标签频率统计:")
    for tag, count in tag_counter.most_common():
        print(f"{tag}: {count}")
    
    # 2. 分析文本内容
    import re
    all_text = " ".join(post["text"] for post in posts)
    words = re.findall(r'\b\w+\b', all_text.lower())
    word_counter = Counter(words)
    
    # 过滤常见停用词
    stop_words = {'i', 'love', 'is', 'amazing', 'for', 'and', 'basics', 'tips', 'tricks'}
    filtered_words = [word for word in words if word not in stop_words]
    filtered_counter = Counter(filtered_words)
    
    print("\n最常见的关键词:")
    for word, count in filtered_counter.most_common(5):
        print(f"{word}: {count}")
    
    # 3. 按点赞数分析帖子
    posts_sorted_by_likes = sorted(posts, key=lambda x: x["likes"], reverse=True)
    
    print("\n按点赞数排序的帖子:")
    for i, post in enumerate(posts_sorted_by_likes, 1):
        print(f"{i}. 帖子 {post['id']}: {post['likes']} 点赞, 标签: {', '.join(post['tags'])}")
    
except Exception as e:
    print(f"\n文本数据分析出错: {e}")
```

### 4.2 算法实现

"collections"模块的数据结构可以用于实现各种算法,如排序,搜索,图算法等.

```python
from collections import deque, defaultdict, Counter

# 示例:使用collections实现算法

# 1. 使用deque实现广度优先搜索(BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    traversal_order = []
    
    while queue:
        current = queue.popleft()
        traversal_order.append(current)
        
        # 访问所有未访问的邻居
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal_order

# 测试BFS
print("广度优先搜索示例:")
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [7],
    4: [8],
    5: [9],
    6: [],
    7: [],
    8: [],
    9: []
}
bfs_result = bfs(graph, 1)
print(f"BFS遍历顺序: {bfs_result}")

# 2. 使用Counter实现拓扑排序
def topological_sort(graph):
    # 计算每个节点的入度
    in_degree = Counter()
    for node in graph:
        if node not in in_degree:
            in_degree[node] = 0
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    
    # 将所有入度为0的节点加入队列
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current)
        
        # 更新邻居节点的入度
        for neighbor in graph.get(current, []):
            in_degree[neighbor] -= 1
            # 如果入度变为0,加入队列
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # 检查是否存在环
    if len(result) != len(in_degree):
        raise ValueError("图中存在环,无法进行拓扑排序")
    
    return result

# 测试拓扑排序
print("\n拓扑排序示例:")
dag = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}
try:
    topo_result = topological_sort(dag)
    print(f"拓扑排序结果: {topo_result}")
except ValueError as e:
    print(f"拓扑排序失败: {e}")

# 3. 使用defaultdict实现Dijkstra最短路径算法
def dijkstra(graph, start):
    # 初始化距离字典
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # 使用集合跟踪已访问的节点
    visited = set()
    
    while visited != set(graph):
        # 找到未访问节点中距离最小的节点
        current = min(
            (node for node in graph if node not in visited),
            key=lambda node: distances[node]
        )
        
        visited.add(current)
        
        # 更新邻居节点的距离
        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                new_distance = distances[current] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
    
    return distances

# 测试Dijkstra算法
print("\nDijkstra最短路径算法示例:")
weighted_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
shortest_paths = dijkstra(weighted_graph, 'A')
print(f"从A到各节点的最短距离: {shortest_paths}")

# 4. 使用deque实现滑动窗口最大值
def sliding_window_max(nums, k):
    result = []
    window = deque()  # 存储索引,保证队列中的元素按降序排列
    
    for i, num in enumerate(nums):
        # 移除窗口外的元素
        while window and window[0] < i - k + 1:
            window.popleft()
        
        # 移除比当前元素小的元素
        while window and nums[window[-1]] < num:
            window.pop()
        
        window.append(i)
        
        # 当窗口达到大小k时开始记录结果
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result

# 测试滑动窗口最大值
print("\n滑动窗口最大值示例:")
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
max_values = sliding_window_max(nums, k)
print(f"数组: {nums}")
print(f"窗口大小: {k}")
print(f"滑动窗口最大值: {max_values}")
```

### 4.3 缓存和内存管理

"collections"模块的数据结构可以用于实现各种缓存策略和内存管理机制.

```python
from collections import OrderedDict, defaultdict, deque
import time

# 示例:实现不同类型的缓存

# 1. 使用OrderedDict实现LRU(最近最少使用)缓存
class LRUCache:
    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = OrderedDict()
        self._hits = 0
        self._misses = 0
    
    def get(self, key):
        """获取键值,如果存在则将其移到最近使用"""
        if key not in self._cache:
            self._misses += 1
            return None
        
        self._hits += 1
        # 将访问的项移到末尾(最近使用)
        self._cache.move_to_end(key)
        return self._cache[key]
    
    def put(self, key, value):
        """添加或更新键值对"""
        # 如果键已存在,先删除(会在后面重新添加到末尾)
        if key in self._cache:
            del self._cache[key]
        # 如果缓存已满,删除最久未使用的项(开头的项)
        elif len(self._cache) >= self._capacity:
            self._cache.popitem(last=False)
        
        # 添加新项到末尾(最近使用)
        self._cache[key] = value
    
    def stats(self):
        """获取缓存统计信息"""
        total = self._hits + self._misses
        hit_rate = (self._hits / total) * 100 if total > 0 else 0
        return {
            'hits': self._hits,
            'misses': self._misses,
            'total': total,
            'hit_rate': hit_rate,
            'size': len(self._cache),
            'capacity': self._capacity
        }
    
    def clear(self):
        """清空缓存"""
        self._cache.clear()
        self._hits = 0
        self._misses = 0

# 测试LRU缓存
print("LRU缓存示例:")
lru_cache = LRUCache(capacity=3)

# 模拟缓存访问模式
access_sequence = ['A', 'B', 'C', 'A', 'D', 'B', 'E', 'C']
for i, key in enumerate(access_sequence):
    # 模拟缓存操作
    if i % 2 == 0:  # 偶数索引位置执行put
        lru_cache.put(key, f"Value-{key}-{i}")
        print(f"Put: {key} -> Value-{key}-{i}")
    else:  # 奇数索引位置执行get
        value = lru_cache.get(key)
        print(f"Get: {key} -> {value}")

# 打印缓存统计信息
stats = lru_cache.stats()
print(f"\n缓存统计信息:")
print(f"  缓存命中率: {stats['hit_rate']:.1f}%")
print(f"  命中次数: {stats['hits']}")
print(f"  未命中次数: {stats['misses']}")
print(f"  缓存大小: {stats['size']}/{stats['capacity']}")

# 2. 使用deque实现FIFO(先进先出)缓存
class FIFOCache:
    def __init__(self, capacity):
        self._capacity = capacity
        self._cache = {}
        self._order = deque()
        self._hits = 0
        self._misses = 0
    
    def get(self, key):
        """获取键值"""
        if key not in self._cache:
            self._misses += 1
            return None
        
        self._hits += 1
        return self._cache[key]
    
    def put(self, key, value):
        """添加或更新键值对"""
        # 如果键已存在,不需要改变顺序
        if key in self._cache:
            self._cache[key] = value
            return
        
        # 如果缓存已满,删除最早添加的项
        if len(self._cache) >= self._capacity:
            oldest_key = self._order.popleft()
            del self._cache[oldest_key]
        
        # 添加新项
        self._order.append(key)
        self._cache[key] = value
    
    def stats(self):
        """获取缓存统计信息"""
        total = self._hits + self._misses
        hit_rate = (self._hits / total) * 100 if total > 0 else 0
        return {
            'hits': self._hits,
            'misses': self._misses,
            'total': total,
            'hit_rate': hit_rate,
            'size': len(self._cache),
            'capacity': self._capacity
        }

# 测试FIFO缓存
print("\nFIFO缓存示例:")
fifo_cache = FIFOCache(capacity=3)

# 使用相同的访问模式
access_sequence = ['A', 'B', 'C', 'A', 'D', 'B', 'E', 'C']
for i, key in enumerate(access_sequence):
    # 模拟缓存操作
    if i % 2 == 0:  # 偶数索引位置执行put
        fifo_cache.put(key, f"Value-{key}-{i}")
        print(f"Put: {key} -> Value-{key}-{i}")
    else:  # 奇数索引位置执行get
        value = fifo_cache.get(key)
        print(f"Get: {key} -> {value}")

# 打印缓存统计信息
fifo_stats = fifo_cache.stats()
print(f"\n缓存统计信息:")
print(f"  缓存命中率: {fifo_stats['hit_rate']:.1f}%")
print(f"  命中次数: {fifo_stats['hits']}")
print(f"  未命中次数: {fifo_stats['misses']}")
print(f"  缓存大小: {fifo_stats['size']}/{fifo_stats['capacity']}")

# 3. 简单的定时缓存(带过期时间)
class TimedCache:
    def __init__(self, default_ttl=300):  # 默认过期时间5分钟
        self._cache = {}
        self._default_ttl = default_ttl
    
    def get(self, key):
        """获取键值,如果已过期则返回None"""
        if key not in self._cache:
            return None
        
        value, expiry = self._cache[key]
        current_time = time.time()
        
        # 检查是否过期
        if current_time > expiry:
            del self._cache[key]
            return None
        
        return value
    
    def put(self, key, value, ttl=None):
        """添加或更新键值对,设置过期时间"""
        ttl = ttl or self._default_ttl
        expiry = time.time() + ttl
        self._cache[key] = (value, expiry)
    
    def clear_expired(self):
        """清理所有过期项"""
        current_time = time.time()
        expired_keys = [key for key, (_, expiry) in self._cache.items() if current_time > expiry]
        
        for key in expired_keys:
            del self._cache[key]
        
        return len(expired_keys)
    
    def size(self):
        """获取缓存大小"""
        return len(self._cache)

# 测试定时缓存
print("\n定时缓存示例:")
timed_cache = TimedCache(default_ttl=2)  # 简化测试,使用2秒过期时间

# 添加缓存项
timed_cache.put('key1', 'value1')
timed_cache.put('key2', 'value2', ttl=1)  # 1秒后过期
print(f"初始缓存大小: {timed_cache.size()}")
print(f"获取key1: {timed_cache.get('key1')}")
print(f"获取key2: {timed_cache.get('key2')}")

# 等待1秒后
print("\n等待1秒...")
time.sleep(1)
print(f"获取key2(应该已过期): {timed_cache.get('key2')}")
print(f"获取key1(应该未过期): {timed_cache.get('key1')}")

# 清理过期项
expired_count = timed_cache.clear_expired()
print(f"清理了 {expired_count} 个过期项")
print(f"当前缓存大小: {timed_cache.size()}")

# 等待2秒后
print("\n再等待2秒...")
time.sleep(2)
print(f"获取key1(应该已过期): {timed_cache.get('key1')}")
print(f"当前缓存大小: {timed_cache.size()}")
```

### 4.4 事件处理和消息队列

"collections"模块的数据结构可以用于实现事件处理系统和消息队列.

```python
```python
"""  # 闭合未闭合的双三引号
from collections import namedtuple, defaultdict, OrderedDict
import json

# 示例:与JSON结合使用

# 1. 使用namedtuple进行数据序列化和反序列化
try:
    # 定义命名元组
    Person = namedtuple('Person', ['name', 'age', 'city', 'skills'])
    
    # 创建实例
    person1 = Person('Alice', 30, 'New York', ['Python', 'Data Science'])
    person2 = Person('Bob', 25, 'Boston', ['Java', 'Spring'])
    
    # 序列化为JSON
    def namedtuple_to_dict(obj):
        """将namedtuple转换为可序列化的字典"""
        if isinstance(obj, tuple) and hasattr(obj, '_asdict'):
            return obj._asdict()
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")
    
    # 转换为列表
    people = [person1, person2]
    
    # 序列化为JSON字符串
    # 使用自定义编码器或手动转换
    people_dicts = [p._asdict() for p in people]
    json_str = json.dumps(people_dicts, indent=2)
    
    print("命名元组序列化示例:")
    print(f"原始数据: {people}")
    print(f"JSON字符串:\n{json_str}")
    
    # 反序列化
    loaded_dicts = json.loads(json_str)
    loaded_people = [Person(**d) for d in loaded_dicts]
    
    print(f"\n反序列化后: {loaded_people}")
    
except Exception as e:
    print(f"命名元组序列化出错: {e}")

# 2. 使用defaultdict处理复杂JSON数据
try:
    # 模拟复杂JSON数据
    json_data = '''
    {
        "users": [
            {"id": 1, "name": "Alice", "roles": ["admin", "user"]},
            {"id": 2, "name": "Bob", "roles": ["user"]},
            {"id": 3, "name": "Charlie", "roles": ["editor", "user"]}
        ],
        "groups": [
            {"id": 101, "name": "Developers", "members": [1, 2]},
            {"id": 102, "name": "Managers", "members": [1, 3]}
        ]
    }
    '''
    
    # 解析JSON
    data = json.loads(json_data)
    
    # 使用defaultdict按角色分组用户
    users_by_role = defaultdict(list)
    
    for user in data['users']:
        for role in user['roles']:
            users_by_role[role].append(user['name'])
    
    print("\n按角色分组的用户:")
    for role, users in users_by_role.items():
        print(f"{role}: {', '.join(users)}")
    
    # 创建用户ID到用户名的映射
    user_id_to_name = {user['id']: user['name'] for user in data['users']}
    
    # 格式化组信息
    groups_with_names = []
    for group in data['groups']:
        group_info = {
            'name': group['name'],
            'members': [user_id_to_name[member_id] for member_id in group['members']]
        }
        groups_with_names.append(group_info)
    
    print("\n组及其成员:")
    for group in groups_with_names:
        print(f"{group['name']}: {', '.join(group['members'])}")
    
except Exception as e:
    print(f"JSON数据处理出错: {e}")

# 3. 使用OrderedDict保持JSON数据的顺序
try:
    # 注意:在Python 3.7+中,普通字典也保持插入顺序
    # 但使用OrderedDict可以确保跨版本的一致性
    ordered_data = OrderedDict()
    ordered_data['id'] = 1001
    ordered_data['name'] = 'Product X'
    ordered_data['price'] = 99.99
    ordered_data['stock'] = 50
    ordered_data['tags'] = ['new', 'popular']
    
    # 序列化为JSON
    ordered_json = json.dumps(ordered_data, indent=2)
    
    print("\n使用OrderedDict保持顺序的JSON:")
    print(ordered_json)
    
except Exception as e:
    print(f"OrderedDict JSON示例出错: {e}")
"""

### 4.6 游戏开发中的应用

"collections"模块的数据结构在游戏开发中也有广泛的应用,如游戏状态管理,实体组件系统等.

"""python
from collections import namedtuple, deque, defaultdict, Counter

# 示例:游戏开发中的应用

# 1. 使用namedtuple定义游戏实体
try:
    # 定义游戏实体组件
    Position = namedtuple('Position', ['x', 'y'])
    Velocity = namedtuple('Velocity', ['dx', 'dy'])
    Health = namedtuple('Health', ['current', 'max'])
    Collision = namedtuple('Collision', ['radius'])
    Renderable = namedtuple('Renderable', ['sprite', 'z_order'])
    
    # 简单的实体组件系统
    class Entity:
        def __init__(self, entity_id):
            self.id = entity_id
            self.components = {}
        
        def add_component(self, component_type, component):
            """添加组件"""
            self.components[component_type] = component
        
        def get_component(self, component_type):
            """获取组件"""
            return self.components.get(component_type)
        
        def has_component(self, component_type):
            """检查是否有组件"""
            return component_type in self.components
    
    # 创建实体管理器
    class EntityManager:
        def __init__(self):
            self.entities = {}
            self.next_id = 1
            # 使用defaultdict按组件类型索引实体
            self.entities_by_component = defaultdict(set)
        
        def create_entity(self):
            """创建新实体"""
            entity_id = self.next_id
            self.next_id += 1
            entity = Entity(entity_id)
            self.entities[entity_id] = entity
            return entity
        
        def add_component(self, entity_id, component_type, component):
            """为实体添加组件"""
            if entity_id in self.entities:
                entity = self.entities[entity_id]
                entity.add_component(component_type, component)
                self.entities_by_component[component_type].add(entity_id)
        
        def get_entities_with_component(self, component_type):
            """获取具有特定组件的所有实体"""
            entity_ids = self.entities_by_component.get(component_type, set())
            return [self.entities[entity_id] for entity_id in entity_ids]
        
        def remove_entity(self, entity_id):
            """移除实体"""
            if entity_id in self.entities:
                entity = self.entities[entity_id]
                # 从组件索引中移除
                for component_type in entity.components:
                    if entity_id in self.entities_by_component[component_type]:
                        self.entities_by_component[component_type].remove(entity_id)
                # 移除实体
                del self.entities[entity_id]
    
    # 测试实体组件系统
    print("游戏实体组件系统示例:")
    em = EntityManager()
    
    # 创建玩家实体
    player = em.create_entity()
    em.add_component(player.id, 'position', Position(100, 100))
    em.add_component(player.id, 'velocity', Velocity(0, 0))
    em.add_component(player.id, 'health', Health(100, 100))
    em.add_component(player.id, 'collision', Collision(20))
    em.add_component(player.id, 'renderable', Renderable('player.png', 10))
    
    # 创建敌人实体
    enemy = em.create_entity()
    em.add_component(enemy.id, 'position', Position(200, 200))
    em.add_component(enemy.id, 'velocity', Velocity(-1, 0))
    em.add_component(enemy.id, 'health', Health(50, 50))
    em.add_component(enemy.id, 'collision', Collision(15))
    em.add_component(enemy.id, 'renderable', Renderable('enemy.png', 10))
    
    # 创建静态对象
    obstacle = em.create_entity()
    em.add_component(obstacle.id, 'position', Position(150, 150))
    em.add_component(obstacle.id, 'collision', Collision(30))
    em.add_component(obstacle.id, 'renderable', Renderable('obstacle.png', 5))
    
    # 查询实体
    print(f"\n实体总数: {len(em.entities)}")
    
    # 获取所有有碰撞组件的实体
    collidable_entities = em.get_entities_with_component('collision')
    print(f"可碰撞实体数: {len(collidable_entities)}")
    
    # 获取所有需要渲染的实体
    renderable_entities = em.get_entities_with_component('renderable')
    print(f"可渲染实体数: {len(renderable_entities)}")
    
    # 示例:简单的物理更新
    def update_physics(entities):
        for entity in entities:
            if entity.has_component('position') and entity.has_component('velocity'):
                pos = entity.get_component('position')
                vel = entity.get_component('velocity')
                # 注意:namedtuple是不可变的,需要创建新实例
                new_pos = Position(pos.x + vel.dx, pos.y + vel.dy)
                entity.add_component('position', new_pos)
                print(f"实体 {entity.id} 移动到 ({new_pos.x}, {new_pos.y})")
    
    # 更新物理
    print("\n更新物理状态:")
    update_physics(em.get_entities_with_component('velocity'))
    
except Exception as e:
    print(f"游戏实体组件系统示例出错: {e}")

# 2. 使用deque实现游戏状态栈
try:
    class GameState:
        def __init__(self, name):
            self.name = name
            print(f"创建游戏状态: {name}")
        
        def enter(self):
            print(f"进入状态: {self.name}")
        
        def exit(self):
            print(f"退出状态: {self.name}")
        
        def update(self, dt):
            print(f"更新状态: {self.name} (dt={dt})")
    
    class GameStateManager:
        def __init__(self):
            self._states = deque()
        
        def push_state(self, state):
            """推入新状态,暂停当前状态"""
            if self._states:
                self._states[-1].exit()
            self._states.append(state)
            state.enter()
        
        def pop_state(self):
            """弹出当前状态,恢复上一个状态"""
            if not self._states:
                return None
            
            current = self._states.pop()
            current.exit()
            
            if self._states:
                self._states[-1].enter()
            
            return current
        
        def replace_state(self, state):
            """替换当前状态"""
            if self._states:
                self._states.pop().exit()
            self._states.append(state)
            state.enter()
        
        def update(self, dt):
            """更新当前状态"""
            if self._states:
                self._states[-1].update(dt)
        
        def current_state(self):
            """获取当前状态"""
            return self._states[-1] if self._states else None
        
        def state_count(self):
            """获取状态栈大小"""
            return len(self._states)
    
    # 测试游戏状态管理器
    print("\n游戏状态管理器示例:")
    gsm = GameStateManager()
    
    # 推入主菜单状态
    main_menu = GameState("主菜单")
    gsm.push_state(main_menu)
    
    # 模拟更新
    gsm.update(0.016)
    
    # 推入游戏状态
    game = GameState("游戏中")
    gsm.push_state(game)
    gsm.update(0.016)
    
    # 推入暂停菜单
    pause_menu = GameState("暂停菜单")
    gsm.push_state(pause_menu)
    gsm.update(0.016)
    
    # 弹出暂停菜单
    print("\n弹出暂停菜单:")
    gsm.pop_state()
    gsm.update(0.016)
    
    # 替换游戏状态为游戏结束状态
    game_over = GameState("游戏结束")
    print("\n替换为游戏结束状态:")
    gsm.replace_state(game_over)
    gsm.update(0.016)
    
except Exception as e:
    print(f"游戏状态管理器示例出错: {e}")
"""

## 5. 性能分析

### 5.1 时间复杂度分析

不同的"collections"数据结构在各种操作上的时间复杂度各不相同.下面是一个比较表:

| 数据结构 | 操作 | 时间复杂度 | 空间复杂度 |
|---------|------|-----------|-----------|
| **namedtuple** | 创建实例 | O(n) | O(n) |
| | 访问元素 | O(1) | O(1) |
| | 替换元素(创建新实例) | O(n) | O(n) |
| **deque** | append/pop(两端) | O(1) | O(1) |
| | appendleft/popleft | O(1) | O(1) |
| | 中间插入/删除 | O(n) | O(1) |
| | 访问任意位置 | O(n) | O(1) |
| **defaultdict** | get/set | O(1) 平均 | O(1) 平均 |
| | 访问不存在的键 | O(1) 平均 | O(1) 平均 |
| **Counter** | 创建 | O(n) | O(k),k为不同元素数量 |
| | 增加计数 | O(1) 平均 | O(1) 平均 |
| | most_common | O(n log n) | O(k) |
| **OrderedDict** | get/set | O(1) 平均 | O(1) 平均 |
| | 移动元素到末尾 | O(1) | O(1) |
| | 迭代 | O(n) | O(1) |
| **ChainMap** | get | O(k),k为映射数量 | O(1) |
| | set(仅修改第一个映射) | O(1) | O(1) |
| | 迭代 | O(n) | O(1) |

### 5.2 性能比较测试

下面是一些常见操作的性能比较测试:

"``python
import time
import random
from collections import deque, defaultdict, Counter, OrderedDict, ChainMap

# 性能测试函数
def timeit(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    return end - start, result

# 测试参数
N = 100000  # 操作次数

# 1. 列表 vs deque 性能比较
print("列表 vs deque 性能比较:")

# 列表从头部添加元素
def list_prepend_test(n):
    lst = []
    for i in range(n):
        lst.insert(0, i)
    return lst

# deque从头部添加元素
def deque_prepend_test(n):
    dq = deque()
    for i in range(n):
        dq.appendleft(i)
    return dq

# 执行测试
list_time, _ = timeit(list_prepend_test, N)
deque_time, _ = timeit(deque_prepend_test, N)

print(f"列表头部插入 {N} 元素耗时: {list_time:.6f} 秒")
print(f"deque头部插入 {N} 元素耗时: {deque_time:.6f} 秒")
print(f"deque比列表快 {list_time/deque_time:.2f} 倍")

# 2. dict vs defaultdict 性能比较
print("\ndict vs defaultdict 性能比较:")

# 使用普通dict进行计数
def dict_count_test(data):
    counts = {}
    for item in data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts

# 使用defaultdict进行计数
def defaultdict_count_test(data):
    counts = defaultdict(int)
    for item in data:
        counts[item] += 1
    return counts

# 准备测试数据
data = [random.randint(0, 10000) for _ in range(N)]

# 执行测试
dict_time, _ = timeit(dict_count_test, data)
defaultdict_time, _ = timeit(defaultdict_count_test, data)

print(f"dict计数 {N} 元素耗时: {dict_time:.6f} 秒")
print(f"defaultdict计数 {N} 元素耗时: {defaultdict_time:.6f} 秒")
print(f"defaultdict比dict快 {dict_time/defaultdict_time:.2f} 倍")

# 3. Counter性能测试
print("\nCounter性能测试:")

# 使用Counter计数
def counter_count_test(data):
    return Counter(data)

# 执行测试
counter_time, _ = timeit(counter_count_test, data)

print(f"Counter计数 {N} 元素耗时: {counter_time:.6f} 秒")
print(f"Counter比dict快 {dict_time/counter_time:.2f} 倍")
print(f"Counter比defaultdict快 {defaultdict_time/counter_time:.2f} 倍")

# 4. 访问顺序性能测试
print("\n有序访问性能测试:")

# 准备数据
items = [(i, f"value_{i}") for i in range(N)]

# 使用dict并保持插入顺序
def dict_order_test(items):
    d = {}
    for key, value in items:
        d[key] = value
    # 按插入顺序访问(Python 3.7+)
    return list(d.items())

# 使用OrderedDict
def ordered_dict_test(items):
    od = OrderedDict()
    for key, value in items:
        od[key] = value
    return list(od.items())

# 执行测试
dict_order_time, _ = timeit(dict_order_test, items)
ordered_dict_time, _ = timeit(ordered_dict_test, items)

print(f"dict保持顺序耗时: {dict_order_time:.6f} 秒")
print(f"OrderedDict保持顺序耗时: {ordered_dict_time:.6f} 秒")
if dict_order_time > ordered_dict_time:
    print(f"OrderedDict比dict快 {dict_order_time/ordered_dict_time:.2f} 倍")
else:
    print(f"dict比OrderedDict快 {ordered_dict_time/dict_order_time:.2f} 倍")

# 5. ChainMap性能测试
print("\nChainMap性能测试:")

# 准备多个字典
dicts = [
    {i: f"value_{i}_1" for i in range(0, N, 10)},
    {i: f"value_{i}_2" for i in range(5, N, 10)},
    {i: f"value_{i}_3" for i in range(2, N, 10)}
]

# 使用ChainMap访问
def chain_map_access_test(cm, keys):
    results = []
    for key in keys:
        if key in cm:
            results.append(cm[key])
    return results

# 手动合并字典并访问
def merged_dict_access_test(dicts, keys):
    merged = {}
    # 注意顺序,后合并的字典优先级高
    for d in reversed(dicts):
        merged.update(d)
    
    results = []
    for key in keys:
        if key in merged:
            results.append(merged[key])
    return results

# 创建ChainMap
cm = ChainMap(*dicts)

# 准备要查找的键
keys = [random.randint(0, N) for _ in range(N//10)]

# 执行测试
chain_map_time, _ = timeit(chain_map_access_test, cm, keys)
merged_dict_time, _ = timeit(merged_dict_access_test, dicts, keys)

print(f"ChainMap访问耗时: {chain_map_time:.6f} 秒")
print(f"合并字典访问耗时: {merged_dict_time:.6f} 秒")
if chain_map_time < merged_dict_time:
    print(f"ChainMap比合并字典快 {merged_dict_time/chain_map_time:.2f} 倍")
else:
    print(f"合并字典比ChainMap快 {chain_map_time/merged_dict_time:.2f} 倍")
```

## 6. 使用注意事项

### 6.1 namedtuple的注意事项

1. **不可变性**:"namedtuple"创建的对象是不可变的,一旦创建就不能修改其属性值.
   - 如果需要修改,必须使用"_replace()"方法创建新实例.

2. **字段名称限制**:字段名称不能是Python关键字或以下划线开头.
   - 使用"rename=True"参数可以自动重命名无效的字段名.

3. **内存占用**:虽然"namedtuple"比普通类更节省内存,但比普通元组略大.

4. **继承问题**:当继承"namedtuple"创建子类时,需要注意正确处理初始化方法.

```python
# 正确使用namedtuple的例子
from collections import namedtuple

# 使用rename=True处理无效字段名
Person = namedtuple('Person', ['class', 'def', 'age'], rename=True)
p = Person(1, 2, 30)
print(p)  # 输出: Person(_0=1, _1=2, age=30)

# 正确继承namedtuple
class Employee(namedtuple('EmployeeBase', ['name', 'id', 'department'])):
    def __new__(cls, name, id, department, salary=None):
        self = super(Employee, cls).__new__(cls, name, id, department)
        self.salary = salary  # 注意:这会创建一个额外的属性,不在namedtuple结构中
        return self
    
    def get_info(self):
        return f"{self.name} (ID: {self.id}) works in {self.department}"

e = Employee("Alice", 1001, "Engineering", 80000)
print(e.get_info())  # 输出: Alice (ID: 1001) works in Engineering
```

### 6.2 deque的注意事项

1. **随机访问性能**:"deque"在两端操作非常高效,但在中间位置访问或修改效率较低.
   - 如果需要频繁访问随机位置的元素,应使用列表而不是"deque".

2. **maxlen限制**:设置"maxlen"后,当队列达到最大长度时,新元素的添加会自动移除相反端的旧元素.
   - 这是一个方便的特性,但需要注意可能的数据丢失.

3. **线程安全性**:"deque"的"append"和"popleft"操作在CPython中是原子的,使其在多线程环境中可以安全使用.

```python
# deque使用注意事项示例
from collections import deque
import threading
import time

# 测试多线程环境下的deque
shared_queue = deque(maxlen=1000)
lock = threading.Lock()

def producer():
    for i in range(10000):
        shared_queue.append(i)
        time.sleep(0.0001)  # 小延迟

def consumer():
    items_consumed = 0
    while items_consumed < 10000:
        try:
            with lock:  # 在多步骤操作时仍需要锁
                if shared_queue:
                    shared_queue.popleft()
                    items_consumed += 1
        except IndexError:
            pass
        time.sleep(0.0001)  # 小延迟

# 在实际应用中,如果只是简单的append和popleft操作,
# 可以不使用锁,因为这些操作在CPython中是原子的
```

### 6.3 defaultdict和Counter的注意事项

1. **默认值生成**:"defaultdict"在访问不存在的键时会自动创建并添加到字典中.
   - 这可能导致意外的内存使用,特别是在处理大量数据时.

2. **Counter的非负性**:"Counter"在减法操作后会自动过滤掉计数为零或负数的项.
   - 如果需要保留这些项,需要使用其他方法.

3. **类型限制**:"Counter"的键必须是可哈希的.

```python
# defaultdict和Counter使用注意事项示例
from collections import defaultdict, Counter

# 注意defaultdict的副作用
print("defaultdict副作用示例:")
d = defaultdict(int)
print("字典初始状态:", dict(d))
print("访问不存在的键'default':", d['default'])
print("访问后字典状态:", dict(d))  # 'default'键已被添加

# Counter减法操作过滤负计数
print("\nCounter减法操作示例:")
c1 = Counter(a=3, b=2, c=1)
c2 = Counter(a=1, b=3, d=2)
print("c1:", c1)
print("c2:", c2)
print("c1 - c2:", c1 - c2)  # b的计数变为0,所以被过滤掉

# 如果需要保留零或负计数,需要使用其他方法
c3 = Counter()
for item, count in c1.items():
    c3[item] = count - c2.get(item, 0)
print("使用自定义方法计算差:", c3)
```

### 6.4 OrderedDict和ChainMap的注意事项

1. **OrderedDict的性能**:在Python 3.7+中,普通字典也保持插入顺序,但"OrderedDict"提供了额外的方法,如"move_to_end()".
   - 如果只需要保持顺序而不需要这些额外方法,可以使用普通字典以获得更好的性能.

2. **ChainMap的修改行为**:对"ChainMap"的修改只会影响第一个映射.
   - 如果需要修改其他映射中的值,需要直接访问该映射.

3. **内存使用**:"ChainMap"不会创建新的字典,而是引用原始字典.
   - 这节省了内存,但也意味着对原始字典的修改会影响"ChainMap".

```python
# OrderedDict和ChainMap使用注意事项示例
from collections import OrderedDict, ChainMap

# Python 3.7+中普通字典也保持顺序
print("普通字典vs OrderedDict:")
d = {}
d['c'] = 3
d['a'] = 1
d['b'] = 2
print("普通字典顺序:", list(d.keys()))

od = OrderedDict()
od['c'] = 3
od['a'] = 1
od['b'] = 2
print("OrderedDict顺序:", list(od.keys()))

# OrderedDict特有方法
od.move_to_end('c', last=False)  # 移动到开头
print("移动'c'到开头后:", list(od.keys()))

# ChainMap修改行为
print("\nChainMap修改行为:")
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 20, 'c': 3}
cm = ChainMap(dict1, dict2)

print("原始ChainMap:", dict(cm))
print("修改'dict1['a']'前: dict1 =", dict1)
cm['a'] = 100  # 修改只会影响第一个映射
print("修改后ChainMap:", dict(cm))
print("修改后dict1:", dict1)
print("修改后dict2:", dict2)

# 原始字典修改影响ChainMap
dict2['c'] = 300
print("\n修改dict2后ChainMap:", dict(cm))
```

## 7. 总结与最佳实践

### 7.1 主要优势

1. **代码可读性**:"namedtuple"通过名称访问元素,使代码更易读,更易维护.

2. **性能优化**:"deque"在两端操作的性能远优于列表,"Counter"提供了高效的计数功能.

3. **代码简洁性**:"defaultdict"避免了手动检查键是否存在的需要,使代码更简洁.

4. **功能增强**:各种数据结构提供了标准容器所没有的额外功能,如"OrderedDict"的顺序保持,"ChainMap"的多字典合并等.

5. **内存效率**:大多数"collections"数据结构比自定义类更节省内存.

### 7.2 最佳实践

1. **选择合适的数据结构**:
   - 需要快速访问,修改,删除两端元素时,使用"deque".
   - 需要为不存在的键提供默认值时,使用"defaultdict".
   - 需要计数功能时,使用"Counter".
   - 需要保持插入顺序或使用特殊顺序操作时,使用"OrderedDict".
   - 需要将多个字典视为单一映射时,使用"ChainMap".
   - 需要不可变,轻量级的数据容器时,使用"namedtuple".

2. **避免性能陷阱**:
   - 避免在"deque"中进行随机访问或中间插入/删除操作.
   - 使用"Counter"代替手动实现的计数逻辑.
   - 对于简单的命名数据容器,优先使用"namedtuple"而不是自定义类.

3. **正确处理边界情况**:
   - 使用"defaultdict"时注意默认值的选择,避免意外创建大量不必要的键.
   - 使用"Counter"时注意减法操作会自动过滤负计数.
   - 使用"ChainMap"时注意修改只会影响第一个映射.

4. **代码组织**:
   - 为"namedtuple"创建有意义的名称和字段,提高代码可读性.
   - 将相关的数据结构操作封装在函数或类中,提高代码重用性.
   - 对于复杂的数据结构组合,考虑创建自定义的容器类.

### 7.3 选择使用建议

| 场景 | 推荐数据结构 | 原因 |
|------|------------|------|
| 频繁从两端添加/删除元素 | deque | O(1)时间复杂度,远优于列表的O(n) |
| 统计元素出现频率 | Counter | 专门为计数设计,比手动实现更高效,更简洁 |
| 分组数据(如按首字母分组单词) | defaultdict | 避免手动检查键是否存在,代码更简洁 |
| 需要保持插入顺序的字典 | OrderedDict | 提供额外的顺序操作方法,如move_to_end |
| 配置管理(默认配置+用户配置+环境配置) | ChainMap | 无需合并字典,支持优先级查找 |
| 不可变的数据记录(如坐标,RGB颜色等) | namedtuple | 比字典更轻量,比普通元组更易读 |
| 缓存实现(如LRU缓存) | OrderedDict | 可以高效地移动最近访问的项到末尾 |
| 事件处理系统 | defaultdict(list) | 方便存储和管理事件监听器 |
| 消息队列 | deque | 高效的两端操作,支持最大长度限制 |
| 游戏开发中的实体组件系统 | namedtuple + defaultdict | 轻量级组件定义,高效的组件查询 |

### 7.4 学习总结

"collections"模块提供了一系列强大的容器数据类型,它们是对Python内置容器的扩展和优化.通过本教程的学习,我们了解了:

1. **核心数据结构**:"namedtuple","deque","defaultdict","Counter","OrderedDict","ChainMap"的基本使用方法和特性.

2. **高级应用**:如何将这些数据结构用于实现复杂的算法,缓存策略,事件处理系统等.

3. **实际场景**:在数据处理,算法实现,缓存管理,游戏开发等领域的具体应用.

4. **性能特性**:各种数据结构的时间和空间复杂度,以及在不同场景下的性能表现.

5. **使用注意事项**:避免常见的陷阱和错误使用方式.

6. **最佳实践**:如何根据具体需求选择合适的数据结构,以及如何高效地使用它们.

掌握"collections"模块的数据结构,可以大大提高Python编程的效率和代码质量.在实际开发中,应根据具体需求选择合适的数据结构,充分利用它们的优势,避免潜在的性能问题和错误.

通过合理使用"collections"模块,我们可以编写更简洁,更高效,更易维护的Python代码,从而提高开发效率和软件质量.
```
"""
'''
"
'
