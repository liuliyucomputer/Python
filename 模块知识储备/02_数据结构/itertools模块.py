# Python itertools模块详解

# 1. itertools模块概述
print("=== 1. itertools模块概述 ===")
print("itertools模块提供了用于高效循环迭代的函数，这些函数创建迭代器以支持循环。")
print("itertools模块中的函数被设计为高效且内存友好，它们通常用于处理大数据流。")
print("这些迭代器函数可以组合使用，创建更复杂的数据处理流水线。")
print("itertools模块特别适用于需要迭代和处理大量数据的场景，避免一次性加载所有数据到内存。")
print()

# 2. 无限迭代器
print("=== 2. 无限迭代器 ===")

def itertools_infinite_iterators():
    """展示itertools模块中的无限迭代器函数"""
    import itertools
    import time
    
    print("1. itertools.count(start=0, step=1):")
    print("   从start开始，以step为步长无限递增的迭代器")
    print("   注意：这是一个无限迭代器，使用时需要设置终止条件")
    
    # 演示count函数，只取前5个元素
    print("   示例: count(10, 2)的前5个元素:")
    for i, num in enumerate(itertools.count(10, 2)):
        print(f"   {num}")
        if i >= 4:  # 只取前5个元素
            break
    
    print("\n2. itertools.cycle(iterable):")
    print("   无限循环迭代iterable中的元素")
    print("   注意：这是一个无限迭代器，使用时需要设置终止条件")
    
    # 演示cycle函数，只取前8个元素
    print("   示例: cycle(['A', 'B', 'C'])的前8个元素:")
    for i, item in enumerate(itertools.cycle(['A', 'B', 'C'])):
        print(f"   {item}")
        if i >= 7:  # 只取前8个元素
            break
    
    print("\n3. itertools.repeat(object, times=None):")
    print("   重复object指定的times次数，如果times为None则无限重复")
    
    # 演示repeat函数，设置times参数
    print("   示例: repeat('Hello', 3):")
    for item in itertools.repeat('Hello', 3):
        print(f"   {item}")
    
    # 演示repeat函数，无限重复但设置终止条件
    print("   示例: repeat(42)的前5个元素:")
    for i, item in enumerate(itertools.repeat(42)):
        print(f"   {item}")
        if i >= 4:  # 只取前5个元素
            break
    
    print("\n4. 实际应用示例:")
    print("   a. 使用count创建带索引的迭代:")
    data = ['apple', 'banana', 'cherry']
    print("   带索引的数据:")
    for i, fruit in enumerate(data):
        print(f"   {i}: {fruit}")
    
    print("   使用count的等效实现:")
    for i, fruit in zip(itertools.count(), data):
        print(f"   {i}: {fruit}")
    
    print("   \nb. 使用cycle实现轮询调度:")
    servers = ['server1', 'server2', 'server3']
    tasks = ['task1', 'task2', 'task3', 'task4', 'task5']
    
    print("   任务分配:")
    for task, server in zip(tasks, itertools.cycle(servers)):
        print(f"   {task} -> {server}")
    
    print("   \nc. 使用repeat创建固定长度的列表:")
    default_values = list(itertools.repeat(0, 5))
    print(f"   创建包含5个0的列表: {default_values}")
    
    # 使用repeat结合zip创建乘法表
    print("   \nd. 使用repeat和zip创建乘法表:")
    print("   3x3乘法表:")
    for i, row in enumerate(range(1, 4)):
        products = [row * col for col in range(1, 4)]
        print(f"   {' '.join(map(str, products))}")
    
    print("   使用itertools的实现:")
    for row in range(1, 4):
        # 使用repeat和map创建乘法表的一行
        products = list(map(lambda x, y: x * y, itertools.repeat(row, 3), range(1, 4)))
        print(f"   {' '.join(map(str, products))}")

itertools_infinite_iterators()
print()

# 3. 迭代器组合器
print("=== 3. 迭代器组合器 ===")

def itertools_combinators():
    """展示itertools模块中的迭代器组合器函数"""
    import itertools
    
    print("1. itertools.accumulate(iterable, func=None, *, initial=None):")
    print("   返回累积和或使用func指定的二元函数的累积结果")
    
    # 默认使用加法累积
    print("   示例: accumulate([1, 2, 3, 4, 5]):")
    result = list(itertools.accumulate([1, 2, 3, 4, 5]))
    print(f"   {result}")
    
    # 使用乘法累积
    print("   示例: accumulate([1, 2, 3, 4, 5], func=lambda x, y: x*y):")
    result = list(itertools.accumulate([1, 2, 3, 4, 5], func=lambda x, y: x*y))
    print(f"   {result}")
    
    # 使用max函数累积
    print("   示例: accumulate([5, 2, 6, 1, 3], func=max):")
    result = list(itertools.accumulate([5, 2, 6, 1, 3], func=max))
    print(f"   {result}")
    
    # 使用initial参数
    print("   示例: accumulate([1, 2, 3], initial=10):")
    result = list(itertools.accumulate([1, 2, 3], initial=10))
    print(f"   {result}")
    
    print("\n2. itertools.chain(*iterables):")
    print("   将多个迭代器连接成一个迭代器")
    
    # 连接多个列表
    print("   示例: chain([1, 2, 3], [4, 5], [6, 7, 8]):")
    result = list(itertools.chain([1, 2, 3], [4, 5], [6, 7, 8]))
    print(f"   {result}")
    
    # 连接列表和元组
    print("   示例: chain([1, 2], (3, 4), {5, 6}, '78'):")
    result = list(itertools.chain([1, 2], (3, 4), {5, 6}, '78'))
    print(f"   {result}")
    
    # 连接生成器表达式
    print("   示例: chain(x for x in range(3), x for x in range(10, 13)):")
    result = list(itertools.chain((x for x in range(3)), (x for x in range(10, 13))))
    print(f"   {result}")
    
    print("\n3. itertools.chain.from_iterable(iterable):")
    print("   从一个可迭代对象中提取子迭代器并连接")
    
    # 从嵌套列表中提取并连接
    print("   示例: chain.from_iterable([[1, 2], [3, 4], [5, 6]]):")
    result = list(itertools.chain.from_iterable([[1, 2], [3, 4], [5, 6]]))
    print(f"   {result}")
    
    # 从字符串列表中提取并连接
    print("   示例: chain.from_iterable(['abc', 'def', 'ghi']):")
    result = list(itertools.chain.from_iterable(['abc', 'def', 'ghi']))
    print(f"   {result}")
    
    print("\n4. itertools.compress(data, selectors):")
    print("   使用selectors过滤data中的元素，仅保留selectors中为True对应位置的元素")
    
    # 基本用法
    print("   示例: compress([1, 2, 3, 4, 5], [True, False, True, False, True]):")
    result = list(itertools.compress([1, 2, 3, 4, 5], [True, False, True, False, True]))
    print(f"   {result}")
    
    # 使用列表推导式生成选择器
    print("   示例: 过滤偶数:")
    data = list(range(1, 11))
    selectors = [x % 2 == 0 for x in data]
    result = list(itertools.compress(data, selectors))
    print(f"   原始数据: {data}")
    print(f"   选择器: {selectors}")
    print(f"   结果: {result}")
    
    # 使用另一个可迭代对象作为选择器
    print("   示例: 使用字符串作为选择器:")
    data = ['a', 'b', 'c', 'd', 'e']
    # 非空字符串为True，空字符串为False
    selectors = ['x', '', 'y', '', 'z']
    result = list(itertools.compress(data, selectors))
    print(f"   原始数据: {data}")
    print(f"   选择器: {selectors}")
    print(f"   结果: {result}")
    
    print("\n5. itertools.dropwhile(predicate, iterable):")
    print("   丢弃iterable中predicate为True的元素，直到遇到第一个predicate为False的元素")
    print("   然后返回该元素及其后的所有元素")
    
    # 基本用法
    print("   示例: dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1]):")
    result = list(itertools.dropwhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1]))
    print(f"   {result}")
    
    # 注意与filter的区别
    print("   比较filter和dropwhile:")
    data = [1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1]
    filter_result = list(filter(lambda x: x >= 5, data))
    dropwhile_result = list(itertools.dropwhile(lambda x: x < 5, data))
    print(f"   原始数据: {data}")
    print(f"   filter结果: {filter_result}")
    print(f"   dropwhile结果: {dropwhile_result}")
    
    print("\n6. itertools.takewhile(predicate, iterable):")
    print("   从iterable中获取元素，直到遇到第一个predicate为False的元素")
    print("   然后停止并返回已获取的元素")
    
    # 基本用法
    print("   示例: takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1]):")
    result = list(itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1]))
    print(f"   {result}")
    
    # 与dropwhile的对比
    print("   takewhile和dropwhile对比:")
    data = [1, 2, 3, 4, 5, 6, 7, 4, 3, 2, 1]
    takewhile_result = list(itertools.takewhile(lambda x: x < 5, data))
    dropwhile_result = list(itertools.dropwhile(lambda x: x < 5, data))
    print(f"   原始数据: {data}")
    print(f"   takewhile结果: {takewhile_result}")
    print(f"   dropwhile结果: {dropwhile_result}")
    print(f"   组合结果: {takewhile_result + dropwhile_result == data}")

itertools_combinators()
print()

# 4. 组合生成器
print("=== 4. 组合生成器 ===")

def itertools_combination_generators():
    """展示itertools模块中的组合生成器函数"""
    import itertools
    
    print("1. itertools.product(*iterables, repeat=1):")
    print("   生成多个可迭代对象的笛卡尔积")
    print("   repeat参数指定重复使用输入的次数")
    
    # 两个列表的笛卡尔积
    print("   示例: product([1, 2], ['a', 'b']):")
    result = list(itertools.product([1, 2], ['a', 'b']))
    print(f"   {result}")
    
    # 三个列表的笛卡尔积
    print("   示例: product([1, 2], ['a', 'b'], ['x', 'y']):")
    result = list(itertools.product([1, 2], ['a', 'b'], ['x', 'y']))
    print(f"   {result}")
    
    # 使用repeat参数
    print("   示例: product([1, 2], repeat=3):")
    result = list(itertools.product([1, 2], repeat=3))
    print(f"   {result}")
    
    print("\n2. itertools.permutations(iterable, r=None):")
    print("   生成iterable中所有长度为r的排列")
    print("   r默认为None，表示生成所有元素的全排列")
    
    # 生成所有元素的全排列
    print("   示例: permutations(['a', 'b', 'c']):")
    result = list(itertools.permutations(['a', 'b', 'c']))
    print(f"   {result}")
    
    # 生成指定长度的排列
    print("   示例: permutations(['a', 'b', 'c'], 2):")
    result = list(itertools.permutations(['a', 'b', 'c'], 2))
    print(f"   {result}")
    
    # 处理包含重复元素的情况
    print("   示例: permutations(['a', 'a', 'b']):")
    result = list(itertools.permutations(['a', 'a', 'b']))
    print(f"   {result}")
    print(f"   注意: 即使输入中有重复元素，也会生成所有可能的排列")
    
    print("\n3. itertools.combinations(iterable, r):")
    print("   生成iterable中所有长度为r的组合（不考虑顺序，元素不重复）")
    
    # 基本用法
    print("   示例: combinations(['a', 'b', 'c'], 2):")
    result = list(itertools.combinations(['a', 'b', 'c'], 2))
    print(f"   {result}")
    
    # 生成3个元素的组合
    print("   示例: combinations(['a', 'b', 'c', 'd'], 3):")
    result = list(itertools.combinations(['a', 'b', 'c', 'd'], 3))
    print(f"   {result}")
    
    print("\n4. itertools.combinations_with_replacement(iterable, r):")
    print("   生成iterable中所有长度为r的组合（不考虑顺序，元素可以重复使用）")
    
    # 基本用法
    print("   示例: combinations_with_replacement(['a', 'b', 'c'], 2):")
    result = list(itertools.combinations_with_replacement(['a', 'b', 'c'], 2))
    print(f"   {result}")
    
    # 生成3个元素的组合（允许重复）
    print("   示例: combinations_with_replacement([1, 2], 3):")
    result = list(itertools.combinations_with_replacement([1, 2], 3))
    print(f"   {result}")
    
    print("\n5. 实际应用示例:")
    print("   a. 使用product生成所有可能的密码组合:")
    print("   生成所有2位数字密码:")
    digits = '0123456789'
    # 仅生成前10个作为示例
    first_10_passwords = list(itertools.islice(itertools.product(digits, repeat=2), 10))
    print(f"   {[''.join(pair) for pair in first_10_passwords]}")
    print(f"   总共有{len(list(itertools.product(digits, repeat=2)))}种可能的组合")
    
    print("   \nb. 使用permutations生成排序选项:")
    print("   生成3个元素的所有排列:")
    elements = ['A', 'B', 'C']
    permutations = list(itertools.permutations(elements))
    for i, perm in enumerate(permutations):
        print(f"   {i+1}. {perm}")
    
    print("   \nc. 使用combinations生成团队成员选择:")
    print("   从5个人中选择3人组成团队的所有可能:")
    people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    teams = list(itertools.combinations(people, 3))
    for i, team in enumerate(teams):
        print(f"   团队{i+1}: {team}")
    
    print("   \nd. 使用combinations_with_replacement生成口味组合:")
    print("   从3种冰淇淋口味中选择2种（允许重复）:")
    flavors = ['香草', '巧克力', '草莓']
    combinations = list(itertools.combinations_with_replacement(flavors, 2))
    for combo in combinations:
        print(f"   {combo}")

itertools_combination_generators()
print()

# 5. 其他实用迭代器
print("=== 5. 其他实用迭代器 ===")

def itertools_other_iterators():
    """展示itertools模块中的其他实用迭代器函数"""
    import itertools
    
    print("1. itertools.groupby(iterable, key=None):")
    print("   根据key函数的结果将iterable中的连续元素分组")
    print("   返回包含(key, group_iterator)对的迭代器")
    print("   注意：输入数据应该已按key函数排序，否则可能导致同一key值被分成多个组")
    
    # 按字母分组
    print("   示例: 按字母分组:")
    data = ['apple', 'ant', 'banana', 'bat', 'cat', 'car']
    # 按第一个字母分组（已排序）
    for key, group in itertools.groupby(data, key=lambda x: x[0]):
        print(f"   字母'{key}': {list(group)}")
    
    # 错误用法：未排序的数据
    print("   \n错误示例: 未排序的数据:")
    unsorted_data = ['apple', 'banana', 'ant', 'bat', 'cat', 'car']
    for key, group in itertools.groupby(unsorted_data, key=lambda x: x[0]):
        print(f"   字母'{key}': {list(group)}")
    print("   注意: 'a'组被分成了两部分，因为数据未排序")
    
    # 按奇偶性分组
    print("   \n示例: 按奇偶性分组:")
    numbers = [1, 1, 2, 3, 3, 3, 4, 4, 5]
    # 按奇偶性分组（已按奇偶数顺序排列）
    for key, group in itertools.groupby(numbers, key=lambda x: x % 2 == 0):
        status = '偶数' if key else '奇数'
        print(f"   {status}: {list(group)}")
    
    print("\n2. itertools.islice(iterable, start, stop=None, step=None):")
    print("   返回iterable的切片，支持start, stop, step参数")
    print("   与列表切片不同，islice不支持负索引")
    
    # 基本用法
    print("   示例: islice(range(10), 2, 8, 2):")
    result = list(itertools.islice(range(10), 2, 8, 2))
    print(f"   {result}")
    
    # 仅指定stop
    print("   示例: islice(range(10), 5):")
    result = list(itertools.islice(range(10), 5))
    print(f"   {result}")
    
    # 与无限迭代器配合使用
    print("   示例: islice(count(), 5, 15, 2):")
    result = list(itertools.islice(itertools.count(), 5, 15, 2))
    print(f"   {result}")
    
    # 从迭代器中获取前N个元素
    print("   示例: 从生成器中获取前5个元素:")
    def infinite_generator():
        i = 0
        while True:
            yield i
            i += 1
    
    limited_result = list(itertools.islice(infinite_generator(), 5))
    print(f"   {limited_result}")
    
    print("\n3. itertools.starmap(function, iterable):")
    print("   对iterable中的每个元素作为参数元组调用function")
    print("   相当于map(lambda args: function(*args), iterable)")
    
    # 基本用法
    print("   示例: starmap(pow, [(2, 5), (3, 2), (10, 3)]):")
    result = list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)]))
    print(f"   {result}")
    
    # 使用lambda函数
    print("   示例: starmap(lambda x, y: x+y, [(1, 2), (3, 4), (5, 6)]):")
    result = list(itertools.starmap(lambda x, y: x+y, [(1, 2), (3, 4), (5, 6)]))
    print(f"   {result}")
    
    # 与zip配合使用
    print("   示例: 计算多个向量的点积:")
    vectors1 = [(1, 2), (3, 4), (5, 6)]
    vectors2 = [(7, 8), (9, 10), (11, 12)]
    # 计算每个对应向量的点积
    dot_products = list(itertools.starmap(
        lambda v1, v2: v1[0]*v2[0] + v1[1]*v2[1], 
        zip(vectors1, vectors2)
    ))
    print(f"   向量1: {vectors1}")
    print(f"   向量2: {vectors2}")
    print(f"   点积结果: {dot_products}")
    
    print("\n4. itertools.zip_longest(*iterables, fillvalue=None):")
    print("   类似于zip，但会填充较短的可迭代对象，直到最长的可迭代对象用完")
    print("   fillvalue指定用于填充的值，默认为None")
    
    # 基本用法
    print("   示例: zip_longest(['a', 'b', 'c'], [1, 2]):")
    result = list(itertools.zip_longest(['a', 'b', 'c'], [1, 2]))
    print(f"   {result}")
    
    # 指定fillvalue
    print("   示例: zip_longest(['a', 'b'], [1, 2, 3, 4], fillvalue='-'):")
    result = list(itertools.zip_longest(['a', 'b'], [1, 2, 3, 4], fillvalue='-'))
    print(f"   {result}")
    
    # 与zip的对比
    print("   对比zip和zip_longest:")
    list1 = ['a', 'b', 'c']
    list2 = [1, 2]
    zip_result = list(zip(list1, list2))
    zip_longest_result = list(itertools.zip_longest(list1, list2))
    print(f"   list1: {list1}")
    print(f"   list2: {list2}")
    print(f"   zip结果: {zip_result}")
    print(f"   zip_longest结果: {zip_longest_result}")
    
    print("\n5. itertools.filterfalse(predicate, iterable):")
    print("   返回iterable中predicate为False的元素")
    print("   与filter函数相反")
    
    # 基本用法
    print("   示例: filterfalse(lambda x: x % 2 == 0, range(10)):")
    result = list(itertools.filterfalse(lambda x: x % 2 == 0, range(10)))
    print(f"   {result}")
    
    # 与filter的对比
    print("   对比filter和filterfalse:")
    numbers = list(range(10))
    filter_result = list(filter(lambda x: x % 2 == 0, numbers))
    filterfalse_result = list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))
    print(f"   原始数据: {numbers}")
    print(f"   filter(偶数): {filter_result}")
    print(f"   filterfalse(偶数): {filterfalse_result}")
    print(f"   检查是否互补: {sorted(filter_result + filterfalse_result) == sorted(numbers)}")
    
    # 使用None作为predicate
    print("   \n使用None作为predicate:")
    data = [0, 1, False, True, '', 'hello', None, []]
    # filter使用None时，只保留真值
    filter_result = list(filter(None, data))
    # filterfalse使用None时，只保留假值
    filterfalse_result = list(itertools.filterfalse(None, data))
    print(f"   原始数据: {data}")
    print(f"   filter(None): {filter_result}")
    print(f"   filterfalse(None): {filterfalse_result}")

itertools_other_iterators()
print()

# 6. 高级应用示例
print("=== 6. 高级应用示例 ===")

def itertools_advanced_examples():
    """itertools模块的高级应用示例"""
    import itertools
    
    print("\n示例1: 创建自定义迭代器组合")
    def custom_iterators():
        """组合多个itertools函数创建自定义迭代器"""
        
        print("   1. 创建一个每隔n个元素采样一次的迭代器:")
        def sample_every_n(iterable, n):
            """每隔n个元素采样一次"""
            # 使用islice的step参数
            return itertools.islice(iterable, 0, None, n)
        
        # 测试sample_every_n函数
        data = list(range(20))
        print(f"   原始数据: {data}")
        print(f"   每隔3个元素采样: {list(sample_every_n(data, 3))}")
        
        print("   \n2. 创建一个迭代器，生成从1到n的所有素数:")
        def primes_up_to(n):
            """生成从2到n的所有素数"""
            # 使用埃拉托斯特尼筛法的变体
            if n < 2:
                return
            
            # 创建一个标记数组，初始假设所有数都是素数
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0和1不是素数
            
            # 标记非素数
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    # 标记i的倍数为非素数
                    for j in range(i*i, n+1, i):
                        is_prime[j] = False
            
            # 使用compress返回所有素数
            return itertools.compress(range(n+1), is_prime)
        
        # 测试primes_up_to函数
        print(f"   100以内的素数: {list(primes_up_to(100))}")
        
        print("   \n3. 创建一个迭代器，生成斐波那契数列:")
        def fibonacci():
            """无限生成斐波那契数列"""
            a, b = 0, 1
            while True:
                yield a
                a, b = b, a + b
        
        # 获取前10个斐波那契数
        fibonacci_10 = list(itertools.islice(fibonacci(), 10))
        print(f"   前10个斐波那契数: {fibonacci_10}")
        
        print("   \n4. 创建一个迭代器，生成帕斯卡三角形的行:")
        def pascals_triangle():
            """无限生成帕斯卡三角形的行"""
            row = [1]  # 第一行
            while True:
                yield row
                # 计算下一行
                # 上一行的每个元素与下一个元素相加，再在开头和结尾添加1
                row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
        
        # 获取前5行帕斯卡三角形
        pascal_5 = list(itertools.islice(pascals_triangle(), 5))
        print("   前5行帕斯卡三角形:")
        for i, row in enumerate(pascal_5):
            print(f"   第{i+1}行: {row}")
    
    custom_iterators()
    
    print("\n示例2: 使用itertools进行数据处理")
    def data_processing_examples():
        """展示如何使用itertools进行数据处理"""
        
        print("   1. 按条件分组并计算统计信息:")
        # 示例数据: 一组学生及其成绩
        students = [
            ('Alice', 'Math', 95),
            ('Alice', 'English', 88),
            ('Alice', 'Science', 92),
            ('Bob', 'Math', 87),
            ('Bob', 'English', 76),
            ('Bob', 'Science', 90),
            ('Charlie', 'Math', 91),
            ('Charlie', 'English', 85),
            ('Charlie', 'Science', 89)
        ]
        
        # 按学生分组
        # 先按学生排序
        sorted_students = sorted(students, key=lambda x: x[0])
        
        print("   学生成绩统计:")
        for student, courses in itertools.groupby(sorted_students, key=lambda x: x[0]):
            # 获取该学生的所有课程和成绩
            student_courses = list(courses)
            # 计算平均分
            avg_score = sum(score for _, _, score in student_courses) / len(student_courses)
            # 获取最高分和最低分
            scores = [score for _, _, score in student_courses]
            max_score = max(scores)
            min_score = min(scores)
            # 打印统计信息
            print(f"   {student}: 平均分={avg_score:.1f}, 最高分={max_score}, 最低分={min_score}")
        
        print("   \n2. 查找文件中的重复行:")
        # 假设这是从文件中读取的行
        file_lines = [
            'apple',
            'banana',
            'apple',
            'orange',
            'banana',
            'apple',
            'grape'
        ]
        
        # 按行内容排序
        sorted_lines = sorted(file_lines)
        
        print("   文件中的重复行:")
        for line, group in itertools.groupby(sorted_lines):
            # 计算行出现的次数
            count = len(list(group))
            if count > 1:
                print(f"   '{line}' 出现了 {count} 次")
        
        print("   \n3. 生成数据序列的所有可能变化:")
        # 示例数据: 一个简单的序列
        sequence = ['A', 'B', 'C']
        
        print("   序列的所有可能变化:")
        print("   1. 所有排列:")
        for perm in itertools.permutations(sequence):
            print(f"      {perm}")
        
        print("   2. 所有长度为2的组合:")
        for combo in itertools.combinations(sequence, 2):
            print(f"      {combo}")
        
        print("   3. 所有长度为2的组合（允许重复）:")
        for combo in itertools.combinations_with_replacement(sequence, 2):
            print(f"      {combo}")
        
        print("   4. 与自身的笛卡尔积:")
        for product in itertools.product(sequence, repeat=2):
            print(f"      {product}")
    
    data_processing_examples()
    
    print("\n示例3: 性能优化示例")
    def performance_examples():
        """展示itertools模块在性能优化方面的应用"""
        import time
        
        print("   1. 大数据集处理中的内存优化:")
        print("   比较处理大型数据集时使用列表和迭代器的内存占用差异:")
        
        # 生成一个大型数据集
        def generate_large_data(n):
            """生成大型数据集"""
            return (i for i in range(n))
        
        # 使用列表处理（一次性加载所有数据）
        n = 10000000  # 一千万条数据
        
        print(f"   处理{n:,}条数据:")
        
        # 方法1: 使用列表
        start_time = time.time()
        data_list = list(generate_large_data(n))
        even_list = [x for x in data_list if x % 2 == 0]
        result_list = [x * 2 for x in even_list]
        end_time = time.time()
        print(f"   使用列表方法耗时: {end_time - start_time:.4f} 秒")
        print(f"   中间结果（偶数列表）长度: {len(even_list):,}")
        
        # 释放内存
        del data_list
        del even_list
        del result_list
        
        # 方法2: 使用迭代器（使用itertools）
        start_time = time.time()
        # 直接在迭代器上操作，避免创建大型中间列表
        data_iter = generate_large_data(n)
        even_iter = itertools.filterfalse(lambda x: x % 2 != 0, data_iter)
        result_count = sum(1 for x in even_iter)  # 只计算结果数量以避免创建列表
        end_time = time.time()
        print(f"   使用迭代器方法耗时: {end_time - start_time:.4f} 秒")
        print(f"   结果数量: {result_count:,}")
        
        print("   \n注意: 迭代器方法在处理大型数据集时显著节省内存，")
        print("        并且在某些情况下也可能更快。")
        
        print("   \n2. 使用itertools进行惰性计算:")
        print("   惰性计算允许在需要时才生成结果，而不是一次性生成所有结果:")
        
        def lazy_computation_example():
            """演示惰性计算"""
            # 创建一个无限生成器
            def infinite_calculator():
                i = 0
                while True:
                    # 模拟耗时计算
                    result = i ** 2
                    yield result
                    i += 1
            
            # 获取前5个结果
            calculator = infinite_calculator()
            first_5_results = list(itertools.islice(calculator, 5))
            print(f"   惰性计算的前5个结果: {first_5_results}")
            
            # 继续获取接下来的5个结果
            next_5_results = list(itertools.islice(calculator, 5))
            print(f"   继续计算的5个结果: {next_5_results}")
        
        lazy_computation_example()
    
    performance_examples()

itertools_advanced_examples()
print()

# 7. 性能考虑
print("=== 7. 性能考虑 ===")

def itertools_performance_considerations():
    """itertools模块的性能考虑"""
    import itertools
    import time
    import random
    
    print("1. 内存效率:")
    print("   - itertools模块生成的是迭代器，只在需要时生成值")
    print("   - 与列表相比，迭代器占用的内存更少，特别是对于大型数据集")
    print("   - 迭代器允许处理无限序列，而这对于列表是不可能的")
    
    print("\n2. 时间效率:")
    print("   - itertools模块中的函数通常是用C实现的，比Python代码实现的相同功能更快")
    print("   - 避免创建中间列表可以显著提高性能")
    print("   - 迭代器链允许高效地组合多个操作")
    
    print("\n3. 性能测试:")
    print("   比较itertools函数与Python原生方法的性能差异:")
    
    # 测试数据大小
    n = 1000000
    
    # 测试1: 生成斐波那契数列
    print(f"\n   测试1: 生成前{n//1000}个斐波那契数:")
    
    # 使用Python原生方法
    def fibonacci_python(n):
        result = []
        a, b = 0, 1
        for _ in range(n):
            result.append(a)
            a, b = b, a + b
        return result
    
    # 使用itertools
    def fibonacci_itertools(n):
        def fib():
            a, b = 0, 1
            while True:
                yield a
                a, b = b, a + b
        return list(itertools.islice(fib(), n))
    
    # 测量Python原生方法的性能
    start_time = time.time()
    fib_python = fibonacci_python(n//1000)
    python_time = time.time() - start_time
    
    # 测量itertools方法的性能
    start_time = time.time()
    fib_itertools = fibonacci_itertools(n//1000)
    itertools_time = time.time() - start_time
    
    print(f"   Python原生方法耗时: {python_time:.6f} 秒")
    print(f"   itertools方法耗时: {itertools_time:.6f} 秒")
    print(f"   itertools比Python原生方法快 {python_time / itertools_time:.2f} 倍")
    
    # 测试2: 过滤偶数
    print(f"\n   测试2: 从{n:,}个随机数中过滤偶数:")
    
    # 生成测试数据
    random_data = [random.randint(0, 1000) for _ in range(n)]
    
    # 使用列表推导式
    start_time = time.time()
    even_list = [x for x in random_data if x % 2 == 0]
    list_comp_time = time.time() - start_time
    list_comp_count = len(even_list)
    
    # 使用filter函数
    start_time = time.time()
    even_filter = list(filter(lambda x: x % 2 == 0, random_data))
    filter_time = time.time() - start_time
    filter_count = len(even_filter)
    
    # 使用itertools.filterfalse
    start_time = time.time()
    even_filterfalse = list(itertools.filterfalse(lambda x: x % 2 != 0, random_data))
    filterfalse_time = time.time() - start_time
    filterfalse_count = len(even_filterfalse)
    
    print(f"   列表推导式耗时: {list_comp_time:.6f} 秒, 结果数量: {list_comp_count:,}")
    print(f"   filter函数耗时: {filter_time:.6f} 秒, 结果数量: {filter_count:,}")
    print(f"   itertools.filterfalse耗时: {filterfalse_time:.6f} 秒, 结果数量: {filterfalse_count:,}")
    
    # 测试3: 生成笛卡尔积
    print("\n   测试3: 生成2个包含100个元素的列表的笛卡尔积:")
    
    # 生成测试数据
    list1 = list(range(100))
    list2 = list(range(100))
    
    # 使用列表推导式
    start_time = time.time()
    product_list_comp = [(x, y) for x in list1 for y in list2]
    list_comp_time = time.time() - start_time
    list_comp_count = len(product_list_comp)
    
    # 使用itertools.product
    start_time = time.time()
    product_itertools = list(itertools.product(list1, list2))
    itertools_time = time.time() - start_time
    itertools_count = len(product_itertools)
    
    print(f"   列表推导式耗时: {list_comp_time:.6f} 秒, 结果数量: {list_comp_count:,}")
    print(f"   itertools.product耗时: {itertools_time:.6f} 秒, 结果数量: {itertools_count:,}")
    print(f"   itertools.product比列表推导式快 {list_comp_time / itertools_time:.2f} 倍")
    
    print("\n4. 性能优化建议:")
    print("   - 对于大型数据集，优先使用迭代器而不是列表")
    print("   - 尽可能组合使用itertools函数，避免创建中间列表")
    print("   - 对于自定义迭代器，使用生成器函数（yield）而不是类实现")
    print("   - 在需要随机访问或多次迭代时，考虑将迭代器转换为列表")
    print("   - 对于简单操作，列表推导式可能比itertools更直观")
    print("   - 避免在循环内部使用复杂的lambda函数，这可能会降低性能")

itertools_performance_considerations()
print()

# 8. 注意事项和常见问题
print("=== 8. 注意事项和常见问题 ===")

def itertools_caveats():
    """itertools模块的注意事项和常见问题"""
    import itertools
    
    print("1. 迭代器只能迭代一次:")
    print("   - 迭代器一旦被消耗（迭代完成），就不能再次使用")
    print("   - 如果需要多次迭代同一数据集，应该将迭代器转换为列表或重新创建迭代器")
    
    # 示例：迭代器只能迭代一次
    print("   \n示例: 迭代器只能迭代一次:")
    # 创建一个迭代器
    iterator = itertools.count(1, 2)  # 生成1, 3, 5, ...
    
    # 第一次迭代
    first_five = list(itertools.islice(iterator, 5))
    print(f"   第一次迭代: {first_five}")
    
    # 第二次迭代（从上次停止的地方继续）
    next_five = list(itertools.islice(iterator, 5))
    print(f"   第二次迭代: {next_five}")
    
    # 解决方法：如果需要多次使用同一迭代器，应该将其转换为列表
    numbers = list(itertools.islice(itertools.count(1, 2), 10))  # 生成1, 3, ..., 19
    print(f"   \n将迭代器转换为列表后:")
    print(f"   第一次列表迭代: {numbers[:5]}")
    print(f"   第二次列表迭代: {numbers[5:10]}")
    
    print("\n2. 无限迭代器需要终止条件:")
    print("   - count(), cycle(), repeat()（不带times参数）生成无限迭代器")
    print("   - 在使用这些函数时，必须提供明确的终止条件")
    print("   - 通常使用islice()或takewhile()来限制迭代次数")
    
    # 示例：使用无限迭代器时必须提供终止条件
    print("   \n示例: 正确使用无限迭代器:")
    # 使用islice限制无限迭代器
    limited_count = list(itertools.islice(itertools.count(0, 0.5), 5))
    print(f"   使用islice限制count: {limited_count}")
    
    # 使用takewhile限制无限迭代器
    limited_cycle = list(itertools.takewhile(lambda x: x < 10, itertools.cycle([1, 3, 5])))
    print(f"   使用takewhile限制cycle: {limited_cycle}")
    
    print("\n3. groupby的排序要求:")
    print("   - groupby函数要求输入数据按分组键排序")
    print("   - 如果数据未排序，相同的键可能被分成多个组")
    
    # 示例：groupby需要排序的数据
    print("   \n示例: groupby对排序和未排序数据的处理:")
    # 未排序的数据
    unsorted_data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
    print(f"   未排序数据: {unsorted_data}")
    print("   分组结果:")
    for key, group in itertools.groupby(unsorted_data, key=lambda x: x[0]):
        print(f"     {key}: {list(group)}")
    
    # 排序后的数据
    sorted_data = sorted(unsorted_data, key=lambda x: x[0])
    print(f"   \n排序后数据: {sorted_data}")
    print("   分组结果:")
    for key, group in itertools.groupby(sorted_data, key=lambda x: x[0]):
        print(f"     {key}: {list(group)}")
    
    print("\n4. islice不支持负索引:")
    print("   - 与列表切片不同，islice不支持负的start、stop或step值")
    print("   - 如果需要负索引功能，可以先将迭代器转换为列表")
    
    # 示例：islice不支持负索引
    print("   \n示例: islice不支持负索引:")
    data = list(range(10))
    print(f"   原始数据: {data}")
    
    # 列表切片支持负索引
    list_slice = data[-5:-1]
    print(f"   列表切片 [-5:-1]: {list_slice}")
    
    # islice不支持负索引，需要转换为列表
    iterator_slice = list(data)[-5:-1]  # 先转换为列表再切片
    print(f"   迭代器处理方式: {iterator_slice}")
    
    print("\n5. starmap与map的区别:")
    print("   - starmap期望iterable中的每个元素都是一个元组，作为函数的参数")
    print("   - map将iterable中的每个元素作为函数的单个参数")
    print("   - 如果参数已经是元组形式，应该使用starmap而不是map")
    
    # 示例：starmap与map的区别
    print("   \n示例: starmap与map的区别:")
    # 定义一个接受两个参数的函数
    def add(a, b):
        return a + b
    
    # 参数已经是元组形式
    pairs = [(1, 2), (3, 4), (5, 6)]
    
    # 使用starmap
    starmap_result = list(itertools.starmap(add, pairs))
    print(f"   starmap结果: {starmap_result}")
    
    # 使用map需要额外的lambda函数
    map_result = list(map(lambda x: add(*x), pairs))
    print(f"   map结果: {map_result}")
    
    print("\n6. 迭代器的副作用:")
    print("   - 某些迭代器可能有副作用，特别是当它们基于有状态的函数或生成器时")
    print("   - 在多线程环境中使用迭代器需要额外的同步机制")
    
    print("\n7. 版本兼容性:")
    print("   - 大多数itertools函数在Python 2和Python 3中都可用")
    print("   - 但有一些函数是在特定版本中新增的，例如:")
    print("     * accumulate()函数在Python 3.2中新增")
    print("     * zip_longest()函数在Python 3中重命名自izip_longest()")
    print("     * initial参数在Python 3.8中添加到accumulate()")
    
    print("\n8. 调试困难:")
    print("   - 迭代器是惰性求值的，这可能使调试变得困难")
    print("   - 当遇到问题时，可以尝试将部分迭代器转换为列表以便调试")
    print("   - 使用itertools.islice()获取迭代器的前几个元素进行检查")

itertools_caveats()
print()

# 9. 输入输出示例
print("=== 9. 输入输出示例 ===")

def itertools_io_examples():
    """itertools模块的输入输出示例"""
    print("\n示例1: 无限迭代器的使用")
    print("输入:")
    print("    import itertools")
    print("    ")
    print("    # 使用count生成递增序列")
    print("    for i in itertools.islice(itertools.count(10, 2), 5):")
    print("        print(i)")
    print("    ")
    print("    # 使用cycle循环元素")
    print("    for i, item in enumerate(itertools.cycle(['A', 'B', 'C'])):")
    print("        print(item)")
    print("        if i >= 7:")
    print("            break")
    print("    ")
    print("    # 使用repeat重复元素")
    print("    print(list(itertools.repeat('Hello', 3)))")
    print("输出:")
    print("    10")
    print("    12")
    print("    14")
    print("    16")
    print("    18")
    print("    A")
    print("    B")
    print("    C")
    print("    A")
    print("    B")
    print("    C")
    print("    A")
    print("    B")
    print("    ['Hello', 'Hello', 'Hello']")
    
    print("\n示例2: 迭代器组合器的使用")
    print("输入:")
    print("    import itertools")
    print("    ")
    print("    # 使用accumulate计算累积和")
    print("    print(list(itertools.accumulate([1, 2, 3, 4, 5])))")
    print("    ")
    print("    # 使用chain连接多个迭代器")
    print("    print(list(itertools.chain([1, 2], [3, 4], [5])))")
    print("    ")
    print("    # 使用compress过滤元素")
    print("    print(list(itertools.compress([1, 2, 3, 4, 5], [True, False, True, False, True])))")
    print("    ")
    print("    # 使用takewhile和dropwhile")
    print("    data = [1, 2, 3, 4, 5, 4, 3, 2, 1]")
    print("    print(list(itertools.takewhile(lambda x: x < 5, data)))")
    print("    print(list(itertools.dropwhile(lambda x: x < 5, data)))")
    print("输出:")
    print("    [1, 3, 6, 10, 15]")
    print("    [1, 2, 3, 4, 5]")
    print("    [1, 3, 5]")
    print("    [1, 2, 3, 4]")
    print("    [5, 4, 3, 2, 1]")
    
    print("\n示例3: 组合生成器的使用")
    print("输入:")
    print("    import itertools")
    print("    ")
    print("    # 使用product生成笛卡尔积")
    print("    print(list(itertools.product(['A', 'B'], [1, 2])))")
    print("    ")
    print("    # 使用permutations生成排列")
    print("    print(list(itertools.permutations(['A', 'B', 'C'], 2)))")
    print("    ")
    print("    # 使用combinations生成组合")
    print("    print(list(itertools.combinations(['A', 'B', 'C'], 2)))")
    print("    ")
    print("    # 使用combinations_with_replacement生成允许重复的组合")
    print("    print(list(itertools.combinations_with_replacement(['A', 'B'], 2)))")
    print("输出:")
    print("    [('A', 1), ('A', 2), ('B', 1), ('B', 2)]")
    print("    [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]")
    print("    [('A', 'B'), ('A', 'C'), ('B', 'C')]")
    print("    [('A', 'A'), ('A', 'B'), ('B', 'B')]")
    
    print("\n示例4: 其他实用迭代器的使用")
    print("输入:")
    print("    import itertools")
    print("    ")
    print("    # 使用groupby分组")
    print("    data = sorted(['apple', 'ant', 'banana', 'bat', 'cat'], key=lambda x: x[0])")
    print("    for key, group in itertools.groupby(data, key=lambda x: x[0]):")
    print("        print(f'{key}: {list(group)}')")
    print("    ")
    print("    # 使用islice切片")
    print("    print(list(itertools.islice(range(10), 2, 8, 2)))")
    print("    ")
    print("    # 使用starmap")
    print("    print(list(itertools.starmap(pow, [(2, 3), (3, 2), (10, 3)])))")
    print("    ")
    print("    # 使用zip_longest")
    print("    print(list(itertools.zip_longest(['A', 'B', 'C'], [1, 2])))")
    print("输出:")
    print("    a: ['apple', 'ant']")
    print("    b: ['banana', 'bat']")
    print("    c: ['cat']")
    print("    [2, 4, 6]")
    print("    [8, 9, 1000]")
    print("    [('A', 1), ('B', 2), ('C', None)]")
    
    print("\n示例5: 组合使用多个itertools函数")
    print("输入:")
    print("    import itertools")
    print("    ")
    print("    # 生成从1到100的所有素数")
    print("    def primes_up_to(n):")
    print("        if n < 2:")
    print("            return []")
    print("        sieve = [True] * (n + 1)")
    print("        sieve[0] = sieve[1] = False")
    print("        for i in range(2, int(n**0.5) + 1):")
    print("            if sieve[i]:")
    print("                sieve[i*i : n+1 : i] = [False] * len(sieve[i*i : n+1 : i])")
    print("        return list(itertools.compress(range(n+1), sieve))")
    print("    ")
    print("    print(primes_up_to(20))")
    print("    ")
    print("    # 生成斐波那契数列的前10个数")
    print("    def fibonacci():")
    print("        a, b = 0, 1")
    print("        while True:")
    print("            yield a")
    print("            a, b = b, a + b")
    print("    ")
    print("    print(list(itertools.islice(fibonacci(), 10)))")
    print("输出:")
    print("    [2, 3, 5, 7, 11, 13, 17, 19]")
    print("    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]")

itertools_io_examples()
print()

# 10. 总结和完整导入指南
print("=== 10. 总结和完整导入指南 ===")

def itertools_summary():
    """itertools模块总结和导入指南"""
    print("itertools模块提供了用于高效循环迭代的函数，这些函数创建迭代器以支持内存高效的循环。\n")
    
    # 主要功能类别
    print("主要功能类别:")
    print("1. 无限迭代器:")
    print("   - count(start=0, step=1): 从start开始，以step为步长无限递增")
    print("   - cycle(iterable): 无限循环迭代iterable中的元素")
    print("   - repeat(object, times=None): 重复object指定次数或无限次")
    
    print("\n2. 迭代器组合器:")
    print("   - accumulate(iterable, func=None, *, initial=None): 计算累积结果")
    print("   - chain(*iterables): 连接多个迭代器")
    print("   - chain.from_iterable(iterable): 从一个可迭代对象中提取并连接子迭代器")
    print("   - compress(data, selectors): 根据selectors过滤data中的元素")
    print("   - dropwhile(predicate, iterable): 丢弃predicate为True的元素直到第一个False")
    print("   - takewhile(predicate, iterable): 获取元素直到predicate为False")
    print("   - filterfalse(predicate, iterable): 获取predicate为False的元素")
    print("   - zip_longest(*iterables, fillvalue=None): 类似于zip，但会填充较短的迭代器")
    
    print("\n3. 组合生成器:")
    print("   - product(*iterables, repeat=1): 生成笛卡尔积")
    print("   - permutations(iterable, r=None): 生成排列")
    print("   - combinations(iterable, r): 生成组合（不允许重复）")
    print("   - combinations_with_replacement(iterable, r): 生成组合（允许重复）")
    
    print("\n4. 其他实用迭代器:")
    print("   - groupby(iterable, key=None): 根据key函数分组")
    print("   - islice(iterable, start, stop=None, step=None): 切片迭代器")
    print("   - starmap(function, iterable): 对元组参数调用函数")
    
    # 完整导入指南
    print("\n完整导入指南:")
    print("1. 基本导入方法:")
    print("   import itertools")
    print("   ")
    print("   然后通过模块名访问函数:")
    print("   result = list(itertools.product(['A', 'B'], [1, 2]))")
    
    print("\n2. 导入特定函数:")
    print("   from itertools import product, permutations, combinations")
    print("   ")
    print("   直接使用导入的函数:")
    print("   result = list(product(['A', 'B'], [1, 2]))")
    
    print("\n3. 导入所有函数:")
    print("   from itertools import *")
    print("   ")
    print("   注意: 虽然方便，但可能导致命名冲突，不推荐在大型项目中使用")
    
    print("\n4. 常用导入组合:")
    print("   # 导入无限迭代器")
    print("   from itertools import count, cycle, repeat")
    print("   ")
    print("   # 导入组合生成器")
    print("   from itertools import product, permutations, combinations, combinations_with_replacement")
    print("   ")
    print("   # 导入实用迭代器")
    print("   from itertools import groupby, islice, starmap, zip_longest")
    
    # 版本兼容性信息
    print("\n版本兼容性信息:")
    print("- itertools模块在Python 2和Python 3中都可用")
    print("- 重要版本差异:")
    print("  * accumulate()函数在Python 3.2中新增")
    print("  * zip_longest()在Python 3中重命名自izip_longest()")
    print("  * combinations_with_replacement()在Python 2.7中新增")
    print("  * initial参数在Python 3.8中添加到accumulate()")
    
    print("\n最佳实践:")
    print("1. 优先使用迭代器而不是列表，特别是处理大型数据集时")
    print("2. 对于无限迭代器，始终提供明确的终止条件")
    print("3. 在使用groupby前对数据进行排序")
    print("4. 组合使用多个itertools函数可以创建强大的数据处理流水线")
    print("5. 如果需要多次迭代，考虑将迭代器转换为列表")
    print("6. 使用生成器表达式与itertools函数配合使用，提高代码可读性")

itertools_summary()
print()

# 11. 运行总结
print("=== 11. 运行总结 ===")
print("本脚本演示了Python itertools模块的所有主要功能，包括:")
print("1. 无限迭代器 (count, cycle, repeat)")
print("2. 迭代器组合器 (accumulate, chain, compress, takewhile, dropwhile等)")
print("3. 组合生成器 (product, permutations, combinations等)")
print("4. 其他实用迭代器 (groupby, islice, starmap, zip_longest等)")
print()
print("itertools模块提供了高效且内存友好的工具，特别适合:")
print("- 处理大型数据集")
print("- 创建自定义迭代器和生成器")
print("- 实现复杂的组合和排列操作")
print("- 构建数据处理流水线")
print()
print("通过合理使用这些工具，可以显著提高Python代码的性能和可读性。")
print("记住，迭代器只能迭代一次，且对于无限迭代器，必须提供明确的终止条件。")