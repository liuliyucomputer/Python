# Python bz2模块详解

```python
"""
bz2模块 - Python处理bzip2压缩文件的标准库

bz2模块提供了对bzip2压缩文件格式的支持，允许创建、读取、写入和追加bzip2压缩文件。
它实现了bzip2压缩算法，通常比gzip提供更好的压缩率，但压缩和解压缩速度稍慢。

bzip2算法特点：
- 使用Burrows-Wheeler变换和Huffman编码
- 比gzip通常提供更高的压缩率（约高10-20%）
- 压缩和解压缩速度较gzip慢
- 内存消耗较大

主要功能：
- 压缩单个文件为bzip2格式
- 解压缩bzip2文件
- 在读写过程中自动压缩/解压缩数据
- 支持压缩级别控制
- 支持文件对象接口
- 支持增量压缩和解压缩

适用场景：
- 需要高压缩率的文件存储
- 归档大型文件
- 数据备份
- 磁盘空间有限的环境
- 与tar结合使用创建tar.bz2归档
"""

import bz2
import os
import shutil
from datetime import datetime
import tempfile
import io
import threading

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
        f.write("这是一个用于测试bzip2压缩的示例文件。\n")
        f.write("bzip2模块可以提供比gzip更高的压缩率，特别适合包含重复模式的文本数据。\n")
        # 添加一些重复内容以提高压缩效果
        f.write("重复内容 " * 200)
        f.write("\n")
        # 添加一些数字和特殊字符
        for i in range(200):
            f.write(f"行号: {i:04d}, 随机数字: {i*123456789 % 10000}\n")
    
    # 创建二进制文件
    binary_file_path = os.path.join(temp_dir, "binary.dat")
    with open(binary_file_path, "wb") as f:
        # 写入一些二进制数据
        data = bytearray(20000)  # 20KB数据
        for i in range(20000):
            data[i] = i % 256
        f.write(data)
    
    return temp_dir, text_file_path, binary_file_path

# 清理示例文件
def cleanup_example_files(temp_dir):
    """清理示例文件"""
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        print(f"清理临时目录: {temp_dir}")

# 1. bz2文件的基本操作
def basic_bz2_operations():
    """
    bz2模块的基本操作
    
    功能说明：演示创建、读取和写入bzip2压缩文件的基本方法。
    """
    print("=== 1. bz2模块的基本操作 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, binary_file_path = prepare_example_files()
    
    try:
        # 1.1 创建bzip2压缩文件
        bz2_file_path = os.path.join(temp_dir, "example.txt.bz2")
        
        # 方法1: 使用bz2.open
        print("\n1.1.1 使用bz2.open创建压缩文件:")
        with open(text_file_path, "rb") as f_in:
            with bz2.open(bz2_file_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了压缩文件: {bz2_file_path}")
        print(f"原始文件大小: {os.path.getsize(text_file_path)} 字节")
        print(f"压缩文件大小: {os.path.getsize(bz2_file_path)} 字节")
        print(f"压缩率: {(1 - os.path.getsize(bz2_file_path) / os.path.getsize(text_file_path)) * 100:.2f}%")
        
        # 方法2: 使用BZ2File对象
        print("\n1.1.2 使用BZ2File对象创建压缩文件:")
        bz2_file_path2 = os.path.join(temp_dir, "example2.txt.bz2")
        
        with open(text_file_path, "rb") as f_in:
            with bz2.BZ2File(bz2_file_path2, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了压缩文件: {bz2_file_path2}")
        
        # 1.2 读取bzip2压缩文件
        print("\n1.2.1 读取压缩文件内容:")
        with bz2.open(bz2_file_path, "rb") as f:
            content = f.read().decode("utf-8")
            # 只显示前200个字符
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"文件内容预览: {preview}")
        
        # 1.3 写入文本到bzip2文件（直接写入，不经过中间文件）
        print("\n1.3.1 直接写入文本到压缩文件:")
        text_bz2_path = os.path.join(temp_dir, "direct_text.txt.bz2")
        
        with bz2.open(text_bz2_path, "wt", encoding="utf-8") as f:
            f.write("这是直接写入到bzip2文件的文本内容。\n")
            f.write("bz2模块支持文本模式，可以自动处理编码。\n")
        
        print(f"创建了直接写入的压缩文件: {text_bz2_path}")
        
        # 验证写入是否成功
        with bz2.open(text_bz2_path, "rt", encoding="utf-8") as f:
            content = f.read()
            print(f"读取的内容: {content}")
            
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 2. 压缩级别控制
def compression_level_control():
    """
    bz2压缩级别控制
    
    功能说明：演示如何控制bz2压缩级别，从1（最快）到9（最高压缩率）。
    bz2的压缩级别主要影响压缩率，压缩速度差异相对较小。
    """
    print("\n=== 2. 压缩级别控制 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, _ = prepare_example_files()
    
    try:
        # 测试不同压缩级别
        results = []
        
        print("测试不同压缩级别的效果:")
        print("级别 | 文件大小(字节) | 压缩率(%) | 耗时(秒)")
        print("-----|---------------|-----------|---------")
        
        for level in range(1, 10):
            bz2_file_path = os.path.join(temp_dir, f"example_level_{level}.txt.bz2")
            
            # 测量压缩时间
            start_time = datetime.now()
            
            with open(text_file_path, "rb") as f_in:
                with bz2.open(bz2_file_path, "wb", compresslevel=level) as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            duration = (datetime.now() - start_time).total_seconds()
            
            # 计算压缩结果
            original_size = os.path.getsize(text_file_path)
            compressed_size = os.path.getsize(bz2_file_path)
            compression_ratio = (1 - compressed_size / original_size) * 100
            
            results.append({
                "level": level,
                "size": compressed_size,
                "ratio": compression_ratio,
                "time": duration
            })
            
            print(f"{level:5d} | {compressed_size:13d} | {compression_ratio:9.2f} | {duration:8.4f}")
        
        # 分析结果
        print("\n压缩级别分析:")
        print(f"最小文件大小: 级别{min(results, key=lambda x: x['size'])['level']}, {min(results, key=lambda x: x['size'])['size']} 字节")
        print(f"最快压缩速度: 级别{min(results, key=lambda x: x['time'])['level']}, {min(results, key=lambda x: x['time'])['time']:.4f} 秒")
        
        # 找出最佳平衡（粗略计算）
        # 我们定义一个简单的评分：size * time
        best_balance = min(results, key=lambda x: x['size'] * x['time'])
        print(f"最佳平衡: 级别{best_balance['level']}, 大小{best_balance['size']}字节, 耗时{best_balance['time']:.4f}秒")
        
        # 推荐使用场景
        print("\nbzip2压缩级别特点:")
        print("- 级别1-3: 速度相对较快，压缩率适中，适合需要较快压缩速度的场景")
        print("- 级别4-6: 平衡模式，默认级别为9，通常可以考虑使用级别5-7作为平衡选择")
        print("- 级别7-9: 压缩率优先，特别是级别9提供最佳压缩率，但速度相对较慢")
        print("- bz2默认使用级别9，这与gzip默认使用级别6不同")
        print("- 注意：bz2各级别之间的速度差异通常小于gzip各级别之间的差异")
            
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 3. 内存中压缩和解压缩
def in_memory_operations():
    """
    内存中的bz2操作
    
    功能说明：演示如何在内存中对数据进行bz2压缩和解压缩，不涉及文件操作。
    这对于处理数据流或API交互特别有用。
    """
    print("\n=== 3. 内存中的bz2操作 ===")
    
    # 3.1 压缩内存中的数据
    print("\n3.1 压缩内存中的数据:")
    
    # 示例数据
    original_data = "这是一段需要在内存中压缩的数据。" * 200  # 复制多次以便观察压缩效果
    original_bytes = original_data.encode("utf-8")
    
    print(f"原始数据大小: {len(original_bytes)} 字节")
    
    # 使用bz2.compress直接压缩
    compressed_data = bz2.compress(original_bytes)
    print(f"压缩后数据大小: {len(compressed_data)} 字节")
    print(f"压缩率: {(1 - len(compressed_data) / len(original_bytes)) * 100:.2f}%")
    
    # 使用io.BytesIO在内存中压缩（更灵活的方式）
    compressed_buffer = io.BytesIO()
    
    with bz2.BZ2File(fileobj=compressed_buffer, mode="wb") as f:
        f.write(original_bytes)
    
    # 获取压缩后的数据
    compressed_data_alt = compressed_buffer.getvalue()
    print(f"使用BZ2File压缩后数据大小: {len(compressed_data_alt)} 字节")
    print(f"两种压缩方法结果比较: {'相同' if compressed_data == compressed_data_alt else '不同'}")
    
    # 3.2 解压缩内存中的数据
    print("\n3.2 解压缩内存中的数据:")
    
    # 使用bz2.decompress直接解压缩
    decompressed_data = bz2.decompress(compressed_data)
    print(f"解压缩后数据大小: {len(decompressed_data)} 字节")
    print(f"数据完整性验证: {'成功' if decompressed_data == original_bytes else '失败'}")
    
    # 使用io.BytesIO在内存中解压缩
    decompressed_buffer = io.BytesIO(compressed_data)
    
    with bz2.BZ2File(fileobj=decompressed_buffer, mode="rb") as f:
        decompressed_data_alt = f.read()
    
    print(f"使用BZ2File解压缩后数据大小: {len(decompressed_data_alt)} 字节")
    print(f"解压缩结果比较: {'相同' if decompressed_data == decompressed_data_alt else '不同'}")
    
    # 3.3 直接操作字符串（便捷函数）
    print("\n3.3 直接压缩和解压缩字符串:")
    
    # 创建便捷函数
    def compress_string(text, level=9):
        """压缩字符串并返回字节"""
        return bz2.compress(text.encode("utf-8"), compresslevel=level)
    
    def decompress_string(compressed_data):
        """解压缩字节数据为字符串"""
        return bz2.decompress(compressed_data).decode("utf-8")
    
    # 测试字符串压缩和解压缩
    test_string = "这是一个用于测试字符串压缩的示例。\n包含多行内容和不同类型的字符！"
    
    compressed_bytes = compress_string(test_string)
    decompressed_string = decompress_string(compressed_bytes)
    
    print(f"原始字符串长度: {len(test_string)} 字符")
    print(f"压缩后字节长度: {len(compressed_bytes)} 字节")
    print(f"解压缩后字符串长度: {len(decompressed_string)} 字符")
    print(f"字符串内容验证: {'成功' if decompressed_string == test_string else '失败'}")

# 4. 增量压缩和解压缩
def incremental_operations():
    """
    增量压缩和解压缩
    
    功能说明：演示如何使用bz2的增量压缩和解压缩功能，这对于处理流式数据或大型数据特别有用。
    """
    print("\n=== 4. 增量压缩和解压缩 ===")
    
    # 4.1 增量压缩
    print("\n4.1 增量压缩:")
    
    # 创建一个增量压缩对象
    compressor = bz2.BZ2Compressor()
    
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
    decompressor = bz2.BZ2Decompressor()
    
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
    
    # 4.3 增量压缩和解压缩的实际应用场景
    print("\n4.3 增量操作的应用场景:")
    print("1. 处理大型文件，避免一次性加载全部内容到内存")
    print("2. 网络流数据的实时压缩和解压缩")
    print("3. 处理数据生成器的输出")
    print("4. 分块处理日志文件")

# 5. 流式处理大型数据
def streaming_large_data():
    """
    流式处理大型数据
    
    功能说明：演示如何使用bz2模块处理大型数据，避免一次性加载全部数据到内存。
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
            f.write(f"这是大型文件的第{i:07d}行内容，包含一些可压缩的数据，bzip2对文本有很好的压缩效果。\n")
    
    try:
        # 5.1 分块压缩大型文件
        print("\n5.1 分块压缩大型文件:")
        
        bz2_large_path = os.path.join(temp_dir, "large_file.txt.bz2")
        chunk_size = 16384  # 16KB块
        
        print(f"开始压缩大型文件: {large_file_path}")
        print(f"原始文件大小: {os.path.getsize(large_file_path):,} 字节")
        
        start_time = datetime.now()
        
        with open(large_file_path, "rb") as f_in:
            with bz2.open(bz2_large_path, "wb") as f_out:
                while True:
                    chunk = f_in.read(chunk_size)
                    if not chunk:
                        break
                    f_out.write(chunk)
        
        compression_time = (datetime.now() - start_time).total_seconds()
        
        compressed_size = os.path.getsize(bz2_large_path)
        compression_ratio = (1 - compressed_size / os.path.getsize(large_file_path)) * 100
        
        print(f"压缩完成，耗时: {compression_time:.2f} 秒")
        print(f"压缩文件大小: {compressed_size:,} 字节")
        print(f"压缩率: {compression_ratio:.2f}%")
        print(f"压缩速度: {os.path.getsize(large_file_path) / (1024 * 1024 * compression_time):.2f} MB/s")
        
        # 5.2 分块解压缩大型文件
        print("\n5.2 分块解压缩大型文件:")
        
        decompressed_path = os.path.join(temp_dir, "decompressed_large.txt")
        
        print(f"开始解压缩: {bz2_large_path}")
        
        start_time = datetime.now()
        
        with bz2.open(bz2_large_path, "rb") as f_in:
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
        print("示例代码 - 使用生成器逐行读取bzip2压缩文件:")
        print("""
        def read_bz2_file_line_by_line(bz2_path):
            """使用生成器逐行读取bzip2压缩文件"""
            with bz2.open(bz2_path, "rt", encoding="utf-8") as f:
                for line in f:
                    yield line.rstrip('\n')
        
        # 使用示例
        # for i, line in enumerate(read_bz2_file_line_by_line(bz2_large_path), 1):
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
    
    功能说明：演示如何将bz2与tarfile模块结合使用，创建tar.bz2归档文件。
    这是处理多文件目录归档的常见方式。
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
        print("\n6.1 创建tar.bz2归档文件:")
        
        import tarfile
        
        tar_bz2_path = os.path.join(temp_dir, "archive.tar.bz2")
        
        print(f"创建归档文件: {tar_bz2_path}")
        print("包含的文件和目录:")
        
        # 列出将要归档的内容
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if file != os.path.basename(tar_bz2_path):  # 排除归档文件自身
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, temp_dir)
                    print(f"  {rel_path}")
        
        # 创建tar.bz2归档
        start_time = datetime.now()
        
        # 方法1: 使用tarfile.open并指定mode='w:bz2'
        with tarfile.open(tar_bz2_path, "w:bz2", compresslevel=9) as tar:
            # 添加根目录下的文件（除了归档文件本身）
            for item in os.listdir(temp_dir):
                item_path = os.path.join(temp_dir, item)
                if item_path != tar_bz2_path:  # 排除归档文件自身
                    arcname = os.path.basename(item_path)
                    tar.add(item_path, arcname=arcname)
        
        compression_time = (datetime.now() - start_time).total_seconds()
        
        print(f"归档完成，耗时: {compression_time:.2f} 秒")
        print(f"归档文件大小: {os.path.getsize(tar_bz2_path):,} 字节")
        
        # 6.2 读取tar.bz2归档文件内容
        print("\n6.2 读取tar.bz2归档文件内容:")
        
        with tarfile.open(tar_bz2_path, "r:bz2") as tar:
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
        
        # 6.3 解压tar.bz2归档文件
        print("\n6.3 解压tar.bz2归档文件:")
        
        extract_dir = os.path.join(temp_dir, "extracted")
        os.makedirs(extract_dir, exist_ok=True)
        
        print(f"解压到目录: {extract_dir}")
        
        start_time = datetime.now()
        
        with tarfile.open(tar_bz2_path, "r:bz2") as tar:
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
        
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 7. 性能考量与优化
def performance_considerations():
    """
    bz2模块的性能考量与优化
    
    功能说明：分析bz2模块的性能特点并提供优化建议。
    """
    print("\n=== 7. 性能考量与优化 ===")
    
    print("\n7.1 bz2与其他压缩算法比较:")
    print("  压缩算法比较概览:")
    print("  - gzip: 速度快，压缩率中等，内存消耗低")
    print("  - bz2: 速度中等，压缩率高，内存消耗较高")
    print("  - lzma/xz: 速度慢，压缩率最高，内存消耗高")
    
    print("\n7.2 bz2性能特点:")
    print("1. 压缩和解压缩速度")
    print("   - bz2的压缩速度比gzip慢约2-3倍")
    print("   - 解压缩速度比压缩速度快，但仍比gzip慢")
    print("   - 各级别之间的速度差异相对较小")
    
    print("\n2. 内存使用")
    print("   - bz2比gzip使用更多的内存")
    print("   - 压缩级别越高，内存消耗越大")
    print("   - 处理大文件时需要注意内存限制")
    
    print("\n3. 压缩率")
    print("   - bz2的压缩率通常比gzip高10-20%")
    print("   - 对文本数据的压缩效果特别好")
    print("   - 对已经压缩的数据（如图片、音频）压缩效果有限")
    
    print("\n7.3 性能优化建议:")
    print("1. 选择合适的压缩级别")
    print("   - 对于大多数场景，级别5-7是速度和压缩率的良好平衡")
    print("   - 不需要总是使用默认的级别9，除非压缩率是首要考虑因素")
    
    print("\n2. 分块处理")
    print("   - 使用增量压缩/解压缩或分块读取大文件")
    print("   - 避免一次性将整个大文件加载到内存")
    print("   - 使用生成器处理流式数据")
    
    print("\n3. 并行处理")
    print("   - 处理多个文件时，可以使用多线程或多进程")
    print("   - 注意I/O瓶颈和CPU核心数")
    
    print("\n4. 数据预处理")
    print("   - 移除冗余数据后再压缩")
    print("   - 对于已压缩格式的数据，考虑不解压直接存储")
    
    print("\n5. 缓冲区大小调整")
    print("   - 对于磁盘I/O密集型操作，较大的缓冲区可能会有所帮助")
    print("   - 对于网络操作，较小的缓冲区可能更合适")

# 8. 错误处理和安全性
def error_handling_and_security():
    """
    bz2模块的错误处理和安全性
    
    功能说明：演示如何正确处理bz2相关的错误以及安全使用bz2模块的建议。
    """
    print("\n=== 8. 错误处理和安全性 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, _ = prepare_example_files()
    
    try:
        # 创建一个正常的bzip2文件
        valid_bz2_path = os.path.join(temp_dir, "valid.txt.bz2")
        with bz2.open(valid_bz2_path, "wb") as f:
            f.write(b"这是一个有效的bzip2压缩文件的内容。")
        
        # 创建一个无效的bzip2文件（只是普通文本）
        invalid_bz2_path = os.path.join(temp_dir, "invalid.txt.bz2")
        with open(invalid_bz2_path, "wb") as f:
            f.write(b"这不是一个有效的bzip2文件。")
        
        print("\n8.1 错误处理示例:")
        print("处理无效的bzip2文件:")
        
        try:
            with bz2.open(invalid_bz2_path, "rb") as f:
                content = f.read()
                print("读取成功:", content)
        except bz2.BZ2Error as e:
            print(f"捕获到bz2错误: {e}")
        except Exception as e:
            print(f"捕获到其他错误: {e}")
        
        # 8.2 安全使用建议
        print("\n8.2 安全使用建议:")
        print("1. 输入验证")
        print("   - 始终验证输入文件的有效性")
        print("   - 对用户提供的文件格外小心")
        print("   - 使用try-except块捕获潜在的压缩/解压缩错误")
        
        print("\n2. 防止资源耗尽攻击")
        print("   - 限制最大解压缩大小，防止解压炸弹攻击")
        print("   - 监控解压缩过程中的内存使用")
        print("   - 实现超时机制")
        
        print("\n3. 解压炸弹防护示例:")
        print("""
        def safe_decompress(compressed_data, max_size=100*1024*1024):  # 100MB限制
            """安全解压缩数据，防止解压炸弹"""
            decompressor = bz2.BZ2Decompressor()
            result = bytearray()
            
            # 分块解压缩
            chunk_size = 8192
            for i in range(0, len(compressed_data), chunk_size):
                chunk = compressed_data[i:i+chunk_size]
                try:
                    decompressed_chunk = decompressor.decompress(chunk)
                except bz2.BZ2Error as e:
                    raise ValueError(f"无效的bzip2数据: {e}")
                
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
                raise ValueError("不完整的bzip2数据")
                
            return bytes(result)
        """)
        
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 9. 实际应用示例
def real_world_examples():
    """
    bz2模块的实际应用示例
    
    功能说明：提供bz2模块在实际项目中的应用示例代码。
    """
    print("\n=== 9. 实际应用示例 ===")
    
    print("\n9.1 大型日志文件归档器:")
    print("""
    import bz2
    import os
    import shutil
    import argparse
    import logging
    from datetime import datetime, timedelta
    import glob
    
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("log_archiver.log"),
            logging.StreamHandler()
        ]
    )
    
    def archive_old_logs(source_dir, target_dir=None, days_threshold=30, 
                       compress_level=7, delete_after_archive=False):
        """
        归档并压缩旧日志文件
        
        参数:
        - source_dir: 日志文件源目录
        - target_dir: 归档文件目标目录，默认与源目录相同
        - days_threshold: 归档多少天前的日志，默认30天
        - compress_level: bz2压缩级别，默认7
        - delete_after_archive: 归档后是否删除原始文件，默认False
        """
        if not os.path.exists(source_dir):
            logging.error(f"源目录不存在: {source_dir}")
            return False
        
        if target_dir is None:
            target_dir = source_dir
        
        if not os.path.exists(target_dir):
            try:
                os.makedirs(target_dir)
                logging.info(f"创建目标目录: {target_dir}")
            except Exception as e:
                logging.error(f"创建目标目录失败: {e}")
                return False
        
        # 计算截止日期
        cutoff_date = datetime.now() - timedelta(days=days_threshold)
        logging.info(f"将归档 {days_threshold} 天前（{cutoff_date.strftime('%Y-%m-%d')}之前）的日志文件")
        
        # 获取所有日志文件
        log_files = []
        for ext in ["*.log", "*.out", "*.txt"]:
            log_files.extend(glob.glob(os.path.join(source_dir, ext)))
        
        archived_count = 0
        failed_count = 0
        total_size = 0
        total_compressed_size = 0
        
        for log_file in log_files:
            try:
                # 获取文件修改时间
                file_mtime = datetime.fromtimestamp(os.path.getmtime(log_file))
                
                # 检查文件是否超过阈值
                if file_mtime < cutoff_date:
                    base_name = os.path.basename(log_file)
                    bz2_file = os.path.join(target_dir, f"{base_name}.bz2")
                    
                    # 检查目标文件是否已存在
                    if os.path.exists(bz2_file):
                        logging.warning(f"跳过，目标文件已存在: {bz2_file}")
                        continue
                    
                    logging.info(f"归档: {base_name} -> {os.path.basename(bz2_file)}")
                    
                    # 压缩文件
                    original_size = os.path.getsize(log_file)
                    start_time = datetime.now()
                    
                    with open(log_file, "rb") as f_in:
                        with bz2.open(bz2_file, "wb", compresslevel=compress_level) as f_out:
                            shutil.copyfileobj(f_in, f_out)
                    
                    duration = (datetime.now() - start_time).total_seconds()
                    compressed_size = os.path.getsize(bz2_file)
                    compression_ratio = (1 - compressed_size / original_size) * 100
                    
                    logging.info(
                        f"压缩完成: 原始大小={original_size:,} 字节, "
                        f"压缩大小={compressed_size:,} 字节, "
                        f"压缩率={compression_ratio:.2f}%, "
                        f"耗时={duration:.2f}秒"
                    )
                    
                    # 删除原始文件
                    if delete_after_archive:
                        os.remove(log_file)
                        logging.info(f"已删除原始文件: {base_name}")
                    
                    archived_count += 1
                    total_size += original_size
                    total_compressed_size += compressed_size
                    
            except Exception as e:
                logging.error(f"处理文件 {os.path.basename(log_file)} 失败: {e}")
                failed_count += 1
        
        # 生成汇总报告
        total_saved = total_size - total_compressed_size
        total_ratio = (1 - total_compressed_size / total_size) * 100 if total_size > 0 else 0
        
        logging.info("==== 归档汇总报告 ====")
        logging.info(f"成功归档: {archived_count} 个文件")
        logging.info(f"归档失败: {failed_count} 个文件")
        logging.info(f"总原始大小: {total_size:,} 字节 ({total_size / (1024*1024):.2f} MB)")
        logging.info(f"总压缩大小: {total_compressed_size:,} 字节 ({total_compressed_size / (1024*1024):.2f} MB)")
        logging.info(f"总共节省: {total_saved:,} 字节 ({total_saved / (1024*1024):.2f} MB)")
        logging.info(f"平均压缩率: {total_ratio:.2f}%")
        
        return archived_count > 0
    
    # 命令行接口
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="日志文件归档和压缩工具")
        parser.add_argument("source", help="日志文件源目录")
        parser.add_argument("-t", "--target", help="归档文件目标目录")
        parser.add_argument("-d", "--days", type=int, default=30, help="归档多少天前的日志")
        parser.add_argument("-l", "--level", type=int, choices=range(1, 10), default=7,
                          help="bzip2压缩级别 (1-9, 默认: 7)")
        parser.add_argument("--delete", action="store_true", help="归档后删除原始文件")
        
        args = parser.parse_args()
        
        archive_old_logs(
            source_dir=args.source,
            target_dir=args.target,
            days_threshold=args.days,
            compress_level=args.level,
            delete_after_archive=args.delete
        )
    """)
    
    print("\n9.2 大规模数据集压缩工具:")
    print("""
    import bz2
    import os
    import argparse
    import sys
    import threading
    import queue
    from datetime import datetime
    import tempfile
    
    def compress_file(file_path, output_path, compress_level=9, chunk_size=16*1024):
        """
        压缩单个文件，显示进度
        """
        try:
            file_size = os.path.getsize(file_path)
            processed = 0
            
            print(f"开始压缩: {os.path.basename(file_path)}")
            print(f"文件大小: {file_size:,} 字节")
            
            with open(file_path, "rb") as f_in:
                with bz2.open(output_path, "wb", compresslevel=compress_level) as f_out:
                    while True:
                        chunk = f_in.read(chunk_size)
                        if not chunk:
                            break
                        
                        f_out.write(chunk)
                        processed += len(chunk)
                        
                        # 更新进度
                        progress = min(100, (processed / file_size) * 100)
                        bar_length = 30
                        filled_length = int(bar_length * processed / file_size)
                        bar = '=' * filled_length + '-' * (bar_length - filled_length)
                        
                        sys.stdout.write(f"[{bar}] {progress:.1f}% ({processed:,}/{file_size:,} 字节)\r")
                        sys.stdout.flush()
            
            sys.stdout.write("\n")
            
            compressed_size = os.path.getsize(output_path)
            compression_ratio = (1 - compressed_size / file_size) * 100
            
            print(f"压缩完成!")
            print(f"压缩文件: {os.path.basename(output_path)}")
            print(f"压缩大小: {compressed_size:,} 字节 ({compressed_size / (1024*1024):.2f} MB)")
            print(f"压缩率: {compression_ratio:.2f}%")
            
            return compressed_size
            
        except Exception as e:
            print(f"压缩失败: {e}")
            # 清理不完整的文件
            if os.path.exists(output_path):
                os.remove(output_path)
            raise
    
    def worker(q, results, compress_level, chunk_size):
        """
        工作线程函数，处理队列中的文件压缩任务
        """
        while True:
            item = q.get()
            if item is None:  # 结束信号
                break
                
            file_path, output_path = item
            try:
                compressed_size = compress_file(file_path, output_path, compress_level, chunk_size)
                results.append((file_path, output_path, compressed_size))
            except Exception as e:
                print(f"处理文件 {file_path} 失败: {e}")
            finally:
                q.task_done()
    
    def batch_compress(file_patterns, output_dir, compress_level=9, chunk_size=16*1024, num_threads=4):
        """
        批量压缩文件，支持多线程
        
        参数:
        - file_patterns: 文件匹配模式列表
        - output_dir: 输出目录
        - compress_level: 压缩级别
        - chunk_size: 读写块大小
        - num_threads: 线程数
        """
        import glob
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # 收集所有匹配的文件
        files_to_compress = []
        for pattern in file_patterns:
            files_to_compress.extend(glob.glob(pattern))
        
        # 过滤掉目录
        files_to_compress = [f for f in files_to_compress if os.path.isfile(f)]
        
        if not files_to_compress:
            print("没有找到匹配的文件")
            return
        
        print(f"找到 {len(files_to_compress)} 个文件待压缩")
        
        # 创建任务队列
        task_queue = queue.Queue()
        results = []
        
        # 填充任务队列
        for file_path in files_to_compress:
            base_name = os.path.basename(file_path)
            output_path = os.path.join(output_dir, f"{base_name}.bz2")
            task_queue.put((file_path, output_path))
        
        # 创建工作线程
        threads = []
        for _ in range(num_threads):
            t = threading.Thread(target=worker, args=(task_queue, results, compress_level, chunk_size))
            t.start()
            threads.append(t)
        
        # 等待所有任务完成
        task_queue.join()
        
        # 发送结束信号
        for _ in range(num_threads):
            task_queue.put(None)
        
        # 等待所有线程结束
        for t in threads:
            t.join()
        
        # 计算汇总信息
        total_original_size = sum(os.path.getsize(f) for f, _, _ in results)
        total_compressed_size = sum(cs for _, _, cs in results)
        total_saved = total_original_size - total_compressed_size
        compression_ratio = (1 - total_compressed_size / total_original_size) * 100 if total_original_size > 0 else 0
        
        print("\n==== 压缩汇总 ====")
        print(f"成功压缩: {len(results)} 个文件")
        print(f"总原始大小: {total_original_size:,} 字节 ({total_original_size / (1024*1024*1024):.2f} GB)")
        print(f"总压缩大小: {total_compressed_size:,} 字节 ({total_compressed_size / (1024*1024*1024):.2f} GB)")
        print(f"总共节省: {total_saved:,} 字节 ({total_saved / (1024*1024*1024):.2f} GB)")
        print(f"平均压缩率: {compression_ratio:.2f}%")
    
    # 命令行接口
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="批量文件压缩工具")
        parser.add_argument("patterns", nargs='+', help="文件匹配模式，如 '*.txt' 'data/*.csv'")
        parser.add_argument("-o", "--output", required=True, help="输出目录")
        parser.add_argument("-l", "--level", type=int, choices=range(1, 10), default=9, 
                          help="bzip2压缩级别 (1-9, 默认: 9)")
        parser.add_argument("-c", "--chunk", type=int, default=16, help="读写块大小 (KB, 默认: 16)")
        parser.add_argument("-t", "--threads", type=int, default=4, help="线程数 (默认: 4)")
        
        args = parser.parse_args()
        
        batch_compress(
            file_patterns=args.patterns,
            output_dir=args.output,
            compress_level=args.level,
            chunk_size=args.chunk * 1024,  # 转换为字节
            num_threads=args.threads
        )
    """)

# 10. bz2模块最佳实践总结
def best_practices_summary():
    """
    bz2模块最佳实践总结
    
    功能说明：总结bz2模块使用的最佳实践和注意事项。
    """
    print("\n=== 10. bz2模块最佳实践总结 ===")
    
    print("\n10.1 选择合适的压缩算法:")
    print("   - 当速度优先时: 使用gzip")
    print("   - 当压缩率优先时: 使用bz2或lzma")
    print("   - 当内存使用受限且速度重要时: 使用gzip")
    print("   - 对于大型文本数据归档: 使用bz2")
    print("   - 对于多文件目录: 与tarfile结合使用")
    
    print("\n10.2 性能优化建议:")
    print("   - 选择合适的压缩级别: 5-7通常是速度和压缩率的良好平衡")
    print("   - 分块处理大文件: 避免内存问题")
    print("   - 使用增量压缩/解压缩: 适合流式数据处理")
    print("   - 并行处理多个文件: 利用多核处理器")
    print("   - 避免对已压缩数据重复压缩")
    
    print("\n10.3 安全使用指南:")
    print("   - 验证输入文件的有效性")
    print("   - 限制最大解压缩大小")
    print("   - 实现超时机制")
    print("   - 妥善处理异常")
    print("   - 对用户提供的压缩文件格外小心")
    
    print("\n10.4 代码使用技巧:")
    print("   - 始终使用上下文管理器(with语句)管理文件")
    print("   - 文本模式下指定正确的编码")
    print("   - 使用增量压缩和解压缩处理流式数据")
    print("   - 使用生成器处理大型文件的读取")
    print("   - 结合其他模块(tarfile, os, shutil)使用")
    
    print("\n10.5 常见问题及解决方案:")
    print("   - 内存错误: 使用分块处理，减小块大小")
    print("   - 压缩速度慢: 降低压缩级别，考虑使用多线程")
    print("   - 解压失败: 验证输入文件的有效性，添加错误处理")
    print("   - 文件损坏: 在处理重要数据时实现校验机制")
    print("   - 不完整的压缩文件: 实现断点续传或完整性检查")

# 运行所有示例
def run_all_examples():
    print("====================================")
    print("Python bz2模块功能详解")
    print("====================================")
    
    # 1. 基本操作
    basic_bz2_operations()
    
    # 2. 压缩级别控制
    compression_level_control()
    
    # 3. 内存中操作
    in_memory_operations()
    
    # 4. 增量操作
    incremental_operations()
    
    # 5. 流式处理
    streaming_large_data()
    
    # 6. 与tarfile结合
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
    print("bz2模块功能演示完成")
    print("====================================")

# 运行示例
if __name__ == "__main__":
    run_all_examples()
```

## bz2模块总结

bz2模块是Python处理bzip2压缩文件的标准库，提供了创建、读取、写入bzip2压缩文件的完整功能。通过本模块的学习，我们了解到：

1. **基本操作**：使用`bz2.open`和`BZ2File`对象创建、读取和写入bzip2压缩文件
2. **压缩级别**：从1到9的压缩级别控制，默认使用级别9
3. **内存操作**：使用`bz2.compress`和`bz2.decompress`在内存中直接处理数据
4. **增量处理**：使用`BZ2Compressor`和`BZ2Decompressor`进行流式数据处理
5. **与tarfile结合**：创建和处理tar.bz2归档文件

在使用bz2模块时，需要注意以下几点：

1. **性能平衡**：bz2提供了较高的压缩率，但速度相对较慢，内存消耗较大
2. **适用场景**：最适合需要高压缩率、磁盘空间有限的场景，如数据归档和长期存储
3. **安全性**：处理未知来源的压缩文件时要注意安全风险，实现解压大小限制和错误处理
4. **多文件处理**：bz2只能压缩单个文件，处理多个文件需要与tarfile等模块结合使用

bz2模块是数据压缩和归档的重要工具，尤其适合对压缩率要求较高的场景。它的高级功能如增量压缩和解压缩，使其能够灵活处理各种规模的数据，从内存中的小型数据到大型文件和数据流。在实际应用中，需要根据具体需求在压缩率、速度和内存使用之间做出合理选择。