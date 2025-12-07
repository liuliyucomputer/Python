# 系统交互模块

本目录包含Python中用于与操作系统交互的标准库模块文档，包括进程管理、系统命令执行、文件系统操作、环境变量管理等功能。

## 目录结构

- README.md - 目录说明文档
- os模块.py - 操作系统接口模块
- sys模块.py - Python解释器接口模块
- subprocess模块.py - 子进程管理模块
- shutil模块.py - 高级文件操作模块
- tempfile模块.py - 临时文件和目录管理模块
- stat模块.py - 文件状态信息模块
- platform模块.py - 平台信息模块

## 核心模块说明

1. **os模块**
   - 提供与操作系统交互的各种功能
   - 支持文件系统操作、进程管理、环境变量等

2. **sys模块**
   - 提供与Python解释器交互的功能
   - 支持命令行参数、标准输入输出、模块导入等

3. **subprocess模块**
   - 用于创建和管理子进程
   - 支持执行系统命令、管道通信等

4. **shutil模块**
   - 提供高级文件操作功能
   - 支持文件复制、移动、删除、归档等

5. **tempfile模块**
   - 用于创建临时文件和目录
   - 支持自动清理临时文件

6. **stat模块**
   - 提供文件状态信息的常量和函数
   - 用于解释os.stat()返回的文件状态

7. **platform模块**
   - 用于获取平台信息
   - 支持获取操作系统、Python版本、硬件信息等

## 学习路径

1. 先学习os模块，掌握基本的操作系统交互功能
2. 学习sys模块，了解Python解释器的接口
3. 学习subprocess模块，掌握子进程管理和系统命令执行
4. 学习shutil模块，掌握高级文件操作
5. 学习tempfile模块，掌握临时文件和目录的创建和管理
6. 学习stat模块，了解文件状态信息
7. 学习platform模块，了解如何获取平台信息

## 示例代码使用方法

每个模块文档都包含详细的示例代码，你可以直接运行这些代码来学习模块的使用方法。例如：

```python
# 导入模块
import os

# 使用os模块的功能
print("当前工作目录:", os.getcwd())
print("当前目录下的文件:", os.listdir("."))
```

## 注意事项

1. 在使用os模块的文件操作功能时，注意处理路径分隔符的差异
2. 在使用subprocess模块执行系统命令时，注意安全问题，避免命令注入
3. 在使用shutil模块进行文件操作时，注意备份重要文件
4. 在使用tempfile模块创建临时文件时，注意资源清理
5. 不同平台的功能可能存在差异，使用platform模块进行平台检测

## 参考资源

- [Python官方文档 - os模块](https://docs.python.org/3/library/os.html)
- [Python官方文档 - sys模块](https://docs.python.org/3/library/sys.html)
- [Python官方文档 - subprocess模块](https://docs.python.org/3/library/subprocess.html)
- [Python官方文档 - shutil模块](https://docs.python.org/3/library/shutil.html)
- [Python官方文档 - tempfile模块](https://docs.python.org/3/library/tempfile.html)
- [Python官方文档 - stat模块](https://docs.python.org/3/library/stat.html)
- [Python官方文档 - platform模块](https://docs.python.org/3/library/platform.html)