# Python tempfile模块详解

import tempfile
import os
import time

# 1. 模块概述
print("=== 1. tempfile模块概述 ===")
print("tempfile模块提供了创建临时文件和目录的功能，是处理临时数据的理想工具。")
print("该模块的主要特点：")
print("- 自动创建临时文件和目录")
print("- 支持自动清理（上下文管理器）")
print("- 提供多种创建临时文件的方法")
print("- 支持自定义临时文件的位置和命名")
print("- 提供安全的文件创建机制")
print("- 支持不同模式的文件访问（文本/二进制）")
print("- 跨平台兼容性好")
print()

# 2. 临时文件创建
print("=== 2. 临时文件创建 ===")
print("tempfile提供了多种创建临时文件的方法：")
print()

# 2.1 TemporaryFile函数
print("2.1 TemporaryFile函数：")
print("创建一个临时文件，关闭后自动删除")

# 创建文本模式的临时文件
with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as f:
    f.write("Hello, tempfile!")
    f.seek(0)  # 移动到文件开头
    content = f.read()
    print(f"  写入并读取的内容: {content}")
    print(f"  文件是否关闭: {f.closed}")

print(f"  文件关闭后是否存在: {os.path.exists(f.name) if hasattr(f, 'name') else '无文件名'}")

# 创建二进制模式的临时文件
with tempfile.TemporaryFile(mode='wb+') as f:
    f.write(b"Binary data")
    f.seek(0)
    content = f.read()
    print(f"  二进制模式写入并读取的内容: {content}")

print()

# 2.2 NamedTemporaryFile函数
print("2.2 NamedTemporaryFile函数：")
print("创建一个有名称的临时文件，默认关闭后自动删除")

# 创建有名称的临时文件
with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8') as f:
    temp_name = f.name
    f.write("Named temporary file content")
    f.seek(0)
    content = f.read()
    print(f"  文件名称: {temp_name}")
    print(f"  文件内容: {content}")
    print(f"  文件是否存在: {os.path.exists(temp_name)}")

print(f"  文件关闭后是否存在: {os.path.exists(temp_name)}")

# 创建不自动删除的临时文件
with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', delete=False) as f:
    temp_name = f.name
    f.write("Persistent temporary file")

print(f"  使用delete=False创建的文件关闭后是否存在: {os.path.exists(temp_name)}")

# 手动删除文件
os.unlink(temp_name)
print(f"  手动删除后文件是否存在: {os.path.exists(temp_name)}")

print()

# 2.3 SpooledTemporaryFile函数
print("2.3 SpooledTemporaryFile函数：")
print("创建一个先保存在内存中的临时文件，超过阈值后写入磁盘")

# 创建SpooledTemporaryFile
with tempfile.SpooledTemporaryFile(max_size=100, mode='w+', encoding='utf-8') as f:
    # 写入少量数据（保存在内存中）
    f.write("Small amount of data")
    print(f"  写入少量数据后，是否在磁盘上: {hasattr(f._file, 'name') if hasattr(f, '_file') else '未知'}")
    
    # 写入大量数据（超过阈值，写入磁盘）
    f.write("X" * 200)
    f.seek(0)
    content = f.read()
    print(f"  写入大量数据后，是否在磁盘上: {hasattr(f._file, 'name') if hasattr(f, '_file') else '未知'}")
    print(f"  文件内容长度: {len(content)}")
    
    # 手动将内存数据写入磁盘
    f.rollover()
    print(f"  调用rollover()后，是否在磁盘上: {hasattr(f._file, 'name') if hasattr(f, '_file') else '未知'}")

print()

# 3. 临时目录创建
print("=== 3. 临时目录创建 ===")
print("tempfile.mkdtemp()函数用于创建临时目录")
print()

# 创建临时目录
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"  临时目录路径: {temp_dir}")
    print(f"  目录是否存在: {os.path.exists(temp_dir)}")
    
    # 在临时目录中创建文件
    temp_file = os.path.join(temp_dir, "test.txt")
    with open(temp_file, "w") as f:
        f.write("File in temporary directory")
    
    print(f"  临时目录中的文件: {os.listdir(temp_dir)}")

print(f"  上下文管理器退出后目录是否存在: {os.path.exists(temp_dir)}")

# 不使用上下文管理器创建临时目录
temp_dir = tempfile.mkdtemp()
print(f"  不使用上下文管理器创建的临时目录: {temp_dir}")
print(f"  目录是否存在: {os.path.exists(temp_dir)}")

# 手动删除临时目录
import shutil
shutil.rmtree(temp_dir)
print(f"  手动删除后目录是否存在: {os.path.exists(temp_dir)}")

print()

# 4. 临时文件和目录的命名
print("=== 4. 临时文件和目录的命名 ===")
print("tempfile允许自定义临时文件和目录的命名规则")
print()

# 使用prefix参数
print("4.1 使用prefix参数（前缀）:")
with tempfile.NamedTemporaryFile(prefix="app_", delete=False) as f:
    temp_name = f.name
    print(f"  使用prefix='app_'创建的临时文件: {os.path.basename(temp_name)}")
os.unlink(temp_name)

# 使用suffix参数
print("4.2 使用suffix参数（后缀）:")
with tempfile.NamedTemporaryFile(suffix=".log", delete=False) as f:
    temp_name = f.name
    print(f"  使用suffix='.log'创建的临时文件: {os.path.basename(temp_name)}")
os.unlink(temp_name)

# 同时使用prefix和suffix
print("4.3 同时使用prefix和suffix:")
with tempfile.NamedTemporaryFile(prefix="report_", suffix=".txt", delete=False) as f:
    temp_name = f.name
    print(f"  使用prefix和suffix创建的临时文件: {os.path.basename(temp_name)}")
os.unlink(temp_name)

# 临时目录的命名
print("4.4 临时目录的命名:")
temp_dir = tempfile.mkdtemp(prefix="temp_", suffix="_dir")
print(f"  使用prefix和suffix创建的临时目录: {os.path.basename(temp_dir)}")
shutil.rmtree(temp_dir)

print()

# 5. 临时文件的位置
print("=== 5. 临时文件的位置 ===")
print("tempfile根据平台选择默认的临时文件目录，但也允许自定义")
print()

# 获取默认临时目录
print("5.1 默认临时目录:")
print(f"  gettempdir(): {tempfile.gettempdir()}")
print(f"  gettempdirb(): {tempfile.gettempdirb()}")  # 字节串形式

# 获取临时文件的前缀
print(f"  gettempprefix(): {tempfile.gettempprefix()}")
print(f"  gettempprefixb(): {tempfile.gettempprefixb()}")  # 字节串形式

# 自定义临时文件位置
print("5.2 自定义临时文件位置:")
custom_dir = "./custom_temp"
os.makedirs(custom_dir, exist_ok=True)

with tempfile.NamedTemporaryFile(dir=custom_dir, delete=False) as f:
    temp_name = f.name
    print(f"  在自定义目录创建的临时文件: {temp_name}")
    print(f"  文件是否在指定目录中: {os.path.dirname(temp_name) == custom_dir}")
os.unlink(temp_name)
os.rmdir(custom_dir)

# 临时目录的自定义位置
print("5.3 临时目录的自定义位置:")
custom_dir = "./custom_temp_dir"
os.makedirs(custom_dir, exist_ok=True)

with tempfile.TemporaryDirectory(dir=custom_dir) as temp_dir:
    print(f"  在自定义目录创建的临时目录: {temp_dir}")
    print(f"  目录是否在指定目录中: {os.path.dirname(temp_dir) == custom_dir}")
os.rmdir(custom_dir)

print()

# 6. 安全考虑
print("=== 6. 安全考虑 ===")
print("tempfile模块提供了安全的临时文件创建机制")
print()

print("6.1 安全特性:")
print("  - 临时文件默认使用0o600权限（仅所有者可读写）")
print("  - 文件名使用随机生成的字符，减少猜测可能性")
print("  - 避免了竞态条件（TOCTOU攻击）")
print("  - 支持安全的文件创建模式")

# 演示权限设置
print("6.2 权限设置:")
with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
    temp_name = f.name
    # 获取文件权限
    import stat
    mode = os.stat(temp_name).st_mode
    print(f"  临时文件的权限: {oct(mode & 0o777)}")  # 仅显示权限部分
os.unlink(temp_name)

print("6.3 安全注意事项:")
print("  - 避免使用可预测的文件名")
print("  - 使用delete=True确保文件及时删除")
print("  - 不要在共享目录中创建敏感的临时文件")
print("  - 对于敏感数据，考虑使用加密")

print()

# 7. 高级用法
print("=== 7. 高级用法 ===")
print()

# 7.1 临时文件的缓冲
print("7.1 临时文件的缓冲:")
with tempfile.TemporaryFile(mode='w+', buffering=1) as f:  # 行缓冲
    f.write("Line 1\n")  # 写入后立即刷新
    f.write("Line 2")
    f.flush()  # 手动刷新缓冲区
    f.seek(0)
    content = f.read()
    print(f"  缓冲模式下的文件内容: {repr(content)}")

# 7.2 临时文件的编码
print("7.2 临时文件的编码:")
with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as f:
    f.write("你好，临时文件！")
    f.seek(0)
    content = f.read()
    print(f"  UTF-8编码下的中文内容: {content}")

# 7.3 自定义临时文件生成器
print("7.3 自定义临时文件生成器:")
# 获取临时文件生成器
prefix = "custom_"
suffix = ".tmp"

# 获取临时文件目录
temp_dir = tempfile.gettempdir()

# 生成临时文件名
print("  使用tempfile._get_candidate_names()生成随机文件名:")
name_generator = tempfile._get_candidate_names()
for i in range(5):
    random_name = next(name_generator)
    full_name = os.path.join(temp_dir, f"{prefix}{random_name}{suffix}")
    print(f"    生成的文件名: {full_name}")

print()

# 8. 实际应用示例
print("=== 8. 实际应用示例 ===")
print()

# 示例1：处理大型数据文件
def process_large_data(data_source):
    """处理大型数据文件，使用临时文件存储中间结果"""
    # 创建临时文件存储处理结果
    with tempfile.NamedTemporaryFile(mode='w+', suffix='.tmp', delete=False) as temp_file:
        temp_name = temp_file.name
        
        # 模拟处理大型数据
        print("  处理大型数据中...")
        time.sleep(1)  # 模拟处理时间
        
        # 写入处理结果
        temp_file.write("Processed data results\n")
        temp_file.write(f"Source: {data_source}\n")
        temp_file.write(f"Processed at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    print(f"  处理结果已保存到临时文件: {temp_name}")
    print(f"  临时文件大小: {os.path.getsize(temp_name)} bytes")
    
    # 读取处理结果
    with open(temp_name, 'r') as f:
        content = f.read()
        print(f"  处理结果内容:\n{content}")
    
    # 处理完成后删除临时文件
    os.unlink(temp_name)
    print(f"  临时文件已删除: {not os.path.exists(temp_name)}")

print("8.1 处理大型数据文件示例:")
process_large_data("https://example.com/large_dataset.csv")

# 示例2：临时目录用于文件操作
def batch_process_files(files):
    """批量处理文件，使用临时目录存储中间文件"""
    with tempfile.TemporaryDirectory(prefix="batch_") as temp_dir:
        print(f"  创建临时目录: {temp_dir}")
        
        # 复制文件到临时目录并处理
        for i, file_path in enumerate(files):
            # 创建临时文件路径
            temp_file_path = os.path.join(temp_dir, f"processed_{i}.txt")
            
            # 模拟文件处理
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write(f"Processed file: {file_path}\n")
                temp_file.write(f"Processed at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # 显示处理结果
        processed_files = os.listdir(temp_dir)
        print(f"  处理完成的文件: {processed_files}")
        
        # 统计总大小
        total_size = sum(os.path.getsize(os.path.join(temp_dir, f)) for f in processed_files)
        print(f"  临时目录总大小: {total_size} bytes")
    
    print(f"  临时目录已自动删除: {not os.path.exists(temp_dir)}")

print("\n8.2 临时目录用于文件操作示例:")
# 创建测试文件
os.makedirs("test_files", exist_ok=True)
test_files = [
    "test_files/file1.txt",
    "test_files/file2.txt",
    "test_files/file3.txt"
]

for f in test_files:
    with open(f, 'w') as file:
        file.write("Test content")

# 批量处理文件
batch_process_files(test_files)

# 清理测试文件
for f in test_files:
    os.remove(f)
os.rmdir("test_files")

# 示例3：临时文件用于单元测试
def test_file_processing():
    """使用临时文件进行单元测试"""
    print("8.3 临时文件用于单元测试示例:")
    
    # 创建测试用的临时文件
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as test_file:
        test_file.write("Line 1\nLine 2\nLine 3\n")
        test_file_path = test_file.name
    
    try:
        # 执行测试
        print(f"  测试文件路径: {test_file_path}")
        
        # 模拟文件处理函数
        def count_lines(file_path):
            with open(file_path, 'r') as f:
                return len(f.readlines())
        
        line_count = count_lines(test_file_path)
        print(f"  测试结果 - 文件行数: {line_count}")
        print(f"  测试通过: {line_count == 3}")
    finally:
        # 清理测试文件
        os.unlink(test_file_path)
        print(f"  测试文件已清理: {not os.path.exists(test_file_path)}")

test_file_processing()

print()

# 9. 最佳实践
print("=== 9. 最佳实践 ===")
print()

print("9.1 使用上下文管理器")
print("   # 推荐使用with语句，自动处理文件关闭和清理")
print("   with tempfile.TemporaryFile() as f:")
print("       f.write('data')")
print("       # 文件自动关闭并删除")

print("\n9.2 明确指定文件模式")
print("   # 文本模式")
print("   with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as f:")
print("       f.write('文本内容')")
print("   ")
print("   # 二进制模式")
print("   with tempfile.TemporaryFile(mode='wb+') as f:")
print("       f.write(b'二进制内容')")

print("\n9.3 使用适当的缓冲区")
print("   # 对于大型文件，考虑使用更大的缓冲区")
print("   with tempfile.TemporaryFile(mode='w+', buffering=8192) as f:")
print("       # 处理大型文件")

print("\n9.4 及时清理临时文件")
print("   # 使用delete=True确保文件自动删除")
print("   with tempfile.NamedTemporaryFile(delete=True) as f:")
print("       # 操作文件")
print("   # 文件自动删除")

print("\n9.5 避免硬编码临时目录")
print("   # 使用tempfile.gettempdir()获取默认临时目录")
print("   temp_dir = tempfile.gettempdir()")
print("   with tempfile.TemporaryFile(dir=temp_dir) as f:")
print("       # 操作文件")

print("\n9.6 考虑安全需求")
print("   # 对于敏感数据，使用安全的创建模式")
print("   with tempfile.NamedTemporaryFile(mode='w+', delete=True) as f:")
print("       # 写入敏感数据")

print("\n9.7 自定义命名规则")
print("   # 使用prefix和suffix提高可读性")
print("   with tempfile.NamedTemporaryFile(prefix='app_', suffix='.log') as f:")
print("       # 操作文件")

print("\n9.8 结合其他模块使用")
print("   # 与shutil模块结合处理临时文件")
print("   import shutil")
print("   with tempfile.TemporaryDirectory() as temp_dir:")
print("       # 使用shutil操作临时目录")
print("       shutil.copy('source.txt', temp_dir)")

print()

# 10. 常见错误和陷阱
print("=== 10. 常见错误和陷阱 ===")
print()

print("10.1 忘记关闭临时文件")
print("   # 错误：")
print("   f = tempfile.TemporaryFile()")
print("   f.write('data')")
print("   # 忘记关闭文件")
print("   ")
print("   # 正确：")
print("   with tempfile.TemporaryFile() as f:")
print("       f.write('data')")

print("\n10.2 文件删除失败")
print("   # 原因：文件可能被其他进程打开")
print("   # 解决方法：确保所有句柄都已关闭")
print("   import gc")
print("   gc.collect()  # 强制垃圾回收")

print("\n10.3 临时文件路径过长")
print("   # 原因：prefix和suffix过长导致路径超过系统限制")
print("   # 解决方法：使用简短的prefix和suffix")
print("   with tempfile.NamedTemporaryFile(prefix='short_', suffix='.tmp') as f:")
print("       pass")

print("\n10.4 编码问题")
print("   # 错误：在文本模式下未指定编码")
print("   with tempfile.TemporaryFile(mode='w+') as f:")
print("       f.write('中文')  # 可能导致编码错误")
print("   ")
print("   # 正确：")
print("   with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as f:")
print("       f.write('中文')")

print("\n10.5 权限不足")
print("   # 原因：临时目录权限不足")
print("   # 解决方法：使用有足够权限的目录")
print("   import os")
print("   custom_dir = './my_temp'")
print("   os.makedirs(custom_dir, exist_ok=True)")
print("   with tempfile.TemporaryFile(dir=custom_dir) as f:")
print("       pass")

print("\n10.6 临时文件被意外保留")
print("   # 原因：使用了delete=False但忘记手动删除")
print("   # 解决方法：使用try-finally确保删除")
print("   f = tempfile.NamedTemporaryFile(delete=False)")
print("   try:")
print("       # 操作文件")
print("   finally:")
print("       os.unlink(f.name)")

print("\n10.7 跨平台兼容性问题")
print("   # 原因：不同平台的临时目录和权限机制不同")
print("   # 解决方法：使用tempfile提供的跨平台函数")
print("   temp_dir = tempfile.gettempdir()")
print("   with tempfile.TemporaryFile(dir=temp_dir) as f:")
print("       pass")

print()

# 11. 总结
print("=== 11. tempfile模块总结 ===")
print("tempfile模块是Python中处理临时文件和目录的理想工具，提供了安全、便捷的临时文件管理功能。")
print()
print("主要功能：")
print("- 创建自动删除的临时文件（TemporaryFile）")
print("- 创建有名称的临时文件（NamedTemporaryFile）")
print("- 创建内存缓冲的临时文件（SpooledTemporaryFile）")
print("- 创建临时目录（TemporaryDirectory）")
print("- 获取默认临时目录和前缀（gettempdir, gettempprefix）")
print()
print("优势：")
print("- 自动清理机制，避免资源泄漏")
print("- 安全的文件创建，减少安全风险")
print("- 跨平台兼容性好")
print("- 灵活的配置选项")
print("- 与上下文管理器良好集成")
print()
print("应用场景：")
print("- 临时存储处理中间结果")
print("- 单元测试中的测试数据")
print("- 批量文件处理")
print("- 处理大型数据集")
print("- 安全存储敏感数据")
print()
print("通过合理使用tempfile模块，可以有效管理临时数据，提高代码的安全性和可维护性。")
