# Python lzma模块详解

```python
"""
lzma模块 - Python处理LZMA/XZ压缩文件的标准库

lzma模块提供了对LZMA（Lempel-Ziv-Markov chain Algorithm）压缩算法的支持，
允许创建、读取、写入和操作LZMA和XZ格式的压缩文件。

LZMA算法特点：
- 由Igor Pavlov开发，首次在7-Zip归档工具中使用
- 提供极高的压缩率，通常优于gzip和bzip2
- 可配置压缩级别和字典大小
- 支持多线程压缩（LZMA2格式）
- 内存消耗较大

主要功能：
- 压缩单个文件为LZMA/XZ格式
- 解压缩LZMA/XZ文件
- 在读写过程中自动压缩/解压缩数据
- 支持多种压缩格式（LZMA1、LZMA2、XZ）
- 支持压缩级别、字典大小等参数配置
- 支持文件对象接口
- 支持增量压缩和解压缩
- 支持自定义压缩参数

适用场景：
- 需要最高压缩率的文件存储
- 长期归档和备份
- 磁盘空间极其有限的环境
- 与tar结合使用创建tar.xz归档
- 压缩大型文本文件
"""

import lzma
import os
import shutil
from datetime import datetime
import tempfile
import io
import threading
import platform

# 示例数据准备
def prepare_example_files():
    """准备示例文件用于测试"""
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    print(f"创建临时目录: {temp_dir}")
    
    # 创建普通文本文件
    text_file_path = os.path.join(temp_dir, "example.txt")
    with open(text_file_path, "w", encoding="utf-8") as f:
        # 写入一些可压缩的文本内容
        f.write("这是一个用于测试LZMA压缩的示例文件。\n")
        f.write("LZMA模块可以提供比gzip和bzip2更高的压缩率，特别适合大型文本数据。\n")
        # 添加一些重复内容以提高压缩效果
        f.write("重复内容 " * 300)
        f.write("\n")
        # 添加一些数字和特殊字符
        for i in range(300):
            f.write(f"行号: {i:04d}, 随机数字: {i*123456789 % 10000}\n")
    
    # 创建二进制文件
    binary_file_path = os.path.join(temp_dir, "binary.dat")
    with open(binary_file_path, "wb") as f:
        # 写入一些二进制数据
        data = bytearray(30000)  # 30KB数据
        for i in range(30000):
            data[i] = i % 256
        f.write(data)
    
    return temp_dir, text_file_path, binary_file_path

# 清理示例文件
def cleanup_example_files(temp_dir):
    """清理示例文件"""
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        print(f"清理临时目录: {temp_dir}")

# 1. lzma文件的基本操作
def basic_lzma_operations():
    """
    lzma模块的基本操作
    
    功能说明：演示创建、读取和写入LZMA/XZ压缩文件的基本方法。
    """
    print("=== 1. lzma模块的基本操作 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, binary_file_path = prepare_example_files()
    
    try:
        # 1.1 创建XZ压缩文件
        xz_file_path = os.path.join(temp_dir, "example.txt.xz")
        
        # 方法1: 使用lzma.open
        print("\n1.1.1 使用lzma.open创建压缩文件:")
        with open(text_file_path, "rb") as f_in:
            with lzma.open(xz_file_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了压缩文件: {xz_file_path}")
        print(f"原始文件大小: {os.path.getsize(text_file_path)} 字节")
        print(f"压缩文件大小: {os.path.getsize(xz_file_path)} 字节")
        print(f"压缩率: {(1 - os.path.getsize(xz_file_path) / os.path.getsize(text_file_path)) * 100:.2f}%")
        
        # 方法2: 使用LZMAFile对象
        print("\n1.1.2 使用LZMAFile对象创建压缩文件:")
        xz_file_path2 = os.path.join(temp_dir, "example2.txt.xz")
        
        with open(text_file_path, "rb") as f_in:
            with lzma.LZMAFile(xz_file_path2, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了压缩文件: {xz_file_path2}")
        
        # 1.2 读取XZ压缩文件
        print("\n1.2.1 读取压缩文件内容:")
        with lzma.open(xz_file_path, "rb") as f:
            content = f.read().decode("utf-8")
            # 只显示前200个字符
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"文件内容预览: {preview}")
        
        # 1.3 写入文本到XZ文件（直接写入，不经过中间文件）
        print("\n1.3.1 直接写入文本到压缩文件:")
        text_xz_path = os.path.join(temp_dir, "direct_text.txt.xz")
        
        with lzma.open(text_xz_path, "wt", encoding="utf-8") as f:
            f.write("这是直接写入到XZ文件的文本内容。\n")
            f.write("lzma模块支持文本模式，可以自动处理编码。\n")
        
        print(f"创建了直接写入的压缩文件: {text_xz_path}")
        
        # 验证写入是否成功
        with lzma.open(text_xz_path, "rt", encoding="utf-8") as f:
            content = f.read()
            print(f"读取的内容: {content}")
        
        # 1.4 创建纯LZMA格式文件
        print("\n1.4.1 创建纯LZMA格式文件:")
        lzma_file_path = os.path.join(temp_dir, "example.txt.lzma")
        
        # 需要指定format=lzma.FORMAT_RAW
        with open(text_file_path, "rb") as f_in:
            with lzma.open(lzma_file_path, "wb", format=lzma.FORMAT_RAW, filters=[{"id": lzma.FILTER_LZMA1}]) as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了纯LZMA格式文件: {lzma_file_path}")
        print(f"原始文件大小: {os.path.getsize(text_file_path)} 字节")
        print(f"压缩文件大小: {os.path.getsize(lzma_file_path)} 字节")
        print(f"压缩率: {(1 - os.path.getsize(lzma_file_path) / os.path.getsize(text_file_path)) * 100:.2f}%")
            
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 2. 压缩级别和参数控制
def compression_level_and_params_control():
    """
    lzma压缩级别和参数控制
    
    功能说明：演示如何控制lzma压缩级别和其他参数，如字典大小、块大小等。
    """
    print("\n=== 2. 压缩级别和参数控制 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, _ = prepare_example_files()
    
    try:
        # 2.1 测试不同压缩级别
        print("\n2.1 测试不同压缩级别:")
        print("压缩级别 | 文件大小(字节) | 压缩率(%) | 耗时(秒)")
        print("----------|---------------|-----------|---------")
        
        # lzma压缩级别从0到9
        results = []
        
        for level in range(0, 10):
            xz_file_path = os.path.join(temp_dir, f"example_level_{level}.txt.xz")
            
            # 测量压缩时间
            start_time = datetime.now()
            
            with open(text_file_path, "rb") as f_in:
                with lzma.open(xz_file_path, "wb", preset=level) as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            duration = (datetime.now() - start_time).total_seconds()
            
            # 计算压缩结果
            original_size = os.path.getsize(text_file_path)
            compressed_size = os.path.getsize(xz_file_path)
            compression_ratio = (1 - compressed_size / original_size) * 100
            
            results.append({
                "level": level,
                "size": compressed_size,
                "ratio": compression_ratio,
                "time": duration
            })
            
            print(f"{level:10d} | {compressed_size:13d} | {compression_ratio:9.2f} | {duration:8.4f}")
        
        # 分析结果
        print("\n压缩级别分析:")
        print(f"最小文件大小: 级别{min(results, key=lambda x: x['size'])['level']}, {min(results, key=lambda x: x['size'])['size']} 字节")
        print(f"最快压缩速度: 级别{min(results, key=lambda x: x['time'])['level']}, {min(results, key=lambda x: x['time'])['time']:.4f} 秒")
        
        # 2.2 测试不同字典大小
        print("\n2.2 测试不同字典大小:")
        print("字典大小(KB) | 文件大小(字节) | 压缩率(%) | 耗时(秒)")
        print("--------------|---------------|-----------|---------")
        
        # 测试不同的字典大小（LZMA2格式）
        dict_sizes = [64, 256, 1024, 4096, 8192]  # KB
        dict_results = []
        
        for dict_size_kb in dict_sizes:
            dict_size = dict_size_kb * 1024  # 转换为字节
            xz_file_path = os.path.join(temp_dir, f"example_dict_{dict_size_kb}k.txt.xz")
            
            # 创建自定义过滤器
            filters = [
                {
                    "id": lzma.FILTER_LZMA2,
                    "dict_size": dict_size,
                    "preset": 6  # 基础级别
                }
            ]
            
            # 测量压缩时间
            start_time = datetime.now()
            
            with open(text_file_path, "rb") as f_in:
                with lzma.open(xz_file_path, "wb", format=lzma.FORMAT_XZ, filters=filters) as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            duration = (datetime.now() - start_time).total_seconds()
            
            # 计算压缩结果
            original_size = os.path.getsize(text_file_path)
            compressed_size = os.path.getsize(xz_file_path)
            compression_ratio = (1 - compressed_size / original_size) * 100
            
            dict_results.append({
                "dict_size": dict_size_kb,
                "size": compressed_size,
                "ratio": compression_ratio,
                "time": duration
            })
            
            print(f"{dict_size_kb:14d} | {compressed_size:13d} | {compression_ratio:9.2f} | {duration:8.4f}")
        
        print("\n字典大小分析:")
        print(f"最小文件大小: {min(dict_results, key=lambda x: x['size'])['dict_size']}KB, {min(dict_results, key=lambda x: x['size'])['size']} 字节")
        print(f"最快压缩速度: {min(dict_results, key=lambda x: x['time'])['dict_size']}KB, {min(dict_results, key=lambda x: x['time'])['time']:.4f} 秒")
        
        # 2.3 自定义压缩参数
        print("\n2.3 自定义压缩参数:")
        print("lzma模块支持丰富的压缩参数配置:")
        print("- preset: 预设级别(0-9)，自动设置其他参数")
        print("- format: 压缩格式(FORMAT_XZ, FORMAT_ALONE, FORMAT_RAW等)")
        print("- check: 校验和类型(CHECK_NONE, CHECK_CRC32, CHECK_CRC64, CHECK_SHA256)")
        print("- filters: 自定义过滤器列表，可配置详细参数")
        
        # 示例：自定义压缩参数
        print("\n自定义压缩参数示例:")
        custom_params = [
            {
                "id": lzma.FILTER_LZMA2,
                "preset": 7,
                "dict_size": 4 * 1024 * 1024,  # 4MB字典
                "lc": 3,  # 字面量上下文位数
                "lp": 0,  # 字面量位置位数
                "pb": 2,  # 位置位数
                "mode": lzma.MODE_FAST,  # 模式
                "mf": lzma.MF_HC3  # 匹配查找算法
            }
        ]
        
        custom_xz_path = os.path.join(temp_dir, "example_custom.txt.xz")
        
        with open(text_file_path, "rb") as f_in:
            with lzma.open(custom_xz_path, "wb", format=lzma.FORMAT_XZ, filters=custom_params, check=lzma.CHECK_CRC64) as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"使用自定义参数创建的文件大小: {os.path.getsize(custom_xz_path)} 字节")
            
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 3. 内存中压缩和解压缩
def in_memory_operations():
    """
    内存中的lzma操作
    
    功能说明：演示如何在内存中对数据进行lzma压缩和解压缩，不涉及文件操作。
    这对于处理数据流或API交互特别有用。
    """
    print("\n=== 3. 内存中的lzma操作 ===")
    
    # 3.1 压缩内存中的数据
    print("\n3.1 压缩内存中的数据:")
    
    # 示例数据
    original_data = "这是一段需要在内存中压缩的数据。" * 300  # 复制多次以便观察压缩效果
    original_bytes = original_data.encode("utf-8")
    
    print(f"原始数据大小: {len(original_bytes)} 字节")
    
    # 使用lzma.compress直接压缩
    compressed_data = lzma.compress(original_bytes)
    print(f"压缩后数据大小: {len(compressed_data)} 字节")
    print(f"压缩率: {(1 - len(compressed_data) / len(original_bytes)) * 100:.2f}%")
    
    # 使用io.BytesIO在内存中压缩（更灵活的方式）
    compressed_buffer = io.BytesIO()
    
    with lzma.LZMAFile(fileobj=compressed_buffer, mode="wb") as f:
        f.write(original_bytes)
    
    # 获取压缩后的数据
    compressed_data_alt = compressed_buffer.getvalue()
    print(f"使用LZMAFile压缩后数据大小: {len(compressed_data_alt)} 字节")
    print(f"两种压缩方法结果比较: {'相同' if compressed_data == compressed_data_alt else '不同'}")
    
    # 3.2 解压缩内存中的数据
    print("\n3.2 解压缩内存中的数据:")
    
    # 使用lzma.decompress直接解压缩
    decompressed_data = lzma.decompress(compressed_data)
    print(f"解压缩后数据大小: {len(decompressed_data)} 字节")
    print(f"数据完整性验证: {'成功' if decompressed_data == original_bytes else '失败'}")
    
    # 使用io.BytesIO在内存中解压缩
    decompressed_buffer = io.BytesIO(compressed_data)
    
    with lzma.LZMAFile(fileobj=decompressed_buffer, mode="rb") as f:
        decompressed_data_alt = f.read()
    
    print(f"使用LZMAFile解压缩后数据大小: {len(decompressed_data_alt)} 字节")
    print(f"解压缩结果比较: {'相同' if decompressed_data == decompressed_data_alt else '不同'}")
    
    # 3.3 使用不同的压缩预设级别
    print("\n3.3 使用不同的压缩预设级别:")
    
    for preset in [0, 3, 6, 9]:
        start_time = datetime.now()
        compressed = lzma.compress(original_bytes, preset=preset)
        duration = (datetime.now() - start_time).total_seconds()
        
        print(f"预设级别 {preset}: 压缩大小={len(compressed)} 字节, 耗时={duration:.4f}秒, 压缩率={(1 - len(compressed)/len(original_bytes))*100:.2f}%")
    
    # 3.4 使用自定义压缩参数进行内存压缩
    print("\n3.4 使用自定义压缩参数进行内存压缩:")
    
    # 自定义过滤器
    filters = [
        {
            "id": lzma.FILTER_LZMA2,
            "preset": 6,
            "dict_size": 1024 * 1024  # 1MB字典
        }
    ]
    
    # 使用自定义参数压缩
    custom_compressed = lzma.compress(original_bytes, format=lzma.FORMAT_XZ, filters=filters)
    print(f"自定义参数压缩大小: {len(custom_compressed)} 字节")
    print(f"标准压缩大小: {len(lzma.compress(original_bytes, preset=6))} 字节")

# 4. 增量压缩和解压缩
def incremental_operations():
    """
    增量压缩和解压缩
    
    功能说明：演示如何使用lzma的增量压缩和解压缩功能，这对于处理流式数据或大型数据特别有用。
    """
    print("\n=== 4. 增量压缩和解压缩 ===")
    
    # 4.1 增量压缩
    print("\n4.1 增量压缩:")
    
    # 创建一个增量压缩对象
    compressor = lzma.LZMACompressor()
    
    # 分多次压缩数据
    chunks = [
        b"这是第一部分数据，",
        b"这是第二部分数据，",
        b"这是第三部分数据。"
    ]
    
    compressed_chunks = []
    
    print("开始增量压缩:")
    for i, chunk in enumerate(chunks, 1):
        # 压缩当前数据块
        compressed = compressor.compress(chunk)
        compressed_chunks.append(compressed)
        print(f"压缩块 {i}: 原始大小 {len(chunk)} 字节, 压缩后大小 {len(compressed)} 字节")
    
    # 完成压缩过程，获取最后一块数据
    final_compressed = compressor.flush()
    compressed_chunks.append(final_compressed)
    print(f"压缩结束块: 大小 {len(final_compressed)} 字节")
    
    # 合并所有压缩块
    total_compressed = b""
    for chunk in compressed_chunks:
        total_compressed += chunk
    
    print(f"总压缩大小: {len(total_compressed)} 字节")
    
    # 4.2 增量解压缩
    print("\n4.2 增量解压缩:")
    
    # 创建一个增量解压缩对象
    decompressor = lzma.LZMADecompressor()
    
    # 分多次解压缩数据
    # 这里我们故意将压缩数据分成更小的块来模拟流式解压缩
    compressed_size = len(total_compressed)
    chunk_size = max(1, compressed_size // 5)  # 将数据分成5块
    
    decompressed_chunks = []
    processed = 0
    
    print("开始增量解压缩:")
    while processed < compressed_size:
        chunk_end = min(processed + chunk_size, compressed_size)
        chunk = total_compressed[processed:chunk_end]
        
        try:
            # 解压缩当前数据块
            decompressed = decompressor.decompress(chunk)
            decompressed_chunks.append(decompressed)
            print(f"解压缩块: 处理字节 {processed}-{chunk_end}, 解压后大小 {len(decompressed)} 字节")
        except Exception as e:
            print(f"解压缩错误: {e}")
            break
        
        processed = chunk_end
    
    # 合并所有解压缩块
    total_decompressed = b""
    for chunk in decompressed_chunks:
        total_decompressed += chunk
    
    # 合并原始数据以便比较
    original_total = b""
    for chunk in chunks:
        original_total += chunk
    
    print(f"总解压缩大小: {len(total_decompressed)} 字节")
    print(f"数据完整性验证: {'成功' if total_decompressed == original_total else '失败'}")
    print(f"解压内容: {total_decompressed.decode('utf-8')}")
    
    # 4.3 使用不同格式进行增量压缩
    print("\n4.3 使用不同格式进行增量压缩:")
    
    # 测试XZ格式
    print("\n使用XZ格式:")
    compressor_xz = lzma.LZMACompressor(format=lzma.FORMAT_XZ, preset=6)
    
    for i, chunk in enumerate(chunks, 1):
        compressed = compressor_xz.compress(chunk)
        print(f"XZ压缩块 {i}: 压缩后大小 {len(compressed)} 字节")
    
    final_compressed_xz = compressor_xz.flush()
    print(f"XZ结束块: 大小 {len(final_compressed_xz)} 字节")
    
    # 测试LZMA格式
    print("\n使用LZMA格式:")
    # 对于LZMA格式，我们需要指定原始格式和过滤器
    filters = [{"id": lzma.FILTER_LZMA1}]
    compressor_lzma = lzma.LZMACompressor(format=lzma.FORMAT_RAW, filters=filters)
    
    for i, chunk in enumerate(chunks, 1):
        compressed = compressor_lzma.compress(chunk)
        print(f"LZMA压缩块 {i}: 压缩后大小 {len(compressed)} 字节")
    
    final_compressed_lzma = compressor_lzma.flush()
    print(f"LZMA结束块: 大小 {len(final_compressed_lzma)} 字节")

# 5. 流式处理大型数据
def streaming_large_data():
    """
    流式处理大型数据
    
    功能说明：演示如何使用lzma模块处理大型数据，避免一次性加载全部数据到内存。
    这对于处理大型文件特别重要。
    """
    print("\n=== 5. 流式处理大型数据 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, binary_file_path = prepare_example_files()
    
    # 创建一个更大的文件用于测试
    large_file_path = os.path.join(temp_dir, "large_file.txt")
    with open(large_file_path, "w", encoding="utf-8") as f:
        # 写入大约20MB的数据
        for i in range(200000):
            f.write(f"这是大型文件的第{i:07d}行内容，包含一些可压缩的数据，LZMA对文本有很好的压缩效果。\n")
    
    try:
        # 5.1 分块压缩大型文件
        print("\n5.1 分块压缩大型文件:")
        
        xz_large_path = os.path.join(temp_dir, "large_file.txt.xz")
        chunk_size = 16384  # 16KB块
        
        print(f"开始压缩大型文件: {large_file_path}")
        print(f"原始文件大小: {os.path.getsize(large_file_path):,} 字节")
        
        start_time = datetime.now()
        
        with open(large_file_path, "rb") as f_in:
            with lzma.open(xz_large_path, "wb", preset=6) as f_out:
                while True:
                    chunk = f_in.read(chunk_size)
                    if not chunk:
                        break
                    f_out.write(chunk)
        
        compression_time = (datetime.now() - start_time).total_seconds()
        
        compressed_size = os.path.getsize(xz_large_path)
        compression_ratio = (1 - compressed_size / os.path.getsize(large_file_path)) * 100
        
        print(f"压缩完成，耗时: {compression_time:.2f} 秒")
        print(f"压缩文件大小: {compressed_size:,} 字节")
        print(f"压缩率: {compression_ratio:.2f}%")
        print(f"压缩速度: {os.path.getsize(large_file_path) / (1024 * 1024 * compression_time):.2f} MB/s")
        
        # 5.2 分块解压缩大型文件
        print("\n5.2 分块解压缩大型文件:")
        
        decompressed_path = os.path.join(temp_dir, "decompressed_large.txt")
        
        print(f"开始解压缩: {xz_large_path}")
        
        start_time = datetime.now()
        
        with lzma.open(xz_large_path, "rb") as f_in:
            with open(decompressed_path, "wb") as f_out:
                while True:
                    chunk = f_in.read(chunk_size)
                    if not chunk:
                        break
                    f_out.write(chunk)
        
        decompression_time = (datetime.now() - start_time).total_seconds()
        
        print(f"解压缩完成，耗时: {decompression_time:.2f} 秒")
        print(f"解压后文件大小: {os.path.getsize(decompressed_path):,} 字节")
        print(f"解压缩速度: {compressed_size / (1024 * 1024 * decompression_time):.2f} MB/s")
        
        # 验证解压后的文件与原始文件是否一致
        original_content = open(large_file_path, "rb").read()
        decompressed_content = open(decompressed_path, "rb").read()
        print(f"文件完整性验证: {'成功' if original_content == decompressed_content else '失败'}")
        
        # 5.3 使用生成器逐行处理压缩文件
        print("\n5.3 使用生成器逐行处理压缩文件:")
        print("示例代码 - 使用生成器逐行读取LZMA压缩文件:")
        print("""
        def read_lzma_file_line_by_line(xz_path):
            """使用生成器逐行读取LZMA压缩文件"""
            with lzma.open(xz_path, "rt", encoding="utf-8") as f:
                for line in f:
                    yield line.rstrip('\n')
        
        # 使用示例
        # for i, line in enumerate(read_lzma_file_line_by_line(xz_large_path), 1):
        #     if i <= 5:  # 只打印前5行
        #         print(f"第{i}行: {line}")
        #     elif i == 6:
        #         print("... 省略中间内容 ...")
        #     elif i > 199995:
        #         print(f"第{i}行: {line}")
        """)
        
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 6. 与tarfile模块结合使用
def combined_with_tarfile():
    """
    与tarfile模块结合使用
    
    功能说明：演示如何将lzma与tarfile模块结合使用，创建tar.xz归档文件。
    这是处理多文件目录归档的常见方式，提供极高的压缩率。
    """
    print("\n=== 6. 与tarfile模块结合使用 ===")
    
    # 准备示例文件和目录
    temp_dir = tempfile.mkdtemp()
    print(f"创建临时目录: {temp_dir}")
    
    # 创建一些测试文件和子目录
    subdir_path = os.path.join(temp_dir, "subdir")
    os.makedirs(subdir_path, exist_ok=True)
    
    # 创建几个测试文件
    for i in range(3):
        file_path = os.path.join(temp_dir, f"test_file_{i}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"这是测试文件 {i} 的内容。\n" * 100)
    
    for i in range(2):
        file_path = os.path.join(subdir_path, f"sub_file_{i}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"这是子目录中的测试文件 {i} 的内容。\n" * 50)
    
    try:
        print("\n6.1 创建tar.xz归档文件:")
        
        import tarfile
        
        tar_xz_path = os.path.join(temp_dir, "archive.tar.xz")
        
        print(f"创建归档文件: {tar_xz_path}")
        print("包含的文件和目录:")
        
        # 列出将要归档的内容
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file != os.path.basename(tar_xz_path):  # 排除归档文件自身
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, temp_dir)
                    print(f"  {rel_path}")
        
        # 创建tar.xz归档
        start_time = datetime.now()
        
        # 方法1: 使用tarfile.open并指定mode='w:xz'
        with tarfile.open(tar_xz_path, "w:xz", compresslevel=6) as tar:
            # 添加根目录下的文件（除了归档文件本身）
            for item in os.listdir(temp_dir):
                item_path = os.path.join(temp_dir, item)
                if item_path != tar_xz_path:  # 排除归档文件自身
                    arcname = os.path.basename(item_path)
                    tar.add(item_path, arcname=arcname)
        
        compression_time = (datetime.now() - start_time).total_seconds()
        
        print(f"归档完成，耗时: {compression_time:.2f} 秒")
        print(f"归档文件大小: {os.path.getsize(tar_xz_path):,} 字节")
        
        # 6.2 读取tar.xz归档文件内容
        print("\n6.2 读取tar.xz归档文件内容:")
        
        with tarfile.open(tar_xz_path, "r:xz") as tar:
            # 列出归档中的所有文件
            print("归档中的文件列表:")
            for member in tar.getmembers():
                print(f"  {member.name} (大小: {member.size:,} 字节)")
            
            # 读取一个文件的内容
            first_file = tar.getmembers()[0]
            if first_file.isfile():
                file_obj = tar.extractfile(first_file)
                if file_obj:
                    content = file_obj.read(200).decode("utf-8")  # 只读取前200个字符
                    print(f"\n第一个文件 '{first_file.name}' 的内容预览: {content}...")
        
        # 6.3 解压tar.xz归档文件
        print("\n6.3 解压tar.xz归档文件:")
        
        extract_dir = os.path.join(temp_dir, "extracted")
        os.makedirs(extract_dir, exist_ok=True)
        
        print(f"解压到目录: {extract_dir}")
        
        start_time = datetime.now()
        
        with tarfile.open(tar_xz_path, "r:xz") as tar:
            tar.extractall(extract_dir)
        
        extraction_time = (datetime.now() - start_time).total_seconds()
        
        print(f"解压完成，耗时: {extraction_time:.2f} 秒")
        print("解压后的文件:")
        
        # 列出解压后的文件
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, extract_dir)
                print(f"  {rel_path}")
        
        # 6.4 与其他压缩格式对比
        print("\n6.4 与其他压缩格式对比:")
        
        # 创建不同压缩格式的tar文件
        formats = [
            ("gz", "w:gz", 9),    # gzip格式
            ("bz2", "w:bz2", 9),  # bzip2格式
            ("xz", "w:xz", 6)     # xz格式
        ]
        
        print("格式 | 文件大小(字节) | 压缩时间(秒) | 解压时间(秒)")
        print("------|---------------|-------------|-------------")
        
        for ext, mode, level in formats:
            # 创建归档
            tar_path = os.path.join(temp_dir, f"archive.tar.{ext}")
            
            # 压缩
            start_time = datetime.now()
            with tarfile.open(tar_path, mode, compresslevel=level) as tar:
                for item in os.listdir(temp_dir):
                    item_path = os.path.join(temp_dir, item)
                    if item_path != tar_xz_path and item_path != tar_path:
                        arcname = os.path.basename(item_path)
                        tar.add(item_path, arcname=arcname)
            
            comp_time = (datetime.now() - start_time).total_seconds()
            
            # 解压
            extract_path = os.path.join(temp_dir, f"extracted_{ext}")
            os.makedirs(extract_path, exist_ok=True)
            
            start_time = datetime.now()
            with tarfile.open(tar_path, f"r:{ext}") as tar:
                tar.extractall(extract_path)
            
            decomp_time = (datetime.now() - start_time).total_seconds()
            
            file_size = os.path.getsize(tar_path)
            print(f"tar.{ext:<5} | {file_size:13d} | {comp_time:11.2f} | {decomp_time:11.2f}")
            
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 7. 性能考量与优化
def performance_considerations():
    """
    lzma模块的性能考量与优化
    
    功能说明：分析lzma模块的性能特点并提供优化建议。
    """
    print("\n=== 7. 性能考量与优化 ===")
    
    print("\n7.1 lzma与其他压缩算法比较:")
    print("  压缩算法比较概览:")
    print("  - gzip: 速度快，压缩率中等，内存消耗低")
    print("  - bz2: 速度中等，压缩率高，内存消耗较高")
    print("  - lzma/xz: 速度慢，压缩率最高，内存消耗高")
    
    print("\n7.2 lzma性能特点:")
    print("1. 压缩和解压缩速度")
    print("   - lzma是所有内置压缩算法中速度最慢的")
    print("   - 压缩速度通常比gzip慢5-10倍")
    print("   - 解压缩速度比压缩速度快，但仍比gzip和bzip2慢")
    print("   - 各级别之间的速度差异较大")
    
    print("\n2. 内存使用")
    print("   - lzma比gzip和bzip2使用更多的内存")
    print("   - 字典大小直接影响内存消耗")
    print("   - 高压缩级别需要更多内存")
    print("   - 处理大文件时需要特别注意内存限制")
    
    print("\n3. 压缩率")
    print("   - lzma提供最高的压缩率，通常比bzip2高10-30%")
    print("   - 对于大型文件和有重复模式的数据效果更好")
    print("   - 对于小文件，压缩头信息可能会影响整体效率")
    
    print("\n7.3 性能优化建议:")
    print("1. 选择合适的压缩参数")
    print("   - 对于大多数场景，预设级别6是速度和压缩率的良好平衡")
    print("   - 考虑使用较小的字典大小以减少内存使用")
    print("   - 仅在绝对需要最高压缩率时使用级别9")
    
    print("\n2. 内存优化")
    print("   - 为大文件设置适当的字典大小，避免过度消耗内存")
    print("   - 使用流式处理而非一次性加载整个文件")
    print("   - 监控内存使用情况，尤其是处理多个文件时")
    
    print("\n3. 并行处理")
    print("   - 处理多个文件时使用多线程或多进程")
    print("   - 注意I/O瓶颈")
    print("   - 对于单一大文件，考虑分段压缩后合并")
    
    print("\n4. 其他优化")
    print("   - 使用LZMA2格式(默认)，它比LZMA1格式更高效")
    print("   - 选择合适的校验和类型(CONTENTION_NONE最快)")
    print("   - 预分块大型文件以提高并行处理效率")
    
    print("\n7.4 字典大小与内存使用关系:")
    print("  - 字典大小直接影响压缩率和内存使用")
    print("  - 推荐字典大小设置:")
    print("    * 小文件(<10MB): 256KB-1MB")
    print("    * 中等文件(10MB-100MB): 1MB-8MB")
    print("    * 大文件(>100MB): 8MB-64MB")
    print("  - 通常字典大小不应超过可用内存的10%")
    print(f"  - 当前系统: {platform.system()} {platform.release()}")

# 8. 错误处理和安全性
def error_handling_and_security():
    """
    lzma模块的错误处理和安全性
    
    功能说明：演示如何正确处理lzma相关的错误以及安全使用lzma模块的建议。
    """
    print("\n=== 8. 错误处理和安全性 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, _ = prepare_example_files()
    
    try:
        # 创建一个正常的xz文件
        valid_xz_path = os.path.join(temp_dir, "valid.txt.xz")
        with lzma.open(valid_xz_path, "wb") as f:
            f.write(b"这是一个有效的xz压缩文件的内容。")
        
        # 创建一个无效的xz文件（只是普通文本）
        invalid_xz_path = os.path.join(temp_dir, "invalid.txt.xz")
        with open(invalid_xz_path, "wb") as f:
            f.write(b"这不是一个有效的xz文件。")
        
        print("\n8.1 错误处理示例:")
        print("处理无效的xz文件:")
        
        try:
            with lzma.open(invalid_xz_path, "rb") as f:
                content = f.read()
                print("读取成功:", content)
        except lzma.LZMAError as e:
            print(f"捕获到LZMA错误: {e}")
        except Exception as e:
            print(f"捕获到其他错误: {e}")
        
        # 8.2 内存限制处理
        print("\n8.2 内存限制处理:")
        
        # 尝试创建一个使用过多内存的配置
        try:
            # 使用过大的字典大小(1GB)来测试内存限制
            print("尝试使用过大的字典大小:")
            
            filters = [
                {
                    "id": lzma.FILTER_LZMA2,
                    "dict_size": 1024 * 1024 * 1024,  # 1GB字典
                    "preset": 6
                }
            ]
            
            memory_test_path = os.path.join(temp_dir, "memory_test.txt.xz")
            
            with open(text_file_path, "rb") as f_in:
                with lzma.open(memory_test_path, "wb", format=lzma.FORMAT_XZ, filters=filters) as f_out:
                    shutil.copyfileobj(f_in, f_out)
        except Exception as e:
            print(f"内存相关错误: {e}")
            print("这表明系统对LZMA字典大小有内存限制")
        
        # 8.3 安全使用建议
        print("\n8.3 安全使用建议:")
        print("1. 输入验证")
        print("   - 始终验证输入文件的有效性")
        print("   - 对用户提供的文件格外小心")
        print("   - 使用try-except块捕获潜在的压缩/解压缩错误")
        
        print("\n2. 防止资源耗尽攻击")
        print("   - 限制最大解压缩大小，防止解压炸弹攻击")
        print("   - 限制最大字典大小")
        print("   - 实现超时机制")
        print("   - 监控内存使用")
        
        print("\n3. 解压炸弹防护示例:")
        print("""
        def safe_decompress(compressed_data, max_size=100*1024*1024):  # 100MB限制
            """安全解压缩数据，防止解压炸弹"""
            decompressor = lzma.LZMADecompressor()
            result = bytearray()
            
            # 分块解压缩
            chunk_size = 8192
            for i in range(0, len(compressed_data), chunk_size):
                chunk = compressed_data[i:i+chunk_size]
                try:
                    decompressed_chunk = decompressor.decompress(chunk)
                except lzma.LZMAError as e:
                    raise ValueError(f"无效的LZMA数据: {e}")
                
                # 检查解压缩后的大小
                if len(result) + len(decompressed_chunk) > max_size:
                    raise ValueError(f"解压缩数据过大，超过限制 {max_size} 字节")
                
                result.extend(decompressed_chunk)
                
                # 检查是否已经完成解压缩
                if decompressor.eof:
                    # 检查是否有未处理的数据
                    if i + chunk_size < len(compressed_data):
                        raise ValueError("压缩数据中包含多个压缩流")
                    break
            
            # 确保解压缩完成
            if not decompressor.eof:
                raise ValueError("不完整的LZMA数据")
                
            return bytes(result)
        """)
        
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 9. 实际应用示例
def real_world_examples():
    """
    lzma模块的实际应用示例
    
    功能说明：提供lzma模块在实际项目中的应用示例代码。
    """
    print("\n=== 9. 实际应用示例 ===")
    
    print("\n9.1 高压缩率归档工具:")
    print("""
    import lzma
    import os
    import shutil
    import argparse
    import logging
    from datetime import datetime, timedelta
    import glob
    import tempfile
    
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("high_compress_archiver.log"),
            logging.StreamHandler()
        ]
    )
    
    def create_high_compression_archive(source_paths, output_path, 
                                      preset=6, dict_size=None, 
                                      exclude_patterns=None, 
                                      dry_run=False):
        """
        创建高压缩率的归档文件
        
        参数:
        - source_paths: 源文件/目录路径列表
        - output_path: 输出归档文件路径
        - preset: LZMA预设级别(0-9)
        - dict_size: 字典大小(字节)，None表示使用预设默认值
        - exclude_patterns: 排除的文件模式列表
        - dry_run: 仅显示将要归档的文件，不实际创建
        """
        import tarfile
        
        # 验证源路径
        for path in source_paths:
            if not os.path.exists(path):
                logging.error(f"源路径不存在: {path}")
                return False
        
        # 准备过滤器
        filters = []
        if dict_size is not None:
            # 自定义过滤器
            filters.append({
                "id": lzma.FILTER_LZMA2,
                "preset": preset,
                "dict_size": dict_size
            })
        
        # 收集所有要归档的文件
        all_files = []
        for path in source_paths:
            if os.path.isfile(path):
                all_files.append(path)
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        all_files.append(file_path)
        
        # 应用排除模式
        if exclude_patterns:
            original_count = len(all_files)
            filtered_files = []
            for file in all_files:
                excluded = False
                for pattern in exclude_patterns:
                    import fnmatch
                    if fnmatch.fnmatch(file, pattern):
                        excluded = True
                        break
                if not excluded:
                    filtered_files.append(file)
            all_files = filtered_files
            logging.info(f"排除了 {original_count - len(all_files)} 个文件")
        
        if not all_files:
            logging.error("没有找到要归档的文件")
            return False
        
        logging.info(f"找到 {len(all_files)} 个文件待归档")
        
        # 显示文件列表（dry_run模式）
        if dry_run:
            logging.info("Dry run模式，将显示文件列表但不实际创建归档")
            for file in all_files[:10]:  # 只显示前10个文件
                logging.info(f"将归档: {file}")
            if len(all_files) > 10:
                logging.info(f"... 以及其他 {len(all_files) - 10} 个文件")
            return True
        
        # 计算总大小
        total_size = sum(os.path.getsize(file) for file in all_files)
        logging.info(f"总原始大小: {total_size:,} 字节 ({total_size / (1024*1024):.2f} MB)")
        
        # 创建临时tar文件
        temp_tar = tempfile.NamedTemporaryFile(delete=False)
        temp_tar.close()
        
        try:
            # 创建未压缩的tar文件
            logging.info(f"正在创建临时tar文件: {temp_tar.name}")
            
            with tarfile.open(temp_tar.name, "w") as tar:
                for i, file_path in enumerate(all_files, 1):
                    # 显示进度
                    if i % 100 == 0 or i == len(all_files):
                        progress = (i / len(all_files)) * 100
                        logging.info(f"添加文件: {i}/{len(all_files)} ({progress:.1f}%)")
                    
                    # 获取相对路径作为归档名
                    # 对于单个文件或目录，使用其基本名称
                    base_name = os.path.basename(file_path)
                    if len(source_paths) == 1 and os.path.isdir(source_paths[0]):
                        # 如果只有一个源目录，保留相对结构
                        base_name = os.path.relpath(file_path, os.path.dirname(source_paths[0]))
                    
                    try:
                        tar.add(file_path, arcname=base_name)
                    except Exception as e:
                        logging.error(f"添加文件 {file_path} 失败: {e}")
            
            # 使用LZMA压缩tar文件
            logging.info(f"正在使用LZMA压缩...")
            logging.info(f"压缩参数: 预设级别={preset}")
            if dict_size is not None:
                logging.info(f"字典大小={dict_size / (1024*1024):.1f} MB")
            
            start_time = datetime.now()
            
            # 创建压缩参数
            lzma_params = {"preset": preset}
            if filters:
                lzma_params["filters"] = filters
            
            # 压缩文件
            with open(temp_tar.name, "rb") as f_in:
                with lzma.open(output_path, "wb", **lzma_params) as f_out:
                    # 使用较大的块大小以提高效率
                    shutil.copyfileobj(f_in, f_out, 65536)
            
            compression_time = (datetime.now() - start_time).total_seconds()
            compressed_size = os.path.getsize(output_path)
            compression_ratio = (1 - compressed_size / total_size) * 100
            
            logging.info(f"压缩完成!")
            logging.info(f"归档文件: {output_path}")
            logging.info(f"压缩大小: {compressed_size:,} 字节 ({compressed_size / (1024*1024):.2f} MB)")
            logging.info(f"压缩率: {compression_ratio:.2f}%")
            logging.info(f"压缩速度: {total_size / (1024*1024 * compression_time):.2f} MB/s")
            
            return True
            
        except Exception as e:
            logging.error(f"创建归档失败: {e}")
            # 删除不完整的输出文件
            if os.path.exists(output_path):
                os.remove(output_path)
            return False
        finally:
            # 清理临时文件
            if os.path.exists(temp_tar.name):
                os.remove(temp_tar.name)
    
    # 命令行接口
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="高压缩率归档工具")
        parser.add_argument("source", nargs='+', help="源文件或目录路径")
        parser.add_argument("-o", "--output", required=True, help="输出归档文件路径")
        parser.add_argument("-p", "--preset", type=int, choices=range(0, 10), default=6,
                          help="LZMA预设级别 (0-9, 默认: 6)")
        parser.add_argument("-d", "--dict-size", type=str, help="字典大小 (例如: 4M, 16M)")
        parser.add_argument("--exclude", nargs='+', help="排除的文件模式列表")
        parser.add_argument("--dry-run", action="store_true", help="仅显示将要归档的文件")
        
        args = parser.parse_args()
        
        # 解析字典大小
        dict_size = None
        if args.dict_size:
            # 支持单位M, G
            import re
            match = re.match(r'(\d+)([MG]?)', args.dict_size.upper())
            if match:
                size = int(match.group(1))
                unit = match.group(2)
                if unit == 'M':
                    dict_size = size * 1024 * 1024
                elif unit == 'G':
                    dict_size = size * 1024 * 1024 * 1024
                else:
                    dict_size = size
            else:
                logging.error(f"无效的字典大小格式: {args.dict_size}")
                exit(1)
        
        create_high_compression_archive(
            source_paths=args.source,
            output_path=args.output,
            preset=args.preset,
            dict_size=dict_size,
            exclude_patterns=args.exclude,
            dry_run=args.dry_run
        )
    """)
    
    print("\n9.2 配置了内存管理的LZMA文件解压工具:")
    print("""
    import lzma
    import os
    import argparse
    import sys
    import threading
    import resource
    
    def set_memory_limit(max_bytes):
        """
        设置进程内存限制（仅在支持resource模块的系统上有效）
        """
        try:
            # 设置软限制和硬限制
            resource.setrlimit(resource.RLIMIT_AS, (max_bytes, max_bytes))
            return True
        except (ImportError, ValueError):
            # 在不支持的系统上忽略
            return False
    
    def decompress_with_memory_control(input_path, output_path, 
                                      chunk_size=16*1024, 
                                      max_memory_mb=512, 
                                      timeout_seconds=None):
        """
        使用内存控制解压LZMA/XZ文件
        
        参数:
        - input_path: 输入压缩文件路径
        - output_path: 输出文件路径
        - chunk_size: 读写块大小
        - max_memory_mb: 最大内存使用（MB）
        - timeout_seconds: 超时时间（秒），None表示不超时
        """
        # 设置内存限制
        memory_limit_set = False
        if sys.platform != 'win32':  # Windows不支持resource模块
            max_memory_bytes = max_memory_mb * 1024 * 1024
            memory_limit_set = set_memory_limit(max_memory_bytes)
            if memory_limit_set:
                print(f"已设置最大内存使用限制: {max_memory_mb} MB")
        
        # 解压函数
        def do_decompress():
            try:
                print(f"开始解压: {input_path}")
                print(f"输入文件大小: {os.path.getsize(input_path):,} 字节")
                
                with lzma.open(input_path, "rb") as f_in:
                    with open(output_path, "wb") as f_out:
                        while True:
                            chunk = f_in.read(chunk_size)
                            if not chunk:
                                break
                            f_out.write(chunk)
                
                print(f"解压完成: {output_path}")
                print(f"解压后文件大小: {os.path.getsize(output_path):,} 字节")
                return True
                
            except MemoryError:
                print("错误: 内存不足")
                if os.path.exists(output_path):
                    os.remove(output_path)
                return False
            except lzma.LZMAError as e:
                print(f"LZMA错误: {e}")
                if os.path.exists(output_path):
                    os.remove(output_path)
                return False
            except Exception as e:
                print(f"解压失败: {e}")
                if os.path.exists(output_path):
                    os.remove(output_path)
                return False
        
        # 如果设置了超时，使用线程执行
        if timeout_seconds:
            print(f"设置解压超时: {timeout_seconds} 秒")
            result = [False]  # 使用列表来在线程间共享结果
            
            def thread_func():
                result[0] = do_decompress()
            
            # 创建并启动线程
            thread = threading.Thread(target=thread_func)
            thread.daemon = True
            thread.start()
            
            # 等待线程完成或超时
            thread.join(timeout_seconds)
            
            # 如果线程仍在运行，说明超时
            if thread.is_alive():
                print(f"解压超时（超过{timeout_seconds}秒）")
                if os.path.exists(output_path):
                    os.remove(output_path)
                return False
            
            return result[0]
        else:
            # 没有超时限制，直接执行
            return do_decompress()
    
    # 命令行接口
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="带内存管理的LZMA解压工具")
        parser.add_argument("input", help="输入LZMA/XZ文件路径")
        parser.add_argument("-o", "--output", required=True, help="输出文件路径")
        parser.add_argument("-c", "--chunk", type=int, default=16, help="读写块大小 (KB, 默认: 16)")
        parser.add_argument("-m", "--max-memory", type=int, default=512, help="最大内存使用 (MB, 默认: 512)")
        parser.add_argument("-t", "--timeout", type=int, help="解压超时时间 (秒)")
        
        args = parser.parse_args()
        
        # 验证输入文件
        if not os.path.exists(args.input):
            print(f"错误: 输入文件不存在: {args.input}")
            sys.exit(1)
        
        # 验证输出目录
        output_dir = os.path.dirname(args.output)
        if output_dir and not os.path.exists(output_dir):
            print(f"错误: 输出目录不存在: {output_dir}")
            sys.exit(1)
        
        success = decompress_with_memory_control(
            input_path=args.input,
            output_path=args.output,
            chunk_size=args.chunk * 1024,  # 转换为字节
            max_memory_mb=args.max_memory,
            timeout_seconds=args.timeout
        )
        
        sys.exit(0 if success else 1)
    """)

# 10. lzma模块最佳实践总结
def best_practices_summary():
    """
    lzma模块最佳实践总结
    
    功能说明：总结lzma模块使用的最佳实践和注意事项。
    """
    print("\n=== 10. lzma模块最佳实践总结 ===")
    
    print("\n10.1 压缩算法选择指南:")
    print("   - 当需要最高压缩率时: 使用lzma/xz")
    print("   - 当速度优先时: 使用gzip")
    print("   - 当需要较好压缩率但又不过慢时: 使用bzip2")
    print("   - 对于非常重视存储效率的场景: lzma是最佳选择")
    print("   - 对于频繁访问的数据: 考虑使用gzip以获得更好的读取性能")
    
    print("\n10.2 性能优化最佳实践:")
    print("   - 平衡预设级别: 预设级别6通常是压缩率和速度的最佳平衡")
    print("   - 优化字典大小: 根据文件大小选择合适的字典大小")
    print("   - 使用分块处理: 避免一次性加载大型文件到内存")
    print("   - 多线程处理多个文件: 充分利用多核处理器")
    print("   - 监控内存使用: 特别是在处理大文件时")
    print("   - 仅在确实需要最高压缩率时使用级别9")
    
    print("\n10.3 安全使用指南:")
    print("   - 实现解压缩大小限制: 防止解压炸弹攻击")
    print("   - 设置合理的超时机制: 避免处理异常文件时无限等待")
    print("   - 实现内存限制: 防止资源耗尽")
    print("   - 验证输入文件: 确保文件格式正确")
    print("   - 对用户提供的文件采取额外的安全措施")
    print("   - 妥善处理所有可能的异常情况")
    
    print("\n10.4 代码编写技巧:")
    print("   - 始终使用上下文管理器(with语句)管理文件")
    print("   - 对大文件使用增量压缩和解压缩")
    print("   - 利用LZMA2格式(默认)而非LZMA1格式")
    print("   - 使用适当的校验和类型")
    print("   - 文本模式下指定正确的编码")
    print("   - 对于多文件操作，考虑与tarfile结合使用")
    
    print("\n10.5 常见问题及解决方案:")
    print("   - 内存不足错误: 减小字典大小，使用分块处理")
    print("   - 压缩速度太慢: 降低压缩级别，考虑使用gzip")
    print("   - 解压缩失败: 验证文件完整性，检查是否为正确的格式")
    print("   - Python解释器崩溃: 可能是内存溢出，限制字典大小和内存使用")
    print("   - 对于小文件效果不佳: 小文件的压缩头可能占用较大比例空间")

# 运行所有示例
def run_all_examples():
    print("====================================")
    print("Python lzma模块功能详解")
    print("====================================")
    
    # 1. 基本操作
    basic_lzma_operations()
    
    # 2. 压缩级别和参数控制
    compression_level_and_params_control()
    
    # 3. 内存中操作
    in_memory_operations()
    
    # 4. 增量操作
    incremental_operations()
    
    # 5. 流式处理
    streaming_large_data()
    
    # 6. 与tarfile结合使用
    combined_with_tarfile()
    
    # 7. 性能考量
    performance_considerations()
    
    # 8. 错误处理和安全性
    error_handling_and_security()
    
    # 9. 实际应用示例
    real_world_examples()
    
    # 10. 最佳实践总结
    best_practices_summary()
    
    print("\n====================================")
    print("lzma模块示例演示完成")
    print("====================================")

# 如果直接运行此文件，执行所有示例
if __name__ == "__main__":
    try:
        run_all_examples()
    except KeyboardInterrupt:
        print("\n操作被用户中断")
    except Exception as e:
        print(f"发生错误: {e}")

"""

总结
----

lzma模块是Python中处理LZMA/XZ压缩格式的强大工具，提供了极高的压缩率。本教程介绍了：

1. **基本操作**：创建、读取和写入LZMA/XZ文件
2. **参数控制**：压缩级别、字典大小等高级配置
3. **内存操作**：内存中直接压缩和解压缩数据
4. **增量处理**：支持流式数据处理
5. **大文件处理**：分块读写避免内存溢出
6. **与tarfile集成**：创建高效的tar.xz归档
7. **性能优化**：压缩速度与内存使用的平衡
8. **安全考量**：防止解压炸弹等安全问题
9. **实际应用**：高压缩率归档工具和安全解压工具

lzma模块特别适合需要极高压缩率的场景，如长期数据存储和备份。虽然压缩速度较慢，但提供了所有标准库中最高的压缩率，是空间敏感应用的理想选择。

使用lzma模块时，务必注意内存使用和处理时间，根据实际需求选择合适的压缩参数，在压缩率和性能之间找到最佳平衡点。

"""