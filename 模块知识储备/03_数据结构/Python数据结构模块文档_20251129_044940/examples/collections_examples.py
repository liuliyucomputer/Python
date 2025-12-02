#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
collections模块示例代码集合

本文件演示了Python collections模块中的各种容器数据类型，
包括Counter、defaultdict、OrderedDict、deque、namedtuple等。

作者: Python数据结构教程
日期: 2023-11-28
"""

import collections
import random
import time
from pprint import pprint


def example_counter():
    """示例1: Counter - 计数器"""
    print("=== 示例1: Counter - 计数器 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 从列表创建计数器
    fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
    fruit_counter = collections.Counter(fruits)
    print(f"水果列表: {fruits}")
    print(f"计数结果: {fruit_counter}")
    
    # 从字符串创建计数器
    text = "hello world"
    char_counter = collections.Counter(text)
    print(f"\n文本: '{text}'")
    print(f"字符计数: {char_counter}")
    
    # 获取最常见的元素
    print(f"\n最常见的2个水果: {fruit_counter.most_common(2)}")
    print(f"最常见的3个字符: {char_counter.most_common(3)}")
    
    # 访问元素计数
    print(f"\n'apple'出现次数: {fruit_counter['apple']}")
    print(f"'grape'出现次数: {fruit_counter['grape']} (不存在的键返回0)")
    
    # 更新计数
    print("\n更新计数:")
    fruit_counter.update(['apple', 'grape'])
    print(f"更新后: {fruit_counter}")
    
    # 计数器运算
    print("\n计数器运算:")
    counter1 = collections.Counter(a=3, b=2, c=1)
    counter2 = collections.Counter(a=1, b=2, c=3)
    
    print(f"counter1: {counter1}")
    print(f"counter2: {counter2}")
    print(f"加法: {counter1 + counter2}")
    print(f"减法: {counter1 - counter2}")  # 只保留正数计数
    print(f"交集: {counter1 & counter2}")  # 取最小值
    print(f"并集: {counter1 | counter2}")  # 取最大值
    
    # 实际应用：文本分析
    print("\n实际应用：文本分析")
    
    sample_text = """Python is a widely used high-level programming language for general-purpose programming,
created by Guido van Rossum and first released in 1991. An interpreted language,
Python has a design philosophy that emphasizes code readability, and a syntax that
allows programmers to express concepts in fewer lines of code than might be
possible in languages such as C++ or Java."""
    
    # 简单分词并过滤标点符号
    words = sample_text.lower().replace('.', '').replace(',', '').split()
    word_counter = collections.Counter(words)
    
    print(f"文本长度: {len(words)}个单词")
    print(f"不同单词数量: {len(word_counter)}个")
    print(f"最常见的10个单词:")
    for word, count in word_counter.most_common(10):
        print(f"  '{word}': {count}")
    print()


def example_defaultdict():
    """示例2: defaultdict - 默认值字典"""
    print("=== 示例2: defaultdict - 默认值字典 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 创建一个默认值为list的字典
    d_list = collections.defaultdict(list)
    
    # 直接添加元素而无需检查键是否存在
    d_list['fruits'].append('apple')
    d_list['fruits'].append('banana')
    d_list['vegetables'].append('carrot')
    
    print(f"defaultdict(list)示例: {dict(d_list)}")
    
    # 创建一个默认值为int的字典
    d_int = collections.defaultdict(int)
    for char in 'hello':
        d_int[char] += 1
    
    print(f"\ndefaultdict(int)示例: {dict(d_int)}")
    
    # 创建一个默认值为set的字典
    d_set = collections.defaultdict(set)
    d_set['words'].add('hello')
    d_set['words'].add('world')
    d_set['words'].add('hello')  # 重复元素会被自动去重
    
    print(f"\ndefaultdict(set)示例: {dict(d_set)}")
    
    # 使用自定义默认值
    print("\n使用自定义默认值:")
    
    def default_factory():
        return "Not Found"
    
    d_custom = collections.defaultdict(default_factory)
    print(f"d_custom['existing'] = {d_custom['existing']}")  # 触发默认值
    d_custom['user_defined'] = "Value Set"
    print(f"d_custom['user_defined'] = {d_custom['user_defined']}")
    
    # 与普通字典比较
    print("\n与普通字典比较:")
    
    # 使用普通字典的方式
    normal_dict = {}
    try:
        normal_dict['key'].append('value')
    except KeyError as e:
        print(f"普通字典错误: {e}")
    
    # 需要手动初始化
    if 'key' not in normal_dict:
        normal_dict['key'] = []
    normal_dict['key'].append('value')
    print(f"手动初始化后: {normal_dict}")
    
    # 实际应用：分组数据
    print("\n实际应用：分组数据")
    
    # 模拟学生数据
    students = [
        {"name": "Alice", "age": 22, "major": "Computer Science"},
        {"name": "Bob", "age": 21, "major": "Mathematics"},
        {"name": "Charlie", "age": 23, "major": "Computer Science"},
        {"name": "David", "age": 22, "major": "Physics"},
        {"name": "Eve", "age": 20, "major": "Mathematics"}
    ]
    
    # 按专业分组
    by_major = collections.defaultdict(list)
    for student in students:
        by_major[student["major"]].append(student)
    
    print("按专业分组的学生:")
    for major, students_in_major in by_major.items():
        print(f"\n{major}: {len(students_in_major)}名学生")
        for student in students_in_major:
            print(f"  {student['name']}, {student['age']}岁")
    print()


def example_ordered_dict():
    """示例3: OrderedDict - 有序字典"""
    print("=== 示例3: OrderedDict - 有序字典 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 创建有序字典
    od = collections.OrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    od['d'] = 4
    
    print(f"有序字典: {dict(od)}")
    print("遍历顺序:")
    for key, value in od.items():
        print(f"  {key}: {value}")
    
    # 注意：在Python 3.7+中，普通字典也保持插入顺序
    # 但OrderedDict有一些特殊的方法
    
    # 重新插入已存在的键会将其移动到末尾
    print("\n重新插入已存在的键:")
    od['a'] = 100  # 这会将'a'移动到末尾
    print(f"重新插入'a'后: {dict(od)}")
    
    # move_to_end方法
    print("\n使用move_to_end方法:")
    od.move_to_end('b')  # 默认移动到末尾
    print(f"'b'移动到末尾后: {dict(od)}")
    
    od.move_to_end('c', last=False)  # 移动到开头
    print(f"'c'移动到开头后: {dict(od)}")
    
    # popitem方法
    print("\n使用popitem方法:")
    last_item = od.popitem()  # 默认移除并返回最后一项
    print(f"移除的最后一项: {last_item}")
    print(f"移除后: {dict(od)}")
    
    first_item = od.popitem(last=False)  # 移除并返回第一项
    print(f"移除的第一项: {first_item}")
    print(f"移除后: {dict(od)}")
    
    # 实际应用：LRU缓存实现
    print("\n实际应用：LRU缓存实现")
    
    class LRUCache:
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = collections.OrderedDict()
        
        def get(self, key):
            if key not in self.cache:
                return -1
            # 访问时将键移到末尾（最近使用）
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key, value):
            # 如果键已存在，先更新并移到末尾
            if key in self.cache:
                self.cache.move_to_end(key)
            # 如果超出容量，删除最久未使用的项（第一项）
            elif len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            # 添加新项到末尾
            self.cache[key] = value
        
        def __repr__(self):
            return str(dict(self.cache))
    
    # 测试LRU缓存
    lru = LRUCache(3)
    lru.put('a', 1)
    lru.put('b', 2)
    lru.put('c', 3)
    print(f"初始化缓存: {lru}")
    
    print(f"访问'a': {lru.get('a')}")  # 'a'移到末尾
    print(f"缓存状态: {lru}")
    
    lru.put('d', 4)  # 应该淘汰'b'
    print(f"添加'd'后: {lru}")
    
    print(f"访问'b': {lru.get('b')}")  # 应该返回-1，因为'b'已被淘汰
    print(f"访问'c': {lru.get('c')}")  # 'c'移到末尾
    print(f"缓存状态: {lru}")
    print()


def example_deque():
    """示例4: deque - 双端队列"""
    print("=== 示例4: deque - 双端队列 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 创建双端队列
    dq = collections.deque([1, 2, 3])
    print(f"初始队列: {dq}")
    
    # 添加元素
    dq.append(4)        # 右侧添加
    print(f"右侧添加4后: {dq}")
    
    dq.appendleft(0)    # 左侧添加
    print(f"左侧添加0后: {dq}")
    
    # 删除元素
    right_element = dq.pop()      # 右侧删除
    print(f"右侧删除元素: {right_element}")
    print(f"删除后: {dq}")
    
    left_element = dq.popleft()   # 左侧删除
    print(f"左侧删除元素: {left_element}")
    print(f"删除后: {dq}")
    
    # 扩展队列
    dq.extend([4, 5, 6])      # 右侧扩展
    print(f"右侧扩展[4,5,6]后: {dq}")
    
    dq.extendleft([-2, -1, 0])  # 左侧扩展（注意顺序会反转）
    print(f"左侧扩展[-2,-1,0]后: {dq}")
    
    # 旋转队列
    print("\n旋转队列:")
    dq = collections.deque([1, 2, 3, 4, 5])
    print(f"原始队列: {dq}")
    
    dq.rotate(1)    # 向右旋转1位
    print(f"向右旋转1位: {dq}")
    
    dq.rotate(-2)   # 向左旋转2位
    print(f"向左旋转2位: {dq}")
    
    # 设置最大长度
    print("\n设置最大长度:")
    dq = collections.deque(maxlen=3)
    dq.append(1)
    dq.append(2)
    dq.append(3)
    print(f"填充后: {dq}")
    
    dq.append(4)  # 自动删除最旧的元素
    print(f"添加第4个元素后: {dq}")
    
    # 性能比较
    print("\n性能比较:")
    
    # 使用列表模拟队列
    def list_queue_performance():
        lst = []
        start = time.time()
        for _ in range(10000):
            lst.append(_)  # 右侧添加
        for _ in range(10000):
            lst.pop(0)     # 左侧删除（效率低）
        return time.time() - start
    
    # 使用deque
    def deque_performance():
        dq = collections.deque()
        start = time.time()
        for _ in range(10000):
            dq.append(_)   # 右侧添加
        for _ in range(10000):
            dq.popleft()   # 左侧删除（效率高）
        return time.time() - start
    
    list_time = list_queue_performance()
    deque_time = deque_performance()
    
    print(f"列表模拟队列耗时: {list_time:.6f}秒")
    print(f"deque耗时: {deque_time:.6f}秒")
    print(f"deque比列表快约{list_time / deque_time:.2f}倍")
    
    # 实际应用：滑动窗口
    print("\n实际应用：滑动窗口")
    
    def sliding_window_max(arr, window_size):
        """计算数组的滑动窗口最大值"""
        result = []
        dq = collections.deque()  # 存储索引
        
        for i in range(len(arr)):
            # 移除超出窗口范围的元素
            while dq and dq[0] <= i - window_size:
                dq.popleft()
            
            # 移除小于当前元素的元素（它们永远不可能是最大值）
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()
            
            # 添加当前元素的索引
            dq.append(i)
            
            # 当窗口完全形成后，记录最大值
            if i >= window_size - 1:
                result.append(arr[dq[0]])
        
        return result
    
    # 测试
    test_array = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size = 3
    max_values = sliding_window_max(test_array, window_size)
    
    print(f"原始数组: {test_array}")
    print(f"窗口大小: {window_size}")
    print(f"滑动窗口最大值: {max_values}")
    print()


def example_namedtuple():
    """示例5: namedtuple - 命名元组"""
    print("=== 示例5: namedtuple - 命名元组 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 定义命名元组
    Point = collections.namedtuple('Point', ['x', 'y', 'z'])
    
    # 创建实例
    p1 = Point(1, 2, 3)
    p2 = Point(x=4, y=5, z=6)
    
    print(f"p1: {p1}")
    print(f"p2: {p2}")
    
    # 通过名称访问字段
    print(f"\np1.x = {p1.x}, p1.y = {p1.y}, p1.z = {p1.z}")
    print(f"p2.x = {p2.x}, p2.y = {p2.y}, p2.z = {p2.z}")
    
    # 也可以通过索引访问
    print(f"\np1[0] = {p1[0]}, p1[1] = {p1[1]}, p1[2] = {p1[2]}")
    
    # 支持解包
    x, y, z = p1
    print(f"\n解包: x = {x}, y = {y}, z = {z}")
    
    # 支持比较（基于字段顺序）
    print(f"\np1 == p2: {p1 == p2}")
    print(f"p1 < p2: {p1 < p2}")
    
    # _fields属性获取字段名
    print(f"\n字段名: {Point._fields}")
    
    # _replace方法创建新实例
    print("\n使用_replace方法:")
    p3 = p1._replace(x=10)
    print(f"p1: {p1}")
    print(f"p3 (p1替换x=10后): {p3}")
    
    # _asdict方法转换为字典
    print(f"\n转换为字典: {p1._asdict()}")
    
    # 实际应用：数据记录
    print("\n实际应用：数据记录")
    
    # 定义员工记录
    Employee = collections.namedtuple('Employee', ['id', 'name', 'department', 'salary'])
    
    # 创建员工列表
    employees = [
        Employee(101, 'Alice', 'Engineering', 80000),
        Employee(102, 'Bob', 'Marketing', 75000),
        Employee(103, 'Charlie', 'Engineering', 90000),
        Employee(104, 'David', 'Sales', 85000)
    ]
    
    # 按部门分组
    engineering_employees = [emp for emp in employees if emp.department == 'Engineering']
    
    print("工程部门员工:")
    for emp in engineering_employees:
        print(f"  ID: {emp.id}, 姓名: {emp.name}, 薪资: ${emp.salary}")
    
    # 计算平均薪资
    avg_salary = sum(emp.salary for emp in employees) / len(employees)
    print(f"\n平均薪资: ${avg_salary:.2f}")
    
    # 将员工数据转换为字典列表（用于JSON序列化等）
    employees_dict = [emp._asdict() for emp in employees]
    print("\n员工数据字典形式:")
    for emp_dict in employees_dict:
        print(f"  {emp_dict}")
    print()


def example_chainmap():
    """示例6: ChainMap - 链式映射"""
    print("=== 示例6: ChainMap - 链式映射 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 创建多个字典
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict3 = {'c': 5, 'd': 6}
    
    # 创建ChainMap
    chain = collections.ChainMap(dict1, dict2, dict3)
    
    print(f"dict1: {dict1}")
    print(f"dict2: {dict2}")
    print(f"dict3: {dict3}")
    print(f"ChainMap: {dict(chain)}")
    
    # 访问元素（按顺序查找）
    print(f"\n查找'a': {chain['a']} (来自dict1)")
    print(f"查找'b': {chain['b']} (来自dict1，而不是dict2)")
    print(f"查找'c': {chain['c']} (来自dict2，而不是dict3)")
    print(f"查找'd': {chain['d']} (来自dict3)")
    
    # 键不存在时抛出KeyError
    try:
        value = chain['e']
    except KeyError as e:
        print(f"\n查找'e': 错误 - {e}")
    
    # 使用get方法避免错误
    print(f"使用get查找'e': {chain.get('e', 'Not found')}")
    
    # 修改原始字典会影响ChainMap
    print("\n修改原始字典:")
    dict1['a'] = 100
    print(f"修改dict1['a'] = 100后，chain['a'] = {chain['a']}")
    
    # 直接修改ChainMap会修改第一个字典
    print("\n直接修改ChainMap:")
    chain['b'] = 200
    print(f"修改chain['b'] = 200后")
    print(f"dict1['b'] = {dict1['b']}")
    print(f"dict2['b'] = {dict2['b']}")
    
    # 添加新键值对会添加到第一个字典
    print("\n添加新键值对:")
    chain['e'] = 500
    print(f"添加chain['e'] = 500后")
    print(f"dict1: {dict1}")
    
    # new_child方法创建新的ChainMap
    print("\n使用new_child方法:")
    new_chain = chain.new_child({'c': 300, 'f': 600})
    print(f"new_chain: {dict(new_chain)}")
    print(f"new_chain['c'] = {new_chain['c']} (来自新的子字典)")
    
    # parents属性获取除第一个字典外的ChainMap
    print("\n使用parents属性:")
    parents = chain.parents
    print(f"parents: {dict(parents)}")
    
    # 实际应用：配置管理
    print("\n实际应用：配置管理")
    
    # 优先级从高到低：命令行参数 > 环境变量 > 配置文件 > 默认配置
    default_config = {
        'host': 'localhost',
        'port': 8000,
        'debug': False,
        'timeout': 30
    }
    
    file_config = {
        'host': 'example.com',
        'port': 8080,
        'timeout': 60
    }
    
    env_config = {
        'host': 'production.example.com',
        'debug': False
    }
    
    # 模拟命令行参数
    cmd_config = {
        'port': 9000,
        'debug': True
    }
    
    # 创建配置ChainMap
    config = collections.ChainMap(cmd_config, env_config, file_config, default_config)
    
    print("最终配置:")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    # 查找值的来源
    def find_config_source(config_chain, key):
        """查找配置项的来源"""
        for i, mapping in enumerate(config_chain.maps):
            if key in mapping:
                sources = ['命令行参数', '环境变量', '配置文件', '默认配置']
                source_name = sources[i] if i < len(sources) else f'映射{i}'
                return source_name, mapping[key]
        return None, None
    
    print("\n配置来源:")
    for key in config:
        source, value = find_config_source(config, key)
        print(f"  {key}: {value} (来自{source})")
    print()


def example_user_dict():
    """示例7: UserDict - 用户字典基类"""
    print("=== 示例7: UserDict - 用户字典基类 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 创建自定义字典类
    class CustomDict(collections.UserDict):
        def __setitem__(self, key, value):
            # 自定义设置项的行为
            if isinstance(key, str):
                key = key.lower()  # 键转换为小写
            self.data[key] = value
        
        def __getitem__(self, key):
            # 自定义获取项的行为
            if isinstance(key, str):
                key = key.lower()  # 键转换为小写
            return self.data[key]
        
        def __contains__(self, key):
            # 自定义包含检查的行为
            if isinstance(key, str):
                key = key.lower()  # 键转换为小写
            return key in self.data
    
    # 创建实例
    custom_dict = CustomDict()
    custom_dict['Name'] = 'Alice'  # 自动转换为小写
    custom_dict['AGE'] = 25        # 自动转换为小写
    custom_dict['city'] = 'New York'
    
    print(f"自定义字典: {dict(custom_dict)}")
    print(f"'name' in custom_dict: {'name' in custom_dict}")
    print(f"'Name' in custom_dict: {'Name' in custom_dict}")  # 忽略大小写
    print(f"custom_dict['NAME']: {custom_dict['NAME']}")      # 忽略大小写
    
    # 与字典方法的兼容性
    print("\n遍历:")
    for key, value in custom_dict.items():
        print(f"  {key}: {value}")
    
    # 扩展UserDict实现更复杂的字典
    print("\n实现缓存字典:")
    
    class CacheDict(collections.UserDict):
        def __init__(self, max_size=100, default_ttl=300):
            super().__init__()
            self.max_size = max_size
            self.default_ttl = default_ttl
            self.expiration_times = {}
        
        def __setitem__(self, key, value, ttl=None):
            # 如果超出大小，删除最早添加的项
            if len(self.data) >= self.max_size and key not in self.data:
                oldest_key = next(iter(self.data))
                del self.data[oldest_key]
                del self.expiration_times[oldest_key]
            
            # 存储值和过期时间
            self.data[key] = value
            self.expiration_times[key] = time.time() + (ttl or self.default_ttl)
        
        def __getitem__(self, key):
            # 检查是否过期
            if key in self.data:
                if time.time() > self.expiration_times[key]:
                    del self.data[key]
                    del self.expiration_times[key]
                    raise KeyError(key)
                return self.data[key]
            raise KeyError(key)
        
        def get(self, key, default=None):
            try:
                return self[key]
            except KeyError:
                return default
        
        def clear_expired(self):
            """清理过期的项目"""
            current_time = time.time()
            expired_keys = [key for key, exp_time in self.expiration_times.items() 
                           if current_time > exp_time]
            
            for key in expired_keys:
                del self.data[key]
                del self.expiration_times[key]
            
            return len(expired_keys)
    
    # 测试缓存字典
    cache = CacheDict(max_size=3, default_ttl=0.5)  # 500毫秒过期
    
    print("添加缓存项:")
    cache['key1'] = 'value1'
    cache['key2'] = 'value2'
    cache['key3'] = 'value3'
    print(f"缓存内容: {dict(cache)}")
    
    print("\n添加第4个项（应该淘汰最早的项）:")
    cache['key4'] = 'value4'
    print(f"缓存内容: {dict(cache)}")
    
    print("\n等待过期...")
    time.sleep(0.6)
    
    print("检查过期项:")
    try:
        print(f"key2: {cache['key2']}")
    except KeyError:
        print("key2已过期")
    
    print(f"使用get方法获取key3: {cache.get('key3', '已过期')}")
    print(f"使用get方法获取key4: {cache.get('key4', '已过期')}")
    
    print("\n手动清理过期项:")
    expired_count = cache.clear_expired()
    print(f"清理了{expired_count}个过期项")
    print(f"缓存内容: {dict(cache)}")
    print()


def example_user_list():
    """示例8: UserList - 用户列表基类"""
    print("=== 示例8: UserList - 用户列表基类 ===")
    
    # 基本用法
    print("基本用法:")
    
    # 创建自定义列表类
    class SortedList(collections.UserList):
        def __init__(self, data=None, key=None):
            super().__init__()
            self.key = key or (lambda x: x)  # 默认排序键
            if data:
                self.extend(data)
        
        def append(self, item):
            # 添加元素并保持排序
            super().append(item)
            self.sort(key=self.key)
        
        def extend(self, iterable):
            # 扩展列表并保持排序
            super().extend(iterable)
            self.sort(key=self.key)
        
        def __setitem__(self, index, item):
            # 设置元素并保持排序
            super().__setitem__(index, item)
            self.sort(key=self.key)
    
    # 创建实例
    sorted_nums = SortedList([3, 1, 4, 1, 5, 9, 2])
    print(f"排序数字列表: {sorted_nums}")
    
    # 添加元素
    sorted_nums.append(6)
    print(f"添加6后: {sorted_nums}")
    
    # 扩展列表
    sorted_nums.extend([8, 7])
    print(f"扩展[8,7]后: {sorted_nums}")
    
    # 使用自定义排序键
    print("\n使用自定义排序键:")
    
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        
        def __repr__(self):
            return f"Person({self.name}, {self.age})"
    
    # 按年龄排序的Person列表
    people = SortedList([
        Person('Bob', 30),
        Person('Alice', 25),
        Person('Charlie', 35)
    ], key=lambda p: p.age)
    
    print(f"按年龄排序的人员列表: {people}")
    
    # 添加新人员
    people.append(Person('David', 28))
    print(f"添加David后: {people}")
    
    # 实际应用：有序集合
    print("\n实际应用：有序集合")
    
    class OrderedSet(collections.UserList):
        def __init__(self, data=None):
            super().__init__()
            self._seen = set()
            if data:
                self.extend(data)
        
        def append(self, item):
            # 只添加不存在的元素
            if item not in self._seen:
                self._seen.add(item)
                super().append(item)
        
        def extend(self, iterable):
            # 只添加不存在的元素
            for item in iterable:
                self.append(item)
        
        def remove(self, item):
            # 移除元素时同时更新集合
            if item in self._seen:
                self._seen.remove(item)
                super().remove(item)
        
        def clear(self):
            # 清空列表和集合
            self._seen.clear()
            super().clear()
        
        def __contains__(self, item):
            # 使用集合进行快速查找
            return item in self._seen
    
    # 测试有序集合
    ordered_set = OrderedSet([1, 2, 3, 2, 1, 4])
    print(f"有序集合（去重）: {ordered_set}")
    
    ordered_set.append(3)  # 重复元素不会添加
    print(f"添加重复元素3后: {ordered_set}")
    
    ordered_set.append(5)  # 添加新元素
    print(f"添加新元素5后: {ordered_set}")
    
    # 测试包含关系（应该很快，因为使用了集合）
    print(f"包含3: {3 in ordered_set}")
    print(f"包含6: {6 in ordered_set}")
    
    # 测试移除
    ordered_set.remove(2)
    print(f"移除2后: {ordered_set}")
    
    # 测试扩展
    ordered_set.extend([5, 6, 7, 3])  # 只有6和7会被添加
    print(f"扩展[5,6,7,3]后: {ordered_set}")
    print()


def example_counter_advanced():
    """示例9: Counter高级用法"""
    print("=== 示例9: Counter高级用法 ===")
    
    # 嵌套Counter
    print("嵌套Counter:")
    
    # 模拟文档词频统计
    documents = {
        "doc1": ["python", "programming", "language", "python"],
        "doc2": ["programming", "java", "python", "c++"],
        "doc3": ["python", "data", "science", "programming"]
    }
    
    # 为每个文档创建Counter
    doc_counters = {doc_id: collections.Counter(words) 
                   for doc_id, words in documents.items()}
    
    print("各文档词频:")
    for doc_id, counter in doc_counters.items():
        print(f"  {doc_id}: {dict(counter)}")
    
    # 计算总词频
    total_counter = collections.Counter()
    for counter in doc_counters.values():
        total_counter.update(counter)
    
    print(f"\n总词频: {dict(total_counter)}")
    
    # 计算文档频率（出现词语的文档数）
    doc_frequency = collections.Counter()
    for words in documents.values():
        for word in set(words):  # 使用set去重
            doc_frequency[word] += 1
    
    print(f"\n文档频率: {dict(doc_frequency)}")
    
    # 计算TF-IDF（简化版）
    import math
    total_docs = len(documents)
    
    tf_idf = {}
    for doc_id, counter in doc_counters.items():
        doc_tf_idf = {}
        doc_length = sum(counter.values())
        
        for word, count in counter.items():
            tf = count / doc_length  # 词频
            idf = math.log(total_docs / doc_frequency[word])  # 逆文档频率
            doc_tf_idf[word] = tf * idf
        
        tf_idf[doc_id] = doc_tf_idf
    
    print("\nTF-IDF值:")
    for doc_id, scores in tf_idf.items():
        print(f"  {doc_id}:")
        for word, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
            print(f"    {word}: {score:.4f}")
    
    # 实际应用：文本相似度
    print("\n实际应用：文本相似度")
    
    def cosine_similarity(counter1, counter2):
        """计算两个Counter的余弦相似度"""
        # 获取所有唯一单词
        all_words = set(counter1.keys()).union(set(counter2.keys()))
        
        # 计算点积
        dot_product = sum(counter1.get(word, 0) * counter2.get(word, 0) for word in all_words)
        
        # 计算向量长度
        len1 = math.sqrt(sum(count ** 2 for count in counter1.values()))
        len2 = math.sqrt(sum(count ** 2 for count in counter2.values()))
        
        # 避免除零错误
        if len1 == 0 or len2 == 0:
            return 0
        
        return dot_product / (len1 * len2)
    
    # 计算文档间相似度
    print("文档间余弦相似度:")
    doc_ids = list(doc_counters.keys())
    for i in range(len(doc_ids)):
        for j in range(i+1, len(doc_ids)):
            sim = cosine_similarity(doc_counters[doc_ids[i]], doc_counters[doc_ids[j]])
            print(f"  {doc_ids[i]} vs {doc_ids[j]}: {sim:.4f}")
    print()


def example_real_world_scenarios():
    """示例10: 实际应用场景"""
    print("=== 示例10: 实际应用场景 ===")
    
    # 1. 日志分析
    print("1. 日志分析:")
    
    # 模拟日志数据
    logs = [
        "2023-11-28 10:00:00 ERROR Database connection failed",
        "2023-11-28 10:01:30 INFO Application started",
        "2023-11-28 10:02:15 WARNING Low disk space",
        "2023-11-28 10:03:45 ERROR Out of memory",
        "2023-11-28 10:05:00 INFO User login successful",
        "2023-11-28 10:06:20 ERROR Database connection failed",
        "2023-11-28 10:07:30 WARNING Low disk space"
    ]
    
    # 解析日志级别
    log_levels = collections.Counter()
    error_messages = collections.Counter()
    
    for log in logs:
        parts = log.split()
        if len(parts) >= 3:
            level = parts[2]
            log_levels[level] += 1
            
            # 收集错误信息
            if level == "ERROR":
                message = " ".join(parts[3:])
                error_messages[message] += 1
    
    print("日志级别统计:")
    for level, count in log_levels.items():
        print(f"  {level}: {count}")
    
    print("\n错误信息统计:")
    for message, count in error_messages.items():
        print(f"  '{message}': {count}")
    
    # 2. 网络爬虫URL队列管理
    print("\n2. 网络爬虫URL队列管理:")
    
    # 模拟URL队列和已访问URL集合
    url_queue = collections.deque()
    visited_urls = set()
    
    # 模拟抓取过程
    def simulate_crawling(start_url, max_depth=2):
        url_queue.append((start_url, 0))  # (URL, 深度)
        crawled_urls = 0
        
        while url_queue:
            current_url, depth = url_queue.popleft()
            
            if current_url in visited_urls or depth > max_depth:
                continue
            
            visited_urls.add(current_url)
            crawled_urls += 1
            
            print(f"抓取: {current_url} (深度: {depth})")
            
            # 模拟发现新链接（实际爬虫中这里会解析页面）
            if depth < max_depth:
                num_links = random.randint(1, 3)
                for i in range(num_links):
                    new_url = f"{current_url}/page{i+1}"
                    url_queue.append((new_url, depth + 1))
        
        return crawled_urls
    
    total_crawled = simulate_crawling("http://example.com", max_depth=2)
    print(f"总共抓取了{total_crawled}个URL")
    
    # 3. 电商购物车实现
    print("\n3. 电商购物车实现:")
    
    class ShoppingCart:
        def __init__(self):
            self.items = collections.defaultdict(lambda: {
                'quantity': 0,
                'price': 0,
                'name': ''
            })
        
        def add_item(self, product_id, name, price, quantity=1):
            """添加商品到购物车"""
            self.items[product_id]['quantity'] += quantity
            self.items[product_id]['price'] = price  # 更新为最新价格
            self.items[product_id]['name'] = name
        
        def remove_item(self, product_id, quantity=None):
            """从购物车移除商品"""
            if product_id not in self.items:
                return False
            
            if quantity is None or quantity >= self.items[product_id]['quantity']:
                del self.items[product_id]
            else:
                self.items[product_id]['quantity'] -= quantity
            
            return True
        
        def get_total(self):
            """计算购物车总金额"""
            return sum(item['price'] * item['quantity'] for item in self.items.values())
        
        def get_item_count(self):
            """获取购物车商品总数"""
            return sum(item['quantity'] for item in self.items.values())
        
        def __str__(self):
            """打印购物车内容"""
            if not self.items:
                return "购物车是空的"
            
            lines = ["购物车内容:", "=" * 50]
            lines.append(f"{'商品名称':<20} {'单价':>10} {'数量':>10} {'小计':>10}")
            lines.append("-" * 50)
            
            for pid, item in self.items.items():
                subtotal = item['price'] * item['quantity']
                lines.append(f"{item['name']:<20} {item['price']:>10.2f} {item['quantity']:>10} {subtotal:>10.2f}")
            
            lines.append("=" * 50)
            lines.append(f"{'总计':<20} {'':>10} {self.get_item_count():>10} {self.get_total():>10.2f}")
            
            return "\n".join(lines)
    
    # 测试购物车
    cart = ShoppingCart()
    
    # 添加商品
    cart.add_item(1, "Python编程书籍", 59.99)
    cart.add_item(2, "编程鼠标", 129.50)
    cart.add_item(1, "Python编程书籍", 59.99, 2)  # 再添加2本同样的书
    cart.add_item(3, "机械键盘", 299.00)
    
    print(cart)
    
    # 移除部分商品
    print("\n移除1本Python书籍:")
    cart.remove_item(1, 1)
    print(cart)
    
    # 移除全部商品
    print("\n移除机械键盘:")
    cart.remove_item(3)
    print(cart)
    print()


if __name__ == "__main__":
    print("Python collections 模块示例代码\n")
    
    # 运行所有示例
    example_counter()
    example_defaultdict()
    example_ordered_dict()
    example_deque()
    example_namedtuple()
    example_chainmap()
    example_user_dict()
    example_user_list()
    example_counter_advanced()
    example_real_world_scenarios()
    
    print("所有示例执行完成！")
