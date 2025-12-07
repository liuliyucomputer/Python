# smtplib模块详解

smtplib是Python中用于发送电子邮件的标准库，提供了SMTP（Simple Mail Transfer Protocol）客户端功能，用于连接SMTP服务器并发送邮件。

## 模块概述

smtplib模块提供了SMTP类和SMTP_SSL类，用于实现SMTP客户端功能，支持以下主要操作：

- 连接SMTP服务器
- 登录SMTP服务器
- 发送电子邮件（包括文本、HTML和附件）
- 使用TLS/SSL加密

## 基本用法

### 发送简单邮件

```python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_simple_email():
    """发送简单邮件"""
    # 邮件配置
    smtp_server = "smtp.example.com"  # SMTP服务器地址
    smtp_port = 587  # SMTP服务器端口
    username = "your_username@example.com"  # 用户名
    password = "your_password"  # 密码
    
    sender = "your_username@example.com"  # 发件人地址
    receiver = "recipient@example.com"  # 收件人地址
    
    # 邮件内容
    subject = "测试邮件"
    body = "这是一封来自Python的测试邮件！"
    
    # 创建MIMEText对象
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    
    try:
        # 创建SMTP连接
        server = smtplib.SMTP(smtp_server, smtp_port)
        
        # 启用TLS加密
        server.starttls()
        
        # 登录SMTP服务器
        server.login(username, password)
        
        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())
        print("邮件发送成功")
        
    except Exception as e:
        print(f"邮件发送失败: {e}")
    finally:
        # 关闭连接
        server.quit()

# 示例
send_simple_email()
```

### 使用上下文管理器

```python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email_with_context():
    """使用上下文管理器发送邮件"""
    # 邮件配置
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_username@example.com"
    password = "your_password"
    
    sender = "your_username@example.com"
    receiver = "recipient@example.com"
    
    # 邮件内容
    subject = "上下文管理器测试邮件"
    body = "这是使用上下文管理器发送的测试邮件！"
    
    # 创建MIMEText对象
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    
    try:
        # 使用上下文管理器
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("邮件发送成功")
            
    except Exception as e:
        print(f"邮件发送失败: {e}")

# 示例
send_email_with_context()
```

## 发送HTML邮件

```python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_html_email():
    """发送HTML邮件"""
    # 邮件配置
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_username@example.com"
    password = "your_password"
    
    sender = "your_username@example.com"
    receiver = "recipient@example.com"
    
    # HTML邮件内容
    subject = "HTML测试邮件"
    html_body = """
    <html>
    <body>
        <h1 style="color: blue;">Python HTML邮件测试</h1>
        <p>这是一封带有HTML格式的邮件：</p>
        <ul>
            <li>项目1：Python</li>
            <li>项目2：smtplib</li>
            <li>项目3：email</li>
        </ul>
        <p><a href="https://www.python.org">访问Python官网</a></p>
    </body>
    </html>
    """
    
    # 创建HTML格式的MIMEText对象
    msg = MIMEText(html_body, "html", "utf-8")
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("HTML邮件发送成功")
            
    except Exception as e:
        print(f"HTML邮件发送失败: {e}")

# 示例
send_html_email()
```

## 发送带附件的邮件

```python
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

def send_email_with_attachment():
    """发送带附件的邮件"""
    # 邮件配置
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_username@example.com"
    password = "your_password"
    
    sender = "your_username@example.com"
    receiver = "recipient@example.com"
    
    # 邮件内容
    subject = "带附件的测试邮件"
    body = "这是一封带有附件的测试邮件！"
    
    # 创建MIMEMultipart对象
    msg = MIMEMultipart()
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    
    # 添加正文
    msg.attach(MIMEText(body, "plain", "utf-8"))
    
    # 添加附件
    attachment_path = "test.txt"
    if os.path.exists(attachment_path):
        with open(attachment_path, "rb") as f:
            part = MIMEApplication(f.read())
            part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
            msg.attach(part)
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("带附件的邮件发送成功")
            
    except Exception as e:
        print(f"带附件的邮件发送失败: {e}")

# 示例
send_email_with_attachment()
```

## 发送多附件邮件

```python
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

def send_email_with_multiple_attachments():
    """发送多附件邮件"""
    # 邮件配置
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_username@example.com"
    password = "your_password"
    
    sender = "your_username@example.com"
    receiver = "recipient@example.com"
    
    # 邮件内容
    subject = "多附件测试邮件"
    body = "这是一封带有多个附件的测试邮件！"
    
    # 创建MIMEMultipart对象
    msg = MIMEMultipart()
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    
    # 添加正文
    msg.attach(MIMEText(body, "plain", "utf-8"))
    
    # 添加多个附件
    attachment_paths = ["test1.txt", "test2.txt", "test3.txt"]
    
    for attachment_path in attachment_paths:
        if os.path.exists(attachment_path):
            with open(attachment_path, "rb") as f:
                part = MIMEApplication(f.read())
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
                msg.attach(part)
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("多附件邮件发送成功")
            
    except Exception as e:
        print(f"多附件邮件发送失败: {e}")

# 示例
send_email_with_multiple_attachments()
```

## 发送带图片的HTML邮件

```python
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header

def send_html_email_with_images():
    """发送带图片的HTML邮件"""
    # 邮件配置
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_username@example.com"
    password = "your_password"
    
    sender = "your_username@example.com"
    receiver = "recipient@example.com"
    
    # 邮件内容
    subject = "带图片的HTML测试邮件"
    
    # HTML内容，引用图片ID
    html_body = """
    <html>
    <body>
        <h1>Python HTML邮件测试</h1>
        <p>这是一封带有图片的HTML邮件：</p>
        <img src="cid:image1" alt="图片1" width="300">
        <img src="cid:image2" alt="图片2" width="300">
    </body>
    </html>
    """
    
    # 创建MIMEMultipart对象
    msg = MIMEMultipart("related")
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    
    # 添加HTML正文
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    
    # 添加图片附件
    image_paths = ["image1.png", "image2.png"]
    image_ids = ["image1", "image2"]
    
    for image_path, image_id in zip(image_paths, image_ids):
        if os.path.exists(image_path):
            with open(image_path, "rb") as f:
                img = MIMEImage(f.read())
                img.add_header("Content-ID", f"<{image_id}>")
                img.add_header("Content-Disposition", f"inline; filename={os.path.basename(image_path)}")
                msg.attach(img)
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("带图片的HTML邮件发送成功")
            
    except Exception as e:
        print(f"带图片的HTML邮件发送失败: {e}")

# 示例
send_html_email_with_images()
```

## 高级功能

### 发送给多个收件人

```python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email_to_multiple_recipients():
    """发送给多个收件人"""
    # 邮件配置
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_username@example.com"
    password = "your_password"
    
    sender = "your_username@example.com"
    receivers = ["recipient1@example.com", "recipient2@example.com", "recipient3@example.com"]  # 多个收件人
    
    # 邮件内容
    subject = "发送给多个收件人的测试邮件"
    body = "这是一封发送给多个收件人的测试邮件！"
    
    # 创建MIMEText对象
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(", ".join(receivers), "utf-8")  # 多个收件人用逗号分隔
    msg["Subject"] = Header(subject, "utf-8")
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, receivers, msg.as_string())
            print(f"邮件发送给 {len(receivers)} 个收件人成功")
            
    except Exception as e:
        print(f"邮件发送失败: {e}")

# 示例
send_email_to_multiple_recipients()
```

### 使用SMTP_SSL

```python
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email_with_ssl():
    """使用SMTP_SSL发送邮件"""
    # 邮件配置
    smtp_server = "smtp.example.com"
    smtp_port = 465  # SMTP_SSL服务器端口
    username = "your_username@example.com"
    password = "your_password"
    
    sender = "your_username@example.com"
    receiver = "recipient@example.com"
    
    # 邮件内容
    subject = "SMTP_SSL测试邮件"
    body = "这是使用SMTP_SSL发送的测试邮件！"
    
    # 创建MIMEText对象
    msg = MIMEText(body, "plain", "utf-8")
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    
    try:
        # 使用SMTP_SSL
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("SMTP_SSL邮件发送成功")
            
    except Exception as e:
        print(f"SMTP_SSL邮件发送失败: {e}")

# 示例
send_email_with_ssl()
```

## 实际应用示例

### 示例1：监控报警邮件

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import datetime
import psutil

def get_system_info():
    """获取系统信息"""
    # 获取CPU使用率
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # 获取内存使用率
    mem_info = psutil.virtual_memory()
    mem_percent = mem_info.percent
    mem_used = mem_info.used / 1024 / 1024  # MB
    mem_total = mem_info.total / 1024 / 1024  # MB
    
    # 获取磁盘使用率
    disk_info = psutil.disk_usage('/')
    disk_percent = disk_info.percent
    disk_used = disk_info.used / 1024 / 1024 / 1024  # GB
    disk_total = disk_info.total / 1024 / 1024 / 1024  # GB
    
    return {
        "cpu_percent": cpu_percent,
        "mem_percent": mem_percent,
        "mem_used": mem_used,
        "mem_total": mem_total,
        "disk_percent": disk_percent,
        "disk_used": disk_used,
        "disk_total": disk_total
    }

def send_alert_email(system_info):
    """发送监控报警邮件"""
    # 邮件配置
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_username@example.com"
    password = "your_password"
    
    sender = "your_username@example.com"
    receiver = "admin@example.com"
    
    # 邮件内容
    subject = "系统监控报警"
    
    # HTML内容
    html_body = f"""
    <html>
    <body>
        <h1>系统监控报警</h1>
        <p>报警时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <table border="1" cellpadding="5">
            <tr>
                <th>指标</th>
                <th>当前值</th>
                <th>阈值</th>
            </tr>
            <tr>
                <td>CPU使用率</td>
                <td style="color: {'red' if system_info['cpu_percent'] > 80 else 'black'}">
                    {system_info['cpu_percent']}%
                </td>
                <td>80%</td>
            </tr>
            <tr>
                <td>内存使用率</td>
                <td style="color: {'red' if system_info['mem_percent'] > 80 else 'black'}">
                    {system_info['mem_percent']}% ({system_info['mem_used']:.1f}MB/{system_info['mem_total']:.1f}MB)
                </td>
                <td>80%</td>
            </tr>
            <tr>
                <td>磁盘使用率</td>
                <td style="color: {'red' if system_info['disk_percent'] > 80 else 'black'}">
                    {system_info['disk_percent']}% ({system_info['disk_used']:.1f}GB/{system_info['disk_total']:.1f}GB)
                </td>
                <td>80%</td>
            </tr>
        </table>
        <p>请及时处理！</p>
    </body>
    </html>
    """
    
    # 创建MIMEMultipart对象
    msg = MIMEMultipart()
    msg["From"] = Header(sender, "utf-8")
    msg["To"] = Header(receiver, "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    
    # 添加HTML正文
    msg.attach(MIMEText(html_body, "html", "utf-8"))
    
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, receiver, msg.as_string())
            print("监控报警邮件发送成功")
            
    except Exception as e:
        print(f"监控报警邮件发送失败: {e}")

# 示例
system_info = get_system_info()
print("系统信息:")
print(f"CPU使用率: {system_info['cpu_percent']}%")
print(f"内存使用率: {system_info['mem_percent']}%")
print(f"磁盘使用率: {system_info['disk_percent']}%")

# 检查是否需要发送报警邮件
if (system_info['cpu_percent'] > 80 or 
    system_info['mem_percent'] > 80 or 
    system_info['disk_percent'] > 80):
    send_alert_email(system_info)
else:
    print("系统指标正常，无需发送报警邮件")
```

### 示例2：邮件发送工具类

```python
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.header import Header

class EmailSender:
    def __init__(self, smtp_server, smtp_port, username, password):
        """初始化邮件发送器"""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
    
    def send_text_email(self, sender, receivers, subject, body):
        """发送文本邮件"""
        msg = MIMEText(body, "plain", "utf-8")
        msg["From"] = Header(sender, "utf-8")
        msg["To"] = Header(", ".join(receivers), "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        
        self._send_email(sender, receivers, msg)
    
    def send_html_email(self, sender, receivers, subject, html_body):
        """发送HTML邮件"""
        msg = MIMEText(html_body, "html", "utf-8")
        msg["From"] = Header(sender, "utf-8")
        msg["To"] = Header(", ".join(receivers), "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        
        self._send_email(sender, receivers, msg)
    
    def send_email_with_attachments(self, sender, receivers, subject, body, attachment_paths):
        """发送带附件的邮件"""
        msg = MIMEMultipart()
        msg["From"] = Header(sender, "utf-8")
        msg["To"] = Header(", ".join(receivers), "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        
        # 添加正文
        msg.attach(MIMEText(body, "plain", "utf-8"))
        
        # 添加附件
        for attachment_path in attachment_paths:
            if os.path.exists(attachment_path):
                with open(attachment_path, "rb") as f:
                    part = MIMEApplication(f.read())
                    part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(attachment_path)}")
                    msg.attach(part)
        
        self._send_email(sender, receivers, msg)
    
    def send_html_email_with_images(self, sender, receivers, subject, html_body, image_paths, image_ids):
        """发送带图片的HTML邮件"""
        msg = MIMEMultipart("related")
        msg["From"] = Header(sender, "utf-8")
        msg["To"] = Header(", ".join(receivers), "utf-8")
        msg["Subject"] = Header(subject, "utf-8")
        
        # 添加HTML正文
        msg.attach(MIMEText(html_body, "html", "utf-8"))
        
        # 添加图片附件
        for image_path, image_id in zip(image_paths, image_ids):
            if os.path.exists(image_path):
                with open(image_path, "rb") as f:
                    img = MIMEImage(f.read())
                    img.add_header("Content-ID", f"<{image_id}>")
                    img.add_header("Content-Disposition", f"inline; filename={os.path.basename(image_path)}")
                    msg.attach(img)
        
        self._send_email(sender, receivers, msg)
    
    def _send_email(self, sender, receivers, msg):
        """发送邮件"""
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.username, self.password)
                server.sendmail(sender, receivers, msg.as_string())
                print(f"邮件发送成功，发件人: {sender}, 收件人: {', '.join(receivers)}")
                
        except Exception as e:
            print(f"邮件发送失败: {e}")

# 使用示例
# 初始化邮件发送器
email_sender = EmailSender(
    smtp_server="smtp.example.com",
    smtp_port=587,
    username="your_username@example.com",
    password="your_password"
)

# 发送文本邮件
email_sender.send_text_email(
    sender="your_username@example.com",
    receivers=["recipient@example.com"],
    subject="测试邮件",
    body="这是一封来自Python的测试邮件！"
)

# 发送带附件的邮件
email_sender.send_email_with_attachments(
    sender="your_username@example.com",
    receivers=["recipient@example.com"],
    subject="带附件的测试邮件",
    body="这是一封带有附件的测试邮件！",
    attachment_paths=["test1.txt", "test2.txt"]
)
```

## 最佳实践

1. **使用上下文管理器**：使用`with`语句自动关闭连接
2. **处理异常**：捕获并处理smtplib.SMTPException异常
3. **使用TLS/SSL**：启用TLS或使用SMTP_SSL加密连接
4. **避免硬编码凭据**：从配置文件或环境变量读取用户名和密码
5. **验证收件人**：验证收件人邮箱地址格式
6. **限制邮件大小**：避免发送过大的邮件
7. **使用合适的端口**：
   - SMTP with STARTTLS: 587
   - SMTP_SSL: 465
8. **使用邮件队列**：对于大量邮件，使用邮件队列系统

## 与其他模块的关系

- **email**：用于创建和解析电子邮件
- **imaplib**：用于接收电子邮件
- **poplib**：用于接收电子邮件
- **yagmail**：第三方库，提供更简洁的邮件发送API

## 总结

smtplib模块是Python中发送电子邮件的标准库，提供了SMTP客户端功能。通过smtplib，可以连接SMTP服务器，发送文本邮件、HTML邮件、带附件的邮件等。

在实际应用中，smtplib模块可以用于创建邮件客户端、监控报警系统、自动报告系统等。对于更复杂的邮件需求，可以考虑使用yagmail等第三方库。