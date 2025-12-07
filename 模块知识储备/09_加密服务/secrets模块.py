#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
secrets模块 - 安全随机数生成

secrets模块提供了生成安全随机数的函数，
专门用于密码、密钥、会话ID等安全敏感场景。

主要功能包括：
- 生成安全的随机字节
- 生成安全的随机整数
- 生成安全的随机字符串
- 从序列中安全选择随机元素

使用场景：
- 生成密码和密码重置令牌
- 生成会话ID和CSRF令牌
- 生成API密钥和访问令牌
- 生成一次性密码(OTP)
- 生成安全的随机文件名
"""

import secrets
import string
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. secrets模块基本介绍")
print("=" * 50)
print("secrets模块提供了生成安全随机数的函数")
print("专门用于密码、密钥、会话ID等安全敏感场景")
print("使用操作系统提供的安全随机数生成器")

# ===========================
# 2. 与random模块的区别
# ===========================
print("\n" + "=" * 50)
print("2. 与random模块的区别")
print("=" * 50)
print("secrets模块 vs random模块:")
print("- random模块适用于非安全场景，如游戏、模拟等")
print("- secrets模块适用于安全敏感场景，如密码、密钥等")
print("- secrets模块使用加密安全的随机数生成器")
print("- random模块生成的随机数可以被预测（如果知道种子）")
print("- secrets模块生成的随机数不可预测")

# ===========================
# 3. 基本用法
# ===========================
print("\n" + "=" * 50)
print("3. 基本用法")
print("=" * 50)

# 生成安全的随机字节
print("演示生成安全的随机字节:")
random_bytes = secrets.token_bytes(16)  # 生成16字节的随机数据
print(f"16字节随机数据: {random_bytes}")
print(f"数据长度: {len(random_bytes)} 字节")

# 生成安全的随机十六进制字符串
print("\n演示生成安全的随机十六进制字符串:")
random_hex = secrets.token_hex(16)  # 生成32字符的十六进制字符串
print(f"32字符十六进制字符串: {random_hex}")
print(f"字符串长度: {len(random_hex)} 字符")

# 生成安全的URL安全字符串
print("\n演示生成安全的URL安全字符串:")
random_urlsafe = secrets.token_urlsafe(16)  # 生成22字符的URL安全字符串
print(f"22字符URL安全字符串: {random_urlsafe}")
print(f"字符串长度: {len(random_urlsafe)} 字符")

# 生成安全的随机整数
print("\n演示生成安全的随机整数:")
random_int = secrets.randbelow(100)  # 生成0-99之间的随机整数
print(f"0-99之间的随机整数: {random_int}")

random_int_range = secrets.randbits(8)  # 生成8位随机整数（0-255）
print(f"8位随机整数: {random_int_range}")

# 从序列中安全选择随机元素
print("\n演示从序列中安全选择随机元素:")
colors = ["red", "green", "blue", "yellow", "purple"]
random_color = secrets.choice(colors)
print(f"从{colors}中随机选择: {random_color}")

# ===========================
# 4. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("4. 实际应用示例")
print("=" * 50)

# 示例1: 生成安全密码
def generate_secure_password(length=12):
    """生成安全密码"""
    # 定义字符集
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # 确保密码包含至少一个小写字母、一个大写字母、一个数字和一个标点符号
    while True:
        password = ''.join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

# 演示生成安全密码
print("示例1: 生成安全密码")
for i in range(3):
    password = generate_secure_password()
    print(f"生成的密码 #{i+1}: {password}")
    print(f"密码长度: {len(password)} 字符")

# 示例2: 生成会话ID
def generate_session_id(length=32):
    """生成安全的会话ID"""
    return secrets.token_urlsafe(length)

# 演示生成会话ID
print("\n示例2: 生成会话ID")
session_id = generate_session_id()
print(f"会话ID: {session_id}")
print(f"会话ID长度: {len(session_id)} 字符")

# 示例3: 生成API密钥
def generate_api_key():
    """生成API密钥"""
    # 生成32字节的随机数据，转换为64字符的十六进制字符串
    return secrets.token_hex(32)

# 演示生成API密钥
print("\n示例3: 生成API密钥")
api_key = generate_api_key()
print(f"API密钥: {api_key}")
print(f"API密钥长度: {len(api_key)} 字符")

# 示例4: 生成一次性密码(OTP)
def generate_otp(length=6):
    """生成一次性密码"""
    # 生成纯数字的OTP
    digits = string.digits
    return ''.join(secrets.choice(digits) for _ in range(length))

# 演示生成OTP
print("\n示例4: 生成一次性密码(OTP)")
otp = generate_otp()
print(f"一次性密码: {otp}")
print(f"OTP长度: {len(otp)} 字符")

# 示例5: 生成安全的随机文件名
def generate_secure_filename(extension=".txt"):
    """生成安全的随机文件名"""
    random_part = secrets.token_hex(8)
    return f"{random_part}{extension}"

# 演示生成安全文件名
print("\n示例5: 生成安全的随机文件名")
for ext in [".txt", ".jpg", ".pdf", ".mp4"]:
    filename = generate_secure_filename(ext)
    print(f"{ext}文件: {filename}")

# 示例6: 生成CSRF令牌
def generate_csrf_token():
    """生成CSRF令牌"""
    return secrets.token_urlsafe(32)

# 演示生成CSRF令牌
print("\n示例6: 生成CSRF令牌")
csrf_token = generate_csrf_token()
print(f"CSRF令牌: {csrf_token}")
print(f"CSRF令牌长度: {len(csrf_token)} 字符")

# 示例7: 生成密码重置令牌
def generate_password_reset_token():
    """生成密码重置令牌"""
    return secrets.token_urlsafe(48)

# 演示生成密码重置令牌
print("\n示例7: 生成密码重置令牌")
reset_token = generate_password_reset_token()
print(f"密码重置令牌: {reset_token}")
print(f"重置令牌长度: {len(reset_token)} 字符")

# ===========================
# 5. 高级用法
# ===========================
print("\n" + "=" * 50)
print("5. 高级用法")
print("=" * 50)

# 生成自定义字符集的随机字符串
def generate_custom_string(length=12, chars=string.ascii_letters + string.digits):
    """生成自定义字符集的随机字符串"""
    return ''.join(secrets.choice(chars) for _ in range(length))

# 演示生成自定义字符集的随机字符串
print("演示生成自定义字符集的随机字符串:")
# 只包含小写字母和数字
custom_str = generate_custom_string(chars=string.ascii_lowercase + string.digits)
print(f"小写字母和数字组成的字符串: {custom_str}")

# 生成固定长度的加密密钥
def generate_encryption_key(key_size=32):
    """生成固定长度的加密密钥"""
    # 生成指定字节数的随机密钥
    return secrets.token_bytes(key_size)

# 演示生成加密密钥
print("\n演示生成加密密钥:")
# 生成AES-256密钥（32字节）
aes_key = generate_encryption_key(32)
print(f"AES-256密钥: {aes_key}")
print(f"密钥长度: {len(aes_key)} 字节")

# 生成安全的随机数范围
def secure_random_range(start, stop):
    """生成指定范围内的安全随机数"""
    if start >= stop:
        raise ValueError("start must be less than stop")
    range_size = stop - start
    return start + secrets.randbelow(range_size)

# 演示生成安全的随机数范围
print("\n演示生成安全的随机数范围:")
random_number = secure_random_range(100, 200)
print(f"100-200之间的随机整数: {random_number}")

# 安全随机选择多个元素（不重复）
def secure_sample(population, k):
    """从序列中安全选择k个不重复的元素"""
    if k > len(population):
        raise ValueError("k cannot be larger than population size")
    
    # 创建序列的副本
    result = population.copy()
    
    # 使用Fisher-Yates洗牌算法的安全版本
    for i in range(len(result)-1, 0, -1):
        j = secrets.randbelow(i+1)
        result[i], result[j] = result[j], result[i]
    
    return result[:k]

# 演示安全随机选择多个元素
print("\n演示安全随机选择多个元素:")
numbers = list(range(1, 21))
sampled = secure_sample(numbers, 5)
print(f"从{numbers}中随机选择5个不重复元素: {sampled}")

# ===========================
# 6. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("6. 最佳实践")
print("=" * 50)

print("1. 使用适当长度的随机数据")
print("   - 密码: 至少12字符")
print("   - 会话ID: 至少16字节")
print("   - API密钥: 至少32字节")
print("   - CSRF令牌: 至少16字节")

print("\n2. 选择合适的字符集")
print("   - 密码: 使用大小写字母、数字和特殊字符")
print("   - URL参数: 使用URL安全字符集")
print("   - 文件名: 避免使用特殊字符")

print("\n3. 定期轮换密钥和令牌")
print("   - 会话ID: 用户登出或定期过期")
print("   - API密钥: 定期轮换，特别是在权限变更时")
print("   - 密码: 鼓励用户定期更改密码")

print("\n4. 安全存储敏感随机数")
print("   - 密码: 使用专门的密码哈希算法存储")
print("   - 密钥: 存储在安全的密钥管理系统中")
print("   - 令牌: 根据需要生成，避免长期存储")

print("\n5. 避免使用不安全的随机源")
print("   - 不要使用random模块生成安全敏感的随机数")
print("   - 不要使用时间戳作为随机数种子")
print("   - 不要使用用户提供的输入作为随机数源")

# ===========================
# 7. 常见错误和陷阱
# ===========================
print("\n" + "=" * 50)
print("7. 常见错误和陷阱")
print("=" * 50)

print("1. 使用random模块生成安全敏感的随机数")
print("   - 错误: 使用random.choice()生成密码")
print("   - 正确: 使用secrets.choice()生成密码")

print("\n2. 使用固定长度或可预测的随机数")
print("   - 错误: 生成太短的会话ID")
print("   - 正确: 生成足够长度的随机数")

print("\n3. 硬编码随机数")
print("   - 错误: 在代码中硬编码密钥或密码")
print("   - 正确: 动态生成或从安全位置读取")

print("\n4. 不安全的字符集选择")
print("   - 错误: 使用容易猜测的字符集")
print("   - 正确: 使用足够复杂的字符集")

print("\n5. 不正确的随机数范围")
print("   - 错误: 生成范围过大或过小的随机数")
print("   - 正确: 根据需求选择合适的范围")

print("\n6. 忽略随机数的周期性")
print("   - 错误: 长期使用同一个随机数作为密钥")
print("   - 正确: 定期轮换随机生成的密钥和令牌")

# ===========================
# 8. 总结
# ===========================
print("\n" + "=" * 50)
print("8. 总结")
print("=" * 50)
print("secrets模块提供了生成安全随机数的函数，")
print("专门用于密码、密钥、会话ID等安全敏感场景。")
print("\n主要功能:")
print("- 生成安全的随机字节、整数和字符串")
print("- 支持URL安全字符串和十六进制字符串")
print("- 从序列中安全选择随机元素")
print("\n使用secrets模块可以确保:")
print("- 随机数的不可预测性")
print("- 应用程序的安全性")
print("- 保护用户数据的安全")
print("\nsecrets是Python 3.6+中用于处理安全随机数的首选模块，")
print("对于任何涉及安全敏感操作的应用程序都至关重要。")
