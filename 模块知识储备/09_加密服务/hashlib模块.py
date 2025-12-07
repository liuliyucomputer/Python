#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hashlib模块 - 哈希算法实现

hashlib模块提供了多种安全哈希算法和消息摘要算法的实现，
可用于数据完整性验证、密码安全存储等场景。

主要支持的算法包括：
- MD5 (Message Digest Algorithm 5)
- SHA-1 (Secure Hash Algorithm 1)
- SHA-224, SHA-256, SHA-384, SHA-512 (SHA-2系列)
- SHA-3系列 (SHA3-224, SHA3-256, SHA3-384, SHA3-512)
- BLAKE2系列 (BLAKE2b, BLAKE2s)

使用场景：
- 验证文件完整性
- 安全存储密码
- 生成数据指纹
- 数字签名
"""

import hashlib
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. hashlib模块基本介绍")
print("=" * 50)
print("hashlib模块提供了多种哈希算法的实现")
print("支持MD5、SHA-1、SHA-2系列、SHA-3系列和BLAKE2系列算法")
print("用于数据完整性验证、密码安全存储等场景")

# ===========================
# 2. 哈希对象的基本用法
# ===========================
print("\n" + "=" * 50)
print("2. 哈希对象的基本用法")
print("=" * 50)

# 创建MD5哈希对象
print("演示创建和使用MD5哈希对象:")
md5_hash = hashlib.md5()
md5_hash.update(b"Hello, hashlib!")  # 更新哈希对象
result = md5_hash.hexdigest()  # 获取十六进制表示的哈希值
print(f"MD5哈希值: {result}")
print(f"哈希值长度: {len(result)} 字符")

# 创建SHA-256哈希对象
print("\n演示创建和使用SHA-256哈希对象:")
sha256_hash = hashlib.sha256()
sha256_hash.update(b"Hello, hashlib!")
result = sha256_hash.hexdigest()
print(f"SHA-256哈希值: {result}")
print(f"哈希值长度: {len(result)} 字符")

# 创建SHA-512哈希对象
print("\n演示创建和使用SHA-512哈希对象:")
sha512_hash = hashlib.sha512()
sha512_hash.update(b"Hello, hashlib!")
result = sha512_hash.hexdigest()
print(f"SHA-512哈希值: {result}")
print(f"哈希值长度: {len(result)} 字符")

# ===========================
# 3. 简化用法
# ===========================
print("\n" + "=" * 50)
print("3. 简化用法")
print("=" * 50)

# 使用简写方式创建哈希对象
print("演示使用简写方式创建哈希对象:")
md5_result = hashlib.md5(b"Hello, hashlib!").hexdigest()
print(f"MD5哈希值(简写): {md5_result}")

sha256_result = hashlib.sha256(b"Hello, hashlib!").hexdigest()
print(f"SHA-256哈希值(简写): {sha256_result}")

# ===========================
# 4. 处理大文件
# ===========================
print("\n" + "=" * 50)
print("4. 处理大文件")
print("=" * 50)

# 创建一个临时大文件用于演示
def create_large_file(filename, size_mb):
    """创建指定大小的临时文件"""
    with open(filename, "wb") as f:
        # 每次写入1MB数据
        chunk_size = 1024 * 1024
        for _ in range(size_mb):
            f.write(os.urandom(chunk_size))

# 计算文件的哈希值
def calculate_file_hash(filename, algorithm="sha256", chunk_size=8192):
    """计算文件的哈希值"""
    hash_obj = hashlib.new(algorithm)
    with open(filename, "rb") as f:
        while chunk := f.read(chunk_size):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# 演示计算大文件哈希
print("演示计算大文件哈希:")
temp_file = "temp_large_file.bin"
create_large_file(temp_file, 10)  # 创建10MB临时文件

file_hash = calculate_file_hash(temp_file)
print(f"文件 '{temp_file}' 的SHA-256哈希值: {file_hash}")

# 清理临时文件
os.remove(temp_file)

# ===========================
# 5. 动态选择哈希算法
# ===========================
print("\n" + "=" * 50)
print("5. 动态选择哈希算法")
print("=" * 50)

# 获取支持的哈希算法列表
print("支持的哈希算法:")
for algorithm in hashlib.algorithms_available:
    print(f"  - {algorithm}")

# 动态创建哈希对象
print("\n演示动态选择哈希算法:")
message = b"Hello, dynamic hashing!"
for algorithm in ["md5", "sha1", "sha256", "sha512", "sha3_256"]:
    if algorithm in hashlib.algorithms_available:
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(message)
        print(f"{algorithm}: {hash_obj.hexdigest()}")

# ===========================
# 6. SHA-3系列算法
# ===========================
print("\n" + "=" * 50)
print("6. SHA-3系列算法")
print("=" * 50)

# SHA-3系列算法示例
print("SHA-3系列算法示例:")
message = b"Hello, SHA-3!"

sha3_224 = hashlib.sha3_224(message).hexdigest()
print(f"SHA3-224: {sha3_224}")

sha3_256 = hashlib.sha3_256(message).hexdigest()
print(f"SHA3-256: {sha3_256}")

sha3_384 = hashlib.sha3_384(message).hexdigest()
print(f"SHA3-384: {sha3_384}")

sha3_512 = hashlib.sha3_512(message).hexdigest()
print(f"SHA3-512: {sha3_512}")

# ===========================
# 7. BLAKE2系列算法
# ===========================
print("\n" + "=" * 50)
print("7. BLAKE2系列算法")
print("=" * 50)

# BLAKE2b算法（适合64位系统）
print("BLAKE2b算法示例:")
blake2b_hash = hashlib.blake2b(b"Hello, BLAKE2b!")
print(f"BLAKE2b哈希值: {blake2b_hash.hexdigest()}")

# BLAKE2s算法（适合32位系统）
print("\nBLAKE2s算法示例:")
blake2s_hash = hashlib.blake2s(b"Hello, BLAKE2s!")
print(f"BLAKE2s哈希值: {blake2s_hash.hexdigest()}")

# 使用密钥的BLAKE2（相当于HMAC）
print("\n使用密钥的BLAKE2算法:")
key = b"secret_key"
blake2b_keyed = hashlib.blake2b(b"Hello, keyed BLAKE2b!", key=key)
print(f"带密钥的BLAKE2b哈希值: {blake2b_keyed.hexdigest()}")

# ===========================
# 8. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("8. 实际应用示例")
print("=" * 50)

# 示例1: 文件完整性验证
def verify_file_integrity(file_path, expected_hash, algorithm="sha256"):
    """验证文件完整性"""
    file_hash = calculate_file_hash(file_path, algorithm)
    if file_hash == expected_hash:
        print(f"✓ 文件 {file_path} 完整性验证通过")
        return True
    else:
        print(f"✗ 文件 {file_path} 完整性验证失败")
        print(f"  预期哈希值: {expected_hash}")
        print(f"  实际哈希值: {file_hash}")
        return False

# 演示文件完整性验证
print("示例1: 文件完整性验证")
# 创建测试文件
with open("test_file.txt", "w") as f:
    f.write("This is a test file for integrity verification")

# 计算预期哈希值
expected_hash = hashlib.sha256(b"This is a test file for integrity verification").hexdigest()

# 验证文件完整性
verify_file_integrity("test_file.txt", expected_hash)

# 修改文件并重新验证
with open("test_file.txt", "a") as f:
    f.write(" (modified)")

verify_file_integrity("test_file.txt", expected_hash)

# 清理测试文件
os.remove("test_file.txt")

# 示例2: 安全存储密码（简化版）
def hash_password(password):
    """哈希密码用于存储"""
    # 注意：实际应用中应使用专门的密码哈希算法，如bcrypt、Argon2
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(hashed_password, password):
    """验证密码"""
    return hashed_password == hash_password(password)

# 演示密码哈希和验证
print("\n示例2: 安全存储密码（简化版）")
password = "my_secure_password"
hashed = hash_password(password)
print(f"原始密码: {password}")
print(f"哈希密码: {hashed}")

# 验证正确密码
if verify_password(hashed, "my_secure_password"):
    print("✓ 密码验证通过")
else:
    print("✗ 密码验证失败")

# 验证错误密码
if verify_password(hashed, "wrong_password"):
    print("✓ 密码验证通过")
else:
    print("✗ 密码验证失败")

# 示例3: 生成数据指纹
def generate_data_fingerprint(data):
    """生成数据的唯一指纹"""
    if isinstance(data, str):
        data = data.encode()
    return hashlib.sha256(data).hexdigest()

# 演示生成数据指纹
print("\n示例3: 生成数据指纹")
data1 = "This is some data to fingerprint"
data2 = "This is some different data"

fingerprint1 = generate_data_fingerprint(data1)
fingerprint2 = generate_data_fingerprint(data2)

print(f"数据1指纹: {fingerprint1}")
print(f"数据2指纹: {fingerprint2}")
print(f"指纹相同: {fingerprint1 == fingerprint2}")

# 示例4: 增量哈希更新
def incremental_hashing():
    """演示增量哈希更新"""
    print("\n示例4: 增量哈希更新")
    
    # 一次性更新
    full_message = b"This is a long message that could be processed in chunks"
    full_hash = hashlib.sha256(full_message).hexdigest()
    
    # 分块更新
    chunked_hash = hashlib.sha256()
    chunked_hash.update(b"This is a long message ")
    chunked_hash.update(b"that could be processed ")
    chunked_hash.update(b"in chunks")
    chunked_result = chunked_hash.hexdigest()
    
    print(f"一次性哈希结果: {full_hash}")
    print(f"分块哈希结果: {chunked_result}")
    print(f"结果相同: {full_hash == chunked_result}")

incremental_hashing()

# ===========================
# 9. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("9. 最佳实践")
print("=" * 50)

print("1. 避免使用不安全的算法")
print("   - 不要使用MD5和SHA-1进行安全敏感操作")
print("   - 推荐使用SHA-256或更强的算法")

print("\n2. 使用合适的哈希算法")
print("   - 数据完整性验证: SHA-256, SHA-3-256")
print("   - 密码存储: 使用专门的密码哈希算法(bcrypt, Argon2)")
print("   - 性能敏感场景: BLAKE2系列")

print("\n3. 处理大文件时使用分块更新")
print("   - 避免一次性加载大文件到内存")
print("   - 使用合理的块大小(如8KB或16KB)")

print("\n4. 密码安全存储")
print("   - 使用专门的密码哈希库，如bcrypt或passlib")
print("   - 为每个密码生成唯一的盐值")
print("   - 考虑使用密钥派生函数(KDF)")

print("\n5. 验证哈希值时使用安全比较")
print("   - 避免使用普通比较操作符(==)，防止时序攻击")
print("   - 在Python 3.7+中使用secrets.compare_digest()")

# ===========================
# 10. 常见错误和陷阱
# ===========================
print("\n" + "=" * 50)
print("10. 常见错误和陷阱")
print("=" * 50)

print("1. 使用错误的数据类型")
print("   - 哈希对象的update()方法只接受字节类型")
print("   - 字符串需要先编码为字节")

print("\n2. 忘记编码字符串")
try:
    hashlib.sha256("Hello, world!")
except TypeError as e:
    print(f"   错误示例: {e}")

print("   正确做法: hashlib.sha256(\"Hello, world!\".encode())")

print("\n3. 重用哈希对象")
print("   - 哈希对象更新后会累积数据")
print("   - 需要创建新的哈希对象处理新数据")

# 错误示例
hash_obj = hashlib.sha256()
hash_obj.update(b"First message")
result1 = hash_obj.hexdigest()

# 错误：重用哈希对象
hash_obj.update(b"Second message")
result2 = hash_obj.hexdigest()

# 正确：创建新的哈希对象
hash_obj2 = hashlib.sha256()
hash_obj2.update(b"Second message")
result2_correct = hash_obj2.hexdigest()

print(f"   错误结果(重用对象): {result2}")
print(f"   正确结果(新对象): {result2_correct}")

print("\n4. 忽略哈希算法的安全性")
print("   - MD5和SHA-1已不再安全")
print("   - 选择算法时考虑安全需求和时效性")

print("\n5. 使用普通哈希存储密码")
print("   - 普通哈希算法不适合密码存储")
print("   - 应使用bcrypt、Argon2等专门的密码哈希算法")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("hashlib模块提供了多种哈希算法的实现，适用于：")
print("- 数据完整性验证")
print("- 生成数据指纹")
print("- 密码安全存储(需要配合专门的密码哈希技术)")
print("\n使用hashlib时应注意：")
print("- 选择安全的哈希算法")
print("- 正确处理数据类型")
print("- 大文件使用分块处理")
print("- 密码存储使用专门的密码哈希算法")
print("\nhashlib是Python中处理哈希操作的核心模块，")
print("熟练掌握它对于数据安全和完整性验证至关重要")
