#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tempfile模块 - 临时文件和目录

tempfile模块提供了创建和管理临时文件和目录的功能，
它能够安全地创建临时文件和目录，并自动处理资源清理。

主要功能包括：
- 创建临时文件
- 创建临时目录
- 自动管理临时文件的生命周期
- 支持不同的临时文件创建模式
"""

import tempfile
import os
import sys

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. tempfile模块基本介绍")
print("=" * 50)
print("tempfile模块用于创建和管理临时文件和目录")
print("它提供了安全的临时文件创建方式，并自动处理资源清理")

# ===========================
# 2. 创建临时文件
# ===========================
print("\n" + "=" * 50)
print("2. 创建临时文件")
print("=" * 50)

# 使用NamedTemporaryFile创建临时文件
print("演示使用NamedTemporaryFile创建临时文件:")
with tempfile.NamedTemporaryFile() as temp:
    print(f"临时文件路径: {temp.name}")
    print(f"文件是否存在: {os.path.exists(temp.name)}")
    
    # 写入数据到临时文件
    temp.write(b"Hello, tempfile!")
    temp.flush()  # 确保数据写入磁盘
    
    # 读取数据
    temp.seek(0)
    content = temp.read()
    print(f"临时文件内容: {content.decode()}")

# 退出with块后，临时文件会自动删除
print(f"退出with块后，临时文件是否存在: {os.path.exists(temp.name)}")

# 创建不自动删除的临时文件
print("\n演示创建不自动删除的临时文件:")
temp = tempfile.NamedTemporaryFile(delete=False)
try:
    print(f"临时文件路径: {temp.name}")
    temp.write(b"This file will not be deleted automatically")
    temp.close()
    
    # 检查文件是否存在
    print(f"关闭文件后，临时文件是否存在: {os.path.exists(temp.name)}")
    
    # 手动删除文件
    os.unlink(temp.name)
    print(f"手动删除后，临时文件是否存在: {os.path.exists(temp.name)}")
finally:
    # 确保文件被删除
    if os.path.exists(temp.name):
        os.unlink(temp.name)

# 创建指定后缀的临时文件
print("\n演示创建指定后缀的临时文件:")
with tempfile.NamedTemporaryFile(suffix=".txt") as temp:
    print(f"带.txt后缀的临时文件: {temp.name}")
    print(f"文件扩展名: {os.path.splitext(temp.name)[1]}")

# 创建指定前缀的临时文件
print("\n演示创建指定前缀的临时文件:")
with tempfile.NamedTemporaryFile(prefix="test_") as temp:
    print(f"带test_前缀的临时文件: {temp.name}")

# 创建指定目录的临时文件
print("\n演示在当前目录创建临时文件:")
with tempfile.NamedTemporaryFile(dir=".") as temp:
    print(f"在当前目录的临时文件: {temp.name}")
    print(f"文件是否在当前目录: {os.path.dirname(temp.name) == os.getcwd()}")

# ===========================
# 3. 创建临时目录
# ===========================
print("\n" + "=" * 50)
print("3. 创建临时目录")
print("=" * 50)

# 使用TemporaryDirectory创建临时目录
print("演示使用TemporaryDirectory创建临时目录:")
with tempfile.TemporaryDirectory() as temp_dir:
    print(f"临时目录路径: {temp_dir}")
    print(f"临时目录是否存在: {os.path.exists(temp_dir)}")
    
    # 在临时目录中创建文件
    temp_file_path = os.path.join(temp_dir, "temp.txt")
    with open(temp_file_path, "w") as f:
        f.write("File in temporary directory")
    
    print(f"临时目录中的文件是否存在: {os.path.exists(temp_file_path)}")

# 退出with块后，临时目录会自动删除
print(f"退出with块后，临时目录是否存在: {os.path.exists(temp_dir)}")

# 创建不自动删除的临时目录
print("\n演示创建不自动删除的临时目录:")
temp_dir = tempfile.TemporaryDirectory(delete=False)
try:
    print(f"临时目录路径: {temp_dir.name}")
    print(f"临时目录是否存在: {os.path.exists(temp_dir.name)}")
    
    # 在临时目录中创建文件
    temp_file_path = os.path.join(temp_dir.name, "temp.txt")
    with open(temp_file_path, "w") as f:
        f.write("File in temporary directory")
    
    # 手动删除临时目录
    temp_dir.cleanup()
    print(f"手动删除后，临时目录是否存在: {os.path.exists(temp_dir.name)}")
finally:
    # 确保目录被删除
    if os.path.exists(temp_dir.name):
        temp_dir.cleanup()

# 创建指定前缀的临时目录
print("\n演示创建指定前缀的临时目录:")
with tempfile.TemporaryDirectory(prefix="test_") as temp_dir:
    print(f"带test_前缀的临时目录: {temp_dir}")

# 创建指定后缀的临时目录
print("\n演示创建指定后缀的临时目录:")
with tempfile.TemporaryDirectory(suffix="_test") as temp_dir:
    print(f"带_test后缀的临时目录: {temp_dir}")

# ===========================
# 4. 低级临时文件创建函数
# ===========================
print("\n" + "=" * 50)
print("4. 低级临时文件创建函数")
print("=" * 50)

# 使用mkstemp创建临时文件（低级函数）
print("演示使用mkstemp创建临时文件:")
fd, path = tempfile.mkstemp()
print(f"文件描述符: {fd}")
print(f"临时文件路径: {path}")

# 使用文件描述符写入数据
try:
    with os.fdopen(fd, 'w') as f:
        f.write("Hello from mkstemp")
    
    # 读取数据
    with open(path, 'r') as f:
        content = f.read()
        print(f"文件内容: {content}")
finally:
    # 必须手动删除文件
    os.unlink(path)
    print(f"手动删除后，文件是否存在: {os.path.exists(path)}")

# 使用mkdtemp创建临时目录（低级函数）
print("\n演示使用mkdtemp创建临时目录:")
temp_dir = tempfile.mkdtemp()
print(f"临时目录路径: {temp_dir}")
print(f"临时目录是否存在: {os.path.exists(temp_dir)}")

# 清理临时目录
os.rmdir(temp_dir)
print(f"清理后，临时目录是否存在: {os.path.exists(temp_dir)}")

# ===========================
# 5. 临时文件的配置参数
# ===========================
print("\n" + "=" * 50)
print("5. 临时文件的配置参数")
print("=" * 50)

# 获取临时文件目录
print(f"默认临时文件目录: {tempfile.gettempdir()}")

# 获取临时文件前缀
print(f"默认临时文件前缀: {tempfile.gettempprefix()}")

# 获取临时目录前缀
print(f"默认临时目录前缀: {tempfile.gettempdirb()}")

# 检查是否支持大文件
print(f"是否支持大文件: {tempfile.TMP_MAX}")

# ===========================
# 6. 高级功能
# ===========================
print("\n" + "=" * 50)
print("6. 高级功能")
print("=" * 50)

# 使用SpooledTemporaryFile（内存中的临时文件，超过阈值后写入磁盘）
print("演示使用SpooledTemporaryFile:")
with tempfile.SpooledTemporaryFile(max_size=100) as temp:
    print(f"临时文件类型: {type(temp)}")
    
    # 写入小数据
    temp.write(b"x" * 50)
    print(f"写入小数据后，文件类型: {type(temp)}")
    
    # 写入大数据
    temp.write(b"x" * 200)
    print(f"写入大数据后，文件类型: {type(temp)}")

# 创建自定义临时文件
print("\n演示创建自定义临时文件:")
def custom_temp_file():
    """创建自定义的临时文件"""
    # 获取默认临时目录
    temp_dir = tempfile.gettempdir()
    
    # 创建唯一的文件名
    import uuid
    filename = f"custom_temp_{uuid.uuid4().hex}.txt"
    
    # 创建文件路径
    file_path = os.path.join(temp_dir, filename)
    
    return file_path

custom_path = custom_temp_file()
print(f"自定义临时文件路径: {custom_path}")

# 清理
if os.path.exists(custom_path):
    os.unlink(custom_path)

# ===========================
# 7. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("7. 实际应用示例")
print("=" * 50)

# 示例1: 临时文件用于数据处理
def process_large_data(data):
    """使用临时文件处理大量数据"""
    print(f"处理数据大小: {len(data)} bytes")
    
    with tempfile.NamedTemporaryFile(suffix=".dat") as temp:
        # 写入数据
        temp.write(data)
        temp.flush()
        
        print(f"使用临时文件: {temp.name} 处理数据")
        
        # 这里可以添加数据处理逻辑
        # 例如：读取数据、分析、转换等
        temp.seek(0)
        processed_data = temp.read()
        
        print(f"处理后数据大小: {len(processed_data)} bytes")
        return processed_data

# 测试数据处理
print("示例1: 临时文件用于数据处理")
large_data = b"x" * 1024 * 1024  # 1MB数据
processed = process_large_data(large_data)
print(f"处理结果: {'成功' if processed else '失败'}")

# 示例2: 临时目录用于文件操作
def batch_process_files(files):
    """使用临时目录批量处理文件"""
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"使用临时目录: {temp_dir} 进行批量处理")
        
        # 复制文件到临时目录
        for file_path in files:
            if os.path.exists(file_path):
                import shutil
                filename = os.path.basename(file_path)
                temp_file = os.path.join(temp_dir, filename)
                shutil.copy(file_path, temp_file)
                print(f"复制文件: {file_path} -> {temp_file}")
        
        # 这里可以添加批量处理逻辑
        print(f"临时目录中的文件: {os.listdir(temp_dir)}")

# 测试批量处理
print("\n示例2: 临时目录用于文件操作")
# 创建测试文件
with open("file1.txt", "w") as f:
    f.write("Test file 1")
with open("file2.txt", "w") as f:
    f.write("Test file 2")

# 批量处理
batch_process_files(["file1.txt", "file2.txt"])

# 清理测试文件
for file in ["file1.txt", "file2.txt"]:
    if os.path.exists(file):
        os.remove(file)

# 示例3: 临时文件用于测试
def test_file_operation():
    """使用临时文件进行测试"""
    print("使用临时文件进行测试")
    
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as temp:
        # 写入测试数据
        temp.write("line 1\nline 2\nline 3")
        temp_path = temp.name
    
    try:
        # 执行测试
        with open(temp_path, 'r') as f:
            lines = f.readlines()
            print(f"文件包含 {len(lines)} 行")
            
            for i, line in enumerate(lines):
                print(f"第 {i+1} 行: {line.strip()}")
        
        # 验证测试结果
        assert len(lines) == 3, f"预期3行，实际{len(lines)}行"
        print("测试通过!")
        
    finally:
        # 清理
        os.unlink(temp_path)

# 测试文件操作
print("\n示例3: 临时文件用于测试")
test_file_operation()

# 示例4: 创建临时配置文件
def create_temp_config(config_dict):
    """创建临时配置文件"""
    import json
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp:
        json.dump(config_dict, temp, indent=4)
        return temp.name

# 测试创建临时配置文件
print("\n示例4: 创建临时配置文件")
config = {
    "server": "localhost",
    "port": 8080,
    "username": "test",
    "password": "secret"
}

config_file = create_temp_config(config)
print(f"创建的临时配置文件: {config_file}")

# 读取配置文件
import json
with open(config_file, 'r') as f:
    loaded_config = json.load(f)
    print(f"加载的配置: {loaded_config}")

# 清理
os.unlink(config_file)

# ===========================
# 8. 最佳实践和注意事项
# ===========================
print("\n" + "=" * 50)
print("8. 最佳实践和注意事项")
print("=" * 50)

print("1. 优先使用with语句管理临时文件，确保自动清理")
print("2. 避免使用delete=False，除非确实需要手动管理文件生命周期")
print("3. 对于大量数据，考虑使用SpooledTemporaryFile提高性能")
print("4. 指定文件后缀可以帮助操作系统识别文件类型")
print("5. 低级函数（如mkstemp）需要手动管理文件描述符和删除操作")
print("6. 注意临时文件的安全性，避免在临时文件中存储敏感信息")
print("7. 对于跨平台应用，使用tempfile模块可以确保临时文件路径的正确性")
print("8. 临时文件默认存储在系统临时目录中，可以通过TMPDIR环境变量修改")
print("9. 定期清理不再使用的临时文件，避免磁盘空间浪费")
print("10. 在异常处理中确保临时文件被正确清理")

# ===========================
# 9. 总结
# ===========================
print("\n" + "=" * 50)
print("9. 总结")
print("=" * 50)
print("tempfile模块提供了安全、便捷的临时文件和目录管理功能：")
print("- 支持创建命名和未命名的临时文件")
print("- 自动处理临时文件的生命周期")
print("- 支持自定义文件前缀、后缀和目录")
print("- 提供低级和高级API满足不同需求")
print("- 支持内存中的临时文件处理")
print("\n熟练掌握tempfile模块可以在处理临时数据、测试和批量操作等场景中提高效率，")
print("同时确保资源的正确管理和清理")
