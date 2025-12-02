"""
# pathlib模块详解：面向对象的路径操作

pathlib模块是Python 3.4引入的标准库，提供了一种面向对象的方式来处理文件路径。相比传统的os.path模块，pathlib提供了更直观、更易读的API，使得文件路径操作更加简洁和面向对象。pathlib模块主要提供了`Path`类及其子类，用于表示和操作文件系统路径。

## 1. 核心功能概览

pathlib模块的主要功能可以分为以下几类：

1. **路径表示**：使用面向对象的方式表示文件和目录路径
2. **路径操作**：路径连接、分割、规范化等基本操作
3. **文件操作**：文件读写、创建、删除等操作
4. **目录操作**：目录遍历、创建、删除等操作
5. **路径属性获取**：获取路径的各种属性（扩展名、文件名等）
6. **路径判断**：检查路径是否存在、是否为文件或目录等

## 2. 基本使用

### 2.1 Path对象创建

```python
from pathlib import Path

def path_creation_demo():
    # 创建当前目录的Path对象
    current_dir = Path('.')
    print(f"当前目录: {current_dir}")
    
    # 创建绝对路径的Path对象
    absolute_path = Path(__file__).resolve()
    print(f"当前文件绝对路径: {absolute_path}")
    
    # 通过字符串创建Path对象
    string_path = Path("folder/subfolder/file.txt")
    print(f"字符串路径: {string_path}")
    
    # 使用Path.joinpath方法连接路径
    joined_path = Path("folder").joinpath("subfolder", "file.txt")
    print(f"连接的路径: {joined_path}")
    
    # 使用除法运算符连接路径（更简洁）
    div_path = Path("folder") / "subfolder" / "file.txt"
    print(f"使用除法运算符连接的路径: {div_path}")
    
    # 父目录访问
    parent_dir = absolute_path.parent
    print(f"父目录: {parent_dir}")
    
    # 祖先目录访问
    grandparent_dir = absolute_path.parent.parent
    print(f"祖父目录: {grandparent_dir}")

# 运行示例
path_creation_demo()
```

### 2.2 路径属性和方法

```python
from pathlib import Path

def path_properties_demo():
    # 创建示例Path对象
    sample_path = Path("folder/subfolder/file.txt")
    
    # 路径的基本属性
    print(f"路径: {sample_path}")
    print(f"名称(带扩展名): {sample_path.name}")  # 文件名和扩展名
    print(f"文件名(不含扩展名): {sample_path.stem}")  # 文件名
    print(f"扩展名: {sample_path.suffix}")  # 文件扩展名
    print(f"父目录: {sample_path.parent}")  # 父目录
    print(f"根目录: {sample_path.root}")  # 根目录
    print(f"驱动(Windows): {sample_path.drive}")  # 驱动器(Windows系统)
    
    # 获取多个扩展名（对于文件名如file.tar.gz）
    multi_ext_path = Path("archive.tar.gz")
    print(f"\n多扩展名文件: {multi_ext_path}")
    print(f"主扩展名: {multi_ext_path.suffix}")  # .gz
    print(f"所有扩展名: {multi_ext_path.suffixes}")  # ['.tar', '.gz']
    print(f"主干名(不含所有扩展名): {multi_ext_path.stem}")  # archive
    
    # 构建新路径
    new_path = sample_path.with_name("new_file.txt")
    print(f"\n替换名称: {new_path}")
    
    new_suffix = sample_path.with_suffix(".md")
    print(f"替换扩展名: {new_suffix}")
    
    # 路径的布尔值
    empty_path = Path()
    print(f"\n空路径布尔值: {bool(empty_path)}")  # False
    print(f"非空路径布尔值: {bool(sample_path)}")  # True

# 运行示例
path_properties_demo()
```

## 3. 路径判断

```python
from pathlib import Path
import os

def path_checks_demo():
    # 创建测试文件和目录
    test_dir = Path("test_dir")
    test_file = test_dir / "test_file.txt"
    
    # 创建目录和文件
    test_dir.mkdir(exist_ok=True)
    test_file.write_text("测试内容")
    
    print(f"创建测试目录: {test_dir}")
    print(f"创建测试文件: {test_file}")
    
    # 路径存在性检查
    print(f"\n路径存在检查:")
    print(f"目录 '{test_dir}' 存在: {test_dir.exists()}")
    print(f"文件 '{test_file}' 存在: {test_file.exists()}")
    print(f"不存在的路径 '{test_dir/'non_exist'}' 存在: {(test_dir/'non_exist').exists()}")
    
    # 文件类型检查
    print(f"\n文件类型检查:")
    print(f"'{test_dir}' 是目录: {test_dir.is_dir()}")
    print(f"'{test_file}' 是目录: {test_file.is_dir()}")
    print(f"'{test_dir}' 是文件: {test_dir.is_file()}")
    print(f"'{test_file}' 是文件: {test_file.is_file()}")
    
    # 其他类型检查
    print(f"\n其他类型检查:")
    print(f"'{test_file}' 是块设备: {test_file.is_block_device()}")
    print(f"'{test_file}' 是字符设备: {test_file.is_char_device()}")
    print(f"'{test_file}' 是符号链接: {test_file.is_symlink()}")
    print(f"'{test_file}' 是套接字: {test_file.is_socket()}")
    print(f"'{test_file}' 是FIFO: {test_file.is_fifo()}")
    
    # 清理测试文件和目录
    test_file.unlink()
    test_dir.rmdir()
    print(f"\n清理完成")

# 运行示例
path_checks_demo()
```

## 4. 文件操作

### 4.1 文件读写

```python
from pathlib import Path

def file_read_write_demo():
    # 创建测试文件
    test_file = Path("read_write_test.txt")
    
    # 写入文本
    content = "这是一个测试文件内容\n第二行内容"
    test_file.write_text(content, encoding="utf-8")
    print(f"写入文件: {test_file}")
    print(f"写入内容: {repr(content)}")
    
    # 读取文本
    read_content = test_file.read_text(encoding="utf-8")
    print(f"\n读取内容: {repr(read_content)}")
    
    # 二进制写入
    binary_content = b"这是二进制内容\x00\x01\x02"
    test_file.write_bytes(binary_content)
    print(f"\n写入二进制内容: {binary_content}")
    
    # 二进制读取
    read_binary = test_file.read_bytes()
    print(f"读取二进制内容: {read_binary}")
    
    # 使用open方法（与内置open函数相同）
    with test_file.open('w', encoding='utf-8') as f:
        f.write("使用open方法写入")
    
    with test_file.open('r', encoding='utf-8') as f:
        open_content = f.read()
    print(f"\n使用open方法读取: {open_content}")
    
    # 清理文件
    test_file.unlink()
    print("清理完成")

# 运行示例
file_read_write_demo()
```

### 4.2 文件创建和删除

```python
from pathlib import Path

def file_creation_deletion_demo():
    # 创建单级目录
    dir_path = Path("new_dir")
    dir_path.mkdir(exist_ok=False)  # 如果目录已存在则抛出异常
    print(f"创建目录: {dir_path}")
    
    # 递归创建多级目录
    nested_dir = Path("parent/child/grandchild")
    nested_dir.mkdir(parents=True, exist_ok=True)
    print(f"递归创建目录: {nested_dir}")
    
    # 创建文件
    file_path = dir_path / "test_file.txt"
    file_path.touch()  # 创建空文件
    print(f"创建空文件: {file_path}")
    
    # 写入内容到文件
    file_path.write_text("文件内容")
    print(f"写入内容到文件")
    
    # 删除文件
    file_path.unlink(missing_ok=True)  # 如果文件不存在也不抛出异常
    print(f"删除文件: {file_path}")
    print(f"文件是否存在: {file_path.exists()}")
    
    # 删除空目录
    dir_path.rmdir()
    print(f"删除空目录: {dir_path}")
    
    # 递归删除非空目录（需要使用shutil模块）
    import shutil
    shutil.rmtree("parent")
    print(f"递归删除目录: parent")
    
    print("清理完成")

# 运行示例
file_creation_deletion_demo()
```

## 5. 目录操作

### 5.1 目录遍历

```python
from pathlib import Path
import os

def directory_traversal_demo():
    # 创建测试目录结构
    root_dir = Path("traversal_test")
    
    # 创建嵌套目录结构
    (root_dir / "subdir1").mkdir(parents=True, exist_ok=True)
    (root_dir / "subdir2").mkdir(parents=True, exist_ok=True)
    (root_dir / "subdir1" / "subsubdir").mkdir(parents=True, exist_ok=True)
    
    # 创建测试文件
    (root_dir / "file1.txt").write_text("根目录文件1")
    (root_dir / "file2.txt").write_text("根目录文件2")
    (root_dir / "subdir1" / "file3.txt").write_text("子目录1文件")
    (root_dir / "subdir2" / "file4.txt").write_text("子目录2文件")
    (root_dir / "subdir1" / "subsubdir" / "file5.txt").write_text("子子目录文件")
    
    print(f"创建测试目录结构: {root_dir}")
    
    # 列出目录内容（仅一级）
    print("\n列出目录内容（仅一级）:")
    for item in root_dir.iterdir():
        print(f"  {item.name} - {'目录' if item.is_dir() else '文件'}")
    
    # 递归遍历所有文件和目录
    print("\n递归遍历所有文件和目录:")
    for path in root_dir.glob("**/*"):
        print(f"  {path.relative_to(root_dir)} - {'目录' if path.is_dir() else '文件'}")
    
    # 仅遍历文件
    print("\n仅遍历文件:")
    for path in root_dir.glob("**/*.txt"):
        print(f"  {path.relative_to(root_dir)}")
    
    # 仅遍历特定子目录
    print("\n仅遍历subdir1及其子目录:")
    for path in (root_dir / "subdir1").glob("**/*"):
        print(f"  {path.relative_to(root_dir / 'subdir1')}")
    
    # 使用rglob（等同于glob("**/*")）
    print("\n使用rglob遍历所有.txt文件:")
    for path in root_dir.rglob("*.txt"):
        print(f"  {path.relative_to(root_dir)}")
    
    # 清理测试目录
    import shutil
    shutil.rmtree(root_dir)
    print("\n清理完成")

# 运行示例
directory_traversal_demo()
```

### 5.2 路径匹配

```python
from pathlib import Path
import os

def path_matching_demo():
    # 创建测试文件结构
    test_dir = Path("matching_test")
    test_dir.mkdir(exist_ok=True)
    
    # 创建测试文件
    files = [
        "file1.txt", "file2.txt", "doc1.doc", "image.png", 
        "data.csv", "file10.txt", "config.json"
    ]
    
    for file in files:
        (test_dir / file).touch()
    
    print(f"创建测试文件结构: {test_dir}")
    
    # 使用glob匹配
    print("\n匹配所有.txt文件:")
    for path in test_dir.glob("*.txt"):
        print(f"  {path.name}")
    
    # 匹配以file开头的文件
    print("\n匹配以file开头的文件:")
    for path in test_dir.glob("file*"):
        print(f"  {path.name}")
    
    # 匹配file后接一个字符的文件
    print("\n匹配file后接一个字符的文件:")
    for path in test_dir.glob("file?.txt"):
        print(f"  {path.name}")
    
    # 匹配特定扩展名
    print("\n匹配.txt或.json文件:")
    for path in test_dir.glob("*.t[xy]t"):
        print(f"  {path.name}")
    
    for path in test_dir.glob("*.json"):
        print(f"  {path.name}")
    
    # 使用更复杂的匹配模式
    print("\n匹配文件名为5个字符加.txt的文件:")
    for path in test_dir.glob("?????.txt"):
        print(f"  {path.name}")
    
    # 清理测试目录
    import shutil
    shutil.rmtree(test_dir)
    print("\n清理完成")

# 运行示例
path_matching_demo()
```

## 6. 高级应用示例

### 6.1 文件和目录监视器

```python
from pathlib import Path
import time
import os

def simple_file_monitor(directory, interval=2):
    """简单的文件监视器"""
    print(f"开始监视目录: {directory}")
    print(f"按 Ctrl+C 停止监视")
    
    # 存储文件状态
    file_states = {}
    
    def get_file_state(path):
        """获取文件状态"""
        stat_info = path.stat()
        return (
            stat_info.st_size,  # 文件大小
            stat_info.st_mtime  # 修改时间
        )
    
    # 初始扫描
    for path in Path(directory).glob("**/*"):
        if path.is_file():
            file_states[path] = get_file_state(path)
    
    try:
        while True:
            # 等待一段时间
            time.sleep(interval)
            
            # 新的状态字典
            new_states = {}
            
            # 扫描当前目录
            for path in Path(directory).glob("**/*"):
                if path.is_file():
                    new_states[path] = get_file_state(path)
            
            # 检查新增文件
            for path in new_states:
                if path not in file_states:
                    print(f"[新增] {path}")
            
            # 检查删除的文件
            for path in file_states:
                if path not in new_states:
                    print(f"[删除] {path}")
            
            # 检查修改的文件
            for path in new_states:
                if path in file_states and new_states[path] != file_states[path]:
                    print(f"[修改] {path}")
            
            # 更新状态
            file_states = new_states
    
    except KeyboardInterrupt:
        print("\n停止监视")

# 测试文件监视器
def test_file_monitor():
    # 创建测试目录
    monitor_dir = Path("monitor_test")
    monitor_dir.mkdir(exist_ok=True)
    
    print("文件监视器演示（模拟）")
    print(f"创建测试目录: {monitor_dir}")
    
    # 模拟文件变化
    test_file = monitor_dir / "test.txt"
    
    # 创建文件
    test_file.write_text("初始内容")
    print(f"1. 创建文件: {test_file}")
    
    # 修改文件
    time.sleep(1)
    test_file.write_text("修改后的内容")
    print(f"2. 修改文件: {test_file}")
    
    # 创建新文件
    time.sleep(1)
    new_file = monitor_dir / "new.txt"
    new_file.write_text("新文件内容")
    print(f"3. 创建新文件: {new_file}")
    
    # 删除文件
    time.sleep(1)
    test_file.unlink()
    print(f"4. 删除文件: {test_file}")
    
    # 注意：在实际使用时，可以取消下面的注释来运行真实的监视器
    # simple_file_monitor(monitor_dir)
    
    # 清理
    new_file.unlink()
    monitor_dir.rmdir()
    print("清理完成")

# 运行测试
test_file_monitor()
```

### 6.2 文件批处理工具

```python
from pathlib import Path
import os
import shutil

def batch_process_files(source_dir, pattern="*.*", action="copy", target_dir=None):
    """
    批量处理文件
    
    参数:
        source_dir: 源目录
        pattern: 文件匹配模式，默认为所有文件
        action: 操作类型，可选值：copy, move, delete
        target_dir: 目标目录（copy和move操作需要）
    """
    source_path = Path(source_dir)
    
    # 验证源目录
    if not source_path.is_dir():
        print(f"错误: 源目录 '{source_dir}' 不存在或不是目录")
        return 0
    
    # 验证操作和目标目录
    if action in ["copy", "move"]:
        if not target_dir:
            print("错误: copy和move操作需要指定目标目录")
            return 0
        
        target_path = Path(target_dir)
        # 创建目标目录（如果不存在）
        target_path.mkdir(parents=True, exist_ok=True)
    
    # 获取匹配的文件
    files = list(source_path.glob(pattern))
    files_processed = 0
    
    print(f"找到 {len(files)} 个匹配 '{pattern}' 的文件")
    
    for file_path in files:
        if file_path.is_file():
            try:
                if action == "copy":
                    # 复制文件
                    target_file = target_path / file_path.name
                    shutil.copy2(file_path, target_file)
                    print(f"复制: {file_path.name} -> {target_file}")
                
                elif action == "move":
                    # 移动文件
                    target_file = target_path / file_path.name
                    shutil.move(file_path, target_file)
                    print(f"移动: {file_path.name} -> {target_file}")
                
                elif action == "delete":
                    # 删除文件
                    file_path.unlink()
                    print(f"删除: {file_path.name}")
                
                else:
                    print(f"错误: 未知操作 '{action}'")
                    return files_processed
                
                files_processed += 1
                
            except Exception as e:
                print(f"处理文件 '{file_path.name}' 时出错: {e}")
    
    print(f"\n操作完成，共处理 {files_processed} 个文件")
    return files_processed

# 测试批量处理功能
def test_batch_process():
    # 创建测试目录结构
    source_dir = Path("batch_source")
    source_dir.mkdir(exist_ok=True)
    
    # 创建测试文件
    file_types = [".txt", ".md", ".py"]
    
    for i in range(10):
        ext = file_types[i % len(file_types)]
        file_path = source_dir / f"test_file_{i}{ext}"
        file_path.write_text(f"This is test file {i}")
    
    print(f"创建测试目录: {source_dir}")
    print(f"创建了 {len(list(source_dir.glob('*')))} 个测试文件")
    
    # 创建目标目录
    target_dir = Path("batch_target")
    
    print("\n=== 测试批量复制 .txt 文件 ===")
    batch_process_files(source_dir, "*.txt", "copy", target_dir)
    
    print("\n=== 测试批量移动 .md 文件 ===")
    batch_process_files(source_dir, "*.md", "move", target_dir)
    
    print("\n=== 测试批量删除 .py 文件 ===")
    batch_process_files(source_dir, "*.py", "delete")
    
    # 显示结果
    print("\n源目录剩余文件:")
    for file in source_dir.glob("*"):
        print(f"  {file.name}")
    
    print("\n目标目录文件:")
    for file in target_dir.glob("*"):
        print(f"  {file.name}")
    
    # 清理
    shutil.rmtree(source_dir)
    shutil.rmtree(target_dir)
    print("\n清理完成")

# 运行测试
test_batch_process()
```

### 6.3 文件统计和分析

```python
from pathlib import Path
import os
from collections import Counter

def analyze_directory(directory):
    """分析目录中的文件统计信息"""
    dir_path = Path(directory)
    
    if not dir_path.is_dir():
        print(f"错误: '{directory}' 不是有效的目录")
        return
    
    # 统计信息
    stats = {
        "total_files": 0,
        "total_size": 0,
        "file_types": Counter(),
        "largest_files": [],
        "newest_files": [],
        "oldest_files": []
    }
    
    # 遍历目录
    for path in dir_path.glob("**/*"):
        if path.is_file():
            try:
                # 获取文件统计信息
                stat_info = path.stat()
                file_size = stat_info.st_size
                file_mtime = stat_info.st_mtime
                file_ext = path.suffix.lower() if path.suffix else "(无扩展名)"
                
                # 更新统计
                stats["total_files"] += 1
                stats["total_size"] += file_size
                stats["file_types"][file_ext] += 1
                
                # 更新最大文件列表
                stats["largest_files"].append((file_size, path))
                stats["largest_files"] = sorted(
                    stats["largest_files"], 
                    key=lambda x: x[0], 
                    reverse=True
                )[:10]  # 只保留前10个
                
                # 更新最新文件列表
                stats["newest_files"].append((file_mtime, path))
                stats["newest_files"] = sorted(
                    stats["newest_files"], 
                    key=lambda x: x[0], 
                    reverse=True
                )[:10]
                
                # 更新最旧文件列表
                stats["oldest_files"].append((file_mtime, path))
                stats["oldest_files"] = sorted(
                    stats["oldest_files"], 
                    key=lambda x: x[0]
                )[:10]
                
            except (OSError, PermissionError) as e:
                print(f"无法访问文件 '{path}': {e}")
    
    # 打印统计结果
    print(f"\n目录分析结果: {directory}")
    print(f"总文件数: {stats['total_files']}")
    print(f"总大小: {stats['total_size'] / (1024 * 1024):.2f} MB")
    
    print(f"\n文件类型统计:")
    for ext, count in stats["file_types"].most_common(10):
        print(f"  {ext}: {count} 个文件")
    
    print(f"\n最大的10个文件:")
    for size, path in stats["largest_files"]:
        print(f"  {path.relative_to(dir_path)}: {size / 1024:.2f} KB")
    
    print(f"\n最新的10个文件:")
    import time
    for mtime, path in stats["newest_files"]:
        print(f"  {path.relative_to(dir_path)}: {time.ctime(mtime)}")

# 测试目录分析功能
def test_directory_analysis():
    # 使用当前目录进行分析
    # 在实际应用中，可以替换为需要分析的目录路径
    analyze_directory('.')

# 运行测试
test_directory_analysis()
```

## 7. pathlib与os.path对比

### 7.1 功能对比

| 功能 | os.path | pathlib |
|------|---------|----------|
| 路径连接 | `os.path.join("folder", "file.txt")` | `Path("folder") / "file.txt"` |
| 检查路径存在 | `os.path.exists("path")` | `Path("path").exists()` |
| 检查是否为文件 | `os.path.isfile("path")` | `Path("path").is_file()` |
| 检查是否为目录 | `os.path.isdir("path")` | `Path("path").is_dir()` |
| 获取绝对路径 | `os.path.abspath("path")` | `Path("path").absolute()` 或 `Path("path").resolve()` |
| 获取文件名 | `os.path.basename("path")` | `Path("path").name` |
| 获取目录名 | `os.path.dirname("path")` | `Path("path").parent` |
| 分割扩展名 | `os.path.splitext("path")` | `Path("path").stem`, `Path("path").suffix` |
| 路径规范化 | `os.path.normpath("path")` | `Path("path").resolve()` |

### 7.2 代码示例对比

```python
# os.path 方式
import os

# 创建路径
path = os.path.join("folder", "subfolder", "file.txt")

# 检查路径
if os.path.exists(path) and os.path.isfile(path):
    # 获取路径信息
    dir_name = os.path.dirname(path)
    file_name = os.path.basename(path)
    name, ext = os.path.splitext(file_name)
    
    # 读取文件
    with open(path, 'r') as f:
        content = f.read()
    
    print(f"目录: {dir_name}")
    print(f"文件名: {name}")
    print(f"扩展名: {ext}")

# pathlib 方式
from pathlib import Path

# 创建路径
path = Path("folder") / "subfolder" / "file.txt"

# 检查路径
if path.exists() and path.is_file():
    # 获取路径信息
    dir_name = path.parent
    file_name = path.name
    name = path.stem
    ext = path.suffix
    
    # 读取文件
    content = path.read_text()
    
    print(f"目录: {dir_name}")
    print(f"文件名: {name}")
    print(f"扩展名: {ext}")
```

## 8. 注意事项和最佳实践

1. **版本兼容性**：
   - pathlib模块在Python 3.4及以上版本可用
   - 对于Python 2.7，可以使用第三方库pathlib2
   - 在需要向后兼容的项目中，可能需要使用os.path模块

2. **性能考虑**：
   - 对于简单的路径操作，os.path模块可能略快
   - 对于复杂的路径处理，pathlib提供的面向对象接口更有优势
   - 大量文件操作时，pathlib的方法调用开销可能略高

3. **错误处理**：
   - pathlib操作会抛出与os模块相同类型的异常
   - 始终使用try-except捕获可能的异常
   - 注意权限错误和路径不存在的情况

4. **跨平台兼容性**：
   - pathlib自动处理不同操作系统的路径分隔符差异
   - 在Windows上，注意大小写不敏感的文件系统
   - 使用Path对象的方法而不是字符串操作，以确保跨平台兼容性

5. **代码可读性**：
   - pathlib的面向对象API通常使代码更易读
   - 使用除法运算符`/`连接路径比os.path.join更直观
   - 路径属性（如name、stem、suffix）使代码更清晰

6. **高级功能**：
   - 对于高级文件操作（如复制、移动目录），仍需结合shutil模块
   - pathlib专注于路径表示和基本操作，不包含所有文件操作功能
   - 对于文件监控等功能，考虑使用专门的库如watchdog

## 9. 总结

pathlib模块提供了一种现代、面向对象的方式来处理文件路径，使得路径操作更加直观和简洁。与传统的os.path模块相比，pathlib提供了更优雅的API，更好的可读性，以及更丰富的路径处理功能。

主要优势包括：
- 面向对象的API，使路径操作更加直观
- 简洁的语法，特别是使用`/`运算符连接路径
- 丰富的路径属性和方法，简化常见操作
- 更好的代码可读性和可维护性
- 跨平台兼容性，自动处理不同操作系统的路径差异

在Python 3.4及以上版本中，pathlib已经成为处理文件路径的推荐方式。对于新项目，建议优先使用pathlib模块，特别是在需要进行复杂的路径操作时。对于现有项目，可以根据需要逐步迁移到pathlib，以提高代码质量和可维护性。