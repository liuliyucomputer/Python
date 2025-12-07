# csv模块详解

csv模块是Python标准库中用于处理CSV（逗号分隔值）格式文件的模块，提供了读取和写入CSV文件的功能。CSV格式是一种常见的电子表格数据交换格式。

## 模块概述

csv模块提供了以下主要功能：

- 读取CSV文件并将其转换为Python数据结构
- 将Python数据结构写入CSV文件
- 支持不同的分隔符、引号字符和行终止符
- 处理包含特殊字符的字段
- 支持Unicode编码

## 基本用法

### 导入模块

```python
import csv
import os
```

### 写入CSV文件

```python
# 创建测试数据
contacts = [
    ["姓名", "年龄", "邮箱", "电话"],
    ["张三", 25, "zhangsan@example.com", "13800138001"],
    ["李四", 30, "lisi@example.com", "13800138002"],
    ["王五", 28, "wangwu@example.com", "13800138003"]
]

# 写入CSV文件
with open("contacts.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    # 写入表头
    writer.writerow(contacts[0])
    # 写入数据行
    writer.writerows(contacts[1:])

print("CSV文件写入完成")

# 查看文件内容
with open("contacts.csv", "r", encoding="utf-8") as f:
    print("文件内容:")
    print(f.read())
```

### 读取CSV文件

```python
# 读取CSV文件
with open("contacts.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    # 读取所有行
    rows = list(reader)

print("CSV文件读取结果:")
print(f"表头: {rows[0]}")
print("数据行:")
for row in rows[1:]:
    print(f"  {row}")
```

## 高级功能

### 使用DictReader和DictWriter

```python
# 创建测试数据（字典格式）
contacts_dict = [
    {"姓名": "张三", "年龄": 25, "邮箱": "zhangsan@example.com", "电话": "13800138001"},
    {"姓名": "李四", "年龄": 30, "邮箱": "lisi@example.com", "电话": "13800138002"},
    {"姓名": "王五", "年龄": 28, "邮箱": "wangwu@example.com", "电话": "13800138003"}
]

# 使用DictWriter写入CSV文件
with open("contacts_dict.csv", "w", encoding="utf-8", newline="") as f:
    # 定义表头
    fieldnames = ["姓名", "年龄", "邮箱", "电话"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    # 写入表头
    writer.writeheader()
    
    # 写入数据行
    writer.writerows(contacts_dict)

print("\n使用DictWriter写入CSV文件完成")

# 使用DictReader读取CSV文件
with open("contacts_dict.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("使用DictReader读取CSV文件结果:")
    for row in reader:
        print(f"  姓名: {row['姓名']}, 年龄: {row['年龄']}, 邮箱: {row['邮箱']}, 电话: {row['电话']}")
```

### 自定义分隔符和引号字符

```python
# 创建测试数据
products = [
    ["产品ID", "产品名称", "价格", "库存"],
    ["P001", "笔记本电脑", "¥5999", "100"],
    ["P002", "智能手机", "¥3999", "200"],
    ["P003", "平板电脑", "¥2999", "150"]
]

# 使用制表符作为分隔符
with open("products_tab.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerows(products)

print("\n使用制表符分隔的CSV文件写入完成")

# 读取制表符分隔的CSV文件
with open("products_tab.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter="\t")
    print("使用制表符分隔的CSV文件读取结果:")
    for row in reader:
        print(f"  {row}")

# 使用分号作为分隔符，单引号作为引号字符
with open("products_semicolon.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";", quotechar="'", quoting=csv.QUOTE_MINIMAL)
    writer.writerows(products)

print("\n使用分号分隔的CSV文件写入完成")

# 读取分号分隔的CSV文件
with open("products_semicolon.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";", quotechar="'")
    print("使用分号分隔的CSV文件读取结果:")
    for row in reader:
        print(f"  {row}")
```

### 处理包含特殊字符的字段

```python
# 创建包含特殊字符的测试数据
data_with_special_chars = [
    ["姓名", "地址", "备注"],
    ["张三", "北京市朝阳区建国路88号", "普通会员"],
    ["李四", "上海市浦东新区陆家嘴金融中心", "VIP会员, 享受8折优惠"],
    ["王五", "广州市天河区天河路385号", "新会员\n赠送积分1000"]
]

# 写入包含特殊字符的CSV文件
with open("special_chars.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerows(data_with_special_chars)

print("\n包含特殊字符的CSV文件写入完成")

# 读取包含特殊字符的CSV文件
with open("special_chars.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("包含特殊字符的CSV文件读取结果:")
    for row in reader:
        print(f"  {row}")
```

## 实际应用示例

### 示例1：数据统计

```python
# 创建销售数据
 sales_data = [
    ["产品", "月份", "销售额", "销售量"],
    ["产品A", "2023-01", 10000, 100],
    ["产品B", "2023-01", 15000, 150],
    ["产品A", "2023-02", 12000, 120],
    ["产品B", "2023-02", 18000, 180],
    ["产品A", "2023-03", 14000, 140],
    ["产品B", "2023-03", 20000, 200]
]

# 写入销售数据到CSV文件
with open("sales_data.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sales_data)

print("\n销售数据CSV文件写入完成")

# 读取销售数据并进行统计
product_stats = {}
month_stats = {}

with open("sales_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["产品"]
        month = row["月份"]
        sales = float(row["销售额"])
        quantity = int(row["销售量"])
        
        # 按产品统计
        if product not in product_stats:
            product_stats[product] = {"总销售额": 0, "总销售量": 0}
        product_stats[product]["总销售额"] += sales
        product_stats[product]["总销售量"] += quantity
        
        # 按月份统计
        if month not in month_stats:
            month_stats[month] = {"总销售额": 0, "总销售量": 0}
        month_stats[month]["总销售额"] += sales
        month_stats[month]["总销售量"] += quantity

print("\n销售数据统计结果:")
print("按产品统计:")
for product, stats in product_stats.items():
    print(f"  {product}: 总销售额={stats['总销售额']}, 总销售量={stats['总销售量']}")

print("按月份统计:")
for month, stats in sorted(month_stats.items()):
    print(f"  {month}: 总销售额={stats['总销售额']}, 总销售量={stats['总销售量']}")
```

### 示例2：数据转换

```python
# 创建原始数据
raw_data = [
    ["ID", "姓名", "科目", "成绩"],
    ["1", "张三", "语文", "85"],
    ["1", "张三", "数学", "90"],
    ["1", "张三", "英语", "88"],
    ["2", "李四", "语文", "82"],
    ["2", "李四", "数学", "87"],
    ["2", "李四", "英语", "91"]
]

# 写入原始数据到CSV文件
with open("raw_scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(raw_data)

print("\n原始成绩数据CSV文件写入完成")

# 转换数据格式（从长格式转换为宽格式）
student_scores = {}

with open("raw_scores.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        student_id = row["ID"]
        name = row["姓名"]
        subject = row["科目"]
        score = row["成绩"]
        
        if student_id not in student_scores:
            student_scores[student_id] = {"ID": student_id, "姓名": name}
        student_scores[student_id][subject] = score

# 将转换后的数据写入新的CSV文件
converted_data = [
    ["ID", "姓名", "语文", "数学", "英语"]
]

for student_id, scores in sorted(student_scores.items()):
    converted_data.append([
        scores["ID"],
        scores["姓名"],
        scores.get("语文", ""),
        scores.get("数学", ""),
        scores.get("英语", "")
    ])

with open("converted_scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(converted_data)

print("\n转换后的成绩数据CSV文件写入完成")

# 读取转换后的数据
with open("converted_scores.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("转换后的成绩数据:")
    for row in reader:
        print(f"  ID: {row['ID']}, 姓名: {row['姓名']}, 语文: {row['语文']}, 数学: {row['数学']}, 英语: {row['英语']}")
```

### 示例3：处理大型CSV文件

```python
# 生成大型测试数据
def generate_large_csv(filename, rows=10000):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        # 写入表头
        writer.writerow(["行号", "随机数1", "随机数2", "随机数3"])
        
        # 写入数据行
        import random
        for i in range(1, rows + 1):
            writer.writerow([
                i,
                random.randint(1, 1000),
                random.randint(1, 1000),
                random.randint(1, 1000)
            ])

# 生成大型CSV文件
generate_large_csv("large_data.csv", rows=10000)
print("\n大型CSV文件生成完成")

# 逐行读取大型CSV文件，避免一次性加载全部数据
row_count = 0
sum_random1 = 0
sum_random2 = 0
sum_random3 = 0

with open("large_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row_count += 1
        sum_random1 += int(row["随机数1"])
        sum_random2 += int(row["随机数2"])
        sum_random3 += int(row["随机数3"])
        
        # 每处理1000行显示进度
        if row_count % 1000 == 0:
            print(f"  已处理 {row_count} 行")

print(f"\n大型CSV文件处理完成")
print(f"  总行数: {row_count}")
print(f"  随机数1平均值: {sum_random1 / row_count:.2f}")
print(f"  随机数2平均值: {sum_random2 / row_count:.2f}")
print(f"  随机数3平均值: {sum_random3 / row_count:.2f}")
```

## 配置参数

### Dialect

csv模块使用Dialect对象来定义CSV文件的格式参数，包括分隔符、引号字符、行终止符等。

```python
# 查看内置的Dialect
print("\n内置的Dialect:")
for dialect in csv.list_dialects():
    print(f"  {dialect}")

# 创建自定义Dialect
csv.register_dialect(
    "my_dialect",
    delimiter="|",
    quotechar="\"",
    quoting=csv.QUOTE_ALL,
    lineterminator="\r\n"
)

# 使用自定义Dialect写入CSV文件
data = [
    ["字段1", "字段2", "字段3"],
    ["值1", "值2", "值3"],
    ["值4", "值5", "值6"]
]

with open("custom_dialect.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, dialect="my_dialect")
    writer.writerows(data)

print("\n使用自定义Dialect的CSV文件写入完成")

# 使用自定义Dialect读取CSV文件
with open("custom_dialect.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, dialect="my_dialect")
    print("使用自定义Dialect的CSV文件读取结果:")
    for row in reader:
        print(f"  {row}")

# 删除自定义Dialect
csv.unregister_dialect("my_dialect")
```

### 常用配置参数

| 参数 | 描述 | 默认值 |
|------|------|--------|
| delimiter | 字段分隔符 | ',' |
| quotechar | 引号字符 | '"' |
| quoting | 引号使用方式 | csv.QUOTE_MINIMAL |
| lineterminator | 行终止符 | '\r\n' |
| skipinitialspace | 是否跳过分隔符后的空格 | False |
| doublequote | 是否使用双引号表示引号字符 | True |
| escapechar | 转义字符 | None |

### quoting参数值

| 值 | 描述 |
|------|------|
| csv.QUOTE_ALL | 所有字段都加引号 |
| csv.QUOTE_MINIMAL | 只有包含特殊字符的字段才加引号 |
| csv.QUOTE_NONNUMERIC | 非数字字段加引号，数字字段转换为浮点数 |
| csv.QUOTE_NONE | 不使用引号，转义字符必须设置 |

## 最佳实践

1. **使用with语句**：始终使用with语句打开CSV文件，确保文件正确关闭
2. **指定编码**：始终指定文件的编码，特别是处理包含非ASCII字符的文件时
3. **设置newline=""**：在写入CSV文件时，设置newline=""可以避免行终止符的问题
4. **处理空值**：根据需求处理CSV文件中的空值
5. **使用DictReader/DictWriter**：当CSV文件有表头时，使用DictReader和DictWriter可以更方便地处理数据
6. **逐行处理大型文件**：对于大型CSV文件，使用逐行读取的方式避免内存溢出
7. **使用Dialect**：当需要处理特定格式的CSV文件时，使用Dialect可以统一配置格式参数
8. **异常处理**：在读取和写入CSV文件时，捕获并处理可能的异常

## 与其他模块的关系

- **pandas**：pandas库提供了更强大的CSV文件处理功能，特别是对于大型数据集和复杂数据操作
- **openpyxl**：openpyxl库用于处理Excel文件，可以与csv模块结合使用进行数据转换
- **json**：json模块用于处理JSON格式数据，可以与csv模块结合使用进行不同格式数据的转换
- **xml.etree.ElementTree**：xml.etree.ElementTree模块用于处理XML格式数据，可以与csv模块结合使用进行不同格式数据的转换

## 清理测试文件

```python
# 清理所有测试文件
for filename in [
    "contacts.csv",
    "contacts_dict.csv",
    "products_tab.csv",
    "products_semicolon.csv",
    "special_chars.csv",
    "sales_data.csv",
    "raw_scores.csv",
    "converted_scores.csv",
    "large_data.csv",
    "custom_dialect.csv"
]:
    if os.path.exists(filename):
        os.remove(filename)

print("\n所有测试文件已清理")
```

## 总结

csv模块是Python标准库中处理CSV格式文件的强大工具，提供了读取和写入CSV文件的功能。它支持各种配置选项，可以处理不同格式的CSV文件。在实际应用中，csv模块常用于数据导入导出、数据交换和数据分析等场景。