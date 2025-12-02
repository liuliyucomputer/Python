# Python gzip模块详解

```python
"""
gzip模块 - Python处理gzip压缩文件的标准库

gzip模块提供了对gzip文件格式的支持，允许创建、读取、写入和追加gzip压缩文件。
它实现了GNU压缩工具的功能，使用DEFLATE压缩算法。

主要功能：
- 压缩单个文件为gzip格式
- 解压缩gzip文件
- 在读写过程中自动压缩/解压缩数据
- 支持压缩级别控制
- 支持文件对象接口

适用场景：
- 单个大文件的压缩和解压缩
- 数据流的在线压缩和解压缩
- 日志文件压缩存储
- HTTP传输中的内容压缩
- 与其他归档格式（如tar）结合使用
"""

import gzip
import os
import shutil
from datetime import datetime
import tempfile
import io

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
        f.write("这是一个用于测试gzip压缩的示例文件。\n")
        f.write("gzip模块可以有效地压缩文本内容，尤其是包含重复模式的数据。\n")
        # 添加一些重复内容以提高压缩效果
        f.write("重复内容 " * 100)
        f.write("\n")
        # 添加一些数字和特殊字符
        for i in range(100):
            f.write(f"行号: {i:03d}, 随机数字: {i*12345 % 1000}\n")
    
    # 创建二进制文件
    binary_file_path = os.path.join(temp_dir, "binary.dat")
    with open(binary_file_path, "wb") as f:
        # 写入一些二进制数据
        data = bytearray(10000)  # 10KB数据
        for i in range(10000):
            data[i] = i % 256
        f.write(data)
    
    return temp_dir, text_file_path, binary_file_path

# 清理示例文件
def cleanup_example_files(temp_dir):
    """清理示例文件"""
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        print(f"清理临时目录: {temp_dir}")

# 1. gzip文件的基本操作
def basic_gzip_operations():
    """
    gzip模块的基本操作
    
    功能说明：演示创建、读取和写入gzip压缩文件的基本方法。
    """
    print("=== 1. gzip模块的基本操作 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, binary_file_path = prepare_example_files()
    
    try:
        # 1.1 创建gzip压缩文件
        gzip_file_path = os.path.join(temp_dir, "example.txt.gz")
        
        # 方法1: 使用gzip.open
        print("\n1.1.1 使用gzip.open创建压缩文件:")
        with open(text_file_path, "rb") as f_in:
            with gzip.open(gzip_file_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了压缩文件: {gzip_file_path}")
        print(f"原始文件大小: {os.path.getsize(text_file_path)} 字节")
        print(f"压缩文件大小: {os.path.getsize(gzip_file_path)} 字节")
        print(f"压缩率: {(1 - os.path.getsize(gzip_file_path) / os.path.getsize(text_file_path)) * 100:.2f}%")
        
        # 方法2: 使用GzipFile对象
        print("\n1.1.2 使用GzipFile对象创建压缩文件:")
        gzip_file_path2 = os.path.join(temp_dir, "example2.txt.gz")
        
        with open(text_file_path, "rb") as f_in:
            with gzip.GzipFile(gzip_file_path2, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了压缩文件: {gzip_file_path2}")
        
        # 1.2 读取gzip压缩文件
        print("\n1.2.1 读取压缩文件内容:")
        with gzip.open(gzip_file_path, "rb") as f:
            content = f.read().decode("utf-8")
            # 只显示前200个字符
            preview = content[:200] + "..." if len(content) > 200 else content
            print(f"文件内容预览: {preview}")
        
        # 1.3 写入文本到gzip文件（直接写入，不经过中间文件）
        print("\n1.3.1 直接写入文本到压缩文件:")
        text_gzip_path = os.path.join(temp_dir, "direct_text.txt.gz")
        
        with gzip.open(text_gzip_path, "wt", encoding="utf-8") as f:
            f.write("这是直接写入到gzip文件的文本内容。\n")
            f.write("gzip模块支持文本模式，可以自动处理编码。\n")
        
        print(f"创建了直接写入的压缩文件: {text_gzip_path}")
        
        # 验证写入是否成功
        with gzip.open(text_gzip_path, "rt", encoding="utf-8") as f:
            content = f.read()
            print(f"读取的内容: {content}")
            
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 2. 压缩级别控制
def compression_level_control():
    """
    gzip压缩级别控制
    
    功能说明：演示如何控制gzip压缩级别，从0（无压缩）到9（最高压缩）。
    压缩级别影响压缩率和压缩速度的平衡。
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
        
        for level in range(0, 10):
            gzip_file_path = os.path.join(temp_dir, f"example_level_{level}.txt.gz")
            
            # 测量压缩时间
            start_time = datetime.now()
            
            with open(text_file_path, "rb") as f_in:
                with gzip.open(gzip_file_path, "wb", compresslevel=level) as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            duration = (datetime.now() - start_time).total_seconds()
            
            # 计算压缩结果
            original_size = os.path.getsize(text_file_path)
            compressed_size = os.path.getsize(gzip_file_path)
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
        print("\n推荐使用场景:")
        print("- 级别0: 仅用于测试或需要最快速度的场景，无实际压缩")
        print("- 级别1-3: 网络传输、实时应用，优先考虑速度")
        print("- 级别4-6: 一般用途，平衡压缩率和速度")
        print("- 级别7-9: 存储归档，优先考虑压缩率")
        print("- 级别6: Python gzip模块的默认值，适合大多数场景")
            
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 3. 内存中压缩和解压缩
def in_memory_operations():
    """
    内存中的gzip操作
    
    功能说明：演示如何在内存中对数据进行gzip压缩和解压缩，不涉及文件操作。
    这对于处理数据流或API交互特别有用。
    """
    print("\n=== 3. 内存中的gzip操作 ===")
    
    # 3.1 压缩内存中的数据
    print("\n3.1 压缩内存中的数据:")
    
    # 示例数据
    original_data = "这是一段需要在内存中压缩的数据。" * 100  # 复制多次以便观察压缩效果
    original_bytes = original_data.encode("utf-8")
    
    print(f"原始数据大小: {len(original_bytes)} 字节")
    
    # 使用io.BytesIO在内存中压缩
    compressed_buffer = io.BytesIO()
    
    with gzip.GzipFile(fileobj=compressed_buffer, mode="wb") as f:
        f.write(original_bytes)
    
    # 获取压缩后的数据
    compressed_data = compressed_buffer.getvalue()
    print(f"压缩后数据大小: {len(compressed_data)} 字节")
    print(f"压缩率: {(1 - len(compressed_data) / len(original_bytes)) * 100:.2f}%")
    
    # 3.2 解压缩内存中的数据
    print("\n3.2 解压缩内存中的数据:")
    
    # 使用io.BytesIO在内存中解压缩
    decompressed_buffer = io.BytesIO(compressed_data)
    
    with gzip.GzipFile(fileobj=decompressed_buffer, mode="rb") as f:
        decompressed_data = f.read()
    
    print(f"解压缩后数据大小: {len(decompressed_data)} 字节")
    print(f"数据完整性验证: {'成功' if decompressed_data == original_bytes else '失败'}")
    
    # 3.3 在内存中直接操作字符串
    print("\n3.3 直接压缩和解压缩字符串:")
    
    # 创建一个函数用于压缩字符串
    def compress_string(text, level=6):
        """压缩字符串并返回字节"""
        buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode="wb", compresslevel=level) as f:
            f.write(text.encode("utf-8"))
        return buffer.getvalue()
    
    # 创建一个函数用于解压缩字节到字符串
    def decompress_string(compressed_data):
        """解压缩字节数据为字符串"""
        buffer = io.BytesIO(compressed_data)
        with gzip.GzipFile(fileobj=buffer, mode="rb") as f:
            return f.read().decode("utf-8")
    
    # 测试字符串压缩和解压缩
    test_string = "这是一个用于测试字符串压缩的示例。\n包含多行内容和不同类型的字符！"
    
    compressed_bytes = compress_string(test_string)
    decompressed_string = decompress_string(compressed_bytes)
    
    print(f"原始字符串长度: {len(test_string)} 字符")
    print(f"压缩后字节长度: {len(compressed_bytes)} 字节")
    print(f"解压缩后字符串长度: {len(decompressed_string)} 字符")
    print(f"字符串内容验证: {'成功' if decompressed_string == test_string else '失败'}")

# 4. 高级gzip功能
def advanced_gzip_features():
    """
    gzip模块的高级功能
    
    功能说明：演示gzip模块的一些高级功能，如自定义mtime、添加注释、读取gzip头信息等。
    """
    print("\n=== 4. gzip模块的高级功能 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, _ = prepare_example_files()
    
    try:
        # 4.1 自定义mtime（修改时间）
        print("\n4.1 自定义文件修改时间(mtime):")
        
        # 获取当前时间戳
        current_time = datetime.now().timestamp()
        # 创建一个过去的时间戳（例如10天前）
        past_time = current_time - (10 * 24 * 60 * 60)
        
        # 使用自定义mtime创建压缩文件
        custom_mtime_path = os.path.join(temp_dir, "custom_mtime.txt.gz")
        
        with open(text_file_path, "rb") as f_in:
            with gzip.GzipFile(custom_mtime_path, "wb", mtime=past_time) as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了自定义mtime的压缩文件: {custom_mtime_path}")
        
        # 4.2 添加注释到gzip文件
        print("\n4.2 添加注释到gzip文件:")
        
        comment_path = os.path.join(temp_dir, "with_comment.txt.gz")
        
        # 注意：Python的gzip模块不直接支持向gzip文件添加注释
        # 这里我们通过直接操作GzipFile对象的方法来实现
        with open(text_file_path, "rb") as f_in:
            with gzip.open(comment_path, "wb") as f_out:
                # 这里无法直接设置注释，因为Python的gzip模块不支持
                # 但我们可以记录我们想要添加的注释内容
                intended_comment = "这是一个测试注释，Python gzip模块不直接支持写入注释"
                shutil.copyfileobj(f_in, f_out)
        
        print(f"创建了注释记录的压缩文件: {comment_path}")
        print(f"(注意：Python的gzip模块不支持直接写入gzip注释)")
        print(f"想要添加的注释: {intended_comment}")
        
        # 4.3 读取gzip文件头信息
        print("\n4.3 读取gzip文件头信息:")
        
        gzip_path = os.path.join(temp_dir, "example.txt.gz")
        
        # 创建一个普通的gzip文件用于读取头信息
        with open(text_file_path, "rb") as f_in:
            with gzip.open(gzip_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        
        # 读取gzip头信息
        with gzip.open(gzip_path, "rb") as f:
            # 获取gzip文件的一些属性
            print(f"压缩方法: {f.method}")  # 通常为8，表示DEFLATE
            print(f"标志: {f.flag}")  # 标志位
            print(f"修改时间(mtime): {datetime.fromtimestamp(f.mtime)}")  # 修改时间
            print(f"操作系统: {f.os}")  # 操作系统标识
            print(f"压缩级别: {f.compresslevel if hasattr(f, 'compresslevel') else '未知'}")  # 压缩级别
        
        # 4.4 追加模式操作
        print("\n4.4 追加模式操作:")
        
        # 注意：gzip格式不支持真正的追加操作，每次写入都会创建新的压缩流
        # 但我们可以模拟追加操作：解压现有内容，添加新内容，然后重新压缩
        
        # 创建初始压缩文件
        append_path = os.path.join(temp_dir, "append_test.txt.gz")
        
        with gzip.open(append_path, "wt", encoding="utf-8") as f:
            f.write("这是初始内容\n")
        
        print(f"创建了初始压缩文件: {append_path}")
        
        # 模拟追加操作
        # 1. 读取现有内容
        existing_content = ""
        with gzip.open(append_path, "rt", encoding="utf-8") as f:
            existing_content = f.read()
        
        # 2. 添加新内容
        new_content = existing_content + "这是追加的内容\n"
        
        # 3. 重新压缩
        with gzip.open(append_path, "wt", encoding="utf-8") as f:
            f.write(new_content)
        
        print("模拟了追加操作（通过解压-修改-重新压缩）")
        
        # 验证结果
        with gzip.open(append_path, "rt", encoding="utf-8") as f:
            final_content = f.read()
            print(f"最终文件内容: {final_content}")
            
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 5. 流式处理大型数据
def streaming_large_data():
    """
    流式处理大型数据
    
    功能说明：演示如何使用gzip模块处理大型数据，避免一次性加载全部数据到内存。
    这对于处理大型文件特别重要。
    """
    print("\n=== 5. 流式处理大型数据 ===")
    
    # 准备示例文件
    temp_dir, text_file_path, binary_file_path = prepare_example_files()
    
    # 创建一个更大的文件用于测试
    large_file_path = os.path.join(temp_dir, "large_file.txt")
    with open(large_file_path, "w", encoding="utf-8") as f:
        # 写入大约10MB的数据
        for i in range(100000):
            f.write(f"这是大型文件的第{i:06d}行内容，包含一些可压缩的数据。\n")
    
    try:
        # 5.1 分块压缩大型文件
        print("\n5.1 分块压缩大型文件:")
        
        gzip_large_path = os.path.join(temp_dir, "large_file.txt.gz")
        chunk_size = 8192  # 8KB块
        
        print(f"开始压缩大型文件: {large_file_path}")
        print(f"原始文件大小: {os.path.getsize(large_file_path):,} 字节")
        
        start_time = datetime.now()
        
        with open(large_file_path, "rb") as f_in:
            with gzip.open(gzip_large_path, "wb") as f_out:
                while True:
                    chunk = f_in.read(chunk_size)
                    if not chunk:
                        break
                    f_out.write(chunk)
        
        compression_time = (datetime.now() - start_time).total_seconds()
        
        compressed_size = os.path.getsize(gzip_large_path)
        compression_ratio = (1 - compressed_size / os.path.getsize(large_file_path)) * 100
        
        print(f"压缩完成，耗时: {compression_time:.2f} 秒")
        print(f"压缩文件大小: {compressed_size:,} 字节")
        print(f"压缩率: {compression_ratio:.2f}%")
        print(f"压缩速度: {os.path.getsize(large_file_path) / (1024 * 1024 * compression_time):.2f} MB/s")
        
        # 5.2 分块解压缩大型文件
        print("\n5.2 分块解压缩大型文件:")
        
        decompressed_path = os.path.join(temp_dir, "decompressed_large.txt")
        
        print(f"开始解压缩: {gzip_large_path}")
        
        start_time = datetime.now()
        
        with gzip.open(gzip_large_path, "rb") as f_in:
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
        
        # 5.3 流式处理与生成器结合
        print("\n5.3 流式处理与生成器结合:")
        print("示例代码 - 使用生成器逐行处理压缩文件:")
        print("""
        def read_gzip_file_line_by_line(gzip_path):
            """使用生成器逐行读取gzip压缩文件"""
            with gzip.open(gzip_path, "rt", encoding="utf-8") as f:
                for line in f:
                    yield line.rstrip('\n')
        
        # 使用示例
        for i, line in enumerate(read_gzip_file_line_by_line(gzip_large_path), 1):
            if i <= 5:  # 只打印前5行
                print(f"第{i}行: {line}")
            elif i == 6:
                print("... 省略中间内容 ...")
            elif i > 99995:
                print(f"第{i}行: {line}")
        """)
        
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 6. gzip模块在HTTP通信中的应用
def http_gzip_examples():
    """
    gzip模块在HTTP通信中的应用
    
    功能说明：演示gzip模块如何用于HTTP通信中的内容压缩和解压缩。
    这在Web开发和API交互中非常常见。
    """
    print("\n=== 6. gzip模块在HTTP通信中的应用 ===")
    
    print("\n6.1 HTTP响应内容的压缩:")
    print("""
    # 服务器端示例 - 使用gzip压缩HTTP响应
    import http.server
    import socketserver
    import gzip
    import io
    
    class GzipHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            # 标准响应处理
            super().do_GET()
            
            # 检查客户端是否支持gzip
            accept_encoding = self.headers.get('Accept-Encoding', '')
            if 'gzip' in accept_encoding and self.path.endswith('.txt'):
                # 获取原始响应内容
                response_content = self.wfile.getvalue()  # 假设已保存响应内容
                
                # 压缩内容
                compressed_buffer = io.BytesIO()
                with gzip.GzipFile(fileobj=compressed_buffer, mode="wb") as f:
                    f.write(response_content)
                compressed_content = compressed_buffer.getvalue()
                
                # 修改响应头
                self.send_response(200)
                self.send_header('Content-Encoding', 'gzip')
                self.send_header('Content-Length', len(compressed_content))
                self.end_headers()
                
                # 发送压缩后的内容
                self.wfile.write(compressed_content)
    """)
    
    print("\n6.2 客户端处理gzip压缩的响应:")
    print("""
    # 客户端示例 - 处理gzip压缩的HTTP响应
    import urllib.request
    import gzip
    import io
    
    def fetch_url_with_gzip_support(url):
        """获取URL内容，自动处理gzip压缩"""
        # 创建请求并添加Accept-Encoding头
        req = urllib.request.Request(url)
        req.add_header('Accept-Encoding', 'gzip, deflate')
        
        with urllib.request.urlopen(req) as response:
            # 检查内容是否被压缩
            content_encoding = response.getheader('Content-Encoding')
            
            if content_encoding == 'gzip':
                # 使用gzip解压缩
                buffer = io.BytesIO(response.read())
                with gzip.GzipFile(fileobj=buffer, mode="rb") as f:
                    content = f.read()
            else:
                # 直接读取内容
                content = response.read()
        
        return content
    
    # 使用示例
    # content = fetch_url_with_gzip_support('https://example.com/large-text-file.txt')
    # print(f"获取内容大小: {len(content)} 字节")
    """)
    
    print("\n6.3 使用requests库处理gzip（更简单的方式）:")
    print("""
    # 注意：实际使用前需要安装requests库: pip install requests
    import requests
    
    # requests库会自动处理gzip压缩的响应
    response = requests.get('https://example.com', headers={'Accept-Encoding': 'gzip, deflate'})
    
    # response.content 已经是解压缩后的内容
    print(f"响应状态码: {response.status_code}")
    print(f"是否使用gzip: {'gzip' in response.headers.get('Content-Encoding', '')}")
    print(f"内容长度: {len(response.content)} 字节")
    """)

# 7. 最佳实践和性能优化
def gzip_best_practices():
    """
    gzip模块的最佳实践和性能优化
    
    功能说明：提供gzip模块使用的最佳实践建议和性能优化技巧。
    """
    print("\n=== 7. gzip模块的最佳实践和性能优化 ===")
    
    print("\n7.1 性能优化建议:")
    print("1. 选择合适的压缩级别:")
    print("   - 级别0: 无压缩，最快但不节省空间，适合已经压缩的数据（如图片、视频）")
    print("   - 级别1-3: 速度优先，适合实时应用和网络传输")
    print("   - 级别4-6: 平衡模式，适合大多数一般用途")
    print("   - 级别7-9: 压缩率优先，适合存储和归档")
    
    print("\n2. 分块处理大型文件:")
    print("   - 避免一次性将整个文件加载到内存")
    print("   - 使用块读取（如8KB或16KB）进行压缩和解压缩")
    print("   - 使用生成器逐行处理文本文件")
    
    print("\n3. 选择合适的缓冲区大小:")
    print("   - 默认缓冲区大小通常为8KB")
    print("   - 对于SSD存储，可以考虑更大的缓冲区（如64KB或128KB）")
    print("   - 对于网络传输，可以使用较小的缓冲区以减少延迟")
    
    print("\n4. 多线程处理多个文件:")
    print("   - 使用concurrent.futures或threading模块并行处理多个文件")
    print("   - 注意避免I/O瓶颈")
    
    print("\n5. 避免过度压缩:")
    print("   - 某些数据（如JPEG、MP3、视频）已经过压缩")
    print("   - 对已压缩数据应用gzip可能会增加文件大小")
    
    print("\n7.2 安全最佳实践:")
    print("1. 输入验证:")
    print("   - 始终验证gzip文件的有效性")
    print("   - 处理用户提供的gzip文件时要格外小心")
    
    print("\n2. 防止DoS攻击:")
    print("   - 限制最大解压缩大小，防止解压炸弹攻击")
    print("   - 监控解压缩比例，拒绝异常大的解压结果")
    
    print("\n3. 错误处理:")
    print("   - 妥善处理gzip.BadGzipFile异常")
    print("   - 实现超时机制，避免处理无限大的数据")
    
    print("\n7.3 一般最佳实践:")
    print("1. 使用上下文管理器:")
    print("   - 始终使用with语句管理gzip文件，确保正确关闭")
    print("   - 避免资源泄漏")
    
    print("\n2. 选择正确的模式:")
    print("   - 'rb'/'wb': 二进制模式，用于大多数gzip操作")
    print("   - 'rt'/'wt': 文本模式，自动处理编码")
    print("   - 'ab': 追加模式（注意：gzip格式不真正支持追加）")
    
    print("\n3. 编码处理:")
    print("   - 文本模式下始终指定编码参数")
    print("   - 二进制模式下自己处理编码转换")
    
    print("\n4. 内存管理:")
    print("   - 对于大型数据，使用io.BytesIO而非字符串")
    print("   - 及时释放不再需要的大型对象")
    
    print("\n5. 与其他模块结合使用:")
    print("   - 与tarfile结合创建tar.gz归档")
    print("   - 与zipfile结合处理zip文件中的gzip压缩数据")
    print("   - 与文件操作模块(os, shutil)结合使用")

# 8. 实际应用示例
def real_world_examples():
    """
    gzip模块的实际应用示例
    
    功能说明：提供gzip模块在实际项目中的应用示例代码。
    """
    print("\n=== 8. 实际应用示例 ===")
    
    print("\n8.1 日志文件压缩器:")
    print("""
    import gzip
    import os
    import shutil
    from datetime import datetime, timedelta
    import glob
    
    def compress_old_logs(log_dir, days_old=7, keep_original=False, compress_level=6):
        """
        压缩指定天数前的日志文件
        
        参数:
        - log_dir: 日志文件目录
        - days_old: 压缩多少天前的日志，默认7天
        - keep_original: 是否保留原始文件，默认不保留
        - compress_level: 压缩级别，默认6
        """
        # 计算截止日期
        cutoff_date = datetime.now() - timedelta(days=days_old)
        
        # 查找所有日志文件
        log_files = glob.glob(os.path.join(log_dir, "*.log"))
        
        print(f"查找日志目录: {log_dir}")
        print(f"将压缩 {days_old} 天前（{cutoff_date.strftime('%Y-%m-%d')}之前）的日志文件")
        
        compressed_count = 0
        total_space_saved = 0
        
        for log_file in log_files:
            # 获取文件修改时间
            file_mtime = datetime.fromtimestamp(os.path.getmtime(log_file))
            
            # 检查文件是否足够旧
            if file_mtime < cutoff_date:
                gzip_file = log_file + ".gz"
                
                print(f"压缩: {os.path.basename(log_file)} -> {os.path.basename(gzip_file)}")
                
                try:
                    # 压缩文件
                    original_size = os.path.getsize(log_file)
                    
                    with open(log_file, "rb") as f_in:
                        with gzip.open(gzip_file, "wb", compresslevel=compress_level) as f_out:
                            shutil.copyfileobj(f_in, f_out)
                    
                    compressed_size = os.path.getsize(gzip_file)
                    space_saved = original_size - compressed_size
                    compression_ratio = (1 - compressed_size / original_size) * 100
                    
                    print(f"  原始大小: {original_size:,} 字节")
                    print(f"  压缩大小: {compressed_size:,} 字节")
                    print(f"  节省空间: {space_saved:,} 字节 ({compression_ratio:.2f}%)")
                    
                    # 删除原始文件（如果不需要保留）
                    if not keep_original:
                        os.remove(log_file)
                        print(f"  已删除原始文件")
                    
                    compressed_count += 1
                    total_space_saved += space_saved
                    
                except Exception as e:
                    print(f"  压缩失败: {e}")
                    # 如果压缩失败，尝试删除不完整的gzip文件
                    if os.path.exists(gzip_file):
                        os.remove(gzip_file)
        
        print(f"\n压缩完成")
        print(f"压缩了 {compressed_count} 个日志文件")
        print(f"总共节省: {total_space_saved:,} 字节 ({total_space_saved / (1024*1024):.2f} MB)")
    
    # 使用示例
    # compress_old_logs("/var/log/myapp", days_old=7, keep_original=False)
    """)
    
    print("\n8.2 数据备份与压缩工具:")
    print("""
    import gzip
    import os
    import shutil
    from datetime import datetime
    import argparse
    import time
    
    def backup_and_compress(source, destination=None, compress_level=6):
        """
        备份文件并压缩
        
        参数:
        - source: 源文件或目录
        - destination: 目标压缩文件路径，默认在当前目录
        - compress_level: 压缩级别
        """
        # 验证源文件是否存在
        if not os.path.exists(source):
            print(f"错误: 源文件或目录不存在: {source}")
            return False
        
        # 确定目标文件名
        if destination is None:
            base_name = os.path.basename(source)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            destination = f"{base_name}_{timestamp}.gz"
        
        print(f"备份开始: {source} -> {destination}")
        print(f"压缩级别: {compress_level}")
        
        start_time = time.time()
        
        try:
            if os.path.isfile(source):
                # 单个文件压缩
                original_size = os.path.getsize(source)
                
                with open(source, "rb") as f_in:
                    with gzip.open(destination, "wb", compresslevel=compress_level) as f_out:
                        shutil.copyfileobj(f_in, f_out)
                
                compressed_size = os.path.getsize(destination)
                space_saved = original_size - compressed_size
                compression_ratio = (1 - compressed_size / original_size) * 100
                
                print(f"文件压缩完成")
                print(f"  原始大小: {original_size:,} 字节")
                print(f"  压缩大小: {compressed_size:,} 字节")
                print(f"  压缩率: {compression_ratio:.2f}%")
                
            elif os.path.isdir(source):
                # 注意：gzip只能压缩单个文件，对于目录，我们需要先创建tar归档
                # 这里简单起见，我们只提供一个示例，实际应用中应结合tarfile模块
                print("注意: gzip不能直接压缩目录。对于目录备份，建议使用tar+gzip组合")
                print("示例命令: tar -czvf archive.tar.gz /path/to/directory")
                print("或使用Python的tarfile和gzip模块结合")
                return False
            
            duration = time.time() - start_time
            print(f"备份完成，耗时: {duration:.2f} 秒")
            print(f"备份文件: {destination}")
            
            return True
            
        except Exception as e:
            print(f"备份失败: {e}")
            # 清理不完整的备份文件
            if os.path.exists(destination):
                os.remove(destination)
            return False
    
    # 命令行接口
    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="文件备份和压缩工具")
        parser.add_argument("source", help="源文件路径")
        parser.add_argument("-d", "--destination", help="目标压缩文件路径")
        parser.add_argument("-l", "--level", type=int, choices=range(0, 10), default=6,
                            help="压缩级别 (0-9, 默认: 6)")
        
        args = parser.parse_args()
        
        backup_and_compress(
            source=args.source,
            destination=args.destination,
            compress_level=args.level
        )
    """)
    
    print("\n8.3 大文件压缩进度监控:")
    print("""
    import gzip
    import os
    import sys
    
    def compress_with_progress(source_file, dest_file, chunk_size=8192, level=6):
        """
        压缩文件并显示进度条
        
        参数:
        - source_file: 源文件路径
        - dest_file: 目标文件路径
        - chunk_size: 读取块大小
        - level: 压缩级别
        """
        # 获取源文件大小
        file_size = os.path.getsize(source_file)
        processed = 0
        
        print(f"开始压缩: {source_file}")
        print(f"目标文件: {dest_file}")
        print(f"文件大小: {file_size:,} 字节")
        
        with open(source_file, "rb") as f_in:
            with gzip.open(dest_file, "wb", compresslevel=level) as f_out:
                while True:
                    chunk = f_in.read(chunk_size)
                    if not chunk:
                        break
                    
                    f_out.write(chunk)
                    processed += len(chunk)
                    
                    # 计算进度百分比
                    progress = min(100, (processed / file_size) * 100)
                    
                    # 显示进度条
                    bar_length = 30
                    filled_length = int(bar_length * processed / file_size)
                    bar = '=' * filled_length + '-' * (bar_length - filled_length)
                    
                    # 使用\r覆盖当前行
                    sys.stdout.write(f"[{bar}] {progress:.1f}% ({processed:,}/{file_size:,} 字节)\r")
                    sys.stdout.flush()
        
        # 完成后换行
        sys.stdout.write("\n")
        
        # 显示压缩结果
        compressed_size = os.path.getsize(dest_file)
        compression_ratio = (1 - compressed_size / file_size) * 100
        
        print(f"压缩完成!")
        print(f"压缩文件大小: {compressed_size:,} 字节")
        print(f"压缩率: {compression_ratio:.2f}%")
    
    # 使用示例
    # compress_with_progress("large_data.bin", "large_data.bin.gz", chunk_size=16384, level=6)
    """)

# 运行所有示例
def run_all_examples():
    print("====================================")
    print("Python gzip模块功能详解")
    print("====================================")
    
    # 1. 基本操作
    basic_gzip_operations()
    
    # 2. 压缩级别控制
    compression_level_control()
    
    # 3. 内存中操作
    in_memory_operations()
    
    # 4. 高级功能
    advanced_gzip_features()
    
    # 5. 流式处理
    streaming_large_data()
    
    # 6. HTTP应用
    http_gzip_examples()
    
    # 7. 最佳实践
    gzip_best_practices()
    
    # 8. 实际应用
    real_world_examples()
    
    print("\n====================================")
    print("gzip模块功能演示完成")
    print("====================================")

# 运行示例
if __name__ == "__main__":
    run_all_examples()
```

## gzip模块总结

gzip模块是Python处理gzip压缩文件的标准库，提供了简单而强大的接口来压缩和解压缩数据。通过本模块的学习，我们了解到：

1. **基本操作**：创建、读取和写入gzip压缩文件的核心功能
2. **压缩级别**：从0（无压缩）到9（最高压缩）的压缩级别控制
3. **内存操作**：在内存中直接压缩和解压缩数据的方法
4. **流式处理**：分块处理大型文件，避免内存问题
5. **高级功能**：自定义修改时间、处理gzip头信息等
6. **HTTP应用**：在Web通信中使用gzip进行内容压缩

在使用gzip模块时，需要注意以下几点：

1. **性能平衡**：根据需求选择合适的压缩级别，平衡压缩率和速度
2. **内存管理**：处理大型文件时使用分块读取，避免一次性加载全部内容
3. **安全性**：处理未知来源的gzip文件时要验证有效性，防止解压炸弹攻击
4. **文件格式限制**：gzip只能压缩单个文件，压缩目录需要先创建tar归档
5. **编码处理**：文本模式下注意指定正确的编码

gzip模块虽然简单，但功能强大，是处理压缩数据的重要工具。它常与其他模块（如tarfile、os、shutil）结合使用，以实现更复杂的压缩和归档功能。对于Web开发、数据备份、日志处理等场景，gzip模块提供了高效的数据压缩解决方案。