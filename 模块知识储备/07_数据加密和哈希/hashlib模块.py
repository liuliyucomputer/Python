# Python hashlib模块详解

```python
"""
hashlib模块 - Python中处理哈希算法的标准库

hashlib模块提供了安全哈希和消息摘要算法的实现，如MD5、SHA1、SHA256等。
这些算法可以将任意长度的数据映射为固定长度的字符串（哈希值），通常用于：
- 数据完整性验证
- 密码存储（与盐值结合）
- 数字签名
- 文件校验和计算
- 数据去重

支持的主要算法：
- MD5 (Message Digest Algorithm 5)
- SHA1 (Secure Hash Algorithm 1)
- SHA2系列 (SHA-224, SHA-256, SHA-384, SHA-512)
- SHA3系列 (SHA3-224, SHA3-256, SHA3-384, SHA3-512)
- BLAKE2b和BLAKE2s
- SHAKE系列可扩展输出函数

主要功能：
- 计算文件和数据的哈希值
- 支持哈希对象的增量更新
- 提供密钥派生函数（KDF）
- 支持盐值和迭代计数
- 提供文件校验和验证工具
- 兼容FIPS安全标准
"""

import hashlib
import os
import binascii
import time
from datetime import datetime
import io
import sys
import platform
import tempfile
import shutil

# 示例数据准备
def prepare_example_files():
    """准备示例文件用于哈希计算"""
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    print(f"创建临时目录: {temp_dir}")
    
    # 创建测试文本文件
    text_file_path = os.path.join(temp_dir, "test_text.txt")
    with open(text_file_path, "w", encoding="utf-8") as f:
        f.write("这是一个用于测试哈希算法的示例文本文件。\n")
        f.write("hashlib模块可以计算各种安全哈希值。\n")
        f.write("不同的哈希算法有不同的安全性和性能特点。\n")
        # 添加一些重复内容以测试哈希计算
        f.write("重复内容 " * 50)
    
    # 创建二进制文件
    binary_file_path = os.path.join(temp_dir, "test_binary.dat")
    with open(binary_file_path, "wb") as f:
        # 写入一些二进制数据
        data = bytearray(1024 * 10)  # 10KB数据
        for i in range(len(data)):
            data[i] = i % 256
        f.write(data)
    
    # 创建空文件
    empty_file_path = os.path.join(temp_dir, "empty.txt")
    open(empty_file_path, "w").close()
    
    return temp_dir, text_file_path, binary_file_path, empty_file_path

# 清理示例文件
def cleanup_example_files(temp_dir):
    """清理示例文件"""
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
        print(f"清理临时目录: {temp_dir}")

# 1. hashlib模块的基本使用
def basic_hashlib_usage():
    """
    hashlib模块的基本使用方法
    
    功能说明：演示如何使用hashlib计算各种数据的哈希值，包括字符串和文件。
    """
    print("=== 1. hashlib模块的基本使用 ===")
    
    # 1.1 支持的算法列表
    print("\n1.1 可用的哈希算法:")
    print("当前系统支持的哈希算法:", sorted(hashlib.algorithms_available))
    print("\n保证可用的哈希算法:", sorted(hashlib.algorithms_guaranteed))
    
    # 1.2 计算字符串的哈希值
    print("\n1.2 计算字符串的哈希值:")
    
    message = "Hello, hashlib! 你好，哈希库！"
    print(f"原始消息: {message}")
    print()
    
    # 计算不同算法的哈希值
    algorithms_to_test = ['md5', 'sha1', 'sha256', 'sha512', 'blake2b', 'sha3_256']
    
    for algorithm in algorithms_to_test:
        try:
            # 创建哈希对象
            hash_obj = hashlib.new(algorithm)
            # 更新数据（需要先转换为字节）
            hash_obj.update(message.encode('utf-8'))
            # 获取哈希值的十六进制表示
            hash_hex = hash_obj.hexdigest()
            # 获取哈希值的字节表示
            hash_bytes = hash_obj.digest()
            
            print(f"{algorithm.upper()}: {hash_hex}")
            print(f"  - 字节表示长度: {len(hash_bytes)} 字节")
            print(f"  - 哈希值长度: {len(hash_hex)} 字符")
        except ValueError as e:
            print(f"算法 {algorithm} 不可用: {e}")
    
    # 1.3 更简洁的哈希计算方式
    print("\n1.3 简洁的哈希计算方式:")
    
    # 直接使用算法名称作为函数名
    md5_hash = hashlib.md5(message.encode('utf-8')).hexdigest()
    sha256_hash = hashlib.sha256(message.encode('utf-8')).hexdigest()
    
    print(f"MD5 (简洁方式): {md5_hash}")
    print(f"SHA256 (简洁方式): {sha256_hash}")
    
    # 1.4 计算文件的哈希值
    print("\n1.4 计算文件的哈希值:")
    
    # 准备示例文件
    temp_dir, text_file_path, binary_file_path, empty_file_path = prepare_example_files()
    
    try:
        # 函数：计算文件哈希值
        def calculate_file_hash(file_path, algorithm='sha256', chunk_size=8192):
            """计算文件的哈希值"""
            hash_obj = hashlib.new(algorithm)
            with open(file_path, "rb") as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    hash_obj.update(chunk)
            return hash_obj.hexdigest()
        
        # 计算文本文件的哈希值
        text_file_sha256 = calculate_file_hash(text_file_path)
        text_file_md5 = calculate_file_hash(text_file_path, 'md5')
        
        print(f"文本文件 ({os.path.basename(text_file_path)}) 的哈希值:")
        print(f"  SHA256: {text_file_sha256}")
        print(f"  MD5: {text_file_md5}")
        print(f"  文件大小: {os.path.getsize(text_file_path)} 字节")
        
        # 计算二进制文件的哈希值
        binary_file_sha256 = calculate_file_hash(binary_file_path)
        print(f"\n二进制文件 ({os.path.basename(binary_file_path)}) 的哈希值:")
        print(f"  SHA256: {binary_file_sha256}")
        print(f"  文件大小: {os.path.getsize(binary_file_path)} 字节")
        
        # 计算空文件的哈希值
        empty_file_sha256 = calculate_file_hash(empty_file_path)
        empty_file_md5 = calculate_file_hash(empty_file_path, 'md5')
        
        print(f"\n空文件 ({os.path.basename(empty_file_path)}) 的哈希值:")
        print(f"  SHA256: {empty_file_sha256}")
        print(f"  MD5: {empty_file_md5}")
        print(f"  文件大小: {os.path.getsize(empty_file_path)} 字节")
        
    finally:
        # 清理
        cleanup_example_files(temp_dir)

# 2. 哈希对象的增量更新
def incremental_hash_updates():
    """
    哈希对象的增量更新
    
    功能说明：演示如何使用hashlib的增量更新功能，适用于处理大型数据或流式数据。
    """
    print("\n=== 2. 哈希对象的增量更新 ===")
    
    # 2.1 基本增量更新
    print("\n2.1 基本增量更新:")
    
    # 一次性计算哈希值
    full_data = "这是一段很长的数据，我们将演示哈希的增量更新功能。" * 10
   一次性_hash = hashlib.sha256(full_data.encode('utf-8')).hexdigest()
    
    # 增量计算哈希值
    incremental_obj = hashlib.sha256()
    # 将数据分割成多个部分
    parts = []
    current = 0
    part_size = 20  # 每部分20个字符
    while current < len(full_data):
        parts.append(full_data[current:current+part_size])
        current += part_size
    
    print(f"数据被分成了 {len(parts)} 部分")
    
    # 逐部分更新哈希
    for i, part in enumerate(parts, 1):
        incremental_obj.update(part.encode('utf-8'))
        print(f"更新部分 {i}/{len(parts)}: {part[:15]}...")
    
    incremental_hash = incremental_obj.hexdigest()
    
    print(f"\n一次性计算的哈希值: {一次性_hash}")
    print(f"增量计算的哈希值: {incremental_hash}")
    print(f"两个哈希值是否相同: {一次性_hash == incremental_hash}")
    
    # 2.2 处理大型文件的增量哈希计算
    print("\n2.2 大型文件的增量哈希计算:")
    
    # 创建一个临时的大文件
    temp_dir = tempfile.mkdtemp()
    large_file_path = os.path.join(temp_dir, "large_test.txt")
    
    try:
        # 写入大约20MB的数据
        print(f"创建大型测试文件: {large_file_path}")
        start_time = time.time()
        
        with open(large_file_path, "w", encoding="utf-8") as f:
            for i in range(200000):
                f.write(f"这是大型文件的第{i:07d}行，用于测试哈希计算的性能。\n")
        
        file_size = os.path.getsize(large_file_path)
        print(f"文件创建完成，大小: {file_size / (1024*1024):.2f} MB, 耗时: {time.time() - start_time:.2f} 秒")
        
        # 测量不同块大小的性能
        print("\n测试不同块大小的哈希计算性能:")
        print("块大小   | 计算时间(秒) | 内存使用估计")
        print("----------|-------------|-------------")
        
        block_sizes = [1024, 4096, 16384, 65536, 262144, 1048576]  # 1KB到1MB
        
        for block_size in block_sizes:
            start_time = time.time()
            hash_obj = hashlib.sha256()
            
            with open(large_file_path, "rb") as f:
                while True:
                    chunk = f.read(block_size)
                    if not chunk:
                        break
                    hash_obj.update(chunk)
            
            hash_value = hash_obj.hexdigest()
            elapsed = time.time() - start_time
            
            print(f"{block_size/1024:8.0f} KB | {elapsed:11.4f} | 低")
        
        # 展示进度的哈希计算函数
        def calculate_hash_with_progress(file_path, algorithm='sha256', chunk_size=65536):
            """计算文件哈希值并显示进度"""
            file_size = os.path.getsize(file_path)
            hash_obj = hashlib.new(algorithm)
            processed = 0
            last_progress = 0
            
            print(f"开始计算{algorithm.upper()}哈希值...")
            print(f"文件大小: {file_size / (1024*1024):.2f} MB")
            
            start_time = time.time()
            
            with open(file_path, "rb") as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    
                    hash_obj.update(chunk)
                    processed += len(chunk)
                    
                    # 显示进度
                    progress = int((processed / file_size) * 100)
                    if progress > last_progress:
                        elapsed = time.time() - start_time
                        rate = processed / (1024*1024) / elapsed if elapsed > 0 else 0
                        print(f"进度: {progress}% - {rate:.2f} MB/秒", end="\r")
                        last_progress = progress
            
            elapsed = time.time() - start_time
            print(f"进度: 100% - {processed / (1024*1024) / elapsed:.2f} MB/秒")
            print(f"计算完成，耗时: {elapsed:.2f} 秒")
            
            return hash_obj.hexdigest()
        
        print("\n带进度显示的哈希计算:")
        final_hash = calculate_hash_with_progress(large_file_path)
        print(f"最终SHA256哈希值: {final_hash}")
        
    finally:
        # 清理
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"清理临时目录: {temp_dir}")

# 3. 哈希算法比较和性能测试
def hash_algorithm_comparison():
    """
    哈希算法比较和性能测试
    
    功能说明：比较不同哈希算法的安全性、速度和输出大小。
    """
    print("\n=== 3. 哈希算法比较和性能测试 ===")
    
    # 3.1 算法特性比较
    print("\n3.1 算法特性比较:")
    
    algorithm_info = [
        {'name': 'MD5', 'output_size': '128位', 'collision_resistance': '低', 'recommended': '否', 'speed': '快', 'use_case': '文件校验(非安全场景)'},
        {'name': 'SHA1', 'output_size': '160位', 'collision_resistance': '低', 'recommended': '否', 'speed': '快', 'use_case': 'Git对象标识(非安全场景)'},
        {'name': 'SHA256', 'output_size': '256位', 'collision_resistance': '高', 'recommended': '是', 'speed': '中等', 'use_case': '一般安全应用'},
        {'name': 'SHA512', 'output_size': '512位', 'collision_resistance': '高', 'recommended': '是', 'speed': '慢', 'use_case': '高安全性要求'},
        {'name': 'SHA3-256', 'output_size': '256位', 'collision_resistance': '高', 'recommended': '是', 'speed': '慢', 'use_case': '抗侧信道攻击'},
        {'name': 'BLAKE2b', 'output_size': '可变(最多512位)', 'collision_resistance': '高', 'recommended': '是', 'speed': '快', 'use_case': '高性能安全应用'}
    ]
    
    # 打印表格
    print("算法       | 输出大小      | 碰撞抵抗 | 推荐 | 速度 | 典型用例")
    print("-----------|--------------|---------|------|------|--------------------")
    
    for info in algorithm_info:
        print(f"{info['name']:<11} | {info['output_size']:<12} | {info['collision_resistance']:<8} | {info['recommended']:<4} | {info['speed']:<4} | {info['use_case']}")
    
    # 3.2 性能测试
    print("\n3.2 性能测试:")
    
    # 准备不同大小的测试数据
    test_data_sizes = [
        (1024, "1KB"),          # 1KB
        (1024*1024, "1MB"),     # 1MB
        (10*1024*1024, "10MB")  # 10MB
    ]
    
    # 测试的算法
    algorithms_to_test = ['md5', 'sha1', 'sha256', 'sha512', 'sha3_256', 'blake2b']
    
    # 创建临时目录存储测试文件
    temp_dir = tempfile.mkdtemp()
    
    try:
        for size_bytes, size_label in test_data_sizes:
            # 创建测试文件
            test_file_path = os.path.join(temp_dir, f"test_{size_label.replace('B', '').lower()}.dat")
            
            # 生成随机数据
            print(f"\n生成{size_label}测试数据...")
            with open(test_file_path, "wb") as f:
                # 使用os.urandom生成随机数据
                chunks = size_bytes // 1024 * 1024  # 每次读取1MB
                remaining = size_bytes
                
                while remaining > 0:
                    chunk_size = min(remaining, 1024*1024)
                    data = os.urandom(chunk_size)
                    f.write(data)
                    remaining -= chunk_size
            
            print(f"{size_label}测试文件创建完成")
            print("\n各算法性能测试结果:")
            print("算法       | 哈希值                                     | 计算时间(秒) | 速度(MB/s)")
            print("-----------|------------------------------------------|-------------|----------")
            
            for algorithm in algorithms_to_test:
                try:
                    # 测量计算时间
                    start_time = time.time()
                    hash_obj = hashlib.new(algorithm)
                    
                    with open(test_file_path, "rb") as f:
                        while True:
                            chunk = f.read(65536)
                            if not chunk:
                                break
                            hash_obj.update(chunk)
                    
                    hash_value = hash_obj.hexdigest()
                    elapsed = time.time() - start_time
                    speed = (size_bytes / (1024*1024)) / elapsed
                    
                    print(f"{algorithm.upper():<11} | {hash_value[:36]:<38} | {elapsed:11.4f} | {speed:8.2f}")
                    
                except ValueError as e:
                    print(f"{algorithm.upper():<11} | {'不可用':<38} | {'N/A':>11} | {'N/A':>8}")
    
    finally:
        # 清理
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"\n清理临时目录: {temp_dir}")
    
    # 3.3 安全性建议
    print("\n3.3 安全性建议:")
    print("1. 哈希算法选择指南:")
    print("   - 安全敏感应用: 选择SHA-256, SHA-384, SHA-512或BLAKE2b")
    print("   - 一般安全应用: SHA-256通常足够")
    print("   - 高性能需求: BLAKE2b提供较好的速度和安全性平衡")
    print("   - 避免使用: MD5和SHA1，它们存在已知的碰撞攻击")
    
    print("\n2. 哈希应用安全注意事项:")
    print("   - 密码存储: 必须使用盐值和慢哈希函数(如bcrypt, Argon2)")
    print("   - 文件完整性: SHA-256或SHA-512是不错的选择")
    print("   - 数字签名: 应使用非对称加密，哈希仅作为其一部分")
    print("   - 敏感数据: 考虑使用带密钥的哈希(HMAC)")

# 4. 哈希在安全领域的应用
def security_applications():
    """
    哈希在安全领域的应用
    
    功能说明：演示哈希在密码存储、文件完整性验证等安全场景中的应用。
    """
    print("\n=== 4. 哈希在安全领域的应用 ===")
    
    # 4.1 密码存储示例（注意：实际应用应使用专门的密码哈希库）
    print("\n4.1 密码存储模拟:")
    print("注意: 这只是演示，实际密码存储应使用bcrypt、Argon2等专门的密码哈希函数!")
    
    def create_password_hash(password, salt=None):
        """模拟创建密码哈希（带盐值）"""
        # 生成随机盐值
        if salt is None:
            salt = os.urandom(16)  # 16字节随机盐
        
        # 组合密码和盐值
        password_with_salt = password.encode('utf-8') + salt
        
        # 使用SHA-256计算哈希
        hash_obj = hashlib.sha256()
        hash_obj.update(password_with_salt)
        password_hash = hash_obj.digest()
        
        # 返回盐值和哈希的组合（使用十六进制表示以便存储）
        return binascii.hexlify(salt).decode('ascii') + ':' + binascii.hexlify(password_hash).decode('ascii')
    
    def verify_password(stored_hash, password):
        """验证密码"""
        # 分割盐值和哈希
        salt_hex, stored_password_hash_hex = stored_hash.split(':', 1)
        salt = binascii.unhexlify(salt_hex)
        stored_password_hash = binascii.unhexlify(stored_password_hash_hex)
        
        # 使用相同的盐值计算输入密码的哈希
        password_with_salt = password.encode('utf-8') + salt
        hash_obj = hashlib.sha256()
        hash_obj.update(password_with_salt)
        password_hash = hash_obj.digest()
        
        # 比较哈希值（使用常量时间比较以防止计时攻击）
        return hmac.compare_digest(password_hash, stored_password_hash)
    
    # 测试密码存储和验证
    test_passwords = ["Password123", "超级安全的密码!"]
    
    for password in test_passwords:
        print(f"\n密码: {password}")
        
        # 创建哈希
        hash1 = create_password_hash(password)
        print(f"存储的哈希值: {hash1}")
        
        # 再次创建哈希（应该不同，因为盐值随机）
        hash2 = create_password_hash(password)
        print(f"另一个哈希值: {hash2}")
        print(f"两次哈希值是否不同: {hash1 != hash2}")
        
        # 验证正确密码
        is_valid = verify_password(hash1, password)
        print(f"正确密码验证: {'通过' if is_valid else '失败'}")
        
        # 验证错误密码
        is_valid = verify_password(hash1, password + "错误")
        print(f"错误密码验证: {'通过' if is_valid else '失败'}")
    
    # 说明为什么实际应用应该使用专门的密码哈希函数
    print("\n为什么不应该直接使用hashlib存储密码:")
    print("1. 速度太快 - 容易受到暴力破解攻击")
    print("2. 没有自适应工作因子 - 无法随计算能力增长调整难度")
    print("3. 缺少内存硬化特性 - 不能抵御专用硬件攻击")
    print("4. 推荐的替代方案: bcrypt、Argon2、PBKDF2")
    
    # 4.2 文件完整性验证
    print("\n4.2 文件完整性验证:")
    
    # 准备示例文件
    temp_dir, text_file_path, binary_file_path, _ = prepare_example_files()
    
    try:
        # 创建文件校验和
        def create_file_checksum(file_path, output_path=None):
            """创建文件校验和文件"""
            file_name = os.path.basename(file_path)
            
            # 计算多种哈希值
            hash_algorithms = ['sha256', 'sha512', 'md5']
            checksums = {}
            
            for algo in hash_algorithms:
                hash_obj = hashlib.new(algo)
                with open(file_path, "rb") as f:
                    while True:
                        chunk = f.read(65536)
                        if not chunk:
                            break
                        hash_obj.update(chunk)
                checksums[algo] = hash_obj.hexdigest()
            
            # 生成校验和内容
            checksum_content = f"# 文件校验和 - 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            checksum_content += f"# 文件名: {file_name}\n"
            checksum_content += f"# 文件大小: {os.path.getsize(file_path)} 字节\n\n"
            
            for algo, hash_value in checksums.items():
                checksum_content += f"{algo.upper()}: {hash_value}\n"
            
            # 保存校验和文件
            if output_path is None:
                output_path = f"{file_path}.sha256"
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(checksum_content)
            
            return output_path, checksums
        
        # 验证文件完整性
        def verify_file_checksum(file_path, checksum_file_path):
            """验证文件校验和"""
            # 读取校验和文件
            expected_checksums = {}
            
            with open(checksum_file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    if ':' in line:
                        algo, hash_value = line.split(':', 1)
                        expected_checksums[algo.strip().lower()] = hash_value.strip()
            
            # 计算实际哈希值
            actual_checksums = {}
            
            for algo in expected_checksums.keys():
                hash_obj = hashlib.new(algo)
                with open(file_path, "rb") as f:
                    while True:
                        chunk = f.read(65536)
                        if not chunk:
                            break
                        hash_obj.update(chunk)
                actual_checksums[algo] = hash_obj.hexdigest()
            
            # 比较
            results = {}
            all_valid = True
            
            for algo, expected in expected_checksums.items():
                actual = actual_checksums.get(algo, "")
                is_valid = expected == actual
                results[algo] = is_valid
                if not is_valid:
                    all_valid = False
            
            return all_valid, results, expected_checksums, actual_checksums
        
        # 测试校验和创建和验证
        print(f"测试文本文件: {text_file_path}")
        checksum_file, _ = create_file_checksum(text_file_path)
        print(f"创建校验和文件: {checksum_file}")
        
        # 验证原始文件
        is_valid, results, expected, actual = verify_file_checksum(text_file_path, checksum_file)
        print(f"\n文件完整性验证结果: {'通过' if is_valid else '失败'}")
        
        for algo in sorted(results.keys()):
            print(f"  {algo.upper()}: {'通过' if results[algo] else '失败'}")
            if not results[algo]:
                print(f"    期望: {expected[algo]}")
                print(f"    实际: {actual[algo]}")
        
        # 模拟文件被修改
        print("\n模拟文件被修改...")
        with open(text_file_path, "ab") as f:
            f.write(b"\n这是恶意添加的内容。")
        
        # 验证被修改的文件
        is_valid, results, expected, actual = verify_file_checksum(text_file_path, checksum_file)
        print(f"\n修改后文件完整性验证结果: {'通过' if is_valid else '失败'}")
        
        for algo in sorted(results.keys()):
            print(f"  {algo.upper()}: {'通过' if results[algo] else '失败'}")
            if not results[algo]:
                print(f"    期望: {expected[algo]}")
                print(f"    实际: {actual[algo]}")
    
    finally:
        # 清理
        cleanup_example_files(temp_dir)
    
    # 4.3 使用hmac进行消息认证
    print("\n4.3 使用hmac进行消息认证:")
    print("HMAC (Hash-based Message Authentication Code) 结合了哈希函数和密钥")
    
    import hmac
    
    # 创建HMAC
    def create_hmac(message, key):
        """创建HMAC"""
        # 确保密钥是字节
        if isinstance(key, str):
            key = key.encode('utf-8')
        
        # 创建HMAC对象
        hmac_obj = hmac.new(key, message.encode('utf-8'), hashlib.sha256)
        
        # 返回十六进制表示的HMAC值
        return hmac_obj.hexdigest()
    
    # 验证HMAC
    def verify_hmac(message, key, hmac_value):
        """验证HMAC"""
        # 计算当前消息的HMAC
        current_hmac = create_hmac(message, key)
        
        # 使用hmac.compare_digest进行安全比较（防止计时攻击）
        return hmac.compare_digest(current_hmac, hmac_value)
    
    # 测试HMAC
    secret_key = "这是一个密钥，应该安全存储"
    test_message = "这是一条需要认证的消息"
    
    print(f"消息: {test_message}")
    print(f"密钥: {secret_key}")
    
    # 创建HMAC
    hmac_value = create_hmac(test_message, secret_key)
    print(f"HMAC (SHA-256): {hmac_value}")
    
    # 验证正确的HMAC
    is_valid = verify_hmac(test_message, secret_key, hmac_value)
    print(f"验证结果: {'通过' if is_valid else '失败'}")
    
    # 尝试篡改消息
    tampered_message = test_message + "，已被篡改"
    is_valid = verify_hmac(tampered_message, secret_key, hmac_value)
    print(f"\n篡改消息后的验证结果: {'通过' if is_valid else '失败'}")
    
    # 尝试使用错误的密钥
    wrong_key = "这是错误的密钥"
    is_valid = verify_hmac(test_message, wrong_key, hmac_value)
    print(f"使用错误密钥的验证结果: {'通过' if is_valid else '失败'}")

# 5. 高级哈希应用
def advanced_hash_applications():
    """
    高级哈希应用
    
    功能说明：演示一些高级哈希应用，如文件去重、分片哈希、自定义哈希等。
    """
    print("\n=== 5. 高级哈希应用 ===")
    
    # 5.1 文件去重工具
    print("\n5.1 文件去重工具:")
    
    # 创建测试目录和重复文件
    temp_dir = tempfile.mkdtemp()
    print(f"创建测试目录: {temp_dir}")
    
    # 创建子目录
    subdir1 = os.path.join(temp_dir, "subdir1")
    subdir2 = os.path.join(temp_dir, "subdir2")
    os.makedirs(subdir1, exist_ok=True)
    os.makedirs(subdir2, exist_ok=True)
    
    try:
        # 创建一些文件
        # 唯一文件
        unique1_path = os.path.join(temp_dir, "unique1.txt")
        with open(unique1_path, "w", encoding="utf-8") as f:
            f.write("这是第一个唯一文件的内容。\n")
            
        # 唯一文件2
        unique2_path = os.path.join(temp_dir, "unique2.txt")
        with open(unique2_path, "w", encoding="utf-8") as f:
            f.write("这是第二个唯一文件的内容。\n")
        
        # 创建重复文件
        original_path = os.path.join(temp_dir, "original.txt")
        with open(original_path, "w", encoding="utf-8") as f:
            f.write("这是一个将会被复制的原始文件。\n")
            f.write("它将在不同目录中有多个副本。\n")
        
        # 创建副本
        copy1_path = os.path.join(subdir1, "copy1.txt")
        copy2_path = os.path.join(subdir1, "copy2.txt")
        copy3_path = os.path.join(subdir2, "copy3.txt")
        
        import shutil
        shutil.copy2(original_path, copy1_path)
        shutil.copy2(original_path, copy2_path)
        shutil.copy2(original_path, copy3_path)
        
        # 文件去重函数
        def find_duplicate_files(directory, algorithm='sha256', min_size=0):
            """
            查找目录中的重复文件
            
            参数:
            - directory: 要扫描的目录
            - algorithm: 使用的哈希算法
            - min_size: 最小文件大小（字节）
            
            返回:
            - 重复文件的字典，键为哈希值，值为文件路径列表
            """
            # 存储文件哈希值和路径的字典
            file_hashes = {}
            
            # 遍历目录
            total_files = 0
            processed_files = 0
            
            print(f"开始扫描目录: {directory}")
            print(f"使用算法: {algorithm.upper()}, 最小文件大小: {min_size} 字节")
            
            # 首先计算总文件数
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.isfile(file_path) and os.path.getsize(file_path) >= min_size:
                        total_files += 1
            
            print(f"找到 {total_files} 个符合条件的文件")
            
            # 计算哈希值
            start_time = time.time()
            
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    
                    # 检查文件大小
                    try:
                        file_size = os.path.getsize(file_path)
                        if file_size < min_size:
                            continue
                        
                        # 计算哈希值
                        hash_obj = hashlib.new(algorithm)
                        with open(file_path, "rb") as f:
                            while True:
                                chunk = f.read(65536)
                                if not chunk:
                                    break
                                hash_obj.update(chunk)
                        
                        file_hash = hash_obj.hexdigest()
                        
                        # 存储哈希值和路径
                        if file_hash in file_hashes:
                            file_hashes[file_hash].append((file_path, file_size))
                        else:
                            file_hashes[file_hash] = [(file_path, file_size)]
                        
                        processed_files += 1
                        
                        # 显示进度
                        if processed_files % 10 == 0 or processed_files == total_files:
                            progress = (processed_files / total_files) * 100
                            elapsed = time.time() - start_time
                            rate = processed_files / elapsed if elapsed > 0 else 0
                            print(f"进度: {processed_files}/{total_files} ({progress:.1f}%) - {rate:.1f} 文件/秒", end="\r")
                            
                    except (IOError, PermissionError) as e:
                        print(f"\n无法处理文件 {file_path}: {e}")
            
            elapsed = time.time() - start_time
            print(f"\n扫描完成，耗时: {elapsed:.2f} 秒 - 平均速度: {processed_files / elapsed:.1f} 文件/秒")
            
            # 提取重复文件
            duplicates = {}
            total_duplicate_size = 0
            total_duplicate_files = 0
            
            for file_hash, file_list in file_hashes.items():
                if len(file_list) > 1:
                    duplicates[file_hash] = file_list
                    # 计算重复占用的空间（减去一个原始文件）
                    total_duplicate_files += len(file_list) - 1
                    total_duplicate_size += (len(file_list) - 1) * file_list[0][1]
            
            print(f"找到 {len(duplicates)} 组重复文件")
            print(f"总重复文件数: {total_duplicate_files}")
            print(f"可回收空间: {total_duplicate_size / (1024):.2f} KB")
            
            return duplicates
        
        # 执行文件去重
        duplicates = find_duplicate_files(temp_dir)
        
        # 显示重复文件
        print("\n重复文件详情:")
        for i, (hash_value, file_list) in enumerate(duplicates.items(), 1):
            print(f"\n组 {i} (哈希值: {hash_value[:16]}...):")
            print(f"  发现 {len(file_list)} 个相同文件，大小: {file_list[0][1]} 字节")
            for file_path, _ in file_list:
                relative_path = os.path.relpath(file_path, temp_dir)
                print(f"    {relative_path}")
    
    finally:
        # 清理
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"\n清理临时目录: {temp_dir}")
    
    # 5.2 分片哈希计算
    print("\n5.2 分片哈希计算:")
    print("分片哈希可用于大文件的部分验证和断点续传")
    
    # 创建一个测试文件
    temp_dir = tempfile.mkdtemp()
    large_file_path = os.path.join(temp_dir, "large_chunk_test.dat")
    
    try:
        # 写入测试数据
        print(f"创建测试文件: {large_file_path}")
        chunk_size = 4 * 1024 * 1024  # 4MB块
        total_chunks = 5  # 总共20MB
        
        with open(large_file_path, "wb") as f:
            for i in range(total_chunks):
                # 为每个块生成唯一的数据
                chunk_data = f"这是块 {i} 的测试数据，包含一些随机内容。".encode('utf-8')
                # 填充到4MB
                chunk = chunk_data * (chunk_size // len(chunk_data) + 1)[:chunk_size]
                f.write(chunk)
        
        print(f"文件创建完成，大小: {os.path.getsize(large_file_path) / (1024*1024):.2f} MB")
        print(f"使用 {chunk_size / (1024*1024):.0f} MB 大小的块")
        
        # 计算分片哈希
        def calculate_chunked_hash(file_path, chunk_size=1024*1024, algorithm='sha256'):
            """计算文件的分片哈希"""
            chunk_hashes = []
            file_size = os.path.getsize(file_path)
            total_chunks = (file_size + chunk_size - 1) // chunk_size  # 向上取整
            
            print(f"开始计算分片哈希，总块数: {total_chunks}")
            
            with open(file_path, "rb") as f:
                for i in range(total_chunks):
                    # 读取块数据
                    chunk = f.read(chunk_size)
                    
                    # 计算块哈希
                    hash_obj = hashlib.new(algorithm)
                    hash_obj.update(chunk)
                    chunk_hash = hash_obj.hexdigest()
                    chunk_hashes.append(chunk_hash)
                    
                    # 显示进度
                    progress = ((i + 1) / total_chunks) * 100
                    print(f"进度: {i+1}/{total_chunks} ({progress:.1f}%)", end="\r")
            
            print()
            
            # 计算整体哈希（可选）
            hash_obj = hashlib.new(algorithm)
            with open(file_path, "rb") as f:
                while True:
                    chunk = f.read(65536)
                    if not chunk:
                        break
                    hash_obj.update(chunk)
            whole_file_hash = hash_obj.hexdigest()
            
            return {
                'file_size': file_size,
                'chunk_size': chunk_size,
                'total_chunks': total_chunks,
                'chunk_hashes': chunk_hashes,
                'whole_file_hash': whole_file_hash,
                'algorithm': algorithm
            }
        
        # 执行分片哈希计算
        chunk_hash_result = calculate_chunked_hash(large_file_path, chunk_size)
        
        # 显示结果
        print("\n分片哈希计算结果:")
        print(f"文件大小: {chunk_hash_result['file_size']} 字节")
        print(f"块大小: {chunk_hash_result['chunk_size']} 字节")
        print(f"总块数: {chunk_hash_result['total_chunks']}")
        print(f"文件整体哈希: {chunk_hash_result['whole_file_hash']}")
        
        # 显示部分分片哈希
        print("\n分片哈希示例:")
        for i, hash_value in enumerate(chunk_hash_result['chunk_hashes'][:3]):
            print(f"块 {i}: {hash_value}")
        
        if len(chunk_hash_result['chunk_hashes']) > 3:
            print(f"... 共 {len(chunk_hash_result['chunk_hashes'])} 个块")
        
        # 模拟验证部分文件
        print("\n验证部分文件示例:")
        
        # 验证第一个块
        with open(large_file_path, "rb") as f:
            first_chunk = f.read(chunk_size)
        
        hash_obj = hashlib.new(chunk_hash_result['algorithm'])
        hash_obj.update(first_chunk)
        calculated_hash = hash_obj.hexdigest()
        expected_hash = chunk_hash_result['chunk_hashes'][0]
        
        print(f"第一个块验证: {'通过' if calculated_hash == expected_hash else '失败'}")
        
    finally:
        # 清理
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"清理临时目录: {temp_dir}")

# 6. 密钥派生函数(KDF)
def key_derivation_functions():
    """
    密钥派生函数(KDF)
    
    功能说明：演示使用hashlib的密钥派生函数，用于从密码生成加密密钥。
    """
    print("\n=== 6. 密钥派生函数(KDF) ===")
    
    # 6.1 使用pbkdf2_hmac
    print("\n6.1 使用pbkdf2_hmac:")
    print("PBKDF2 (Password-Based Key Derivation Function 2) 是一种从密码派生密钥的算法")
    
    # 生成密钥
    def derive_key_from_password(password, salt=None, iterations=100000, key_length=32):
        """从密码派生密钥"""
        # 如果没有提供盐值，生成一个随机盐值
        if salt is None:
            salt = os.urandom(16)
        
        # 确保密码是字节
        if isinstance(password, str):
            password = password.encode('utf-8')
        
        # 使用PBKDF2派生密钥
        key = hashlib.pbkdf2_hmac(
            'sha256',  # 哈希算法
            password,  # 密码
            salt,      # 盐值
            iterations,  # 迭代次数
            dklen=key_length  # 派生密钥的长度
        )
        
        return {
            'key': key,
            'salt': salt,
            'iterations': iterations,
            'key_length': key_length,
            'algorithm': 'sha256'
        }
    
    # 测试密钥派生
    test_password = "我的强密码123!"
    print(f"原始密码: {test_password}")
    
    # 使用不同的迭代次数
    for iterations in [10000, 100000, 500000]:
        start_time = time.time()
        result = derive_key_from_password(test_password, iterations=iterations)
        elapsed = time.time() - start_time
        
        print(f"\n迭代次数: {iterations}")
        print(f"派生密钥(十六进制): {binascii.hexlify(result['key']).decode('ascii')}")
        print(f"盐值(十六进制): {binascii.hexlify(result['salt']).decode('ascii')}")
        print(f"派生时间: {elapsed:.4f} 秒")
        print(f"密钥长度: {result['key_length']} 字节")
    
    # 验证相同密码和盐值产生相同的密钥
    print("\n验证相同参数产生相同密钥:")
    result1 = derive_key_from_password(test_password)
    # 使用相同的盐值再次派生
    result2 = derive_key_from_password(test_password, salt=result1['salt'])
    
    print(f"两次派生的密钥是否相同: {result1['key'] == result2['key']}")
    print(f"使用不同盐值时密钥是否不同: {derive_key_from_password(test_password)['key'] != result1['key']}")
    
    # 6.2 KDF的应用场景
    print("\n6.2 KDF的应用场景:")
    print("1. 密码存储")
    print("   - 存储从密码派生的哈希值，而非密码本身")
    print("   - 增加迭代次数提高破解难度")
    
    print("\n2. 加密密钥生成")
    print("   - 从用户密码生成用于加密的密钥")
    print("   - 用于文件加密、数据加密等")
    
    print("\n3. 安全存储建议:")
    print("   - 存储盐值、迭代次数和派生的哈希值")
    print("   - 盐值应该对每个用户不同")
    print("   - 迭代次数应该足够大，但又不至于影响用户体验")
    print("   - 对于现代系统，建议至少100,000次迭代")
    
    # 6.3 使用scrypt（如果可用）
    print("\n6.3 使用scrypt:")
    
    # 检查scrypt是否可用
    if hasattr(hashlib, 'scrypt'):
        print("scrypt算法可用，提供更好的安全性和性能")
        
        def derive_key_with_scrypt(password, salt=None, N=16384, r=8, p=1, key_length=32):
            """使用scrypt派生密钥"""
            # 如果没有提供盐值，生成一个随机盐值
            if salt is None:
                salt = os.urandom(16)
            
            # 确保密码是字节
            if isinstance(password, str):
                password = password.encode('utf-8')
            
            # 使用scrypt派生密钥
            key = hashlib.scrypt(
                password,
                salt=salt,
                n=N,      # CPU/内存成本因子
                r=r,      # 块大小
                p=p,      # 并行化因子
                dklen=key_length
            )
            
            return {
                'key': key,
                'salt': salt,
                'N': N,
                'r': r,
                'p': p,
                'key_length': key_length
            }
        
        # 测试scrypt
        start_time = time.time()
        scrypt_result = derive_key_with_scrypt(test_password)
        elapsed = time.time() - start_time
        
        print(f"scrypt参数:")
        print(f"  N (CPU/内存成本): {scrypt_result['N']}")
        print(f"  r (块大小): {scrypt_result['r']}")
        print(f"  p (并行因子): {scrypt_result['p']}")
        print(f"派生密钥(十六进制): {binascii.hexlify(scrypt_result['key']).decode('ascii')}")
        print(f"派生时间: {elapsed:.4f} 秒")
        
        # 比较pbkdf2和scrypt
        print("\nPBKDF2 vs scrypt 性能比较:")
        
        # pbkdf2
        start_time = time.time()
        pbkdf2_result = derive_key_from_password(test_password, iterations=100000)
        pbkdf2_time = time.time() - start_time
        
        # scrypt（使用较小的N值以获得相似的时间）
        start_time = time.time()
        scrypt_result = derive_key_with_scrypt(test_password, N=8192)
        scrypt_time = time.time() - start_time
        
        print(f"PBKDF2 (100,000次迭代): {pbkdf2_time:.4f} 秒")
        print(f"scrypt (N=8192): {scrypt_time:.4f} 秒")
        
    else:
        print("scrypt算法在当前Python版本中不可用")
        print("scrypt比PBKDF2提供更好的抗ASIC和GPU攻击能力")

# 7. hashlib模块最佳实践总结
def best_practices_summary():
    """
    hashlib模块最佳实践总结
    
    功能说明：总结使用hashlib模块的最佳实践和安全建议。
    """
    print("\n=== 7. hashlib模块最佳实践总结 ===")
    
    print("\n7.1 哈希算法选择指南:")
    print("1. 安全应用的算法选择:")
    print("   - 推荐使用: SHA-256, SHA-384, SHA-512, SHA3-256, BLAKE2b")
    print("   - 避免使用: MD5, SHA1")
    print("   - 高安全性需求: SHA-512或BLAKE2b")
    print("   - 平衡安全性和性能: SHA-256或BLAKE2b")
    
    print("\n2. 不同应用场景的选择:")
    print("   - 文件校验和: SHA-256或SHA-512")
    print("   - 数据去重: SHA-256")
    print("   - 消息认证: HMAC-SHA256")
    print("   - 密钥派生: pbkdf2_hmac或scrypt")
    print("   - 密码存储: 使用专门的库如bcrypt、Argon2")
    
    print("\n7.2 安全性最佳实践:")
    print("1. 通用安全建议:")
    print("   - 始终使用随机盐值")
    print("   - 使用足够的迭代次数")
    print("   - 保护哈希值和盐值")
    print("   - 定期更新算法和参数")
    
    print("\n2. 避免常见安全错误:")
    print("   - 不要在没有盐值的情况下存储密码哈希")
    print("   - 不要使用固定盐值")
    print("   - 不要低估迭代次数")
    print("   - 不要直接比较哈希值（使用hmac.compare_digest）")
    print("   - 不要向用户泄露哈希值或盐值")
    
    print("\n7.3 性能优化技巧:")
    print("1. 哈希计算优化:")
    print("   - 处理大文件时使用分块读取")
    print("   - 选择合适的块大小（通常64KB左右）")
    print("   - 使用增量更新而非一次性加载数据")
    print("   - 对频繁使用的数据缓存哈希值")
    
    print("\n2. 内存使用优化:")
    print("   - 避免同时加载多个大文件到内存")
    print("   - 使用生成器处理文件流")
    print("   - 及时释放不再需要的哈希对象")
    
    print("\n7.4 错误处理和日志记录:")
    print("1. 适当的错误处理:")
    print("   - 捕获并处理文件IO异常")
    print("   - 验证哈希算法是否可用")
    print("   - 处理可能的内存错误")
    print("   - 实现超时机制以避免长时间阻塞")
    
    print("\n2. 日志记录建议:")
    print("   - 记录哈希操作的结果（但不记录原始数据）")
    print("   - 记录异常情况")
    print("   - 避免记录敏感信息（密码、密钥）")
    print("   - 记录性能指标用于优化")
    
    print("\n7.5 常见问题及解决方案:")
    print("1. 哈希碰撞问题:")
    print("   - 使用更长的哈希算法（如从SHA-256升级到SHA-512）")
    print("   - 使用双哈希策略（计算两个不同算法的哈希值）")
    print("   - 使用带密钥的哈希（HMAC）")
    
    print("\n2. 性能与安全性平衡:")
    print("   - 选择适合场景的哈希算法")
    print("   - 动态调整迭代次数")
    print("   - 使用硬件加速（如可用）")
    print("   - 实施缓存策略")
    
    print("\n3. 兼容性问题:")
    print("   - 使用algorithms_guaranteed检查算法可用性")
    print("   - 提供算法降级机制")
    print("   - 确保跨平台一致性")
    print("   - 明确记录使用的哈希算法和参数")

# 运行所有示例
def run_all_examples():
    print("====================================")
    print("Python hashlib模块功能详解")
    print("====================================")
    
    # 1. 基本使用
    basic_hashlib_usage()
    
    # 2. 增量更新
    incremental_hash_updates()
    
    # 3. 算法比较
    hash_algorithm_comparison()
    
    # 4. 安全应用
    security_applications()
    
    # 5. 高级应用
    advanced_hash_applications()
    
    # 6. 密钥派生函数
    key_derivation_functions()
    
    # 7. 最佳实践总结
    best_practices_summary()
    
    print("\n====================================")
    print("hashlib模块示例演示完成")
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

Python的hashlib模块提供了一套完整的哈希算法实现，是数据安全和完整性验证的重要工具。本教程全面介绍了hashlib的功能和应用：

1. **基本哈希计算**：支持各种哈希算法，可处理字符串和文件数据
2. **增量更新功能**：适合处理大型数据或流式数据
3. **算法比较**：不同哈希算法的安全性、速度和适用场景对比
4. **安全应用**：密码存储模拟、文件完整性验证、消息认证(HMAC)
5. **高级应用**：文件去重工具、分片哈希计算
6. **密钥派生**：PBKDF2和scrypt等KDF函数的使用
7. **最佳实践**：安全建议、性能优化、错误处理

使用hashlib模块时，务必注意安全最佳实践，特别是在处理敏感数据时。对于密码存储等关键安全场景，应优先考虑使用专门的密码哈希库（如bcrypt、Argon2），而不是直接使用hashlib。

hashlib模块在数据完整性验证、文件校验、数据去重等方面表现出色，是Python中处理哈希相关操作的标准工具。通过合理选择算法和参数，可以在安全性和性能之间找到最佳平衡点。

"""