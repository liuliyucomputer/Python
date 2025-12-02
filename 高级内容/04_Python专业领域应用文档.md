# Python专业领域应用文档

本文档介绍Python在各个专业领域的高级应用，包括网络安全、游戏开发、数据科学与机器学习、物联网应用等。每个领域都会提供实际的代码示例、最佳实践和相关工具库推荐。

## 1. 网络安全应用
**[标识: SECURITY-001]**

Python在网络安全领域有着广泛的应用，从简单的脚本到复杂的安全工具，Python都能胜任。本节将介绍Python在网络安全中的常见应用场景和工具。

### 1.1 网络扫描与漏洞检测

```python
# 使用Python进行基本的网络扫描

import socket
import ipaddress
import concurrent.futures
from datetime import datetime

print("=== Python网络扫描示例 ===")

# 端口扫描函数
def scan_port(ip, port):
    """扫描单个IP的指定端口"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((ip, port))
    sock.close()
    return port, result == 0

# 主机扫描函数
def scan_host(ip, start_port=1, end_port=1024, max_workers=100):
    """扫描指定IP地址的端口范围"""
    print(f"\n开始扫描 {ip}")
    print(f"扫描时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    open_ports = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_port = {executor.submit(scan_port, ip, port): port 
                         for port in range(start_port, end_port + 1)}
        
        for future in concurrent.futures.as_completed(future_to_port):
            port, is_open = future.result()
            if is_open:
                try:
                    service = socket.getservbyport(port)
                    open_ports.append((port, service))
                except:
                    open_ports.append((port, "unknown"))
    
    print(f"发现 {len(open_ports)} 个开放端口")
    for port, service in sorted(open_ports):
        print(f"端口 {port}: {service}")
    
    return open_ports

# 网络扫描函数
def scan_network(network, start_port=1, end_port=1024):
    """扫描整个网络范围"""
    try:
        ip_net = ipaddress.ip_network(network)
        print(f"扫描网络: {network} ({ip_net.num_addresses} 个IP地址)")
        
        for ip in ip_net.hosts():
            # 检查主机是否活跃
            if is_host_alive(str(ip)):
                scan_host(str(ip), start_port, end_port)
    except ValueError:
        print("无效的网络地址格式，请使用CIDR表示法，例如: 192.168.1.0/24")

def is_host_alive(ip):
    """使用简单的ping检查主机是否活跃"""
    import subprocess
    param = '-n' if subprocess.os.name == 'nt' else '-c'
    command = ['ping', param, '1', '-w', '1', ip]
    
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

# 示例使用
if __name__ == "__main__":
    # 扫描单个主机的常用端口
    scan_host("127.0.0.1", 1, 1024)
    
    # 可以取消注释下面的代码来扫描整个网络
    # scan_network("192.168.1.0/24", 1, 100)
```

### 1.2 Web安全与渗透测试

```python
# 使用Python进行简单的Web安全测试

import requests
from bs4 import BeautifulSoup
import hashlib
import re

print("=== Python Web安全测试示例 ===")

class WebSecurityTester:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def check_security_headers(self):
        """检查网站的安全响应头"""
        print("\n=== 安全响应头检查 ===")
        
        # 重要的安全响应头列表
        security_headers = {
            'Content-Security-Policy': '防止XSS和数据注入攻击',
            'X-Content-Type-Options': '防止MIME类型嗅探',
            'X-Frame-Options': '防止点击劫持攻击',
            'X-XSS-Protection': '启用浏览器XSS过滤',
            'Strict-Transport-Security': '强制使用HTTPS',
            'Referrer-Policy': '控制Referer头信息',
            'Permissions-Policy': '限制网站可以使用的功能和API'
        }
        
        try:
            response = self.session.get(self.base_url, allow_redirects=True)
            found_headers = 0
            
            print(f"目标URL: {response.url}")
            print(f"状态码: {response.status_code}")
            print("\n安全响应头检查结果:")
            
            for header, description in security_headers.items():
                if header in response.headers:
                    print(f"✓ {header}: {response.headers[header]} - {description}")
                    found_headers += 1
                else:
                    print(f"✗ {header} - {description} (缺失)")
            
            score = (found_headers / len(security_headers)) * 100
            print(f"\n安全头覆盖率: {found_headers}/{len(security_headers)} ({score:.1f}%)")
            
        except Exception as e:
            print(f"检查安全响应头时出错: {e}")
    
    def check_form_vulnerabilities(self):
        """检查表单中的常见安全漏洞"""
        print("\n=== 表单安全检查 ===")
        
        try:
            response = self.session.get(self.base_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            forms = soup.find_all('form')
            
            print(f"发现 {len(forms)} 个表单")
            
            for i, form in enumerate(forms, 1):
                print(f"\n表单 #{i}:")
                
                # 检查表单提交方法
                method = form.get('method', 'get').lower()
                action = form.get('action', '')
                
                print(f"  提交方法: {method.upper()}")
                print(f"  提交目标: {action}")
                
                # 检查是否使用HTTPS
                if 'https' not in action and action.startswith('http'):
                    print("  ⚠️  警告: 表单提交到非HTTPS地址")
                
                # 检查CSRF令牌
                csrf_token = form.find('input', {'name': re.compile(r'csrf|token|secret', re.IGNORECASE)})
                if csrf_token:
                    print(f"  ✓ 发现CSRF令牌: {csrf_token.get('name')}")
                else:
                    print("  ✗ 未发现CSRF令牌")
                
                # 检查密码字段
                password_fields = form.find_all('input', {'type': 'password'})
                for password in password_fields:
                    print(f"  密码字段: {password.get('name')}")
                    # 检查是否有autocomplete属性
                    if password.get('autocomplete') != 'off':
                        print(f"    ⚠️  警告: 密码字段未禁用自动完成")
        
        except Exception as e:
            print(f"检查表单漏洞时出错: {e}")
    
    def check_insecure_files(self):
        """检查常见的敏感文件是否可访问"""
        print("\n=== 敏感文件检查 ===")
        
        # 常见的敏感文件路径
        sensitive_files = [
            '.git/HEAD',
            'robots.txt',
            'sitemap.xml',
            '.htaccess',
            'backup.zip',
            'backup.sql',
            'config.php',
            'admin/login.php',
            'wp-admin/',
            'phpmyadmin/',
            '.env',
            'package.json'
        ]
        
        accessible_files = []
        
        for file_path in sensitive_files:
            url = f"{self.base_url}/{file_path}"
            try:
                response = self.session.get(url, allow_redirects=False, timeout=3)
                if response.status_code == 200:
                    # 计算简单的文件指纹
                    file_hash = hashlib.md5(response.content).hexdigest()[:8]
                    accessible_files.append((file_path, file_hash, len(response.content)))
            except:
                pass
        
        if accessible_files:
            print(f"发现 {len(accessible_files)} 个可能可访问的敏感文件:")
            for path, file_hash, size in accessible_files:
                print(f"  ✗ {path} - MD5: {file_hash} - {size} 字节")
        else:
            print("未发现明显的敏感文件可访问")

# 示例使用
if __name__ == "__main__":
    # 替换为要测试的网站
    tester = WebSecurityTester("https://example.com")
    tester.check_security_headers()
    tester.check_form_vulnerabilities()
    tester.check_insecure_files()
```

### 1.3 加密与解密应用

```python
# Python加密与解密应用示例

import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
import secrets

print("=== Python加密与解密应用示例 ===")

class EncryptionUtils:
    @staticmethod
    def aes_encrypt(plaintext, key):
        """使用AES-CBC模式加密数据"""
        # 确保密钥长度为16, 24或32字节
        key_bytes = key.encode('utf-8')[:32]  # 取前32字节
        key_bytes = key_bytes.ljust(32, b'\0')  # 不足32字节的话用\0填充
        
        # 生成随机IV
        iv = secrets.token_bytes(16)
        
        # 创建填充器
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext.encode('utf-8')) + padder.finalize()
        
        # 创建加密器并加密
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        # 返回IV和密文的base64编码
        return base64.b64encode(iv + ciphertext).decode('utf-8')
    
    @staticmethod
    def aes_decrypt(ciphertext_b64, key):
        """使用AES-CBC模式解密数据"""
        try:
            # 解码base64数据
            raw_data = base64.b64decode(ciphertext_b64)
            
            # 提取IV和密文
            iv = raw_data[:16]
            ciphertext = raw_data[16:]
            
            # 确保密钥长度
            key_bytes = key.encode('utf-8')[:32]
            key_bytes = key_bytes.ljust(32, b'\0')
            
            # 创建解密器并解密
            cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
            
            # 去除填充
            unpadder = padding.PKCS7(128).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
            
            return plaintext.decode('utf-8')
        except Exception as e:
            print(f"解密失败: {e}")
            return None
    
    @staticmethod
    def generate_rsa_keys(key_size=2048):
        """生成RSA密钥对"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key
    
    @staticmethod
    def rsa_encrypt(plaintext, public_key):
        """使用RSA公钥加密数据"""
        ciphertext = public_key.encrypt(
            plaintext.encode('utf-8'),
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return base64.b64encode(ciphertext).decode('utf-8')
    
    @staticmethod
    def rsa_decrypt(ciphertext_b64, private_key):
        """使用RSA私钥解密数据"""
        try:
            ciphertext = base64.b64decode(ciphertext_b64)
            plaintext = private_key.decrypt(
                ciphertext,
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return plaintext.decode('utf-8')
        except Exception as e:
            print(f"解密失败: {e}")
            return None
    
    @staticmethod
    def hash_file(file_path, algorithm='sha256'):
        """计算文件的哈希值"""
        try:
            if algorithm == 'md5':
                hash_obj = hashes.Hash(hashes.MD5(), backend=default_backend())
            elif algorithm == 'sha1':
                hash_obj = hashes.Hash(hashes.SHA1(), backend=default_backend())
            elif algorithm == 'sha256':
                hash_obj = hashes.Hash(hashes.SHA256(), backend=default_backend())
            elif algorithm == 'sha512':
                hash_obj = hashes.Hash(hashes.SHA512(), backend=default_backend())
            else:
                raise ValueError(f"不支持的哈希算法: {algorithm}")
            
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(8192)  # 8KB chunks
                    if not data:
                        break
                    hash_obj.update(data)
            
            return hash_obj.finalize().hex()
        except Exception as e:
            print(f"计算文件哈希失败: {e}")
            return None

# 演示加密解密功能
def demonstrate_encryption():
    print("\n=== AES加密演示 ===")
    
    # 准备数据和密钥
    plaintext = "这是一个需要加密的敏感信息。"
    key = "my_secure_encryption_key"
    
    print(f"原始文本: {plaintext}")
    print(f"使用的密钥: {key}")
    
    # AES加密
    encrypted = EncryptionUtils.aes_encrypt(plaintext, key)
    print(f"加密后: {encrypted}")
    
    # AES解密
    decrypted = EncryptionUtils.aes_decrypt(encrypted, key)
    print(f"解密后: {decrypted}")
    
    print("\n=== RSA加密演示 ===")
    
    # 生成RSA密钥对
    private_key, public_key = EncryptionUtils.generate_rsa_keys()
    print("已生成RSA密钥对 (2048位)")
    
    # 使用更短的文本进行RSA演示（因为RSA有明文长度限制）
    short_text = "RSA加密测试"
    print(f"原始文本: {short_text}")
    
    # RSA加密
    rsa_encrypted = EncryptionUtils.rsa_encrypt(short_text, public_key)
    print(f"加密后: {rsa_encrypted[:50]}...")  # 只显示部分密文
    
    # RSA解密
    rsa_decrypted = EncryptionUtils.rsa_decrypt(rsa_encrypted, private_key)
    print(f"解密后: {rsa_decrypted}")

# 运行演示
if __name__ == "__main__":
    demonstrate_encryption()
    
    # 注意: 以下代码需要有实际文件才能运行
    # file_hash = EncryptionUtils.hash_file("example.txt")
    # if file_hash:
    #     print(f"\n文件哈希值 (SHA-256): {file_hash}")
```

### 1.4 网络安全工具集成

```python
# Python网络安全工具集成示例

import subprocess
import json
import re
import os
from datetime import datetime

print("=== Python网络安全工具集成示例 ===")

class SecurityTools:
    def __init__(self, target):
        self.target = target
        self.results_dir = "security_results"
        
        # 确保结果目录存在
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
    
    def run_nmap_scan(self, options="-sV -sC -p 1-1000"):
        """运行Nmap扫描（需要安装Nmap）"""
        print(f"\n=== 运行Nmap扫描: {self.target} ===")
        
        try:
            # 构建Nmap命令
            cmd = f"nmap {options} {self.target}"
            print(f"执行命令: {cmd}")
            
            # 运行命令
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=300
            )
            
            # 保存结果
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.results_dir, f"nmap_scan_{timestamp}.txt")
            
            with open(output_file, "w") as f:
                f.write(result.stdout)
            
            print(f"Nmap扫描结果已保存到: {output_file}")
            
            # 解析和显示关键发现
            self._parse_nmap_results(result.stdout)
            
            return True
        except subprocess.TimeoutExpired:
            print("Nmap扫描超时")
            return False
        except Exception as e:
            print(f"Nmap扫描失败: {e}")
            return False
    
    def _parse_nmap_results(self, nmap_output):
        """解析Nmap扫描结果"""
        # 提取开放端口
        open_ports = re.findall(r'^(\d+)/(tcp|udp)\s+open\s+(\S+)', nmap_output, re.MULTILINE)
        
        if open_ports:
            print(f"\n发现 {len(open_ports)} 个开放端口:")
            for port, proto, service in open_ports:
                print(f"  - {port}/{proto}: {service}")
        else:
            print("\n未发现开放端口")
        
        # 提取操作系统信息
        os_info = re.search(r'OS details: (.+)', nmap_output)
        if os_info:
            print(f"\n操作系统信息: {os_info.group(1)}")
        
        # 提取漏洞信息或警告
        vuln_info = re.findall(r'(WARNING|VULNERABLE).*', nmap_output)
        if vuln_info:
            print(f"\n发现 {len(vuln_info)} 个警告或漏洞")
    
    def run_sqlmap(self, url, options="--batch --level=1 --risk=1"):
        """运行SQLMap扫描（需要安装SQLMap）"""
        print(f"\n=== 运行SQLMap扫描: {url} ===")
        
        try:
            # 构建SQLMap命令
            cmd = f"sqlmap -u {url} {options}"
            print(f"执行命令: {cmd}")
            
            # 运行命令
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=600
            )
            
            # 保存结果
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(self.results_dir, f"sqlmap_scan_{timestamp}.txt")
            
            with open(output_file, "w") as f:
                f.write(result.stdout)
            
            print(f"SQLMap扫描结果已保存到: {output_file}")
            
            # 检查是否发现注入点
            if "all tested parameters do not appear to be injectable" in result.stdout:
                print("未发现SQL注入漏洞")
            elif "injection point" in result.stdout.lower():
                print("发现潜在的SQL注入漏洞！")
            
            return True
        except subprocess.TimeoutExpired:
            print("SQLMap扫描超时")
            return False
        except Exception as e:
            print(f"SQLMap扫描失败: {e}")
            return False
    
    def run_sslyze(self, port=443):
        """运行SSLyze检查SSL/TLS配置（需要安装SSLyze）"""
        print(f"\n=== 运行SSLyze检查: {self.target}:{port} ===")
        
        try:
            # 构建SSLyze命令
            cmd = f"sslyze --json_out=- {self.target}:{port}"
            print(f"执行命令: {cmd}")
            
            # 运行命令
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=300
            )
            
            # 保存原始结果
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            text_output_file = os.path.join(self.results_dir, f"sslyze_scan_{timestamp}.txt")
            
            with open(text_output_file, "w") as f:
                f.write(result.stdout)
            
            # 解析JSON结果
            try:
                json_result = json.loads(result.stdout)
                
                # 保存格式化的JSON
                json_output_file = os.path.join(self.results_dir, f"sslyze_scan_{timestamp}.json")
                with open(json_output_file, "w") as f:
                    json.dump(json_result, f, indent=2)
                
                print(f"SSLyze扫描结果已保存到: {json_output_file}")
                
                # 显示基本SSL/TLS信息
                self._parse_sslyze_results(json_result)
                
            except json.JSONDecodeError:
                print("无法解析SSLyze的JSON输出")
            
            return True
        except subprocess.TimeoutExpired:
            print("SSLyze扫描超时")
            return False
        except Exception as e:
            print(f"SSLyze扫描失败: {e}")
            return False
    
    def _parse_sslyze_results(self, json_result):
        """解析SSLyze JSON结果"""
        try:
            # 提取证书信息
            cert_info = json_result.get('server_certificate', {}).get('certificate_deployment', {})
            if cert_info:
                subject = cert_info.get('subject', {})
                print(f"\nSSL证书信息:")
                print(f"  通用名称: {subject.get('common_name', 'N/A')}")
                print(f"  颁发者: {cert_info.get('issuer', {}).get('common_name', 'N/A')}")
            
            # 检查SSL/TLS漏洞
            vulnerabilities = json_result.get('vulnerabilities', {})
            print(f"\nSSL/TLS漏洞检查:")
            
            # 检查常见漏洞
            common_vulns = {
                'heartbleed': 'Heartbleed',
                'robot': 'ROBOT',
                'beast': 'BEAST',
                'poodle': 'POODLE'
            }
            
            for vuln_key, vuln_name in common_vulns.items():
                vuln_info = vulnerabilities.get(vuln_key, {})
                if isinstance(vuln_info, dict):
                    is_vulnerable = vuln_info.get('is_vulnerable', False)
                    print(f"  {vuln_name}: {'易受攻击' if is_vulnerable else '安全'}")
        except Exception:
            print("无法解析SSL/TLS信息")
    
    def generate_security_report(self):
        """生成安全扫描汇总报告"""
        print("\n=== 生成安全扫描汇总报告 ===")
        
        report = {
            'target': self.target,
            'scan_date': datetime.now().isoformat(),
            'summary': {
                'nmap_scans': 0,
                'sqlmap_scans': 0,
                'sslyze_scans': 0,
                'potential_vulnerabilities': 0
            }
        }
        
        # 统计扫描文件
        for filename in os.listdir(self.results_dir):
            if filename.startswith('nmap_scan_'):
                report['summary']['nmap_scans'] += 1
            elif filename.startswith('sqlmap_scan_'):
                report['summary']['sqlmap_scans'] += 1
            elif filename.startswith('sslyze_scan_'):
                report['summary']['sslyze_scans'] += 1
        
        # 保存报告
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = os.path.join(self.results_dir, f"security_report_{timestamp}.json")
        
        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)
        
        print(f"安全扫描报告已生成: {report_file}")
        print("\n扫描统计:")
        print(f"  Nmap扫描次数: {report['summary']['nmap_scans']}")
        print(f"  SQLMap扫描次数: {report['summary']['sqlmap_scans']}")
        print(f"  SSLyze扫描次数: {report['summary']['sslyze_scans']}")

# 演示使用
def demonstrate_security_tools():
    # 设置目标（在实际使用中替换为真实目标）
    target = "example.com"
    
    # 初始化安全工具
    tools = SecurityTools(target)
    
    print(f"开始对目标 {target} 进行安全扫描")
    
    # 注意: 以下扫描需要安装相应工具，且在扫描非授权目标前请获得许可
    
    # 运行Nmap扫描（简单端口扫描）
    # tools.run_nmap_scan("-p 80,443")  # 只扫描常用Web端口
    
    # 运行SQLMap扫描
    # tools.run_sqlmap(f"https://{target}/?id=1")  # 假设有一个带参数的URL
    
    # 运行SSLyze检查
    # tools.run_sslyze()
    
    # 生成报告
    tools.generate_security_report()
    
    print("\n安全工具演示完成。注意：在实际环境中使用这些工具前请确保获得适当授权。")

if __name__ == "__main__":
    demonstrate_security_tools()
```

### 1.5 网络安全最佳实践

**[标识: SECURITY-BEST-PRACTICES-001]**

1. **输入验证与净化**
   - 始终验证和净化所有用户输入
   - 使用参数化查询防止SQL注入
   - 实施内容安全策略(CSP)防止XSS攻击

2. **认证与授权**
   - 使用强密码哈希算法(如bcrypt, Argon2)
   - 实施多因素认证(MFA)
   - 遵循最小权限原则

3. **安全通信**
   - 始终使用TLS 1.2+加密传输
   - 适当配置SSL/TLS参数和密码套件
   - 实施证书固定(Certificate Pinning)

4. **安全编码**
   - 避免使用不安全的函数和库
   - 定期更新依赖项修复安全漏洞
   - 使用静态代码分析工具检查安全问题

5. **日志与监控**
   - 记录所有安全相关事件
   - 监控异常行为和攻击尝试
   - 定期审计和分析日志

6. **应急响应**
   - 制定安全事件响应计划
   - 定期进行安全演练
   - 建立漏洞披露和修复流程

## 2. 游戏开发应用
**[标识: GAME-DEV-001]**

Python在游戏开发领域也有广泛应用，从简单的2D游戏到复杂的3D游戏原型，Python都能胜任。本节将介绍Python游戏开发的常用框架和技术。

### 2.1 Pygame游戏开发

```python
# Pygame基础游戏开发示例

import pygame
import sys
import random

print("=== Pygame基础游戏开发示例 ===")

# 初始化Pygame
pygame.init()

# 确保中文正常显示
pygame.font.init()
try:
    font = pygame.font.Font("simhei.ttf", 24)  # 尝试加载中文字体
    print("成功加载中文字体")
except:
    # 如果无法加载指定字体，使用系统默认字体
    font = pygame.font.SysFont(None, 24)
    print("使用系统默认字体")

# 游戏常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 创建游戏窗口
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python游戏开发示例")
clock = pygame.time.Clock()

# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 创建一个简单的玩家图形
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.health = 100
    
    def update(self):
        # 获取按键状态
        keys = pygame.key.get_pressed()
        
        # 移动玩家
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed
    
    def draw_health_bar(self, surface):
        # 绘制血条
        bar_length = 100
        bar_height = 10
        fill = (self.health / 100) * bar_length
        
        # 血条背景
        pygame.draw.rect(surface, RED, (self.rect.x, self.rect.y - 20, bar_length, bar_height))
        # 血条填充
        pygame.draw.rect(surface, GREEN, (self.rect.x, self.rect.y - 20, fill, bar_height))

# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 创建一个简单的敌人图形
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
        # 随机生成敌人位置
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 4)
        self.speedx = random.randrange(-2, 2)
    
    def update(self):
        # 移动敌人
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # 如果敌人移出屏幕，重新放置到顶部
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 25:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # 创建一个简单的子弹图形
        self.image = pygame.Surface((10, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
    
    def update(self):
        # 向上移动子弹
        self.rect.y += self.speedy
        # 如果子弹移出屏幕顶部，删除它
        if self.rect.bottom < 0:
            self.kill()

# 爆炸效果类
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.size = 50
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50  # 更新频率
        self.radius = 5
        self.max_radius = self.size // 2
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.radius += 3
            if self.radius > self.max_radius:
                self.kill()
            else:
                # 更新爆炸效果
                self.image = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
                pygame.draw.circle(self.image, YELLOW, (self.size//2, self.size//2), self.radius)

# 初始化精灵组
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

# 创建玩家
player = Player()
all_sprites.add(player)

# 创建敌人
for i in range(8):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# 游戏变量
score = 0
game_over = False

# 游戏主循环
def game_loop():
    global score, game_over
    
    # 游戏主循环
    running = True
    while running:
        # 保持循环以正确的速度运行
        clock.tick(FPS)
        
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    # 创建子弹
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                elif event.key == pygame.K_r and game_over:
                    # 重新开始游戏
                    restart_game()
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        if not game_over:
            # 更新所有精灵
            all_sprites.update()
            
            # 检测子弹和敌人的碰撞
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                score += 10
                # 创建爆炸效果
                explosion = Explosion(hit.rect.center)
                all_sprites.add(explosion)
                # 创建新敌人
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)
            
            # 检测敌人和玩家的碰撞
            hits = pygame.sprite.spritecollide(player, enemies, True)
            for hit in hits:
                player.health -= 25
                # 创建爆炸效果
                explosion = Explosion(hit.rect.center)
                all_sprites.add(explosion)
                # 创建新敌人
                enemy = Enemy()
                all_sprites.add(enemy)
                enemies.add(enemy)
                
                if player.health <= 0:
                    game_over = True
        
        # 绘制
        screen.fill(BLACK)
        all_sprites.draw(screen)
        
        # 绘制分数
        score_text = font.render(f"分数: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # 绘制玩家血条
        player.draw_health_bar(screen)
        
        # 绘制游戏结束画面
        if game_over:
            # 创建半透明覆盖层
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))
            screen.blit(overlay, (0, 0))
            
            # 绘制游戏结束文本
            game_over_text = font.render("游戏结束!", True, RED)
            restart_text = font.render("按R键重新开始", True, WHITE)
            quit_text = font.render("按ESC键退出", True, WHITE)
            
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2))
            screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        
        # 更新屏幕
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

def restart_game():
    global score, game_over, player, all_sprites, enemies, bullets
    
    # 重置游戏状态
    score = 0
    game_over = False
    
    # 清空所有精灵组
    all_sprites.empty()
    enemies.empty()
    bullets.empty()
    
    # 重新创建玩家
    player = Player()
    all_sprites.add(player)
    
    # 重新创建敌人
    for i in range(8):
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

# 启动游戏
if __name__ == "__main__":
    print("游戏启动中...")
    print("操作说明:")
    print("- 使用方向键移动玩家")
    print("- 按空格键发射子弹")
    print("- 游戏结束后按R键重新开始")
    print("- 按ESC键退出游戏")
    game_loop()
```

### 2.2 Pyglet 3D游戏开发

```python
# Pyglet 3D游戏开发基础示例

import pyglet
from pyglet.gl import *
import math
import numpy as np

print("=== Pyglet 3D游戏开发基础示例 ===")

class Game3D:
    def __init__(self):
        # 创建窗口
        self.window = pyglet.window.Window(800, 600, caption='Python 3D游戏开发示例')
        
        # 设置OpenGL
        self.setup_opengl()
        
        # 相机参数
        self.camera_x = 0
        self.camera_y = 0
        self.camera_z = 5
        self.camera_rotation_x = 0
        self.camera_rotation_y = 0
        
        # 游戏对象
        self.cube_position = [0, 0, 0]
        self.cube_rotation = [0, 0, 0]
        
        # 键盘状态
        self.keys = set()
        
        # 注册事件处理
        self.window.push_handlers(
            on_draw=self.on_draw,
            on_resize=self.on_resize,
            on_key_press=self.on_key_press,
            on_key_release=self.on_key_release
        )
        
        # 调度更新
        pyglet.clock.schedule_interval(self.update, 1/60.0)
    
    def setup_opengl(self):
        # 启用深度测试
        glEnable(GL_DEPTH_TEST)
        # 设置背景颜色
        glClearColor(0.1, 0.1, 0.2, 1.0)
    
    def on_resize(self, width, height):
        # 设置视口
        glViewport(0, 0, width, height)
        
        # 设置投影矩阵
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspect_ratio = width / float(height)
        gluPerspective(60.0, aspect_ratio, 0.1, 1000.0)
        
        # 切换回模型视图矩阵
        glMatrixMode(GL_MODELVIEW)
        return pyglet.event.EVENT_HANDLED
    
    def on_key_press(self, symbol, modifiers):
        # 记录按键状态
        self.keys.add(symbol)
        
        # ESC键退出
        if symbol == pyglet.window.key.ESCAPE:
            self.window.close()
    
    def on_key_release(self, symbol, modifiers):
        # 移除按键状态
        if symbol in self.keys:
            self.keys.remove(symbol)
    
    def update(self, dt):
        # 更新立方体旋转
        self.cube_rotation[0] += 10 * dt
        self.cube_rotation[1] += 15 * dt
        self.cube_rotation[2] += 5 * dt
        
        # 处理相机移动
        camera_speed = 3.0 * dt
        rotation_speed = 90.0 * dt
        
        # 计算相机方向
        rad_y = math.radians(self.camera_rotation_y)
        
        if pyglet.window.key.W in self.keys:
            # 向前移动
            self.camera_x += math.sin(rad_y) * camera_speed
            self.camera_z -= math.cos(rad_y) * camera_speed
        if pyglet.window.key.S in self.keys:
            # 向后移动
            self.camera_x -= math.sin(rad_y) * camera_speed
            self.camera_z += math.cos(rad_y) * camera_speed
        if pyglet.window.key.A in self.keys:
            # 向左移动
            self.camera_x -= math.cos(rad_y) * camera_speed
            self.camera_z -= math.sin(rad_y) * camera_speed
        if pyglet.window.key.D in self.keys:
            # 向右移动
            self.camera_x += math.cos(rad_y) * camera_speed
            self.camera_z += math.sin(rad_y) * camera_speed
        if pyglet.window.key.SPACE in self.keys:
            # 向上移动
            self.camera_y += camera_speed
        if pyglet.window.key.LSHIFT in self.keys:
            # 向下移动
            self.camera_y -= camera_speed
        if pyglet.window.key.LEFT in self.keys:
            # 向左旋转
            self.camera_rotation_y -= rotation_speed
        if pyglet.window.key.RIGHT in self.keys:
            # 向右旋转
            self.camera_rotation_y += rotation_speed
        if pyglet.window.key.UP in self.keys:
            # 向上旋转
            self.camera_rotation_x -= rotation_speed
            # 限制垂直旋转角度
            self.camera_rotation_x = max(-85, min(85, self.camera_rotation_x))
        if pyglet.window.key.DOWN in self.keys:
            # 向下旋转
            self.camera_rotation_x += rotation_speed
            # 限制垂直旋转角度
            self.camera_rotation_x = max(-85, min(85, self.camera_rotation_x))
    
    def on_draw(self):
        # 清空屏幕
        self.window.clear()
        
        # 重置模型视图矩阵
        glLoadIdentity()
        
        # 设置相机位置和旋转
        glRotatef(self.camera_rotation_x, 1, 0, 0)  # X轴旋转
        glRotatef(self.camera_rotation_y, 0, 1, 0)  # Y轴旋转
        glTranslatef(-self.camera_x, -self.camera_y, -self.camera_z)  # 移动相机
        
        # 绘制网格地面
        self.draw_grid()
        
        # 绘制立方体
        self.draw_cube()
        
        # 绘制坐标轴
        self.draw_axes()
    
    def draw_grid(self):
        # 绘制地面网格
        glBegin(GL_LINES)
        glColor3f(0.3, 0.3, 0.3)  # 网格颜色
        
        # 绘制水平线
        for i in range(-10, 11):
            glVertex3f(-10, 0, i)
            glVertex3f(10, 0, i)
            glVertex3f(i, 0, -10)
            glVertex3f(i, 0, 10)
        glEnd()
        
        # 绘制原点
        glPointSize(5)
        glBegin(GL_POINTS)
        glColor3f(1, 1, 1)  # 白色
        glVertex3f(0, 0, 0)
        glEnd()
    
    def draw_cube(self):
        # 保存当前矩阵
        glPushMatrix()
        
        # 移动到立方体位置
        glTranslatef(self.cube_position[0], self.cube_position[1], self.cube_position[2])
        
        # 应用旋转
        glRotatef(self.cube_rotation[0], 1, 0, 0)
        glRotatef(self.cube_rotation[1], 0, 1, 0)
        glRotatef(self.cube_rotation[2], 0, 0, 1)
        
        # 绘制彩色立方体
        glBegin(GL_QUADS)
        
        # 前面 (红色)
        glColor3f(1, 0, 0)
        glVertex3f(-1, -1, 1)
        glVertex3f(1, -1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(-1, 1, 1)
        
        # 后面 (绿色)
        glColor3f(0, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, 1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, -1, -1)
        
        # 上面 (蓝色)
        glColor3f(0, 0, 1)
        glVertex3f(-1, 1, -1)
        glVertex3f(-1, 1, 1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, 1, -1)
        
        # 下面 (黄色)
        glColor3f(1, 1, 0)
        glVertex3f(-1, -1, -1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, -1, 1)
        glVertex3f(-1, -1, 1)
        
        # 右面 (品红)
        glColor3f(1, 0, 1)
        glVertex3f(1, -1, -1)
        glVertex3f(1, 1, -1)
        glVertex3f(1, 1, 1)
        glVertex3f(1, -1, 1)
        
        # 左面 (青色)
        glColor3f(0, 1, 1)
        glVertex3f(-1, -1, -1)
        glVertex3f(-1, -1, 1)
        glVertex3f(-1, 1, 1)
        glVertex3f(-1, 1, -1)
        
        glEnd()
        
        # 恢复之前的矩阵
        glPopMatrix()
    
    def draw_axes(self):
        # 绘制坐标轴
        glBegin(GL_LINES)
        
        # X轴 (红色)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(2, 0, 0)
        
        # Y轴 (绿色)
        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 2, 0)
        
        # Z轴 (蓝色)
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 2)
        
        glEnd()
    
    def run(self):
        # 启动游戏主循环
        print("3D游戏已启动!")
        print("操作说明:")
        print("- W/A/S/D: 前后左右移动")
        print("- 空格键: 向上移动")
        print("- Shift键: 向下移动")
        print("- 方向键: 旋转视角")
        print("- ESC键: 退出游戏")
        
        pyglet.app.run()

# 启动游戏
if __name__ == "__main__":
    try:
        game = Game3D()
        game.run()
    except Exception as e:
        print(f"游戏运行出错: {e}")
```

### 2.3 游戏物理引擎应用

```python
# Pymunk物理引擎游戏开发示例

import pygame
import pymunk
import pymunk.pygame_util
import sys
import random

print("=== Pymunk物理引擎游戏开发示例 ===")

# 初始化pygame
pygame.init()

# 确保中文正常显示
pygame.font.init()
try:
    font = pygame.font.Font("simhei.ttf", 24)  # 尝试加载中文字体
except:
    font = pygame.font.SysFont(None, 24)  # 使用系统默认字体

# 游戏常量
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

class PhysicsGame:
    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Python物理引擎游戏示例")
        self.clock = pygame.time.Clock()
        
        # 初始化物理空间
        self.space = pymunk.Space()
        self.space.gravity = (0, 900)  # 设置重力
        
        # 初始化pygame绘图工具
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        
        # 游戏变量
        self.is_dragging = False
        self.drag_body = None
        self.drag_joint = None
        self.shape_to_remove = None
        self.score = 0
        self.objects_count = 0
        
        # 创建边界和地面
        self.create_boundaries()
        
        # 创建一些初始物体
        self.create_figures()
        
        # 鼠标事件
        self.mouse_joint = None
        self.pressed_pos = None
        
        # 记录按键状态
        self.keys = set()
        
        # 游戏主循环
        self.running = True
    
    def create_boundaries(self):
        """创建游戏边界和地面"""
        # 墙壁厚度
        thickness = 20
        
        # 创建地面
        ground = pymunk.Segment(self.space.static_body, (0, SCREEN_HEIGHT-thickness), (SCREEN_WIDTH, SCREEN_HEIGHT-thickness), thickness)
        ground.friction = 1.0
        ground.elasticity = 0.8
        self.space.add(ground)
        
        # 创建左右墙壁
        left_wall = pymunk.Segment(self.space.static_body, (thickness, 0), (thickness, SCREEN_HEIGHT), thickness)
        right_wall = pymunk.Segment(self.space.static_body, (SCREEN_WIDTH-thickness, 0), (SCREEN_WIDTH-thickness, SCREEN_HEIGHT), thickness)
        
        left_wall.friction = 1.0
        left_wall.elasticity = 0.8
        right_wall.friction = 1.0
        right_wall.elasticity = 0.8
        
        self.space.add(left_wall, right_wall)
        
        # 创建天花板
        ceiling = pymunk.Segment(self.space.static_body, (0, thickness), (SCREEN_WIDTH, thickness), thickness)
        ceiling.friction = 1.0
        ceiling.elasticity = 0.8
        self.space.add(ceiling)
        
        # 创建一些静态障碍物
        self.create_obstacles()
    
    def create_obstacles(self):
        """创建静态障碍物"""
        # 创建一个斜面
        points = [(100, SCREEN_HEIGHT-100), (250, SCREEN_HEIGHT-250), (250, SCREEN_HEIGHT-200), (100, SCREEN_HEIGHT-50)]
        obstacle = pymunk.Poly(self.space.static_body, points)
        obstacle.friction = 0.5
        obstacle.elasticity = 0.3
        self.space.add(obstacle)
        
        # 创建一个静态圆圈
        circle = pymunk.Circle(self.space.static_body, 40, (SCREEN_WIDTH-200, SCREEN_HEIGHT-300))
        circle.friction = 0.5
        circle.elasticity = 0.8
        self.space.add(circle)
        
        # 创建一个静态矩形
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = (SCREEN_WIDTH/2, SCREEN_HEIGHT-400)
        shape = pymunk.Poly.create_box(body, (100, 20))
        shape.friction = 0.5
        shape.elasticity = 0.8
        self.space.add(body, shape)
    
    def create_figures(self):
        """创建一些初始的物理物体"""
        # 创建一些不同形状的物体
        for _ in range(5):
            self.create_random_object()
    
    def create_random_object(self, pos=None):
        """创建随机物体"""
        if pos is None:
            pos = (random.randint(100, SCREEN_WIDTH-100), random.randint(50, 200))
        
        # 随机选择物体类型
        obj_type = random.randint(0, 2)
        
        if obj_type == 0:  # 圆形
            radius = random.randint(10, 30)
            mass = radius  # 质量与大小成正比
            inertia = pymunk.moment_for_circle(mass, 0, radius)
            body = pymunk.Body(mass, inertia)
            body.position = pos
            shape = pymunk.Circle(body, radius)
        
        elif obj_type == 1:  # 矩形
            width = random.randint(20, 50)
            height = random.randint(20, 50)
            mass = width * height / 100  # 质量与面积成正比
            inertia = pymunk.moment_for_box(mass, (width, height))
            body = pymunk.Body(mass, inertia)
            body.position = pos
            shape = pymunk.Poly.create_box(body, (width, height))
        
        else:  # 多边形
            num_vertices = random.randint(3, 6)
            radius = random.randint(20, 40)
            vertices = []
            for i in range(num_vertices):
                angle = 2 * 3.14159 * i / num_vertices
                x = radius * random.uniform(0.8, 1.0) * random.choice([-1, 1]) * abs(math.cos(angle))
                y = radius * random.uniform(0.8, 1.0) * random.choice([-1, 1]) * abs(math.sin(angle))
                vertices.append((x, y))
            
            mass = radius  # 简化质量计算
            inertia = pymunk.moment_for_poly(mass, vertices)
            body = pymunk.Body(mass, inertia)
            body.position = pos
            shape = pymunk.Poly(body, vertices)
        
        # 设置物体属性
        shape.friction = random.uniform(0.3, 0.8)
        shape.elasticity = random.uniform(0.1, 0.8)
        
        # 随机颜色
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        shape.color = color + (255,)
        
        # 添加到空间
        self.space.add(body, shape)
        self.objects_count += 1
        
        return shape
    
    def handle_events(self):
        """处理游戏事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                self.keys.add(event.key)
                
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE:
                    # 空格键添加新物体
                    self.create_random_object()
                elif event.key == pygame.K_r:
                    # R键重置游戏
                    self.reset_game()
                elif event.key == pygame.K_c:
                    # C键清除所有物体
                    self.clear_objects()
            
            elif event.type == pygame.KEYUP:
                if event.key in self.keys:
                    self.keys.remove(event.key)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左键点击
                    self.handle_mouse_down(event.pos)
                elif event.button == 3:  # 右键点击
                    self.handle_right_mouse_down(event.pos)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # 左键释放
                    self.handle_mouse_up()
            
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_motion(event.pos)
    
    def handle_mouse_down(self, pos):
        """处理鼠标按下事件"""
        # 检查是否点击到物体
        shape = self.space.point_query_nearest(pos, 0, pymunk.ShapeFilter())
        if shape:
            # 创建鼠标关节来拖动物体
            body = shape.shape.body
            self.pressed_pos = pymunk.Vec2d(*pos)
            self.drag_body = body
            
            # 创建一个销关节将物体连接到鼠标位置
            pivot_joint = pymunk.PivotJoint(
                self.space.static_body, body, self.pressed_pos, body.world_to_local(self.pressed_pos)
            )
            pivot_joint.max_bias = 0  # 禁用矫正
            pivot_joint.max_force = 10000  # 很大的力来移动物体
            self.space.add(pivot_joint)
            self.mouse_joint = pivot_joint
    
    def handle_right_mouse_down(self, pos):
        """处理右键点击事件 - 移除物体"""
        shape = self.space.point_query_nearest(pos, 0, pymunk.ShapeFilter())
        if shape and not isinstance(shape.shape.body, pymunk.Body) or shape.shape.body.body_type != pymunk.Body.STATIC:
            self.shape_to_remove = shape.shape
    
    def handle_mouse_up(self):
        """处理鼠标释放事件"""
        if self.mouse_joint:
            self.space.remove(self.mouse_joint)
            self.mouse_joint = None
        self.drag_body = None
        self.pressed_pos = None
    
    def handle_mouse_motion(self, pos):
        """处理鼠标移动事件"""
        if self.mouse_joint and self.pressed_pos:
            # 更新鼠标关节的锚点
            self.mouse_joint.anchor_a = pymunk.Vec2d(*pos)
    
    def update_physics(self, dt):
        """更新物理状态"""
        # 移除标记为删除的物体
        if self.shape_to_remove:
            body = self.shape_to_remove.body
            self.space.remove(self.shape_to_remove, body)
            self.shape_to_remove = None
            self.objects_count -= 1
            self.score += 1  # 每移除一个物体加1分
        
        # 步进物理模拟
        self.space.step(dt)
        
        # 添加随机力或扭矩
        if pygame.K_f in self.keys:
            # 为所有物体添加随机力
            for shape in self.space.shapes:
                if hasattr(shape, 'body') and shape.body.body_type == pymunk.Body.DYNAMIC:
                    force = (random.randint(-1000, 1000), random.randint(-1000, 1000))
                    shape.body.apply_force_at_local_point(force, (0, 0))
        
        # 持续生成物体
        if pygame.K_g in self.keys:
            if random.random() < 0.1:  # 10%概率生成物体
                self.create_random_object()
    
