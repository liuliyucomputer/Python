# codecs模块 - 编解码器注册和使用
# 功能作用：提供编码器和解码器的注册和访问机制，支持各种字符编码的转换
# 使用情景：多语言文本处理、文件编码转换、网络协议编码处理、国际化应用开发
# 注意事项：处理不同编码时需注意编码声明的准确性，避免编码错误导致的数据损坏

import codecs
import io

# 模块概述
"""
codecs模块提供了编解码器注册和访问的标准接口，允许在不同的字符编码之间进行转换。
主要功能包括：
- 注册和检索编解码器
- 提供文件编码转换接口
- 实现各种字符编码的编码和解码
- 支持增量编码/解码操作
- 提供编码错误处理机制

codecs模块在国际化应用、多语言文本处理、文件编码转换等场景中非常有用。
"""

# 1. 基本编码和解码
print("=== 基本编码和解码 ===")

# 字符串编码为字节
test_str = "你好，Python!"

# UTF-8编码
utf8_bytes = codecs.encode(test_str, 'utf-8')
print(f"UTF-8编码: {utf8_bytes}")

# GBK编码
gbk_bytes = codecs.encode(test_str, 'gbk')
print(f"GBK编码: {gbk_bytes}")

# UTF-16编码
utf16_bytes = codecs.encode(test_str, 'utf-16')
print(f"UTF-16编码: {utf16_bytes}")
print()

# 字节解码为字符串
# UTF-8解码
utf8_decoded = codecs.decode(utf8_bytes, 'utf-8')
print(f"UTF-8解码: {utf8_decoded}")

# GBK解码
gbk_decoded = codecs.decode(gbk_bytes, 'gbk')
print(f"GBK解码: {gbk_decoded}")

# UTF-16解码
utf16_decoded = codecs.decode(utf16_bytes, 'utf-16')
print(f"UTF-16解码: {utf16_decoded}")
print()

# 2. 编码错误处理
print("=== 编码错误处理 ===")

# 模拟包含非法字符的字节序列
invalid_bytes = b'\xff\xfe\x00H\x00e\x00l\x00l\x00o\x00'  # 这是UTF-16编码的"Hello"

# 默认行为 - 解码错误会抛出异常
try:
    invalid_bytes.decode('utf-8')  # 尝试用UTF-8解码UTF-16数据
except UnicodeDecodeError as e:
    print(f"默认解码错误: {e}")

# 使用errors参数处理错误
# 'ignore': 忽略无法解码的字节
decoded_ignore = codecs.decode(invalid_bytes, 'utf-8', errors='ignore')
print(f"ignore模式解码: '{decoded_ignore}'")

# 'replace': 用替换字符替换无法解码的字节
decoded_replace = codecs.decode(invalid_bytes, 'utf-8', errors='replace')
print(f"replace模式解码: '{decoded_replace}'")

# 'surrogateescape': 将无法解码的字节转换为代理字符
decoded_surrogate = codecs.decode(invalid_bytes, 'utf-8', errors='surrogateescape')
print(f"surrogateescape模式解码: {repr(decoded_surrogate)}")

# 'backslashreplace': 用反斜杠转义序列替换无法解码的字节
decoded_backslash = codecs.decode(invalid_bytes, 'utf-8', errors='backslashreplace')
print(f"backslashreplace模式解码: '{decoded_backslash}'")

# 'namereplace': 用\N{...}命名替换无法解码的字节
decoded_name = codecs.decode(invalid_bytes, 'utf-8', errors='namereplace')
print(f"namereplace模式解码: '{decoded_name}'")
print()

# 3. 获取编码器和解码器信息
print("=== 获取编码器和解码器信息 ===")

# 获取编码器
def get_encoder_info(encoding):
    try:
        encoder = codecs.getencoder(encoding)
        print(f"编码器 '{encoding}': {encoder}")
    except LookupError as e:
        print(f"找不到编码器 '{encoding}': {e}")

# 获取解码器
def get_decoder_info(encoding):
    try:
        decoder = codecs.getdecoder(encoding)
        print(f"解码器 '{encoding}': {decoder}")
    except LookupError as e:
        print(f"找不到解码器 '{encoding}': {e}")

# 获取编码器和解码器
encodings = ['utf-8', 'gbk', 'ascii', 'latin-1', 'utf-16', 'utf-32']

print("编码器信息:")
for enc in encodings:
    get_encoder_info(enc)
print()

print("解码器信息:")
for enc in encodings:
    get_decoder_info(enc)
print()

# 4. 获取编解码器
print("=== 获取编解码器 ===")

# 获取编解码器对象
def get_codec_info(encoding):
    try:
        codec_info = codecs.lookup(encoding)
        print(f"\n编解码器 '{encoding}':")
        print(f"  名称: {codec_info.name}")
        print(f"  编码: {codec_info.encode}")
        print(f"  解码: {codec_info.decode}")
        print(f"  流读取: {codec_info.streamreader}")
        print(f"  流写入: {codec_info.streamwriter}")
        print(f"  增量编码: {codec_info.incrementalencoder}")
        print(f"  增量解码: {codec_info.incrementaldecoder}")
        print(f"  字符映射: {codec_info.charmap if hasattr(codec_info, 'charmap') else 'N/A'}")
        print(f"  输入编码: {codec_info.input_encoding if hasattr(codec_info, 'input_encoding') else 'N/A'}")
        print(f"  输出编码: {codec_info.output_encoding if hasattr(codec_info, 'output_encoding') else 'N/A'}")
        print(f"  错误处理: {codec_info.errors if hasattr(codec_info, 'errors') else 'N/A'}")
    except LookupError as e:
        print(f"找不到编解码器 '{encoding}': {e}")

# 获取常见编解码器信息
print("获取常见编解码器信息:")
get_codec_info('utf-8')
get_codec_info('ascii')

# 查找所有可用的编码
try:
    all_encodings = codecs.CodecRegistry().aliases
    print(f"\n已注册的编码别名数量: {len(all_encodings)}")
    # 打印部分常见编码别名
    common_aliases = {k: v for k, v in all_encodings.items() if k in ['utf-8', 'latin1', 'iso-8859-1', 'cp1252', 'gb2312', 'gbk', 'big5']}
    print("常见编码别名映射:")
    for alias, canonical in common_aliases.items():
        print(f"  {alias} -> {canonical}")
except Exception as e:
    print(f"获取编码别名时出错: {e}")
print()

# 5. 文件编码处理
print("=== 文件编码处理 ===")

# 演示如何使用codecs处理文件编码
def demonstrate_file_operations():
    """演示文件编码操作"""
    print("文件编码操作演示:")
    print("注: 以下是演示代码，不会实际创建或修改文件")
    
    # 写入UTF-8编码的文件
    print("\n写入UTF-8编码文件:")
    print("""
    with codecs.open('example_utf8.txt', 'w', encoding='utf-8') as f:
        f.write("你好，世界！Hello, World!\n")
        f.write("这是一个UTF-8编码的文件。\n")
    """)
    
    # 读取UTF-8编码的文件
    print("\n读取UTF-8编码文件:")
    print("""
    with codecs.open('example_utf8.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    """)
    
    # 写入GBK编码的文件
    print("\n写入GBK编码文件:")
    print("""
    with codecs.open('example_gbk.txt', 'w', encoding='gbk') as f:
        f.write("你好，世界！Hello, World!\n")
        f.write("这是一个GBK编码的文件。\n")
    """)
    
    # 读取GBK编码的文件
    print("\n读取GBK编码文件:")
    print("""
    with codecs.open('example_gbk.txt', 'r', encoding='gbk') as f:
        content = f.read()
        print(content)
    """)
    
    # 编码转换：GBK到UTF-8
    print("\n文件编码转换 - GBK到UTF-8:")
    print("""
    with codecs.open('example_gbk.txt', 'r', encoding='gbk') as f:
        content = f.read()
    
    with codecs.open('converted_utf8.txt', 'w', encoding='utf-8') as f:
        f.write(content)
    """)
    
    # 使用不同的错误处理模式打开文件
    print("\n使用不同的错误处理模式打开文件:")
    print("""
    # 忽略错误
    with codecs.open('corrupted_file.txt', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 替换错误字符
    with codecs.open('corrupted_file.txt', 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    """)

# 运行文件操作演示
demonstrate_file_operations()
print()

# 6. 流式编解码
print("=== 流式编解码 ===")

# 创建内存流并使用codecs进行编码处理
def demonstrate_stream_encoding():
    """演示流式编解码"""
    print("流式编解码演示:")
    
    # 创建内存缓冲区
    buffer = io.BytesIO()
    
    # 创建UTF-8编码的写入器
    writer = codecs.getwriter('utf-8')(buffer)
    
    # 写入数据
    writer.write("第一行：你好，Python!\n")
    writer.write("第二行：Codecs模块\n")
    writer.write("第三行：Stream Encoding\n")
    writer.flush()  # 确保所有数据都被写入
    
    # 获取缓冲区内容
    encoded_data = buffer.getvalue()
    print(f"编码后的字节数据: {encoded_data[:100]}...")
    print(f"字节数据长度: {len(encoded_data)} 字节")
    
    # 创建解码器读取器
    buffer.seek(0)
    reader = codecs.getreader('utf-8')(buffer)
    
    # 读取和解码数据
    decoded_content = reader.read()
    print(f"\n解码后的内容:\n{decoded_content}")
    
    # 测试行读取
    buffer.seek(0)
    reader = codecs.getreader('utf-8')(buffer)
    print("\n逐行读取:")
    for line in reader:
        print(f"行: {line.strip()}")

# 运行流式编解码演示
demonstrate_stream_encoding()
print()

# 7. 增量编解码
print("=== 增量编解码 ===")

# 增量编码示例
def demonstrate_incremental_encoding():
    """演示增量编码"""
    print("增量编码演示:")
    
    # 创建增量编码器
    incremental_encoder = codecs.getincrementalencoder('utf-8')()
    
    # 分块编码数据
    chunks = [
        "这是第一部分",
        "，这是第二部分",
        "，这是最后一部分。"
    ]
    
    encoded_chunks = []
    for chunk in chunks:
        # 编码当前块
        encoded_chunk = incremental_encoder.encode(chunk, final=False)
        print(f"编码块: {repr(chunk)} -> {repr(encoded_chunk)}")
        encoded_chunks.append(encoded_chunk)
    
    # 完成编码过程
    final_chunk = incremental_encoder.encode("", final=True)
    if final_chunk:
        print(f"最终块: {repr(final_chunk)}")
        encoded_chunks.append(final_chunk)
    
    # 组合所有编码块
    full_encoded = b''.join(encoded_chunks)
    print(f"完整编码结果: {full_encoded}")
    
    # 验证结果
    direct_encoded = ''.join(chunks).encode('utf-8')
    print(f"直接编码结果: {direct_encoded}")
    print(f"两种方法结果一致: {full_encoded == direct_encoded}")

# 增量解码示例
def demonstrate_incremental_decoding():
    """演示增量解码"""
    print("\n增量解码演示:")
    
    # 原始字符串
    original_str = "你好，Python! 这是一个增量解码的示例。"
    encoded_bytes = original_str.encode('utf-8')
    print(f"原始字符串: {original_str}")
    print(f"编码后字节: {encoded_bytes}")
    
    # 创建增量解码器
    incremental_decoder = codecs.getincrementaldecoder('utf-8')()
    
    # 模拟分块接收数据
    chunk_size = 6
    decoded_chunks = []
    
    for i in range(0, len(encoded_bytes), chunk_size):
        chunk = encoded_bytes[i:i+chunk_size]
        # 解码当前块
        decoded_chunk = incremental_decoder.decode(chunk, final=False)
        print(f"解码块 {i//chunk_size+1}: {repr(chunk)} -> '{decoded_chunk}'")
        decoded_chunks.append(decoded_chunk)
    
    # 完成解码过程
    final_chunk = incremental_decoder.decode(b"", final=True)
    if final_chunk:
        print(f"最终块: '{final_chunk}'")
        decoded_chunks.append(final_chunk)
    
    # 组合所有解码块
    full_decoded = ''.join(decoded_chunks)
    print(f"完整解码结果: '{full_decoded}'")
    print(f"解码结果正确: {full_decoded == original_str}")

# 运行增量编解码演示
demonstrate_incremental_encoding()
demonstrate_incremental_decoding()
print()

# 8. 实际应用示例
print("=== 实际应用示例 ===")

def practical_examples():
    """演示实际应用示例"""
    
    # 1. 文件编码检测器
    def detect_file_encoding(file_path):
        """检测文件可能的编码（简化版）"""
        print("\n1. 文件编码检测器:")
        print("注意：实际应用中，可以使用chardet或charset-normalizer库进行更准确的检测")
        print("""
        import codecs
        
        def detect_encoding(file_path):
            encodings = ['utf-8', 'utf-16', 'latin-1', 'gbk', 'big5']
            
            for encoding in encodings:
                try:
                    with codecs.open(file_path, 'r', encoding=encoding) as f:
                        # 读取部分内容进行测试
                        content = f.read(1000)
                    print(f"可能的编码: {encoding}")
                    return encoding
                except UnicodeDecodeError:
                    continue
            
            print("无法确定文件编码")
            return None
        """)
    
    # 2. 批量文件编码转换
    def batch_convert_encoding(source_dir, target_dir, from_encoding, to_encoding):
        """批量转换文件编码"""
        print("\n2. 批量文件编码转换:")
        print("""
        import os
        import codecs
        
        def convert_file_encoding(source_path, target_path, from_enc, to_enc):
            """转换单个文件的编码"""
            try:
                with codecs.open(source_path, 'r', encoding=from_enc) as f:
                    content = f.read()
                    
                with codecs.open(target_path, 'w', encoding=to_enc) as f:
                    f.write(content)
                    
                print(f"已转换: {source_path} -> {target_path}")
                return True
            except Exception as e:
                print(f"转换失败 {source_path}: {e}")
                return False
        
        def batch_convert(source_dir, target_dir, from_enc, to_enc, extensions=['.txt', '.py', '.csv']):
            """批量转换目录中文件的编码"""
            # 确保目标目录存在
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            
            success_count = 0
            fail_count = 0
            
            # 遍历源目录中的所有文件
            for root, dirs, files in os.walk(source_dir):
                # 创建对应的目标子目录
                rel_path = os.path.relpath(root, source_dir)
                if rel_path != '.':
                    target_root = os.path.join(target_dir, rel_path)
                else:
                    target_root = target_dir
                    
                if not os.path.exists(target_root):
                    os.makedirs(target_root)
                
                # 处理每个文件
                for file in files:
                    # 检查文件扩展名
                    _, ext = os.path.splitext(file)
                    if ext.lower() in extensions:
                        source_path = os.path.join(root, file)
                        target_path = os.path.join(target_root, file)
                        
                        if convert_file_encoding(source_path, target_path, from_enc, to_enc):
                            success_count += 1
                        else:
                            fail_count += 1
            
            print(f"转换完成 - 成功: {success_count}, 失败: {fail_count}")
        """)
    
    # 3. 多语言文本处理
    def multilingual_text_processing():
        """多语言文本处理"""
        print("\n3. 多语言文本处理:")
        
        # 不同语言的文本
        texts = {
            '中文': "你好，世界！",
            '英文': "Hello, World!",
            '日文': "こんにちは、世界！",
            '韩文': "안녕하세요, 세계!",
            '俄文': "Привет, мир!",
            '阿拉伯文': "مرحبا بالعالم!",
            '泰文': "สวัสดีชาวโลก!"
        }
        
        # 测试不同编码的支持情况
        encodings_to_test = ['utf-8', 'utf-16', 'latin-1', 'gbk']
        
        print("各种语言在不同编码下的支持情况:")
        for lang, text in texts.items():
            print(f"\n{lang}:")
            for encoding in encodings_to_test:
                try:
                    # 尝试编码
                    encoded = codecs.encode(text, encoding)
                    # 尝试解码
                    decoded = codecs.decode(encoded, encoding)
                    success = decoded == text
                    print(f"  {encoding}: {'支持' if success else '不支持'}")
                except Exception as e:
                    print(f"  {encoding}: 不支持 ({str(e)[:30]}...)")
    
    # 4. 自定义编解码器注册
    def custom_codec_registration():
        """自定义编解码器注册"""
        print("\n4. 自定义编解码器注册:")
        print("""
        import codecs
        
        # 简单的ROT13编码实现
        def rot13_encode(text, errors='strict'):
            result = []
            for char in text:
                code = ord(char)
                if 65 <= code <= 90:  # A-Z
                    result.append(chr(65 + (code - 65 + 13) % 26))
                elif 97 <= code <= 122:  # a-z
                    result.append(chr(97 + (code - 97 + 13) % 26))
                else:
                    result.append(char)
            return ''.join(result), len(text)
        
        def rot13_decode(text, errors='strict'):
            # ROT13是自反的，解码和编码使用相同的逻辑
            return rot13_encode(text, errors)
        
        # 创建编解码器注册信息
        def rot13_search_function(encoding):
            if encoding.lower() == 'rot13':
                return codecs.CodecInfo(
                    name='rot13',
                    encode=rot13_encode,
                    decode=rot13_decode,
                )
            return None
        
        # 注册自定义编解码器
        codecs.register(rot13_search_function)
        
        # 测试自定义编解码器
        test_text = "Hello, World! 这是一个测试。ABCdef123"
        encoded = codecs.encode(test_text, 'rot13')
        decoded = codecs.decode(encoded, 'rot13')
        
        print(f"原始文本: {test_text}")
        print(f"ROT13编码: {encoded}")
        print(f"ROT13解码: {decoded}")
        print(f"解码正确: {decoded == test_text}")
        """)
    
    # 5. 处理BOM (Byte Order Mark)
    def handle_bom():
        """处理字节顺序标记(BOM)"""
        print("\n5. 处理BOM (Byte Order Mark):")
        
        # BOM定义
        BOMS = {
            'utf-8-sig': b'\xef\xbb\xbf',
            'utf-16-be': b'\xfe\xff',
            'utf-16-le': b'\xff\xfe',
            'utf-32-be': b'\x00\x00\xfe\xff',
            'utf-32-le': b'\xff\xfe\x00\x00'
        }
        
        print("常见的BOM标记:")
        for encoding, bom in BOMS.items():
            print(f"  {encoding}: {bom.hex()}")
        
        print("\nBOM处理示例:")
        print("""
        # 写入带BOM的UTF-8文件
        with codecs.open('utf8_with_bom.txt', 'w', encoding='utf-8-sig') as f:
            f.write("这是带BOM的UTF-8文件\n")
            f.write("BOM将帮助程序识别文件编码\n")
        
        # 读取带BOM的文件
        with codecs.open('utf8_with_bom.txt', 'r', encoding='utf-8-sig') as f:
            content = f.read()
            print(content)
        
        # 手动检测和处理BOM
        def read_file_with_bom_detection(file_path):
            with open(file_path, 'rb') as f:
                raw = f.read(4)  # 读取前4个字节检查BOM
                
                # 检测BOM
                if raw.startswith(b'\xef\xbb\xbf'):
                    encoding = 'utf-8'
                    content = raw[3:]
                elif raw.startswith(b'\xfe\xff'):
                    encoding = 'utf-16-be'
                    content = raw[2:]
                elif raw.startswith(b'\xff\xfe'):
                    encoding = 'utf-16-le'
                    content = raw[2:]
                elif raw.startswith(b'\x00\x00\xfe\xff'):
                    encoding = 'utf-32-be'
                    content = raw[4:]
                elif raw.startswith(b'\xff\xfe\x00\x00'):
                    encoding = 'utf-32-le'
                    content = raw[4:]
                else:
                    encoding = 'utf-8'  # 默认假设为UTF-8
                    content = raw
                    
                # 读取剩余内容
                content += f.read()
                
            # 解码内容
            return content.decode(encoding)
        """)
    
    # 6. 编码转换实用函数
    def encoding_utils():
        """编码转换实用函数"""
        print("\n6. 编码转换实用函数:")
        
        print("编码转换工具函数示例:")
        
        # 字符串编码转换函数
        def convert_string_encoding(text, from_encoding, to_encoding):
            """转换字符串的编码表示"""
            # 首先解码为Unicode
            unicode_text = text if isinstance(text, str) else text.decode(from_encoding)
            # 然后编码为目标编码
            return unicode_text.encode(to_encoding)
        
        # 测试编码转换
        test_str = "测试编码转换"
        print(f"原始字符串: {test_str}")
        
        # UTF-8 到 GBK
        utf8_bytes = test_str.encode('utf-8')
        gbk_bytes = convert_string_encoding(utf8_bytes, 'utf-8', 'gbk')
        print(f"UTF-8 -> GBK: {gbk_bytes}")
        
        # GBK 到 UTF-16
        utf16_bytes = convert_string_encoding(gbk_bytes, 'gbk', 'utf-16')
        print(f"GBK -> UTF-16: {utf16_bytes}")
        
        # 解码回字符串验证
        result_str = utf16_bytes.decode('utf-16')
        print(f"最终解码结果: {result_str}")
        print(f"转换成功: {result_str == test_str}")
    
    # 运行实用示例
    detect_file_encoding("example.txt")
    batch_convert_encoding("source_dir", "target_dir", "gbk", "utf-8")
    multilingual_text_processing()
    custom_codec_registration()
    handle_bom()
    encoding_utils()

# 运行实际应用示例
practical_examples()
print()

# 9. 高级用法和技巧
print("=== 高级用法和技巧 ===")

def advanced_techniques():
    """高级用法和技巧"""
    
    # 1. 上下文管理器和编解码器
    print("1. 上下文管理器和编解码器:")
    print("""
    # 创建自定义编码的上下文管理器
    class EncodedFile:
        def __init__(self, file_path, mode, from_encoding='utf-8', to_encoding='utf-8'):
            self.file_path = file_path
            self.mode = mode
            self.from_encoding = from_encoding
            self.to_encoding = to_encoding
            self.file = None
        
        def __enter__(self):
            if 'r' in self.mode:
                self.file = codecs.open(self.file_path, self.mode, encoding=self.from_encoding)
            elif 'w' in self.mode or 'a' in self.mode:
                self.file = codecs.open(self.file_path, self.mode, encoding=self.to_encoding)
            return self.file
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if self.file:
                self.file.close()
            return False
    
    # 使用示例
    # with EncodedFile('example.txt', 'r', from_encoding='gbk') as f:
    #     content = f.read()
    """)
    
    # 2. 编码和解码过滤器
    print("\n2. 编码和解码过滤器:")
    
    class TextEncodingFilter:
        """文本编码过滤器"""
        
        def __init__(self, from_encoding='utf-8', to_encoding='utf-8', errors='replace'):
            self.from_encoding = from_encoding
            self.to_encoding = to_encoding
            self.errors = errors
        
        def filter_text(self, text):
            """过滤文本，执行编码转换"""
            if isinstance(text, bytes):
                # 先解码
                decoded = text.decode(self.from_encoding, errors=self.errors)
                # 再编码
                return decoded.encode(self.to_encoding, errors=self.errors)
            elif isinstance(text, str):
                # 字符串直接编码
                return text.encode(self.to_encoding, errors=self.errors)
            else:
                raise TypeError("输入必须是字符串或字节序列")
        
        def filter_file(self, input_path, output_path):
            """过滤文件内容"""
            try:
                with open(input_path, 'rb') as f:
                    content = f.read()
                
                filtered = self.filter_text(content)
                
                with open(output_path, 'wb') as f:
                    f.write(filtered)
                
                return True
            except Exception as e:
                print(f"过滤文件时出错: {e}")
                return False
    
    # 测试编码过滤器
    filter_utf8_to_gbk = TextEncodingFilter(from_encoding='utf-8', to_encoding='gbk')
    test_bytes = "测试过滤器".encode('utf-8')
    filtered_bytes = filter_utf8_to_gbk.filter_text(test_bytes)
    print(f"原始字节 (UTF-8): {test_bytes}")
    print(f"过滤后字节 (GBK): {filtered_bytes}")
    
    # 3. 增量编解码器的高级应用
    print("\n3. 增量编解码器的高级应用:")
    
    class StreamProcessor:
        """流式处理器，使用增量编解码器处理数据"""
        
        def __init__(self, input_encoding='utf-8', output_encoding='utf-8'):
            self.input_encoding = input_encoding
            self.output_encoding = output_encoding
            self.decoder = codecs.getincrementaldecoder(input_encoding)()
            self.encoder = codecs.getincrementalencoder(output_encoding)()
        
        def process_chunk(self, chunk, final=False):
            """处理数据块"""
            # 解码输入
            decoded = self.decoder.decode(chunk, final=final)
            
            # 在这里可以添加文本处理逻辑
            # processed = some_text_processing(decoded)
            processed = decoded  # 简单示例，不做处理
            
            # 编码输出
            encoded = self.encoder.encode(processed, final=final)
            
            return encoded
        
        def reset(self):
            """重置处理器状态"""
            self.decoder = codecs.getincrementaldecoder(self.input_encoding)()
            self.encoder = codecs.getincrementalencoder(self.output_encoding)()
    
    # 测试流式处理器
    processor = StreamProcessor(input_encoding='utf-8', output_encoding='utf-16')
    
    chunks = [
        "这是第一块数据",
        "，这是第二块数据",
        "，这是最后一块数据。"
    ]
    
    print("流式处理数据块:")
    for i, chunk in enumerate(chunks):
        final = (i == len(chunks) - 1)
        result = processor.process_chunk(chunk.encode('utf-8'), final=final)
        print(f"块 {i+1} 处理结果: {result}")
    
    # 4. 编码检测和处理策略
    print("\n4. 编码检测和处理策略:")
    
    class EncodingHandler:
        """编码处理器，提供编码检测和处理功能"""
        
        # 常见编码，按优先级排序
        COMMON_ENCODINGS = [
            'utf-8-sig',  # 带BOM的UTF-8
            'utf-8',
            'latin-1',    # ISO-8859-1
            'cp1252',     # Windows-1252
            'utf-16',
            'utf-16-le',
            'utf-16-be',
            'gbk',
            'gb2312',
            'big5'
        ]
        
        @staticmethod
        def try_decode(data, encoding, errors='strict'):
            """尝试使用指定编码解码数据"""
            try:
                return data.decode(encoding, errors=errors), True
            except (UnicodeDecodeError, LookupError):
                return None, False
        
        @staticmethod
        def detect_encoding(data, encodings=None, errors='strict'):
            """尝试检测数据的编码"""
            if encodings is None:
                encodings = EncodingHandler.COMMON_ENCODINGS
            
            # 快速检查BOM
            if data.startswith(b'\xef\xbb\xbf'):
                return 'utf-8'
            elif data.startswith(b'\xfe\xff'):
                return 'utf-16-be'
            elif data.startswith(b'\xff\xfe'):
                return 'utf-16-le'
            
            # 尝试不同的编码
            for encoding in encodings:
                result, success = EncodingHandler.try_decode(data, encoding, errors)
                if success:
                    return encoding
            
            return None
        
        @staticmethod
        def safe_decode(data, default_encoding='utf-8', fallback_encoding='latin-1'):
            """安全地解码数据，尝试多种编码"""
            # 已经是字符串
            if isinstance(data, str):
                return data
            
            # 尝试检测编码
            encoding = EncodingHandler.detect_encoding(data)
            
            if encoding:
                try:
                    return data.decode(encoding)
                except UnicodeDecodeError:
                    pass
            
            # 尝试默认编码
            result, success = EncodingHandler.try_decode(data, default_encoding)
            if success:
                return result
            
            # 最后使用fallback编码（latin-1几乎可以解码任何字节序列）
            return data.decode(fallback_encoding)
    
    # 测试编码检测
    test_data = {
        'utf-8': "你好，世界！".encode('utf-8'),
        'gbk': "你好，世界！".encode('gbk'),
        'latin-1': "Hello, World! ".encode('latin-1') + b'\xff\xfe\x00'
    }
    
    print("编码检测测试:")
    for expected, data in test_data.items():
        detected = EncodingHandler.detect_encoding(data)
        print(f"  期望: {expected}, 检测: {detected}, 结果: {'正确' if detected == expected else '错误'}")
    
    # 测试安全解码
    print("安全解码测试:")
    for name, data in test_data.items():
        decoded = EncodingHandler.safe_decode(data)
        print(f"  {name}: {decoded[:20]}..." if len(decoded) > 20 else f"  {name}: {decoded}")

# 运行高级用法演示
advanced_techniques()
print()

# 10. 注意事项和最佳实践
"""
1. **编码选择**：
   - 优先使用UTF-8作为默认编码，它支持所有Unicode字符且兼容性好
   - 在需要处理特定语言时，考虑使用该语言常用的编码（如中文使用GBK/GB2312）
   - 避免使用ASCII编码处理非英语文本

2. **错误处理策略**：
   - 读取不可信来源的数据时，使用适当的错误处理模式（如'replace'）
   - 写入数据时，通常应使用'strict'模式确保数据完整性
   - 了解各种错误处理模式的行为差异，选择最适合的策略

3. **BOM处理**：
   - UTF-8文件通常不需要BOM，但某些应用可能依赖它识别编码
   - 使用'utf-8-sig'编码自动处理UTF-8 BOM
   - 读写UTF-16/UTF-32文件时，注意字节序问题

4. **性能考虑**：
   - 对于频繁的编码转换操作，缓存编码结果
   - 处理大文件时，使用流式处理而不是一次性加载
   - 使用增量编解码器处理网络流或大型数据流

5. **跨平台兼容性**：
   - 注意不同操作系统的默认编码差异
   - Windows常用cp1252，macOS和Linux常用UTF-8
   - 明确指定文件编码，不要依赖默认值

6. **编码声明**：
   - Python源文件中使用`# -*- coding: utf-8 -*-`声明文件编码
   - 在处理配置文件或数据交换格式时，包含编码信息
   - Web应用中设置正确的Content-Type头，包含charset参数

7. **调试技巧**：
   - 遇到编码问题时，检查数据的十六进制表示
   - 使用repr()函数查看字符串的内部表示
   - 检查文件的BOM标记
   - 使用专门的工具（如chardet）检测未知编码

8. **数据完整性**：
   - 在编码转换过程中，注意保留所有字符信息
   - 使用错误处理模式时，记录替换或忽略的字符
   - 定期验证编码转换结果的正确性
"""

def best_practices():
    """最佳实践"""
    print("=== 最佳实践 ===")
    
    # 1. 编码使用建议
    print("1. 编码使用建议:")
    print("   - 新项目始终使用UTF-8作为默认编码")
    print("   - 为Python源文件添加编码声明")
    print("   - 在文件I/O操作中明确指定编码")
    print("   - 使用codecs.open()而不是open()以获得更好的编码支持")
    print()
    
    # 2. 文件处理最佳实践
    print("2. 文件处理最佳实践:")
    print("""
    # 推荐的文件读取方式
    def read_text_file(file_path, encoding='utf-8', fallback_encoding='latin-1'):
        """安全地读取文本文件"""
        try:
            with codecs.open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except UnicodeDecodeError:
            # 尝试fallback编码
            with codecs.open(file_path, 'r', encoding=fallback_encoding) as f:
                return f.read()
    
    # 推荐的文件写入方式
    def write_text_file(file_path, content, encoding='utf-8'):
        """安全地写入文本文件"""
        with codecs.open(file_path, 'w', encoding=encoding) as f:
            f.write(content)
    """)
    print()
    
    # 3. 字符串和字节处理
    print("3. 字符串和字节处理:")
    print("""
    # 字符串到字节的安全转换
    def str_to_bytes(text, encoding='utf-8', errors='strict'):
        """将字符串转换为字节"""
        if isinstance(text, bytes):
            return text
        return text.encode(encoding, errors=errors)
    
    # 字节到字符串的安全转换
    def bytes_to_str(data, encoding='utf-8', errors='replace'):
        """将字节转换为字符串"""
        if isinstance(data, str):
            return data
        return data.decode(encoding, errors=errors)
    """)
    print()
    
    # 4. 性能优化示例
    print("4. 性能优化示例:")
    print("""
    import time
    
    # 测试不同编码方式的性能
    def benchmark_encoding():
        text = "这是一个长文本，用于测试编码性能。" * 1000
        iterations = 1000
        
        # 直接编码
        start = time.time()
        for _ in range(iterations):
            b = text.encode('utf-8')
        direct_time = time.time() - start
        print(f"直接编码: {direct_time:.6f}秒")
        
        # 使用codecs.encode
        start = time.time()
        for _ in range(iterations):
            b = codecs.encode(text, 'utf-8')
        codecs_time = time.time() - start
        print(f"codecs.encode: {codecs_time:.6f}秒")
        
        # 获取编码器后使用
        encoder = codecs.getencoder('utf-8')
        start = time.time()
        for _ in range(iterations):
            b, _ = encoder(text)
        encoder_time = time.time() - start
        print(f"使用编码器: {encoder_time:.6f}秒")
    """)
    print()
    
    # 5. 调试编码问题
    print("5. 调试编码问题:")
    print("""
    def debug_encoding_issue(data, max_bytes=50):
        """调试编码问题的辅助函数"""
        print(f"数据类型: {type(data)}")
        
        if isinstance(data, bytes):
            print(f"字节长度: {len(data)}")
            print(f"前{max_bytes}字节(十六进制): {data[:max_bytes].hex()}")
            
            # 检查常见BOM
            if data.startswith(b'\xef\xbb\xbf'):
                print("检测到UTF-8 BOM")
            elif data.startswith(b'\xfe\xff'):
                print("检测到UTF-16 BE BOM")
            elif data.startswith(b'\xff\xfe'):
                print("检测到UTF-16 LE BOM")
            
            # 尝试解码为常见编码
            for encoding in ['utf-8', 'latin-1', 'cp1252', 'gbk']:
                try:
                    decoded = data[:max_bytes].decode(encoding)
                    print(f"尝试{encoding}解码: {repr(decoded)}")
                except UnicodeDecodeError:
                    print(f"{encoding}解码失败")
        
        elif isinstance(data, str):
            print(f"字符串长度: {len(data)}")
            print(f"字符串表示: {repr(data[:50])}")
            
            # 检查非ASCII字符
            non_ascii = [c for c in data if ord(c) > 127]
            print(f"非ASCII字符数量: {len(non_ascii)}")
            if non_ascii:
                print(f"部分非ASCII字符: {[repr(c) for c in non_ascii[:10]]}")
    """)
    print()

# 运行最佳实践演示
best_practices()

# 总结
print("\n=== 总结 ===")
print("codecs模块是Python中处理字符编码的核心模块，它提供了丰富的功能：")
print("1. 支持多种字符编码的编码和解码操作")
print("2. 提供文件编码处理接口")
print("3. 支持增量编解码操作")
print("4. 提供灵活的错误处理机制")
print("5. 支持自定义编解码器的注册")
print()
print("在处理国际化应用、多语言文本、文件格式转换等场景中，")
print("正确使用codecs模块可以有效避免编码相关的问题，")
print("确保文本数据在不同系统和应用程序之间的正确传递。")

# 运行完整演示
if __name__ == "__main__":
    print("Python codecs模块演示\n")
    print("请参考源代码中的详细示例和说明")