# json模块详解

json模块是Python标准库中用于处理JSON（JavaScript Object Notation）格式数据的模块，提供了将Python对象与JSON数据之间进行转换的功能。JSON是一种轻量级的数据交换格式，易于阅读和编写，也易于机器解析和生成。

## 模块概述

json模块提供了以下主要功能：

- 将Python对象序列化为JSON字符串
- 将JSON字符串反序列化为Python对象
- 支持读取和写入JSON文件
- 支持自定义序列化和反序列化
- 支持各种数据类型的转换

## 基本用法

### 导入模块

```python
import json
import os
```

### JSON数据类型与Python数据类型的对应关系

| JSON数据类型 | Python数据类型 |
|--------------|----------------|
| object       | dict           |
| array        | list, tuple    |
| string       | str            |
| number (int) | int            |
| number (real)| float          |
| true         | True           |
| false        | False          |
| null         | None           |

### 将Python对象转换为JSON字符串（序列化）

```python
# 创建Python对象
python_data = {
    "name": "张三",
    "age": 25,
    "is_student": False,
    "scores": [85, 90, 88],
    "address": {
        "city": "北京",
        "district": "朝阳区",
        "street": "建国路"
    },
    "phone_numbers": ("13800138001", "13800138002"),
    "email": None
}

# 将Python对象转换为JSON字符串
json_str = json.dumps(python_data)
print("Python对象转换为JSON字符串:")
print(json_str)
print(f"类型: {type(json_str)}")

# 美化输出，增加缩进和排序
pretty_json_str = json.dumps(python_data, indent=4, sort_keys=True)
print("\n美化后的JSON字符串:")
print(pretty_json_str)

# 设置中文字符的输出
chinese_json_str = json.dumps(python_data, ensure_ascii=False, indent=4)
print("\n保留中文字符的JSON字符串:")
print(chinese_json_str)
```

### 将JSON字符串转换为Python对象（反序列化）

```python
# JSON字符串
json_str = '{
    "name": "李四",
    "age": 30,
    "is_student": false,
    "scores": [82, 87, 91],
    "address": {
        "city": "上海",
        "district": "浦东新区",
        "street": "陆家嘴"
    },
    "phone_numbers": ["13900139001", "13900139002"],
    "email": "lisi@example.com"
}'

# 将JSON字符串转换为Python对象
python_obj = json.loads(json_str)
print("JSON字符串转换为Python对象:")
print(python_obj)
print(f"类型: {type(python_obj)}")
print(f"姓名: {python_obj['name']}, 年龄: {python_obj['age']}, 城市: {python_obj['address']['city']}")

# 转换包含数组的JSON字符串
json_array_str = '[1, 2, 3, 4, 5, "hello", null, true, false]'
python_array = json.loads(json_array_str)
print("\nJSON数组转换为Python对象:")
print(python_array)
print(f"类型: {type(python_array)}")
print(f"元素类型: {[type(item).__name__ for item in python_array]}")
```

### 读取和写入JSON文件

```python
# 创建Python对象
student_data = {
    "students": [
        {
            "id": 1,
            "name": "张三",
            "gender": "男",
            "age": 25,
            "major": "计算机科学",
            "scores": {
                "语文": 85,
                "数学": 90,
                "英语": 88
            }
        },
        {
            "id": 2,
            "name": "李四",
            "gender": "女",
            "age": 23,
            "major": "软件工程",
            "scores": {
                "语文": 82,
                "数学": 87,
                "英语": 91
            }
        },
        {
            "id": 3,
            "name": "王五",
            "gender": "男",
            "age": 24,
            "major": "数据科学",
            "scores": {
                "语文": 88,
                "数学": 92,
                "英语": 89
            }
        }
    ]
}

# 写入JSON文件
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(student_data, f, ensure_ascii=False, indent=4)

print("\nJSON文件写入完成")

# 读取JSON文件
with open("students.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("JSON文件读取结果:")
for student in loaded_data["students"]:
    print(f"  ID: {student['id']}, 姓名: {student['name']}, 专业: {student['major']}, 数学成绩: {student['scores']['数学']}")
```

## 高级功能

### 自定义序列化（default参数）

```python
# 定义一个自定义类
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# 创建Person对象
person = Person("赵六", 28, "深圳市南山区科技园")

# 尝试直接序列化Person对象（会失败）
try:
    json_str = json.dumps(person)
    print(json_str)
except TypeError as e:
    print(f"\n直接序列化失败: {e}")

# 使用default参数自定义序列化函数
def person_to_dict(obj):
    if isinstance(obj, Person):
        return {
            "name": obj.name,
            "age": obj.age,
            "address": obj.address
        }
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# 使用自定义序列化函数
json_str = json.dumps(person, default=person_to_dict, ensure_ascii=False, indent=4)
print("\n使用自定义序列化函数的结果:")
print(json_str)

# 使用lambda函数简化
default_func = lambda obj: obj.__dict__ if hasattr(obj, "__dict__") else str(obj)
json_str = json.dumps(person, default=default_func, ensure_ascii=False, indent=4)
print("\n使用lambda函数的结果:")
print(json_str)
```

### 自定义反序列化（object_hook参数）

```python
# JSON字符串
json_str = '{
    "name": "孙七",
    "age": 32,
    "address": "广州市天河区珠江新城"
}'

# 定义一个自定义类
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, address={self.address})"

# 使用object_hook参数自定义反序列化函数
def dict_to_person(d):
    if "name" in d and "age" in d and "address" in d:
        return Person(d["name"], d["age"], d["address"])
    return d

# 使用自定义反序列化函数
person = json.loads(json_str, object_hook=dict_to_person)
print("\n使用自定义反序列化函数的结果:")
print(person)
print(f"类型: {type(person)}")
print(f"姓名: {person.name}, 年龄: {person.age}, 地址: {person.address}")
```

### 使用JSONEncoder和JSONDecoder类

```python
# 定义一个自定义类
class Student:
    def __init__(self, id, name, courses):
        self.id = id
        self.name = name
        self.courses = courses

# 自定义JSONEncoder类
class StudentEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return {
                "id": obj.id,
                "name": obj.name,
                "courses": obj.courses,
                "__student__": True
            }
        return super().default(obj)

# 自定义JSONDecoder类
class StudentDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.dict_to_student, *args, **kwargs)
    
    def dict_to_student(self, d):
        if "__student__" in d:
            return Student(d["id"], d["name"], d["courses"])
        return d

# 创建Student对象
student = Student(101, "周八", ["数学", "英语", "计算机科学"])

# 使用自定义JSONEncoder序列化
json_str = json.dumps(student, cls=StudentEncoder, ensure_ascii=False, indent=4)
print("\n使用自定义JSONEncoder序列化的结果:")
print(json_str)

# 使用自定义JSONDecoder反序列化
student_obj = json.loads(json_str, cls=StudentDecoder)
print("\n使用自定义JSONDecoder反序列化的结果:")
print(student_obj)
print(f"类型: {type(student_obj)}")
print(f"ID: {student_obj.id}, 姓名: {student_obj.name}, 课程: {student_obj.courses}")
```

## 实际应用示例

### 示例1：配置文件管理

```python
# 创建配置数据
config = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "debug": True,
    "server": {
        "host": "localhost",
        "port": 8080,
        "timeout": 30
    },
    "database": {
        "type": "mysql",
        "host": "localhost",
        "port": 3306,
        "username": "root",
        "password": "password",
        "dbname": "myapp"
    },
    "log": {
        "level": "INFO",
        "file": "app.log",
        "max_size": 10485760  # 10MB
    },
    "allowed_users": ["admin", "user1", "user2"]
}

# 写入配置文件
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=4)

print("\n配置文件写入完成")

# 读取配置文件
with open("config.json", "r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print("配置文件读取结果:")
print(f"  应用名称: {loaded_config['app_name']}")
print(f"  版本: {loaded_config['version']}")
print(f"  调试模式: {loaded_config['debug']}")
print(f"  服务器地址: {loaded_config['server']['host']}:{loaded_config['server']['port']}")
print(f"  数据库类型: {loaded_config['database']['type']}")
print(f"  日志级别: {loaded_config['log']['level']}")

# 更新配置文件
loaded_config["server"]["port"] = 9090
loaded_config["log"]["level"] = "DEBUG"

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(loaded_config, f, ensure_ascii=False, indent=4)

print("\n配置文件更新完成")

# 验证更新后的配置
with open("config.json", "r", encoding="utf-8") as f:
    updated_config = json.load(f)

print(f"  更新后的服务器端口: {updated_config['server']['port']}")
print(f"  更新后的日志级别: {updated_config['log']['level']}")
```

### 示例2：API数据处理

```python
# 模拟API返回的JSON数据
api_response = '''
{
    "status": "success",
    "code": 200,
    "message": "请求成功",
    "data": {
        "total": 2,
        "items": [
            {
                "id": 1,
                "title": "Python编程入门",
                "author": "张三",
                "price": 89.9,
                "publish_date": "2023-01-01",
                "tags": ["Python", "编程", "入门"]
            },
            {
                "id": 2,
                "title": "Python数据分析",
                "author": "李四",
                "price": 129.9,
                "publish_date": "2023-03-15",
                "tags": ["Python", "数据分析", "Pandas"]
            }
        ]
    },
    "timestamp": "2023-10-01T12:00:00Z"
}
'''

# 解析API响应
data = json.loads(api_response)

# 检查请求状态
if data["status"] == "success" and data["code"] == 200:
    print("\nAPI请求成功")
    print(f"  消息: {data['message']}")
    print(f"  时间戳: {data['timestamp']}")
    
    # 处理数据
    items = data["data"]["items"]
    print(f"  共找到 {len(items)} 本书:")
    
    for item in items:
        print(f"    书名: {item['title']}")
        print(f"    作者: {item['author']}")
        print(f"    价格: {item['price']}元")
        print(f"    出版日期: {item['publish_date']}")
        print(f"    标签: {', '.join(item['tags'])}")
        print()
        
    # 计算平均价格
    total_price = sum(item["price"] for item in items)
    average_price = total_price / len(items)
    print(f"  平均价格: {average_price:.2f}元")
    
    # 查找特定标签的书籍
    pandas_books = [item for item in items if "Pandas" in item["tags"]]
    print(f"  包含'Pandas'标签的书籍: {len(pandas_books)}本")
    for book in pandas_books:
        print(f"    - {book['title']}")
else:
    print(f"\nAPI请求失败: {data['message']} (状态码: {data['code']})")
```

### 示例3：数据存储与分析

```python
# 创建销售数据
sales_data = {
    "sales": [
        {
            "date": "2023-01-01",
            "product_id": "P001",
            "product_name": "笔记本电脑",
            "category": "电子设备",
            "price": 5999,
            "quantity": 10,
            "total": 59990,
            "region": "华北"
        },
        {
            "date": "2023-01-01",
            "product_id": "P002",
            "product_name": "智能手机",
            "category": "电子设备",
            "price": 3999,
            "quantity": 20,
            "total": 79980,
            "region": "华南"
        },
        {
            "date": "2023-01-02",
            "product_id": "P003",
            "product_name": "平板电脑",
            "category": "电子设备",
            "price": 2999,
            "quantity": 15,
            "total": 44985,
            "region": "华东"
        },
        {
            "date": "2023-01-02",
            "product_id": "P004",
            "product_name": "无线耳机",
            "category": "配件",
            "price": 999,
            "quantity": 30,
            "total": 29970,
            "region": "华北"
        },
        {
            "date": "2023-01-03",
            "product_id": "P005",
            "product_name": "智能手表",
            "category": "配件",
            "price": 1999,
            "quantity": 25,
            "total": 49975,
            "region": "华南"
        }
    ]
}

# 写入销售数据到JSON文件
with open("sales_data.json", "w", encoding="utf-8") as f:
    json.dump(sales_data, f, ensure_ascii=False, indent=4)

print("\n销售数据写入完成")

# 读取销售数据
with open("sales_data.json", "r", encoding="utf-8") as f:
    loaded_sales_data = json.load(f)

# 数据分析
sales = loaded_sales_data["sales"]

# 计算总销售额
total_sales = sum(item["total"] for item in sales)
print(f"\n总销售额: {total_sales}元")

# 计算平均销售额
average_sales = total_sales / len(sales)
print(f"平均销售额: {average_sales:.2f}元")

# 按地区统计销售额
region_sales = {}
for item in sales:
    region = item["region"]
    if region not in region_sales:
        region_sales[region] = 0
    region_sales[region] += item["total"]

print("\n按地区统计销售额:")
for region, amount in region_sales.items():
    print(f"  {region}: {amount}元")

# 按产品类别统计销售额
category_sales = {}
for item in sales:
    category = item["category"]
    if category not in category_sales:
        category_sales[category] = 0
    category_sales[category] += item["total"]

print("\n按产品类别统计销售额:")
for category, amount in category_sales.items():
    print(f"  {category}: {amount}元")

# 找出销售额最高的产品
highest_sale = max(sales, key=lambda x: x["total"])
print(f"\n销售额最高的产品:")
print(f"  产品名称: {highest_sale['product_name']}")
print(f"  销售额: {highest_sale['total']}元")
print(f"  销售数量: {highest_sale['quantity']}件")
print(f"  销售地区: {highest_sale['region']}")
```

## 配置参数

### json.dumps()和json.dump()的参数

| 参数 | 描述 | 默认值 |
|------|------|--------|
| obj | 要序列化的Python对象 | 必填 |
| skipkeys | 是否跳过非字符串类型的键 | False |
| ensure_ascii | 是否将非ASCII字符转义 | True |
| check_circular | 是否检查循环引用 | True |
| allow_nan | 是否允许NaN、Infinity和-Infinity | True |
| cls | 自定义的JSONEncoder子类 | None |
| indent | 缩进空格数 | None |
| separators | 分隔符元组(项分隔符, 键值分隔符) | (', ', ': ') |
| default | 自定义序列化函数 | None |
| sort_keys | 是否按键排序 | False |
| **kw | 其他关键字参数 | - |

### json.loads()和json.load()的参数

| 参数 | 描述 | 默认值 |
|------|------|--------|
| s | 要反序列化的JSON字符串 | 必填 |
| cls | 自定义的JSONDecoder子类 | None |
| object_hook | 自定义对象钩子函数 | None |
| parse_float | 解析浮点数的函数 | float |
| parse_int | 解析整数的函数 | int |
| parse_constant | 解析常量的函数 | None |
| object_pairs_hook | 自定义键值对钩子函数 | None |
| **kw | 其他关键字参数 | - |

## 最佳实践

1. **使用with语句**：始终使用with语句打开JSON文件，确保文件正确关闭
2. **指定编码**：始终指定文件的编码，特别是处理包含非ASCII字符的文件时
3. **使用ensure_ascii=False**：当JSON数据包含非ASCII字符（如中文）时，设置ensure_ascii=False可以保留原始字符
4. **使用indent参数**：在调试或生成人类可读的JSON文件时，使用indent参数增加缩进
5. **自定义序列化和反序列化**：当需要处理自定义类时，使用自定义的序列化和反序列化函数
6. **检查请求状态**：在处理API返回的JSON数据时，始终检查请求状态码和状态信息
7. **异常处理**：在解析JSON数据时，捕获并处理可能的异常（如json.JSONDecodeError）
8. **避免循环引用**：确保要序列化的Python对象不包含循环引用，否则会导致序列化失败
9. **使用合适的数据结构**：根据数据的结构选择合适的Python数据类型，如字典、列表等
10. **性能考虑**：对于大型JSON数据，考虑使用流式处理或分块处理

## 与其他模块的关系

- **pickle**：pickle模块用于Python对象的序列化和反序列化，与json模块类似，但pickle可以序列化更多Python数据类型，且生成的是二进制数据，而json生成的是文本数据
- **csv**：csv模块用于处理CSV格式的数据，可以与json模块结合使用进行不同格式数据的转换
- **yaml**：yaml模块用于处理YAML格式的数据，与json模块类似，但YAML格式更加灵活和易读
- **requests**：requests模块用于发送HTTP请求，通常与json模块结合使用处理API响应
- **pandas**：pandas库提供了更强大的数据处理功能，可以与json模块结合使用进行数据转换和分析

## 清理测试文件

```python
# 清理所有测试文件
for filename in [
    "students.json",
    "config.json",
    "sales_data.json"
]:
    if os.path.exists(filename):
        os.remove(filename)

print("\n所有测试文件已清理")
```

## 总结

json模块是Python标准库中用于处理JSON数据的强大工具，提供了将Python对象与JSON数据之间进行转换的功能。它支持读取和写入JSON文件，支持自定义序列化和反序列化，支持各种数据类型的转换。

在实际应用中，json模块常用于配置文件管理、API数据处理、数据存储与分析等场景。它是Python中处理JSON数据的标准工具，也是与其他系统进行数据交换的常用格式。