# io模块详解

io模块提供了处理输入输出流的功能，是Python中文件处理的核心模块之一。

## 模块概述

io模块包含了一系列用于处理输入输出流的类和函数，这些功能可以：
- 处理文本流和二进制流
- 创建内存中的流对象
- 实现流的缓冲和非缓冲操作
- 支持流的编码和解码

## 基本用法

### 导入模块

```python
import io
```

### 文本流和二进制流

#### io.StringIO
创建一个内存中的文本流，用于处理字符串数据。

```python
# 创建文本流
with io.StringIO() as f:
    # 写入文本数据
    f.write('Hello, StringIO!')
    f.write('\nPython is awesome!')
    # 移动文件指针到开头
    f.seek(0)
    # 读取全部内容
    content = f.read()
    print(f"文本流内容:\n{content}")

# 也可以直接初始化文本流
text_stream = io.StringIO('Initial content')
print(f"初始内容: {text_stream.read()}")
text_stream.close()
```

#### io.BytesIO
创建一个内存中的二进制流，用于处理二进制数据。

```python
# 创建二进制流
with io.BytesIO() as f:
    # 写入二进制数据
    f.write(b'Hello, BytesIO!')
    f.write(b'\nPython is awesome!')
    # 移动文件指针到开头
    f.seek(0)
    # 读取全部内容
    content = f.read()
    print(f"二进制流内容: {content}")
    print(f"解码后内容: {content.decode('utf-8')}")

# 也可以直接初始化二进制流
binary_stream = io.BytesIO(b'Initial binary content')
print(f"初始内容: {binary_stream.read()}")
binary_stream.close()
```

### 流的基本操作

#### 读取和写入

流对象支持基本的读取和写入操作。

```python
# 文本流的读取和写入
with io.StringIO() as f:
    # 写入数据
    f.write('Line 1\n')
    f.write('Line 2\n')
    f.write('Line 3\n')
    
    # 移动文件指针到开头
    f.seek(0)
    
    # 读取一行
    line1 = f.readline()
    print(f"第一行: {line1.strip()}")
    
    # 读取所有行
    lines = f.readlines()
    print(f"剩余行: {[line.strip() for line in lines]}")
    
    # 移动文件指针到开头
    f.seek(0)
    
    # 读取全部内容
    content = f.read()
    print(f"全部内容:\n{content}")
```

#### 缓冲区操作

流对象支持缓冲区操作。

```python
# 缓冲区操作
with io.BytesIO() as f:
    # 检查是否可写
    print(f"是否可写: {f.writable()}")
    # 检查是否可读
    print(f"是否可读: {f.readable()}")
    # 检查是否可查找
    print(f"是否可查找: {f.seekable()}")
    
    # 写入数据
    f.write(b'Hello, Buffer!')
    
    # 获取当前位置
    pos = f.tell()
    print(f"当前位置: {pos}")
    
    # 移动到指定位置
    f.seek(0)
    
    # 获取缓冲区大小
    print(f"缓冲区大小: {f.buffer.getbuffer().nbytes}")
    
    # 读取数据
    content = f.read()
    print(f"内容: {content}")
```

## 高级功能

### 流的编码和解码

io.TextIOWrapper类用于将二进制流包装为文本流，支持编码和解码。

```python
# 流的编码和解码
binary_data = b'Hello, 你好, こんにちは!'

# 将二进制数据包装为文本流
with io.BytesIO(binary_data) as binary_stream:
    with io.TextIOWrapper(binary_stream, encoding='utf-8') as text_stream:
        # 读取文本内容
        text_content = text_stream.read()
        print(f"解码后内容: {text_content}")

# 将文本流包装为二进制流
text_content = 'Hello, 你好, こんにちは!'
with io.StringIO(text_content) as text_stream:
    # 获取底层二进制流
    binary_stream = io.BytesIO()
    # 手动编码
    binary_data = text_content.encode('utf-8')
    binary_stream.write(binary_data)
    binary_stream.seek(0)
    print(f"编码后内容: {binary_stream.read()}")
```

### 流的缓冲

io模块支持不同级别的缓冲。

```python
# 流的缓冲
import sys

# 无缓冲文本流
unbuffered_text = io.TextIOWrapper(sys.stdout.buffer, line_buffering=False)
# 行缓冲文本流
line_buffered_text = io.TextIOWrapper(sys.stdout.buffer, line_buffering=True)
# 固定大小缓冲文本流
fixed_buffer_text = io.TextIOWrapper(sys.stdout.buffer, buffer_size=4096)

print(f"无缓冲文本流: {unbuffered_text}")
print(f"行缓冲文本流: {line_buffered_text}")
print(f"固定大小缓冲文本流: {fixed_buffer_text}")

# 关闭流
unbuffered_text.close()
line_buffered_text.close()
fixed_buffer_text.close()
```

### 自定义流

可以通过继承io模块的基类来创建自定义流。

```python
# 自定义流
class CustomTextIO(io.TextIOBase):
    def __init__(self):
        self.buffer = []
    
    def write(self, s):
        """写入文本数据"""
        if not isinstance(s, str):
            raise TypeError("must be str, not {}".format(type(s).__name__))
        self.buffer.append(s)
        return len(s)
    
    def read(self, size=-1):
        """读取文本数据"""
        content = ''.join(self.buffer)
        if size == -1:
            self.buffer = []
            return content
        else:
            result = content[:size]
            self.buffer = [content[size:]]
            return result
    
    def seek(self, offset, whence=io.SEEK_SET):
        """设置文件指针位置"""
        # 简单实现，仅支持SEEK_SET
        if whence != io.SEEK_SET:
            raise IOError("Unsupported whence")
        if offset < 0:
            raise IOError("Negative offset")
        # 这里简化处理，实际实现需要更复杂的逻辑
        return offset

# 使用自定义流
custom_stream = CustomTextIO()
custom_stream.write('Hello, ')
custom_stream.write('Custom Stream!')
custom_stream.seek(0)
content = custom_stream.read()
print(f"自定义流内容: {content}")
custom_stream.close()
```

## 实际应用示例

### 示例1：内存中的数据处理

```python
def process_data_in_memory(data_list):
    """在内存中处理数据"""
    # 创建文本流
    with io.StringIO() as stream:
        # 将数据写入流
        for item in data_list:
            stream.write(f"{item}\n")
        
        # 移动文件指针到开头
        stream.seek(0)
        
        # 处理数据
        processed_data = []
        for line in stream:
            # 简单处理：去重并转换为大写
            processed_item = line.strip().upper()
            if processed_item not in processed_data:
                processed_data.append(processed_item)
        
        return processed_data

# 使用示例
data = ['apple', 'banana', 'cherry', 'apple', 'date', 'banana']
processed = process_data_in_memory(data)
print(f"原始数据: {data}")
print(f"处理后数据: {processed}")
```

### 示例2：二进制数据的编码和解码

```python
def encode_decode_binary_data(text_data):
    """编码和解码二进制数据"""
    # 编码为二进制数据
    binary_data = text_data.encode('utf-8')
    print(f"编码后二进制数据: {binary_data}")
    
    # 创建二进制流
    with io.BytesIO(binary_data) as binary_stream:
        # 读取二进制数据
        read_binary = binary_stream.read()
        print(f"从流中读取的二进制数据: {read_binary}")
        
        # 解码为文本数据
        decoded_text = read_binary.decode('utf-8')
        print(f"解码后文本数据: {decoded_text}")
    
    return decoded_text

# 使用示例
text = 'Hello, 世界! This is a test.'
decoded = encode_decode_binary_data(text)
print(f"解码后是否与原文本相同: {decoded == text}")
```

### 示例3：捕获标准输出

```python
def capture_stdout(func):
    """装饰器，用于捕获函数的标准输出"""
    def wrapper(*args, **kwargs):
        # 创建文本流
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        try:
            # 执行函数
            result = func(*args, **kwargs)
            # 获取标准输出内容
            output = sys.stdout.getvalue()
            return result, output
        finally:
            # 恢复标准输出
            sys.stdout = old_stdout
    
    return wrapper

# 使用示例
import sys

@capture_stdout
def print_hello():
    print("Hello, World!")
    print("Python is awesome!")
    return "Function completed"

result, output = print_hello()
print(f"函数返回值: {result}")
print(f"捕获的标准输出:\n{output}")
```

### 示例4：模拟文件上传

```python
def simulate_file_upload(file_content, filename):
    """模拟文件上传"""
    # 创建二进制流
    with io.BytesIO(file_content.encode('utf-8')) as binary_stream:
        # 模拟上传过程
        print(f"正在上传文件: {filename}")
        print(f"文件大小: {len(file_content)} 字节")
        
        # 读取流内容（模拟上传）
        uploaded_content = binary_stream.read().decode('utf-8')
        print(f"上传内容预览: {uploaded_content[:50]}...")
        
        # 返回上传结果
        return {
            'filename': filename,
            'size': len(file_content),
            'content': uploaded_content,
            'status': 'success'
        }

# 使用示例
file_content = 'This is a test file content.\nIt contains multiple lines.\nPython is awesome!'
filename = 'test.txt'

upload_result = simulate_file_upload(file_content, filename)
print(f"\n上传结果: {upload_result}")
```

## 最佳实践

1. **使用with语句**：始终使用with语句创建流对象，确保在使用后正确关闭。
2. **选择合适的流类型**：根据需要选择文本流（StringIO）或二进制流（BytesIO）。
3. **注意编码问题**：在处理文本流和二进制流转换时，要注意编码和解码的正确性。
4. **避免内存溢出**：在处理大量数据时，要注意内存使用，避免内存溢出。
5. **使用缓冲**：适当使用缓冲可以提高流操作的效率。

## 与其他模块的关系

- **os模块**：io模块与os模块配合使用，可以处理文件系统中的文件流。
- **sys模块**：io模块与sys模块配合使用，可以捕获和重定向标准输入输出。
- **pickle模块**：可以与pickle模块配合使用，将对象序列化到内存流中。
- **json模块**：可以与json模块配合使用，将JSON数据读写到内存流中。

## 总结

io模块是Python中处理输入输出流的核心模块，提供了丰富的功能用于创建、管理和操作流对象。熟练掌握io模块的使用，可以使文件处理任务更加高效、灵活和方便。

通过结合io模块与其他文件处理模块（如os、sys、pickle、json等），可以完成各种复杂的文件处理任务，如数据处理、二进制编码解码、标准输出捕获、文件上传模拟等。