# poplib模块详解

poplib是Python中用于处理POP3（Post Office Protocol 3）的标准库，提供了POP3客户端功能，用于连接POP3服务器、接收和管理电子邮件。

## 模块概述

poplib模块提供了POP3、POP3_SSL和POP3_STREAM类，用于实现POP3客户端功能，支持以下主要操作：

- 连接和登录POP3服务器
- 获取邮件列表
- 获取邮件数量和大小
- 获取邮件内容
- 标记和删除邮件
- 重置和退出

## 基本用法

### 连接POP3服务器

```python
import poplib

def connect_pop3_server():
    """连接POP3服务器"""
    # POP3服务器配置
    pop_server = "pop.example.com"  # POP3服务器地址
    pop_port = 995  # POP3_SSL服务器端口
    username = "your_username@example.com"  # 用户名
    password = "your_password"  # 密码
    
    try:
        # 创建POP3_SSL连接
        pop = poplib.POP3_SSL(pop_server, pop_port)
        
        # 打印服务器欢迎信息
        print(pop.getwelcome().decode("utf-8"))
        
        # 登录POP3服务器
        pop.user(username)
        pop.pass_(password)
        
        print("已连接到POP3服务器")
        return pop
        
    except poplib.error_proto as e:
        print(f"POP3错误: {e}")
        return None

# 示例
pop = connect_pop3_server()
if pop:
    # 关闭连接
    pop.quit()
    print("已断开POP3服务器连接")
```

### 使用上下文管理器

```python
import poplib

class POP3Connection:
    def __init__(self, pop_server, pop_port, username, password):
        self.pop_server = pop_server
        self.pop_port = pop_port
        self.username = username
        self.password = password
        self.pop = None
    
    def __enter__(self):
        """进入上下文"""
        self.pop = poplib.POP3_SSL(self.pop_server, self.pop_port)
        self.pop.user(self.username)
        self.pop.pass_(self.password)
        return self.pop
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.pop:
            self.pop.quit()

# 示例
with POP3Connection(
    pop_server="pop.example.com",
    pop_port=995,
    username="your_username@example.com",
    password="your_password"
) as pop:
    print("已连接到POP3服务器")
    # 在这里进行POP3操作

print("已断开POP3服务器连接")
```

## 邮件操作

### 获取邮件状态

```python
import poplib

def get_mail_status(pop):
    """获取邮件状态"""
    # 获取邮件数量和大小
    num_messages, total_size = pop.stat()
    
    print(f"邮件总数: {num_messages}")
    print(f"总大小: {total_size} bytes")
    
    return num_messages, total_size

# 示例
pop = connect_pop3_server()
if pop:
    get_mail_status(pop)
    pop.quit()
```

### 获取邮件列表

```python
import poplib

def get_mail_list(pop):
    """获取邮件列表"""
    # 获取邮件列表（返回序号和大小）
    status, message_list, octets = pop.list()
    
    if status == b"+OK":
        print("邮件列表:")
        for i, message_info in enumerate(message_list):
            # 解码并打印邮件信息
            message_info_str = message_info.decode("utf-8")
            print(f"  邮件 {i+1}: {message_info_str}")
    else:
        print("无法获取邮件列表")
    
    return message_list

# 示例
pop = connect_pop3_server()
if pop:
    get_mail_list(pop)
    pop.quit()
```

### 获取邮件内容

```python
import poplib
import email

def get_email_content(pop, message_number):
    """获取邮件内容"""
    # 获取邮件原始内容
    status, message_lines, octets = pop.retr(message_number)
    
    if status == b"+OK":
        # 合并邮件行
        raw_email = b"\r\n".join(message_lines)
        
        # 解析邮件内容
        msg = email.message_from_bytes(raw_email)
        
        # 获取邮件基本信息
        email_info = {
            "subject": msg["Subject"],
            "from": msg["From"],
            "to": msg["To"],
            "date": msg["Date"],
            "content": ""
        }
        
        # 获取邮件正文
        if msg.is_multipart():
            # 多部分邮件
            for part in msg.walk():
                # 获取内容类型
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                
                # 忽略附件
                if "attachment" not in content_disposition:
                    # 获取文本内容
                    if content_type == "text/plain":
                        email_info["content"] += part.get_payload(decode=True).decode("utf-8", errors="ignore")
                    elif content_type == "text/html":
                        email_info["content"] += part.get_payload(decode=True).decode("utf-8", errors="ignore")
        else:
            # 单部分邮件
            email_info["content"] = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
        
        return email_info
    else:
        print(f"无法获取邮件内容: {message_number}")
        return None

# 示例
pop = connect_pop3_server()
if pop:
    num_messages, _ = pop.stat()
    
    if num_messages > 0:
        # 获取最新的一封邮件
        email_content = get_email_content(pop, num_messages)
        
        if email_content:
            print(f"主题: {email_content['subject']}")
            print(f"发件人: {email_content['from']}")
            print(f"收件人: {email_content['to']}")
            print(f"日期: {email_content['date']}")
            print(f"内容: {email_content['content'][:100]}...")  # 只显示前100个字符
    
    pop.quit()
```

### 获取邮件附件

```python
import poplib
import email
import os

def get_email_attachments(pop, message_number, save_dir="./attachments"):
    """获取邮件附件"""
    # 确保保存目录存在
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # 获取邮件原始内容
    status, message_lines, octets = pop.retr(message_number)
    
    if status == b"+OK":
        # 合并邮件行
        raw_email = b"\r\n".join(message_lines)
        
        # 解析邮件内容
        msg = email.message_from_bytes(raw_email)
        
        attachments = []
        
        # 遍历邮件部分
        for part in msg.walk():
            # 获取内容类型
            content_disposition = str(part.get("Content-Disposition"))
            
            # 检查是否为附件
            if "attachment" in content_disposition:
                # 获取附件文件名
                filename = part.get_filename()
                if filename:
                    # 保存附件
                    filepath = os.path.join(save_dir, filename)
                    with open(filepath, "wb") as f:
                        f.write(part.get_payload(decode=True))
                    
                    attachments.append({
                        "filename": filename,
                        "filepath": filepath,
                        "size": os.path.getsize(filepath)
                    })
        
        return attachments
    else:
        print(f"无法获取邮件附件: {message_number}")
        return []

# 示例
pop = connect_pop3_server()
if pop:
    num_messages, _ = pop.stat()
    
    if num_messages > 0:
        # 获取最新的一封邮件的附件
        attachments = get_email_attachments(pop, num_messages)
        
        if attachments:
            print(f"找到 {len(attachments)} 个附件:")
            for attachment in attachments:
                print(f"  - {attachment['filename']} ({attachment['size']} bytes)")
    
    pop.quit()
```

## 高级功能

### 标记和删除邮件

```python
import poplib

def mark_and_delete_emails(pop):
    """标记和删除邮件"""
    num_messages, _ = pop.stat()
    
    if num_messages > 0:
        print(f"当前邮件总数: {num_messages}")
        
        # 标记最后一封邮件为已删除
        pop.dele(num_messages)
        print(f"已标记邮件 {num_messages} 为已删除")
        
        # 查看未删除邮件数量
        num_messages, _ = pop.stat()
        print(f"未删除邮件数量: {num_messages}")
        
        # 查看已标记删除的邮件
        status, deleted_list, octets = pop.list_deleted()
        if status == b"+OK":
            print("已标记删除的邮件:")
            for deleted in deleted_list:
                print(f"  {deleted.decode('utf-8')}")
        
        # 重置标记
        pop.rset()
        print("已重置所有标记")
        
        # 再次查看未删除邮件数量
        num_messages, _ = pop.stat()
        print(f"重置后邮件数量: {num_messages}")

# 示例
pop = connect_pop3_server()
if pop:
    mark_and_delete_emails(pop)
    pop.quit()
```

### 获取邮件头

```python
import poplib
import email

def get_email_headers(pop, message_number):
    """获取邮件头"""
    # 获取邮件头
    status, message_lines, octets = pop.top(message_number, 0)  # 0表示只获取头
    
    if status == b"+OK":
        # 合并邮件行
        raw_headers = b"\r\n".join(message_lines)
        
        # 解析邮件头
        msg = email.message_from_bytes(raw_headers)
        
        # 打印邮件头信息
        print("邮件头信息:")
        for header, value in msg.items():
            print(f"  {header}: {value}")
        
        return msg
    else:
        print(f"无法获取邮件头: {message_number}")
        return None

# 示例
pop = connect_pop3_server()
if pop:
    num_messages, _ = pop.stat()
    
    if num_messages > 0:
        get_email_headers(pop, num_messages)
    
    pop.quit()
```

### 下载邮件并保存到本地

```python
import poplib
import email
import os
import time

def download_emails(pop, save_dir="./emails", max_count=10):
    """下载邮件并保存到本地"""
    # 确保保存目录存在
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    num_messages, _ = pop.stat()
    
    if num_messages == 0:
        print("没有邮件可下载")
        return
    
    # 下载最新的max_count封邮件
    start_num = max(1, num_messages - max_count + 1)
    
    for message_number in range(start_num, num_messages + 1):
        print(f"\n下载邮件 {message_number}...")
        
        # 获取邮件内容
        status, message_lines, octets = pop.retr(message_number)
        
        if status == b"+OK":
            # 合并邮件行
            raw_email = b"\r\n".join(message_lines)
            
            # 解析邮件内容
            msg = email.message_from_bytes(raw_email)
            
            # 获取邮件主题
            subject = msg["Subject"]
            if subject is None:
                subject = "无主题"
            else:
                # 解码邮件主题
                subject = email.header.decode_header(subject)[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode("utf-8")
            
            # 创建保存文件名
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_{message_number}_{subject[:50]}.eml"
            filename = filename.replace("/", "_").replace("\\", "_")  # 替换非法字符
            filepath = os.path.join(save_dir, filename)
            
            # 保存邮件
            with open(filepath, "wb") as f:
                f.write(raw_email)
            
            print(f"已保存邮件到: {filepath}")

# 示例
pop = connect_pop3_server()
if pop:
    download_emails(pop, max_count=5)
    pop.quit()
```

## 实际应用示例

### 示例1：邮件接收客户端

```python
import poplib
import email
import os
import time

class EmailClient:
    def __init__(self, pop_server, pop_port, username, password):
        """初始化邮件客户端"""
        self.pop_server = pop_server
        self.pop_port = pop_port
        self.username = username
        self.password = password
        self.pop = None
    
    def connect(self):
        """连接POP3服务器"""
        try:
            self.pop = poplib.POP3_SSL(self.pop_server, self.pop_port)
            self.pop.user(self.username)
            self.pop.pass_(self.password)
            print("已连接到POP3服务器")
            return True
        except poplib.error_proto as e:
            print(f"连接POP3服务器失败: {e}")
            return False
    
    def disconnect(self):
        """断开POP3服务器连接"""
        if self.pop:
            self.pop.quit()
            print("已断开POP3服务器连接")
    
    def get_email_list(self):
        """获取邮件列表"""
        if not self.pop:
            print("未连接到POP3服务器")
            return []
        
        status, message_list, octets = pop.list()
        if status != b"+OK":
            print("无法获取邮件列表")
            return []
        
        emails = []
        for i, message_info in enumerate(message_list):
            message_info_str = message_info.decode("utf-8")
            parts = message_info_str.split()
            if len(parts) >= 2:
                emails.append({
                    "number": int(parts[0]),
                    "size": int(parts[1])
                })
        
        return emails
    
    def get_email_summary(self, message_number):
        """获取邮件摘要"""
        if not self.pop:
            print("未连接到POP3服务器")
            return None
        
        # 获取邮件头
        status, message_lines, octets = self.pop.top(message_number, 0)
        if status != b"+OK":
            print(f"无法获取邮件头: {message_number}")
            return None
        
        # 合并邮件行
        raw_headers = b"\r\n".join(message_lines)
        
        # 解析邮件头
        msg = email.message_from_bytes(raw_headers)
        
        # 解析邮件主题
        subject = msg["Subject"]
        if subject:
            subject = email.header.decode_header(subject)[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode("utf-8")
        
        # 解析发件人
        from_addr = msg["From"]
        if from_addr:
            from_addr = email.header.decode_header(from_addr)[0][0]
            if isinstance(from_addr, bytes):
                from_addr = from_addr.decode("utf-8")
        
        return {
            "number": message_number,
            "subject": subject,
            "from": from_addr,
            "date": msg["Date"]
        }
    
    def get_full_email(self, message_number):
        """获取完整邮件"""
        if not self.pop:
            print("未连接到POP3服务器")
            return None
        
        # 获取邮件原始内容
        status, message_lines, octets = self.pop.retr(message_number)
        if status != b"+OK":
            print(f"无法获取邮件内容: {message_number}")
            return None
        
        # 合并邮件行
        raw_email = b"\r\n".join(message_lines)
        
        # 解析邮件内容
        msg = email.message_from_bytes(raw_email)
        
        # 获取邮件基本信息
        email_info = {
            "number": message_number,
            "subject": msg["Subject"],
            "from": msg["From"],
            "to": msg["To"],
            "date": msg["Date"],
            "content": "",
            "attachments": []
        }
        
        # 解码邮件主题
        if email_info["subject"]:
            subject = email.header.decode_header(email_info["subject"])[0][0]
            if isinstance(subject, bytes):
                email_info["subject"] = subject.decode("utf-8")
        
        # 解码发件人
        if email_info["from"]:
            from_addr = email.header.decode_header(email_info["from"])[0][0]
            if isinstance(from_addr, bytes):
                email_info["from"] = from_addr.decode("utf-8")
        
        # 获取邮件正文和附件
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))
                
                if "attachment" in content_disposition:
                    # 处理附件
                    filename = part.get_filename()
                    if filename:
                        # 解码附件文件名
                        filename = email.header.decode_header(filename)[0][0]
                        if isinstance(filename, bytes):
                            filename = filename.decode("utf-8")
                        
                        email_info["attachments"].append({
                            "filename": filename,
                            "content_type": content_type,
                            "size": len(part.get_payload(decode=True))
                        })
                else:
                    # 处理正文
                    if content_type == "text/plain":
                        content = part.get_payload(decode=True)
                        if content:
                            email_info["content"] += content.decode("utf-8", errors="ignore")
        else:
            # 单部分邮件
            content = msg.get_payload(decode=True)
            if content:
                email_info["content"] = content.decode("utf-8", errors="ignore")
        
        return email_info

# 使用示例
if __name__ == "__main__":
    # 创建邮件客户端
    client = EmailClient(
        pop_server="pop.example.com",
        pop_port=995,
        username="your_username@example.com",
        password="your_password"
    )
    
    if client.connect():
        try:
            # 获取邮件列表
            emails = client.get_email_list()
            print(f"\n共有 {len(emails)} 封邮件")
            
            # 显示最新的5封邮件摘要
            if emails:
                print("\n最新的5封邮件:")
                for email in emails[-5:]:
                    summary = client.get_email_summary(email["number"])
                    if summary:
                        print(f"\n邮件 {summary['number']}:")
                        print(f"  主题: {summary['subject']}")
                        print(f"  发件人: {summary['from']}")
                        print(f"  日期: {summary['date']}")
            
            # 获取最新的一封完整邮件
            if emails:
                latest_email = client.get_full_email(emails[-1]["number"])
                if latest_email:
                    print(f"\n\n最新邮件详情:")
                    print(f"主题: {latest_email['subject']}")
                    print(f"发件人: {latest_email['from']}")
                    print(f"收件人: {latest_email['to']}")
                    print(f"日期: {latest_email['date']}")
                    print(f"附件数量: {len(latest_email['attachments'])}")
                    print(f"内容预览: {latest_email['content'][:100]}...")
        
        finally:
            client.disconnect()
```

## 最佳实践

1. **使用POP3_SSL**：使用POP3_SSL加密连接，提高通信安全性
2. **处理异常**：捕获并处理poplib.error_proto异常
3. **设置超时**：使用socket.setdefaulttimeout设置超时时间
4. **关闭连接**：使用quit方法关闭连接，释放资源
5. **使用top命令**：对于只需要查看邮件头的操作，使用top命令而非retr
6. **解码处理**：正确处理邮件内容和主题的编码
7. **避免硬编码凭据**：从配置文件或环境变量读取用户名和密码
8. **定期备份**：定期备份重要邮件，避免意外丢失
9. **限制邮件数量**：使用top命令或限制retr命令获取的邮件数量

## 与其他模块的关系

- **email**：用于解析和构建电子邮件
- **smtplib**：用于发送电子邮件
- **imaplib**：用于IMAP协议接收电子邮件
- **popclient**：第三方库，提供更高级的POP3客户端API

## POP3与IMAP的比较

| 特性 | POP3 | IMAP |
|------|------|------|
| **邮件存储位置** | 本地 | 服务器 |
| **邮件管理** | 基本（删除、标记） | 高级（文件夹、搜索、标记） |
| **同步** | 无 | 支持多设备同步 |
| **带宽使用** | 低（只下载新邮件） | 高（需要同步邮件状态） |
| **离线访问** | 支持 | 部分支持（需要先同步） |
| **服务器资源** | 低（邮件下载后可删除） | 高（长期存储邮件） |

## 总结

poplib模块是Python中用于实现POP3客户端功能的标准库，支持连接POP3服务器、接收和管理电子邮件。通过POP3_SSL类，可以安全地连接POP3服务器，执行获取邮件列表、获取邮件内容、标记和删除邮件等操作。

在实际应用中，poplib模块可以用于创建邮件客户端、邮件备份工具等。对于需要更高级的邮件管理功能（如文件夹、搜索、多设备同步等），可以考虑使用IMAP协议（通过imaplib模块）。