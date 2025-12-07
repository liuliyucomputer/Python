# sys模块详解

sys模块是Python中用于与Python解释器和系统交互的标准库，提供了访问解释器内部信息和控制解释器行为的功能。

## 模块概述

sys模块提供了以下主要功能：

- 访问命令行参数
- 控制Python解释器的输入输出流
- 获取系统路径和模块搜索路径
- 获取Python解释器的版本信息
- 控制解释器的退出
- 处理异常和追踪信息
- 访问系统相关信息

## 基本用法

### 导入模块

```python
import sys
```

### 命令行参数

```python
# 获取命令行参数
print(f"命令行参数: {sys.argv}")
print(f"参数数量: {len(sys.argv)}")

# 脚本名称
script_name = sys.argv[0]
print(f"脚本名称: {script_name}")

# 其他参数
if len(sys.argv) > 1:
    print(f"第一个参数: {sys.argv[1]}")
    print(f"所有其他参数: {sys.argv[1:]}")
```

### 输入输出流

```python
# 标准输入
print("请输入内容:")
user_input = sys.stdin.readline()
print(f"您输入的内容: {user_input.strip()}")

# 标准输出
sys.stdout.write("这是通过sys.stdout输出的内容\n")

# 标准错误输出
sys.stderr.write("这是通过sys.stderr输出的错误信息\n")

# 重定向输出
with open("output.txt", "w") as f:
    original_stdout = sys.stdout
    sys.stdout = f
    print("这段内容将写入到文件中")
    sys.stdout = original_stdout  # 恢复原始输出

print("这段内容将显示在控制台")
```

### 路径和模块搜索路径

```python
# 获取Python解释器路径
print(f"Python解释器路径: {sys.executable}")

# 获取Python版本信息
print(f"Python版本: {sys.version}")
print(f"Python版本信息: {sys.version_info}")
print(f"Python主版本号: {sys.version_info.major}")
print(f"Python次版本号: {sys.version_info.minor}")
print(f"Python修订版本号: {sys.version_info.micro}")

# 获取模块搜索路径
print(f"模块搜索路径: {sys.path}")

# 添加自定义路径到模块搜索路径
sys.path.append("/path/to/custom/modules")
print(f"更新后的模块搜索路径: {sys.path}")
```

### 解释器控制

```python
# 获取最大递归深度
print(f"最大递归深度: {sys.getrecursionlimit()}")

# 设置最大递归深度
sys.setrecursionlimit(2000)
print(f"更新后的最大递归深度: {sys.getrecursionlimit()}")

# 获取默认编码
print(f"默认编码: {sys.getdefaultencoding()}")

# 获取文件系统编码
print(f"文件系统编码: {sys.getfilesystemencoding()}")

# 获取平台信息
print(f"平台: {sys.platform}")  # win32表示Windows, linux表示Linux, darwin表示macOS

# 获取字节序
print(f"字节序: {sys.byteorder}")  # little表示小端, big表示大端
```

### 退出程序

```python
# 正常退出
sys.exit(0)  # 退出码0表示成功

# 异常退出
sys.exit(1)  # 退出码非0表示失败

# 带消息退出
sys.exit("程序因错误而退出")
```

## 高级功能

### 异常和追踪信息

```python
# 获取当前异常信息
try:
    1 / 0
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"异常类型: {exc_type}")
    print(f"异常值: {exc_value}")
    print(f"异常追踪对象: {exc_traceback}")

# 打印异常追踪信息
import traceback

try:
    1 / 0
except Exception:
    traceback.print_exc(file=sys.stdout)
```

### 内存使用信息

```python
# 获取内存使用信息（需要sys模块和psutil模块）
try:
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    print(f"进程ID: {os.getpid()}")
    print(f"物理内存使用: {memory_info.rss / 1024 / 1024:.2f} MB")
    print(f"虚拟内存使用: {memory_info.vms / 1024 / 1024:.2f} MB")
    print(f"共享内存: {memory_info.shared / 1024 / 1024:.2f} MB")
    print(f"文本段内存: {memory_info.text / 1024 / 1024:.2f} MB")
    print(f"数据段内存: {memory_info.data / 1024 / 1024:.2f} MB")
except ImportError:
    print("psutil模块未安装，无法获取详细内存信息")
```

### 资源限制

```python
# 获取和设置资源限制（Windows上可能无法正常工作）
try:
    # 获取最大文件描述符数
    print(f"最大文件描述符数: {sys.getdtablesize()}")
    
    # 获取CPU时间
    print(f"用户CPU时间: {sys.getcpuclockid()}")
except AttributeError as e:
    print(f"此平台不支持该功能: {e}")
```

### 线程和进程信息

```python
# 获取线程信息
print(f"线程数量: {sys.getsizeof([])}")  # 这不是真正的线程数量，仅示例

# 获取进程信息
print(f"进程信息: {sys.argv[0]}")
```

### 性能计数器

```python
# 获取性能计数器
print(f"性能计数器: {sys.thread_info}")
print(f"线程名称: {sys.thread_info.name}")
print(f"线程锁类型: {sys.thread_info.lock}")
print(f"线程版本: {sys.thread_info.version}")
```

## 实际应用示例

### 示例1：命令行参数解析

```python
import sys

def parse_arguments():
    """解析命令行参数"""
    if len(sys.argv) < 2:
        print("用法: python script.py [options]")
        print("选项:")
        print("  -h, --help    显示帮助信息")
        print("  -v, --verbose 启用详细输出")
        print("  -o, --output <file> 指定输出文件")
        sys.exit(1)
    
    args = {
        "verbose": False,
        "output": None
    }
    
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] in ("-h", "--help"):
            print("帮助信息...")
            sys.exit(0)
        elif sys.argv[i] in ("-v", "--verbose"):
            args["verbose"] = True
        elif sys.argv[i] in ("-o", "--output"):
            if i + 1 < len(sys.argv):
                args["output"] = sys.argv[i + 1]
                i += 1
            else:
                print("错误: --output选项需要一个参数")
                sys.exit(1)
        else:
            print(f"未知选项: {sys.argv[i]}")
            sys.exit(1)
        i += 1
    
    return args

# 示例
# args = parse_arguments()
# print(f"命令行参数: {args}")
```

### 示例2：进度条实现

```python
import sys
import time

def progress_bar(iterable, total=None, prefix="", suffix="", decimals=1, length=50, fill="█"):
    """显示进度条"""
    if total is None:
        total = len(iterable)
    
    # 格式化百分比
    format_str = f"{{0}}{{1:.{decimals}f}}% {{2}}"
    
    # 初始进度
    filled_length = 0
    previous = 0
    
    for i, item in enumerate(iterable):
        # 计算进度
        percent = (i + 1) / total * 100
        filled_length = int(length * (i + 1) // total)
        
        # 更新进度条
        if percent - previous >= 0.1:  # 每0.1%更新一次
            bar = fill * filled_length + "-" * (length - filled_length)
            sys.stdout.write("\r" + format_str.format(prefix, percent, bar) + suffix)
            sys.stdout.flush()
            previous = percent
        
        yield item
    
    # 完成进度条
    bar = fill * length
    sys.stdout.write("\r" + format_str.format(prefix, 100, bar) + suffix + "\n")
    sys.stdout.flush()

# 示例
# items = list(range(100))
# for item in progress_bar(items, prefix="处理中:", suffix="完成", length=30):
#     time.sleep(0.01)  # 模拟处理时间
```

### 示例3：动态导入模块

```python
import sys

def dynamic_import(module_name):
    """动态导入模块"""
    try:
        # 检查模块是否已导入
        if module_name in sys.modules:
            return sys.modules[module_name]
        
        # 动态导入模块
        __import__(module_name)
        return sys.modules[module_name]
    except ImportError:
        print(f"无法导入模块: {module_name}")
        return None

# 示例
# math_module = dynamic_import("math")
# if math_module:
#     print(f"π的值: {math_module.pi}")
#     print(f"sin(π/2): {math_module.sin(math_module.pi/2)}")

# os_module = dynamic_import("os")
# if os_module:
#     print(f"当前工作目录: {os_module.getcwd()}")
```

### 示例4：退出处理

```python
import sys
import atexit

def cleanup():
    """程序退出时的清理函数"""
    print("执行清理操作...")
    print("关闭文件...")
    print("释放资源...")
    print("程序已退出")

# 注册退出处理函数
atexit.register(cleanup)

# 模拟程序执行
print("程序开始执行...")

# 检查命令行参数
if len(sys.argv) < 2:
    print("错误: 缺少必要参数")
    sys.exit(1)

# 执行主程序逻辑
print(f"处理参数: {sys.argv[1]}")
print("程序执行完成")

# 正常退出
sys.exit(0)
```

### 示例5：调试信息输出控制

```python
import sys

# 定义调试级别
DEBUG = 0
INFO = 1
WARNING = 2
ERROR = 3
CRITICAL = 4

# 当前日志级别
LOG_LEVEL = INFO

def log(level, message):
    """输出日志信息"""
    level_names = {
        DEBUG: "DEBUG",
        INFO: "INFO",
        WARNING: "WARNING",
        ERROR: "ERROR",
        CRITICAL: "CRITICAL"
    }
    
    if level >= LOG_LEVEL:
        # 根据级别选择输出流
        if level >= ERROR:
            stream = sys.stderr
        else:
            stream = sys.stdout
        
        # 输出日志信息
        stream.write(f"[{level_names[level]}] {message}\n")
        stream.flush()

# 使用示例
log(DEBUG, "这是调试信息")  # 不会输出，因为LOG_LEVEL=INFO
log(INFO, "这是普通信息")
log(WARNING, "这是警告信息")
log(ERROR, "这是错误信息")
log(CRITICAL, "这是严重错误信息")

# 解析命令行参数设置日志级别
if "--debug" in sys.argv:
    LOG_LEVEL = DEBUG
    log(DEBUG, "调试模式已启用")
```

## 最佳实践

1. **使用sys.argv解析命令行参数**：对于简单的命令行参数解析，可以使用sys.argv直接解析
2. **重定向输出时保存原始流**：在重定向输出后，记得恢复原始输出流
3. **添加自定义路径到sys.path**：在导入自定义模块时，可以将模块所在路径添加到sys.path
4. **使用sys.exit()退出程序**：使用sys.exit()退出程序时，可以指定退出码
5. **处理异常时使用sys.exc_info()**：在异常处理中，可以使用sys.exc_info()获取详细的异常信息
6. **考虑平台差异**：使用sys.platform检测当前平台，处理平台特定的代码
7. **使用atexit注册退出处理函数**：使用atexit模块注册程序退出时的清理函数
8. **避免修改sys模块的全局状态**：修改sys模块的全局状态可能会影响其他代码的执行

## 与其他模块的关系

- **argparse**：提供更强大的命令行参数解析功能
- **logging**：提供更完善的日志记录功能
- **os**：提供与操作系统交互的功能
- **subprocess**：提供执行系统命令的功能
- **atexit**：提供程序退出时的处理函数注册功能
- **traceback**：提供异常追踪信息的打印功能

## 总结

sys模块是Python中用于与Python解释器和系统交互的核心模块，提供了访问命令行参数、控制输入输出流、获取系统路径、管理模块搜索路径等功能。通过sys模块，可以编写更灵活、更强大的Python程序，与操作系统和Python解释器进行交互。

在实际应用中，sys模块常用于命令行参数解析、输出重定向、模块动态导入、程序退出控制等场景。对于更复杂的命令行参数解析，可以结合argparse模块使用；对于更完善的日志记录，可以结合logging模块使用。