"""
# operator模块详解：函数式编程的操作符工具箱

operator模块提供了与Python内置操作符对应的函数，这些函数是标准操作符的函数式封装。在函数式编程范式中，operator模块特别有用，可以避免创建简单的lambda函数，提高代码的可读性和执行效率。

## 1. 核心功能概览

operator模块主要提供以下几类操作符函数：

1. **算术操作符**：如加法、乘法、取模等
2. **比较操作符**：如等于、大于、小于等
3. **位操作符**：如按位与、按位或、左移等
4. **逻辑操作符**：如与、或、非
5. **序列操作符**：如索引、切片、连接等
6. **属性和元素访问操作符**：如获取属性、获取项
7. **真值测试函数**：如truth、is_not

## 2. 算术操作符

### 2.1 基本算术运算

```python
import operator

# 加法
a = operator.add(3, 5)  # 相当于 3 + 5
print(f"加法: {a}")  # 输出: 8

# 减法
b = operator.sub(10, 4)  # 相当于 10 - 4
print(f"减法: {b}")  # 输出: 6

# 乘法
c = operator.mul(6, 7)  # 相当于 6 * 7
print(f"乘法: {c}")  # 输出: 42

# 除法
d = operator.truediv(20, 4)  # 相当于 20 / 4
print(f"真除法: {d}")  # 输出: 5.0

# 整除
e = operator.floordiv(20, 3)  # 相当于 20 // 3
print(f"整除: {e}")  # 输出: 6

# 取模
f = operator.mod(17, 5)  # 相当于 17 % 5
print(f"取模: {f}")  # 输出: 2

# 幂运算
g = operator.pow(2, 10)  # 相当于 2 ** 10
print(f"幂运算: {g}")  # 输出: 1024
```

### 2.2 负数和绝对值

```python
import operator

# 取负数
neg_value = operator.neg(8)  # 相当于 -8
print(f"负数: {neg_value}")  # 输出: -8

# 取正数（不改变值，但确保是数字）
pos_value = operator.pos(-7)  # 相当于 +(-7)，仍为 -7
print(f"正数: {pos_value}")  # 输出: -7

# 取绝对值
abs_value = operator.abs(-10)  # 相当于 abs(-10)
print(f"绝对值: {abs_value}")  # 输出: 10
```

## 3. 比较操作符

```python
import operator

# 等于
equal = operator.eq(5, 5)  # 相当于 5 == 5
print(f"等于: {equal}")  # 输出: True

# 不等于
not_equal = operator.ne(5, 6)  # 相当于 5 != 6
print(f"不等于: {not_equal}")  # 输出: True

# 大于
greater = operator.gt(10, 7)  # 相当于 10 > 7
print(f"大于: {greater}")  # 输出: True

# 大于等于
greater_eq = operator.ge(10, 10)  # 相当于 10 >= 10
print(f"大于等于: {greater_eq}")  # 输出: True

# 小于
less = operator.lt(3, 7)  # 相当于 3 < 7
print(f"小于: {less}")  # 输出: True

# 小于等于
less_eq = operator.le(3, 3)  # 相当于 3 <= 3
print(f"小于等于: {less_eq}")  # 输出: True
```

## 4. 位操作符

```python
import operator

# 按位与
bit_and = operator.and_(0b1010, 0b1100)  # 相当于 0b1010 & 0b1100
print(f"按位与: {bin(bit_and)}")  # 输出: 0b1000

# 按位或
bit_or = operator.or_(0b1010, 0b1100)  # 相当于 0b1010 | 0b1100
print(f"按位或: {bin(bit_or)}")  # 输出: 0b1110

# 按位异或
bit_xor = operator.xor(0b1010, 0b1100)  # 相当于 0b1010 ^ 0b1100
print(f"按位异或: {bin(bit_xor)}")  # 输出: 0b0110

# 按位取反
bit_invert = operator.inv(0b1010)  # 相当于 ~0b1010
print(f"按位取反: {bin(bit_invert)}")  # 输出: -0b1011（在Python中为补码表示）

# 左移
left_shift = operator.lshift(5, 2)  # 相当于 5 << 2
print(f"左移: {left_shift}")  # 输出: 20

# 右移
right_shift = operator.rshift(20, 2)  # 相当于 20 >> 2
print(f"右移: {right_shift}")  # 输出: 5
```

## 5. 逻辑操作符

```python
import operator

# 逻辑与（注意：不是短路操作符）
logical_and = operator.and_(True, False)  # 相当于 True & False
print(f"逻辑与: {logical_and}")  # 输出: False

# 逻辑或（注意：不是短路操作符）
logical_or = operator.or_(True, False)  # 相当于 True | False
print(f"逻辑或: {logical_or}")  # 输出: True

# 逻辑异或
logical_xor = operator.xor(True, False)  # 相当于 True ^ False
print(f"逻辑异或: {logical_xor}")  # 输出: True

# 逻辑非
logical_not = operator.not_(True)  # 相当于 not True
print(f"逻辑非: {logical_not}")  # 输出: False
```

## 6. 序列操作符

### 6.1 索引和切片

```python
import operator

# 获取单个元素（索引操作）
sequence = [10, 20, 30, 40, 50]
elem = operator.getitem(sequence, 2)  # 相当于 sequence[2]
print(f"索引获取: {elem}")  # 输出: 30

# 设置单个元素
operator.setitem(sequence, 1, 200)  # 相当于 sequence[1] = 200
print(f"设置后序列: {sequence}")  # 输出: [10, 200, 30, 40, 50]

# 删除元素
operator.delitem(sequence, 3)  # 相当于 del sequence[3]
print(f"删除后序列: {sequence}")  # 输出: [10, 200, 30, 50]

# 切片操作
slice_result = operator.getitem(sequence, slice(1, 4))  # 相当于 sequence[1:4]
print(f"切片结果: {slice_result}")  # 输出: [200, 30, 50]
```

### 6.2 序列连接和重复

```python
import operator

# 序列连接
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = operator.concat(list1, list2)  # 相当于 list1 + list2
print(f"连接结果: {concatenated}")  # 输出: [1, 2, 3, 4, 5, 6]

# 序列重复
repeated = operator.concat([7], [7])  # 相当于 [7] + [7]，但不是 [7] * 2
print(f"重复结果: {repeated}")  # 输出: [7, 7]

# 注意：对于序列重复，operator模块没有直接对应 * 操作符的函数
# 可以使用以下方式实现
repeated_properly = operator.concat([8] * 3, [])  # 间接实现 [8] * 3
print(f"正确重复: {repeated_properly}")  # 输出: [8, 8, 8]
```

## 7. 属性和元素访问操作符

### 7.1 属性访问

```python
import operator

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

# 获取属性
name = operator.attrgetter('name')(person)  # 相当于 person.name
age = operator.attrgetter('age')(person)  # 相当于 person.age
print(f"姓名: {name}, 年龄: {age}")  # 输出: 姓名: Alice, 年龄: 30

# 设置属性
operator.setattr(person, 'age', 31)  # 相当于 person.age = 31
print(f"更新后年龄: {person.age}")  # 输出: 31

# 删除属性
operator.delattr(person, 'age')  # 相当于 del person.age
# print(person.age)  # 会抛出 AttributeError
```

### 7.2 元素访问器（用于排序和映射）

```python
import operator

# 创建元素访问器
get_second = operator.itemgetter(1)

# 使用访问器获取列表元素
values = [10, 20, 30, 40]
second_value = get_second(values)  # 相当于 values[1]
print(f"第二个元素: {second_value}")  # 输出: 20

# 使用访问器获取字典值
person = {'name': 'Bob', 'age': 25, 'city': 'New York'}
get_name = operator.itemgetter('name')
get_age = operator.itemgetter('age')
print(f"姓名: {get_name(person)}, 年龄: {get_age(person)}")  # 输出: 姓名: Bob, 年龄: 25

# 一次获取多个元素
get_multiple = operator.itemgetter(0, 2)
multi_values = get_multiple([1, 2, 3, 4])
print(f"多个元素: {multi_values}")  # 输出: (1, 3)

# 用于排序
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# 按年龄排序
people_sorted_by_age = sorted(people, key=operator.itemgetter('age'))
print(f"按年龄排序: {people_sorted_by_age}")
```

## 8. 真值测试和身份比较

```python
import operator

# 真值测试
truthy = operator.truth("hello")  # 相当于 bool("hello")
falsey = operator.truth("")  # 相当于 bool("")
print(f"非空字符串真值: {truthy}")  # 输出: True
print(f"空字符串真值: {falsey}")  # 输出: False

# 身份测试（is）
is_same = operator.is_(None, None)  # 相当于 None is None
print(f"身份相同: {is_same}")  # 输出: True

# 非身份测试（is not）
is_not_same = operator.is_not([], [])  # 相当于 [] is not []
print(f"身份不同: {is_not_same}")  # 输出: True
```

## 9. 在函数式编程中的应用

### 9.1 与高阶函数配合使用

```python
import operator
from functools import reduce

# 使用operator.add代替lambda x, y: x + y
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(operator.add, numbers)
print(f"列表求和: {sum_result}")  # 输出: 15

# 使用operator.mul计算阶乘
factorial = reduce(operator.mul, range(1, 6))
print(f"5的阶乘: {factorial}")  # 输出: 120

# 使用operator.itemgetter进行排序
students = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 78),
    ('David', 90)
]

# 按分数排序
students_sorted = sorted(students, key=operator.itemgetter(1), reverse=True)
print("按分数降序排序:")
for name, score in students_sorted:
    print(f"{name}: {score}")
```

### 9.2 创建数据转换管道

```python
import operator
from functools import partial
from itertools import filterfalse, accumulate

# 创建操作符函数的部分应用
get_age = operator.itemgetter('age')
older_than_30 = partial(operator.gt, 30)

# 数据处理管道
def process_people(people_data):
    # 提取年龄
    ages = map(get_age, people_data)
    # 过滤小于等于30岁的
    older_ages = filterfalse(partial(operator.le, 30), ages)
    # 计算累积和
    cumulative_sum = accumulate(older_ages, operator.add)
    return cumulative_sum

# 测试数据
people = [
    {'name': 'Alice', 'age': 28},
    {'name': 'Bob', 'age': 35},
    {'name': 'Charlie', 'age': 42},
    {'name': 'David', 'age': 29},
    {'name': 'Eve', 'age': 31}
]

# 处理数据
result = list(process_people(people))
print(f"处理结果: {result}")  # 输出: [35, 77, 108]
```

### 9.3 实现多属性排序

```python
import operator

# 示例数据
products = [
    {'category': 'electronics', 'name': 'phone', 'price': 599},
    {'category': 'electronics', 'name': 'laptop', 'price': 999},
    {'category': 'clothing', 'name': 'shirt', 'price': 29},
    {'category': 'clothing', 'name': 'jacket', 'price': 199},
    {'category': 'electronics', 'name': 'tablet', 'price': 399}
]

# 按类别升序、价格降序排序
products_sorted = sorted(products, key=operator.itemgetter('category', 'price'), reverse=False)

# 或者使用多个键
products_sorted_alt = sorted(
    products,
    key=lambda x: (x['category'], -x['price'])  # 类别升序，价格降序
)

print("按类别和价格排序:")
for product in products_sorted_alt:
    print(f"{product['category']} - {product['name']}: ${product['price']}")
```

## 10. 性能比较

operator模块的函数通常比等效的lambda函数执行得更快，因为它们是用C实现的。

```python
import operator
import time
from functools import reduce

def benchmark():
    # 测试数据
    numbers = list(range(1, 1000000))
    
    # 使用lambda函数
    start = time.time()
    sum_lambda = reduce(lambda x, y: x + y, numbers)
    lambda_time = time.time() - start
    
    # 使用operator.add
    start = time.time()
    sum_operator = reduce(operator.add, numbers)
    operator_time = time.time() - start
    
    print(f"Lambda函数求和: {sum_lambda}, 用时: {lambda_time:.6f}秒")
    print(f"operator.add求和: {sum_operator}, 用时: {operator_time:.6f}秒")
    print(f"性能提升: {(lambda_time - operator_time) / lambda_time * 100:.2f}%")

# 运行基准测试
benchmark()
```

## 11. 最佳实践和注意事项

1. **优先使用operator函数代替lambda**：
   - 提高代码可读性
   - 通常有更好的性能
   - 减少样板代码

2. **与functools和itertools结合使用**：
   - `operator.itemgetter`和`operator.attrgetter`在排序和映射操作中特别有用
   - `operator`函数与`reduce`等高阶函数配合效果极佳

3. **注意位操作符和逻辑操作符的区别**：
   - `operator.and_`、`operator.or_`执行的是位操作，不是短路逻辑操作
   - 使用短路逻辑时，仍需使用Python的内置`and`、`or`、`not`关键字

4. **使用`partial`创建专用操作符**：
   - 对于频繁使用的特定操作，考虑使用`functools.partial`创建专用函数

5. **在数据处理管道中使用**：
   - operator函数可以构建清晰的数据转换管道
   - 配合`map`、`filter`等函数使用，创建声明式的数据处理流程

## 12. 总结

operator模块为Python的函数式编程提供了强大的支持，通过提供标准操作符的函数形式，使开发者能够：

- 编写更简洁、更可读的函数式代码
- 利用预定义函数提高性能
- 轻松地与高阶函数结合使用
- 创建清晰的数据处理管道

在处理集合操作、排序、映射和归约等任务时，operator模块是一个不可或缺的工具，它使函数式编程风格在Python中更加自然和高效。通过将operator模块与functools和itertools模块结合使用，可以实现复杂的数据处理逻辑，同时保持代码的优雅和可读性。