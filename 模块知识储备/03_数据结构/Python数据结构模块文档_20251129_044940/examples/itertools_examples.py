#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
itertools模块示例代码集合

本文件演示了Python itertools模块的各种实用功能，
包括无限迭代器、组合迭代器和终止迭代器的使用方法。

作者: Python数据结构教程
日期: 2023-11-28
"""

import itertools
import time
from pprint import pprint


def example_count():
    """示例1: count() 无限计数器的使用"""
    print("=== 示例1: count() 无限计数器 ===")
    print("生成从10开始，步长为2的序列（前5个）:")
    
    # 限制数量，避免无限循环
    for i in itertools.count(10, 2):
        if i > 20:
            break
        print(i, end=" ")
    print()
    
    # 与zip结合为列表添加索引
    fruits = ['apple', 'banana', 'cherry', 'date']
    print("\n为水果列表添加索引:")
    indexed_fruits = list(zip(itertools.count(1), fruits))
    print(indexed_fruits)
    print()


def example_cycle():
    """示例2: cycle() 无限循环迭代器"""
    print("=== 示例2: cycle() 无限循环迭代器 ===")
    
    # 轮询任务分配模拟
    servers = ['server1', 'server2', 'server3']
    tasks = ['task1', 'task2', 'task3', 'task4', 'task5']
    
    print("任务轮询分配:")
    server_cycle = itertools.cycle(servers)
    
    for task in tasks:
        server = next(server_cycle)
        print(f"  分配 {task} 到 {server}")
    print()


def example_repeat():
    """示例3: repeat() 重复迭代器"""
    print("=== 示例3: repeat() 重复迭代器 ===")
    
    # 重复单个值
    print("重复'Hello' 3次:")
    repeated = list(itertools.repeat('Hello', 3))
    print(repeated)
    
    # 与map结合使用
    print("\n计算多个数的平方:")
    numbers = [1, 2, 3, 4]
    squares = list(map(pow, numbers, itertools.repeat(2)))
    print(f"平方结果: {squares}")
    print()


def example_accumulate():
    """示例4: accumulate() 累积迭代器"""
    print("=== 示例4: accumulate() 累积迭代器 ===")
    
    # 默认累加
    numbers = [1, 2, 3, 4, 5]
    cumulative_sum = list(itertools.accumulate(numbers))
    print(f"累加结果: {cumulative_sum}")
    
    # 使用乘法
    import operator
    cumulative_product = list(itertools.accumulate(numbers, operator.mul))
    print(f"累乘结果: {cumulative_product}")
    
    # 自定义函数（最大值）
    max_so_far = list(itertools.accumulate([3, 1, 4, 1, 5, 9], max))
    print(f"累积最大值: {max_so_far}")
    print()


def example_chain():
    """示例5: chain() 链接多个迭代器"""
    print("=== 示例5: chain() 链接多个迭代器 ===")
    
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    tuple1 = (4, 5, 6)
    
    # 链接多个序列
    chained = list(itertools.chain(list1, list2, tuple1))
    print(f"链接结果: {chained}")
    
    # 链接嵌套列表
    nested_lists = [[1, 2], [3, 4], [5, 6]]
    flattened = list(itertools.chain.from_iterable(nested_lists))
    print(f"扁平化嵌套列表: {flattened}")
    print()


def example_combinatorics():
    """示例6: 组合数学相关函数"""
    print("=== 示例6: 组合数学相关函数 ===")
    
    items = ['A', 'B', 'C', 'D']
    
    # permutations: 排列（考虑顺序）
    permutations_2 = list(itertools.permutations(items, 2))
    print(f"从{item_count}个元素中取2个的排列数: {len(permutations_2)}")
    print(f"前5个排列: {permutations_2[:5]}")
    
    # combinations: 组合（不考虑顺序）
    combinations_2 = list(itertools.combinations(items, 2))
    print(f"从{item_count}个元素中取2个的组合数: {len(combinations_2)}")
    print(f"所有组合: {combinations_2}")
    
    # combinations_with_replacement: 允许重复的组合
    combinations_with_rep = list(itertools.combinations_with_replacement(items, 2))
    print(f"从{item_count}个元素中取2个的允许重复组合数: {len(combinations_with_rep)}")
    print(f"所有允许重复的组合: {combinations_with_rep}")
    print()


def example_product():
    """示例7: product() 笛卡尔积"""
    print("=== 示例7: product() 笛卡尔积 ===")
    
    # 简单的笛卡尔积
    colors = ['红', '绿', '蓝']
    sizes = ['S', 'M', 'L']
    
    print("颜色和尺寸的笛卡尔积:")
    products = list(itertools.product(colors, sizes))
    for item in products:
        print(f"  {item}")
    
    # 带重复的笛卡尔积
    digits = ['0', '1']
    binary_numbers = list(itertools.product(digits, repeat=3))
    print(f"\n3位二进制数的所有可能: {len(binary_numbers)}")
    print(f"前5个: {binary_numbers[:5]}")
    print()


def example_filtering():
    """示例8: 过滤迭代器"""
    print("=== 示例8: 过滤迭代器 ===")
    
    numbers = range(1, 11)
    
    # filterfalse: 过滤掉满足条件的元素（与filter相反）
    odd_numbers = list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))
    print(f"奇数: {odd_numbers}")
    
    # takewhile: 只要条件满足就返回元素
    takewhile_result = list(itertools.takewhile(lambda x: x < 6, numbers))
    print(f"小于6的数: {takewhile_result}")
    
    # dropwhile: 直到条件满足才开始返回元素
    dropwhile_result = list(itertools.dropwhile(lambda x: x < 6, numbers))
    print(f"从6开始的数: {dropwhile_result}")
    
    # compress: 根据选择器压缩数据
    data = ['A', 'B', 'C', 'D', 'E']
    selectors = [True, False, True, False, True]
    compressed = list(itertools.compress(data, selectors))
    print(f"根据选择器筛选: {compressed}")
    print()


def example_groupby():
    """示例9: groupby() 分组迭代器"""
    print("=== 示例9: groupby() 分组迭代器 ===")
    
    # 分组前需要排序相同的键
    people = [
        {'name': 'Alice', 'department': 'HR'},
        {'name': 'Bob', 'department': 'Engineering'},
        {'name': 'Charlie', 'department': 'HR'},
        {'name': 'David', 'department': 'Engineering'},
        {'name': 'Eve', 'department': 'Marketing'}
    ]
    
    # 按部门分组
    people.sort(key=lambda x: x['department'])  # 必须先排序
    
    print("按部门分组的员工:")
    for department, group in itertools.groupby(people, key=lambda x: x['department']):
        print(f"  {department}:")
        for person in group:
            print(f"    - {person['name']}")
    print()


def example_practical_applications():
    """示例10: 实际应用场景"""
    print("=== 示例10: 实际应用场景 ===")
    
    # 应用1: 生成所有可能的密码组合（仅用于教育目的）
    print("1. 生成简单密码组合:")
    characters = 'abc123'
    # 只生成少量示例
    for length in range(1, 4):
        print(f"  {length}位密码示例:")
        # 限制只显示前5个
        examples = list(itertools.islice(itertools.product(characters, repeat=length), 5))
        for combo in examples:
            print(f"    {''.join(combo)}")
    
    # 应用2: 滑动窗口计算
    print("\n2. 滑动窗口平均值计算:")
    data = [1, 2, 3, 4, 5, 6, 7]
    window_size = 3
    
    # 创建滑动窗口
    windows = zip(*(itertools.islice(data, i, None) for i in range(window_size)))
    
    for i, window in enumerate(windows):
        avg = sum(window) / window_size
        print(f"  窗口 {i+1}: {window}, 平均值: {avg:.2f}")
    
    # 应用3: 处理大量数据时的内存优化
    print("\n3. 内存优化的文件处理:")
    # 这里模拟大文件处理
    def process_large_file(file_lines):
        # 使用迭代器逐行处理，而不是一次性加载全部内容
        for line in file_lines:
            # 模拟处理
            if 'error' in line.lower():
                yield f"错误行: {line.strip()}"
    
    # 模拟文件行
    mock_file = [f"这是第{i}行数据" for i in range(100)]
    mock_file[42] = "这里包含 ERROR 信息"
    mock_file[88] = "另一个 Error 示例"
    
    # 使用islice限制输出
    errors = list(itertools.islice(process_large_file(mock_file), 10))
    for error in errors:
        print(error)


def benchmark_itertools():
    """性能基准测试"""
    print("\n=== 性能基准测试 ===")
    
    # 测试数据
    n = 1000000
    
    # 测试1: 列表推导式 vs itertools.chain
    print("测试1: 连接多个列表")
    
    # 创建测试数据
    lists = [[i] for i in range(1000)]  # 1000个单元素列表
    
    # 方法1: 列表推导式
    start = time.time()
    result1 = [item for sublist in lists for item in sublist]
    list_time = time.time() - start
    print(f"  列表推导式: {list_time:.6f}秒")
    
    # 方法2: itertools.chain.from_iterable
    start = time.time()
    result2 = list(itertools.chain.from_iterable(lists))
    chain_time = time.time() - start
    print(f"  itertools.chain: {chain_time:.6f}秒")
    print(f"  性能提升: {list_time / chain_time:.2f}倍")
    
    # 测试2: 内存使用比较
    print("\n测试2: 内存使用比较")
    import sys
    
    # 生成器表达式
    gen_expr = (x*x for x in range(n))
    print(f"  生成器表达式内存占用: {sys.getsizeof(gen_expr)} 字节")
    
    # 列表推导式
    list_expr = [x*x for x in range(n)]
    print(f"  列表推导式内存占用: {sys.getsizeof(list_expr) / 1024 / 1024:.2f} MB")
    
    # 释放内存
    del list_expr


if __name__ == "__main__":
    print("Python itertools 模块示例代码\n")
    
    # 运行所有示例
    example_count()
    example_cycle()
    example_repeat()
    example_accumulate()
    example_chain()
    
    # 定义变量用于后续示例
    items = ['A', 'B', 'C', 'D']
    item_count = len(items)
    
    example_combinatorics()
    example_product()
    example_filtering()
    example_groupby()
    example_practical_applications()
    
    # 性能测试（可选）
    # benchmark_itertools()
    
    print("\n所有示例执行完成！")
