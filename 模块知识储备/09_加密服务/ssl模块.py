#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ssl模块 - SSL/TLS加密通信

ssl模块提供了对SSL/TLS协议的支持，
用于创建安全的加密通信通道。

主要功能包括：
- 创建SSL/TLS套接字
- 配置SSL上下文
- 证书验证和管理
- 安全HTTP通信(HTTPS)

使用场景：
- 安全网络通信
- 加密数据传输
- 保护敏感信息
- 创建HTTPS服务器
- 验证服务器证书
"""

import ssl
import socket
import http.client
import urllib.request
import os
import tempfile

# ===========================
# 1. 基本介绍
# ===========================
print("=" * 50)
print("1. ssl模块基本介绍")
print("=" * 50)
print("ssl模块提供了对SSL/TLS协议的支持")
print("用于创建安全的加密通信通道")
print("支持多种SSL/TLS版本和加密算法")
print("提供证书验证和管理功能")

# ===========================
# 2. SSL/TLS协议概述
# ===========================
print("\n" + "=" * 50)
print("2. SSL/TLS协议概述")
print("=" * 50)
print("SSL/TLS协议版本:")
print("- SSL 2.0 (已废弃)")
print("- SSL 3.0 (已废弃)")
print("- TLS 1.0 (不推荐使用)")
print("- TLS 1.1 (不推荐使用)")
print("- TLS 1.2 (推荐使用)")
print("- TLS 1.3 (最新版本，推荐使用)")

print("\nSSL/TLS工作原理:")
print("1. 握手阶段: 协商加密算法和密钥")
print("2. 证书验证: 验证服务器身份")
print("3. 加密通信: 使用协商的密钥加密数据")
print("4. 连接关闭: 安全关闭连接")

# ===========================
# 3. SSL上下文
# ===========================
print("\n" + "=" * 50)
print("3. SSL上下文")
print("=" * 50)

# 创建SSL上下文
def create_ssl_context(protocol=ssl.PROTOCOL_TLS_CLIENT):
    """创建SSL上下文"""
    ctx = ssl.create_default_context(protocol)
    return ctx

# 配置SSL上下文
def configure_ssl_context(ctx):
    """配置SSL上下文"""
    # 设置最低和最高协议版本
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.maximum_version = ssl.TLSVersion.TLSv1_3
    
    # 配置密码套件（加密算法组合）
    ctx.set_ciphers('ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384')
    
    # 启用证书验证
    ctx.verify_mode = ssl.CERT_REQUIRED
    
    # 加载系统默认的证书颁发机构(CA)证书
    ctx.load_default_certs()
    
    return ctx

# 演示SSL上下文
print("演示SSL上下文的创建和配置:")

# 创建SSL上下文
ctx = create_ssl_context()
print(f"默认SSL上下文: {ctx}")
print(f"默认协议版本: {ctx.protocol}")

# 配置SSL上下文
configured_ctx = configure_ssl_context(ctx)
print(f"\n配置后的SSL上下文:")
print(f"最低协议版本: {configured_ctx.minimum_version}")
print(f"最高协议版本: {configured_ctx.maximum_version}")
print(f"证书验证模式: {configured_ctx.verify_mode}")

# ===========================
# 4. HTTPS客户端示例
# ===========================
print("\n" + "=" * 50)
print("4. HTTPS客户端示例")
print("=" * 50)

# 使用http.client进行HTTPS请求
def https_request_httpclient(host, path="/"):
    """使用http.client进行HTTPS请求"""
    # 创建HTTPS连接
    conn = http.client.HTTPSConnection(host)
    
    # 发送请求
    conn.request("GET", path)
    
    # 获取响应
    response = conn.getresponse()
    
    # 读取响应数据
    data = response.read()
    
    # 关闭连接
    conn.close()
    
    return response.status, data

# 使用urllib进行HTTPS请求
def https_request_urllib(url):
    """使用urllib进行HTTPS请求"""
    # 创建SSL上下文
    ctx = ssl.create_default_context()
    
    # 创建请求对象
    req = urllib.request.Request(url)
    
    # 发送请求
    with urllib.request.urlopen(req, context=ctx) as response:
        # 读取响应数据
        data = response.read()
        
        return response.status, data

# 演示HTTPS请求
print("演示HTTPS请求:")

# 尝试发送HTTPS请求
# 注意：实际运行时需要网络连接
try:
    print("\n使用http.client访问https://www.baidu.com:")
    status, data = https_request_httpclient("www.baidu.com")
    print(f"状态码: {status}")
    print(f"响应长度: {len(data)} 字节")
    print(f"响应前500字节: {data[:500].decode('utf-8', errors='ignore')}")
except Exception as e:
    print(f"请求失败: {e}")

# ===========================
# 5. SSL套接字
# ===========================
print("\n" + "=" * 50)
print("5. SSL套接字")
print("=" * 50)

# 创建SSL客户端套接字
def create_ssl_socket(host, port):
    """创建SSL客户端套接字"""
    # 创建普通套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 创建SSL上下文
    ctx = ssl.create_default_context()
    
    # 包装套接字为SSL套接字
    ssl_sock = ctx.wrap_socket(sock, server_hostname=host)
    
    return ssl_sock

# 演示SSL套接字
print("演示SSL套接字的创建:")

# 尝试创建SSL套接字连接到服务器
try:
    print("\n创建SSL套接字连接到www.baidu.com:443:")
    ssl_sock = create_ssl_socket("www.baidu.com", 443)
    
    # 连接到服务器
    ssl_sock.connect(("www.baidu.com", 443))
    print(f"成功连接到服务器")
    
    # 获取对等证书信息
    cert = ssl_sock.getpeercert()
    print(f"服务器证书信息: {cert['subject'][0][0][1]}")
    
    # 发送HTTPS请求
    request = "GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n"
    ssl_sock.send(request.encode())
    
    # 接收响应
    response = ssl_sock.recv(4096)
    print(f"响应前500字节: {response[:500].decode('utf-8', errors='ignore')}")
    
    # 关闭套接字
    ssl_sock.close()
except Exception as e:
    print(f"SSL套接字操作失败: {e}")

# ===========================
# 6. 证书验证
# ===========================
print("\n" + "=" * 50)
print("6. 证书验证")
print("=" * 50)

# 证书验证级别
print("证书验证级别:")
print(f"- CERT_NONE: {ssl.CERT_NONE} (不验证证书)")
print(f"- CERT_OPTIONAL: {ssl.CERT_OPTIONAL} (可选验证)")
print(f"- CERT_REQUIRED: {ssl.CERT_REQUIRED} (必须验证)")

# 验证证书主机名
def verify_cert_hostname(cert, hostname):
    """验证证书是否匹配主机名"""
    try:
        # 使用ssl.match_hostname验证证书主机名
        ssl.match_hostname(cert, hostname)
        return True
    except ssl.CertificateError:
        return False

# 演示证书验证
try:
    print("\n演示证书验证:")
    
    # 创建SSL套接字连接到服务器
    ssl_sock = create_ssl_socket("www.baidu.com", 443)
    ssl_sock.connect(("www.baidu.com", 443))
    
    # 获取对等证书
    cert = ssl_sock.getpeercert()
    
    # 验证证书主机名
    is_valid = verify_cert_hostname(cert, "www.baidu.com")
    print(f"证书主机名验证结果: {'有效' if is_valid else '无效'}")
    
    # 验证错误的主机名
    is_invalid = verify_cert_hostname(cert, "www.example.com")
    print(f"错误主机名验证结果: {'有效' if is_invalid else '无效'}")
    
    ssl_sock.close()
except Exception as e:
    print(f"证书验证演示失败: {e}")

# ===========================
# 7. 创建自签名证书
# ===========================
print("\n" + "=" * 50)
print("7. 创建自签名证书")
print("=" * 50)

# 创建临时自签名证书
# 注意：实际应用中应使用正式CA颁发的证书
def create_self_signed_cert():
    """创建自签名证书（演示用，实际应使用OpenSSL或其他工具）"""
    # 这里我们只是创建临时文件，实际证书需要使用OpenSSL生成
    # 在实际应用中，可以使用以下命令生成自签名证书：
    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    
    # 创建临时文件
    cert_fd, cert_path = tempfile.mkstemp(suffix=".pem")
    key_fd, key_path = tempfile.mkstemp(suffix=".pem")
    
    # 关闭文件描述符
    os.close(cert_fd)
    os.close(key_fd)
    
    return cert_path, key_path

# 演示自签名证书创建
print("演示自签名证书创建:")
cert_path, key_path = create_self_signed_cert()
print(f"创建临时证书文件: {cert_path}")
print(f"创建临时密钥文件: {key_path}")

# 清理临时文件
os.unlink(cert_path)
os.unlink(key_path)

# ===========================
# 8. SSL服务器示例
# ===========================
print("\n" + "=" * 50)
print("8. SSL服务器示例")
print("=" * 50)

# 创建SSL服务器
def create_ssl_server(host="localhost", port=4433, certfile=None, keyfile=None):
    """创建SSL服务器"""
    # 创建SSL上下文
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    
    # 加载证书和密钥
    if certfile and keyfile:
        ctx.load_cert_chain(certfile=certfile, keyfile=keyfile)
    
    # 创建普通套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 设置套接字选项
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # 绑定地址和端口
    sock.bind((host, port))
    
    # 开始监听
    sock.listen(5)
    
    # 包装套接字为SSL套接字
    ssl_sock = ctx.wrap_socket(sock, server_side=True)
    
    print(f"SSL服务器启动在 {host}:{port}")
    print("按Ctrl+C停止服务器")
    
    try:
        # 接受连接
        while True:
            client_socket, addr = ssl_sock.accept()
            print(f"接受来自 {addr} 的连接")
            
            try:
                # 接收客户端数据
                data = client_socket.recv(1024)
                print(f"接收到数据: {data.decode()}")
                
                # 发送响应
                response = "HTTP/1.1 200 OK\r\nContent-Length: 12\r\n\r\nHello World!"
                client_socket.sendall(response.encode())
            finally:
                # 关闭客户端连接
                client_socket.close()
    except KeyboardInterrupt:
        print("服务器停止")
    finally:
        # 关闭SSL套接字
        ssl_sock.close()

# 演示SSL服务器创建
print("演示SSL服务器创建:")
print("注意：实际运行服务器需要有效的证书文件")
print("可以使用以下命令生成自签名证书:")
print("openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365")
print("然后运行: create_ssl_server(certfile='cert.pem', keyfile='key.pem')")

# ===========================
# 9. 证书管理
# ===========================
print("\n" + "=" * 50)
print("9. 证书管理")
print("=" * 50)

# 加载自定义证书
def load_custom_cert(ctx, certfile):
    """加载自定义证书"""
    ctx.load_verify_locations(cafile=certfile)
    return ctx

# 检查证书有效性
def check_cert_validity(host, port=443):
    """检查服务器证书有效性"""
    try:
        # 创建SSL上下文
        ctx = ssl.create_default_context()
        
        # 创建套接字
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ctx.wrap_socket(sock, server_hostname=host)
        
        # 连接到服务器
        ssl_sock.connect((host, port))
        
        # 获取证书
        cert = ssl_sock.getpeercert()
        
        # 关闭套接字
        ssl_sock.close()
        
        return True, cert
    except ssl.CertificateError as e:
        return False, f"证书错误: {e}"
    except Exception as e:
        return False, f"连接错误: {e}"

# 演示证书管理
try:
    print("演示证书检查:")
    
    # 检查百度证书
    is_valid, result = check_cert_validity("www.baidu.com")
    print(f"百度证书有效性: {'有效' if is_valid else '无效'}")
    if is_valid:
        print(f"证书主题: {result['subject'][0][0][1]}")
        print(f"证书颁发者: {result['issuer'][0][0][1]}")
        print(f"证书有效期: {result['notBefore']} 到 {result['notAfter']}")
except Exception as e:
    print(f"证书检查失败: {e}")

# ===========================
# 10. 安全最佳实践
# ===========================
print("\n" + "=" * 50)
print("10. 安全最佳实践")
print("=" * 50)

print("1. 使用最新的SSL/TLS版本")
print("   - 避免使用SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1")
print("   - 推荐使用TLS 1.2或TLS 1.3")

print("\n2. 证书验证")
print("   - 始终验证服务器证书")
print("   - 使用受信任的CA证书")
print("   - 验证证书主机名")

print("\n3. 密码套件配置")
print("   - 使用强密码套件")
print("   - 禁用弱加密算法")
print("   - 优先使用前向保密算法")

print("\n4. 安全配置")
print("   - 启用证书撤销检查")
print("   - 使用证书固定")
print("   - 定期更新证书")

print("\n5. 错误处理")
print("   - 妥善处理SSL错误")
print("   - 不要忽略证书验证错误")
print("   - 记录SSL错误信息")

# ===========================
# 11. 常见SSL错误和解决方案
# ===========================
print("\n" + "=" * 50)
print("11. 常见SSL错误和解决方案")
print("=" * 50)

print("1. CERTIFICATE_VERIFY_FAILED")
print("   - 原因: 服务器证书验证失败")
print("   - 解决方案: 检查证书是否有效，是否由受信任的CA颁发")

print("\n2. HANDSHAKE_FAILED")
print("   - 原因: SSL握手失败")
print("   - 解决方案: 检查SSL版本和加密算法是否兼容")

print("\n3. CERTIFICATE_MISMATCH")
print("   - 原因: 证书主机名不匹配")
print("   - 解决方案: 检查服务器域名和证书中的域名是否一致")

print("\n4. SSLV3_ALERT_HANDSHAKE_FAILURE")
print("   - 原因: SSL 3.0握手失败")
print("   - 解决方案: 使用更高版本的SSL/TLS协议")

print("\n5. PROTOCOL_SSLv2")
print("   - 原因: 使用了已废弃的SSL 2.0协议")
print("   - 解决方案: 使用更高版本的SSL/TLS协议")

# ===========================
# 12. 总结
# ===========================
print("\n" + "=" * 50)
print("12. 总结")
print("=" * 50)
print("ssl模块提供了对SSL/TLS协议的支持")
print("用于创建安全的加密通信通道")
print("\n主要功能:")
print("- 创建SSL/TLS套接字")
print("- 配置SSL上下文")
print("- 证书验证和管理")
print("- 安全HTTP通信(HTTPS)")
print("\n使用ssl模块可以确保:")
print("- 网络通信的安全性")
print("- 数据传输的加密保护")
print("- 服务器身份的验证")
print("- 敏感信息的保护")
print("\n在实际应用中，应遵循安全最佳实践")
print("使用最新的SSL/TLS版本和强加密算法")
print("始终验证服务器证书，确保通信安全")
