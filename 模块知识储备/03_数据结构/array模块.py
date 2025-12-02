# array模块详解 - Python高效同质数组实现

## 1. 核心功能与概述

`array`模块提供了一种存储相同类型数据的紧凑数组实现。与Python内置的列表相比，array模块创建的数组占用更少的内存空间，且在某些操作上具有更好的性能。这种特性使得array模块特别适合处理大量同质数据，如数值计算、信号处理、数据存储等场景。

主要功能特点：
- 存储相同类型的数据，内存布局紧凑
- 比普通列表占用更少的内存空间
- 提供与列表类似的接口，但数据类型受限
- 支持数据的序列化和反序列化
- 支持基本的数组操作，如添加、删除、切片等

适用场景：
- 存储和处理大量数值数据
- 需要节省内存空间的应用
- 与底层系统交互的数据缓冲区
- 数据文件的读写操作
- 数值计算和科学计算的中间数据结构

## 2. 基本使用方法

### 2.1 创建数组

`array`模块的核心是`array`类，创建数组时需要指定类型码（typecode）来表示数组中元素的数据类型：

```python
import array

# 创建整数数组（类型码'i'表示有符号整型）
int_array = array.array('i', [1, 2, 3, 4, 5])
print(f"整数数组: {int_array}")  # 输出: 整数数组: array('i', [1, 2, 3, 4, 5])

# 创建浮点数数组（类型码'f'表示单精度浮点数）
float_array = array.array('f', [1.1, 2.2, 3.3])
print(f"浮点数数组: {float_array}")  # 输出: 浮点数数组: array('f', [1.100000023841858, 2.200000047683716, 3.299999952316284])

# 创建空数组
empty_array = array.array('i')
print(f"空数组: {empty_array}")  # 输出: 空数组: array('i')

# 从字节序列创建数组
bytes_data = b'hello'
char_array = array.array('B', bytes_data)  # 'B'表示无符号字节
print(f"字节数组: {char_array}")  # 输出: 字节数组: array('B', [104, 101, 108, 108, 111])
```

### 2.2 支持的类型码

`array`模块支持多种类型码，用于表示不同的数据类型：

| 类型码 | C类型 | Python类型 | 字节大小 | 描述 |
|-------|-------|-----------|---------|------|
| 'b' | signed char | int | 1 | 有符号字节 |
| 'B' | unsigned char | int | 1 | 无符号字节 |
| 'u' | wchar_t | Unicode字符 | 2 | Unicode字符 |
| 'h' | signed short | int | 2 | 有符号短整型 |
| 'H' | unsigned short | int | 2 | 无符号短整型 |
| 'i' | signed int | int | 2或4 | 有符号整型 |
| 'I' | unsigned int | int | 2或4 | 无符号整型 |
| 'l' | signed long | int | 4 | 有符号长整型 |
| 'L' | unsigned long | int | 4 | 无符号长整型 |
| 'q' | signed long long | int | 8 | 有符号长整型 |
| 'Q' | unsigned long long | int | 8 | 无符号长整型 |
| 'f' | float | float | 4 | 单精度浮点数 |
| 'd' | double | float | 8 | 双精度浮点数 |

### 2.3 基本操作

数组支持许多与列表相同的操作，如索引访问、切片、长度查询等：

```python
import array

# 创建一个整数数组
numbers = array.array('i', [10, 20, 30, 40, 50])

# 索引访问
print(f"第一个元素: {numbers[0]}")  # 输出: 第一个元素: 10
print(f"最后一个元素: {numbers[-1]}")  # 输出: 最后一个元素: 50

# 修改元素
numbers[2] = 35
print(f"修改后的数组: {numbers}")  # 输出: 修改后的数组: array('i', [10, 20, 35, 40, 50])

# 切片操作
slice_result = numbers[1:4]
print(f"切片[1:4]: {slice_result}")  # 输出: 切片[1:4]: array('i', [20, 35, 40])

# 长度查询
print(f"数组长度: {len(numbers)}")  # 输出: 数组长度: 5

# 检查元素是否存在
print(f"20在数组中: {20 in numbers}")  # 输出: 20在数组中: True
print(f"60在数组中: {60 in numbers}")  # 输出: 60在数组中: False

# 迭代数组
print("遍历数组元素:")
for num in numbers:
    print(num, end=' ')
print()  # 输出: 10 20 35 40 50
```

### 2.4 添加和删除元素

数组提供了多种方法来添加和删除元素：

```python
import array

# 创建空数组
arr = array.array('i')

# 添加单个元素
arr.append(10)
arr.append(20)
print(f"添加元素后: {arr}")  # 输出: 添加元素后: array('i', [10, 20])

# 添加多个元素
arr.extend([30, 40, 50])
print(f"扩展数组后: {arr}")  # 输出: 扩展数组后: array('i', [10, 20, 30, 40, 50])

# 在指定位置插入元素
arr.insert(1, 15)
print(f"插入元素后: {arr}")  # 输出: 插入元素后: array('i', [10, 15, 20, 30, 40, 50])

# 删除指定值的第一个出现
arr.remove(30)
print(f"删除30后: {arr}")  # 输出: 删除30后: array('i', [10, 15, 20, 40, 50])

# 弹出指定位置的元素
popped = arr.pop(2)
print(f"弹出元素: {popped}")  # 输出: 弹出元素: 20
print(f"弹出后数组: {arr}")  # 输出: 弹出后数组: array('i', [10, 15, 40, 50])

# 清空数组
arr.clear()
print(f"清空后: {arr}")  # 输出: 清空后: array('i')
```

## 3. 高级用法

### 3.1 数据序列化与反序列化

`array`模块提供了便捷的方法将数组数据保存到文件或从文件读取：

```python
import array
import os

# 创建一个浮点数数组
float_array = array.array('d', [1.1, 2.2, 3.3, 4.4, 5.5])

# 将数组写入文件
filename = 'float_data.bin'
with open(filename, 'wb') as f:
    float_array.tofile(f)
print(f"数组已写入文件: {filename}")

# 从文件读取数组
new_array = array.array('d')  # 必须指定相同的类型码
with open(filename, 'rb') as f:
    new_array.fromfile(f, len(float_array))
print(f"从文件读取的数组: {new_array}")

# 清理
os.remove(filename)

# 使用bytes进行序列化和反序列化
data_bytes = float_array.tobytes()
print(f"序列化后的字节数: {len(data_bytes)}")

restored_array = array.array('d')
restored_array.frombytes(data_bytes)
print(f"反序列化后的数组: {restored_array}")
```

### 3.2 数组转换

数组可以与其他Python数据结构相互转换：

```python
import array

# 创建一个整数数组
int_array = array.array('i', [1, 2, 3, 4, 5])

# 转换为列表
int_list = int_array.tolist()
print(f"转换为列表: {int_list}")  # 输出: 转换为列表: [1, 2, 3, 4, 5]

# 从列表创建数组
new_array = array.array('i', int_list)
print(f"从列表创建的数组: {new_array}")  # 输出: 从列表创建的数组: array('i', [1, 2, 3, 4, 5])

# 转换为字节序列
bytes_data = int_array.tobytes()
print(f"转换为字节序列: {bytes_data}")

# 转换为不同类型的数组
float_array = array.array('f', (float(x) for x in int_array))
print(f"转换为浮点数组: {float_array}")

# 使用缓冲区协议（低层次操作）
import sys
if hasattr(int_array, 'buffer_info'):
    address, size = int_array.buffer_info()
    print(f"数组缓冲区地址: {address}")
    print(f"数组元素数量: {size}")
    print(f"每个元素字节数: {sys.getsizeof(int_array[0])}")
```

### 3.3 数组操作和算法

可以使用数组实现各种算法和操作：

```python
import array

# 数组排序
numbers = array.array('i', [5, 2, 9, 1, 7, 6, 3])
numbers_sorted = array.array('i', sorted(numbers))
print(f"排序后的数组: {numbers_sorted}")  # 输出: 排序后的数组: array('i', [1, 2, 3, 5, 6, 7, 9])

# 原地排序（Python 3.9+支持list.sort方法）
if hasattr(numbers, 'sort'):
    numbers.sort()
    print(f"原地排序后的数组: {numbers}")

# 数组反转
reversed_array = array.array(numbers.typecode, reversed(numbers))
print(f"反转后的数组: {reversed_array}")

# 数组拼接
array1 = array.array('i', [1, 2, 3])
array2 = array.array('i', [4, 5, 6])
combined = array.array('i', array1)
combined.extend(array2)
print(f"拼接后的数组: {combined}")  # 输出: 拼接后的数组: array('i', [1, 2, 3, 4, 5, 6])

# 数组去重
duplicate_array = array.array('i', [1, 2, 2, 3, 3, 3, 4])
unique_array = array.array('i', sorted(set(duplicate_array)))
print(f"去重后的数组: {unique_array}")  # 输出: 去重后的数组: array('i', [1, 2, 3, 4])

# 数组统计
def array_stats(arr):
    if not arr:
        return None
    
    # 转换为列表进行统计
    lst = arr.tolist()
    return {
        'min': min(lst),
        'max': max(lst),
        'sum': sum(lst),
        'count': len(lst),
        'avg': sum(lst) / len(lst) if lst else 0
    }

stats = array_stats(array.array('d', [1.5, 2.5, 3.5, 4.5, 5.5]))
print(f"数组统计信息: {stats}")
```

### 3.4 与NumPy的互操作

在需要更高级数值计算功能时，可以与NumPy库进行互操作：

```python
import array

# 注意：实际使用时需要安装NumPy库
# import numpy as np

def array_to_numpy_example():
    # 创建一个数组
    py_array = array.array('d', [1.1, 2.2, 3.3, 4.4, 5.5])
    
    # 转换为NumPy数组
    # np_array = np.frombuffer(py_array, dtype=np.float64)
    # 或者
    # np_array = np.array(py_array, dtype=np.float64)
    
    # 从NumPy数组创建Python数组
    # new_py_array = array.array('d', np_array)
    
    print("NumPy互操作示例（需要安装NumPy库）")

# 调用示例函数
array_to_numpy_example()
```

### 3.5 内存高效的数据结构

使用`array`模块可以创建内存效率更高的数据结构：

```python
import array
import sys

# 比较数组和列表的内存占用
def compare_memory():
    # 创建包含10000个整数的列表
    int_list = list(range(10000))
    # 创建包含相同整数的数组
    int_array = array.array('i', range(10000))
    
    # 计算内存占用（近似值）
    list_size = sys.getsizeof(int_list)
    array_size = sys.getsizeof(int_array)
    
    print(f"列表大小: {list_size} 字节")
    print(f"数组大小: {array_size} 字节")
    print(f"内存节省: {list_size - array_size} 字节 ({(1 - array_size / list_size) * 100:.2f}%)")

# 内存高效的矩阵实现
class CompactMatrix:
    def __init__(self, rows, cols, typecode='d'):
        self.rows = rows
        self.cols = cols
        self.data = array.array(typecode, [0] * (rows * cols))
    
    def get(self, i, j):
        """获取矩阵元素"""
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i * self.cols + j]
        raise IndexError("Matrix index out of range")
    
    def set(self, i, j, value):
        """设置矩阵元素"""
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i * self.cols + j] = value
        else:
            raise IndexError("Matrix index out of range")
    
    def __repr__(self):
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(str(self.get(i, j)))
            result.append(' '.join(row))
        return '\n'.join(result)

# 使用示例
print("内存占用比较:")
compare_memory()

print("\n紧凑矩阵示例:")
matrix = CompactMatrix(3, 3)
for i in range(3):
    for j in range(3):
        matrix.set(i, j, i * 3 + j)
print(matrix)
```

## 4. 实际应用场景

### 4.1 大规模数值数据处理

`array`模块特别适合处理大规模数值数据，如传感器数据、金融数据等：

```python
import array
import random
import time

def process_large_dataset():
    """处理大规模数据集示例"""
    print("生成大规模数值数据...")
    
    # 生成100万个随机浮点数
    start_time = time.time()
    # 使用array存储
    float_array = array.array('d', (random.random() for _ in range(1000000)))
    array_time = time.time() - start_time
    print(f"使用array创建时间: {array_time:.4f}秒")
    
    # 使用列表存储（对比）
    start_time = time.time()
    float_list = [random.random() for _ in range(1000000)]
    list_time = time.time() - start_time
    print(f"使用列表创建时间: {list_time:.4f}秒")
    
    # 计算统计信息
    start_time = time.time()
    array_sum = sum(float_array)
    array_avg = array_sum / len(float_array)
    array_process_time = time.time() - start_time
    print(f"Array处理时间: {array_process_time:.4f}秒")
    print(f"Array平均值: {array_avg:.6f}")
    
    start_time = time.time()
    list_sum = sum(float_list)
    list_avg = list_sum / len(float_list)
    list_process_time = time.time() - start_time
    print(f"List处理时间: {list_process_time:.4f}秒")
    print(f"List平均值: {list_avg:.6f}")

# 数据过滤和转换示例
def filter_and_transform_data():
    """数据过滤和转换"""
    # 创建原始数据
    data = array.array('d', (random.uniform(-100, 100) for _ in range(100000)))
    
    # 过滤出正数并转换为整数
    start_time = time.time()
    positive_ints = array.array('i', (int(x) for x in data if x > 0))
    process_time = time.time() - start_time
    
    print(f"过滤后数据量: {len(positive_ints)}")
    print(f"处理时间: {process_time:.4f}秒")
    if positive_ints:
        print(f"数据样本: {positive_ints[:10]}")

# 运行示例
process_large_dataset()
filter_and_transform_data()
```

### 4.2 二进制文件处理

`array`模块非常适合处理二进制文件，如图像文件、音频文件、数据日志等：

```python
import array
import os

def read_binary_file_example(filename='sample.bin'):
    """读取二进制文件示例"""
    # 首先创建一个示例二进制文件
    # 创建一个包含随机整数的数组
    sample_array = array.array('i', (random.randint(0, 1000) for _ in range(100)))
    
    # 将数组写入二进制文件
    with open(filename, 'wb') as f:
        sample_array.tofile(f)
    
    print(f"已创建示例二进制文件: {filename}")
    print(f"文件大小: {os.path.getsize(filename)} 字节")
    
    # 读取二进制文件
    new_array = array.array('i')
    with open(filename, 'rb') as f:
        new_array.fromfile(f, 100)
    
    print(f"成功读取文件数据")
    print(f"读取的数据样本: {new_array[:10]}")
    
    # 验证数据
    is_same = (sample_array == new_array)
    print(f"数据一致性验证: {'成功' if is_same else '失败'}")
    
    # 清理
    os.remove(filename)

def process_image_data_example():
    """处理图像数据示例（概念性）"""
    print("\n图像数据处理示例（概念性）")
    print("1. 使用array存储像素数据可以节省内存")
    print("2. 可以使用无符号字节('B')存储灰度图像")
    print("3. 可以使用多个数组存储RGB通道数据")
    print("4. 数组支持快速的文件读写操作")
    
    # 概念性代码框架
    # width, height = 640, 480
    # gray_data = array.array('B', [0] * (width * height))  # 灰度图像
    # red_data = array.array('B', [0] * (width * height))   # R通道
    # green_data = array.array('B', [0] * (width * height)) # G通道
    # blue_data = array.array('B', [0] * (width * height))  # B通道
    
    # # 图像处理操作...
    # # 保存到文件...

# 运行示例
import random
read_binary_file_example()
process_image_data_example()
```

### 4.3 信号处理和数值计算

在信号处理和简单数值计算场景中，`array`模块可以作为轻量级的数值数组：

```python
import array
import math

def generate_sine_wave(frequency=1.0, amplitude=1.0, sample_rate=44100, duration=1.0):
    """生成正弦波形数据
    
    Args:
        frequency: 频率（Hz）
        amplitude: 振幅
        sample_rate: 采样率
        duration: 持续时间（秒）
        
    Returns:
        包含正弦波形数据的数组
    """
    num_samples = int(sample_rate * duration)
    wave = array.array('f', [0.0] * num_samples)
    
    for i in range(num_samples):
        t = i / sample_rate
        wave[i] = amplitude * math.sin(2 * math.pi * frequency * t)
    
    return wave

def process_signal(signal):
    """简单的信号处理
    
    Args:
        signal: 输入信号数组
        
    Returns:
        处理后的信号数组
    """
    # 创建结果数组
    result = array.array(signal.typecode, [0] * len(signal))
    
    # 简单的低通滤波（移动平均）
    window_size = 5
    for i in range(len(signal)):
        # 计算窗口边界
        start = max(0, i - window_size // 2)
        end = min(len(signal), i + window_size // 2 + 1)
        
        # 计算窗口内的平均值
        window_sum = 0
        for j in range(start, end):
            window_sum += signal[j]
        result[i] = window_sum / (end - start)
    
    return result

# 信号统计分析
def analyze_signal(signal):
    """分析信号特性
    
    Args:
        signal: 输入信号数组
        
    Returns:
        包含信号统计信息的字典
    """
    # 转换为列表进行计算
    sig_list = signal.tolist()
    
    # 计算统计量
    sig_min = min(sig_list)
    sig_max = max(sig_list)
    sig_sum = sum(sig_list)
    sig_avg = sig_sum / len(sig_list)
    
    # 计算RMS值
    rms = math.sqrt(sum(x*x for x in sig_list) / len(sig_list))
    
    # 计算峰值因数
    crest_factor = sig_max / rms if rms > 0 else 0
    
    return {
        'min': sig_min,
        'max': sig_max,
        'mean': sig_avg,
        'rms': rms,
        'peak_to_peak': sig_max - sig_min,
        'crest_factor': crest_factor
    }

# 运行示例
print("生成和处理正弦波信号:")
sine_wave = generate_sine_wave(frequency=440, duration=0.1)  # 440Hz A音，0.1秒
print(f"信号长度: {len(sine_wave)} 采样点")
print(f"信号样本: {sine_wave[:10]}")

# 添加噪声
noise = array.array('f', [random.uniform(-0.1, 0.1) for _ in range(len(sine_wave))])
noisy_signal = array.array('f', [sine_wave[i] + noise[i] for i in range(len(sine_wave))])

# 处理信号
filtered_signal = process_signal(noisy_signal)

# 分析信号
stats = analyze_signal(filtered_signal)
print(f"信号统计信息: {stats}")
```

### 4.4 数据压缩和编码

`array`模块可以与其他库结合用于数据压缩和编码：

```python
import array
import zlib

def compress_array_data():
    """压缩数组数据示例"""
    # 创建一个较大的数值数组
    large_array = array.array('d', (random.uniform(0, 1) for _ in range(100000)))
    
    # 转换为字节数据
    bytes_data = large_array.tobytes()
    print(f"原始字节数据大小: {len(bytes_data)} 字节")
    
    # 压缩数据
    compressed_data = zlib.compress(bytes_data)
    print(f"压缩后数据大小: {len(compressed_data)} 字节")
    print(f"压缩率: {(1 - len(compressed_data) / len(bytes_data)) * 100:.2f}%")
    
    # 解压缩数据
    decompressed_data = zlib.decompress(compressed_data)
    
    # 还原数组
    restored_array = array.array('d')
    restored_array.frombytes(decompressed_data)
    
    # 验证数据
    is_same = len(large_array) == len(restored_array)
    if is_same:
        for i in range(len(large_array)):
            if abs(large_array[i] - restored_array[i]) > 1e-10:
                is_same = False
                break
    
    print(f"数据一致性验证: {'成功' if is_same else '失败'}")

def delta_encoding_example():
    """Delta编码示例（适用于时间序列数据）"""
    print("\nDelta编码示例:")
    
    # 创建一个有相关性的时间序列数据（如温度传感器读数）
    base_value = 25.0
    time_series = array.array('f', [])
    
    for _ in range(1000):
        # 生成相关数据（小幅波动）
        base_value += random.uniform(-0.5, 0.5)
        time_series.append(base_value)
    
    # 进行delta编码
    delta_encoded = array.array('f', [time_series[0]])  # 存储第一个值
    for i in range(1, len(time_series)):
        delta_encoded.append(time_series[i] - time_series[i-1])
    
    # 验证编码
    decoded = array.array('f', [delta_encoded[0]])
    for i in range(1, len(delta_encoded)):
        decoded.append(decoded[i-1] + delta_encoded[i])
    
    # 检查编码解码是否正确
    is_correct = True
    for i in range(len(time_series)):
        if abs(time_series[i] - decoded[i]) > 1e-6:
            is_correct = False
            break
    
    print(f"Delta编码验证: {'成功' if is_correct else '失败'}")
    print("Delta编码对于有相关性的数据更易压缩")

# 运行示例
import random
compress_array_data()
delta_encoding_example()
```

### 4.5 实现自定义数据结构

利用`array`模块可以实现内存高效的自定义数据结构：

```python
import array

class CompactQueue:
    """基于数组实现的内存高效队列"""
    def __init__(self, max_size, typecode='i'):
        self.data = array.array(typecode, [0] * max_size)
        self.max_size = max_size
        self.front = 0  # 队列头
        self.rear = 0   # 队列尾
        self.count = 0  # 当前元素数量
    
    def enqueue(self, item):
        """入队操作"""
        if self.count >= self.max_size:
            raise IndexError("Queue is full")
        
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.max_size
        self.count += 1
    
    def dequeue(self):
        """出队操作"""
        if self.count == 0:
            raise IndexError("Queue is empty")
        
        item = self.data[self.front]
        self.front = (self.front + 1) % self.max_size
        self.count -= 1
        return item
    
    def is_empty(self):
        """检查队列是否为空"""
        return self.count == 0
    
    def is_full(self):
        """检查队列是否已满"""
        return self.count >= self.max_size
    
    def size(self):
        """获取队列当前大小"""
        return self.count

class CompactStack:
    """基于数组实现的内存高效栈"""
    def __init__(self, max_size, typecode='i'):
        self.data = array.array(typecode, [0] * max_size)
        self.max_size = max_size
        self.top = -1  # 栈顶指针
    
    def push(self, item):
        """压栈操作"""
        if self.top >= self.max_size - 1:
            raise IndexError("Stack is full")
        
        self.top += 1
        self.data[self.top] = item
    
    def pop(self):
        """弹栈操作"""
        if self.top < 0:
            raise IndexError("Stack is empty")
        
        item = self.data[self.top]
        self.top -= 1
        return item
    
    def peek(self):
        """查看栈顶元素"""
        if self.top < 0:
            raise IndexError("Stack is empty")
        
        return self.data[self.top]
    
    def is_empty(self):
        """检查栈是否为空"""
        return self.top < 0
    
    def is_full(self):
        """检查栈是否已满"""
        return self.top >= self.max_size - 1
    
    def size(self):
        """获取栈当前大小"""
        return self.top + 1

class TypedBuffer:
    """类型化缓冲区，用于二进制数据处理"""
    def __init__(self, typecode='B', initial_size=1024):
        self.data = array.array(typecode, [0] * initial_size)
        self.size = 0
        self.typecode = typecode
        self.initial_size = initial_size
    
    def append(self, value):
        """添加单个值"""
        # 检查是否需要扩容
        if self.size >= len(self.data):
            # 扩展数组大小
            new_data = array.array(self.typecode, [0] * (len(self.data) * 2))
            new_data[:len(self.data)] = self.data
            self.data = new_data
        
        self.data[self.size] = value
        self.size += 1
    
    def extend(self, values):
        """添加多个值"""
        # 检查是否需要扩容
        required_size = self.size + len(values)
        if required_size > len(self.data):
            # 扩展数组大小
            new_size = max(len(self.data) * 2, required_size)
            new_data = array.array(self.typecode, [0] * new_size)
            new_data[:self.size] = self.data[:self.size]
            self.data = new_data
        
        self.data[self.size:self.size + len(values)] = values
        self.size += len(values)
    
    def to_bytes(self):
        """转换为字节序列"""
        return self.data[:self.size].tobytes()
    
    def clear(self):
        """清空缓冲区"""
        self.size = 0
        # 可选：重置为初始大小以节省内存
        if len(self.data) > self.initial_size:
            self.data = array.array(self.typecode, [0] * self.initial_size)

# 使用示例
print("紧凑队列示例:")
queue = CompactQueue(max_size=5)
for i in range(5):
    queue.enqueue(i)
    print(f"入队: {i}, 队列大小: {queue.size()}")

while not queue.is_empty():
    value = queue.dequeue()
    print(f"出队: {value}, 队列大小: {queue.size()}")

print("\n紧凑栈示例:")
stack = CompactStack(max_size=5)
for i in range(5):
    stack.push(i)
    print(f"压栈: {i}, 栈大小: {stack.size()}")

while not stack.is_empty():
    value = stack.pop()
    print(f"弹栈: {value}, 栈大小: {stack.size()}")

print("\n类型化缓冲区示例:")
buffer = TypedBuffer(typecode='B')
buffer.extend([65, 66, 67, 68, 69])  # ASCII编码的A, B, C, D, E
print(f"缓冲区内容: {buffer.data[:buffer.size]}")
print(f"转换为字符串: {buffer.to_bytes().decode('ascii')}")
```

### 4.6 高效的图形和游戏开发

在图形和游戏开发中，`array`模块可以用于高效存储顶点数据、颜色数据等：

```python
import array
import math

def create_color_array(width, height):
    """创建一个存储像素颜色的数组"""
    # 使用无符号字节存储RGBA颜色（每个通道一个字节）
    # 总共需要width * height * 4个字节
    colors = array.array('B', [0] * (width * height * 4))
    return colors

def create_vertex_array(num_vertices):
    """创建一个存储3D顶点的数组"""
    # 每个顶点包含x, y, z三个坐标，使用浮点数
    vertices = array.array('f', [0.0] * (num_vertices * 3))
    return vertices

def create_texture_coordinates(num_vertices):
    """创建纹理坐标数组"""
    # 每个顶点包含u, v两个纹理坐标
    tex_coords = array.array('f', [0.0] * (num_vertices * 2))
    return tex_coords

class MeshData:
    """3D模型网格数据"""
    def __init__(self, num_vertices):
        self.vertices = create_vertex_array(num_vertices)
        self.normals = create_vertex_array(num_vertices)  # 法线向量
        self.tex_coords = create_texture_coordinates(num_vertices)
        self.indices = array.array('I', [])  # 面索引，使用无符号整型
        self.num_vertices = num_vertices
    
    def set_vertex(self, index, x, y, z):
        """设置顶点坐标"""
        if 0 <= index < self.num_vertices:
            vertex_offset = index * 3
            self.vertices[vertex_offset] = x
            self.vertices[vertex_offset + 1] = y
            self.vertices[vertex_offset + 2] = z
    
    def add_face(self, v1, v2, v3):
        """添加三角形面"""
        self.indices.extend([v1, v2, v3])
    
    def calculate_normals(self):
        """计算法线向量（简化版）"""
        # 初始化法线为零向量
        for i in range(self.num_vertices * 3):
            self.normals[i] = 0.0
        
        # 计算每个面的法线并累加到顶点
        for i in range(0, len(self.indices), 3):
            # 获取三个顶点的索引
            v1_idx = self.indices[i] * 3
            v2_idx = self.indices[i+1] * 3
            v3_idx = self.indices[i+2] * 3
            
            # 获取顶点坐标
            v1 = (self.vertices[v1_idx], self.vertices[v1_idx+1], self.vertices[v1_idx+2])
            v2 = (self.vertices[v2_idx], self.vertices[v2_idx+1], self.vertices[v2_idx+2])
            v3 = (self.vertices[v3_idx], self.vertices[v3_idx+1], self.vertices[v3_idx+2])
            
            # 计算两个边向量
            edge1 = (v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2])
            edge2 = (v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2])
            
            # 计算叉乘得到法线向量
            normal = (
                edge1[1] * edge2[2] - edge1[2] * edge2[1],
                edge1[2] * edge2[0] - edge1[0] * edge2[2],
                edge1[0] * edge2[1] - edge1[1] * edge2[0]
            )
            
            # 归一化法线
            length = math.sqrt(normal[0]**2 + normal[1]**2 + normal[2]**2)
            if length > 0:
                normal = (normal[0]/length, normal[1]/length, normal[2]/length)
            
            # 将法线累加到三个顶点
            for j in range(3):
                self.normals[v1_idx + j] += normal[j]
                self.normals[v2_idx + j] += normal[j]
                self.normals[v3_idx + j] += normal[j]
        
        # 归一化所有顶点的法线
        for i in range(0, self.num_vertices * 3, 3):
            length = math.sqrt(
                self.normals[i]**2 + 
                self.normals[i+1]**2 + 
                self.normals[i+2]**2
            )
            if length > 0:
                self.normals[i] /= length
                self.normals[i+1] /= length
                self.normals[i+2] /= length

# 创建一个简单立方体示例
def create_cube():
    """创建一个立方体网格"""
    # 立方体有8个顶点
    cube = MeshData(8)
    
    # 设置顶点坐标
    cube.set_vertex(0, -1, -1, -1)  # 左下后
    cube.set_vertex(1, 1, -1, -1)   # 右下后
    cube.set_vertex(2, 1, 1, -1)    # 右上后
    cube.set_vertex(3, -1, 1, -1)   # 左上后
    cube.set_vertex(4, -1, -1, 1)   # 左下前
    cube.set_vertex(5, 1, -1, 1)    # 右下前
    cube.set_vertex(6, 1, 1, 1)     # 右上前
    cube.set_vertex(7, -1, 1, 1)    # 左上前
    
    # 添加六个面
    # 后面
    cube.add_face(0, 1, 2)
    cube.add_face(2, 3, 0)
    # 前面
    cube.add_face(4, 6, 5)
    cube.add_face(6, 4, 7)
    # 左面
    cube.add_face(0, 3, 7)
    cube.add_face(7, 4, 0)
    # 右面
    cube.add_face(1, 5, 6)
    cube.add_face(6, 2, 1)
    # 下面
    cube.add_face(0, 4, 5)
    cube.add_face(5, 1, 0)
    # 上面
    cube.add_face(2, 6, 7)
    cube.add_face(7, 3, 2)
    
    # 计算法线
    cube.calculate_normals()
    
    return cube

# 使用示例
print("3D网格数据示例:")
cube = create_cube()
print(f"顶点数量: {cube.num_vertices}")
print(f"面数量: {len(cube.indices) // 3}")
print(f"前3个顶点: {cube.vertices[:9]}")
```

### 4.7 实现位操作和位向量

`array`模块可以用于实现位级别的操作和位向量：

```python
import array

class BitVector:
    """基于数组实现的位向量"""
    def __init__(self, size=0):
        # 使用无符号长整型数组存储位，每个元素存储32位
        self.bits_per_element = 32
        self.data = array.array('I', [0] * ((size + self.bits_per_element - 1) // self.bits_per_element))
        self.size = size
    
    def _get_element_index(self, bit_index):
        """获取位所在的元素索引和偏移"""
        if bit_index < 0 or bit_index >= self.size:
            raise IndexError("Bit index out of range")
        return bit_index // self.bits_per_element, bit_index % self.bits_per_element
    
    def get(self, bit_index):
        """获取指定位的值"""
        element_index, bit_offset = self._get_element_index(bit_index)
        return (self.data[element_index] >> bit_offset) & 1
    
    def set(self, bit_index, value=1):
        """设置指定位的值"""
        element_index, bit_offset = self._get_element_index(bit_index)
        if value:
            # 设置位为1
            self.data[element_index] |= (1 << bit_offset)
        else:
            # 设置位为0
            self.data[element_index] &= ~(1 << bit_offset)
    
    def flip(self, bit_index):
        """翻转指定位的值"""
        element_index, bit_offset = self._get_element_index(bit_index)
        self.data[element_index] ^= (1 << bit_offset)
    
    def clear(self):
        """清空所有位"""
        for i in range(len(self.data)):
            self.data[i] = 0
    
    def resize(self, new_size):
        """调整位向量大小"""
        new_data = array.array('I', [0] * ((new_size + self.bits_per_element - 1) // self.bits_per_element))
        # 复制原有数据
        copy_count = min(len(self.data), len(new_data))
        new_data[:copy_count] = self.data[:copy_count]
        # 对于缩小的情况，截断多余的数据
        if new_size < self.size and copy_count < len(new_data):
            # 清除最后一个元素中多余的位
            last_element_bits = new_size % self.bits_per_element
            if last_element_bits > 0:
                mask = (1 << last_element_bits) - 1
                new_data[-1] &= mask
        self.data = new_data
        self.size = new_size
    
    def count_set_bits(self):
        """统计设置为1的位的数量"""
        count = 0
        for element in self.data[:-1]:  # 处理除最后一个元素外的所有元素
            # 使用Brian Kernighan算法计算设置位
            bits = element
            while bits:
                bits &= bits - 1
                count += 1
        
        # 处理最后一个元素，只计算有效位
        if self.data and self.size > 0:
            last_element = self.data[-1]
            effective_bits = self.size % self.bits_per_element
            if effective_bits > 0:
                # 只保留有效位
                last_element &= (1 << effective_bits) - 1
            while last_element:
                last_element &= last_element - 1
                count += 1
        
        return count
    
    def to_bytes(self):
        """转换为字节序列"""
        return self.data.tobytes()
    
    @classmethod
    def from_bytes(cls, data_bytes, size):
        """从字节序列创建位向量"""
        bit_vec = cls(size)
        # 计算需要读取的元素数量
        element_count = min(len(bit_vec.data), len(data_bytes) // 4)  # 每个元素4字节
        # 直接从字节读取到数组
        bit_vec.data[:element_count] = array.array('I', data_bytes[:element_count * 4])
        return bit_vec

class BitSet:
    """位集合，用于高效存储布尔值集合"""
    def __init__(self, max_value=1000):
        self.bit_vector = BitVector(max_value)
        self.max_value = max_value
    
    def add(self, value):
        """添加一个值"""
        self.bit_vector.set(value)
    
    def remove(self, value):
        """移除一个值"""
        self.bit_vector.set(value, 0)
    
    def contains(self, value):
        """检查是否包含某个值"""
        try:
            return self.bit_vector.get(value) == 1
        except IndexError:
            return False
    
    def toggle(self, value):
        """切换值的状态"""
        self.bit_vector.flip(value)
    
    def clear(self):
        """清空集合"""
        self.bit_vector.clear()
    
    def size(self):
        """获取集合大小"""
        return self.bit_vector.count_set_bits()
    
    def intersection(self, other):
        """计算与另一个BitSet的交集"""
        result = BitSet(min(self.max_value, other.max_value))
        # 计算按位与
        for i in range(min(len(self.bit_vector.data), len(other.bit_vector.data))):
            result.bit_vector.data[i] = self.bit_vector.data[i] & other.bit_vector.data[i]
        return result
    
    def union(self, other):
        """计算与另一个BitSet的并集"""
        result = BitSet(max(self.max_value, other.max_value))
        # 计算按位或
        result.bit_vector.data[:len(self.bit_vector.data)] = self.bit_vector.data
        for i in range(len(other.bit_vector.data)):
            result.bit_vector.data[i] |= other.bit_vector.data[i]
        return result

# 使用示例
print("位向量示例:")
bv = BitVector(100)

# 设置一些位
bv.set(10)
bv.set(20)
bv.set(30)

print(f"位10的值: {bv.get(10)}")  # 应该是1
print(f"位15的值: {bv.get(15)}")  # 应该是0

# 翻转位
bv.flip(10)
print(f"翻转后位10的值: {bv.get(10)}")  # 应该是0

# 统计设置位
print(f"设置位的数量: {bv.count_set_bits()}")  # 应该是2

print("\n位集合示例:")
bs1 = BitSet(100)
bs2 = BitSet(100)

# 添加元素
for i in range(0, 100, 2):
    bs1.add(i)

for i in range(0, 100, 3):
    bs2.add(i)

print(f"bs1大小: {bs1.size()}")  # 应该是50
print(f"bs2大小: {bs2.size()}")  # 应该是34

# 检查包含关系
print(f"bs1包含6: {bs1.contains(6)}")  # 应该是True
print(f"bs1包含7: {bs1.contains(7)}")  # 应该是False

# 计算交集
intersect = bs1.intersection(bs2)
print(f"交集大小: {intersect.size()}")  # 应该是17

# 计算并集
union = bs1.union(bs2)
print(f"并集大小: {union.size()}")  # 应该是67