#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
operator模块示例代码集合

本文件演示了Python operator模块的各种实用功能，
包括算术运算、比较运算、逻辑运算以及序列操作等。

作者: Python数据结构教程
日期: 2023-11-28
"""

import operator
import functools
from pprint import pprint


def example_arithmetic_operators():
    """示例1: 算术运算符"""
    print("=== 示例1: 算术运算符 ===")
    
    a, b = 10, 5
    
    # 基本算术运算
    print(f"a = {a}, b = {b}")
    print(f"加法: operator.add(a, b) = {operator.add(a, b)}")
    print(f"减法: operator.sub(a, b) = {operator.sub(a, b)}")
    print(f"乘法: operator.mul(a, b) = {operator.mul(a, b)}")
    print(f"除法: operator.truediv(a, b) = {operator.truediv(a, b)}")
    print(f"整除: operator.floordiv(a, b) = {operator.floordiv(a, b)}")
    print(f"取余: operator.mod(a, b) = {operator.mod(a, b)}")
    print(f"幂运算: operator.pow(a, b) = {operator.pow(a, b)}")
    
    # 赋值运算符
    a = 10
    print(f"\n初始 a = {a}")
    a = operator.iadd(a, 5)  # a += 5
    print(f"a += 5 后: {a}")
    a = operator.imul(a, 2)  # a *= 2
    print(f"a *= 2 后: {a}")
    print()


def example_comparison_operators():
    """示例2: 比较运算符"""
    print("=== 示例2: 比较运算符 ===")
    
    x, y = 10, 20
    
    print(f"x = {x}, y = {y}")
    print(f"小于: operator.lt(x, y) = {operator.lt(x, y)}")
    print(f"小于等于: operator.le(x, y) = {operator.le(x, y)}")
    print(f"等于: operator.eq(x, y) = {operator.eq(x, y)}")
    print(f"不等于: operator.ne(x, y) = {operator.ne(x, y)}")
    print(f"大于: operator.gt(x, y) = {operator.gt(x, y)}")
    print(f"大于等于: operator.ge(x, y) = {operator.ge(x, y)}")
    
    # 应用: 自定义排序
    print("\n自定义排序示例:")
    people = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35},
        {'name': 'David', 'age': 25}
    ]
    
    # 按年龄升序排序
    people_sorted = sorted(people, key=lambda p: p['age'])
    print("按年龄升序排序:")
    for person in people_sorted:
        print(f"  {person['name']}: {person['age']}")
    print()


def example_itemgetter():
    """示例3: itemgetter - 获取元素"""
    print("=== 示例3: itemgetter - 获取元素 ===")
    
    # 基本用法
    data = [
        ('Alice', 30, 'HR'),
        ('Bob', 25, 'Engineering'),
        ('Charlie', 35, 'Marketing')
    ]
    
    # 获取第二个元素（索引1）
    get_age = operator.itemgetter(1)
    print("获取每个人的年龄:")
    for person in data:
        print(f"  {person[0]}: {get_age(person)}")
    
    # 获取多个元素
    get_name_and_department = operator.itemgetter(0, 2)
    print("\n获取每个人的姓名和部门:")
    for person in data:
        name, dept = get_name_and_department(person)
        print(f"  {name}: {dept}")
    
    # 用于排序
    print("\n按年龄排序:")
    sorted_by_age = sorted(data, key=operator.itemgetter(1))
    for person in sorted_by_age:
        print(f"  {person}")
    
    # 字典排序
    print("\n字典排序示例:")
    people = [
        {'name': 'Alice', 'salary': 50000, 'department': 'HR'},
        {'name': 'Bob', 'salary': 80000, 'department': 'Engineering'},
        {'name': 'Charlie', 'salary': 55000, 'department': 'HR'}
    ]
    
    # 多级排序：先按部门，再按薪资降序
    sorted_people = sorted(
        people, 
        key=lambda p: (p['department'], -p['salary'])
    )
    print("按部门和薪资排序:")
    for person in sorted_people:
        print(f"  {person['department']}: {person['name']} - ${person['salary']}")
    print()


def example_attrgetter():
    """示例4: attrgetter - 获取属性"""
    print("=== 示例4: attrgetter - 获取属性 ===")
    
    # 定义一个简单的类
    class Product:
        def __init__(self, name, price, category):
            self.name = name
            self.price = price
            self.category = category
        
        def __repr__(self):
            return f"Product({self.name}, ${self.price:.2f})"
    
    # 创建产品实例
    products = [
        Product('Laptop', 999.99, 'Electronics'),
        Product('Phone', 499.99, 'Electronics'),
        Product('Desk', 199.99, 'Furniture'),
        Product('Chair', 89.99, 'Furniture')
    ]
    
    # 获取单个属性
    get_price = operator.attrgetter('price')
    print("所有产品价格:")
    for product in products:
        print(f"  {product.name}: ${get_price(product):.2f}")
    
    # 获取多个属性
    get_name_and_category = operator.attrgetter('name', 'category')
    print("\n所有产品名称和类别:")
    for product in products:
        name, category = get_name_and_category(product)
        print(f"  {name}: {category}")
    
    # 用于排序
    print("\n按类别和价格排序:")
    sorted_products = sorted(products, key=operator.attrgetter('category', 'price'))
    for product in sorted_products:
        print(f"  {product.category}: {product}")
    print()


def example_methodcaller():
    """示例5: methodcaller - 调用方法"""
    print("=== 示例5: methodcaller - 调用方法 ===")
    
    # 基本用法
    strings = ['hello', 'WORLD', 'Python', 'EXAMPLE']
    
    # 调用upper()方法
    to_upper = operator.methodcaller('upper')
    upper_strings = list(map(to_upper, strings))
    print(f"大写转换: {upper_strings}")
    
    # 调用replace()方法，带参数
    replace_hello = operator.methodcaller('replace', 'hello', 'hi')
    replaced = replace_hello('hello world')
    print(f"替换 'hello' 为 'hi': {replaced}")
    
    # 调用split()方法
    split_by_comma = operator.methodcaller('split', ',')
    data = ['a,b,c', '1,2,3', 'x,y,z']
    split_data = list(map(split_by_comma, data))
    print(f"按逗号分割: {split_data}")
    print()


def example_functional_programming():
    """示例6: 函数式编程应用"""
    print("=== 示例6: 函数式编程应用 ===")
    
    # 使用operator与functools.reduce
    numbers = [1, 2, 3, 4, 5]
    
    # 计算总和
    total = functools.reduce(operator.add, numbers)
    print(f"总和: {total}")
    
    # 计算乘积
    product = functools.reduce(operator.mul, numbers)
    print(f"乘积: {product}")
    
    # 计算最大值（使用初始值）
    max_value = functools.reduce(
        lambda a, b: a if a > b else b, 
        numbers, 
        float('-inf')
    )
    print(f"最大值: {max_value}")
    
    # 使用operator代替lambda
    max_value_op = functools.reduce(
        lambda a, b: a if operator.gt(a, b) else b, 
        numbers, 
        float('-inf')
    )
    print(f"使用operator.gt的最大值: {max_value_op}")
    
    # 更简洁的方式
    max_value_direct = max(numbers)
    print(f"直接使用max: {max_value_direct}")
    print()


def example_dynamic_operations():
    """示例7: 动态操作选择"""
    print("=== 示例7: 动态操作选择 ===")
    
    # 创建操作符映射
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '//': operator.floordiv,
        '%': operator.mod,
        '**': operator.pow
    }
    
    # 动态计算器
    def calculate(a, b, op_symbol):
        if op_symbol in operations:
            return operations[op_symbol](a, b)
        else:
            raise ValueError(f"不支持的操作符: {op_symbol}")
    
    # 测试
    a, b = 20, 5
    print(f"a = {a}, b = {b}")
    
    for op in ['+', '-', '*', '/', '//', '%', '**']:
        try:
            result = calculate(a, b, op)
            print(f"{a} {op} {b} = {result}")
        except ValueError as e:
            print(e)
    
    # 比较操作符映射
    compare_ops = {
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>': operator.gt,
        '>=': operator.ge
    }
    
    print("\n比较操作:")
    for op in ['<', '<=', '==', '!=', '>', '>=']:
        result = compare_ops[op](a, b)
        print(f"{a} {op} {b} = {result}")
    print()


def example_sequence_operations():
    """示例8: 序列操作符"""
    print("=== 示例8: 序列操作符 ===")
    
    # 索引和切片
    seq = [10, 20, 30, 40, 50]
    
    # 获取单个元素
    print(f"序列: {seq}")
    print(f"索引2的元素: {operator.getitem(seq, 2)}")
    print(f"倒数第一个元素: {operator.getitem(seq, -1)}")
    
    # 设置元素
    seq_copy = seq.copy()
    operator.setitem(seq_copy, 1, 200)
    print(f"设置索引1后的序列: {seq_copy}")
    
    # 删除元素
    operator.delitem(seq_copy, 3)
    print(f"删除索引3后的序列: {seq_copy}")
    
    # 切片
    print(f"切片 [1:4]: {operator.getitem(seq, slice(1, 4))}")
    print(f"切片 [::2]: {operator.getitem(seq, slice(None, None, 2))}")
    
    # 连接序列
    seq1 = [1, 2, 3]
    seq2 = [4, 5, 6]
    concatenated = operator.concat(seq1, seq2)
    print(f"连接 {seq1} 和 {seq2}: {concatenated}")
    
    # 包含检查
    print(f"30 在 {seq} 中: {operator.contains(seq, 30)}")
    print(f"300 在 {seq} 中: {operator.contains(seq, 300)}")
    print()


def example_practical_applications():
    """示例9: 实际应用场景"""
    print("=== 示例9: 实际应用场景 ===")
    
    # 应用1: 数据转换流水线
    print("1. 数据转换流水线:")
    
    # 定义数据处理函数
    def process_data(raw_data):
        # 步骤1: 转换为浮点数
        to_float = lambda x: list(map(float, x))
        # 步骤2: 计算平均值
        avg = lambda x: sum(x) / len(x) if x else 0
        # 步骤3: 四舍五入到2位小数
        round_2 = lambda x: round(x, 2)
        
        # 构建处理流水线
        pipeline = [to_float, avg, round_2]
        
        # 执行流水线
        result = raw_data
        for func in pipeline:
            result = func(result)
        
        return result
    
    # 测试数据
    test_data = [['10.5', '12.3', '15.8'], ['5.2', '6.7', '8.9']]
    
    for i, data in enumerate(test_data):
        result = process_data(data)
        print(f"  数据集 {i+1}: {data} -> 平均值 = {result}")
    
    # 应用2: 动态排序系统
    print("\n2. 动态排序系统:")
    
    employees = [
        {'id': 1, 'name': 'Alice', 'age': 30, 'salary': 50000},
        {'id': 2, 'name': 'Bob', 'age': 25, 'salary': 80000},
        {'id': 3, 'name': 'Charlie', 'age': 35, 'salary': 55000},
        {'id': 4, 'name': 'David', 'age': 40, 'salary': 75000}
    ]
    
    # 定义排序字段映射
    sort_fields = {
        'name': operator.itemgetter('name'),
        'age': operator.itemgetter('age'),
        'salary': operator.itemgetter('salary')
    }
    
    # 动态排序函数
    def sort_employees(field, reverse=False):
        if field in sort_fields:
            return sorted(employees, key=sort_fields[field], reverse=reverse)
        else:
            raise ValueError(f"不支持的排序字段: {field}")
    
    # 测试不同排序方式
    for field in ['name', 'age', 'salary']:
        print(f"\n按{field}升序排序:")
        sorted_emp = sort_employees(field)
        for emp in sorted_emp:
            print(f"  {emp['name']}: {emp[field]}")
    
    # 按薪资降序
    print("\n按薪资降序排序:")
    sorted_by_salary_desc = sort_employees('salary', reverse=True)
    for emp in sorted_by_salary_desc:
        print(f"  {emp['name']}: ${emp['salary']}")


def example_performance_comparison():
    """示例10: 性能比较"""
    print("\n=== 示例10: 性能比较 ===")
    
    import time
    
    # 测试数据
    data = list(range(1000000))
    
    # 测试1: lambda vs operator
    print("测试1: lambda vs operator.add")
    
    # 使用lambda
    start = time.time()
    sum_lambda = functools.reduce(lambda a, b: a + b, data)
    lambda_time = time.time() - start
    print(f"  lambda: {lambda_time:.6f}秒, 结果: {sum_lambda}")
    
    # 使用operator.add
    start = time.time()
    sum_operator = functools.reduce(operator.add, data)
    operator_time = time.time() - start
    print(f"  operator.add: {operator_time:.6f}秒, 结果: {sum_operator}")
    print(f"  性能提升: {lambda_time / operator_time:.2f}倍")
    
    # 测试2: 自定义getter vs itemgetter
    print("\n测试2: 自定义getter vs itemgetter")
    
    # 创建测试数据
    test_list = [{'value': i} for i in range(1000000)]
    
    # 自定义lambda
    start = time.time()
    values_lambda = list(map(lambda x: x['value'], test_list))
    lambda_time = time.time() - start
    print(f"  lambda: {lambda_time:.6f}秒")
    
    # 使用itemgetter
    start = time.time()
    get_value = operator.itemgetter('value')
    values_itemgetter = list(map(get_value, test_list))
    itemgetter_time = time.time() - start
    print(f"  itemgetter: {itemgetter_time:.6f}秒")
    print(f"  性能提升: {lambda_time / itemgetter_time:.2f}倍")


if __name__ == "__main__":
    print("Python operator 模块示例代码\n")
    
    # 运行所有示例
    example_arithmetic_operators()
    example_comparison_operators()
    example_itemgetter()
    example_attrgetter()
    example_methodcaller()
    example_functional_programming()
    example_dynamic_operations()
    example_sequence_operations()
    example_practical_applications()
    
    # 性能测试（可选）
    # example_performance_comparison()
    
    print("\n所有示例执行完成！")
