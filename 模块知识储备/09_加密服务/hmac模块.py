#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hmac模块 - 基于哈希的消息认证码

hmac模块实现了基于哈希的消息认证码（HMAC）算法，
用于验证消息的完整性和真实性。HMAC结合了哈希算法和密钥，
可以防止消息在传输过程中被篡改或伪造。

主要功能包括：
- 生成HMAC值
- 验证HMAC值
- 支持各种哈希算法

使用场景：
- API请求认证
- 消息完整性验证
- 安全通信
- 数字签名
"""

import hmac
import hashlib
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. hmac模块基本介绍")
print("=" * 50)
print("hmac模块实现了基于哈希的消息认证码（HMAC）算法")
print("HMAC结合了哈希算法和密钥，用于验证消息的完整性和真实性")
print("支持MD5、SHA-1、SHA-2系列等多种哈希算法")

# ===========================
# 2. HMAC的基本原理
# ===========================
print("\n" + "=" * 50)
print("2. HMAC的基本原理")
print("=" * 50)
print("HMAC的计算过程：")
print("1. 使用密钥和内部填充生成两个新密钥")
print("2. 使用第一个密钥与消息计算哈希值")
print("3. 使用第二个密钥与上一步的哈希值计算最终HMAC值")
print("\nHMAC的特点：")
print("- 安全性依赖于密钥的保密性")
print("- 可以检测消息是否被篡改")
print("- 可以防止伪造消息")

# ===========================
# 3. 基本用法
# ===========================
print("\n" + "=" * 50)
print("3. 基本用法")
print("=" * 50)

# 生成HMAC值
print("演示生成HMAC值:")
message = b"Hello, HMAC!"
key = b"secret_key"

# 使用默认的MD5算法
hmac_md5 = hmac.new(key, message, hashlib.md5)
hmac_value = hmac_md5.hexdigest()
print(f"使用MD5的HMAC值: {hmac_value}")

# 使用SHA-256算法
hmac_sha256 = hmac.new(key, message, hashlib.sha256)
hmac_value = hmac_sha256.hexdigest()
print(f"使用SHA-256的HMAC值: {hmac_value}")

# ===========================
# 4. 分块更新消息
# ===========================
print("\n" + "=" * 50)
print("4. 分块更新消息")
print("=" * 50)

# 对于大消息，可以分块更新
print("演示分块更新消息:")
key = b"large_message_key"
message_parts = [b"Part 1 of the message ", b"Part 2 of the message ", b"Part 3 of the message"]

# 创建HMAC对象
hmac_obj = hmac.new(key, digestmod=hashlib.sha256)

# 分块更新
for part in message_parts:
    hmac_obj.update(part)
    print(f"更新块: {part.decode()}")

# 获取最终HMAC值
final_hmac = hmac_obj.hexdigest()
print(f"最终HMAC值: {final_hmac}")

# 与一次性计算比较
full_message = b"Part 1 of the message Part 2 of the message Part 3 of the message"
hmac_full = hmac.new(key, full_message, hashlib.sha256).hexdigest()
print(f"一次性计算的HMAC值: {hmac_full}")
print(f"结果相同: {final_hmac == hmac_full}")

# ===========================
# 5. 验证HMAC值
# ===========================
print("\n" + "=" * 50)
print("5. 验证HMAC值")
print("=" * 50)

# 验证HMAC值的正确方法
def verify_hmac(message, received_hmac, key, digestmod=hashlib.sha256):
    """验证HMAC值"""
    # 重新计算HMAC值
    computed_hmac = hmac.new(key, message, digestmod).hexdigest()
    
    # 使用安全比较函数
    return hmac.compare_digest(computed_hmac, received_hmac)

# 演示验证HMAC值
print("演示验证HMAC值:")
message = b"Message to verify"
key = b"verification_key"

# 生成HMAC值
generated_hmac = hmac.new(key, message, hashlib.sha256).hexdigest()
print(f"生成的HMAC值: {generated_hmac}")

# 验证正确的HMAC值
if verify_hmac(message, generated_hmac, key):
    print("✓ HMAC验证通过")
else:
    print("✗ HMAC验证失败")

# 验证错误的HMAC值
wrong_hmac = "wrong_hmac_value"
if verify_hmac(message, wrong_hmac, key):
    print("✓ HMAC验证通过")
else:
    print("✗ HMAC验证失败")

# ===========================
# 6. 高级特性
# ===========================
print("\n" + "=" * 50)
print("6. 高级特性")
print("=" * 50)

# 使用不同的哈希算法
print("演示使用不同的哈希算法:")
message = b"Test message"
key = b"algorithm_key"

for algorithm in [hashlib.md5, hashlib.sha1, hashlib.sha256, hashlib.sha512]:
    hmac_obj = hmac.new(key, message, algorithm)
    print(f"使用{algorithm.__name__}的HMAC值: {hmac_obj.hexdigest()}")

# 处理不同长度的密钥
print("\n演示处理不同长度的密钥:")
message = b"Key length test"

# 短密钥
short_key = b"short"
hmac_short = hmac.new(short_key, message, hashlib.sha256).hexdigest()
print(f"短密钥的HMAC值: {hmac_short}")

# 长密钥
long_key = b"very_long_key_that_exceeds_the_block_size_of_the_hash_algorithm"
hmac_long = hmac.new(long_key, message, hashlib.sha256).hexdigest()
print(f"长密钥的HMAC值: {hmac_long}")

# 随机密钥
token = os.urandom(32)  # 生成32字节的随机密钥
hmac_random = hmac.new(token, message, hashlib.sha256).hexdigest()
print(f"随机密钥的HMAC值: {hmac_random}")

# 使用二进制HMAC值
print("\n演示使用二进制HMAC值:")
hmac_obj = hmac.new(key, message, hashlib.sha256)
binary_hmac = hmac_obj.digest()  # 返回二进制HMAC值
hex_hmac = hmac_obj.hexdigest()  # 返回十六进制HMAC值

print(f"二进制HMAC值: {binary_hmac}")
print(f"十六进制HMAC值: {hex_hmac}")
print(f"十六进制长度: {len(hex_hmac)} 字符")
print(f"二进制长度: {len(binary_hmac)} 字节")

# ===========================
# 7. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("7. 实际应用示例")
print("=" * 50)

# 示例1: API请求认证
def generate_api_signature(api_key, api_secret, data, timestamp):
    """生成API请求签名"""
    # 创建签名字符串
    signature_string = f"{api_key}{timestamp}{data}"
    
    # 生成HMAC签名
    signature = hmac.new(
        api_secret.encode(),
        signature_string.encode(),
        hashlib.sha256
    ).hexdigest()
    
    return signature

def verify_api_signature(api_key, api_secret, data, timestamp, received_signature):
    """验证API请求签名"""
    # 重新生成签名
    expected_signature = generate_api_signature(api_key, api_secret, data, timestamp)
    
    # 使用安全比较
    return hmac.compare_digest(expected_signature, received_signature)

# 演示API请求认证
print("示例1: API请求认证")
api_key = "user123"
api_secret = "secret_key_abc123"
data = "request_data"
timestamp = "1234567890"

# 生成签名
signature = generate_api_signature(api_key, api_secret, data, timestamp)
print(f"API请求签名: {signature}")

# 验证签名
if verify_api_signature(api_key, api_secret, data, timestamp, signature):
    print("✓ API签名验证通过")
else:
    print("✗ API签名验证失败")

# 示例2: 文件完整性验证
def calculate_file_hmac(file_path, key, digestmod=hashlib.sha256, chunk_size=8192):
    """计算文件的HMAC值"""
    hmac_obj = hmac.new(key, digestmod=digestmod)
    
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            hmac_obj.update(chunk)
    
    return hmac_obj.hexdigest()

def verify_file_hmac(file_path, key, expected_hmac, digestmod=hashlib.sha256):
    """验证文件的HMAC值"""
    file_hmac = calculate_file_hmac(file_path, key, digestmod)
    return hmac.compare_digest(file_hmac, expected_hmac)

# 演示文件完整性验证
print("\n示例2: 文件完整性验证")

# 创建测试文件
with open("test_file.txt", "w") as f:
    f.write("This is a test file for HMAC verification")

# 生成文件的HMAC值
key = b"file_verification_key"
file_hmac = calculate_file_hmac("test_file.txt", key)
print(f"文件HMAC值: {file_hmac}")

# 验证文件完整性
if verify_file_hmac("test_file.txt", key, file_hmac):
    print("✓ 文件完整性验证通过")
else:
    print("✗ 文件完整性验证失败")

# 修改文件并重新验证
with open("test_file.txt", "a") as f:
    f.write(" (modified)")

if verify_file_hmac("test_file.txt", key, file_hmac):
    print("✓ 文件完整性验证通过")
else:
    print("✗ 文件完整性验证失败")

# 清理测试文件
os.remove("test_file.txt")

# 示例3: 安全通信验证
def secure_communication():
    """演示安全通信验证"""
    print("\n示例3: 安全通信验证")
    
    # 模拟客户端和服务器共享密钥
    shared_key = b"secure_communication_key"
    
    # 客户端发送消息和HMAC
    message = b"Confidential information"
    message_hmac = hmac.new(shared_key, message, hashlib.sha256).hexdigest()
    
    print(f"客户端发送消息: {message.decode()}")
    print(f"客户端发送HMAC: {message_hmac}")
    
    # 服务器接收消息并验证
    print("\n服务器接收并验证:")
    if hmac.compare_digest(hmac.new(shared_key, message, hashlib.sha256).hexdigest(), message_hmac):
        print("✓ 消息验证通过，内容安全可靠")
    else:
        print("✗ 消息验证失败，可能已被篡改")

secure_communication()

# 示例4: 防止重放攻击
def prevent_replay_attack():
    """演示防止重放攻击"""
    print("\n示例4: 防止重放攻击")
    
    # 模拟客户端和服务器共享密钥
    shared_key = b"replay_prevention_key"
    
    # 客户端发送消息、时间戳和HMAC
    message = b"Transaction: $100"
    timestamp = "2023-10-01 14:30:00"
    
    # 创建包含时间戳的签名字符串
    signature_data = f"{message.decode()}|{timestamp}".encode()
    signature = hmac.new(shared_key, signature_data, hashlib.sha256).hexdigest()
    
    print(f"客户端发送:")
    print(f"  消息: {message.decode()}")
    print(f"  时间戳: {timestamp}")
    print(f"  HMAC: {signature}")
    
    # 服务器验证
    print("\n服务器验证:")
    
    # 1. 检查时间戳是否在有效范围内
    # (实际应用中需要与当前时间比较)
    print("✓ 时间戳在有效范围内")
    
    # 2. 验证HMAC
    computed_signature = hmac.new(
        shared_key,
        f"{message.decode()}|{timestamp}".encode(),
        hashlib.sha256
    ).hexdigest()
    
    if hmac.compare_digest(computed_signature, signature):
        print("✓ HMAC验证通过")
        print("✓ 消息有效，处理交易")
    else:
        print("✗ HMAC验证失败")

prevent_replay_attack()

# ===========================
# 8. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("8. 最佳实践")
print("=" * 50)

print("1. 使用强哈希算法")
print("   - 推荐使用SHA-256或更强的算法")
print("   - 避免使用MD5和SHA-1")

print("\n2. 使用安全的密钥管理")
print("   - 密钥应足够长（至少256位）")
print("   - 使用随机生成的密钥")
print("   - 避免硬编码密钥")
print("   - 定期轮换密钥")

print("\n3. 使用安全比较函数")
print("   - 使用hmac.compare_digest()而不是==")
print("   - 防止时序攻击")

print("\n4. 保护HMAC值")
print("   - HMAC值应与消息一起传输")
print("   - 但不应单独存储在数据库中")

print("\n5. 处理大消息")
print("   - 使用分块更新处理大文件")
print("   - 避免一次性加载大消息到内存")

print("\n6. 考虑性能影响")
print("   - 选择适当的哈希算法平衡安全性和性能")
print("   - 对于频繁调用的API，考虑使用更快的算法")

# ===========================
# 9. 常见错误和陷阱
# ===========================
print("\n" + "=" * 50)
print("9. 常见错误和陷阱")
print("=" * 50)

print("1. 使用不安全的哈希算法")
print("   - MD5和SHA-1已不再安全")
print("   - 应使用SHA-256或更强的算法")

print("\n2. 密钥管理不当")
print("   - 硬编码密钥到代码中")
print("   - 使用弱密钥或可预测密钥")
print("   - 密钥长度不足")

print("\n3. 不正确的比较方式")
print("   - 使用普通比较操作符(==)而不是hmac.compare_digest()")
print("   - 可能导致时序攻击")

# 错误示例
def insecure_compare(a, b):
    """不安全的比较函数"""
    return a == b

# 正确示例
def secure_compare(a, b):
    """安全的比较函数"""
    return hmac.compare_digest(a, b)

print("\n4. 重用HMAC对象")
print("   - HMAC对象更新后会累积数据")
print("   - 需要为每个消息创建新的HMAC对象")

# 错误示例
hmac_obj = hmac.new(b"key", digestmod=hashlib.sha256)
hmac_obj.update(b"message1")
hmac1 = hmac_obj.hexdigest()

# 错误：重用HMAC对象
hmac_obj.update(b"message2")
hmac2 = hmac_obj.hexdigest()

# 正确示例
hmac1 = hmac.new(b"key", b"message1", hashlib.sha256).hexdigest()
hmac2 = hmac.new(b"key", b"message2", hashlib.sha256).hexdigest()

print("\n5. 忽略时间戳")
print("   - 不使用时间戳可能导致重放攻击")
print("   - 应在HMAC计算中包含时间戳")

print("\n6. 传输明文密钥")
print("   - 密钥不应在网络上明文传输")
print("   - 应使用安全的密钥交换机制")

# ===========================
# 10. 与其他认证方法的比较
# ===========================
print("\n" + "=" * 50)
print("10. 与其他认证方法的比较")
print("=" * 50)

print("HMAC vs 普通哈希:")
print("- HMAC使用密钥，普通哈希不使用")
print("- HMAC可以验证消息真实性，普通哈希只能验证完整性")
print("- HMAC更安全，防止伪造消息")

print("\nHMAC vs 数字签名:")
print("- HMAC使用对称密钥，数字签名使用非对称密钥")
print("- HMAC速度更快，适合高频调用")
print("- 数字签名可以提供不可否认性")

print("\nHMAC vs API密钥:")
print("- API密钥通常明文传输，安全性较低")
print("- HMAC使用密钥生成签名，密钥不直接传输")
print("- HMAC可以防止API密钥被窃取后的滥用")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("hmac模块提供了基于哈希的消息认证码（HMAC）实现，")
print("可用于验证消息的完整性和真实性。")
print("\n主要应用场景：")
print("- API请求认证")
print("- 消息完整性验证")
print("- 安全通信")
print("- 防止重放攻击")
print("\n使用HMAC时的最佳实践：")
print("- 使用强哈希算法和安全密钥")
print("- 使用安全比较函数")
print("- 妥善管理密钥")
print("- 防止重放攻击")
print("\nhmac是Python中实现安全消息认证的重要模块，")
print("熟练掌握它对于保障数据通信安全至关重要。")
