#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cryptography模块 - 高级加密库

cryptography是Python中一个强大的加密库，
提供了对称加密、非对称加密、哈希函数、数字签名等功能。

主要功能包括：
- 对称加密 (AES, ChaCha20等)
- 非对称加密 (RSA, ECDSA, Ed25519等)
- 哈希函数和消息摘要
- 数字签名和验证
- 密钥派生函数 (PBKDF2, scrypt, argon2等)
- X.509证书操作

使用场景：
- 数据加密和解密
- 安全通信
- 数字签名和验证
- 密码存储
- 证书管理

安装方法：
pip install cryptography
"""

from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat
from cryptography.hazmat.primitives.serialization import BestAvailableEncryption, NoEncryption
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
import os
import base64

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. cryptography模块基本介绍")
print("=" * 50)
print("cryptography是Python中一个强大的加密库")
print("提供了对称加密、非对称加密、哈希函数等功能")
print("设计遵循安全优先原则，易于使用")

# ===========================
# 2. 哈希函数
# ===========================
print("\n" + "=" * 50)
print("2. 哈希函数")
print("=" * 50)

# 计算字符串的SHA-256哈希值
def compute_hash(data):
    """计算数据的SHA-256哈希值"""
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(data)
    return digest.finalize()

# 演示哈希函数
print("演示哈希函数的使用:")

# 哈希字符串
message = b"Hello, cryptography!"
hashed_message = compute_hash(message)
print(f"原始消息: {message.decode()}")
print(f"SHA-256哈希值: {base64.b64encode(hashed_message).decode()}")
print(f"哈希值长度: {len(hashed_message)} 字节")

# 哈希不同的消息
message2 = b"Hello, cryptography! "  # 注意末尾有空格
hashed_message2 = compute_hash(message2)
print(f"\n不同消息: {message2.decode()}")
print(f"SHA-256哈希值: {base64.b64encode(hashed_message2).decode()}")
print(f"哈希值相同吗? {hashed_message == hashed_message2}")

# ===========================
# 3. 对称加密
# ===========================
print("\n" + "=" * 50)
print("3. 对称加密")
print("=" * 50)

# AES-256-CBC加密
def aes_encrypt(plaintext, key):
    """使用AES-256-CBC加密数据"""
    # 生成随机IV
    iv = os.urandom(16)
    
    # 创建加密器
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # 使用PKCS7填充
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    
    # 加密数据
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # 返回IV和密文
    return iv + ciphertext

# AES-256-CBC解密
def aes_decrypt(ciphertext_with_iv, key):
    """使用AES-256-CBC解密数据"""
    # 分离IV和密文
    iv = ciphertext_with_iv[:16]
    ciphertext = ciphertext_with_iv[16:]
    
    # 创建解密器
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # 解密数据
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # 移除PKCS7填充
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    
    return plaintext

# 演示对称加密
print("演示AES-256-CBC对称加密:")

# 生成256位密钥
key = os.urandom(32)  # AES-256需要32字节密钥
print(f"AES密钥: {base64.b64encode(key).decode()}")

# 要加密的数据
plaintext = b"这是一个需要加密的敏感数据。"
print(f"原始数据: {plaintext.decode()}")

# 加密数据
ciphertext = aes_encrypt(plaintext, key)
print(f"加密后的数据: {base64.b64encode(ciphertext).decode()}")

# 解密数据
decrypted_plaintext = aes_decrypt(ciphertext, key)
print(f"解密后的数据: {decrypted_plaintext.decode()}")

# 验证解密结果
print(f"解密结果正确吗? {decrypted_plaintext == plaintext}")

# ===========================
# 4. 非对称加密
# ===========================
print("\n" + "=" * 50)
print("4. 非对称加密")
print("=" * 50)

# 生成RSA密钥对
def generate_rsa_key_pair():
    """生成RSA密钥对"""
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# RSA加密
def rsa_encrypt(plaintext, public_key):
    """使用RSA公钥加密数据"""
    ciphertext = public_key.encrypt(
        plaintext,
        asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

# RSA解密
def rsa_decrypt(ciphertext, private_key):
    """使用RSA私钥解密数据"""
    plaintext = private_key.decrypt(
        ciphertext,
        asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

# 演示非对称加密
print("演示RSA非对称加密:")

# 生成RSA密钥对
private_key, public_key = generate_rsa_key_pair()
print(f"RSA密钥对生成成功")

# 要加密的数据（注意RSA加密的数据大小有限制）
small_plaintext = b"这是一个小数据，适合RSA加密。"
print(f"原始数据: {small_plaintext.decode()}")

# 加密数据
rsa_ciphertext = rsa_encrypt(small_plaintext, public_key)
print(f"加密后的数据: {base64.b64encode(rsa_ciphertext).decode()}")

# 解密数据
rsa_decrypted = rsa_decrypt(rsa_ciphertext, private_key)
print(f"解密后的数据: {rsa_decrypted.decode()}")

# 验证解密结果
print(f"解密结果正确吗? {rsa_decrypted == small_plaintext}")

# ===========================
# 5. 数字签名
# ===========================
print("\n" + "=" * 50)
print("5. 数字签名")
print("=" * 50)

# 生成数字签名
def sign_data(private_key, data):
    """使用RSA私钥对数据进行签名"""
    signature = private_key.sign(
        data,
        asymmetric_padding.PSS(
            mgf=asymmetric_padding.MGF1(hashes.SHA256()),
            salt_length=asymmetric_padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# 验证数字签名
def verify_signature(public_key, data, signature):
    """使用RSA公钥验证数据签名"""
    try:
        public_key.verify(
            signature,
            data,
            asymmetric_padding.PSS(
                mgf=asymmetric_padding.MGF1(hashes.SHA256()),
                salt_length=asymmetric_padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

# 演示数字签名
print("演示RSA数字签名:")

# 要签名的数据
document = b"这是一份需要签名的重要文档。"
print(f"原始文档: {document.decode()}")

# 生成签名
signature = sign_data(private_key, document)
print(f"数字签名: {base64.b64encode(signature).decode()}")

# 验证签名
is_valid = verify_signature(public_key, document, signature)
print(f"签名验证结果: {'有效' if is_valid else '无效'}")

# 验证被篡改的文档
tampered_document = b"这是一份被篡改的重要文档。"
is_tampered_valid = verify_signature(public_key, tampered_document, signature)
print(f"篡改文档的签名验证结果: {'有效' if is_tampered_valid else '无效'}")

# ===========================
# 6. 密钥派生函数
# ===========================
print("\n" + "=" * 50)
print("6. 密钥派生函数")
print("=" * 50)

# 使用PBKDF2从密码派生密钥
def derive_key_pbkdf2(password, salt=None):
    """使用PBKDF2从密码派生密钥"""
    if salt is None:
        salt = os.urandom(16)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32字节 = 256位
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    key = kdf.derive(password)
    return key, salt

# 使用scrypt从密码派生密钥
def derive_key_scrypt(password, salt=None):
    """使用scrypt从密码派生密钥"""
    if salt is None:
        salt = os.urandom(16)
    
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,  # CPU/Memory cost factor
        r=8,      # Block size
        p=1,      # Parallelization factor
        backend=default_backend()
    )
    
    key = kdf.derive(password)
    return key, salt

# 演示密钥派生函数
print("演示密钥派生函数:")

# 用户密码
password = b"my_strong_password123"
print(f"用户密码: {password.decode()}")

# 使用PBKDF2派生密钥
pbkdf2_key, pbkdf2_salt = derive_key_pbkdf2(password)
print(f"\nPBKDF2派生密钥: {base64.b64encode(pbkdf2_key).decode()}")
print(f"使用的盐值: {base64.b64encode(pbkdf2_salt).decode()}")

# 使用scrypt派生密钥
scrypt_key, scrypt_salt = derive_key_scrypt(password)
print(f"\nscrypt派生密钥: {base64.b64encode(scrypt_key).decode()}")
print(f"使用的盐值: {base64.b64encode(scrypt_salt).decode()}")

# ===========================
# 7. ECC椭圆曲线加密
# ===========================
print("\n" + "=" * 50)
print("7. ECC椭圆曲线加密")
print("=" * 50)

# 生成ECC密钥对
def generate_ecc_key_pair():
    """生成ECC密钥对"""
    private_key = ec.generate_private_key(
        ec.SECP384R1(),  # 使用P-384曲线
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

# ECC数字签名
def ecc_sign(private_key, data):
    """使用ECC私钥对数据进行签名"""
    signature = private_key.sign(
        data,
        ec.ECDSA(hashes.SHA256())
    )
    return signature

# ECC验证签名
def ecc_verify(public_key, data, signature):
    """使用ECC公钥验证数据签名"""
    try:
        public_key.verify(
            signature,
            data,
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception:
        return False

# 演示ECC椭圆曲线加密
print("演示ECC椭圆曲线加密和签名:")

# 生成ECC密钥对
ecc_private_key, ecc_public_key = generate_ecc_key_pair()
print(f"ECC密钥对生成成功")

# 要签名的数据
document = b"这是一份需要使用ECC签名的文档。"
print(f"原始文档: {document.decode()}")

# 生成签名
ecc_signature = ecc_sign(ecc_private_key, document)
print(f"ECC数字签名: {base64.b64encode(ecc_signature).decode()}")

# 验证签名
ecc_is_valid = ecc_verify(ecc_public_key, document, ecc_signature)
print(f"签名验证结果: {'有效' if ecc_is_valid else '无效'}")

# ===========================
# 8. 密钥序列化和反序列化
# ===========================
print("\n" + "=" * 50)
print("8. 密钥序列化和反序列化")
print("=" * 50)

# 序列化RSA密钥
def serialize_rsa_keys(private_key, public_key, password=None):
    """序列化RSA密钥对"""
    # 序列化私钥
    if password:
        encryption_algorithm = BestAvailableEncryption(password)
    else:
        encryption_algorithm = NoEncryption()
    
    private_pem = private_key.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.PKCS8,
        encryption_algorithm=encryption_algorithm
    )
    
    # 序列化公钥
    public_pem = public_key.public_bytes(
        encoding=Encoding.PEM,
        format=PublicFormat.SubjectPublicKeyInfo
    )
    
    return private_pem, public_pem

# 演示密钥序列化
print("演示密钥序列化和反序列化:")

# 序列化RSA密钥对
private_pem, public_pem = serialize_rsa_keys(private_key, public_key)
print(f"\nRSA私钥PEM格式:")
print(private_pem.decode())

print(f"\nRSA公钥PEM格式:")
print(public_pem.decode())

# ===========================
# 9. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("9. 实际应用示例")
print("=" * 50)

# 示例1: 安全存储密码
def secure_password_storage(password):
    """安全存储密码"""
    # 生成随机盐
    salt = os.urandom(16)
    
    # 使用scrypt派生密钥
    key, _ = derive_key_scrypt(password, salt)
    
    # 存储盐和密钥哈希
    # 实际应用中，应该将salt和key存储在数据库中
    return salt, key

# 示例2: 安全传输数据（混合加密）
def secure_data_transfer(data, recipient_public_key):
    """安全传输数据（混合加密）"""
    # 生成随机对称密钥
    symmetric_key = os.urandom(32)
    
    # 使用对称密钥加密数据
    encrypted_data = aes_encrypt(data, symmetric_key)
    
    # 使用接收方公钥加密对称密钥
    encrypted_key = rsa_encrypt(symmetric_key, recipient_public_key)
    
    # 返回加密的对称密钥和加密的数据
    return encrypted_key, encrypted_data

# 示例3: 文件加密
def encrypt_file(file_path, key):
    """加密文件"""
    # 读取文件内容
    with open(file_path, 'rb') as f:
        content = f.read()
    
    # 加密内容
    encrypted_content = aes_encrypt(content, key)
    
    # 写入加密后的内容
    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, 'wb') as f:
        f.write(encrypted_content)
    
    return encrypted_file_path

# 示例4: 文件解密
def decrypt_file(encrypted_file_path, key):
    """解密文件"""
    # 读取加密内容
    with open(encrypted_file_path, 'rb') as f:
        encrypted_content = f.read()
    
    # 解密内容
    content = aes_decrypt(encrypted_content, key)
    
    # 写入解密后的内容
    decrypted_file_path = encrypted_file_path.replace(".encrypted", ".decrypted")
    with open(decrypted_file_path, 'wb') as f:
        f.write(content)
    
    return decrypted_file_path

# 演示实际应用示例
print("示例1: 安全存储密码")
password = b"user_password123"
salt, stored_key = secure_password_storage(password)
print(f"密码已安全存储，盐值: {base64.b64encode(salt).decode()}")

print("\n示例2: 安全传输数据")
# 模拟数据传输
secret_data = b"这是需要安全传输的机密数据。"
print(f"原始数据: {secret_data.decode()}")

# 模拟生成接收方密钥对
recipient_private, recipient_public = generate_rsa_key_pair()

# 安全传输数据
encrypted_key, encrypted_data = secure_data_transfer(secret_data, recipient_public)
print(f"加密后的对称密钥: {base64.b64encode(encrypted_key).decode()}")
print(f"加密后的数据: {base64.b64encode(encrypted_data).decode()}")

# 接收方解密数据
# 1. 使用私钥解密对称密钥
decrypted_symmetric_key = rsa_decrypt(encrypted_key, recipient_private)
# 2. 使用对称密钥解密数据
decrypted_data = aes_decrypt(encrypted_data, decrypted_symmetric_key)
print(f"解密后的数据: {decrypted_data.decode()}")
print(f"数据传输安全吗? {decrypted_data == secret_data}")

# ===========================
# 10. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("10. 最佳实践")
print("=" * 50)

print("1. 密钥管理")
print("   - 使用安全的密钥生成方法")
print("   - 定期轮换密钥")
print("   - 安全存储私钥和敏感密钥")
print("   - 使用密钥管理系统(KMS)")

print("\n2. 加密算法选择")
print("   - 对称加密: 使用AES-256")
print("   - 非对称加密: 使用RSA-2048+或ECC P-384")
print("   - 哈希函数: 使用SHA-256+或SHA-3")
print("   - 密钥派生: 使用PBKDF2(高迭代次数)或scrypt")

print("\n3. 安全通信")
print("   - 使用TLS/SSL保护网络通信")
print("   - 验证证书的有效性")
print("   - 避免使用不安全的协议")

print("\n4. 数据加密")
print("   - 加密敏感数据")
print("   - 使用适当的填充方案")
print("   - 生成安全的随机IV")
print("   - 不要重复使用IV")

print("\n5. 密码存储")
print("   - 不要明文存储密码")
print("   - 使用密钥派生函数")
print("   - 为每个密码使用唯一的盐值")
print("   - 使用高强度的哈希函数")

# ===========================
# 11. 总结
# ===========================
print("\n" + "=" * 50)
print("11. 总结")
print("=" * 50)
print("cryptography是Python中一个强大的加密库，")
print("提供了对称加密、非对称加密、哈希函数等功能。")
print("\n主要功能:")
print("- 哈希函数: SHA-256, SHA-512等")
print("- 对称加密: AES, ChaCha20等")
print("- 非对称加密: RSA, ECC等")
print("- 数字签名和验证")
print("- 密钥派生函数")
print("- X.509证书操作")
print("\ncryptography库设计遵循安全优先原则，")
print("易于使用，适合各种安全应用场景。")
print("在实际应用中，应遵循安全最佳实践，")
print("确保数据和通信的安全性。")
