# ftplib模块详解

ftplib是Python中用于处理FTP（File Transfer Protocol）的标准库，提供了FTP客户端功能，用于连接FTP服务器、上传和下载文件等操作。

## 模块概述

ftplib模块提供了FTP类，用于实现FTP客户端功能，支持以下主要操作：

- 连接和登录FTP服务器
- 切换目录
- 上传和下载文件
- 创建和删除目录
- 重命名文件
- 获取文件列表
- 更改文件权限

## 基本用法

### 连接FTP服务器

```python
import ftplib

# 创建FTP客户端实例
ftp = ftplib.FTP()

# 连接FTP服务器
ftp.connect("ftp.example.com", 21)  # 默认端口是21

# 登录FTP服务器
ftp.login("username", "password")

# 打印欢迎信息
print(ftp.getwelcome())

# 关闭连接
ftp.quit()
```

### 使用上下文管理器

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    # 登录
    ftp.login("username", "password")
    
    # 打印欢迎信息
    print(ftp.getwelcome())
    
# 连接会自动关闭
```

## 文件传输操作

### 下载文件

```python
import ftplib

def download_file(ftp, remote_file, local_file):
    """下载文件"""
    with open(local_file, 'wb') as f:
        # 使用RETR命令下载文件
        ftp.retrbinary('RETR ' + remote_file, f.write)

# 示例
with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 下载文件
    download_file(ftp, "remote_file.txt", "local_file.txt")
    print("文件下载完成")
```

### 上传文件

```python
import ftplib

def upload_file(ftp, local_file, remote_file):
    """上传文件"""
    with open(local_file, 'rb') as f:
        # 使用STOR命令上传文件
        ftp.storbinary('STOR ' + remote_file, f)

# 示例
with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 上传文件
    upload_file(ftp, "local_file.txt", "remote_file.txt")
    print("文件上传完成")
```

### 下载文本文件

```python
import ftplib

def download_text_file(ftp, remote_file, local_file):
    """下载文本文件"""
    with open(local_file, 'w') as f:
        # 使用RETR命令下载文本文件
        ftp.retrlines('RETR ' + remote_file, f.write)

# 示例
with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 下载文本文件
    download_text_file(ftp, "remote_text.txt", "local_text.txt")
    print("文本文件下载完成")
```

### 上传文本文件

```python
import ftplib

def upload_text_file(ftp, local_file, remote_file):
    """上传文本文件"""
    with open(local_file, 'r') as f:
        # 使用STOR命令上传文本文件
        ftp.storlines('STOR ' + remote_file, f)

# 示例
with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 上传文本文件
    upload_text_file(ftp, "local_text.txt", "remote_text.txt")
    print("文本文件上传完成")
```

## 目录操作

### 获取当前目录

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 获取当前目录
    current_dir = ftp.pwd()
    print(f"当前目录: {current_dir}")
```

### 切换目录

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 切换到指定目录
    ftp.cwd("documents")
    
    # 验证当前目录
    print(f"当前目录: {ftp.pwd()}")
    
    # 切换到父目录
    ftp.cwd("..")
    print(f"当前目录: {ftp.pwd()}")
```

### 创建目录

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 创建目录
    ftp.mkd("new_directory")
    print("目录创建完成")
```

### 删除目录

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 删除目录
    ftp.rmd("empty_directory")
    print("目录删除完成")
```

## 文件操作

### 获取文件列表

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 获取当前目录下的文件列表（包含详细信息）
    print("目录列表:")
    ftp.dir()
    
    # 获取当前目录下的文件名列表
    print("\n文件名列表:")
    files = ftp.nlst()
    for file in files:
        print(file)
    
    # 获取特定文件的详细信息
    print("\n文件信息:")
    ftp.retrlines("LIST filename.txt")
```

### 重命名文件

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 重命名文件
    ftp.rename("old_name.txt", "new_name.txt")
    print("文件重命名完成")
```

### 删除文件

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 删除文件
    ftp.delete("filename.txt")
    print("文件删除完成")
```

### 获取文件大小

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 获取文件大小
    size = ftp.size("filename.txt")
    print(f"文件大小: {size} 字节")
```

## 高级功能

### 使用被动模式

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 启用被动模式
    ftp.set_pasv(True)
    
    # 验证被动模式
    print(f"被动模式: {ftp.passiveserver}")
```

### 更改文件权限

```python
import ftplib

with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 更改文件权限
    ftp.sendcmd('SITE CHMOD 755 filename.txt')
    print("文件权限更改完成")
```

### 下载大文件（带进度条）

```python
import ftplib
import os

def download_file_with_progress(ftp, remote_file, local_file):
    """下载文件并显示进度条"""
    # 获取文件大小
    file_size = ftp.size(remote_file)
    downloaded = 0
    
    with open(local_file, 'wb') as f:
        def callback(data):
            nonlocal downloaded
            f.write(data)
            downloaded += len(data)
            # 计算并显示进度
            progress = (downloaded / file_size) * 100
            print(f"下载进度: {progress:.1f}% ({downloaded}/{file_size} bytes)", end='\r')
        
        ftp.retrbinary('RETR ' + remote_file, callback)
    
    print("\n文件下载完成")

# 示例
with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 下载文件并显示进度条
    download_file_with_progress(ftp, "large_file.zip", "local_large_file.zip")
```

### 递归下载目录

```python
import ftplib
import os

def download_directory(ftp, remote_dir, local_dir):
    """递归下载目录"""
    # 创建本地目录
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    
    # 保存当前目录
    current_dir = ftp.pwd()
    
    try:
        # 切换到远程目录
        ftp.cwd(remote_dir)
        
        # 获取文件列表
        files = ftp.nlst()
        
        for file in files:
            remote_file = os.path.join(remote_dir, file)
            local_file = os.path.join(local_dir, file)
            
            try:
                # 尝试切换到子目录
                ftp.cwd(file)
                ftp.cwd("..")
                
                # 是目录，递归下载
                download_directory(ftp, remote_file, local_file)
            except ftplib.error_perm:
                # 不是目录，下载文件
                print(f"下载文件: {remote_file} -> {local_file}")
                with open(local_file, 'wb') as f:
                    ftp.retrbinary('RETR ' + file, f.write)
    finally:
        # 切换回原目录
        ftp.cwd(current_dir)

# 示例
with ftplib.FTP("ftp.example.com") as ftp:
    ftp.login("username", "password")
    
    # 递归下载目录
    download_directory(ftp, "remote_directory", "local_directory")
    print("目录下载完成")
```

## 实际应用示例

### 示例1：FTP文件同步工具

```python
import ftplib
import os
import hashlib

def calculate_md5(file_path, block_size=8192):
    """计算文件的MD5值"""
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            md5.update(block)
    return md5.hexdigest()

class FTPSync:
    def __init__(self, host, username, password, remote_dir, local_dir):
        self.host = host
        self.username = username
        self.password = password
        self.remote_dir = remote_dir
        self.local_dir = local_dir
    
    def sync(self):
        """同步文件"""
        with ftplib.FTP(self.host) as ftp:
            ftp.login(self.username, self.password)
            
            # 获取远程文件列表和大小
            remote_files = {}
            ftp.cwd(self.remote_dir)
            files = ftp.nlst()
            
            for file in files:
                try:
                    size = ftp.size(file)
                    remote_files[file] = size
                except ftplib.error_perm:
                    # 不是文件，跳过
                    continue
            
            # 获取本地文件列表和大小
            local_files = {}
            if os.path.exists(self.local_dir):
                for file in os.listdir(self.local_dir):
                    local_file = os.path.join(self.local_dir, file)
                    if os.path.isfile(local_file):
                        local_files[file] = os.path.getsize(local_file)
            
            # 下载新文件或大小不同的文件
            for file, size in remote_files.items():
                local_file = os.path.join(self.local_dir, file)
                if file not in local_files or local_files[file] != size:
                    print(f"下载文件: {file}")
                    with open(local_file, 'wb') as f:
                        ftp.retrbinary('RETR ' + file, f.write)
            
            # 删除本地存在但远程不存在的文件
            for file in local_files:
                if file not in remote_files:
                    local_file = os.path.join(self.local_dir, file)
                    print(f"删除文件: {file}")
                    os.remove(local_file)
            
            print("同步完成")

# 使用示例
sync_tool = FTPSync(
    host="ftp.example.com",
    username="username",
    password="password",
    remote_dir="documents",
    local_dir="local_documents"
)
sync_tool.sync()
```

### 示例2：FTP文件上传工具

```python
import ftplib
import os
import argparse

def upload_file(ftp, local_path, remote_path):
    """上传文件"""
    with open(local_path, 'rb') as f:
        ftp.storbinary('STOR ' + remote_path, f)
    print(f"上传完成: {local_path} -> {remote_path}")

def upload_directory(ftp, local_dir, remote_dir):
    """递归上传目录"""
    # 创建远程目录
    try:
        ftp.mkd(remote_dir)
    except ftplib.error_perm:
        # 目录已存在
        pass
    
    # 切换到远程目录
    ftp.cwd(remote_dir)
    
    # 遍历本地目录
    for item in os.listdir(local_dir):
        local_item = os.path.join(local_dir, item)
        remote_item = item
        
        if os.path.isfile(local_item):
            # 上传文件
            upload_file(ftp, local_item, remote_item)
        elif os.path.isdir(local_item):
            # 递归上传目录
            upload_directory(ftp, local_item, remote_item)
    
    # 切换回父目录
    ftp.cwd("..")

def main():
    parser = argparse.ArgumentParser(description="FTP文件上传工具")
    parser.add_argument("host", help="FTP服务器地址")
    parser.add_argument("username", help="FTP用户名")
    parser.add_argument("password", help="FTP密码")
    parser.add_argument("local_path", help="本地文件或目录路径")
    parser.add_argument("remote_path", help="远程文件或目录路径")
    
    args = parser.parse_args()
    
    with ftplib.FTP(args.host) as ftp:
        ftp.login(args.username, args.password)
        
        if os.path.isfile(args.local_path):
            # 上传文件
            upload_file(ftp, args.local_path, args.remote_path)
        elif os.path.isdir(args.local_path):
            # 上传目录
            upload_directory(ftp, args.local_path, args.remote_path)
        else:
            print("本地路径不存在")

if __name__ == "__main__":
    main()
```

### 示例3：FTP服务器文件浏览器

```python
import ftplib
import os

class FTPBrowser:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.ftp = None
    
    def connect(self):
        """连接FTP服务器"""
        self.ftp = ftplib.FTP(self.host)
        self.ftp.login(self.username, self.password)
        print(f"已连接到 {self.host}")
        print(f"当前目录: {self.ftp.pwd()}")
    
    def disconnect(self):
        """断开连接"""
        if self.ftp:
            self.ftp.quit()
            print("已断开连接")
    
    def list_files(self, directory=None):
        """列出文件"""
        if not self.ftp:
            print("未连接到FTP服务器")
            return
        
        if directory:
            self.ftp.cwd(directory)
        
        print(f"\n当前目录: {self.ftp.pwd()}")
        print("文件列表:")
        print("-" * 50)
        
        def list_callback(line):
            """处理列表行"""
            parts = line.split()
            if len(parts) < 6:
                return
            
            # 提取权限、类型、大小、日期和名称
            permissions = parts[0]
            size = parts[4]
            date = f"{parts[5]} {parts[6]}"
            name = " ".join(parts[8:])
            
            # 判断是文件还是目录
            if permissions.startswith('d'):
                name += "/"
                size = "<DIR>"
            
            print(f"{permissions}  {size:>10}  {date}  {name}")
        
        self.ftp.dir(list_callback)
        print("-" * 50)
    
    def download_file(self, remote_file, local_file):
        """下载文件"""
        if not self.ftp:
            print("未连接到FTP服务器")
            return
        
        print(f"下载文件: {remote_file} -> {local_file}")
        with open(local_file, 'wb') as f:
            self.ftp.retrbinary('RETR ' + remote_file, f.write)
        print("下载完成")
    
    def upload_file(self, local_file, remote_file):
        """上传文件"""
        if not self.ftp:
            print("未连接到FTP服务器")
            return
        
        print(f"上传文件: {local_file} -> {remote_file}")
        with open(local_file, 'rb') as f:
            self.ftp.storbinary('STOR ' + remote_file, f)
        print("上传完成")

# 使用示例
browser = FTPBrowser("ftp.example.com", "username", "password")
browser.connect()

try:
    # 列出根目录文件
    browser.list_files()
    
    # 切换到documents目录并列出文件
    browser.list_files("documents")
    
    # 下载文件
    browser.download_file("example.txt", "local_example.txt")
    
    # 上传文件
    browser.upload_file("local_file.txt", "remote_file.txt")
finally:
    browser.disconnect()
```

## 错误处理

```python
import ftplib

try:
    with ftplib.FTP("ftp.example.com") as ftp:
        # 尝试匿名登录
        ftp.login()
        
        # 尝试访问不存在的目录
        ftp.cwd("nonexistent_directory")
        
        # 下载不存在的文件
        with open("local_file.txt", "wb") as f:
            ftp.retrbinary("RETR nonexistent_file.txt", f.write)
            
except ftplib.all_errors as e:
    print(f"FTP错误: {e}")
```

## 最佳实践

1. **使用上下文管理器**：使用`with`语句自动关闭连接
2. **处理异常**：捕获并处理ftplib.all_errors异常
3. **设置超时**：使用`ftp.connect(host, port, timeout)`设置超时时间
4. **使用被动模式**：对于防火墙后面的客户端，启用被动模式
5. **验证文件完整性**：使用MD5或SHA1验证文件完整性
6. **限制并发连接**：避免同时创建过多FTP连接
7. **使用安全连接**：考虑使用FTPS或SFTP（paramiko库）代替FTP
8. **避免硬编码凭据**：从配置文件或环境变量读取用户名和密码

## 与其他模块的关系

- **paramiko**：第三方库，提供SFTP（SSH File Transfer Protocol）功能
- **ftputil**：第三方库，提供更高级的FTP客户端功能
- **os**：用于处理本地文件系统操作

## 总结

ftplib模块是Python中用于实现FTP客户端功能的标准库，支持连接FTP服务器、上传和下载文件、创建和删除目录等操作。通过FTP类，可以方便地实现FTP客户端功能。

在实际应用中，ftplib模块可以用于创建文件同步工具、文件上传和下载工具、FTP浏览器等。对于需要更高级功能或安全连接的场景，可以考虑使用paramiko或ftputil等第三方库。