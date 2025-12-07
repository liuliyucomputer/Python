# subprocess模块详解

subprocess模块是Python中用于创建和管理子进程的标准库，提供了执行系统命令、管理子进程输入输出和错误流、获取命令执行结果等功能。

## 模块概述

subprocess模块提供了以下主要功能：

- 执行系统命令
- 管理子进程的输入输出流
- 获取命令执行结果和退出码
- 支持同步和异步执行命令
- 支持shell和非shell模式
- 支持命令行参数的安全传递

## 基本用法

### 导入模块

```python
import subprocess
```

### 执行简单命令

```python
# 执行简单命令，等待命令完成
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print(f"命令退出码: {result.returncode}")
print(f"命令输出:\n{result.stdout}")
print(f"命令错误:\n{result.stderr}")

# 执行ls命令（Linux/Mac）
# result = subprocess.run(["ls", "-la"], capture_output=True, text=True)
# print(f"命令退出码: {result.returncode}")
# print(f"命令输出:\n{result.stdout}")
```

### 捕获输出

```python
# 捕获标准输出
output = subprocess.check_output(["echo", "Hello, World!"]).decode("utf-8")
print(f"命令输出: {output.strip()}")

# 捕获标准输出和标准错误
result = subprocess.run(["python", "-c", "print('stdout'); import sys; sys.stderr.write('stderr\n')"], 
                      capture_output=True, text=True)
print(f"标准输出: {result.stdout.strip()}")
print(f"标准错误: {result.stderr.strip()}")
```

### 处理错误

```python
# 使用check_call检查命令是否执行成功
try:
    subprocess.check_call(["python", "-c", "exit(0)"])
    print("命令执行成功")
except subprocess.CalledProcessError as e:
    print(f"命令执行失败: {e}")

# 使用check_output检查命令是否执行成功
try:
    output = subprocess.check_output(["python", "-c", "print('success'); exit(0)"]).decode("utf-8")
    print(f"命令输出: {output.strip()}")
except subprocess.CalledProcessError as e:
    print(f"命令执行失败: {e}")
```

### 传递参数

```python
# 安全传递参数（推荐）
filename = "test.txt"
result = subprocess.run(["echo", "文件名:", filename], capture_output=True, text=True)
print(f"命令输出: {result.stdout.strip()}")

# 使用shell=True传递参数（不推荐，存在安全风险）
filename = "test.txt"
result = subprocess.run(f"echo 文件名: {filename}", shell=True, capture_output=True, text=True)
print(f"命令输出: {result.stdout.strip()}")
```

### 环境变量

```python
# 使用默认环境变量
result = subprocess.run(["echo", "$PATH"], shell=True, capture_output=True, text=True)
print(f"默认PATH: {result.stdout.strip()}")

# 使用自定义环境变量
import os

my_env = os.environ.copy()
my_env["MY_VAR"] = "my_value"

result = subprocess.run(["python", "-c", "import os; print(os.environ.get('MY_VAR'))"], 
                      env=my_env, capture_output=True, text=True)
print(f"自定义环境变量: {result.stdout.strip()}")
```

## 高级功能

### 管道通信

```python
# 单个命令的管道
result = subprocess.run(["echo", "Hello, World!
This is a test."], 
                      capture_output=True, text=True)

# 两个命令的管道（Linux/Mac）
# result = subprocess.run("echo 'Hello, World!' | grep 'World'", 
#                       shell=True, capture_output=True, text=True)
# print(f"管道命令输出: {result.stdout.strip()}")

# 使用subprocess实现管道
p1 = subprocess.Popen(["echo", "Hello, World!
This is a test."], 
                     stdout=subprocess.PIPE, text=True)
p2 = subprocess.Popen(["findstr", "World"], stdin=p1.stdout, 
                     stdout=subprocess.PIPE, text=True)
p1.stdout.close()  # 关闭p1的stdout，让p1在p2结束时也能结束
output, _ = p2.communicate()
print(f"管道命令输出: {output.strip()}")
```

### 实时输出

```python
# 实时获取命令输出
process = subprocess.Popen(["ping", "www.google.com"], 
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                          text=True, bufsize=1)

print("正在执行ping命令，按Ctrl+C停止...")

try:
    for line in process.stdout:
        print(line.strip())
    process.wait()
    print(f"命令退出码: {process.returncode}")
except KeyboardInterrupt:
    process.terminate()
    print("命令已终止")
```

### 超时控制

```python
# 设置命令执行超时
try:
    result = subprocess.run(["ping", "www.google.com", "-n", "10"], 
                          capture_output=True, text=True, timeout=5)
    print(f"命令输出:\n{result.stdout}")
except subprocess.TimeoutExpired:
    print("命令执行超时")
```

### 后台执行命令

```python
# 后台执行命令
process = subprocess.Popen(["python", "-c", "import time; time.sleep(10); print('Done')"], 
                          stdout=subprocess.PIPE, text=True)

print(f"后台进程ID: {process.pid}")
print(f"进程是否正在运行: {process.poll() is None}")

# 等待进程完成
process.wait()
print(f"进程退出码: {process.returncode}")
print(f"进程输出: {process.stdout.read().strip()}")
```

### 输入传递

```python
# 向进程传递输入
process = subprocess.Popen(["python", "-c", "input_text = input(); print(f'You entered: {input_text}')"], 
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

# 传递输入并获取输出
output, _ = process.communicate(input="Hello from subprocess")
print(f"进程输出: {output.strip()}")
```

## 实际应用示例

### 示例1：执行外部程序并处理输出

```python
import subprocess

def run_external_program(program_path, args=None, timeout=None):
    """执行外部程序并返回结果"""
    if args is None:
        args = []
    
    try:
        # 构建命令列表
        cmd = [program_path] + args
        
        # 执行命令
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        
        # 返回结果
        return {
            "success": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "error": "Command timed out"
        }
    except FileNotFoundError:
        return {
            "success": False,
            "error": f"Program not found: {program_path}"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# 示例
# result = run_external_program("python", ["--version"])
# print(f"执行结果: {result}")
```

### 示例2：批量执行命令

```python
import subprocess

def batch_run_commands(commands, shell=True):
    """批量执行命令并返回结果"""
    results = []
    
    for cmd in commands:
        print(f"执行命令: {cmd}")
        
        try:
            if shell:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            else:
                result = subprocess.run(cmd, capture_output=True, text=True)
            
            results.append({
                "command": cmd,
                "success": result.returncode == 0,
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            })
            
            print(f"  退出码: {result.returncode}")
            if result.stdout:
                print(f"  输出: {result.stdout.strip()}")
            if result.stderr:
                print(f"  错误: {result.stderr.strip()}")
                
        except Exception as e:
            results.append({
                "command": cmd,
                "success": False,
                "error": str(e)
            })
            print(f"  错误: {e}")
        
        print()
    
    return results

# 示例
# commands = [
#     "echo 'Command 1'",
#     "echo 'Command 2'",
#     "echo 'Command 3'"
# ]
# 
# results = batch_run_commands(commands)
# print(f"执行完成，共执行 {len(results)} 个命令")
# print(f"成功: {sum(1 for r in results if r['success'])}")
# print(f"失败: {sum(1 for r in results if not r['success'])}")
```

### 示例3：文件压缩

```python
import subprocess
import os

def compress_file(file_path, output_path=None):
    """使用zip命令压缩文件"""
    if not os.path.exists(file_path):
        return False, "文件不存在"
    
    if output_path is None:
        output_path = file_path + ".zip"
    
    try:
        # 使用zip命令压缩文件
        result = subprocess.run(["zip", output_path, file_path], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            return True, f"文件已压缩为: {output_path}"
        else:
            return False, f"压缩失败: {result.stderr}"
    except Exception as e:
        return False, f"压缩失败: {str(e)}"

# 示例
# success, message = compress_file("test.txt")
# print(f"压缩结果: {success}, {message}")
```

### 示例4：执行SQL脚本

```python
import subprocess

def execute_sql_script(database, username, password, script_path):
    """使用mysql命令执行SQL脚本"""
    try:
        # 构建命令
        cmd = f"mysql -u {username} -p{password} {database} < {script_path}"
        
        # 执行命令
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            return True, "SQL脚本执行成功"
        else:
            return False, f"SQL脚本执行失败: {result.stderr}"
    except Exception as e:
        return False, f"SQL脚本执行失败: {str(e)}"

# 示例
# success, message = execute_sql_script("mydb", "root", "password", "script.sql")
# print(f"SQL脚本执行结果: {success}, {message}")
```

### 示例5：监控网络连接

```python
import subprocess
import time

def monitor_network_connections(interval=5, duration=30):
    """监控网络连接"""
    end_time = time.time() + duration
    
    print(f"开始监控网络连接，每 {interval} 秒一次，持续 {duration} 秒...")
    
    while time.time() < end_time:
        print(f"\n监控时间: {time.strftime('%H:%M:%S')}")
        
        try:
            # 执行netstat命令
            result = subprocess.run(["netstat", "-an"], capture_output=True, text=True)
            
            if result.returncode == 0:
                # 显示前10行输出
                lines = result.stdout.split("\n")
                for line in lines[:10]:
                    print(line)
                print(f"... 共 {len(lines)} 行")
            else:
                print(f"netstat命令执行失败: {result.stderr}")
                
        except Exception as e:
            print(f"监控失败: {str(e)}")
        
        # 等待指定时间
        time.sleep(interval)
    
    print("\n网络连接监控结束")

# 示例
# monitor_network_connections(interval=2, duration=10)
```

## 最佳实践

1. **使用列表形式传递命令**：使用列表形式传递命令可以避免shell注入攻击，提高安全性
2. **使用text参数**：设置text=True可以将输出作为字符串处理，方便后续操作
3. **捕获输出**：使用capture_output=True可以捕获命令的输出和错误信息
4. **检查退出码**：使用result.returncode检查命令是否执行成功
5. **使用check_output/check_call**：对于不需要复杂控制的命令，可以使用check_output或check_call简化代码
6. **设置超时**：对于可能长时间运行的命令，设置timeout参数避免程序卡死
7. **使用Popen进行复杂控制**：对于需要实时交互或复杂控制的命令，使用Popen类
8. **关闭文件描述符**：在使用管道时，记得关闭不需要的文件描述符，避免资源泄漏
9. **处理异常**：捕获并处理可能的异常，如FileNotFoundError、TimeoutExpired等
10. **避免使用shell=True**：除非必要，否则避免使用shell=True，因为它存在安全风险

## 与其他模块的关系

- **os.system**：os.system是subprocess的前身，功能相对简单
- **os.popen**：os.popen提供了更简单的管道通信功能
- **shutil**：shutil模块提供了高级文件操作功能，可以与subprocess结合使用
- **tempfile**：tempfile模块提供了临时文件和目录的创建功能，可以与subprocess结合使用

## 总结

subprocess模块是Python中用于执行系统命令和管理子进程的核心模块，提供了丰富的功能，包括命令执行、输出捕获、管道通信、实时输出等。通过subprocess模块，可以编写与系统交互的Python程序，执行各种系统命令和外部程序。

在实际应用中，subprocess模块常用于执行系统命令、调用外部程序、批量处理任务等场景。使用subprocess模块时，需要注意安全性和错误处理，避免shell注入攻击，并正确处理命令执行过程中可能出现的异常。