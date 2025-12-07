# imaplib模块详解

imaplib是Python中用于处理IMAP（Internet Message Access Protocol）的标准库，提供了IMAP客户端功能，用于连接IMAP服务器、接收和管理电子邮件。

## 模块概述

imaplib模块提供了IMAP4、IMAP4_SSL和IMAP4_stream类，用于实现IMAP客户端功能，支持以下主要操作：

- 连接和登录IMAP服务器
- 列出邮箱列表
- 选择邮箱
- 搜索邮件
- 获取邮件内容
- 标记和删除邮件
- 创建和删除邮箱

## 基本用法

### 连接IMAP服务器

```python
import imaplib

def connect_imap_server():
    """连接IMAP服务器"""
    # IMAP服务器配置
    imap_server = "imap.example.com"  # IMAP服务器地址
    imap_port = 993  # IMAP_SSL服务器端口
    username = "your_username@example.com"  # 用户名
    password = "your_password"  # 密码
    
    try:
        # 创建IMAP4_SSL连接
        imap = imaplib.IMAP4_SSL(imap_server, imap_port)
        
        # 登录IMAP服务器
        imap.login(username, password)
        
        print("已连接到IMAP服务器")
        return imap
        
    except imaplib.IMAP4.error as e:
        print(f"IMAP错误: {e}")
        return None

# 示例
imap = connect_imap_server()
if imap:
    # 关闭连接
    imap.logout()
    print("已断开IMAP服务器连接")
```

### 使用上下文管理器

```python
import imaplib

class IMAPConnection:
    def __init__(self, imap_server, imap_port, username, password):
        self.imap_server = imap_server
        self.imap_port = imap_port
        self.username = username
        self.password = password
        self.imap = None
    
    def __enter__(self):
        """进入上下文"""
        self.imap = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
        self.imap.login(self.username, self.password)
        return self.imap
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文"""
        if self.imap:
            self.imap.logout()

# 示例
with IMAPConnection(
    imap_server="imap.example.com",
    imap_port=993,
    username="your_username@example.com",
    password="your_password"
) as imap:
    print("已连接到IMAP服务器")
    # 在这里进行IMAP操作

print("已断开IMAP服务器连接")
```

## 邮箱操作

### 列出邮箱列表

```python
import imaplib

def list_mailboxes(imap):
    """列出邮箱列表"""
    # 列出所有邮箱
    status, mailboxes = imap.list()
    
    if status == "OK":
        print("邮箱列表:")
        for mailbox in mailboxes:
            # 解码并打印邮箱信息
            mailbox_info = mailbox.decode("utf-8")
            print(f"  {mailbox_info}")
    else:
        print("无法获取邮箱列表")

# 示例
imap = connect_imap_server()
if imap:
    list_mailboxes(imap)
    imap.logout()
```

### 选择邮箱

```python
import imaplib

def select_mailbox(imap, mailbox_name="INBOX"):
    """选择邮箱"""
    # 选择邮箱（只读模式）
    status, response = imap.select(mailbox_name, readonly=True)
    
    if status == "OK":
        print(f"已选择邮箱: {mailbox_name}")
        print(f"邮件总数: {response[0].decode('utf-8')}")
        return True
    else:
        print(f"无法选择邮箱: {mailbox_name}")
        return False

# 示例
imap = connect_imap_server()
if imap:
    select_mailbox(imap, "INBOX")
    imap.logout()
```

### 创建邮箱

```python
import imaplib

def create_mailbox(imap, mailbox_name):
    """创建邮箱"""
    # 创建邮箱
    status, response = imap.create(mailbox_name)
    
    if status == "OK":
        print(f"邮箱创建成功: {mailbox_name}")
        return True
    else:
        print(f"邮箱创建失败: {mailbox_name}")
        return False

# 示例
imap = connect_imap_server()
if imap:
    create_mailbox(imap, "TestMailbox")
    imap.logout()
```

### 删除邮箱

```python
import imaplib

def delete_mailbox(imap, mailbox_name):
    """删除邮箱"""
    # 删除邮箱
    status, response = imap.delete(mailbox_name)
    
    if status == "OK":
        print(f"邮箱删除成功: {mailbox_name}")
        return True
    else:
        print(f"邮箱删除失败: {mailbox_name}")
        return False

# 示例
imap = connect_imap_server()
if imap:
    delete_mailbox(imap, "TestMailbox")
    imap.logout()
```

## 邮件操作

### 搜索邮件

```python
import imaplib
import email.utils

def search_emails(imap, criteria="ALL"):
    """搜索邮件"""
    # 搜索邮件
    status, response = imap.search(None, criteria)
    
    if status == "OK":
        # 获取邮件ID列表
        email_ids = response[0].split()
        print(f"找到 {len(email_ids)} 封邮件")
        return email_ids
    else:
        print("邮件搜索失败")
        return []

# 示例
imap = connect_imap_server()
if imap:
    select_mailbox(imap, "INBOX")
    
    # 搜索所有邮件
    email_ids = search_emails(imap, "ALL")
    
    # 搜索未读邮件
    unread_email_ids = search_emails(imap, "UNSEEN")
    
    # 搜索特定发件人邮件
    sender = "sender@example.com"
    sender_email_ids = search_emails(imap, f'FROM "{sender}"')
    
    # 搜索特定主题邮件
    subject = "测试邮件"
    subject_email_ids = search_emails(imap, f'SUBJECT "{subject}"')
    
    imap.logout()
```

### 获取邮件内容

```python
import imaplib
import email

def get_email_content(imap, email_id):
    """获取邮件内容"""
    # 获取邮件原始内容
    status, response = imap.fetch(email_id, "(RFC822)")
    
    if status == "OK":
        # 解析邮件内容
        raw_email = response[0][1]
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
                        email_info["content"] += part.get_payload(decode=True).decode("utf-8")
                    elif content_type == "text/html":
                        email_info["content"] += part.get_payload(decode=True).decode("utf-8")
        else:
            # 单部分邮件
            content_type = msg.get_content_type()
            email_info["content"] = msg.get_payload(decode=True).decode("utf-8")
        
        return email_info
    else:
        print(f"无法获取邮件内容: {email_id}")
        return None

# 示例
imap = connect_imap_server()
if imap:
    select_mailbox(imap, "INBOX")
    
    # 搜索最新的5封邮件
    email_ids = search_emails(imap, "ALL")
    if email_ids:
        for email_id in email_ids[-5:]:  # 获取最新的5封邮件
            print(f"\n邮件ID: {email_id.decode('utf-8')}")
            email_content = get_email_content(imap, email_id)
            if email_content:
                print(f"主题: {email_content['subject']}")
                print(f"发件人: {email_content['from']}")
                print(f"收件人: {email_content['to']}")
                print(f"日期: {email_content['date']}")
                print(f"内容: {email_content['content'][:100]}...")  # 只显示前100个字符
    
    imap.logout()
```

### 获取邮件附件

```python
import imaplib
import email
import os

def get_email_attachments(imap, email_id, save_dir="./attachments"):
    """获取邮件附件"""
    # 确保保存目录存在
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # 获取邮件原始内容
    status, response = imap.fetch(email_id, "(RFC822)")
    
    if status == "OK":
        # 解析邮件内容
        raw_email = response[0][1]
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
        print(f"无法获取邮件附件: {email_id}")
        return []

# 示例
imap = connect_imap_server()
if imap:
    select_mailbox(imap, "INBOX")
    
    # 搜索最新的5封邮件
    email_ids = search_emails(imap, "ALL")
    if email_ids:
        for email_id in email_ids[-5:]:  # 获取最新的5封邮件
            print(f"\n邮件ID: {email_id.decode('utf-8')}")
            
            # 获取邮件附件
            attachments = get_email_attachments(imap, email_id)
            if attachments:
                print(f"找到 {len(attachments)} 个附件:")
                for attachment in attachments:
                    print(f"  - {attachment['filename']} ({attachment['size']} bytes)")
    
    imap.logout()
```

## 高级功能

### 标记和删除邮件

```python
import imaplib

def mark_and_delete_emails(imap):
    """标记和删除邮件"""
    # 选择邮箱（读写模式）
    status = select_mailbox(imap, "INBOX")
    if not status:
        return
    
    # 搜索未读邮件
    status, response = imap.search(None, "UNSEEN")
    if status == "OK":
        email_ids = response[0].split()
        if email_ids:
            print(f"找到 {len(email_ids)} 封未读邮件")
            
            # 标记未读邮件为已读
            for email_id in email_ids:
                imap.store(email_id, '+FLAGS', '\\Seen')
            print("未读邮件已标记为已读")
    
    # 搜索特定主题邮件
    subject = "垃圾邮件"
    status, response = imap.search(None, f'SUBJECT "{subject}"')
    if status == "OK":
        email_ids = response[0].split()
        if email_ids:
            print(f"找到 {len(email_ids)} 封主题为'{subject}'的邮件")
            
            # 标记邮件为已删除
            for email_id in email_ids:
                imap.store(email_id, '+FLAGS', '\\Deleted')
            print("邮件已标记为已删除")
            
            # 永久删除已标记邮件
            imap.expunge()
            print("已永久删除邮件")

# 示例
imap = connect_imap_server()
if imap:
    mark_and_delete_emails(imap)
    imap.logout()
```

### 移动邮件

```python
import imaplib

def move_email(imap, email_id, source_mailbox, target_mailbox):
    """移动邮件"""
    # 选择源邮箱（读写模式）
    imap.select(source_mailbox, readonly=False)
    
    # 将邮件复制到目标邮箱
    status, response = imap.copy(email_id, target_mailbox)
    if status == "OK":
        print(f"邮件 {email_id.decode('utf-8')} 已复制到 {target_mailbox}")
        
        # 标记源邮件为已删除
        imap.store(email_id, '+FLAGS', '\\Deleted')
        
        # 永久删除源邮件
        imap.expunge()
        print(f"邮件 {email_id.decode('utf-8')} 已从 {source_mailbox} 删除")
        return True
    else:
        print(f"移动邮件失败: {response}")
        return False

# 示例
imap = connect_imap_server()
if imap:
    # 创建目标邮箱
    create_mailbox(imap, "ARCHIVE")
    
    # 选择源邮箱
    select_mailbox(imap, "INBOX")
    
    # 搜索最新的1封邮件
    status, response = imap.search(None, "ALL")
    if status == "OK":
        email_ids = response[0].split()
        if email_ids:
            latest_email_id = email_ids[-1]
            
            # 移动邮件
            move_email(imap, latest_email_id, "INBOX", "ARCHIVE")
    
    imap.logout()
```

## 实际应用示例

### 示例1：邮件接收客户端

```python
import imaplib
import email
import os
import time

class EmailClient:
    def __init__(self, imap_server, imap_port, username, password):
        """初始化邮件客户端"""
        self.imap_server = imap_server
        self.imap_port = imap_port
        self.username = username
        self.password = password
        self.imap = None
    
    def connect(self):
        """连接IMAP服务器"""
        try:
            self.imap = imaplib.IMAP4_SSL(self.imap_server, self.imap_port)
            self.imap.login(self.username, self.password)
            print("已连接到IMAP服务器")
            return True
        except imaplib.IMAP4.error as e:
            print(f"连接IMAP服务器失败: {e}")
            return False
    
    def disconnect(self):
        """断开IMAP服务器连接"""
        if self.imap:
            self.imap.logout()
            print("已断开IMAP服务器连接")
    
    def get_unread_emails(self, mailbox_name="INBOX", max_count=10):
        """获取未读邮件"""
        if not self.imap:
            print("未连接到IMAP服务器")
            return []
        
        # 选择邮箱
        status, response = self.imap.select(mailbox_name, readonly=True)
        if status != "OK":
            print(f"无法选择邮箱: {mailbox_name}")
            return []
        
        # 搜索未读邮件
        status, response = self.imap.search(None, "UNSEEN")
        if status != "OK":
            print("无法搜索未读邮件")
            return []
        
        email_ids = response[0].split()
        if not email_ids:
            print("没有未读邮件")
            return []
        
        # 获取最新的max_count封邮件
        email_ids = email_ids[-max_count:]
        
        emails = []
        for email_id in reversed(email_ids):  # 按时间倒序
            # 获取邮件内容
            status, response = self.imap.fetch(email_id, "(RFC822)")
            if status == "OK":
                raw_email = response[0][1]
                msg = email.message_from_bytes(raw_email)
                
                email_info = {
                    "id": email_id.decode("utf-8"),
                    "subject": msg["Subject"],
                    "from": msg["From"],
                    "to": msg["To"],
                    "date": msg["Date"],
                    "content": ""
                }
                
                # 获取邮件正文
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        
                        if "attachment" not in content_disposition:
                            if content_type == "text/plain":
                                email_info["content"] += part.get_payload(decode=True).decode("utf-8", errors="ignore")
                        else:
                            # 统计附件数量
                            if "attachments" not in email_info:
                                email_info["attachments"] = 0
                            email_info["attachments"] += 1
                else:
                    email_info["content"] = msg.get_payload(decode=True).decode("utf-8", errors="ignore")
                
                emails.append(email_info)
        
        return emails
    
    def monitor_new_emails(self, mailbox_name="INBOX", check_interval=60):
        """监控新邮件"""
        if not self.imap:
            print("未连接到IMAP服务器")
            return
        
        print(f"开始监控邮箱 {mailbox_name}，每 {check_interval} 秒检查一次")
        
        try:
            while True:
                # 获取未读邮件数量
                status, response = self.imap.select(mailbox_name, readonly=True)
                if status == "OK":
                    total_count = int(response[0].decode("utf-8"))
                    
                    status, response = self.imap.search(None, "UNSEEN")
                    if status == "OK":
                        unread_count = len(response[0].split())
                        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 总邮件数: {total_count}, 未读邮件数: {unread_count}")
                        
                        if unread_count > 0:
                            # 获取未读邮件
                            emails = self.get_unread_emails(mailbox_name, max_count=unread_count)
                            for email in emails:
                                print(f"\n新邮件:")
                                print(f"  主题: {email['subject']}")
                                print(f"  发件人: {email['from']}")
                                print(f"  日期: {email['date']}")
                                if "attachments" in email:
                                    print(f"  附件: {email['attachments']} 个")
                                print(f"  内容: {email['content'][:100]}...")
                
                # 等待指定时间
                time.sleep(check_interval)
                
        except KeyboardInterrupt:
            print("\n停止监控新邮件")

# 使用示例
email_client = EmailClient(
    imap_server="imap.example.com",
    imap_port=993,
    username="your_username@example.com",
    password="your_password"
)

if email_client.connect():
    try:
        # 获取未读邮件
        unread_emails = email_client.get_unread_emails("INBOX", max_count=5)
        print(f"\n获取到 {len(unread_emails)} 封未读邮件:")
        for email in unread_emails:
            print(f"\n主题: {email['subject']}")
            print(f"发件人: {email['from']}")
            print(f"日期: {email['date']}")
            if "attachments" in email:
                print(f"附件: {email['attachments']} 个")
        
        # 监控新邮件（按Ctrl+C停止）
        email_client.monitor_new_emails("INBOX", check_interval=30)
        
    finally:
        email_client.disconnect()
```

## 最佳实践

1. **使用IMAP4_SSL**：使用IMAP4_SSL加密连接，提高通信安全性
2. **处理异常**：捕获并处理imaplib.IMAP4.error异常
3. **设置超时**：使用socket.setdefaulttimeout设置超时时间
4. **关闭连接**：使用logout方法关闭连接，释放资源
5. **使用只读模式**：对于不需要修改的操作，使用只读模式选择邮箱
6. **限制邮件数量**：使用搜索条件限制获取的邮件数量
7. **解码处理**：正确处理邮件内容的编码
8. **避免硬编码凭据**：从配置文件或环境变量读取用户名和密码

## 与其他模块的关系

- **email**：用于解析和构建电子邮件
- **smtplib**：用于发送电子邮件
- **poplib**：用于POP3协议接收电子邮件
- **imapclient**：第三方库，提供更高级的IMAP客户端API

## 总结

imaplib模块是Python中用于实现IMAP客户端功能的标准库，支持连接IMAP服务器、接收和管理电子邮件。通过IMAP4_SSL类，可以安全地连接IMAP服务器，执行列出邮箱、选择邮箱、搜索邮件、获取邮件内容、标记和删除邮件等操作。

在实际应用中，imaplib模块可以用于创建邮件客户端、邮件监控系统、邮件归档工具等。对于更复杂的邮件处理需求，可以考虑使用imapclient等第三方库。