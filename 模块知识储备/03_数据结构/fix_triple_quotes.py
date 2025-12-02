#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复Python模块文件中的三引号字符串问题
"""

import os
import re

def fix_triple_quotes(file_path):
    """修复文件中的三引号字符串问题"""
    print(f"处理文件: {file_path}")
    
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = content
        changes = 0
        
        # 找到所有的Python代码块
        code_blocks = re.findall(r'```python\n(.*?)```', modified, re.DOTALL)
        
        for i, block in enumerate(code_blocks):
            # 检查三引号字符串
            triple_single = re.findall(r"'''(.*?)'''", block, re.DOTALL)
            triple_double = re.findall(r'"""(.*?)"""', block, re.DOTALL)
            
            # 简单检查三引号的数量
            single_count = block.count("'''")
            double_count = block.count('"""')
            
            # 修复奇数个三引号的情况
            if single_count % 2 != 0:
                # 添加一个三引号来闭合
                block = block + "'''"
                changes += 1
                print(f"  修复代码块 #{i+1}: 添加闭合的单三引号")
            
            if double_count % 2 != 0:
                # 添加一个三引号来闭合
                block = block + '"""'
                changes += 1
                print(f"  修复代码块 #{i+1}: 添加闭合的双三引号")
            
            # 替换修复后的代码块
            modified = modified.replace(f'```python\n{code_blocks[i]}```', f'```python\n{block}```')
        
        # 移除或替换特殊字符
        special_chars = {'∞': 'float("inf")', '≤': '<=', '≥': '>='}
        for special, replacement in special_chars.items():
            if special in modified:
                count = modified.count(special)
                modified = modified.replace(special, replacement)
                changes += count
                print(f"  替换特殊字符 '{special}' -> '{replacement}': {count} 处")
        
        # 清理文件结构
        # 确保每个代码块都有正确的格式
        modified = re.sub(r'```python\s*```', '```python\n```', modified)
        
        # 检查是否有变化
        if changes > 0:
            # 写回文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified)
            print(f"✅ 文件修复完成，进行了 {changes} 处修改")
        else:
            print(f"✅ 文件无需修复")
        
        return changes
        
    except Exception as e:
        print(f"❌ 处理文件时出错: {e}")
        return -1

def main():
    """主函数"""
    print("Python模块文件三引号修复工具")
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
    total_changes = 0
    for module in modules:
        file_path = os.path.join(current_dir, module)
        if os.path.exists(file_path):
            changes = fix_triple_quotes(file_path)
            if changes >= 0:
                total_changes += changes
        else:
            print(f"❌ 文件不存在: {file_path}")
    
    # 输出总结
    print("\n" + "=" * 50)
    print(f"修复总结: 总共进行了 {total_changes} 处修改")
    print("修复完成!")

if __name__ == "__main__":
    main()
