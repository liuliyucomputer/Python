# struct模块 - 二进制数据打包和解包
# 功能作用：用于将Python数据类型与C结构体表示进行转换，支持二进制数据的打包和解包
# 使用情景：网络通信、文件格式解析、二进制数据处理、系统调用接口
# 注意事项：处理二进制数据时需要特别注意字节序和数据对齐问题

import struct
import binascii

# 模块概述
"""
struct模块提供了在Python值和表示为Python字节对象的C结构体之间转换的函数。
主要功能包括：
- 打包：将Python对象转换为字节序列
- 解包：将字节序列转换回Python对象
- 大小计算：计算特定格式结构体的大小
- 字节序控制：支持不同的字节序（大端序、小端序、主机字节序）

struct模块在处理二进制文件格式、网络协议、底层系统交互等场景中非常有用。
"""

# 1. 基本的打包和解包
print("=== 基本的打包和解包 ===")

# 格式字符说明：
# i: 整数 (int)
# f: 浮点数 (float)
# s: 字符串 (string)
# b: 有符号字节 (signed byte)
# B: 无符号字节 (unsigned byte)
# h: 短整数 (short)
# H: 无符号短整数 (unsigned short)
# l: 长整数 (long)
# L: 无符号长整数 (unsigned long)
# d: 双精度浮点数 (double)
# q: 长整型 (long long)
# Q: 无符号长整型 (unsigned long long)

# 基本打包
packed_data = struct.pack('ifh', 123, 45.67, 89)
print(f"打包数据 (i,f,h): {binascii.hexlify(packed_data)}")
print(f"打包后字节数: {len(packed_data)}")
print()

# 基本解包
unpacked_data = struct.unpack('ifh', packed_data)
print(f"解包数据: {unpacked_data}")
print(f"解包数据类型: {[type(x) for x in unpacked_data]}")
print()

# 2. 字节序控制
print("=== 字节序控制 ===")

# 字节序前缀：
# @: 本机字节序，本机大小，本机对齐（默认）
# =: 本机字节序，标准大小，无对齐
# <: 小端序，标准大小，无对齐
# >: 大端序，标准大小，无对齐
# !: 网络字节序（大端序），标准大小，无对齐

# 测试不同字节序
value = 0x12345678

# 小端序
packed_little = struct.pack('<I', value)
print(f"小端序 (<) 打包: {binascii.hexlify(packed_little)}")

# 大端序
packed_big = struct.pack('>I', value)
print(f"大端序 (>) 打包: {binascii.hexlify(packed_big)}")

# 网络字节序（等同于大端序）
packed_network = struct.pack('!I', value)
print(f"网络字节序 (!) 打包: {binascii.hexlify(packed_network)}")

# 本机字节序
packed_native = struct.pack('@I', value)
print(f"本机字节序 (@) 打包: {binascii.hexlify(packed_native)}")
print()

# 验证解包
print(f"小端序解包: {struct.unpack('<I', packed_little)[0]:#x}")
print(f"大端序解包: {struct.unpack('>I', packed_big)[0]:#x}")
print(f"网络字节序解包: {struct.unpack('!I', packed_network)[0]:#x}")
print(f"本机字节序解包: {struct.unpack('@I', packed_native)[0]:#x}")
print()

# 3. 字符串和字节的打包
print("=== 字符串和字节的打包 ===")

# 打包固定长度的字符串
test_string = "Hello"
packed_string = struct.pack('5s', test_string.encode('utf-8'))
print(f"字符串打包 (5s): {binascii.hexlify(packed_string)}")

# 解包字符串
unpacked_string = struct.unpack('5s', packed_string)[0].decode('utf-8')
print(f"字符串解包: {unpacked_string}")
print()

# 变长字符串的处理
# 方法1: 先发送长度，再发送字符串
string_data = "Python struct module"
string_bytes = string_data.encode('utf-8')

# 打包字符串长度和内容
packed_length = struct.pack('I', len(string_bytes))
packed_vlen_string = packed_length + string_bytes

print(f"变长字符串打包前: {string_data}")
print(f"字符串长度: {len(string_bytes)}")
print(f"打包后的长度数据: {binascii.hexlify(packed_length)}")
print(f"打包后的总字节数: {len(packed_vlen_string)}")

# 解包变长字符串
unpacked_length = struct.unpack('I', packed_vlen_string[:4])[0]
unpacked_vlen_string = packed_vlen_string[4:4+unpacked_length].decode('utf-8')
print(f"解包后的变长字符串: {unpacked_vlen_string}")
print()

# 4. 结构体大小计算
print("=== 结构体大小计算 ===")

# 使用calcsize计算结构体大小
size1 = struct.calcsize('ifh')
size2 = struct.calcsize('<ifh')
size3 = struct.calcsize('>ifh')
size4 = struct.calcsize('@ifh')

def format_size_info(format_str, size):
    return f"格式 '{format_str}': {size} 字节"

print(format_size_info('ifh', size1))
print(format_size_info('<ifh', size2))
print(format_size_info('>ifh', size3))
print(format_size_info('@ifh', size4))
print()

# 5. 高级打包功能
print("=== 高级打包功能 ===")

# 使用pack_into直接打包到预分配的缓冲区
import array
buf = array.array('B', b'\x00' * 100)  # 创建一个100字节的缓冲区
pos = 10  # 起始位置

# 将数据打包到缓冲区
struct.pack_into('ifh', buf, pos, 123, 45.67, 89)

# 从缓冲区解包
data_from_buf = struct.unpack_from('ifh', buf, pos)
print(f"从缓冲区解包的数据: {data_from_buf}")
print()

# 6. 复杂结构体示例
print("=== 复杂结构体示例 ===")

# 定义一个包含多种数据类型的结构体
person_format = 'I 10s f B'
person_data = (12345, b'Alice', 36.5, 1)

# 打包结构体
packed_person = struct.pack(person_format, *person_data)
print(f"打包后的人员数据: {binascii.hexlify(packed_person)}")

# 解包结构体
unpacked_person = struct.unpack(person_format, packed_person)
print(f"解包后的人员数据: ID={unpacked_person[0]}, "
      f"Name={unpacked_person[1].decode('utf-8').rstrip('\x00')}, "
      f"Temperature={unpacked_person[2]}, "
      f"Status={unpacked_person[3]}")
print()

# 7. 实际应用示例
def practical_examples():
    """演示实际应用示例"""
    print("=== 实际应用示例 ===")
    
    # 1. 模拟网络协议数据包
    def create_network_packet(seq_num, payload):
        """创建一个简单的网络数据包"""
        # 数据包格式: 序列号(4字节) + 负载长度(4字节) + 负载(n字节)
        payload_bytes = payload.encode('utf-8')
        packet = struct.pack('!II', seq_num, len(payload_bytes)) + payload_bytes
        return packet
    
    def parse_network_packet(packet):
        """解析网络数据包"""
        # 解包头部
        seq_num, payload_len = struct.unpack('!II', packet[:8])
        # 提取负载
        payload = packet[8:8+payload_len].decode('utf-8')
        return seq_num, payload
    
    # 创建并解析数据包
    packet = create_network_packet(123, "Hello, Network!")
    print(f"创建的数据包 (十六进制): {binascii.hexlify(packet)}")
    
    parsed_seq, parsed_payload = parse_network_packet(packet)
    print(f"解析的数据包: 序列号={parsed_seq}, 负载='{parsed_payload}'")
    print()
    
    # 2. 读取二进制文件头
    def parse_wav_header(header_data):
        """解析WAV文件头（简化版）"""
        # WAV文件头格式（部分字段）
        format_size = 16  # 简化的格式大小
        
        if len(header_data) < format_size + 12:  # RIFF头 + 格式块
            return None
        
        # 解析RIFF头
        riff_id, file_size, wave_id = struct.unpack('4sI4s', header_data[:12])
        
        if riff_id != b'RIFF' or wave_id != b'WAVE':
            return None
        
        # 解析格式块
        fmt_id, fmt_chunk_size, audio_format, num_channels, sample_rate = struct.unpack(
            '4sIHHH', header_data[12:28]
        )
        
        if fmt_id != b'fmt ':
            return None
        
        return {
            'file_size': file_size,
            'audio_format': audio_format,
            'num_channels': num_channels,
            'sample_rate': sample_rate
        }
    
    # 创建一个模拟的WAV文件头
    mock_wav_header = (
        b'RIFF' +  # RIFF标识符
        struct.pack('<I', 12345) +  # 文件大小
        b'WAVE' +  # WAVE标识符
        b'fmt ' +  # 格式块标识符
        struct.pack('<IHHH', 16, 1, 2, 44100)  # 格式块大小, 音频格式, 声道数, 采样率
    )
    
    wav_info = parse_wav_header(mock_wav_header)
    print("模拟WAV文件头解析结果:")
    if wav_info:
        for key, value in wav_info.items():
            print(f"  {key}: {value}")
    print()
    
    # 3. 二进制数据序列化和反序列化
    class BinarySerializable:
        """可二进制序列化的基类"""
        
        @classmethod
        def from_binary(cls, binary_data):
            """从二进制数据创建对象"""
            raise NotImplementedError
        
        def to_binary(self):
            """将对象转换为二进制数据"""
            raise NotImplementedError
    
    class Point(BinarySerializable):
        """二维点类"""
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        @classmethod
        def from_binary(cls, binary_data):
            x, y = struct.unpack('dd', binary_data)
            return cls(x, y)
        
        def to_binary(self):
            return struct.pack('dd', self.x, self.y)
        
        def __repr__(self):
            return f"Point({self.x}, {self.y})"
    
    class Rectangle(BinarySerializable):
        """矩形类"""
        
        def __init__(self, origin, width, height):
            self.origin = origin  # Point对象
            self.width = width
            self.height = height
        
        @classmethod
        def from_binary(cls, binary_data):
            # 先解析原点
            origin = Point.from_binary(binary_data[:16])  # 2个双精度浮点数 = 16字节
            # 解析宽度和高度
            width, height = struct.unpack('dd', binary_data[16:32])
            return cls(origin, width, height)
        
        def to_binary(self):
            # 组合原点的二进制数据和宽高的二进制数据
            return self.origin.to_binary() + struct.pack('dd', self.width, self.height)
        
        def __repr__(self):
            return f"Rectangle(origin={self.origin}, width={self.width}, height={self.height})"
    
    # 测试序列化和反序列化
    rect = Rectangle(Point(10.5, 20.75), 100.0, 50.0)
    print(f"原始矩形对象: {rect}")
    
    # 序列化为二进制
    binary_rect = rect.to_binary()
    print(f"序列化后的二进制数据长度: {len(binary_rect)} 字节")
    print(f"十六进制表示: {binascii.hexlify(binary_rect)[:60]}...")  # 只显示前60个字符
    
    # 反序列化
    restored_rect = Rectangle.from_binary(binary_rect)
    print(f"反序列化后的矩形对象: {restored_rect}")
    print()
    
    # 4. 实现简单的二进制协议
    class BinaryProtocol:
        """简单的二进制协议实现"""
        
        # 消息类型
        MSG_TYPE_DATA = 0
        MSG_TYPE_ACK = 1
        MSG_TYPE_ERROR = 2
        
        # 头部格式: 消息类型(1字节) + 消息ID(2字节) + 负载长度(2字节)
        HEADER_FORMAT = 'BHI'
        HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
        
        @staticmethod
        def create_message(msg_type, msg_id, payload=b''):
            """创建消息"""
            # 打包头部
            header = struct.pack(BinaryProtocol.HEADER_FORMAT, msg_type, msg_id, len(payload))
            # 返回头部 + 负载
            return header + payload
        
        @staticmethod
        def parse_message(data):
            """解析消息"""
            if len(data) < BinaryProtocol.HEADER_SIZE:
                return None, data  # 数据不足，返回剩余数据
            
            # 解析头部
            msg_type, msg_id, payload_len = struct.unpack(BinaryProtocol.HEADER_FORMAT, data[:BinaryProtocol.HEADER_SIZE])
            
            # 检查负载是否完整
            total_size = BinaryProtocol.HEADER_SIZE + payload_len
            if len(data) < total_size:
                return None, data  # 数据不足，返回剩余数据
            
            # 提取负载
            payload = data[BinaryProtocol.HEADER_SIZE:total_size]
            remaining_data = data[total_size:]
            
            return (msg_type, msg_id, payload), remaining_data
        
        @staticmethod
        def serialize_data(data_dict):
            """序列化字典数据"""
            # 这里使用简单的格式：键长度(1字节) + 键 + 值长度(2字节) + 值
            serialized = b''
            
            for key, value in data_dict.items():
                # 处理键
                key_bytes = key.encode('utf-8')
                if len(key_bytes) > 255:  # 键长度限制为255
                    key_bytes = key_bytes[:255]
                serialized += struct.pack('B', len(key_bytes)) + key_bytes
                
                # 处理值
                if isinstance(value, str):
                    value_bytes = value.encode('utf-8')
                    serialized += struct.pack('H', len(value_bytes)) + value_bytes
                elif isinstance(value, int):
                    value_bytes = struct.pack('i', value)
                    serialized += struct.pack('H', 4) + value_bytes
                elif isinstance(value, float):
                    value_bytes = struct.pack('d', value)
                    serialized += struct.pack('H', 8) + value_bytes
                else:
                    # 未知类型，转为字符串
                    value_bytes = str(value).encode('utf-8')
                    serialized += struct.pack('H', len(value_bytes)) + value_bytes
            
            return serialized
        
        @staticmethod
        def deserialize_data(serialized_data):
            """反序列化数据"""
            data_dict = {}
            pos = 0
            
            while pos < len(serialized_data):
                # 读取键长度和键
                key_len = struct.unpack('B', serialized_data[pos:pos+1])[0]
                pos += 1
                key = serialized_data[pos:pos+key_len].decode('utf-8')
                pos += key_len
                
                # 读取值长度
                value_len = struct.unpack('H', serialized_data[pos:pos+2])[0]
                pos += 2
                
                # 尝试解析不同类型的值
                if value_len == 4:
                    # 可能是整数
                    try:
                        value = struct.unpack('i', serialized_data[pos:pos+4])[0]
                    except:
                        value = serialized_data[pos:pos+value_len].decode('utf-8', errors='replace')
                elif value_len == 8:
                    # 可能是浮点数
                    try:
                        value = struct.unpack('d', serialized_data[pos:pos+8])[0]
                    except:
                        value = serialized_data[pos:pos+value_len].decode('utf-8', errors='replace')
                else:
                    # 假设是字符串
                    try:
                        value = serialized_data[pos:pos+value_len].decode('utf-8')
                    except:
                        value = "<binary data>"
                
                data_dict[key] = value
                pos += value_len
            
            return data_dict
    
    # 测试二进制协议
    # 创建数据字典
    data = {
        'name': 'Sensor Data',
        'id': 42,
        'timestamp': 1623456789.123,
        'readings': [1.23, 4.56, 7.89],
        'status': 'active'
    }
    
    # 序列化数据
    serialized_data = BinaryProtocol.serialize_data(data)
    
    # 创建消息
    message = BinaryProtocol.create_message(BinaryProtocol.MSG_TYPE_DATA, 123, serialized_data)
    print(f"创建的消息长度: {len(message)} 字节")
    
    # 解析消息
    parsed_message, remaining = BinaryProtocol.parse_message(message)
    if parsed_message:
        msg_type, msg_id, payload = parsed_message
        print(f"解析的消息: 类型={msg_type}, ID={msg_id}, 负载长度={len(payload)} 字节")
        
        # 反序列化负载数据
        deserialized_data = BinaryProtocol.deserialize_data(payload)
        print("反序列化的数据:")
        for key, value in deserialized_data.items():
            print(f"  {key}: {value}")
    print()
    
    # 5. 模拟二进制文件I/O操作
    def save_binary_file(filename, data_list):
        """保存数据到二进制文件"""
        with open(filename, 'wb') as f:
            # 写入数据项数量
            f.write(struct.pack('I', len(data_list)))
            
            # 为每个数据项写入类型标记和数据
            for item in data_list:
                if isinstance(item, int):
                    f.write(b'i')  # 整数类型标记
                    f.write(struct.pack('i', item))
                elif isinstance(item, float):
                    f.write(b'f')  # 浮点数类型标记
                    f.write(struct.pack('d', item))
                elif isinstance(item, str):
                    f.write(b's')  # 字符串类型标记
                    item_bytes = item.encode('utf-8')
                    f.write(struct.pack('I', len(item_bytes)))
                    f.write(item_bytes)
                elif isinstance(item, bytes):
                    f.write(b'b')  # 字节类型标记
                    f.write(struct.pack('I', len(item)))
                    f.write(item)
    
    def load_binary_file(filename):
        """从二进制文件加载数据"""
        result = []
        
        try:
            with open(filename, 'rb') as f:
                # 读取数据项数量
                count = struct.unpack('I', f.read(4))[0]
                
                for _ in range(count):
                    # 读取类型标记
                    type_tag = f.read(1)
                    
                    if type_tag == b'i':
                        # 整数
                        result.append(struct.unpack('i', f.read(4))[0])
                    elif type_tag == b'f':
                        # 浮点数
                        result.append(struct.unpack('d', f.read(8))[0])
                    elif type_tag == b's':
                        # 字符串
                        length = struct.unpack('I', f.read(4))[0]
                        result.append(f.read(length).decode('utf-8'))
                    elif type_tag == b'b':
                        # 字节
                        length = struct.unpack('I', f.read(4))[0]
                        result.append(f.read(length))
        except Exception as e:
            print(f"加载文件时出错: {e}")
        
        return result
    
    # 测试二进制文件I/O（这里只是模拟，不实际写入文件）
    test_data = [42, 3.14159, "Hello, Binary!", b'Raw bytes data', -123]
    print(f"要保存的测试数据: {test_data}")
    
    # 在实际应用中，这里会调用save_binary_file和load_binary_file
    # 但为了演示，我们直接打印序列化过程
    print("模拟序列化过程:")
    print(f"  数据项数量: {len(test_data)}")
    for item in test_data:
        if isinstance(item, int):
            print(f"  整数 {item} -> 类型标记: b'i', 数据: {binascii.hexlify(struct.pack('i', item))}")
        elif isinstance(item, float):
            print(f"  浮点数 {item} -> 类型标记: b'f', 数据: {binascii.hexlify(struct.pack('d', item))}")
        elif isinstance(item, str):
            item_bytes = item.encode('utf-8')
            print(f"  字符串 '{item}' -> 类型标记: b's', 长度: {len(item_bytes)}, 数据: {binascii.hexlify(item_bytes)}")
        elif isinstance(item, bytes):
            print(f"  字节 {item} -> 类型标记: b'b', 长度: {len(item)}, 数据: {binascii.hexlify(item)}")
    print()
    
    # 6. 实现一个简单的二进制哈希表
    class BinaryHashTable:
        """简单的二进制哈希表实现"""
        
        def __init__(self, capacity=16):
            self.capacity = capacity
            self.size = 0
            # 使用二进制数据存储键值对
            self.buckets = [b''] * capacity
        
        def _hash(self, key):
            """简单的哈希函数"""
            key_bytes = key.encode('utf-8')
            h = 0
            for byte in key_bytes:
                h = (h * 31 + byte) % self.capacity
            return h
        
        def put(self, key, value):
            """添加或更新键值对"""
            index = self._hash(key)
            
            # 序列化键值对: 键长度(2字节) + 键 + 值长度(4字节) + 值
            key_bytes = key.encode('utf-8')
            
            if isinstance(value, str):
                value_bytes = value.encode('utf-8')
            elif isinstance(value, int):
                value_bytes = struct.pack('Q', value)  # 使用8字节存储整数
            elif isinstance(value, float):
                value_bytes = struct.pack('d', value)
            else:
                value_bytes = str(value).encode('utf-8')
            
            # 打包数据
            entry = struct.pack('HI', len(key_bytes), len(value_bytes)) + key_bytes + value_bytes
            
            # 如果是空桶或更新现有键，更新计数
            if not self.buckets[index]:
                self.size += 1
            
            self.buckets[index] = entry
            
            # 简单的扩容策略
            if self.size >= self.capacity * 0.75:
                self._resize()
        
        def get(self, key):
            """获取键对应的值"""
            index = self._hash(key)
            entry = self.buckets[index]
            
            if not entry:
                return None
            
            # 解析条目
            key_len, value_len = struct.unpack('HI', entry[:6])
            stored_key = entry[6:6+key_len].decode('utf-8')
            
            # 检查键是否匹配
            if stored_key != key:
                # 简单处理冲突的情况
                return None
            
            # 提取值
            value_data = entry[6+key_len:6+key_len+value_len]
            
            # 尝试解析不同类型
            try:
                # 尝试作为整数解析
                if value_len == 8:
                    return struct.unpack('Q', value_data)[0]
                # 尝试作为浮点数解析
                elif value_len == 8:
                    return struct.unpack('d', value_data)[0]
                # 默认作为字符串解析
                return value_data.decode('utf-8')
            except:
                return value_data
        
        def _resize(self):
            """调整哈希表大小"""
            old_buckets = self.buckets
            self.capacity *= 2
            self.size = 0
            self.buckets = [b''] * self.capacity
            
            # 重新插入所有非空桶
            for entry in old_buckets:
                if entry:
                    key_len, value_len = struct.unpack('HI', entry[:6])
                    key = entry[6:6+key_len].decode('utf-8')
                    value_data = entry[6+key_len:6+key_len+value_len]
                    
                    # 重新插入
                    self.put(key, value_data)
        
        def to_binary(self):
            """转换为二进制数据"""
            # 格式: 容量(4字节) + 大小(4字节) + 非空桶数量(4字节) + 非空桶数据
            non_empty_buckets = [(i, entry) for i, entry in enumerate(self.buckets) if entry]
            
            binary = struct.pack('III', self.capacity, self.size, len(non_empty_buckets))
            
            for i, entry in non_empty_buckets:
                # 桶索引(4字节) + 条目长度(4字节) + 条目数据
                binary += struct.pack('II', i, len(entry)) + entry
            
            return binary
        
        @classmethod
        def from_binary(cls, binary_data):
            """从二进制数据创建哈希表"""
            offset = 0
            
            # 读取基本信息
            capacity, size, non_empty_count = struct.unpack('III', binary_data[offset:offset+12])
            offset += 12
            
            # 创建哈希表
            hashtable = cls(capacity)
            hashtable.size = size
            
            # 读取非空桶数据
            for _ in range(non_empty_count):
                i, entry_len = struct.unpack('II', binary_data[offset:offset+8])
                offset += 8
                entry = binary_data[offset:offset+entry_len]
                offset += entry_len
                hashtable.buckets[i] = entry
            
            return hashtable
    
    # 测试二进制哈希表
    print("测试二进制哈希表:")
    hash_table = BinaryHashTable()
    
    # 添加一些数据
    hash_table.put('name', 'Binary Hash Table')
    hash_table.put('version', 1.0)
    hash_table.put('capacity', hash_table.capacity)
    hash_table.put('created', '2023-06-01')
    hash_table.put('binary', True)
    
    # 获取数据
    print(f"  name: {hash_table.get('name')}")
    print(f"  version: {hash_table.get('version')}")
    print(f"  capacity: {hash_table.get('capacity')}")
    print(f"  created: {hash_table.get('created')}")
    print(f"  binary: {hash_table.get('binary')}")
    
    # 转换为二进制
    binary_data = hash_table.to_binary()
    print(f"  二进制数据长度: {len(binary_data)} 字节")
    
    # 从二进制重建
    new_hash_table = BinaryHashTable.from_binary(binary_data)
    print(f"  重建后 - name: {new_hash_table.get('name')}")
    print(f"  重建后 - version: {new_hash_table.get('version')}")
    print()

# 8. 高级用法和技巧
print("=== 高级用法和技巧 ===")

# 1. 使用格式缓存提高性能
class StructCache:
    """struct格式缓存"""
    
    def __init__(self):
        self.struct_cache = {}
    
    def get_struct(self, format_str):
        """获取或创建struct对象"""
        if format_str not in self.struct_cache:
            self.struct_cache[format_str] = struct.Struct(format_str)
        return self.struct_cache[format_str]
    
    def pack(self, format_str, *args):
        """打包数据"""
        return self.get_struct(format_str).pack(*args)
    
    def unpack(self, format_str, buffer):
        """解包数据"""
        return self.get_struct(format_str).unpack(buffer)
    
    def calcsize(self, format_str):
        """计算格式大小"""
        return self.get_struct(format_str).size

# 使用格式缓存
cache = StructCache()
packed = cache.pack('ifh', 123, 45.67, 89)
unpacked = cache.unpack('ifh', packed)
print(f"使用缓存打包/解包: {unpacked}")
print(f"格式大小: {cache.calcsize('ifh')}")
print()

# 2. 处理变长二进制数据
class BinaryBuffer:
    """二进制缓冲区类"""
    
    def __init__(self):
        self.buffer = bytearray()
        self.position = 0
    
    def write_int8(self, value):
        """写入8位整数"""
        self.buffer.extend(struct.pack('b', value))
        return self
    
    def write_uint8(self, value):
        """写入无符号8位整数"""
        self.buffer.extend(struct.pack('B', value))
        return self
    
    def write_int16(self, value, endianness='<'):
        """写入16位整数"""
        self.buffer.extend(struct.pack(f'{endianness}h', value))
        return self
    
    def write_uint16(self, value, endianness='<'):
        """写入无符号16位整数"""
        self.buffer.extend(struct.pack(f'{endianness}H', value))
        return self
    
    def write_int32(self, value, endianness='<'):
        """写入32位整数"""
        self.buffer.extend(struct.pack(f'{endianness}i', value))
        return self
    
    def write_uint32(self, value, endianness='<'):
        """写入无符号32位整数"""
        self.buffer.extend(struct.pack(f'{endianness}I', value))
        return self
    
    def write_float(self, value, endianness='<'):
        """写入浮点数"""
        self.buffer.extend(struct.pack(f'{endianness}f', value))
        return self
    
    def write_double(self, value, endianness='<'):
        """写入双精度浮点数"""
        self.buffer.extend(struct.pack(f'{endianness}d', value))
        return self
    
    def write_string(self, value, encoding='utf-8', null_terminated=False):
        """写入字符串"""
        string_bytes = value.encode(encoding)
        if null_terminated:
            string_bytes += b'\x00'
        self.buffer.extend(string_bytes)
        return self
    
    def write_bytes(self, value):
        """写入字节数据"""
        self.buffer.extend(value)
        return self
    
    def write_prefixed_string(self, value, encoding='utf-8', prefix_format='H'):
        """写入带前缀长度的字符串"""
        string_bytes = value.encode(encoding)
        self.buffer.extend(struct.pack(prefix_format, len(string_bytes)))
        self.buffer.extend(string_bytes)
        return self
    
    def read_int8(self):
        """读取8位整数"""
        value = struct.unpack_from('b', self.buffer, self.position)[0]
        self.position += 1
        return value
    
    def read_uint8(self):
        """读取无符号8位整数"""
        value = struct.unpack_from('B', self.buffer, self.position)[0]
        self.position += 1
        return value
    
    def read_int16(self, endianness='<'):
        """读取16位整数"""
        value = struct.unpack_from(f'{endianness}h', self.buffer, self.position)[0]
        self.position += 2
        return value
    
    def read_uint16(self, endianness='<'):
        """读取无符号16位整数"""
        value = struct.unpack_from(f'{endianness}H', self.buffer, self.position)[0]
        self.position += 2
        return value
    
    def read_int32(self, endianness='<'):
        """读取32位整数"""
        value = struct.unpack_from(f'{endianness}i', self.buffer, self.position)[0]
        self.position += 4
        return value
    
    def read_uint32(self, endianness='<'):
        """读取无符号32位整数"""
        value = struct.unpack_from(f'{endianness}I', self.buffer, self.position)[0]
        self.position += 4
        return value
    
    def read_float(self, endianness='<'):
        """读取浮点数"""
        value = struct.unpack_from(f'{endianness}f', self.buffer, self.position)[0]
        self.position += 4
        return value
    
    def read_double(self, endianness='<'):
        """读取双精度浮点数"""
        value = struct.unpack_from(f'{endianness}d', self.buffer, self.position)[0]
        self.position += 8
        return value
    
    def read_bytes(self, length):
        """读取指定长度的字节"""
        value = self.buffer[self.position:self.position+length]
        self.position += length
        return bytes(value)
    
    def read_string(self, length, encoding='utf-8'):
        """读取指定长度的字符串"""
        value = self.read_bytes(length).decode(encoding)
        return value
    
    def read_null_terminated_string(self, encoding='utf-8'):
        """读取空终止字符串"""
        start = self.position
        while self.position < len(self.buffer) and self.buffer[self.position] != 0:
            self.position += 1
        
        value = self.buffer[start:self.position].decode(encoding)
        if self.position < len(self.buffer):
            self.position += 1  # 跳过空终止符
        
        return value
    
    def read_prefixed_string(self, encoding='utf-8', prefix_format='H'):
        """读取带前缀长度的字符串"""
        prefix_size = struct.calcsize(prefix_format)
        length = struct.unpack_from(prefix_format, self.buffer, self.position)[0]
        self.position += prefix_size
        return self.read_string(length, encoding)
    
    def to_bytes(self):
        """转换为bytes对象"""
        return bytes(self.buffer)
    
    def clear(self):
        """清空缓冲区"""
        self.buffer.clear()
        self.position = 0
    
    def tell(self):
        """获取当前位置"""
        return self.position
    
    def seek(self, position):
        """设置当前位置"""
        self.position = max(0, min(position, len(self.buffer)))
        return self.position
    
    def __len__(self):
        """获取缓冲区长度"""
        return len(self.buffer)

# 使用二进制缓冲区
buffer = BinaryBuffer()

# 写入各种类型的数据
buffer.write_int32(12345)
    .write_string("Hello, Binary Buffer!")
    .write_prefixed_string("Prefixed String")
    .write_double(3.1415926535)
    .write_uint8(255)

# 获取二进制数据
binary_data = buffer.to_bytes()
print(f"二进制缓冲区内容长度: {len(binary_data)} 字节")
print(f"十六进制表示: {binascii.hexlify(binary_data)[:60]}...")  # 只显示前60个字符

# 重置位置并读取数据
buffer.seek(0)
read_int = buffer.read_int32()
read_str = buffer.read_string(22)  # "Hello, Binary Buffer!" 的长度
read_prefixed = buffer.read_prefixed_string()
read_double = buffer.read_double()
read_byte = buffer.read_uint8()

print(f"读取的整数: {read_int}")
print(f"读取的字符串: '{read_str}'")
print(f"读取的前缀字符串: '{read_prefixed}'")
print(f"读取的浮点数: {read_double}")
print(f"读取的字节: {read_byte}")
print()

# 9. 注意事项和最佳实践
"""
1. **字节序问题**：
   - 在处理跨平台数据时，始终明确指定字节序
   - 网络通信使用大端序（'!' 或 '>'）
   - 文件格式根据规范使用正确的字节序

2. **对齐问题**：
   - 使用'='、'<'、'>'或'!'时不进行对齐
   - 使用'@'时会进行本机对齐，可能导致结构体大小大于预期
   - 跨平台应用通常应避免使用'@'格式

3. **性能优化**：
   - 频繁使用相同格式时，使用struct.Struct对象并缓存
   - 对于大量数据，考虑使用pack_into和unpack_from直接操作缓冲区
   - 避免不必要的类型转换

4. **错误处理**：
   - 总是检查打包/解包的数据长度是否符合预期
   - 处理可能出现的struct.error异常
   - 在读取二进制文件或网络数据时，处理部分读取的情况

5. **内存使用**：
   - 对于大型二进制数据，考虑使用内存映射文件或分块处理
   - 使用bytearray而不是bytes进行频繁修改的二进制数据

6. **兼容性**：
   - 注意不同平台和Python版本间的兼容性
   - 整数大小在不同平台可能不同，使用明确大小的格式字符（如'i'、'l'）
   - Python 3中字符串和字节的严格区分需要特别注意

7. **文档和注释**：
   - 为二进制格式定义添加详细注释
   - 明确定义每个字段的含义、大小和字节序
   - 使用常量命名格式字符串以提高可维护性

8. **测试**：
   - 编写全面的测试用例验证打包和解包的正确性
   - 包括边界情况和异常情况的测试
   - 测试跨平台兼容性
"""

def demonstrate_best_practices():
    """演示最佳实践"""
    print("=== 最佳实践示例 ===")
    
    # 1. 使用struct.Struct提高性能
    print("使用struct.Struct提高性能:")
    import time
    
    # 定义格式
    format_str = '!IHBH6s'
    test_data = (0x1234, 0x5678, 0x9A, 0xBC, b'abcdef')
    iterations = 100000
    
    # 方法1: 直接使用struct.pack/unpack
    start_time = time.time()
    for _ in range(iterations):
        packed = struct.pack(format_str, *test_data)
        unpacked = struct.unpack(format_str, packed)
    direct_time = time.time() - start_time
    print(f"直接使用struct: {direct_time:.6f}秒")
    
    # 方法2: 使用struct.Struct对象
    my_struct = struct.Struct(format_str)
    start_time = time.time()
    for _ in range(iterations):
        packed = my_struct.pack(*test_data)
        unpacked = my_struct.unpack(packed)
    struct_obj_time = time.time() - start_time
    print(f"使用struct.Struct对象: {struct_obj_time:.6f}秒")
    print(f"性能提升: {direct_time / struct_obj_time:.2f}倍")
    print()
    
    # 2. 正确处理字节序
    print("正确处理字节序:")
    
    def create_platform_independent_data(data):
        """创建平台无关的数据"""
        # 使用网络字节序（大端序）确保跨平台兼容性
        return struct.pack('!IdQ', data[0], data[1], data[2])
    
    def parse_platform_independent_data(packed_data):
        """解析平台无关的数据"""
        # 使用相同的字节序进行解析
        return struct.unpack('!IdQ', packed_data)
    
    test_values = (123456789, 3.1415926535, 9876543210)
    
    # 模拟跨平台传输
    transmitted_data = create_platform_independent_data(test_values)
    received_data = parse_platform_independent_data(transmitted_data)
    
    print(f"原始数据: {test_values}")
    print(f"传输后数据: {received_data}")
    print(f"数据是否一致: {test_values == received_data}")
    print()
    
    # 3. 安全的二进制数据解析
    print("安全的二进制数据解析:")
    
    def safe_unpack(format_str, data):
        """安全地解包二进制数据"""
        expected_size = struct.calcsize(format_str)
        if len(data) < expected_size:
            raise ValueError(f"数据不足: 需要{expected_size}字节, 实际只有{len(data)}字节")
        return struct.unpack(format_str, data[:expected_size])
    
    # 测试安全解包
    try:
        # 正常情况
        valid_data = struct.pack('ifh', 123, 45.67, 89)
        result = safe_unpack('ifh', valid_data)
        print(f"正常解包: {result}")
        
        # 数据不足情况
        invalid_data = valid_data[:-2]  # 缺少2个字节
        result = safe_unpack('ifh', invalid_data)
        print("这行不应该被执行")
    except ValueError as e:
        print(f"预期的错误: {e}")
    print()
    
    # 4. 处理部分读取的数据
    print("处理部分读取的数据:")
    
    class BinaryDataReader:
        """处理部分读取的二进制数据"""
        
        def __init__(self):
            self.buffer = bytearray()
        
        def add_data(self, data):
            """添加新数据到缓冲区"""
            self.buffer.extend(data)
        
        def try_read_packet(self, header_format, payload_format_creator=None):
            """尝试读取一个完整的数据包
            
            Args:
                header_format: 头部格式字符串
                payload_format_creator: 可选，一个函数，接收头部数据并返回负载格式字符串
            
            Returns:
                (成功, 数据包, 剩余数据) 三元组
            """
            header_size = struct.calcsize(header_format)
            
            # 检查是否有足够的数据读取头部
            if len(self.buffer) < header_size:
                return False, None, bytes(self.buffer)
            
            # 读取头部
            header = struct.unpack_from(header_format, self.buffer)
            
            # 如果有负载格式创建器，使用它来确定负载大小
            if payload_format_creator:
                payload_format = payload_format_creator(header)
                payload_size = struct.calcsize(payload_format)
                total_size = header_size + payload_size
                
                # 检查是否有足够的数据读取整个数据包
                if len(self.buffer) < total_size:
                    return False, None, bytes(self.buffer)
                
                # 读取负载
                payload = struct.unpack_from(payload_format, self.buffer, header_size)
                packet = (header, payload)
                
                # 更新缓冲区
                self.buffer = self.buffer[total_size:]
                return True, packet, bytes(self.buffer)
            else:
                # 没有负载，只返回头部
                packet = header
                self.buffer = self.buffer[header_size:]
                return True, packet, bytes(self.buffer)
    
    # 模拟流式数据接收
    reader = BinaryDataReader()
    
    # 创建一个数据包：头部(2字节长度 + 1字节类型) + 负载(变长)
    def create_packet(packet_type, payload):
        payload_bytes = payload.encode('utf-8')
        header = struct.pack('HB', len(payload_bytes), packet_type)
        return header + payload_bytes
    
    # 定义负载格式创建器
    def payload_format_creator(header):
        payload_length = header[0]
        return f'{payload_length}s'  # 返回对应长度的字符串格式
    
    # 创建两个数据包
    packet1 = create_packet(1, "First packet data")
    packet2 = create_packet(2, "Second packet with more data")
    
    # 模拟部分接收数据
    reader.add_data(packet1[:5])  # 只接收部分第一个数据包
    success, packet, remaining = reader.try_read_packet('HB', payload_format_creator)
    print(f"部分读取后 - 成功: {success}, 数据包: {packet}")
    
    # 接收更多数据
    reader.add_data(packet1[5:] + packet2[:10])
    success, packet, remaining = reader.try_read_packet('HB', payload_format_creator)
    print(f"接收完整第一个包后 - 成功: {success}")
    if success:
        header, payload = packet
        print(f"  头部: 长度={header[0]}, 类型={header[1]}")
        print(f"  负载: {payload[0].decode('utf-8')}")
    
    # 接收剩余数据
    reader.add_data(packet2[10:])
    success, packet, remaining = reader.try_read_packet('HB', payload_format_creator)
    print(f"接收完整第二个包后 - 成功: {success}")
    if success:
        header, payload = packet
        print(f"  头部: 长度={header[0]}, 类型={header[1]}")
        print(f"  负载: {payload[0].decode('utf-8')}")
    print()
    
    # 5. 定义二进制格式的常量
    print("定义二进制格式的常量:")
    
    # 使用常量定义格式字符串，提高可维护性
    class BinaryFormats:
        # 基本类型
        INT8 = 'b'
        UINT8 = 'B'
        INT16_LE = '<h'
        UINT16_LE = '<H'
        INT16_BE = '>h'
        UINT16_BE = '>H'
        INT32_LE = '<i'
        UINT32_LE = '<I'
        INT32_BE = '>i'
        UINT32_BE = '>I'
        FLOAT_LE = '<f'
        FLOAT_BE = '>f'
        DOUBLE_LE = '<d'
        DOUBLE_BE = '>d'
        
        # 复合类型
        POINT_LE = '<dd'  # 小端序二维点
        POINT_BE = '>dd'  # 大端序二维点
        
        # 协议格式
        MESSAGE_HEADER = '!IIB'  # 网络字节序: 长度(4字节) + ID(4字节) + 类型(1字节)
    
    # 使用常量
    point_data = (10.5, 20.75)
    packed_point = struct.pack(BinaryFormats.POINT_LE, *point_data)
    unpacked_point = struct.unpack(BinaryFormats.POINT_LE, packed_point)
    
    print(f"使用常量定义 - 原始点: {point_data}")
    print(f"使用常量定义 - 解包点: {unpacked_point}")
    print()
    
    # 6. 使用内存映射处理大文件
    print("使用内存映射处理大文件:")
    
    def demonstrate_memory_mapping():
        """演示内存映射文件操作"""
        # 注意：这只是演示代码，实际应用中需要适当处理文件操作
        print("在实际应用中，可以使用以下方式处理大文件:")
        print("""
        import mmap
        import os
        
        # 创建或打开一个文件
        with open('large_file.bin', 'r+b') as f:
            # 获取文件大小
            size = os.path.getsize('large_file.bin')
            
            # 创建内存映射
            with mmap.mmap(f.fileno(), length=size, access=mmap.ACCESS_READ) as mm:
                # 定义结构体格式
                record_format = 'IIdd'  # 假设记录格式
                record_size = struct.calcsize(record_format)
                
                # 遍历所有记录
                for i in range(0, size, record_size):
                    if i + record_size <= size:
                        # 直接从内存映射中解包数据
                        record = struct.unpack_from(record_format, mm, i)
                        # 处理记录...
        """)
    
    demonstrate_memory_mapping()
    print()

# 运行演示代码
if __name__ == "__main__":
    print("Python struct模块演示\n")
    
    # 运行基本演示
    # 实际应用示例
    practical_examples()
    # 高级用法和最佳实践
    demonstrate_best_practices()
    
    print("演示完成！")