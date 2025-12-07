# Python函数式编程详细指南

## 一、模块概述

函数式编程是一种编程范式，它将计算视为数学函数的求值，并避免使用可变状态和可变数据。Python虽然不是纯函数式编程语言，但它支持许多函数式编程的特性，如高阶函数、匿名函数、闭包、装饰器等。本指南将详细介绍Python中的函数式编程概念、API和最佳实践。

## 二、基本概念

1. **函数式编程（Functional Programming）**：一种编程范式，强调使用纯函数、不可变数据和避免副作用
2. **纯函数（Pure Function）**：给定相同的输入，总是返回相同的输出，且没有副作用的函数
3. **不可变数据（Immutable Data）**：创建后不能修改的数据结构
4. **高阶函数（Higher-Order Function）**：接受函数作为参数或返回函数作为结果的函数
5. **匿名函数（Anonymous Function）**：没有名称的函数，通常用于一次性操作
6. **闭包（Closure）**：可以访问其词法作用域之外的变量的函数
7. **柯里化（Currying）**：将接受多个参数的函数转换为接受一个参数并返回接受剩余参数的函数的过程
8. **递归（Recursion）**：函数调用自身的过程
9. **列表推导式（List Comprehension）**：一种创建列表的简洁方式，类似于函数式编程中的map和filter

## 三、函数式编程基础

### 1. 纯函数

```python
# 纯函数示例
def add(a, b):
    """纯函数：加法"""
    return a + b

def multiply(a, b):
    """纯函数：乘法"""
    return a * b

def square(x):
    """纯函数：平方"""
    return x * x

def factorial(n):
    """纯函数：阶乘（递归实现）"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

# 非纯函数示例
counter = 0
def increment():
    """非纯函数：修改全局变量"""
    global counter
    counter += 1
    return counter

def get_current_time():
    """非纯函数：依赖外部状态"""
    import time
    return time.time()

def print_message(message):
    """非纯函数：产生副作用（打印）"""
    print(message)
    return message

# 测试纯函数
print("纯函数测试:")
print(f"add(2, 3): {add(2, 3)}")
print(f"multiply(2, 3): {multiply(2, 3)}")
print(f"square(5): {square(5)}")
print(f"factorial(5): {factorial(5)}")

# 测试非纯函数
print("\n非纯函数测试:")
print(f"increment(): {increment()}")
print(f"increment(): {increment()}")
print(f"get_current_time(): {get_current_time()}")
print(f"print_message('Hello'): {print_message('Hello')}")
```

输出结果：
```
纯函数测试:
add(2, 3): 5
multiply(2, 3): 6
square(5): 25
factorial(5): 120

非纯函数测试:
increment(): 1
increment(): 2
get_current_time(): 1685234567.890123
Hello
print_message('Hello'): Hello
```

### 2. 不可变数据

```python
# 不可变数据示例

# 字符串是不可变的
string = "hello"
print(f"原始字符串: {string}")
# 不能直接修改字符串的字符
# string[0] = 'H'  # 会引发TypeError
# 创建新字符串
new_string = string.capitalize()
print(f"新字符串: {new_string}")
print(f"原始字符串不变: {string}")

# 元组是不可变的
tuple_data = (1, 2, 3, 4, 5)
print(f"\n原始元组: {tuple_data}")
# 不能直接修改元组元素
# tuple_data[0] = 10  # 会引发TypeError
# 创建新元组
new_tuple = tuple_data + (6, 7)
print(f"新元组: {new_tuple}")
print(f"原始元组不变: {tuple_data}")

# 列表是可变的
list_data = [1, 2, 3, 4, 5]
print(f"\n原始列表: {list_data}")
# 可以直接修改列表元素
list_data[0] = 10
list_data.append(6)
print(f"修改后的列表: {list_data}")

# 冻结集合（frozenset）是不可变的
frozen_set = frozenset([1, 2, 3, 4, 5])
print(f"\n冻结集合: {frozen_set}")
# 不能添加或删除元素
# frozen_set.add(6)  # 会引发AttributeError
# 创建新的冻结集合
new_frozen_set = frozen_set.union({6, 7})
print(f"新冻结集合: {new_frozen_set}")
print(f"原始冻结集合不变: {frozen_set}")

# 使用不可变数据的优势
# 1. 线程安全：不需要锁来保护不可变数据
# 2. 可预测性：数据不会被意外修改
# 3. 更安全的并行编程：避免数据竞争
# 4. 更容易推理代码：减少状态变化
```

输出结果：
```
原始字符串: hello
新字符串: Hello
原始字符串不变: hello

原始元组: (1, 2, 3, 4, 5)
新元组: (1, 2, 3, 4, 5, 6, 7)
原始元组不变: (1, 2, 3, 4, 5)

原始列表: [1, 2, 3, 4, 5]
修改后的列表: [10, 2, 3, 4, 5, 6]

冻结集合: frozenset({1, 2, 3, 4, 5})
新冻结集合: frozenset({1, 2, 3, 4, 5, 6, 7})
原始冻结集合不变: frozenset({1, 2, 3, 4, 5})
```

### 3. 高阶函数

```python
# 高阶函数示例

# map函数：将函数应用于序列中的每个元素
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(f"map(square, {numbers}): {squared_numbers}")

# filter函数：过滤序列中的元素
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(f"filter(is_even, {numbers}): {even_numbers}")

# reduce函数：将序列中的元素合并为一个值
from functools import reduce

def add(a, b):
    return a + b

sum_numbers = reduce(add, numbers)
print(f"reduce(add, {numbers}): {sum_numbers}")

# sorted函数：排序，可以接受自定义比较函数
words = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_by_length = sorted(words, key=len)
print(f"sorted({words}, key=len): {sorted_by_length}")

# 接受函数作为参数的自定义高阶函数
def apply_operation(func, x, y):
    """将函数应用于两个参数"""
    return func(x, y)

result_add = apply_operation(add, 5, 3)
result_multiply = apply_operation(lambda a, b: a * b, 5, 3)
print(f"\napply_operation(add, 5, 3): {result_add}")
print(f"apply_operation(lambda a, b: a * b, 5, 3): {result_multiply}")

# 返回函数的高阶函数
def create_adder(n):
    """创建一个加法函数"""
    def adder(x):
        return x + n
    return adder

add_5 = create_adder(5)
add_10 = create_adder(10)
print(f"\nadd_5(3): {add_5(3)}")
print(f"add_10(3): {add_10(3)}")
```

输出结果：
```
map(square, [1, 2, 3, 4, 5]): [1, 4, 9, 16, 25]
filter(is_even, [1, 2, 3, 4, 5]): [2, 4]
reduce(add, [1, 2, 3, 4, 5]): 15
sorted(['apple', 'banana', 'cherry', 'date', 'elderberry'], key=len): ['date', 'apple', 'banana', 'cherry', 'elderberry']

apply_operation(add, 5, 3): 8
apply_operation(lambda a, b: a * b, 5, 3): 15

add_5(3): 8
add_10(3): 13
```

### 4. 匿名函数

```python
# 匿名函数示例

# 使用lambda定义匿名函数
square = lambda x: x * x
double = lambda x: x * 2
sum_two = lambda a, b: a + b

print(f"lambda x: x * x (5): {square(5)}")
print(f"lambda x: x * 2 (5): {double(5)}")
print(f"lambda a, b: a + b (3, 4): {sum_two(3, 4)}")

# 与高阶函数一起使用
numbers = [1, 2, 3, 4, 5]

# 使用lambda作为map的参数
squared = list(map(lambda x: x * x, numbers))
print(f"\nmap(lambda x: x * x, {numbers}): {squared}")

# 使用lambda作为filter的参数
even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"filter(lambda x: x % 2 == 0, {numbers}): {even}")

# 使用lambda作为reduce的参数
from functools import reduce

sum_all = reduce(lambda a, b: a + b, numbers)
print(f"reduce(lambda a, b: a + b, {numbers}): {sum_all}")

# 使用lambda作为sorted的key
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 22},
    {"name": "David", "age": 19}
]

# 按年龄排序
sorted_by_age = sorted(students, key=lambda x: x["age"])
print(f"\n按年龄排序学生: {sorted_by_age}")

# 按姓名长度排序
sorted_by_name_length = sorted(students, key=lambda x: len(x["name"]))
print(f"按姓名长度排序学生: {sorted_by_name_length}")

# lambda的局限性
# 1. 只能包含一个表达式
# 2. 不能包含语句（如if、for、while）
# 3. 通常用于简单的一次性操作
```

输出结果：
```
lambda x: x * x (5): 25
lambda x: x * 2 (5): 10
lambda a, b: a + b (3, 4): 7

map(lambda x: x * x, [1, 2, 3, 4, 5]): [1, 4, 9, 16, 25]
filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]): [2, 4]
reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]): 15

按年龄排序学生: [{'name': 'Bob', 'age': 18}, {'name': 'David', 'age': 19}, {'name': 'Alice', 'age': 20}, {'name': 'Charlie', 'age': 22}]
按姓名长度排序学生: [{'name': 'Bob', 'age': 18}, {'name': 'Alice', 'age': 20}, {'name': 'David', 'age': 19}, {'name': 'Charlie', 'age': 22}]
```

## 四、函数式编程进阶

### 1. 闭包

```python
# 闭包示例
def outer_function(x):
    """外部函数"""
    def inner_function(y):
        """内部函数（闭包）"""
        return x + y
    return inner_function

# 创建闭包
add_5 = outer_function(5)
add_10 = outer_function(10)

# 调用闭包
print(f"add_5(3): {add_5(3)}")  # 5 + 3 = 8
print(f"add_10(3): {add_10(3)}")  # 10 + 3 = 13

# 闭包可以访问外部函数的变量
print(f"add_5.__closure__: {add_5.__closure__}")
print(f"add_5闭包中的变量: {add_5.__closure__[0].cell_contents}")

# 闭包的实际应用
# 1. 计数器
def create_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

counter1 = create_counter()
counter2 = create_counter()

print(f"\n计数器示例:")
print(f"counter1(): {counter1()}")
print(f"counter1(): {counter1()}")
print(f"counter2(): {counter2()}")
print(f"counter1(): {counter1()}")
print(f"counter2(): {counter2()}")

# 2. 配置化函数
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(f"\n配置化函数示例:")
print(f"double(5): {double(5)}")
print(f"triple(5): {triple(5)}")
print(f"quadruple(5): {quadruple(5)}")

# 3. 缓存
def create_cache():
    cache = {}
    def cached_function(x):
        if x not in cache:
            print(f"计算 {x}")
            cache[x] = x * x
        return cache[x]
    return cached_function

cached_square = create_cache()

print(f"\n缓存示例:")
print(f"cached_square(5): {cached_square(5)}")
print(f"cached_square(5): {cached_square(5)}")  # 不会重新计算
print(f"cached_square(6): {cached_square(6)}")
print(f"cached_square(6): {cached_square(6)}")  # 不会重新计算
```

输出结果：
```
add_5(3): 8
add_10(3): 13
add_5.__closure__: (<cell at 0x000001234567890: int object at 0x00000123456789A>,)
add_5闭包中的变量: 5

计数器示例:
counter1(): 1
counter1(): 2
counter2(): 1
counter1(): 3
counter2(): 2

配置化函数示例:
double(5): 10
triple(5): 15
quadruple(5): 20

缓存示例:
计算 5
cached_square(5): 25
cached_square(5): 25
计算 6
cached_square(6): 36
cached_square(6): 36
```

### 2. 柯里化

```python
# 柯里化示例

# 普通函数：接受两个参数
def add(a, b):
    return a + b

# 柯里化版本
def curry_add(a):
    def add_b(b):
        return a + b
    return add_b

# 使用柯里化函数
add_5 = curry_add(5)
result = add_5(3)  # 相当于 add(5, 3)
print(f"curry_add(5)(3): {result}")

# 使用functools.partial实现柯里化
from functools import partial

add_10 = partial(add, 10)
result = add_10(3)  # 相当于 add(10, 3)
print(f"partial(add, 10)(3): {result}")

# 多参数函数的柯里化
def multiply(a, b, c):
    return a * b * c

# 手动柯里化
def curry_multiply(a):
    def multiply_b(b):
        def multiply_c(c):
            return a * b * c
        return multiply_c
    return multiply_b

# 使用手动柯里化的函数
multiply_by_2 = curry_multiply(2)
multiply_by_2_and_3 = multiply_by_2(3)
result = multiply_by_2_and_3(4)  # 相当于 multiply(2, 3, 4)
print(f"curry_multiply(2)(3)(4): {result}")

# 使用partial实现多参数柯里化
multiply_by_5 = partial(multiply, 5)
multiply_by_5_and_2 = partial(multiply_by_5, 2)
result = multiply_by_5_and_2(3)  # 相当于 multiply(5, 2, 3)
print(f"partial(partial(multiply, 5), 2)(3): {result}")

# 柯里化的应用场景
# 1. 创建专用函数
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"\n专用函数示例:")
print(f"square(5): {square(5)}")
print(f"cube(5): {cube(5)}")

# 2. 函数组合
def compose(f, g):
    """函数组合：f(g(x))"""
    def composed(x):
        return f(g(x))
    return composed

# 创建组合函数
square_then_double = compose(partial(multiply, 2), square)
double_then_square = compose(square, partial(multiply, 2))

print(f"\n函数组合示例:")
print(f"square_then_double(3): {square_then_double(3)}")  # 2 * (3^2) = 18
print(f"double_then_square(3): {double_then_square(3)}")  # (2 * 3)^2 = 36
```

输出结果：
```
curry_add(5)(3): 8
partial(add, 10)(3): 13
curry_multiply(2)(3)(4): 24
partial(partial(multiply, 5), 2)(3): 30

专用函数示例:
square(5): 25
cube(5): 125

函数组合示例:
square_then_double(3): 18
double_then_square(3): 36
```

### 3. 列表推导式与生成器表达式

```python
# 列表推导式示例

# 基本列表推导式：创建平方数列表
numbers = [1, 2, 3, 4, 5]
squares = [x * x for x in numbers]
print(f"[x * x for x in {numbers}]: {squares}")

# 带条件的列表推导式：创建偶数平方数列表
even_squares = [x * x for x in numbers if x % 2 == 0]
print(f"[x * x for x in {numbers} if x % 2 == 0]: {even_squares}")

# 嵌套列表推导式：展平嵌套列表
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for sublist in nested_list for x in sublist]
print(f"[x for sublist in {nested_list} for x in sublist]: {flattened}")

# 字典推导式
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(f"{{word: len(word) for word in {words}}}: {word_lengths}")

# 集合推导式
unique_lengths = {len(word) for word in words}
print(f"{{len(word) for word in {words}}}: {unique_lengths}")

# 生成器表达式：与列表推导式类似，但返回生成器
# 生成器表达式使用圆括号，而不是方括号
numbers = [1, 2, 3, 4, 5]
square_generator = (x * x for x in numbers)

print(f"\n(x * x for x in {numbers}): {square_generator}")
print(f"list(square_generator): {list(square_generator)}")

# 生成器表达式的优势：
# 1. 节省内存：不会一次性创建整个列表
# 2. 可以处理无限序列
# 3. 适用于只需要迭代一次的情况

# 使用生成器表达式计算和
sum_squares = sum(x * x for x in numbers)
print(f"sum(x * x for x in {numbers}): {sum_squares}")

# 使用生成器表达式过滤
filtered_generator = (x for x in numbers if x % 2 == 0)
print(f"list(x for x in {numbers} if x % 2 == 0): {list(filtered_generator)}")

# 比较列表推导式和生成器表达式的内存使用
import sys

large_list = [x for x in range(1000000)]
large_generator = (x for x in range(1000000))

print(f"\n内存使用比较:")
print(f"列表推导式 (1,000,000个元素) 内存使用: {sys.getsizeof(large_list)} 字节")
print(f"生成器表达式 (1,000,000个元素) 内存使用: {sys.getsizeof(large_generator)} 字节")
```

输出结果：
```
[x * x for x in [1, 2, 3, 4, 5]]: [1, 4, 9, 16, 25]
[x * x for x in [1, 2, 3, 4, 5] if x % 2 == 0]: [4, 16]
[x for sublist in [[1, 2, 3], [4, 5, 6], [7, 8, 9]] for x in sublist]: [1, 2, 3, 4, 5, 6, 7, 8, 9]
{word: len(word) for word in ['apple', 'banana', 'cherry', 'date']}: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4}
{len(word) for word in ['apple', 'banana', 'cherry', 'date']}: {4, 5, 6}

(x * x for x in [1, 2, 3, 4, 5]): <generator object <genexpr> at 0x000001234567890>
list(square_generator): [1, 4, 9, 16, 25]
sum(x * x for x in [1, 2, 3, 4, 5]): 55
list(x for x in [1, 2, 3, 4, 5] if x % 2 == 0): [2, 4]

内存使用比较:
列表推导式 (1,000,000个元素) 内存使用: 8448728 字节
生成器表达式 (1,000,000个元素) 内存使用: 112 字节
```

## 四、函数式编程高级特性

### 1. 递归

```python
# 递归示例

# 阶乘
def factorial(n):
    """计算阶乘"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5): {factorial(5)}")

# 斐波那契数列
def fibonacci(n):
    """计算斐波那契数列的第n项"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"\n斐波那契数列前10项:")
for i in range(10):
    print(f"fibonacci({i}): {fibonacci(i)}")

# 递归的优化：尾递归
# Python不支持尾递归优化，所以这个示例只是展示尾递归的写法
def factorial_tail(n, accumulator=1):
    """尾递归版本的阶乘"""
    if n == 0:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

print(f"\n尾递归阶乘:")
print(f"factorial_tail(5): {factorial_tail(5)}")

# 递归的应用场景
# 1. 树结构的遍历
class TreeNode:
    """树节点"""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 创建一棵树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 前序遍历（根-左-右）
def preorder_traversal(node):
    """前序遍历树"""
    if not node:
        return []
    return [node.value] + preorder_traversal(node.left) + preorder_traversal(node.right)

print(f"\n树的前序遍历:")
print(f"preorder_traversal(root): {preorder_traversal(root)}")

# 2. 分治算法
def merge_sort(arr):
    """归并排序"""
    if len(arr) <= 1:
        return arr
    
    # 分治
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # 合并
    return merge(left, right)

def merge(left, right):
    """合并两个有序列表"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

numbers = [5, 3, 8, 4, 2, 7, 1, 6]
sorted_numbers = merge_sort(numbers)
print(f"\n归并排序:")
print(f"merge_sort({numbers}): {sorted_numbers}")
```

输出结果：
```
factorial(5): 120

斐波那契数列前10项:
fibonacci(0): 0
fibonacci(1): 1
fibonacci(2): 1
fibonacci(3): 2
fibonacci(4): 3
fibonacci(5): 5
fibonacci(6): 8
fibonacci(7): 13
fibonacci(8): 21
fibonacci(9): 34

尾递归阶乘:
factorial_tail(5): 120

树的前序遍历:
preorder_traversal(root): [1, 2, 4, 5, 3]

归并排序:
merge_sort([5, 3, 8, 4, 2, 7, 1, 6]): [1, 2, 3, 4, 5, 6, 7, 8]
```

### 2. 函数组合

```python
# 函数组合示例

# 基本的函数组合
def compose(f, g):
    """组合两个函数：f(g(x))"""
    def composed(x):
        return f(g(x))
    return composed

def double(x):
    return x * 2

def square(x):
    return x * x

# 创建组合函数
square_then_double = compose(double, square)
double_then_square = compose(square, double)

print(f"square_then_double(5): {square_then_double(5)}")  # double(square(5)) = double(25) = 50
print(f"double_then_square(5): {double_then_square(5)}")  # square(double(5)) = square(10) = 100

# 多个函数的组合
def add_1(x):
    return x + 1

# 手动组合三个函数
def compose_three(f, g, h):
    """组合三个函数：f(g(h(x)))"""
    def composed(x):
        return f(g(h(x)))
    return composed

add_1_then_square_then_double = compose_three(double, square, add_1)

print(f"\nadd_1_then_square_then_double(5): {add_1_then_square_then_double(5)}")  # double(square(add_1(5))) = double(square(6)) = double(36) = 72

# 使用reduce组合任意数量的函数
from functools import reduce

def compose_multiple(*functions):
    """组合任意数量的函数"""
    def composed(x):
        return reduce(lambda acc, f: f(acc), reversed(functions), x)
    return composed

# 组合四个函数
add_1_then_double_then_square_then_add_1 = compose_multiple(add_1, double, square, add_1)

result = add_1_then_double_then_square_then_add_1(5)
# 计算过程：add_1(5) = 6 -> square(6) = 36 -> double(36) = 72 -> add_1(72) = 73
print(f"\nadd_1_then_double_then_square_then_add_1(5): {result}")

# 使用函数组合进行数据处理
# 示例：处理用户数据
users = [
    {"name": "Alice", "age": 20, "score": 85},
    {"name": "Bob", "age": 18, "score": 92},
    {"name": "Charlie", "age": 22, "score": 78},
    {"name": "David", "age": 19, "score": 95},
    {"name": "Eve", "age": 21, "score": 88}
]

# 定义数据处理函数
def get_score(user):
    return user["score"]

def is_high_score(score):
    return score > 90

def get_name(user):
    return user["name"]

# 使用函数组合处理数据
def process_users(users):
    # 获取分数大于90的用户姓名
    high_score_users = filter(lambda user: is_high_score(get_score(user)), users)
    names = map(get_name, high_score_users)
    return list(names)

print(f"\n分数大于90的用户: {process_users(users)}")
```

输出结果：
```
square_then_double(5): 50
double_then_square(5): 100

add_1_then_square_then_double(5): 72

add_1_then_double_then_square_then_add_1(5): 73

分数大于90的用户: ['Bob', 'David']
```

### 3. 惰性求值

```python
# 惰性求值示例

# 生成器函数
def infinite_sequence():
    """生成无限序列"""
    num = 0
    while True:
        yield num
        num += 1

# 创建无限序列生成器
seq = infinite_sequence()

print(f"无限序列的前10个元素:")
for _ in range(10):
    print(next(seq), end=" ")
print()

# 惰性过滤
def even_numbers(seq):
    """生成序列中的偶数"""
    for num in seq:
        if num % 2 == 0:
            yield num

# 创建偶数生成器
even_seq = even_numbers(infinite_sequence())

print(f"\n无限序列中的前10个偶数:")
for _ in range(10):
    print(next(even_seq), end=" ")
print()

# 惰性映射
def square_numbers(seq):
    """生成序列中元素的平方"""
    for num in seq:
        yield num * num

# 创建平方数生成器
square_seq = square_numbers(infinite_sequence())

print(f"\n无限序列中前10个元素的平方:")
for _ in range(10):
    print(next(square_seq), end=" ")
print()

# 组合惰性操作
def even_squares(seq):
    """生成序列中偶数的平方"""
    return square_numbers(even_numbers(seq))

# 创建偶数平方生成器
even_square_seq = even_squares(infinite_sequence())

print(f"\n无限序列中前10个偶数的平方:")
for _ in range(10):
    print(next(even_square_seq), end=" ")
print()

# 惰性求值的优势：
# 1. 可以处理无限序列
# 2. 节省内存：只在需要时计算值
# 3. 提高性能：避免不必要的计算

# 使用itertools模块进行惰性操作
import itertools

# 无限计数器
count = itertools.count(start=0, step=1)

print(f"\nitertools.count()的前10个元素:")
for _ in range(10):
    print(next(count), end=" ")
print()

# 无限重复
repeat = itertools.repeat(5, times=5)  # 重复5次

print(f"\nitertools.repeat(5, times=5): {list(repeat)}")

# 循环重复
cycle = itertools.cycle([1, 2, 3])

print(f"\nitertools.cycle([1, 2, 3])的前10个元素:")
for _ in range(10):
    print(next(cycle), end=" ")
print()
```

输出结果：
```
无限序列的前10个元素:
0 1 2 3 4 5 6 7 8 9 

无限序列中的前10个偶数:
0 2 4 6 8 10 12 14 16 18 

无限序列中前10个元素的平方:
0 1 4 9 16 25 36 49 64 81 

无限序列中前10个偶数的平方:
0 4 16 36 64 100 144 196 256 324 

itertools.count()的前10个元素:
0 1 2 3 4 5 6 7 8 9 

itertools.repeat(5, times=5): [5, 5, 5, 5, 5]

itertools.cycle([1, 2, 3])的前10个元素:
1 2 3 1 2 3 1 2 3 1 
```

## 五、函数式编程实践

### 1. 数据处理

```python
# 使用函数式编程进行数据处理

# 示例数据
employees = [
    {"name": "Alice", "department": "HR", "salary": 50000},
    {"name": "Bob", "department": "IT", "salary": 60000},
    {"name": "Charlie", "department": "IT", "salary": 70000},
    {"name": "David", "department": "HR", "salary": 55000},
    {"name": "Eve", "department": "Finance", "salary": 65000},
    {"name": "Frank", "department": "IT", "salary": 80000},
    {"name": "Grace", "department": "Finance", "salary": 75000},
    {"name": "Henry", "department": "HR", "salary": 60000}
]

# 1. 过滤出IT部门的员工
from functools import reduce

it_employees = list(filter(lambda emp: emp["department"] == "IT", employees))
print(f"IT部门的员工: {[emp['name'] for emp in it_employees]}")

# 2. 计算IT部门员工的平均工资
if it_employees:
    total_salary = reduce(lambda acc, emp: acc + emp["salary"], it_employees, 0)
    average_salary = total_salary / len(it_employees)
    print(f"IT部门的平均工资: {average_salary:.2f}")

# 3. 计算每个部门的总工资
department_totals = reduce(
    lambda acc, emp:
    {
        **acc,
        emp["department"]: acc.get(emp["department"], 0) + emp["salary"]
    },
    employees,
    {}
)

print(f"\n每个部门的总工资: {department_totals}")

# 4. 找出工资最高的员工
highest_paid = reduce(
    lambda acc, emp:
    emp if emp["salary"] > acc["salary"] else acc,
    employees
)

print(f"\n工资最高的员工: {highest_paid['name']} (${highest_paid['salary']})")

# 5. 对员工按工资降序排序
sorted_by_salary = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
print(f"\n按工资降序排序的员工: {[emp['name'] for emp in sorted_by_salary]}")

# 6. 计算所有员工的工资总额
total_company_salary = reduce(lambda acc, emp: acc + emp["salary"], employees, 0)
print(f"\n公司工资总额: ${total_company_salary}")

# 7. 使用列表推导式创建员工姓名列表
employee_names = [emp["name"] for emp in employees]
print(f"\n所有员工姓名: {employee_names}")

# 8. 使用列表推导式创建高工资员工列表（工资>70000）
high_salary_employees = [emp["name"] for emp in employees if emp["salary"] > 70000]
print(f"\n高工资员工（>70000）: {high_salary_employees}")
```

输出结果：
```
IT部门的员工: ['Bob', 'Charlie', 'Frank']
IT部门的平均工资: 70000.00

每个部门的总工资: {'HR': 165000, 'IT': 210000, 'Finance': 140000}

工资最高的员工: Frank ($80000)

按工资降序排序的员工: ['Frank', 'Grace', 'Charlie', 'Eve', 'Bob', 'Henry', 'David', 'Alice']

公司工资总额: $515000

所有员工姓名: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry']

高工资员工（>70000）: ['Frank', 'Grace', 'Charlie']
```

### 2. 文本处理

```python
# 使用函数式编程进行文本处理

# 示例文本
text = "