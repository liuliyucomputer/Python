# cryptography模块

## 模块概述

cryptography是一个功能强大的第三方加密库，提供了广泛的加密功能，包括对称加密、非对称加密、哈希函数、数字签名等。与Python标准库中的加密模块相比，cryptography提供了更全面、更现代化的加密功能。

**注意**：cryptography是第三方库，需要先安装：
```bash
pip install cryptography
```

cryptography模块提供了以下主要功能：
- 对称加密（如AES、ChaCha20）
- 非对称加密（如RSA、ECC）
- 哈希函数和消息认证码
- 数字签名
- 密钥派生函数
- X.509证书管理

## 核心组件

cryptography库包含两个主要部分：

1. **hazmat层**：低级密码学原语，提供更灵活但需要更多专业知识的API
2. **高级层**：更易于使用的高级API，封装了hazmat层的复杂性

## 基本用法

### 1. 对称加密（AES）

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# 生成随机密钥和IV
key = os.urandom(32)  # AES-256需要32字节密钥
iv = os.urandom(16)  # AES块大小为16字节

# 创建AES加密器
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()

# 加密数据
plaintext = b"Hello, World!" * 10
# 填充数据以适应块大小
pad_length = 16 - (len(plaintext) % 16)
plaintext += bytes([pad_length]) * pad_length

ciphertext = encryptor.update(plaintext) + encryptor.finalize()
print(f"加密后的数据: {ciphertext}")

# 创建AES解密器
decryptor = cipher.decryptor()

# 解密数据
decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
# 移除填充
decrypted_data = decrypted_data[:-decrypted_data[-1]]
print(f"解密后的数据: {decrypted_data.decode()}")
```

### 2. 非对称加密（RSA）

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# 生成RSA密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# 要加密的数据
plaintext = b"This is a secret message"

# 使用公钥加密数据
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"加密后的数据: {ciphertext}")

# 使用私钥解密数据
decrypted_data = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(f"解密后的数据: {decrypted_data.decode()}")
```

### 3. 数字签名

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# 生成RSA密钥对
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# 要签名的数据
data = b"This is a message to be signed"

# 使用私钥签名数据
signature = private_key.sign(
    data,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)
print(f"签名: {signature}")

# 使用公钥验证签名
try:
    public_key.verify(
        signature,
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("签名验证通过")
except Exception as e:
    print(f"签名验证失败: {e}")
```

### 4. 哈希函数

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# 创建哈希对象
hash_obj = hashes.Hash(hashes.SHA256(), backend=default_backend())

# 更新哈希对象
hash_obj.update(b"Hello, ")
hash_obj.update(b"World!")

# 获取哈希值
hash_value = hash_obj.finalize()
print(f"SHA256哈希值: {hash_value.hex()}")

# 使用SHA3-256哈希算法
hash_obj = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
hash_obj.update(b"Hello, World!")
hash_value = hash_obj.finalize()
print(f"SHA3-256哈希值: {hash_value.hex()}")
```

### 5. 密钥派生函数（PBKDF2）

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
import os

# 密码
password = b"my_secure_password"

# 盐值
salt = os.urandom(16)

# 创建PBKDF2密钥派生器
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,  # 派生32字节密钥
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

# 派生密钥
key = kdf.derive(password)
print(f"派生密钥: {key}")

# 验证密钥
try:
    kdf.verify(password, key)
    print("密钥验证通过")
except Exception as e:
    print(f"密钥验证失败: {e}")
```

## 实际应用示例

### 1. 文件加密

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_file(input_file, output_file, key):
    """
    加密文件
    
    参数:
        input_file: 输入文件路径
        output_file: 输出文件路径
        key: 加密密钥
    """
    # 生成随机IV
    iv = os.urandom(16)
    
    # 创建AES加密器
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    with open(input_file, "rb") as f_in, open(output_file, "wb") as f_out:
        # 写入IV
        f_out.write(iv)
        
        # 分块加密文件
        while True:
            chunk = f_in.read(4096)
            if not chunk:
                break
            
            # 填充最后一个块
            if len(chunk) < 4096:
                pad_length = 16 - (len(chunk) % 16)
                chunk += bytes([pad_length]) * pad_length
            
            encrypted_chunk = encryptor.update(chunk)
            f_out.write(encrypted_chunk)
        
        # 写入最后一个块
        f_out.write(encryptor.finalize())

def decrypt_file(input_file, output_file, key):
    """
    解密文件
    
    参数:
        input_file: 输入文件路径
        output_file: 输出文件路径
        key: 解密密钥
    """
    with open(input_file, "rb") as f_in:
        # 读取IV
        iv = f_in.read(16)
        
        # 创建AES解密器
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        with open(output_file, "wb") as f_out:
            # 分块解密文件
            while True:
                chunk = f_in.read(4096)
                if not chunk:
                    break
                
                decrypted_chunk = decryptor.update(chunk)
                f_out.write(decrypted_chunk)
            
            # 写入最后一个块并移除填充
            last_chunk = decryptor.finalize()
            if last_chunk:
                # 移除填充
                last_chunk = last_chunk[:-last_chunk[-1]]
                f_out.write(last_chunk)

# 示例用法
# 生成密钥
key = os.urandom(32)

# 加密文件
encrypt_file("plaintext.txt", "encrypted.bin", key)
print("文件加密完成")

# 解密文件
decrypt_file("encrypted.bin", "decrypted.txt", key)
print("文件解密完成")
```

### 2. 安全存储密码

```python
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os

def hash_password(password):
    """
    哈希密码
    
    参数:
        password: 明文密码
    
    返回:
        包含盐值和哈希值的元组
    """
    # 生成随机盐值
    salt = os.urandom(16)
    
    # 创建PBKDF2密钥派生器
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    # 派生密钥（哈希密码）
    hashed_password = kdf.derive(password.encode())
    
    return salt, hashed_password

def verify_password(password, salt, hashed_password):
    """
    验证密码
    
    参数:
        password: 明文密码
        salt: 盐值
        hashed_password: 哈希密码
    
    返回:
        验证结果（True/False）
    """
    # 创建PBKDF2密钥派生器
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    
    try:
        kdf.verify(password.encode(), hashed_password)
        return True
    except Exception:
        return False

# 示例用法
password = "my_secure_password"

# 哈希密码
salt, hashed_password = hash_password(password)
print(f"盐值: {salt}")
print(f"哈希密码: {hashed_password}")

# 验证密码
if verify_password(password, salt, hashed_password):
    print("密码验证通过")
else:
    print("密码验证失败")

# 验证错误密码
if verify_password("wrong_password", salt, hashed_password):
    print("密码验证通过")
else:
    print("密码验证失败")
```

### 3. 生成X.509证书

```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime
import os

def generate_self_signed_cert():
    """
    生成自签名X.509证书
    
    返回:
        私钥和证书
    """
    # 生成RSA密钥对
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    
    # 设置证书主题和颁发者
    subject = issuer = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, "CN"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Beijing"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, "Beijing"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Example Company"),
        x509.NameAttribute(NameOID.COMMON_NAME, "example.com"),
    ])
    
    # 构建证书
    cert = x509.CertificateBuilder().subject_name(
        subject
    ).issuer_name(
        issuer
    ).public_key(
        private_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
        # 证书有效期为1年
        datetime.datetime.utcnow() + datetime.timedelta(days=365)
    ).add_extension(
        x509.SubjectAlternativeName([x509.DNSName("example.com")]),
        critical=False,
    ).sign(private_key, hashes.SHA256(), backend=default_backend())
    
    return private_key, cert

# 示例用法
private_key, cert = generate_self_signed_cert()

# 保存私钥和证书
with open("private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("certificate.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("自签名证书生成完成")
```

## 最佳实践

1. **使用高级API**：
   - 优先使用cryptography的高级API
   - 只有在需要特定功能时才使用hazmat层

2. **安全生成密钥**：
   - 使用os.urandom()生成随机密钥
   - 不要使用弱密钥或可预测的密钥

3. **选择合适的加密算法**：
   - 对称加密：优先使用AES-256
   - 非对称加密：优先使用RSA-2048或更高
   - 哈希函数：优先使用SHA-256或SHA-3

4. **保护私钥**：
   - 私钥必须保密存储
   - 使用加密的方式存储私钥

5. **定期更新密钥**：
   - 定期更换加密密钥
   - 避免长期使用同一个密钥

## 常见错误和陷阱

1. **错误的填充方式**：
   ```python
   # 错误：使用错误的填充方式
   ciphertext = encryptor.update(plaintext) + encryptor.finalize()  # 数据长度不是块大小的倍数
   
   # 正确：使用适当的填充方式
   pad_length = 16 - (len(plaintext) % 16)
   plaintext += bytes([pad_length]) * pad_length
   ciphertext = encryptor.update(plaintext) + encryptor.finalize()
   ```

2. **弱密码或密钥**：
   ```python
   # 错误：使用弱密钥
   weak_key = b"password" * 4  # 可预测的密钥
   
   # 正确：使用强密钥
   import os
   strong_key = os.urandom(32)  # 32字节的随机密钥
   ```

3. **错误的协议版本**：
   ```python
   # 错误：使用过时的协议
   from cryptography.hazmat.primitives.ciphers import algorithms
   cipher = Cipher(algorithms.DES(key), modes.CBC(iv), backend=default_backend())  # DES已过时
   
   # 正确：使用现代加密算法
   cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
   ```

## 总结

cryptography模块是Python中功能强大的加密库，提供了广泛的加密功能，包括对称加密、非对称加密、哈希函数、数字签名等。它的设计注重安全性和易用性，分为高级API和低级hazmat层，满足不同用户的需求。在实际应用中，cryptography库广泛用于数据加密、安全通信、密码存储等场景，是Python中进行加密操作的首选库。
