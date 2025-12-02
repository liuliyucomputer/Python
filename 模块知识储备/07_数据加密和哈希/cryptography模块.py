# Python cryptography模块详解

```python
"""
cryptography模块 - Python中强大的加密和安全工具包

cryptography是Python中一个功能全面、安全且易于使用的密码学库，
提供了对称加密、非对称加密、哈希函数、密钥派生函数等密码学原语。

主要功能与特点：
- 提供高级和低级API，满足不同安全需求
- 实现了现代安全的加密算法和协议
- 维护良好，定期更新以应对新的安全威胁
- 遵循最佳实践，如安全默认值和自动内存管理
- 广泛应用于需要强安全性的生产环境

应用场景：
- 数据加密与解密（文件、数据库、通信）
- 用户认证与授权系统
- 数字签名与验证
- 密钥管理与轮换
- 安全通信协议实现
- 密码存储与验证
- 证书管理
"""

import os
import binascii
import base64
import json
from datetime import datetime, timedelta
import time

# 注意：cryptography是第三方库，需要安装
# 这里使用try-except处理可能的导入错误
try:
    # 对称加密相关导入
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    
    # 非对称加密相关导入
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives import hashes, serialization
    
    # 密钥派生函数
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
    
    # X.509证书相关
    from cryptography import x509
    from cryptography.x509.oid import NameOID
    
    # 密码验证
    from cryptography.fernet import Fernet
    
    CRYPTOGRAPHY_AVAILABLE = True
except ImportError:
    print("警告: cryptography库未安装。请使用 'pip install cryptography' 安装。")
    print("将使用模拟函数进行演示，实际应用中请确保安装了cryptography库。")
    CRYPTOGRAPHY_AVAILABLE = False

# 模拟函数，仅用于演示（当cryptography未安装时）
class CryptographySimulator:
    """cryptography模块的简单模拟，用于演示目的"""
    
    def __init__(self):
        self.backend = "simulated_backend"
    
    def generate_key(self):
        return "simulated_fernet_key_" + binascii.hexlify(os.urandom(16)).decode()
    
    def encrypt(self, data):
        return "encrypted:" + base64.b64encode(data.encode()).decode()
    
    def decrypt(self, token):
        if token.startswith("encrypted:"):
            return base64.b64decode(token[10:]).decode()
        return "解密失败"

# 1. 对称加密基础
def symmetric_encryption_basics():
    """
    对称加密基础
    
    功能说明：演示使用cryptography模块进行对称加密和解密操作。
    对称加密使用相同的密钥进行加密和解密。
    """
    print("=== 1. 对称加密基础 ===")
    
    if not CRYPTOGRAPHY_AVAILABLE:
        print("\n注意：cryptography库未安装，将使用模拟演示。")
        print("实际应用中请安装cryptography库以获得完整功能和安全性。")
        
        # 使用模拟函数
        print("\n使用Fernet（高级对称加密）模拟:")
        print("Fernet是基于AES-128的高级加密方案，提供了良好的安全性。")
        
        simulator = CryptographySimulator()
        
        # 生成密钥（模拟）
        key = simulator.generate_key()
        print(f"\n生成的密钥: {key}")
        
        # 加密数据（模拟）
        message = "这是一条需要加密的敏感消息"
        print(f"原始消息: {message}")
        
        encrypted = simulator.encrypt(message)
        print(f"加密后: {encrypted}")
        
        # 解密数据（模拟）
        decrypted = simulator.decrypt(encrypted)
        print(f"解密后: {decrypted}")
        
        print("\n模拟演示完成。在实际应用中，cryptography库提供了真正的加密功能。")
        return
    
    # 1.1 Fernet高级对称加密
    print("\n1.1 Fernet高级对称加密:")
    print("Fernet是基于AES-128的高级加密方案，提供了良好的安全性和易用性。")
    
    # 生成Fernet密钥
    key = Fernet.generate_key()
    print(f"\n生成的密钥: {key.decode()}")
    print(f"密钥十六进制表示: {binascii.hexlify(key).decode()}")
    print(f"密钥长度: {len(key)} 字节")
    
    # 创建Fernet实例
    f = Fernet(key)
    
    # 要加密的消息
    original_message = "这是一条需要加密的敏感消息"
    print(f"\n原始消息: {original_message}")
    
    # 必须将消息编码为字节
    message_bytes = original_message.encode()
    
    # 加密消息
    encrypted_message = f.encrypt(message_bytes)
    print(f"加密后的消息: {encrypted_message.decode()}")
    print(f"加密后长度: {len(encrypted_message)} 字节")
    
    # 解密消息
    decrypted_message = f.decrypt(encrypted_message)
    
    # 将解密后的字节转换回字符串
    decrypted_text = decrypted_message.decode()
    print(f"解密后的消息: {decrypted_text}")
    
    # 验证解密后的消息与原始消息是否相同
    print(f"消息验证: {'成功' if decrypted_text == original_message else '失败'}")
    
    # 1.2 使用密码派生密钥
    print("\n1.2 使用密码派生密钥:")
    print("通常我们不直接使用Fernet.generate_key()，而是从用户密码派生密钥。")
    
    # 用户密码
    password = "用户的强密码123!"
    print(f"用户密码: {password}")
    
    # 生成随机盐值（每次都不同）
    salt = os.urandom(16)
    print(f"生成的盐值: {binascii.hexlify(salt).decode()}")
    
    # 创建PBKDF2密钥派生函数
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Fernet需要32字节密钥
        salt=salt,
        iterations=100000,  # 迭代次数，越高越安全但越慢
        backend=default_backend()
    )
    
    # 从密码派生密钥
    key_from_password = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    print(f"从密码派生的密钥: {key_from_password.decode()}")
    
    # 使用派生的密钥创建Fernet实例
    f_from_password = Fernet(key_from_password)
    
    # 加密消息
    encrypted_with_password = f_from_password.encrypt(original_message.encode())
    print(f"使用密码加密的消息: {encrypted_with_password.decode()}")
    
    # 解密消息（需要相同的密码和盐值）
    # 在实际应用中，你需要保存盐值以便解密
    # 这里我们直接使用已保存的盐值进行解密演示
    kdf_decrypt = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    # 重新派生密钥
    key_for_decrypt = base64.urlsafe_b64encode(kdf_decrypt.derive(password.encode()))
    
    # 解密
    f_decrypt = Fernet(key_for_decrypt)
    decrypted_with_password = f_decrypt.decrypt(encrypted_with_password).decode()
    
    print(f"使用密码解密的消息: {decrypted_with_password}")
    print(f"解密验证: {'成功' if decrypted_with_password == original_message else '失败'}")
    
    # 1.3 AES低级API示例
    print("\n1.3 AES低级API示例:")
    print("对于需要更精细控制的场景，可以使用低级API。")
    
    # 生成随机AES密钥（16字节=128位，也可以是24字节=192位或32字节=256位）
    aes_key = os.urandom(16)
    print(f"AES密钥 (128位): {binascii.hexlify(aes_key).decode()}")
    
    # 生成随机IV（初始化向量）
    iv = os.urandom(16)
    print(f"初始化向量 (IV): {binascii.hexlify(iv).decode()}")
    
    # 要加密的数据
    data_to_encrypt = "这是使用AES-CBC模式加密的数据".encode()
    print(f"原始数据: {data_to_encrypt.decode()}")
    
    # AES-CBC模式要求数据长度是16字节的倍数，所以需要填充
    # 简单的PKCS#7填充（实际应用中应使用标准填充）
    block_size = 16
    padding_length = block_size - (len(data_to_encrypt) % block_size)
    padded_data = data_to_encrypt + (chr(padding_length) * padding_length).encode()
    
    print(f"填充后数据长度: {len(padded_data)} 字节")
    
    # 创建加密器
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # 加密数据
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    print(f"加密后数据 (十六进制): {binascii.hexlify(ciphertext).decode()}")
    print(f"加密后数据长度: {len(ciphertext)} 字节")
    
    # 创建解密器
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # 解密数据
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    
    # 移除填充
    padding_length = decrypted_padded[-1]
    decrypted_data = decrypted_padded[:-padding_length]
    
    print(f"解密后数据: {decrypted_data.decode()}")
    print(f"解密验证: {'成功' if decrypted_data == data_to_encrypt else '失败'}")
    
    # 1.4 不同AES模式比较
    print("\n1.4 不同AES模式比较:")
    
    modes_comparison = [
        {
            "mode": "ECB (Electronic Codebook)",
            "description": "最简单的模式，每个数据块独立加密",
            "advantages": ["实现简单", "并行处理能力强"],
            "disadvantages": ["相同的明文块产生相同的密文块", "不推荐使用", "不安全"],
            "use_cases": ["仅用于测试", "不建议实际应用"]
        },
        {
            "mode": "CBC (Cipher Block Chaining)",
            "description": "每个明文块与前一个密文块进行异或后再加密",
            "advantages": ["相同的明文块产生不同的密文块", "广泛使用", "安全性良好"],
            "disadvantages": ["需要IV", "加密不能并行", "解密可以并行"],
            "use_cases": ["文件加密", "数据库加密", "通用加密"]
        },
        {
            "mode": "CTR (Counter)",
            "description": "使用递增的计数器值进行加密",
            "advantages": ["加密和解密都可以并行", "不需要填充", "随机访问能力强"],
            "disadvantages": ["需要唯一的计数器", "实现复杂"],
            "use_cases": ["流媒体加密", "随机访问加密", "高性能要求场景"]
        },
        {
            "mode": "GCM (Galois/Counter Mode)",
            "description": "CTR模式的扩展，增加了认证功能",
            "advantages": ["提供加密和认证", "并行处理能力强", "不需要填充"],
            "disadvantages": ["实现复杂", "密钥使用次数受限"],
            "use_cases": ["网络通信", "需要完整性验证的场景", "TLS/SSL协议"]
        }
    ]
    
    for mode_info in modes_comparison:
        print(f"\n{mode_info['mode']}:")
        print(f"  描述: {mode_info['description']}")
        print(f"  优点: {', '.join(mode_info['advantages'])}")
        print(f"  缺点: {', '.join(mode_info['disadvantages'])}")
        print(f"  适用场景: {', '.join(mode_info['use_cases'])}")

# 2. 非对称加密
def asymmetric_encryption():
    """
    非对称加密
    
    功能说明：演示使用cryptography模块进行非对称加密和解密操作。
    非对称加密使用公钥加密，私钥解密，或使用私钥签名，公钥验证。
    """
    print("\n=== 2. 非对称加密 ===")
    
    if not CRYPTOGRAPHY_AVAILABLE:
        print("\n注意：cryptography库未安装，将使用模拟演示非对称加密概念。")
        print("\n非对称加密基本概念:")
        print("1. 使用一对密钥：公钥和私钥")
        print("2. 公钥加密的数据只能用对应的私钥解密")
        print("3. 私钥签名的数据只能用对应的公钥验证")
        print("4. 常用算法：RSA, ECC (椭圆曲线加密)")
        print("5. 应用场景：安全通信、数字签名、身份认证")
        print("\n模拟演示完成。在实际应用中，请安装cryptography库以获得真正的非对称加密功能。")
        return
    
    # 2.1 生成RSA密钥对
    print("\n2.1 生成RSA密钥对:")
    
    print("生成2048位RSA密钥对...")
    # 生成私钥
    private_key = rsa.generate_private_key(
        public_exponent=65537,  # 标准值，安全且高效
        key_size=2048,  # 密钥大小，2048位或更高（推荐4096位用于高安全性）
        backend=default_backend()
    )
    
    print("RSA私钥生成成功")
    
    # 从私钥中获取公钥
    public_key = private_key.public_key()
    print("RSA公钥提取成功")
    
    # 2.2 私钥序列化和保存
    print("\n2.2 私钥序列化和保存:")
    
    # 以PEM格式序列化私钥（带密码保护）
    password = "私钥保护密码123!"
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
    )
    
    print("私钥序列化成功（带密码保护）")
    print("私钥PEM格式（前100字符）:")
    print(private_pem.decode()[:100] + "...")
    
    # 2.3 公钥序列化和保存
    print("\n2.3 公钥序列化和保存:")
    
    # 以PEM格式序列化公钥
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    print("公钥序列化成功")
    print("公钥PEM格式（前100字符）:")
    print(public_pem.decode()[:100] + "...")
    
    # 2.4 RSA加密和解密
    print("\n2.4 RSA加密和解密:")
    
    # 要加密的消息（注意：RSA只能加密少量数据，通常只加密对称密钥）
    message = "这是使用RSA公钥加密的短消息"
    print(f"原始消息: {message}")
    
    # 使用公钥加密
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print(f"加密后数据长度: {len(encrypted_message)} 字节")
    print(f"加密后数据（十六进制，前50字符）: {binascii.hexlify(encrypted_message).decode()[:50]}...")
    
    # 使用私钥解密
    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    decrypted_text = decrypted_message.decode()
    print(f"解密后的消息: {decrypted_text}")
    print(f"解密验证: {'成功' if decrypted_text == message else '失败'}")
    
    # 2.5 数字签名和验证
    print("\n2.5 数字签名和验证:")
    
    # 要签名的数据
    data_to_sign = "这是需要数字签名的数据，用于验证数据的完整性和来源"
    print(f"要签名的数据: {data_to_sign}")
    
    # 使用私钥签名
    signature = private_key.sign(
        data_to_sign.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    print(f"生成的签名长度: {len(signature)} 字节")
    print(f"签名（十六进制，前50字符）: {binascii.hexlify(signature).decode()[:50]}...")
    
    # 使用公钥验证签名
    try:
        public_key.verify(
            signature,
            data_to_sign.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("签名验证成功！数据完整且来源于私钥持有者")
    except Exception as e:
        print(f"签名验证失败: {e}")
    
    # 模拟数据被篡改的情况
    tampered_data = data_to_sign + "，已被篡改"
    print(f"\n篡改后的数据: {tampered_data}")
    
    try:
        public_key.verify(
            signature,  # 使用原始签名
            tampered_data.encode(),  # 使用篡改的数据
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("签名验证成功！")
    except Exception as e:
        print(f"签名验证失败: {e}")
        print("成功检测到数据篡改！")
    
    # 2.6 混合加密示例（结合对称加密和非对称加密）
    print("\n2.6 混合加密示例:")
    print("在实际应用中，通常结合使用对称加密和非对称加密。")
    print("使用对称加密加密大量数据，然后使用非对称加密加密对称密钥。")
    
    # 生成随机AES密钥（对称密钥）
    aes_key = os.urandom(32)  # 256位AES密钥
    print(f"生成的AES密钥: {binascii.hexlify(aes_key).decode()}")
    
    # 要加密的大量数据
    large_data = "这是需要加密的大量数据。" * 100  # 生成一个较大的文本
    print(f"要加密的数据大小: {len(large_data)} 字符")
    
    # 1. 使用AES-GCM加密大量数据
    print("\n1. 使用AES-GCM加密大量数据:")
    iv = os.urandom(12)  # GCM模式推荐使用12字节IV
    encryptor = Cipher(
        algorithms.AES(aes_key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()
    
    # 加密数据
    ciphertext = encryptor.update(large_data.encode()) + encryptor.finalize()
    
    # 获取认证标签（GCM模式提供认证功能）
    tag = encryptor.tag
    
    print(f"加密后数据大小: {len(ciphertext)} 字节")
    print(f"认证标签: {binascii.hexlify(tag).decode()}")
    
    # 2. 使用RSA公钥加密AES密钥
    print("\n2. 使用RSA公钥加密AES密钥:")
    encrypted_aes_key = public_key.encrypt(
        aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print(f"加密后的AES密钥大小: {len(encrypted_aes_key)} 字节")
    
    # 模拟将加密后的数据、IV、认证标签和加密后的AES密钥发送给接收方
    print("\n3. 模拟发送加密数据和加密的AES密钥:")
    print("在实际应用中，这些数据会被发送给接收方。")
    
    # 4. 接收方使用RSA私钥解密AES密钥
    print("\n4. 接收方使用RSA私钥解密AES密钥:")
    decrypted_aes_key = private_key.decrypt(
        encrypted_aes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print(f"解密后的AES密钥: {binascii.hexlify(decrypted_aes_key).decode()}")
    print(f"密钥验证: {'成功' if decrypted_aes_key == aes_key else '失败'}")
    
    # 5. 接收方使用解密的AES密钥解密数据
    print("\n5. 接收方使用解密的AES密钥解密数据:")
    decryptor = Cipher(
        algorithms.AES(decrypted_aes_key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()
    
    # 解密数据
    decrypted_large_data = decryptor.update(ciphertext) + decryptor.finalize()
    decrypted_text = decrypted_large_data.decode()
    
    print(f"解密后数据大小: {len(decrypted_text)} 字符")
    print(f"解密验证: {'成功' if decrypted_text == large_data else '失败'}")
    print(f"解密文本前50字符: {decrypted_text[:50]}...")

# 3. 哈希函数和消息摘要
def hash_functions():
    """
    哈希函数和消息摘要
    
    功能说明：演示使用cryptography模块的哈希函数进行数据摘要计算、
    文件完整性验证等操作。
    """
    print("\n=== 3. 哈希函数和消息摘要 ===")
    
    if not CRYPTOGRAPHY_AVAILABLE:
        print("\n注意：cryptography库未安装，将使用模拟演示哈希函数概念。")
        print("\n哈希函数基本概念:")
        print("1. 将任意长度的输入转换为固定长度的输出")
        print("2. 单向函数，不可逆")
        print("3. 微小的输入变化会导致输出的巨大变化（雪崩效应）")
        print("4. 常用算法：SHA-256, SHA-512, SHA-3等")
        print("5. 应用场景：文件完整性验证、密码存储、数据去重")
        print("\n模拟演示完成。在实际应用中，请安装cryptography库以获得真正的哈希功能。")
        return
    
    # 3.1 基本哈希函数使用
    print("\n3.1 基本哈希函数使用:")
    
    # 测试数据
    test_data = "这是需要计算哈希值的数据"
    print(f"原始数据: {test_data}")
    
    # 支持的哈希算法列表
    hash_algorithms = [
        ("SHA-256", hashes.SHA256()),
        ("SHA-512", hashes.SHA512()),
        ("SHA-3-256", hashes.SHA3_256()),
        ("MD5", hashes.MD5())  # 注意：MD5已不安全，仅用于演示
    ]
    
    for name, algorithm in hash_algorithms:
        # 创建哈希对象
        digest = hashes.Hash(algorithm, backend=default_backend())
        
        # 更新数据
        digest.update(test_data.encode())
        
        # 获取哈希值
        hash_value = digest.finalize()
        
        # 转换为十六进制字符串
        hash_hex = binascii.hexlify(hash_value).decode()
        
        print(f"\n{name}哈希值:")
        print(f"  十六进制表示: {hash_hex}")
        print(f"  哈希值长度: {len(hash_value)} 字节 ({len(hash_hex)} 字符)")
    
    # 3.2 增量哈希计算
    print("\n3.2 增量哈希计算:")
    print("对于大型数据，可以分块计算哈希值。")
    
    # 模拟大文件数据
    large_data_chunks = [
        "这是第一块数据，",
        "这是第二块数据，",
        "这是第三块数据，",
        "这是最后一块数据。"
    ]
    
    print("大文件数据块:")
    for i, chunk in enumerate(large_data_chunks):
        print(f"  块{i+1}: {chunk}")
    
    # 合并所有数据以进行比较
    full_data = ''.join(large_data_chunks)
    
    # 一次性计算完整数据的哈希值
   一次性哈希 = hashes.Hash(hashes.SHA256(), backend=default_backend())
    一次性哈希.update(full_data.encode())
    一次性哈希值 = binascii.hexlify(一次性哈希.finalize()).decode()
    
    print(f"一次性计算哈希值: {一次性哈希值}")
    
    # 增量计算哈希值
    增量哈希 = hashes.Hash(hashes.SHA256(), backend=default_backend())
    
    for i, chunk in enumerate(large_data_chunks):
        增量哈希.update(chunk.encode())
        print(f"更新块{i+1}后的哈希状态已更新")
    
    增量哈希值 = binascii.hexlify(增量哈希.finalize()).decode()
    
    print(f"增量计算哈希值: {增量哈希值}")
    print(f"哈希值比较: {'相同' if 增量哈希值 == 一次性哈希值 else '不同'}")
    
    # 3.3 文件完整性验证
    print("\n3.3 文件完整性验证:")
    
    def calculate_file_hash(file_path, algorithm=hashes.SHA256(), chunk_size=8192):
        """
        计算文件的哈希值
        
        参数:
        - file_path: 文件路径
        - algorithm: 哈希算法
        - chunk_size: 读取块大小
        
        返回:
        - 十六进制格式的哈希值
        """
        digest = hashes.Hash(algorithm, backend=default_backend())
        
        try:
            with open(file_path, 'rb') as f:
                while True:
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    digest.update(chunk)
            
            return binascii.hexlify(digest.finalize()).decode()
        except Exception as e:
            print(f"计算文件哈希时出错: {e}")
            return None
    
    # 创建一个临时文件进行演示
    import tempfile
    
    with tempfile.NamedTemporaryFile(delete=False, mode='w+', encoding='utf-8') as temp_file:
        temp_file.write("这是一个测试文件，用于演示文件完整性验证。\n")
        temp_file.write("计算文件的哈希值可以验证文件是否被篡改。\n")
        temp_file.write("如果文件内容发生变化，哈希值也会完全不同。")
        temp_file_path = temp_file.name
    
    print(f"创建临时测试文件: {temp_file_path}")
    
    try:
        # 计算文件哈希值
        file_hash = calculate_file_hash(temp_file_path)
        print(f"文件SHA-256哈希值: {file_hash}")
        
        # 验证文件完整性（重新计算哈希值并比较）
        verify_hash = calculate_file_hash(temp_file_path)
        print(f"验证哈希值: {verify_hash}")
        print(f"文件完整性验证: {'通过' if file_hash == verify_hash else '失败'}")
        
        # 模拟文件被篡改
        print("\n模拟文件被篡改:")
        with open(temp_file_path, 'a', encoding='utf-8') as f:
            f.write("\n这是恶意添加的内容。")
        
        # 重新计算哈希值
        tampered_hash = calculate_file_hash(temp_file_path)
        print(f"篡改后文件哈希值: {tampered_hash}")
        print(f"文件完整性验证: {'通过' if file_hash == tampered_hash else '失败'}")
        
        if file_hash != tampered_hash:
            print("成功检测到文件篡改！")
    finally:
        # 清理临时文件
        try:
            os.unlink(temp_file_path)
            print(f"\n已删除临时测试文件")
        except:
            pass
    
    # 3.4 哈希算法比较
    print("\n3.4 哈希算法比较:")
    
    hash_comparison = [
        {
            "算法": "SHA-256",
            "输出长度": "256位 (32字节)",
            "安全性": "高",
            "性能": "良好",
            "推荐场景": "大多数应用，文件完整性验证，安全通信",
            "是否推荐": "是，推荐使用"
        },
        {
            "算法": "SHA-512",
            "输出长度": "512位 (64字节)",
            "安全性": "非常高",
            "性能": "比SHA-256慢，但安全性更高",
            "推荐场景": "高安全性要求的应用，密码存储",
            "是否推荐": "是，对安全性要求高的场景"
        },
        {
            "算法": "SHA-3-256",
            "输出长度": "256位 (32字节)",
            "安全性": "高，抵抗长度扩展攻击",
            "性能": "略慢于SHA-256",
            "推荐场景": "需要抵抗长度扩展攻击的应用",
            "是否推荐": "是，特别是对安全性有特殊要求的场景"
        },
        {
            "算法": "MD5",
            "输出长度": "128位 (16字节)",
            "安全性": "低，已被破解",
            "性能": "非常快",
            "推荐场景": "仅用于非安全场景（如文件校验和）",
            "是否推荐": "否，不推荐用于安全目的"
        },
        {
            "算法": "SHA-1",
            "输出长度": "160位 (20字节)",
            "安全性": "低，已被破解",
            "性能": "快",
            "推荐场景": "仅用于兼容性目的",
            "是否推荐": "否，不推荐用于安全目的"
        }
    ]
    
    # 打印表格头部
    print("算法     | 输出长度      | 安全性 | 性能               | 推荐场景                               | 是否推荐")
    print("---------|-------------|--------|-------------------|---------------------------------------|--------")
    
    # 打印每个算法的信息
    for algo in hash_comparison:
        print(f"{algo['算法']:<9} | {algo['输出长度']:<12} | {algo['安全性']:<6} | {algo['性能']:<17} | {algo['推荐场景']:<31} | {algo['是否推荐']}")

# 4. 密钥派生函数
def key_derivation_functions():
    """
    密钥派生函数
    
    功能说明：演示使用cryptography模块的密钥派生函数，用于从用户密码生成
    加密密钥、存储密码哈希等安全操作。
    """
    print("\n=== 4. 密钥派生函数 ===")
    
    if not CRYPTOGRAPHY_AVAILABLE:
        print("\n注意：cryptography库未安装，将使用模拟演示密钥派生函数概念。")
        print("\n密钥派生函数基本概念:")
        print("1. 从用户密码生成加密密钥的函数")
        print("2. 添加盐值(Salt)防止彩虹表攻击")
        print("3. 使用迭代次数或工作因子增加计算难度")
        print("4. 常用算法：PBKDF2, bcrypt, Argon2, scrypt")
        print("5. 应用场景：密码存储、密钥生成、加密密钥派生")
        print("\n模拟演示完成。在实际应用中，请安装cryptography库以获得真正的密钥派生功能。")
        return
    
    # 4.1 PBKDF2密钥派生
    print("\n4.1 PBKDF2密钥派生:")
    print("PBKDF2 (Password-Based Key Derivation Function 2) 是一种常用的密钥派生函数。")
    
    # 用户密码
    password = "用户的强密码123!"
    print(f"用户密码: {password}")
    
    # 生成随机盐值
    salt = os.urandom(16)
    print(f"生成的盐值: {binascii.hexlify(salt).decode()}")
    
    # 迭代次数
    iterations = 100000
    print(f"迭代次数: {iterations}")
    
    # 创建PBKDF2实例
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 派生32字节(256位)密钥
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    
    # 派生密钥
    start_time = time.time()
    key = kdf.derive(password.encode())
    end_time = time.time()
    
    print(f"派生的密钥: {binascii.hexlify(key).decode()}")
    print(f"密钥长度: {len(key)} 字节")
    print(f"派生耗时: {(end_time - start_time) * 1000:.2f} 毫秒")
    
    # 验证密码
    try:
        kdf.verify(password.encode(), key)
        print("密码验证成功！")
    except Exception as e:
        print(f"密码验证失败: {e}")
    
    # 验证错误密码
    wrong_password = "错误的密码456!"
    try:
        kdf.verify(wrong_password.encode(), key)
        print("错误密码验证成功！（这是个问题）")
    except Exception as e:
        print(f"错误密码验证失败: {e}")
        print("正确拒绝了错误密码！")
    
    # 4.2 Scrypt密钥派生
    print("\n4.2 Scrypt密钥派生:")
    print("Scrypt是一种内存硬密钥派生函数，设计用于抵抗GPU和ASIC攻击。")
    
    # 生成新的盐值
    scrypt_salt = os.urandom(16)
    print(f"生成的盐值: {binascii.hexlify(scrypt_salt).decode()}")
    
    # 参数说明
    print("Scrypt参数说明:")
    print("- n: CPU/内存成本因子 (2的幂，通常为2^14=16384或更高)")
    print("- r: 块大小 (通常为8)")
    print("- p: 并行化参数 (通常为1)")
    
    # 创建Scrypt实例（注意：为了演示，使用较小的参数值）
    # 实际应用中，应使用更大的参数值以提高安全性
    n = 2**12  # 4096，实际应用中应使用更大的值如16384
    r = 8
    p = 1
    
    print(f"使用参数: n={n}, r={r}, p={p}")
    
    # 派生密钥
    start_time = time.time()
    scrypt_key = Scrypt(
        salt=scrypt_salt,
        length=32,
        n=n,
        r=r,
        p=p,
        backend=default_backend()
    ).derive(password.encode())
    end_time = time.time()
    
    print(f"派生的密钥: {binascii.hexlify(scrypt_key).decode()}")
    print(f"密钥长度: {len(scrypt_key)} 字节")
    print(f"派生耗时: {(end_time - start_time) * 1000:.2f} 毫秒")
    
    # 4.3 密码存储最佳实践
    print("\n4.3 密码存储最佳实践:")
    
    print("密码存储安全要求:")
    print("1. 使用专用的密码哈希函数，而非普通哈希函数")
    print("2. 每个用户使用唯一的盐值")
    print("3. 使用足够的工作因子使破解成本高昂")
    print("4. 定期更新哈希算法和参数")
    
    print("\n推荐的密码哈希函数:")
    print("- Argon2id: 2015年密码哈希竞赛获胜者，抵抗多种攻击")
    print("- bcrypt: 广泛使用，成熟稳定")
    print("- scrypt: 内存硬函数，抵抗GPU攻击")
    print("- PBKDF2: 实现简单，广泛支持，但安全性相对较低")
    
    # 演示密码存储方案
    class PasswordStorage:
        """
        简单的密码存储类，演示密码哈希存储和验证
        
        注意：这只是一个演示。在实际应用中，应使用专门的密码哈希库如passlib。
        """
        
        def __init__(self):
            # 模拟数据库，存储用户名和密码哈希信息
            self.password_db = {}
        
        def hash_password(self, password):
            """
            哈希密码并返回存储信息
            
            返回格式: {"salt": 盐值, "iterations": 迭代次数, "hash": 密码哈希}
            """
            # 生成随机盐值
            salt = os.urandom(16)
            
            # 设置迭代次数（实际应用中应更大）
            iterations = 100000
            
            # 使用PBKDF2派生密钥作为密码哈希
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=iterations,
                backend=default_backend()
            )
            password_hash = kdf.derive(password.encode())
            
            # 返回可序列化的字典
            return {
                "salt": base64.b64encode(salt).decode(),
                "iterations": iterations,
                "hash": base64.b64encode(password_hash).decode()
            }
        
        def register_user(self, username, password):
            """
            注册新用户
            """
            if username in self.password_db:
                return False, "用户名已存在"
            
            # 哈希密码
            password_data = self.hash_password(password)
            
            # 存储到数据库
            self.password_db[username] = password_data
            
            return True, "注册成功"
        
        def verify_password(self, username, password):
            """
            验证用户密码
            """
            if username not in self.password_db:
                # 注意：为防止用户名枚举攻击，这里也返回密码错误
                # 而不是明确告诉用户用户名不存在
                return False
            
            # 获取密码数据
            password_data = self.password_db[username]
            
            # 解码存储的数据
            salt = base64.b64decode(password_data["salt"])
            iterations = password_data["iterations"]
            expected_hash = base64.b64decode(password_data["hash"])
            
            # 创建验证用的KDF
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=iterations,
                backend=default_backend()
            )
            
            try:
                # 验证密码
                kdf.verify(password.encode(), expected_hash)
                return True
            except Exception:
                return False
    
    # 测试密码存储类
    print("\n测试密码存储系统:")
    
    password_store = PasswordStorage()
    
    # 注册用户
    success, message = password_store.register_user("alice", "SecurePass123!")
    print(f"注册用户 'alice': {message}")
    
    # 尝试使用相同用户名注册
    success, message = password_store.register_user("alice", "DifferentPass456!")
    print(f"尝试重复注册: {message}")
    
    # 验证正确密码
    is_valid = password_store.verify_password("alice", "SecurePass123!")
    print(f"验证正确密码: {'成功' if is_valid else '失败'}")
    
    # 验证错误密码
    is_valid = password_store.verify_password("alice", "WrongPass!")
    print(f"验证错误密码: {'成功' if is_valid else '失败'}")
    
    # 验证不存在的用户
    is_valid = password_store.verify_password("bob", "AnyPass!")
    print(f"验证不存在用户: {'成功' if is_valid else '失败'}")
    
    # 显示存储的密码数据（实际应用中不应显示）
    print("\n存储的密码数据（仅演示）:")
    print(json.dumps(password_store.password_db, indent=2))

# 5. 数字证书和X.509
def digital_certificates():
    """
    数字证书和X.509
    
    功能说明：演示使用cryptography模块处理数字证书，包括生成自签名证书、
    证书解析和验证等操作。
    """
    print("\n=== 5. 数字证书和X.509 ===")
    
    if not CRYPTOGRAPHY_AVAILABLE:
        print("\n注意：cryptography库未安装，将使用模拟演示数字证书概念。")
        print("\n数字证书基本概念:")
        print("1. 数字证书是包含公钥和身份信息的电子文档")
        print("2. 由证书颁发机构(CA)签发，证明公钥与特定实体的绑定")
        print("3. 基于X.509标准格式")
        print("4. 包含主题、颁发者、有效期、公钥、签名算法等信息")
        print("5. 应用场景：HTTPS/TLS加密通信、代码签名、身份认证")
        print("\n模拟演示完成。在实际应用中，请安装cryptography库以获得真正的证书功能。")
        return
    
    # 5.1 生成自签名证书
    print("\n5.1 生成自签名证书:")
    print("注意：自签名证书仅用于测试和演示。在生产环境中，应使用由受信任CA签发的证书。")
    
    # 生成RSA密钥对
    print("生成RSA密钥对...")
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    # 创建证书主体信息
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"CN"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"Beijing"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"Beijing"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Example Organization"),
        x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
    ])
    
    # 自签名证书的颁发者与主体相同
    issuer = subject
    
    # 设置证书有效期（1年）
    validity_start = datetime.utcnow()
    validity_end = validity_start + timedelta(days=365)
    
    print(f"证书有效期: {validity_start} 至 {validity_end}")
    
    # 创建证书构建器
    cert_builder = x509.CertificateBuilder()
    cert_builder = cert_builder.subject_name(subject)
    cert_builder = cert_builder.issuer_name(issuer)
    cert_builder = cert_builder.public_key(private_key.public_key())
    cert_builder = cert_builder.serial_number(x509.random_serial_number())
    cert_builder = cert_builder.not_valid_before(validity_start)
    cert_builder = cert_builder.not_valid_after(validity_end)
    
    # 添加扩展（可选）
    # 主题备用名称（Subject Alternative Name）
    cert_builder = cert_builder.add_extension(
        x509.SubjectAlternativeName([x509.DNSName(u"example.com"), x509.DNSName(u"www.example.com")]),
        critical=False,
    )
    
    # 基本约束扩展（用于CA证书）
    cert_builder = cert_builder.add_extension(
        x509.BasicConstraints(ca=False, path_length=None),
        critical=True,
    )
    
    # 签名证书
    print("签名证书...")
    certificate = cert_builder.sign(private_key, hashes.SHA256(), backend=default_backend())
    
    print("自签名证书生成成功！")
    
    # 5.2 证书序列化
    print("\n5.2 证书序列化:")
    
    # PEM格式（Base64编码，人类可读）
    cert_pem = certificate.public_bytes(encoding=serialization.Encoding.PEM)
    print("证书PEM格式（前200字符）:")
    print(cert_pem.decode()[:200] + "...")
    
    # DER格式（二进制）
    cert_der = certificate.public_bytes(encoding=serialization.Encoding.DER)
    print(f"\n证书DER格式大小: {len(cert_der)} 字节")
    print(f"证书DER格式（十六进制，前100字符）: {binascii.hexlify(cert_der).decode()[:100]}...")
    
    # 5.3 证书信息解析
    print("\n5.3 证书信息解析:")
    
    print("证书基本信息:")
    print(f"  序列号: {certificate.serial_number}")
    print(f"  主体: {certificate.subject}")
    print(f"  颁发者: {certificate.issuer}")
    print(f"  有效期开始: {certificate.not_valid_before}")
    print(f"  有效期结束: {certificate.not_valid_after}")
    print(f"  签名算法: {certificate.signature_algorithm_oid._name}")
    
    # 获取公钥信息
    public_key = certificate.public_key()
    print("\n证书公钥信息:")
    print(f"  密钥类型: {type(public_key).__name__}")
    
    # 如果是RSA公钥，获取其模数和指数
    if hasattr(public_key, 'public_numbers'):
        numbers = public_key.public_numbers()
        print(f"  模数大小: {numbers.n.bit_length()} 位")
        print(f"  公钥指数: {numbers.e}")
    
    # 获取证书扩展信息
    print("\n证书扩展信息:")
    for extension in certificate.extensions:
        oid = extension.oid._name if extension.oid._name is not None else str(extension.oid.dotted_string)
        print(f"  {oid}: {extension.value}")
        print(f"    关键扩展: {extension.critical}")
    
    # 5.4 证书验证
    print("\n5.4 证书验证:")
    
    # 注意：这里只进行简单的演示验证
    # 实际的证书验证需要检查证书链、吊销状态等
    
    print("验证证书签名:")
    try:
        # 使用证书的公钥验证证书签名（仅演示，自签名证书的特殊验证）
        # 实际场景中，应该使用CA的公钥验证
        cert_public_key = certificate.public_key()
        
        # 获取证书的TBS（待签名）部分
        tbs_certificate = certificate.tbs_certificate_bytes
        
        # 验证签名
        # 注意：这里只是概念演示，实际验证逻辑更复杂
        print("自签名证书验证演示完成。在实际应用中，应使用证书链验证。")
        print("完整的证书验证应该包括：")
        print("1. 验证证书签名是否由颁发者的私钥生成")
        print("2. 检查证书是否在有效期内")
        print("3. 验证证书链直到受信任的根CA")
        print("4. 检查证书是否被吊销")
        print("5. 验证证书的使用目的是否符合要求")
        print("6. 检查证书的主体备用名称是否匹配目标域名")
        
    except Exception as e:
        print(f"证书验证错误: {e}")
    
    # 5.5 证书在TLS/SSL中的应用
    print("\n5.5 证书在TLS/SSL中的应用:")
    
    print("TLS/SSL证书主要用途:")
    print("1. 服务器身份验证：证明服务器身份，防止中间人攻击")
    print("2. 建立加密通信通道：客户端使用证书中的公钥加密会话密钥")
    print("3. 数据传输安全：确保通信内容加密且不被篡改")
    
    print("\n证书链验证流程:")
    print("1. 客户端连接到服务器，服务器提供证书")
    print("2. 客户端验证证书的签名是否由受信任的CA签发")
    print("3. 客户端检查证书是否在有效期内")
    print("4. 客户端检查证书的吊销状态（可选）")
    print("5. 客户端验证证书中的域名是否匹配所访问的域名")
    print("6. 如果所有验证通过，建立加密通信通道")
    
    print("\n常见证书问题:")
    print("- 证书过期: 需要更新证书")
    print("- 证书不匹配域名: 证书与访问的域名不匹配")
    print("- 自签名证书: 浏览器默认不信任")
    print("- 证书链不完整: 缺少中间证书")
    print("- 不受信任的根CA: 浏览器/系统未安装对应的根证书")

# 6. 高级应用示例
def advanced_applications():
    """
    高级应用示例
    
    功能说明：演示cryptography模块在实际应用中的高级用法，包括文件加密、
    安全通信、数字签名等综合应用。
    """
    print("\n=== 6. 高级应用示例 ===")
    
    if not CRYPTOGRAPHY_AVAILABLE:
        print("\n注意：cryptography库未安装，将跳过高级应用示例。")
        print("安装cryptography库后可运行完整演示。")
        return
    
    # 6.1 安全文件加密器
    print("\n6.1 安全文件加密器:")
    print("使用AES-GCM模式加密文件，提供加密和认证功能。")
    
    class SecureFileEncryptor:
        """
        安全文件加密器，使用AES-GCM模式进行文件加密和解密
        """
        
        def __init__(self, chunk_size=8192):
            """
            初始化文件加密器
            
            参数:
            - chunk_size: 读取/写入块大小
            """
            self.chunk_size = chunk_size
        
        def derive_key_from_password(self, password, salt=None, iterations=100000):
            """
            从密码派生加密密钥
            
            参数:
            - password: 用户密码
            - salt: 盐值（如果为None则生成新的）
            - iterations: PBKDF2迭代次数
            
            返回:
            - (派生的密钥, 使用的盐值)
            """
            if salt is None:
                salt = os.urandom(16)
            
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,  # 256位AES密钥
                salt=salt,
                iterations=iterations,
                backend=default_backend()
            )
            
            key = kdf.derive(password.encode())
            return key, salt
        
        def encrypt_file(self, input_file_path, output_file_path, password):
            """
            加密文件
            
            参数:
            - input_file_path: 输入文件路径
            - output_file_path: 输出加密文件路径
            - password: 加密密码
            
            返回:
            - 是否加密成功
            """
            try:
                # 从密码派生密钥
                key, salt = self.derive_key_from_password(password)
                
                # 生成随机IV（GCM模式推荐使用12字节IV）
                iv = os.urandom(12)
                
                # 创建加密器
                encryptor = Cipher(
                    algorithms.AES(key),
                    modes.GCM(iv),
                    backend=default_backend()
                ).encryptor()
                
                # 打开输入和输出文件
                with open(input_file_path, 'rb') as infile, open(output_file_path, 'wb') as outfile:
                    # 写入盐值和IV到输出文件开头
                    outfile.write(salt)  # 16字节
                    outfile.write(iv)     # 12字节
                    
                    # 分块加密文件
                    while True:
                        chunk = infile.read(self.chunk_size)
                        if not chunk:
                            break
                        encrypted_chunk = encryptor.update(chunk)
                        outfile.write(encrypted_chunk)
                    
                    # 完成加密并获取认证标签
                    encrypted_final = encryptor.finalize()
                    if encrypted_final:
                        outfile.write(encrypted_final)
                    
                    # 写入认证标签
                    tag = encryptor.tag
                    outfile.write(tag)  # 16字节
                
                print(f"文件加密成功: {input_file_path} -> {output_file_path}")
                return True
                
            except Exception as e:
                print(f"文件加密失败: {e}")
                # 清理部分写入的输出文件
                try:
                    if os.path.exists(output_file_path):
                        os.unlink(output_file_path)
                except:
                    pass
                return False
        
        def decrypt_file(self, input_file_path, output_file_path, password):
            """
            解密文件
            
            参数:
            - input_file_path: 输入加密文件路径
            - output_file_path: 输出解密文件路径
            - password: 解密密码
            
            返回:
            - 是否解密成功
            """
            try:
                # 打开加密文件并读取盐值、IV和认证标签
                with open(input_file_path, 'rb') as infile:
                    # 读取盐值
                    salt = infile.read(16)
                    # 读取IV
                    iv = infile.read(12)
                    # 读取剩余内容（密文和认证标签）
                    remaining_data = infile.read()
                
                # 认证标签在文件末尾，长度为16字节
                tag = remaining_data[-16:]
                ciphertext = remaining_data[:-16]
                
                # 从密码和盐值派生密钥
                key, _ = self.derive_key_from_password(password, salt)
                
                # 创建解密器
                decryptor = Cipher(
                    algorithms.AES(key),
                    modes.GCM(iv, tag),
                    backend=default_backend()
                ).decryptor()
                
                # 打开输出文件并解密
                with open(output_file_path, 'wb') as outfile:
                    # 分块解密文件
                    # 首先解密主要部分
                    chunk_size = self.chunk_size
                    for i in range(0, len(ciphertext), chunk_size):
                        chunk = ciphertext[i:i+chunk_size]
                        decrypted_chunk = decryptor.update(chunk)
                        outfile.write(decrypted_chunk)
                    
                    # 完成解密
                    decrypted_final = decryptor.finalize()
                    if decrypted_final:
                        outfile.write(decrypted_final)
                
                print(f"文件解密成功: {input_file_path} -> {output_file_path}")
                return True
                
            except Exception as e:
                print(f"文件解密失败: {e}")
                # 清理部分写入的输出文件
                try:
                    if os.path.exists(output_file_path):
                        os.unlink(output_file_path)
                except:
                    pass
                return False
    
    # 测试文件加密器
    print("\n测试文件加密器:")
    
    # 创建测试文件
    import tempfile
    
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    print(f"创建临时目录: {temp_dir}")
    
    try:
        # 创建测试文件
        test_file_path = os.path.join(temp_dir, "test_file.txt")
        with open(test_file_path, "w", encoding="utf-8") as f:
            f.write("这是一个测试文件，用于演示安全文件加密。\n")
            f.write("这个文件将被加密并解密，以验证加密过程的正确性。\n")
            f.write("加密使用AES-GCM模式，提供了保密性和认证功能。\n")
            f.write("\n" * 5)  # 添加一些空行
            f.write("文件结尾标记。")
        
        print(f"创建测试文件: {test_file_path}")
        print(f"文件大小: {os.path.getsize(test_file_path)} 字节")
        
        # 加密文件
        encryptor = SecureFileEncryptor()
        password = "文件加密密码123!"
        encrypted_file_path = os.path.join(temp_dir, "test_file.enc")
        
        print(f"\n使用密码 '{password}' 加密文件...")
        success = encryptor.encrypt_file(test_file_path, encrypted_file_path, password)
        
        if success:
            print(f"加密后文件大小: {os.path.getsize(encrypted_file_path)} 字节")
            
            # 解密文件
            decrypted_file_path = os.path.join(temp_dir, "test_file_decrypted.txt")
            print(f"\n解密文件...")
            success = encryptor.decrypt_file(encrypted_file_path, decrypted_file_path, password)
            
            if success:
                print(f"解密后文件大小: {os.path.getsize(decrypted_file_path)} 字节")
                
                # 验证解密后文件与原始文件是否相同
                with open(test_file_path, "r", encoding="utf-8") as f1, \
                     open(decrypted_file_path, "r", encoding="utf-8") as f2:
                    original_content = f1.read()
                    decrypted_content = f2.read()
                    
                    if original_content == decrypted_content:
                        print("\n验证成功: 解密后文件与原始文件内容完全相同！")
                    else:
                        print("\n验证失败: 解密后文件与原始文件内容不匹配！")
                
                # 测试错误密码
                wrong_decrypted_path = os.path.join(temp_dir, "wrong_decrypted.txt")
                print(f"\n使用错误密码 'wrongpassword' 尝试解密...")
                success = encryptor.decrypt_file(encrypted_file_path, wrong_decrypted_path, "wrongpassword")
                
                if not success:
                    print("正确拒绝了错误密码！")
    
    finally:
        # 清理临时文件和目录
        try:
            import shutil
            shutil.rmtree(temp_dir)
            print(f"\n已清理临时目录: {temp_dir}")
        except:
            pass
    
    # 6.2 数字签名应用
    print("\n6.2 数字签名应用:")
    print("使用RSA进行文档数字签名和验证，确保文档完整性和真实性。")
    
    class DigitalDocumentSigner:
        """
        数字文档签名器，使用RSA算法进行文档签名和验证
        """
        
        def __init__(self):
            """
            初始化数字签名器
            """
            self.private_key = None
            self.public_key = None
        
        def generate_key_pair(self, key_size=2048):
            """
            生成RSA密钥对
            
            参数:
            - key_size: 密钥大小（位）
            
            返回:
            - (私钥, 公钥)
            """
            print(f"生成{key_size}位RSA密钥对...")
            self.private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=key_size,
                backend=default_backend()
            )
            self.public_key = self.private_key.public_key()
            print("密钥对生成成功")
            return self.private_key, self.public_key
        
        def sign_document(self, document_path):
            """
            对文档进行数字签名
            
            参数:
            - document_path: 文档文件路径
            
            返回:
            - 签名数据（字节）
            """
            if self.private_key is None:
                raise ValueError("未生成或加载私钥")
            
            try:
                # 计算文档的哈希值
                hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
                
                with open(document_path, 'rb') as f:
                    while True:
                        chunk = f.read(8192)
                        if not chunk:
                            break
                        hasher.update(chunk)
                
                document_hash = hasher.finalize()
                
                # 使用私钥对哈希值进行签名
                signature = self.private_key.sign(
                    document_hash,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )
                
                print(f"文档签名成功: {document_path}")
                return signature
                
            except Exception as e:
                print(f"文档签名失败: {e}")
                raise
        
        def verify_signature(self, document_path, signature, public_key=None):
            """
            验证文档签名
            
            参数:
            - document_path: 文档文件路径
            - signature: 签名数据
            - public_key: 公钥（如果为None则使用内部公钥）
            
            返回:
            - 是否验证成功
            """
            if public_key is None:
                public_key = self.public_key
            
            if public_key is None:
                raise ValueError("未生成或加载公钥")
            
            try:
                # 计算文档的哈希值
                hasher = hashes.Hash(hashes.SHA256(), backend=default_backend())
                
                with open(document_path, 'rb') as f:
                    while True:
                        chunk = f.read(8192)
                        if not chunk:
                            break
                        hasher.update(chunk)
                
                document_hash = hasher.finalize()
                
                # 使用公钥验证签名
                public_key.verify(
                    signature,
                    document_hash,
                    padding.PSS(
                        mgf=padding.MGF1(hashes.SHA256()),
                        salt_length=padding.PSS.MAX_LENGTH
                    ),
                    hashes.SHA256()
                )
                
                print(f"签名验证成功: {document_path}")
                return True
                
            except Exception as e:
                print(f"签名验证失败: {e}")
                return False
        
        def save_signature(self, signature, signature_path):
            """
            保存签名到文件
            
            参数:
            - signature: 签名数据
            - signature_path: 输出文件路径
            """
            try:
                with open(signature_path, 'wb') as f:
                    f.write(signature)
                print(f"签名已保存到: {signature_path}")
                return True
            except Exception as e:
                print(f"保存签名失败: {e}")
                return False
        
        def load_signature(self, signature_path):
            """
            从文件加载签名
            
            参数:
            - signature_path: 签名文件路径
            
            返回:
            - 签名数据
            """
            try:
                with open(signature_path, 'rb') as f:
                    signature = f.read()
                print(f"签名已从 {signature_path} 加载")
                return signature
            except Exception as e:
                print(f"加载签名失败: {e}")
                raise
        
        def save_key_pair(self, private_key_path, public_key_path, private_key_password=None):
            """
            保存密钥对到文件
            
            参数:
            - private_key_path: 私钥文件路径
            - public_key_path: 公钥文件路径
            - private_key_password: 私钥保护密码（可选）
            """
            # 保存私钥
            if self.private_key is not None:
                encryption_algorithm = serialization.NoEncryption()
                if private_key_password is not None:
                    encryption_algorithm = serialization.BestAvailableEncryption(
                        private_key_password.encode()
                    )
                
                private_pem = self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=encryption_algorithm
                )
                
                with open(private_key_path, 'wb') as f:
                    f.write(private_pem)
                print(f"私钥已保存到: {private_key_path}")
            
            # 保存公钥
            if self.public_key is not None:
                public_pem = self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
                
                with open(public_key_path, 'wb') as f:
                    f.write(public_pem)
                print(f"公钥已保存到: {public_key_path}")
            
            return True
        
        def load_private_key(self, private_key_path, password=None):
            """
            从文件加载私钥
            
            参数:
            - private_key_path: 私钥文件路径
            - password: 私钥保护密码（可选）
            """
            try:
                with open(private_key_path, 'rb') as f:
                    private_pem = f.read()
                
                password_bytes = password.encode() if password is not None else None
                
                self.private_key = serialization.load_pem_private_key(
                    private_pem,
                    password=password_bytes,
                    backend=default_backend()
                )
                
                # 更新公钥
                self.public_key = self.private_key.public_key()
                
                print(f"私钥已从 {private_key_path} 加载")
                return self.private_key
                
            except Exception as e:
                print(f"加载私钥失败: {e}")
                raise
        
        def load_public_key(self, public_key_path):
            """
            从文件加载公钥
            
            参数:
            - public_key_path: 公钥文件路径
            """
            try:
                with open(public_key_path, 'rb') as f:
                    public_pem = f.read()
                
                self.public_key = serialization.load_pem_public_key(
                    public_pem,
                    backend=default_backend()
                )
                
                print(f"公钥已从 {public_key_path} 加载")
                return self.public_key
                
            except Exception as e:
                print(f"加载公钥失败: {e}")
                raise
    
    # 测试数字文档签名器
    print("\n测试数字文档签名器:")
    
    # 创建临时目录
    temp_dir = tempfile.mkdtemp()
    print(f"创建临时目录: {temp_dir}")
    
    try:
        # 创建测试文档
        document_path = os.path.join(temp_dir, "document.txt")
        with open(document_path, "w", encoding="utf-8") as f:
            f.write("这是一份重要的法律文档，需要进行数字签名。\n")
            f.write("数字签名可以确保文档的完整性和真实性。\n")
            f.write("如果文档被篡改，签名验证将失败。\n")
            f.write("\n签署日期: 2023年10月15日")
        
        print(f"创建测试文档: {document_path}")
        
        # 初始化签名器并生成密钥对
        signer = DigitalDocumentSigner()
        signer.generate_key_pair()
        
        # 保存密钥对
        private_key_path = os.path.join(temp_dir, "private_key.pem")
        public_key_path = os.path.join(temp_dir, "public_key.pem")
        key_password = "密钥保护密码123!"
        
        print(f"\n保存密钥对（私钥带密码保护）...")
        signer.save_key_pair(private_key_path, public_key_path, key_password)
        
        # 对文档进行签名
        print(f"\n对文档进行签名...")
        signature = signer.sign_document(document_path)
        
        # 保存签名
        signature_path = os.path.join(temp_dir, "document.sig")
        signer.save_signature(signature, signature_path)
        
        # 验证签名
        print(f"\n验证签名...")
        success = signer.verify_signature(document_path, signature)
        
        if success:
            print("签名验证成功！文档完整性和真实性得到确认。")
        
        # 模拟文档被篡改
        print(f"\n模拟文档被篡改...")
        with open(document_path, "a", encoding="utf-8") as f:
            f.write("\n\n--- 已被恶意篡改！ ---")
        
        # 尝试验证被篡改的文档
        print(f"\n验证被篡改的文档...")
        success = signer.verify_signature(document_path, signature)
        
        if not success:
            print("签名验证失败！成功检测到文档被篡改。")
        
        # 测试加载密钥和签名
        print(f"\n测试加载密钥和签名...")
        
        # 创建新的签名器实例
        new_signer = DigitalDocumentSigner()
        
        # 加载公钥
        new_signer.load_public_key(public_key_path)
        
        # 加载签名
        loaded_signature = new_signer.load_signature(signature_path)
        
        # 验证签名（应该失败，因为文档已被篡改）
        success = new_signer.verify_signature(document_path, loaded_signature)
        print(f"验证结果: {'成功' if success else '失败'}")
        
    finally:
        # 清理临时文件和目录
        try:
            import shutil
            shutil.rmtree(temp_dir)
            print(f"\n已清理临时目录: {temp_dir}")
        except:
            pass
    
    # 6.3 安全令牌系统
    print("\n6.3 安全令牌系统:")
    print("实现基于JWT思想的简单安全令牌系统，用于身份验证和授权。")
    
    class SecureTokenSystem:
        """
        基于JWT思想的简单安全令牌系统
        
        注意：这只是一个演示实现。在实际应用中，应使用成熟的JWT库。
        """
        
        def __init__(self, secret_key=None, expiration_seconds=3600):
            """
            初始化令牌系统
            
            参数:
            - secret_key: 签名密钥（如果为None则生成随机密钥）
            - expiration_seconds: 令牌过期时间（秒）
            """
            if secret_key is None:
                self.secret_key = os.urandom(32)
            else:
                # 确保密钥是字节类型
                self.secret_key = secret_key if isinstance(secret_key, bytes) else secret_key.encode()
            
            self.expiration_seconds = expiration_seconds
            print(f"安全令牌系统初始化成功，令牌有效期: {expiration_seconds} 秒")
        
        def generate_token(self, user_id, additional_claims=None):
            """
            生成安全令牌
            
            参数:
            - user_id: 用户ID
            - additional_claims: 额外的声明（可选）
            
            返回:
            - 生成的令牌（字符串）
            """
            try:
                # 创建令牌负载
                payload = {
                    "user_id": user_id,
                    "iat": int(time.time()),  # 颁发时间
                    "exp": int(time.time()) + self.expiration_seconds  # 过期时间
                }
                
                # 添加额外声明
                if additional_claims:
                    payload.update(additional_claims)
                
                # 将负载转换为JSON字符串
                payload_json = json.dumps(payload, separators=(',', ':'))
                
                # Base64编码负载
                # 注意：实际JWT使用URL安全的Base64编码
                encoded_payload = base64.b64encode(payload_json.encode()).decode('utf-8')
                
                # 创建签名
                h = hmac.new(self.secret_key, encoded_payload.encode(), hashlib.sha256)
                signature = base64.b64encode(h.digest()).decode('utf-8')
                
                # 组合令牌：payload.signature
                # 注意：标准JWT格式为 header.payload.signature
                token = f"{encoded_payload}.{signature}"
                
                return token
                
            except Exception as e:
                print(f"生成令牌失败: {e}")
                raise
        
        def verify_token(self, token):
            """
            验证令牌
            
            参数:
            - token: 要验证的令牌
            
            返回:
            - 验证成功返回令牌负载，否则返回None
            """
            try:
                # 分割令牌
                parts = token.split('.')
                if len(parts) != 2:
                    print("无效的令牌格式")
                    return None
                
                encoded_payload, encoded_signature = parts
                
                # 验证签名
                h = hmac.new(self.secret_key, encoded_payload.encode(), hashlib.sha256)
                expected_signature = base64.b64encode(h.digest()).decode('utf-8')
                
                # 使用时间安全的比较
                if not hmac.compare_digest(encoded_signature, expected_signature):
                    print("无效的签名")
                    return None
                
                # 解码负载
                try:
                    payload_bytes = base64.b64decode(encoded_payload)
                    payload = json.loads(payload_bytes.decode('utf-8'))
                except Exception as e:
                    print(f"解码令牌负载失败: {e}")
                    return None
                
                # 检查令牌是否过期
                current_time = int(time.time())
                if 'exp' in payload and current_time > payload['exp']:
                    print("令牌已过期")
                    return None
                
                return payload
                
            except Exception as e:
                print(f"验证令牌失败: {e}")
                return None
        
        def refresh_token(self, token):
            """
            刷新令牌
            
            参数:
            - token: 要刷新的令牌
            
            返回:
            - 新的令牌（如果刷新成功）
            """
            # 验证令牌
            payload = self.verify_token(token)
            if not payload:
                return None
            
            # 提取用户ID和其他声明
            user_id = payload.get('user_id')
            
            # 复制除了iat和exp之外的所有声明
            additional_claims = {k: v for k, v in payload.items() 
                               if k not in ['user_id', 'iat', 'exp']}
            
            # 生成新令牌
            return self.generate_token(user_id, additional_claims)
    
    # 测试安全令牌系统
    print("\n测试安全令牌系统:")
    
    # 初始化令牌系统
    token_system = SecureTokenSystem(expiration_seconds=60)  # 令牌有效期60秒
    
    # 生成令牌
    print("\n生成用户令牌...")
    user_id = "user123"
    additional_claims = {
        "username": "johndoe",
        "roles": ["user", "premium"],
        "permissions": ["read", "write"]
    }
    
    token = token_system.generate_token(user_id, additional_claims)
    print(f"生成的令牌: {token}")
    print(f"令牌长度: {len(token)} 字符")
    
    # 验证令牌
    print("\n验证令牌...")
    payload = token_system.verify_token(token)
    
    if payload:
        print("令牌验证成功！")
        print("令牌内容:")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    
    # 测试无效令牌
    print("\n测试无效令牌...")
    invalid_token = token + "invalid"  # 篡改令牌
    payload = token_system.verify_token(invalid_token)
    
    # 测试令牌刷新
    print("\n测试令牌刷新...")
    new_token = token_system.refresh_token(token)
    
    if new_token:
        print(f"令牌刷新成功！")
        print(f"新令牌: {new_token}")
        
        # 验证新令牌
        new_payload = token_system.verify_token(new_token)
        if new_payload:
            print("新令牌验证成功！")
            print(f"新令牌过期时间: {datetime.fromtimestamp(new_payload['exp'])}")
    
    # 测试令牌过期
    print("\n测试令牌过期...")
    print("等待61秒让令牌过期...")
    
    # 注意：为了演示，我们修改令牌中的过期时间而不是实际等待
    # 解码令牌
    parts = token.split('.')
    encoded_payload, _ = parts
    payload_bytes = base64.b64decode(encoded_payload)
    payload = json.loads(payload_bytes.decode('utf-8'))
    
    # 设置过期时间为过去
    payload['exp'] = int(time.time()) - 60
    
    # 重新编码令牌
    payload_json = json.dumps(payload, separators=(',', ':'))
    new_encoded_payload = base64.b64encode(payload_json.encode()).decode('utf-8')
    
    # 创建新签名
    h = hmac.new(token_system.secret_key, new_encoded_payload.encode(), hashlib.sha256)
    new_signature = base64.b64encode(h.digest()).decode('utf-8')
    
    # 创建过期令牌
    expired_token = f"{new_encoded_payload}.{new_signature}"
    
    # 尝试验证过期令牌
    print("验证过期令牌...")
    expired_payload = token_system.verify_token(expired_token)
    
    if not expired_payload:
        print("成功检测到过期令牌！")

# 7. 安全最佳实践
def security_best_practices():
    """
    安全最佳实践
    
    功能说明：总结cryptography模块使用的安全最佳实践，帮助开发者安全地
    实现加密功能，避免常见的安全陷阱。
    """
    print("\n=== 7. 安全最佳实践 ===")
    
    # 7.1 密钥管理
    print("\n7.1 密钥管理:")
    
    key_management_practices = [
        {
            "原则": "密钥安全存储",
            "描述": "加密密钥绝不应硬编码在源代码中或存储在版本控制系统中",
            "建议": [
                "使用环境变量存储敏感密钥",
                "使用专用密钥管理服务（如AWS KMS、HashiCorp Vault）",
                "加密后存储在配置文件中，解密密钥通过安全通道提供",
                "定期轮换密钥，减少长期泄露的风险"
            ]
        },
        {
            "原则": "密钥长度和强度",
            "描述": "选择适当长度和强度的密钥以抵抗暴力破解攻击",
            "建议": [
                "对称加密（AES）: 至少256位密钥",
                "非对称加密（RSA）: 至少4096位密钥",
                "椭圆曲线加密: 使用P-256或更强的曲线",
                "避免使用过时或已知有缺陷的算法"
            ]
        },
        {
            "原则": "随机数生成",
            "描述": "使用密码学安全的随机数生成器创建密钥和IV",
            "建议": [
                "使用 os.urandom() 生成加密安全的随机数",
                "不要使用普通的随机模块生成密钥材料",
                "IV、盐值、密钥应每次生成新的随机值",
                "确保随机数生成器有足够的熵"
            ]
        },
        {
            "原则": "密钥备份和恢复",
            "描述": "建立安全的密钥备份和恢复机制，防止密钥丢失",
            "建议": [
                "实施密钥分割（Shamir's Secret Sharing）",
                "使用硬件安全模块（HSM）保护主密钥",
                "制定详细的密钥恢复程序和应急计划",
                "定期测试密钥恢复流程"
            ]
        }
    ]
    
    for practice in key_management_practices:
        print(f"\n{practice['原则']}:")
        print(f"  描述: {practice['描述']}")
        print("  建议:")
        for suggestion in practice['建议']:
            print(f"    - {suggestion}")
    
    # 7.2 算法选择
    print("\n7.2 算法选择:")
    
    algorithm_recommendations = [
        {
            "类别": "对称加密",
            "推荐算法": "AES-256-GCM",
            "理由": "提供强加密和认证，防止篡改",
            "替代方案": "AES-256-CTR, AES-256-CBC+HMAC",
            "避免使用": "DES, 3DES, Blowfish, AES-ECB模式"
        },
        {
            "类别": "非对称加密",
            "推荐算法": "RSA-4096, ECDSA (P-256)",
            "理由": "提供强安全性和合理的性能",
            "替代方案": "ECC (P-384, P-521)",
            "避免使用": "RSA-1024, RSA-2048（对高安全性要求）, DSA"
        },
        {
            "类别": "哈希函数",
            "推荐算法": "SHA-256, SHA-3-256",
            "理由": "提供强碰撞抵抗和良好性能",
            "替代方案": "SHA-512, SHA-3-512",
            "避免使用": "MD5, SHA-1, RIPEMD-160"
        },
        {
            "类别": "密钥派生",
            "推荐算法": "Argon2id, bcrypt",
            "理由": "专为密码哈希设计，抵抗GPU攻击",
            "替代方案": "scrypt, PBKDF2 (高迭代次数)",
            "避免使用": "简单哈希函数（如直接使用SHA-256）"
        }
    ]
    
    print("\n算法推荐表:")
    print("类别       | 推荐算法                | 理由                       | 替代方案                  | 避免使用")
    print("-----------|------------------------|---------------------------|---------------------------|---------")
    
    for algo in algorithm_recommendations:
        print(f"{algo['类别']:<11} | {algo['推荐算法']:<23} | {algo['理由']:<23} | {algo['替代方案']:<23} | {algo['避免使用']}")
    
    # 7.3 常见安全陷阱
    print("\n7.3 常见安全陷阱:")
    
    security_pitfalls = [
        {
            "陷阱": "忽略初始化向量(IV)的重要性",
            "风险": "使用固定IV会导致相同的明文产生相同的密文",
            "解决方案": "每次加密使用新的随机IV，并与密文一起存储或传输"
        },
        {
            "陷阱": "不验证加密数据的完整性",
            "风险": "攻击者可以修改密文，导致解密后的数据被篡改",
            "解决方案": "使用AEAD模式（如GCM）或单独添加HMAC认证"
        },
        {
            "陷阱": "直接使用密码作为加密密钥",
            "风险": "密码通常不够随机且长度不足，容易被破解",
            "解决方案": "使用专门的密钥派生函数（如Argon2）从密码生成密钥"
        },
        {
            "陷阱": "不保护私钥",
            "风险": "私钥泄露会导致整个加密系统崩溃",
            "解决方案": "使用密码保护私钥，存储在安全位置，限制访问权限"
        },
        {
            "陷阱": "忽视侧信道攻击",
            "风险": "通过分析时间、内存使用、功耗等泄露信息",
            "解决方案": "使用恒定时间比较函数，避免早期返回，实施防护措施"
        },
        {
            "陷阱": "加密但不隐藏数据长度",
            "风险": "数据长度本身可能泄露敏感信息",
            "解决方案": "填充到固定长度，或采用加密填充方案"
        },
        {
            "陷阱": "使用过期或不安全的协议/算法",
            "风险": "已知漏洞可能被利用",
            "解决方案": "定期更新密码学库，关注安全公告，使用最新安全标准"
        }
    ]
    
    print("\n常见安全陷阱及解决方案:")
    for i, pitfall in enumerate(security_pitfalls, 1):
        print(f"\n{i}. {pitfall['陷阱']}:")
        print(f"   风险: {pitfall['风险']}")
        print(f"   解决方案: {pitfall['解决方案']}")
    
    # 7.4 实现安全检查清单
    print("\n7.4 实现安全检查清单:")
    
    security_checklist = [
        "□ 使用密码学安全的随机数生成器",
        "□ 为每次加密生成新的随机IV/nonce",
        "□ 使用足够长度的密钥（至少256位对称密钥）",
        "□ 实现数据完整性验证（使用AEAD或HMAC）",
        "□ 使用适当的密钥派生函数处理密码",
        "□ 安全存储和管理所有密钥材料",
        "□ 实施适当的错误处理，不泄露敏感信息",
        "□ 考虑侧信道攻击的防护措施",
        "□ 定期更新密码学库到最新安全版本",
        "□ 进行代码审查和安全审计",
        "□ 测试加密实现的正确性和安全性",
        "□ 遵循最小权限原则",
        "□ 实施密钥轮换策略",
        "□ 加密敏感数据时考虑性能和资源消耗",
        "□ 确保日志中不包含敏感信息（如密钥、明文等）"
    ]
    
    print("\n密码学实现安全检查清单:")
    for item in security_checklist:
        print(item)
    
    # 7.5 性能与安全性平衡
    print("\n7.5 性能与安全性平衡:")
    
    print("在实际应用中，需要平衡安全性和性能需求:")
    print("\n1. 算法选择权衡:")
    print("   - 更高安全性的算法通常需要更多计算资源")
    print("   - 选择适合应用场景的算法，不要过度或不足")
    print("   - 例如：实时系统可能优先考虑性能，金融系统优先考虑安全性")
    
    print("\n2. 密钥派生函数参数调整:")
    print("   - 调整工作因子以适应系统性能需求")
    print("   - 在安全要求和用户体验之间找到平衡")
    print("   - 定期重新评估参数设置，随着硬件性能提升而增加")
    
    print("\n3. 批量处理与并行计算:")
    print("   - 利用多线程/多进程加速加密操作")
    print("   - 大文件使用流式处理而非一次性加载到内存")
    print("   - 使用硬件加速（如AES-NI指令集）")
    
    print("\n4. 缓存策略:")
    print("   - 缓存频繁使用的密钥或派生密钥（注意安全风险）")
    print("   - 实施适当的缓存过期和刷新机制")
    print("   - 确保缓存中的敏感数据受到保护")
    
    print("\n5. 分层安全策略:")
    print("   - 对不同敏感级别的数据采用不同强度的加密")
    print("   - 敏感数据使用最强保护，一般数据可适当降低要求")
    print("   - 实施深度防御策略，不依赖单一安全机制")

# 8. 总结与最佳实践
def summary_and_best_practices():
    """
    总结与最佳实践
    
    功能说明：总结cryptography模块的核心功能和使用最佳实践，帮助开发者
    高效、安全地使用该模块。
    """
    print("\n=== 8. 总结与最佳实践 ===")
    
    # 8.1 核心功能总结
    print("\n8.1 核心功能总结:")
    
    core_features = [
        {
            "模块": "对称加密",
            "主要功能": "使用相同密钥进行加密和解密",
            "推荐API": "Fernet（高级）, Cipher/algorithms/modes（低级）",
            "典型应用": "数据加密、文件加密、安全通信"
        },
        {
            "模块": "非对称加密",
            "主要功能": "使用公钥加密私钥解密，或私钥签名公钥验证",
            "推荐API": "RSA, padding模块",
            "典型应用": "密钥交换、数字签名、身份认证"
        },
        {
            "模块": "哈希函数",
            "主要功能": "计算数据的固定长度摘要",
            "推荐API": "Hash类，SHA-256算法",
            "典型应用": "数据完整性、密码存储、数字签名"
        },
        {
            "模块": "密钥派生",
            "主要功能": "从密码或其他源派生加密密钥",
            "推荐API": "PBKDF2HMAC, Scrypt",
            "典型应用": "密码存储、密钥生成"
        },
        {
            "模块": "X.509证书",
            "主要功能": "处理数字证书和PKI操作",
            "推荐API": "x509模块",
            "典型应用": "TLS/SSL、身份验证、代码签名"
        }
    ]
    
    print("\ncryptography模块核心功能表:")
    print("模块       | 主要功能                          | 推荐API                               | 典型应用")
    print("-----------|----------------------------------|---------------------------------------|------------------------")
    
    for feature in core_features:
        print(f"{feature['模块']:<11} | {feature['主要功能']:<32} | {feature['推荐API']:<31} | {feature['典型应用']}")
    
    # 8.2 推荐使用场景
    print("\n8.2 推荐使用场景:")
    
    use_cases = [
        {
            "场景": "Web应用安全",
            "组件": [
                "TLS/SSL证书管理",
                "密码存储与验证",
                "敏感数据加密",
                "CSRF令牌生成"
            ]
        },
        {
            "场景": "数据保护",
            "组件": [
                "文件加密与解密",
                "数据库字段加密",
                "备份数据加密",
                "端到端加密"
            ]
        },
        {
            "场景": "身份认证与授权",
            "组件": [
                "密码哈希与验证",
                "JWT令牌生成与验证",
                "API密钥管理",
                "数字签名验证"
            ]
        },
        {
            "场景": "安全通信",
            "组件": [
                "密钥交换",
                "消息加密",
                "消息认证",
                "TLS实现支持"
            ]
        },
        {
            "场景": "系统安全",
            "组件": [
                "文件完整性验证",
                "代码签名",
                "安全配置加密",
                "特权访问管理"
            ]
        }
    ]
    
    for use_case in use_cases:
        print(f"\n{use_case['场景']}:")
        for component in use_case['组件']:
            print(f"  - {component}")
    
    # 8.3 学习资源与进阶建议
    print("\n8.3 学习资源与进阶建议:")
    
    resources = [
        {
            "类型": "官方文档",
            "资源": "cryptography.io 官方文档",
            "链接": "https://cryptography.io/"
        },
        {
            "类型": "安全标准",
            "资源": "NIST密码学标准",
            "链接": "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57Pt1r5.pdf"
        },
        {
            "类型": "密码学教程",
            "资源": "Real World Cryptography（书籍）",
            "链接": "https://www.manning.com/books/real-world-cryptography"
        },
        {
            "类型": "实践指南",
            "资源": "OWASP密码学备忘单",
            "链接": "https://cheatsheetseries.owasp.org/cheatsheets/Cryptography_Cheat_Sheet.html"
        },
        {
            "类型": "在线课程",
            "资源": "Coursera: 密码学I、密码学II",
            "链接": "https://www.coursera.org/learn/crypto"
        }
    ]
    
    print("\n推荐学习资源:")
    for resource in resources:
        print(f"- {resource['类型']}: {resource['资源']} ({resource['链接']})")
    
    print("\n进阶学习建议:")
    print("1. 深入学习密码学理论基础")
    print("2. 了解常见密码学攻击及其防护")
    print("3. 参与安全代码审查和渗透测试")
    print("4. 关注密码学研究最新进展和安全公告")
    print("5. 实践实现和破解密码学算法，加深理解")
    print("6. 学习密码学工程实践和性能优化")
    print("7. 研究和应用后量子密码学技术")
    
    # 8.4 最终建议
    print("\n8.4 最终建议:")
    
    final_recommendations = [
        "始终使用经过验证的密码学库，避免自己实现密码学原语",
        "保持库的更新，及时修复已知安全漏洞",
        "采用最小权限原则，限制加密操作的访问权限",
        "实施全面的密钥管理策略，包括生成、存储、轮换和销毁",
        "进行定期安全审计和渗透测试，确保加密实现的安全性",
        "记录和监控加密操作，及时发现异常行为",
        "制定应急响应计划，应对可能的安全事件",
        "平衡安全性和可用性，不要过度加密影响用户体验",
        "了解业务需求，选择适当级别的安全保护",
        "持续学习和更新密码学知识，适应不断变化的安全威胁"
    ]
    
    print("\n密码学应用最终建议:")
    for i, recommendation in enumerate(final_recommendations, 1):
        print(f"{i}. {recommendation}")
    
    print("\n记住：密码学是安全的基础，但不是全部。建立完整的安全体系，结合其他安全措施，")
    print("才能真正保障应用和数据的安全。")

# 主函数
def main():
    """
    主函数，演示cryptography模块的主要功能
    """
    print("=" * 80)
    print("Python cryptography模块详解与实践")
    print("=" * 80)
    print("本示例展示了cryptography模块的主要功能和使用方法。")
    print("注意：如果cryptography库未安装，部分功能将以模拟方式演示。")
    print("在生产环境中，请确保安装cryptography库以获得完整的安全功能。")
    print("安装命令: pip install cryptography")
    print("=" * 80)
    
    # 演示各个功能模块
    print("\n【1】演示对称加密基础...")
    symmetric_encryption_basics()
    
    print("\n【2】演示非对称加密...")
    asymmetric_encryption()
    
    print("\n【3】演示哈希函数和消息摘要...")
    hash_functions()
    
    print("\n【4】演示密钥派生函数...")
    key_derivation_functions()
    
    print("\n【5】演示数字证书和X.509...")
    digital_certificates()
    
    print("\n【6】演示高级应用示例...")
    advanced_applications()
    
    print("\n【7】演示安全最佳实践...")
    security_best_practices()
    
    print("\n【8】总结与最佳实践...")
    summary_and_best_practices()
    
    print("\n" + "=" * 80)
    print("cryptography模块演示完成！")
    print("在实际应用中，请根据具体需求和安全要求选择合适的加密方案。")
    print("请记住：密码学是一个复杂的领域，不正确的实现可能导致安全漏洞。")
    print("始终遵循安全最佳实践，并在必要时咨询安全专家。")
    print("=" * 80)

# 如果直接运行此脚本
if __name__ == "__main__":
    # 导入hashlib（用于SecureTokenSystem）
    import hashlib
    
    # 运行主函数
    main()
