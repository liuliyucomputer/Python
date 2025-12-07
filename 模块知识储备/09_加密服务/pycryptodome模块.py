#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pycryptodome模块 - 密码学库

PyCryptodome是PyCrypto的替代库，提供了全面的密码学功能，
包括对称加密、非对称加密、哈希函数、数字签名等。

主要功能包括：
- 对称加密 (AES, DES, 3DES, RC4等)
- 非对称加密 (RSA, DSA, ElGamal等)
- 哈希函数和消息摘要 (MD5, SHA-1, SHA-256等)
- 数字签名和验证
- 随机数生成
- 密钥管理

使用场景：
- 数据加密和解密
- 安全通信
- 数字签名和验证
- 密码存储
- 密钥生成和管理

安装方法：
pip install pycryptodome
"""

from Crypto.Cipher import AES, DES, ARC4
from Crypto.PublicKey import RSA, DSA
from Crypto.Hash import MD5, SHA1, SHA256, SHA512, HMAC
from Crypto.Signature import pkcs1_15, DSS
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2, scrypt
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import number
import base64
import os

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. PyCryptodome模块基本介绍")
print("=" * 50)
print("PyCryptodome是PyCrypto的替代库")
print("提供了全面的密码学功能")
print("支持多种加密算法和协议")
print("易于使用，文档完善")

# ===========================
# 2. 哈希函数
# ===========================
print("\n" + "=" * 50)
print("2. 哈希函数")
print("=" * 50)

# 计算字符串的哈希值
def compute_hash(data, algorithm="SHA256"):
    """计算数据的哈希值"""
    if algorithm == "MD5":
        hash_obj = MD5.new()
    elif algorithm == "SHA1":
        hash_obj = SHA1.new()
    elif algorithm == "SHA256":
        hash_obj = SHA256.new()
    elif algorithm == "SHA512":
        hash_obj = SHA512.new()
    else:
        raise ValueError("不支持的哈希算法")
    
    hash_obj.update(data)
    return hash_obj.hexdigest()

# 演示哈希函数
print("演示哈希函数的使用:")

# 哈希字符串
message = b"Hello, PyCryptodome!"
print(f"原始消息: {message.decode()}")

# 使用不同的哈希算法
for alg in ["MD5", "SHA1", "SHA256", "SHA512"]:
    hashed = compute_hash(message, alg)
    print(f"{alg}哈希值: {hashed}")
    print(f"{alg}哈希值长度: {len(hashed)} 字符")

# ===========================
# 3. HMAC消息认证码
# ===========================
print("\n" + "=" * 50)
print("3. HMAC消息认证码")
print("=" * 50)

# 生成HMAC
def generate_hmac(data, key, algorithm=SHA256):
    """生成HMAC消息认证码"""
    hmac_obj = HMAC.new(key, data, algorithm)
    return hmac_obj.hexdigest()

# 验证HMAC
def verify_hmac(data, key, hmac_value, algorithm=SHA256):
    """验证HMAC消息认证码"""
    hmac_obj = HMAC.new(key, data, algorithm)
    try:
        hmac_obj.hexverify(hmac_value)
        return True
    except ValueError:
        return False

# 演示HMAC
print("演示HMAC消息认证码的使用:")

# 生成密钥
key = get_random_bytes(16)
print(f"HMAC密钥: {base64.b64encode(key).decode()}")

# 消息
message = b"需要认证的消息"
print(f"原始消息: {message.decode()}")

# 生成HMAC
hmac_value = generate_hmac(message, key)
print(f"HMAC值: {hmac_value}")

# 验证HMAC
is_valid = verify_hmac(message, key, hmac_value)
print(f"HMAC验证结果: {'有效' if is_valid else '无效'}")

# 验证被篡改的消息
tampered_message = b"被篡改的消息"
is_tampered_valid = verify_hmac(tampered_message, key, hmac_value)
print(f"篡改消息的HMAC验证结果: {'有效' if is_tampered_valid else '无效'}")

# ===========================
# 4. 对称加密
# ===========================
print("\n" + "=" * 50)
print("4. 对称加密")
print("=" * 50)

# AES-256-CBC加密
def aes_encrypt(plaintext, key):
    """使用AES-256-CBC加密数据"""
    # 生成随机IV
    iv = get_random_bytes(16)
    
    # 创建加密器
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # 使用PKCS7填充
    padded_data = pad(plaintext, AES.block_size)
    
    # 加密数据
    ciphertext = cipher.encrypt(padded_data)
    
    # 返回IV和密文
    return iv + ciphertext

# AES-256-CBC解密
def aes_decrypt(ciphertext_with_iv, key):
    """使用AES-256-CBC解密数据"""
    # 分离IV和密文
    iv = ciphertext_with_iv[:16]
    ciphertext = ciphertext_with_iv[16:]
    
    # 创建解密器
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # 解密数据
    padded_plaintext = cipher.decrypt(ciphertext)
    
    # 移除填充
    plaintext = unpad(padded_plaintext, AES.block_size)
    
    return plaintext

# 演示对称加密
print("演示AES对称加密的使用:")

# 生成256位密钥
key = get_random_bytes(32)  # AES-256需要32字节密钥
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
# 5. 非对称加密
# ===========================
print("\n" + "=" * 50)
print("5. 非对称加密")
print("=" * 50)

# 生成RSA密钥对
def generate_rsa_key_pair(bits=2048):
    """生成RSA密钥对"""
    key = RSA.generate(bits)
    return key

# RSA加密
def rsa_encrypt(plaintext, public_key):
    """使用RSA公钥加密数据"""
    ciphertext = public_key.encrypt(
        plaintext,
        None  # 填充方案，None表示使用默认的PKCS#1 v1.5填充
    )[0]  # encrypt()返回一个元组，第一个元素是密文
    return ciphertext

# RSA解密
def rsa_decrypt(ciphertext, private_key):
    """使用RSA私钥解密数据"""
    plaintext = private_key.decrypt(ciphertext)
    return plaintext

# 演示非对称加密
print("演示RSA非对称加密的使用:")

# 生成RSA密钥对
rsa_key = generate_rsa_key_pair()
print(f"RSA密钥对生成成功")

# 获取公钥和私钥
private_key = rsa_key
public_key = rsa_key.publickey()

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
# 6. 数字签名
# ===========================
print("\n" + "=" * 50)
print("6. 数字签名")
print("=" * 50)

# RSA数字签名
def rsa_sign(private_key, data):
    """使用RSA私钥对数据进行签名"""
    # 计算数据的哈希值
    hash_obj = SHA256.new(data)
    
    # 使用私钥签名
    signature = pkcs1_15.new(private_key).sign(hash_obj)
    return signature

# RSA验证签名
def rsa_verify(public_key, data, signature):
    """使用RSA公钥验证数据签名"""
    # 计算数据的哈希值
    hash_obj = SHA256.new(data)
    
    try:
        # 验证签名
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        return True
    except (ValueError, TypeError):
        return False

# DSA数字签名
def dsa_sign(private_key, data):
    """使用DSA私钥对数据进行签名"""
    # 计算数据的哈希值
    hash_obj = SHA256.new(data)
    
    # 使用私钥签名
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature

# DSA验证签名
def dsa_verify(public_key, data, signature):
    """使用DSA公钥验证数据签名"""
    # 计算数据的哈希值
    hash_obj = SHA256.new(data)
    
    try:
        # 验证签名
        verifier = DSS.new(public_key, 'fips-186-3')
        verifier.verify(hash_obj, signature)
        return True
    except (ValueError, TypeError):
        return False

# 演示RSA数字签名
print("演示RSA数字签名的使用:")

# 要签名的数据
document = b"这是一份需要签名的重要文档。"
print(f"原始文档: {document.decode()}")

# 生成签名
signature = rsa_sign(private_key, document)
print(f"RSA数字签名: {base64.b64encode(signature).decode()}")

# 验证签名
is_valid = rsa_verify(public_key, document, signature)
print(f"签名验证结果: {'有效' if is_valid else '无效'}")

# 验证被篡改的文档
tampered_document = b"这是一份被篡改的重要文档。"
is_tampered_valid = rsa_verify(public_key, tampered_document, signature)
print(f"篡改文档的签名验证结果: {'有效' if is_tampered_valid else '无效'}")

# 演示DSA数字签名
print("\n演示DSA数字签名的使用:")

# 生成DSA密钥对
dsa_key = DSA.generate(2048)
print(f"DSA密钥对生成成功")

dsa_private_key = dsa_key
dsa_public_key = dsa_key.publickey()

# 生成DSA签名
dsa_sig = dsa_sign(dsa_private_key, document)
print(f"DSA数字签名: {base64.b64encode(dsa_sig).decode()}")

# 验证DSA签名
dsa_is_valid = dsa_verify(dsa_public_key, document, dsa_sig)
print(f"DSA签名验证结果: {'有效' if dsa_is_valid else '无效'}")

# ===========================
# 7. 密钥派生函数
# ===========================
print("\n" + "=" * 50)
print("7. 密钥派生函数")
print("=" * 50)

# 使用PBKDF2从密码派生密钥
def derive_key_pbkdf2(password, salt=None, iterations=100000, key_len=32):
    """使用PBKDF2从密码派生密钥"""
    if salt is None:
        salt = get_random_bytes(16)
    
    # 使用PBKDF2派生密钥
    key = PBKDF2(password, salt, dkLen=key_len, count=iterations, hmac_hash_module=SHA256)
    return key, salt

# 使用scrypt从密码派生密钥
def derive_key_scrypt(password, salt=None, key_len=32):
    """使用scrypt从密码派生密钥"""
    if salt is None:
        salt = get_random_bytes(16)
    
    # 使用scrypt派生密钥
    key = scrypt(password, salt, key_len, N=2**14, r=8, p=1)
    return key, salt

# 演示密钥派生函数
print("演示密钥派生函数的使用:")

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
# 8. 其他对称加密算法
# ===========================
print("\n" + "=" * 50)
print("8. 其他对称加密算法")
print("=" * 50)

# DES加密
def des_encrypt(plaintext, key):
    """使用DES-CBC加密数据"""
    # 生成随机IV
    iv = get_random_bytes(8)  # DES使用8字节IV
    
    # 创建加密器
    cipher = DES.new(key, DES.MODE_CBC, iv)
    
    # 使用PKCS7填充
    padded_data = pad(plaintext, DES.block_size)
    
    # 加密数据
    ciphertext = cipher.encrypt(padded_data)
    
    # 返回IV和密文
    return iv + ciphertext

# RC4加密
def rc4_encrypt(plaintext, key):
    """使用RC4加密数据"""
    # 创建RC4加密器
    cipher = ARC4.new(key)
    
    # RC4不需要填充
    ciphertext = cipher.encrypt(plaintext)
    
    return ciphertext

# 演示DES加密
print("演示DES加密的使用:")

# DES需要8字节密钥
des_key = get_random_bytes(8)
print(f"DES密钥: {base64.b64encode(des_key).decode()}")

# 加密数据
des_ciphertext = des_encrypt(plaintext, des_key)
print(f"DES加密后的数据: {base64.b64encode(des_ciphertext).decode()}")

# 演示RC4加密
print("\n演示RC4加密的使用:")

# RC4密钥可以是任意长度（建议至少16字节）
rc4_key = get_random_bytes(16)
print(f"RC4密钥: {base64.b64encode(rc4_key).decode()}")

# RC4加密数据
rc4_ciphertext = rc4_encrypt(plaintext, rc4_key)
print(f"RC4加密后的数据: {base64.b64encode(rc4_ciphertext).decode()}")

# ===========================
# 9. 密钥序列化和反序列化
# ===========================
print("\n" + "=" * 50)
print("9. 密钥序列化和反序列化")
print("=" * 50)

# 序列化RSA密钥
def serialize_rsa_key(key, password=None):
    """序列化RSA密钥"""
    if password:
        # 使用密码保护私钥
        return key.export_key(passphrase=password, pkcs=8, protection="scryptAndAES128-CBC")
    else:
        # 导出未加密的密钥
        return key.export_key()

# 反序列化RSA密钥
def deserialize_rsa_key(key_data, password=None):
    """反序列化RSA密钥"""
    return RSA.import_key(key_data, passphrase=password)

# 演示密钥序列化
print("演示RSA密钥序列化和反序列化:")

# 序列化RSA私钥（无密码保护）
private_pem = serialize_rsa_key(private_key)
print(f"\nRSA私钥PEM格式:")
print(private_pem.decode())

# 序列化RSA公钥
public_pem = serialize_rsa_key(public_key)
print(f"\nRSA公钥PEM格式:")
print(public_pem.decode())

# 使用密码保护私钥
password = b"my_key_password"
encrypted_private_pem = serialize_rsa_key(private_key, password)
print(f"\n使用密码保护的RSA私钥:")
print(encrypted_private_pem.decode())

# 反序列化密钥
deserialized_key = deserialize_rsa_key(encrypted_private_pem, password)
print(f"\n密钥反序列化成功")

# ===========================
# 10. 实际应用示例
# ===========================
print("\n" + "=" * 50)
print("10. 实际应用示例")
print("=" * 50)

# 示例1: 安全存储密码
def secure_password_storage(password):
    """安全存储密码"""
    # 生成随机盐
    salt = get_random_bytes(16)
    
    # 使用PBKDF2派生密钥
    key, _ = derive_key_pbkdf2(password, salt, iterations=100000, key_len=32)
    
    # 计算密钥的哈希值作为存储值
    stored_value = SHA256.new(key).hexdigest()
    
    # 返回盐和存储值
    return salt, stored_value

# 示例2: 混合加密（对称加密+非对称加密）
def hybrid_encrypt(data, recipient_public_key):
    """混合加密：使用非对称加密保护对称密钥"""
    # 生成随机对称密钥
    symmetric_key = get_random_bytes(32)
    
    # 使用对称密钥加密数据
    encrypted_data = aes_encrypt(data, symmetric_key)
    
    # 使用接收方公钥加密对称密钥
    encrypted_key = rsa_encrypt(symmetric_key, recipient_public_key)
    
    # 返回加密的对称密钥和加密的数据
    return encrypted_key, encrypted_data

# 示例3: 随机数生成
def generate_secure_random(length=32):
    """生成安全的随机数"""
    return get_random_bytes(length)

# 演示实际应用示例
print("示例1: 安全存储密码")
password = b"user_password123"
salt, stored_value = secure_password_storage(password)
print(f"密码已安全存储，盐值: {base64.b64encode(salt).decode()}")
print(f"存储的哈希值: {stored_value}")

print("\n示例2: 混合加密")
# 要加密的数据
secret_data = b"这是需要安全传输的机密数据。这是一个较长的数据，可以使用混合加密方式传输。"
print(f"原始数据: {secret_data.decode()}")

# 使用混合加密
encrypted_key, encrypted_data = hybrid_encrypt(secret_data, public_key)
print(f"加密后的对称密钥: {base64.b64encode(encrypted_key).decode()}")
print(f"加密后的数据: {base64.b64encode(encrypted_data).decode()}")

# 解密混合加密数据
# 1. 使用私钥解密对称密钥
decrypted_symmetric_key = rsa_decrypt(encrypted_key, private_key)
# 2. 使用对称密钥解密数据
decrypted_data = aes_decrypt(encrypted_data, decrypted_symmetric_key)
print(f"解密后的数据: {decrypted_data.decode()}")
print(f"数据传输安全吗? {decrypted_data == secret_data}")

print("\n示例3: 随机数生成")
random_data = generate_secure_random(16)
print(f"16字节安全随机数: {base64.b64encode(random_data).decode()}")

# ===========================
# 11. 最佳实践
# ===========================
print("\n" + "=" * 50)
print("11. 最佳实践")
print("=" * 50)

print("1. 密钥管理")
print("   - 使用安全的随机数生成密钥")
print("   - 定期轮换密钥")
print("   - 安全存储私钥")
print("   - 使用密码保护私钥")

print("\n2. 加密算法选择")
print("   - 对称加密: 优先使用AES-256")
print("   - 非对称加密: 优先使用RSA-2048+或DSA-2048+")
print("   - 哈希函数: 避免使用MD5和SHA-1，优先使用SHA-256+")
print("   - 密钥派生: 优先使用PBKDF2(高迭代次数)或scrypt")

print("\n3. 安全通信")
print("   - 使用TLS/SSL保护网络通信")
print("   - 验证证书的有效性")
print("   - 避免使用不安全的协议和算法")

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
# 12. 总结
# ===========================
print("\n" + "=" * 50)
print("12. 总结")
print("=" * 50)
print("PyCryptodome是一个功能全面的密码学库")
print("提供了对称加密、非对称加密、哈希函数等功能")
print("\n主要功能:")
print("- 对称加密: AES, DES, 3DES, RC4等")
print("- 非对称加密: RSA, DSA, ElGamal等")
print("- 哈希函数: MD5, SHA-1, SHA-256, SHA-512等")
print("- 数字签名和验证")
print("- 密钥派生函数")
print("- 随机数生成")
print("\nPyCryptodome易于使用，文档完善")
print("适合各种安全应用场景")
print("在实际应用中，应遵循安全最佳实践")
print("确保数据和通信的安全性")
