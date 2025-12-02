"""
# itertools模块详解：高效迭代器工具集

itertools模块提供了用于创建高效迭代器的函数，这些函数在函数式编程范式中扮演着重要角色。通过这些工具，开发者可以实现惰性计算、函数组合和数据流处理，从而编写更高效、更优雅的代码。

## 1. 核心功能概览

itertools模块主要提供以下几类迭代器函数：

1. **无限迭代器**：生成无限序列的迭代器
2. **有限迭代器**：操作和转换输入迭代器的迭代器
3. **组合迭代器**：用于生成排列、组合和笛卡尔积的迭代器

## 2. 无限迭代器

### 2.1 itertools.count - 无限计数器

`count`函数创建一个从指定起点开始，以指定步长递增的无限迭代器。

```python
from itertools import count

# 创建从10开始，步长为2的计数器
counter = count(start=10, step=2)

# 获取前5个值
first_five = [next(counter) for _ in range(5)]
print(f"前5个值: {first_five}")  # 输出: [10, 12, 14, 16, 18]

# 与zip结合使用，为序列添加索引
names = ['Alice', 'Bob', 'Charlie']
indexed_names = list(zip(count(1), names))
print(f"带索引的名字: {indexed_names}")  # 输出: [(1, 'Alice'), (2, 'Bob'), (3, 'Charlie')]
```

### 2.2 itertools.cycle - 循环迭代器

`cycle`函数创建一个无限循环遍历输入迭代器内容的迭代器。

```python
from itertools import cycle

# 创建循环遍历['red', 'green', 'blue']的迭代器
color_cycle = cycle(['red', 'green', 'blue'])

# 获取前7个颜色值
colors = [next(color_cycle) for _ in range(7)]
print(f"颜色序列: {colors}")  # 输出: ['red', 'green', 'blue', 'red', 'green', 'blue', 'red']

# 为数据列表交替添加标记
values = [10, 20, 30, 40, 50]
tags = cycle(['+', '-'])
marked_values = [(next(tags), value) for value in values]
print(f"带标记的值: {marked_values}")  # 输出: [('+', 10), ('-', 20), ('+', 30), ('-', 40), ('+', 50)]
```

### 2.3 itertools.repeat - 重复迭代器

`repeat`函数创建一个重复产生指定值的迭代器，可以指定重复次数或无限重复。

```python
from itertools import repeat

# 重复'hello' 3次
hello_repeats = list(repeat('hello', 3))
print(f"重复3次: {hello_repeats}")  # 输出: ['hello', 'hello', 'hello']

# 无限重复42
forty_two = repeat(42)
first_ten = [next(forty_two) for _ in range(10)]
print(f"前10个值: {first_ten}")  # 输出: [42, 42, 42, 42, 42, 42, 42, 42, 42, 42]

# 与map结合使用，为多个值应用相同的参数
def multiply(x, y):
    return x * y

# 将每个数字乘以5
results = list(map(multiply, [1, 2, 3, 4, 5], repeat(5)))
print(f"乘法结果: {results}")  # 输出: [5, 10, 15, 20, 25]
```

## 3. 有限迭代器

### 3.1 序列操作迭代器

#### 3.1.1 itertools.accumulate - 累积迭代器

`accumulate`函数创建一个迭代器，返回累计汇总值。

```python
from itertools import accumulate
import operator

# 默认累加
numbers = [1, 2, 3, 4, 5]
sums = list(accumulate(numbers))
print(f"累计和: {sums}")  # 输出: [1, 3, 6, 10, 15]

# 使用乘法
products = list(accumulate(numbers, operator.mul))
print(f"累计积: {products}")  # 输出: [1, 2, 6, 24, 120]

# 使用自定义函数
max_values = list(accumulate([3, 1, 4, 1, 5, 9], max))
print(f"累计最大值: {max_values}")  # 输出: [3, 3, 4, 4, 5, 9]
```

#### 3.1.2 itertools.chain - 链式迭代器

`chain`函数创建一个迭代器，按顺序遍历多个迭代器。

```python
from itertools import chain

# 连接多个列表
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False]

combined = list(chain(list1, list2, list3))
print(f"组合结果: {combined}")  # 输出: [1, 2, 3, 'a', 'b', 'c', True, False]

# 使用chain.from_iterable处理可迭代的可迭代对象
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened = list(chain.from_iterable(nested_list))
print(f"扁平化结果: {flattened}")  # 输出: [1, 2, 3, 4, 5, 6]
```

#### 3.1.3 itertools.compress - 条件筛选迭代器

`compress`函数创建一个迭代器，根据选择器的值过滤元素。

```python
from itertools import compress

# 原始数据
data = ['a', 'b', 'c', 'd', 'e']
# 选择器（布尔值列表）
selectors = [True, False, True, False, True]

# 筛选结果
result = list(compress(data, selectors))
print(f"筛选结果: {result}")  # 输出: ['a', 'c', 'e']

# 使用列表推导式作为选择器
numbers = [10, 22, 35, 47, 53]
# 选择偶数
is_even = [x % 2 == 0 for x in numbers]
even_numbers = list(compress(numbers, is_even))
print(f"偶数: {even_numbers}")  # 输出: [10, 22]
```

#### 3.1.4 itertools.dropwhile - 丢弃满足条件的元素

`dropwhile`函数创建一个迭代器，丢弃满足条件的元素，直到找到不满足条件的元素，然后返回后续所有元素。

```python
from itertools import dropwhile

# 丢弃所有小于10的元素，直到找到第一个不小于10的元素
numbers = [3, 7, 9, 10, 5, 15, 8]
greater_than_10 = list(dropwhile(lambda x: x < 10, numbers))
print(f"结果: {greater_than_10}")  # 输出: [10, 5, 15, 8]

# 注意：只检查开头的元素，一旦找到不满足条件的元素，后续所有元素都会被返回
```

#### 3.1.5 itertools.takewhile - 获取满足条件的元素

`takewhile`函数与`dropwhile`相反，创建一个迭代器，返回满足条件的元素，直到找到不满足条件的元素为止。

```python
from itertools import takewhile

# 只获取小于10的元素，直到遇到第一个不小于10的元素
numbers = [3, 7, 9, 10, 5, 15, 8]
less_than_10 = list(takewhile(lambda x: x < 10, numbers))
print(f"结果: {less_than_10}")  # 输出: [3, 7, 9]

# 处理字符串
text = "abc123def"
alpha_chars = list(takewhile(lambda x: x.isalpha(), text))
print(f"字母字符: {alpha_chars}")  # 输出: ['a', 'b', 'c']
```

#### 3.1.6 itertools.filterfalse - 过滤不满足条件的元素

`filterfalse`函数创建一个迭代器，返回不满足条件的元素，与内置的`filter`函数相反。

```python
from itertools import filterfalse

# 过滤所有偶数，返回奇数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filterfalse(lambda x: x % 2 == 0, numbers))
print(f"奇数: {odd_numbers}")  # 输出: [1, 3, 5, 7, 9]

# 过滤非空字符串
strings = ["hello", "", "world", "", "python"]
non_empty = list(filterfalse(lambda x: x == "", strings))
print(f"非空字符串: {non_empty}")  # 输出: ['hello', 'world', 'python']
```

#### 3.1.7 itertools.starmap - 带星号的映射

`starmap`函数创建一个迭代器，将可迭代对象中的每个元素作为参数元组解包后传给指定函数。

```python
from itertools import starmap

def multiply(a, b):
    return a * b

# 应用函数到多个参数元组
pairs = [(2, 3), (4, 5), (6, 7)]
results = list(starmap(multiply, pairs))
print(f"乘法结果: {results}")  # 输出: [6, 20, 42]

# 使用内置函数
from operator import sub
differences = list(starmap(sub, [(10, 5), (20, 7), (30, 15)]))
print(f"差值: {differences}")  # 输出: [5, 13, 15]
```

#### 3.1.8 itertools.tee - 复制迭代器

`tee`函数创建指定数量的迭代器，这些迭代器都从原始迭代器的当前位置开始迭代。

```python
from itertools import tee

# 创建一个迭代器
original = range(10)

# 复制为3个迭代器
it1, it2, it3 = tee(original, 3)

# 每个迭代器都是独立的
print(f"it1的前3个元素: {[next(it1) for _ in range(3)]}")  # 输出: [0, 1, 2]
print(f"it2的前5个元素: {[next(it2) for _ in range(5)]}")  # 输出: [0, 1, 2, 3, 4]
print(f"it3的前2个元素: {[next(it3) for _ in range(2)]}")  # 输出: [0, 1]

# 注意：tee创建的迭代器共享底层数据，应避免在创建后再使用原始迭代器
```

#### 3.1.9 itertools.zip_longest - 最长长度的zip

`zip_longest`函数创建一个迭代器，聚合多个可迭代对象的元素，直到所有可迭代对象都被耗尽。

```python
from itertools import zip_longest

# 不等长的列表
list1 = [1, 2, 3]
list2 = ['a', 'b']
list3 = [True, False, None, 'extra']

# 使用默认填充值
combined = list(zip_longest(list1, list2, list3))
print(f"默认填充: {combined}")  # 输出: [(1, 'a', True), (2, 'b', False), (3, None, None), (None, None, 'extra')]

# 指定填充值
combined_with_fill = list(zip_longest(list1, list2, fillvalue='N/A'))
print(f"指定填充值: {combined_with_fill}")  # 输出: [(1, 'a'), (2, 'b'), (3, 'N/A')]
```

## 4. 组合迭代器

### 4.1 itertools.product - 笛卡尔积

`product`函数创建一个迭代器，返回多个可迭代对象的笛卡尔积。

```python
from itertools import product

# 两个集合的笛卡尔积
colors = ['红', '蓝']
sizes = ['S', 'M', 'L']
combinations = list(product(colors, sizes))
print(f"笛卡尔积: {combinations}")  # 输出: [('红', 'S'), ('红', 'M'), ('红', 'L'), ('蓝', 'S'), ('蓝', 'M'), ('蓝', 'L')]

# 带重复的笛卡尔积（相当于自己与自己的笛卡尔积）
digits = [1, 2]
square = list(product(digits, repeat=2))
print(f"带重复的笛卡尔积: {square}")  # 输出: [(1, 1), (1, 2), (2, 1), (2, 2)]

# 三个集合的笛卡尔积
shapes = ['圆形', '方形']
combinations_3d = list(product(colors, sizes, shapes))
print(f"三维笛卡尔积元素数量: {len(combinations_3d)}")  # 输出: 12
```

### 4.2 itertools.permutations - 排列

`permutations`函数创建一个迭代器，返回可迭代对象中所有长度为r的排列。

```python
from itertools import permutations

# 从4个元素中取2个的排列
letters = ['a', 'b', 'c', 'd']
perms = list(permutations(letters, 2))
print(f"排列数量: {len(perms)}")  # 输出: 12
print(f"前5个排列: {perms[:5]}")  # 输出: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c')]

# 所有元素的全排列
full_perms = list(permutations([1, 2, 3]))
print(f"全排列数量: {len(full_perms)}")  # 输出: 6
```

### 4.3 itertools.combinations - 组合

`combinations`函数创建一个迭代器，返回可迭代对象中所有长度为r的组合（不考虑顺序）。

```python
from itertools import combinations

# 从4个元素中取2个的组合
letters = ['a', 'b', 'c', 'd']
combs = list(combinations(letters, 2))
print(f"组合数量: {len(combs)}")  # 输出: 6
print(f"所有组合: {combs}")  # 输出: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

# 从5个元素中取3个的组合
numbers = [1, 2, 3, 4, 5]
triples = list(combinations(numbers, 3))
print(f"三元组数量: {len(triples)}")  # 输出: 10
```

### 4.4 itertools.combinations_with_replacement - 允许重复的组合

`combinations_with_replacement`函数创建一个迭代器，返回可迭代对象中所有长度为r的组合，允许元素重复使用。

```python
from itertools import combinations_with_replacement

# 允许重复的组合
colors = ['红', '蓝', '绿']
repeat_combs = list(combinations_with_replacement(colors, 2))
print(f"允许重复的组合数量: {len(repeat_combs)}")  # 输出: 6
print(f"所有组合: {repeat_combs}")  # 输出: [('红', '红'), ('红', '蓝'), ('红', '绿'), ('蓝', '蓝'), ('蓝', '绿'), ('绿', '绿')]

# 数字的重复组合
digits = [1, 2]
repeat_digit_combs = list(combinations_with_replacement(digits, 3))
print(f"数字重复组合: {repeat_digit_combs}")  # 输出: [(1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]
```

## 5. 高级应用示例

### 5.1 惰性数据流处理

使用itertools创建高效的惰性数据流处理管道。

```python
from itertools import filterfalse, accumulate, takewhile

# 创建一个惰性数据流处理管道
def process_data(data):
    # 1. 过滤掉负数
    positive_numbers = filterfalse(lambda x: x < 0, data)
    # 2. 计算累积和
    cumulative_sums = accumulate(positive_numbers)
    # 3. 只取累积和小于100的结果
    result = takewhile(lambda x: x < 100, cumulative_sums)
    return result

# 测试数据
data = [30, -5, 20, 15, -10, 25, 35, 40]

# 处理数据（惰性计算，只在需要时执行）
result = process_data(data)

# 转换为列表触发计算
print(list(result))  # 输出: [30, 50, 65, 90]
```

### 5.2 生成词频统计

结合多个itertools函数生成文本的词频统计。

```python
from itertools import groupby
from collections import Counter

def word_frequency(text):
    # 将文本拆分为单词并转为小写
    words = text.lower().split()
    # 按字母顺序排序以便groupby工作
    words.sort()
    # 使用groupby进行分组
    grouped_words = groupby(words)
    # 计算每个单词的频率
    frequencies = [(word, len(list(group))) for word, group in grouped_words]
    # 按频率降序排序
    frequencies.sort(key=lambda x: x[1], reverse=True)
    return frequencies

# 测试文本
text = "Hello world hello python world hello programming python hello world"
frequencies = word_frequency(text)
print("词频统计（前5个）:")
for word, freq in frequencies[:5]:
    print(f"{word}: {freq}")
```

### 5.3 生成所有可能的IP地址

使用product函数生成所有可能的IPv4地址组合。

```python
from itertools import product

def generate_ip_addresses():
    # 生成所有可能的IP地址段（0-255）
    octets = range(256)
    # 生成所有四个段的组合
    all_ips = product(octets, repeat=4)
    # 将组合转换为IP地址字符串
    return (f"{a}.{b}.{c}.{d}" for a, b, c, d in all_ips)

# 获取前10个IP地址
first_10_ips = [next(generate_ip_addresses()) for _ in range(10)]
print("前10个IP地址:")
for ip in first_10_ips:
    print(ip)
```

### 5.4 实现高效的集合操作

使用itertools实现高级集合操作。

```python
from itertools import chain, filterfalse

def symmetric_difference(set1, set2):
    """计算两个集合的对称差（仅在其中一个集合中出现的元素）"""
    # 计算差集：set1 - set2
    diff1 = filterfalse(set2.__contains__, set1)
    # 计算差集：set2 - set1
    diff2 = filterfalse(set1.__contains__, set2)
    # 合并两个差集
    return chain(diff1, diff2)

# 测试
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# 获取对称差
result = set(symmetric_difference(set_a, set_b))
print(f"对称差: {result}")  # 输出: {1, 2, 3, 6, 7, 8}
```

## 6. 性能考量与最佳实践

1. **惰性计算的优势**：
   - itertools的迭代器是惰性的，只在需要时计算值
   - 对于大型数据集，避免一次性加载所有数据到内存
   - 支持无限序列的处理

2. **内存效率**：
   - 迭代器通常比创建中间列表更节省内存
   - 使用`chain.from_iterable`代替列表推导式进行扁平化操作
   - 避免不必要的`list()`调用，保持惰性计算

3. **性能优化技巧**：
   - 使用内置函数和运算符模块中的函数代替lambda函数
   - 对于频繁使用的操作，考虑预计算或缓存结果
   - 避免在迭代器上多次迭代，必要时使用`tee`创建副本

4. **代码可读性**：
   - 为复杂的迭代器操作添加注释
   - 将复杂的迭代器组合封装到命名函数中
   - 平衡简洁性和可读性

## 7. 总结

itertools模块提供了丰富的迭代器工具，使开发者能够高效地处理各种序列操作。通过这些工具，我们可以：

- 创建高效的惰性计算管道
- 实现复杂的序列转换和过滤
- 生成组合数学中的各种排列和组合
- 优雅地处理无限序列和数据流

itertools模块的函数设计遵循了函数式编程的原则，强调组合性和不可变性，使代码更加声明式和易于理解。掌握这些工具对于编写高效、优雅的Python代码至关重要，特别是在处理大数据集或需要复杂序列操作的场景中。