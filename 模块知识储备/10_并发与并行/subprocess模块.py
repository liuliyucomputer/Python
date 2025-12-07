# subprocess模块详解

subprocess模块是Python标准库中用于创建和管理子进程的模块，它提供了比旧的os.system和os.spawn*函数更强大、更灵活的接口。

## 模块概述

subprocess模块主要提供以下功能：

- 创建子进程并执行外部命令
- 与子进程通信（输入/输出）
- 控制子进程的环境和工作目录
- 处理子进程的退出状态
- 支持管道和重定向
- 支持超时处理

## 基本概念

在使用subprocess模块之前，需要了解几个基本概念：

1. **子进程（Child Process）**：由当前进程创建的新进程，用于执行外部命令
2. **标准输入（stdin）**：子进程的输入流
3. **标准输出（stdout）**：子进程的输出流
4. **标准错误（stderr）**：子进程的错误输出流
5. **管道（Pipe）**：用于进程间通信的数据通道
6. **重定向（Redirection）**：将输入/输出流从默认设备重定向到其他设备或文件
7. **退出状态（Exit Status）**：子进程执行完成后的状态码，0表示成功，非0表示失败
8. **进程ID（PID）**：进程的唯一标识符

## 基本用法

### subprocess.run()

subprocess.run()是Python 3.5+中推荐使用的函数，用于执行外部命令并等待其完成。

```python
import subprocess

# 执行简单命令
result = subprocess.run(['ls', '-la'])
print(f"返回码: {result.returncode}")

# 捕获输出
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(f"标准输出:\n{result.stdout}")
print(f"标准错误:\n{result.stderr}")

# 检查返回码
result = subprocess.run(['ls', '-la'], check=True)
print("命令执行成功")

# 设置工作目录
result = subprocess.run(['ls', '-la'], cwd='/tmp')

# 设置环境变量
import os
env = os.environ.copy()
env['PATH'] = '/usr/local/bin:' + env['PATH']
result = subprocess.run(['ls', '-la'], env=env)

# 超时处理
try:
    result = subprocess.run(['sleep', '3'], timeout=2)
except subprocess.TimeoutExpired:
    print("命令执行超时")
```

### subprocess.Popen()

subprocess.Popen()是更底层的函数，用于创建子进程并与子进程通信。

```python
import subprocess

# 创建子进程
process = subprocess.Popen(['ls', '-la'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 等待子进程完成
stdout, stderr = process.communicate()

print(f"标准输出:\n{stdout}")
print(f"标准错误:\n{stderr}")
print(f"返回码: {process.returncode}")

# 实时获取输出
process = subprocess.Popen(['ping', '-c', '5', 'localhost'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)

while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())

return_code = process.poll()
print(f"返回码: {return_code}")

# 向子进程发送输入
process = subprocess.Popen(['grep', 'hello'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

stdout, stderr = process.communicate('hello world\nhello python\ngoodbye')

print(f"标准输出:\n{stdout}")
```

### 管道操作

```python
import subprocess

# 单个管道
p1 = subprocess.Popen(['ls', '-la'], stdout=subprocess.PIPE, text=True)
p2 = subprocess.Popen(['grep', '.py'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()  # 允许p1在p2结束时收到SIGPIPE
stdout, stderr = p2.communicate()

print(f"Python文件:\n{stdout}")

# 多个管道
p1 = subprocess.Popen(['ls', '-la'], stdout=subprocess.PIPE, text=True)
p2 = subprocess.Popen(['grep', '.py'], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
p1.stdout.close()  # 允许p1在p2结束时收到SIGPIPE
p3 = subprocess.Popen(['wc', '-l'], stdin=p2.stdout, stdout=subprocess.PIPE, text=True)
p2.stdout.close()  # 允许p2在p3结束时收到SIGPIPE
stdout, stderr = p3.communicate()

print(f"Python文件数量: {stdout.strip()}")
```

### 重定向

```python
import subprocess

# 重定向到文件
with open('output.txt', 'w') as f:
    subprocess.run(['ls', '-la'], stdout=f)

# 重定向到文件并追加
with open('output.txt', 'a') as f:
    subprocess.run(['date'], stdout=f)

# 合并标准输出和标准错误
result = subprocess.run(['ls', '-la', 'non_existent_file'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
print(f"输出:\n{result.stdout}")
```

## 高级用法

### 异步执行

```python
import subprocess
import time

# 异步执行命令
process = subprocess.Popen(['sleep', '3'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 执行其他操作
print("等待命令执行完成...")
time.sleep(1)
print("继续执行其他操作...")

# 等待命令完成
stdout, stderr = process.communicate()
print(f"命令执行完成，返回码: {process.returncode}")

# 轮询进程状态
process = subprocess.Popen(['sleep', '3'])

while process.poll() is None:
    print("命令正在执行...")
    time.sleep(0.5)

print(f"命令执行完成，返回码: {process.returncode}")
```

### 信号处理

```python
import subprocess
import time
import signal

# 发送信号给进程
process = subprocess.Popen(['sleep', '10'])
print(f"进程ID: {process.pid}")

# 等待2秒后发送SIGTERM信号
time.sleep(2)
process.terminate()

# 等待进程结束
stdout, stderr = process.communicate()
print(f"命令执行完成，返回码: {process.returncode}")

# 发送SIGKILL信号
process = subprocess.Popen(['sleep', '10'])
print(f"进程ID: {process.pid}")

# 等待2秒后发送SIGKILL信号
time.sleep(2)
process.kill()

# 等待进程结束
stdout, stderr = process.communicate()
print(f"命令执行完成，返回码: {process.returncode}")
```

### 环境变量

```python
import subprocess
import os

# 设置环境变量
env = os.environ.copy()
env['MY_VAR'] = 'my_value'

result = subprocess.run(['env'], env=env, capture_output=True, text=True)
print(f"环境变量:\n{result.stdout}")

# 清除环境变量
result = subprocess.run(['env'], env={}, capture_output=True, text=True)
print(f"环境变量:\n{result.stdout}")
```

### 子进程组

```python
import subprocess
import os
import signal
import time

# 创建子进程组
process = subprocess.Popen(['bash', '-c', 'sleep 5; echo child1; sleep 5'], preexec_fn=os.setsid)
print(f"进程ID: {process.pid}")

# 等待2秒后终止整个进程组
time.sleep(2)
os.killpg(os.getpgid(process.pid), signal.SIGTERM)

# 等待进程结束
stdout, stderr = process.communicate()
print(f"命令执行完成，返回码: {process.returncode}")
```

## 实际应用示例

### 示例1：执行命令并获取输出

```python
import subprocess

def run_command(command):
    """执行命令并返回输出"""
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout.strip()

# 获取当前目录下的文件列表
files = run_command(['ls', '-la'])
print(f"当前目录下的文件列表:\n{files}")

# 获取系统信息
os_info = run_command(['uname', '-a'])
print(f"系统信息: {os_info}")

# 获取Python版本
python_version = run_command(['python', '--version'])
print(f"Python版本: {python_version}")
```

### 示例2：批量处理文件

```python
import subprocess
import os

# 批量压缩文件
def batch_compress_files(directory, extension='.txt'):
    """批量压缩指定目录下的文件"""
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            compressed_path = f"{file_path}.gz"
            
            print(f"压缩文件: {file_path} -> {compressed_path}")
            
            # 使用gzip压缩文件
            subprocess.run(['gzip', '-c', file_path], stdout=open(compressed_path, 'wb'))

# 批量解压文件
def batch_decompress_files(directory, extension='.gz'):
    """批量解压指定目录下的文件"""
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            decompressed_path = file_path[:-3]  # 去掉.gz扩展名
            
            print(f"解压文件: {file_path} -> {decompressed_path}")
            
            # 使用gzip解压文件
            subprocess.run(['gzip', '-d', '-c', file_path], stdout=open(decompressed_path, 'wb'))

# 测试
# batch_compress_files('/tmp', '.txt')
# batch_decompress_files('/tmp', '.gz')
```

### 示例3：网络端口扫描

```python
import subprocess
import ipaddress

def scan_ports(host, start_port=1, end_port=1000):
    """扫描指定主机的端口"""
    open_ports = []
    
    print(f"扫描主机 {host} 的端口 {start_port}-{end_port}...")
    
    for port in range(start_port, end_port + 1):
        # 使用nc命令扫描端口
        result = subprocess.run(['nc', '-z', '-w', '1', host, str(port)], capture_output=True)
        
        if result.returncode == 0:
            open_ports.append(port)
            print(f"端口 {port} 开放")
    
    print(f"扫描完成，共发现 {len(open_ports)} 个开放端口")
    return open_ports

# 测试
# open_ports = scan_ports('127.0.0.1', start_port=1, end_port=100)
# print(f"开放端口: {open_ports}")
```

### 示例4：数据库备份

```python
import subprocess
import os
import datetime

def backup_database(database_name, username, password, backup_dir):
    """备份数据库"""
    # 创建备份目录
    os.makedirs(backup_dir, exist_ok=True)
    
    # 生成备份文件名
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(backup_dir, f"{database_name}_{timestamp}.sql")
    
    print(f"备份数据库 {database_name} 到 {backup_file}")
    
    # 使用mysqldump备份数据库
    command = [
        'mysqldump',
        '-u', username,
        f'--password={password}',
        database_name
    ]
    
    with open(backup_file, 'w') as f:
        result = subprocess.run(command, stdout=f, stderr=subprocess.PIPE, text=True)
    
    if result.returncode == 0:
        print("数据库备份成功")
        
        # 压缩备份文件
        compressed_file = f"{backup_file}.gz"
        print(f"压缩备份文件到 {compressed_file}")
        
        with open(backup_file, 'rb') as f_in:
            with open(compressed_file, 'wb') as f_out:
                subprocess.run(['gzip', '-c'], stdin=f_in, stdout=f_out)
        
        # 删除原始备份文件
        os.remove(backup_file)
        print("数据库备份压缩成功")
    else:
        print(f"数据库备份失败: {result.stderr}")

# 测试
# backup_database('test_db', 'root', 'password', '/tmp/backups')
```

### 示例5：并行执行命令

```python
import subprocess
import time

def run_parallel(commands):
    """并行执行命令"""
    processes = []
    
    # 启动所有命令
    for command in commands:
        print(f"启动命令: {' '.join(command)}")
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        processes.append(process)
    
    # 等待所有命令完成
    results = []
    for i, process in enumerate(processes):
        stdout, stderr = process.communicate()
        results.append({
            'command': commands[i],
            'stdout': stdout,
            'stderr': stderr,
            'returncode': process.returncode
        })
        
        if process.returncode == 0:
            print(f"命令 {' '.join(commands[i])} 执行成功")
        else:
            print(f"命令 {' '.join(commands[i])} 执行失败")
    
    return results

# 测试
commands = [
    ['sleep', '3'],
    ['echo', 'hello world'],
    ['ls', '-la'],
    ['python', '--version']
]

start_time = time.time()
results = run_parallel(commands)
end_time = time.time()

print(f"\n所有命令执行完成，耗时: {end_time - start_time:.2f}秒")

for result in results:
    print(f"\n命令: {' '.join(result['command'])}")
    print(f"返回码: {result['returncode']}")
    if result['stdout']:
        print(f"标准输出: {result['stdout'].strip()}")
    if result['stderr']:
        print(f"标准错误: {result['stderr'].strip()}")
```

## 最佳实践

1. **使用列表形式的命令**：避免使用shell=True，减少安全风险

```python
# 安全的方式
subprocess.run(['ls', '-la'])

# 不安全的方式（避免使用）
subprocess.run('ls -la', shell=True)
```

2. **检查返回码**：使用check=True确保命令执行成功

```python
# 检查返回码
try:
    result = subprocess.run(['ls', '-la'], check=True)
    print("命令执行成功")
except subprocess.CalledProcessError:
    print("命令执行失败")
```

3. **捕获输出**：使用capture_output=True捕获命令输出

```python
# 捕获输出
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(f"标准输出:\n{result.stdout}")
print(f"标准错误:\n{result.stderr}")
```

4. **使用text参数**：设置text=True（Python 3.7+）或universal_newlines=True（Python 3.6-）将输出转换为字符串

```python
# 将输出转换为字符串
result = subprocess.run(['ls', '-la'], capture_output=True, text=True)
print(f"标准输出:\n{result.stdout}")
```

5. **设置超时时间**：使用timeout参数避免命令无限期运行

```python
# 设置超时时间
try:
    result = subprocess.run(['sleep', '3'], timeout=2)
except subprocess.TimeoutExpired:
    print("命令执行超时")
```

6. **避免暴露密码**：不要在命令行参数中直接暴露密码

```python
# 不安全的方式（避免使用）
subprocess.run(['mysql', '-u', 'root', '--password=secret'])

# 安全的方式
import os
env = os.environ.copy()
env['MYSQL_PWD'] = 'secret'
subprocess.run(['mysql', '-u', 'root'], env=env)
```

7. **使用上下文管理器**：使用with语句确保资源正确释放

```python
# 使用上下文管理器
with open('output.txt', 'w') as f:
    subprocess.run(['ls', '-la'], stdout=f)
```

8. **处理异常**：捕获可能的异常并进行适当处理

```python
# 处理异常
try:
    result = subprocess.run(['ls', '-la', 'non_existent_file'], check=True)
except subprocess.CalledProcessError as e:
    print(f"命令执行失败，返回码: {e.returncode}")
except subprocess.TimeoutExpired:
    print("命令执行超时")
except FileNotFoundError:
    print("命令不存在")
```

## 与其他模块的关系

- **os模块**：subprocess模块替代了os.system、os.spawn*等函数
- **shlex模块**：用于解析命令行字符串
- **threading模块**：用于并发执行多个子进程
- **multiprocessing模块**：用于并行执行多个子进程
- **concurrent.futures模块**：用于更高级的并发控制

## 总结

subprocess模块是Python标准库中用于创建和管理子进程的模块，它提供了比旧的os.system和os.spawn*函数更强大、更灵活的接口。

subprocess模块的主要特点包括：

1. **简单易用**：提供了run()函数，用于执行简单命令
2. **灵活强大**：提供了Popen()类，用于更高级的进程管理
3. **安全可靠**：支持列表形式的命令，避免shell注入攻击
4. **功能丰富**：支持管道、重定向、超时处理等高级功能
5. **跨平台**：在Windows、Linux、macOS等平台上都能使用

subprocess模块在系统管理、自动化脚本、数据处理等领域非常有用，可以大大简化与外部命令的交互。

与其他模块相比，subprocess模块的优势在于：

1. **统一接口**：提供了统一的接口，替代了多个旧的函数
2. **安全性**：避免了shell注入攻击的风险
3. **灵活性**：支持各种高级功能，满足不同的需求
4. **可移植性**：在不同平台上都能使用相同的接口

总的来说，subprocess模块是Python中执行外部命令的首选工具，掌握它的使用可以大大提高自动化脚本的编写效率。