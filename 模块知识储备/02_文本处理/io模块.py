# io模块 - 输入输出流操作
# 功能作用：提供处理各种I/O（输入/输出）操作的核心工具，包括文件操作、内存缓冲区操作等
# 使用情景：文件读写、内存中的数据处理、流处理、文本和二进制数据转换
# 注意事项：区分文本模式和二进制模式，注意编码处理，避免资源泄漏

import io
import os

# 模块概述
"""
io模块提供了处理各种I/O（输入/输出）操作的统一接口和工具。
它定义了基本的流接口和多种流实现，包括：
- 文本I/O：处理文本数据的流（需要编码/解码）
- 二进制I/O：处理原始字节的流
- 缓冲I/O：提供缓冲区功能以提高性能

主要组件：
- IOBase：所有I/O类的抽象基类
- RawIOBase：原始二进制I/O的基类
- FileIO：文件系统文件的原始I/O操作
- BufferedIOBase：缓冲二进制流的基类
- BufferedReader/BufferedWriter/BufferedRandom：缓冲二进制流实现
- TextIOBase：文本I/O的基类
- TextIOWrapper：将二进制流包装为文本流
- StringIO：内存中的文本流
- BytesIO：内存中的二进制流

io模块是Python处理各种输入输出操作的基础，特别是在需要统一处理不同来源的数据时非常有用。
"""

# 1. 基本流类型
print("=== 1. 基本流类型 ===")

# 流类型层次结构
def print_stream_hierarchy():
    """打印I/O流类型的层次结构"""
    print("I/O流类型层次结构:")
    print("- IOBase: 所有I/O类的抽象基类")
    print("  ├── RawIOBase: 原始二进制I/O的基类")
    print("  │   └── FileIO: 文件系统文件的原始I/O操作")
    print("  ├── BufferedIOBase: 缓冲二进制流的基类")
    print("  │   ├── BufferedReader: 缓冲二进制读取流")
    print("  │   ├── BufferedWriter: 缓冲二进制写入流")
    print("  │   └── BufferedRandom: 随机访问缓冲二进制流")
    print("  └── TextIOBase: 文本I/O的基类")
    print("      ├── TextIOWrapper: 将二进制流包装为文本流")
    print("      ├── StringIO: 内存中的文本流")
    print("      └── 其他文本流实现")

print_stream_hierarchy()
print()

# 2. StringIO - 内存中的文本流
print("=== 2. StringIO - 内存中的文本流 ===")

# 创建和写入StringIO
def stringio_basic_example():
    """StringIO基本示例"""
    print("StringIO基本操作:")
    
    # 创建一个StringIO对象
    output = io.StringIO()
    
    # 写入数据
    output.write("Hello, World!\n")
    output.write("这是一个StringIO示例\n")
    output.write(f"当前位置: {output.tell()}\n")
    
    # 获取内容（需要先将指针移到开头）
    output.seek(0)
    content = output.read()
    print(f"读取的内容:\n{content}")
    
    # 再次写入数据（追加到末尾）
    output.write("这是追加的数据\n")
    
    # 获取全部内容
    output.seek(0)
    all_content = output.read()
    print(f"全部内容:\n{all_content}")
    
    # 关闭流
    output.close()
    
    print("\nStringIO作为上下文管理器:")
    # 使用with语句自动关闭流
    with io.StringIO() as f:
        f.write("使用with语句创建的StringIO\n")
        f.write("自动管理资源\n")
        
        # 读取内容
        f.seek(0)
        print(f.read())

stringio_basic_example()
print()

# 3. BytesIO - 内存中的二进制流
print("=== 3. BytesIO - 内存中的二进制流 ===")

def bytesio_basic_example():
    """BytesIO基本示例"""
    print("BytesIO基本操作:")
    
    # 创建一个BytesIO对象
    output = io.BytesIO()
    
    # 写入二进制数据
    output.write(b"Hello, Binary World!\n")
    output.write("你好，二进制世界！\n".encode('utf-8'))
    output.write(b"Current position: " + str(output.tell()).encode('utf-8') + b"\n")
    
    # 获取内容
    output.seek(0)
    content = output.read()
    print(f"读取的二进制内容:\n{content}")
    
    # 解码查看文本内容
    try:
        text_content = content.decode('utf-8')
        print(f"解码后的文本内容:\n{text_content}")
    except UnicodeDecodeError as e:
        print(f"解码错误: {e}")
    
    # 从已有字节创建BytesIO
    existing_bytes = b"这是一个预设的字节串"
    input_stream = io.BytesIO(existing_bytes)
    
    # 读取内容
    read_bytes = input_stream.read()
    print(f"\n从预设字节创建BytesIO:\n{read_bytes.decode('utf-8')}")
    
    # 关闭流
    output.close()
    input_stream.close()
    
    # 使用with语句
    print("\nBytesIO作为上下文管理器:")
    with io.BytesIO() as f:
        f.write(b"使用with语句的BytesIO\n")
        f.write("自动管理资源\n".encode('utf-8'))
        
        # 读取内容
        f.seek(0)
        print(f.read())

bytesio_basic_example()
print()

# 4. 文件I/O操作
print("=== 4. 文件I/O操作 ===")

def file_io_example():
    """文件I/O操作示例"""
    # 注意：这里不实际创建文件，仅展示代码
    
    print("文件I/O操作示例:")
    print("注意：以下是演示代码，不会实际创建或修改文件")
    
    # 文本模式文件操作
    print("\n文本模式文件操作:")
    print("""
    # 使用io.open()打开文本文件（与内置open()功能相同）
    with io.open('example.txt', 'w', encoding='utf-8') as f:
        f.write("这是一个文本文件\n")
        f.write("使用UTF-8编码\n")
    
    with io.open('example.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    """)
    
    # 二进制模式文件操作
    print("\n二进制模式文件操作:")
    print("""
    # 二进制模式打开文件
    with io.open('binary.bin', 'wb') as f:
        f.write(b'\x00\x01\x02\x03')
        f.write("你好".encode('utf-8'))
    
    with io.open('binary.bin', 'rb') as f:
        data = f.read()
        print(f"读取的二进制数据: {data}")
    """)
    
    # 高级文件操作
    print("\n高级文件操作:")
    print("""
    # 行缓冲模式
    with io.open('line_buffered.txt', 'w', buffering=1, encoding='utf-8') as f:
        for i in range(10):
            f.write(f"这是第{i+1}行\n")  # 每行都会刷新缓冲区
    
    # 指定缓冲区大小
    buffer_size = io.DEFAULT_BUFFER_SIZE  # 默认缓冲区大小
    with io.open('custom_buffer.txt', 'w', buffering=buffer_size*2, encoding='utf-8') as f:
        f.write("大缓冲区写入示例")
    """)

file_io_example()
print()

# 5. 缓冲I/O
print("=== 5. 缓冲I/O ===")

def buffered_io_example():
    """缓冲I/O示例"""
    print("缓冲I/O操作示例:")
    
    # 注意：以下示例使用内存流模拟
    print("\n缓冲读取器示例:")
    
    # 创建一个二进制流
    raw_data = b"这是一个缓冲I/O的示例数据。" * 1000
    binary_stream = io.BytesIO(raw_data)
    
    # 创建缓冲读取器
    buffered_reader = io.BufferedReader(binary_stream, buffer_size=8192)
    
    # 读取数据
    chunk1 = buffered_reader.read(100)
    print(f"读取第一个块: {chunk1}")
    
    # 使用readline()方法
    binary_stream.seek(0)
    line = buffered_reader.readline(50)  # 尝试读取一行，最多50个字节
    print(f"读取一行: {line}")
    
    # 使用readlines()方法
    binary_stream.seek(0)
    lines = buffered_reader.readlines(200)  # 读取最多200个字节的所有行
    print(f"读取多行，行数: {len(lines)}")
    
    # 缓冲写入器示例
    print("\n缓冲写入器示例:")
    
    output_stream = io.BytesIO()
    buffered_writer = io.BufferedWriter(output_stream, buffer_size=1024)
    
    # 写入数据
    buffered_writer.write(b"这是写入缓冲的数据\n")
    buffered_writer.write(b"更多的数据\n")
    
    # 注意：数据可能仍在缓冲区中，需要刷新或关闭写入器
    buffered_writer.flush()  # 确保数据被写入到底层流
    
    # 获取写入的数据
    output_stream.seek(0)
    written_data = output_stream.read()
    print(f"写入的数据: {written_data}")
    
    # 随机访问缓冲流
    print("\n随机访问缓冲流示例:")
    
    # 创建一个可读写的缓冲流
    random_stream = io.BytesIO()
    buffered_random = io.BufferedRandom(random_stream, buffer_size=1024)
    
    # 写入数据
    buffered_random.write(b"这是随机访问缓冲流的测试")
    
    # 移动到开头并读取数据
    buffered_random.seek(0)
    read_data = buffered_random.read(10)
    print(f"读取的数据: {read_data}")
    
    # 在中间位置写入
    buffered_random.seek(5)
    buffered_random.write(b"MODIFIED")
    
    # 查看修改后的数据
    buffered_random.seek(0)
    modified_data = buffered_random.read()
    print(f"修改后的数据: {modified_data}")
    
    # 清理资源
    buffered_reader.close()
    buffered_writer.close()
    buffered_random.close()

buffered_io_example()
print()

# 6. 文本I/O包装器
print("=== 6. 文本I/O包装器 ===")

def text_io_wrapper_example():
    """文本I/O包装器示例"""
    print("文本I/O包装器示例:")
    
    # 创建二进制流
    binary_stream = io.BytesIO()
    
    # 创建文本I/O包装器
    text_wrapper = io.TextIOWrapper(
        binary_stream,
        encoding='utf-8',       # 指定编码
        errors='replace',       # 错误处理方式
        newline='\n',           # 换行符处理
        write_through=False     # 写入是否立即刷新到底层流
    )
    
    # 写入文本
    text_wrapper.write("你好，这是中文文本！\n")
    text_wrapper.write("Hello, this is English text!\n")
    text_wrapper.write("这行包含一个非法字符: \ud800")  # 非法的UTF-16代理项
    
    # 刷新缓冲区以确保所有数据都被编码并写入二进制流
    text_wrapper.flush()
    
    # 查看二进制流中的编码数据
    binary_stream.seek(0)
    encoded_data = binary_stream.read()
    print(f"编码后的数据: {encoded_data}")
    
    # 重新读取文本
    binary_stream.seek(0)
    text_wrapper.detach()  # 分离之前的二进制流
    
    # 创建新的文本包装器来读取数据
    new_text_wrapper = io.TextIOWrapper(binary_stream, encoding='utf-8')
    read_text = new_text_wrapper.read()
    print(f"\n重新读取的文本:\n{read_text}")
    
    # 配置行缓冲
    print("\n配置行缓冲:")
    
    with io.BytesIO() as binary_output:
        # 配置行缓冲的文本包装器
        line_buffered = io.TextIOWrapper(
            binary_output,
            encoding='utf-8',
            line_buffering=True  # 启用行缓冲
        )
        
        line_buffered.write("这将立即刷新\n")  # 写入换行符会触发刷新
        line_buffered.write("这行不会立即刷新，直到写入更多数据或显式刷新")
        
        # 手动刷新
        line_buffered.flush()
        
        binary_output.seek(0)
        content = binary_output.read()
        print(f"行缓冲写入的内容: {content.decode('utf-8')}")
    
    # 清理资源
    new_text_wrapper.close()

text_io_wrapper_example()
print()

# 7. 自定义流
print("=== 7. 自定义流 ===")

def custom_stream_example():
    """自定义流示例"""
    print("自定义流示例:")
    
    # 自定义文本流类
    class CustomTextIO(io.TextIOBase):
        """自定义文本流示例"""
        
        def __init__(self):
            self.buffer = []
            self.position = 0
        
        def write(self, text):
            """写入文本"""
            if not isinstance(text, str):
                raise TypeError("必须写入字符串")
            
            self.buffer.append(text)
            return len(text)
        
        def read(self, size=None):
            """读取文本"""
            content = ''.join(self.buffer)
            if size is None:
                result = content[self.position:]
                self.position = len(content)
            else:
                result = content[self.position:self.position + size]
                self.position += len(result)
            return result
        
        def tell(self):
            """返回当前位置"""
            return self.position
        
        def seek(self, offset, whence=io.SEEK_SET):
            """移动到指定位置"""
            content = ''.join(self.buffer)
            length = len(content)
            
            if whence == io.SEEK_SET:
                self.position = offset
            elif whence == io.SEEK_CUR:
                self.position += offset
            elif whence == io.SEEK_END:
                self.position = length + offset
            else:
                raise ValueError("无效的whence参数")
            
            # 确保位置有效
            self.position = max(0, min(self.position, length))
            return self.position
        
        def close(self):
            """关闭流"""
            self.buffer = []
            self.position = 0
            super().close()
    
    # 测试自定义文本流
    print("\n自定义文本流测试:")
    custom_stream = CustomTextIO()
    
    # 写入数据
    custom_stream.write("Hello, ")
    custom_stream.write("自定义文本流!")
    custom_stream.write("\n这是第二行")
    
    # 读取数据
    custom_stream.seek(0)
    content = custom_stream.read()
    print(f"读取的内容:\n{content}")
    
    # 测试定位和部分读取
    custom_stream.seek(7)
    partial = custom_stream.read(10)
    print(f"从位置7读取10个字符: '{partial}'")
    
    # 测试关闭
    custom_stream.close()
    
    # 自定义二进制流
    print("\n自定义二进制流:")
    
    class CustomBinaryIO(io.RawIOBase):
        """自定义二进制流示例"""
        
        def __init__(self):
            self.buffer = bytearray()
            self.position = 0
        
        def write(self, b):
            """写入二进制数据"""
            if isinstance(b, str):
                raise TypeError("必须写入字节或字节数组")
            
            self.buffer.extend(b)
            return len(b)
        
        def readinto(self, b):
            """读取数据到提供的缓冲区"""
            available = len(self.buffer) - self.position
            if available <= 0:
                return 0
            
            size = len(b)
            read_size = min(available, size)
            
            b[:read_size] = self.buffer[self.position:self.position + read_size]
            self.position += read_size
            
            return read_size
        
        def tell(self):
            """返回当前位置"""
            return self.position
        
        def seek(self, offset, whence=io.SEEK_SET):
            """移动到指定位置"""
            length = len(self.buffer)
            
            if whence == io.SEEK_SET:
                self.position = offset
            elif whence == io.SEEK_CUR:
                self.position += offset
            elif whence == io.SEEK_END:
                self.position = length + offset
            else:
                raise ValueError("无效的whence参数")
            
            # 确保位置有效
            self.position = max(0, min(self.position, length))
            return self.position
        
        def close(self):
            """关闭流"""
            self.buffer = bytearray()
            self.position = 0
            super().close()
    
    # 测试自定义二进制流
    print("\n自定义二进制流测试:")
    binary_stream = CustomBinaryIO()
    
    # 写入数据
    binary_stream.write(b"Hello, ")
    binary_stream.write("二进制流".encode('utf-8'))
    
    # 读取数据
    binary_stream.seek(0)
    read_buffer = bytearray(20)
    read_size = binary_stream.readinto(read_buffer)
    print(f"读取的字节数: {read_size}")
    print(f"读取的内容: {read_buffer[:read_size]}")
    
    # 转换为文本
    text = bytes(read_buffer[:read_size]).decode('utf-8')
    print(f"解码后的文本: '{text}'")
    
    # 关闭流
    binary_stream.close()

custom_stream_example()
print()

# 8. 实用工具和常量
print("=== 8. 实用工具和常量 ===")

def io_utils_and_constants():
    """I/O实用工具和常量"""
    print("I/O实用工具和常量:")
    
    # 缓冲区大小
    print(f"默认缓冲区大小: {io.DEFAULT_BUFFER_SIZE}")
    print()
    
    # 常量
    print("I/O常量:")
    print(f"SEEK_SET (从开始位置): {io.SEEK_SET}")
    print(f"SEEK_CUR (从当前位置): {io.SEEK_CUR}")
    print(f"SEEK_END (从结束位置): {io.SEEK_END}")
    print()
    
    # 检查流类型
    print("检查流类型:")
    
    # 创建不同类型的流
    text_stream = io.StringIO()
    binary_stream = io.BytesIO()
    
    # 检查是否为文本流
    print(f"StringIO是文本流: {io.is_text_stream(text_stream)}")
    print(f"BytesIO是文本流: {io.is_text_stream(binary_stream)}")
    
    # 检查是否为二进制流
    print(f"StringIO是二进制流: {io.is_binary_stream(text_stream)}")
    print(f"BytesIO是二进制流: {io.is_binary_stream(binary_stream)}")
    print()
    
    # 打开方法
    print("io.open()方法:")
    print("io.open()函数与内置open()函数功能相同，提供统一的文件打开接口")
    print("""
    # 打开文本文件
    with io.open('text.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 打开二进制文件
    with io.open('binary.bin', 'rb') as f:
        data = f.read()
    """)
    
    # 清理资源
    text_stream.close()
    binary_stream.close()

io_utils_and_constants()
print()

# 9. 实际应用示例
print("=== 9. 实际应用示例 ===")

def practical_applications():
    """实际应用示例"""
    
    # 1. 内存中的CSV处理
    def csv_in_memory():
        """内存中的CSV处理"""
        print("\n1. 内存中的CSV处理:")
        
        import csv
        
        # 创建模拟CSV数据
        csv_data = io.StringIO()
        
        # 写入CSV数据
        writer = csv.writer(csv_data)
        writer.writerow(['姓名', '年龄', '城市'])
        writer.writerow(['张三', 25, '北京'])
        writer.writerow(['李四', 30, '上海'])
        writer.writerow(['王五', 28, '广州'])
        
        # 将指针移到开头
        csv_data.seek(0)
        
        # 读取CSV数据
        reader = csv.reader(csv_data)
        rows = list(reader)
        
        print("CSV数据:")
        for row in rows:
            print(row)
        
        # CSV数据的二进制表示
        csv_data.seek(0)
        binary_csv = csv_data.read().encode('utf-8')
        print(f"\nCSV数据的二进制表示: {binary_csv[:100]}...")
        
        # 清理资源
        csv_data.close()
    
    # 2. 捕获标准输出
    def capture_stdout():
        """捕获标准输出"""
        print("\n2. 捕获标准输出:")
        
        import sys
        
        # 保存原始的stdout
        original_stdout = sys.stdout
        
        try:
            # 创建StringIO对象来捕获输出
            captured_output = io.StringIO()
            sys.stdout = captured_output
            
            # 生成一些输出
            print("这行输出会被捕获")
            print("这行也会被捕获")
            print(f"计算结果: {1 + 1}")
            
            # 恢复原始的stdout
            sys.stdout = original_stdout
            
            # 获取捕获的内容
            output = captured_output.getvalue()
            print("\n捕获的输出内容:")
            print(output)
            
        finally:
            # 确保无论如何都恢复stdout
            sys.stdout = original_stdout
            captured_output.close()
    
    # 3. 二进制数据处理
    def binary_data_processing():
        """二进制数据处理"""
        print("\n3. 二进制数据处理:")
        
        # 创建二进制数据
        binary_data = io.BytesIO()
        
        # 写入各种二进制数据
        binary_data.write(b'\x00\x01\x02\x03')  # 简单的字节序列
        binary_data.write(int(100).to_bytes(2, byteorder='big'))  # 整数转换为字节
        binary_data.write(b'\x00')  # 分隔符
        binary_data.write('测试字符串'.encode('utf-8'))  # 编码的字符串
        
        # 处理二进制数据
        binary_data.seek(0)
        
        # 读取前4个字节
        header = binary_data.read(4)
        print(f"头部数据: {header.hex()}")
        
        # 读取2字节整数
        int_bytes = binary_data.read(2)
        number = int.from_bytes(int_bytes, byteorder='big')
        print(f"读取的整数: {number}")
        
        # 跳过分隔符
        binary_data.read(1)
        
        # 读取剩余的字符串
        string_data = binary_data.read()
        text = string_data.decode('utf-8')
        print(f"读取的字符串: '{text}'")
        
        # 清理资源
        binary_data.close()
    
    # 4. 文本和二进制转换
    def text_binary_conversion():
        """文本和二进制转换"""
        print("\n4. 文本和二进制转换:")
        
        # 文本到二进制
        original_text = "这是一个包含多种字符的文本：!@#$%^&*()"
        
        # 使用不同编码转换
        utf8_bytes = original_text.encode('utf-8')
        gbk_bytes = original_text.encode('gbk')
        latin1_bytes = original_text.encode('latin-1', errors='replace')
        
        print(f"原始文本: '{original_text}'")
        print(f"UTF-8编码: {utf8_bytes}")
        print(f"GBK编码: {gbk_bytes}")
        print(f"Latin-1编码(替换错误): {latin1_bytes}")
        print()
        
        # 二进制到文本
        print("二进制到文本转换:")
        
        try:
            utf8_text = utf8_bytes.decode('utf-8')
            print(f"UTF-8解码: '{utf8_text}'")
        except UnicodeDecodeError as e:
            print(f"UTF-8解码错误: {e}")
        
        try:
            # 尝试用错误的编码解码
            wrong_text = utf8_bytes.decode('gbk')
            print(f"错误编码(GBK)解码: '{wrong_text}'")
        except UnicodeDecodeError as e:
            print(f"GBK解码错误: {e}")
        
        # 使用不同的错误处理方式
        replace_text = b'\xff\xfe\x00'.decode('utf-8', errors='replace')
        ignore_text = b'\xff\xfe\x00'.decode('utf-8', errors='ignore')
        backslash_text = b'\xff\xfe\x00'.decode('utf-8', errors='backslashreplace')
        
        print(f"替换错误字符: '{replace_text}'")
        print(f"忽略错误字符: '{ignore_text}'")
        print(f"反斜杠转义: '{backslash_text}'")
    
    # 5. 流过滤器
    def stream_filter():
        """流过滤器示例"""
        print("\n5. 流过滤器:")
        
        class UppercaseFilter:
            """将通过的所有文本转换为大写的过滤器"""
            
            def __init__(self, stream):
                self.stream = stream
            
            def write(self, text):
                """写入转换为大写的文本"""
                return self.stream.write(text.upper())
            
            def __getattr__(self, name):
                """将未定义的方法委托给底层流"""
                return getattr(self.stream, name)
        
        # 测试过滤器
        output_stream = io.StringIO()
        filtered_stream = UppercaseFilter(output_stream)
        
        # 写入数据
        filtered_stream.write("Hello, World!\n")
        filtered_stream.write("这是一个测试。This is a test.\n")
        
        # 获取结果
        output_stream.seek(0)
        result = output_stream.read()
        
        print("通过大写过滤器后的结果:")
        print(result)
        
        # 清理资源
        output_stream.close()
    
    # 运行实用示例
    csv_in_memory()
    capture_stdout()
    binary_data_processing()
    text_binary_conversion()
    stream_filter()

practical_applications()
print()

# 10. 高级用法和技巧
print("=== 10. 高级用法和技巧 ===")

def advanced_techniques():
    """高级用法和技巧"""
    
    # 1. 内存映射文件
    def memory_mapped_files():
        """内存映射文件"""
        print("\n1. 内存映射文件:")
        print("注意：以下是演示代码，不会实际创建或修改文件")
        
        print("""
        import mmap
        import io
        
        def memory_map_example():
            """内存映射文件示例"""
            with open('large_file.bin', 'r+b') as f:
                # 创建内存映射
                with mmap.mmap(
                    f.fileno(),        # 文件描述符
                    length=0,          # 0表示映射整个文件
                    access=mmap.ACCESS_WRITE,  # 可写访问
                    offset=0           # 映射的起始位置
                ) as mm:
                    # 现在可以像访问字节数组一样访问文件
                    mm[0:10] = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
                    
                    # 读取数据
                    data = mm[100:200]
                    print(f"读取的数据: {data}")
        """)
    
    # 2. 流式处理大型数据集
    def streaming_large_datasets():
        """流式处理大型数据集"""
        print("\n2. 流式处理大型数据集:")
        
        def stream_processor():
            """流式数据处理器"""
            class StreamProcessor:
                """处理大型数据流的处理器"""
                
                def __init__(self, chunk_size=8192):
                    self.chunk_size = chunk_size
                
                def process_text_file(self, file_path, processor_func):
                    """处理文本文件"""
                    results = []
                    
                    with io.open(file_path, 'r', encoding='utf-8') as f:
                        while True:
                            chunk = f.read(self.chunk_size)
                            if not chunk:
                                break
                            results.append(processor_func(chunk))
                    
                    return results
                
                def process_binary_file(self, file_path, processor_func):
                    """处理二进制文件"""
                    results = []
                    
                    with io.open(file_path, 'rb') as f:
                        while True:
                            chunk = f.read(self.chunk_size)
                            if not chunk:
                                break
                            results.append(processor_func(chunk))
                    
                    return results
        
        # 演示StreamProcessor类的使用
        print("流处理器类定义:")
        print(stream_processor.__doc__)
        print()
        print("使用示例:")
        print("""
        # 创建处理器实例
        processor = StreamProcessor(chunk_size=4096)
        
        # 定义处理函数 - 计算文本中的单词数
        def count_words(text_chunk):
            words = text_chunk.split()
            return len(words)
        
        # 处理文本文件
        # word_counts = processor.process_text_file('large_document.txt', count_words)
        # total_words = sum(word_counts)
        # print(f"总单词数: {total_words}")
        """)
    
    # 3. 自定义缓冲策略
    def custom_buffering_strategies():
        """自定义缓冲策略"""
        print("\n3. 自定义缓冲策略:")
        
        class CustomBuffer:
            """自定义缓冲类"""
            
            def __init__(self, underlying_stream, buffer_size=8192):
                self.stream = underlying_stream
                self.buffer_size = buffer_size
                self.buffer = bytearray()
            
            def write(self, data):
                """写入数据，使用自定义缓冲策略"""
                self.buffer.extend(data)
                
                # 当缓冲区超过阈值时刷新
                if len(self.buffer) >= self.buffer_size:
                    return self.flush()
                
                return len(data)
            
            def flush(self):
                """刷新缓冲区"""
                if self.buffer:
                    written = self.stream.write(self.buffer)
                    self.buffer = bytearray()
                    return written
                return 0
            
            def close(self):
                """关闭流"""
                self.flush()
                return self.stream.close()
        
        # 测试自定义缓冲
        print("自定义缓冲类示例:")
        
        # 创建内存流和自定义缓冲
        memory_stream = io.BytesIO()
        custom_buffer = CustomBuffer(memory_stream, buffer_size=10)
        
        # 写入小于缓冲区大小的数据
        custom_buffer.write(b"Hello")
        print(f"写入小数据后缓冲区大小: {len(custom_buffer.buffer)}")
        
        # 写入更多数据，触发刷新
        custom_buffer.write(b" World!")
        print(f"写入大数据后缓冲区大小: {len(custom_buffer.buffer)}")
        
        # 获取内存流中的数据
        memory_stream.seek(0)
        content = memory_stream.read()
        print(f"内存流中的内容: {content}")
        
        # 手动刷新
        custom_buffer.write(b" Additional")
        custom_buffer.flush()
        
        memory_stream.seek(0)
        final_content = memory_stream.read()
        print(f"最终内容: {final_content}")
        
        # 清理资源
        custom_buffer.close()
    
    # 4. 异步I/O简介
    def async_io_intro():
        """异步I/O简介"""
        print("\n4. 异步I/O简介:")
        print("注意：完整的异步I/O通常使用asyncio模块，这里只做简单介绍")
        
        print("""
        import asyncio
        import io
        
        async def async_file_operations():
            """异步文件操作示例"""
            # 注意：异步文件I/O在Python中需要特定的支持
            # 这里仅作为示例
            
            # 异步读取文件
            async def read_file_async(file_path):
                # 在实际应用中，应该使用aiofiles等库
                loop = asyncio.get_event_loop()
                with open(file_path, 'r', encoding='utf-8') as f:
                    # 使用执行器在单独线程中执行阻塞操作
                    content = await loop.run_in_executor(
                        None,  # 使用默认执行器
                        f.read
                    )
                    return content
            
            # 异步写入文件
            async def write_file_async(file_path, content):
                loop = asyncio.get_event_loop()
                with open(file_path, 'w', encoding='utf-8') as f:
                    await loop.run_in_executor(
                        None,
                        f.write, content
                    )
            
            # 使用示例
            # await write_file_async('async_example.txt', 'Hello, Async World!')
            # content = await read_file_async('async_example.txt')
            # print(content)
        """)
    
    # 5. 二进制协议实现
    def binary_protocol_implementation():
        """二进制协议实现"""
        print("\n5. 二进制协议实现:")
        
        class BinaryProtocol:
            """简单的二进制协议实现"""
            
            @staticmethod
            def encode_message(message_type, payload):
                """编码消息"""
                # 消息格式: [type(1字节)][length(2字节)][payload]
                if not isinstance(payload, bytes):
                    payload = payload.encode('utf-8')
                
                # 确保message_type是单个字节
                if isinstance(message_type, int):
                    type_byte = message_type.to_bytes(1, byteorder='big')
                else:
                    type_byte = message_type[:1].encode('utf-8')
                
                # 计算负载长度
                length_bytes = len(payload).to_bytes(2, byteorder='big')
                
                # 组装消息
                return type_byte + length_bytes + payload
            
            @staticmethod
            def decode_message(data):
                """解码消息"""
                # 确保数据足够长
                if len(data) < 3:
                    return None, None, data  # 数据不足，返回剩余部分
                
                # 解析消息类型
                message_type = data[0]
                
                # 解析负载长度
                length = int.from_bytes(data[1:3], byteorder='big')
                
                # 检查是否有足够的数据
                if len(data) < 3 + length:
                    return None, None, data  # 数据不足，返回剩余部分
                
                # 提取负载
                payload = data[3:3+length]
                
                # 返回解析结果和未使用的数据
                return message_type, payload, data[3+length:]
        
        # 测试二进制协议
        print("二进制协议测试:")
        
        # 编码消息
        message1 = BinaryProtocol.encode_message(1, "Hello, Protocol!")
        message2 = BinaryProtocol.encode_message(2, "Another message")
        
        print(f"编码的消息1: {message1.hex()}")
        print(f"编码的消息2: {message2.hex()}")
        
        # 合并消息以模拟流
        combined = message1 + message2
        print(f"合并的消息: {combined.hex()}")
        
        # 解码消息
        remaining = combined
        messages = []
        
        while remaining:
            msg_type, payload, remaining = BinaryProtocol.decode_message(remaining)
            if msg_type is not None:
                messages.append((msg_type, payload))
            else:
                break
        
        print("\n解码的消息:")
        for i, (msg_type, payload) in enumerate(messages):
            print(f"消息 {i+1}:")
            print(f"  类型: {msg_type}")
            try:
                print(f"  内容: '{payload.decode('utf-8')}'")
            except UnicodeDecodeError:
                print(f"  内容(二进制): {payload.hex()}")
    
    # 运行高级技巧示例
    memory_mapped_files()
    streaming_large_datasets()
    custom_buffering_strategies()
    async_io_intro()
    binary_protocol_implementation()

advanced_techniques()
print()

# 11. 注意事项和最佳实践
"""
1. **区分文本和二进制模式**:
   - 处理文本文件时使用文本模式（'r', 'w', 'a'）
   - 处理二进制文件时使用二进制模式（'rb', 'wb', 'ab'）
   - 文本模式会自动处理编码/解码，二进制模式直接操作字节

2. **编码处理**:
   - 总是显式指定文件的编码，不要依赖默认编码
   - 使用UTF-8作为首选编码，它支持所有Unicode字符
   - 处理国际化文本时特别注意编码问题

3. **资源管理**:
   - 使用with语句（上下文管理器）自动关闭文件和流
   - 避免手动管理文件描述符，减少资源泄漏
   - 在异常处理中确保资源被正确释放

4. **性能考虑**:
   - 对大文件使用缓冲I/O以提高性能
   - 对于频繁的小操作，考虑增加缓冲区大小
   - 流式处理大型数据集，避免一次性加载全部数据

5. **错误处理**:
   - 捕获并妥善处理I/O异常（IOError, OSError）
   - 处理编码/解码错误，选择合适的错误处理策略
   - 验证文件操作的返回值，确保操作成功

6. **文件路径**:
   - 使用os.path模块处理跨平台文件路径
   - 避免硬编码文件路径，使用配置或参数
   - 检查文件和目录是否存在，在必要时创建它们

7. **并发安全**:
   - 注意I/O操作在多线程/多进程环境中的并发问题
   - 考虑使用锁或其他同步机制保护共享的I/O资源
   - 对于并发写入，考虑使用原子操作或临时文件

8. **内存使用**:
   - 对于非常大的文件，使用迭代器或生成器逐行处理
   - 使用BytesIO/StringIO处理内存中的临时数据
   - 避免在内存中保存过多的文件内容
"""

def best_practices():
    """最佳实践"""
    print("=== 11. 注意事项和最佳实践 ===")
    
    # 1. 资源管理最佳实践
    print("1. 资源管理最佳实践:")
    print("   - 始终使用with语句管理文件和流")
    print("   - 避免手动关闭，让上下文管理器处理")
    print("   - 在异常处理中确保资源被释放")
    print("""
    # 推荐的文件操作方式
    try:
        with io.open('file.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            # 处理内容
    except IOError as e:
        print(f"文件操作错误: {e}")
    except UnicodeDecodeError as e:
        print(f"编码错误: {e}")
    """)
    print()
    
    # 2. 性能优化建议
    print("2. 性能优化建议:")
    print("   - 大文件使用缓冲I/O")
    print("   - 流式处理大型数据集")
    print("   - 适当设置缓冲区大小")
    print("""
    # 大文件处理示例
    def process_large_file(file_path, chunk_size=1024*1024):  # 1MB块
        """高效处理大文件"""
        with io.open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                # 处理数据块
                process_chunk(chunk)
    """)
    print()
    
    # 3. 编码处理建议
    print("3. 编码处理建议:")
    print("   - 始终显式指定编码")
    print("   - 使用UTF-8作为默认编码")
    print("   - 处理未知编码数据时使用错误处理模式")
    print("""
    # 安全的文本读取
    def read_text_safely(file_path, encodings=['utf-8', 'latin-1', 'gbk']):
        """尝试多种编码读取文本文件"""
        for encoding in encodings:
            try:
                with io.open(file_path, 'r', encoding=encoding) as f:
                    return f.read()
            except UnicodeDecodeError:
                continue
        
        # 如果所有编码都失败，使用replace模式
        with io.open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            return f.read()
    """)
    print()
    
    # 4. 错误处理策略
    print("4. 错误处理策略:")
    print("   - 使用分层异常处理")
    print("   - 记录详细错误信息")
    print("   - 提供有用的错误消息")
    print("""
    # 健壮的文件复制函数
    def copy_file(source, destination):
        """安全地复制文件"""
        try:
            # 检查源文件是否存在
            if not os.path.exists(source):
                raise FileNotFoundError(f"源文件不存在: {source}")
            
            # 确保目标目录存在
            dest_dir = os.path.dirname(destination)
            if dest_dir and not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            # 二进制模式复制
            with io.open(source, 'rb') as src, io.open(destination, 'wb') as dst:
                # 使用缓冲复制
                while True:
                    data = src.read(io.DEFAULT_BUFFER_SIZE)
                    if not data:
                        break
                    dst.write(data)
            
            return True
            
        except IOError as e:
            print(f"I/O错误: {e}")
        except PermissionError as e:
            print(f"权限错误: {e}")
        except Exception as e:
            print(f"复制文件时发生错误: {e}")
        
        return False
    """)
    print()
    
    # 5. 并发I/O处理
    print("5. 并发I/O处理:")
    print("   - 使用线程池处理多个I/O操作")
    print("   - 避免在单线程中阻塞等待I/O")
    print("   - 使用异步I/O处理并发请求")
    print("""
    # 多文件并行读取示例
    import concurrent.futures
    
    def read_files_parallel(file_paths, max_workers=4):
        """并行读取多个文件"""
        results = {}
        
        def read_single_file(file_path):
            """读取单个文件"""
            try:
                with io.open(file_path, 'r', encoding='utf-8') as f:
                    return file_path, f.read()
            except Exception as e:
                return file_path, str(e)
        
        # 使用线程池并行读取
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_file = {executor.submit(read_single_file, file_path): file_path 
                             for file_path in file_paths}
            
            for future in concurrent.futures.as_completed(future_to_file):
                file_path = future_to_file[future]
                try:
                    file_path, content = future.result()
                    results[file_path] = content
                except Exception as e:
                    results[file_path] = str(e)
        
        return results
    """)

# 运行最佳实践演示
best_practices()

# 总结
print("\n=== 总结 ===")
print("io模块提供了Python中处理各种输入输出操作的统一接口。")
print("主要特点和功能：")
print("1. 提供文本和二进制两种基本流类型")
print("2. 支持内存中的I/O操作（StringIO、BytesIO）")
print("3. 提供缓冲机制以提高性能")
print("4. 支持自定义流的实现")
print("5. 提供丰富的错误处理机制")
print()
print("在实际应用中，io模块是处理各种数据输入输出的基础，")
print("特别适合需要统一处理不同来源数据的场景，如文件处理、")
print("网络通信、数据转换等。正确使用io模块可以提高程序的")
print("性能、可靠性和可维护性。")

# 运行完整演示
if __name__ == "__main__":
    print("Python io模块演示\n")
    print("请参考源代码中的详细示例和说明")