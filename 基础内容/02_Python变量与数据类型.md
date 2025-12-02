# Python变量与数据类型

## 1. 变量的基本概念

变量是编程中用于存储数据的基本单位。在Python中，变量非常灵活，不需要预先声明类型。

### 变量的命名规则
- 变量名只能包含字母、数字和下划线
- 变量名不能以数字开头
- 变量名区分大小写
- 不能使用Python的关键字作为变量名

### 1. 私有变量补充（插入到变量命名规则后）

#### 私有变量的概念与用法

在Python中，变量名前加下划线有特殊含义：

- 单下划线 `_var`：表示“受保护变量”，约定仅类或模块内部使用，外部可访问但不推荐。
- 双下划线 `__var`：表示“私有变量”，会触发名称重整（name mangling），外部无法直接访问，推荐通过方法访问。

**示例：**
```python
class Demo:
    def __init__(self):
        self._protected = "受保护变量"
        self.__private = "私有变量"

    def get_private(self):
        return self.__private

obj = Demo()
print(obj._protected)           # 虽然可以访问，但不推荐
# print(obj.__private)          # 会报错
print(obj.get_private())        # 推荐方式
print(obj._Demo__private)       # 通过名称重整访问（不推荐）
```

### 变量赋值
Python中的变量赋值非常直观：

```python
# 基本赋值
x = 10
name = "李明"

# 多重赋值
a, b, c = 1, 2, 3

# 交换变量值（Python特有）
a, b = b, a  # a和b的值互换
```

## 2. Python的基本数据类型

### 数字类型
#### 整数（int）
Python的整数可以是任意大小，不受限制。

```python
age = 25
big_number = 123456789012345678901234567890
```

#### 浮点数（float）
用于表示小数。

```python
height = 1.75
pi = 3.14159
scientific = 1.23e4  # 科学计数法，等于12300.0
```

#### 复数（complex）
形式为`a + bj`，其中`a`和`b`是实数，`j`是虚数单位。

```python
z = 2 + 3j
```

### 字符串（str）
字符串是Unicode字符的序列，用单引号或双引号括起来。

```python
name = "王小明"
address = '北京市海淀区'

# 多行字符串
description = """这是一个
多行字符串
示例"""

# 字符串拼接
full_name = "张" + "三"  # "张三"

# 字符串重复
stars = "*" * 10  # "**********"

# 字符串切片
text = "Python编程"
first_char = text[0]  # "P"
substring = text[0:6]  # "Python"
```

### 布尔类型（bool）
只有两个值：`True`和`False`。

```python
is_student = True
has_car = False
```

### 列表（list）
有序、可变的集合，可以包含不同类型的元素。

```python
# 创建列表
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", True, 3.14]

# 访问列表元素
first = numbers[0]  # 1
last = numbers[-1]  # 5

# 切片
subset = numbers[1:4]  # [2, 3, 4]

# 修改列表
numbers[0] = 10  # 现在numbers是[10, 2, 3, 4, 5]
numbers.append(6)  # 添加元素，现在numbers是[10, 2, 3, 4, 5, 6]
numbers.insert(1, 15)  # 在索引1处插入15，现在numbers是[10, 15, 2, 3, 4, 5, 6]
numbers.remove(3)  # 删除值为3的元素
numbers.pop()  # 删除最后一个元素并返回它
```

### 元组（tuple）
有序、不可变的集合。

```python
# 创建元组
coordinates = (10, 20)
single_item = (42,)  # 单个元素的元组需要逗号

# 访问元组元素
x = coordinates[0]  # 10

# 元组不能被修改
# coordinates[0] = 15  # 这会引发错误
```

### 字典（dict）
键值对的集合，使用大括号定义。

```python
# 创建字典
person = {
    "name": "李华",
    "age": 30,
    "city": "上海"
}

# 访问字典值
name = person["name"]  # "李华"
age = person.get("age")  # 30
unknown = person.get("phone", "未知")  # 如果键不存在，返回默认值"未知"

# 修改字典
person["age"] = 31
person["phone"] = "12345678"  # 添加新键值对
```

### 集合（set）
无序、无重复元素的集合。

```python
# 创建集合
fruits = {"苹果", "香蕉", "橙子"}
numbers = {1, 2, 3, 3, 4, 4, 5}  # 结果是{1, 2, 3, 4, 5}，重复元素被自动去除

# 集合操作
fruits.add("梨")
fruits.remove("香蕉")

# 集合运算
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2  # 并集：{1, 2, 3, 4, 5}
intersection = set1 & set2  # 交集：{3}
difference = set1 - set2  # 差集：{1, 2}
```

## 3. 数据类型转换

Python提供了多种函数来实现数据类型之间的转换：

```python
# 字符串转数字
num_str = "123"
num_int = int(num_str)  # 123
num_float = float(num_str)  # 123.0

# 数字转字符串
num = 456
str_num = str(num)  # "456"

# 其他类型转换
float_to_int = int(3.9)  # 3（截断，不是四舍五入）
int_to_float = float(7)  # 7.0

# 转换为列表或元组
list_from_tuple = list((1, 2, 3))  # [1, 2, 3]
tuple_from_list = tuple([4, 5, 6])  # (4, 5, 6)

# 转换为集合（去除重复）
set_from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
```

## 4. 练习题

### 基础练习
1. 创建变量存储你的姓名、年龄和身高，并打印输出。
2. 尝试交换两个变量的值，不使用第三个变量。
3. 创建一个包含5个不同数据类型的列表。

### 进阶练习
1. 编写程序计算圆的面积和周长，用变量存储半径和结果。
2. 创建一个字典，包含5个学生的姓名和分数，然后计算平均分。
3. 使用集合操作找出两个列表中的共同元素。

### 编程挑战
编写一个简单的通讯录程序，使用字典存储联系人信息（姓名、电话、邮箱），并实现添加、查询、删除联系人的功能。

## 5. 解决方案

### 基础练习解答
```python
# 1. 创建个人信息变量
name = "王小明"
age = 25
height = 1.78
print(f"姓名: {name}, 年龄: {age}岁, 身高: {height}米")

# 2. 交换变量值
a = 10
b = 20
print(f"交换前: a = {a}, b = {b}")
a, b = b, a
print(f"交换后: a = {a}, b = {b}")

# 3. 不同数据类型的列表
mixed_list = [100, "Python", 3.14, True, [1, 2, 3]]
for i, item in enumerate(mixed_list):
    print(f"第{i+1}个元素: {item}, 类型: {type(item)}")
```

### 进阶练习解答
```python
# 1. 计算圆的面积和周长
import math

radius = 5
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius
print(f"半径为{radius}的圆:")
print(f"面积: {area:.2f}")
print(f"周长: {circumference:.2f}")

# 2. 学生分数字典
students = {
    "张三": 85,
    "李四": 92,
    "王五": 78,
    "赵六": 95,
    "钱七": 88
}

total_score = sum(students.values())
average = total_score / len(students)
print(f"学生平均分: {average:.2f}")

# 3. 查找共同元素
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
common = set(list1) & set(list2)
print(f"共同元素: {common}")
```

### 2. 变量与数据类型相关的其他常见知识点补充

#### 变量作用域
- **全局变量**：在函数外部定义，整个模块都可访问。
- **局部变量**：在函数内部定义，只能在函数内部访问。
- **global 关键字**：在函数内部声明全局变量。
- **nonlocal 关键字**：在嵌套函数中声明外层（非全局）变量。

**示例：**
```python
x = 10  # 全局变量

def func():
    global x
    x = 20  # 修改全局变量
    y = 5   # 局部变量
    print(y)

func()
print(x)  # 20
```

#### 不可变与可变类型
- **不可变类型**：int、float、str、tuple、frozenset
- **可变类型**：list、dict、set

**示例：**
```python
a = [1, 2, 3]
b = a
a.append(4)
print(b)  # [1, 2, 3, 4]，b也被修改（可变类型）

x = 10
y = x
x = 20
print(y)  # 10，不可变类型
```

#### 类型注解（Type Hint）
Python 3.5+ 支持类型注解，提升代码可读性和可维护性。

**示例：**
```python
def add(a: int, b: int) -> int:
    return a + b
```

#### None类型
- `None` 表示“空值”或“无值”，常用于函数无返回值或变量初始化。

**示例：**
```python
result = None
if result is None:
    print("没有结果")
```

#### bytes与bytearray
- `bytes`：不可变的字节序列
- `bytearray`：可变的字节序列

**示例：**
```python
b = b"hello"
ba = bytearray(b"world")
ba[0] = 87  # 修改为大写W
print(ba)  # bytearray(b'World')
```
