# fileinput模块详解

fileinput模块提供了处理多个文件输入的功能，是Python中文件处理的重要模块之一。

## 模块概述

fileinput模块包含了一系列用于处理多个文件输入的函数，这些函数可以：
- 逐行读取多个文件
- 在读取文件时修改文件内容
- 获取当前读取的文件信息（文件名、行号等）
- 支持标准输入和文件混合输入

## 基本用法

### 导入模块

```python
import fileinput
```

### 逐行读取文件

#### 基本读取

使用fileinput.input()函数可以逐行读取多个文件。

```python
# 逐行读取单个文件
for line in fileinput.input('g:/Python/模块知识储备/05_文件处理/README.md'):
    print(line.strip())
    # 只读取前10行
    if fileinput.lineno() >= 10:
        break

# 逐行读取多个文件
for line in fileinput.input([
    'g:/Python/模块知识储备/05_文件处理/README.md',
    'g:/Python/模块知识储备/05_文件处理/os.path模块.py'
]):
    print(line.strip())
    # 只读取前5行
    if fileinput.lineno() >= 5:
        break
```

#### 获取当前读取信息

fileinput模块提供了一些函数来获取当前读取的文件信息。

```python
for line in fileinput.input('g:/Python/模块知识储备/05_文件处理/README.md'):
    # 获取当前行号（所有文件的累计行号）
    print(f"行号: {fileinput.lineno()}")
    # 获取当前文件中的行号
    print(f"当前文件行号: {fileinput.filelineno()}")
    # 获取当前文件名
    print(f"文件名: {fileinput.filename()}")
    # 检查是否是文件的第一行
    print(f"是否是文件第一行: {fileinput.isfirstline()}")
    # 检查是否是标准输入
    print(f"是否是标准输入: {fileinput.isstdin()}")
    
    print(f"行内容: {line.strip()}")
    print("-" * 50)
    
    # 只读取前3行
    if fileinput.lineno() >= 3:
        break
```

### 修改文件内容

使用fileinput.input()函数的inplace参数可以在读取文件时修改文件内容。

```python
# 在文件中替换文本（注意：此示例仅用于演示，实际运行会修改文件）
# for line in fileinput.input('g:/Python/模块知识储备/05_文件处理/test.txt', inplace=True):
#     # 将所有"Python"替换为"Python 3"
#     new_line = line.replace('Python', 'Python 3')
#     # 打印新内容（会写入文件）
#     print(new_line, end='')
# 
# print("文件内容已修改")
```

### 标准输入支持

fileinput模块支持从标准输入读取内容。

```python
# 从标准输入读取内容（注意：此示例在交互式环境中运行效果更好）
# print("请输入内容，按Ctrl+D结束:")
# for line in fileinput.input():
#     print(f"您输入的内容: {line.strip()}")
```

## 高级功能

### 钩子函数

fileinput模块支持使用钩子函数来处理文件打开和关闭事件。

```python
# 使用钩子函数处理文件编码
def open_with_encoding(encoding):
    def opener(filename, mode):
        return open(filename, mode, encoding=encoding)
    return opener

# 使用指定编码读取文件
for line in fileinput.input(
    'g:/Python/模块知识储备/05_文件处理/README.md',
    openhook=open_with_encoding('utf-8')
):
    print(f"行内容: {line.strip()}")
    # 只读取前5行
    if fileinput.lineno() >= 5:
        break
```

### 文件过滤

使用fileinput模块可以方便地过滤文件内容。

```python
# 过滤包含特定关键字的行
def filter_lines(file_list, keyword):
    filtered_lines = []
    for line in fileinput.input(file_list):
        if keyword in line:
            filtered_lines.append((fileinput.filename(), fileinput.filelineno(), line.strip()))
    return filtered_lines

# 使用示例
files = ['g:/Python/模块知识储备/05_文件处理/README.md']
keyword = '文件处理'
filtered = filter_lines(files, keyword)

print(f"包含关键字 '{keyword}' 的行:")
for filename, line_num, content in filtered:
    print(f"{filename}: {line_num}: {content}")
```

## 实际应用示例

### 示例1：批量替换文件内容

```python
def batch_replace(file_list, old_str, new_str, encoding='utf-8'):
    """批量替换多个文件中的文本"""
    replaced_count = 0
    
    for filename in file_list:
        file_changed = False
        
        # 读取文件内容
        with open(filename, 'r', encoding=encoding) as f:
            lines = f.readlines()
        
        # 替换内容
        new_lines = []
        for line in lines:
            if old_str in line:
                new_line = line.replace(old_str, new_str)
                new_lines.append(new_line)
                file_changed = True
            else:
                new_lines.append(line)
        
        # 写回文件
        if file_changed:
            with open(filename, 'w', encoding=encoding) as f:
                f.writelines(new_lines)
            replaced_count += 1
            print(f"已修改文件: {filename}")
    
    return replaced_count

# 使用示例（注意：此示例仅用于演示，实际运行会修改文件）
# files_to_replace = [
#     'g:/Python/模块知识储备/05_文件处理/test1.txt',
#     'g:/Python/模块知识储备/05_文件处理/test2.txt'
# ]
# old_text = 'Python 2'
# new_text = 'Python 3'
# 
# replaced = batch_replace(files_to_replace, old_text, new_text)
# print(f"共修改了 {replaced} 个文件")
```

### 示例2：统计文件中的单词出现次数

```python
def count_word_occurrences(file_list, word):
    """统计多个文件中单词出现的次数"""
    occurrences = {}
    
    for line in fileinput.input(file_list):
        filename = fileinput.filename()
        if filename not in occurrences:
            occurrences[filename] = 0
        
        # 统计单词出现次数（简单实现，不考虑标点符号）
        words = line.lower().split()
        occurrences[filename] += words.count(word.lower())
    
    return occurrences

# 使用示例
files_to_count = [
    'g:/Python/模块知识储备/05_文件处理/README.md',
    'g:/Python/模块知识储备/05_文件处理/os.path模块.py'
]
word_to_count = '文件'

word_counts = count_word_occurrences(files_to_count, word_to_count)

print(f"单词 '{word_to_count}' 在各文件中的出现次数:")
for filename, count in word_counts.items():
    print(f"{filename}: {count} 次")
```

### 示例3：查找包含特定模式的行

```python
def find_pattern_in_files(file_list, pattern):
    """查找多个文件中包含特定模式的行"""
    import re
    
    matches = []
    regex = re.compile(pattern)
    
    for line in fileinput.input(file_list):
        if regex.search(line):
            matches.append({
                'filename': fileinput.filename(),
                'line_num': fileinput.filelineno(),
                'content': line.strip()
            })
    
    return matches

# 使用示例
files_to_search = [
    'g:/Python/模块知识储备/05_文件处理/README.md',
    'g:/Python/模块知识储备/05_文件处理/os.path模块.py'
]
pattern = r'模块'

found_matches = find_pattern_in_files(files_to_search, pattern)

print(f"包含模式 '{pattern}' 的行:")
for match in found_matches[:10]:  # 只显示前10个匹配
    print(f"{match['filename']}: {match['line_num']}: {match['content']}")
```

### 示例4：合并多个文件

```python
def merge_files(file_list, output_file):
    """合并多个文件为一个文件"""
    with open(output_file, 'w', encoding='utf-8') as out_f:
        for line in fileinput.input(file_list):
            out_f.write(line)
            
            # 在文件之间添加分隔线
            if fileinput.isfirstline() and fileinput.lineno() > 1:
                out_f.write('\n' + '='*50 + '\n\n')
    
    print(f"已合并 {len(file_list)} 个文件到 {output_file}")

# 使用示例
files_to_merge = [
    'g:/Python/模块知识储备/05_文件处理/README.md',
    'g:/Python/模块知识储备/05_文件处理/os.path模块.py'
]
output_file = 'g:/Python/模块知识储备/05_文件处理/merged_files.txt'

merge_files(files_to_merge, output_file)
print(f"合并后的文件内容:")
with open(output_file, 'r', encoding='utf-8') as f:
    print(f.read()[:1000] + '...')  # 只显示前1000个字符
```

## 最佳实践

1. **使用with语句**：虽然fileinput模块会自动关闭文件，但使用with语句可以更明确地控制文件的打开和关闭。
2. **限制读取行数**：在处理大文件时，使用break语句限制读取行数可以提高效率。
3. **处理编码问题**：使用openhook参数处理不同编码的文件。
4. **备份原文件**：在修改文件内容前，最好备份原文件，避免数据丢失。
5. **使用正则表达式**：对于复杂的模式匹配，使用正则表达式可以提高匹配的准确性。

## 与其他模块的关系

- **os模块**：fileinput模块与os模块配合使用，可以更方便地遍历文件和目录。
- **re模块**：fileinput模块与re模块配合使用，可以更方便地进行模式匹配和文本替换。
- **sys模块**：fileinput模块与sys模块配合使用，可以处理命令行参数和标准输入。

## 总结

fileinput模块是Python中处理多个文件输入的核心模块，提供了丰富的功能用于逐行读取、修改和过滤多个文件的内容。熟练掌握fileinput模块的使用，可以使多文件处理任务更加高效和方便。

通过结合fileinput模块与其他文件处理模块（如os、re、sys等），可以完成各种复杂的多文件处理任务，如批量替换、单词统计、模式查找和文件合并等。