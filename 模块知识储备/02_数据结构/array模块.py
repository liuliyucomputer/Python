# Python array模块详解

# 1. array模块概述
print("=== 1. array模块概述 ===")
print("array模块提供了一种高效的数组数据类型，用于存储相同类型的数值。")
print("与Python内置的列表相比，array模块中的数组占用更少的内存空间。")
print("array数组中的所有元素必须是相同的数据类型，这使得内存分配更加高效。")
print("array模块适用于需要存储大量数值数据且对内存效率有要求的场景。")
print()

# 2. 支持的数据类型
print("=== 2. 支持的数据类型 ===")
def array_types():
    """展示array模块支持的数据类型"""
    import array
    
    print("array模块支持的数据类型:")
    print("'b': signed byte (有符号字节，范围: -128 到 127)")
    print("'B': unsigned byte (无符号字节，范围: 0 到 255)")
    print("'u': Py_UCS4 (Unicode字符)")
    print("'h': signed short (有符号短整型，通常为2字节)")
    print("'H': unsigned short (无符号短整型，通常为2字节)")
    print("'i': signed int (有符号整型，通常为4字节)")
    print("'I': unsigned int (无符号整型，通常为4字节)")
    print("'l': signed long (有符号长整型，通常为4或8字节)")
    print("'L': unsigned long (无符号长整型，通常为4或8字节)")
    print("'q': signed long long (有符号长长整型，通常为8字节)")
    print("'Q': unsigned long long (无符号长长整型，通常为8字节)")
    print("'f': float (浮点数，通常为4字节)")
    print("'d': double (双精度浮点数，通常为8字节)")
    
    print("\n注意：具体的字节大小可能因操作系统和硬件架构而异。")

array_types()
print()

# 3. 创建数组
print("=== 3. 创建数组 ===")
def array_creation():
    """展示如何创建数组"""
    import array
    
    # 从类型代码和初始值创建数组
    print("1. 创建不同类型的数组:")
    # 整数数组
    arr_int = array.array('i', [1, 2, 3, 4, 5])
    print(f"整数数组 (i): {arr_int}")
    
    # 浮点数数组
    arr_float = array.array('f', [1.1, 2.2, 3.3, 4.4, 5.5])
    print(f"浮点数数组 (f): {arr_float}")
    
    # 双精度浮点数数组
    arr_double = array.array('d', [1.1, 2.2, 3.3, 4.4, 5.5])
    print(f"双精度浮点数数组 (d): {arr_double}")
    
    # 字节数组
    arr_byte = array.array('b', [10, 20, 30, 40, 50])
    print(f"字节数组 (b): {arr_byte}")
    
    print("\n2. 创建空数组:")
    # 创建空的整数数组
    empty_int = array.array('i')
    print(f"空整数数组: {empty_int}")
    
    print("\n3. 从其他序列创建数组:")
    # 从元组创建
    from_tuple = array.array('i', (10, 20, 30, 40, 50))
    print(f"从元组创建的数组: {from_tuple}")
    
    # 从字符串创建Unicode数组
    unicode_arr = array.array('u', 'Hello')
    print(f"Unicode数组: {unicode_arr}")
    
    print("\n4. 类型转换:")
    # 不同类型数组之间的转换
    int_arr = array.array('i', [1, 2, 3, 4, 5])
    # 转换为浮点数数组
    float_arr = array.array('f', int_arr)
    print(f"整数数组: {int_arr}")
    print(f"转换为浮点数数组: {float_arr}")

array_creation()
print()

# 4. 数组操作
print("=== 4. 数组操作 ===")
def array_operations():
    """展示数组的基本操作"""
    import array
    
    # 创建一个整数数组用于演示
    arr = array.array('i', [10, 20, 30, 40, 50])
    print(f"原始数组: {arr}")
    
    # 访问元素
    print(f"\n访问元素:")
    print(f"arr[0] = {arr[0]}")
    print(f"arr[-1] = {arr[-1]}")
    print(f"arr[1:3] = {arr[1:3]}")  # 切片操作
    
    # 修改元素
    print(f"\n修改元素:")
    arr[0] = 100
    print(f"修改第一个元素后: {arr}")
    
    # 添加元素
    print(f"\n添加元素:")
    # append方法 - 添加单个元素
    arr.append(60)
    print(f"append(60)后: {arr}")
    
    # extend方法 - 添加多个元素
    arr.extend([70, 80, 90])
    print(f"extend([70, 80, 90])后: {arr}")
    
    # insert方法 - 在指定位置插入元素
    arr.insert(1, 15)
    print(f"insert(1, 15)后: {arr}")
    
    # 删除元素
    print(f"\n删除元素:")
    # remove方法 - 删除指定值的第一个匹配项
    arr.remove(30)
    print(f"remove(30)后: {arr}")
    
    # pop方法 - 删除并返回指定位置的元素
    popped = arr.pop()
    print(f"pop()后: {arr}")
    print(f"弹出的元素: {popped}")
    
    popped_index = arr.pop(2)
    print(f"pop(2)后: {arr}")
    print(f"弹出的索引为2的元素: {popped_index}")
    
    # 查找元素
    print(f"\n查找元素:")
    # index方法 - 查找元素的索引
    idx = arr.index(50)
    print(f"元素50的索引: {idx}")
    
    # count方法 - 统计元素出现次数
    arr.append(100)
    count = arr.count(100)
    print(f"数组: {arr}")
    print(f"元素100出现的次数: {count}")
    
    # 数组长度
    print(f"\n数组长度: {len(arr)}")
    
    # 数组迭代
    print(f"\n数组迭代:")
    print("数组中的元素:", end=" ")
    for element in arr:
        print(element, end=" ")
    print()
    
    # 数组反转
    print(f"\n数组反转:")
    arr.reverse()
    print(f"反转后: {arr}")
    
    # 数组排序
    print(f"\n数组排序:")
    arr.sort()
    print(f"排序后: {arr}")
    
    # 数组清空
    print(f"\n数组清空:")
    arr.clear()
    print(f"清空后: {arr}")

array_operations()
print()

# 5. 数组与其他数据结构的比较
print("=== 5. 数组与其他数据结构的比较 ===")
def array_comparison():
    """比较array数组与列表、元组等其他数据结构"""
    import array
    import sys
    
    print("1. 内存占用比较:")
    
    # 创建包含1000000个整数的列表
    py_list = [i for i in range(1000000)]
    # 创建包含相同元素的array数组
    arr_int = array.array('i', py_list)
    
    print(f"Python列表内存占用: {sys.getsizeof(py_list)} 字节")
    print(f"array数组内存占用: {sys.getsizeof(arr_int)} 字节")
    print(f"内存节省比例: {(sys.getsizeof(py_list) - sys.getsizeof(arr_int)) / sys.getsizeof(py_list) * 100:.2f}%")
    
    print("\n2. 性能比较:")
    print("   - 对于基本的索引访问，array数组和列表性能相近")
    print("   - 对于大数据量的数学运算，array数组通常比列表更快")
    print("   - 与numpy数组相比，Python的array模块功能较少，但内存占用更小")
    
    print("\n3. 功能对比:")
    print("Python列表:")
    print("   - 可以存储不同类型的元素")
    print("   - 提供丰富的方法和操作")
    print("   - 内存占用较大")
    
    print("\narray数组:")
    print("   - 只能存储相同类型的数值")
    print("   - 提供类似列表的基本操作")
    print("   - 内存占用小，更高效")
    print("   - 支持文件I/O操作")
    
    print("\nnumpy数组:")
    print("   - 提供多维数组支持")
    print("   - 丰富的数学函数和向量化操作")
    print("   - 性能优异，适合科学计算")
    print("   - 第三方库，需要额外安装")
    
    print("\n4. 适用场景:")
    print("   - Python列表: 通用数据存储，混合类型数据，操作灵活")
    print("   - array数组: 大量数值数据，内存受限环境，需要文件I/O")
    print("   - numpy数组: 科学计算，数据分析，矩阵操作，高性能要求")

array_comparison()
print()

# 6. 文件I/O操作
print("=== 6. 文件I/O操作 ===")
def array_file_io():
    """展示array数组的文件I/O操作"""
    import array
    import os
    
    # 创建一个测试数组
    test_array = array.array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print(f"原始数组: {test_array}")
    
    # 定义文件名
    filename = 'array_test.bin'
    
    print("\n1. 写入数组到文件:")
    # 使用tofile方法将数组写入二进制文件
    with open(filename, 'wb') as f:
        test_array.tofile(f)
    print(f"数组已写入到文件 '{filename}'")
    
    print("\n2. 从文件读取数组:")
    # 创建一个新数组用于读取数据
    new_array = array.array('i')
    # 使用fromfile方法从文件读取数组
    with open(filename, 'rb') as f:
        new_array.fromfile(f, len(test_array))  # 读取指定数量的元素
    print(f"从文件读取的数组: {new_array}")
    
    print("\n3. 数组与bytes的转换:")
    # 使用tobytes方法转换为字节序列
    byte_data = test_array.tobytes()
    print(f"数组转换为bytes: {byte_data}")
    
    # 使用frombytes方法从字节序列创建数组
    bytes_array = array.array('i')
    bytes_array.frombytes(byte_data)
    print(f"从bytes创建的数组: {bytes_array}")
    
    # 清理测试文件
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\n测试文件 '{filename}' 已删除")

array_file_io()
print()

# 7. 高级应用示例
print("=== 7. 高级应用示例 ===")
def array_advanced_examples():
    """展示array模块的高级应用示例"""
    import array
    import struct
    import sys
    
    print("1. 高效存储大量数据:")
    def demonstrate_memory_efficiency():
        """演示array数组的内存效率"""
        # 比较不同数据类型的内存占用
        n = 1000000  # 一百万元素
        
        # 创建不同类型的数组
        arr_byte = array.array('b', (i % 128 for i in range(n)))
        arr_short = array.array('h', range(n))
        arr_int = array.array('i', range(n))
        arr_float = array.array('f', (float(i) for i in range(n)))
        arr_double = array.array('d', (float(i) for i in range(n)))
        
        # 创建Python列表用于比较
        py_list = list(range(n))
        py_float_list = [float(i) for i in range(n)]
        
        # 计算内存占用
        results = [
            ("Python列表(int)", sys.getsizeof(py_list)),
            ("Python列表(float)", sys.getsizeof(py_float_list)),
            ("array('b')", sys.getsizeof(arr_byte)),
            ("array('h')", sys.getsizeof(arr_short)),
            ("array('i')", sys.getsizeof(arr_int)),
            ("array('f')", sys.getsizeof(arr_float)),
            ("array('d')", sys.getsizeof(arr_double)),
        ]
        
        # 打印结果
        print(f"存储{n:,}个元素的内存占用比较:")
        for name, size in results:
            print(f"  {name:<20}: {size:,} 字节")
    
    demonstrate_memory_efficiency()
    
    print("\n2. 二进制数据处理:")
    def binary_data_handling():
        """演示如何处理二进制数据"""
        # 创建一个包含混合数据的二进制表示
        # 假设我们有：2个整数，1个浮点数，2个字节
        
        # 使用struct打包数据
        binary_data = struct.pack('iifbb', 100, 200, 3.14159, 65, 66)
        print(f"打包后的二进制数据: {binary_data}")
        
        # 使用array处理相同的数据
        # 注意：array要求单一数据类型，所以我们需要使用不同的数组
        int_array = array.array('i', [100, 200])
        float_array = array.array('f', [3.14159])
        byte_array = array.array('B', [65, 66])  # 使用无符号字节
        
        print(f"\n使用array存储的各部分数据:")
        print(f"整数部分: {int_array}")
        print(f"浮点数部分: {float_array}")
        print(f"字节部分: {byte_array}")
        
        # 模拟从二进制流中读取数据
        # 这里我们只是演示，实际应用中可能从文件或网络读取
        
        # 计算每种类型的字节数
        int_size = int_array.itemsize
        float_size = float_array.itemsize
        byte_size = byte_array.itemsize
        
        # 从二进制数据中提取整数
        int1, int2 = struct.unpack('ii', binary_data[:2*int_size])
        # 提取浮点数
        float_val = struct.unpack('f', binary_data[2*int_size:2*int_size+float_size])[0]
        # 提取字节
        byte1, byte2 = struct.unpack('BB', binary_data[2*int_size+float_size:])
        
        print(f"\n从二进制数据中解包的值:")
        print(f"整数1: {int1}, 整数2: {int2}")
        print(f"浮点数: {float_val}")
        print(f"字节1: {byte1} ({chr(byte1)}), 字节2: {byte2} ({chr(byte2)})")
    
    binary_data_handling()
    
    print("\n3. 模拟信号处理:")
    def signal_processing_simulation():
        """模拟信号处理应用"""
        import math
        
        # 生成模拟的正弦波数据
        frequency = 1.0  # 1Hz
        sampling_rate = 1000  # 每秒1000个采样点
        duration = 1.0  # 持续1秒
        amplitude = 1.0
        
        # 计算总采样点数
        num_samples = int(sampling_rate * duration)
        
        # 使用array存储信号数据
        signal = array.array('d')  # 使用双精度浮点数以获得更好的精度
        
        # 生成正弦波
        for i in range(num_samples):
            t = i / sampling_rate
            value = amplitude * math.sin(2 * math.pi * frequency * t)
            signal.append(value)
        
        print(f"生成了包含{num_samples}个采样点的正弦波信号")
        print(f"信号的前10个值: {signal[:10]}")
        
        # 计算信号的平均值
        avg_value = sum(signal) / len(signal)
        print(f"信号的平均值: {avg_value:.6f}")
        
        # 计算信号的最大值和最小值
        max_val = max(signal)
        min_val = min(signal)
        print(f"信号的最大值: {max_val:.6f}, 最小值: {min_val:.6f}")
        
        # 注意：在实际应用中，我们可能会使用numpy进行更复杂的信号处理
    
    signal_processing_simulation()

array_advanced_examples()
print()

# 8. 性能优化和注意事项
print("=== 8. 性能优化和注意事项 ===")
def array_performance_tips():
    """array模块的性能优化和注意事项"""
    print("1. 内存优化:")
    print("   - 选择最适合数据范围的类型代码，以最小化内存占用")
    print("   - 例如：如果数据范围在-128到127之间，使用'b'类型而非'i'类型")
    print("   - 对于不需要小数点的数值，优先使用整数类型")
    
    print("\n2. 性能考虑:")
    print("   - 创建数组时，尽可能一次性初始化，避免多次append操作")
    print("   - 使用extend()方法一次添加多个元素，而不是多次append()")
    print("   - 对于频繁的元素访问，array数组和Python列表性能相近")
    print("   - 对于大数据量的数学运算，考虑使用numpy库")
    
    print("\n3. 数据类型限制:")
    print("   - array数组只能存储相同类型的数值")
    print("   - 不能存储字符串、字典等非数值类型")
    print("   - 类型转换可能会导致精度损失（如int转float）")
    
    print("\n4. 溢出和精度问题:")
    print("   - 存储超出范围的值会导致溢出错误或未定义行为")
    print("   - 浮点数有精度限制，可能会有舍入误差")
    print("   - 处理大数值时应选择合适的整数类型（如'l', 'q'等）")
    
    print("\n5. 文件I/O注意事项:")
    print("   - tofile()和fromfile()方法以机器原生格式读写数据")
    print("   - 在不同架构的机器间传输数据时要小心字节序问题")
    print("   - 读取数据时要确保类型代码和数据大小匹配")
    print("   - 使用tobytes()和frombytes()方法可以更灵活地处理二进制数据")
    
    print("\n6. 与第三方库的配合:")
    print("   - 对于科学计算和数据分析，numpy提供了更丰富的功能")
    print("   - 可以将array数组转换为numpy数组以使用更多数学函数")
    print("   - array数组比numpy数组更轻量级，适合简单的内存高效存储")

array_performance_tips()
print()

# 9. 输入输出示例
print("=== 9. 输入输出示例 ===")

def array_io_examples():
    """array模块的输入输出示例"""
    print("\n示例1: 基本数组操作")
    print("输入:")
    print("    import array")
    print("    # 创建整数数组")
    print("    arr = array.array('i', [10, 20, 30, 40, 50])")
    print("    print(arr)")
    print("    # 添加元素")
    print("    arr.append(60)")
    print("    arr.extend([70, 80])")
    print("    print(arr)")
    print("    # 访问元素")
    print("    print(f'第一个元素: {arr[0]}')")
    print("    print(f'最后一个元素: {arr[-1]}')")
    print("    print(f'切片: {arr[2:5]}')")
    print("输出:")
    print("    array('i', [10, 20, 30, 40, 50])")
    print("    array('i', [10, 20, 30, 40, 50, 60, 70, 80])")
    print("    第一个元素: 10")
    print("    最后一个元素: 80")
    print("    切片: array('i', [30, 40, 50])")
    
    print("\n示例2: 数组的文件I/O操作")
    print("输入:")
    print("    import array")
    print("    import os")
    print("    ")
    print("    # 创建数组")
    print("    data = array.array('d', [1.1, 2.2, 3.3, 4.4, 5.5])")
    print("    filename = 'test_array.bin'")
    print("    ")
    print("    # 写入文件")
    print("    with open(filename, 'wb') as f:")
    print("        data.tofile(f)")
    print("    ")
    print("    # 读取文件")
    print("    new_data = array.array('d')")
    print("    with open(filename, 'rb') as f:")
    print("        new_data.fromfile(f, len(data))")
    print("    ")
    print("    print(f'原始数据: {data}')")
    print("    print(f'读取数据: {new_data}')")
    print("    ")
    print("    # 清理文件")
    print("    if os.path.exists(filename):")
    print("        os.remove(filename)")
    print("输出:")
    print("    原始数据: array('d', [1.1, 2.2, 3.3, 4.4, 5.5])")
    print("    读取数据: array('d', [1.1, 2.2, 3.3, 4.4, 5.5])")
    
    print("\n示例3: 内存效率对比")
    print("输入:")
    print("    import array")
    print("    import sys")
    print("    ")
    print("    # 创建包含1000个整数的列表")
    print("    py_list = [i for i in range(1000)]")
    print("    # 创建包含相同元素的array数组")
    print("    arr_int = array.array('i', py_list)")
    print("    arr_byte = array.array('B', (i % 256 for i in range(1000)))")
    print("    ")
    print("    print(f'Python列表: {sys.getsizeof(py_list)} 字节')")
    print("    print(f'array(int): {sys.getsizeof(arr_int)} 字节')")
    print("    print(f'array(byte): {sys.getsizeof(arr_byte)} 字节')")
    print("输出:")
    print("    Python列表: 8048 字节 (示例值，实际可能不同)")
    print("    array(int): 4040 字节 (示例值，实际可能不同)")
    print("    array(byte): 1040 字节 (示例值，实际可能不同)")
    
    print("\n示例4: 数组类型转换")
    print("输入:")
    print("    import array")
    print("    ")
    print("    # 创建整数数组")
    print("    int_arr = array.array('i', [10, 20, 30, 40, 50])")
    print("    print(f'整数数组: {int_arr}')")
    print("    ")
    print("    # 转换为浮点数数组")
    print("    float_arr = array.array('f', int_arr)")
    print("    print(f'浮点数数组: {float_arr}')")
    print("    ")
    print("    # 转换为Python列表")
    print("    py_list = list(int_arr)")
    print("    print(f'Python列表: {py_list}')")
    print("    ")
    print("    # 转换为bytes")
    print("    byte_data = int_arr.tobytes()")
    print("    print(f'bytes数据长度: {len(byte_data)} 字节')")
    print("    print(f'bytes前10个字节: {byte_data[:10]}')")
    print("输出:")
    print("    整数数组: array('i', [10, 20, 30, 40, 50])")
    print("    浮点数数组: array('f', [10.0, 20.0, 30.0, 40.0, 50.0])")
    print("    Python列表: [10, 20, 30, 40, 50]")
    print("    bytes数据长度: 20 字节")
    print("    bytes前10个字节: b'\n\x00\x00\x00\x14\x00\x00\x00\x1e\x00'")

array_io_examples()
print()

# 10. 总结和完整导入指南
print("=== 10. 总结和完整导入指南 ===")

def array_summary():
    """array模块总结和导入指南"""
    print("array模块提供了一种内存高效的方式来存储相同类型的数值数据。\n")
    
    # 主要特性
    print("主要特性:")
    print("- 只能存储相同类型的数值数据")
    print("- 相比Python列表占用更少的内存")
    print("- 支持基本的序列操作（索引、切片、迭代等）")
    print("- 提供高效的文件I/O操作")
    print("- 适用于需要存储大量数值数据的场景")
    
    # 常用方法
    print("\n常用方法:")
    print("- array(typecode[, initializer]): 创建数组")
    print("- append(x): 添加元素到数组末尾")
    print("- extend(iterable): 添加多个元素")
    print("- insert(i, x): 在指定位置插入元素")
    print("- remove(x): 删除第一个匹配的元素")
    print("- pop([i]): 删除并返回指定位置的元素")
    print("- index(x): 返回元素第一次出现的索引")
    print("- count(x): 统计元素出现的次数")
    print("- reverse(): 反转数组")
    print("- sort(): 排序数组")
    print("- tolist(): 转换为Python列表")
    print("- tofile(f): 写入数组到文件")
    print("- fromfile(f, n): 从文件读取n个元素")
    print("- tobytes(): 转换为字节序列")
    print("- frombytes(s): 从字节序列添加元素")
    
    # 导入指南
    print("\n导入指南:")
    print("\n1. 导入整个模块:")
    print("   import array")
    print("   arr = array.array('i', [1, 2, 3, 4, 5])")
    
    print("\n2. 直接导入array类:")
    print("   from array import array")
    print("   arr = array('i', [1, 2, 3, 4, 5])")
    
    # 版本兼容性
    print("\n版本兼容性:")
    print("- array模块在Python 2和Python 3中都可用")
    print("- 数据类型和大小可能因Python版本和平台而异")
    print("- 在Python 3中，'u'类型表示Py_UCS4，而在Python 2中表示Unicode字符")
    
    # 最终建议
    print("\n最终建议:")
    print("- 当需要存储大量数值数据且对内存效率有要求时使用array模块")
    print("- 选择合适的类型代码以最小化内存占用")
    print("- 对于复杂的数值计算和数据分析，考虑使用numpy库")
    print("- 在处理文件I/O时注意不同平台间的字节序问题")
    print("- 当需要存储混合类型数据时，使用Python列表或字典")

array_summary()

print("\n至此，array模块的全部功能已详细介绍完毕。")
