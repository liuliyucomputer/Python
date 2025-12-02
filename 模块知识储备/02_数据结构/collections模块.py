# Python collections模块详解

# 1. collections模块概述
print("=== 1. collections模块概述 ===")
print("collections模块提供了高性能的容器数据类型，扩展了Python内置的集合类型。")
print("该模块主要包含以下几种核心数据结构：")
print("- namedtuple: 创建命名元组子类的工厂函数")
print("- deque: 双端队列，支持两端快速添加和删除元素")
print("- ChainMap: 字典的集合类，将多个映射快速链接成一个")
print("- Counter: 计数器，用于统计可哈希对象的出现次数")
print("- OrderedDict: 有序字典，保持插入顺序（Python 3.7+中dict已默认有序）")
print("- defaultdict: 带有默认值的字典")
print("- UserDict: 封装了字典对象的类，便于自定义字典子类")
print("- UserList: 封装了列表对象的类，便于自定义列表子类")
print("- UserString: 封装了字符串对象的类，便于自定义字符串子类")
print("collections模块适用于需要高效数据处理、特殊数据结构或简化代码的场景。")
print()

# 2. 核心数据结构详解
print("=== 2. 核心数据结构详解 ===")

def collections_core_data_structures():
    """详细介绍collections模块的核心数据结构"""
    import collections
    import time
    
    print("1. namedtuple - 命名元组")
    print("   创建具有字段名的元组子类，提高代码可读性")
    
    # 创建命名元组
    print("   创建和使用命名元组:")
    
    # 基本创建方式
    Point = collections.namedtuple('Point', ['x', 'y'])
    p1 = Point(10, 20)
    
    print(f"   基本访问: p1.x = {p1.x}, p1.y = {p1.y}")
    print(f"   索引访问: p1[0] = {p1[0]}, p1[1] = {p1[1]}")
    print(f"   解包: x, y = p1 → x={p1[0]}, y={p1[1]}")
    print(f"   转换为字典: {p1._asdict()}")
    print(f"   替换字段: {p1._replace(x=15)}")
    
    # 高级特性
    print("   \n命名元组的高级特性:")
    
    # 使用字符串分割创建字段名
    Color = collections.namedtuple('Color', 'red green blue')
    c1 = Color(255, 0, 0)
    print(f"   使用空格分割字段名: Color(255, 0, 0) → {c1}")
    
    # 默认值
    Person = collections.namedtuple('Person', 'name age city', defaults=['Unknown'])
    p2 = Person('Alice', 30)
    print(f"   默认值支持: Person('Alice', 30) → {p2}")
    
    # 字段名列表
    print(f"   字段名列表: {Person._fields}")
    
    # 从字典创建
    d = {'name': 'Bob', 'age': 25, 'city': 'New York'}
    p3 = Person(**d)
    print(f"   从字典创建: Person(**{d}) → {p3}")
    
    print("\n2. deque - 双端队列")
    print("   支持两端快速添加和删除操作的队列数据结构")
    
    # 创建和基本操作
    print("   创建和基本操作:")
    
    # 创建空deque
    dq1 = collections.deque()
    print(f"   创建空deque: {dq1}")
    
    # 从迭代器创建
    dq2 = collections.deque([1, 2, 3, 4, 5])
    print(f"   从列表创建: {dq2}")
    
    # 左侧添加
    dq2.appendleft(0)
    print(f"   左侧添加0: {dq2}")
    
    # 右侧添加
    dq2.append(6)
    print(f"   右侧添加6: {dq2}")
    
    # 左侧删除
    left_val = dq2.popleft()
    print(f"   左侧删除: {left_val}, 结果: {dq2}")
    
    # 右侧删除
    right_val = dq2.pop()
    print(f"   右侧删除: {right_val}, 结果: {dq2}")
    
    # 高级操作
    print("   \ndeque的高级操作:")
    
    # 限制最大长度
    limited_dq = collections.deque(maxlen=3)
    for i in range(5):
        limited_dq.append(i)
        print(f"   添加{i}后: {limited_dq}")
    
    # 扩展操作
    dq3 = collections.deque([1, 2, 3])
    dq3.extend([4, 5, 6])
    print(f"   右侧扩展[4,5,6]: {dq3}")
    
    dq3.extendleft([0, -1, -2])
    print(f"   左侧扩展[0,-1,-2]: {dq3}")
    
    # 旋转操作
    dq4 = collections.deque([1, 2, 3, 4, 5])
    dq4.rotate(2)  # 向右旋转2步
    print(f"   向右旋转2步: {dq4}")
    
    dq4.rotate(-1)  # 向左旋转1步
    print(f"   向左旋转1步: {dq4}")
    
    print("\n3. Counter - 计数器")
    print("   用于统计可哈希对象出现次数的字典子类")
    
    # 基本使用
    print("   基本计数功能:")
    
    # 从字符串创建
    counter1 = collections.Counter('abracadabra')
    print(f"   统计字符串'abracadabra': {counter1}")
    
    # 从列表创建
    counter2 = collections.Counter([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    print(f"   统计列表频率: {counter2}")
    
    # 从字典创建
    counter3 = collections.Counter({'a': 3, 'b': 2, 'c': 1})
    print(f"   从字典创建: {counter3}")
    
    # 手动更新计数
    counter3['a'] += 1
    print(f"   更新'a'的计数后: {counter3}")
    
    # 高级方法
    print("   \nCounter的高级方法:")
    
    # most_common: 获取最常见的元素
    top2 = counter1.most_common(2)
    print(f"   最常见的2个元素: {top2}")
    
    # elements: 获取迭代器，按计数生成元素
    elements = list(counter2.elements())
    print(f"   按计数生成元素: {elements}")
    
    # subtract: 减少计数
    counter4 = collections.Counter(a=4, b=2, c=0, d=-2)
    counter5 = collections.Counter(a=1, b=1, d=2, c=3)
    counter4.subtract(counter5)
    print(f"   counter4减去counter5: {counter4}")
    
    # update: 更新计数
    counter6 = collections.Counter(a=1, b=2)
    counter6.update({'a': 3, 'b': 1, 'c': 5})
    print(f"   更新计数: {counter6}")
    
    print("\n4. defaultdict - 默认值字典")
    print("   自动为不存在的键提供默认值的字典子类")
    
    # 基本使用
    print("   基本默认值功能:")
    
    # 使用列表作为默认值
    dd_list = collections.defaultdict(list)
    dd_list['key1'].append('value1')
    dd_list['key1'].append('value2')
    dd_list['key2'].append('value3')
    print(f"   列表默认值: {dict(dd_list)}")
    
    # 使用集合作为默认值
    dd_set = collections.defaultdict(set)
    dd_set['key1'].add('value1')
    dd_set['key1'].add('value2')
    dd_set['key2'].add('value3')
    print(f"   集合默认值: {dict(dd_set)}")
    
    # 使用整数作为默认值（用于计数）
    dd_int = collections.defaultdict(int)
    for word in ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']:
        dd_int[word] += 1
    print(f"   整数默认值(计数): {dict(dd_int)}")
    
    # 使用自定义默认工厂函数
    print("   \n自定义默认工厂函数:")
    
    def default_factory():
        return {"status": "new", "created_at": time.time()}
    
    dd_custom = collections.defaultdict(default_factory)
    print(f"   自定义默认值1: {dd_custom['item1']}")
    print(f"   自定义默认值2: {dd_custom['item2']}")
    
    # 嵌套defaultdict
    print("   \n嵌套defaultdict:")
    
    # 创建两层嵌套的defaultdict
    nested_dd = collections.defaultdict(lambda: collections.defaultdict(list))
    nested_dd['group1']['item1'].append('value1')
    nested_dd['group1']['item2'].append('value2')
    nested_dd['group2']['item1'].append('value3')
    
    # 转换为普通字典以显示
    result = {}
    for group, items in nested_dd.items():
        result[group] = dict(items)
    
    print(f"   嵌套defaultdict: {result}")
    
    print("\n5. OrderedDict - 有序字典")
    print("   保持插入顺序的字典子类（Python 3.7+中dict已默认有序）")
    
    # 基本使用
    print("   基本有序特性:")
    
    # 创建OrderedDict
    od1 = collections.OrderedDict()
    od1['b'] = 2
    od1['a'] = 1
    od1['c'] = 3
    print(f"   按插入顺序: {list(od1.keys())}")
    
    # 删除和重新插入会改变顺序
    od1.pop('a')
    od1['a'] = 1
    print(f"   删除'a'后重新插入: {list(od1.keys())}")
    
    # 特殊方法
    print("   \nOrderedDict特有的方法:")
    
    od2 = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    
    # move_to_end: 将指定键移到末尾
    od2.move_to_end('a')
    print(f"   将'a'移到末尾: {list(od2.keys())}")
    
    # 移动到开头（Python 3.2+）
    od2.move_to_end('a', last=False)
    print(f"   将'a'移到开头: {list(od2.keys())}")
    
    # reversed: 逆序迭代
    reversed_keys = list(reversed(od2))
    print(f"   逆序键: {reversed_keys}")
    
    print("\n6. ChainMap - 链式映射")
    print("   将多个映射链接成一个单一的可更新视图")
    
    # 基本使用
    print("   基本链接功能:")
    
    # 创建多个字典
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    dict3 = {'a': 5, 'e': 6}  # 注意'a'键重复
    
    # 创建ChainMap
    chain = collections.ChainMap(dict1, dict2, dict3)
    print(f"   链接三个字典: {dict(chain)}")
    print(f"   访问'a': {chain['a']} (从第一个字典获取)")
    print(f"   访问'c': {chain['c']} (从第二个字典获取)")
    print(f"   访问'e': {chain['e']} (从第三个字典获取)")
    
    # 键查找顺序
    print(f"   查找顺序: {list(chain.keys())}")
    
    # 修改操作
    print("   \n修改操作:")
    
    # 修改会影响第一个字典
    chain['a'] = 10
    print(f"   修改'a'后chain: {dict(chain)}")
    print(f"   dict1变成: {dict1}")
    
    # 新增键也会添加到第一个字典
    chain['f'] = 7
    print(f"   新增'f'后chain: {dict(chain)}")
    print(f"   dict1变成: {dict1}")
    
    # 高级方法
    print("   \nChainMap特有的方法:")
    
    # new_child: 创建包含新映射的ChainMap
    new_chain = chain.new_child({'g': 8})
    print(f"   新增子映射后: {dict(new_chain)}")
    
    # parents: 返回不包含第一个映射的新ChainMap
    parents = chain.parents
    print(f"   不包含第一个映射: {dict(parents)}")
    
    print("\n7. UserDict, UserList, UserString")
    print("   封装内置类型的基类，便于自定义子类")
    
    print("   UserDict - 字典封装类:")
    class CustomDict(collections.UserDict):
        def __setitem__(self, key, value):
            # 自定义设置值的逻辑
            if isinstance(value, str):
                value = value.upper()
            super().__setitem__(key, value)
    
    custom_dict = CustomDict({'a': 'apple', 'b': 42})
    custom_dict['c'] = 'cherry'
    print(f"   自定义字典: {custom_dict}")
    
    print("   \nUserList - 列表封装类:")
    class CustomList(collections.UserList):
        def append(self, item):
            # 只允许添加数字类型
            if isinstance(item, (int, float)):
                super().append(item)
            else:
                print(f"   忽略非数字类型: {item}")
    
    custom_list = CustomList([1, 2, 3])
    custom_list.append(4)
    custom_list.append('not a number')
    print(f"   自定义列表: {custom_list}")
    
    print("   \nUserString - 字符串封装类:")
    class CustomString(collections.UserString):
        def append(self, string):
            # 添加append方法
            self.data += string
    
    custom_string = CustomString("Hello")
    custom_string.append(" World")
    print(f"   自定义字符串: {custom_string}")
    
    print("\n8. 容器数据类型对比")
    print("   各数据结构的性能和适用场景比较")
    
    print("   操作效率比较:")
    print("   - deque: 两端操作O(1)，中间操作O(n)")
    print("   - list: 末尾操作O(1)，头部操作O(n)，随机访问O(1)")
    print("   - dict/OrderedDict: 查找、插入、删除O(1)")
    print("   - Counter: 统计操作高效，继承自dict")
    print("   - defaultdict: 访问不存在键时自动创建默认值")
    
    print("   \n内存占用比较:")
    print("   - namedtuple: 比普通类更节省内存")
    print("   - deque: 比列表内存占用略高")
    print("   - OrderedDict: 比普通dict内存占用高")
    print("   - defaultdict: 与普通dict内存占用相近")
    
    print("   \n适用场景建议:")
    print("   - 频繁在两端操作: deque")
    print("   - 数据统计: Counter")
    print("   - 分组或嵌套结构: defaultdict")
    print("   - 需要命名字段的不可变数据: namedtuple")
    print("   - 需要保持插入顺序且Python < 3.7: OrderedDict")
    print("   - 组合多个字典: ChainMap")
    print("   - 自定义容器类型: UserDict/UserList/UserString")

# 运行核心数据结构详解
collections_core_data_structures()
print()

# 3. 高级应用示例
print("=== 3. 高级应用示例 ===")

def collections_advanced_examples():
    """collections模块的高级应用示例"""
    import collections
    import time
    from itertools import islice
    
    print("1. 使用namedtuple优化代码结构")
    print("   场景: 替代普通元组和简单类")
    
    # 示例1: 表示二维和三维点
    Point2D = collections.namedtuple('Point2D', ['x', 'y'])
    Point3D = collections.namedtuple('Point3D', Point2D._fields + ('z',))
    
    p2d = Point2D(10, 20)
    p3d = Point3D(10, 20, 30)
    
    print(f"   2D点: {p2d}")
    print(f"   3D点: {p3d}")
    
    # 计算距离
    def distance(p1, p2):
        if hasattr(p1, 'z') and hasattr(p2, 'z'):
            # 3D距离
            return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2 + (p1.z - p2.z)**2) ** 0.5
        else:
            # 2D距离
            return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2) ** 0.5
    
    print(f"   点距离 (2D): {distance(p2d, Point2D(15, 25)):.2f}")
    print(f"   点距离 (3D): {distance(p3d, Point3D(15, 25, 35)):.2f}")
    
    # 示例2: 替代简单类存储数据
    print("   \n使用namedtuple替代简单数据类:")
    
    # 传统方式
    class Product:
        def __init__(self, id, name, price, quantity):
            self.id = id
            self.name = name
            self.price = price
            self.quantity = quantity
    
    # 使用namedtuple
    ProductNT = collections.namedtuple('ProductNT', ['id', 'name', 'price', 'quantity'])
    
    # 创建实例
    product1 = Product(1, 'Laptop', 999.99, 5)
    product2 = ProductNT(2, 'Phone', 499.99, 10)
    
    print(f"   类方式: {product1.name} - ${product1.price}")
    print(f"   namedtuple方式: {product2.name} - ${product2.price}")
    
    # 序列化支持
    print(f"   namedtuple转字典: {product2._asdict()}")
    
    print("\n2. 使用deque实现高效队列和栈")
    print("   场景: 双端队列、滑动窗口、回文检测")
    
    # 示例1: 滑动窗口最大值
    def sliding_window_max(nums, k):
        """使用deque高效计算滑动窗口最大值"""
        result = []
        dq = collections.deque()  # 存储索引，保持降序
        
        for i in range(len(nums)):
            # 移除超出窗口范围的元素
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # 移除小于当前元素的值（维护降序）
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            # 添加当前索引
            dq.append(i)
            
            # 当窗口形成后，添加最大值
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
    
    test_nums = [1, 3, -1, -3, 5, 3, 6, 7]
    window_size = 3
    max_values = sliding_window_max(test_nums, window_size)
    
    print(f"   数组: {test_nums}")
    print(f"   窗口大小: {window_size}")
    print(f"   滑动窗口最大值: {max_values}")
    
    # 示例2: 回文检测
    def is_palindrome(s):
        """使用deque检测回文字符串"""
        # 过滤非字母数字并转换为小写
        filtered_chars = [c.lower() for c in s if c.isalnum()]
        dq = collections.deque(filtered_chars)
        
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
    
    test_strings = ["A man, a plan, a canal: Panama", "race a car", "Was it a car or a cat I saw?"]
    
    print("   \n回文检测:")
    for test in test_strings:
        result = is_palindrome(test)
        print(f"   '{test}' -> {'是回文' if result else '不是回文'}")
    
    print("\n3. 使用Counter进行文本分析")
    print("   场景: 词频统计、文本相似度、密码分析")
    
    # 示例1: 词频统计和停用词过滤
    def word_frequency(text, top_n=10, stop_words=None):
        """统计文本中词频最高的前N个词"""
        if stop_words is None:
            stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'of', 'for', 'with', 'by'}
        
        # 转换为小写并分割单词
        words = text.lower().split()
        # 过滤单词（移除标点和停用词）
        filtered_words = [word.strip('.,!?;:"') for word in words if word.strip('.,!?;:"') not in stop_words]
        
        # 统计词频
        word_counts = collections.Counter(filtered_words)
        
        return word_counts.most_common(top_n)
    
    sample_text = """Python is a high-level, interpreted, general-purpose programming language. 
    Its design philosophy emphasizes code readability with the use of significant indentation. 
    Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, 
    including structured (particularly procedural), object-oriented and functional programming. 
    It is often described as a "batteries included" language due to its comprehensive standard library."""
    
    top_words = word_frequency(sample_text, 5)
    
    print(f"   文本中最常见的5个单词:")
    for word, count in top_words:
        print(f"   '{word}': {count}次")
    
    # 示例2: 字符频率分析（用于简单密码分析）
    def char_frequency_analysis(text, plot=False):
        """分析文本中字符频率"""
        char_counter = collections.Counter(text)
        
        # 按频率排序
        sorted_chars = char_counter.most_common()
        
        print(f"   前10个最常见字符:")
        for char, count in sorted_chars[:10]:
            # 处理不可打印字符
            char_repr = repr(char)[1:-1]  # 获取字符的repr表示
            if len(char_repr) == 0:
                char_repr = 'space'
            print(f"   '{char_repr}': {count}次")
        
        return char_counter
    
    # 简单文本分析
    sample_passwords = "password123 admin qwerty letmein welcome123 abc123 password secret 123456789"
    char_freq = char_frequency_analysis(sample_passwords)
    
    print("\n4. 使用defaultdict构建复杂数据结构")
    print("   场景: 分组、嵌套数据处理、图表示")
    
    # 示例1: 分组数据
    def group_by_category(items, key_func):
        """根据指定键函数分组数据"""
        groups = collections.defaultdict(list)
        for item in items:
            key = key_func(item)
            groups[key].append(item)
        return groups
    
    # 测试数据
    products = [
        {"name": "Laptop", "category": "Electronics", "price": 999.99},
        {"name": "Smartphone", "category": "Electronics", "price": 599.99},
        {"name": "Book", "category": "Books", "price": 19.99},
        {"name": "Coffee Mug", "category": "Kitchen", "price": 12.99},
        {"name": "Novel", "category": "Books", "price": 14.99},
        {"name": "Toaster", "category": "Kitchen", "price": 29.99}
    ]
    
    # 按类别分组
    grouped_products = group_by_category(products, lambda p: p["category"])
    
    print("   按类别分组的产品:")
    for category, items in grouped_products.items():
        print(f"   {category}:")
        for item in items:
            print(f"     - {item['name']}: ${item['price']}")
    
    # 示例2: 构建图结构
    def build_graph(edges):
        """从边列表构建图（邻接表表示）"""
        graph = collections.defaultdict(list)
        for src, dest, weight in edges:
            graph[src].append((dest, weight))
        return graph
    
    # 示例边数据（无向图）
    edges = [
        ('A', 'B', 5),
        ('A', 'C', 2),
        ('B', 'D', 4),
        ('B', 'E', 3),
        ('C', 'F', 7),
        ('D', 'E', 1),
        ('E', 'F', 8)
    ]
    
    graph = build_graph(edges)
    
    print("   \n图的邻接表表示:")
    for node, neighbors in sorted(graph.items()):
        print(f"   {node} -> {neighbors}")
    
    # 示例3: 嵌套defaultdict处理JSON-like数据
    def process_nested_data(records):
        """处理嵌套数据结构"""
        # 创建多层嵌套的defaultdict
        nested_dict = collections.defaultdict(lambda: collections.defaultdict(list))
        
        for record in records:
            country = record["country"]
            city = record["city"]
            nested_dict[country][city].append(record["name"])
        
        return nested_dict
    
    # 测试数据
    people = [
        {"name": "Alice", "country": "USA", "city": "New York"},
        {"name": "Bob", "country": "USA", "city": "Boston"},
        {"name": "Charlie", "country": "Canada", "city": "Toronto"},
        {"name": "Dave", "country": "Canada", "city": "Vancouver"},
        {"name": "Eve", "country": "USA", "city": "New York"},
        {"name": "Frank", "country": "Canada", "city": "Toronto"}
    ]
    
    # 处理数据
    nested_data = process_nested_data(people)
    
    print("   \n按国家和城市分组的人员:")
    for country, cities in sorted(nested_data.items()):
        print(f"   {country}:")
        for city, names in sorted(cities.items()):
            print(f"     {city}: {', '.join(names)}")
    
    print("\n5. 使用ChainMap管理配置")
    print("   场景: 配置管理、环境变量覆盖、默认值处理")
    
    # 示例: 多级配置管理
    def create_config():
        """创建多级配置系统"""
        # 导入需要的模块
        import os
        import collections
        
        # 默认配置
        default_config = {
            'debug': False,
            'port': 8000,
            'host': 'localhost',
            'log_level': 'INFO',
            'database_url': 'sqlite:///:memory:'
        }
        
        # 用户配置（通常从文件加载）
        user_config = {
            'port': 8080,
            'debug': True
        }
        
        # 环境变量配置（最高优先级）
        env_config = {}
        # 尝试从环境变量获取配置
        if 'PORT' in os.environ:
            env_config['port'] = int(os.environ['PORT'])
        if 'HOST' in os.environ:
            env_config['host'] = os.environ['HOST']
        
        # 创建配置链（优先级从高到低）
        config = collections.ChainMap(env_config, user_config, default_config)
        
        return config
    
    # 模拟环境变量（在实际应用中由操作系统提供）
    # os.environ['PORT'] = '9000'  # 取消注释可测试
    
    config = create_config()
    
    print(f"   最终配置:")
    print(f"   调试模式: {config['debug']}")
    print(f"   端口: {config['port']}")
    print(f"   主机: {config['host']}")
    print(f"   日志级别: {config['log_level']}")
    print(f"   数据库URL: {config['database_url']}")
    
    # 配置更新示例
    print("   \n更新配置示例:")
    print(f"   初始端口: {config['port']}")
    
    # 添加新的环境变量
    config.maps[0]['port'] = 9000  # 更新最高优先级映射
    print(f"   更新后端口: {config['port']}")
    
    # 创建带额外配置的新ChainMap
    new_config = config.new_child({'port': 9500})
    print(f"   新配置端口: {new_config['port']}")
    
    print("\n6. 使用collections优化算法实现")
    print("   场景: 广度优先搜索、最小生成树、哈希表应用")
    
    # 示例1: 广度优先搜索（BFS）
    def bfs(graph, start_node, target_node):
        """使用deque实现广度优先搜索"""
        # 检查起始节点和目标节点是否相同
        if start_node == target_node:
            return [start_node]
        
        # 初始化队列和已访问集合
        queue = collections.deque([(start_node, [start_node])])
        visited = set([start_node])
        
        # BFS主循环
        while queue:
            current_node, path = queue.popleft()
            
            # 遍历所有邻居
            for neighbor, _ in graph.get(current_node, []):
                if neighbor not in visited:
                    # 找到目标
                    if neighbor == target_node:
                        return path + [neighbor]
                    
                    # 标记为已访问并加入队列
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        # 没有找到路径
        return None
    
    # 使用之前创建的图
    print(f"   图中从'A'到'F'的路径: {bfs(graph, 'A', 'F')}")
    
    # 示例2: 最小生成树（Kruskal算法）
    def kruskal_mst(edges):
        """使用Union-Find算法和Counter实现Kruskal最小生成树"""
        # 按权重排序边
        sorted_edges = sorted(edges, key=lambda x: x[2])
        
        # 初始化Union-Find结构
        parent = {}
        rank = {}
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  # 路径压缩
            return parent[node]
        
        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 == root2:
                return False  # 已在同一集合
            
            # 按秩合并
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
            
            return True
        
        # 初始化所有节点
        nodes = set()
        for src, dest, _ in edges:
            nodes.add(src)
            nodes.add(dest)
        
        for node in nodes:
            parent[node] = node
            rank[node] = 0
        
        # 构建MST
        mst = []
        total_weight = 0
        
        for src, dest, weight in sorted_edges:
            if union(src, dest):
                mst.append((src, dest, weight))
                total_weight += weight
        
        return mst, total_weight
    
    # 测试Kruskal算法
    mst_edges, total_weight = kruskal_mst(edges)
    
    print(f"   \n最小生成树边:")
    for src, dest, weight in mst_edges:
        print(f"   {src}-{dest}: {weight}")
    print(f"   总权重: {total_weight}")
    
# 运行高级应用示例
collections_advanced_examples()
print()

# 4. 性能分析和最佳实践
print("=== 4. 性能分析和最佳实践 ===")

def collections_performance_analysis():
    """collections模块的性能分析和最佳实践"""
    import collections
    import time
    import random
    
    print("1. 性能对比测试")
    print("   各数据结构在不同操作下的性能表现")
    
    # 测试参数
    sizes = [1000, 10000, 100000]
    iterations = 3
    
    # 1.1 列表 vs deque - 追加操作
    print("\n   1.1 追加操作性能对比 (列表 vs deque):")
    
    for size in sizes:
        # 测试列表
        start_time = time.time()
        for _ in range(iterations):
            lst = []
            for i in range(size):
                lst.append(i)
        list_time = (time.time() - start_time) / iterations
        
        # 测试deque
        start_time = time.time()
        for _ in range(iterations):
            dq = collections.deque()
            for i in range(size):
                dq.append(i)
        deque_time = (time.time() - start_time) / iterations
        
        print(f"   规模 {size}: 列表 {list_time:.6f}s, deque {deque_time:.6f}s")
    
    # 1.2 列表 vs deque - 左侧插入
    print("\n   1.2 左侧插入性能对比 (列表 vs deque):")
    
    for size in sizes:
        # 测试列表
        start_time = time.time()
        for _ in range(iterations):
            lst = []
            for i in range(size):
                lst.insert(0, i)
        list_time = (time.time() - start_time) / iterations
        
        # 测试deque
        start_time = time.time()
        for _ in range(iterations):
            dq = collections.deque()
            for i in range(size):
                dq.appendleft(i)
        deque_time = (time.time() - start_time) / iterations
        
        print(f"   规模 {size}: 列表 {list_time:.6f}s, deque {deque_time:.6f}s")
        print(f"   性能提升: {list_time / deque_time:.2f}倍")
    
    # 1.3 字典 vs defaultdict - 访问不存在的键
    print("\n   1.3 访问不存在键的性能对比 (字典 vs defaultdict):")
    
    for size in sizes:
        # 测试普通字典
        start_time = time.time()
        for _ in range(iterations):
            d = {}
            for i in range(size):
                # 使用get方法避免KeyError
                d.get(i, []).append(i)
        dict_time = (time.time() - start_time) / iterations
        
        # 测试defaultdict
        start_time = time.time()
        for _ in range(iterations):
            dd = collections.defaultdict(list)
            for i in range(size):
                dd[i].append(i)
        defaultdict_time = (time.time() - start_time) / iterations
        
        print(f"   规模 {size}: 普通字典 {dict_time:.6f}s, defaultdict {defaultdict_time:.6f}s")
        print(f"   性能提升: {dict_time / defaultdict_time:.2f}倍")
    
    # 1.4 列表.count() vs Counter - 元素统计
    print("\n   1.4 元素统计性能对比 (列表.count() vs Counter):")
    
    # 生成测试数据
    for size in sizes:
        data = [random.randint(0, 1000) for _ in range(size)]
        
        # 测试列表.count() (只统计前10个不同元素)
        unique_elements = list(set(data))[:10]
        
        start_time = time.time()
        for _ in range(iterations):
            counts = {}
            for elem in unique_elements:
                counts[elem] = data.count(elem)
        list_count_time = (time.time() - start_time) / iterations
        
        # 测试Counter
        start_time = time.time()
        for _ in range(iterations):
            counter = collections.Counter(data)
            counts = {elem: counter[elem] for elem in unique_elements}
        counter_time = (time.time() - start_time) / iterations
        
        print(f"   规模 {size}: 列表.count() {list_count_time:.6f}s, Counter {counter_time:.6f}s")
        print(f"   性能提升: {list_count_time / counter_time:.2f}倍")
    
    print("\n2. 内存使用分析")
    print("   各数据结构的内存占用情况")
    
    # 2.1 namedtuple vs 普通类 vs 字典
    print("\n   2.1 数据结构内存占用对比:")
    
    # 创建一个namedtuple
    PersonNT = collections.namedtuple('PersonNT', ['name', 'age', 'city'])
    
    # 创建一个普通类
    class PersonClass:
        def __init__(self, name, age, city):
            self.name = name
            self.age = age
            self.city = city
    
    # 创建实例并估算内存使用
    import sys
    
    # 普通元组
    t = ('John', 30, 'New York')
    # namedtuple
    nt = PersonNT('John', 30, 'New York')
    # 普通类
    c = PersonClass('John', 30, 'New York')
    # 字典
    d = {'name': 'John', 'age': 30, 'city': 'New York'}
    
    print(f"   普通元组: {sys.getsizeof(t)} bytes")
    print(f"   namedtuple: {sys.getsizeof(nt)} bytes")
    print(f"   普通类: {sys.getsizeof(c)} bytes (不含实例属性)")
    print(f"   字典: {sys.getsizeof(d)} bytes")
    
    # 测试大量实例的内存使用
    print("   \n   2.2 10000个实例的内存使用:")
    
    # 创建10000个namedtuple实例
    start_mem = sys.getsizeof([])
    nt_list = [PersonNT(f'Person{i}', i % 100, 'City') for i in range(10000)]
    nt_mem = sum(sys.getsizeof(nt) for nt in nt_list) + start_mem
    
    # 创建10000个类实例
    start_mem = sys.getsizeof([])
    class_list = [PersonClass(f'Person{i}', i % 100, 'City') for i in range(10000)]
    class_mem = sum(sys.getsizeof(obj) for obj in class_list) + start_mem
    
    # 创建10000个字典
    start_mem = sys.getsizeof([])
    dict_list = [{'name': f'Person{i}', 'age': i % 100, 'city': 'City'} for i in range(10000)]
    dict_mem = sum(sys.getsizeof(d) for d in dict_list) + start_mem
    
    print(f"   10000个namedtuple实例: {nt_mem / 1024:.2f} KB")
    print(f"   10000个普通类实例: {class_mem / 1024:.2f} KB")
    print(f"   10000个字典: {dict_mem / 1024:.2f} KB")
    
    print("\n3. 最佳实践和注意事项")
    print("   使用collections模块的推荐做法和常见陷阱")
    
    print("\n   3.1 推荐使用场景:")
    print("   - 需要频繁在两端操作数据: 使用deque代替列表")
    print("   - 需要快速统计元素频率: 使用Counter代替手动计数")
    print("   - 需要处理可能不存在的键: 使用defaultdict避免KeyError")
    print("   - 需要表示简单数据结构: 使用namedtuple提高可读性")
    print("   - 需要组合多个配置映射: 使用ChainMap保持优先级")
    print("   - 需要保持插入顺序且Python < 3.7: 使用OrderedDict")
    
    print("\n   3.2 性能优化建议:")
    print("   - 对于频繁的头部操作，总是使用deque而非列表")
    print("   - 使用Counter的most_common()方法获取高频元素")
    print("   - 为defaultdict选择合适的默认工厂函数")
    print("   - 使用namedtuple._asdict()进行序列化")
    print("   - 对大型数据集，考虑使用生成器表达式配合collections使用")
    
    print("\n   3.3 常见陷阱和注意事项:")
    print("   - namedtuple是不可变的，无法修改其字段值")
    print("   - deque的rotate()方法接受正数(右移)和负数(左移)参数")
    print("   - Counter在统计空容器时返回空Counter，而非0")
    print("   - defaultdict会自动为不存在的键创建默认值，这可能导致内存占用增加")
    print("   - OrderedDict在Python 3.7+中已基本被dict替代")
    print("   - ChainMap修改会影响原始字典，而不是创建副本")
    print("   - UserDict、UserList、UserString需要通过.data属性访问底层容器")
    
    print("\n   3.4 使用示例中的性能提示:")
    # 示例: 优化Counter使用
    print("   示例: 高效使用Counter进行词频统计:")
    
    # 低效方式
    def inefficient_word_count(text):
        words = text.split()
        counts = {}
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
    
    # 高效方式
    def efficient_word_count(text):
        return collections.Counter(text.split())
    
    # 性能测试
    test_text = "word " * 100000
    
    start_time = time.time()
    inefficient_word_count(test_text)
    inefficient_time = time.time() - start_time
    
    start_time = time.time()
    efficient_word_count(test_text)
    efficient_time = time.time() - start_time
    
    print(f"   低效方式: {inefficient_time:.6f}s")
    print(f"   高效方式: {efficient_time:.6f}s")
    print(f"   性能提升: {inefficient_time / efficient_time:.2f}倍")
    
    # 示例: deque作为队列的最佳实践
    print("   \n   示例: 高效队列实现:")
    
    # 使用collections.deque作为队列
    queue = collections.deque()
    
    # 添加元素
    for i in range(10000):
        queue.append(i)
    
    # 消费元素
    while queue:
        queue.popleft()  # O(1)操作
    
    print(f"   deque实现队列: 添加和消费10000个元素成功")
    
    # 版本兼容性注意
    print("\n   3.5 版本兼容性注意:")
    print("   - Python 3.1+: OrderedDict支持move_to_end方法")
    print("   - Python 3.7+: 内置dict保持插入顺序，OrderedDict的用途减少")
    print("   - Python 3.6+: 字典在CPython实现中保留插入顺序(非正式)")
    print("   - Python 2.x: 某些方法可能有所不同，建议查阅具体版本文档")
    
    # 错误处理建议
    print("\n   3.6 错误处理建议:")
    print("   - 使用defaultdict可以避免KeyError，但要确保默认值符合业务逻辑")
    print("   - 使用namedtuple._replace()创建新实例，而不是尝试修改现有实例")
    print("   - 处理Counter结果时，注意可能存在零或负计数")
    print("   - 使用ChainMap时，注意修改操作只影响第一个映射")

# 运行性能分析和最佳实践
collections_performance_analysis()
print()

# 5. 输入输出示例
print("=== 5. 输入输出示例 ===")

def collections_io_examples():
    """collections模块的输入输出示例"""
    import collections
    
    print("1. namedtuple使用示例")
    print("   输入:")
    print("   \"")
    from collections import namedtuple
    
    # 创建命名元组类
    Employee = namedtuple('Employee', ['id', 'name', 'position', 'salary'])
    
    # 创建实例
    emp1 = Employee(101, 'Alice', 'Developer', 80000)
    emp2 = Employee(102, 'Bob', 'Manager', 95000)
    
    # 访问字段
    print(f"ID: {emp1.id}, Name: {emp1.name}")
    print(f"Position: {emp2.position}, Salary: ${emp2.salary}")
    
    # 转换为字典
    print(emp1._asdict())
    
    # 字段替换
    emp3 = emp1._replace(salary=85000)
    print(f"Updated: {emp3}")
    """)
    
    print("   输出:")
    # 执行代码并捕获输出
    from collections import namedtuple
    
    # 创建命名元组类
    Employee = namedtuple('Employee', ['id', 'name', 'position', 'salary'])
    
    # 创建实例
    emp1 = Employee(101, 'Alice', 'Developer', 80000)
    emp2 = Employee(102, 'Bob', 'Manager', 95000)
    
    print(f"   ID: {emp1.id}, Name: {emp1.name}")
    print(f"   Position: {emp2.position}, Salary: ${emp2.salary}")
    print(f"   {emp1._asdict()}")
    
    # 字段替换
    emp3 = emp1._replace(salary=85000)
    print(f"   Updated: {emp3}")
    
    print("\n2. deque使用示例")
    print("   输入:")
    print("   """
    from collections import deque
    
    # 创建双端队列
    dq = deque([1, 2, 3])
    
    # 两端添加
    dq.append(4)      # 右侧添加
    dq.appendleft(0)  # 左侧添加
    print(f"添加后: {dq}")
    
    # 两端删除
    right_val = dq.pop()     # 右侧删除
    left_val = dq.popleft()  # 左侧删除
    print(f"删除后: {dq}")
    print(f"删除的值: right={right_val}, left={left_val}")
    
    # 旋转操作
    dq.rotate(1)  # 向右旋转1步
    print(f"右旋转后: {dq}")
    
    # 最大长度限制
    limited_dq = deque(maxlen=3)
    for i in range(5):
        limited_dq.append(i)
        print(f"  添加{i}: {limited_dq}")
    """)
    
    print("   输出:")
    from collections import deque
    
    # 创建双端队列
    dq = deque([1, 2, 3])
    
    # 两端添加
    dq.append(4)      # 右侧添加
    dq.appendleft(0)  # 左侧添加
    print(f"   添加后: {dq}")
    
    # 两端删除
    right_val = dq.pop()     # 右侧删除
    left_val = dq.popleft()  # 左侧删除
    print(f"   删除后: {dq}")
    print(f"   删除的值: right={right_val}, left={left_val}")
    
    # 旋转操作
    dq.rotate(1)  # 向右旋转1步
    print(f"   右旋转后: {dq}")
    
    # 最大长度限制
    limited_dq = deque(maxlen=3)
    print(f"   有限制队列:")
    for i in range(5):
        limited_dq.append(i)
        print(f"     添加{i}: {limited_dq}")
    
    print("\n3. Counter使用示例")
    print("   输入:")
    print("   """
    from collections import Counter
    
    # 从字符串创建计数器
    text = "programming is fun and programming is challenging"
    word_counter = Counter(text.split())
    
    # 输出计数结果
    print(f"词频统计: {dict(word_counter)}")
    
    # 获取最常见的3个词
    print(f"最常见的3个词: {word_counter.most_common(3)}")
    
    # 增加计数
    word_counter['programming'] += 1
    print(f"更新后: {word_counter['programming']}")
    
    # 减去计数
    word_counter.subtract({'programming': 2, 'is': 1})
    print(f"减少后: {dict(word_counter)}")
    
    # 清除负计数
    word_counter = Counter({k: v for k, v in word_counter.items() if v > 0})
    print(f"清除负计数后: {dict(word_counter)}")
    """)
    
    print("   输出:")
    from collections import Counter
    
    # 从字符串创建计数器
    text = "programming is fun and programming is challenging"
    word_counter = Counter(text.split())
    
    # 输出计数结果
    print(f"   词频统计: {dict(word_counter)}")
    
    # 获取最常见的3个词
    print(f"   最常见的3个词: {word_counter.most_common(3)}")
    
    # 增加计数
    word_counter['programming'] += 1
    print(f"   更新后: {word_counter['programming']}")
    
    # 减去计数
    word_counter.subtract({'programming': 2, 'is': 1})
    print(f"   减少后: {dict(word_counter)}")
    
    # 清除负计数
    word_counter = Counter({k: v for k, v in word_counter.items() if v > 0})
    print(f"   清除负计数后: {dict(word_counter)}")
    
    print("\n4. defaultdict使用示例")
    print("   输入:")
    print("   """
    from collections import defaultdict
    
    # 使用列表作为默认值（分组示例）
    grouped_by_age = defaultdict(list)
    
    people = [
        ('Alice', 30), ('Bob', 25), ('Charlie', 30),
        ('David', 25), ('Eve', 35), ('Frank', 25)
    ]
    
    # 按年龄分组
    for name, age in people:
        grouped_by_age[age].append(name)
    
    print(f"按年龄分组: {dict(grouped_by_age)}")
    
    # 使用整数作为默认值（计数示例）
    letter_count = defaultdict(int)
    text = "hello world"
    
    for letter in text:
        if letter.isalnum():
            letter_count[letter] += 1
    
    print(f"字母计数: {dict(letter_count)}")
    
    # 使用集合作为默认值（去重示例）
    words_by_length = defaultdict(set)
    words = ["cat", "dog", "apple", "car", "banana", "bat"]
    
    for word in words:
        words_by_length[len(word)].add(word)
    
    print(f"按长度分组(去重): {dict(words_by_length)}")
    """)
    
    print("   输出:")
    from collections import defaultdict
    
    # 使用列表作为默认值（分组示例）
    grouped_by_age = defaultdict(list)
    
    people = [
        ('Alice', 30), ('Bob', 25), ('Charlie', 30),
        ('David', 25), ('Eve', 35), ('Frank', 25)
    ]
    
    # 按年龄分组
    for name, age in people:
        grouped_by_age[age].append(name)
    
    print(f"   按年龄分组: {dict(grouped_by_age)}")
    
    # 使用整数作为默认值（计数示例）
    letter_count = defaultdict(int)
    text = "hello world"
    
    for letter in text:
        if letter.isalnum():
            letter_count[letter] += 1
    
    print(f"   字母计数: {dict(letter_count)}")
    
    # 使用集合作为默认值（去重示例）
    words_by_length = defaultdict(set)
    words = ["cat", "dog", "apple", "car", "banana", "bat"]
    
    for word in words:
        words_by_length[len(word)].add(word)
    
    print(f"   按长度分组(去重): {dict(words_by_length)}")
    
    print("\n5. ChainMap使用示例")
    print("   输入:")
    print("   """
    from collections import ChainMap
    
    # 创建多个字典
    config_defaults = {'theme': 'light', 'font_size': 12, 'show_help': True}
    user_config = {'font_size': 14, 'theme': 'dark'}
    session_config = {'show_help': False}
    
    # 创建配置链（优先级: session_config > user_config > config_defaults）
    config = ChainMap(session_config, user_config, config_defaults)
    
    # 访问配置
    print(f"主题: {config['theme']}")  # 来自user_config
    print(f"字体大小: {config['font_size']}")  # 来自user_config
    print(f"显示帮助: {config['show_help']}")  # 来自session_config
    
    # 修改配置（只影响第一个字典）
    config['font_size'] = 16
    print(f"\n修改后:")
    print(f"字体大小: {config['font_size']}")  # 现在来自session_config
    print(f"session_config: {session_config}")  # 被修改
    print(f"user_config: {user_config}")  # 未被修改
    
    # 获取父配置（不包含第一个映射）
    parent_config = config.parents
    print(f"\n父配置主题: {parent_config['theme']}")  # 现在来自user_config
    
    print("   输出:")
    from collections import ChainMap
    
    # 创建多个字典
    config_defaults = {'theme': 'light', 'font_size': 12, 'show_help': True}
    user_config = {'font_size': 14, 'theme': 'dark'}
    session_config = {'show_help': False}
    
    # 创建配置链（优先级: session_config > user_config > config_defaults）
    config = ChainMap(session_config, user_config, config_defaults)
    
    # 访问配置
    print(f"   主题: {config['theme']}")  # 来自user_config
    print(f"   字体大小: {config['font_size']}")  # 来自user_config
    print(f"   显示帮助: {config['show_help']}")  # 来自session_config
    
    # 修改配置（只影响第一个字典）
    config['font_size'] = 16
    print(f"   \n修改后:")
    print(f"   字体大小: {config['font_size']}")  # 现在来自session_config
    print(f"   session_config: {session_config}")  # 被修改
    print(f"   user_config: {user_config}")  # 未被修改
    
    # 获取父配置（不包含第一个映射）
    parent_config = config.parents
    print(f"   \n父配置主题: {parent_config['theme']}")  # 现在来自user_config

# 运行输入输出示例
collections_io_examples()
print()

# 6. 总结和导入指南
print("=== 6. 总结和导入指南 ===")

def collections_summary():
    """collections模块的总结和导入指南"""
    
    print("1. 核心功能总结")
    print("   collections模块提供了多种高性能、专业化的容器数据类型，扩展了Python内置的数据结构:")
    print("   - namedtuple: 创建带命名字段的元组，提高代码可读性和数据结构清晰度")
    print("   - deque: 双端队列，支持两端高效插入和删除，适用于队列、栈和滑动窗口等场景")
    print("   - Counter: 计数器，提供高效的元素频率统计功能")
    print("   - defaultdict: 自动为不存在的键提供默认值，简化代码并避免KeyError")
    print("   - OrderedDict: 保持插入顺序的字典（Python 3.7+中dict已具备此功能）")
    print("   - ChainMap: 组合多个映射，维持查找优先级，适用于配置管理等场景")
    print("   - UserDict/UserList/UserString: 封装内置类型的基类，便于自定义容器子类")
    
    print("\n2. 应用场景总结")
    print("   collections模块在以下场景中特别有用:")
    print("   - 数据处理和分析: 使用Counter进行频率统计，defaultdict进行分组")
    print("   - 算法实现: 使用deque实现队列、栈和BFS，优化性能")
    print("   - 配置管理: 使用ChainMap组合多级配置，保持优先级")
    print("   - 数据建模: 使用namedtuple表示简单数据结构，比普通类更高效")
    print("   - 自定义容器: 使用UserDict等类创建自定义数据结构")
    print("   - 性能优化: 针对特定操作选择更高效的数据结构")
    
    print("\n3. 完整导入指南")
    print("   collections模块的导入方式:")
    
    print("   3.1 基本导入")
    print("   导入整个模块:")
    print("   >>> import collections")
    print("   使用方式:")
    print("   >>> dq = collections.deque()")
    print("   >>> counter = collections.Counter()")
    
    print("   \n3.2 导入特定功能")
    print("   导入常用类:")
    print("   >>> from collections import deque, Counter, defaultdict, namedtuple")
    print("   使用方式:")
    print("   >>> dq = deque()")
    print("   >>> counter = Counter()")
    
    print("   \n3.3 常用导入组合")
    print("   数据处理场景:")
    print("   >>> from collections import Counter, defaultdict")
    
    print("   队列和算法场景:")
    print("   >>> from collections import deque")
    
    print("   数据建模场景:")
    print("   >>> from collections import namedtuple")
    
    print("   配置管理场景:")
    print("   >>> from collections import ChainMap")
    
    print("   自定义容器场景:")
    print("   >>> from collections import UserDict, UserList, UserString")
    
    print("\n4. 版本兼容性")
    print("   collections模块在Python各版本中的变化:")
    print("   - Python 2.x: 基础功能已存在，但某些方法可能有所不同")
    print("   - Python 3.1+: OrderedDict添加了move_to_end方法")
    print("   - Python 3.3+: ChainMap被添加到标准库")
    print("   - Python 3.6+: dict在CPython实现中开始保留插入顺序")
    print("   - Python 3.7+: dict正式保证保留插入顺序，OrderedDict的作用更多是向后兼容")
    print("   - Python 3.9+: 增强了对某些类型的支持")
    
    print("\n5. 最佳实践建议")
    print("   使用collections模块的最佳实践:")
    print("   - 根据操作特点选择合适的数据结构，优先考虑性能和代码可读性")
    print("   - 对于频繁的两端操作，总是使用deque而不是列表")
    print("   - 使用Counter进行频率统计，避免手动实现计数逻辑")
    print("   - 使用defaultdict处理需要默认值的场景，避免KeyError")
    print("   - 使用namedtuple代替简单类或元组，提高代码可读性")
    print("   - 对于多级配置，使用ChainMap保持优先级关系")
    print("   - 在Python 3.7+中，普通dict可以替代OrderedDict用于保持插入顺序")
    print("   - 注意内存使用，特别是在处理大规模数据时")
    print("   - 结合其他标准库模块（如itertools、functools）使用，获得更强大的功能")

# 运行总结和导入指南
collections_summary()

print("\n=== collections模块文档完成 ===")
print("本模块文档详细介绍了collections模块的所有核心功能、使用方法和最佳实践。")
print("包含了namedtuple、deque、Counter、defaultdict、OrderedDict、ChainMap等数据结构的详细说明。")
print("通过丰富的代码示例展示了这些数据结构在实际应用中的使用方式和性能特点。")
print("建议在需要高效数据处理或特殊数据结构时优先考虑使用collections模块。")