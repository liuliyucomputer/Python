# Python hmac模块详解

```python
"""
hmac模块 - Python中基于哈希的消息认证码实现

hmac模块提供了实现HMAC（Hash-based Message Authentication Code，基于哈希的消息认证码）的功能。
HMAC结合了哈希函数和密钥，可以同时验证数据的完整性和真实性。

主要功能与特点：
- 提供密钥相关的哈希认证功能
- 支持多种哈希算法（MD5、SHA1、SHA256等）
- 防止重放攻击和数据篡改
- 提供常数时间比较方法防止计时攻击
- 可用于API认证、消息签名、数据完整性校验等安全场景

应用场景：
- API请求签名验证
- 文件完整性和真实性校验
- 安全通信协议（如TLS）
- 用户身份验证
- 防止中间人攻击
- 消息认证和不可否认性
"""

import hmac
import hashlib
import os
import time
import base64
import struct
import binascii
import tempfile
import shutil
from datetime import datetime, timedelta
import json
import re

# 1. hmac模块的基本使用
def basic_hmac_usage():
    """
    hmac模块的基本使用方法
    
    功能说明：演示如何使用hmac模块创建和验证HMAC。
    """
    print("=== 1. hmac模块的基本使用 ===")
    
    # 1.1 创建HMAC
    print("\n1.1 创建HMAC:")
    
    # 示例消息和密钥
    message = "这是一条需要认证的消息"
    key = "这是一个密钥，应该安全存储"
    
    print(f"原始消息: {message}")
    print(f"密钥: {key}")
    
    # 创建HMAC对象
    hmac_obj = hmac.new(
        key.encode('utf-8'),  # 密钥（需要是字节类型）
        message.encode('utf-8'),  # 消息（需要是字节类型）
        hashlib.sha256  # 使用的哈希算法
    )
    
    # 获取十六进制表示的HMAC值
    hmac_hex = hmac_obj.hexdigest()
    print(f"HMAC (十六进制): {hmac_hex}")
    print(f"HMAC长度: {len(hmac_hex)} 字符")
    
    # 获取二进制表示的HMAC值
    hmac_bytes = hmac_obj.digest()
    print(f"HMAC (二进制长度): {len(hmac_bytes)} 字节")
    
    # 1.2 使用不同的哈希算法
    print("\n1.2 使用不同的哈希算法:")
    
    algorithms_to_test = ['md5', 'sha1', 'sha256', 'sha512', 'blake2b']
    
    for algorithm in algorithms_to_test:
        try:
            # 获取哈希函数
            hash_func = getattr(hashlib, algorithm)
            
            # 创建HMAC
            hmac_obj = hmac.new(key.encode('utf-8'), message.encode('utf-8'), hash_func)
            hmac_hex = hmac_obj.hexdigest()
            
            print(f"{algorithm.upper()}: {hmac_hex}")
            print(f"  - 二进制长度: {len(hmac_obj.digest())} 字节")
        except AttributeError:
            print(f"算法 {algorithm} 不可用")
    
    # 1.3 增量更新HMAC
    print("\n1.3 增量更新HMAC:")
    
    # 创建HMAC对象（不立即提供消息）
    hmac_obj = hmac.new(key.encode('utf-8'), digestmod=hashlib.sha256)
    
    # 分多次更新消息
    parts = [
        "这是",
        "一条",
        "需要",
        "认证",
        "的消息"
    ]
    
    for i, part in enumerate(parts):
        hmac_obj.update(part.encode('utf-8'))
        print(f"更新部分 {i+1}/{len(parts)}: {part}")
    
    # 计算最终HMAC
    incremental_hmac = hmac_obj.hexdigest()
    
    # 计算一次性HMAC进行比较
   一次性_hmac = hmac.new(
        key.encode('utf-8'),
        ''.join(parts).encode('utf-8'),
        hashlib.sha256
    ).hexdigest()
    
    print(f"\n增量计算的HMAC: {incremental_hmac}")
    print(f"一次性计算的HMAC: {一次性_hmac}")
    print(f"两个HMAC是否相同: {incremental_hmac == 一次性_hmac}")
    
    # 1.4 验证HMAC
    print("\n1.4 验证HMAC:")
    
    # 模拟接收方收到消息和HMAC
    received_message = message
    received_hmac_hex = hmac_hex
    
    # 接收方使用相同的密钥重新计算HMAC
    calculated_hmac_obj = hmac.new(
        key.encode('utf-8'),
        received_message.encode('utf-8'),
        hashlib.sha256
    )
    calculated_hmac_hex = calculated_hmac_obj.hexdigest()
    
    # 方法1: 直接比较字符串（不推荐，存在计时攻击风险）
    print("方法1: 直接字符串比较（不推荐）")
    if calculated_hmac_hex == received_hmac_hex:
        print("  HMAC验证成功，消息未被篡改")
    else:
        print("  HMAC验证失败，消息可能被篡改")
    
    # 方法2: 使用hmac.compare_digest（推荐，防止计时攻击）
    print("方法2: 使用hmac.compare_digest（推荐）")
    if hmac.compare_digest(calculated_hmac_hex, received_hmac_hex):
        print("  HMAC验证成功，消息未被篡改")
    else:
        print("  HMAC验证失败，消息可能被篡改")
    
    # 演示篡改检测
    print("\n演示消息篡改检测:")
    tampered_message = message + "，已被篡改"
    
    # 对篡改后的消息计算HMAC
    tampered_hmac_obj = hmac.new(
        key.encode('utf-8'),
        tampered_message.encode('utf-8'),
        hashlib.sha256
    )
    tampered_hmac_hex = tampered_hmac_obj.hexdigest()
    
    print(f"原始消息的HMAC: {hmac_hex}")
    print(f"篡改后消息的HMAC: {tampered_hmac_hex}")
    print(f"HMAC是否不同: {hmac_hex != tampered_hmac_hex}")
    
    # 使用compare_digest验证
    if not hmac.compare_digest(hmac_hex, tampered_hmac_hex):
        print("成功检测到消息篡改")

# 2. HMAC在API认证中的应用
def api_authentication_example():
    """
    HMAC在API认证中的应用
    
    功能说明：演示如何使用HMAC实现API请求签名验证机制。
    """
    print("\n=== 2. HMAC在API认证中的应用 ===")
    
    # 2.1 API请求签名生成器
    print("\n2.1 API请求签名生成器:")
    
    class APISignatureGenerator:
        """API请求签名生成器"""
        
        def __init__(self, api_key, secret_key):
            """
            初始化API签名生成器
            
            参数:
            - api_key: API密钥（通常可以公开）
            - secret_key: 签名密钥（必须保密）
            """
            self.api_key = api_key
            self.secret_key = secret_key
        
        def generate_signature(self, method, path, params, timestamp=None):
            """
            生成API请求签名
            
            参数:
            - method: HTTP方法（GET, POST等）
            - path: API路径
            - params: 请求参数（字典）
            - timestamp: 时间戳（如果为None则自动生成）
            
            返回:
            - 包含签名、时间戳等信息的字典
            """
            # 如果没有提供时间戳，生成当前时间戳
            if timestamp is None:
                timestamp = int(time.time())
            
            # 创建签名字符串
            # 1. 首先添加HTTP方法
            signature_string = method.upper()
            
            # 2. 添加API路径
            signature_string += path
            
            # 3. 添加时间戳
            signature_string += str(timestamp)
            
            # 4. 添加排序后的参数（键值对用=连接，参数间用&连接）
            if params:
                # 按键名排序
                sorted_params = sorted(params.items())
                param_string = '&'.join([f"{k}={v}" for k, v in sorted_params])
                signature_string += param_string
            
            print(f"\n生成签名的原始字符串:")
            print(f"  {signature_string}")
            
            # 使用HMAC-SHA256生成签名
            hmac_obj = hmac.new(
                self.secret_key.encode('utf-8'),
                signature_string.encode('utf-8'),
                hashlib.sha256
            )
            
            # 将签名转换为Base64编码
            signature = base64.b64encode(hmac_obj.digest()).decode('utf-8')
            
            # 返回包含认证信息的字典
            return {
                'api_key': self.api_key,
                'signature': signature,
                'timestamp': timestamp,
                'signature_method': 'HMAC-SHA256'
            }
    
    # 测试API签名生成器
    api_key = "test_api_key_123"
    secret_key = "test_secret_key_456"
    
    print(f"API密钥: {api_key}")
    print(f"签名密钥: {secret_key}")
    
    # 创建签名生成器实例
    signature_generator = APISignatureGenerator(api_key, secret_key)
    
    # 测试数据
    method = "GET"
    path = "/api/v1/users"
    params = {
        "limit": 10,
        "offset": 0,
        "sort": "created_at"
    }
    
    print(f"\nAPI请求信息:")
    print(f"  HTTP方法: {method}")
    print(f"  API路径: {path}")
    print(f"  请求参数: {params}")
    
    # 生成签名
    auth_info = signature_generator.generate_signature(method, path, params)
    
    print(f"\n生成的认证信息:")
    print(f"  API Key: {auth_info['api_key']}")
    print(f"  签名: {auth_info['signature']}")
    print(f"  时间戳: {auth_info['timestamp']}")
    print(f"  签名方法: {auth_info['signature_method']}")
    
    # 2.2 API请求签名验证器
    print("\n2.2 API请求签名验证器:")
    
    class APISignatureVerifier:
        """API请求签名验证器"""
        
        def __init__(self):
            """初始化验证器"""
            # 在实际应用中，这里应该有一个方法来获取用户的密钥
            # 这里为了演示，我们使用一个模拟的密钥存储
            self.secret_keys = {
                "test_api_key_123": "test_secret_key_456",
                "user_123": "secret_xyz",
                "admin": "admin_super_secret"
            }
            
            # 允许的时间偏差（秒）
            self.max_time_delta = 300  # 5分钟
        
        def get_secret_key(self, api_key):
            """根据API密钥获取对应的签名密钥"""
            return self.secret_keys.get(api_key)
        
        def verify_signature(self, method, path, params, api_key, signature, timestamp):
            """
            验证API请求签名
            
            参数:
            - method: HTTP方法
            - path: API路径
            - params: 请求参数
            - api_key: API密钥
            - signature: 接收到的签名
            - timestamp: 时间戳
            
            返回:
            - (是否验证成功, 错误信息或None)
            """
            # 1. 验证API密钥是否存在
            secret_key = self.get_secret_key(api_key)
            if not secret_key:
                return False, "无效的API密钥"
            
            # 2. 验证时间戳是否在允许的偏差范围内
            current_time = int(time.time())
            time_diff = abs(current_time - timestamp)
            
            if time_diff > self.max_time_delta:
                return False, f"请求过期，时间偏差为{time_diff}秒，超过允许的{self.max_time_delta}秒"
            
            # 3. 重建签名字符串（与生成时相同的步骤）
            signature_string = method.upper() + path + str(timestamp)
            
            if params:
                sorted_params = sorted(params.items())
                param_string = '&'.join([f"{k}={v}" for k, v in sorted_params])
                signature_string += param_string
            
            # 4. 使用密钥重新计算HMAC
            hmac_obj = hmac.new(
                secret_key.encode('utf-8'),
                signature_string.encode('utf-8'),
                hashlib.sha256
            )
            
            # 将计算的签名转换为Base64
            calculated_signature = base64.b64encode(hmac_obj.digest()).decode('utf-8')
            
            # 5. 使用安全的比较方法比较签名
            if hmac.compare_digest(calculated_signature, signature):
                return True, None
            else:
                return False, "签名验证失败，请求可能被篡改"
    
    # 测试API签名验证器
    verifier = APISignatureVerifier()
    
    print("\n测试1: 有效签名")
    # 验证之前生成的签名
    is_valid, error = verifier.verify_signature(
        method, path, params, 
        auth_info['api_key'], 
        auth_info['signature'], 
        auth_info['timestamp']
    )
    
    if is_valid:
        print("  ✓ 签名验证成功")
    else:
        print(f"  ✗ 签名验证失败: {error}")
    
    print("\n测试2: 篡改的签名")
    # 篡改签名
    tampered_signature = auth_info['signature'][:-1] + 'X'
    is_valid, error = verifier.verify_signature(
        method, path, params, 
        auth_info['api_key'], 
        tampered_signature, 
        auth_info['timestamp']
    )
    
    if is_valid:
        print("  ✓ 签名验证成功")
    else:
        print(f"  ✗ 签名验证失败: {error}")
    
    print("\n测试3: 篡改的参数")
    # 篡改参数
    tampered_params = params.copy()
    tampered_params['limit'] = 100  # 把10改为100
    
    is_valid, error = verifier.verify_signature(
        method, path, tampered_params, 
        auth_info['api_key'], 
        auth_info['signature'], 
        auth_info['timestamp']
    )
    
    if is_valid:
        print("  ✓ 签名验证成功")
    else:
        print(f"  ✗ 签名验证失败: {error}")
    
    print("\n测试4: 过期的时间戳")
    # 使用过期的时间戳
    expired_timestamp = auth_info['timestamp'] - 3600  # 过期1小时
    
    is_valid, error = verifier.verify_signature(
        method, path, params, 
        auth_info['api_key'], 
        auth_info['signature'], 
        expired_timestamp
    )
    
    if is_valid:
        print("  ✓ 签名验证成功")
    else:
        print(f"  ✗ 签名验证失败: {error}")
    
    print("\n测试5: 无效的API密钥")
    # 使用无效的API密钥
    invalid_api_key = "non_existent_key"
    
    is_valid, error = verifier.verify_signature(
        method, path, params, 
        invalid_api_key, 
        auth_info['signature'], 
        auth_info['timestamp']
    )
    
    if is_valid:
        print("  ✓ 签名验证成功")
    else:
        print(f"  ✗ 签名验证失败: {error}")

# 3. HMAC用于文件完整性和真实性验证
def file_integrity_and_authenticity():
    """
    HMAC用于文件完整性和真实性验证
    
    功能说明：演示如何使用HMAC确保文件不仅没有被篡改（完整性），
    而且确实来自预期的发送方（真实性）。
    """
    print("\n=== 3. HMAC用于文件完整性和真实性验证 ===")
    
    # 准备示例文件
    temp_dir = tempfile.mkdtemp()
    print(f"创建临时目录: {temp_dir}")
    
    try:
        # 创建测试文件
        test_file_path = os.path.join(temp_dir, "test_data.txt")
        with open(test_file_path, "w", encoding="utf-8") as f:
            f.write("这是一个测试文件，用于演示HMAC文件完整性和真实性验证。\n")
            f.write("HMAC不仅可以验证文件是否被篡改，还可以验证文件来源。\n")
            f.write("这比简单的哈希值更安全，因为它需要一个密钥。\n")
            f.write("\n" * 5)  # 添加一些空行
            f.write("文件结尾标记。")
        
        print(f"创建测试文件: {test_file_path}")
        print(f"文件大小: {os.path.getsize(test_file_path)} 字节")
        
        # 3.1 生成文件HMAC
        print("\n3.1 生成文件HMAC:")
        
        def generate_file_hmac(file_path, key, algorithm=hashlib.sha256, chunk_size=8192):
            """
            为文件生成HMAC
            
            参数:
            - file_path: 文件路径
            - key: 密钥
            - algorithm: 哈希算法
            - chunk_size: 读取块大小
            
            返回:
            - HMAC的十六进制表示
            """
            # 确保密钥是字节类型
            if isinstance(key, str):
                key = key.encode('utf-8')
            
            # 创建HMAC对象
            hmac_obj = hmac.new(key, digestmod=algorithm)
            
            # 分块读取文件并更新HMAC
            try:
                with open(file_path, "rb") as f:
                    while True:
                        chunk = f.read(chunk_size)
                        if not chunk:
                            break
                        hmac_obj.update(chunk)
                
                # 返回十六进制表示的HMAC
                return hmac_obj.hexdigest()
            except IOError as e:
                print(f"无法读取文件 {file_path}: {e}")
                return None
        
        # 测试密钥
        file_key = "这是保护文件完整性和真实性的密钥"
        
        # 生成文件HMAC
        file_hmac = generate_file_hmac(test_file_path, file_key)
        
        print(f"使用密钥: {file_key}")
        print(f"生成的文件HMAC: {file_hmac}")
        
        # 3.2 验证文件HMAC
        print("\n3.2 验证文件HMAC:")
        
        def verify_file_hmac(file_path, key, expected_hmac, algorithm=hashlib.sha256):
            """
            验证文件HMAC
            
            参数:
            - file_path: 文件路径
            - key: 密钥
            - expected_hmac: 预期的HMAC值
            - algorithm: 哈希算法
            
            返回:
            - 是否验证成功
            """
            # 计算文件的当前HMAC
            current_hmac = generate_file_hmac(file_path, key, algorithm)
            
            if current_hmac is None:
                return False
            
            # 使用安全的比较方法
            return hmac.compare_digest(current_hmac, expected_hmac)
        
        # 测试验证
        print("\n测试1: 验证未修改的文件")
        is_valid = verify_file_hmac(test_file_path, file_key, file_hmac)
        print(f"验证结果: {'成功' if is_valid else '失败'}")
        print(f"结论: 文件{'完整且来源可信' if is_valid else '可能被篡改或来源不可信'}")
        
        # 3.3 篡改检测演示
        print("\n测试2: 验证被篡改的文件")
        
        # 模拟文件被篡改
        with open(test_file_path, "a", encoding="utf-8") as f:
            f.write("\n这是恶意添加的内容。")
        
        print(f"文件已被修改，新大小: {os.path.getsize(test_file_path)} 字节")
        
        # 验证被篡改的文件
        is_valid = verify_file_hmac(test_file_path, file_key, file_hmac)
        print(f"验证结果: {'成功' if is_valid else '失败'}")
        print(f"结论: 文件{'完整且来源可信' if is_valid else '可能被篡改或来源不可信'}")
        
        # 3.4 创建和验证签名文件
        print("\n3.3 创建和验证签名文件:")
        
        def create_signature_file(file_path, key, signature_file_path=None, algorithm=hashlib.sha256):
            """
            创建签名文件，包含文件的HMAC和元数据
            
            参数:
            - file_path: 要签名的文件路径
            - key: 签名密钥
            - signature_file_path: 签名文件路径（如果为None则在原文件名后添加.sig）
            - algorithm: 哈希算法
            
            返回:
            - 签名文件路径
            """
            # 生成文件HMAC
            file_hmac = generate_file_hmac(file_path, key, algorithm)
            if file_hmac is None:
                return None
            
            # 获取算法名称
            algorithm_name = algorithm.__name__
            
            # 创建签名数据
            signature_data = {
                'file_name': os.path.basename(file_path),
                'file_size': os.path.getsize(file_path),
                'timestamp': datetime.now().isoformat(),
                'algorithm': algorithm_name,
                'hmac': file_hmac
            }
            
            # 确定签名文件路径
            if signature_file_path is None:
                signature_file_path = f"{file_path}.sig"
            
            # 保存签名数据
            with open(signature_file_path, "w", encoding="utf-8") as f:
                json.dump(signature_data, f, indent=2, ensure_ascii=False)
            
            return signature_file_path
        
        def verify_signature_file(file_path, key, signature_file_path):
            """
            验证签名文件
            
            参数:
            - file_path: 要验证的文件路径
            - key: 签名密钥
            - signature_file_path: 签名文件路径
            
            返回:
            - (是否验证成功, 详细信息)
            """
            try:
                # 读取签名数据
                with open(signature_file_path, "r", encoding="utf-8") as f:
                    signature_data = json.load(f)
                
                # 验证文件名
                if os.path.basename(file_path) != signature_data['file_name']:
                    return False, f"文件名不匹配: 期望 {signature_data['file_name']}, 得到 {os.path.basename(file_path)}"
                
                # 验证文件大小（可选，但可以快速检测明显的修改）
                current_size = os.path.getsize(file_path)
                if current_size != signature_data['file_size']:
                    return False, f"文件大小不匹配: 期望 {signature_data['file_size']}, 得到 {current_size}"
                
                # 获取算法
                algorithm_name = signature_data['algorithm']
                try:
                    algorithm = getattr(hashlib, algorithm_name)
                except AttributeError:
                    return False, f"不支持的哈希算法: {algorithm_name}"
                
                # 验证HMAC
                expected_hmac = signature_data['hmac']
                is_valid = verify_file_hmac(file_path, key, expected_hmac, algorithm)
                
                if is_valid:
                    return True, {
                        'verified': True,
                        'signature_time': signature_data['timestamp'],
                        'algorithm': algorithm_name,
                        'message': "文件完整性和真实性验证成功"
                    }
                else:
                    return False, "HMAC验证失败，文件可能被篡改或密钥错误"
                    
            except json.JSONDecodeError:
                return False, "签名文件格式无效"
            except IOError as e:
                return False, f"无法读取签名文件: {e}"
        
        # 创建一个新的未被篡改的测试文件
        new_test_file_path = os.path.join(temp_dir, "authentic_file.txt")
        with open(new_test_file_path, "w", encoding="utf-8") as f:
            f.write("这是一个将被签名的真实文件。\n")
            f.write("签名将证明这个文件的完整性和真实性。\n")
        
        print(f"创建新的测试文件: {new_test_file_path}")
        
        # 创建签名文件
        signature_file = create_signature_file(new_test_file_path, file_key)
        print(f"创建签名文件: {signature_file}")
        
        # 读取并显示签名文件内容
        with open(signature_file, "r", encoding="utf-8") as f:
            signature_content = f.read()
        print("\n签名文件内容:")
        print(signature_content)
        
        # 验证签名文件
        print("\n验证签名文件:")
        is_valid, info = verify_signature_file(new_test_file_path, file_key, signature_file)
        
        if is_valid:
            print(f"✓ 验证成功: {info['message']}")
            print(f"  签名时间: {info['signature_time']}")
            print(f"  使用算法: {info['algorithm']}")
        else:
            print(f"✗ 验证失败: {info}")
        
        # 模拟文件被篡改并验证
        print("\n模拟文件被篡改后验证:")
        with open(new_test_file_path, "a", encoding="utf-8") as f:
            f.write("\n恶意篡改内容！")
        
        is_valid, info = verify_signature_file(new_test_file_path, file_key, signature_file)
        
        if is_valid:
            print(f"✓ 验证成功: {info['message']}")
        else:
            print(f"✗ 验证失败: {info}")
        
    finally:
        # 清理
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"\n清理临时目录: {temp_dir}")

# 4. 基于时间的一次性密码(TOTP)实现
def totp_implementation():
    """
    基于时间的一次性密码(TOTP)实现
    
    功能说明：演示如何使用HMAC实现基于时间的一次性密码，常用于双因素认证。
    """
    print("\n=== 4. 基于时间的一次性密码(TOTP)实现 ===")
    
    # TOTP实现类
    class TOTPGenerator:
        """基于时间的一次性密码生成器"""
        
        def __init__(self, secret_key, digits=6, period=30, algorithm=hashlib.sha1):
            """
            初始化TOTP生成器
            
            参数:
            - secret_key: 密钥（应为base32编码）
            - digits: 验证码位数（通常为6或8）
            - period: 有效周期（秒，通常为30）
            - algorithm: 哈希算法（通常为SHA1）
            """
            self.secret_key = secret_key
            self.digits = digits
            self.period = period
            self.algorithm = algorithm
        
        def _base32_decode(self, s):
            """解码base32编码的字符串"""
            # 添加padding以确保长度正确
            s = s.upper().replace('=', '')
            padding = '=' * ((8 - len(s) % 8) % 8)
            s += padding
            
            # 使用base64进行解码
            try:
                return base64.b32decode(s)
            except binascii.Error:
                raise ValueError("无效的base32编码密钥")
        
        def _get_timestamp(self):
            """获取当前时间戳，基于指定周期"""
            return int(time.time() / self.period)
        
        def generate(self, timestamp=None):
            """
            生成TOTP码
            
            参数:
            - timestamp: 可选的时间戳，如果为None则使用当前时间
            
            返回:
            - TOTP码
            """
            # 如果没有提供时间戳，使用当前时间戳
            if timestamp is None:
                timestamp = self._get_timestamp()
            
            # 将时间戳转换为字节（大端序）
            timestamp_bytes = struct.pack('!Q', timestamp)  # !表示网络字节序（大端序），Q表示无符号长整型
            
            # 解码密钥
            key_bytes = self._base32_decode(self.secret_key)
            
            # 使用HMAC计算哈希值
            hmac_obj = hmac.new(key_bytes, timestamp_bytes, self.algorithm)
            hmac_hash = hmac_obj.digest()
            
            # 动态截取（Dynamic Truncation）
            # 取哈希值的最后一个字节的低4位作为偏移量
            offset = hmac_hash[-1] & 0x0F
            
            # 从偏移量开始取4个字节，使用大端序，并忽略最高位
            code = struct.unpack('!I', hmac_hash[offset:offset+4])[0] & 0x7FFFFFFF
            
            # 取模以获得指定位数的数字
            code = code % (10 ** self.digits)
            
            # 格式化为指定位数，不足前导补零
            return f"{code:0{self.digits}d}"
        
        def verify(self, totp, window=1):
            """
            验证TOTP码
            
            参数:
            - totp: 要验证的TOTP码
            - window: 验证窗口大小（当前时间戳±window）
            
            返回:
            - 是否验证成功
            """
            current_timestamp = self._get_timestamp()
            
            # 检查当前时间戳和周围的时间戳
            for i in range(-window, window + 1):
                candidate_timestamp = current_timestamp + i
                candidate_totp = self.generate(candidate_timestamp)
                
                # 使用安全比较
                if hmac.compare_digest(candidate_totp, totp):
                    return True
            
            return False
        
        def get_remaining_time(self):
            """
            获取当前TOTP码的剩余有效时间
            
            返回:
            - 剩余秒数
            """
            current_time = time.time()
            return self.period - (current_time % self.period)
        
        def generate_provisioning_uri(self, account_name, issuer_name="Python-TOTP"):
            """
            生成用于TOTP应用程序的配置URI
            
            参数:
            - account_name: 账户名称
            - issuer_name: 发行者名称
            
            返回:
            - URI字符串
            """
            # 构建URI参数
            params = {
                'secret': self.secret_key,
                'issuer': issuer_name,
                'algorithm': self.algorithm.__name__.upper(),
                'digits': self.digits,
                'period': self.period
            }
            
            # 构建URI
            param_string = '&'.join([f"{k}={v}" for k, v in params.items()])
            return f"otpauth://totp/{issuer_name}:{account_name}?{param_string}"
    
    # 演示TOTP生成和验证
    print("\nTOTP生成器演示:")
    
    # 示例密钥（base32编码）
    secret_key = "JBSWY3DPEHPK3PXP"  # 这是一个标准测试密钥
    print(f"使用密钥: {secret_key}")
    
    # 创建TOTP生成器
    totp = TOTPGenerator(secret_key)
    
    # 生成当前TOTP
    current_totp = totp.generate()
    remaining_time = totp.get_remaining_time()
    
    print(f"当前TOTP码: {current_totp}")
    print(f"有效剩余时间: {remaining_time:.1f} 秒")
    print(f"配置URI: {totp.generate_provisioning_uri('user@example.com')}")
    
    # 验证正确的TOTP
    is_valid = totp.verify(current_totp)
    print(f"\n验证当前TOTP:")
    print(f"  验证结果: {'成功' if is_valid else '失败'}")
    
    # 验证错误的TOTP
    wrong_totp = "123456"
    is_valid = totp.verify(wrong_totp)
    print(f"\n验证错误的TOTP ({wrong_totp}):")
    print(f"  验证结果: {'成功' if is_valid else '失败'}")
    
    # 模拟时间窗口验证
    print("\n演示时间窗口验证:")
    
    # 获取当前时间戳
    current_timestamp = totp._get_timestamp()
    
    # 生成未来时间戳的TOTP
    future_timestamp = current_timestamp + 1  # 下一个时间窗口
    future_totp = totp.generate(future_timestamp)
    
    print(f"当前时间戳: {current_timestamp}")
    print(f"当前TOTP: {totp.generate(current_timestamp)}")
    print(f"未来时间戳: {future_timestamp}")
    print(f"未来TOTP: {future_totp}")
    
    # 默认窗口大小为1，应该验证失败
    is_valid = totp.verify(future_totp, window=0)  # 只验证当前时间戳
    print(f"\n使用window=0验证未来TOTP:")
    print(f"  验证结果: {'成功' if is_valid else '失败'}")
    
    # 使用更大的窗口应该验证成功
    is_valid = totp.verify(future_totp, window=1)  # 验证当前±1个时间窗口
    print(f"\n使用window=1验证未来TOTP:")
    print(f"  验证结果: {'成功' if is_valid else '失败'}")

# 5. HMAC的安全性分析和最佳实践
def security_analysis_and_best_practices():
    """
    HMAC的安全性分析和最佳实践
    
    功能说明：分析HMAC的安全性，并提供使用HMAC时的最佳实践。
    """
    print("\n=== 5. HMAC的安全性分析和最佳实践 ===")
    
    # 5.1 HMAC的安全性分析
    print("\n5.1 HMAC的安全性分析:")
    
    print("HMAC安全性的关键优势:")
    print("1. 密钥分离:")
    print("   - HMAC使用密钥和哈希算法的组合，即使哈希算法存在碰撞漏洞")
    print("   - 没有密钥，即使知道哈希算法也无法伪造有效的HMAC")
    
    print("\n2. 安全性证明:")
    print("   - HMAC有严格的密码学安全性证明")
    print("   - 如果底层哈希函数是抗碰撞的，那么HMAC也是抗碰撞的")
    print("   - 理论上，破解HMAC的难度不低于破解底层哈希函数")
    
    print("\n3. 抵抗常见攻击:")
    print("   - 可以抵抗长度扩展攻击(length extension attacks)")
    print("   - 可以抵抗碰撞攻击(collision attacks)")
    print("   - 可以抵抗预计算攻击(precomputation attacks)")
    print("   - 可以抵抗彩虹表攻击(rainbow table attacks)")
    
    print("\n4. 常见的HMAC安全问题:")
    print("   - 密钥泄露: 最严重的安全风险，会导致整个系统被破解")
    print("   - 弱密钥: 太短或可预测的密钥容易被暴力破解")
    print("   - 不安全的比较: 不使用constant-time比较可能导致计时攻击")
    print("   - 密钥重用: 在多个系统中重用相同密钥增加风险")
    print("   - 过期哈希算法: 使用已知存在漏洞的哈希函数(SHA1, MD5)")
    
    # 5.2 实际安全威胁演示
    print("\n5.2 演示计时攻击风险:")
    
    def vulnerable_compare(hmac1, hmac2):
        """不安全的HMAC比较方法（有计时攻击风险）"""
        return hmac1 == hmac2
    
    def secure_compare(hmac1, hmac2):
        """安全的HMAC比较方法（使用hmac.compare_digest）"""
        return hmac.compare_digest(hmac1, hmac2)
    
    # 生成两个不同的HMAC
    valid_hmac = hmac.new(
        b"secret_key",
        b"test_message",
        hashlib.sha256
    ).hexdigest()
    
    # 一个只有第一位不同的HMAC
    tampered_hmac1 = "a" + valid_hmac[1:]
    
    # 一个只有最后一位不同的HMAC
    tampered_hmac2 = valid_hmac[:-1] + "a"
    
    print(f"有效HMAC: {valid_hmac}")
    print(f"第一位不同: {tampered_hmac1}")
    print(f"最后位不同: {tampered_hmac2}")
    
    print("\n计时攻击风险测试:")
    print("注意: 这个测试可能需要多次运行才能观察到明显的差异")
    
    # 测试不安全比较的时间
    total_time1 = 0
    total_time2 = 0
    iterations = 10000
    
    print(f"\n运行{iterations}次比较...")
    
    # 测量比较第一个字节不同的HMAC所需时间
    for _ in range(iterations):
        start = time.time()
        vulnerable_compare(tampered_hmac1, valid_hmac)
        end = time.time()
        total_time1 += (end - start)
    
    # 测量比较最后一个字节不同的HMAC所需时间
    for _ in range(iterations):
        start = time.time()
        vulnerable_compare(tampered_hmac2, valid_hmac)
        end = time.time()
        total_time2 += (end - start)
    
    avg_time1 = total_time1 / iterations * 10**9  # 转换为纳秒
    avg_time2 = total_time2 / iterations * 10**9  # 转换为纳秒
    
    print(f"第一位不同的平均比较时间: {avg_time1:.2f} 纳秒")
    print(f"最后位不同的平均比较时间: {avg_time2:.2f} 纳秒")
    print(f"差异: {abs(avg_time1 - avg_time2):.2f} 纳秒 ({abs(avg_time1 - avg_time2)/max(avg_time1, avg_time2)*100:.2f}%)")
    print("\n结论: 不安全的比较方法可能泄露HMAC差异的位置信息，")
    print("这使得攻击者可以通过测量比较时间来逐位猜测HMAC值。")
    
    # 5.3 HMAC最佳实践
    print("\n5.3 HMAC最佳实践:")
    
    print("1. 密钥管理:")
    print("   - 使用足够长度的随机密钥（至少与哈希输出长度相当）")
    print("   - 使用安全的随机数生成器生成密钥(os.urandom)")
    print("   - 为不同系统使用不同的密钥")
    print("   - 定期轮换密钥")
    print("   - 使用密钥管理系统存储密钥，不要硬编码")
    
    print("\n2. 哈希算法选择:")
    print("   - 推荐使用SHA-256或SHA-512")
    print("   - 避免使用MD5和SHA1")
    print("   - 对于更高安全性，考虑使用SHA-3系列")
    
    print("\n3. 实现安全:")
    print("   - 始终使用hmac.compare_digest进行HMAC比较")
    print("   - 不要在日志中记录原始密钥")
    print("   - 为API请求添加时间戳防止重放攻击")
    print("   - 实现请求限流防止暴力破解")
    
    print("\n4. 密钥长度建议:")
    print("   - SHA-256: 至少32字节（256位）密钥")
    print("   - SHA-512: 至少64字节（512位）密钥")
    print("   - 对于预共享密钥，使用Base64或Base32编码便于传输")
    
    print("\n5. 安全示例:")
    print("生成安全的HMAC密钥:")
    
    # 生成安全的随机密钥示例
    for algorithm in ['sha256', 'sha512']:
        # 对于SHA-256，推荐至少32字节密钥；对于SHA-512，推荐至少64字节密钥
        key_length = 32 if algorithm == 'sha256' else 64
        secure_key = os.urandom(key_length)
        base64_key = base64.b64encode(secure_key).decode('ascii')
        
        print(f"  {algorithm.upper()} ({key_length}字节密钥): {base64_key}")

# 6. 高级HMAC应用场景
def advanced_hmac_applications():
    """
    高级HMAC应用场景
    
    功能说明：演示一些高级的HMAC应用场景，如消息认证、数据完整性校验等。
    """
    print("\n=== 6. 高级HMAC应用场景 ===")
    
    # 6.1 安全消息传递系统
    print("\n6.1 安全消息传递系统:")
    
    class SecureMessageSystem:
        """安全消息传递系统，使用HMAC确保消息的完整性和真实性"""
        
        def __init__(self, shared_key):
            """
            初始化安全消息系统
            
            参数:
            - shared_key: 通信双方共享的密钥
            """
            self.shared_key = shared_key
        
        def create_message(self, message):
            """
            创建安全消息
            
            参数:
            - message: 要发送的消息内容
            
            返回:
            - 包含消息、HMAC和时间戳的字典
            """
            # 添加时间戳以防止重放攻击
            timestamp = int(time.time())
            
            # 创建消息内容
            message_data = {
                'content': message,
                'timestamp': timestamp
            }
            
            # 将消息转换为JSON
            message_json = json.dumps(message_data, sort_keys=True, ensure_ascii=False)
            
            # 计算HMAC
            hmac_obj = hmac.new(
                self.shared_key.encode('utf-8'),
                message_json.encode('utf-8'),
                hashlib.sha256
            )
            
            # 创建最终消息
            secure_message = {
                'message': message_data,
                'hmac': hmac_obj.hexdigest(),
                'algorithm': 'HMAC-SHA256'
            }
            
            return secure_message
        
        def verify_message(self, secure_message, max_age=300):
            """
            验证安全消息
            
            参数:
            - secure_message: 接收到的安全消息
            - max_age: 消息最大有效期（秒）
            
            返回:
            - (是否验证成功, 消息内容或错误信息)
            """
            # 提取消息内容
            message_data = secure_message.get('message')
            received_hmac = secure_message.get('hmac')
            
            if not message_data or not received_hmac:
                return False, "无效的消息格式"
            
            # 验证时间戳
            timestamp = message_data.get('timestamp')
            if not timestamp:
                return False, "消息缺少时间戳"
            
            # 检查消息是否过期
            current_time = int(time.time())
            if current_time - timestamp > max_age:
                return False, f"消息已过期，超过{max_age}秒有效期"
            
            # 重新计算HMAC进行验证
            message_json = json.dumps(message_data, sort_keys=True, ensure_ascii=False)
            hmac_obj = hmac.new(
                self.shared_key.encode('utf-8'),
                message_json.encode('utf-8'),
                hashlib.sha256
            )
            
            calculated_hmac = hmac_obj.hexdigest()
            
            # 使用安全比较
            if hmac.compare_digest(calculated_hmac, received_hmac):
                return True, message_data['content']
            else:
                return False, "HMAC验证失败，消息可能被篡改"
    
    # 测试安全消息传递系统
    shared_key = "这是通信双方共享的密钥，必须保密"
    message_system = SecureMessageSystem(shared_key)
    
    # 创建安全消息
    original_message = "这是一条需要安全传输的敏感消息"
    secure_message = message_system.create_message(original_message)
    
    print(f"原始消息: {original_message}")
    print("\n创建的安全消息:")
    print(json.dumps(secure_message, indent=2, ensure_ascii=False))
    
    # 验证消息
    is_valid, result = message_system.verify_message(secure_message)
    print("\n验证结果:")
    if is_valid:
        print(f"✓ 验证成功，消息内容: {result}")
    else:
        print(f"✗ 验证失败: {result}")
    
    # 模拟篡改消息
    tampered_message = secure_message.copy()
    tampered_message['message']['content'] = "这是被篡改的消息内容"
    
    print("\n模拟篡改消息后验证:")
    is_valid, result = message_system.verify_message(tampered_message)
    if is_valid:
        print(f"✓ 验证成功，消息内容: {result}")
    else:
        print(f"✗ 验证失败: {result}")
    
    # 6.2 数据库记录完整性保护
    print("\n6.2 数据库记录完整性保护:")
    
    class DatabaseIntegrityProtector:
        """数据库记录完整性保护工具，使用HMAC保护数据库记录"""
        
        def __init__(self, secret_key):
            """
            初始化数据库完整性保护器
            
            参数:
            - secret_key: 用于生成HMAC的密钥
            """
            self.secret_key = secret_key
        
        def generate_record_signature(self, record):
            """
            为数据库记录生成签名
            
            参数:
            - record: 数据库记录（字典）
            
            返回:
            - 记录签名
            """
            # 确保记录是字典
            if not isinstance(record, dict):
                raise ValueError("记录必须是字典类型")
            
            # 按键名排序以确保一致的顺序
            sorted_record = sorted(record.items())
            
            # 创建签名字符串（不包含signature字段本身）
            signature_string = ""
            for key, value in sorted_record:
                if key != 'signature':  # 排除signature字段本身
                    signature_string += f"{key}:{value}|"
            
            # 移除末尾的分隔符
            if signature_string:
                signature_string = signature_string[:-1]
            
            # 计算HMAC
            hmac_obj = hmac.new(
                self.secret_key.encode('utf-8'),
                signature_string.encode('utf-8'),
                hashlib.sha256
            )
            
            return hmac_obj.hexdigest()
        
        def sign_record(self, record):
            """
            为记录添加签名
            
            参数:
            - record: 数据库记录（字典）
            
            返回:
            - 添加了签名的记录
            """
            # 复制记录以避免修改原始数据
            signed_record = record.copy()
            
            # 移除可能存在的旧签名
            if 'signature' in signed_record:
                del signed_record['signature']
            
            # 生成并添加新签名
            signed_record['signature'] = self.generate_record_signature(signed_record)
            
            return signed_record
        
        def verify_record(self, record):
            """
            验证记录的完整性
            
            参数:
            - record: 数据库记录（字典）
            
            返回:
            - 是否验证成功
            """
            # 检查记录是否包含签名
            if 'signature' not in record:
                return False
            
            # 提取签名
            received_signature = record['signature']
            
            # 创建不包含签名的记录副本
            record_without_signature = record.copy()
            del record_without_signature['signature']
            
            # 计算预期签名
            expected_signature = self.generate_record_signature(record_without_signature)
            
            # 使用安全比较
            return hmac.compare_digest(expected_signature, received_signature)
    
    # 测试数据库记录完整性保护
    db_protector = DatabaseIntegrityProtector("database_integrity_key")
    
    # 创建测试记录
    original_record = {
        'id': 1001,
        'username': 'test_user',
        'email': 'test@example.com',
        'created_at': '2023-04-01T10:00:00',
        'role': 'user',
        'status': 'active'
    }
    
    # 为记录添加签名
    signed_record = db_protector.sign_record(original_record)
    
    print("原始数据库记录:")
    print(json.dumps(original_record, indent=2))
    
    print("\n添加签名后的记录:")
    print(json.dumps(signed_record, indent=2))
    
    # 验证记录
    is_valid = db_protector.verify_record(signed_record)
    print(f"\n记录完整性验证: {'成功' if is_valid else '失败'}")
    
    # 模拟篡改记录
    tampered_record = signed_record.copy()
    tampered_record['role'] = 'admin'  # 尝试提升权限
    
    print("\n篡改后的记录:")
    print(json.dumps(tampered_record, indent=2))
    
    # 验证被篡改的记录
    is_valid = db_protector.verify_record(tampered_record)
    print(f"\n篡改后记录完整性验证: {'成功' if is_valid else '失败'}")
    
    # 6.3 安全cookie实现
    print("\n6.3 安全cookie实现:")
    
    class SecureCookie:
        """安全cookie实现，使用HMAC防止cookie被篡改"""
        
        def __init__(self, secret_key):
            """
            初始化安全cookie
            
            参数:
            - secret_key: 用于生成HMAC的密钥
            """
            self.secret_key = secret_key
        
        def create_cookie(self, data, max_age=86400):  # 默认有效期1天
            """
            创建安全cookie
            
            参数:
            - data: 要存储在cookie中的数据（字典）
            - max_age: cookie最大有效期（秒）
            
            返回:
            - 序列化并签名的cookie值
            """
            # 添加过期时间
            expires_at = int(time.time()) + max_age
            cookie_data = {
                'data': data,
                'expires_at': expires_at
            }
            
            # 序列化数据
            try:
                json_data = json.dumps(cookie_data, sort_keys=True)
            except (TypeError, ValueError) as e:
                raise ValueError(f"无法序列化cookie数据: {e}")
            
            # 生成HMAC
            hmac_obj = hmac.new(
                self.secret_key.encode('utf-8'),
                json_data.encode('utf-8'),
                hashlib.sha256
            )
            signature = hmac_obj.hexdigest()
            
            # 组合数据和签名（使用|分隔）
            cookie_value = f"{json_data}|{signature}"
            
            # Base64编码以确保安全传输
            return base64.b64encode(cookie_value.encode('utf-8')).decode('utf-8')
        
        def parse_cookie(self, cookie_value):
            """
            解析和验证安全cookie
            
            参数:
            - cookie_value: cookie值
            
            返回:
            - (是否有效, cookie数据或错误信息)
            """
            try:
                # Base64解码
                decoded_value = base64.b64decode(cookie_value).decode('utf-8')
                
                # 分割数据和签名
                if '|' not in decoded_value:
                    return False, "无效的cookie格式"
                
                json_data, signature = decoded_value.rsplit('|', 1)
                
                # 验证签名
                hmac_obj = hmac.new(
                    self.secret_key.encode('utf-8'),
                    json_data.encode('utf-8'),
                    hashlib.sha256
                )
                calculated_signature = hmac_obj.hexdigest()
                
                if not hmac.compare_digest(calculated_signature, signature):
                    return False, "cookie签名验证失败，可能被篡改"
                
                # 解析JSON数据
                cookie_data = json.loads(json_data)
                
                # 验证是否过期
                current_time = int(time.time())
                if cookie_data.get('expires_at', 0) < current_time:
                    return False, "cookie已过期"
                
                # 返回cookie数据
                return True, cookie_data['data']
                
            except (base64.binascii.Error, json.JSONDecodeError):
                return False, "无效的cookie格式"
            except Exception as e:
                return False, f"解析cookie时出错: {str(e)}"
    
    # 测试安全cookie
    cookie_secret = "secure_cookie_signing_key"
    secure_cookie = SecureCookie(cookie_secret)
    
    # 用户会话数据
    user_session = {
        'user_id': 1234,
        'username': 'johndoe',
        'roles': ['user', 'premium'],
        'login_time': datetime.now().isoformat()
    }
    
    # 创建安全cookie
    cookie_value = secure_cookie.create_cookie(user_session)
    
    print("用户会话数据:")
    print(json.dumps(user_session, indent=2))
    
    print("\n生成的安全cookie:")
    print(cookie_value)
    
    # 解析和验证cookie
    is_valid, data = secure_cookie.parse_cookie(cookie_value)
    print(f"\ncookie验证结果: {'成功' if is_valid else '失败'}")
    
    if is_valid:
        print("解析出的用户数据:")
        print(json.dumps(data, indent=2))
    else:
        print(f"错误信息: {data}")
    
    # 模拟篡改cookie
    print("\n模拟篡改cookie:")
    # 解码cookie
    decoded = base64.b64decode(cookie_value).decode('utf-8')
    # 修改数据部分（不修改签名）
    json_part, signature_part = decoded.rsplit('|', 1)
    cookie_data = json.loads(json_part)
    cookie_data['data']['roles'].append('admin')  # 尝试添加管理员权限
    modified_json = json.dumps(cookie_data, sort_keys=True)
    # 重新组合，但不更新签名
    tampered_cookie = base64.b64encode(
        f"{modified_json}|{signature_part}".encode('utf-8')
    ).decode('utf-8')
    
    # 验证被篡改的cookie
    is_valid, data = secure_cookie.parse_cookie(tampered_cookie)
    print(f"篡改后cookie验证结果: {'成功' if is_valid else '失败'}")
    
    if not is_valid:
        print(f"错误信息: {data}")

# 7. HMAC性能优化与比较
def hmac_performance_optimization():
    """
    HMAC性能优化与比较
    
    功能说明：分析HMAC的性能特点，并与其他认证方法进行比较。
    """
    print("\n=== 7. HMAC性能优化与比较 ===")
    
    # 7.1 HMAC性能测试
    print("\n7.1 HMAC性能测试:")
    
    # 测试不同大小的消息
    message_sizes = [
        (10, "10字节"),
        (100, "100字节"),
        (1000, "1KB"),
        (10000, "10KB"),
        (100000, "100KB"),
        (1000000, "1MB")
    ]
    
    # 测试的哈希算法
    algorithms_to_test = ['md5', 'sha1', 'sha256', 'sha512', 'blake2b']
    
    print("不同大小消息的HMAC计算性能:")
    print("消息大小 | 算法     | 执行时间(秒) | 处理速度(MB/s)")
    print("---------|---------|------------|---------------")
    
    for size_bytes, size_label in message_sizes:
        # 生成测试消息
        test_message = b'x' * size_bytes
        test_key = os.urandom(32)  # 32字节密钥
        
        # 执行测试次数
        iterations = 1000 if size_bytes < 100000 else 100  # 小消息多测试几次
        
        for algorithm in algorithms_to_test:
            try:
                hash_func = getattr(hashlib, algorithm)
                
                # 预热
                for _ in range(10):
                    hmac.new(test_key, test_message, hash_func).hexdigest()
                
                # 测量时间
                start_time = time.time()
                for _ in range(iterations):
                    hmac.new(test_key, test_message, hash_func).hexdigest()
                end_time = time.time()
                
                # 计算性能指标
                elapsed = end_time - start_time
                total_bytes = size_bytes * iterations
                mb_per_second = (total_bytes / (1024 * 1024)) / elapsed if elapsed > 0 else 0
                
                print(f"{size_label:<8} | {algorithm.upper():<8} | {elapsed/iterations:.6f} | {mb_per_second:11.2f}")
                
            except AttributeError:
                print(f"{size_label:<8} | {algorithm.upper():<8} | {'不可用':>11} | {'N/A':>11}")
    
    # 7.2 与其他认证方法的比较
    print("\n7.2 HMAC与其他认证方法的比较:")
    
    comparison_data = [
        {
            'method': 'HMAC',
            'security': '高',
            'speed': '高',
            'key_management': '需要安全存储密钥',
            'advantages': ['安全性高', '速度快', '实现简单', '抵抗多种攻击'],
            'disadvantages': ['需要密钥交换', '需要安全存储密钥'],
            'use_cases': ['API认证', '消息完整性', '文件验证', '双因素认证']
        },
        {
            'method': '数字签名',
            'security': '非常高',
            'speed': '中',
            'key_management': '公钥系统，私钥需要安全存储',
            'advantages': ['不可否认性', '不需要安全交换密钥'],
            'disadvantages': ['计算开销大', '实现复杂'],
            'use_cases': ['软件签名', '法律文件', '身份认证']
        },
        {
            'method': '简单哈希',
            'security': '低',
            'speed': '很高',
            'key_management': '不需要密钥',
            'advantages': ['实现简单', '速度最快'],
            'disadvantages': ['无法验证来源', '容易被篡改'],
            'use_cases': ['文件校验和', '数据去重']
        }
    ]
    
    for method_data in comparison_data:
        print(f"\n{method_data['method']}:")
        print(f"  安全性: {method_data['security']}")
        print(f"  速度: {method_data['speed']}")
        print(f"  密钥管理: {method_data['key_management']}")
        print(f"  优点: {', '.join(method_data['advantages'])}")
        print(f"  缺点: {', '.join(method_data['disadvantages'])}")
        print(f"  适用场景: {', '.join(method_data['use_cases'])}")
    
    # 7.3 性能优化建议
    print("\n7.3 HMAC性能优化建议:")
    
    print("1. 选择合适的哈希算法:")
    print("   - 对于大多数应用，SHA-256提供了良好的安全性和性能平衡")
    print("   - 对于非常高性能的场景，可以考虑BLAKE2b")
    print("   - 避免使用不安全的MD5和SHA1，即使它们速度较快")
    
    print("\n2. 消息分块处理:")
    print("   - 对于大型消息，使用增量更新方法(hmac.update)分块处理")
    print("   - 推荐的块大小为8192字节(8KB)")
    
    print("\n3. 密钥预生成和缓存:")
    print("   - 如果需要频繁生成HMAC，预生成和缓存HMAC对象")
    print("   - 只更新消息部分，避免重复创建HMAC对象")
    
    print("\n4. 并发处理:")
    print("   - 对于大量独立的HMAC计算，可以使用多线程或多进程处理")
    print("   - 注意Python的GIL限制，对于CPU密集型任务，多进程更有效")
    
    print("\n5. 批量处理:")
    print("   - 将多个小消息批量处理，减少HMAC对象创建的开销")
    
    # 7.4 优化示例
    print("\n7.4 HMAC性能优化示例:")
    
    def optimized_hmac_processing(messages, key, algorithm=hashlib.sha256):
        """
        优化的批量HMAC处理函数
        
        参数:
        - messages: 消息列表
        - key: 密钥
        - algorithm: 哈希算法
        
        返回:
        - HMAC值列表
        """
        # 预先确保密钥是字节类型
        if isinstance(key, str):
            key_bytes = key.encode('utf-8')
        else:
            key_bytes = key
        
        results = []
        
        # 为每个消息单独创建HMAC对象
        for message in messages:
            # 确保消息是字节类型
            if isinstance(message, str):
                message_bytes = message.encode('utf-8')
            else:
                message_bytes = message
            
            # 创建并计算HMAC
            hmac_obj = hmac.new(key_bytes, message_bytes, algorithm)
            results.append(hmac_obj.hexdigest())
        
        return results
    
    # 测试性能优化
    print("\n测试批量HMAC处理性能:")
    
    # 准备测试数据
    test_messages = [f"Message {i}" for i in range(1000)]
    test_key = "performance_test_key"
    
    # 测试优化函数
    start_time = time.time()
    hmac_results = optimized_hmac_processing(test_messages, test_key)
    end_time = time.time()
    
    print(f"处理1000个消息的时间: {(end_time - start_time):.6f} 秒")
    print(f"平均每个消息: {(end_time - start_time) / 1000 * 1000:.2f} 微秒")
    print(f"示例HMAC结果: {hmac_results[0]} (第一个消息)")

# 8. 总结与最佳实践

def hmac_summary():
    """
    hmac模块总结与最佳实践
    """
    print("\n=== 8. 总结与最佳实践 ===")
    
    print("HMAC模块核心功能:")
    print("1. 提供基于哈希的消息认证码，同时确保数据完整性和真实性")
    print("2. 支持多种哈希算法，包括SHA-256、SHA-512等现代安全算法")
    print("3. 提供常量时间比较方法(compare_digest)防止计时攻击")
    print("4. 支持增量更新，适合处理大型数据")
    
    print("\nHMAC应用场景:")
    print("1. API认证和授权")
    print("2. 文件完整性和真实性验证")
    print("3. 安全消息传递")
    print("4. 数据库记录完整性保护")
    print("5. 双因素认证(TOTP)")
    print("6. 安全cookie实现")
    print("7. 防止重放攻击和中间人攻击")
    
    print("\nHMAC最佳实践:")
    print("1. 密钥安全:")
    print("   - 使用强随机密钥，长度至少与哈希输出相同(SHA-256需要至少32字节)")
    print("   - 使用os.urandom()生成安全的随机密钥")
    print("   - 永远不要在代码中硬编码密钥")
    print("   - 使用密钥管理系统安全存储密钥")
    print("   - 定期轮换密钥")
    
    print("\n2. 算法选择:")
    print("   - 推荐使用SHA-256或SHA-512")
    print("   - 避免使用MD5和SHA1")
    print("   - 对于敏感应用，考虑使用SHA-3系列")
    
    print("\n3. 安全实现:")
    print("   - 总是使用hmac.compare_digest()进行HMAC比较")
    print("   - 为API请求添加时间戳防止重放攻击")
    print("   - 实现请求限流防止暴力攻击")
    print("   - 对消息内容进行适当编码(如UTF-8)后再计算HMAC")
    print("   - 包含所有相关字段进行签名，避免部分验证")
    
    print("\n4. 性能优化:")
    print("   - 对大型数据使用增量更新")
    print("   - 预生成和缓存HMAC对象")
    print("   - 对于批量处理，考虑多进程并发")
    
    print("\n5. 常见陷阱:")
    print("   - 错误的密钥编码处理导致跨平台问题")
    print("   - 使用普通字符串比较导致计时攻击")
    print("   - 忽略时间戳验证导致重放攻击")
    print("   - 签名时遗漏重要字段导致安全漏洞")
    print("   - 使用不安全的随机数生成器")

# 主函数，运行所有示例
def main():
    print("===== Python hmac模块详解 =====")
    print()
    
    # 运行各种示例
    basic_hmac_usage()
    api_authentication_example()
    file_integrity_and_authenticity()
    totp_implementation()
    security_analysis_and_best_practices()
    advanced_hmac_applications()
    hmac_performance_optimization()
    hmac_summary()
    
    print("\n===== 演示完成 =====")
    print("注意: 本示例代码仅用于教学目的，实际应用中请根据具体需求进行安全配置。")

if __name__ == "__main__":
    main()
    