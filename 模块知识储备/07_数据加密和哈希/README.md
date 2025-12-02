# Python 数据加密和哈希模块

本目录包含了Python中用于数据加密、解密和哈希操作的核心模块详解与实践示例。加密和哈希技术在保障数据安全、身份验证和数据完整性方面起着至关重要的作用。

## 目录内容

- [hashlib模块.py](hashlib模块.py) - 提供各种哈希算法实现
- [hmac模块.py](hmac模块.py) - 基于哈希的消息认证码实现
- [cryptography模块.py](cryptography模块.py) - 功能全面的加密库，支持对称加密、非对称加密和X.509证书等

## 模块简介

### hashlib模块
**hashlib** 模块提供了多种安全哈希和消息摘要算法的实现，用于生成固定长度的数据指纹。

- **主要功能**：MD5、SHA1、SHA256、SHA512等哈希算法
- **应用场景**：文件完整性校验、密码存储（需配合盐值和迭代）、数据去重
- **特点**：计算速度快，单向不可逆，相同输入始终产生相同输出

### hmac模块
**hmac** 模块实现了基于哈希的消息认证码（HMAC）算法，结合密钥和哈希函数提供消息认证功能。

- **主要功能**：HMAC-SHA256等算法实现
- **应用场景**：API认证、消息完整性验证、密钥派生
- **特点**：结合密钥和哈希，提供更高的安全性，可防止消息篡改

### cryptography模块
**cryptography** 是一个功能全面的第三方加密库，提供高级和低级加密原语的实现。

- **主要功能**：
  - 对称加密（AES、ChaCha20等）
  - 非对称加密（RSA、ECC等）
  - 数字签名
  - X.509证书操作
  - 密钥派生函数
- **应用场景**：安全通信、数据加密、身份验证、数字签名
- **特点**：安全、现代、高性能，遵循最佳实践设计

## 功能比较

| 功能 | hashlib | hmac | cryptography |
|------|---------|------|--------------|
| 哈希算法 | 丰富 | 依赖外部哈希算法 | 丰富 |
| 对称加密 | 不支持 | 不支持 | 全面支持 |
| 非对称加密 | 不支持 | 不支持 | 全面支持 |
| 密钥派生 | 有限（PBKDF2） | 不支持 | 全面支持 |
| 数字签名 | 不直接支持 | 不支持 | 全面支持 |
| X.509证书 | 不支持 | 不支持 | 全面支持 |
| 易用性 | 简单 | 简单 | 适中（高级API简单，低级API灵活） |
| 安全级别 | 基础 | 中高级 | 高 |
| 性能 | 快 | 快 | 根据算法不同而变化 |

## 模块选择指南

1. **简单哈希操作**（文件校验、数据指纹）：
   - 使用 `hashlib` 模块
   - 推荐算法：SHA-256 或 SHA-512

2. **需要密钥的消息认证**（API认证、安全通信）：
   - 使用 `hmac` 模块
   - 推荐算法：HMAC-SHA256

3. **复杂加密需求**（数据加密、密钥管理、数字证书）：
   - 使用 `cryptography` 模块
   - 根据具体需求选择适当的算法和API

4. **密码存储**：
   - 简单场景：`hashlib` 的 `pbkdf2_hmac`
   - 高安全需求：`cryptography` 的 `pbkdf2_hmac` 或 `scrypt`

## 基本使用示例

### 1. hashlib 示例（计算文件哈希值）

```python
import hashlib

def calculate_file_hash(file_path, algorithm='sha256', chunk_size=8192):
    """计算文件的哈希值"""
    hasher = hashlib.new(algorithm)
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)
    return hasher.hexdigest()

# 使用示例
file_hash = calculate_file_hash('example.txt')
print(f"文件哈希值: {file_hash}")
```

### 2. hmac 示例（API签名）

```python
import hmac
import hashlib
import time
import base64

def generate_api_signature(api_key, secret_key, data):
    """生成API请求签名"""
    timestamp = str(int(time.time()))
    message = f"{api_key}{timestamp}{data}"
    
    # 创建HMAC对象
    h = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256)
    signature = base64.b64encode(h.digest()).decode()
    
    return signature, timestamp

# 使用示例
api_key = "my_api_key"
secret_key = "my_secret_key"
data = "API请求数据"

signature, timestamp = generate_api_signature(api_key, secret_key, data)
print(f"签名: {signature}")
print(f"时间戳: {timestamp}")
```

### 3. cryptography 示例（文件加密）

```python
from cryptography.fernet import Fernet

def encrypt_file(file_path, output_path):
    """使用Fernet对称加密算法加密文件"""
    # 生成密钥
    key = Fernet.generate_key()
    fernet = Fernet(key)
    
    # 读取文件并加密
    with open(file_path, 'rb') as f:
        data = f.read()
    
    encrypted_data = fernet.encrypt(data)
    
    # 保存加密后的数据
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    
    # 返回密钥（实际应用中需要安全存储）
    return key

def decrypt_file(encrypted_file_path, output_path, key):
    """解密文件"""
    fernet = Fernet(key)
    
    with open(encrypted_file_path, 'rb') as f:
        encrypted_data = f.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)

# 使用示例
key = encrypt_file('sensitive_data.txt', 'encrypted_data.bin')
print(f"加密密钥: {key.decode()}")

# 解密文件
# 注意：在实际应用中，密钥需要通过安全渠道获取
# decrypt_file('encrypted_data.bin', 'decrypted_data.txt', key)
```

## 高级功能示例

### 1. 密码存储最佳实践

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

def hash_password(password):
    """安全地哈希密码"""
    # 生成随机盐值
    salt = os.urandom(16)
    
    # 创建密钥派生函数
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    
    # 派生密钥（哈希密码）
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    # 返回盐值和哈希后的密码
    return salt, key

def verify_password(stored_salt, stored_key, password):
    """验证密码"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=stored_salt,
        iterations=100000,
    )
    
    # 尝试使用相同的盐值派生密钥
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    
    # 时间安全的比较
    return stored_key == key

# 使用示例
password = "MySecurePassword123!"
salt, hashed_password = hash_password(password)
print(f"盐值: {base64.urlsafe_b64encode(salt).decode()}")
print(f"哈希密码: {hashed_password.decode()}")

# 验证密码
is_valid = verify_password(salt, hashed_password, "MySecurePassword123!")
print(f"密码验证: {'成功' if is_valid else '失败'}")

# 错误密码验证
is_valid = verify_password(salt, hashed_password, "WrongPassword")
print(f"错误密码验证: {'成功' if is_valid else '失败'}")
```

### 2. RSA非对称加密

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

def generate_rsa_keys():
    """生成RSA密钥对"""
    # 生成私钥
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
    )
    
    # 从私钥获取公钥
    public_key = private_key.public_key()
    
    return private_key, public_key

def encrypt_data(public_key, data):
    """使用RSA公钥加密数据"""
    ciphertext = public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt_data(private_key, ciphertext):
    """使用RSA私钥解密数据"""
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext

def save_keys(private_key, public_key, private_key_path, public_key_path, password=None):
    """保存密钥到文件"""
    # 保存私钥
    encryption_algorithm = serialization.NoEncryption()
    if password:
        encryption_algorithm = serialization.BestAvailableEncryption(password.encode())
    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=encryption_algorithm
    )
    
    with open(private_key_path, 'wb') as f:
        f.write(private_pem)
    
    # 保存公钥
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    with open(public_key_path, 'wb') as f:
        f.write(public_pem)

# 使用示例
private_key, public_key = generate_rsa_keys()

# 加密数据（注意：RSA有数据大小限制，实际应用中应使用混合加密）
data = b"This is a secret message"
ciphertext = encrypt_data(public_key, data)
print(f"加密数据: {base64.b64encode(ciphertext).decode()}")

# 解密数据
plaintext = decrypt_data(private_key, ciphertext)
print(f"解密数据: {plaintext.decode()}")

# 保存密钥
# save_keys(private_key, public_key, 'private_key.pem', 'public_key.pem', '密钥密码')
```

## 安全注意事项

1. **密钥管理**：
   - 永远不要硬编码密钥或存储在版本控制系统中
   - 使用环境变量或专用密钥管理服务
   - 定期轮换密钥

2. **算法选择**：
   - 避免使用已弃用的算法（如MD5、SHA-1、DES）
   - 对称加密推荐使用AES-256-GCM
   - 哈希函数推荐使用SHA-256或SHA-512
   - 非对称加密推荐使用RSA-4096或ECC P-256

3. **密码存储**：
   - 永远不要明文存储密码
   - 使用专门的密钥派生函数（如PBKDF2、Argon2、scrypt）
   - 为每个密码使用独立的盐值
   - 使用足够的迭代次数

4. **随机数生成**：
   - 使用密码学安全的随机数生成器（如`os.urandom()`）
   - 避免使用普通的`random`模块生成密钥材料

5. **常见安全陷阱**：
   - 忽略初始化向量(IV)的重要性
   - 不验证加密数据的完整性
   - 直接使用密码作为加密密钥
   - 不保护私钥
   - 忽视侧信道攻击

## 性能考量

1. **算法性能**：
   - 哈希算法：MD5 > SHA-1 > SHA-256 > SHA-512
   - 对称加密：AES-CTR > AES-GCM > AES-CBC
   - 非对称加密：ECC > RSA（相同安全级别下）

2. **数据大小考虑**：
   - 哈希和HMAC：适合小数据，大文件使用分块处理
   - 对称加密：适合各种大小的数据，大文件使用流式处理
   - 非对称加密：不适合加密大文件，应与对称加密结合使用

3. **优化建议**：
   - 使用适当的缓冲区大小处理大文件
   - 利用硬件加速（如AES-NI指令集）
   - 对于大量小操作，考虑批量处理和并行计算
   - 密钥派生函数的工作因子应根据系统性能调整

## 进一步学习资源

1. **官方文档**：
   - [Python hashlib 文档](https://docs.python.org/3/library/hashlib.html)
   - [Python hmac 文档](https://docs.python.org/3/library/hmac.html)
   - [cryptography 官方文档](https://cryptography.io/)

2. **安全标准**：
   - [NIST密码学标准](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57Pt1r5.pdf)
   - [OWASP密码学备忘单](https://cheatsheetseries.owasp.org/cheatsheets/Cryptography_Cheat_Sheet.html)

3. **推荐书籍**：
   - 《实用密码学》(Practical Cryptography)
   - 《Real World Cryptography》
   - 《密码工程》(Cryptography Engineering)

4. **在线课程**：
   - Coursera: 密码学I、密码学II
   - edX: 现代密码学

通过学习和实践这些模块，您将能够在Python应用中实现安全的数据处理、通信和存储。请记住，密码学是一个复杂的领域，不正确的实现可能导致安全漏洞，始终遵循最佳实践并在必要时咨询安全专家。