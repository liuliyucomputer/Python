#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Python模块文件语法错误修复脚本
修复反引号、字符串未闭合等常见语法错误
"""

import os
import re

def fix_module_file(file_path):
    """修复模块文件中的语法错误"""
    print(f"\n处理文件: {file_path}")
    
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = content
        changes = {}
        
        # 1. 替换反引号为双引号或删除（如果在代码块外）
        # 对于代码块内的反引号，替换为单引号
        # 使用正则表达式查找Markdown代码块
        code_blocks = re.findall(r'```python\n(.*?)```', modified, re.DOTALL)
        for block in code_blocks:
            if '`' in block:
                new_block = block.replace('`', "'")
                modified = modified.replace(f'```python\n{block}```', f'```python\n{new_block}```')
                changes['反引号替换(代码块内)'] = changes.get('反引号替换(代码块内)', 0) + block.count('`')
        
        # 对于非代码块内的反引号，替换为双引号
        # 先标记代码块位置
        code_block_positions = []
        for match in re.finditer(r'```python\n.*?```', modified, re.DOTALL):
            code_block_positions.append((match.start(), match.end()))
        
        # 在非代码块区域替换反引号
        def is_in_code_block(pos):
            for start, end in code_block_positions:
                if start <= pos < end:
                    return True
            return False
        
        i = 0
        while i < len(modified):
            if modified[i] == '`' and not is_in_code_block(i):
                # 找到匹配的反引号
                j = i + 1
                while j < len(modified) and modified[j] != '`':
                    j += 1
                if j < len(modified):  # 找到结束反引号
                    # 替换为双引号
                    modified = modified[:i] + '"' + modified[i+1:j] + '"' + modified[j+1:]
                    changes['反引号替换(非代码块)'] = changes.get('反引号替换(非代码块)', 0) + 2
                    j += 1  # 跳过替换的字符
                    i = j
                else:
                    i += 1
            else:
                i += 1
        
        # 2. 修复可能的未闭合字符串
        # 检查每个代码块
        code_blocks = re.findall(r'```python\n(.*?)```', modified, re.DOTALL)
        for block in code_blocks:
            # 简单检查单引号和双引号的匹配情况
            single_quotes = block.count("'")
            double_quotes = block.count('"')
            
            if single_quotes % 2 != 0:
                # 修复奇数个单引号的问题
                # 找到最后一个单引号并替换或添加一个
                last_single = block.rfind("'")
                if last_single != -1:
                    new_block = block[:last_single] + "''" + block[last_single+1:]
                    modified = modified.replace(f'```python\n{block}```', f'```python\n{new_block}```')
                    changes['修复未闭合单引号'] = changes.get('修复未闭合单引号', 0) + 1
            
            if double_quotes % 2 != 0:
                # 修复奇数个双引号的问题
                last_double = block.rfind('"')
                if last_double != -1:
                    new_block = block[:last_double] + '""' + block[last_double+1:]
                    modified = modified.replace(f'```python\n{block}```', f'```python\n{new_block}```')
                    changes['修复未闭合双引号'] = changes.get('修复未闭合双引号', 0) + 1
        
        # 3. 修复可能的花括号不匹配问题
        # 主要针对functools模块中的问题
        code_blocks = re.findall(r'```python\n(.*?)```', modified, re.DOTALL)
        for block in code_blocks:
            open_braces = block.count('{')
            close_braces = block.count('}')
            
            if open_braces != close_braces:
                # 修复花括号不匹配
                diff = open_braces - close_braces
                if diff > 0:
                    # 添加缺少的右花括号
                    new_block = block + '}' * diff
                    changes['添加缺少的右花括号'] = changes.get('添加缺少的右花括号', 0) + diff
                else:
                    # 添加缺少的左花括号（这种情况较少见）
                    new_block = '{' * (-diff) + block
                    changes['添加缺少的左花括号'] = changes.get('添加缺少的左花括号', 0) + (-diff)
                
                modified = modified.replace(f'```python\n{block}```', f'```python\n{new_block}```')
        
        # 4. 清理多余的空白行
        modified = re.sub(r'\n{3,}', '\n\n', modified)
        
        # 5. 确保文件以换行符结尾
        if not modified.endswith('\n'):
            modified += '\n'
        
        # 检查是否有变化
        if modified != content:
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified)
            
            print("✅ 文件修复完成!")
            for change_type, count in changes.items():
                print(f"  - {change_type}: {count}")
            return True
        else:
            print("✅ 文件无需修复")
            return False
            
    except Exception as e:
        print(f"❌ 处理文件时出错: {e}")
        return False

def test_syntax(file_path):
    """测试文件的Python语法是否正确"""
    try:
        with open(file_path, 'rb') as f:
            # 使用compile来检查语法，但不执行
            compile(f.read(), file_path, 'exec')
        print(f"✅ {file_path} 语法正确")
        return True
    except SyntaxError as e:
        print(f"❌ {file_path} 语法错误: {e}")
        return False

def main():
    """主函数"""
    print("Python模块文件语法修复工具")
    print("=" * 50)
    
    # 定义要处理的模块文件列表
    modules = [
        "itertools模块.py",
        "operator模块.py",
        "collections模块.py",
        "heapq模块.py",
        "functools模块.py"
    ]
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 处理每个文件
    fixed_files = 0
    for module in modules:
        file_path = os.path.join(current_dir, module)
        if os.path.exists(file_path):
            # 先尝试修复
            if fix_module_file(file_path):
                fixed_files += 1
            
            # 测试修复后的语法
            print("检查语法...")
            test_syntax(file_path)
        else:
            print(f"❌ 文件不存在: {file_path}")
    
    # 输出总结
    print("\n" + "=" * 50)
    print(f"修复总结: 修复了 {fixed_files} 个文件")
    print("修复完成!")

if __name__ == "__main__":
    main()
