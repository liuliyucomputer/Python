"""
此文件是Python模块的学习文档，包含Markdown格式和代码示例。
请使用文本编辑器或Markdown查看器打开以获得最佳阅读体验。
"""

# Python operator模块详解

## 1. 核心功能与概述

"operator"模块提供了对应于Python内置运算符的函数集合,这些函数可以用于函数式编程,排序,比较和其他操作.该模块的主要优势在于:

1. **函数式接口**:提供了运算符的函数式接口,便于在高阶函数中使用
2. **性能优化**:底层实现通常是C语言,比等效的lambda表达式更高效
3. **代码可读性**:对于复杂操作,使用命名函数比匿名lambda更清晰
4. **特殊操作支持**:提供了一些直接使用运算符难以实现的功能

"operator"模块主要包含以下几类函数:
- 算术运算符函数
- 比较运算符函数
- 逻辑运算符函数
- 按位运算符函数
- 序列操作函数
- 属性和索引访问函数
- 自定义对象操作函数

## 2. 基本使用方法

### 2.1 算术运算符函数

```python
import operator

# 加法
print(operator.add(10, 5))         # 输出: 15

# 减法
print(operator.sub(10, 5))         # 输出: 5

# 乘法
print(operator.mul(10, 5))         # 输出: 50

# 除法
print(operator.truediv(10, 5))     # 输出: 2.0
print(operator.floordiv(10, 3))    # 输出: 3 (整除)

# 取模
print(operator.mod(10, 3))         # 输出: 1

# 幂运算
print(operator.pow(2, 3))          # 输出: 8

# 取负
print(operator.neg(10))            # 输出: -10

# 取正
print(operator.pos(-10))           # 输出: -10 (保持不变)

# 绝对值
print(operator.abs(-10))           # 输出: 10
```

### 2.2 比较运算符函数

```python
# 等于
print(operator.eq(10, 10))         # 输出: True

# 不等于
print(operator.ne(10, 5))          # 输出: True

# 大于
print(operator.gt(10, 5))          # 输出: True

# 大于等于
print(operator.ge(10, 10))         # 输出: True

# 小于
print(operator.lt(5, 10))          # 输出: True

# 小于等于
print(operator.le(10, 10))         # 输出: True
```

### 2.3 逻辑运算符函数

```python
# 逻辑与
print(operator.and_(True, False))  # 输出: False
print(operator.and_(1, 0))         # 输出: 0 (数字上下文中的与)

# 逻辑或
print(operator.or_(True, False))   # 输出: True
print(operator.or_(1, 0))          # 输出: 1 (数字上下文中的或)

# 逻辑非(注意:这里不是函数,而是一个方法包装器)
from operator import not_
print(not_(True))                  # 输出: False
print(not_(0))                     # 输出: True
```

### 2.4 按位运算符函数

```python
# 按位与
print(operator.and_(0b1010, 0b1100))  # 输出: 8 (0b1000)

# 按位或
print(operator.or_(0b1010, 0b1100))   # 输出: 14 (0b1110)

# 按位异或
print(operator.xor(0b1010, 0b1100))   # 输出: 6 (0b0110)

# 按位非
print(operator.invert(0b1010))        # 输出: -11 (Python中按位非的结果)

# 左移
print(operator.lshift(5, 2))          # 输出: 20 (5 << 2)

# 右移
print(operator.rshift(20, 2))         # 输出: 5 (20 >> 2)
```

### 2.5 序列操作函数

```python
# 序列连接
print(operator.concat([1, 2, 3], [4, 5, 6]))  # 输出: [1, 2, 3, 4, 5, 6]

# 包含检查
print(operator.contains([1, 2, 3], 2))        # 输出: True

# 索引查找
print(operator.getitem([1, 2, 3], 1))         # 输出: 2

# 设置索引值
lst = [1, 2, 3]
operator.setitem(lst, 1, 10)
print(lst)                                    # 输出: [1, 10, 3]

# 删除索引
operator.delitem(lst, 1)
print(lst)                                    # 输出: [1, 3]

# 获取长度
print(operator.length_hint([1, 2, 3, 4, 5]))  # 输出: 5
```

### 2.6 属性和索引访问函数

```python
# 属性访问
try:
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    p = Person("Alice", 30)
    print(operator.attrgetter('name')(p))     # 输出: Alice
    print(operator.attrgetter('age')(p))      # 输出: 30
    
    # 多个属性访问
    name_age = operator.attrgetter('name', 'age')(p)
    print(name_age)                           # 输出: ('Alice', 30)
    
except Exception as e:
    print(f"属性访问示例出错: {e}")

# 索引访问
print(operator.itemgetter(1)([10, 20, 30]))   # 输出: 20
print(operator.itemgetter(0, 2)([10, 20, 30])) # 输出: (10, 30)
print(operator.itemgetter('a')({'a': 1, 'b': 2})) # 输出: 1
```

### 2.7 自定义对象操作

```python
# 用于创建自定义对象的操作符函数
from operator import methodcaller

try:
    # 方法调用
    s = "hello world"
    print(methodcaller('upper')(s))           # 输出: HELLO WORLD
    print(methodcaller('replace', 'world', 'python')(s)) # 输出: hello python
    
except Exception as e:
    print(f"方法调用示例出错: {e}")
```

## 3. 高级用法

### 3.1 在排序中的应用

"operator"模块的函数在排序操作中特别有用,可以避免使用lambda表达式,提高代码可读性和性能.

```python
import operator

# 按单个键排序
students = [
    {"name": "Alice", "score": 85, "age": 20},
    {"name": "Bob", "score": 92, "age": 19},
    {"name": "Charlie", "score": 78, "age": 21}
]

# 按分数排序(升序)
sorted_by_score = sorted(students, key=operator.itemgetter('score'))
print("按分数升序排序:")
for student in sorted_by_score:
    print(f"  {student['name']}: {student['score']}")

# 按分数排序(降序)
sorted_by_score_desc = sorted(students, key=operator.itemgetter('score'), reverse=True)
print("\n按分数降序排序:")
for student in sorted_by_score_desc:
    print(f"  {student['name']}: {student['score']}")

# 按多个键排序(先按分数降序,再按年龄升序)
sorted_by_score_age = sorted(students, key=operator.itemgetter('score', 'age'), reverse=True)
print("\n按分数降序和年龄升序排序:")
for student in sorted_by_score_age:
    print(f"  {student['name']}: 分数={student['score']}, 年龄={student['age']}")

# 使用attrgetter排序自定义对象
try:
    class Student:
        def __init__(self, name, score, age):
            self.name = name
            self.score = score
            self.age = age
        
        def __repr__(self):
            return f"Student(name={self.name}, score={self.score}, age={self.age})"
    
    student_objects = [
        Student("Alice", 85, 20),
        Student("Bob", 92, 19),
        Student("Charlie", 78, 21)
    ]
    
    # 按分数排序
    sorted_students = sorted(student_objects, key=operator.attrgetter('score'))
    print("\n学生对象按分数排序:")
    for student in sorted_students:
        print(f"  {student}")
    
    # 按多个属性排序
    sorted_students_multi = sorted(student_objects, key=operator.attrgetter('score', 'age'), reverse=True)
    print("\n学生对象按分数和年龄排序:")
    for student in sorted_students_multi:
        print(f"  {student}")
    
except Exception as e:
    print(f"自定义对象排序示例出错: {e}")
```

### 3.2 在函数式编程中的应用

结合"functools"和其他函数式编程工具,"operator"模块可以实现更简洁,高效的函数式编程模式.

```python
import operator
import functools
from itertools import accumulate

# 计算列表元素的和
numbers = [1, 2, 3, 4, 5]
sum_result = functools.reduce(operator.add, numbers)
print(f"列表求和: {sum_result}")

# 计算列表元素的乘积
product_result = functools.reduce(operator.mul, numbers)
print(f"列表乘积: {product_result}")

# 计算累积和
cumulative_sums = list(accumulate(numbers, operator.add))
print(f"累积和: {cumulative_sums}")

# 计算累积乘积
cumulative_products = list(accumulate(numbers, operator.mul))
print(f"累积乘积: {cumulative_products}")

# 检查所有元素是否为真
all_true = functools.reduce(operator.and_, [True, True, True])
print(f"所有元素为真: {all_true}")

# 检查是否有任何元素为真
any_true = functools.reduce(operator.or_, [False, False, True])
print(f"有元素为真: {any_true}")
```

### 3.3 自定义比较器

使用"operator"模块可以创建自定义比较器,实现复杂的排序逻辑.

```python
import operator

# 自定义比较函数
def compare_by_abs(a, b):
    # 按绝对值大小排序
    return operator.sub(abs(a), abs(b))

# 使用自定义比较函数排序(Python 3中不再直接支持cmp参数)
numbers = [-5, 3, -1, 2, -4]

# 方法1:转换为键函数
sorted_by_abs = sorted(numbers, key=abs)
print(f"按绝对值排序: {sorted_by_abs}")

# 方法2:使用functools.cmp_to_key(Python 3兼容方式)
import functools
sorted_with_cmp = sorted(numbers, key=functools.cmp_to_key(compare_by_abs))
print(f"使用自定义比较器排序: {sorted_with_cmp}")

# 自定义复杂比较
try:
    class Product:
        def __init__(self, name, price, rating):
            self.name = name
            self.price = price
            self.rating = rating
        
        def __repr__(self):
            return f"Product(name={self.name}, price={self.price}, rating={self.rating})"
    
    products = [
        Product("手机", 3999, 4.5),
        Product("笔记本", 5999, 4.7),
        Product("平板", 2999, 4.3),
        Product("耳机", 999, 4.6)
    ]
    
    # 先按评分降序,再按价格升序
    def product_comparator(a, b):
        # 先比较评分(降序)
        rating_diff = operator.sub(b.rating, a.rating)
        if rating_diff != 0:
            return rating_diff
        # 评分相同时比较价格(升序)
        return operator.sub(a.price, b.price)
    
    sorted_products = sorted(products, key=functools.cmp_to_key(product_comparator))
    print("\n产品按评分和价格排序:")
    for product in sorted_products:
        print(f"  {product}")
    
except Exception as e:
    print(f"自定义比较器示例出错: {e}")
```

### 3.4 数据转换与映射

使用"operator"模块可以实现高效的数据转换和映射操作.

```python
import operator
from functools import partial

# 数据提取
students = [
    {"name": "Alice", "score": 85, "age": 20},
    {"name": "Bob", "score": 92, "age": 19},
    {"name": "Charlie", "score": 78, "age": 21}
]

# 提取所有学生的姓名
names = list(map(operator.itemgetter('name'), students))
print(f"学生姓名列表: {names}")

# 提取所有学生的分数
scores = list(map(operator.itemgetter('score'), students))
print(f"学生分数列表: {scores}")

# 提取多个字段
name_score_pairs = list(map(operator.itemgetter('name', 'score'), students))
print(f"学生姓名-分数对: {name_score_pairs}")

# 使用methodcaller进行数据转换
strings = ["hello", "world", "python"]

# 转换为大写
upper_strings = list(map(methodcaller('upper'), strings))
print(f"大写字符串列表: {upper_strings}")

# 替换字符串
replaced_strings = list(map(methodcaller('replace', 'o', 'O'), strings))
print(f"替换后的字符串列表: {replaced_strings}")

# 使用partial创建特定操作的函数
try:
    # 创建一个用于提取特定索引的函数
    get_first = partial(operator.itemgetter, 0)
    get_second = partial(operator.itemgetter, 1)
    
    pairs = [(1, 10), (2, 20), (3, 30)]
    first_elements = list(map(get_first, pairs))
    second_elements = list(map(get_second, pairs))
    
    print(f"第一个元素列表: {first_elements}")
    print(f"第二个元素列表: {second_elements}")
    
except Exception as e:
    print(f"数据转换与映射示例出错: {e}")
```

### 3.5 动态属性访问

使用"operator"模块可以实现动态的属性和方法访问.

```python
import operator

# 动态属性访问
try:
    class Config:
        def __init__(self):
            self.host = "localhost"
            self.port = 8080
            self.debug = False
            self.timeout = 30
    
    config = Config()
    
    # 动态获取属性
    prop_names = ['host', 'port', 'debug']
    for prop_name in prop_names:
        getter = operator.attrgetter(prop_name)
        print(f"{prop_name}: {getter(config)}")
    
    # 动态设置属性
    operator.setattr(config, 'port', 9090)
    print(f"更新后的端口: {config.port}")
    
    # 动态检查属性是否存在
    has_debug = hasattr(config, 'debug')
    has_username = hasattr(config, 'username')
    print(f"是否有debug属性: {has_debug}")
    print(f"是否有username属性: {has_username}")
    
except Exception as e:
    print(f"动态属性访问示例出错: {e}")

# 动态方法调用
try:
    class StringProcessor:
        def __init__(self):
            pass
        
        def process_upper(self, s):
            return s.upper()
        
        def process_lower(self, s):
            return s.lower()
        
        def process_title(self, s):
            return s.title()
    
    processor = StringProcessor()
    text = "hello world"
    
    # 动态选择处理方法
    methods = ['process_upper', 'process_lower', 'process_title']
    
    for method_name in methods:
        # 检查方法是否存在
        if hasattr(processor, method_name):
            # 获取方法并调用
            method = getattr(processor, method_name)
            result = method(text)
            print(f"{method_name} 结果: {result}")
    
    # 使用methodcaller动态调用
    for method_name in methods:
        if hasattr(processor, method_name):
            # 创建方法调用器
            method_caller = methodcaller(method_name, text)
            result = method_caller(processor)
            print(f"使用methodcaller调用{method_name} 结果: {result}")
    
except Exception as e:
    print(f"动态方法调用示例出错: {e}")
```

## 4. 实际应用场景

### 4.1 高效排序

"operator"模块在需要基于对象属性或字典键进行排序时特别有用,可以显著提高代码的可读性和性能.

```python
import operator

# 示例:根据多个条件排序产品列表
try:
    class Product:
        def __init__(self, name, category, price, rating):
            self.name = name
            self.category = category
            self.price = price
            self.rating = rating
        
        def __repr__(self):
            return f"{self.name} ({self.category}): ¥{self.price}, 评分: {self.rating}"
    
    # 创建产品列表
    products = [
        Product("iPhone 13", "手机", 5999, 4.7),
        Product("Samsung Galaxy S21", "手机", 5799, 4.6),
        Product("MacBook Pro", "笔记本", 11999, 4.9),
        Product("ThinkPad X1", "笔记本", 9999, 4.8),
        Product("iPad Pro", "平板", 6299, 4.8),
        Product("Surface Pro", "平板", 7699, 4.7)
    ]
    
    # 1. 按类别和价格排序
    sorted_by_category_price = sorted(products, key=operator.attrgetter('category', 'price'))
    print("按类别和价格排序:")
    for product in sorted_by_category_price:
        print(f"  {product}")
    
    # 2. 按评分降序排序
    sorted_by_rating_desc = sorted(products, key=operator.attrgetter('rating'), reverse=True)
    print("\n按评分降序排序:")
    for product in sorted_by_rating_desc:
        print(f"  {product}")
    
    # 3. 按类别分组后排序
    # 先按类别排序
    products_by_category = sorted(products, key=operator.attrgetter('category'))
    
    # 然后在每个类别内按评分降序排序
    from itertools import groupby
    print("\n按类别分组并在组内按评分排序:")
    for category, group in groupby(products_by_category, key=operator.attrgetter('category')):
        # 对每个组内的产品按评分降序排序
        sorted_group = sorted(group, key=operator.attrgetter('rating'), reverse=True)
        print(f"类别: {category}")
        for product in sorted_group:
            print(f"  {product}")
    
except Exception as e:
    print(f"高效排序示例出错: {e}")
```

### 4.2 数据处理和转换

在数据处理管道中,"operator"模块可以用于高效地提取,转换和组合数据.

```python
import operator
from functools import reduce

# 示例:处理销售数据
sales_data = [
    {"product": "A", "quantity": 10, "price": 20},
    {"product": "B", "quantity": 5, "price": 30},
    {"product": "A", "quantity": 8, "price": 20},
    {"product": "C", "quantity": 12, "price": 15},
    {"product": "B", "quantity": 3, "price": 30}
]

# 1. 计算每个销售记录的总金额(数量 * 价格)
for sale in sales_data:
    sale['total'] = operator.mul(sale['quantity'], sale['price'])

print("销售记录带总金额:")
for sale in sales_data:
    print(f"  {sale['product']}: {sale['quantity']} * {sale['price']} = {sale['total']}")

# 2. 按产品分组并计算总销售额
product_totals = {}
for sale in sales_data:
    product = sale['product']
    if product not in product_totals:
        product_totals[product] = 0
    product_totals[product] = operator.add(product_totals[product], sale['total'])

print("\n按产品统计总销售额:")
for product, total in sorted(product_totals.items()):
    print(f"  产品 {product}: ¥{total}")

# 3. 计算所有产品的总销售额
total_sales = reduce(operator.add, product_totals.values())
print(f"\n所有产品总销售额: ¥{total_sales}")

# 4. 找出销售额最高的产品
best_product = max(product_totals.items(), key=operator.itemgetter(1))
print(f"\n销售额最高的产品: {best_product[0]} (¥{best_product[1]})")
```

### 4.3 函数式编程模式

"operator"模块与Python的函数式编程工具结合,可以实现优雅的数据处理模式.

```python
import operator
import functools
from itertools import filterfalse

# 函数式数据处理示例

# 准备数据
numbers = list(range(1, 11))
print(f"原始数据: {numbers}")

# 1. 过滤出偶数
is_even = lambda x: operator.mod(x, 2) == 0
even_numbers = list(filter(is_even, numbers))
print(f"偶数: {even_numbers}")

# 2. 过滤出奇数(使用filterfalse)
odd_numbers = list(filterfalse(is_even, numbers))
print(f"奇数: {odd_numbers}")

# 3. 计算平方
squares = list(map(operator.mul, numbers, numbers))  # x * x
print(f"平方: {squares}")

# 4. 计算立方
cubes = list(map(lambda x: operator.mul(operator.mul(x, x), x), numbers))
print(f"立方: {cubes}")

# 5. 计算累积和
cumulative_sum = functools.reduce(operator.add, numbers)
print(f"累积和: {cumulative_sum}")

# 6. 计算累积乘积
cumulative_product = functools.reduce(operator.mul, numbers)
print(f"累积乘积: {cumulative_product}")

# 7. 找出最大值和最小值
max_value = functools.reduce(lambda a, b: a if operator.gt(a, b) else b, numbers)
min_value = functools.reduce(lambda a, b: a if operator.lt(a, b) else b, numbers)
print(f"最大值: {max_value}")
print(f"最小值: {min_value}")

# 8. 创建复合函数
def compose(f, g):
    return lambda x: f(g(x))

# 先平方,再乘以2
square_then_double = compose(partial(operator.mul, 2), lambda x: operator.mul(x, x))
result = list(map(square_then_double, numbers))
print(f"平方后乘以2: {result}")
```

### 4.4 自定义数据结构操作

"operator"模块可以用于实现自定义数据结构的操作符功能.

```python
import operator

# 示例:实现向量类的操作符功能
try:
    class Vector:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        
        def __repr__(self):
            return f"Vector({self.x}, {self.y}, {self.z})"
        
        # 使用operator模块实现向量操作
        def add(self, other):
            return Vector(
                operator.add(self.x, other.x),
                operator.add(self.y, other.y),
                operator.add(self.z, other.z)
            )
        
        def subtract(self, other):
            return Vector(
                operator.sub(self.x, other.x),
                operator.sub(self.y, other.y),
                operator.sub(self.z, other.z)
            )
        
        def multiply(self, scalar):
            return Vector(
                operator.mul(self.x, scalar),
                operator.mul(self.y, scalar),
                operator.mul(self.z, scalar)
            )
        
        def dot_product(self, other):
            return operator.add(
                operator.add(
                    operator.mul(self.x, other.x),
                    operator.mul(self.y, other.y)
                ),
                operator.mul(self.z, other.z)
            )
        
        def magnitude(self):
            return (operator.add(
                operator.add(
                    operator.mul(self.x, self.x),
                    operator.mul(self.y, self.y)
                ),
                operator.mul(self.z, self.z)
            )) ** 0.5
        
        def equals(self, other):
            return (operator.eq(self.x, other.x) and 
                    operator.eq(self.y, other.y) and 
                    operator.eq(self.z, other.z))
    
    # 创建向量
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    # 测试向量操作
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1.add(v2)}")
    print(f"v1 - v2 = {v1.subtract(v2)}")
    print(f"v1 * 2 = {v1.multiply(2)}")
    print(f"v1 · v2 = {v1.dot_product(v2)}")
    print(f"|v1| = {v1.magnitude():.2f}")
    print(f"v1 == v2: {v1.equals(v2)}")
    
except Exception as e:
    print(f"自定义数据结构操作示例出错: {e}")
```

### 4.5 高级属性访问与配置管理

"operator"模块可以用于实现灵活的配置管理和动态属性访问.

```python
import operator
import json

# 示例:动态配置管理器
try:
    class ConfigManager:
        def __init__(self, default_config=None):
            self._config = default_config or {}
        
        def load_config(self, config_file):
            """从文件加载配置"""
            try:
                with open(config_file, 'r') as f:
                    new_config = json.load(f)
                # 合并配置
                self._config.update(new_config)
                return True
            except Exception as e:
                print(f"加载配置失败: {e}")
                return False
        
        def get(self, key, default=None):
            """获取配置值,支持点表示法访问嵌套配置"""
            keys = key.split('.')
            value = self._config
            
            try:
                for k in keys:
                    # 尝试作为整数索引访问(用于列表)
                    try:
                        k_idx = int(k)
                        value = operator.getitem(value, k_idx)
                    except (ValueError, TypeError, IndexError):
                        # 作为键访问(用于字典)
                        value = operator.getitem(value, k)
                return value
            except (KeyError, TypeError):
                return default
        
        def set(self, key, value):
            """设置配置值,支持点表示法访问嵌套配置"""
            keys = key.split('.')
            config = self._config
            
            # 处理除最后一个键以外的所有键
            for k in keys[:-1]:
                # 尝试作为整数索引访问
                try:
                    k_idx = int(k)
                    # 确保索引存在
                    while k_idx >= len(config):
                        config.append({})
                    if not isinstance(operator.getitem(config, k_idx), (dict, list)):
                        operator.setitem(config, k_idx, {})
                    config = operator.getitem(config, k_idx)
                except (ValueError, TypeError):
                    # 作为字典键访问
                    if k not in config:
                        operator.setitem(config, k, {})
                    elif not isinstance(operator.getitem(config, k), (dict, list)):
                        operator.setitem(config, k, {})
                    config = operator.getitem(config, k)
            
            # 设置最后一个键的值
            last_key = keys[-1]
            try:
                last_key_idx = int(last_key)
                # 确保列表足够长
                while last_key_idx >= len(config):
                    config.append(None)
                operator.setitem(config, last_key_idx, value)
            except (ValueError, TypeError):
                operator.setitem(config, last_key, value)
        
        def has(self, key):
            """检查配置键是否存在"""
            try:
                self.get(key)
                return True
            except (KeyError, TypeError, IndexError):
                return False
        
        def remove(self, key):
            """删除配置键"""
            keys = key.split('.')
            config = self._config
            
            # 处理除最后一个键以外的所有键
            for k in keys[:-1]:
                try:
                    k_idx = int(k)
                    config = operator.getitem(config, k_idx)
                except (ValueError, TypeError, KeyError, IndexError):
                    return False
            
            # 删除最后一个键
            last_key = keys[-1]
            try:
                last_key_idx = int(last_key)
                del config[last_key_idx]
            except (ValueError, TypeError, KeyError, IndexError):
                try:
                    del config[last_key]
                except (KeyError, TypeError):
                    return False
            
            return True
        
        def get_config(self):
            """获取完整配置"""
            return self._config
    
    # 使用配置管理器
    config_manager = ConfigManager({
        "app": {
            "name": "MyApp",
            "version": "1.0.0"
        },
        "server": {
            "host": "localhost",
            "port": 8000
        },
        "database": {
            "url": "sqlite:///data.db",
            "timeout": 30
        }
    })
    
    # 获取配置
    print(f"应用名称: {config_manager.get('app.name')}")
    print(f"服务器地址: {config_manager.get('server.host')}:{config_manager.get('server.port')}")
    print(f"数据库URL: {config_manager.get('database.url')}")
    print(f"不存在的配置: {config_manager.get('unknown.key', '默认值')}")
    
    # 修改配置
    config_manager.set('server.port', 9000)
    config_manager.set('logging.level', 'INFO')
    config_manager.set('features', ["auth", "dashboard", "api"])
    config_manager.set('features.1', "reports")  # 修改列表元素
    
    print("\n更新后的配置:")
    print(f"服务器端口: {config_manager.get('server.port')}")
    print(f"日志级别: {config_manager.get('logging.level')}")
    print(f"功能列表: {config_manager.get('features')}")
    
    # 检查配置是否存在
    print(f"\n是否有数据库配置: {config_manager.has('database')}")
    print(f"是否有缓存配置: {config_manager.has('cache')}")
    
    # 删除配置
    config_manager.remove('database.timeout')
    print(f"\n删除超时配置后: {config_manager.get('database')}")
    
    # 获取完整配置
    print("\n完整配置:")
    print(json.dumps(config_manager.get_config(), indent=2))
    
except Exception as e:
    print(f"高级属性访问与配置管理示例出错: {e}")
```

### 4.6 动态方法调度

"operator"模块可以用于实现动态的方法调度系统.

```python
import operator

# 示例:实现命令模式的动态调度器
try:
    class CommandHandler:
        def __init__(self):
            self._commands = {}
        
        def register_command(self, command_name, handler_func):
            """注册命令处理器"""
            self._commands[command_name] = handler_func
        
        def execute_command(self, command_name, *args, **kwargs):
            """执行命令"""
            if command_name in self._commands:
                handler = self._commands[command_name]
                return handler(*args, **kwargs)
            else:
                raise ValueError(f"未知命令: {command_name}")
        
        def has_command(self, command_name):
            """检查命令是否存在"""
            return command_name in self._commands
        
        def get_commands(self):
            """获取所有注册的命令"""
            return list(self._commands.keys())
    
    # 创建命令处理器
    command_handler = CommandHandler()
    
    # 注册一些数学运算命令
    command_handler.register_command('add', operator.add)
    command_handler.register_command('subtract', operator.sub)
    command_handler.register_command('multiply', operator.mul)
    command_handler.register_command('divide', operator.truediv)
    command_handler.register_command('power', operator.pow)
    
    # 执行命令
    print("执行数学命令:")
    print(f"2 + 3 = {command_handler.execute_command('add', 2, 3)}")
    print(f"5 - 2 = {command_handler.execute_command('subtract', 5, 2)}")
    print(f"4 * 6 = {command_handler.execute_command('multiply', 4, 6)}")
    print(f"10 / 2 = {command_handler.execute_command('divide', 10, 2)}")
    print(f"2 ^ 8 = {command_handler.execute_command('power', 2, 8)}")
    
    # 注册自定义命令
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    command_handler.register_command('greet', greet)
    
    print(f"\n自定义命令:")
    print(f"{command_handler.execute_command('greet', 'Alice')}")
    print(f"{command_handler.execute_command('greet', 'Bob', greeting='Hi')}")
    
    # 获取所有命令
    print(f"\n所有可用命令: {command_handler.get_commands()}")
    
except Exception as e:
    print(f"动态方法调度示例出错: {e}")

# 示例:通用数据转换系统
try:
    class DataTransformer:
        def __init__(self):
            self._transformations = {}
        
        def register_transformation(self, name, func):
            """注册转换函数"""
            self._transformations[name] = func
        
        def transform(self, data, transformation_name):
            """应用转换"""
            if transformation_name in self._transformations:
                transform_func = self._transformations[transformation_name]
                return transform_func(data)
            else:
                raise ValueError(f"未知转换: {transformation_name}")
        
        def apply_pipeline(self, data, transformations):
            """应用转换管道"""
            result = data
            for transformation_name in transformations:
                result = self.transform(result, transformation_name)
            return result
    
    # 创建数据转换器
    transformer = DataTransformer()
    
    # 注册转换函数
    transformer.register_transformation('double', lambda x: list(map(partial(operator.mul, 2), x)))
    transformer.register_transformation('square', lambda x: list(map(lambda y: operator.mul(y, y), x)))
    transformer.register_transformation('filter_even', lambda x: list(filter(lambda y: operator.mod(y, 2) == 0, x)))
    transformer.register_transformation('sum', lambda x: functools.reduce(operator.add, x))
    
    # 测试转换
    data = [1, 2, 3, 4, 5]
    print(f"\n数据转换示例:")
    print(f"原始数据: {data}")
    print(f"加倍后: {transformer.transform(data, 'double')}")
    print(f"平方后: {transformer.transform(data, 'square')}")
    print(f"过滤偶数后: {transformer.transform(data, 'filter_even')}")
    print(f"求和: {transformer.transform(data, 'sum')}")
    
    # 应用转换管道:先过滤偶数,然后加倍,最后求和
    pipeline_result = transformer.apply_pipeline(data, ['filter_even', 'double', 'sum'])
    print(f"\n转换管道结果 (偶数 -> 加倍 -> 求和): {pipeline_result}")
    
except Exception as e:
    print(f"通用数据转换系统示例出错: {e}")
```

## 5. 性能分析

### 5.1 时间复杂度分析

| 函数类型 | 时间复杂度 | 空间复杂度 | 说明 |
|---------|-----------|-----------|------|
| 算术运算符函数 | O(1) | O(1) | 基本算术运算 |
| 比较运算符函数 | O(1) | O(1) | 基本比较运算 |
| 逻辑运算符函数 | O(1) | O(1) | 基本逻辑运算 |
| 按位运算符函数 | O(1) | O(1) | 基本位运算 |
| itemgetter | O(1) | O(1) | 索引访问 |
| attrgetter | O(1) | O(1) | 属性访问 |
| methodcaller | O(1) (创建), O(k) (调用) | O(1) | k为方法调用的复杂度 |

### 5.2 性能比较测试

```python
import operator
import timeit

# 性能比较测试
def performance_test():
    print("=== operator模块性能测试 ===")
    
    # 1. 比较算术运算符函数与直接运算符
    add_func_time = timeit.timeit(
        "operator.add(10, 5)",
        setup="import operator",
        number=1000000
    )
    
    add_op_time = timeit.timeit(
        "10 + 5",
        number=1000000
    )
    
    print(f"operator.add vs 直接+运算符: {add_func_time:.6f}s vs {add_op_time:.6f}s")
    
    # 2. 比较itemgetter与lambda表达式
    itemgetter_time = timeit.timeit(
        "get_score(student)",
        setup="import operator; get_score = operator.itemgetter('score'); student = {'name': 'Alice', 'score': 85}",
        number=1000000
    )
    
    lambda_time = timeit.timeit(
        "get_score(student)",
        setup="get_score = lambda x: x['score']; student = {'name': 'Alice', 'score': 85}",
        number=1000000
    )
    
    print(f"operator.itemgetter vs lambda: {itemgetter_time:.6f}s vs {lambda_time:.6f}s")
    
    # 3. 比较attrgetter与lambda表达式
try:
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    attrgetter_time = timeit.timeit(
        "get_age(person)",
        setup="import operator; from __main__ import Person; get_age = operator.attrgetter('age'); person = Person('Alice', 30)",
        number=1000000
    )
    
    lambda_attr_time = timeit.timeit(
        "get_age(person)",
        setup="from __main__ import Person; get_age = lambda x: x.age; person = Person('Alice', 30)",
        number=1000000
    )
    
    print(f"operator.attrgetter vs lambda: {attrgetter_time:.6f}s vs {lambda_attr_time:.6f}s")
    
except Exception as e:
    print(f"attrgetter性能测试出错: {e}")
    
    # 4. 比较methodcaller与直接方法调用
try:
    methodcaller_time = timeit.timeit(
        "to_upper(s)",
        setup="import operator; to_upper = operator.methodcaller('upper'); s = 'hello world'",
        number=1000000
    )
    
    direct_call_time = timeit.timeit(
        "s.upper()",
        setup="s = 'hello world'",
        number=1000000
    )
    
    print(f"operator.methodcaller vs 直接调用: {methodcaller_time:.6f}s vs {direct_call_time:.6f}s")
    
except Exception as e:
    print(f"methodcaller性能测试出错: {e}")
    
    # 5. 比较排序性能
    sort_itemgetter_time = timeit.timeit(
        "sorted(students, key=get_score)",
        setup="import operator; get_score = operator.itemgetter('score'); students = [{'name': f'student{i}', 'score': i} for i in range(100)]",
        number=1000
    )
    
    sort_lambda_time = timeit.timeit(
        "sorted(students, key=lambda x: x['score'])",
        setup="students = [{'name': f'student{i}', 'score': i} for i in range(100)]",
        number=1000
    )
    
    print(f"使用itemgetter排序 vs 使用lambda排序: {sort_itemgetter_time:.6f}s vs {sort_lambda_time:.6f}s")

# 运行性能测试
performance_test()
```

## 6. 使用注意事项

### 6.1 性能考虑

1. **直接运算符 vs operator函数**:对于简单操作,直接使用运算符(如"+", "-", "*")通常比使用"operator"模块的函数更快."operator"模块主要在需要函数式接口时使用.

2. **itemgetter vs lambda**:对于简单的索引或键访问,"operator.itemgetter"通常比等效的lambda表达式更快,尤其是在排序等需要多次调用的场景中.

3. **内存使用**:"operator"模块的函数通常比lambda表达式有更小的内存占用,因为它们是预定义的函数对象,而不是动态创建的闭包.

### 6.2 安全性考虑

1. **动态属性访问**:使用"attrgetter"和"getattr"进行动态属性访问时,需要注意安全风险,避免访问敏感属性.

2. **用户输入处理**:在处理来自用户的输入时,特别是在动态调度命令或访问属性时,需要进行适当的验证,防止注入攻击.

### 6.3 兼容性和版本差异

1. **Python 2 vs Python 3**:"operator"模块在Python 2和Python 3之间有一些差异,特别是在排序相关的功能上.Python 3移除了"cmp"参数,需要使用"functools.cmp_to_key".

2. **API变更**:虽然"operator"模块相对稳定,但在升级Python版本时仍需注意可能的API变更.

### 6.4 最佳实践建议

1. **在排序和映射中优先使用itemgetter/attrgetter**:对于排序和映射操作,使用这些函数比lambda表达式更清晰,更高效.

2. **在函数式编程中使用operator函数**:在需要传递操作符作为函数参数时,使用"operator"模块的函数.

3. **避免过度使用**:对于简单操作,直接使用运算符通常更直观.

4. **注意methodcaller的局限性**:"methodcaller"只能调用无参数方法或在创建时绑定参数,对于需要动态参数的场景可能不太适用.

## 7. 总结与最佳实践

### 7.1 主要优势

1. **函数式接口**:提供了运算符的函数式表示,便于在高阶函数中使用.

2. **性能优化**:对于排序和映射等操作,"operator"模块的函数通常比lambda表达式更高效.

3. **代码可读性**:使用命名函数(如"itemgetter('score')")比匿名lambda表达式更清晰,特别是在复杂操作中.

4. **减少样板代码**:避免了编写重复的lambda表达式,使代码更简洁.

### 7.2 最佳实践

1. **排序时使用itemgetter/attrgetter**:
   ```python
   # 推荐
   sorted(students, key=operator.itemgetter('score', 'age'))
   
   # 不推荐
   sorted(students, key=lambda x: (x['score'], x['age']))
   ```

2. **在高阶函数中使用operator**:
   ```python
   # 推荐
   from functools import reduce
   total = reduce(operator.add, numbers)
   
   # 不推荐
   total = reduce(lambda a, b: a + b, numbers)
   ```

3. **使用methodcaller进行方法调用**:
   ```python
   # 推荐
   to_upper = operator.methodcaller('upper')
   result = list(map(to_upper, strings))
   
   # 不推荐
   result = list(map(lambda s: s.upper(), strings))
   ```

4. **创建复合操作**:使用"functools.partial"和"operator"函数创建复合操作.

### 7.3 选择使用建议

- **简单操作**:直接使用运算符,更直观.
- **排序/映射**:使用"itemgetter"/"attrgetter",更高效,更清晰.
- **函数式编程**:使用"operator"函数作为高阶函数的参数.
- **动态属性/方法访问**:使用"attrgetter"/"methodcaller",提供一致的接口.

### 7.4 学习总结

"operator"模块是Python标准库中一个强大但经常被忽视的工具,它提供了对应于Python内置运算符的函数集合,使得在需要函数式接口的场景中能够方便地使用这些操作.通过熟练掌握"operator"模块的各种函数,可以编写更简洁,更高效,更易读的Python代码.

在实际应用中,"operator"模块特别适合于排序,映射,函数式编程和动态属性访问等场景.结合Python的其他特性(如高阶函数,列表推导式),"operator"模块可以帮助构建更加优雅和高效的数据处理解决方案.
```
"""
'''
"
'
